# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 11:47:32 IST` (`2026-10-30 06:17:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.26` | **Live Ask Quote**: `1.26` | **Mid Price**: `1.26`
- **Spread Points**: `3.00` | **Spread BPS**: `23.84 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.23` | VWAP Z-Score: `+1.23` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0094` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `61.68` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.29` | Lower -3.00σ Band: `1.17`
  * Upper +2.51σ Band: `1.28` | Lower -2.51σ Band: `1.18`
  * Upper +2.01σ Band: `1.27` | Lower -2.01σ Band: `1.19`
  * Upper +2.00σ Band: `1.27` | Lower -2.00σ Band: `1.19`
  * Upper +1.28σ Band: `1.25` | Lower -1.28σ Band: `1.21`
  * Upper +1.00σ Band: `1.25` | Lower -1.00σ Band: `1.21`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.25` | EMA-20=`1.24` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.25` (Slope: `+0.0000`) | EMA-100=`1.26`
  * Institutional Anchors: EMA-144=`1.27` | EMA-200=`1.28` (Slope: `-0.3569`) | EMA-233=`1.29`
- **Range Boundaries**: 24H High=`1.31` | 24H Low=`1.19` | Weekly High=`1.34` | Weekly Low=`1.19`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `+0.04%`)
  * Point of Control (POC) = `1.25` (Distance: `+0.73%`)
  * Value Area Low (VAL) = `1.23` (Distance: `+2.63%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.33` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.19`
  * London Session (08:00-16:00 UTC): High=`1.26` | Low=`1.25`
  * New York Session (13:00-21:00 UTC): High=`1.27` | Low=`1.25`
  * Initial Balance (First Hour): IB High=`1.26` | IB Low=`1.25`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.25` - `1.26`
  * Optimal Trade Entry (OTE 0.705): `1.26`
  * Structural Invalidation Anchor (0.786): `1.27`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.26` | `1.26` | `1.25` | `1.26` | `3,527,930` | 4,432,651.56 USD | -678,598.21 USD | `-15.31%` | -40,306,129.73 USD | `-1.93` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `2,066,444` | 2,598,444.37 USD | 203,925.90 USD | `+7.85%` | -40,102,203.83 USD | `-0.15` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `1,723,549` | 2,172,311.74 USD | 353,910.25 USD | `+16.29%` | -39,748,293.58 USD | `+0.21` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.26` | `1.26` | `1.26` | `1.26` | `4,350,612` | 5,482,004.91 USD | 350,972.75 USD | `+6.40%` | -39,114,220.35 USD | `-0.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.26` | `1.26` | `1.26` | `1.26` | `6,268,556` | 7,888,806.65 USD | -513,311.17 USD | `-6.51%` | -39,627,531.52 USD | `-0.51` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.26` | `1.26` | `1.25` | `1.26` | `7,317,923` | 9,203,407.67 USD | -120,762.07 USD | `-1.31%` | -39,748,293.58 USD | `-0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `1.25` | `1.26` | `1.24` | `1.25` | `31,772,661` | 39,740,326.41 USD | 3,435,958.07 USD | `+8.65%` | -42,192,555.99 USD | `+0.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.25` | `1.26` | `1.25` | `1.26` | `23,391,078` | 29,445,157.81 USD | 3,228,147.46 USD | `+10.96%` | -38,964,408.53 USD | `+0.58` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.26` | `1.26` | `1.25` | `1.26` | `7,338,964` | 9,229,962.29 USD | -95,259.44 USD | `-1.03%` | -39,059,667.97 USD | `+0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -42,956,799.49 USD | `-1.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -45,386,586.40 USD | `+0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.26` | `62,481,662` | 78,388,891.89 USD | 6,543,343.47 USD | `+8.35%` | -38,843,242.93 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | 545,129.68 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -14,866,665.27 USD | `-1.39` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -42,956,799.49 USD | `-1.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -45,386,586.40 USD | `+0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.26` | `62,481,662` | 78,388,891.89 USD | 6,543,343.47 USD | `+8.35%` | -38,843,242.93 USD | `+1.11` | **`BULLISH`** | `DELTA ALIGNED` |

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
| --- | **`1.26`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `1.26` | `27519.0000` | 34,786.77 USD | 2,487,671.73 USD | `4 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `183168.0000` | 231,524.35 USD | 2,452,884.97 USD | `1 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `55906.0000` | 70,659.59 USD | 2,221,360.61 USD | `4 orders` | `+0.14%` | `-` |
| `ASK` | `1.26` | `321826.0000` | 406,723.70 USD | 2,150,701.02 USD | `10 orders` | `+0.13%` | `-` |
| `ASK` | `1.26` | `507677.0000` | 641,551.42 USD | 1,743,977.32 USD | `4 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `17023.0000` | 21,510.26 USD | 1,102,425.90 USD | `5 orders` | `+0.11%` | `-` |
| `ASK` | `1.26` | `99446.0000` | 125,650.02 USD | 1,080,915.63 USD | `8 orders` | `+0.11%` | `-` |
| `ASK` | `1.26` | `37762.0000` | 47,708.51 USD | 955,265.61 USD | `6 orders` | `+0.10%` | `-` |
| `ASK` | `1.26` | `34118.0000` | 43,101.27 USD | 907,557.10 USD | `10 orders` | `+0.09%` | `-` |
| `ASK` | `1.26` | `324927.0000` | 410,447.79 USD | 864,455.83 USD | `9 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `94126.0000` | 118,890.55 USD | 454,008.05 USD | `11 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `52421.0000` | 66,207.72 USD | 335,117.50 USD | `11 orders` | `+0.07%` | `-` |
| `ASK` | `1.26` | `42193.0000` | 53,285.54 USD | 268,909.77 USD | `8 orders` | `+0.06%` | `-` |
| `ASK` | `1.26` | `49282.0000` | 62,233.31 USD | 215,624.23 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `1.26` | `39011.0000` | 49,259.19 USD | 153,390.92 USD | `9 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `28146.0000` | 35,537.14 USD | 104,131.73 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `19414.0000` | 24,510.17 USD | 68,594.59 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `1.26` | `16754.0000` | 21,150.25 USD | 44,084.42 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `1.26` | `12583.0000` | 15,883.52 USD | 22,934.17 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `1.26` | `5586.0000` | 7,050.65 USD | 7,050.65 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.26` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.26` | `0.00%` | `-` |
| `BID` | `1.26` | `37071.0000` | 46,787.31 USD | 46,787.31 USD | `20 orders` | `-0.00%` | `-` |
| `BID` | `1.26` | `48404.0000` | 61,085.85 USD | 107,873.16 USD | `17 orders` | `-0.01%` | `-` |
| `BID` | `1.26` | `7930.0000` | 10,006.87 USD | 117,880.02 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `1.26` | `37523.0000` | 47,346.52 USD | 165,226.55 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `1.26` | `38883.0000` | 49,058.68 USD | 214,285.23 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `99396.0000` | 125,397.99 USD | 339,683.22 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `42159.0000` | 53,183.58 USD | 392,866.80 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `1.26` | `83200.0000` | 104,948.48 USD | 497,815.28 USD | `12 orders` | `-0.06%` | `-` |
| `BID` | `1.26` | `271513.0000` | 342,459.35 USD | 840,274.63 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `1.26` | `29569.0000` | 37,292.42 USD | 877,567.05 USD | `6 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `100498.0000` | 126,738.03 USD | 1,004,305.08 USD | `4 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `246416.0000` | 310,730.58 USD | 1,315,035.65 USD | `5 orders` | `-0.09%` | `-` |
| `BID` | `1.26` | `41961.0000` | 52,908.62 USD | 1,367,944.28 USD | `5 orders` | `-0.10%` | `-` |
| `BID` | `1.26` | `13233.0000` | 16,684.17 USD | 1,384,628.44 USD | `3 orders` | `-0.11%` | `-` |
| `BID` | `1.26` | `65025.0000` | 81,977.02 USD | 1,466,605.46 USD | `4 orders` | `-0.11%` | `-` |
| `BID` | `1.26` | `29350.0000` | 36,998.61 USD | 1,503,604.07 USD | `4 orders` | `-0.12%` | `-` |
| `BID` | `1.26` | `32429.0000` | 40,876.75 USD | 1,544,480.83 USD | `6 orders` | `-0.13%` | `-` |
| `BID` | `1.26` | `39019.0000` | 49,179.55 USD | 1,593,660.37 USD | `5 orders` | `-0.14%` | `-` |
| `BID` | `1.26` | `383009.0000` | 482,706.24 USD | 2,076,366.62 USD | `9 orders` | `-0.15%` | `-` |
| `BID` | `1.26` | `32879.0000` | 41,434.12 USD | 2,117,800.73 USD | `6 orders` | `-0.15%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `28` | `0x31b1...1434` | `LONG` | 44,160,620.66 USD | `35,031,430.00` | `1.13` | `1.26` | `0.9612` | 4,581,737.39 USD | `+10.38%` | `10X Cross` |
| `92` | `0x5b5d...c060` | `SHORT` | 20,124,534.81 USD | `15,964,251.00` | `1.44` | `1.26` | `11.31` | 2,791,533.90 USD | `+13.87%` | `5X Cross` |
| `157` | `0xb83d...6e36` | `SHORT` | 13,310,422.45 USD | `10,555,450.00` | `1.50` | `1.26` | `13.74` | 2,512,147.19 USD | `+18.87%` | `5X Cross` |
| `340` | `0x58f0...0d20` | `LONG` | 6,690,189.51 USD | `5,307,147.00` | `1.24` | `1.26` | `1.22` | 87,346.01 USD | `+1.31%` | `20X Cross` |
| `394` | `0xecb6...2b00` | `SHORT` | 5,719,752.53 USD | `4,539,306.00` | `1.27` | `1.26` | `7.57` | 45,772.28 USD | `+0.80%` | `10X Cross` |
| `424` | `0xca49...53c8` | `SHORT` | 5,216,651.91 USD | `4,138,886.00` | `1.44` | `1.26` | `4.81` | 736,670.82 USD | `+14.12%` | `20X Cross` |
| `436` | `0xdd53...2b13` | `SHORT` | 5,042,630.55 USD | `3,998,914.00` | `1.40` | `1.26` | `16.61` | 554,245.56 USD | `+10.99%` | `3X Cross` |
| `502` | `0x610b...b613` | `LONG` | 4,468,915.91 USD | `3,543,946.00` | `1.44` | `1.26` | `0.8108` | -631,076.70 USD | `-14.12%` | `5X Cross` |
| `531` | `0xfc27...9d9d` | `SHORT` | 4,191,853.01 USD | `3,325,284.00` | `1.29` | `1.26` | `6.59` | 108,856.29 USD | `+2.60%` | `20X Cross` |
| `616` | `0x9946...0852` | `SHORT` | 3,672,267.86 USD | `2,912,418.00` | `1.41` | `1.26` | `1.78` | 436,234.72 USD | `+11.88%` | `20X Cross` |
| `662` | `0xc30c...a4c9` | `SHORT` | 3,397,928.59 USD | `2,695,699.00` | `1.42` | `1.26` | `1.58` | 417,644.29 USD | `+12.29%` | `7X Cross` |
| `698` | `0xf48f...10fe` | `LONG` | 3,235,447.32 USD | `2,565,779.00` | `1.53` | `1.26` | `0.9935` | -689,193.41 USD | `-21.30%` | `4X Cross` |
| `734` | `0x023a...2355` | `SHORT` | 3,108,272.95 USD | `2,464,927.00` | `1.32` | `1.26` | `3.35` | 144,723.29 USD | `+4.66%` | `20X Cross` |
| `739` | `0x45d2...4029` | `SHORT` | 3,092,987.70 USD | `2,453,000.00` | `1.48` | `1.26` | `18.17` | 545,292.72 USD | `+17.63%` | `20X Cross` |
| `1063` | `0xeadc...9d55` | `LONG` | 2,041,926.18 USD | `1,619,805.00` | `1.21` | `1.26` | `0.000000` | 83,083.16 USD | `+4.07%` | `20X Cross` |
| `1138` | `0x94b2...599e` | `SHORT` | 1,942,663.59 USD | `1,540,696.00` | `1.36` | `1.26` | `1.86` | 157,802.86 USD | `+8.12%` | `20X Cross` |
| `1147` | `0xbcd4...0dd2` | `SHORT` | 1,928,191.48 USD | `1,529,461.00` | `1.31` | `1.26` | `1.86` | 76,353.11 USD | `+3.96%` | `20X Cross` |
| `1160` | `0x3fc5...c0c1` | `SHORT` | 1,906,353.32 USD | `1,511,779.00` | `1.52` | `1.26` | `2.32` | 385,261.28 USD | `+20.21%` | `20X Cross` |
| `1197` | `0x31ef...f715` | `LONG` | 1,859,485.85 USD | `1,475,080.00` | `1.49` | `1.26` | `1.04` | -339,779.55 USD | `-18.27%` | `3X Isolated` |
| `1241` | `0x7737...bf66` | `SHORT` | 1,781,815.24 USD | `1,413,466.00` | `1.41` | `1.26` | `13.65` | 217,053.41 USD | `+12.18%` | `10X Cross` |
| `1301` | `0x95da...2328` | `LONG` | 1,670,138.69 USD | `1,324,876.00` | `1.35` | `1.26` | `0.0720` | -123,502.41 USD | `-7.39%` | `5X Cross` |
| `1320` | `0xee2b...d67e` | `LONG` | 1,647,224.12 USD | `1,306,284.00` | `1.55` | `1.26` | `0.3879` | -383,430.78 USD | `-23.28%` | `4X Cross` |
| `1359` | `0x215d...f80a` | `LONG` | 1,577,990.09 USD | `1,251,777.00` | `1.32` | `1.26` | `1.13` | -76,464.14 USD | `-4.85%` | `14X Cross` |
| `1387` | `0x5fa3...35b7` | `SHORT` | 1,563,964.65 USD | `1,240,651.00` | `1.30` | `1.26` | `2.60` | 52,527.48 USD | `+3.36%` | `20X Cross` |
| `1415` | `0x123d...3bff` | `LONG` | 1,531,375.31 USD | `1,215,329.00` | `1.35` | `1.26` | `0.000000` | -105,693.91 USD | `-6.90%` | `10X Cross` |
| `1473` | `0xdf95...7d72` | `SHORT` | 1,460,392.49 USD | `1,158,490.00` | `1.37` | `1.26` | `34.31` | 130,253.40 USD | `+8.92%` | `20X Cross` |
| `1547` | `0xc179...e0c8` | `SHORT` | 1,390,191.74 USD | `1,103,283.00` | `1.29` | `1.26` | `6.84` | 36,779.08 USD | `+2.65%` | `10X Cross` |
| `1558` | `0xef96...9383` | `SHORT` | 1,378,352.03 USD | `1,092,976.00` | `1.34` | `1.26` | `4.52` | 84,395.40 USD | `+6.12%` | `20X Cross` |
| `1637` | `0xb1ce...681b` | `LONG` | 1,288,035.70 USD | `1,021,764.00` | `1.49` | `1.26` | `1.16` | -236,020.80 USD | `-18.32%` | `4X Isolated` |
| `1644` | `0x7fda...17d1` | `LONG` | 1,277,789.99 USD | `1,012,621.00` | `1.21` | `1.26` | `0.000000` | 49,447.85 USD | `+3.87%` | `20X Cross` |
| `1735` | `0x3c36...461a` | `LONG` | 1,185,141.10 USD | `940,051.00` | `1.30` | `1.26` | `1.05` | -33,939.52 USD | `-2.86%` | `10X Cross` |
| `1816` | `0x2577...4897` | `SHORT` | 1,124,829.60 USD | `892,297.00` | `1.24` | `1.26` | `4.97` | -15,999.70 USD | `-1.42%` | `20X Cross` |
| `1990` | `0xbfc7...80b4` | `SHORT` | 1,008,480.00 USD | `800,000.00` | `1.48` | `1.26` | `3.12` | 174,974.65 USD | `+17.35%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,058.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.06K USD at 1.2927 USD [API] | `2026-10-29 03:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,712.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.71K USD at 1.2921 USD [API] | `2026-10-29 03:23:59` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,236.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.24K USD at 1.2917 USD [API] | `2026-10-29 03:43:55` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,725.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.73K USD at 1.2875 USD [API] | `2026-10-29 04:10:08` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10,126.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.13K USD at 1.2875 USD [API] | `2026-10-29 04:10:08` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 12,896.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 12.90K USD at 1.2885 USD [API] | `2026-10-29 04:12:59` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 27,673.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 27.67K USD at 1.2913 USD [API] | `2026-10-29 04:25:24` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,702.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.70K USD at 1.2913 USD [API] | `2026-10-29 04:25:24` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.2914 USD [API] | `2026-10-29 04:25:24` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,257.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.26K USD at 1.2914 USD [API] | `2026-10-29 04:25:24` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,702.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.70K USD at 1.2914 USD [API] | `2026-10-29 04:25:24` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 491.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.49K USD at 1.2862 USD [API] | `2026-10-29 04:07:55` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 105.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.11K USD at 1.2862 USD [API] | `2026-10-29 04:07:55` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 24,253.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 24.25K USD at 1.2924 USD [API] | `2026-10-29 04:36:50` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 13,332.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 13.33K USD at 1.2924 USD [API] | `2026-10-29 04:36:50` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 33,325.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 33.33K USD at 1.2924 USD [API] | `2026-10-29 04:36:50` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,446.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.45K USD at 1.2949 USD [API] | `2026-10-29 04:46:22` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,772.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.77K USD at 1.2946 USD [API] | `2026-10-29 04:46:02` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 219.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.22K USD at 1.3690 USD [API] | `2026-10-21 09:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 4,139.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.14K USD at 1.3690 USD [API] | `2026-10-21 09:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 8,216.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 8.22K USD at 1.3689 USD [API] | `2026-10-21 09:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 698.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.70K USD at 1.3689 USD [API] | `2026-10-21 09:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 2,269.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.27K USD at 1.3689 USD [API] | `2026-10-21 09:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 4,192.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.19K USD at 1.3688 USD [API] | `2026-10-21 09:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 4,192.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.19K USD at 1.3688 USD [API] | `2026-10-21 09:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 635.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.64K USD at 1.3687 USD [API] | `2026-10-21 09:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 463.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.46K USD at 1.3686 USD [API] | `2026-10-21 09:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 200.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.20K USD at 1.4823 USD [API] | `2026-10-07 01:58:19` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 215.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.22K USD at 1.4943 USD [API] | `2026-09-28 02:34:39` |
| `ANNOUNCEMENT` | `INFO` | `1.54` | 402.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.5365 USD [API] | `2026-09-26 09:31:14` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 576.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.58K USD at 1.4560 USD [API] | `2026-09-24 09:33:21` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 1,495.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.50K USD at 1.4817 USD [API] | `2026-09-23 16:02:17` |
| `ANNOUNCEMENT` | `INFO` | `1.54` | 3,522.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.52K USD at 1.5443 USD [API] | `2026-09-23 14:11:51` |
| `ANNOUNCEMENT` | `INFO` | `1.58` | 1,378.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.38K USD at 1.5788 USD [API] | `2026-09-23 10:25:31` |
| `ANNOUNCEMENT` | `INFO` | `1.58` | 3,999.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.5789 USD [API] | `2026-09-23 10:25:31` |
| `ANNOUNCEMENT` | `INFO` | `1.58` | 48.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.5789 USD [API] | `2026-09-23 10:25:31` |
| `ANNOUNCEMENT` | `INFO` | `1.58` | 48.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.5790 USD [API] | `2026-09-23 10:25:31` |
| `ANNOUNCEMENT` | `INFO` | `1.58` | 2,281.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.28K USD at 1.5790 USD [API] | `2026-09-23 10:25:31` |
| `ANNOUNCEMENT` | `INFO` | `1.55` | 192.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.19K USD at 1.5525 USD [API] | `2026-09-22 08:53:18` |
| `ANNOUNCEMENT` | `INFO` | `1.54` | 242.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.24K USD at 1.5435 USD [API] | `2026-09-21 21:37:17` |
| `ANNOUNCEMENT` | `INFO` | `1.54` | 162.07 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.16K USD at 1.5435 USD [API] | `2026-09-21 21:37:17` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 648.57 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.65K USD at 1.5083 USD [API] | `2026-09-21 14:50:41` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 1,332.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.33K USD at 1.4857 USD [API] | `2026-09-21 08:48:37` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 129.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.13K USD at 1.4857 USD [API] | `2026-09-21 08:48:37` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 1,350.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.35K USD at 1.4427 USD [API] | `2026-09-21 06:20:42` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 1,683.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.68K USD at 1.4427 USD [API] | `2026-09-21 06:20:42` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 3,498.45 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.50K USD at 1.4391 USD [API] | `2026-09-19 05:38:45` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 928.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.93K USD at 1.4391 USD [API] | `2026-09-19 05:38:45` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 9,846.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 9.85K USD at 1.4079 USD [API] | `2026-09-18 19:32:08` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 16,219.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 16.22K USD at 1.2959 USD [API] | `2026-10-29 04:46:54` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 7,775.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.78K USD at 1.2959 USD [API] | `2026-10-29 04:46:54` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 7,775.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.78K USD at 1.2959 USD [API] | `2026-10-29 04:46:54` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 13,384.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 13.38K USD at 1.2959 USD [API] | `2026-10-29 04:46:54` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 288,673.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 288.67K USD at 1.2959 USD [API] | `2026-10-29 04:46:54` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 11,164.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.16K USD at 1.2955 USD [API] | `2026-10-29 04:49:51` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,195.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.20K USD at 1.2969 USD [API] | `2026-10-29 04:58:00` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,951.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.95K USD at 1.3008 USD [API] | `2026-10-29 05:07:52` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 12,049.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 12.05K USD at 1.3031 USD [API] | `2026-10-29 05:15:41` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 5,006.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3031 USD [API] | `2026-10-29 05:17:17` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 7,651.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.65K USD at 1.3032 USD [API] | `2026-10-29 05:17:13` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 5,986.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.99K USD at 1.3032 USD [API] | `2026-10-29 05:21:38` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 29,583.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 29.58K USD at 1.3257 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 2,985.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.99K USD at 1.3257 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 3,999.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3257 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 1,218.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.22K USD at 1.3258 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 3,999.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3258 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 2,908.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.91K USD at 1.3258 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 2,181.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.18K USD at 1.3259 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 3,998.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3259 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 2,909.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.91K USD at 1.3259 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 140.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.14K USD at 1.3259 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 2,617.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.62K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 1,963.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.96K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 1,308.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.31K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 655.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.66K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 1,593.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.59K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 3,999.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 1,657.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.66K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 917.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.92K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 4,999.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 4,999.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 917.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.92K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 917.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.92K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 1,485.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.49K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 4,999.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 2,193.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.19K USD at 1.3260 USD [API] | `2026-10-08 17:24:11` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 5,926.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.93K USD at 1.3587 USD [API] | `2026-10-08 15:23:05` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 247.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.25K USD at 1.3588 USD [API] | `2026-10-08 15:23:05` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 48.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3589 USD [API] | `2026-10-08 15:23:05` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 10.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3589 USD [API] | `2026-10-08 15:23:05` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 2,912.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.91K USD at 1.3589 USD [API] | `2026-10-08 15:23:05` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 2,519.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.52K USD at 1.3589 USD [API] | `2026-10-08 15:23:05` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 13.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3590 USD [API] | `2026-10-08 15:23:05` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 1,359.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.36K USD at 1.3590 USD [API] | `2026-10-08 15:23:05` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 9,804.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.80K USD at 1.3591 USD [API] | `2026-10-08 15:23:05` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 5,327.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.33K USD at 1.3013 USD [API] | `2026-10-29 05:24:17` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 78,897.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 78.90K USD at 1.2905 USD [API] | `2026-10-29 07:45:03` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2938 USD [API] | `2026-10-29 08:19:36` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2938 USD [API] | `2026-10-29 08:19:36` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+2.78%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.86%`)
  * 48H Horizon: Short MP=`1.32` (Vol: 2,300,000.00 USD, Dist: `+4.99%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.88%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+7.15%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.88%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 2,900,000.00 USD, Dist: `+7.03%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.88%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 8,800.00 USD | 64,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 7,270.00 USD | 64,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 14,460.00 USD | 64,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 730.74 USD | 64,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 44,110.00 USD | 64,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 645.07 USD | 64,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 4,910.00 USD | 64,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 31,610.00 USD | 64,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 327.75 USD | 64,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 126,600.00 USD | 64,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 7,440.00 USD | 64,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 825.00 USD | 64,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 502,920.00 USD | 64,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 469.26 USD | 63,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 780.84 USD | 63,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 1,330.00 USD | 63,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 3,700.00 USD | 63,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 16,190.00 USD | 63,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 11,510.00 USD | 63,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 244.34 USD | 63,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 4,900.00 USD | 63,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 581.88 USD | 63,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 289.06 USD | 63,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 13,820.00 USD | 63,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 2,790.00 USD | 63,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 2,290.00 USD | 63,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 151,650.00 USD | 63,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 588.50 USD | 63,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 324.82 USD | 63,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 8,520.00 USD | 63,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 309.06 USD | 63,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 6,350.00 USD | 63,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 31,660.00 USD | 63,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 13,240.00 USD | 63,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 16,880.00 USD | 63,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 36,240.00 USD | 63,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 2,150.00 USD | 63,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 10,750.00 USD | 63,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 19,740.00 USD | 63,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 11,460.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 17,310.00 USD | 63,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 27,430.00 USD | 63,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 30,960.00 USD | 63,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 146,660.00 USD | 63,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 37,890.00 USD | 63,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 70,060.00 USD | 63,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 304,290.00 USD | 63,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 45,360.00 USD | 62,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 53,080.00 USD | 62,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 86,370.00 USD | 62,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 2,440.00 USD | 62,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 5,970.00 USD | 62,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 502,860.00 USD | 62,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 37,440.00 USD | 62,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 2,860,000.00 USD | 62,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 49,150.00 USD | 59,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 20,540.00 USD | 59,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 37,510.00 USD | 59,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 199,730.00 USD | 59,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 61,530.00 USD | 58,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 29,710.00 USD | 58,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 93,340.00 USD | 58,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 356,540.00 USD | 58,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 87,370.00 USD | 58,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 174,440.00 USD | 58,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 121,110.00 USD | 58,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 73,070.00 USD | 57,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 199,270.00 USD | 57,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 129,650.00 USD | 57,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 79,540.00 USD | 57,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,890,000.00 USD | 57,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 151,870.00 USD | 23,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 455,950.00 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 2,690,000.00 USD | 23,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 441,850.00 USD | 20,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 385,710.00 USD | 19,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 53,890.00 USD | 19,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,120,000.00 USD | 19,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 659,030.00 USD | 17,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,480,000.00 USD | 16,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 404,390.00 USD | 15,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.07` | 87,170,000.00 USD | 87,170,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.07` | 946,050.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 463,070.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.09` | 87,170,000.00 USD | 87,170,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 87,130,000.00 USD | 87,130,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 87,030,000.00 USD | 87,030,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.09` | 386,050.00 USD | 13,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.10` | 86,990,000.00 USD | 86,990,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 86,990,000.00 USD | 86,990,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 86,700,000.00 USD | 86,700,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.10` | 102,310.00 USD | 12,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.11` | 86,700,000.00 USD | 86,700,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 86,690,000.00 USD | 86,690,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 86,690,000.00 USD | 86,690,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 295,190.00 USD | 12,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.12` | 86,640,000.00 USD | 86,640,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 78,360,000.00 USD | 78,360,000.00 USD | 3,530.00 USD | 16,050.00 USD | 149,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 86,620,000.00 USD | 86,620,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 78,190,000.00 USD | 78,190,000.00 USD | 15,020.00 USD | 68,320.00 USD | 29,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 78,070,000.00 USD | 78,070,000.00 USD | 5,340.00 USD | 40,010.00 USD | 87,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 86,550,000.00 USD | 86,550,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 77,940,000.00 USD | 77,940,000.00 USD | 5,470.00 USD | 2,460.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 86,520,000.00 USD | 86,520,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,210,000.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 77,860,000.00 USD | 77,860,000.00 USD | 92,060.00 USD | 28,150.00 USD | 50,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 77,690,000.00 USD | 77,690,000.00 USD | 69,610.00 USD | 19,950.00 USD | 166,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 86,310,000.00 USD | 86,310,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 77,430,000.00 USD | 77,430,000.00 USD | 0.00 USD | 107,140.00 USD | 160,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 86,120,000.00 USD | 86,120,000.00 USD | 5,450.00 USD | 2,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 77,170,000.00 USD | 77,170,000.00 USD | 0.00 USD | 13,730.00 USD | 243,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 86,110,000.00 USD | 86,110,000.00 USD | 69,750.00 USD | 93,260.00 USD | 108,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 76,910,000.00 USD | 76,910,000.00 USD | 63,980.00 USD | 70,910.00 USD | 56,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 85,840,000.00 USD | 85,840,000.00 USD | 74,920.00 USD | 97,060.00 USD | 224,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 129,840.00 USD | 10,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.14` | 76,720,000.00 USD | 76,720,000.00 USD | 40,370.00 USD | 125,930.00 USD | 65,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 85,440,000.00 USD | 85,440,000.00 USD | 79,780.00 USD | 88,050.00 USD | 219,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 85,060,000.00 USD | 85,060,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 76,490,000.00 USD | 76,490,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 85,030,000.00 USD | 85,030,000.00 USD | 39,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 76,420,000.00 USD | 76,420,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 84,990,000.00 USD | 84,990,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 76,350,000.00 USD | 76,350,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 84,850,000.00 USD | 84,850,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 524,090.00 USD | 10,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 84,840,000.00 USD | 84,840,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 76,220,000.00 USD | 76,220,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 84,780,000.00 USD | 84,780,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 84,400,000.00 USD | 84,400,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 76,200,000.00 USD | 76,200,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 84,250,000.00 USD | 84,250,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 76,140,000.00 USD | 76,140,000.00 USD | 73,200.00 USD | 45,600.00 USD | 263,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 84,090,000.00 USD | 84,090,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 119,480.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 75,750,000.00 USD | 75,750,000.00 USD | 20,480.00 USD | 25,050.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 83,210,000.00 USD | 83,210,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 75,620,000.00 USD | 75,620,000.00 USD | 122,170.00 USD | 21,140.00 USD | 392,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 82,970,000.00 USD | 82,970,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 75,090,000.00 USD | 75,090,000.00 USD | 212,900.00 USD | 76,950.00 USD | 158,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 82,110,000.00 USD | 82,110,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 74,640,000.00 USD | 74,640,000.00 USD | 270,110.00 USD | 293,490.00 USD | 148,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 81,020,000.00 USD | 81,020,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 73,930,000.00 USD | 73,930,000.00 USD | 179,260.00 USD | 89,000.00 USD | 719,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 79,730,000.00 USD | 79,730,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,290,000.00 USD | 9,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 72,940,000.00 USD | 72,940,000.00 USD | 87,310.00 USD | 70,600.00 USD | 151,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 78,060,000.00 USD | 78,060,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 72,630,000.00 USD | 72,630,000.00 USD | 113,470.00 USD | 166,170.00 USD | 170,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 76,720,000.00 USD | 76,720,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 72,180,000.00 USD | 72,180,000.00 USD | 152,210.00 USD | 22,380.00 USD | 358,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 75,650,000.00 USD | 75,650,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 71,650,000.00 USD | 71,650,000.00 USD | 371,850.00 USD | 5,850.00 USD | 266,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 73,610,000.00 USD | 73,610,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 71,000,000.00 USD | 71,000,000.00 USD | 124,360.00 USD | 130,370.00 USD | 474,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 72,410,000.00 USD | 72,410,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 420,950.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 70,270,000.00 USD | 70,270,000.00 USD | 304,390.00 USD | 85,620.00 USD | 356,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 70,840,000.00 USD | 70,840,000.00 USD | 181,850.00 USD | 100,190.00 USD | 377,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 69,530,000.00 USD | 69,530,000.00 USD | 71,040.00 USD | 84,480.00 USD | 175,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 70,180,000.00 USD | 70,180,000.00 USD | 85,020.00 USD | 74,230.00 USD | 489,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 69,200,000.00 USD | 69,200,000.00 USD | 113,290.00 USD | 10,150.00 USD | 24,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 69,530,000.00 USD | 69,530,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 69,050,000.00 USD | 69,050,000.00 USD | 222,930.00 USD | 10,160.00 USD | 666,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 68,920,000.00 USD | 68,920,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 68,150,000.00 USD | 68,150,000.00 USD | 196,910.00 USD | 73,630.00 USD | 143,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 68,650,000.00 USD | 68,650,000.00 USD | 299,450.00 USD | 571,700.00 USD | 235,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 424,770.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 67,730,000.00 USD | 67,730,000.00 USD | 86,540.00 USD | 511,780.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 67,550,000.00 USD | 67,550,000.00 USD | 76,370.00 USD | 109,420.00 USD | 706,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 67,070,000.00 USD | 67,070,000.00 USD | 365,260.00 USD | 93,260.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 66,650,000.00 USD | 66,650,000.00 USD | 250,710.00 USD | 93,330.00 USD | 585,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 65,040,000.00 USD | 65,040,000.00 USD | 110,600.00 USD | 45,410.00 USD | 319,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 65,730,000.00 USD | 65,730,000.00 USD | 227,280.00 USD | 92,240.00 USD | 795,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 64,570,000.00 USD | 64,570,000.00 USD | 147,820.00 USD | 199,810.00 USD | 469,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 64,610,000.00 USD | 64,610,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 63,750,000.00 USD | 63,750,000.00 USD | 190,850.00 USD | 428,210.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 63,250,000.00 USD | 63,250,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 670,140.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 61,440,000.00 USD | 61,440,000.00 USD | 784,530.00 USD | 121,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 62,420,000.00 USD | 62,420,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 59,320,000.00 USD | 59,320,000.00 USD | 264,550.00 USD | 834,460.00 USD | 657,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 60,830,000.00 USD | 60,830,000.00 USD | 31,150.00 USD | 372,080.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 57,560,000.00 USD | 57,560,000.00 USD | 708,890.00 USD | 419,750.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 57,820,000.00 USD | 57,820,000.00 USD | 736,290.00 USD | 330,310.00 USD | 18,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 54,130,000.00 USD | 54,130,000.00 USD | 137,910.00 USD | 157,180.00 USD | 820,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 56,740,000.00 USD | 56,740,000.00 USD | 264,000.00 USD | 144,630.00 USD | 464,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 53,010,000.00 USD | 53,010,000.00 USD | 526,510.00 USD | 511,570.00 USD | 378,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 55,860,000.00 USD | 55,860,000.00 USD | 47,500.00 USD | 589,990.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 40,050.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 51,600,000.00 USD | 51,600,000.00 USD | 328,050.00 USD | 532,540.00 USD | 467,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 55,220,000.00 USD | 55,220,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 50,270,000.00 USD | 50,270,000.00 USD | 1,660,000.00 USD | 193,480.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 55,200,000.00 USD | 55,200,000.00 USD | 456,280.00 USD | 0.00 USD | 248,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 46,560,000.00 USD | 46,560,000.00 USD | 533,310.00 USD | 413,110.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 54,490,000.00 USD | 54,490,000.00 USD | 257,960.00 USD | 492,370.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 44,490,000.00 USD | 44,490,000.00 USD | 1,410,000.00 USD | 572,260.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 50,660,000.00 USD | 50,660,000.00 USD | 1,230,000.00 USD | 0.00 USD | 369,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 41,320,000.00 USD | 41,320,000.00 USD | 0.00 USD | 90,950.00 USD | 898,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 49,060,000.00 USD | 49,060,000.00 USD | 108,640.00 USD | 0.00 USD | 910,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 27,240.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.22` | 40,330,000.00 USD | 40,330,000.00 USD | 226,520.00 USD | 85,640.00 USD | 680,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 48,040,000.00 USD | 48,040,000.00 USD | 142,210.00 USD | 9,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 39,340,000.00 USD | 39,340,000.00 USD | 143,650.00 USD | 4,200.00 USD | 183,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 47,890,000.00 USD | 47,890,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 39,010,000.00 USD | 39,010,000.00 USD | 222,150.00 USD | 97,750.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 47,150,000.00 USD | 47,150,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 38,680,000.00 USD | 38,680,000.00 USD | 113,990.00 USD | 273,720.00 USD | 435,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 46,070,000.00 USD | 46,070,000.00 USD | 0.00 USD | 164,230.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 37,860,000.00 USD | 37,860,000.00 USD | 123,900.00 USD | 0.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 45,890,000.00 USD | 45,890,000.00 USD | 51,610.00 USD | 166,160.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 6,710,000.00 USD | 6,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.23` | 35,100,000.00 USD | 35,100,000.00 USD | 281,350.00 USD | 575,430.00 USD | 223,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 45,640,000.00 USD | 45,640,000.00 USD | 112,770.00 USD | 535,430.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 34,020,000.00 USD | 34,020,000.00 USD | 452,620.00 USD | 578,850.00 USD | 389,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 44,980,000.00 USD | 44,980,000.00 USD | 59,160.00 USD | 950,550.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 32,600,000.00 USD | 32,600,000.00 USD | 170,630.00 USD | 1,010,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 43,950,000.00 USD | 43,950,000.00 USD | 198,530.00 USD | 888,470.00 USD | 807,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 28,280,000.00 USD | 28,280,000.00 USD | 1,190,000.00 USD | 1,100,000.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 42,050,000.00 USD | 42,050,000.00 USD | 1,020,000.00 USD | 963,040.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 22,410,000.00 USD | 22,410,000.00 USD | 340,470.00 USD | 1,190,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 38,750,000.00 USD | 38,750,000.00 USD | 1,460,000.00 USD | 1,820,000.00 USD | 3,860,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 365.56 USD | 1,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 19,030,000.00 USD | 19,030,000.00 USD | 189,670.00 USD | 885,210.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 31,610,000.00 USD | 31,610,000.00 USD | 2,040,000.00 USD | 1,800,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 16,950,000.00 USD | 16,950,000.00 USD | 33,830.00 USD | 224,610.00 USD | 61,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 26,080,000.00 USD | 26,080,000.00 USD | 2,630,000.00 USD | 1,580,000.00 USD | 3,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 16,630,000.00 USD | 16,630,000.00 USD | 618,430.00 USD | 187,820.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 18,380,000.00 USD | 18,380,000.00 USD | 2,070,000.00 USD | 950,140.00 USD | 535,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 14,270,000.00 USD | 14,270,000.00 USD | 319,740.00 USD | 812,380.00 USD | 36,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 14,820,000.00 USD | 14,820,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 13,100,000.00 USD | 13,100,000.00 USD | 1,810,000.00 USD | 5,660.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 13,690,000.00 USD | 13,690,000.00 USD | 1,420,000.00 USD | 15,000.00 USD | 992,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 8,940,000.00 USD | 8,940,000.00 USD | 851,070.00 USD | 389,970.00 USD | 746,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 11,270,000.00 USD | 11,270,000.00 USD | 3,370,000.00 USD | 337,070.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 6,960,000.00 USD | 6,960,000.00 USD | 133,680.00 USD | 890,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 5,270,000.00 USD | 5,270,000.00 USD | 1,630,000.00 USD | 325,530.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 4,500,000.00 USD | 4,500,000.00 USD | 331,570.00 USD | 171,540.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 9,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 2,990,000.00 USD | 2,990,000.00 USD | 220,120.00 USD | 3,370.00 USD | 192,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 455,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 10,370.00 USD | 669,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 1,370,000.00 USD | 1,370,000.00 USD | 63,660.00 USD | 7,340.00 USD | 878,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 1,530.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.26` | 1,890,000.00 USD | 1,890,000.00 USD | 1,570,000.00 USD | 284,390.00 USD | 39,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 423,470.00 USD | 423,470.00 USD | 150,010.00 USD | 273,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 261,340.00 USD | 261,340.00 USD | 69,930.00 USD | 191,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 522,670.00 USD | 522,670.00 USD | 69,930.00 USD | 191,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 19,840.00 USD | 19,840.00 USD | 0.00 USD | 19,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 39,670.00 USD | 39,670.00 USD | 0.00 USD | 19,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 783,460.00 USD | 783,460.00 USD | 208,340.00 USD | 27,670.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 132,130.00 USD | 132,130.00 USD | 0.00 USD | 10,110.00 USD | 82,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 2,510,000.00 USD | 2,510,000.00 USD | 755,130.00 USD | 100,700.00 USD | 872,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 1,450,000.00 USD | 1,450,000.00 USD | 144,170.00 USD | 26,950.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 6,330,000.00 USD | 6,330,000.00 USD | 772,130.00 USD | 1,180,000.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 6,900,000.00 USD | 6,900,000.00 USD | 834,020.00 USD | 925,190.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 116,940.00 USD | 116,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.27` | 11,230,000.00 USD | 11,230,000.00 USD | 1,040,000.00 USD | 1,310,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 22,950,000.00 USD | 22,950,000.00 USD | 4,260,000.00 USD | 3,030,000.00 USD | 8,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 14,690,000.00 USD | 14,690,000.00 USD | 198,110.00 USD | 1,950,000.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 28,700,000.00 USD | 28,700,000.00 USD | 0.00 USD | 1,360,000.00 USD | 4,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 20,070,000.00 USD | 20,070,000.00 USD | 960,010.00 USD | 1,020,000.00 USD | 3,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 32,720,000.00 USD | 32,720,000.00 USD | 138,500.00 USD | 2,540,000.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 23,440,000.00 USD | 23,440,000.00 USD | 1,050,000.00 USD | 988,040.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 40,410,000.00 USD | 40,410,000.00 USD | 1,280,000.00 USD | 4,950,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 29,660,000.00 USD | 29,660,000.00 USD | 818,720.00 USD | 1,810,000.00 USD | 3,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 54,520,000.00 USD | 54,520,000.00 USD | 2,710,000.00 USD | 2,870,000.00 USD | 8,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 15,420.00 USD | 132,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 35,100,000.00 USD | 35,100,000.00 USD | 982,470.00 USD | 2,090,000.00 USD | 2,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 68,160,000.00 USD | 68,160,000.00 USD | 4,660,000.00 USD | 2,810,000.00 USD | 6,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 45,650,000.00 USD | 45,650,000.00 USD | 4,660,000.00 USD | 1,640,000.00 USD | 4,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 85,270,000.00 USD | 85,270,000.00 USD | 7,780,000.00 USD | 3,210,000.00 USD | 6,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 48,420,000.00 USD | 48,420,000.00 USD | 237,040.00 USD | 1,810,000.00 USD | 729,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 86,790,000.00 USD | 86,790,000.00 USD | 0.00 USD | 1,440,000.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 51,280,000.00 USD | 51,280,000.00 USD | 846,340.00 USD | 100,660.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 88,430,000.00 USD | 88,430,000.00 USD | 1,030,000.00 USD | 30,200.00 USD | 582,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 53,970,000.00 USD | 53,970,000.00 USD | 985,220.00 USD | 490,930.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 91,820,000.00 USD | 91,820,000.00 USD | 902,470.00 USD | 1,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 37,070.00 USD | 169,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 57,350,000.00 USD | 57,350,000.00 USD | 683,710.00 USD | 899,070.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 95,320,000.00 USD | 95,320,000.00 USD | 796,960.00 USD | 1,290,000.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 58,470,000.00 USD | 58,470,000.00 USD | 584,100.00 USD | 427,810.00 USD | 106,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 95,800,000.00 USD | 95,800,000.00 USD | 440,460.00 USD | 2,730.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 58,660,000.00 USD | 58,660,000.00 USD | 95,060.00 USD | 36,830.00 USD | 58,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 96,380,000.00 USD | 96,380,000.00 USD | 70,460.00 USD | 4,320.00 USD | 510,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 60,800,000.00 USD | 60,800,000.00 USD | 378,690.00 USD | 14,980.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 98,470,000.00 USD | 98,470,000.00 USD | 1,040,000.00 USD | 202,640.00 USD | 846,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 64,940,000.00 USD | 64,940,000.00 USD | 1,170,000.00 USD | 375,550.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 102,110,000.00 USD | 102,110,000.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 11,740.00 USD | 181,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 70,220,000.00 USD | 70,220,000.00 USD | 1,460,000.00 USD | 1,240,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 109,400,000.00 USD | 109,400,000.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 71,350,000.00 USD | 71,350,000.00 USD | 464,690.00 USD | 20,370.00 USD | 647,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 111,350,000.00 USD | 111,350,000.00 USD | 25,800.00 USD | 172,080.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 72,650,000.00 USD | 72,650,000.00 USD | 203,220.00 USD | 344,440.00 USD | 752,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 113,350,000.00 USD | 113,350,000.00 USD | 208,510.00 USD | 298,720.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 75,270,000.00 USD | 75,270,000.00 USD | 726,640.00 USD | 871,770.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 114,380,000.00 USD | 114,380,000.00 USD | 85,960.00 USD | 944,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 76,380,000.00 USD | 76,380,000.00 USD | 366,890.00 USD | 250,070.00 USD | 487,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 116,910,000.00 USD | 116,910,000.00 USD | 0.00 USD | 2,040,000.00 USD | 485,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 1,630.00 USD | 182,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 77,930,000.00 USD | 77,930,000.00 USD | 493,480.00 USD | 507,360.00 USD | 549,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 118,860,000.00 USD | 118,860,000.00 USD | 1,770,000.00 USD | 183,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 81,310,000.00 USD | 81,310,000.00 USD | 895,610.00 USD | 341,920.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 123,790,000.00 USD | 123,790,000.00 USD | 1,450,000.00 USD | 821,310.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 84,330,000.00 USD | 84,330,000.00 USD | 1,150,000.00 USD | 326,160.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 126,190,000.00 USD | 126,190,000.00 USD | 1,340,000.00 USD | 408,300.00 USD | 647,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 86,710,000.00 USD | 86,710,000.00 USD | 910,680.00 USD | 566,230.00 USD | 908,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 130,530,000.00 USD | 130,530,000.00 USD | 189,510.00 USD | 858,660.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 88,070,000.00 USD | 88,070,000.00 USD | 437,800.00 USD | 146,840.00 USD | 767,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 131,700,000.00 USD | 131,700,000.00 USD | 515,950.00 USD | 151,320.00 USD | 501,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 91,470,000.00 USD | 91,470,000.00 USD | 195,170.00 USD | 875,040.00 USD | 2,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 135,910,000.00 USD | 135,910,000.00 USD | 68,520.00 USD | 1,750,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 98,080,000.00 USD | 98,080,000.00 USD | 2,070,000.00 USD | 957,920.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 140,760,000.00 USD | 140,760,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 101,030,000.00 USD | 101,030,000.00 USD | 1,570,000.00 USD | 414,530.00 USD | 962,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 142,780,000.00 USD | 142,780,000.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 104,470,000.00 USD | 104,470,000.00 USD | 1,310,000.00 USD | 757,740.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 146,130,000.00 USD | 146,130,000.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 106,320,000.00 USD | 106,320,000.00 USD | 914,960.00 USD | 83,530.00 USD | 851,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 148,910,000.00 USD | 148,910,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 41,770.00 USD | 224,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 107,360,000.00 USD | 107,360,000.00 USD | 405,790.00 USD | 56,240.00 USD | 578,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 150,720,000.00 USD | 150,720,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 108,570,000.00 USD | 108,570,000.00 USD | 545,530.00 USD | 170,390.00 USD | 494,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 151,820,000.00 USD | 151,820,000.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 110,270,000.00 USD | 110,270,000.00 USD | 729,070.00 USD | 105,530.00 USD | 862,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 153,530,000.00 USD | 153,530,000.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 112,090,000.00 USD | 112,090,000.00 USD | 465,720.00 USD | 179,640.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 155,990,000.00 USD | 155,990,000.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 113,940,000.00 USD | 113,940,000.00 USD | 783,210.00 USD | 229,580.00 USD | 838,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 158,020,000.00 USD | 158,020,000.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,950.00 USD | 226,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 115,050,000.00 USD | 115,050,000.00 USD | 286,040.00 USD | 208,270.00 USD | 616,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 159,570,000.00 USD | 159,570,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 115,640,000.00 USD | 115,640,000.00 USD | 289,820.00 USD | 80,370.00 USD | 215,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 162,000,000.00 USD | 162,000,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 116,510,000.00 USD | 116,510,000.00 USD | 353,910.00 USD | 145,200.00 USD | 374,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 163,870,000.00 USD | 163,870,000.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 118,380,000.00 USD | 118,380,000.00 USD | 932,000.00 USD | 374,950.00 USD | 560,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 169,390,000.00 USD | 169,390,000.00 USD | 2,380,000.00 USD | 2,480,000.00 USD | 660,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 120,450,000.00 USD | 120,450,000.00 USD | 820,840.00 USD | 470,890.00 USD | 777,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 176,800,000.00 USD | 176,800,000.00 USD | 2,000,000.00 USD | 2,170,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 3,630.00 USD | 230,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 121,400,000.00 USD | 121,400,000.00 USD | 374,110.00 USD | 172,120.00 USD | 401,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 185,940,000.00 USD | 185,940,000.00 USD | 3,530,000.00 USD | 1,720,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 122,140,000.00 USD | 122,140,000.00 USD | 263,580.00 USD | 78,220.00 USD | 400,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 194,490,000.00 USD | 194,490,000.00 USD | 3,010,000.00 USD | 1,930,000.00 USD | 3,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 122,530,000.00 USD | 122,530,000.00 USD | 200,720.00 USD | 40,980.00 USD | 146,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 202,510,000.00 USD | 202,510,000.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 122,800,000.00 USD | 122,800,000.00 USD | 69,740.00 USD | 28,660.00 USD | 174,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 211,630,000.00 USD | 211,630,000.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 123,110,000.00 USD | 123,110,000.00 USD | 105,080.00 USD | 3,170.00 USD | 194,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 218,380,000.00 USD | 218,380,000.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 34,090.00 USD | 264,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 123,930,000.00 USD | 123,930,000.00 USD | 335,960.00 USD | 65,930.00 USD | 426,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 224,720,000.00 USD | 224,720,000.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 124,440,000.00 USD | 124,440,000.00 USD | 148,530.00 USD | 42,970.00 USD | 310,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 227,270,000.00 USD | 227,270,000.00 USD | 1,060,000.00 USD | 639,580.00 USD | 849,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 124,990,000.00 USD | 124,990,000.00 USD | 269,010.00 USD | 49,330.00 USD | 234,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 230,370,000.00 USD | 230,370,000.00 USD | 1,460,000.00 USD | 414,770.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 125,520,000.00 USD | 125,520,000.00 USD | 143,090.00 USD | 115,680.00 USD | 276,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 234,160,000.00 USD | 234,160,000.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 125,620,000.00 USD | 125,620,000.00 USD | 78,610.00 USD | 14,730.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 236,920,000.00 USD | 236,920,000.00 USD | 1,430,000.00 USD | 616,140.00 USD | 713,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 193,360.00 USD | 457,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 125,890,000.00 USD | 125,890,000.00 USD | 56,040.00 USD | 1,320.00 USD | 206,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 237,730,000.00 USD | 237,730,000.00 USD | 206,650.00 USD | 190,380.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 126,120,000.00 USD | 126,120,000.00 USD | 97,000.00 USD | 109,930.00 USD | 29,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 238,840,000.00 USD | 238,840,000.00 USD | 535,200.00 USD | 181,120.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 126,130,000.00 USD | 126,130,000.00 USD | 0.00 USD | 10,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 240,320,000.00 USD | 240,320,000.00 USD | 410,950.00 USD | 339,760.00 USD | 733,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 126,260,000.00 USD | 126,260,000.00 USD | 5,340.00 USD | 29,850.00 USD | 87,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 241,930,000.00 USD | 241,930,000.00 USD | 553,200.00 USD | 231,700.00 USD | 820,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 126,340,000.00 USD | 126,340,000.00 USD | 5,470.00 USD | 2,460.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 243,850,000.00 USD | 243,850,000.00 USD | 619,020.00 USD | 407,640.00 USD | 893,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 64,420.00 USD | 522,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.38` | 126,510,000.00 USD | 126,510,000.00 USD | 92,060.00 USD | 28,150.00 USD | 50,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 245,080,000.00 USD | 245,080,000.00 USD | 360,280.00 USD | 277,980.00 USD | 586,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 126,760,000.00 USD | 126,760,000.00 USD | 69,610.00 USD | 19,950.00 USD | 166,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 246,540,000.00 USD | 246,540,000.00 USD | 692,200.00 USD | 267,730.00 USD | 499,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 126,890,000.00 USD | 126,890,000.00 USD | 0.00 USD | 41,620.00 USD | 81,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 248,180,000.00 USD | 248,180,000.00 USD | 436,360.00 USD | 142,590.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 127,030,000.00 USD | 127,030,000.00 USD | 0.00 USD | 65,520.00 USD | 78,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 250,040,000.00 USD | 250,040,000.00 USD | 710,620.00 USD | 348,810.00 USD | 802,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 127,290,000.00 USD | 127,290,000.00 USD | 0.00 USD | 13,730.00 USD | 243,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 250,930,000.00 USD | 250,930,000.00 USD | 403,730.00 USD | 253,120.00 USD | 228,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,280.00 USD | 523,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 127,480,000.00 USD | 127,480,000.00 USD | 63,980.00 USD | 70,910.00 USD | 56,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 251,950,000.00 USD | 251,950,000.00 USD | 377,810.00 USD | 231,880.00 USD | 413,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 127,710,000.00 USD | 127,710,000.00 USD | 40,370.00 USD | 125,320.00 USD | 65,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 253,010,000.00 USD | 253,010,000.00 USD | 384,080.00 USD | 308,280.00 USD | 366,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 253,760,000.00 USD | 253,760,000.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 254,090,000.00 USD | 254,090,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 254,150,000.00 USD | 254,150,000.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 2,090.00 USD | 525,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,370,000.00 USD | 254,370,000.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,380,000.00 USD | 254,380,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,440,000.00 USD | 254,440,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,520,000.00 USD | 254,520,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,820,000.00 USD | 254,820,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 635.06 USD | 526,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 254,970,000.00 USD | 254,970,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 255,130,000.00 USD | 255,130,000.00 USD | 13,200.00 USD | 17,670.00 USD | 126,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 255,410,000.00 USD | 255,410,000.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,930.00 USD | 529,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,510.00 USD | 623,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 988.72 USD | 624,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 561,440.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 128,580.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 500.03 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,150.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 25,060.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 174.99 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 1,370.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 679.21 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,900.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 4,240,000.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 1,510.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 2,660.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 271.38 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 4,890.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 2,350.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 134,550.00 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 120.60 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 8,130.00 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 974.62 USD | 5,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 3,210.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,730.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,460.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 5,140,000.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 130,410.00 USD | 11,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 2,690.00 USD | 11,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 4,500.00 USD | 11,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 15,410.00 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 260.98 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 186,300.00 USD | 11,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 2,830,000.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 428.50 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,980,000.00 USD | 17,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,190.00 USD | 17,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 373.38 USD | 17,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 40,810.00 USD | 17,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 313,150.00 USD | 17,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.95` | 680.75 USD | 17,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 17,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 227,560.00 USD | 17,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 17,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 940.34 USD | 17,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 419,270.00 USD | 18,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 198.36 USD | 18,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 369.90 USD | 18,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 4,940.00 USD | 18,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 1,240.00 USD | 18,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 469.42 USD | 18,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 251,210.00 USD | 18,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 79,940.00 USD | 18,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,090.00 USD | 18,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 52,220.00 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 101.43 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 440.78 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 11,570.00 USD | 18,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 75,430.00 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 45,670.00 USD | 18,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 105.57 USD | 18,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 248.94 USD | 18,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 1,540.00 USD | 18,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 14,690.00 USD | 18,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 3,550,000.00 USD | 22,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 146.01 USD | 22,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 90,810.00 USD | 22,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 2,380.00 USD | 22,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 2,260.00 USD | 22,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 707.07 USD | 22,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 847.66 USD | 22,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 24,250.00 USD | 22,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 158.28 USD | 22,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 22,490.00 USD | 22,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 473.81 USD | 22,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 4,490.00 USD | 22,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 1,520,000.00 USD | 23,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 95,670.00 USD | 23,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 748.50 USD | 23,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 115.23 USD | 23,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 213,880.00 USD | 24,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 64,560,000.00 USD | 0.00 USD | 8,800.00 USD | `-79.77%` | `34,524.00` |
| `Live` | `Long` | `0.2650` | 64,550,000.00 USD | 0.00 USD | 7,270.00 USD | `-78.97%` | `27,436.00` |
| `Live` | `Long` | `0.2750` | 64,540,000.00 USD | 0.00 USD | 14,460.00 USD | `-78.18%` | `52,593.00` |
| `Live` | `Long` | `0.2850` | 64,520,000.00 USD | 0.00 USD | 730.74 USD | `-77.39%` | `2,564.00` |
| `Live` | `Long` | `0.2950` | 64,520,000.00 USD | 0.00 USD | 44,110.00 USD | `-76.59%` | `149,530.00` |
| `Live` | `Long` | `0.3050` | 64,480,000.00 USD | 0.00 USD | 645.07 USD | `-75.80%` | `2,115.00` |
| `Live` | `Long` | `0.3150` | 64,480,000.00 USD | 0.00 USD | 4,910.00 USD | `-75.01%` | `15,577.00` |
| `Live` | `Long` | `0.3250` | 64,470,000.00 USD | 0.00 USD | 31,610.00 USD | `-74.21%` | `97,270.00` |
| `Live` | `Long` | `0.3450` | 64,440,000.00 USD | 0.00 USD | 327.75 USD | `-72.63%` | `950.00` |
| `Live` | `Long` | `0.3550` | 64,440,000.00 USD | 0.00 USD | 126,600.00 USD | `-71.83%` | `356,625.00` |
| `Live` | `Long` | `0.3650` | 64,320,000.00 USD | 0.00 USD | 7,440.00 USD | `-71.04%` | `20,395.00` |
| `Live` | `Long` | `0.3750` | 64,310,000.00 USD | 0.00 USD | 825.00 USD | `-70.25%` | `2,200.00` |
| `Live` | `Long` | `0.3850` | 64,310,000.00 USD | 0.00 USD | 502,920.00 USD | `-69.45%` | `1,306,284.00` |
| `Live` | `Long` | `0.3950` | 63,800,000.00 USD | 0.00 USD | 469.26 USD | `-68.66%` | `1,188.00` |
| `Live` | `Long` | `0.4050` | 63,800,000.00 USD | 0.00 USD | 780.84 USD | `-67.87%` | `1,928.00` |
| `Live` | `Long` | `0.4150` | 63,800,000.00 USD | 0.00 USD | 1,330.00 USD | `-67.07%` | `3,214.00` |
| `Live` | `Long` | `0.4250` | 63,800,000.00 USD | 0.00 USD | 3,700.00 USD | `-66.28%` | `8,700.00` |
| `Live` | `Long` | `0.4350` | 63,800,000.00 USD | 0.00 USD | 16,190.00 USD | `-65.49%` | `37,219.00` |
| `Live` | `Long` | `0.4450` | 63,780,000.00 USD | 0.00 USD | 11,510.00 USD | `-64.69%` | `25,873.00` |
| `Live` | `Long` | `0.4550` | 63,770,000.00 USD | 0.00 USD | 244.34 USD | `-63.90%` | `537.00` |
| `Live` | `Long` | `0.4650` | 63,770,000.00 USD | 0.00 USD | 4,900.00 USD | `-63.11%` | `10,537.00` |
| `Live` | `Long` | `0.4750` | 63,770,000.00 USD | 0.00 USD | 581.88 USD | `-62.31%` | `1,225.00` |
| `Live` | `Long` | `0.4850` | 63,760,000.00 USD | 0.00 USD | 289.06 USD | `-61.52%` | `596.00` |
| `Live` | `Long` | `0.4950` | 63,760,000.00 USD | 0.00 USD | 13,820.00 USD | `-60.73%` | `27,925.00` |
| `Live` | `Long` | `0.5050` | 63,750,000.00 USD | 0.00 USD | 2,790.00 USD | `-59.93%` | `5,527.00` |
| `Live` | `Long` | `0.5150` | 63,750,000.00 USD | 0.00 USD | 2,290.00 USD | `-59.14%` | `4,443.00` |
| `Live` | `Long` | `0.5250` | 63,750,000.00 USD | 0.00 USD | 151,650.00 USD | `-58.35%` | `288,866.00` |
| `Live` | `Long` | `0.5350` | 63,590,000.00 USD | 0.00 USD | 588.50 USD | `-57.55%` | `1,100.00` |
| `Live` | `Long` | `0.5450` | 63,590,000.00 USD | 0.00 USD | 324.82 USD | `-56.76%` | `596.00` |
| `Live` | `Long` | `0.5550` | 63,590,000.00 USD | 0.00 USD | 8,520.00 USD | `-55.97%` | `15,350.00` |
| `Live` | `Long` | `0.5650` | 63,580,000.00 USD | 0.00 USD | 309.06 USD | `-55.17%` | `547.00` |
| `Live` | `Long` | `0.5750` | 63,580,000.00 USD | 0.00 USD | 6,350.00 USD | `-54.38%` | `11,052.00` |
| `Live` | `Long` | `0.5850` | 63,580,000.00 USD | 0.00 USD | 31,660.00 USD | `-53.59%` | `54,118.00` |
| `Live` | `Long` | `0.5950` | 63,550,000.00 USD | 0.00 USD | 13,240.00 USD | `-52.79%` | `22,258.00` |
| `Live` | `Long` | `0.6050` | 63,530,000.00 USD | 0.00 USD | 16,880.00 USD | `-52.00%` | `27,899.00` |
| `Live` | `Long` | `0.6150` | 63,520,000.00 USD | 0.00 USD | 36,240.00 USD | `-51.21%` | `58,922.00` |
| `Live` | `Long` | `0.6250` | 63,480,000.00 USD | 0.00 USD | 2,150.00 USD | `-50.41%` | `3,446.00` |
| `Live` | `Long` | `0.6350` | 63,480,000.00 USD | 0.00 USD | 10,750.00 USD | `-49.62%` | `16,934.00` |
| `Live` | `Long` | `0.6450` | 63,470,000.00 USD | 0.00 USD | 19,740.00 USD | `-48.83%` | `30,597.00` |
| `Live` | `Long` | `0.6550` | 63,450,000.00 USD | 0.00 USD | 11,460.00 USD | `-48.03%` | `17,501.00` |
| `Live` | `Long` | `0.6650` | 63,440,000.00 USD | 0.00 USD | 17,310.00 USD | `-47.24%` | `26,027.00` |
| `Live` | `Long` | `0.6750` | 63,420,000.00 USD | 0.00 USD | 27,430.00 USD | `-46.45%` | `40,639.00` |
| `Live` | `Long` | `0.6850` | 63,390,000.00 USD | 0.00 USD | 30,960.00 USD | `-45.65%` | `45,204.00` |
| `Live` | `Long` | `0.6950` | 63,360,000.00 USD | 0.00 USD | 146,660.00 USD | `-44.86%` | `211,016.00` |
| `Live` | `Long` | `0.7050` | 63,210,000.00 USD | 0.00 USD | 37,890.00 USD | `-44.07%` | `53,747.00` |
| `Live` | `Long` | `0.7150` | 63,180,000.00 USD | 0.00 USD | 70,060.00 USD | `-43.27%` | `97,985.00` |
| `Live` | `Long` | `0.7250` | 63,110,000.00 USD | 0.00 USD | 304,290.00 USD | `-42.48%` | `419,704.00` |
| `Live` | `Long` | `0.7350` | 62,800,000.00 USD | 0.00 USD | 45,360.00 USD | `-41.69%` | `61,711.00` |
| `Live` | `Long` | `0.7450` | 62,760,000.00 USD | 0.00 USD | 53,080.00 USD | `-40.89%` | `71,250.00` |
| `Live` | `Long` | `0.7550` | 62,700,000.00 USD | 0.00 USD | 86,370.00 USD | `-40.10%` | `114,392.00` |
| `Live` | `Long` | `0.7650` | 62,620,000.00 USD | 0.00 USD | 2,440.00 USD | `-39.30%` | `3,184.00` |
| `Live` | `Long` | `0.7750` | 62,610,000.00 USD | 0.00 USD | 5,970.00 USD | `-38.51%` | `7,699.00` |
| `Live` | `Long` | `0.7850` | 62,610,000.00 USD | 0.00 USD | 502,860.00 USD | `-37.72%` | `640,590.00` |
| `Live` | `Long` | `0.7950` | 62,100,000.00 USD | 0.00 USD | 37,440.00 USD | `-36.92%` | `47,089.00` |
| `Live` | `Long` | `0.8050` | 62,070,000.00 USD | 0.00 USD | 2,860,000.00 USD | `-36.13%` | `3,554,084.00` |
| `Live` | `Long` | `0.8150` | 59,210,000.00 USD | 0.00 USD | 49,150.00 USD | `-35.34%` | `60,308.00` |
| `Live` | `Long` | `0.8250` | 59,160,000.00 USD | 0.00 USD | 20,540.00 USD | `-34.54%` | `24,898.00` |
| `Live` | `Long` | `0.8350` | 59,140,000.00 USD | 0.00 USD | 37,510.00 USD | `-33.75%` | `44,922.00` |
| `Live` | `Long` | `0.8450` | 59,100,000.00 USD | 0.00 USD | 199,730.00 USD | `-32.96%` | `236,362.00` |
| `Live` | `Long` | `0.8550` | 58,900,000.00 USD | 0.00 USD | 61,530.00 USD | `-32.16%` | `71,961.00` |
| `Live` | `Long` | `0.8650` | 58,840,000.00 USD | 0.00 USD | 29,710.00 USD | `-31.37%` | `34,347.00` |
| `Live` | `Long` | `0.8750` | 58,810,000.00 USD | 0.00 USD | 93,340.00 USD | `-30.58%` | `106,673.00` |
| `Live` | `Long` | `0.8850` | 58,710,000.00 USD | 0.00 USD | 356,540.00 USD | `-29.78%` | `402,870.00` |
| `Live` | `Long` | `0.8950` | 58,360,000.00 USD | 0.00 USD | 87,370.00 USD | `-28.99%` | `97,619.00` |
| `Live` | `Long` | `0.9050` | 58,270,000.00 USD | 0.00 USD | 174,440.00 USD | `-28.20%` | `192,749.00` |
| `Live` | `Long` | `0.9150` | 58,100,000.00 USD | 0.00 USD | 121,110.00 USD | `-27.40%` | `132,361.00` |
| `Live` | `Long` | `0.9250` | 57,980,000.00 USD | 0.00 USD | 73,070.00 USD | `-26.61%` | `78,996.00` |
| `Live` | `Long` | `0.9350` | 57,900,000.00 USD | 0.00 USD | 199,270.00 USD | `-25.82%` | `213,126.00` |
| `Live` | `Long` | `0.9450` | 57,700,000.00 USD | 0.00 USD | 129,650.00 USD | `-25.02%` | `137,195.00` |
| `Live` | `Long` | `0.9550` | 57,570,000.00 USD | 0.00 USD | 79,540.00 USD | `-24.23%` | `83,289.00` |
| `Live` | `Long` | `0.9650` | 57,490,000.00 USD | 0.00 USD | 33,890,000.00 USD | `-23.44%` | `35,117,109.00` |
| `Live` | `Long` | `0.9750` | 23,610,000.00 USD | 0.00 USD | 151,870.00 USD | `-22.64%` | `155,766.00` |
| `Live` | `Long` | `0.9850` | 23,450,000.00 USD | 0.00 USD | 455,950.00 USD | `-21.85%` | `462,891.00` |
| `Live` | `Long` | `0.9950` | 23,000,000.00 USD | 0.00 USD | 2,690,000.00 USD | `-21.06%` | `2,703,948.00` |
| `Live` | `Long` | `1.00` | 20,310,000.00 USD | 0.00 USD | 441,850.00 USD | `-20.26%` | `439,651.00` |
| `Live` | `Long` | `1.01` | 19,870,000.00 USD | 0.00 USD | 385,710.00 USD | `-19.47%` | `380,014.00` |
| `Live` | `Long` | `1.02` | 19,480,000.00 USD | 0.00 USD | 53,890.00 USD | `-18.68%` | `52,571.00` |
| `Live` | `Long` | `1.03` | 19,430,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-17.88%` | `2,051,140.00` |
| `Live` | `Long` | `1.04` | 17,300,000.00 USD | 0.00 USD | 659,030.00 USD | `-17.09%` | `630,652.00` |
| `Live` | `Long` | `1.05` | 16,640,000.00 USD | 0.00 USD | 1,480,000.00 USD | `-16.30%` | `1,400,077.00` |
| `Live` | `Long` | `1.06` | 15,170,000.00 USD | 0.00 USD | 404,390.00 USD | `-15.50%` | `379,713.00` |
| `Live` | `Long` | `1.07` | 14,760,000.00 USD | 0.00 USD | 946,050.00 USD | `-14.71%` | `880,046.00` |
| `Live` | `Long` | `1.08` | 13,820,000.00 USD | 0.00 USD | 463,070.00 USD | `-13.92%` | `426,797.00` |
| `Live` | `Long` | `1.09` | 13,350,000.00 USD | 0.00 USD | 386,050.00 USD | `-13.12%` | `352,558.00` |
| `Live` | `Long` | `1.10` | 12,970,000.00 USD | 0.00 USD | 102,310.00 USD | `-12.33%` | `92,590.00` |
| `Live` | `Long` | `1.11` | 12,870,000.00 USD | 0.00 USD | 295,190.00 USD | `-11.54%` | `264,746.00` |
| `Live` | `Long` | `1.12` | 12,570,000.00 USD | 0.00 USD | 2,210,000.00 USD | `-10.74%` | `1,961,407.00` |
| `Live` | `Long` | `1.14` | 10,360,000.00 USD | 0.00 USD | 129,840.00 USD | `-9.95%` | `114,400.00` |
| `Live` | `Long` | `1.15` | 10,230,000.00 USD | 0.00 USD | 524,090.00 USD | `-9.16%` | `457,717.00` |
| `Live` | `Long` | `1.16` | 9,710,000.00 USD | 0.00 USD | 119,480.00 USD | `-8.36%` | `103,442.00` |
| `Live` | `Long` | `1.17` | 9,590,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-7.57%` | `1,108,309.00` |
| `Live` | `Long` | `1.18` | 8,300,000.00 USD | 0.00 USD | 420,950.00 USD | `-6.78%` | `358,258.00` |
| `Live` | `Long` | `1.19` | 7,880,000.00 USD | 0.00 USD | 424,770.00 USD | `-5.98%` | `358,459.00` |
| `Live` | `Long` | `1.20` | 7,450,000.00 USD | 0.00 USD | 670,140.00 USD | `-5.19%` | `560,785.00` |
| `Live` | `Long` | `1.21` | 6,780,000.00 USD | 0.00 USD | 40,050.00 USD | `-4.40%` | `33,233.00` |
| `Live` | `Long` | `1.22` | 6,740,000.00 USD | 0.00 USD | 27,240.00 USD | `-3.60%` | `22,422.00` |
| `Live` | `Long` | `1.23` | 6,720,000.00 USD | 0.00 USD | 6,710,000.00 USD | `-2.81%` | `5,480,769.00` |
| `Live` | `Long` | `1.24` | 1,900.00 USD | 0.00 USD | 365.56 USD | `-2.02%` | `296.00` |
| `Live` | `Long` | `1.25` | 1,530.00 USD | 0.00 USD | 1,530.00 USD | `-0.43%` | `1,219.00` |
| `Live` | `Short` | `1.26` | 116,940.00 USD | 116,940.00 USD | 0.00 USD | `+0.36%` | `92,442.00` |
| `Live` | `Short` | `1.27` | 132,360.00 USD | 15,420.00 USD | 0.00 USD | `+1.16%` | `12,095.00` |
| `Live` | `Short` | `1.28` | 169,430.00 USD | 37,070.00 USD | 0.00 USD | `+1.95%` | `28,847.00` |
| `Live` | `Short` | `1.29` | 181,170.00 USD | 11,740.00 USD | 0.00 USD | `+2.75%` | `9,069.00` |
| `Live` | `Short` | `1.30` | 182,800.00 USD | 1,630.00 USD | 0.00 USD | `+3.54%` | `1,246.00` |
| `Live` | `Short` | `1.32` | 224,570.00 USD | 41,770.00 USD | 0.00 USD | `+5.13%` | `31,526.00` |
| `Live` | `Short` | `1.33` | 226,520.00 USD | 1,950.00 USD | 0.00 USD | `+5.92%` | `1,462.00` |
| `Live` | `Short` | `1.34` | 230,160.00 USD | 3,630.00 USD | 0.00 USD | `+6.71%` | `2,702.00` |
| `Live` | `Short` | `1.35` | 264,250.00 USD | 34,090.00 USD | 0.00 USD | `+7.51%` | `25,161.00` |
| `Live` | `Short` | `1.36` | 457,610.00 USD | 193,360.00 USD | 0.00 USD | `+8.30%` | `141,656.00` |
| `Live` | `Short` | `1.38` | 522,030.00 USD | 64,420.00 USD | 0.00 USD | `+9.09%` | `46,848.00` |
| `Live` | `Short` | `1.39` | 523,300.00 USD | 1,280.00 USD | 0.00 USD | `+9.89%` | `921.00` |
| `Live` | `Short` | `1.40` | 525,390.00 USD | 2,090.00 USD | 0.00 USD | `+10.68%` | `1,500.00` |
| `Live` | `Short` | `1.41` | 526,030.00 USD | 635.06 USD | 0.00 USD | `+11.47%` | `452.00` |
| `Live` | `Short` | `1.42` | 529,960.00 USD | 3,930.00 USD | 0.00 USD | `+12.27%` | `2,776.00` |
| `Live` | `Short` | `1.43` | 623,460.00 USD | 93,510.00 USD | 0.00 USD | `+13.06%` | `65,619.00` |
| `Live` | `Short` | `1.44` | 624,450.00 USD | 988.72 USD | 0.00 USD | `+13.85%` | `689.00` |
| `Live` | `Short` | `1.45` | 1,190,000.00 USD | 561,440.00 USD | 0.00 USD | `+14.65%` | `388,541.00` |
| `Live` | `Short` | `1.47` | 1,310,000.00 USD | 128,580.00 USD | 0.00 USD | `+16.23%` | `87,771.00` |
| `Live` | `Short` | `1.48` | 1,310,000.00 USD | 500.03 USD | 0.00 USD | `+17.03%` | `339.00` |
| `Live` | `Short` | `1.50` | 1,330,000.00 USD | 12,150.00 USD | 0.00 USD | `+18.61%` | `8,126.00` |
| `Live` | `Short` | `1.51` | 1,350,000.00 USD | 25,060.00 USD | 0.00 USD | `+20.20%` | `16,540.00` |
| `Live` | `Short` | `1.53` | 1,350,000.00 USD | 174.99 USD | 0.00 USD | `+21.79%` | `114.00` |
| `Live` | `Short` | `1.54` | 1,350,000.00 USD | 1,370.00 USD | 0.00 USD | `+22.58%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,360,000.00 USD | 1,360.00 USD | 0.00 USD | `+23.37%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,360,000.00 USD | 679.21 USD | 0.00 USD | `+24.17%` | `434.00` |
| `Live` | `Short` | `1.57` | 1,360,000.00 USD | 2,900.00 USD | 0.00 USD | `+24.96%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 5,600,000.00 USD | 4,240,000.00 USD | 0.00 USD | `+25.75%` | `2,675,059.00` |
| `Live` | `Short` | `1.60` | 5,600,000.00 USD | 1,510.00 USD | 0.00 USD | `+27.34%` | `938.00` |
| `Live` | `Short` | `1.61` | 5,600,000.00 USD | 2,660.00 USD | 0.00 USD | `+28.13%` | `1,647.00` |
| `Live` | `Short` | `1.62` | 5,600,000.00 USD | 271.38 USD | 0.00 USD | `+28.93%` | `167.00` |
| `Live` | `Short` | `1.64` | 5,610,000.00 USD | 4,890.00 USD | 0.00 USD | `+29.72%` | `2,989.00` |
| `Live` | `Short` | `1.65` | 5,610,000.00 USD | 2,350.00 USD | 0.00 USD | `+30.51%` | `1,429.00` |
| `Live` | `Short` | `1.66` | 5,740,000.00 USD | 134,550.00 USD | 0.00 USD | `+31.31%` | `81,299.00` |
| `Live` | `Short` | `1.67` | 5,750,000.00 USD | 586.08 USD | 0.00 USD | `+32.10%` | `352.00` |
| `Live` | `Short` | `1.68` | 5,750,000.00 USD | 120.60 USD | 0.00 USD | `+32.89%` | `72.00` |
| `Live` | `Short` | `1.69` | 5,750,000.00 USD | 8,130.00 USD | 0.00 USD | `+33.69%` | `4,826.00` |
| `Live` | `Short` | `1.70` | 5,750,000.00 USD | 974.62 USD | 0.00 USD | `+34.48%` | `575.00` |
| `Live` | `Short` | `1.71` | 5,760,000.00 USD | 3,210.00 USD | 0.00 USD | `+35.27%` | `1,883.00` |
| `Live` | `Short` | `1.74` | 5,760,000.00 USD | 2,970.00 USD | 0.00 USD | `+37.65%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 5,760,000.00 USD | 2,730.00 USD | 0.00 USD | `+38.45%` | `1,564.00` |
| `Live` | `Short` | `1.75` | 5,770,000.00 USD | 1,460.00 USD | 0.00 USD | `+39.24%` | `831.00` |
| `Live` | `Short` | `1.76` | 10,910,000.00 USD | 5,140,000.00 USD | 0.00 USD | `+40.03%` | `2,913,901.00` |
| `Live` | `Short` | `1.78` | 11,040,000.00 USD | 130,410.00 USD | 0.00 USD | `+41.62%` | `73,058.00` |
| `Live` | `Short` | `1.79` | 11,040,000.00 USD | 2,690.00 USD | 0.00 USD | `+42.42%` | `1,500.00` |
| `Live` | `Short` | `1.80` | 11,050,000.00 USD | 4,500.00 USD | 0.00 USD | `+43.21%` | `2,493.00` |
| `Live` | `Short` | `1.81` | 11,060,000.00 USD | 15,410.00 USD | 0.00 USD | `+44.00%` | `8,490.00` |
| `Live` | `Short` | `1.82` | 11,060,000.00 USD | 260.98 USD | 0.00 USD | `+44.80%` | `143.00` |
| `Live` | `Short` | `1.83` | 11,250,000.00 USD | 186,300.00 USD | 0.00 USD | `+45.59%` | `101,524.00` |
| `Live` | `Short` | `1.84` | 14,080,000.00 USD | 2,830,000.00 USD | 0.00 USD | `+46.38%` | `1,534,522.00` |
| `Live` | `Short` | `1.85` | 14,080,000.00 USD | 428.50 USD | 0.00 USD | `+47.18%` | `231.00` |
| `Live` | `Short` | `1.86` | 17,050,000.00 USD | 2,980,000.00 USD | 0.00 USD | `+47.97%` | `1,595,490.00` |
| `Live` | `Short` | `1.90` | 17,060,000.00 USD | 4,190.00 USD | 0.00 USD | `+50.35%` | `2,211.00` |
| `Live` | `Short` | `1.91` | 17,060,000.00 USD | 373.38 USD | 0.00 USD | `+51.14%` | `196.00` |
| `Live` | `Short` | `1.92` | 17,100,000.00 USD | 40,810.00 USD | 0.00 USD | `+51.94%` | `21,309.00` |
| `Live` | `Short` | `1.93` | 17,410,000.00 USD | 313,150.00 USD | 0.00 USD | `+52.73%` | `162,677.00` |
| `Live` | `Short` | `1.95` | 17,410,000.00 USD | 680.75 USD | 0.00 USD | `+54.32%` | `350.00` |
| `Live` | `Short` | `1.96` | 17,410,000.00 USD | 293.25 USD | 0.00 USD | `+55.11%` | `150.00` |
| `Live` | `Short` | `1.97` | 17,640,000.00 USD | 227,560.00 USD | 0.00 USD | `+55.90%` | `115,806.00` |
| `Live` | `Short` | `1.98` | 17,640,000.00 USD | 651.75 USD | 0.00 USD | `+56.70%` | `330.00` |
| `Live` | `Short` | `2.00` | 17,640,000.00 USD | 940.34 USD | 0.00 USD | `+59.08%` | `469.00` |
| `Live` | `Short` | `2.02` | 18,060,000.00 USD | 419,270.00 USD | 0.00 USD | `+59.87%` | `208,072.00` |
| `Live` | `Short` | `2.04` | 18,060,000.00 USD | 198.36 USD | 0.00 USD | `+62.25%` | `97.00` |
| `Live` | `Short` | `2.06` | 18,060,000.00 USD | 369.90 USD | 0.00 USD | `+63.04%` | `180.00` |
| `Live` | `Short` | `2.06` | 18,070,000.00 USD | 4,940.00 USD | 0.00 USD | `+63.84%` | `2,390.00` |
| `Live` | `Short` | `2.10` | 18,070,000.00 USD | 1,240.00 USD | 0.00 USD | `+66.22%` | `592.00` |
| `Live` | `Short` | `2.10` | 18,070,000.00 USD | 469.42 USD | 0.00 USD | `+67.01%` | `223.00` |
| `Live` | `Short` | `2.12` | 18,320,000.00 USD | 251,210.00 USD | 0.00 USD | `+67.80%` | `118,776.00` |
| `Live` | `Short` | `2.15` | 18,400,000.00 USD | 79,940.00 USD | 0.00 USD | `+70.98%` | `37,096.00` |
| `Live` | `Short` | `2.17` | 18,400,000.00 USD | 2,090.00 USD | 0.00 USD | `+71.77%` | `965.00` |
| `Live` | `Short` | `2.17` | 18,460,000.00 USD | 52,220.00 USD | 0.00 USD | `+72.56%` | `24,011.00` |
| `Live` | `Short` | `2.21` | 18,460,000.00 USD | 101.43 USD | 0.00 USD | `+74.94%` | `46.00` |
| `Live` | `Short` | `2.21` | 18,460,000.00 USD | 440.78 USD | 0.00 USD | `+75.74%` | `199.00` |
| `Live` | `Short` | `2.23` | 18,470,000.00 USD | 11,570.00 USD | 0.00 USD | `+76.53%` | `5,198.00` |
| `Live` | `Short` | `2.25` | 18,540,000.00 USD | 75,430.00 USD | 0.00 USD | `+78.91%` | `33,451.00` |
| `Live` | `Short` | `2.29` | 18,590,000.00 USD | 45,670.00 USD | 0.00 USD | `+81.29%` | `19,987.00` |
| `Live` | `Short` | `2.29` | 18,590,000.00 USD | 105.57 USD | 0.00 USD | `+82.09%` | `46.00` |
| `Live` | `Short` | `2.31` | 18,590,000.00 USD | 248.94 USD | 0.00 USD | `+82.88%` | `108.00` |
| `Live` | `Short` | `2.31` | 18,590,000.00 USD | 1,540.00 USD | 0.00 USD | `+83.67%` | `665.00` |
| `Live` | `Short` | `2.33` | 18,610,000.00 USD | 14,690.00 USD | 0.00 USD | `+84.47%` | `6,318.00` |
| `Live` | `Short` | `2.35` | 22,150,000.00 USD | 3,550,000.00 USD | 0.00 USD | `+86.05%` | `1,511,779.00` |
| `Live` | `Short` | `2.35` | 22,150,000.00 USD | 146.01 USD | 0.00 USD | `+86.85%` | `62.00` |
| `Live` | `Short` | `2.37` | 22,240,000.00 USD | 90,810.00 USD | 0.00 USD | `+87.64%` | `38,397.00` |
| `Live` | `Short` | `2.38` | 22,240,000.00 USD | 2,380.00 USD | 0.00 USD | `+88.43%` | `1,000.00` |
| `Live` | `Short` | `2.38` | 22,250,000.00 USD | 2,260.00 USD | 0.00 USD | `+89.23%` | `947.00` |
| `Live` | `Short` | `2.40` | 22,250,000.00 USD | 707.07 USD | 0.00 USD | `+90.81%` | `294.00` |
| `Live` | `Short` | `2.42` | 22,250,000.00 USD | 847.66 USD | 0.00 USD | `+91.61%` | `351.00` |
| `Live` | `Short` | `2.42` | 22,270,000.00 USD | 24,250.00 USD | 0.00 USD | `+92.40%` | `10,000.00` |
| `Live` | `Short` | `2.44` | 22,270,000.00 USD | 158.28 USD | 0.00 USD | `+93.19%` | `65.00` |
| `Live` | `Short` | `2.44` | 22,290,000.00 USD | 22,490.00 USD | 0.00 USD | `+93.99%` | `9,197.00` |
| `Live` | `Short` | `2.46` | 22,290,000.00 USD | 473.81 USD | 0.00 USD | `+94.78%` | `193.00` |
| `Live` | `Short` | `2.46` | 22,300,000.00 USD | 4,490.00 USD | 0.00 USD | `+95.57%` | `1,822.00` |
| `Live` | `Short` | `2.48` | 23,820,000.00 USD | 1,520,000.00 USD | 0.00 USD | `+96.37%` | `613,646.00` |
| `Live` | `Short` | `2.48` | 23,910,000.00 USD | 95,670.00 USD | 0.00 USD | `+97.16%` | `38,498.00` |
| `Live` | `Short` | `2.50` | 23,910,000.00 USD | 748.50 USD | 0.00 USD | `+97.95%` | `300.00` |
| `Live` | `Short` | `2.50` | 23,910,000.00 USD | 115.23 USD | 0.00 USD | `+98.75%` | `46.00` |
| `Live` | `Short` | `2.52` | 24,130,000.00 USD | 213,880.00 USD | 0.00 USD | `+99.54%` | `85,040.00` |
| `Live` | `Short` | `2.52` | 24,170,000.00 USD | 42,820.00 USD | 0.00 USD | `+100.33%` | `16,960.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 1,790,000.00 USD | 0.00 USD | 102.00 USD | `-79.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3650` | 1,790,000.00 USD | 0.00 USD | 351.50 USD | `-71.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 1,790,000.00 USD | 0.00 USD | 139.12 USD | `-70.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3950` | 1,790,000.00 USD | 0.00 USD | 2,880.00 USD | `-68.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4050` | 1,790,000.00 USD | 0.00 USD | 2,950.00 USD | `-67.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 1,790,000.00 USD | 0.00 USD | 408.51 USD | `-64.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 1,780,000.00 USD | 0.00 USD | 273.00 USD | `-63.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 1,780,000.00 USD | 0.00 USD | 151.12 USD | `-63.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 1,780,000.00 USD | 0.00 USD | 142.50 USD | `-62.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 1,780,000.00 USD | 0.00 USD | 145.50 USD | `-61.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 1,780,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 1,780,000.00 USD | 0.00 USD | 285.82 USD | `-59.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 1,780,000.00 USD | 0.00 USD | 306.60 USD | `-58.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 1,780,000.00 USD | 0.00 USD | 121.55 USD | `-55.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 1,780,000.00 USD | 0.00 USD | 656.53 USD | `-55.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 1,780,000.00 USD | 0.00 USD | 100.62 USD | `-53.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 1,780,000.00 USD | 0.00 USD | 203.75 USD | `-50.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 1,780,000.00 USD | 0.00 USD | 791.85 USD | `-49.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 1,780,000.00 USD | 0.00 USD | 573.40 USD | `-48.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 1,780,000.00 USD | 0.00 USD | 244.31 USD | `-48.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 1,780,000.00 USD | 0.00 USD | 29,530.00 USD | `-47.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 1,750,000.00 USD | 0.00 USD | 503.55 USD | `-46.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 1,750,000.00 USD | 0.00 USD | 480.19 USD | `-45.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 1,750,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 1,740,000.00 USD | 0.00 USD | 2,260.00 USD | `-44.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 1,740,000.00 USD | 0.00 USD | 228.80 USD | `-43.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 1,740,000.00 USD | 0.00 USD | 536.50 USD | `-42.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 1,730,000.00 USD | 0.00 USD | 1,300.00 USD | `-40.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 1,730,000.00 USD | 0.00 USD | 2,880.00 USD | `-39.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 1,730,000.00 USD | 0.00 USD | 878.48 USD | `-36.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 1,730,000.00 USD | 0.00 USD | 6,020.00 USD | `-34.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 1,720,000.00 USD | 0.00 USD | 1,260.00 USD | `-32.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 1,720,000.00 USD | 0.00 USD | 690.38 USD | `-30.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 1,720,000.00 USD | 0.00 USD | 1,210.00 USD | `-29.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 1,720,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 1,720,000.00 USD | 0.00 USD | 838.94 USD | `-28.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 1,720,000.00 USD | 0.00 USD | 932.38 USD | `-27.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 1,720,000.00 USD | 0.00 USD | 1,060.00 USD | `-26.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 1,710,000.00 USD | 0.00 USD | 1,090.00 USD | `-25.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 1,710,000.00 USD | 0.00 USD | 112.46 USD | `-25.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 1,710,000.00 USD | 0.00 USD | 1,730.00 USD | `-24.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 1,710,000.00 USD | 0.00 USD | 4,010.00 USD | `-23.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 1,710,000.00 USD | 0.00 USD | 6,300.00 USD | `-22.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 1,700,000.00 USD | 0.00 USD | 4,890.00 USD | `-21.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 1,700,000.00 USD | 0.00 USD | 902.47 USD | `-21.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 1,700,000.00 USD | 0.00 USD | 50,360.00 USD | `-20.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 1,640,000.00 USD | 0.00 USD | 6,640.00 USD | `-19.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 1,640,000.00 USD | 0.00 USD | 1,840.00 USD | `-18.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 1,640,000.00 USD | 0.00 USD | 42,670.00 USD | `-17.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 1,590,000.00 USD | 0.00 USD | 1,780.00 USD | `-17.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 1,590,000.00 USD | 0.00 USD | 23,530.00 USD | `-16.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,570,000.00 USD | 0.00 USD | 3,960.00 USD | `-15.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,560,000.00 USD | 0.00 USD | 48,460.00 USD | `-14.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,520,000.00 USD | 0.00 USD | 3,360.00 USD | `-13.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,510,000.00 USD | 0.00 USD | 100,190.00 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 1,410,000.00 USD | 0.00 USD | 21,590.00 USD | `-12.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 1,390,000.00 USD | 0.00 USD | 9,780.00 USD | `-11.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 1,380,000.00 USD | 0.00 USD | 101,980.00 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 1,280,000.00 USD | 0.00 USD | 13,380.00 USD | `-9.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 1,270,000.00 USD | 0.00 USD | 120,050.00 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 1,150,000.00 USD | 0.00 USD | 40,470.00 USD | `-8.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 1,110,000.00 USD | 0.00 USD | 37,000.00 USD | `-7.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 1,070,000.00 USD | 0.00 USD | 103,200.00 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 964,940.00 USD | 0.00 USD | 244,030.00 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 720,900.00 USD | 0.00 USD | 240,810.00 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 480,090.00 USD | 0.00 USD | 86,040.00 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 394,050.00 USD | 0.00 USD | 36,710.00 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 357,340.00 USD | 0.00 USD | 152,410.00 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 204,920.00 USD | 0.00 USD | 41,350.00 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 163,570.00 USD | 0.00 USD | 91,100.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 72,470.00 USD | 0.00 USD | 72,470.00 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 188,020.00 USD | 188,020.00 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 220,200.00 USD | 32,180.00 USD | 0.00 USD | `+1.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 474,140.00 USD | 253,940.00 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 489,490.00 USD | 15,360.00 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 513,620.00 USD | 24,130.00 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 1,150,000.00 USD | 640,000.00 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,370,000.00 USD | 221,350.00 USD | 0.00 USD | `+5.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,420,000.00 USD | 43,890.00 USD | 0.00 USD | `+5.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,480,000.00 USD | 65,480.00 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,500,000.00 USD | 14,640.00 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,750,000.00 USD | 249,240.00 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,830,000.00 USD | 81,760.00 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,880,000.00 USD | 53,970.00 USD | 0.00 USD | `+9.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,890,000.00 USD | 3,960.00 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 6,070,000.00 USD | 4,180,000.00 USD | 0.00 USD | `+11.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 6,070,000.00 USD | 2,080.00 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 6,070,000.00 USD | 6,460.00 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,150,000.00 USD | 78,630.00 USD | 0.00 USD | `+13.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,400,000.00 USD | 242,580.00 USD | 0.00 USD | `+14.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,400,000.00 USD | 7,510.00 USD | 0.00 USD | `+15.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,430,000.00 USD | 23,260.00 USD | 0.00 USD | `+16.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,530,000.00 USD | 108,140.00 USD | 0.00 USD | `+17.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,550,000.00 USD | 14,990.00 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,570,000.00 USD | 15,800.00 USD | 0.00 USD | `+18.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,650,000.00 USD | 85,390.00 USD | 0.00 USD | `+19.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,660,000.00 USD | 11,760.00 USD | 0.00 USD | `+20.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,680,000.00 USD | 19,430.00 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,730,000.00 USD | 45,620.00 USD | 0.00 USD | `+21.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,740,000.00 USD | 10,870.00 USD | 0.00 USD | `+22.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,740,000.00 USD | 2,380.00 USD | 0.00 USD | `+23.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,750,000.00 USD | 6,450.00 USD | 0.00 USD | `+24.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,750,000.00 USD | 5,570.00 USD | 0.00 USD | `+24.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,760,000.00 USD | 10,410.00 USD | 0.00 USD | `+25.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,900,000.00 USD | 139,120.00 USD | 0.00 USD | `+26.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,900,000.00 USD | 1,840.00 USD | 0.00 USD | `+27.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 6,980,000.00 USD | 80,330.00 USD | 0.00 USD | `+28.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 6,990,000.00 USD | 464.75 USD | 0.00 USD | `+28.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,160,000.00 USD | 179,860.00 USD | 0.00 USD | `+29.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,170,000.00 USD | 2,670.00 USD | 0.00 USD | `+30.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,250,000.00 USD | 85,010.00 USD | 0.00 USD | `+31.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,260,000.00 USD | 6,080.00 USD | 0.00 USD | `+32.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,280,000.00 USD | 18,400.00 USD | 0.00 USD | `+32.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,350,000.00 USD | 70,850.00 USD | 0.00 USD | `+33.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,370,000.00 USD | 18,000.00 USD | 0.00 USD | `+34.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,600,000.00 USD | 231,640.00 USD | 0.00 USD | `+35.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,610,000.00 USD | 14,250.00 USD | 0.00 USD | `+36.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,610,000.00 USD | 534.75 USD | 0.00 USD | `+36.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,660,000.00 USD | 43,240.00 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,660,000.00 USD | 3,330.00 USD | 0.00 USD | `+38.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,670,000.00 USD | 9,200.00 USD | 0.00 USD | `+39.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,690,000.00 USD | 21,720.00 USD | 0.00 USD | `+40.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,820,000.00 USD | 128,330.00 USD | 0.00 USD | `+40.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,940,000.00 USD | 124,660.00 USD | 0.00 USD | `+41.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 7,950,000.00 USD | 3,980.00 USD | 0.00 USD | `+42.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 7,950,000.00 USD | 254.51 USD | 0.00 USD | `+43.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 7,960,000.00 USD | 11,080.00 USD | 0.00 USD | `+44.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 7,960,000.00 USD | 3,970.00 USD | 0.00 USD | `+44.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 7,970,000.00 USD | 8,170.00 USD | 0.00 USD | `+45.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 7,970,000.00 USD | 843.17 USD | 0.00 USD | `+46.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 7,980,000.00 USD | 8,390.00 USD | 0.00 USD | `+47.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 7,980,000.00 USD | 4,420.00 USD | 0.00 USD | `+48.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 7,980,000.00 USD | 591.89 USD | 0.00 USD | `+49.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 8,030,000.00 USD | 46,370.00 USD | 0.00 USD | `+50.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 8,040,000.00 USD | 9,270.00 USD | 0.00 USD | `+51.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 8,040,000.00 USD | 265.10 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 8,040,000.00 USD | 2,040.00 USD | 0.00 USD | `+54.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 8,040,000.00 USD | 807.42 USD | 0.00 USD | `+55.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,060,000.00 USD | 14,120.00 USD | 0.00 USD | `+55.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,060,000.00 USD | 4,010.00 USD | 0.00 USD | `+56.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,060,000.00 USD | 325.54 USD | 0.00 USD | `+57.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,070,000.00 USD | 7,020.00 USD | 0.00 USD | `+58.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,190,000.00 USD | 123,020.00 USD | 0.00 USD | `+59.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,200,000.00 USD | 3,350.00 USD | 0.00 USD | `+60.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,200,000.00 USD | 181.12 USD | 0.00 USD | `+61.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,200,000.00 USD | 382.41 USD | 0.00 USD | `+62.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,200,000.00 USD | 3,420.00 USD | 0.00 USD | `+63.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,200,000.00 USD | 661.93 USD | 0.00 USD | `+64.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,320,000.00 USD | 124,400.00 USD | 0.00 USD | `+66.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,330,000.00 USD | 1,580.00 USD | 0.00 USD | `+67.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,340,000.00 USD | 13,900.00 USD | 0.00 USD | `+68.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,360,000.00 USD | 24,840.00 USD | 0.00 USD | `+70.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,420,000.00 USD | 50,580.00 USD | 0.00 USD | `+70.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,420,000.00 USD | 2,690.00 USD | 0.00 USD | `+71.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,420,000.00 USD | 2,180.00 USD | 0.00 USD | `+74.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,570,000.00 USD | 151,380.00 USD | 0.00 USD | `+75.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,570,000.00 USD | 2,230.00 USD | 0.00 USD | `+80.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,570,000.00 USD | 1,140.00 USD | 0.00 USD | `+81.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,590,000.00 USD | 11,670.00 USD | 0.00 USD | `+82.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,590,000.00 USD | 370.40 USD | 0.00 USD | `+83.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,590,000.00 USD | 733.19 USD | 0.00 USD | `+85.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,590,000.00 USD | 2,410.00 USD | 0.00 USD | `+87.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,590,000.00 USD | 475.00 USD | 0.00 USD | `+88.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,590,000.00 USD | 1,190.00 USD | 0.00 USD | `+89.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,590,000.00 USD | 2,540.00 USD | 0.00 USD | `+90.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,600,000.00 USD | 1,590.00 USD | 0.00 USD | `+90.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,600,000.00 USD | 1,370.00 USD | 0.00 USD | `+91.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,620,000.00 USD | 19,590.00 USD | 0.00 USD | `+92.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,620,000.00 USD | 564.92 USD | 0.00 USD | `+93.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,630,000.00 USD | 8,110.00 USD | 0.00 USD | `+94.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,630,000.00 USD | 3,420.00 USD | 0.00 USD | `+97.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,630,000.00 USD | 124.75 USD | 0.00 USD | `+97.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,660,000.00 USD | 29,920.00 USD | 0.00 USD | `+98.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.52` | 8,660,000.00 USD | 378.75 USD | 0.00 USD | `+100.33%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.07` | 87,170,000.00 USD | 0.00 USD | 87,170,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `1.09` | 87,170,000.00 USD | 0.00 USD | 87,170,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `1.09` | 87,130,000.00 USD | 0.00 USD | 87,130,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD |
| `7D` | `1.09` | 87,030,000.00 USD | 0.00 USD | 87,030,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD |
| `7D` | `1.10` | 86,990,000.00 USD | 0.00 USD | 86,990,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD |
| `7D` | `1.10` | 86,990,000.00 USD | 0.00 USD | 86,990,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD |
| `7D` | `1.10` | 86,700,000.00 USD | 0.00 USD | 86,700,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD |
| `7D` | `1.11` | 86,700,000.00 USD | 0.00 USD | 86,700,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD |
| `7D` | `1.11` | 86,690,000.00 USD | 0.00 USD | 86,690,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `7D` | `1.11` | 86,690,000.00 USD | 0.00 USD | 86,690,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD |
| `7D` | `1.12` | 86,640,000.00 USD | 0.00 USD | 86,640,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `1D` | `1.12` | 78,360,000.00 USD | 0.00 USD | 78,360,000.00 USD | 3,530.00 USD | 16,050.00 USD | 149,950.00 USD |
| `7D` | `1.12` | 86,620,000.00 USD | 0.00 USD | 86,620,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 78,190,000.00 USD | 0.00 USD | 78,190,000.00 USD | 15,020.00 USD | 68,320.00 USD | 29,680.00 USD |
| `1D` | `1.12` | 78,070,000.00 USD | 0.00 USD | 78,070,000.00 USD | 5,340.00 USD | 40,010.00 USD | 87,140.00 USD |
| `7D` | `1.12` | 86,550,000.00 USD | 0.00 USD | 86,550,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `1.12` | 77,940,000.00 USD | 0.00 USD | 77,940,000.00 USD | 5,470.00 USD | 2,460.00 USD | 71,880.00 USD |
| `7D` | `1.12` | 86,520,000.00 USD | 0.00 USD | 86,520,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.13` | 77,860,000.00 USD | 0.00 USD | 77,860,000.00 USD | 92,060.00 USD | 28,150.00 USD | 50,130.00 USD |
| `1D` | `1.13` | 77,690,000.00 USD | 0.00 USD | 77,690,000.00 USD | 69,610.00 USD | 19,950.00 USD | 166,510.00 USD |
| `7D` | `1.13` | 86,310,000.00 USD | 0.00 USD | 86,310,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 77,430,000.00 USD | 0.00 USD | 77,430,000.00 USD | 0.00 USD | 107,140.00 USD | 160,740.00 USD |
| `7D` | `1.13` | 86,120,000.00 USD | 0.00 USD | 86,120,000.00 USD | 5,450.00 USD | 2,460.00 USD | 0.00 USD |
| `1D` | `1.13` | 77,170,000.00 USD | 0.00 USD | 77,170,000.00 USD | 0.00 USD | 13,730.00 USD | 243,160.00 USD |
| `7D` | `1.13` | 86,110,000.00 USD | 0.00 USD | 86,110,000.00 USD | 69,750.00 USD | 93,260.00 USD | 108,230.00 USD |
| `1D` | `1.13` | 76,910,000.00 USD | 0.00 USD | 76,910,000.00 USD | 63,980.00 USD | 70,910.00 USD | 56,100.00 USD |
| `7D` | `1.13` | 85,840,000.00 USD | 0.00 USD | 85,840,000.00 USD | 74,920.00 USD | 97,060.00 USD | 224,140.00 USD |
| `1D` | `1.14` | 76,720,000.00 USD | 0.00 USD | 76,720,000.00 USD | 40,370.00 USD | 125,930.00 USD | 65,260.00 USD |
| `7D` | `1.14` | 85,440,000.00 USD | 0.00 USD | 85,440,000.00 USD | 79,780.00 USD | 88,050.00 USD | 219,170.00 USD |
| `7D` | `1.14` | 85,060,000.00 USD | 0.00 USD | 85,060,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 76,490,000.00 USD | 0.00 USD | 76,490,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD |
| `7D` | `1.14` | 85,030,000.00 USD | 0.00 USD | 85,030,000.00 USD | 39,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 76,420,000.00 USD | 0.00 USD | 76,420,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.14` | 84,990,000.00 USD | 0.00 USD | 84,990,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD |
| `1D` | `1.14` | 76,350,000.00 USD | 0.00 USD | 76,350,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD |
| `7D` | `1.14` | 84,850,000.00 USD | 0.00 USD | 84,850,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.15` | 84,840,000.00 USD | 0.00 USD | 84,840,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `1D` | `1.15` | 76,220,000.00 USD | 0.00 USD | 76,220,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 84,780,000.00 USD | 0.00 USD | 84,780,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD |
| `7D` | `1.15` | 84,400,000.00 USD | 0.00 USD | 84,400,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.15` | 76,200,000.00 USD | 0.00 USD | 76,200,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.15` | 84,250,000.00 USD | 0.00 USD | 84,250,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 76,140,000.00 USD | 0.00 USD | 76,140,000.00 USD | 73,200.00 USD | 45,600.00 USD | 263,680.00 USD |
| `7D` | `1.15` | 84,090,000.00 USD | 0.00 USD | 84,090,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `1D` | `1.16` | 75,750,000.00 USD | 0.00 USD | 75,750,000.00 USD | 20,480.00 USD | 25,050.00 USD | 82,910.00 USD |
| `7D` | `1.16` | 83,210,000.00 USD | 0.00 USD | 83,210,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 75,620,000.00 USD | 0.00 USD | 75,620,000.00 USD | 122,170.00 USD | 21,140.00 USD | 392,890.00 USD |
| `7D` | `1.16` | 82,970,000.00 USD | 0.00 USD | 82,970,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 75,090,000.00 USD | 0.00 USD | 75,090,000.00 USD | 212,900.00 USD | 76,950.00 USD | 158,690.00 USD |
| `7D` | `1.16` | 82,110,000.00 USD | 0.00 USD | 82,110,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 74,640,000.00 USD | 0.00 USD | 74,640,000.00 USD | 270,110.00 USD | 293,490.00 USD | 148,960.00 USD |
| `7D` | `1.16` | 81,020,000.00 USD | 0.00 USD | 81,020,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD |
| `1D` | `1.16` | 73,930,000.00 USD | 0.00 USD | 73,930,000.00 USD | 179,260.00 USD | 89,000.00 USD | 719,120.00 USD |
| `7D` | `1.16` | 79,730,000.00 USD | 0.00 USD | 79,730,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD |
| `1D` | `1.17` | 72,940,000.00 USD | 0.00 USD | 72,940,000.00 USD | 87,310.00 USD | 70,600.00 USD | 151,280.00 USD |
| `7D` | `1.17` | 78,060,000.00 USD | 0.00 USD | 78,060,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD |
| `1D` | `1.17` | 72,630,000.00 USD | 0.00 USD | 72,630,000.00 USD | 113,470.00 USD | 166,170.00 USD | 170,840.00 USD |
| `7D` | `1.17` | 76,720,000.00 USD | 0.00 USD | 76,720,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 72,180,000.00 USD | 0.00 USD | 72,180,000.00 USD | 152,210.00 USD | 22,380.00 USD | 358,690.00 USD |
| `7D` | `1.17` | 75,650,000.00 USD | 0.00 USD | 75,650,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 71,650,000.00 USD | 0.00 USD | 71,650,000.00 USD | 371,850.00 USD | 5,850.00 USD | 266,890.00 USD |
| `7D` | `1.17` | 73,610,000.00 USD | 0.00 USD | 73,610,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD |
| `1D` | `1.17` | 71,000,000.00 USD | 0.00 USD | 71,000,000.00 USD | 124,360.00 USD | 130,370.00 USD | 474,190.00 USD |
| `7D` | `1.17` | 72,410,000.00 USD | 0.00 USD | 72,410,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD |
| `1D` | `1.18` | 70,270,000.00 USD | 0.00 USD | 70,270,000.00 USD | 304,390.00 USD | 85,620.00 USD | 356,950.00 USD |
| `7D` | `1.18` | 70,840,000.00 USD | 0.00 USD | 70,840,000.00 USD | 181,850.00 USD | 100,190.00 USD | 377,590.00 USD |
| `1D` | `1.18` | 69,530,000.00 USD | 0.00 USD | 69,530,000.00 USD | 71,040.00 USD | 84,480.00 USD | 175,590.00 USD |
| `7D` | `1.18` | 70,180,000.00 USD | 0.00 USD | 70,180,000.00 USD | 85,020.00 USD | 74,230.00 USD | 489,310.00 USD |
| `1D` | `1.18` | 69,200,000.00 USD | 0.00 USD | 69,200,000.00 USD | 113,290.00 USD | 10,150.00 USD | 24,100.00 USD |
| `7D` | `1.18` | 69,530,000.00 USD | 0.00 USD | 69,530,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD |
| `1D` | `1.18` | 69,050,000.00 USD | 0.00 USD | 69,050,000.00 USD | 222,930.00 USD | 10,160.00 USD | 666,440.00 USD |
| `7D` | `1.18` | 68,920,000.00 USD | 0.00 USD | 68,920,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 68,150,000.00 USD | 0.00 USD | 68,150,000.00 USD | 196,910.00 USD | 73,630.00 USD | 143,880.00 USD |
| `7D` | `1.18` | 68,650,000.00 USD | 0.00 USD | 68,650,000.00 USD | 299,450.00 USD | 571,700.00 USD | 235,490.00 USD |
| `1D` | `1.19` | 67,730,000.00 USD | 0.00 USD | 67,730,000.00 USD | 86,540.00 USD | 511,780.00 USD | 65,030.00 USD |
| `7D` | `1.19` | 67,550,000.00 USD | 0.00 USD | 67,550,000.00 USD | 76,370.00 USD | 109,420.00 USD | 706,450.00 USD |
| `1D` | `1.19` | 67,070,000.00 USD | 0.00 USD | 67,070,000.00 USD | 365,260.00 USD | 93,260.00 USD | 1,570,000.00 USD |
| `7D` | `1.19` | 66,650,000.00 USD | 0.00 USD | 66,650,000.00 USD | 250,710.00 USD | 93,330.00 USD | 585,020.00 USD |
| `1D` | `1.19` | 65,040,000.00 USD | 0.00 USD | 65,040,000.00 USD | 110,600.00 USD | 45,410.00 USD | 319,610.00 USD |
| `7D` | `1.19` | 65,730,000.00 USD | 0.00 USD | 65,730,000.00 USD | 227,280.00 USD | 92,240.00 USD | 795,050.00 USD |
| `1D` | `1.19` | 64,570,000.00 USD | 0.00 USD | 64,570,000.00 USD | 147,820.00 USD | 199,810.00 USD | 469,390.00 USD |
| `7D` | `1.19` | 64,610,000.00 USD | 0.00 USD | 64,610,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD |
| `1D` | `1.19` | 63,750,000.00 USD | 0.00 USD | 63,750,000.00 USD | 190,850.00 USD | 428,210.00 USD | 1,690,000.00 USD |
| `7D` | `1.19` | 63,250,000.00 USD | 0.00 USD | 63,250,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD |
| `1D` | `1.20` | 61,440,000.00 USD | 0.00 USD | 61,440,000.00 USD | 784,530.00 USD | 121,000.00 USD | 1,220,000.00 USD |
| `7D` | `1.20` | 62,420,000.00 USD | 0.00 USD | 62,420,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD |
| `1D` | `1.20` | 59,320,000.00 USD | 0.00 USD | 59,320,000.00 USD | 264,550.00 USD | 834,460.00 USD | 657,850.00 USD |
| `7D` | `1.20` | 60,830,000.00 USD | 0.00 USD | 60,830,000.00 USD | 31,150.00 USD | 372,080.00 USD | 2,610,000.00 USD |
| `1D` | `1.20` | 57,560,000.00 USD | 0.00 USD | 57,560,000.00 USD | 708,890.00 USD | 419,750.00 USD | 2,300,000.00 USD |
| `7D` | `1.20` | 57,820,000.00 USD | 0.00 USD | 57,820,000.00 USD | 736,290.00 USD | 330,310.00 USD | 18,590.00 USD |
| `1D` | `1.20` | 54,130,000.00 USD | 0.00 USD | 54,130,000.00 USD | 137,910.00 USD | 157,180.00 USD | 820,430.00 USD |
| `7D` | `1.20` | 56,740,000.00 USD | 0.00 USD | 56,740,000.00 USD | 264,000.00 USD | 144,630.00 USD | 464,230.00 USD |
| `1D` | `1.20` | 53,010,000.00 USD | 0.00 USD | 53,010,000.00 USD | 526,510.00 USD | 511,570.00 USD | 378,960.00 USD |
| `7D` | `1.20` | 55,860,000.00 USD | 0.00 USD | 55,860,000.00 USD | 47,500.00 USD | 589,990.00 USD | 5,570.00 USD |
| `1D` | `1.21` | 51,600,000.00 USD | 0.00 USD | 51,600,000.00 USD | 328,050.00 USD | 532,540.00 USD | 467,640.00 USD |
| `7D` | `1.21` | 55,220,000.00 USD | 0.00 USD | 55,220,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD |
| `1D` | `1.21` | 50,270,000.00 USD | 0.00 USD | 50,270,000.00 USD | 1,660,000.00 USD | 193,480.00 USD | 1,860,000.00 USD |
| `7D` | `1.21` | 55,200,000.00 USD | 0.00 USD | 55,200,000.00 USD | 456,280.00 USD | 0.00 USD | 248,110.00 USD |
| `1D` | `1.21` | 46,560,000.00 USD | 0.00 USD | 46,560,000.00 USD | 533,310.00 USD | 413,110.00 USD | 1,120,000.00 USD |
| `7D` | `1.21` | 54,490,000.00 USD | 0.00 USD | 54,490,000.00 USD | 257,960.00 USD | 492,370.00 USD | 3,090,000.00 USD |
| `1D` | `1.21` | 44,490,000.00 USD | 0.00 USD | 44,490,000.00 USD | 1,410,000.00 USD | 572,260.00 USD | 1,190,000.00 USD |
| `7D` | `1.21` | 50,660,000.00 USD | 0.00 USD | 50,660,000.00 USD | 1,230,000.00 USD | 0.00 USD | 369,560.00 USD |
| `1D` | `1.21` | 41,320,000.00 USD | 0.00 USD | 41,320,000.00 USD | 0.00 USD | 90,950.00 USD | 898,860.00 USD |
| `7D` | `1.21` | 49,060,000.00 USD | 0.00 USD | 49,060,000.00 USD | 108,640.00 USD | 0.00 USD | 910,410.00 USD |
| `1D` | `1.22` | 40,330,000.00 USD | 0.00 USD | 40,330,000.00 USD | 226,520.00 USD | 85,640.00 USD | 680,350.00 USD |
| `7D` | `1.22` | 48,040,000.00 USD | 0.00 USD | 48,040,000.00 USD | 142,210.00 USD | 9,150.00 USD | 0.00 USD |
| `1D` | `1.22` | 39,340,000.00 USD | 0.00 USD | 39,340,000.00 USD | 143,650.00 USD | 4,200.00 USD | 183,070.00 USD |
| `7D` | `1.22` | 47,890,000.00 USD | 0.00 USD | 47,890,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD |
| `1D` | `1.22` | 39,010,000.00 USD | 0.00 USD | 39,010,000.00 USD | 222,150.00 USD | 97,750.00 USD | 4,090.00 USD |
| `7D` | `1.22` | 47,150,000.00 USD | 0.00 USD | 47,150,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD |
| `1D` | `1.22` | 38,680,000.00 USD | 0.00 USD | 38,680,000.00 USD | 113,990.00 USD | 273,720.00 USD | 435,680.00 USD |
| `7D` | `1.22` | 46,070,000.00 USD | 0.00 USD | 46,070,000.00 USD | 0.00 USD | 164,230.00 USD | 11,370.00 USD |
| `1D` | `1.22` | 37,860,000.00 USD | 0.00 USD | 37,860,000.00 USD | 123,900.00 USD | 0.00 USD | 2,640,000.00 USD |
| `7D` | `1.22` | 45,890,000.00 USD | 0.00 USD | 45,890,000.00 USD | 51,610.00 USD | 166,160.00 USD | 33,260.00 USD |
| `1D` | `1.23` | 35,100,000.00 USD | 0.00 USD | 35,100,000.00 USD | 281,350.00 USD | 575,430.00 USD | 223,320.00 USD |
| `7D` | `1.23` | 45,640,000.00 USD | 0.00 USD | 45,640,000.00 USD | 112,770.00 USD | 535,430.00 USD | 9,210.00 USD |
| `1D` | `1.23` | 34,020,000.00 USD | 0.00 USD | 34,020,000.00 USD | 452,620.00 USD | 578,850.00 USD | 389,390.00 USD |
| `7D` | `1.23` | 44,980,000.00 USD | 0.00 USD | 44,980,000.00 USD | 59,160.00 USD | 950,550.00 USD | 24,470.00 USD |
| `1D` | `1.23` | 32,600,000.00 USD | 0.00 USD | 32,600,000.00 USD | 170,630.00 USD | 1,010,000.00 USD | 3,140,000.00 USD |
| `7D` | `1.23` | 43,950,000.00 USD | 0.00 USD | 43,950,000.00 USD | 198,530.00 USD | 888,470.00 USD | 807,050.00 USD |
| `1D` | `1.23` | 28,280,000.00 USD | 0.00 USD | 28,280,000.00 USD | 1,190,000.00 USD | 1,100,000.00 USD | 3,580,000.00 USD |
| `7D` | `1.23` | 42,050,000.00 USD | 0.00 USD | 42,050,000.00 USD | 1,020,000.00 USD | 963,040.00 USD | 1,320,000.00 USD |
| `1D` | `1.23` | 22,410,000.00 USD | 0.00 USD | 22,410,000.00 USD | 340,470.00 USD | 1,190,000.00 USD | 1,850,000.00 USD |
| `7D` | `1.23` | 38,750,000.00 USD | 0.00 USD | 38,750,000.00 USD | 1,460,000.00 USD | 1,820,000.00 USD | 3,860,000.00 USD |
| `1D` | `1.24` | 19,030,000.00 USD | 0.00 USD | 19,030,000.00 USD | 189,670.00 USD | 885,210.00 USD | 1,000,000.00 USD |
| `7D` | `1.24` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 2,040,000.00 USD | 1,800,000.00 USD | 1,680,000.00 USD |
| `1D` | `1.24` | 16,950,000.00 USD | 0.00 USD | 16,950,000.00 USD | 33,830.00 USD | 224,610.00 USD | 61,110.00 USD |
| `7D` | `1.24` | 26,080,000.00 USD | 0.00 USD | 26,080,000.00 USD | 2,630,000.00 USD | 1,580,000.00 USD | 3,490,000.00 USD |
| `1D` | `1.24` | 16,630,000.00 USD | 0.00 USD | 16,630,000.00 USD | 618,430.00 USD | 187,820.00 USD | 1,550,000.00 USD |
| `7D` | `1.24` | 18,380,000.00 USD | 0.00 USD | 18,380,000.00 USD | 2,070,000.00 USD | 950,140.00 USD | 535,960.00 USD |
| `1D` | `1.24` | 14,270,000.00 USD | 0.00 USD | 14,270,000.00 USD | 319,740.00 USD | 812,380.00 USD | 36,980.00 USD |
| `7D` | `1.24` | 14,820,000.00 USD | 0.00 USD | 14,820,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.24` | 13,100,000.00 USD | 0.00 USD | 13,100,000.00 USD | 1,810,000.00 USD | 5,660.00 USD | 2,340,000.00 USD |
| `7D` | `1.24` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 1,420,000.00 USD | 15,000.00 USD | 992,420.00 USD |
| `1D` | `1.25` | 8,940,000.00 USD | 0.00 USD | 8,940,000.00 USD | 851,070.00 USD | 389,970.00 USD | 746,290.00 USD |
| `7D` | `1.25` | 11,270,000.00 USD | 0.00 USD | 11,270,000.00 USD | 3,370,000.00 USD | 337,070.00 USD | 2,290,000.00 USD |
| `1D` | `1.25` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 133,680.00 USD | 890,000.00 USD | 1,430,000.00 USD |
| `7D` | `1.25` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 1,630,000.00 USD | 325,530.00 USD | 1,480,000.00 USD |
| `1D` | `1.25` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 331,570.00 USD | 171,540.00 USD | 1,010,000.00 USD |
| `7D` | `1.25` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 0.00 USD | 9,140.00 USD | 0.00 USD |
| `1D` | `1.25` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 220,120.00 USD | 3,370.00 USD | 192,270.00 USD |
| `7D` | `1.25` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 455,200.00 USD |
| `1D` | `1.25` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 0.00 USD | 10,370.00 USD | 669,770.00 USD |
| `7D` | `1.25` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 63,660.00 USD | 7,340.00 USD | 878,920.00 USD |
| `1D` | `1.26` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 1,570,000.00 USD | 284,390.00 USD | 39,040.00 USD |
| `7D` | `1.26` | 423,470.00 USD | 0.00 USD | 423,470.00 USD | 150,010.00 USD | 273,460.00 USD | 0.00 USD |
| `1D` | `1.26` | 261,340.00 USD | 261,340.00 USD | 0.00 USD | 69,930.00 USD | 191,400.00 USD | 0.00 USD |
| `1D` | `1.26` | 522,670.00 USD | 522,670.00 USD | 0.00 USD | 69,930.00 USD | 191,400.00 USD | 0.00 USD |
| `7D` | `1.26` | 19,840.00 USD | 19,840.00 USD | 0.00 USD | 0.00 USD | 19,840.00 USD | 0.00 USD |
| `7D` | `1.26` | 39,670.00 USD | 39,670.00 USD | 0.00 USD | 0.00 USD | 19,840.00 USD | 0.00 USD |
| `1D` | `1.26` | 783,460.00 USD | 783,460.00 USD | 0.00 USD | 208,340.00 USD | 27,670.00 USD | 24,770.00 USD |
| `7D` | `1.26` | 132,130.00 USD | 132,130.00 USD | 0.00 USD | 0.00 USD | 10,110.00 USD | 82,350.00 USD |
| `1D` | `1.26` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 755,130.00 USD | 100,700.00 USD | 872,590.00 USD |
| `7D` | `1.26` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 144,170.00 USD | 26,950.00 USD | 1,150,000.00 USD |
| `1D` | `1.26` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 772,130.00 USD | 1,180,000.00 USD | 1,860,000.00 USD |
| `7D` | `1.26` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 834,020.00 USD | 925,190.00 USD | 3,700,000.00 USD |
| `1D` | `1.27` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 1,040,000.00 USD | 1,310,000.00 USD | 2,550,000.00 USD |
| `7D` | `1.27` | 22,950,000.00 USD | 22,950,000.00 USD | 0.00 USD | 4,260,000.00 USD | 3,030,000.00 USD | 8,760,000.00 USD |
| `1D` | `1.27` | 14,690,000.00 USD | 14,690,000.00 USD | 0.00 USD | 198,110.00 USD | 1,950,000.00 USD | 1,310,000.00 USD |
| `7D` | `1.27` | 28,700,000.00 USD | 28,700,000.00 USD | 0.00 USD | 0.00 USD | 1,360,000.00 USD | 4,400,000.00 USD |
| `1D` | `1.27` | 20,070,000.00 USD | 20,070,000.00 USD | 0.00 USD | 960,010.00 USD | 1,020,000.00 USD | 3,400,000.00 USD |
| `7D` | `1.27` | 32,720,000.00 USD | 32,720,000.00 USD | 0.00 USD | 138,500.00 USD | 2,540,000.00 USD | 1,340,000.00 USD |
| `1D` | `1.27` | 23,440,000.00 USD | 23,440,000.00 USD | 0.00 USD | 1,050,000.00 USD | 988,040.00 USD | 1,330,000.00 USD |
| `7D` | `1.27` | 40,410,000.00 USD | 40,410,000.00 USD | 0.00 USD | 1,280,000.00 USD | 4,950,000.00 USD | 1,450,000.00 USD |
| `1D` | `1.27` | 29,660,000.00 USD | 29,660,000.00 USD | 0.00 USD | 818,720.00 USD | 1,810,000.00 USD | 3,600,000.00 USD |
| `7D` | `1.27` | 54,520,000.00 USD | 54,520,000.00 USD | 0.00 USD | 2,710,000.00 USD | 2,870,000.00 USD | 8,540,000.00 USD |
| `1D` | `1.28` | 35,100,000.00 USD | 35,100,000.00 USD | 0.00 USD | 982,470.00 USD | 2,090,000.00 USD | 2,360,000.00 USD |
| `7D` | `1.28` | 68,160,000.00 USD | 68,160,000.00 USD | 0.00 USD | 4,660,000.00 USD | 2,810,000.00 USD | 6,170,000.00 USD |
| `1D` | `1.28` | 45,650,000.00 USD | 45,650,000.00 USD | 0.00 USD | 4,660,000.00 USD | 1,640,000.00 USD | 4,250,000.00 USD |
| `7D` | `1.28` | 85,270,000.00 USD | 85,270,000.00 USD | 0.00 USD | 7,780,000.00 USD | 3,210,000.00 USD | 6,120,000.00 USD |
| `1D` | `1.28` | 48,420,000.00 USD | 48,420,000.00 USD | 0.00 USD | 237,040.00 USD | 1,810,000.00 USD | 729,750.00 USD |
| `7D` | `1.28` | 86,790,000.00 USD | 86,790,000.00 USD | 0.00 USD | 0.00 USD | 1,440,000.00 USD | 84,070.00 USD |
| `1D` | `1.28` | 51,280,000.00 USD | 51,280,000.00 USD | 0.00 USD | 846,340.00 USD | 100,660.00 USD | 1,910,000.00 USD |
| `7D` | `1.28` | 88,430,000.00 USD | 88,430,000.00 USD | 0.00 USD | 1,030,000.00 USD | 30,200.00 USD | 582,200.00 USD |
| `1D` | `1.28` | 53,970,000.00 USD | 53,970,000.00 USD | 0.00 USD | 985,220.00 USD | 490,930.00 USD | 1,220,000.00 USD |
| `7D` | `1.28` | 91,820,000.00 USD | 91,820,000.00 USD | 0.00 USD | 902,470.00 USD | 1,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `1.29` | 57,350,000.00 USD | 57,350,000.00 USD | 0.00 USD | 683,710.00 USD | 899,070.00 USD | 1,790,000.00 USD |
| `7D` | `1.29` | 95,320,000.00 USD | 95,320,000.00 USD | 0.00 USD | 796,960.00 USD | 1,290,000.00 USD | 1,420,000.00 USD |
| `1D` | `1.29` | 58,470,000.00 USD | 58,470,000.00 USD | 0.00 USD | 584,100.00 USD | 427,810.00 USD | 106,320.00 USD |
| `7D` | `1.29` | 95,800,000.00 USD | 95,800,000.00 USD | 0.00 USD | 440,460.00 USD | 2,730.00 USD | 33,260.00 USD |
| `1D` | `1.29` | 58,660,000.00 USD | 58,660,000.00 USD | 0.00 USD | 95,060.00 USD | 36,830.00 USD | 58,760.00 USD |
| `7D` | `1.29` | 96,380,000.00 USD | 96,380,000.00 USD | 0.00 USD | 70,460.00 USD | 4,320.00 USD | 510,220.00 USD |
| `1D` | `1.29` | 60,800,000.00 USD | 60,800,000.00 USD | 0.00 USD | 378,690.00 USD | 14,980.00 USD | 1,740,000.00 USD |
| `7D` | `1.29` | 98,470,000.00 USD | 98,470,000.00 USD | 0.00 USD | 1,040,000.00 USD | 202,640.00 USD | 846,810.00 USD |
| `1D` | `1.29` | 64,940,000.00 USD | 64,940,000.00 USD | 0.00 USD | 1,170,000.00 USD | 375,550.00 USD | 2,600,000.00 USD |
| `7D` | `1.29` | 102,110,000.00 USD | 102,110,000.00 USD | 0.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD |
| `1D` | `1.30` | 70,220,000.00 USD | 70,220,000.00 USD | 0.00 USD | 1,460,000.00 USD | 1,240,000.00 USD | 2,570,000.00 USD |
| `7D` | `1.30` | 109,400,000.00 USD | 109,400,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD |
| `1D` | `1.30` | 71,350,000.00 USD | 71,350,000.00 USD | 0.00 USD | 464,690.00 USD | 20,370.00 USD | 647,970.00 USD |
| `7D` | `1.30` | 111,350,000.00 USD | 111,350,000.00 USD | 0.00 USD | 25,800.00 USD | 172,080.00 USD | 1,750,000.00 USD |
| `1D` | `1.30` | 72,650,000.00 USD | 72,650,000.00 USD | 0.00 USD | 203,220.00 USD | 344,440.00 USD | 752,990.00 USD |
| `7D` | `1.30` | 113,350,000.00 USD | 113,350,000.00 USD | 0.00 USD | 208,510.00 USD | 298,720.00 USD | 1,490,000.00 USD |
| `1D` | `1.30` | 75,270,000.00 USD | 75,270,000.00 USD | 0.00 USD | 726,640.00 USD | 871,770.00 USD | 1,020,000.00 USD |
| `7D` | `1.30` | 114,380,000.00 USD | 114,380,000.00 USD | 0.00 USD | 85,960.00 USD | 944,610.00 USD | 0.00 USD |
| `1D` | `1.30` | 76,380,000.00 USD | 76,380,000.00 USD | 0.00 USD | 366,890.00 USD | 250,070.00 USD | 487,840.00 USD |
| `7D` | `1.30` | 116,910,000.00 USD | 116,910,000.00 USD | 0.00 USD | 0.00 USD | 2,040,000.00 USD | 485,710.00 USD |
| `1D` | `1.31` | 77,930,000.00 USD | 77,930,000.00 USD | 0.00 USD | 493,480.00 USD | 507,360.00 USD | 549,980.00 USD |
| `7D` | `1.31` | 118,860,000.00 USD | 118,860,000.00 USD | 0.00 USD | 1,770,000.00 USD | 183,660.00 USD | 0.00 USD |
| `1D` | `1.31` | 81,310,000.00 USD | 81,310,000.00 USD | 0.00 USD | 895,610.00 USD | 341,920.00 USD | 2,140,000.00 USD |
| `7D` | `1.31` | 123,790,000.00 USD | 123,790,000.00 USD | 0.00 USD | 1,450,000.00 USD | 821,310.00 USD | 2,650,000.00 USD |
| `1D` | `1.31` | 84,330,000.00 USD | 84,330,000.00 USD | 0.00 USD | 1,150,000.00 USD | 326,160.00 USD | 1,540,000.00 USD |
| `7D` | `1.31` | 126,190,000.00 USD | 126,190,000.00 USD | 0.00 USD | 1,340,000.00 USD | 408,300.00 USD | 647,870.00 USD |
| `1D` | `1.31` | 86,710,000.00 USD | 86,710,000.00 USD | 0.00 USD | 910,680.00 USD | 566,230.00 USD | 908,640.00 USD |
| `7D` | `1.31` | 130,530,000.00 USD | 130,530,000.00 USD | 0.00 USD | 189,510.00 USD | 858,660.00 USD | 3,300,000.00 USD |
| `1D` | `1.31` | 88,070,000.00 USD | 88,070,000.00 USD | 0.00 USD | 437,800.00 USD | 146,840.00 USD | 767,230.00 USD |
| `7D` | `1.31` | 131,700,000.00 USD | 131,700,000.00 USD | 0.00 USD | 515,950.00 USD | 151,320.00 USD | 501,780.00 USD |
| `1D` | `1.32` | 91,470,000.00 USD | 91,470,000.00 USD | 0.00 USD | 195,170.00 USD | 875,040.00 USD | 2,330,000.00 USD |
| `7D` | `1.32` | 135,910,000.00 USD | 135,910,000.00 USD | 0.00 USD | 68,520.00 USD | 1,750,000.00 USD | 2,380,000.00 USD |
| `1D` | `1.32` | 98,080,000.00 USD | 98,080,000.00 USD | 0.00 USD | 2,070,000.00 USD | 957,920.00 USD | 3,590,000.00 USD |
| `7D` | `1.32` | 140,760,000.00 USD | 140,760,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD |
| `1D` | `1.32` | 101,030,000.00 USD | 101,030,000.00 USD | 0.00 USD | 1,570,000.00 USD | 414,530.00 USD | 962,970.00 USD |
| `7D` | `1.32` | 142,780,000.00 USD | 142,780,000.00 USD | 0.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 104,470,000.00 USD | 104,470,000.00 USD | 0.00 USD | 1,310,000.00 USD | 757,740.00 USD | 1,380,000.00 USD |
| `7D` | `1.32` | 146,130,000.00 USD | 146,130,000.00 USD | 0.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 106,320,000.00 USD | 106,320,000.00 USD | 0.00 USD | 914,960.00 USD | 83,530.00 USD | 851,430.00 USD |
| `7D` | `1.32` | 148,910,000.00 USD | 148,910,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD |
| `1D` | `1.33` | 107,360,000.00 USD | 107,360,000.00 USD | 0.00 USD | 405,790.00 USD | 56,240.00 USD | 578,770.00 USD |
| `7D` | `1.33` | 150,720,000.00 USD | 150,720,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 108,570,000.00 USD | 108,570,000.00 USD | 0.00 USD | 545,530.00 USD | 170,390.00 USD | 494,230.00 USD |
| `7D` | `1.33` | 151,820,000.00 USD | 151,820,000.00 USD | 0.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 110,270,000.00 USD | 110,270,000.00 USD | 0.00 USD | 729,070.00 USD | 105,530.00 USD | 862,480.00 USD |
| `7D` | `1.33` | 153,530,000.00 USD | 153,530,000.00 USD | 0.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 112,090,000.00 USD | 112,090,000.00 USD | 0.00 USD | 465,720.00 USD | 179,640.00 USD | 1,180,000.00 USD |
| `7D` | `1.33` | 155,990,000.00 USD | 155,990,000.00 USD | 0.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD |
| `1D` | `1.33` | 113,940,000.00 USD | 113,940,000.00 USD | 0.00 USD | 783,210.00 USD | 229,580.00 USD | 838,970.00 USD |
| `7D` | `1.33` | 158,020,000.00 USD | 158,020,000.00 USD | 0.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD |
| `1D` | `1.34` | 115,050,000.00 USD | 115,050,000.00 USD | 0.00 USD | 286,040.00 USD | 208,270.00 USD | 616,920.00 USD |
| `7D` | `1.34` | 159,570,000.00 USD | 159,570,000.00 USD | 0.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 115,640,000.00 USD | 115,640,000.00 USD | 0.00 USD | 289,820.00 USD | 80,370.00 USD | 215,870.00 USD |
| `7D` | `1.34` | 162,000,000.00 USD | 162,000,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 116,510,000.00 USD | 116,510,000.00 USD | 0.00 USD | 353,910.00 USD | 145,200.00 USD | 374,680.00 USD |
| `7D` | `1.34` | 163,870,000.00 USD | 163,870,000.00 USD | 0.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD |
| `1D` | `1.34` | 118,380,000.00 USD | 118,380,000.00 USD | 0.00 USD | 932,000.00 USD | 374,950.00 USD | 560,930.00 USD |
| `7D` | `1.34` | 169,390,000.00 USD | 169,390,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,480,000.00 USD | 660,660.00 USD |
| `1D` | `1.34` | 120,450,000.00 USD | 120,450,000.00 USD | 0.00 USD | 820,840.00 USD | 470,890.00 USD | 777,090.00 USD |
| `7D` | `1.34` | 176,800,000.00 USD | 176,800,000.00 USD | 0.00 USD | 2,000,000.00 USD | 2,170,000.00 USD | 3,240,000.00 USD |
| `1D` | `1.35` | 121,400,000.00 USD | 121,400,000.00 USD | 0.00 USD | 374,110.00 USD | 172,120.00 USD | 401,650.00 USD |
| `7D` | `1.35` | 185,940,000.00 USD | 185,940,000.00 USD | 0.00 USD | 3,530,000.00 USD | 1,720,000.00 USD | 3,880,000.00 USD |
| `1D` | `1.35` | 122,140,000.00 USD | 122,140,000.00 USD | 0.00 USD | 263,580.00 USD | 78,220.00 USD | 400,600.00 USD |
| `7D` | `1.35` | 194,490,000.00 USD | 194,490,000.00 USD | 0.00 USD | 3,010,000.00 USD | 1,930,000.00 USD | 3,610,000.00 USD |
| `1D` | `1.35` | 122,530,000.00 USD | 122,530,000.00 USD | 0.00 USD | 200,720.00 USD | 40,980.00 USD | 146,530.00 USD |
| `7D` | `1.35` | 202,510,000.00 USD | 202,510,000.00 USD | 0.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD |
| `1D` | `1.35` | 122,800,000.00 USD | 122,800,000.00 USD | 0.00 USD | 69,740.00 USD | 28,660.00 USD | 174,610.00 USD |
| `7D` | `1.35` | 211,630,000.00 USD | 211,630,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 123,110,000.00 USD | 123,110,000.00 USD | 0.00 USD | 105,080.00 USD | 3,170.00 USD | 194,110.00 USD |
| `7D` | `1.35` | 218,380,000.00 USD | 218,380,000.00 USD | 0.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD |
| `1D` | `1.36` | 123,930,000.00 USD | 123,930,000.00 USD | 0.00 USD | 335,960.00 USD | 65,930.00 USD | 426,530.00 USD |
| `7D` | `1.36` | 224,720,000.00 USD | 224,720,000.00 USD | 0.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD |
| `1D` | `1.36` | 124,440,000.00 USD | 124,440,000.00 USD | 0.00 USD | 148,530.00 USD | 42,970.00 USD | 310,320.00 USD |
| `7D` | `1.36` | 227,270,000.00 USD | 227,270,000.00 USD | 0.00 USD | 1,060,000.00 USD | 639,580.00 USD | 849,400.00 USD |
| `1D` | `1.36` | 124,990,000.00 USD | 124,990,000.00 USD | 0.00 USD | 269,010.00 USD | 49,330.00 USD | 234,460.00 USD |
| `7D` | `1.36` | 230,370,000.00 USD | 230,370,000.00 USD | 0.00 USD | 1,460,000.00 USD | 414,770.00 USD | 1,230,000.00 USD |
| `1D` | `1.36` | 125,520,000.00 USD | 125,520,000.00 USD | 0.00 USD | 143,090.00 USD | 115,680.00 USD | 276,810.00 USD |
| `7D` | `1.36` | 234,160,000.00 USD | 234,160,000.00 USD | 0.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD |
| `1D` | `1.36` | 125,620,000.00 USD | 125,620,000.00 USD | 0.00 USD | 78,610.00 USD | 14,730.00 USD | 6,070.00 USD |
| `7D` | `1.36` | 236,920,000.00 USD | 236,920,000.00 USD | 0.00 USD | 1,430,000.00 USD | 616,140.00 USD | 713,350.00 USD |
| `1D` | `1.37` | 125,890,000.00 USD | 125,890,000.00 USD | 0.00 USD | 56,040.00 USD | 1,320.00 USD | 206,760.00 USD |
| `7D` | `1.37` | 237,730,000.00 USD | 237,730,000.00 USD | 0.00 USD | 206,650.00 USD | 190,380.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 126,120,000.00 USD | 126,120,000.00 USD | 0.00 USD | 97,000.00 USD | 109,930.00 USD | 29,680.00 USD |
| `7D` | `1.37` | 238,840,000.00 USD | 238,840,000.00 USD | 0.00 USD | 535,200.00 USD | 181,120.00 USD | 389,280.00 USD |
| `1D` | `1.37` | 126,130,000.00 USD | 126,130,000.00 USD | 0.00 USD | 0.00 USD | 10,160.00 USD | 0.00 USD |
| `7D` | `1.37` | 240,320,000.00 USD | 240,320,000.00 USD | 0.00 USD | 410,950.00 USD | 339,760.00 USD | 733,820.00 USD |
| `1D` | `1.37` | 126,260,000.00 USD | 126,260,000.00 USD | 0.00 USD | 5,340.00 USD | 29,850.00 USD | 87,140.00 USD |
| `7D` | `1.37` | 241,930,000.00 USD | 241,930,000.00 USD | 0.00 USD | 553,200.00 USD | 231,700.00 USD | 820,700.00 USD |
| `1D` | `1.37` | 126,340,000.00 USD | 126,340,000.00 USD | 0.00 USD | 5,470.00 USD | 2,460.00 USD | 71,880.00 USD |
| `7D` | `1.37` | 243,850,000.00 USD | 243,850,000.00 USD | 0.00 USD | 619,020.00 USD | 407,640.00 USD | 893,850.00 USD |
| `1D` | `1.38` | 126,510,000.00 USD | 126,510,000.00 USD | 0.00 USD | 92,060.00 USD | 28,150.00 USD | 50,130.00 USD |
| `7D` | `1.38` | 245,080,000.00 USD | 245,080,000.00 USD | 0.00 USD | 360,280.00 USD | 277,980.00 USD | 586,390.00 USD |
| `1D` | `1.38` | 126,760,000.00 USD | 126,760,000.00 USD | 0.00 USD | 69,610.00 USD | 19,950.00 USD | 166,510.00 USD |
| `7D` | `1.38` | 246,540,000.00 USD | 246,540,000.00 USD | 0.00 USD | 692,200.00 USD | 267,730.00 USD | 499,710.00 USD |
| `1D` | `1.38` | 126,890,000.00 USD | 126,890,000.00 USD | 0.00 USD | 0.00 USD | 41,620.00 USD | 81,940.00 USD |
| `7D` | `1.38` | 248,180,000.00 USD | 248,180,000.00 USD | 0.00 USD | 436,360.00 USD | 142,590.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 127,030,000.00 USD | 127,030,000.00 USD | 0.00 USD | 0.00 USD | 65,520.00 USD | 78,800.00 USD |
| `7D` | `1.38` | 250,040,000.00 USD | 250,040,000.00 USD | 0.00 USD | 710,620.00 USD | 348,810.00 USD | 802,530.00 USD |
| `1D` | `1.38` | 127,290,000.00 USD | 127,290,000.00 USD | 0.00 USD | 0.00 USD | 13,730.00 USD | 243,160.00 USD |
| `7D` | `1.38` | 250,930,000.00 USD | 250,930,000.00 USD | 0.00 USD | 403,730.00 USD | 253,120.00 USD | 228,560.00 USD |
| `1D` | `1.39` | 127,480,000.00 USD | 127,480,000.00 USD | 0.00 USD | 63,980.00 USD | 70,910.00 USD | 56,100.00 USD |
| `7D` | `1.39` | 251,950,000.00 USD | 251,950,000.00 USD | 0.00 USD | 377,810.00 USD | 231,880.00 USD | 413,510.00 USD |
| `1D` | `1.39` | 127,710,000.00 USD | 127,710,000.00 USD | 0.00 USD | 40,370.00 USD | 125,320.00 USD | 65,260.00 USD |
| `7D` | `1.39` | 253,010,000.00 USD | 253,010,000.00 USD | 0.00 USD | 384,080.00 USD | 308,280.00 USD | 366,440.00 USD |
| `7D` | `1.39` | 253,760,000.00 USD | 253,760,000.00 USD | 0.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD |
| `7D` | `1.39` | 254,090,000.00 USD | 254,090,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `7D` | `1.39` | 254,150,000.00 USD | 254,150,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD |
| `7D` | `1.40` | 254,370,000.00 USD | 254,370,000.00 USD | 0.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD |
| `7D` | `1.40` | 254,380,000.00 USD | 254,380,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 254,440,000.00 USD | 254,440,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 254,520,000.00 USD | 254,520,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `7D` | `1.40` | 254,820,000.00 USD | 254,820,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 254,970,000.00 USD | 254,970,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.41` | 255,130,000.00 USD | 255,130,000.00 USD | 0.00 USD | 13,200.00 USD | 17,670.00 USD | 126,530.00 USD |
| `7D` | `1.41` | 255,410,000.00 USD | 255,410,000.00 USD | 0.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.86B` | Total OI Tokens: `2,271,282,304.3 XRP`
  * 1h OI Change: `+0.69%` | 4h OI Change: `+4.69%` | 24h OI Change: `-3.95%`
  * Exchange Breakdown: Binance=`433.73M` | Bybit=`321.42M` | OKX=`95.48M` | Hyperliquid=`199.02M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-42.07K` | Last 24h: `81.98K` | Last 3d: `547.43K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0090%` | **USDT OKX** | `-0.0130%` |
| **USDT Bybit** | `-0.0238%` | **USDT KuCoin** | `-0.0038%` |
| **USDT MEXC** | `0.0090%` | **USDT BingX** | `0.0089%` |
| **USDT Gate** | `-0.0023%` | **USDT Bitget** | `-0.0042%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `50.52%` | `49.48%` | `1.02` | 407,220,000.00 USD |
| `15M` | `Binance` | `46.66%` | `53.34%` | `0.87` | 136,240,000.00 USD |
| `15M` | `OKX` | `50.6%` | `49.4%` | `1.02` | 55,650,000.00 USD |
| `15M` | `Bybit` | `50.41%` | `49.59%` | `1.02` | 39,280,000.00 USD |
| `15M` | `KuCoin` | `71.26%` | `28.74%` | `2.48` | 962,540.00 USD |
| `15M` | `Gate` | `47.42%` | `52.58%` | `0.90` | 49,310,000.00 USD |
| `15M` | `Bitget` | `53.97%` | `46.03%` | `1.17` | 20,700,000.00 USD |
| `15M` | `BingX` | `40.58%` | `59.42%` | `0.68` | 4,780,000.00 USD |
| `15M` | `MEXC` | `53.16%` | `46.84%` | `1.13` | 21,670,000.00 USD |
| `15M` | `Bitunix` | `48.12%` | `51.88%` | `0.93` | 13,070,000.00 USD |
| `15M` | `Hyperliquid` | `60.75%` | `39.25%` | `1.55` | 26,800,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `43.6%` | `56.4%` | `0.77` | 2,570,000.00 USD |
| `15M` | `Crypto.com` | `58.6%` | `41.4%` | `1.42` | 1,590,000.00 USD |
| `15M` | `WhiteBIT` | `86.13%` | `13.87%` | `6.21` | 7,990,000.00 USD |
| `15M` | `HTX` | `58.63%` | `41.37%` | `1.42` | 2,030,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `52.66%` | `47.34%` | `1.11` | 14,690,000.00 USD |
| `15M` | `Bitfinex` | `12.75%` | `87.25%` | `0.15` | 916,030.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `48.68%` | `51.32%` | `0.95` | 2,760,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `57.87%` | `42.13%` | `1.37` | 6,220,000.00 USD |
| `15M` | `Whale Positions` | `46.66%` | `53.34%` | `0.87` | 136,240,000.00 USD |
| `15M` | `Global Accounts` | `50.52%` | `49.48%` | `1.02` | 407,220,000.00 USD |
| `1H` | `XRP` | `44.53%` | `55.47%` | `0.80` | 2,070,000,000.00 USD |
| `1H` | `Binance` | `40.94%` | `59.06%` | `0.69` | 746,780,000.00 USD |
| `1H` | `OKX` | `43.83%` | `56.17%` | `0.78` | 300,780,000.00 USD |
| `1H` | `Bybit` | `43.25%` | `56.75%` | `0.76` | 177,450,000.00 USD |
| `1H` | `KuCoin` | `40.12%` | `59.88%` | `0.67` | 5,490,000.00 USD |
| `1H` | `Gate` | `45.93%` | `54.07%` | `0.85` | 221,440,000.00 USD |
| `1H` | `Bitget` | `46.58%` | `53.42%` | `0.87` | 106,770,000.00 USD |
| `1H` | `BingX` | `39.21%` | `60.79%` | `0.65` | 29,330,000.00 USD |
| `1H` | `MEXC` | `38.65%` | `61.35%` | `0.63` | 94,780,000.00 USD |
| `1H` | `Bitunix` | `39.41%` | `60.59%` | `0.65` | 81,170,000.00 USD |
| `1H` | `Hyperliquid` | `60.59%` | `39.41%` | `1.54` | 132,510,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `43.44%` | `56.56%` | `0.77` | 11,710,000.00 USD |
| `1H` | `Crypto.com` | `50.65%` | `49.35%` | `1.03` | 5,830,000.00 USD |
| `1H` | `WhiteBIT` | `88.6%` | `11.4%` | `7.77` | 18,560,000.00 USD |
| `1H` | `HTX` | `42.26%` | `57.74%` | `0.73` | 9,420,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `49.7%` | `50.3%` | `0.99` | 83,010,000.00 USD |
| `1H` | `Bitfinex` | `36.58%` | `63.42%` | `0.58` | 1,690,000.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `53.88%` | `46.12%` | `1.17` | 16,960,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `53.22%` | `46.78%` | `1.14` | 24,920,000.00 USD |
| `1H` | `Whale Positions` | `40.94%` | `59.06%` | `0.69` | 746,780,000.00 USD |
| `1H` | `Global Accounts` | `44.53%` | `55.47%` | `0.80` | 2,070,000,000.00 USD |
| `4H` | `XRP` | `51.52%` | `48.48%` | `1.06` | 8,230,000,000.00 USD |
| `4H` | `Binance` | `53.06%` | `46.94%` | `1.13` | 2,430,000,000.00 USD |
| `4H` | `OKX` | `50.6%` | `49.4%` | `1.02` | 1,420,000,000.00 USD |
| `4H` | `Bybit` | `50.68%` | `49.32%` | `1.03` | 555,970,000.00 USD |
| `4H` | `KuCoin` | `56.67%` | `43.33%` | `1.31` | 40,990,000.00 USD |
| `4H` | `Gate` | `50.58%` | `49.42%` | `1.02` | 1,120,000,000.00 USD |
| `4H` | `Bitget` | `51.59%` | `48.41%` | `1.07` | 359,240,000.00 USD |
| `4H` | `BingX` | `52.76%` | `47.24%` | `1.12` | 71,160,000.00 USD |
| `4H` | `MEXC` | `48.68%` | `51.32%` | `0.95` | 198,960,000.00 USD |
| `4H` | `Bitunix` | `52.3%` | `47.7%` | `1.10` | 271,710,000.00 USD |
| `4H` | `Hyperliquid` | `54.91%` | `45.09%` | `1.22` | 206,710,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.01%` | `44.99%` | `1.22` | 43,450,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `46.06%` | `53.94%` | `0.85` | 1,130,000,000.00 USD |
| `4H` | `HTX` | `79.67%` | `20.33%` | `3.92` | 168,700,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `48.28%` | `51.72%` | `0.93` | 48,920,000.00 USD |
| `4H` | `Bitfinex` | `27.79%` | `72.21%` | `0.38` | 4,740,000.00 USD |
| `4H` | `Kraken` | `71.65%` | `28.35%` | `2.53` | 1,240,000.00 USD |
| `4H` | `Aster` | `53.59%` | `46.41%` | `1.15` | 56,780,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.17%` | `49.83%` | `1.01` | 102,410,000.00 USD |
| `4H` | `Whale Positions` | `53.06%` | `46.94%` | `1.13` | 2,430,000,000.00 USD |
| `4H` | `Global Accounts` | `51.52%` | `48.48%` | `1.06` | 8,230,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.24` | 13,408,965.14 USD | 7,227,260.97 USD | 6,181,704.17 USD | 1,045,556.80 USD | `+7.80%` | `8B / 3S` |
| `0:00 UTC` | `1.24` | `1.25` | `1.24` | `1.25` | `1.24` | 11,613,568.18 USD | 6,301,411.52 USD | 5,312,156.67 USD | 989,254.85 USD | `+8.52%` | `26B / 9S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 11,339,015.88 USD | 5,463,329.20 USD | 5,875,686.68 USD | -412,357.48 USD | `-3.64%` | `7B / 6S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 9,975,142.90 USD | 5,917,919.57 USD | 4,057,223.33 USD | 1,860,696.23 USD | `+18.65%` | `9B / 2S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 6,812,599.45 USD | 3,905,481.96 USD | 2,907,117.49 USD | 998,364.47 USD | `+14.65%` | `4B / 3S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 9,935,673.56 USD | 6,437,809.71 USD | 3,497,863.85 USD | 2,939,945.86 USD | `+29.59%` | `23B / 7S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 6,138,672.69 USD | 3,294,606.36 USD | 2,844,066.33 USD | 450,540.03 USD | `+7.34%` | `3B / 1S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 5,482,004.91 USD | 2,916,488.83 USD | 2,565,516.08 USD | 350,972.75 USD | `+6.40%` | `2B / 2S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 7,888,806.65 USD | 3,687,747.74 USD | 4,201,058.91 USD | -513,311.17 USD | `-6.51%` | `4B / 11S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 6,984,589.03 USD | 3,240,816.52 USD | 3,743,772.51 USD | -502,955.99 USD | `-7.20%` | `2B / 4S` |

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
| `5m` | 392,680.00 USD | 161,960.00 USD | **`ACCUMULATION`** |
| `15m` | 1,340,000.00 USD | -215,560.00 USD | **`ACCUMULATION`** |
| `30m` | 1,430,000.00 USD | -1,430,000.00 USD | **`NEUTRAL`** |
| `1h` | 1,950,000.00 USD | -337,900.00 USD | **`ACCUMULATION`** |
| `2h` | 6,580,000.00 USD | 10,650,000.00 USD | **`ACCUMULATION`** |
| `4h` | 20,150,000.00 USD | 32,770,000.00 USD | **`ACCUMULATION`** |
| `6h` | 4,770,000.00 USD | -1,170,000.00 USD | **`ACCUMULATION`** |
| `8h` | -14,300,000.00 USD | -7,580,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -49,000,000.00 USD | -118,090,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -50,920,000.00 USD | -130,390,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -119,090,000.00 USD | -223,140,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -596,920,000.00 USD | -1,290,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+392.68K` | 15m=`+1.34M` | 1h=`+1.95M` | 24h=`-50.92M`
* Futures Capital Netflows: 5m=`+161.96K` | 15m=`-215.56K` | 1h=`-337.90K` | 24h=`-130.39M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.23` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.21` (Risk Distance: `0.0158` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0158` pts)
  * +2.5R Take Profit: `1.22`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
