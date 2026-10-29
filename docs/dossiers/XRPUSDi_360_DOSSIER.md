# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 00:20:14 IST` (`2026-10-29 18:50:14 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `1.28` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.29` | Lower -3.00σ Band: `1.27`
  * Upper +2.51σ Band: `1.29` | Lower -2.51σ Band: `1.27`
  * Upper +2.01σ Band: `1.29` | Lower -2.01σ Band: `1.28`
  * Upper +2.00σ Band: `1.29` | Lower -2.00σ Band: `1.28`
  * Upper +1.28σ Band: `1.29` | Lower -1.28σ Band: `1.28`
  * Upper +1.00σ Band: `1.28` | Lower -1.00σ Band: `1.28`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.28` | EMA-20=`1.28` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.28` (Slope: `+0.0000`) | EMA-100=`1.28`
  * Institutional Anchors: EMA-144=`1.28` | EMA-200=`1.28` (Slope: `+0.0000`) | EMA-233=`1.28`
- **Range Boundaries**: 24H High=`1.29` | 24H Low=`1.27` | Weekly High=`1.31` | Weekly Low=`1.26`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.30` (Distance: `-1.28%`)
  * Point of Control (POC) = `1.29` (Distance: `-0.53%`)
  * Value Area Low (VAL) = `1.28` (Distance: `-0.16%`)
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
| `5m` | `1.29` | `1.29` | `1.29` | `1.29` | `1,203,513` | 1,550,537.31 USD | -316,148.15 USD | `-20.39%` | -26,764,171.49 USD | `-0.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.29` | `1.29` | `1.28` | `1.28` | `16,533,574` | 21,201,783.24 USD | -9,782,682.17 USD | `-46.14%` | -36,546,853.67 USD | `-4.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.28` | `1.28` | `1.28` | `1.28` | `400,728` | 513,598.97 USD | -174,847.97 USD | `-34.04%` | -36,721,701.64 USD | `+0.18` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.29` | `1.29` | `1.29` | `1.29` | `3,797,142` | 4,908,299.96 USD | 182,130.57 USD | `+3.71%` | -26,013,413.71 USD | `+0.28` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `1.29` | `1.29` | `1.29` | `1.29` | `3,408,363` | 4,397,440.00 USD | -499,769.95 USD | `-11.37%` | -26,513,183.66 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.29` | `1.29` | `1.28` | `1.28` | `16,933,961` | 21,714,946.34 USD | -9,957,284.42 USD | `-45.85%` | -36,470,468.08 USD | `-3.75` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.31` | `1.32` | `1.30` | `1.30` | `30,534,069` | 39,864,527.69 USD | -3,664,960.48 USD | `-9.19%` | -24,545,254.96 USD | `-0.63` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.30` | `1.30` | `1.29` | `1.29` | `27,238,695` | 35,241,786.93 USD | -1,210,810.88 USD | `-3.44%` | -25,756,065.84 USD | `+0.08` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.28` | `24,139,766` | 31,021,070.28 USD | -10,275,127.88 USD | `-33.12%` | -36,031,193.72 USD | `-2.11` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `81,912,597` | 106,127,471.89 USD | -15,150,975.98 USD | `-14.28%` | -39,653,151.12 USD | `-0.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.33` | `1.29` | `1.29` | `112,558,954` | 146,533,666.97 USD | -23,231,128.88 USD | `-15.85%` | -23,206,069.15 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,047,304.81 USD | `+0.62` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `88,859,028` | 115,023,863.59 USD | -15,099,314.90 USD | `-13.13%` | -39,601,490.04 USD | `-0.92` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `ASK` | `1.28` | `51292.0000` | 65,899.96 USD | 2,866,071.22 USD | `5 orders` | `+0.15%` | `-` |
| `ASK` | `1.28` | `15847.0000` | 20,358.64 USD | 2,800,171.26 USD | `5 orders` | `+0.14%` | `-` |
| `ASK` | `1.28` | `15668.0000` | 20,127.11 USD | 2,779,812.62 USD | `7 orders` | `+0.14%` | `-` |
| `ASK` | `1.28` | `98513.0000` | 126,539.95 USD | 2,759,685.51 USD | `9 orders` | `+0.13%` | `-` |
| `ASK` | `1.28` | `354100.0000` | 454,806.04 USD | 2,633,145.56 USD | `5 orders` | `+0.12%` | `-` |
| `ASK` | `1.28` | `438776.0000` | 563,520.02 USD | 2,178,339.52 USD | `10 orders` | `+0.11%` | `-` |
| `ASK` | `1.28` | `165763.0000` | 212,872.84 USD | 1,614,819.50 USD | `12 orders` | `+0.11%` | `-` |
| `ASK` | `1.28` | `65342.0000` | 83,905.66 USD | 1,401,946.66 USD | `7 orders` | `+0.10%` | `-` |
| `ASK` | `1.28` | `322062.0000` | 413,527.61 USD | 1,318,041.00 USD | `14 orders` | `+0.09%` | `-` |
| `ASK` | `1.28` | `61582.0000` | 79,065.13 USD | 904,513.39 USD | `9 orders` | `+0.08%` | `-` |
| `ASK` | `1.28` | `76244.0000` | 97,882.05 USD | 825,448.26 USD | `10 orders` | `+0.07%` | `-` |
| `ASK` | `1.28` | `62664.0000` | 80,441.78 USD | 727,566.21 USD | `6 orders` | `+0.07%` | `-` |
| `ASK` | `1.28` | `67181.0000` | 86,233.53 USD | 647,124.44 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `1.28` | `45942.0000` | 58,966.56 USD | 560,890.90 USD | `13 orders` | `+0.05%` | `-` |
| `ASK` | `1.28` | `38387.0000` | 49,265.88 USD | 501,924.35 USD | `13 orders` | `+0.04%` | `-` |
| `ASK` | `1.28` | `96693.0000` | 124,086.13 USD | 452,658.47 USD | `16 orders` | `+0.04%` | `-` |
| `ASK` | `1.28` | `92493.0000` | 118,687.02 USD | 328,572.34 USD | `17 orders` | `+0.03%` | `-` |
| `ASK` | `1.28` | `44993.0000` | 57,730.52 USD | 209,885.33 USD | `10 orders` | `+0.02%` | `-` |
| `ASK` | `1.28` | `28682.0000` | 36,799.01 USD | 152,154.81 USD | `8 orders` | `+0.01%` | `-` |
| `ASK` | `1.28` | `89918.0000` | 115,355.80 USD | 115,355.80 USD | `24 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.28` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.28` | `0.00%` | `-` |
| `BID` | `1.28` | `2824.0000` | 3,622.63 USD | 3,622.63 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `1.28` | `3697.0000` | 4,742.14 USD | 8,364.77 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `1.28` | `14050.0000` | 18,020.53 USD | 26,385.30 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `1.28` | `13809.0000` | 17,710.04 USD | 44,095.34 USD | `7 orders` | `-0.03%` | `-` |
| `BID` | `1.28` | `63785.0000` | 81,797.88 USD | 125,893.23 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `1.28` | `36401.0000` | 46,677.00 USD | 172,570.23 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `1.28` | `50958.0000` | 65,338.35 USD | 237,908.58 USD | `9 orders` | `-0.05%` | `-` |
| `BID` | `1.28` | `34178.0000` | 43,819.61 USD | 281,728.19 USD | `9 orders` | `-0.06%` | `-` |
| `BID` | `1.28` | `113060.0000` | 144,942.92 USD | 426,671.11 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `1.28` | `104662.0000` | 134,166.22 USD | 560,837.33 USD | `10 orders` | `-0.07%` | `-` |
| `BID` | `1.28` | `292828.0000` | 375,346.93 USD | 936,184.26 USD | `14 orders` | `-0.08%` | `-` |
| `BID` | `1.28` | `137902.0000` | 176,748.99 USD | 1,112,933.25 USD | `12 orders` | `-0.09%` | `-` |
| `BID` | `1.28` | `89827.0000` | 115,122.28 USD | 1,228,055.53 USD | `14 orders` | `-0.10%` | `-` |
| `BID` | `1.28` | `49541.0000` | 63,486.79 USD | 1,291,542.33 USD | `12 orders` | `-0.11%` | `-` |
| `BID` | `1.28` | `24308.0000` | 31,148.27 USD | 1,322,690.60 USD | `10 orders` | `-0.11%` | `-` |
| `BID` | `1.28` | `109556.0000` | 140,374.10 USD | 1,463,064.70 USD | `14 orders` | `-0.12%` | `-` |
| `BID` | `1.28` | `272531.0000` | 349,166.72 USD | 1,812,231.42 USD | `9 orders` | `-0.13%` | `-` |
| `BID` | `1.28` | `90113.0000` | 115,443.76 USD | 1,927,675.18 USD | `11 orders` | `-0.14%` | `-` |
| `BID` | `1.28` | `555880.0000` | 712,082.28 USD | 2,639,757.46 USD | `12 orders` | `-0.14%` | `-` |
| `BID` | `1.28` | `181967.0000` | 233,081.53 USD | 2,872,838.99 USD | `7 orders` | `-0.15%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:15:45 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `26` | `0x31b1...1434` | `LONG` | 44,899,783.83 USD | `35,031,430.00` | `1.13` | `1.28` | `0.9612` | 5,320,900.56 USD | `+11.85%` | `10X Cross` |
| `89` | `0x5b5d...c060` | `SHORT` | 20,324,588.51 USD | `15,857,524.00` | `1.44` | `1.28` | `11.27` | 2,454,373.86 USD | `+12.08%` | `5X Cross` |
| `149` | `0x58f0...0d20` | `LONG` | 14,013,255.22 USD | `10,931,629.00` | `1.36` | `1.28` | `1.26` | -851,897.75 USD | `-6.08%` | `20X Cross` |
| `155` | `0xb83d...6e36` | `SHORT` | 13,539,475.71 USD | `10,555,450.00` | `1.50` | `1.28` | `13.84` | 2,283,093.93 USD | `+16.86%` | `5X Cross` |
| `436` | `0xca49...53c8` | `SHORT` | 5,304,810.19 USD | `4,138,886.00` | `1.44` | `1.28` | `4.43` | 648,512.55 USD | `+12.22%` | `20X Cross` |
| `457` | `0xfc27...9d9d` | `SHORT` | 5,078,162.89 USD | `3,962,671.00` | `1.31` | `1.28` | `4.98` | 130,961.88 USD | `+2.58%` | `20X Cross` |
| `505` | `0x610b...b613` | `LONG` | 4,544,756.35 USD | `3,543,946.00` | `1.44` | `1.28` | `0.7092` | -555,236.26 USD | `-12.22%` | `5X Cross` |
| `539` | `0xc30c...a4c9` | `SHORT` | 4,233,799.07 USD | `3,302,753.00` | `1.42` | `1.28` | `1.60` | 466,087.78 USD | `+11.01%` | `8X Cross` |
| `549` | `0xdd53...2b13` | `SHORT` | 4,157,399.02 USD | `3,243,660.00` | `1.44` | `1.28` | `18.83` | 508,939.22 USD | `+12.24%` | `3X Cross` |
| `599` | `0x9946...0852` | `SHORT` | 3,877,284.77 USD | `3,025,111.00` | `1.43` | `1.28` | `1.66` | 435,899.79 USD | `+11.24%` | `20X Cross` |
| `610` | `0xecb6...2b00` | `SHORT` | 3,813,052.50 USD | `2,974,764.00` | `1.31` | `1.28` | `10.47` | 74,064.73 USD | `+1.94%` | `10X Cross` |
| `691` | `0x9aa5...58af` | `SHORT` | 3,338,174.00 USD | `2,604,083.00` | `1.46` | `1.28` | `4.24` | 459,546.66 USD | `+13.77%` | `20X Cross` |
| `706` | `0xf48f...10fe` | `LONG` | 3,291,124.72 USD | `2,565,779.00` | `1.53` | `1.28` | `0.9295` | -633,516.00 USD | `-19.25%` | `4X Cross` |
| `725` | `0x023a...2355` | `SHORT` | 3,221,318.50 USD | `2,513,121.00` | `1.33` | `1.28` | `4.55` | 114,803.32 USD | `+3.56%` | `20X Cross` |
| `745` | `0x45d2...4029` | `SHORT` | 3,143,519.50 USD | `2,453,000.00` | `1.48` | `1.28` | `16.33` | 494,760.92 USD | `+15.74%` | `20X Cross` |
| `1016` | `0xc179...e0c8` | `SHORT` | 2,229,207.86 USD | `1,739,123.00` | `1.30` | `1.28` | `4.76` | 34,014.66 USD | `+1.53%` | `10X Cross` |
| `1074` | `0xfc66...ca06` | `SHORT` | 2,085,397.59 USD | `1,626,929.00` | `1.31` | `1.28` | `22.91` | 46,169.11 USD | `+2.21%` | `20X Cross` |
| `1086` | `0xeadc...9d55` | `LONG` | 2,076,104.07 USD | `1,619,805.00` | `1.21` | `1.28` | `0.000000` | 117,261.05 USD | `+5.65%` | `20X Cross` |
| `1156` | `0x94b2...599e` | `SHORT` | 1,974,710.06 USD | `1,540,696.00` | `1.36` | `1.28` | `1.83` | 125,756.39 USD | `+6.37%` | `20X Cross` |
| `1164` | `0xbcd4...0dd2` | `SHORT` | 1,961,839.62 USD | `1,529,461.00` | `1.31` | `1.28` | `2.22` | 42,704.97 USD | `+2.18%` | `20X Cross` |
| `1177` | `0x3fc5...c0c1` | `SHORT` | 1,939,158.92 USD | `1,511,779.00` | `1.52` | `1.28` | `2.66` | 352,455.68 USD | `+18.18%` | `20X Cross` |
| `1211` | `0x31ef...f715` | `LONG` | 1,890,905.05 USD | `1,475,080.00` | `1.49` | `1.28` | `1.04` | -308,360.35 USD | `-16.31%` | `3X Isolated` |
| `1259` | `0x7737...bf66` | `SHORT` | 1,811,639.37 USD | `1,413,466.00` | `1.41` | `1.28` | `13.96` | 187,229.28 USD | `+10.33%` | `10X Cross` |
| `1278` | `0x77ee...a018` | `LONG` | 1,788,231.27 USD | `1,394,985.00` | `1.28` | `1.28` | `0.000000` | -3,628.88 USD | `-0.20%` | `20X Cross` |
| `1280` | `0xef96...9383` | `SHORT` | 1,782,982.52 USD | `1,390,999.00` | `1.34` | `1.28` | `4.04` | 80,802.70 USD | `+4.53%` | `20X Cross` |
| `1355` | `0xee2b...d67e` | `LONG` | 1,675,178.60 USD | `1,306,284.00` | `1.55` | `1.28` | `0.2574` | -355,476.30 USD | `-21.22%` | `4X Cross` |
| `1420` | `0x215d...f80a` | `LONG` | 1,604,402.58 USD | `1,251,777.00` | `1.32` | `1.28` | `1.19` | -50,051.65 USD | `-3.12%` | `14X Cross` |
| `1456` | `0x123d...3bff` | `LONG` | 1,558,902.51 USD | `1,215,329.00` | `1.35` | `1.28` | `0.000000` | -78,166.71 USD | `-5.01%` | `10X Cross` |
| `1499` | `0x95da...2328` | `LONG` | 1,502,152.21 USD | `1,171,817.00` | `1.37` | `1.28` | `0.000000` | -99,623.78 USD | `-6.63%` | `5X Cross` |
| `1506` | `0xdf95...7d72` | `SHORT` | 1,486,919.40 USD | `1,160,115.00` | `1.37` | `1.28` | `33.30` | 106,439.86 USD | `+7.16%` | `20X Cross` |
| `1558` | `0x5fa3...35b7` | `SHORT` | 1,428,099.41 USD | `1,114,049.00` | `1.31` | `1.28` | `3.10` | 30,530.28 USD | `+2.14%` | `20X Cross` |
| `1639` | `0x4537...8732` | `SHORT` | 1,332,776.05 USD | `1,039,688.00` | `1.32` | `1.28` | `2.22` | 34,679.90 USD | `+2.60%` | `10X Cross` |
| `1668` | `0xb1ce...681b` | `LONG` | 1,309,288.39 USD | `1,021,764.00` | `1.49` | `1.28` | `1.16` | -214,768.11 USD | `-16.40%` | `4X Isolated` |
| `1771` | `0x3c36...461a` | `LONG` | 1,204,863.37 USD | `940,051.00` | `1.30` | `1.28` | `1.06` | -14,217.25 USD | `-1.18%` | `10X Cross` |
| `1984` | `0xbfc7...80b4` | `SHORT` | 1,025,520.00 USD | `800,000.00` | `1.48` | `1.28` | `6.99` | 157,934.65 USD | `+15.40%` | `20X Cross` |

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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.32` (Vol: 2,200,000.00 USD, Dist: `+2.69%`) | Long MP=`1.28` (Vol: 2,900,000.00 USD, Dist: `--0.76%`)
  * 48H Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+4.84%`) | Long MP=`1.28` (Vol: 2,900,000.00 USD, Dist: `--0.76%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,600,000.00 USD, Dist: `+4.84%`) | Long MP=`1.28` (Vol: 3,700,000.00 USD, Dist: `--0.29%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,200,000.00 USD, Dist: `+4.92%`) | Long MP=`1.28` (Vol: 4,400,000.00 USD, Dist: `--0.33%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2850` | 577.70 USD | 74,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 3,800.00 USD | 74,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 4,910.00 USD | 74,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 1,530.00 USD | 74,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 112.23 USD | 74,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 1,500.00 USD | 74,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 2,220.00 USD | 74,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 1,020.00 USD | 74,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 10,290.00 USD | 74,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 3,560.00 USD | 74,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 972.00 USD | 74,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 1,640.00 USD | 74,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 14,900.00 USD | 74,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 9,040.00 USD | 74,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 129,490.00 USD | 74,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 8,210.00 USD | 74,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 3,250.00 USD | 74,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 1,010.00 USD | 74,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 11,350.00 USD | 74,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 28,520.00 USD | 74,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 1,840.00 USD | 74,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 15,090.00 USD | 74,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 9,930.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 7,680.00 USD | 74,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 12,880.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 3,650.00 USD | 74,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 45,720.00 USD | 74,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 8,470.00 USD | 74,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 5,660.00 USD | 74,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 22,060.00 USD | 74,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 17,370.00 USD | 74,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 30,240.00 USD | 74,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 826.88 USD | 74,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 6,070.00 USD | 74,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 21,290.00 USD | 74,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 134,650.00 USD | 74,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 32,280.00 USD | 74,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 28,770.00 USD | 74,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 20,460.00 USD | 74,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 9,220.00 USD | 74,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 2,520,000.00 USD | 74,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 73,720.00 USD | 71,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 220,580.00 USD | 71,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 19,400.00 USD | 71,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 64,730.00 USD | 71,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 106,840.00 USD | 71,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 3,450.00 USD | 71,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 11,680.00 USD | 71,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 43,850.00 USD | 71,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 19,820.00 USD | 71,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 20,760.00 USD | 71,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 26,290.00 USD | 71,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 493,440.00 USD | 71,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 72,430.00 USD | 70,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 57,140.00 USD | 70,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 44,650.00 USD | 70,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 5,650.00 USD | 70,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 179,560.00 USD | 70,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 358,710.00 USD | 70,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 109,640.00 USD | 69,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 2,440,000.00 USD | 69,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 116,090.00 USD | 67,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 81,170.00 USD | 67,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 89,100.00 USD | 67,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 859,740.00 USD | 67,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 94,530.00 USD | 66,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,920,000.00 USD | 66,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 158,150.00 USD | 32,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 449,560.00 USD | 31,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 555,750.00 USD | 31,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 525,880.00 USD | 30,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 187,640.00 USD | 30,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 139,190.00 USD | 30,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,110,000.00 USD | 30,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 86,610.00 USD | 28,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,070,000.00 USD | 27,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 440,620.00 USD | 26,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 437,520.00 USD | 26,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 770,430.00 USD | 25,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 91,580.00 USD | 25,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 66,790.00 USD | 25,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 586,790.00 USD | 25,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 298,010.00 USD | 24,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 384,090.00 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 280,600.00 USD | 23,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 201,030,000.00 USD | 201,030,000.00 USD | 272,740.00 USD | 53,330.00 USD | 52,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 200,650,000.00 USD | 200,650,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 200,490,000.00 USD | 200,490,000.00 USD | 12,250.00 USD | 37,300.00 USD | 120,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 69,580,000.00 USD | 69,580,000.00 USD | 1,740.00 USD | 414.70 USD | 112,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 200,320,000.00 USD | 200,320,000.00 USD | 97,250.00 USD | 57,460.00 USD | 136,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 116,500.00 USD | 23,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 69,470,000.00 USD | 69,470,000.00 USD | 29,120.00 USD | 9,250.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 200,030,000.00 USD | 200,030,000.00 USD | 173,190.00 USD | 99,350.00 USD | 520,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 69,400,000.00 USD | 69,400,000.00 USD | 137,370.00 USD | 26,520.00 USD | 98,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 199,230,000.00 USD | 199,230,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 69,130,000.00 USD | 69,130,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 198,800,000.00 USD | 198,800,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 68,520,000.00 USD | 68,520,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 197,780,000.00 USD | 197,780,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 67,890,000.00 USD | 67,890,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 196,400,000.00 USD | 196,400,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,600,000.00 USD | 23,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 67,680,000.00 USD | 67,680,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 195,780,000.00 USD | 195,780,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 67,370,000.00 USD | 67,370,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 194,400,000.00 USD | 194,400,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 67,210,000.00 USD | 67,210,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 192,890,000.00 USD | 192,890,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 67,030,000.00 USD | 67,030,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 191,500,000.00 USD | 191,500,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 66,780,000.00 USD | 66,780,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 190,710,000.00 USD | 190,710,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 925,770.00 USD | 21,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 66,440,000.00 USD | 66,440,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 189,820,000.00 USD | 189,820,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 66,310,000.00 USD | 66,310,000.00 USD | 77,850.00 USD | 41,360.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 189,370,000.00 USD | 189,370,000.00 USD | 299,590.00 USD | 131,210.00 USD | 405,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 66,140,000.00 USD | 66,140,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 188,530,000.00 USD | 188,530,000.00 USD | 69,670.00 USD | 152,290.00 USD | 199,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 66,110,000.00 USD | 66,110,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 188,110,000.00 USD | 188,110,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 66,000,000.00 USD | 66,000,000.00 USD | 48,820.00 USD | 7,460.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 187,980,000.00 USD | 187,980,000.00 USD | 81,610.00 USD | 98,170.00 USD | 428,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 1,720,000.00 USD | 20,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 65,920,000.00 USD | 65,920,000.00 USD | 1,560.00 USD | 16,590.00 USD | 20,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 187,370,000.00 USD | 187,370,000.00 USD | 190,550.00 USD | 38,510.00 USD | 383,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 65,880,000.00 USD | 65,880,000.00 USD | 29,730.00 USD | 103.33 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 186,760,000.00 USD | 186,760,000.00 USD | 186,430.00 USD | 128,180.00 USD | 350,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 65,840,000.00 USD | 65,840,000.00 USD | 28,290.00 USD | 10,480.00 USD | 48,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 186,090,000.00 USD | 186,090,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 65,750,000.00 USD | 65,750,000.00 USD | 67,440.00 USD | 29,830.00 USD | 130,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 185,630,000.00 USD | 185,630,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 65,520,000.00 USD | 65,520,000.00 USD | 106,940.00 USD | 33,950.00 USD | 31,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 184,970,000.00 USD | 184,970,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 496,770.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 65,350,000.00 USD | 65,350,000.00 USD | 109,050.00 USD | 6,620.00 USD | 18,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 184,260,000.00 USD | 184,260,000.00 USD | 5,350.00 USD | 93,870.00 USD | 187,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 65,210,000.00 USD | 65,210,000.00 USD | 41,430.00 USD | 21,290.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 183,970,000.00 USD | 183,970,000.00 USD | 67,200.00 USD | 57,670.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 65,150,000.00 USD | 65,150,000.00 USD | 23,000.00 USD | 6,640.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 183,830,000.00 USD | 183,830,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 65,120,000.00 USD | 65,120,000.00 USD | 43,340.00 USD | 13,890.00 USD | 61,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 183,750,000.00 USD | 183,750,000.00 USD | 202,570.00 USD | 53,170.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 183,450,000.00 USD | 183,450,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 664,010.00 USD | 18,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 65,000,000.00 USD | 65,000,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 183,350,000.00 USD | 183,350,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 64,990,000.00 USD | 64,990,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 183,260,000.00 USD | 183,260,000.00 USD | 361,660.00 USD | 45,260.00 USD | 357,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 182,490,000.00 USD | 182,490,000.00 USD | 70,670.00 USD | 152,900.00 USD | 457,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 181,810,000.00 USD | 181,810,000.00 USD | 278,240.00 USD | 50,420.00 USD | 33,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 181,450,000.00 USD | 181,450,000.00 USD | 5,680.00 USD | 39,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 366,920.00 USD | 17,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 181,400,000.00 USD | 181,400,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 181,310,000.00 USD | 181,310,000.00 USD | 0.00 USD | 765.15 USD | 40,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 181,260,000.00 USD | 181,260,000.00 USD | 54,470.00 USD | 2,490.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 181,190,000.00 USD | 181,190,000.00 USD | 10,460.00 USD | 191,360.00 USD | 207,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 180,780,000.00 USD | 180,780,000.00 USD | 649,620.00 USD | 191,250.00 USD | 200,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,440,000.00 USD | 17,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 179,740,000.00 USD | 179,740,000.00 USD | 341,300.00 USD | 128,580.00 USD | 60,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 179,210,000.00 USD | 179,210,000.00 USD | 44,790.00 USD | 125,700.00 USD | 371,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 64,960,000.00 USD | 64,960,000.00 USD | 50,810.00 USD | 1,040.00 USD | 336,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 178,670,000.00 USD | 178,670,000.00 USD | 257,070.00 USD | 187,490.00 USD | 678,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 64,570,000.00 USD | 64,570,000.00 USD | 4,340.00 USD | 396.00 USD | 72,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 177,550,000.00 USD | 177,550,000.00 USD | 724,190.00 USD | 142,840.00 USD | 467,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 64,490,000.00 USD | 64,490,000.00 USD | 73,550.00 USD | 22,720.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 176,210,000.00 USD | 176,210,000.00 USD | 1,150,000.00 USD | 525,690.00 USD | 2,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 692,280.00 USD | 16,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 64,390,000.00 USD | 64,390,000.00 USD | 802,870.00 USD | 317,390.00 USD | 493,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 172,090,000.00 USD | 172,090,000.00 USD | 1,620,000.00 USD | 912,620.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 62,770,000.00 USD | 62,770,000.00 USD | 1,340,000.00 USD | 641,660.00 USD | 928,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 167,710,000.00 USD | 167,710,000.00 USD | 1,890,000.00 USD | 972,840.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 59,870,000.00 USD | 59,870,000.00 USD | 576,610.00 USD | 333,360.00 USD | 574,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 162,590,000.00 USD | 162,590,000.00 USD | 1,980,000.00 USD | 677,720.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 58,380,000.00 USD | 58,380,000.00 USD | 207,000.00 USD | 233,640.00 USD | 324,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 157,360,000.00 USD | 157,360,000.00 USD | 982,310.00 USD | 740,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 57,620,000.00 USD | 57,620,000.00 USD | 546,970.00 USD | 84,110.00 USD | 349,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 154,550,000.00 USD | 154,550,000.00 USD | 2,160,000.00 USD | 376,950.00 USD | 1,810,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 250,530.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.25` | 56,640,000.00 USD | 56,640,000.00 USD | 384,220.00 USD | 90,850.00 USD | 261,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 150,200,000.00 USD | 150,200,000.00 USD | 2,120,000.00 USD | 1,190,000.00 USD | 5,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 55,900,000.00 USD | 55,900,000.00 USD | 207,040.00 USD | 196,500.00 USD | 303,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 141,580,000.00 USD | 141,580,000.00 USD | 2,280,000.00 USD | 1,370,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 55,190,000.00 USD | 55,190,000.00 USD | 117,990.00 USD | 79,810.00 USD | 571,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 134,460,000.00 USD | 134,460,000.00 USD | 2,810,000.00 USD | 918,840.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 54,420,000.00 USD | 54,420,000.00 USD | 374,100.00 USD | 17,220.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 128,730,000.00 USD | 128,730,000.00 USD | 1,240,000.00 USD | 673,830.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 53,500,000.00 USD | 53,500,000.00 USD | 315,330.00 USD | 42,480.00 USD | 194,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 125,330,000.00 USD | 125,330,000.00 USD | 625,270.00 USD | 468,670.00 USD | 763,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 14,240,000.00 USD | 15,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.26` | 52,950,000.00 USD | 52,950,000.00 USD | 267,930.00 USD | 152,060.00 USD | 759,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 123,480,000.00 USD | 123,480,000.00 USD | 413,880.00 USD | 407,350.00 USD | 993,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 51,770,000.00 USD | 51,770,000.00 USD | 194,390.00 USD | 1,980.00 USD | 313,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 121,660,000.00 USD | 121,660,000.00 USD | 1,190,000.00 USD | 449,360.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 51,260,000.00 USD | 51,260,000.00 USD | 433,900.00 USD | 218,760.00 USD | 376,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 118,510,000.00 USD | 118,510,000.00 USD | 1,470,000.00 USD | 1,130,000.00 USD | 852,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 50,230,000.00 USD | 50,230,000.00 USD | 1,470,000.00 USD | 545,220.00 USD | 885,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 115,060,000.00 USD | 115,060,000.00 USD | 2,860,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 47,330,000.00 USD | 47,330,000.00 USD | 2,670,000.00 USD | 1,350,000.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 108,450,000.00 USD | 108,450,000.00 USD | 3,640,000.00 USD | 1,830,000.00 USD | 4,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.26` | 431,470.00 USD | 983,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.27` | 41,330,000.00 USD | 41,330,000.00 USD | 1,230,000.00 USD | 666,960.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 98,510,000.00 USD | 98,510,000.00 USD | 3,940,000.00 USD | 1,630,000.00 USD | 6,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 38,220,000.00 USD | 38,220,000.00 USD | 664,170.00 USD | 468,170.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 86,510,000.00 USD | 86,510,000.00 USD | 1,990,000.00 USD | 1,500,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 35,030,000.00 USD | 35,030,000.00 USD | 1,210,000.00 USD | 219,850.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 79,320,000.00 USD | 79,320,000.00 USD | 4,070,000.00 USD | 1,680,000.00 USD | 4,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 32,440,000.00 USD | 32,440,000.00 USD | 1,300,000.00 USD | 345,070.00 USD | 855,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 69,480,000.00 USD | 69,480,000.00 USD | 4,300,000.00 USD | 3,000,000.00 USD | 10,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 29,940,000.00 USD | 29,940,000.00 USD | 2,350,000.00 USD | 848,600.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 51,680,000.00 USD | 51,680,000.00 USD | 3,980,000.00 USD | 1,300,000.00 USD | 7,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.27` | 432,580.00 USD | 552,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.28` | 24,790,000.00 USD | 24,790,000.00 USD | 4,650,000.00 USD | 2,820,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 39,160,000.00 USD | 39,160,000.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 13,370,000.00 USD | 13,370,000.00 USD | 4,550,000.00 USD | 2,050,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 20,890,000.00 USD | 20,890,000.00 USD | 4,790,000.00 USD | 1,750,000.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 2,800,000.00 USD | 2,800,000.00 USD | 1,070,000.00 USD | 844,780.00 USD | 882,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 8,120,000.00 USD | 8,120,000.00 USD | 4,580,000.00 USD | 1,610,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 2,140,000.00 USD | 2,140,000.00 USD | 1,340,000.00 USD | 798,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 5,570,000.00 USD | 5,570,000.00 USD | 3,390,000.00 USD | 2,130,000.00 USD | 45,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 5,020,000.00 USD | 5,020,000.00 USD | 2,380,000.00 USD | 488,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 11,060,000.00 USD | 11,060,000.00 USD | 3,830,000.00 USD | 1,550,000.00 USD | 116,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.28` | 119,630.00 USD | 119,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 5,490,000.00 USD | 5,490,000.00 USD | 365,870.00 USD | 100,470.00 USD | 8,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 11,780,000.00 USD | 11,780,000.00 USD | 724,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 665,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 14,300,000.00 USD | 14,300,000.00 USD | 1,040,000.00 USD | 0.00 USD | 819,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 0.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 301,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 8,670,000.00 USD | 8,670,000.00 USD | 195,630.00 USD | 184,260.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 16,650,000.00 USD | 16,650,000.00 USD | 440,550.00 USD | 0.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 12,650.00 USD | 12,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 9,370,000.00 USD | 9,370,000.00 USD | 0.00 USD | 413,600.00 USD | 288,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 389,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 86,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 10,010,000.00 USD | 10,010,000.00 USD | 193,920.00 USD | 81,320.00 USD | 278,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 18,570,000.00 USD | 18,570,000.00 USD | 0.00 USD | 286,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 11,440,000.00 USD | 11,440,000.00 USD | 516,450.00 USD | 910,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 21,080,000.00 USD | 21,080,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 12,130,000.00 USD | 12,130,000.00 USD | 202,870.00 USD | 353,430.00 USD | 127,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 2,560.00 USD | 15,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 12,600,000.00 USD | 12,600,000.00 USD | 303,100.00 USD | 64,580.00 USD | 111,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 23,030,000.00 USD | 23,030,000.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 14,360,000.00 USD | 14,360,000.00 USD | 413,300.00 USD | 2,070.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 24,270,000.00 USD | 24,270,000.00 USD | 586,970.00 USD | 0.00 USD | 649,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 16,130,000.00 USD | 16,130,000.00 USD | 634,790.00 USD | 687,160.00 USD | 450,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 27,260,000.00 USD | 27,260,000.00 USD | 704,520.00 USD | 318,670.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 18,610,000.00 USD | 18,610,000.00 USD | 1,290,000.00 USD | 511,150.00 USD | 689,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 29,620,000.00 USD | 29,620,000.00 USD | 557,940.00 USD | 430,030.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 21,990,000.00 USD | 21,990,000.00 USD | 372,630.00 USD | 572,040.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 32,040,000.00 USD | 32,040,000.00 USD | 57,160.00 USD | 1,070,000.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 269.57 USD | 15,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 28,520,000.00 USD | 28,520,000.00 USD | 1,250,000.00 USD | 1,730,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 36,660,000.00 USD | 36,660,000.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 34,220,000.00 USD | 34,220,000.00 USD | 2,210,000.00 USD | 977,080.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 39,680,000.00 USD | 39,680,000.00 USD | 755,330.00 USD | 495,580.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 37,460,000.00 USD | 37,460,000.00 USD | 1,510,000.00 USD | 706,650.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 41,250,000.00 USD | 41,250,000.00 USD | 966,720.00 USD | 235,180.00 USD | 367,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 42,040,000.00 USD | 42,040,000.00 USD | 1,970,000.00 USD | 720,740.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 45,290,000.00 USD | 45,290,000.00 USD | 1,980,000.00 USD | 761,100.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 44,040,000.00 USD | 44,040,000.00 USD | 1,080,000.00 USD | 287,550.00 USD | 625,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 47,660,000.00 USD | 47,660,000.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 101,940.00 USD | 117,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 46,530,000.00 USD | 46,530,000.00 USD | 624,130.00 USD | 621,340.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 48,190,000.00 USD | 48,190,000.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 48,770,000.00 USD | 48,770,000.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 49,350,000.00 USD | 49,350,000.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 51,350,000.00 USD | 51,350,000.00 USD | 748,200.00 USD | 298,240.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 51,070,000.00 USD | 51,070,000.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 52,980,000.00 USD | 52,980,000.00 USD | 764,030.00 USD | 85,990.00 USD | 777,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 53,340,000.00 USD | 53,340,000.00 USD | 830,370.00 USD | 108,920.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 54,740,000.00 USD | 54,740,000.00 USD | 721,700.00 USD | 300,370.00 USD | 737,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 53,850,000.00 USD | 53,850,000.00 USD | 131,350.00 USD | 194,680.00 USD | 189,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 58,590.00 USD | 176,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 56,770,000.00 USD | 56,770,000.00 USD | 831,030.00 USD | 219,020.00 USD | 976,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 55,800,000.00 USD | 55,800,000.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 60,230,000.00 USD | 60,230,000.00 USD | 1,430,000.00 USD | 370,350.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 57,900,000.00 USD | 57,900,000.00 USD | 1,240,000.00 USD | 362,920.00 USD | 494,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 63,830,000.00 USD | 63,830,000.00 USD | 1,780,000.00 USD | 821,890.00 USD | 999,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 62,630,000.00 USD | 62,630,000.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 440,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 68,560,000.00 USD | 68,560,000.00 USD | 2,510,000.00 USD | 785,850.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 68,370,000.00 USD | 68,370,000.00 USD | 1,730,000.00 USD | 2,870,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 71,220,000.00 USD | 71,220,000.00 USD | 1,130,000.00 USD | 629,160.00 USD | 904,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 79,600,000.00 USD | 79,600,000.00 USD | 3,700,000.00 USD | 1,930,000.00 USD | 5,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 165,000.00 USD | 341,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 72,630,000.00 USD | 72,630,000.00 USD | 585,620.00 USD | 289,260.00 USD | 527,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 87,360,000.00 USD | 87,360,000.00 USD | 2,550,000.00 USD | 2,230,000.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 75,620,000.00 USD | 75,620,000.00 USD | 1,290,000.00 USD | 356,450.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 97,850,000.00 USD | 97,850,000.00 USD | 4,410,000.00 USD | 1,760,000.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 76,720,000.00 USD | 76,720,000.00 USD | 516,420.00 USD | 130,090.00 USD | 452,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 105,620,000.00 USD | 105,620,000.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 78,970,000.00 USD | 78,970,000.00 USD | 879,540.00 USD | 405,430.00 USD | 968,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 113,950,000.00 USD | 113,950,000.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 81,330,000.00 USD | 81,330,000.00 USD | 848,160.00 USD | 297,760.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 122,180,000.00 USD | 122,180,000.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 3,990.00 USD | 345,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 83,110,000.00 USD | 83,110,000.00 USD | 992,470.00 USD | 102,980.00 USD | 687,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 126,250,000.00 USD | 126,250,000.00 USD | 1,320,000.00 USD | 879,500.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 83,930,000.00 USD | 83,930,000.00 USD | 504,090.00 USD | 150,540.00 USD | 163,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 130,040,000.00 USD | 130,040,000.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 84,720,000.00 USD | 84,720,000.00 USD | 374,230.00 USD | 183,190.00 USD | 237,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 132,420,000.00 USD | 132,420,000.00 USD | 671,910.00 USD | 542,980.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 85,830,000.00 USD | 85,830,000.00 USD | 452,880.00 USD | 103,540.00 USD | 545,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 136,650,000.00 USD | 136,650,000.00 USD | 2,100,000.00 USD | 895,970.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 85,880,000.00 USD | 85,880,000.00 USD | 0.00 USD | 26,460.00 USD | 25,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 138,350,000.00 USD | 138,350,000.00 USD | 664,020.00 USD | 328,930.00 USD | 707,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 201,820.00 USD | 546,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 86,200,000.00 USD | 86,200,000.00 USD | 68,130.00 USD | 85,100.00 USD | 170,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 138,850,000.00 USD | 138,850,000.00 USD | 239,150.00 USD | 216,290.00 USD | 40,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 86,590,000.00 USD | 86,590,000.00 USD | 159,370.00 USD | 1,410.00 USD | 229,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 140,630,000.00 USD | 140,630,000.00 USD | 547,200.00 USD | 138,950.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 86,780,000.00 USD | 86,780,000.00 USD | 1,740.00 USD | 66,370.00 USD | 119,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 142,040,000.00 USD | 142,040,000.00 USD | 465,040.00 USD | 398,870.00 USD | 543,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 86,930,000.00 USD | 86,930,000.00 USD | 75,340.00 USD | 249.08 USD | 69,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 144,900,000.00 USD | 144,900,000.00 USD | 931,390.00 USD | 404,120.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 87,050,000.00 USD | 87,050,000.00 USD | 54,550.00 USD | 884.30 USD | 69,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 146,590,000.00 USD | 146,590,000.00 USD | 594,550.00 USD | 326,340.00 USD | 769,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 87,380,000.00 USD | 87,380,000.00 USD | 117,150.00 USD | 51,620.00 USD | 164,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 148,210,000.00 USD | 148,210,000.00 USD | 676,760.00 USD | 389,310.00 USD | 552,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 88,130,000.00 USD | 88,130,000.00 USD | 336,250.00 USD | 76,440.00 USD | 332,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 150,140,000.00 USD | 150,140,000.00 USD | 579,450.00 USD | 290,350.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 88,720,000.00 USD | 88,720,000.00 USD | 327,030.00 USD | 108,980.00 USD | 158,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 152,690,000.00 USD | 152,690,000.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 89,150,000.00 USD | 89,150,000.00 USD | 309,190.00 USD | 42,880.00 USD | 77,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 153,780,000.00 USD | 153,780,000.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 89,390,000.00 USD | 89,390,000.00 USD | 145,190.00 USD | 54,030.00 USD | 40,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 154,870,000.00 USD | 154,870,000.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 31,650.00 USD | 578,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 89,490,000.00 USD | 89,490,000.00 USD | 57,490.00 USD | 16,600.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 155,370,000.00 USD | 155,370,000.00 USD | 86,820.00 USD | 203,870.00 USD | 200,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 89,870,000.00 USD | 89,870,000.00 USD | 140,810.00 USD | 51,770.00 USD | 189,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 156,460,000.00 USD | 156,460,000.00 USD | 690,420.00 USD | 162,590.00 USD | 238,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 156,620,000.00 USD | 156,620,000.00 USD | 118,760.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 156,940,000.00 USD | 156,940,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 89,890,000.00 USD | 89,890,000.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 157,090,000.00 USD | 157,090,000.00 USD | 121,260.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 11,960.00 USD | 590,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.40` | 89,990,000.00 USD | 89,990,000.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 157,100,000.00 USD | 157,100,000.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 157,110,000.00 USD | 157,110,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 157,250,000.00 USD | 157,250,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 157,360,000.00 USD | 157,360,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 157,610,000.00 USD | 157,610,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 2,610.00 USD | 593,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 157,770,000.00 USD | 157,770,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 157,940,000.00 USD | 157,940,000.00 USD | 12,250.00 USD | 37,300.00 USD | 120,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 90,110,000.00 USD | 90,110,000.00 USD | 1,740.00 USD | 414.70 USD | 112,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 158,230,000.00 USD | 158,230,000.00 USD | 97,250.00 USD | 57,460.00 USD | 136,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 90,140,000.00 USD | 90,140,000.00 USD | 0.00 USD | 158.40 USD | 28,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 158,400,000.00 USD | 158,400,000.00 USD | 11,290.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 90,180,000.00 USD | 90,180,000.00 USD | 29,120.00 USD | 9,090.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 159,030,000.00 USD | 159,030,000.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 596,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.42` | 90,440,000.00 USD | 90,440,000.00 USD | 137,370.00 USD | 26,520.00 USD | 98,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 159,460,000.00 USD | 159,460,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 91,060,000.00 USD | 91,060,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 160,480,000.00 USD | 160,480,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 91,680,000.00 USD | 91,680,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 161,850,000.00 USD | 161,850,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 91,890,000.00 USD | 91,890,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 162,480,000.00 USD | 162,480,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 91,990,000.00 USD | 91,990,000.00 USD | 31,260.00 USD | 27,740.00 USD | 34,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 162,840,000.00 USD | 162,840,000.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 96,220.00 USD | 693,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.43` | 92,210,000.00 USD | 92,210,000.00 USD | 151,550.00 USD | 11,130.00 USD | 55,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 163,860,000.00 USD | 163,860,000.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 92,370,000.00 USD | 92,370,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 165,370,000.00 USD | 165,370,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 92,540,000.00 USD | 92,540,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 166,750,000.00 USD | 166,750,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 92,790,000.00 USD | 92,790,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 167,550,000.00 USD | 167,550,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 92,960,000.00 USD | 92,960,000.00 USD | 93,560.00 USD | 0.00 USD | 75,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 168,080,000.00 USD | 168,080,000.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 32,780.00 USD | 725,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 168,430,000.00 USD | 168,430,000.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 168,890,000.00 USD | 168,890,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 169,730,000.00 USD | 169,730,000.00 USD | 299,590.00 USD | 131,210.00 USD | 405,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 170,150,000.00 USD | 170,150,000.00 USD | 69,670.00 USD | 152,290.00 USD | 199,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 170,280,000.00 USD | 170,280,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 143,010.00 USD | 868,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.45` | 170,410,000.00 USD | 170,410,000.00 USD | 11,070.00 USD | 2,120.00 USD | 116,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 170,890,000.00 USD | 170,890,000.00 USD | 70,540.00 USD | 96,050.00 USD | 311,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 171,500,000.00 USD | 171,500,000.00 USD | 190,550.00 USD | 38,510.00 USD | 383,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 172,140,000.00 USD | 172,140,000.00 USD | 169,890.00 USD | 128,180.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 172,210,000.00 USD | 172,210,000.00 USD | 47,300.00 USD | 23,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.46` | 14,470.00 USD | 883,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 30,250.00 USD | 913,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 10,700.00 USD | 924,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 343,310.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 11,950.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 48,310.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 1,940.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 234.85 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 1,010.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 5,550.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,840.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 8,350.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 5,300,000.00 USD | 6,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 2,520.00 USD | 6,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 1,420.00 USD | 6,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 4,960,000.00 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 134,550.00 USD | 11,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 333,590.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 5,920.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 8,640.00 USD | 12,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 10,670.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 792.33 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 1,690.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 3,940.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 286.06 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 2,540.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 1,140.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 129,650.00 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 2,850.00 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 2,960.00 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 1,650.00 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 2,830,000.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 6,300.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 1,860.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 245,090.00 USD | 15,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 640.90 USD | 15,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,190.00 USD | 15,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 373.38 USD | 15,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 103.95 USD | 15,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 113,350.00 USD | 15,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 582.59 USD | 15,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 227,680.00 USD | 15,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 15,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.99` | 1,760.00 USD | 15,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 322,160.00 USD | 16,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 2,100.00 USD | 16,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 198.36 USD | 16,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 280,760.00 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 6,600.00 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 331.01 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 2,520.00 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 178,520.00 USD | 16,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 16,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 3,330,000.00 USD | 19,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 703.57 USD | 19,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 403.88 USD | 19,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 8,920.00 USD | 19,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 3,890.00 USD | 19,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 64,350.00 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 2,290,000.00 USD | 22,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 63,810.00 USD | 22,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 104.19 USD | 22,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 14,930.00 USD | 22,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 1,530.00 USD | 22,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 5,230.00 USD | 22,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 92,080.00 USD | 22,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 938.67 USD | 22,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 939,560.00 USD | 23,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 109.25 USD | 23,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 179,790.00 USD | 23,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 165,190.00 USD | 23,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 110.63 USD | 23,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 2,420.00 USD | 23,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 169.75 USD | 23,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 309.25 USD | 23,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 24,720.00 USD | 23,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 4,190.00 USD | 23,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 4,890.00 USD | 23,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 5,640.00 USD | 23,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 42,820.00 USD | 23,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.54` | 496.86 USD | 23,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 11,400.00 USD | 23,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 187.25 USD | 23,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.58` | 2,250.00 USD | 23,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.58` | 380.00 USD | 23,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2850` | 74,870,000.00 USD | 0.00 USD | 577.70 USD | `-77.97%` | `2,027.00` |
| `Live` | `Long` | `0.2950` | 74,870,000.00 USD | 0.00 USD | 3,800.00 USD | `-77.19%` | `12,870.00` |
| `Live` | `Long` | `0.3150` | 74,870,000.00 USD | 0.00 USD | 4,910.00 USD | `-75.65%` | `15,577.00` |
| `Live` | `Long` | `0.3250` | 74,860,000.00 USD | 0.00 USD | 1,530.00 USD | `-74.87%` | `4,695.00` |
| `Live` | `Long` | `0.3350` | 74,860,000.00 USD | 0.00 USD | 112.23 USD | `-74.10%` | `335.00` |
| `Live` | `Long` | `0.3450` | 74,860,000.00 USD | 0.00 USD | 1,500.00 USD | `-73.33%` | `4,353.00` |
| `Live` | `Long` | `0.3550` | 74,860,000.00 USD | 0.00 USD | 2,220.00 USD | `-72.55%` | `6,259.00` |
| `Live` | `Long` | `0.3650` | 74,860,000.00 USD | 0.00 USD | 1,020.00 USD | `-71.78%` | `2,790.00` |
| `Live` | `Long` | `0.3850` | 74,850,000.00 USD | 0.00 USD | 10,290.00 USD | `-70.23%` | `26,734.00` |
| `Live` | `Long` | `0.3950` | 74,840,000.00 USD | 0.00 USD | 3,560.00 USD | `-69.46%` | `9,019.00` |
| `Live` | `Long` | `0.4050` | 74,840,000.00 USD | 0.00 USD | 972.00 USD | `-68.69%` | `2,400.00` |
| `Live` | `Long` | `0.4150` | 74,840,000.00 USD | 0.00 USD | 1,640.00 USD | `-67.91%` | `3,960.00` |
| `Live` | `Long` | `0.4250` | 74,840,000.00 USD | 0.00 USD | 14,900.00 USD | `-67.14%` | `35,066.00` |
| `Live` | `Long` | `0.4350` | 74,820,000.00 USD | 0.00 USD | 9,040.00 USD | `-66.37%` | `20,778.00` |
| `Live` | `Long` | `0.4450` | 74,810,000.00 USD | 0.00 USD | 129,490.00 USD | `-65.59%` | `290,999.00` |
| `Live` | `Long` | `0.4550` | 74,680,000.00 USD | 0.00 USD | 8,210.00 USD | `-64.82%` | `18,052.00` |
| `Live` | `Long` | `0.4650` | 74,680,000.00 USD | 0.00 USD | 3,250.00 USD | `-64.05%` | `6,998.00` |
| `Live` | `Long` | `0.4750` | 74,670,000.00 USD | 0.00 USD | 1,010.00 USD | `-63.28%` | `2,127.00` |
| `Live` | `Long` | `0.4850` | 74,670,000.00 USD | 0.00 USD | 11,350.00 USD | `-62.50%` | `23,397.00` |
| `Live` | `Long` | `0.4950` | 74,660,000.00 USD | 0.00 USD | 28,520.00 USD | `-61.73%` | `57,620.00` |
| `Live` | `Long` | `0.5050` | 74,630,000.00 USD | 0.00 USD | 1,840.00 USD | `-60.96%` | `3,635.00` |
| `Live` | `Long` | `0.5150` | 74,630,000.00 USD | 0.00 USD | 15,090.00 USD | `-60.18%` | `29,295.00` |
| `Live` | `Long` | `0.5250` | 74,620,000.00 USD | 0.00 USD | 9,930.00 USD | `-59.41%` | `18,915.00` |
| `Live` | `Long` | `0.5350` | 74,610,000.00 USD | 0.00 USD | 7,680.00 USD | `-58.64%` | `14,359.00` |
| `Live` | `Long` | `0.5450` | 74,600,000.00 USD | 0.00 USD | 12,880.00 USD | `-57.86%` | `23,637.00` |
| `Live` | `Long` | `0.5550` | 74,580,000.00 USD | 0.00 USD | 3,650.00 USD | `-57.09%` | `6,571.00` |
| `Live` | `Long` | `0.5650` | 74,580,000.00 USD | 0.00 USD | 45,720.00 USD | `-56.32%` | `80,926.00` |
| `Live` | `Long` | `0.5750` | 74,540,000.00 USD | 0.00 USD | 8,470.00 USD | `-55.54%` | `14,732.00` |
| `Live` | `Long` | `0.5850` | 74,530,000.00 USD | 0.00 USD | 5,660.00 USD | `-54.77%` | `9,672.00` |
| `Live` | `Long` | `0.5950` | 74,520,000.00 USD | 0.00 USD | 22,060.00 USD | `-54.00%` | `37,077.00` |
| `Live` | `Long` | `0.6050` | 74,500,000.00 USD | 0.00 USD | 17,370.00 USD | `-53.22%` | `28,715.00` |
| `Live` | `Long` | `0.6150` | 74,480,000.00 USD | 0.00 USD | 30,240.00 USD | `-52.45%` | `49,170.00` |
| `Live` | `Long` | `0.6250` | 74,450,000.00 USD | 0.00 USD | 826.88 USD | `-51.68%` | `1,323.00` |
| `Live` | `Long` | `0.6350` | 74,450,000.00 USD | 0.00 USD | 6,070.00 USD | `-50.90%` | `9,564.00` |
| `Live` | `Long` | `0.6450` | 74,440,000.00 USD | 0.00 USD | 21,290.00 USD | `-50.13%` | `33,012.00` |
| `Live` | `Long` | `0.6550` | 74,420,000.00 USD | 0.00 USD | 134,650.00 USD | `-49.36%` | `205,565.00` |
| `Live` | `Long` | `0.6650` | 74,290,000.00 USD | 0.00 USD | 32,280.00 USD | `-48.59%` | `48,539.00` |
| `Live` | `Long` | `0.6750` | 74,260,000.00 USD | 0.00 USD | 28,770.00 USD | `-47.81%` | `42,625.00` |
| `Live` | `Long` | `0.6850` | 74,230,000.00 USD | 0.00 USD | 20,460.00 USD | `-47.04%` | `29,872.00` |
| `Live` | `Long` | `0.6950` | 74,210,000.00 USD | 0.00 USD | 9,220.00 USD | `-46.27%` | `13,269.00` |
| `Live` | `Long` | `0.7050` | 74,200,000.00 USD | 0.00 USD | 2,520,000.00 USD | `-45.49%` | `3,575,234.00` |
| `Live` | `Long` | `0.7150` | 71,680,000.00 USD | 0.00 USD | 73,720.00 USD | `-44.72%` | `103,108.00` |
| `Live` | `Long` | `0.7250` | 71,600,000.00 USD | 0.00 USD | 220,580.00 USD | `-43.95%` | `304,246.00` |
| `Live` | `Long` | `0.7350` | 71,380,000.00 USD | 0.00 USD | 19,400.00 USD | `-43.17%` | `26,388.00` |
| `Live` | `Long` | `0.7450` | 71,360,000.00 USD | 0.00 USD | 64,730.00 USD | `-42.40%` | `86,884.00` |
| `Live` | `Long` | `0.7550` | 71,300,000.00 USD | 0.00 USD | 106,840.00 USD | `-41.63%` | `141,516.00` |
| `Live` | `Long` | `0.7650` | 71,190,000.00 USD | 0.00 USD | 3,450.00 USD | `-40.85%` | `4,514.00` |
| `Live` | `Long` | `0.7750` | 71,190,000.00 USD | 0.00 USD | 11,680.00 USD | `-40.08%` | `15,077.00` |
| `Live` | `Long` | `0.7850` | 71,180,000.00 USD | 0.00 USD | 43,850.00 USD | `-39.31%` | `55,864.00` |
| `Live` | `Long` | `0.7950` | 71,130,000.00 USD | 0.00 USD | 19,820.00 USD | `-38.53%` | `24,931.00` |
| `Live` | `Long` | `0.8050` | 71,110,000.00 USD | 0.00 USD | 20,760.00 USD | `-37.76%` | `25,795.00` |
| `Live` | `Long` | `0.8150` | 71,090,000.00 USD | 0.00 USD | 26,290.00 USD | `-36.99%` | `32,261.00` |
| `Live` | `Long` | `0.8250` | 71,070,000.00 USD | 0.00 USD | 493,440.00 USD | `-36.21%` | `598,110.00` |
| `Live` | `Long` | `0.8350` | 70,570,000.00 USD | 0.00 USD | 72,430.00 USD | `-35.44%` | `86,738.00` |
| `Live` | `Long` | `0.8450` | 70,500,000.00 USD | 0.00 USD | 57,140.00 USD | `-34.67%` | `67,618.00` |
| `Live` | `Long` | `0.8550` | 70,440,000.00 USD | 0.00 USD | 44,650.00 USD | `-33.90%` | `52,218.00` |
| `Live` | `Long` | `0.8650` | 70,400,000.00 USD | 0.00 USD | 5,650.00 USD | `-33.12%` | `6,537.00` |
| `Live` | `Long` | `0.8750` | 70,390,000.00 USD | 0.00 USD | 179,560.00 USD | `-32.35%` | `205,210.00` |
| `Live` | `Long` | `0.8850` | 70,210,000.00 USD | 0.00 USD | 358,710.00 USD | `-31.58%` | `405,327.00` |
| `Live` | `Long` | `0.8950` | 69,850,000.00 USD | 0.00 USD | 109,640.00 USD | `-30.80%` | `122,501.00` |
| `Live` | `Long` | `0.9050` | 69,750,000.00 USD | 0.00 USD | 2,440,000.00 USD | `-30.03%` | `2,696,683.00` |
| `Live` | `Long` | `0.9150` | 67,300,000.00 USD | 0.00 USD | 116,090.00 USD | `-29.26%` | `126,870.00` |
| `Live` | `Long` | `0.9250` | 67,190,000.00 USD | 0.00 USD | 81,170.00 USD | `-28.48%` | `87,752.00` |
| `Live` | `Long` | `0.9350` | 67,110,000.00 USD | 0.00 USD | 89,100.00 USD | `-27.71%` | `95,291.00` |
| `Live` | `Long` | `0.9450` | 67,020,000.00 USD | 0.00 USD | 859,740.00 USD | `-26.94%` | `909,774.00` |
| `Live` | `Long` | `0.9550` | 66,160,000.00 USD | 0.00 USD | 94,530.00 USD | `-26.16%` | `98,987.00` |
| `Live` | `Long` | `0.9650` | 66,060,000.00 USD | 0.00 USD | 33,920,000.00 USD | `-25.39%` | `35,153,783.00` |
| `Live` | `Long` | `0.9750` | 32,140,000.00 USD | 0.00 USD | 158,150.00 USD | `-24.62%` | `162,200.00` |
| `Live` | `Long` | `0.9850` | 31,980,000.00 USD | 0.00 USD | 449,560.00 USD | `-23.84%` | `456,407.00` |
| `Live` | `Long` | `0.9950` | 31,530,000.00 USD | 0.00 USD | 555,750.00 USD | `-23.07%` | `558,539.00` |
| `Live` | `Long` | `1.00` | 30,980,000.00 USD | 0.00 USD | 525,880.00 USD | `-22.30%` | `523,263.00` |
| `Live` | `Long` | `1.01` | 30,450,000.00 USD | 0.00 USD | 187,640.00 USD | `-21.52%` | `184,871.00` |
| `Live` | `Long` | `1.02` | 30,260,000.00 USD | 0.00 USD | 139,190.00 USD | `-20.75%` | `135,797.00` |
| `Live` | `Long` | `1.03` | 30,120,000.00 USD | 0.00 USD | 2,110,000.00 USD | `-19.98%` | `2,042,618.00` |
| `Live` | `Long` | `1.04` | 28,010,000.00 USD | 0.00 USD | 86,610.00 USD | `-19.21%` | `82,885.00` |
| `Live` | `Long` | `1.05` | 27,920,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-18.43%` | `1,010,081.00` |
| `Live` | `Long` | `1.06` | 26,860,000.00 USD | 0.00 USD | 440,620.00 USD | `-17.66%` | `413,725.00` |
| `Live` | `Long` | `1.07` | 26,420,000.00 USD | 0.00 USD | 437,520.00 USD | `-16.89%` | `406,994.00` |
| `Live` | `Long` | `1.08` | 25,980,000.00 USD | 0.00 USD | 770,430.00 USD | `-16.11%` | `710,074.00` |
| `Live` | `Long` | `1.09` | 25,210,000.00 USD | 0.00 USD | 91,580.00 USD | `-15.34%` | `83,635.00` |
| `Live` | `Long` | `1.10` | 25,120,000.00 USD | 0.00 USD | 66,790.00 USD | `-14.57%` | `60,440.00` |
| `Live` | `Long` | `1.11` | 25,050,000.00 USD | 0.00 USD | 586,790.00 USD | `-13.79%` | `526,268.00` |
| `Live` | `Long` | `1.12` | 24,460,000.00 USD | 0.00 USD | 298,010.00 USD | `-13.02%` | `264,894.00` |
| `Live` | `Long` | `1.14` | 24,170,000.00 USD | 0.00 USD | 384,090.00 USD | `-12.25%` | `338,401.00` |
| `Live` | `Long` | `1.15` | 23,780,000.00 USD | 0.00 USD | 280,600.00 USD | `-11.47%` | `245,065.00` |
| `Live` | `Long` | `1.16` | 23,500,000.00 USD | 0.00 USD | 116,500.00 USD | `-10.70%` | `100,864.00` |
| `Live` | `Long` | `1.17` | 23,390,000.00 USD | 0.00 USD | 1,600,000.00 USD | `-9.93%` | `1,369,879.00` |
| `Live` | `Long` | `1.18` | 21,790,000.00 USD | 0.00 USD | 925,770.00 USD | `-9.15%` | `787,886.00` |
| `Live` | `Long` | `1.19` | 20,860,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-8.38%` | `1,452,858.00` |
| `Live` | `Long` | `1.20` | 19,140,000.00 USD | 0.00 USD | 496,770.00 USD | `-7.61%` | `415,704.00` |
| `Live` | `Long` | `1.21` | 18,650,000.00 USD | 0.00 USD | 664,010.00 USD | `-6.83%` | `551,048.00` |
| `Live` | `Long` | `1.22` | 17,980,000.00 USD | 0.00 USD | 366,920.00 USD | `-6.06%` | `301,994.00` |
| `Live` | `Long` | `1.23` | 17,610,000.00 USD | 0.00 USD | 1,440,000.00 USD | `-5.29%` | `1,177,773.00` |
| `Live` | `Long` | `1.24` | 16,170,000.00 USD | 0.00 USD | 692,280.00 USD | `-4.52%` | `560,547.00` |
| `Live` | `Long` | `1.25` | 15,480,000.00 USD | 0.00 USD | 250,530.00 USD | `-3.74%` | `201,228.00` |
| `Live` | `Long` | `1.25` | 15,230,000.00 USD | 0.00 USD | 14,240,000.00 USD | `-2.97%` | `11,350,516.00` |
| `Live` | `Long` | `1.26` | 983,680.00 USD | 0.00 USD | 431,470.00 USD | `-2.20%` | `341,083.00` |
| `Live` | `Long` | `1.27` | 552,210.00 USD | 0.00 USD | 432,580.00 USD | `-1.42%` | `339,277.00` |
| `Live` | `Long` | `1.28` | 119,630.00 USD | 0.00 USD | 119,630.00 USD | `-0.65%` | `93,101.00` |
| `Live` | `Short` | `1.29` | 12,650.00 USD | 12,650.00 USD | 0.00 USD | `+0.12%` | `9,768.00` |
| `Live` | `Short` | `1.30` | 15,210.00 USD | 2,560.00 USD | 0.00 USD | `+0.90%` | `1,962.00` |
| `Live` | `Short` | `1.31` | 15,480.00 USD | 269.57 USD | 0.00 USD | `+1.67%` | `205.00` |
| `Live` | `Short` | `1.32` | 117,420.00 USD | 101,940.00 USD | 0.00 USD | `+2.44%` | `76,937.00` |
| `Live` | `Short` | `1.33` | 176,010.00 USD | 58,590.00 USD | 0.00 USD | `+3.22%` | `43,886.00` |
| `Live` | `Short` | `1.34` | 341,010.00 USD | 165,000.00 USD | 0.00 USD | `+3.99%` | `122,674.00` |
| `Live` | `Short` | `1.35` | 345,000.00 USD | 3,990.00 USD | 0.00 USD | `+4.76%` | `2,947.00` |
| `Live` | `Short` | `1.36` | 546,820.00 USD | 201,820.00 USD | 0.00 USD | `+5.54%` | `147,857.00` |
| `Live` | `Short` | `1.39` | 578,470.00 USD | 31,650.00 USD | 0.00 USD | `+7.08%` | `22,851.00` |
| `Live` | `Short` | `1.40` | 590,430.00 USD | 11,960.00 USD | 0.00 USD | `+7.86%` | `8,570.00` |
| `Live` | `Short` | `1.41` | 593,040.00 USD | 2,610.00 USD | 0.00 USD | `+8.63%` | `1,859.00` |
| `Live` | `Short` | `1.42` | 596,900.00 USD | 3,860.00 USD | 0.00 USD | `+9.40%` | `2,727.00` |
| `Live` | `Short` | `1.43` | 693,120.00 USD | 96,220.00 USD | 0.00 USD | `+10.17%` | `67,525.00` |
| `Live` | `Short` | `1.44` | 725,900.00 USD | 32,780.00 USD | 0.00 USD | `+10.95%` | `22,845.00` |
| `Live` | `Short` | `1.45` | 868,920.00 USD | 143,010.00 USD | 0.00 USD | `+11.72%` | `98,972.00` |
| `Live` | `Short` | `1.46` | 883,390.00 USD | 14,470.00 USD | 0.00 USD | `+12.49%` | `9,945.00` |
| `Live` | `Short` | `1.47` | 913,640.00 USD | 30,250.00 USD | 0.00 USD | `+13.27%` | `20,647.00` |
| `Live` | `Short` | `1.48` | 924,340.00 USD | 10,700.00 USD | 0.00 USD | `+14.04%` | `7,254.00` |
| `Live` | `Short` | `1.49` | 1,270,000.00 USD | 343,310.00 USD | 0.00 USD | `+14.81%` | `231,184.00` |
| `Live` | `Short` | `1.50` | 1,280,000.00 USD | 11,950.00 USD | 0.00 USD | `+15.59%` | `7,994.00` |
| `Live` | `Short` | `1.50` | 1,330,000.00 USD | 48,310.00 USD | 0.00 USD | `+16.36%` | `32,099.00` |
| `Live` | `Short` | `1.51` | 1,330,000.00 USD | 1,940.00 USD | 0.00 USD | `+17.13%` | `1,280.00` |
| `Live` | `Short` | `1.52` | 1,330,000.00 USD | 234.85 USD | 0.00 USD | `+17.91%` | `154.00` |
| `Live` | `Short` | `1.53` | 1,330,000.00 USD | 1,010.00 USD | 0.00 USD | `+18.68%` | `658.00` |
| `Live` | `Short` | `1.54` | 1,340,000.00 USD | 5,550.00 USD | 0.00 USD | `+19.45%` | `3,594.00` |
| `Live` | `Short` | `1.55` | 1,340,000.00 USD | 1,360.00 USD | 0.00 USD | `+20.23%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,340,000.00 USD | 555.57 USD | 0.00 USD | `+21.00%` | `355.00` |
| `Live` | `Short` | `1.57` | 1,340,000.00 USD | 2,840.00 USD | 0.00 USD | `+21.77%` | `1,800.00` |
| `Live` | `Short` | `1.58` | 1,350,000.00 USD | 8,350.00 USD | 0.00 USD | `+22.55%` | `5,267.00` |
| `Live` | `Short` | `1.60` | 6,650,000.00 USD | 5,300,000.00 USD | 0.00 USD | `+24.09%` | `3,302,753.00` |
| `Live` | `Short` | `1.61` | 6,650,000.00 USD | 2,520.00 USD | 0.00 USD | `+24.86%` | `1,562.00` |
| `Live` | `Short` | `1.62` | 6,650,000.00 USD | 1,420.00 USD | 0.00 USD | `+25.64%` | `872.00` |
| `Live` | `Short` | `1.64` | 11,610,000.00 USD | 4,960,000.00 USD | 0.00 USD | `+26.41%` | `3,032,003.00` |
| `Live` | `Short` | `1.66` | 11,750,000.00 USD | 134,550.00 USD | 0.00 USD | `+27.96%` | `81,299.00` |
| `Live` | `Short` | `1.67` | 12,080,000.00 USD | 333,590.00 USD | 0.00 USD | `+28.73%` | `200,352.00` |
| `Live` | `Short` | `1.68` | 12,090,000.00 USD | 5,920.00 USD | 0.00 USD | `+29.50%` | `3,532.00` |
| `Live` | `Short` | `1.69` | 12,090,000.00 USD | 8,640.00 USD | 0.00 USD | `+30.28%` | `5,127.00` |
| `Live` | `Short` | `1.70` | 12,110,000.00 USD | 10,670.00 USD | 0.00 USD | `+31.05%` | `6,296.00` |
| `Live` | `Short` | `1.71` | 12,110,000.00 USD | 1,980.00 USD | 0.00 USD | `+31.82%` | `1,163.00` |
| `Live` | `Short` | `1.72` | 12,110,000.00 USD | 792.33 USD | 0.00 USD | `+32.60%` | `462.00` |
| `Live` | `Short` | `1.73` | 12,110,000.00 USD | 1,690.00 USD | 0.00 USD | `+33.37%` | `977.00` |
| `Live` | `Short` | `1.74` | 12,110,000.00 USD | 2,970.00 USD | 0.00 USD | `+34.14%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 12,120,000.00 USD | 3,940.00 USD | 0.00 USD | `+34.92%` | `2,256.00` |
| `Live` | `Short` | `1.75` | 12,120,000.00 USD | 286.06 USD | 0.00 USD | `+35.69%` | `163.00` |
| `Live` | `Short` | `1.76` | 12,120,000.00 USD | 2,540.00 USD | 0.00 USD | `+36.46%` | `1,440.00` |
| `Live` | `Short` | `1.77` | 12,120,000.00 USD | 1,140.00 USD | 0.00 USD | `+37.24%` | `642.00` |
| `Live` | `Short` | `1.78` | 12,250,000.00 USD | 129,650.00 USD | 0.00 USD | `+38.01%` | `72,634.00` |
| `Live` | `Short` | `1.79` | 12,250,000.00 USD | 2,850.00 USD | 0.00 USD | `+38.78%` | `1,590.00` |
| `Live` | `Short` | `1.80` | 12,260,000.00 USD | 2,960.00 USD | 0.00 USD | `+39.55%` | `1,641.00` |
| `Live` | `Short` | `1.82` | 12,260,000.00 USD | 1,650.00 USD | 0.00 USD | `+41.10%` | `905.00` |
| `Live` | `Short` | `1.83` | 15,090,000.00 USD | 2,830,000.00 USD | 0.00 USD | `+41.87%` | `1,540,766.00` |
| `Live` | `Short` | `1.84` | 15,090,000.00 USD | 6,300.00 USD | 0.00 USD | `+42.65%` | `3,415.00` |
| `Live` | `Short` | `1.85` | 15,090,000.00 USD | 1,860.00 USD | 0.00 USD | `+43.42%` | `1,002.00` |
| `Live` | `Short` | `1.86` | 15,340,000.00 USD | 245,090.00 USD | 0.00 USD | `+44.19%` | `131,415.00` |
| `Live` | `Short` | `1.89` | 15,340,000.00 USD | 640.90 USD | 0.00 USD | `+45.74%` | `340.00` |
| `Live` | `Short` | `1.90` | 15,340,000.00 USD | 4,190.00 USD | 0.00 USD | `+46.51%` | `2,211.00` |
| `Live` | `Short` | `1.91` | 15,340,000.00 USD | 373.38 USD | 0.00 USD | `+47.29%` | `196.00` |
| `Live` | `Short` | `1.93` | 15,340,000.00 USD | 103.95 USD | 0.00 USD | `+48.83%` | `54.00` |
| `Live` | `Short` | `1.94` | 15,460,000.00 USD | 113,350.00 USD | 0.00 USD | `+49.61%` | `58,578.00` |
| `Live` | `Short` | `1.96` | 15,460,000.00 USD | 582.59 USD | 0.00 USD | `+51.15%` | `298.00` |
| `Live` | `Short` | `1.97` | 15,690,000.00 USD | 227,680.00 USD | 0.00 USD | `+51.93%` | `115,869.00` |
| `Live` | `Short` | `1.98` | 15,690,000.00 USD | 651.75 USD | 0.00 USD | `+52.70%` | `330.00` |
| `Live` | `Short` | `1.99` | 15,690,000.00 USD | 1,760.00 USD | 0.00 USD | `+53.47%` | `889.00` |
| `Live` | `Short` | `2.00` | 16,010,000.00 USD | 322,160.00 USD | 0.00 USD | `+55.02%` | `160,677.00` |
| `Live` | `Short` | `2.02` | 16,010,000.00 USD | 2,100.00 USD | 0.00 USD | `+55.79%` | `1,044.00` |
| `Live` | `Short` | `2.04` | 16,010,000.00 USD | 198.36 USD | 0.00 USD | `+58.11%` | `97.00` |
| `Live` | `Short` | `2.06` | 16,290,000.00 USD | 280,760.00 USD | 0.00 USD | `+58.88%` | `136,625.00` |
| `Live` | `Short` | `2.06` | 16,300,000.00 USD | 6,600.00 USD | 0.00 USD | `+59.66%` | `3,198.00` |
| `Live` | `Short` | `2.10` | 16,300,000.00 USD | 331.01 USD | 0.00 USD | `+61.98%` | `158.00` |
| `Live` | `Short` | `2.10` | 16,300,000.00 USD | 2,520.00 USD | 0.00 USD | `+62.75%` | `1,196.00` |
| `Live` | `Short` | `2.12` | 16,480,000.00 USD | 178,520.00 USD | 0.00 USD | `+63.52%` | `84,408.00` |
| `Live` | `Short` | `2.15` | 16,480,000.00 USD | 196.11 USD | 0.00 USD | `+66.62%` | `91.00` |
| `Live` | `Short` | `2.17` | 19,810,000.00 USD | 3,330,000.00 USD | 0.00 USD | `+68.16%` | `1,530,668.00` |
| `Live` | `Short` | `2.19` | 19,810,000.00 USD | 703.57 USD | 0.00 USD | `+68.93%` | `322.00` |
| `Live` | `Short` | `2.19` | 19,810,000.00 USD | 403.88 USD | 0.00 USD | `+69.71%` | `184.00` |
| `Live` | `Short` | `2.21` | 19,820,000.00 USD | 8,920.00 USD | 0.00 USD | `+70.48%` | `4,046.00` |
| `Live` | `Short` | `2.23` | 19,820,000.00 USD | 3,890.00 USD | 0.00 USD | `+72.03%` | `1,748.00` |
| `Live` | `Short` | `2.23` | 19,890,000.00 USD | 64,350.00 USD | 0.00 USD | `+72.80%` | `28,791.00` |
| `Live` | `Short` | `2.25` | 22,180,000.00 USD | 2,290,000.00 USD | 0.00 USD | `+73.57%` | `1,020,659.00` |
| `Live` | `Short` | `2.25` | 22,240,000.00 USD | 63,810.00 USD | 0.00 USD | `+74.35%` | `28,297.00` |
| `Live` | `Short` | `2.27` | 22,240,000.00 USD | 104.19 USD | 0.00 USD | `+75.12%` | `46.00` |
| `Live` | `Short` | `2.27` | 22,260,000.00 USD | 14,930.00 USD | 0.00 USD | `+75.89%` | `6,561.00` |
| `Live` | `Short` | `2.29` | 22,260,000.00 USD | 1,530.00 USD | 0.00 USD | `+77.44%` | `665.00` |
| `Live` | `Short` | `2.31` | 22,270,000.00 USD | 5,230.00 USD | 0.00 USD | `+78.21%` | `2,271.00` |
| `Live` | `Short` | `2.33` | 22,360,000.00 USD | 92,080.00 USD | 0.00 USD | `+79.76%` | `39,606.00` |
| `Live` | `Short` | `2.33` | 22,360,000.00 USD | 938.67 USD | 0.00 USD | `+80.53%` | `402.00` |
| `Live` | `Short` | `2.35` | 23,300,000.00 USD | 939,560.00 USD | 0.00 USD | `+81.31%` | `400,666.00` |
| `Live` | `Short` | `2.38` | 23,300,000.00 USD | 109.25 USD | 0.00 USD | `+83.62%` | `46.00` |
| `Live` | `Short` | `2.38` | 23,480,000.00 USD | 179,790.00 USD | 0.00 USD | `+84.40%` | `75,385.00` |
| `Live` | `Short` | `2.40` | 23,640,000.00 USD | 165,190.00 USD | 0.00 USD | `+85.17%` | `68,972.00` |
| `Live` | `Short` | `2.40` | 23,640,000.00 USD | 110.63 USD | 0.00 USD | `+85.94%` | `46.00` |
| `Live` | `Short` | `2.42` | 23,650,000.00 USD | 2,420.00 USD | 0.00 USD | `+86.72%` | `1,000.00` |
| `Live` | `Short` | `2.42` | 23,650,000.00 USD | 169.75 USD | 0.00 USD | `+87.49%` | `70.00` |
| `Live` | `Short` | `2.44` | 23,650,000.00 USD | 309.25 USD | 0.00 USD | `+88.26%` | `127.00` |
| `Live` | `Short` | `2.44` | 23,670,000.00 USD | 24,720.00 USD | 0.00 USD | `+89.04%` | `10,111.00` |
| `Live` | `Short` | `2.46` | 23,680,000.00 USD | 4,190.00 USD | 0.00 USD | `+90.58%` | `1,698.00` |
| `Live` | `Short` | `2.48` | 23,680,000.00 USD | 4,890.00 USD | 0.00 USD | `+92.13%` | `1,966.00` |
| `Live` | `Short` | `2.52` | 23,690,000.00 USD | 5,640.00 USD | 0.00 USD | `+94.45%` | `2,244.00` |
| `Live` | `Short` | `2.52` | 23,730,000.00 USD | 42,820.00 USD | 0.00 USD | `+95.22%` | `16,960.00` |
| `Live` | `Short` | `2.54` | 23,730,000.00 USD | 496.86 USD | 0.00 USD | `+96.00%` | `196.00` |
| `Live` | `Short` | `2.56` | 23,740,000.00 USD | 11,400.00 USD | 0.00 USD | `+97.54%` | `4,460.00` |
| `Live` | `Short` | `2.56` | 23,740,000.00 USD | 187.25 USD | 0.00 USD | `+98.31%` | `73.00` |
| `Live` | `Short` | `2.58` | 23,740,000.00 USD | 2,250.00 USD | 0.00 USD | `+99.09%` | `875.00` |
| `Live` | `Short` | `2.58` | 23,740,000.00 USD | 380.00 USD | 0.00 USD | `+99.86%` | `147.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3050` | 67,390,000.00 USD | 0.00 USD | 147.62 USD | `-76.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3250` | 67,390,000.00 USD | 0.00 USD | 145.28 USD | `-74.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 67,390,000.00 USD | 0.00 USD | 139.12 USD | `-71.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 67,390,000.00 USD | 0.00 USD | 200.86 USD | `-67.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4250` | 67,390,000.00 USD | 0.00 USD | 173.82 USD | `-67.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 67,390,000.00 USD | 0.00 USD | 408.51 USD | `-65.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 67,390,000.00 USD | 0.00 USD | 520.52 USD | `-64.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 67,390,000.00 USD | 0.00 USD | 151.12 USD | `-64.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 67,390,000.00 USD | 0.00 USD | 190.00 USD | `-63.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 67,390,000.00 USD | 0.00 USD | 145.50 USD | `-62.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 67,390,000.00 USD | 0.00 USD | 1,030.00 USD | `-60.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 67,390,000.00 USD | 0.00 USD | 306.60 USD | `-59.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 67,390,000.00 USD | 0.00 USD | 6,750.00 USD | `-57.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 67,380,000.00 USD | 0.00 USD | 374.60 USD | `-56.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 67,380,000.00 USD | 0.00 USD | 100.62 USD | `-54.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 67,380,000.00 USD | 0.00 USD | 791.85 USD | `-50.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 67,380,000.00 USD | 0.00 USD | 573.40 USD | `-50.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 67,380,000.00 USD | 0.00 USD | 3,450.00 USD | `-49.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 67,380,000.00 USD | 0.00 USD | 3,010.00 USD | `-48.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 67,370,000.00 USD | 0.00 USD | 1,060.00 USD | `-46.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 67,370,000.00 USD | 0.00 USD | 1,590.00 USD | `-45.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 67,370,000.00 USD | 0.00 USD | 1,300.00 USD | `-41.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 67,370,000.00 USD | 0.00 USD | 2,880.00 USD | `-40.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 67,370,000.00 USD | 0.00 USD | 1,110.00 USD | `-38.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 67,370,000.00 USD | 0.00 USD | 798.57 USD | `-33.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 67,370,000.00 USD | 0.00 USD | 690.38 USD | `-32.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 67,370,000.00 USD | 0.00 USD | 1,420.00 USD | `-31.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 67,360,000.00 USD | 0.00 USD | 1,910.00 USD | `-30.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 67,360,000.00 USD | 0.00 USD | 838.94 USD | `-30.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 67,360,000.00 USD | 0.00 USD | 188.49 USD | `-29.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 67,360,000.00 USD | 0.00 USD | 2,730.00 USD | `-28.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 67,360,000.00 USD | 0.00 USD | 1,150.00 USD | `-27.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 67,360,000.00 USD | 0.00 USD | 112.46 USD | `-26.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 67,360,000.00 USD | 0.00 USD | 2,360.00 USD | `-26.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 67,350,000.00 USD | 0.00 USD | 3,910.00 USD | `-25.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 67,350,000.00 USD | 0.00 USD | 546,370.00 USD | `-24.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 66,800,000.00 USD | 0.00 USD | 5,250.00 USD | `-23.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 66,800,000.00 USD | 0.00 USD | 897.49 USD | `-23.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 66,800,000.00 USD | 0.00 USD | 15,070.00 USD | `-22.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 66,780,000.00 USD | 0.00 USD | 4,330.00 USD | `-21.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 66,780,000.00 USD | 0.00 USD | 2,020.00 USD | `-20.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 66,780,000.00 USD | 0.00 USD | 38,000.00 USD | `-19.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 66,740,000.00 USD | 0.00 USD | 3,970.00 USD | `-19.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 66,730,000.00 USD | 0.00 USD | 7,090.00 USD | `-18.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 66,730,000.00 USD | 0.00 USD | 3,230.00 USD | `-17.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 66,720,000.00 USD | 0.00 USD | 34,770.00 USD | `-16.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 66,690,000.00 USD | 0.00 USD | 973.25 USD | `-16.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 66,690,000.00 USD | 0.00 USD | 8,250.00 USD | `-15.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 66,680,000.00 USD | 0.00 USD | 2,970.00 USD | `-14.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 66,680,000.00 USD | 0.00 USD | 9,300.00 USD | `-13.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 66,670,000.00 USD | 0.00 USD | 77,120.00 USD | `-13.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 66,590,000.00 USD | 0.00 USD | 12,910.00 USD | `-12.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 66,580,000.00 USD | 0.00 USD | 35,220.00 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 66,540,000.00 USD | 0.00 USD | 5,360.00 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 66,540,000.00 USD | 0.00 USD | 14,080.00 USD | `-9.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 66,520,000.00 USD | 0.00 USD | 4,790.00 USD | `-9.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 66,520,000.00 USD | 0.00 USD | 90,010.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 66,430,000.00 USD | 0.00 USD | 12,570.00 USD | `-7.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 66,420,000.00 USD | 0.00 USD | 57,020.00 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 66,360,000.00 USD | 0.00 USD | 57,160.00 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 66,300,000.00 USD | 0.00 USD | 144,860.00 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 66,160,000.00 USD | 0.00 USD | 398,990.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 65,760,000.00 USD | 0.00 USD | 258,780.00 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 65,500,000.00 USD | 0.00 USD | 480,130.00 USD | `-2.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.26` | 65,020,000.00 USD | 0.00 USD | 134,550.00 USD | `-2.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.27` | 64,880,000.00 USD | 0.00 USD | 360,930.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.28` | 64,520,000.00 USD | 0.00 USD | 64,520,000.00 USD | `-0.65%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `1.29` | 129,630,000.00 USD | 129,630,000.00 USD | 0.00 USD | `+0.12%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `1.30` | 129,640,000.00 USD | 2,670.00 USD | 0.00 USD | `+0.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 129,700,000.00 USD | 66,700.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 129,990,000.00 USD | 283,070.00 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 130,100,000.00 USD | 110,440.00 USD | 0.00 USD | `+3.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 130,270,000.00 USD | 172,830.00 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 130,300,000.00 USD | 28,410.00 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 130,600,000.00 USD | 300,090.00 USD | 0.00 USD | `+5.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 130,670,000.00 USD | 73,650.00 USD | 0.00 USD | `+6.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 130,740,000.00 USD | 71,640.00 USD | 0.00 USD | `+7.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 130,820,000.00 USD | 81,740.00 USD | 0.00 USD | `+7.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 135,200,000.00 USD | 4,370,000.00 USD | 0.00 USD | `+8.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 135,230,000.00 USD | 31,160.00 USD | 0.00 USD | `+9.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 135,250,000.00 USD | 19,800.00 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 135,330,000.00 USD | 82,400.00 USD | 0.00 USD | `+10.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 135,590,000.00 USD | 260,610.00 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 135,640,000.00 USD | 44,870.00 USD | 0.00 USD | `+12.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 135,660,000.00 USD | 27,080.00 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 135,770,000.00 USD | 108,480.00 USD | 0.00 USD | `+14.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 135,860,000.00 USD | 84,290.00 USD | 0.00 USD | `+14.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 135,870,000.00 USD | 15,160.00 USD | 0.00 USD | `+15.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 135,960,000.00 USD | 84,680.00 USD | 0.00 USD | `+16.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 135,980,000.00 USD | 18,210.00 USD | 0.00 USD | `+17.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 136,010,000.00 USD | 32,440.00 USD | 0.00 USD | `+17.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 136,070,000.00 USD | 57,450.00 USD | 0.00 USD | `+18.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 136,100,000.00 USD | 36,160.00 USD | 0.00 USD | `+19.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 136,110,000.00 USD | 6,110.00 USD | 0.00 USD | `+20.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 136,110,000.00 USD | 6,300.00 USD | 0.00 USD | `+21.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 136,120,000.00 USD | 6,410.00 USD | 0.00 USD | `+21.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 136,130,000.00 USD | 9,700.00 USD | 0.00 USD | `+22.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 136,260,000.00 USD | 126,740.00 USD | 0.00 USD | `+23.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 136,260,000.00 USD | 1,130.00 USD | 0.00 USD | `+24.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 136,340,000.00 USD | 83,090.00 USD | 0.00 USD | `+24.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 136,340,000.00 USD | 464.75 USD | 0.00 USD | `+25.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 136,540,000.00 USD | 199,230.00 USD | 0.00 USD | `+26.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 136,540,000.00 USD | 3,970.00 USD | 0.00 USD | `+27.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 136,580,000.00 USD | 33,550.00 USD | 0.00 USD | `+27.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 136,590,000.00 USD | 8,220.00 USD | 0.00 USD | `+28.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 136,590,000.00 USD | 5,760.00 USD | 0.00 USD | `+29.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 136,660,000.00 USD | 70,850.00 USD | 0.00 USD | `+30.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 136,670,000.00 USD | 8,570.00 USD | 0.00 USD | `+31.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 136,930,000.00 USD | 259,410.00 USD | 0.00 USD | `+31.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 136,940,000.00 USD | 14,030.00 USD | 0.00 USD | `+32.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 136,960,000.00 USD | 14,560.00 USD | 0.00 USD | `+33.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 137,000,000.00 USD | 44,100.00 USD | 0.00 USD | `+34.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 137,010,000.00 USD | 4,710.00 USD | 0.00 USD | `+34.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 137,010,000.00 USD | 6,330.00 USD | 0.00 USD | `+35.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 137,040,000.00 USD | 21,720.00 USD | 0.00 USD | `+36.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 137,160,000.00 USD | 122,200.00 USD | 0.00 USD | `+37.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 137,260,000.00 USD | 96,900.00 USD | 0.00 USD | `+38.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 137,290,000.00 USD | 33,690.00 USD | 0.00 USD | `+38.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 137,290,000.00 USD | 254.51 USD | 0.00 USD | `+39.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 137,290,000.00 USD | 2,530.00 USD | 0.00 USD | `+40.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 137,290,000.00 USD | 1,830.00 USD | 0.00 USD | `+41.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 137,300,000.00 USD | 7,630.00 USD | 0.00 USD | `+41.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 137,310,000.00 USD | 5,700.00 USD | 0.00 USD | `+42.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 137,320,000.00 USD | 8,390.00 USD | 0.00 USD | `+43.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 137,320,000.00 USD | 4,550.00 USD | 0.00 USD | `+44.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 137,320,000.00 USD | 591.89 USD | 0.00 USD | `+45.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 137,360,000.00 USD | 44,350.00 USD | 0.00 USD | `+46.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 137,370,000.00 USD | 10,020.00 USD | 0.00 USD | `+47.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 137,380,000.00 USD | 7,410.00 USD | 0.00 USD | `+48.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 137,380,000.00 USD | 265.10 USD | 0.00 USD | `+49.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 137,380,000.00 USD | 2,040.00 USD | 0.00 USD | `+50.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 137,390,000.00 USD | 1,510.00 USD | 0.00 USD | `+51.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 137,400,000.00 USD | 14,120.00 USD | 0.00 USD | `+51.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 137,400,000.00 USD | 4,010.00 USD | 0.00 USD | `+52.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 137,400,000.00 USD | 325.54 USD | 0.00 USD | `+53.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 137,410,000.00 USD | 7,020.00 USD | 0.00 USD | `+54.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 137,550,000.00 USD | 138,900.00 USD | 0.00 USD | `+55.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 137,550,000.00 USD | 781.82 USD | 0.00 USD | `+55.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 137,550,000.00 USD | 222.75 USD | 0.00 USD | `+56.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 137,550,000.00 USD | 862.84 USD | 0.00 USD | `+57.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 137,560,000.00 USD | 3,490.00 USD | 0.00 USD | `+58.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 137,560,000.00 USD | 3,940.00 USD | 0.00 USD | `+59.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 137,560,000.00 USD | 661.93 USD | 0.00 USD | `+60.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 137,680,000.00 USD | 124,400.00 USD | 0.00 USD | `+61.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 137,690,000.00 USD | 1,580.00 USD | 0.00 USD | `+62.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 137,700,000.00 USD | 13,900.00 USD | 0.00 USD | `+64.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 137,730,000.00 USD | 24,840.00 USD | 0.00 USD | `+65.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 137,780,000.00 USD | 50,580.00 USD | 0.00 USD | `+66.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 137,780,000.00 USD | 1,710.00 USD | 0.00 USD | `+67.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 137,780,000.00 USD | 1,970.00 USD | 0.00 USD | `+69.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 137,930,000.00 USD | 151,380.00 USD | 0.00 USD | `+71.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 137,940,000.00 USD | 7,340.00 USD | 0.00 USD | `+72.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 137,940,000.00 USD | 3,120.00 USD | 0.00 USD | `+75.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 137,940,000.00 USD | 1,140.00 USD | 0.00 USD | `+76.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 137,950,000.00 USD | 12,150.00 USD | 0.00 USD | `+77.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 137,950,000.00 USD | 370.40 USD | 0.00 USD | `+78.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 138,000,000.00 USD | 47,430.00 USD | 0.00 USD | `+80.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 138,000,000.00 USD | 2,410.00 USD | 0.00 USD | `+82.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 138,010,000.00 USD | 475.00 USD | 0.00 USD | `+83.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 138,010,000.00 USD | 2,540.00 USD | 0.00 USD | `+85.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 138,260,000.00 USD | 251,200.00 USD | 0.00 USD | `+85.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 138,260,000.00 USD | 1,370.00 USD | 0.00 USD | `+86.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 138,260,000.00 USD | 564.92 USD | 0.00 USD | `+88.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 138,270,000.00 USD | 8,110.00 USD | 0.00 USD | `+89.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 138,270,000.00 USD | 3,420.00 USD | 0.00 USD | `+92.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 138,270,000.00 USD | 124.75 USD | 0.00 USD | `+92.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 138,320,000.00 USD | 42,600.00 USD | 0.00 USD | `+93.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.52` | 138,320,000.00 USD | 378.75 USD | 0.00 USD | `+95.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.56` | 138,320,000.00 USD | 389.88 USD | 0.00 USD | `+98.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.58` | 138,320,000.00 USD | 775.50 USD | 0.00 USD | `+99.86%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.15` | 201,030,000.00 USD | 0.00 USD | 201,030,000.00 USD | 272,740.00 USD | 53,330.00 USD | 52,710.00 USD |
| `7D` | `1.15` | 200,650,000.00 USD | 0.00 USD | 200,650,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.15` | 66,270,000.00 USD | 0.00 USD | 66,270,000.00 USD | 1,390.00 USD | 149.67 USD | 64,030.00 USD |
| `7D` | `1.15` | 200,490,000.00 USD | 0.00 USD | 200,490,000.00 USD | 12,250.00 USD | 37,300.00 USD | 120,130.00 USD |
| `1D` | `1.15` | 66,200,000.00 USD | 0.00 USD | 66,200,000.00 USD | 48,490.00 USD | 414.70 USD | 112,380.00 USD |
| `7D` | `1.16` | 200,320,000.00 USD | 0.00 USD | 200,320,000.00 USD | 97,250.00 USD | 57,460.00 USD | 136,900.00 USD |
| `1D` | `1.16` | 66,040,000.00 USD | 0.00 USD | 66,040,000.00 USD | 1,740.00 USD | 158.40 USD | 28,820.00 USD |
| `7D` | `1.16` | 200,030,000.00 USD | 0.00 USD | 200,030,000.00 USD | 173,190.00 USD | 99,350.00 USD | 520,790.00 USD |
| `1D` | `1.16` | 66,010,000.00 USD | 0.00 USD | 66,010,000.00 USD | 66,460.00 USD | 27,280.00 USD | 27,240.00 USD |
| `7D` | `1.16` | 199,230,000.00 USD | 0.00 USD | 199,230,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD |
| `1D` | `1.16` | 65,890,000.00 USD | 0.00 USD | 65,890,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.16` | 198,800,000.00 USD | 0.00 USD | 198,800,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.16` | 65,510,000.00 USD | 0.00 USD | 65,510,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.16` | 197,780,000.00 USD | 0.00 USD | 197,780,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.16` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.17` | 196,400,000.00 USD | 0.00 USD | 196,400,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.17` | 64,340,000.00 USD | 0.00 USD | 64,340,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD |
| `7D` | `1.17` | 195,780,000.00 USD | 0.00 USD | 195,780,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD |
| `1D` | `1.17` | 64,010,000.00 USD | 0.00 USD | 64,010,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.17` | 194,400,000.00 USD | 0.00 USD | 194,400,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 63,830,000.00 USD | 0.00 USD | 63,830,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.17` | 192,890,000.00 USD | 0.00 USD | 192,890,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 63,670,000.00 USD | 0.00 USD | 63,670,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.17` | 191,500,000.00 USD | 0.00 USD | 191,500,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.17` | 63,450,000.00 USD | 0.00 USD | 63,450,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.18` | 190,710,000.00 USD | 0.00 USD | 190,710,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD |
| `1D` | `1.18` | 63,170,000.00 USD | 0.00 USD | 63,170,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD |
| `7D` | `1.18` | 189,820,000.00 USD | 0.00 USD | 189,820,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `1D` | `1.18` | 62,950,000.00 USD | 0.00 USD | 62,950,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.18` | 189,370,000.00 USD | 0.00 USD | 189,370,000.00 USD | 299,590.00 USD | 131,210.00 USD | 405,740.00 USD |
| `1D` | `1.18` | 62,780,000.00 USD | 0.00 USD | 62,780,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.18` | 188,530,000.00 USD | 0.00 USD | 188,530,000.00 USD | 69,670.00 USD | 152,290.00 USD | 199,660.00 USD |
| `1D` | `1.18` | 62,700,000.00 USD | 0.00 USD | 62,700,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.18` | 188,110,000.00 USD | 0.00 USD | 188,110,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD |
| `1D` | `1.18` | 62,610,000.00 USD | 0.00 USD | 62,610,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD |
| `7D` | `1.19` | 187,980,000.00 USD | 0.00 USD | 187,980,000.00 USD | 81,610.00 USD | 98,170.00 USD | 428,040.00 USD |
| `1D` | `1.19` | 62,500,000.00 USD | 0.00 USD | 62,500,000.00 USD | 694.57 USD | 23,390.00 USD | 20,370.00 USD |
| `7D` | `1.19` | 187,370,000.00 USD | 0.00 USD | 187,370,000.00 USD | 190,550.00 USD | 38,510.00 USD | 383,280.00 USD |
| `1D` | `1.19` | 62,450,000.00 USD | 0.00 USD | 62,450,000.00 USD | 30,140.00 USD | 99.63 USD | 12,880.00 USD |
| `7D` | `1.19` | 186,760,000.00 USD | 0.00 USD | 186,760,000.00 USD | 186,430.00 USD | 128,180.00 USD | 350,400.00 USD |
| `1D` | `1.19` | 62,410,000.00 USD | 0.00 USD | 62,410,000.00 USD | 10,800.00 USD | 238.88 USD | 21,580.00 USD |
| `7D` | `1.19` | 186,090,000.00 USD | 0.00 USD | 186,090,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `1D` | `1.19` | 62,380,000.00 USD | 0.00 USD | 62,380,000.00 USD | 20,520.00 USD | 18,150.00 USD | 56,850.00 USD |
| `7D` | `1.19` | 185,630,000.00 USD | 0.00 USD | 185,630,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD |
| `1D` | `1.19` | 62,280,000.00 USD | 0.00 USD | 62,280,000.00 USD | 130,470.00 USD | 44,250.00 USD | 112,000.00 USD |
| `7D` | `1.20` | 184,970,000.00 USD | 0.00 USD | 184,970,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 62,000,000.00 USD | 0.00 USD | 62,000,000.00 USD | 64,240.00 USD | 18,340.00 USD | 29,820.00 USD |
| `7D` | `1.20` | 184,260,000.00 USD | 0.00 USD | 184,260,000.00 USD | 5,350.00 USD | 93,870.00 USD | 187,830.00 USD |
| `1D` | `1.20` | 61,880,000.00 USD | 0.00 USD | 61,880,000.00 USD | 112,660.00 USD | 7,010.00 USD | 10,750.00 USD |
| `7D` | `1.20` | 183,970,000.00 USD | 0.00 USD | 183,970,000.00 USD | 67,200.00 USD | 57,670.00 USD | 21,970.00 USD |
| `1D` | `1.20` | 61,750,000.00 USD | 0.00 USD | 61,750,000.00 USD | 26,800.00 USD | 20,630.00 USD | 1,060.00 USD |
| `7D` | `1.20` | 183,830,000.00 USD | 0.00 USD | 183,830,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD |
| `1D` | `1.20` | 61,710,000.00 USD | 0.00 USD | 61,710,000.00 USD | 55,140.00 USD | 14,180.00 USD | 61,870.00 USD |
| `7D` | `1.20` | 183,750,000.00 USD | 0.00 USD | 183,750,000.00 USD | 202,570.00 USD | 53,170.00 USD | 48,290.00 USD |
| `7D` | `1.21` | 183,450,000.00 USD | 0.00 USD | 183,450,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 61,570,000.00 USD | 0.00 USD | 61,570,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD |
| `7D` | `1.21` | 183,350,000.00 USD | 0.00 USD | 183,350,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD |
| `1D` | `1.21` | 61,560,000.00 USD | 0.00 USD | 61,560,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `1.21` | 183,260,000.00 USD | 0.00 USD | 183,260,000.00 USD | 361,660.00 USD | 45,260.00 USD | 357,420.00 USD |
| `7D` | `1.21` | 182,490,000.00 USD | 0.00 USD | 182,490,000.00 USD | 70,670.00 USD | 152,900.00 USD | 457,650.00 USD |
| `7D` | `1.21` | 181,810,000.00 USD | 0.00 USD | 181,810,000.00 USD | 278,240.00 USD | 50,420.00 USD | 33,960.00 USD |
| `7D` | `1.22` | 181,450,000.00 USD | 0.00 USD | 181,450,000.00 USD | 5,680.00 USD | 39,860.00 USD | 0.00 USD |
| `7D` | `1.22` | 181,400,000.00 USD | 0.00 USD | 181,400,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.22` | 181,310,000.00 USD | 0.00 USD | 181,310,000.00 USD | 0.00 USD | 765.15 USD | 40,620.00 USD |
| `7D` | `1.22` | 181,260,000.00 USD | 0.00 USD | 181,260,000.00 USD | 54,470.00 USD | 2,490.00 USD | 14,710.00 USD |
| `7D` | `1.22` | 181,190,000.00 USD | 0.00 USD | 181,190,000.00 USD | 10,460.00 USD | 191,360.00 USD | 207,400.00 USD |
| `7D` | `1.23` | 180,780,000.00 USD | 0.00 USD | 180,780,000.00 USD | 649,620.00 USD | 191,250.00 USD | 200,510.00 USD |
| `7D` | `1.23` | 179,740,000.00 USD | 0.00 USD | 179,740,000.00 USD | 341,300.00 USD | 128,580.00 USD | 60,930.00 USD |
| `1D` | `1.23` | 61,530,000.00 USD | 0.00 USD | 61,530,000.00 USD | 48,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.23` | 179,210,000.00 USD | 0.00 USD | 179,210,000.00 USD | 44,790.00 USD | 125,700.00 USD | 371,190.00 USD |
| `1D` | `1.23` | 61,480,000.00 USD | 0.00 USD | 61,480,000.00 USD | 102,730.00 USD | 374.17 USD | 215,900.00 USD |
| `7D` | `1.23` | 178,670,000.00 USD | 0.00 USD | 178,670,000.00 USD | 257,070.00 USD | 187,490.00 USD | 678,370.00 USD |
| `1D` | `1.23` | 61,170,000.00 USD | 0.00 USD | 61,170,000.00 USD | 125,570.00 USD | 1,040.00 USD | 280,940.00 USD |
| `7D` | `1.23` | 177,550,000.00 USD | 0.00 USD | 177,550,000.00 USD | 724,190.00 USD | 142,840.00 USD | 467,410.00 USD |
| `1D` | `1.23` | 60,760,000.00 USD | 0.00 USD | 60,760,000.00 USD | 11,570.00 USD | 989.25 USD | 73,470.00 USD |
| `7D` | `1.24` | 176,210,000.00 USD | 0.00 USD | 176,210,000.00 USD | 1,150,000.00 USD | 525,690.00 USD | 2,440,000.00 USD |
| `1D` | `1.24` | 60,670,000.00 USD | 0.00 USD | 60,670,000.00 USD | 515,840.00 USD | 120,320.00 USD | 331,740.00 USD |
| `7D` | `1.24` | 172,090,000.00 USD | 0.00 USD | 172,090,000.00 USD | 1,620,000.00 USD | 912,620.00 USD | 1,860,000.00 USD |
| `1D` | `1.24` | 59,700,000.00 USD | 0.00 USD | 59,700,000.00 USD | 1,080,000.00 USD | 666,380.00 USD | 709,340.00 USD |
| `7D` | `1.24` | 167,710,000.00 USD | 0.00 USD | 167,710,000.00 USD | 1,890,000.00 USD | 972,840.00 USD | 2,250,000.00 USD |
| `1D` | `1.24` | 57,240,000.00 USD | 0.00 USD | 57,240,000.00 USD | 942,890.00 USD | 493,310.00 USD | 740,300.00 USD |
| `7D` | `1.24` | 162,590,000.00 USD | 0.00 USD | 162,590,000.00 USD | 1,980,000.00 USD | 677,720.00 USD | 2,560,000.00 USD |
| `1D` | `1.24` | 55,070,000.00 USD | 0.00 USD | 55,070,000.00 USD | 347,740.00 USD | 188,510.00 USD | 341,680.00 USD |
| `7D` | `1.24` | 157,360,000.00 USD | 0.00 USD | 157,360,000.00 USD | 982,310.00 USD | 740,000.00 USD | 1,100,000.00 USD |
| `1D` | `1.24` | 54,190,000.00 USD | 0.00 USD | 54,190,000.00 USD | 372,570.00 USD | 122,390.00 USD | 516,600.00 USD |
| `7D` | `1.25` | 154,550,000.00 USD | 0.00 USD | 154,550,000.00 USD | 2,160,000.00 USD | 376,950.00 USD | 1,810,000.00 USD |
| `1D` | `1.25` | 53,180,000.00 USD | 0.00 USD | 53,180,000.00 USD | 546,010.00 USD | 129,710.00 USD | 161,620.00 USD |
| `7D` | `1.25` | 150,200,000.00 USD | 0.00 USD | 150,200,000.00 USD | 2,120,000.00 USD | 1,190,000.00 USD | 5,300,000.00 USD |
| `1D` | `1.25` | 52,340,000.00 USD | 0.00 USD | 52,340,000.00 USD | 218,430.00 USD | 101,390.00 USD | 355,010.00 USD |
| `7D` | `1.25` | 141,580,000.00 USD | 0.00 USD | 141,580,000.00 USD | 2,280,000.00 USD | 1,370,000.00 USD | 3,470,000.00 USD |
| `1D` | `1.25` | 51,670,000.00 USD | 0.00 USD | 51,670,000.00 USD | 177,400.00 USD | 102,610.00 USD | 457,850.00 USD |
| `7D` | `1.25` | 134,460,000.00 USD | 0.00 USD | 134,460,000.00 USD | 2,810,000.00 USD | 918,840.00 USD | 2,000,000.00 USD |
| `1D` | `1.25` | 50,930,000.00 USD | 0.00 USD | 50,930,000.00 USD | 351,630.00 USD | 92,050.00 USD | 426,530.00 USD |
| `7D` | `1.25` | 128,730,000.00 USD | 0.00 USD | 128,730,000.00 USD | 1,240,000.00 USD | 673,830.00 USD | 1,480,000.00 USD |
| `1D` | `1.25` | 50,060,000.00 USD | 0.00 USD | 50,060,000.00 USD | 332,170.00 USD | 42,640.00 USD | 632,330.00 USD |
| `7D` | `1.25` | 125,330,000.00 USD | 0.00 USD | 125,330,000.00 USD | 625,270.00 USD | 468,670.00 USD | 763,070.00 USD |
| `1D` | `1.26` | 49,050,000.00 USD | 0.00 USD | 49,050,000.00 USD | 610,960.00 USD | 49,250.00 USD | 790,470.00 USD |
| `7D` | `1.26` | 123,480,000.00 USD | 0.00 USD | 123,480,000.00 USD | 413,880.00 USD | 407,350.00 USD | 993,490.00 USD |
| `1D` | `1.26` | 47,600,000.00 USD | 0.00 USD | 47,600,000.00 USD | 231,420.00 USD | 104,190.00 USD | 463,780.00 USD |
| `7D` | `1.26` | 121,660,000.00 USD | 0.00 USD | 121,660,000.00 USD | 1,190,000.00 USD | 449,360.00 USD | 1,510,000.00 USD |
| `1D` | `1.26` | 46,800,000.00 USD | 0.00 USD | 46,800,000.00 USD | 281,000.00 USD | 71,910.00 USD | 171,240.00 USD |
| `7D` | `1.26` | 118,510,000.00 USD | 0.00 USD | 118,510,000.00 USD | 1,470,000.00 USD | 1,130,000.00 USD | 852,870.00 USD |
| `1D` | `1.26` | 46,280,000.00 USD | 0.00 USD | 46,280,000.00 USD | 992,410.00 USD | 254,090.00 USD | 693,350.00 USD |
| `7D` | `1.26` | 115,060,000.00 USD | 0.00 USD | 115,060,000.00 USD | 2,860,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD |
| `1D` | `1.26` | 44,340,000.00 USD | 0.00 USD | 44,340,000.00 USD | 2,210,000.00 USD | 1,360,000.00 USD | 1,530,000.00 USD |
| `7D` | `1.26` | 108,450,000.00 USD | 0.00 USD | 108,450,000.00 USD | 3,640,000.00 USD | 1,830,000.00 USD | 4,470,000.00 USD |
| `1D` | `1.27` | 39,240,000.00 USD | 0.00 USD | 39,240,000.00 USD | 2,080,000.00 USD | 1,030,000.00 USD | 1,570,000.00 USD |
| `7D` | `1.27` | 98,510,000.00 USD | 0.00 USD | 98,510,000.00 USD | 3,940,000.00 USD | 1,630,000.00 USD | 6,430,000.00 USD |
| `1D` | `1.27` | 34,550,000.00 USD | 0.00 USD | 34,550,000.00 USD | 1,160,000.00 USD | 377,270.00 USD | 1,610,000.00 USD |
| `7D` | `1.27` | 86,510,000.00 USD | 0.00 USD | 86,510,000.00 USD | 1,990,000.00 USD | 1,500,000.00 USD | 3,710,000.00 USD |
| `1D` | `1.27` | 31,400,000.00 USD | 0.00 USD | 31,400,000.00 USD | 1,330,000.00 USD | 277,410.00 USD | 2,270,000.00 USD |
| `7D` | `1.27` | 79,320,000.00 USD | 0.00 USD | 79,320,000.00 USD | 4,070,000.00 USD | 1,680,000.00 USD | 4,080,000.00 USD |
| `1D` | `1.27` | 27,520,000.00 USD | 0.00 USD | 27,520,000.00 USD | 1,320,000.00 USD | 332,670.00 USD | 815,330.00 USD |
| `7D` | `1.27` | 69,480,000.00 USD | 0.00 USD | 69,480,000.00 USD | 4,300,000.00 USD | 3,000,000.00 USD | 10,500,000.00 USD |
| `1D` | `1.27` | 25,050,000.00 USD | 0.00 USD | 25,050,000.00 USD | 1,460,000.00 USD | 568,780.00 USD | 1,290,000.00 USD |
| `7D` | `1.27` | 51,680,000.00 USD | 0.00 USD | 51,680,000.00 USD | 3,980,000.00 USD | 1,300,000.00 USD | 7,240,000.00 USD |
| `1D` | `1.28` | 21,740,000.00 USD | 0.00 USD | 21,740,000.00 USD | 2,960,000.00 USD | 1,280,000.00 USD | 2,560,000.00 USD |
| `7D` | `1.28` | 39,160,000.00 USD | 0.00 USD | 39,160,000.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 14,930,000.00 USD | 0.00 USD | 14,930,000.00 USD | 6,210,000.00 USD | 2,740,000.00 USD | 4,520,000.00 USD |
| `7D` | `1.28` | 20,890,000.00 USD | 0.00 USD | 20,890,000.00 USD | 4,790,000.00 USD | 1,750,000.00 USD | 6,220,000.00 USD |
| `1D` | `1.28` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD |
| `7D` | `1.28` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 4,580,000.00 USD | 1,610,000.00 USD | 1,930,000.00 USD |
| `1D` | `1.28` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD |
| `1D` | `1.28` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD |
| `7D` | `1.28` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.28` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 3,390,000.00 USD | 2,130,000.00 USD | 45,690.00 USD |
| `1D` | `1.28` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 2,480,000.00 USD | 530,190.00 USD | 0.00 USD |
| `7D` | `1.28` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 3,830,000.00 USD | 1,550,000.00 USD | 116,000.00 USD |
| `1D` | `1.29` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 1,390,000.00 USD | 327,360.00 USD | 0.00 USD |
| `7D` | `1.29` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 724,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.29` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 221,930.00 USD | 100,470.00 USD | 8,840.00 USD |
| `7D` | `1.29` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 665,270.00 USD |
| `7D` | `1.29` | 14,300,000.00 USD | 14,300,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 819,130.00 USD |
| `1D` | `1.29` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 194,230.00 USD | 0.00 USD | 1,220,000.00 USD |
| `7D` | `1.29` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 301,640.00 USD |
| `1D` | `1.29` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 389,390.00 USD | 0.00 USD | 1,100,000.00 USD |
| `7D` | `1.29` | 16,650,000.00 USD | 16,650,000.00 USD | 0.00 USD | 440,550.00 USD | 0.00 USD | 1,610,000.00 USD |
| `1D` | `1.30` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 484,930.00 USD | 597,860.00 USD | 1,110,000.00 USD |
| `7D` | `1.30` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 0.00 USD | 389,370.00 USD | 0.00 USD |
| `1D` | `1.30` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 288,210.00 USD |
| `7D` | `1.30` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `1.30` | 12,710,000.00 USD | 12,710,000.00 USD | 0.00 USD | 0.00 USD | 168,250.00 USD | 0.00 USD |
| `7D` | `1.30` | 18,570,000.00 USD | 18,570,000.00 USD | 0.00 USD | 0.00 USD | 286,660.00 USD | 0.00 USD |
| `1D` | `1.30` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 521,850.00 USD | 910,560.00 USD | 278,310.00 USD |
| `7D` | `1.30` | 21,080,000.00 USD | 21,080,000.00 USD | 0.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD |
| `1D` | `1.30` | 14,830,000.00 USD | 14,830,000.00 USD | 0.00 USD | 188,510.00 USD | 98,100.00 USD | 127,330.00 USD |
| `1D` | `1.31` | 15,960,000.00 USD | 15,960,000.00 USD | 0.00 USD | 493,480.00 USD | 319,190.00 USD | 320,170.00 USD |
| `7D` | `1.31` | 23,030,000.00 USD | 23,030,000.00 USD | 0.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD |
| `1D` | `1.31` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 455,910.00 USD | 3,540.00 USD | 776,190.00 USD |
| `7D` | `1.31` | 24,270,000.00 USD | 24,270,000.00 USD | 0.00 USD | 586,970.00 USD | 0.00 USD | 649,130.00 USD |
| `1D` | `1.31` | 19,040,000.00 USD | 19,040,000.00 USD | 0.00 USD | 616,030.00 USD | 287,750.00 USD | 940,430.00 USD |
| `7D` | `1.31` | 27,260,000.00 USD | 27,260,000.00 USD | 0.00 USD | 704,520.00 USD | 318,670.00 USD | 1,970,000.00 USD |
| `1D` | `1.31` | 21,740,000.00 USD | 21,740,000.00 USD | 0.00 USD | 1,570,000.00 USD | 443,660.00 USD | 688,860.00 USD |
| `7D` | `1.31` | 29,620,000.00 USD | 29,620,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,370,000.00 USD |
| `1D` | `1.31` | 23,010,000.00 USD | 23,010,000.00 USD | 0.00 USD | 464,990.00 USD | 483,320.00 USD | 321,130.00 USD |
| `7D` | `1.31` | 32,040,000.00 USD | 32,040,000.00 USD | 0.00 USD | 57,160.00 USD | 1,070,000.00 USD | 1,280,000.00 USD |
| `1D` | `1.32` | 29,230,000.00 USD | 29,230,000.00 USD | 0.00 USD | 213,000.00 USD | 1,830,000.00 USD | 4,170,000.00 USD |
| `7D` | `1.32` | 36,660,000.00 USD | 36,660,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 36,210,000.00 USD | 36,210,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,060,000.00 USD | 3,590,000.00 USD |
| `7D` | `1.32` | 39,680,000.00 USD | 39,680,000.00 USD | 0.00 USD | 755,330.00 USD | 495,580.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 39,740,000.00 USD | 39,740,000.00 USD | 0.00 USD | 1,720,000.00 USD | 742,480.00 USD | 1,060,000.00 USD |
| `7D` | `1.32` | 41,250,000.00 USD | 41,250,000.00 USD | 0.00 USD | 966,720.00 USD | 235,180.00 USD | 367,890.00 USD |
| `1D` | `1.32` | 44,260,000.00 USD | 44,260,000.00 USD | 0.00 USD | 1,830,000.00 USD | 981,550.00 USD | 1,710,000.00 USD |
| `7D` | `1.32` | 45,290,000.00 USD | 45,290,000.00 USD | 0.00 USD | 1,980,000.00 USD | 761,100.00 USD | 1,290,000.00 USD |
| `1D` | `1.32` | 47,260,000.00 USD | 47,260,000.00 USD | 0.00 USD | 1,770,000.00 USD | 259,410.00 USD | 968,180.00 USD |
| `7D` | `1.32` | 47,660,000.00 USD | 47,660,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 49,510,000.00 USD | 49,510,000.00 USD | 0.00 USD | 646,920.00 USD | 308,630.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 48,190,000.00 USD | 48,190,000.00 USD | 0.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 51,700,000.00 USD | 51,700,000.00 USD | 0.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD |
| `7D` | `1.33` | 49,350,000.00 USD | 49,350,000.00 USD | 0.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 54,140,000.00 USD | 54,140,000.00 USD | 0.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 51,070,000.00 USD | 51,070,000.00 USD | 0.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 55,970,000.00 USD | 55,970,000.00 USD | 0.00 USD | 365,160.00 USD | 249,050.00 USD | 1,220,000.00 USD |
| `7D` | `1.33` | 53,340,000.00 USD | 53,340,000.00 USD | 0.00 USD | 830,370.00 USD | 108,920.00 USD | 1,330,000.00 USD |
| `1D` | `1.33` | 57,780,000.00 USD | 57,780,000.00 USD | 0.00 USD | 945,140.00 USD | 95,380.00 USD | 773,790.00 USD |
| `7D` | `1.33` | 53,850,000.00 USD | 53,850,000.00 USD | 0.00 USD | 131,350.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 60,140,000.00 USD | 60,140,000.00 USD | 0.00 USD | 842,300.00 USD | 333,220.00 USD | 1,180,000.00 USD |
| `7D` | `1.34` | 55,800,000.00 USD | 55,800,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD |
| `1D` | `1.34` | 62,690,000.00 USD | 62,690,000.00 USD | 0.00 USD | 1,230,000.00 USD | 398,480.00 USD | 924,530.00 USD |
| `7D` | `1.34` | 57,900,000.00 USD | 57,900,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 494,950.00 USD |
| `1D` | `1.34` | 66,660,000.00 USD | 66,660,000.00 USD | 0.00 USD | 1,730,000.00 USD | 549,090.00 USD | 1,700,000.00 USD |
| `7D` | `1.34` | 62,630,000.00 USD | 62,630,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 440,440.00 USD |
| `1D` | `1.34` | 70,380,000.00 USD | 70,380,000.00 USD | 0.00 USD | 1,630,000.00 USD | 878,740.00 USD | 1,200,000.00 USD |
| `7D` | `1.34` | 68,370,000.00 USD | 68,370,000.00 USD | 0.00 USD | 1,730,000.00 USD | 2,870,000.00 USD | 1,140,000.00 USD |
| `1D` | `1.34` | 74,500,000.00 USD | 74,500,000.00 USD | 0.00 USD | 2,250,000.00 USD | 696,110.00 USD | 1,170,000.00 USD |
| `7D` | `1.34` | 79,600,000.00 USD | 79,600,000.00 USD | 0.00 USD | 3,700,000.00 USD | 1,930,000.00 USD | 5,610,000.00 USD |
| `1D` | `1.35` | 76,400,000.00 USD | 76,400,000.00 USD | 0.00 USD | 825,410.00 USD | 386,900.00 USD | 692,690.00 USD |
| `7D` | `1.35` | 87,360,000.00 USD | 87,360,000.00 USD | 0.00 USD | 2,550,000.00 USD | 2,230,000.00 USD | 2,980,000.00 USD |
| `1D` | `1.35` | 78,250,000.00 USD | 78,250,000.00 USD | 0.00 USD | 786,490.00 USD | 263,070.00 USD | 799,350.00 USD |
| `7D` | `1.35` | 97,850,000.00 USD | 97,850,000.00 USD | 0.00 USD | 4,410,000.00 USD | 1,760,000.00 USD | 4,320,000.00 USD |
| `1D` | `1.35` | 80,770,000.00 USD | 80,770,000.00 USD | 0.00 USD | 1,120,000.00 USD | 301,120.00 USD | 1,100,000.00 USD |
| `7D` | `1.35` | 105,620,000.00 USD | 105,620,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 82,110,000.00 USD | 82,110,000.00 USD | 0.00 USD | 558,120.00 USD | 208,670.00 USD | 571,840.00 USD |
| `7D` | `1.35` | 113,950,000.00 USD | 113,950,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD |
| `1D` | `1.35` | 84,450,000.00 USD | 84,450,000.00 USD | 0.00 USD | 935,850.00 USD | 362,020.00 USD | 1,040,000.00 USD |
| `7D` | `1.35` | 122,180,000.00 USD | 122,180,000.00 USD | 0.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD |
| `1D` | `1.36` | 86,390,000.00 USD | 86,390,000.00 USD | 0.00 USD | 758,190.00 USD | 199,730.00 USD | 978,960.00 USD |
| `7D` | `1.36` | 126,250,000.00 USD | 126,250,000.00 USD | 0.00 USD | 1,320,000.00 USD | 879,500.00 USD | 1,870,000.00 USD |
| `1D` | `1.36` | 87,700,000.00 USD | 87,700,000.00 USD | 0.00 USD | 812,050.00 USD | 76,930.00 USD | 425,930.00 USD |
| `7D` | `1.36` | 130,040,000.00 USD | 130,040,000.00 USD | 0.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.36` | 88,520,000.00 USD | 88,520,000.00 USD | 0.00 USD | 430,370.00 USD | 151,930.00 USD | 229,660.00 USD |
| `7D` | `1.36` | 132,420,000.00 USD | 132,420,000.00 USD | 0.00 USD | 671,910.00 USD | 542,980.00 USD | 1,170,000.00 USD |
| `1D` | `1.36` | 89,470,000.00 USD | 89,470,000.00 USD | 0.00 USD | 390,480.00 USD | 174,320.00 USD | 389,900.00 USD |
| `7D` | `1.36` | 136,650,000.00 USD | 136,650,000.00 USD | 0.00 USD | 2,100,000.00 USD | 895,970.00 USD | 1,240,000.00 USD |
| `1D` | `1.36` | 90,120,000.00 USD | 90,120,000.00 USD | 0.00 USD | 253,080.00 USD | 60,540.00 USD | 338,290.00 USD |
| `7D` | `1.36` | 138,350,000.00 USD | 138,350,000.00 USD | 0.00 USD | 664,020.00 USD | 328,930.00 USD | 707,350.00 USD |
| `1D` | `1.37` | 90,300,000.00 USD | 90,300,000.00 USD | 0.00 USD | 53,740.00 USD | 0.00 USD | 124,610.00 USD |
| `7D` | `1.37` | 138,850,000.00 USD | 138,850,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 40,350.00 USD |
| `1D` | `1.37` | 90,530,000.00 USD | 90,530,000.00 USD | 0.00 USD | 99,090.00 USD | 85,720.00 USD | 48,400.00 USD |
| `7D` | `1.37` | 140,630,000.00 USD | 140,630,000.00 USD | 0.00 USD | 547,200.00 USD | 138,950.00 USD | 1,100,000.00 USD |
| `1D` | `1.37` | 90,910,000.00 USD | 90,910,000.00 USD | 0.00 USD | 76,400.00 USD | 25,940.00 USD | 270,940.00 USD |
| `7D` | `1.37` | 142,040,000.00 USD | 142,040,000.00 USD | 0.00 USD | 465,040.00 USD | 398,870.00 USD | 543,240.00 USD |
| `1D` | `1.37` | 91,050,000.00 USD | 91,050,000.00 USD | 0.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD |
| `7D` | `1.37` | 144,900,000.00 USD | 144,900,000.00 USD | 0.00 USD | 931,390.00 USD | 404,120.00 USD | 1,520,000.00 USD |
| `1D` | `1.37` | 91,190,000.00 USD | 91,190,000.00 USD | 0.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD |
| `7D` | `1.38` | 146,590,000.00 USD | 146,590,000.00 USD | 0.00 USD | 594,550.00 USD | 326,340.00 USD | 769,660.00 USD |
| `1D` | `1.38` | 91,450,000.00 USD | 91,450,000.00 USD | 0.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD |
| `7D` | `1.38` | 148,210,000.00 USD | 148,210,000.00 USD | 0.00 USD | 676,760.00 USD | 389,310.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 91,960,000.00 USD | 91,960,000.00 USD | 0.00 USD | 231,710.00 USD | 73,260.00 USD | 203,900.00 USD |
| `7D` | `1.38` | 150,140,000.00 USD | 150,140,000.00 USD | 0.00 USD | 579,450.00 USD | 290,350.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 92,730,000.00 USD | 92,730,000.00 USD | 0.00 USD | 379,220.00 USD | 101,680.00 USD | 292,290.00 USD |
| `7D` | `1.38` | 152,690,000.00 USD | 152,690,000.00 USD | 0.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 93,060,000.00 USD | 93,060,000.00 USD | 0.00 USD | 165,220.00 USD | 53,840.00 USD | 115,580.00 USD |
| `7D` | `1.38` | 153,780,000.00 USD | 153,780,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.38` | 93,480,000.00 USD | 93,480,000.00 USD | 0.00 USD | 340,420.00 USD | 17,520.00 USD | 56,890.00 USD |
| `7D` | `1.39` | 154,870,000.00 USD | 154,870,000.00 USD | 0.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 93,670,000.00 USD | 93,670,000.00 USD | 0.00 USD | 81,750.00 USD | 52,380.00 USD | 56,350.00 USD |
| `7D` | `1.39` | 155,370,000.00 USD | 155,370,000.00 USD | 0.00 USD | 86,820.00 USD | 203,870.00 USD | 200,360.00 USD |
| `1D` | `1.39` | 93,820,000.00 USD | 93,820,000.00 USD | 0.00 USD | 83,870.00 USD | 35,460.00 USD | 36,020.00 USD |
| `7D` | `1.39` | 156,460,000.00 USD | 156,460,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 238,810.00 USD |
| `1D` | `1.39` | 94,080,000.00 USD | 94,080,000.00 USD | 0.00 USD | 86,460.00 USD | 17,040.00 USD | 153,570.00 USD |
| `7D` | `1.39` | 156,620,000.00 USD | 156,620,000.00 USD | 0.00 USD | 118,760.00 USD | 39,430.00 USD | 0.00 USD |
| `7D` | `1.39` | 156,940,000.00 USD | 156,940,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.39` | 94,100,000.00 USD | 94,100,000.00 USD | 0.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD |
| `7D` | `1.40` | 157,090,000.00 USD | 157,090,000.00 USD | 0.00 USD | 121,260.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 94,200,000.00 USD | 94,200,000.00 USD | 0.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `1.40` | 157,100,000.00 USD | 157,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD |
| `7D` | `1.40` | 157,110,000.00 USD | 157,110,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 157,250,000.00 USD | 157,250,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 157,360,000.00 USD | 157,360,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `7D` | `1.41` | 157,610,000.00 USD | 157,610,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 157,770,000.00 USD | 157,770,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.41` | 94,270,000.00 USD | 94,270,000.00 USD | 0.00 USD | 1,390.00 USD | 149.67 USD | 64,030.00 USD |
| `7D` | `1.41` | 157,940,000.00 USD | 157,940,000.00 USD | 0.00 USD | 12,250.00 USD | 37,300.00 USD | 120,130.00 USD |
| `1D` | `1.41` | 94,430,000.00 USD | 94,430,000.00 USD | 0.00 USD | 48,490.00 USD | 414.70 USD | 112,380.00 USD |
| `7D` | `1.41` | 158,230,000.00 USD | 158,230,000.00 USD | 0.00 USD | 97,250.00 USD | 57,460.00 USD | 136,900.00 USD |
| `1D` | `1.41` | 94,460,000.00 USD | 94,460,000.00 USD | 0.00 USD | 1,740.00 USD | 158.40 USD | 28,820.00 USD |
| `7D` | `1.41` | 158,400,000.00 USD | 158,400,000.00 USD | 0.00 USD | 11,290.00 USD | 26,480.00 USD | 132,120.00 USD |
| `1D` | `1.41` | 94,470,000.00 USD | 94,470,000.00 USD | 0.00 USD | 4,630.00 USD | 237.30 USD | 204.46 USD |
| `7D` | `1.42` | 159,030,000.00 USD | 159,030,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD |
| `1D` | `1.42` | 94,580,000.00 USD | 94,580,000.00 USD | 0.00 USD | 61,830.00 USD | 27,040.00 USD | 27,040.00 USD |
| `7D` | `1.42` | 159,460,000.00 USD | 159,460,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD |
| `1D` | `1.42` | 94,960,000.00 USD | 94,960,000.00 USD | 0.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.42` | 160,480,000.00 USD | 160,480,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.42` | 95,700,000.00 USD | 95,700,000.00 USD | 0.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.42` | 161,850,000.00 USD | 161,850,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.42` | 96,130,000.00 USD | 96,130,000.00 USD | 0.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.42` | 162,480,000.00 USD | 162,480,000.00 USD | 0.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.42` | 96,220,000.00 USD | 96,220,000.00 USD | 0.00 USD | 9,670.00 USD | 55,100.00 USD | 21,210.00 USD |
| `7D` | `1.43` | 162,840,000.00 USD | 162,840,000.00 USD | 0.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD |
| `1D` | `1.43` | 96,460,000.00 USD | 96,460,000.00 USD | 0.00 USD | 113,650.00 USD | 38,740.00 USD | 90,040.00 USD |
| `7D` | `1.43` | 163,860,000.00 USD | 163,860,000.00 USD | 0.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD |
| `1D` | `1.43` | 96,640,000.00 USD | 96,640,000.00 USD | 0.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.43` | 165,370,000.00 USD | 165,370,000.00 USD | 0.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.43` | 96,810,000.00 USD | 96,810,000.00 USD | 0.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.43` | 166,750,000.00 USD | 166,750,000.00 USD | 0.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.43` | 97,000,000.00 USD | 97,000,000.00 USD | 0.00 USD | 18,490.00 USD | 28,360.00 USD | 151,220.00 USD |
| `7D` | `1.43` | 167,550,000.00 USD | 167,550,000.00 USD | 0.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `7D` | `1.44` | 168,080,000.00 USD | 168,080,000.00 USD | 0.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD |
| `7D` | `1.44` | 168,430,000.00 USD | 168,430,000.00 USD | 0.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD |
| `7D` | `1.44` | 168,890,000.00 USD | 168,890,000.00 USD | 0.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `7D` | `1.44` | 169,730,000.00 USD | 169,730,000.00 USD | 0.00 USD | 299,590.00 USD | 131,210.00 USD | 405,740.00 USD |
| `7D` | `1.44` | 170,150,000.00 USD | 170,150,000.00 USD | 0.00 USD | 69,670.00 USD | 152,290.00 USD | 199,660.00 USD |
| `7D` | `1.45` | 170,280,000.00 USD | 170,280,000.00 USD | 0.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD |
| `7D` | `1.45` | 170,410,000.00 USD | 170,410,000.00 USD | 0.00 USD | 11,070.00 USD | 2,120.00 USD | 116,410.00 USD |
| `7D` | `1.45` | 170,890,000.00 USD | 170,890,000.00 USD | 0.00 USD | 70,540.00 USD | 96,050.00 USD | 311,630.00 USD |
| `7D` | `1.45` | 171,500,000.00 USD | 171,500,000.00 USD | 0.00 USD | 190,550.00 USD | 38,510.00 USD | 383,280.00 USD |
| `7D` | `1.45` | 172,140,000.00 USD | 172,140,000.00 USD | 0.00 USD | 169,890.00 USD | 128,180.00 USD | 338,310.00 USD |
| `7D` | `1.45` | 172,210,000.00 USD | 172,210,000.00 USD | 0.00 USD | 47,300.00 USD | 23,220.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.98B` | Total OI Tokens: `2,325,091,838.2 XRP`
  * 1h OI Change: `-0.70%` | 4h OI Change: `-2.96%` | 24h OI Change: `+0.07%`
  * Exchange Breakdown: Binance=`490.31M` | Bybit=`328.51M` | OKX=`100.31M` | Hyperliquid=`226.01M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `61.70K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0034%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0069%` | **USDT Bitget** | `0.0040%` |
| **CoinM Binance** | `0.0096%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `38.81%` | `61.19%` | `0.63` | 803,800,000.00 USD |
| `15M` | `Binance` | `33.97%` | `66.03%` | `0.51` | 252,230,000.00 USD |
| `15M` | `OKX` | `36.49%` | `63.51%` | `0.57` | 142,480,000.00 USD |
| `15M` | `Bybit` | `40.66%` | `59.34%` | `0.69` | 60,850,000.00 USD |
| `15M` | `KuCoin` | `50.36%` | `49.64%` | `1.01` | 1,090,000.00 USD |
| `15M` | `Gate` | `49.87%` | `50.13%` | `0.99` | 147,470,000.00 USD |
| `15M` | `Bitget` | `31.76%` | `68.24%` | `0.47` | 53,830,000.00 USD |
| `15M` | `BingX` | `48.84%` | `51.16%` | `0.95` | 6,740,000.00 USD |
| `15M` | `MEXC` | `41.77%` | `58.23%` | `0.72` | 32,870,000.00 USD |
| `15M` | `Bitunix` | `52.9%` | `47.1%` | `1.12` | 28,560,000.00 USD |
| `15M` | `Hyperliquid` | `17.03%` | `82.97%` | `0.21` | 6,980,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `62.1%` | `37.9%` | `1.64` | 1,810,000.00 USD |
| `15M` | `Crypto.com` | `55.47%` | `44.53%` | `1.25` | 0.00 USD |
| `15M` | `WhiteBIT` | `85.31%` | `14.69%` | `5.81` | 42,220,000.00 USD |
| `15M` | `HTX` | `87.59%` | `12.41%` | `7.06` | 6,640,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 2,520,000.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 20,430.00 USD |
| `15M` | `Kraken` | `23.46%` | `76.54%` | `0.31` | 1,940,000.00 USD |
| `15M` | `Aster` | `61.86%` | `38.14%` | `1.62` | 6,660,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `23.15%` | `76.85%` | `0.30` | 8,870,000.00 USD |
| `15M` | `Whale Positions` | `33.97%` | `66.03%` | `0.51` | 252,230,000.00 USD |
| `15M` | `Global Accounts` | `38.81%` | `61.19%` | `0.63` | 803,800,000.00 USD |
| `1H` | `XRP` | `48.01%` | `51.99%` | `0.92` | 1,870,000,000.00 USD |
| `1H` | `Binance` | `43.38%` | `56.62%` | `0.77` | 546,100,000.00 USD |
| `1H` | `OKX` | `46.4%` | `53.6%` | `0.87` | 348,720,000.00 USD |
| `1H` | `Bybit` | `41.17%` | `58.83%` | `0.70` | 130,850,000.00 USD |
| `1H` | `KuCoin` | `54.13%` | `45.87%` | `1.18` | 5,360,000.00 USD |
| `1H` | `Gate` | `50.69%` | `49.31%` | `1.03` | 310,180,000.00 USD |
| `1H` | `Bitget` | `50.83%` | `49.17%` | `1.03` | 119,670,000.00 USD |
| `1H` | `BingX` | `55.17%` | `44.83%` | `1.23` | 20,850,000.00 USD |
| `1H` | `MEXC` | `53.14%` | `46.86%` | `1.13` | 92,940,000.00 USD |
| `1H` | `Bitunix` | `49.88%` | `50.12%` | `1.00` | 65,780,000.00 USD |
| `1H` | `Hyperliquid` | `72.92%` | `27.08%` | `2.69` | 51,670,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.7%` | `52.3%` | `0.91` | 4,740,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `58.03%` | `41.97%` | `1.38` | 104,260,000.00 USD |
| `1H` | `HTX` | `38.41%` | `61.59%` | `0.62` | 16,070,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `41.17%` | `58.83%` | `0.70` | 10,760,000.00 USD |
| `1H` | `Bitfinex` | `61.73%` | `38.27%` | `1.61` | 113,690.00 USD |
| `1H` | `Kraken` | `27.53%` | `72.47%` | `0.38` | 4,700,000.00 USD |
| `1H` | `Aster` | `40.05%` | `59.95%` | `0.67` | 16,580,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.15%` | `45.85%` | `1.18` | 25,160,000.00 USD |
| `1H` | `Whale Positions` | `43.38%` | `56.62%` | `0.77` | 546,100,000.00 USD |
| `1H` | `Global Accounts` | `48.01%` | `51.99%` | `0.92` | 1,870,000,000.00 USD |
| `4H` | `XRP` | `44.83%` | `55.17%` | `0.81` | 10,320,000,000.00 USD |
| `4H` | `Binance` | `45.57%` | `54.43%` | `0.84` | 3,110,000,000.00 USD |
| `4H` | `OKX` | `44.04%` | `55.96%` | `0.79` | 2,000,000,000.00 USD |
| `4H` | `Bybit` | `44.96%` | `55.04%` | `0.82` | 736,740,000.00 USD |
| `4H` | `KuCoin` | `47.4%` | `52.6%` | `0.90` | 33,960,000.00 USD |
| `4H` | `Gate` | `46.64%` | `53.36%` | `0.87` | 1,640,000,000.00 USD |
| `4H` | `Bitget` | `44.09%` | `55.91%` | `0.79` | 541,530,000.00 USD |
| `4H` | `BingX` | `33.13%` | `66.87%` | `0.50` | 142,530,000.00 USD |
| `4H` | `MEXC` | `48.16%` | `51.84%` | `0.93` | 427,060,000.00 USD |
| `4H` | `Bitunix` | `48.24%` | `51.76%` | `0.93` | 377,520,000.00 USD |
| `4H` | `Hyperliquid` | `44.53%` | `55.47%` | `0.80` | 310,660,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `56.84%` | `43.16%` | `1.32` | 26,160,000.00 USD |
| `4H` | `Crypto.com` | `49.54%` | `50.46%` | `0.98` | 0.00 USD |
| `4H` | `WhiteBIT` | `27.01%` | `72.99%` | `0.37` | 503,040,000.00 USD |
| `4H` | `HTX` | `68.96%` | `31.04%` | `2.22` | 151,170,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 55,890,000.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 1,910,000.00 USD |
| `4H` | `Kraken` | `50.79%` | `49.21%` | `1.03` | 47,090,000.00 USD |
| `4H` | `Aster` | `40.23%` | `59.77%` | `0.67` | 97,040,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.37%` | `54.63%` | `0.83` | 128,100,000.00 USD |
| `4H` | `Whale Positions` | `45.57%` | `54.43%` | `0.84` | 3,110,000,000.00 USD |
| `4H` | `Global Accounts` | `44.83%` | `55.17%` | `0.81` | 10,320,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.30` | `1.31` | `1.30` | `1.31` | `1.30` | 11,087,990.94 USD | 4,090,249.58 USD | 6,997,741.36 USD | -2,907,491.79 USD | `-26.22%` | `5B / 28S` |
| `0:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 10,205,311.65 USD | 4,505,902.50 USD | 5,699,409.15 USD | -1,193,506.66 USD | `-11.69%` | `6B / 11S` |
| `5:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 4,776,328.08 USD | 2,498,208.46 USD | 2,278,119.62 USD | 220,088.84 USD | `+4.61%` | `7B / 8S` |
| `0:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.29` | 9,199,982.08 USD | 4,187,578.87 USD | 5,012,403.21 USD | -824,824.35 USD | `-8.97%` | `4B / 7S` |
| `5:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.29` | 5,359,755.08 USD | 2,909,456.29 USD | 2,450,298.78 USD | 459,157.51 USD | `+8.57%` | `5B / 3S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.30` | `1.29` | 8,857,459.31 USD | 3,136,112.07 USD | 5,721,347.24 USD | -2,585,235.17 USD | `-29.19%` | `5B / 22S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 11,824,590.46 USD | 6,782,340.79 USD | 5,042,249.67 USD | 1,740,091.12 USD | `+14.72%` | `12B / 8S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 4,908,299.96 USD | 2,545,215.27 USD | 2,363,084.69 USD | 182,130.57 USD | `+3.71%` | `7B / 8S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 4,397,440.00 USD | 1,948,835.02 USD | 2,448,604.98 USD | -499,769.95 USD | `-11.37%` | `7B / 14S` |
| `0:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 28,650,202.07 USD | 8,920,240.47 USD | 19,729,961.60 USD | -10,809,721.13 USD | `-37.73%` | `4B / 41S` |

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
| `5m` | 177,380.00 USD | -442,250.00 USD | **`DISTRIBUTION`** |
| `15m` | -7,280,000.00 USD | -17,460,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -7,640,000.00 USD | -17,580,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -8,530,000.00 USD | -19,460,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -11,770,000.00 USD | -25,810,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -10,080,000.00 USD | -34,540,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -8,010,000.00 USD | -23,670,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -9,840,000.00 USD | -30,000,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -9,320,000.00 USD | -26,180,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -31,260,000.00 USD | -79,350,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -77,820,000.00 USD | -94,900,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -561,260,000.00 USD | -1,200,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+177.38K` | 15m=`-7.28M` | 1h=`-8.53M` | 24h=`-31.26M`
* Futures Capital Netflows: 5m=`-442.25K` | 15m=`-17.46M` | 1h=`-19.46M` | 24h=`-79.35M`
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
  * `2026-10-29 23:31:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:18 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
