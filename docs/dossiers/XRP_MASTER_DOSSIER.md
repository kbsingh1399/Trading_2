# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 11:26:19 IST` (`2026-10-30 05:56:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.25` | **Live Ask Quote**: `1.26` | **Mid Price**: `1.26`
- **Spread Points**: `4.00` | **Spread BPS**: `31.82 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.23` | VWAP Z-Score: `+1.45` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0095` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `65.28` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.28` | Lower -3.00σ Band: `1.17`
  * Upper +2.51σ Band: `1.28` | Lower -2.51σ Band: `1.18`
  * Upper +2.01σ Band: `1.27` | Lower -2.01σ Band: `1.19`
  * Upper +2.00σ Band: `1.27` | Lower -2.00σ Band: `1.19`
  * Upper +1.28σ Band: `1.25` | Lower -1.28σ Band: `1.21`
  * Upper +1.00σ Band: `1.25` | Lower -1.00σ Band: `1.21`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.25` | EMA-20=`1.24` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.25` (Slope: `+0.0000`) | EMA-100=`1.26`
  * Institutional Anchors: EMA-144=`1.27` | EMA-200=`1.28` (Slope: `-0.3878`) | EMA-233=`1.29`
- **Range Boundaries**: 24H High=`1.31` | 24H Low=`1.19` | Weekly High=`1.34` | Weekly Low=`1.19`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-0.12%`)
  * Point of Control (POC) = `1.25` (Distance: `+0.94%`)
  * Value Area Low (VAL) = `1.23` (Distance: `+2.58%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.33` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.19`
  * London Session (08:00-16:00 UTC): High=`1.26` | Low=`1.25`
  * New York Session (13:00-21:00 UTC): High=`1.26` | Low=`1.25`
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
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `1,621,187` | 2,042,950.99 USD | 362,753.61 USD | `+17.76%` | -40,250,099.75 USD | `+0.03` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `1,490,330` | 1,878,331.43 USD | 31,398.89 USD | `+1.67%` | -40,218,700.86 USD | `-0.63` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `885,031` | 1,114,472.84 USD | -59,221.51 USD | `-5.31%` | -40,277,922.37 USD | `-0.87` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.26` | `7,899,972` | 9,935,673.56 USD | 2,939,945.86 USD | `+29.59%` | -41,063,393.39 USD | `+1.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.26` | `1.26` | `1.26` | `1.26` | `4,871,938` | 6,138,672.69 USD | 450,540.03 USD | `+7.34%` | -40,612,853.36 USD | `-0.02` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.26` | `1.26` | `1.26` | `1.26` | `3,996,548` | 5,035,755.26 USD | 334,930.99 USD | `+6.65%` | -40,277,922.37 USD | `-0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.22` | `1.25` | `1.22` | `1.25` | `36,941,941` | 45,661,386.25 USD | 4,453,356.28 USD | `+9.75%` | -46,975,781.11 USD | `+0.76` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.25` | `1.26` | `1.24` | `1.25` | `31,772,661` | 39,740,326.41 USD | 3,435,958.07 USD | `+8.65%` | -43,539,823.04 USD | `+0.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.25` | `1.26` | `1.25` | `1.26` | `16,768,458` | 21,110,101.52 USD | 3,725,416.88 USD | `+17.65%` | -39,814,406.17 USD | `+0.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -42,956,799.49 USD | `-1.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -45,386,586.40 USD | `+0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.26` | `48,541,119` | 60,850,427.93 USD | 7,161,374.95 USD | `+11.77%` | -38,225,211.45 USD | `+1.14` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | 545,129.68 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -14,866,665.27 USD | `-1.39` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -42,956,799.49 USD | `-1.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -45,386,586.40 USD | `+0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.26` | `51,143,484` | 64,130,709.62 USD | 7,432,417.92 USD | `+11.59%` | -37,954,168.48 USD | `+1.15` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `ASK` | `1.26` | `34140.0000` | 43,057.37 USD | 2,075,730.56 USD | `9 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `8635.0000` | 10,889.60 USD | 2,032,673.19 USD | `4 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `105755.0000` | 133,357.05 USD | 2,021,783.59 USD | `7 orders` | `+0.14%` | `-` |
| `ASK` | `1.26` | `521858.0000` | 658,010.75 USD | 1,888,426.54 USD | `10 orders` | `+0.13%` | `-` |
| `ASK` | `1.26` | `24789.0000` | 31,253.97 USD | 1,230,415.78 USD | `4 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `30234.0000` | 38,116.00 USD | 1,199,161.81 USD | `5 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `44537.0000` | 56,143.34 USD | 1,161,045.81 USD | `8 orders` | `+0.11%` | `-` |
| `ASK` | `1.26` | `61091.0000` | 77,005.21 USD | 1,104,902.47 USD | `7 orders` | `+0.10%` | `-` |
| `ASK` | `1.26` | `46238.0000` | 58,278.38 USD | 1,027,897.26 USD | `7 orders` | `+0.09%` | `-` |
| `ASK` | `1.26` | `105742.0000` | 133,266.64 USD | 969,618.89 USD | `15 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `352504.0000` | 444,225.54 USD | 836,352.24 USD | `7 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `65776.0000` | 82,884.34 USD | 392,126.70 USD | `10 orders` | `+0.07%` | `-` |
| `ASK` | `1.26` | `35839.0000` | 45,157.14 USD | 309,242.37 USD | `9 orders` | `+0.06%` | `-` |
| `ASK` | `1.26` | `50241.0000` | 63,298.64 USD | 264,085.23 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `1.26` | `54288.0000` | 68,392.02 USD | 200,786.59 USD | `11 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `48645.0000` | 61,278.11 USD | 132,394.57 USD | `8 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `24726.0000` | 31,144.87 USD | 71,116.46 USD | `6 orders` | `+0.03%` | `-` |
| `ASK` | `1.26` | `14608.0000` | 18,398.78 USD | 39,971.59 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `1.26` | `10057.0000` | 12,665.79 USD | 21,572.81 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `1.26` | `7073.0000` | 8,907.03 USD | 8,907.03 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.26` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.26` | `0.00%` | `-` |
| `BID` | `1.26` | `19864.0000` | 25,012.75 USD | 25,012.75 USD | `7 orders` | `-0.00%` | `-` |
| `BID` | `1.26` | `28232.0000` | 35,546.91 USD | 60,559.66 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `1.26` | `15359.0000` | 19,336.98 USD | 79,896.64 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `1.26` | `13120.0000` | 16,516.77 USD | 96,413.41 USD | `7 orders` | `-0.03%` | `-` |
| `BID` | `1.26` | `47769.0000` | 60,131.62 USD | 156,545.03 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `76002.0000` | 95,663.72 USD | 252,208.74 USD | `8 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `93699.0000` | 117,929.56 USD | 370,138.30 USD | `7 orders` | `-0.05%` | `-` |
| `BID` | `1.26` | `280162.0000` | 352,583.88 USD | 722,722.18 USD | `14 orders` | `-0.06%` | `-` |
| `BID` | `1.26` | `37839.0000` | 47,616.60 USD | 770,338.78 USD | `9 orders` | `-0.07%` | `-` |
| `BID` | `1.26` | `35377.0000` | 44,514.88 USD | 814,853.66 USD | `9 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `88734.0000` | 111,645.12 USD | 926,498.78 USD | `9 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `259401.0000` | 326,352.40 USD | 1,252,851.18 USD | `9 orders` | `-0.09%` | `-` |
| `BID` | `1.26` | `15645.0000` | 19,681.41 USD | 1,272,532.59 USD | `4 orders` | `-0.10%` | `-` |
| `BID` | `1.26` | `77610.0000` | 97,625.62 USD | 1,370,158.20 USD | `8 orders` | `-0.11%` | `-` |
| `BID` | `1.26` | `16267.0000` | 20,460.63 USD | 1,390,618.84 USD | `4 orders` | `-0.12%` | `-` |
| `BID` | `1.26` | `360164.0000` | 452,978.26 USD | 1,843,597.10 USD | `5 orders` | `-0.12%` | `-` |
| `BID` | `1.26` | `82175.0000` | 103,343.28 USD | 1,946,940.38 USD | `12 orders` | `-0.13%` | `-` |
| `BID` | `1.26` | `64105.0000` | 80,612.04 USD | 2,027,552.42 USD | `4 orders` | `-0.14%` | `-` |
| `BID` | `1.26` | `7100.0000` | 8,927.54 USD | 2,036,479.96 USD | `5 orders` | `-0.15%` | `-` |
| `BID` | `1.26` | `75029.0000` | 94,333.96 USD | 2,130,813.92 USD | `5 orders` | `-0.15%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:24:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `28` | `0x31b1...1434` | `LONG` | 44,107,548.04 USD | `35,031,430.00` | `1.13` | `1.26` | `0.9612` | 4,528,664.77 USD | `+10.27%` | `10X Cross` |
| `91` | `0x5b5d...c060` | `SHORT` | 20,099,965.83 USD | `15,964,251.00` | `1.44` | `1.26` | `11.35` | 2,816,102.88 USD | `+14.01%` | `5X Cross` |
| `156` | `0xb83d...6e36` | `SHORT` | 13,284,033.82 USD | `10,555,450.00` | `1.50` | `1.26` | `13.87` | 2,538,535.82 USD | `+19.11%` | `5X Cross` |
| `337` | `0x58f0...0d20` | `LONG` | 6,680,902.00 USD | `5,307,147.00` | `1.24` | `1.26` | `1.22` | 78,058.50 USD | `+1.17%` | `20X Cross` |
| `397` | `0xecb6...2b00` | `SHORT` | 5,621,025.91 USD | `4,466,094.00` | `1.27` | `1.26` | `8.15` | 52,555.95 USD | `+0.93%` | `10X Cross` |
| `423` | `0xca49...53c8` | `SHORT` | 5,211,685.25 USD | `4,138,886.00` | `1.44` | `1.26` | `4.82` | 741,637.48 USD | `+14.23%` | `20X Cross` |
| `436` | `0xdd53...2b13` | `SHORT` | 5,032,633.27 USD | `3,998,914.00` | `1.40` | `1.26` | `16.75` | 564,242.84 USD | `+11.21%` | `3X Cross` |
| `499` | `0x610b...b613` | `LONG` | 4,461,828.01 USD | `3,543,946.00` | `1.44` | `1.26` | `0.8160` | -638,164.59 USD | `-14.30%` | `5X Cross` |
| `528` | `0xfc27...9d9d` | `SHORT` | 4,185,202.44 USD | `3,325,284.00` | `1.29` | `1.26` | `6.62` | 115,506.86 USD | `+2.76%` | `20X Cross` |
| `616` | `0x9946...0852` | `SHORT` | 3,665,315.91 USD | `2,912,418.00` | `1.41` | `1.26` | `1.78` | 443,186.66 USD | `+12.09%` | `20X Cross` |
| `666` | `0xc30c...a4c9` | `SHORT` | 3,365,446.13 USD | `2,672,981.00` | `1.42` | `1.26` | `1.59` | 421,517.97 USD | `+12.52%` | `6X Cross` |
| `695` | `0xf48f...10fe` | `LONG` | 3,229,032.87 USD | `2,565,779.00` | `1.53` | `1.26` | `0.9997` | -695,607.86 USD | `-21.54%` | `4X Cross` |
| `735` | `0x023a...2355` | `SHORT` | 3,102,357.12 USD | `2,464,927.00` | `1.32` | `1.26` | `3.37` | 150,639.12 USD | `+4.86%` | `20X Cross` |
| `744` | `0x45d2...4029` | `SHORT` | 3,087,345.80 USD | `2,453,000.00` | `1.48` | `1.26` | `18.38` | 550,934.62 USD | `+17.84%` | `20X Cross` |
| `1068` | `0xeadc...9d55` | `LONG` | 2,039,472.18 USD | `1,619,805.00` | `1.21` | `1.26` | `0.000000` | 80,629.16 USD | `+3.95%` | `20X Cross` |
| `1143` | `0x94b2...599e` | `SHORT` | 1,939,505.16 USD | `1,540,696.00` | `1.36` | `1.26` | `1.87` | 160,961.29 USD | `+8.30%` | `20X Cross` |
| `1150` | `0xbcd4...0dd2` | `SHORT` | 1,924,826.67 USD | `1,529,461.00` | `1.31` | `1.26` | `1.85` | 79,717.93 USD | `+4.14%` | `20X Cross` |
| `1165` | `0x3fc5...c0c1` | `SHORT` | 1,902,725.05 USD | `1,511,779.00` | `1.52` | `1.26` | `2.34` | 388,889.55 USD | `+20.44%` | `20X Cross` |
| `1188` | `0x31ef...f715` | `LONG` | 1,857,215.70 USD | `1,475,080.00` | `1.49` | `1.26` | `1.04` | -342,049.70 USD | `-18.42%` | `3X Isolated` |
| `1242` | `0x7737...bf66` | `SHORT` | 1,779,673.84 USD | `1,413,466.00` | `1.41` | `1.26` | `13.54` | 219,194.81 USD | `+12.32%` | `10X Cross` |
| `1300` | `0x95da...2328` | `LONG` | 1,668,099.70 USD | `1,324,876.00` | `1.35` | `1.26` | `0.0754` | -125,541.40 USD | `-7.53%` | `5X Cross` |
| `1322` | `0xee2b...d67e` | `LONG` | 1,643,958.41 USD | `1,306,284.00` | `1.55` | `1.26` | `0.3933` | -386,696.49 USD | `-23.52%` | `4X Cross` |
| `1362` | `0x215d...f80a` | `LONG` | 1,575,799.48 USD | `1,251,777.00` | `1.32` | `1.26` | `1.13` | -78,654.75 USD | `-4.99%` | `14X Cross` |
| `1391` | `0x5fa3...35b7` | `SHORT` | 1,561,793.51 USD | `1,240,651.00` | `1.30` | `1.26` | `2.62` | 54,698.62 USD | `+3.50%` | `20X Cross` |
| `1417` | `0x123d...3bff` | `LONG` | 1,529,491.55 USD | `1,215,329.00` | `1.35` | `1.26` | `0.000000` | -107,577.67 USD | `-7.03%` | `10X Cross` |
| `1481` | `0xdf95...7d72` | `SHORT` | 1,458,075.51 USD | `1,158,490.00` | `1.37` | `1.26` | `34.53` | 132,570.38 USD | `+9.09%` | `20X Cross` |
| `1558` | `0xc179...e0c8` | `SHORT` | 1,379,985.52 USD | `1,096,532.00` | `1.29` | `1.26` | `6.79` | 38,959.86 USD | `+2.82%` | `10X Cross` |
| `1562` | `0xef96...9383` | `SHORT` | 1,375,619.59 USD | `1,092,976.00` | `1.34` | `1.26` | `4.55` | 87,127.84 USD | `+6.33%` | `20X Cross` |
| `1617` | `0x7fda...17d1` | `LONG` | 1,305,798.21 USD | `1,037,583.00` | `1.21` | `1.26` | `0.000000` | 47,235.75 USD | `+3.62%` | `20X Cross` |
| `1639` | `0xb1ce...681b` | `LONG` | 1,285,992.17 USD | `1,021,764.00` | `1.49` | `1.26` | `1.16` | -238,064.33 USD | `-18.51%` | `4X Isolated` |
| `1743` | `0x3c36...461a` | `LONG` | 1,183,900.23 USD | `940,051.00` | `1.30` | `1.26` | `1.05` | -35,180.38 USD | `-2.97%` | `10X Cross` |
| `1811` | `0x2577...4897` | `SHORT` | 1,141,920.23 USD | `907,294.00` | `1.24` | `1.26` | `4.89` | -14,714.13 USD | `-1.29%` | `20X Cross` |
| `2002` | `0xbfc7...80b4` | `SHORT` | 1,007,280.00 USD | `800,000.00` | `1.48` | `1.26` | `3.17` | 176,174.65 USD | `+17.49%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.29` | 11,967.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.97K USD at 1.2923 USD [API] | `2026-10-29 02:32:11` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 11,967.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.97K USD at 1.2923 USD [API] | `2026-10-29 02:32:11` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 91.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2914 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,703.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.70K USD at 1.2930 USD [API] | `2026-10-29 02:29:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 641.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.64K USD at 1.2930 USD [API] | `2026-10-29 02:29:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 14.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2930 USD [API] | `2026-10-29 02:29:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 29.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 29.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,202.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.20K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 541.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.54K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 953.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.95K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 126.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.13K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 541.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.54K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 19.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 144.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.14K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 673.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.67K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 77.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.08K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 148.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.15K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 584.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.58K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 112.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.11K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 53.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.05K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,263.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.26K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 393.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.39K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 69.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,471.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.47K USD at 1.2931 USD [API] | `2026-10-29 02:28:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 2,293.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.29K USD at 1.2942 USD [API] | `2026-10-29 02:28:14` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,605.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.61K USD at 1.2882 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.01K USD at 1.2882 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 13,841.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 13.84K USD at 1.2901 USD [API] | `2026-10-29 02:39:29` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 8,956.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.96K USD at 1.3086 USD [API] | `2026-10-15 02:22:19` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,701.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 9.70K USD at 1.2898 USD [API] | `2026-10-29 02:44:33` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,438.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.44K USD at 1.2927 USD [API] | `2026-10-29 02:49:16` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 8,808.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.81K USD at 1.2954 USD [API] | `2026-10-29 02:54:54` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 24,668.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 24.67K USD at 1.2984 USD [API] | `2026-10-29 03:02:22` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11,165.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 11.17K USD at 1.2700 USD [API] | `2026-10-17 21:38:11` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 462.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.46K USD at 1.2700 USD [API] | `2026-10-17 21:38:11` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 12.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:11` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 124.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.12K USD at 1.2700 USD [API] | `2026-10-17 21:38:11` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 66.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.2700 USD [API] | `2026-10-17 21:38:11` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 48.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.05K USD at 1.2700 USD [API] | `2026-10-17 21:38:11` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 185.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.19K USD at 1.2700 USD [API] | `2026-10-17 21:38:11` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 657.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.66K USD at 1.3200 USD [API] | `2026-10-08 17:25:18` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 5,006.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.2951 USD [API] | `2026-10-29 03:08:35` |
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
| `Live` | `Long Liquidation` | `0.2550` | 8,750.00 USD | 64,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 1,090.00 USD | 64,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 25,980.00 USD | 64,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 20,650.00 USD | 64,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 9,190.00 USD | 64,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 5,840.00 USD | 64,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 28,240.00 USD | 64,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 6,060.00 USD | 64,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 1,280.00 USD | 64,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 4,090.00 USD | 64,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 6,600.00 USD | 64,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 139,290.00 USD | 64,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 530,660.00 USD | 64,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 509.62 USD | 63,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 3,700.00 USD | 63,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 15,820.00 USD | 63,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 632.90 USD | 63,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 4,610.00 USD | 63,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 13,480.00 USD | 63,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 2,220.00 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 2,660.00 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 8,250.00 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 2,340.00 USD | 63,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 3,420.00 USD | 63,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 164,540.00 USD | 63,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 1,110.00 USD | 63,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 1,600.00 USD | 63,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 7,820.00 USD | 63,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 1,970.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 5,380.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 24,310.00 USD | 63,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 32,120.00 USD | 63,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 33,040.00 USD | 63,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 11,070.00 USD | 63,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 21,460.00 USD | 63,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 5,440.00 USD | 63,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 17,830.00 USD | 63,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 37,140.00 USD | 63,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 5,800.00 USD | 63,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 161,800.00 USD | 63,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 19,510.00 USD | 63,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 70,640.00 USD | 63,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 245,330.00 USD | 63,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 73,300.00 USD | 62,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 113,230.00 USD | 62,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 88,950.00 USD | 62,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 2,190.00 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 7,080.00 USD | 62,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 507,020.00 USD | 62,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 19,410.00 USD | 61,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 17,740.00 USD | 61,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 2,940,000.00 USD | 61,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 136,650.00 USD | 58,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 42,390.00 USD | 58,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 59,040.00 USD | 58,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 56,260.00 USD | 58,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 14,630.00 USD | 58,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 107,360.00 USD | 58,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 352,960.00 USD | 58,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 87,440.00 USD | 58,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 163,090.00 USD | 58,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 136,030.00 USD | 57,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 69,680.00 USD | 57,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 199,270.00 USD | 57,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 57,060.00 USD | 57,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 152,100.00 USD | 57,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,890,000.00 USD | 57,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 177,550.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 2,990,000.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 130,060.00 USD | 20,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 490,240.00 USD | 20,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 346,370.00 USD | 19,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 59,550.00 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,120,000.00 USD | 19,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 660,310.00 USD | 17,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 378,350.00 USD | 15,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.07` | 83,780,000.00 USD | 83,780,000.00 USD | 0.00 USD | 0.00 USD | 39,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.07` | 950,500.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.08` | 83,740,000.00 USD | 83,740,000.00 USD | 0.00 USD | 2,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.08` | 191,170.00 USD | 13,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.09` | 83,730,000.00 USD | 83,730,000.00 USD | 37,460.00 USD | 100,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 83,600,000.00 USD | 83,600,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 83,590,000.00 USD | 83,590,000.00 USD | 0.00 USD | 2,020.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.09` | 361,000.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.10` | 83,560,000.00 USD | 83,560,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 83,550,000.00 USD | 83,550,000.00 USD | 0.00 USD | 0.00 USD | 140,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 83,410,000.00 USD | 83,410,000.00 USD | 0.00 USD | 0.00 USD | 147,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 83,270,000.00 USD | 83,270,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.10` | 388,580.00 USD | 13,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.11` | 83,260,000.00 USD | 83,260,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 83,260,000.00 USD | 83,260,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 83,260,000.00 USD | 83,260,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 83,240,000.00 USD | 83,240,000.00 USD | 28,830.00 USD | 4,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 83,200,000.00 USD | 83,200,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 283,400.00 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.12` | 75,920,000.00 USD | 75,920,000.00 USD | 0.00 USD | 16,040.00 USD | 112,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 83,190,000.00 USD | 83,190,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 75,790,000.00 USD | 75,790,000.00 USD | 7,460.00 USD | 48,180.00 USD | 41,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 75,690,000.00 USD | 75,690,000.00 USD | 16,420.00 USD | 60,880.00 USD | 88,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 83,110,000.00 USD | 83,110,000.00 USD | 17,190.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 75,530,000.00 USD | 75,530,000.00 USD | 5,470.00 USD | 1,530.00 USD | 84,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 83,090,000.00 USD | 83,090,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 75,440,000.00 USD | 75,440,000.00 USD | 79,690.00 USD | 29,190.00 USD | 63,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 83,090,000.00 USD | 83,090,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,230,000.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 75,260,000.00 USD | 75,260,000.00 USD | 12,370.00 USD | 1,260.00 USD | 105,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 75,140,000.00 USD | 75,140,000.00 USD | 69,610.00 USD | 60,790.00 USD | 142,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 82,880,000.00 USD | 82,880,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 74,870,000.00 USD | 74,870,000.00 USD | 0.00 USD | 66,770.00 USD | 168,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 82,680,000.00 USD | 82,680,000.00 USD | 5,450.00 USD | 3,410.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 74,640,000.00 USD | 74,640,000.00 USD | 63,980.00 USD | 37,600.00 USD | 5,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 82,670,000.00 USD | 82,670,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 74,530,000.00 USD | 74,530,000.00 USD | 0.00 USD | 122,160.00 USD | 66,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 82,190,000.00 USD | 82,190,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 129,840.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.14` | 74,340,000.00 USD | 74,340,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 81,950,000.00 USD | 81,950,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 74,250,000.00 USD | 74,250,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 81,850,000.00 USD | 81,850,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 74,220,000.00 USD | 74,220,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 81,840,000.00 USD | 81,840,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 74,160,000.00 USD | 74,160,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 81,780,000.00 USD | 81,780,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 74,020,000.00 USD | 74,020,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 81,660,000.00 USD | 81,660,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 306,590.00 USD | 10,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 81,650,000.00 USD | 81,650,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 73,980,000.00 USD | 73,980,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 81,510,000.00 USD | 81,510,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 81,150,000.00 USD | 81,150,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 73,960,000.00 USD | 73,960,000.00 USD | 4,040.00 USD | 14,590.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 80,990,000.00 USD | 80,990,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 73,760,000.00 USD | 73,760,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 80,610,000.00 USD | 80,610,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 337,540.00 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 73,420,000.00 USD | 73,420,000.00 USD | 72,570.00 USD | 16,310.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 79,960,000.00 USD | 79,960,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 73,300,000.00 USD | 73,300,000.00 USD | 126,860.00 USD | 16,130.00 USD | 446,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 79,160,000.00 USD | 79,160,000.00 USD | 265,410.00 USD | 70,050.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 72,710,000.00 USD | 72,710,000.00 USD | 253,200.00 USD | 126,280.00 USD | 170,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 78,520,000.00 USD | 78,520,000.00 USD | 352,520.00 USD | 494,920.00 USD | 654,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 72,160,000.00 USD | 72,160,000.00 USD | 253,180.00 USD | 314,800.00 USD | 334,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 77,020,000.00 USD | 77,020,000.00 USD | 485,880.00 USD | 177,220.00 USD | 811,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 71,260,000.00 USD | 71,260,000.00 USD | 95,890.00 USD | 51,030.00 USD | 486,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 75,550,000.00 USD | 75,550,000.00 USD | 209,000.00 USD | 168,650.00 USD | 491,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,290,000.00 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 70,630,000.00 USD | 70,630,000.00 USD | 146,120.00 USD | 120,500.00 USD | 131,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 74,680,000.00 USD | 74,680,000.00 USD | 454,610.00 USD | 248,780.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 70,230,000.00 USD | 70,230,000.00 USD | 111,200.00 USD | 95,250.00 USD | 206,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 72,910,000.00 USD | 72,910,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 69,810,000.00 USD | 69,810,000.00 USD | 361,890.00 USD | 3,910.00 USD | 415,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 71,410,000.00 USD | 71,410,000.00 USD | 502,470.00 USD | 180,770.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 69,030,000.00 USD | 69,030,000.00 USD | 104,550.00 USD | 79,710.00 USD | 360,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 70,010,000.00 USD | 70,010,000.00 USD | 290,530.00 USD | 139,010.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 68,490,000.00 USD | 68,490,000.00 USD | 396,370.00 USD | 140,700.00 USD | 416,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 68,410,000.00 USD | 68,410,000.00 USD | 520,770.00 USD | 90,550.00 USD | 499,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 394,220.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 67,540,000.00 USD | 67,540,000.00 USD | 71,610.00 USD | 44,040.00 USD | 250,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 67,300,000.00 USD | 67,300,000.00 USD | 154,760.00 USD | 59,570.00 USD | 473,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 67,170,000.00 USD | 67,170,000.00 USD | 90,040.00 USD | 42,260.00 USD | 198,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 66,610,000.00 USD | 66,610,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 66,840,000.00 USD | 66,840,000.00 USD | 144,240.00 USD | 19,410.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 65,900,000.00 USD | 65,900,000.00 USD | 69,670.00 USD | 117,700.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 66,670,000.00 USD | 66,670,000.00 USD | 150,010.00 USD | 19,860.00 USD | 660,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 65,510,000.00 USD | 65,510,000.00 USD | 254,520.00 USD | 92,820.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 65,840,000.00 USD | 65,840,000.00 USD | 225,800.00 USD | 63,560.00 USD | 143,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 65,160,000.00 USD | 65,160,000.00 USD | 123,240.00 USD | 581,580.00 USD | 764,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 520,520.00 USD | 7,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 65,400,000.00 USD | 65,400,000.00 USD | 109,160.00 USD | 518,680.00 USD | 653,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 63,690,000.00 USD | 63,690,000.00 USD | 229,250.00 USD | 60,320.00 USD | 621,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 64,120,000.00 USD | 64,120,000.00 USD | 360,560.00 USD | 90,130.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 62,780,000.00 USD | 62,780,000.00 USD | 182,110.00 USD | 138,450.00 USD | 757,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 62,380,000.00 USD | 62,380,000.00 USD | 61,250.00 USD | 47,660.00 USD | 373,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 61,700,000.00 USD | 61,700,000.00 USD | 140,460.00 USD | 503,850.00 USD | 906,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 61,900,000.00 USD | 61,900,000.00 USD | 157,580.00 USD | 502,360.00 USD | 448,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 60,150,000.00 USD | 60,150,000.00 USD | 147,020.00 USD | 91,800.00 USD | 467,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 60,790,000.00 USD | 60,790,000.00 USD | 381,040.00 USD | 157,690.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 59,440,000.00 USD | 59,440,000.00 USD | 348,260.00 USD | 72,600.00 USD | 247,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 672,400.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 58,210,000.00 USD | 58,210,000.00 USD | 748,570.00 USD | 84,750.00 USD | 788,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 58,770,000.00 USD | 58,770,000.00 USD | 5,350.00 USD | 1,100,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 56,590,000.00 USD | 56,590,000.00 USD | 112,900.00 USD | 934,870.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 55,870,000.00 USD | 55,870,000.00 USD | 553,590.00 USD | 399,490.00 USD | 949,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 54,030,000.00 USD | 54,030,000.00 USD | 730,270.00 USD | 464,920.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 53,960,000.00 USD | 53,960,000.00 USD | 293,850.00 USD | 223,240.00 USD | 470,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 51,200,000.00 USD | 51,200,000.00 USD | 314,820.00 USD | 47,550.00 USD | 740,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 52,980,000.00 USD | 52,980,000.00 USD | 226,160.00 USD | 696,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 50,100,000.00 USD | 50,100,000.00 USD | 295,960.00 USD | 920,650.00 USD | 246,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 52,050,000.00 USD | 52,050,000.00 USD | 0.00 USD | 37,150.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 12,330.00 USD | 6,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 48,640,000.00 USD | 48,640,000.00 USD | 825,290.00 USD | 104,970.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 52,010,000.00 USD | 52,010,000.00 USD | 66,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 46,380,000.00 USD | 46,380,000.00 USD | 1,590,000.00 USD | 227,220.00 USD | 824,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 51,940,000.00 USD | 51,940,000.00 USD | 576,740.00 USD | 84,270.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 43,740,000.00 USD | 43,740,000.00 USD | 160,630.00 USD | 650,810.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 49,670,000.00 USD | 49,670,000.00 USD | 1,100,000.00 USD | 408,100.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 41,290,000.00 USD | 41,290,000.00 USD | 1,350,000.00 USD | 271,760.00 USD | 998,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 46,690,000.00 USD | 46,690,000.00 USD | 302,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 38,670,000.00 USD | 38,670,000.00 USD | 52,290.00 USD | 154,650.00 USD | 685,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 46,380,000.00 USD | 46,380,000.00 USD | 49,970.00 USD | 0.00 USD | 910,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 40,860.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.22` | 37,780,000.00 USD | 37,780,000.00 USD | 307,460.00 USD | 26,150.00 USD | 176,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 45,420,000.00 USD | 45,420,000.00 USD | 157,620.00 USD | 9,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 37,270,000.00 USD | 37,270,000.00 USD | 203,470.00 USD | 49,690.00 USD | 10,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 45,260,000.00 USD | 45,260,000.00 USD | 308,930.00 USD | 0.00 USD | 432,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 37,000,000.00 USD | 37,000,000.00 USD | 64,370.00 USD | 321,780.00 USD | 300,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 44,520,000.00 USD | 44,520,000.00 USD | 85,970.00 USD | 928,300.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 36,320,000.00 USD | 36,320,000.00 USD | 106,100.00 USD | 0.00 USD | 348,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 43,490,000.00 USD | 43,490,000.00 USD | 51,610.00 USD | 330,390.00 USD | 31,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 35,860,000.00 USD | 35,860,000.00 USD | 270,600.00 USD | 510,520.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 43,070,000.00 USD | 43,070,000.00 USD | 0.00 USD | 476,630.00 USD | 4,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.23` | 32,440,000.00 USD | 32,440,000.00 USD | 107,280.00 USD | 64,900.00 USD | 86,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 42,590,000.00 USD | 42,590,000.00 USD | 171,930.00 USD | 761,700.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 32,180,000.00 USD | 32,180,000.00 USD | 556,720.00 USD | 1,090,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 41,640,000.00 USD | 41,640,000.00 USD | 0.00 USD | 1,080,000.00 USD | 817,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 28,080,000.00 USD | 28,080,000.00 USD | 66,520.00 USD | 1,250,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 39,740,000.00 USD | 39,740,000.00 USD | 969,900.00 USD | 495,660.00 USD | 791,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 24,410,000.00 USD | 24,410,000.00 USD | 1,480,000.00 USD | 505,910.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 37,490,000.00 USD | 37,490,000.00 USD | 1,090,000.00 USD | 1,080,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 20,210,000.00 USD | 20,210,000.00 USD | 241,040.00 USD | 1,490,000.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 33,330,000.00 USD | 33,330,000.00 USD | 1,920,000.00 USD | 2,020,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 16,710,000.00 USD | 16,710,000.00 USD | 18,660.00 USD | 428,450.00 USD | 134,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 27,260,000.00 USD | 27,260,000.00 USD | 1,640,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 16,130,000.00 USD | 16,130,000.00 USD | 15,170.00 USD | 220,870.00 USD | 931,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 20,490,000.00 USD | 20,490,000.00 USD | 2,610,000.00 USD | 1,380,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 14,960,000.00 USD | 14,960,000.00 USD | 734,030.00 USD | 182,970.00 USD | 651,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 15,060,000.00 USD | 15,060,000.00 USD | 1,820,000.00 USD | 374,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 13,390,000.00 USD | 13,390,000.00 USD | 658,110.00 USD | 818,040.00 USD | 994,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 12,860,000.00 USD | 12,860,000.00 USD | 896,470.00 USD | 15,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 10,920,000.00 USD | 10,920,000.00 USD | 1,640,000.00 USD | 134,980.00 USD | 379,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 11,950,000.00 USD | 11,950,000.00 USD | 3,330,000.00 USD | 0.00 USD | 700,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 8,760,000.00 USD | 8,760,000.00 USD | 700,330.00 USD | 712,880.00 USD | 997,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 7,920,000.00 USD | 7,920,000.00 USD | 2,700,000.00 USD | 662,610.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 6,350,000.00 USD | 6,350,000.00 USD | 331,570.00 USD | 602,270.00 USD | 356,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 5,060,000.00 USD | 5,060,000.00 USD | 202,510.00 USD | 1,390.00 USD | 993,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 9,140.00 USD | 455,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 3,860,000.00 USD | 3,860,000.00 USD | 17,600.00 USD | 8,750.00 USD | 4,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 860,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 3,830,000.00 USD | 3,830,000.00 USD | 633,250.00 USD | 12,640.00 USD | 681,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 1,650,000.00 USD | 1,650,000.00 USD | 213,660.00 USD | 39,910.00 USD | 801,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.25` | 559.73 USD | 559.73 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.26` | 2,510,000.00 USD | 2,510,000.00 USD | 936,860.00 USD | 443,180.00 USD | 551,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 593,100.00 USD | 593,100.00 USD | 0.00 USD | 249,600.00 USD | 239,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 575,170.00 USD | 575,170.00 USD | 192,760.00 USD | 38,980.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 103,580.00 USD | 103,580.00 USD | 0.00 USD | 21,230.00 USD | 82,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 332,220.00 USD | 332,220.00 USD | 264,250.00 USD | 22,310.00 USD | 45,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 2,750,000.00 USD | 2,750,000.00 USD | 144,170.00 USD | 23,560.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 5,500,000.00 USD | 5,500,000.00 USD | 144,170.00 USD | 23,560.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 3,840,000.00 USD | 3,840,000.00 USD | 1,250,000.00 USD | 819,120.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 9,290,000.00 USD | 9,290,000.00 USD | 834,020.00 USD | 803,260.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 7,450,000.00 USD | 7,450,000.00 USD | 479,740.00 USD | 980,510.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 16,950,000.00 USD | 16,950,000.00 USD | 1,640,000.00 USD | 1,350,000.00 USD | 4,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 116,940.00 USD | 117,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.27` | 11,770,000.00 USD | 11,770,000.00 USD | 745,260.00 USD | 1,270,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 30,590,000.00 USD | 30,590,000.00 USD | 2,620,000.00 USD | 2,380,000.00 USD | 8,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 14,960,000.00 USD | 14,960,000.00 USD | 466,250.00 USD | 2,030,000.00 USD | 697,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 35,820,000.00 USD | 35,820,000.00 USD | 52,540.00 USD | 2,640,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 18,960,000.00 USD | 18,960,000.00 USD | 647,480.00 USD | 1,080,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 40,210,000.00 USD | 40,210,000.00 USD | 1,010,000.00 USD | 2,540,000.00 USD | 842,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 23,790,000.00 USD | 23,790,000.00 USD | 1,840,000.00 USD | 1,040,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 47,040,000.00 USD | 47,040,000.00 USD | 468,870.00 USD | 4,920,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 29,810,000.00 USD | 29,810,000.00 USD | 814,880.00 USD | 2,270,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 63,710,000.00 USD | 63,710,000.00 USD | 4,840,000.00 USD | 2,350,000.00 USD | 9,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 15,590.00 USD | 133,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 36,800,000.00 USD | 36,800,000.00 USD | 1,940,000.00 USD | 1,760,000.00 USD | 3,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 82,330,000.00 USD | 82,330,000.00 USD | 6,930,000.00 USD | 3,330,000.00 USD | 8,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 44,620,000.00 USD | 44,620,000.00 USD | 3,090,000.00 USD | 2,110,000.00 USD | 2,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 88,630,000.00 USD | 88,630,000.00 USD | 3,260,000.00 USD | 1,950,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 46,030,000.00 USD | 46,030,000.00 USD | 257,680.00 USD | 558,100.00 USD | 586,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 89,590,000.00 USD | 89,590,000.00 USD | 0.00 USD | 883,970.00 USD | 79,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 49,140,000.00 USD | 49,140,000.00 USD | 1,260,000.00 USD | 301,200.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 91,650,000.00 USD | 91,650,000.00 USD | 1,510,000.00 USD | 480,590.00 USD | 67,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 52,000,000.00 USD | 52,000,000.00 USD | 633,890.00 USD | 677,470.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 96,090,000.00 USD | 96,090,000.00 USD | 712,000.00 USD | 1,720,000.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 48,740.00 USD | 181,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 54,340,000.00 USD | 54,340,000.00 USD | 828,650.00 USD | 960,560.00 USD | 545,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 97,250,000.00 USD | 97,250,000.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 54,720,000.00 USD | 54,720,000.00 USD | 210,950.00 USD | 24,800.00 USD | 148,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 97,370,000.00 USD | 97,370,000.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 55,210,000.00 USD | 55,210,000.00 USD | 177,490.00 USD | 42,820.00 USD | 268,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 99,660,000.00 USD | 99,660,000.00 USD | 1,060,000.00 USD | 202,640.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 58,210,000.00 USD | 58,210,000.00 USD | 570,020.00 USD | 197,630.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 100,280,000.00 USD | 100,280,000.00 USD | 119,390.00 USD | 0.00 USD | 497,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 64,380,000.00 USD | 64,380,000.00 USD | 1,880,000.00 USD | 719,050.00 USD | 3,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 109,980,000.00 USD | 109,980,000.00 USD | 3,420,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 66,950,000.00 USD | 66,950,000.00 USD | 554,720.00 USD | 703,990.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 111,300,000.00 USD | 111,300,000.00 USD | 209,360.00 USD | 480,300.00 USD | 628,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 67,710,000.00 USD | 67,710,000.00 USD | 335,370.00 USD | 109,620.00 USD | 312,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 113,470,000.00 USD | 113,470,000.00 USD | 25,800.00 USD | 183,900.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 69,960,000.00 USD | 69,960,000.00 USD | 530,940.00 USD | 364,450.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 115,190,000.00 USD | 115,190,000.00 USD | 264,890.00 USD | 486,620.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 71,990,000.00 USD | 71,990,000.00 USD | 761,460.00 USD | 808,970.00 USD | 455,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 118,400,000.00 USD | 118,400,000.00 USD | 29,580.00 USD | 2,690,000.00 USD | 485,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 73,270,000.00 USD | 73,270,000.00 USD | 304,340.00 USD | 649,450.00 USD | 327,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 118,400,000.00 USD | 118,400,000.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 1,630.00 USD | 183,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 75,640,000.00 USD | 75,640,000.00 USD | 736,330.00 USD | 147,250.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 121,410,000.00 USD | 121,410,000.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 79,060,000.00 USD | 79,060,000.00 USD | 1,160,000.00 USD | 424,760.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 126,190,000.00 USD | 126,190,000.00 USD | 1,700,000.00 USD | 1,150,000.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 81,320,000.00 USD | 81,320,000.00 USD | 899,580.00 USD | 565,300.00 USD | 801,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 129,530,000.00 USD | 129,530,000.00 USD | 839,350.00 USD | 511,590.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 83,340,000.00 USD | 83,340,000.00 USD | 729,330.00 USD | 341,030.00 USD | 944,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 132,370,000.00 USD | 132,370,000.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 85,610,000.00 USD | 85,610,000.00 USD | 342,500.00 USD | 387,380.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 134,830,000.00 USD | 134,830,000.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 90,810,000.00 USD | 90,810,000.00 USD | 1,300,000.00 USD | 929,120.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 139,450,000.00 USD | 139,450,000.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 95,690,000.00 USD | 95,690,000.00 USD | 1,680,000.00 USD | 733,340.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 142,540,000.00 USD | 142,540,000.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 98,650,000.00 USD | 98,650,000.00 USD | 1,500,000.00 USD | 499,050.00 USD | 959,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 144,370,000.00 USD | 144,370,000.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 101,770,000.00 USD | 101,770,000.00 USD | 997,120.00 USD | 481,660.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 148,820,000.00 USD | 148,820,000.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 102,910,000.00 USD | 102,910,000.00 USD | 710,170.00 USD | 83,050.00 USD | 341,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 151,190,000.00 USD | 151,190,000.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 36,960.00 USD | 220,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 104,050,000.00 USD | 104,050,000.00 USD | 481,530.00 USD | 225,260.00 USD | 436,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 151,730,000.00 USD | 151,730,000.00 USD | 462,320.00 USD | 8,400.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 105,540,000.00 USD | 105,540,000.00 USD | 504,110.00 USD | 72,470.00 USD | 911,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 153,020,000.00 USD | 153,020,000.00 USD | 90,750.00 USD | 110,720.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 107,710,000.00 USD | 107,710,000.00 USD | 848,670.00 USD | 101,110.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 154,750,000.00 USD | 154,750,000.00 USD | 581,420.00 USD | 273,310.00 USD | 869,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 109,660,000.00 USD | 109,660,000.00 USD | 737,030.00 USD | 194,040.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 158,840,000.00 USD | 158,840,000.00 USD | 1,450,000.00 USD | 406,200.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 110,990,000.00 USD | 110,990,000.00 USD | 459,140.00 USD | 356,270.00 USD | 517,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 159,380,000.00 USD | 159,380,000.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,950.00 USD | 222,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 111,740,000.00 USD | 111,740,000.00 USD | 388,720.00 USD | 23,420.00 USD | 332,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 161,330,000.00 USD | 161,330,000.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 112,340,000.00 USD | 112,340,000.00 USD | 179,460.00 USD | 83,160.00 USD | 334,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 163,670,000.00 USD | 163,670,000.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 113,850,000.00 USD | 113,850,000.00 USD | 701,920.00 USD | 312,600.00 USD | 499,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 168,150,000.00 USD | 168,150,000.00 USD | 2,650,000.00 USD | 1,400,000.00 USD | 423,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 115,900,000.00 USD | 115,900,000.00 USD | 963,900.00 USD | 368,440.00 USD | 716,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 173,700,000.00 USD | 173,700,000.00 USD | 1,700,000.00 USD | 2,610,000.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 117,470,000.00 USD | 117,470,000.00 USD | 556,930.00 USD | 328,690.00 USD | 683,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 183,980,000.00 USD | 183,980,000.00 USD | 3,320,000.00 USD | 1,810,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 17,080.00 USD | 239,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 118,060,000.00 USD | 118,060,000.00 USD | 206,540.00 USD | 183,280.00 USD | 204,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 190,920,000.00 USD | 190,920,000.00 USD | 2,310,000.00 USD | 2,160,000.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 118,720,000.00 USD | 118,720,000.00 USD | 305,090.00 USD | 33,600.00 USD | 316,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 200,520,000.00 USD | 200,520,000.00 USD | 4,230,000.00 USD | 1,560,000.00 USD | 3,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 119,200,000.00 USD | 119,200,000.00 USD | 201,390.00 USD | 41,110.00 USD | 237,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 207,860,000.00 USD | 207,860,000.00 USD | 2,210,000.00 USD | 1,380,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 119,380,000.00 USD | 119,380,000.00 USD | 100,960.00 USD | 30,780.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 215,640,000.00 USD | 215,640,000.00 USD | 2,610,000.00 USD | 1,030,000.00 USD | 4,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 119,950,000.00 USD | 119,950,000.00 USD | 86,720.00 USD | 34,870.00 USD | 451,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 222,970,000.00 USD | 222,970,000.00 USD | 3,390,000.00 USD | 710,240.00 USD | 3,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 2,700.00 USD | 242,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 120,910,000.00 USD | 120,910,000.00 USD | 391,410.00 USD | 32,820.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 226,750,000.00 USD | 226,750,000.00 USD | 1,340,000.00 USD | 802,060.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 121,240,000.00 USD | 121,240,000.00 USD | 209,880.00 USD | 43,200.00 USD | 82,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 230,540,000.00 USD | 230,540,000.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 121,900,000.00 USD | 121,900,000.00 USD | 225,120.00 USD | 162,390.00 USD | 269,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 232,710,000.00 USD | 232,710,000.00 USD | 696,770.00 USD | 547,690.00 USD | 925,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 122,200,000.00 USD | 122,200,000.00 USD | 130,140.00 USD | 3,300.00 USD | 166,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 236,810,000.00 USD | 236,810,000.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 122,320,000.00 USD | 122,320,000.00 USD | 0.00 USD | 12,740.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 238,530,000.00 USD | 238,530,000.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 193,360.00 USD | 435,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 122,570,000.00 USD | 122,570,000.00 USD | 59,970.00 USD | 89,800.00 USD | 103,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 239,010,000.00 USD | 239,010,000.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 122,720,000.00 USD | 122,720,000.00 USD | 93,070.00 USD | 21,460.00 USD | 28,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 240,430,000.00 USD | 240,430,000.00 USD | 528,490.00 USD | 135,290.00 USD | 750,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 122,820,000.00 USD | 122,820,000.00 USD | 5,340.00 USD | 39,430.00 USD | 60,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 241,580,000.00 USD | 241,580,000.00 USD | 351,750.00 USD | 349,810.00 USD | 445,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 122,910,000.00 USD | 122,910,000.00 USD | 5,470.00 USD | 1,530.00 USD | 84,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 243,630,000.00 USD | 243,630,000.00 USD | 680,710.00 USD | 318,880.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 123,080,000.00 USD | 123,080,000.00 USD | 79,690.00 USD | 29,190.00 USD | 63,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 245,390,000.00 USD | 245,390,000.00 USD | 519,370.00 USD | 275,610.00 USD | 966,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 61,720.00 USD | 497,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.38` | 123,200,000.00 USD | 123,200,000.00 USD | 12,370.00 USD | 1,260.00 USD | 105,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 246,410,000.00 USD | 246,410,000.00 USD | 417,010.00 USD | 308,370.00 USD | 300,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 123,480,000.00 USD | 123,480,000.00 USD | 69,610.00 USD | 60,790.00 USD | 142,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 248,270,000.00 USD | 248,270,000.00 USD | 573,060.00 USD | 190,650.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 123,540,000.00 USD | 123,540,000.00 USD | 0.00 USD | 65,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 250,370,000.00 USD | 250,370,000.00 USD | 1,020,000.00 USD | 249,550.00 USD | 825,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 123,710,000.00 USD | 123,710,000.00 USD | 0.00 USD | 1,250.00 USD | 168,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 251,300,000.00 USD | 251,300,000.00 USD | 297,210.00 USD | 273,610.00 USD | 361,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 123,820,000.00 USD | 123,820,000.00 USD | 63,980.00 USD | 37,600.00 USD | 5,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 252,590,000.00 USD | 252,590,000.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,280.00 USD | 498,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 124,010,000.00 USD | 124,010,000.00 USD | 0.00 USD | 122,160.00 USD | 66,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 253,130,000.00 USD | 253,130,000.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 124,100,000.00 USD | 124,100,000.00 USD | 40,370.00 USD | 48,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 254,230,000.00 USD | 254,230,000.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 254,400,000.00 USD | 254,400,000.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 254,720,000.00 USD | 254,720,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,890,000.00 USD | 254,890,000.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 2,090.00 USD | 500,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 255,010,000.00 USD | 255,010,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 255,020,000.00 USD | 255,020,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 255,160,000.00 USD | 255,160,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 255,270,000.00 USD | 255,270,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 255,510,000.00 USD | 255,510,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 17,770.00 USD | 518,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 255,680,000.00 USD | 255,680,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 256,060,000.00 USD | 256,060,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 256,710,000.00 USD | 256,710,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 256,880,000.00 USD | 256,880,000.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 257,510,000.00 USD | 257,510,000.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,930.00 USD | 522,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.42` | 258,030,000.00 USD | 258,030,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 259,050,000.00 USD | 259,050,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 260,430,000.00 USD | 260,430,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 261,040,000.00 USD | 261,040,000.00 USD | 202,370.00 USD | 161,570.00 USD | 244,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,510.00 USD | 615,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 3,800.00 USD | 619,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 284.66 USD | 619,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.46` | 565,040.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 128,580.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,470.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 11,570.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 174.99 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 1,370.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 679.21 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,900.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 4,540.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 4,260,000.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 239.15 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 4,590.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 271.38 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 3,530.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 135,940.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 4,180.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 974.62 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 4,200.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 5,250.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 1,430.00 USD | 5,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,730.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 591.43 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 808.37 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 876.85 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 5,330,000.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 2,690.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 190,860.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 260.98 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 425.72 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 120,750.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 428.50 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,880,000.00 USD | 14,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 2,880,000.00 USD | 17,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,190.00 USD | 17,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 256,010.00 USD | 17,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 160.86 USD | 17,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 39,740.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 315,580.00 USD | 17,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 17,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 228,250.00 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 164.41 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 513.83 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 121.50 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 787.55 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 409,200.00 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 832.19 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 1,240.00 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 294.70 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 251,390.00 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.13` | 16,560.00 USD | 18,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 18,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 437.33 USD | 18,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,730.00 USD | 18,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 100.51 USD | 18,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 132,960.00 USD | 18,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 101.89 USD | 18,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 11,460.00 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 102.81 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 103.27 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 121,240.00 USD | 18,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 212.06 USD | 18,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 250.02 USD | 18,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 2,850.00 USD | 18,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 11,810.00 USD | 19,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 469.00 USD | 19,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 2,570.00 USD | 19,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 551.05 USD | 19,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 3,590,000.00 USD | 22,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 94,360.00 USD | 22,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 1,160.00 USD | 22,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 169.75 USD | 22,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 24,510.00 USD | 22,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 3,580.00 USD | 22,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 360.88 USD | 22,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 23,250.00 USD | 22,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 306.90 USD | 22,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 95,780.00 USD | 22,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 201,990.00 USD | 23,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 64,470,000.00 USD | 0.00 USD | 8,750.00 USD | `-79.66%` | `34,317.00` |
| `Live` | `Long` | `0.2750` | 64,460,000.00 USD | 0.00 USD | 1,090.00 USD | `-78.06%` | `3,950.00` |
| `Live` | `Long` | `0.2850` | 64,460,000.00 USD | 0.00 USD | 25,980.00 USD | `-77.26%` | `91,168.00` |
| `Live` | `Long` | `0.2950` | 64,440,000.00 USD | 0.00 USD | 20,650.00 USD | `-76.46%` | `69,994.00` |
| `Live` | `Long` | `0.3050` | 64,410,000.00 USD | 0.00 USD | 9,190.00 USD | `-75.67%` | `30,141.00` |
| `Live` | `Long` | `0.3150` | 64,410,000.00 USD | 0.00 USD | 5,840.00 USD | `-74.87%` | `18,525.00` |
| `Live` | `Long` | `0.3350` | 64,400,000.00 USD | 0.00 USD | 28,240.00 USD | `-73.27%` | `84,306.00` |
| `Live` | `Long` | `0.3450` | 64,370,000.00 USD | 0.00 USD | 6,060.00 USD | `-72.47%` | `17,571.00` |
| `Live` | `Long` | `0.3550` | 64,370,000.00 USD | 0.00 USD | 1,280.00 USD | `-71.68%` | `3,619.00` |
| `Live` | `Long` | `0.3650` | 64,360,000.00 USD | 0.00 USD | 4,090.00 USD | `-70.88%` | `11,212.00` |
| `Live` | `Long` | `0.3750` | 64,360,000.00 USD | 0.00 USD | 6,600.00 USD | `-70.08%` | `17,605.00` |
| `Live` | `Long` | `0.3950` | 64,350,000.00 USD | 0.00 USD | 139,290.00 USD | `-68.49%` | `352,642.00` |
| `Live` | `Long` | `0.4050` | 64,210,000.00 USD | 0.00 USD | 530,660.00 USD | `-67.69%` | `1,310,276.00` |
| `Live` | `Long` | `0.4150` | 63,680,000.00 USD | 0.00 USD | 509.62 USD | `-66.89%` | `1,228.00` |
| `Live` | `Long` | `0.4250` | 63,680,000.00 USD | 0.00 USD | 3,700.00 USD | `-66.09%` | `8,700.00` |
| `Live` | `Long` | `0.4350` | 63,680,000.00 USD | 0.00 USD | 15,820.00 USD | `-65.29%` | `36,365.00` |
| `Live` | `Long` | `0.4550` | 63,660,000.00 USD | 0.00 USD | 632.90 USD | `-63.70%` | `1,391.00` |
| `Live` | `Long` | `0.4750` | 63,660,000.00 USD | 0.00 USD | 4,610.00 USD | `-62.10%` | `9,705.00` |
| `Live` | `Long` | `0.4850` | 63,660,000.00 USD | 0.00 USD | 13,480.00 USD | `-61.31%` | `27,793.00` |
| `Live` | `Long` | `0.4950` | 63,640,000.00 USD | 0.00 USD | 2,220.00 USD | `-60.51%` | `4,475.00` |
| `Live` | `Long` | `0.5050` | 63,640,000.00 USD | 0.00 USD | 2,660.00 USD | `-59.71%` | `5,258.00` |
| `Live` | `Long` | `0.5150` | 63,640,000.00 USD | 0.00 USD | 8,250.00 USD | `-58.91%` | `16,012.00` |
| `Live` | `Long` | `0.5250` | 63,630,000.00 USD | 0.00 USD | 2,340.00 USD | `-58.11%` | `4,460.00` |
| `Live` | `Long` | `0.5350` | 63,630,000.00 USD | 0.00 USD | 3,420.00 USD | `-57.32%` | `6,390.00` |
| `Live` | `Long` | `0.5450` | 63,630,000.00 USD | 0.00 USD | 164,540.00 USD | `-56.52%` | `301,902.00` |
| `Live` | `Long` | `0.5550` | 63,460,000.00 USD | 0.00 USD | 1,110.00 USD | `-55.72%` | `2,009.00` |
| `Live` | `Long` | `0.5650` | 63,460,000.00 USD | 0.00 USD | 1,600.00 USD | `-54.92%` | `2,839.00` |
| `Live` | `Long` | `0.5750` | 63,460,000.00 USD | 0.00 USD | 7,820.00 USD | `-54.12%` | `13,601.00` |
| `Live` | `Long` | `0.5850` | 63,450,000.00 USD | 0.00 USD | 1,970.00 USD | `-53.33%` | `3,376.00` |
| `Live` | `Long` | `0.5950` | 63,450,000.00 USD | 0.00 USD | 5,380.00 USD | `-52.53%` | `9,046.00` |
| `Live` | `Long` | `0.6050` | 63,440,000.00 USD | 0.00 USD | 24,310.00 USD | `-51.73%` | `40,178.00` |
| `Live` | `Long` | `0.6150` | 63,420,000.00 USD | 0.00 USD | 32,120.00 USD | `-50.93%` | `52,223.00` |
| `Live` | `Long` | `0.6250` | 63,390,000.00 USD | 0.00 USD | 33,040.00 USD | `-50.14%` | `52,858.00` |
| `Live` | `Long` | `0.6350` | 63,350,000.00 USD | 0.00 USD | 11,070.00 USD | `-49.34%` | `17,430.00` |
| `Live` | `Long` | `0.6450` | 63,340,000.00 USD | 0.00 USD | 21,460.00 USD | `-48.54%` | `33,272.00` |
| `Live` | `Long` | `0.6550` | 63,320,000.00 USD | 0.00 USD | 5,440.00 USD | `-47.74%` | `8,312.00` |
| `Live` | `Long` | `0.6650` | 63,320,000.00 USD | 0.00 USD | 17,830.00 USD | `-46.94%` | `26,813.00` |
| `Live` | `Long` | `0.6750` | 63,300,000.00 USD | 0.00 USD | 37,140.00 USD | `-46.15%` | `55,029.00` |
| `Live` | `Long` | `0.6850` | 63,260,000.00 USD | 0.00 USD | 5,800.00 USD | `-45.35%` | `8,473.00` |
| `Live` | `Long` | `0.6950` | 63,250,000.00 USD | 0.00 USD | 161,800.00 USD | `-44.55%` | `232,806.00` |
| `Live` | `Long` | `0.7050` | 63,090,000.00 USD | 0.00 USD | 19,510.00 USD | `-43.75%` | `27,677.00` |
| `Live` | `Long` | `0.7150` | 63,070,000.00 USD | 0.00 USD | 70,640.00 USD | `-42.96%` | `98,791.00` |
| `Live` | `Long` | `0.7250` | 63,000,000.00 USD | 0.00 USD | 245,330.00 USD | `-42.16%` | `338,391.00` |
| `Live` | `Long` | `0.7350` | 62,760,000.00 USD | 0.00 USD | 73,300.00 USD | `-41.36%` | `99,726.00` |
| `Live` | `Long` | `0.7450` | 62,680,000.00 USD | 0.00 USD | 113,230.00 USD | `-40.56%` | `151,990.00` |
| `Live` | `Long` | `0.7550` | 62,570,000.00 USD | 0.00 USD | 88,950.00 USD | `-39.76%` | `117,815.00` |
| `Live` | `Long` | `0.7650` | 62,480,000.00 USD | 0.00 USD | 2,190.00 USD | `-38.97%` | `2,860.00` |
| `Live` | `Long` | `0.7750` | 62,480,000.00 USD | 0.00 USD | 7,080.00 USD | `-38.17%` | `9,140.00` |
| `Live` | `Long` | `0.7850` | 62,470,000.00 USD | 0.00 USD | 507,020.00 USD | `-37.37%` | `645,886.00` |
| `Live` | `Long` | `0.7950` | 61,970,000.00 USD | 0.00 USD | 19,410.00 USD | `-36.57%` | `24,409.00` |
| `Live` | `Long` | `0.8050` | 61,950,000.00 USD | 0.00 USD | 17,740.00 USD | `-35.77%` | `22,042.00` |
| `Live` | `Long` | `0.8150` | 61,930,000.00 USD | 0.00 USD | 2,940,000.00 USD | `-34.98%` | `3,602,095.00` |
| `Live` | `Long` | `0.8250` | 58,990,000.00 USD | 0.00 USD | 136,650.00 USD | `-34.18%` | `165,633.00` |
| `Live` | `Long` | `0.8350` | 58,860,000.00 USD | 0.00 USD | 42,390.00 USD | `-33.38%` | `50,768.00` |
| `Live` | `Long` | `0.8450` | 58,810,000.00 USD | 0.00 USD | 59,040.00 USD | `-32.58%` | `69,872.00` |
| `Live` | `Long` | `0.8550` | 58,750,000.00 USD | 0.00 USD | 56,260.00 USD | `-31.79%` | `65,798.00` |
| `Live` | `Long` | `0.8650` | 58,700,000.00 USD | 0.00 USD | 14,630.00 USD | `-30.99%` | `16,919.00` |
| `Live` | `Long` | `0.8750` | 58,680,000.00 USD | 0.00 USD | 107,360.00 USD | `-30.19%` | `122,695.00` |
| `Live` | `Long` | `0.8850` | 58,580,000.00 USD | 0.00 USD | 352,960.00 USD | `-29.39%` | `398,825.00` |
| `Live` | `Long` | `0.8950` | 58,220,000.00 USD | 0.00 USD | 87,440.00 USD | `-28.59%` | `97,701.00` |
| `Live` | `Long` | `0.9050` | 58,140,000.00 USD | 0.00 USD | 163,090.00 USD | `-27.80%` | `180,215.00` |
| `Live` | `Long` | `0.9150` | 57,970,000.00 USD | 0.00 USD | 136,030.00 USD | `-27.00%` | `148,666.00` |
| `Live` | `Long` | `0.9250` | 57,840,000.00 USD | 0.00 USD | 69,680.00 USD | `-26.20%` | `75,328.00` |
| `Live` | `Long` | `0.9350` | 57,770,000.00 USD | 0.00 USD | 199,270.00 USD | `-25.40%` | `213,126.00` |
| `Live` | `Long` | `0.9450` | 57,570,000.00 USD | 0.00 USD | 57,060.00 USD | `-24.61%` | `60,378.00` |
| `Live` | `Long` | `0.9550` | 57,510,000.00 USD | 0.00 USD | 152,100.00 USD | `-23.81%` | `159,272.00` |
| `Live` | `Long` | `0.9650` | 57,360,000.00 USD | 0.00 USD | 33,890,000.00 USD | `-23.01%` | `35,121,040.00` |
| `Live` | `Long` | `0.9750` | 23,470,000.00 USD | 0.00 USD | 177,550.00 USD | `-22.21%` | `182,104.00` |
| `Live` | `Long` | `0.9850` | 23,290,000.00 USD | 0.00 USD | 2,990,000.00 USD | `-21.41%` | `3,031,520.00` |
| `Live` | `Long` | `0.9950` | 20,300,000.00 USD | 0.00 USD | 130,060.00 USD | `-20.62%` | `130,718.00` |
| `Live` | `Long` | `1.00` | 20,170,000.00 USD | 0.00 USD | 490,240.00 USD | `-19.82%` | `487,803.00` |
| `Live` | `Long` | `1.01` | 19,680,000.00 USD | 0.00 USD | 346,370.00 USD | `-19.02%` | `341,252.00` |
| `Live` | `Long` | `1.02` | 19,340,000.00 USD | 0.00 USD | 59,550.00 USD | `-18.22%` | `58,097.00` |
| `Live` | `Long` | `1.03` | 19,280,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-17.42%` | `2,048,357.00` |
| `Live` | `Long` | `1.04` | 17,160,000.00 USD | 0.00 USD | 660,310.00 USD | `-16.63%` | `631,874.00` |
| `Live` | `Long` | `1.05` | 16,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | `-15.83%` | `1,419,096.00` |
| `Live` | `Long` | `1.06` | 15,000,000.00 USD | 0.00 USD | 378,350.00 USD | `-15.03%` | `355,256.00` |
| `Live` | `Long` | `1.07` | 14,620,000.00 USD | 0.00 USD | 950,500.00 USD | `-14.23%` | `884,182.00` |
| `Live` | `Long` | `1.08` | 13,670,000.00 USD | 0.00 USD | 191,170.00 USD | `-13.44%` | `176,192.00` |
| `Live` | `Long` | `1.09` | 13,480,000.00 USD | 0.00 USD | 361,000.00 USD | `-12.64%` | `329,682.00` |
| `Live` | `Long` | `1.10` | 13,120,000.00 USD | 0.00 USD | 388,580.00 USD | `-11.84%` | `351,656.00` |
| `Live` | `Long` | `1.11` | 12,730,000.00 USD | 0.00 USD | 283,400.00 USD | `-11.04%` | `254,169.00` |
| `Live` | `Long` | `1.12` | 12,450,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-10.24%` | `1,986,295.00` |
| `Live` | `Long` | `1.14` | 10,210,000.00 USD | 0.00 USD | 129,840.00 USD | `-9.45%` | `114,400.00` |
| `Live` | `Long` | `1.15` | 10,080,000.00 USD | 0.00 USD | 306,590.00 USD | `-8.65%` | `267,767.00` |
| `Live` | `Long` | `1.16` | 9,780,000.00 USD | 0.00 USD | 337,540.00 USD | `-7.85%` | `292,239.00` |
| `Live` | `Long` | `1.17` | 9,440,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-7.05%` | `1,105,276.00` |
| `Live` | `Long` | `1.18` | 8,150,000.00 USD | 0.00 USD | 394,220.00 USD | `-6.25%` | `335,506.00` |
| `Live` | `Long` | `1.19` | 7,760,000.00 USD | 0.00 USD | 520,520.00 USD | `-5.46%` | `439,259.00` |
| `Live` | `Long` | `1.20` | 7,240,000.00 USD | 0.00 USD | 672,400.00 USD | `-4.66%` | `562,674.00` |
| `Live` | `Long` | `1.21` | 6,560,000.00 USD | 0.00 USD | 12,330.00 USD | `-3.86%` | `10,233.00` |
| `Live` | `Long` | `1.22` | 6,550,000.00 USD | 0.00 USD | 40,860.00 USD | `-3.06%` | `33,630.00` |
| `Live` | `Long` | `1.23` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | `-2.27%` | `5,314,604.00` |
| `Live` | `Short` | `1.25` | 559.73 USD | 559.73 USD | 0.00 USD | `+0.13%` | `446.00` |
| `Live` | `Short` | `1.26` | 117,500.00 USD | 116,940.00 USD | 0.00 USD | `+0.93%` | `92,442.00` |
| `Live` | `Short` | `1.27` | 133,090.00 USD | 15,590.00 USD | 0.00 USD | `+1.72%` | `12,225.00` |
| `Live` | `Short` | `1.28` | 181,830.00 USD | 48,740.00 USD | 0.00 USD | `+2.52%` | `37,930.00` |
| `Live` | `Short` | `1.30` | 183,450.00 USD | 1,630.00 USD | 0.00 USD | `+4.12%` | `1,246.00` |
| `Live` | `Short` | `1.32` | 220,410.00 USD | 36,960.00 USD | 0.00 USD | `+5.71%` | `27,896.00` |
| `Live` | `Short` | `1.33` | 222,370.00 USD | 1,950.00 USD | 0.00 USD | `+6.51%` | `1,462.00` |
| `Live` | `Short` | `1.34` | 239,450.00 USD | 17,080.00 USD | 0.00 USD | `+7.31%` | `12,702.00` |
| `Live` | `Short` | `1.35` | 242,150.00 USD | 2,700.00 USD | 0.00 USD | `+8.11%` | `1,989.00` |
| `Live` | `Short` | `1.36` | 435,510.00 USD | 193,360.00 USD | 0.00 USD | `+8.90%` | `141,656.00` |
| `Live` | `Short` | `1.38` | 497,230.00 USD | 61,720.00 USD | 0.00 USD | `+9.70%` | `44,888.00` |
| `Live` | `Short` | `1.39` | 498,500.00 USD | 1,280.00 USD | 0.00 USD | `+10.50%` | `921.00` |
| `Live` | `Short` | `1.40` | 500,590.00 USD | 2,090.00 USD | 0.00 USD | `+11.30%` | `1,500.00` |
| `Live` | `Short` | `1.41` | 518,360.00 USD | 17,770.00 USD | 0.00 USD | `+12.10%` | `12,646.00` |
| `Live` | `Short` | `1.42` | 522,290.00 USD | 3,930.00 USD | 0.00 USD | `+12.89%` | `2,776.00` |
| `Live` | `Short` | `1.43` | 615,800.00 USD | 93,510.00 USD | 0.00 USD | `+13.69%` | `65,619.00` |
| `Live` | `Short` | `1.44` | 619,600.00 USD | 3,800.00 USD | 0.00 USD | `+14.49%` | `2,649.00` |
| `Live` | `Short` | `1.45` | 619,880.00 USD | 284.66 USD | 0.00 USD | `+15.29%` | `197.00` |
| `Live` | `Short` | `1.46` | 1,180,000.00 USD | 565,040.00 USD | 0.00 USD | `+16.08%` | `388,344.00` |
| `Live` | `Short` | `1.47` | 1,310,000.00 USD | 128,580.00 USD | 0.00 USD | `+16.88%` | `87,771.00` |
| `Live` | `Short` | `1.50` | 1,330,000.00 USD | 12,470.00 USD | 0.00 USD | `+19.28%` | `8,338.00` |
| `Live` | `Short` | `1.51` | 1,340,000.00 USD | 11,570.00 USD | 0.00 USD | `+20.87%` | `7,640.00` |
| `Live` | `Short` | `1.53` | 1,340,000.00 USD | 174.99 USD | 0.00 USD | `+22.47%` | `114.00` |
| `Live` | `Short` | `1.54` | 1,340,000.00 USD | 1,370.00 USD | 0.00 USD | `+23.26%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,340,000.00 USD | 1,360.00 USD | 0.00 USD | `+24.06%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,340,000.00 USD | 679.21 USD | 0.00 USD | `+24.86%` | `434.00` |
| `Live` | `Short` | `1.57` | 1,340,000.00 USD | 2,900.00 USD | 0.00 USD | `+25.66%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 1,350,000.00 USD | 4,540.00 USD | 0.00 USD | `+26.46%` | `2,867.00` |
| `Live` | `Short` | `1.59` | 5,610,000.00 USD | 4,260,000.00 USD | 0.00 USD | `+27.25%` | `2,672,981.00` |
| `Live` | `Short` | `1.60` | 5,610,000.00 USD | 239.15 USD | 0.00 USD | `+28.05%` | `149.00` |
| `Live` | `Short` | `1.61` | 5,620,000.00 USD | 4,590.00 USD | 0.00 USD | `+28.85%` | `2,842.00` |
| `Live` | `Short` | `1.62` | 5,620,000.00 USD | 271.38 USD | 0.00 USD | `+29.65%` | `167.00` |
| `Live` | `Short` | `1.64` | 5,620,000.00 USD | 3,530.00 USD | 0.00 USD | `+30.45%` | `2,160.00` |
| `Live` | `Short` | `1.65` | 5,760,000.00 USD | 135,940.00 USD | 0.00 USD | `+31.24%` | `82,639.00` |
| `Live` | `Short` | `1.66` | 5,760,000.00 USD | 147.30 USD | 0.00 USD | `+32.04%` | `89.00` |
| `Live` | `Short` | `1.67` | 5,760,000.00 USD | 586.08 USD | 0.00 USD | `+32.84%` | `352.00` |
| `Live` | `Short` | `1.69` | 5,760,000.00 USD | 4,180.00 USD | 0.00 USD | `+34.43%` | `2,481.00` |
| `Live` | `Short` | `1.70` | 5,760,000.00 USD | 974.62 USD | 0.00 USD | `+35.23%` | `575.00` |
| `Live` | `Short` | `1.71` | 5,770,000.00 USD | 4,200.00 USD | 0.00 USD | `+36.03%` | `2,466.00` |
| `Live` | `Short` | `1.72` | 5,770,000.00 USD | 5,250.00 USD | 0.00 USD | `+36.83%` | `3,059.00` |
| `Live` | `Short` | `1.73` | 5,770,000.00 USD | 1,430.00 USD | 0.00 USD | `+37.63%` | `829.00` |
| `Live` | `Short` | `1.74` | 5,780,000.00 USD | 2,970.00 USD | 0.00 USD | `+38.42%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 5,780,000.00 USD | 2,730.00 USD | 0.00 USD | `+39.22%` | `1,564.00` |
| `Live` | `Short` | `1.75` | 5,780,000.00 USD | 591.43 USD | 0.00 USD | `+40.02%` | `337.00` |
| `Live` | `Short` | `1.76` | 5,780,000.00 USD | 808.37 USD | 0.00 USD | `+40.82%` | `458.00` |
| `Live` | `Short` | `1.77` | 5,780,000.00 USD | 876.85 USD | 0.00 USD | `+41.61%` | `494.00` |
| `Live` | `Short` | `1.78` | 11,110,000.00 USD | 5,330,000.00 USD | 0.00 USD | `+42.41%` | `2,986,501.00` |
| `Live` | `Short` | `1.79` | 11,110,000.00 USD | 2,690.00 USD | 0.00 USD | `+43.21%` | `1,500.00` |
| `Live` | `Short` | `1.80` | 11,120,000.00 USD | 889.87 USD | 0.00 USD | `+44.01%` | `493.00` |
| `Live` | `Short` | `1.81` | 11,310,000.00 USD | 190,860.00 USD | 0.00 USD | `+44.81%` | `105,157.00` |
| `Live` | `Short` | `1.82` | 11,310,000.00 USD | 260.98 USD | 0.00 USD | `+45.60%` | `143.00` |
| `Live` | `Short` | `1.83` | 11,310,000.00 USD | 425.72 USD | 0.00 USD | `+46.40%` | `232.00` |
| `Live` | `Short` | `1.84` | 11,430,000.00 USD | 120,750.00 USD | 0.00 USD | `+47.20%` | `65,447.00` |
| `Live` | `Short` | `1.85` | 11,430,000.00 USD | 428.50 USD | 0.00 USD | `+48.00%` | `231.00` |
| `Live` | `Short` | `1.86` | 14,300,000.00 USD | 2,880,000.00 USD | 0.00 USD | `+48.80%` | `1,541,696.00` |
| `Live` | `Short` | `1.89` | 17,190,000.00 USD | 2,880,000.00 USD | 0.00 USD | `+50.39%` | `1,529,461.00` |
| `Live` | `Short` | `1.90` | 17,190,000.00 USD | 4,190.00 USD | 0.00 USD | `+51.19%` | `2,211.00` |
| `Live` | `Short` | `1.91` | 17,450,000.00 USD | 256,010.00 USD | 0.00 USD | `+51.99%` | `134,388.00` |
| `Live` | `Short` | `1.92` | 17,450,000.00 USD | 160.86 USD | 0.00 USD | `+52.78%` | `84.00` |
| `Live` | `Short` | `1.93` | 17,490,000.00 USD | 39,740.00 USD | 0.00 USD | `+53.58%` | `20,643.00` |
| `Live` | `Short` | `1.94` | 17,800,000.00 USD | 315,580.00 USD | 0.00 USD | `+54.38%` | `163,092.00` |
| `Live` | `Short` | `1.96` | 17,800,000.00 USD | 293.25 USD | 0.00 USD | `+55.98%` | `150.00` |
| `Live` | `Short` | `1.97` | 18,030,000.00 USD | 228,250.00 USD | 0.00 USD | `+56.77%` | `116,156.00` |
| `Live` | `Short` | `1.98` | 18,030,000.00 USD | 651.75 USD | 0.00 USD | `+57.57%` | `330.00` |
| `Live` | `Short` | `2.00` | 18,030,000.00 USD | 164.41 USD | 0.00 USD | `+59.96%` | `82.00` |
| `Live` | `Short` | `2.02` | 18,030,000.00 USD | 513.83 USD | 0.00 USD | `+60.76%` | `255.00` |
| `Live` | `Short` | `2.02` | 18,030,000.00 USD | 121.50 USD | 0.00 USD | `+61.56%` | `60.00` |
| `Live` | `Short` | `2.04` | 18,030,000.00 USD | 787.55 USD | 0.00 USD | `+62.36%` | `387.00` |
| `Live` | `Short` | `2.04` | 18,440,000.00 USD | 409,200.00 USD | 0.00 USD | `+63.16%` | `200,097.00` |
| `Live` | `Short` | `2.06` | 18,440,000.00 USD | 832.19 USD | 0.00 USD | `+64.75%` | `403.00` |
| `Live` | `Short` | `2.10` | 18,440,000.00 USD | 1,240.00 USD | 0.00 USD | `+67.15%` | `592.00` |
| `Live` | `Short` | `2.10` | 18,440,000.00 USD | 294.70 USD | 0.00 USD | `+67.94%` | `140.00` |
| `Live` | `Short` | `2.12` | 18,700,000.00 USD | 251,390.00 USD | 0.00 USD | `+68.74%` | `118,859.00` |
| `Live` | `Short` | `2.13` | 18,710,000.00 USD | 16,560.00 USD | 0.00 USD | `+70.34%` | `7,757.00` |
| `Live` | `Short` | `2.15` | 18,710,000.00 USD | 196.11 USD | 0.00 USD | `+71.93%` | `91.00` |
| `Live` | `Short` | `2.17` | 18,710,000.00 USD | 437.33 USD | 0.00 USD | `+72.73%` | `202.00` |
| `Live` | `Short` | `2.17` | 18,720,000.00 USD | 2,730.00 USD | 0.00 USD | `+73.53%` | `1,253.00` |
| `Live` | `Short` | `2.19` | 18,720,000.00 USD | 100.51 USD | 0.00 USD | `+74.33%` | `46.00` |
| `Live` | `Short` | `2.19` | 18,850,000.00 USD | 132,960.00 USD | 0.00 USD | `+75.12%` | `60,572.00` |
| `Live` | `Short` | `2.21` | 18,850,000.00 USD | 101.89 USD | 0.00 USD | `+76.72%` | `46.00` |
| `Live` | `Short` | `2.23` | 18,860,000.00 USD | 11,460.00 USD | 0.00 USD | `+77.52%` | `5,152.00` |
| `Live` | `Short` | `2.23` | 18,860,000.00 USD | 102.81 USD | 0.00 USD | `+78.31%` | `46.00` |
| `Live` | `Short` | `2.25` | 18,860,000.00 USD | 103.27 USD | 0.00 USD | `+79.11%` | `46.00` |
| `Live` | `Short` | `2.29` | 18,980,000.00 USD | 121,240.00 USD | 0.00 USD | `+83.10%` | `52,830.00` |
| `Live` | `Short` | `2.31` | 18,980,000.00 USD | 212.06 USD | 0.00 USD | `+83.90%` | `92.00` |
| `Live` | `Short` | `2.31` | 18,980,000.00 USD | 250.02 USD | 0.00 USD | `+84.70%` | `108.00` |
| `Live` | `Short` | `2.33` | 18,990,000.00 USD | 2,850.00 USD | 0.00 USD | `+85.50%` | `1,227.00` |
| `Live` | `Short` | `2.33` | 19,000,000.00 USD | 11,810.00 USD | 0.00 USD | `+86.29%` | `5,057.00` |
| `Live` | `Short` | `2.35` | 19,000,000.00 USD | 469.00 USD | 0.00 USD | `+87.09%` | `200.00` |
| `Live` | `Short` | `2.35` | 19,000,000.00 USD | 2,570.00 USD | 0.00 USD | `+87.89%` | `1,090.00` |
| `Live` | `Short` | `2.37` | 19,000,000.00 USD | 551.05 USD | 0.00 USD | `+88.69%` | `233.00` |
| `Live` | `Short` | `2.38` | 22,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | `+89.48%` | `1,511,779.00` |
| `Live` | `Short` | `2.40` | 22,690,000.00 USD | 94,360.00 USD | 0.00 USD | `+91.08%` | `39,397.00` |
| `Live` | `Short` | `2.42` | 22,690,000.00 USD | 1,160.00 USD | 0.00 USD | `+92.68%` | `481.00` |
| `Live` | `Short` | `2.42` | 22,690,000.00 USD | 169.75 USD | 0.00 USD | `+93.47%` | `70.00` |
| `Live` | `Short` | `2.44` | 22,710,000.00 USD | 24,510.00 USD | 0.00 USD | `+94.27%` | `10,065.00` |
| `Live` | `Short` | `2.44` | 22,720,000.00 USD | 3,580.00 USD | 0.00 USD | `+95.07%` | `1,463.00` |
| `Live` | `Short` | `2.46` | 22,720,000.00 USD | 360.88 USD | 0.00 USD | `+95.87%` | `147.00` |
| `Live` | `Short` | `2.46` | 22,740,000.00 USD | 23,250.00 USD | 0.00 USD | `+96.67%` | `9,432.00` |
| `Live` | `Short` | `2.48` | 22,740,000.00 USD | 306.90 USD | 0.00 USD | `+97.46%` | `124.00` |
| `Live` | `Short` | `2.48` | 22,830,000.00 USD | 95,780.00 USD | 0.00 USD | `+98.26%` | `38,544.00` |
| `Live` | `Short` | `2.50` | 23,040,000.00 USD | 201,990.00 USD | 0.00 USD | `+99.06%` | `80,958.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 2,180,000.00 USD | 0.00 USD | 102.00 USD | `-79.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3650` | 2,180,000.00 USD | 0.00 USD | 351.50 USD | `-70.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 2,180,000.00 USD | 0.00 USD | 139.12 USD | `-70.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3950` | 2,180,000.00 USD | 0.00 USD | 2,880.00 USD | `-68.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4050` | 2,180,000.00 USD | 0.00 USD | 2,950.00 USD | `-67.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 2,170,000.00 USD | 0.00 USD | 408.51 USD | `-64.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 2,170,000.00 USD | 0.00 USD | 273.00 USD | `-63.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 2,170,000.00 USD | 0.00 USD | 151.12 USD | `-62.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 2,170,000.00 USD | 0.00 USD | 142.50 USD | `-62.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 2,170,000.00 USD | 0.00 USD | 145.50 USD | `-61.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 2,170,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 2,170,000.00 USD | 0.00 USD | 285.82 USD | `-58.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 2,170,000.00 USD | 0.00 USD | 306.60 USD | `-58.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 2,170,000.00 USD | 0.00 USD | 121.55 USD | `-55.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 2,170,000.00 USD | 0.00 USD | 656.53 USD | `-54.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 2,170,000.00 USD | 0.00 USD | 100.62 USD | `-53.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 2,170,000.00 USD | 0.00 USD | 203.75 USD | `-50.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 2,170,000.00 USD | 0.00 USD | 791.85 USD | `-49.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 2,170,000.00 USD | 0.00 USD | 573.40 USD | `-48.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 2,170,000.00 USD | 0.00 USD | 244.31 USD | `-47.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 2,170,000.00 USD | 0.00 USD | 29,530.00 USD | `-46.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 2,140,000.00 USD | 0.00 USD | 503.55 USD | `-46.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 2,140,000.00 USD | 0.00 USD | 480.19 USD | `-45.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 2,140,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 2,130,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 2,120,000.00 USD | 0.00 USD | 228.80 USD | `-42.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 2,120,000.00 USD | 0.00 USD | 536.50 USD | `-42.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 2,120,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 2,120,000.00 USD | 0.00 USD | 2,880.00 USD | `-38.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 2,120,000.00 USD | 0.00 USD | 878.48 USD | `-36.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 2,120,000.00 USD | 0.00 USD | 6,020.00 USD | `-34.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 2,110,000.00 USD | 0.00 USD | 1,360.00 USD | `-31.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 2,110,000.00 USD | 0.00 USD | 690.38 USD | `-30.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 2,110,000.00 USD | 0.00 USD | 1,210.00 USD | `-29.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 2,110,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 2,110,000.00 USD | 0.00 USD | 838.94 USD | `-27.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 2,110,000.00 USD | 0.00 USD | 338.55 USD | `-27.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 2,110,000.00 USD | 0.00 USD | 1,060.00 USD | `-26.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 2,100,000.00 USD | 0.00 USD | 1,090.00 USD | `-25.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 2,100,000.00 USD | 0.00 USD | 112.46 USD | `-24.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 2,100,000.00 USD | 0.00 USD | 1,730.00 USD | `-23.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 2,100,000.00 USD | 0.00 USD | 4,010.00 USD | `-23.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 2,100,000.00 USD | 0.00 USD | 6,200.00 USD | `-22.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 2,090,000.00 USD | 0.00 USD | 4,890.00 USD | `-21.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 2,090,000.00 USD | 0.00 USD | 902.47 USD | `-20.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 2,090,000.00 USD | 0.00 USD | 15,420.00 USD | `-19.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 2,070,000.00 USD | 0.00 USD | 6,640.00 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 2,060,000.00 USD | 0.00 USD | 1,840.00 USD | `-18.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 2,060,000.00 USD | 0.00 USD | 42,670.00 USD | `-17.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 2,020,000.00 USD | 0.00 USD | 1,780.00 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 2,020,000.00 USD | 0.00 USD | 24,230.00 USD | `-15.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,990,000.00 USD | 0.00 USD | 4,570.00 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,990,000.00 USD | 0.00 USD | 48,460.00 USD | `-14.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,940,000.00 USD | 0.00 USD | 3,690.00 USD | `-13.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,940,000.00 USD | 0.00 USD | 279,970.00 USD | `-12.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 1,660,000.00 USD | 0.00 USD | 21,590.00 USD | `-11.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 1,630,000.00 USD | 0.00 USD | 9,410.00 USD | `-11.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 1,630,000.00 USD | 0.00 USD | 101,980.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 1,520,000.00 USD | 0.00 USD | 13,490.00 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 1,510,000.00 USD | 0.00 USD | 120,050.00 USD | `-8.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 1,390,000.00 USD | 0.00 USD | 40,320.00 USD | `-7.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 1,350,000.00 USD | 0.00 USD | 42,080.00 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 1,310,000.00 USD | 0.00 USD | 94,830.00 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 1,210,000.00 USD | 0.00 USD | 221,020.00 USD | `-5.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 991,250.00 USD | 0.00 USD | 409,570.00 USD | `-4.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 581,680.00 USD | 0.00 USD | 93,540.00 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 488,140.00 USD | 0.00 USD | 289,680.00 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 198,450.00 USD | 0.00 USD | 22,330.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 176,120.00 USD | 0.00 USD | 86,220.00 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 89,900.00 USD | 0.00 USD | 89,900.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 74,830.00 USD | 74,830.00 USD | 0.00 USD | `+0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 378,850.00 USD | 304,020.00 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 397,010.00 USD | 18,160.00 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 647,790.00 USD | 250,780.00 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 702,030.00 USD | 54,240.00 USD | 0.00 USD | `+3.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 944,760.00 USD | 242,720.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 1,590,000.00 USD | 649,810.00 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,810,000.00 USD | 214,110.00 USD | 0.00 USD | `+5.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,860,000.00 USD | 47,230.00 USD | 0.00 USD | `+6.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,970,000.00 USD | 112,700.00 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,980,000.00 USD | 14,640.00 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 2,230,000.00 USD | 249,240.00 USD | 0.00 USD | `+8.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 2,310,000.00 USD | 81,760.00 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 2,370,000.00 USD | 53,860.00 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 2,370,000.00 USD | 3,960.00 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 6,220,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+12.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 6,220,000.00 USD | 3,710.00 USD | 0.00 USD | `+12.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 6,230,000.00 USD | 5,990.00 USD | 0.00 USD | `+13.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,300,000.00 USD | 78,630.00 USD | 0.00 USD | `+14.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,550,000.00 USD | 242,580.00 USD | 0.00 USD | `+15.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,550,000.00 USD | 7,510.00 USD | 0.00 USD | `+16.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,580,000.00 USD | 23,260.00 USD | 0.00 USD | `+16.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,690,000.00 USD | 108,020.00 USD | 0.00 USD | `+17.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,700,000.00 USD | 14,970.00 USD | 0.00 USD | `+18.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,720,000.00 USD | 15,800.00 USD | 0.00 USD | `+19.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,770,000.00 USD | 57,590.00 USD | 0.00 USD | `+20.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,790,000.00 USD | 11,760.00 USD | 0.00 USD | `+20.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,810,000.00 USD | 19,430.00 USD | 0.00 USD | `+21.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,850,000.00 USD | 45,620.00 USD | 0.00 USD | `+22.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,860,000.00 USD | 10,870.00 USD | 0.00 USD | `+23.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,860,000.00 USD | 2,380.00 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,870,000.00 USD | 6,450.00 USD | 0.00 USD | `+24.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,880,000.00 USD | 5,570.00 USD | 0.00 USD | `+25.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,890,000.00 USD | 10,250.00 USD | 0.00 USD | `+26.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 7,000,000.00 USD | 113,910.00 USD | 0.00 USD | `+27.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 7,040,000.00 USD | 40,290.00 USD | 0.00 USD | `+28.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 7,120,000.00 USD | 80,330.00 USD | 0.00 USD | `+28.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 7,120,000.00 USD | 464.75 USD | 0.00 USD | `+29.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,300,000.00 USD | 179,860.00 USD | 0.00 USD | `+30.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,300,000.00 USD | 2,670.00 USD | 0.00 USD | `+31.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,390,000.00 USD | 85,010.00 USD | 0.00 USD | `+32.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,400,000.00 USD | 6,080.00 USD | 0.00 USD | `+32.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,410,000.00 USD | 18,400.00 USD | 0.00 USD | `+33.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,480,000.00 USD | 70,850.00 USD | 0.00 USD | `+34.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,500,000.00 USD | 18,000.00 USD | 0.00 USD | `+35.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,720,000.00 USD | 217,560.00 USD | 0.00 USD | `+36.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,730,000.00 USD | 14,250.00 USD | 0.00 USD | `+36.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,740,000.00 USD | 3,980.00 USD | 0.00 USD | `+37.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,780,000.00 USD | 43,240.00 USD | 0.00 USD | `+38.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,780,000.00 USD | 3,330.00 USD | 0.00 USD | `+39.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,790,000.00 USD | 9,200.00 USD | 0.00 USD | `+40.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,820,000.00 USD | 21,720.00 USD | 0.00 USD | `+40.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,940,000.00 USD | 128,330.00 USD | 0.00 USD | `+41.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 8,040,000.00 USD | 96,600.00 USD | 0.00 USD | `+42.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 8,040,000.00 USD | 3,980.00 USD | 0.00 USD | `+43.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 8,040,000.00 USD | 254.51 USD | 0.00 USD | `+44.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 8,060,000.00 USD | 12,860.00 USD | 0.00 USD | `+44.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 8,060,000.00 USD | 3,970.00 USD | 0.00 USD | `+45.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 8,070,000.00 USD | 8,170.00 USD | 0.00 USD | `+46.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 8,070,000.00 USD | 843.17 USD | 0.00 USD | `+47.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 8,080,000.00 USD | 8,390.00 USD | 0.00 USD | `+48.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 8,080,000.00 USD | 4,420.00 USD | 0.00 USD | `+49.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 8,080,000.00 USD | 591.89 USD | 0.00 USD | `+50.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 8,130,000.00 USD | 46,370.00 USD | 0.00 USD | `+51.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 8,140,000.00 USD | 9,270.00 USD | 0.00 USD | `+51.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 8,140,000.00 USD | 265.10 USD | 0.00 USD | `+54.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 8,140,000.00 USD | 2,040.00 USD | 0.00 USD | `+55.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 8,140,000.00 USD | 807.42 USD | 0.00 USD | `+55.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,160,000.00 USD | 14,120.00 USD | 0.00 USD | `+56.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,160,000.00 USD | 4,010.00 USD | 0.00 USD | `+57.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,160,000.00 USD | 325.54 USD | 0.00 USD | `+58.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,170,000.00 USD | 7,020.00 USD | 0.00 USD | `+59.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,290,000.00 USD | 123,020.00 USD | 0.00 USD | `+59.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,290,000.00 USD | 3,350.00 USD | 0.00 USD | `+61.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,290,000.00 USD | 181.12 USD | 0.00 USD | `+62.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,300,000.00 USD | 382.41 USD | 0.00 USD | `+63.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,300,000.00 USD | 3,420.00 USD | 0.00 USD | `+64.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,300,000.00 USD | 661.93 USD | 0.00 USD | `+65.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,420,000.00 USD | 124,400.00 USD | 0.00 USD | `+67.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,430,000.00 USD | 1,580.00 USD | 0.00 USD | `+67.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,440,000.00 USD | 13,900.00 USD | 0.00 USD | `+69.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,460,000.00 USD | 24,840.00 USD | 0.00 USD | `+71.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,510,000.00 USD | 50,580.00 USD | 0.00 USD | `+71.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,520,000.00 USD | 2,690.00 USD | 0.00 USD | `+72.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,520,000.00 USD | 2,180.00 USD | 0.00 USD | `+75.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,670,000.00 USD | 151,380.00 USD | 0.00 USD | `+76.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,670,000.00 USD | 3,120.00 USD | 0.00 USD | `+81.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,680,000.00 USD | 1,140.00 USD | 0.00 USD | `+82.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,690,000.00 USD | 11,670.00 USD | 0.00 USD | `+83.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,690,000.00 USD | 370.40 USD | 0.00 USD | `+84.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,690,000.00 USD | 733.19 USD | 0.00 USD | `+86.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,690,000.00 USD | 2,410.00 USD | 0.00 USD | `+88.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,690,000.00 USD | 475.00 USD | 0.00 USD | `+89.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,690,000.00 USD | 1,190.00 USD | 0.00 USD | `+90.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,690,000.00 USD | 2,540.00 USD | 0.00 USD | `+91.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,700,000.00 USD | 1,590.00 USD | 0.00 USD | `+91.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,700,000.00 USD | 1,370.00 USD | 0.00 USD | `+92.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,720,000.00 USD | 19,590.00 USD | 0.00 USD | `+93.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,720,000.00 USD | 564.92 USD | 0.00 USD | `+94.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,730,000.00 USD | 8,110.00 USD | 0.00 USD | `+95.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,730,000.00 USD | 3,420.00 USD | 0.00 USD | `+98.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,730,000.00 USD | 124.75 USD | 0.00 USD | `+99.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,760,000.00 USD | 29,920.00 USD | 0.00 USD | `+99.86%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.07` | 83,780,000.00 USD | 0.00 USD | 83,780,000.00 USD | 0.00 USD | 0.00 USD | 39,860.00 USD |
| `7D` | `1.08` | 83,740,000.00 USD | 0.00 USD | 83,740,000.00 USD | 0.00 USD | 2,940.00 USD | 0.00 USD |
| `7D` | `1.09` | 83,730,000.00 USD | 0.00 USD | 83,730,000.00 USD | 37,460.00 USD | 100,340.00 USD | 0.00 USD |
| `7D` | `1.09` | 83,600,000.00 USD | 0.00 USD | 83,600,000.00 USD | 0.00 USD | 4,450.00 USD | 0.00 USD |
| `7D` | `1.09` | 83,590,000.00 USD | 0.00 USD | 83,590,000.00 USD | 0.00 USD | 2,020.00 USD | 32,940.00 USD |
| `7D` | `1.10` | 83,560,000.00 USD | 0.00 USD | 83,560,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD |
| `7D` | `1.10` | 83,550,000.00 USD | 0.00 USD | 83,550,000.00 USD | 0.00 USD | 0.00 USD | 140,160.00 USD |
| `7D` | `1.10` | 83,410,000.00 USD | 0.00 USD | 83,410,000.00 USD | 0.00 USD | 0.00 USD | 147,140.00 USD |
| `7D` | `1.10` | 83,270,000.00 USD | 0.00 USD | 83,270,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD |
| `7D` | `1.11` | 83,260,000.00 USD | 0.00 USD | 83,260,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD |
| `7D` | `1.11` | 83,260,000.00 USD | 0.00 USD | 83,260,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `7D` | `1.11` | 83,260,000.00 USD | 0.00 USD | 83,260,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.11` | 83,240,000.00 USD | 0.00 USD | 83,240,000.00 USD | 28,830.00 USD | 4,710.00 USD | 0.00 USD |
| `7D` | `1.11` | 83,200,000.00 USD | 0.00 USD | 83,200,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `1D` | `1.12` | 75,920,000.00 USD | 0.00 USD | 75,920,000.00 USD | 0.00 USD | 16,040.00 USD | 112,550.00 USD |
| `7D` | `1.12` | 83,190,000.00 USD | 0.00 USD | 83,190,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 75,790,000.00 USD | 0.00 USD | 75,790,000.00 USD | 7,460.00 USD | 48,180.00 USD | 41,970.00 USD |
| `1D` | `1.12` | 75,690,000.00 USD | 0.00 USD | 75,690,000.00 USD | 16,420.00 USD | 60,880.00 USD | 88,470.00 USD |
| `7D` | `1.12` | 83,110,000.00 USD | 0.00 USD | 83,110,000.00 USD | 17,190.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `1.12` | 75,530,000.00 USD | 0.00 USD | 75,530,000.00 USD | 5,470.00 USD | 1,530.00 USD | 84,110.00 USD |
| `7D` | `1.12` | 83,090,000.00 USD | 0.00 USD | 83,090,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD |
| `1D` | `1.12` | 75,440,000.00 USD | 0.00 USD | 75,440,000.00 USD | 79,690.00 USD | 29,190.00 USD | 63,290.00 USD |
| `7D` | `1.12` | 83,090,000.00 USD | 0.00 USD | 83,090,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.13` | 75,260,000.00 USD | 0.00 USD | 75,260,000.00 USD | 12,370.00 USD | 1,260.00 USD | 105,870.00 USD |
| `1D` | `1.13` | 75,140,000.00 USD | 0.00 USD | 75,140,000.00 USD | 69,610.00 USD | 60,790.00 USD | 142,490.00 USD |
| `7D` | `1.13` | 82,880,000.00 USD | 0.00 USD | 82,880,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 74,870,000.00 USD | 0.00 USD | 74,870,000.00 USD | 0.00 USD | 66,770.00 USD | 168,450.00 USD |
| `7D` | `1.13` | 82,680,000.00 USD | 0.00 USD | 82,680,000.00 USD | 5,450.00 USD | 3,410.00 USD | 3,970.00 USD |
| `1D` | `1.13` | 74,640,000.00 USD | 0.00 USD | 74,640,000.00 USD | 63,980.00 USD | 37,600.00 USD | 5,920.00 USD |
| `7D` | `1.13` | 82,670,000.00 USD | 0.00 USD | 82,670,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD |
| `1D` | `1.14` | 74,530,000.00 USD | 0.00 USD | 74,530,000.00 USD | 0.00 USD | 122,160.00 USD | 66,680.00 USD |
| `7D` | `1.14` | 82,190,000.00 USD | 0.00 USD | 82,190,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD |
| `1D` | `1.14` | 74,340,000.00 USD | 0.00 USD | 74,340,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD |
| `7D` | `1.14` | 81,950,000.00 USD | 0.00 USD | 81,950,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 74,250,000.00 USD | 0.00 USD | 74,250,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.14` | 81,850,000.00 USD | 0.00 USD | 81,850,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 74,220,000.00 USD | 0.00 USD | 74,220,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD |
| `7D` | `1.14` | 81,840,000.00 USD | 0.00 USD | 81,840,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 74,160,000.00 USD | 0.00 USD | 74,160,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD |
| `7D` | `1.14` | 81,780,000.00 USD | 0.00 USD | 81,780,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.15` | 74,020,000.00 USD | 0.00 USD | 74,020,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD |
| `7D` | `1.15` | 81,660,000.00 USD | 0.00 USD | 81,660,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.15` | 81,650,000.00 USD | 0.00 USD | 81,650,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `1D` | `1.15` | 73,980,000.00 USD | 0.00 USD | 73,980,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 81,510,000.00 USD | 0.00 USD | 81,510,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD |
| `7D` | `1.15` | 81,150,000.00 USD | 0.00 USD | 81,150,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.15` | 73,960,000.00 USD | 0.00 USD | 73,960,000.00 USD | 4,040.00 USD | 14,590.00 USD | 185,060.00 USD |
| `7D` | `1.15` | 80,990,000.00 USD | 0.00 USD | 80,990,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `1D` | `1.16` | 73,760,000.00 USD | 0.00 USD | 73,760,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD |
| `7D` | `1.16` | 80,610,000.00 USD | 0.00 USD | 80,610,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `1D` | `1.16` | 73,420,000.00 USD | 0.00 USD | 73,420,000.00 USD | 72,570.00 USD | 16,310.00 USD | 30,470.00 USD |
| `7D` | `1.16` | 79,960,000.00 USD | 0.00 USD | 79,960,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD |
| `1D` | `1.16` | 73,300,000.00 USD | 0.00 USD | 73,300,000.00 USD | 126,860.00 USD | 16,130.00 USD | 446,310.00 USD |
| `7D` | `1.16` | 79,160,000.00 USD | 0.00 USD | 79,160,000.00 USD | 265,410.00 USD | 70,050.00 USD | 301,800.00 USD |
| `1D` | `1.16` | 72,710,000.00 USD | 0.00 USD | 72,710,000.00 USD | 253,200.00 USD | 126,280.00 USD | 170,950.00 USD |
| `7D` | `1.16` | 78,520,000.00 USD | 0.00 USD | 78,520,000.00 USD | 352,520.00 USD | 494,920.00 USD | 654,650.00 USD |
| `1D` | `1.16` | 72,160,000.00 USD | 0.00 USD | 72,160,000.00 USD | 253,180.00 USD | 314,800.00 USD | 334,700.00 USD |
| `7D` | `1.16` | 77,020,000.00 USD | 0.00 USD | 77,020,000.00 USD | 485,880.00 USD | 177,220.00 USD | 811,990.00 USD |
| `1D` | `1.17` | 71,260,000.00 USD | 0.00 USD | 71,260,000.00 USD | 95,890.00 USD | 51,030.00 USD | 486,240.00 USD |
| `7D` | `1.17` | 75,550,000.00 USD | 0.00 USD | 75,550,000.00 USD | 209,000.00 USD | 168,650.00 USD | 491,860.00 USD |
| `1D` | `1.17` | 70,630,000.00 USD | 0.00 USD | 70,630,000.00 USD | 146,120.00 USD | 120,500.00 USD | 131,100.00 USD |
| `7D` | `1.17` | 74,680,000.00 USD | 0.00 USD | 74,680,000.00 USD | 454,610.00 USD | 248,780.00 USD | 1,060,000.00 USD |
| `1D` | `1.17` | 70,230,000.00 USD | 0.00 USD | 70,230,000.00 USD | 111,200.00 USD | 95,250.00 USD | 206,520.00 USD |
| `7D` | `1.17` | 72,910,000.00 USD | 0.00 USD | 72,910,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 69,810,000.00 USD | 0.00 USD | 69,810,000.00 USD | 361,890.00 USD | 3,910.00 USD | 415,800.00 USD |
| `7D` | `1.17` | 71,410,000.00 USD | 0.00 USD | 71,410,000.00 USD | 502,470.00 USD | 180,770.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 69,030,000.00 USD | 0.00 USD | 69,030,000.00 USD | 104,550.00 USD | 79,710.00 USD | 360,510.00 USD |
| `7D` | `1.17` | 70,010,000.00 USD | 0.00 USD | 70,010,000.00 USD | 290,530.00 USD | 139,010.00 USD | 1,170,000.00 USD |
| `1D` | `1.18` | 68,490,000.00 USD | 0.00 USD | 68,490,000.00 USD | 396,370.00 USD | 140,700.00 USD | 416,380.00 USD |
| `7D` | `1.18` | 68,410,000.00 USD | 0.00 USD | 68,410,000.00 USD | 520,770.00 USD | 90,550.00 USD | 499,970.00 USD |
| `1D` | `1.18` | 67,540,000.00 USD | 0.00 USD | 67,540,000.00 USD | 71,610.00 USD | 44,040.00 USD | 250,850.00 USD |
| `7D` | `1.18` | 67,300,000.00 USD | 0.00 USD | 67,300,000.00 USD | 154,760.00 USD | 59,570.00 USD | 473,440.00 USD |
| `1D` | `1.18` | 67,170,000.00 USD | 0.00 USD | 67,170,000.00 USD | 90,040.00 USD | 42,260.00 USD | 198,520.00 USD |
| `7D` | `1.18` | 66,610,000.00 USD | 0.00 USD | 66,610,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `1D` | `1.18` | 66,840,000.00 USD | 0.00 USD | 66,840,000.00 USD | 144,240.00 USD | 19,410.00 USD | 6,800.00 USD |
| `7D` | `1.18` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 69,670.00 USD | 117,700.00 USD | 197,340.00 USD |
| `1D` | `1.18` | 66,670,000.00 USD | 0.00 USD | 66,670,000.00 USD | 150,010.00 USD | 19,860.00 USD | 660,810.00 USD |
| `7D` | `1.18` | 65,510,000.00 USD | 0.00 USD | 65,510,000.00 USD | 254,520.00 USD | 92,820.00 USD | 8,750.00 USD |
| `1D` | `1.19` | 65,840,000.00 USD | 0.00 USD | 65,840,000.00 USD | 225,800.00 USD | 63,560.00 USD | 143,880.00 USD |
| `7D` | `1.19` | 65,160,000.00 USD | 0.00 USD | 65,160,000.00 USD | 123,240.00 USD | 581,580.00 USD | 764,370.00 USD |
| `1D` | `1.19` | 65,400,000.00 USD | 0.00 USD | 65,400,000.00 USD | 109,160.00 USD | 518,680.00 USD | 653,320.00 USD |
| `7D` | `1.19` | 63,690,000.00 USD | 0.00 USD | 63,690,000.00 USD | 229,250.00 USD | 60,320.00 USD | 621,570.00 USD |
| `1D` | `1.19` | 64,120,000.00 USD | 0.00 USD | 64,120,000.00 USD | 360,560.00 USD | 90,130.00 USD | 1,290,000.00 USD |
| `7D` | `1.19` | 62,780,000.00 USD | 0.00 USD | 62,780,000.00 USD | 182,110.00 USD | 138,450.00 USD | 757,050.00 USD |
| `1D` | `1.19` | 62,380,000.00 USD | 0.00 USD | 62,380,000.00 USD | 61,250.00 USD | 47,660.00 USD | 373,810.00 USD |
| `7D` | `1.19` | 61,700,000.00 USD | 0.00 USD | 61,700,000.00 USD | 140,460.00 USD | 503,850.00 USD | 906,740.00 USD |
| `1D` | `1.19` | 61,900,000.00 USD | 0.00 USD | 61,900,000.00 USD | 157,580.00 USD | 502,360.00 USD | 448,490.00 USD |
| `7D` | `1.19` | 60,150,000.00 USD | 0.00 USD | 60,150,000.00 USD | 147,020.00 USD | 91,800.00 USD | 467,490.00 USD |
| `1D` | `1.20` | 60,790,000.00 USD | 0.00 USD | 60,790,000.00 USD | 381,040.00 USD | 157,690.00 USD | 2,040,000.00 USD |
| `7D` | `1.20` | 59,440,000.00 USD | 0.00 USD | 59,440,000.00 USD | 348,260.00 USD | 72,600.00 USD | 247,820.00 USD |
| `1D` | `1.20` | 58,210,000.00 USD | 0.00 USD | 58,210,000.00 USD | 748,570.00 USD | 84,750.00 USD | 788,910.00 USD |
| `7D` | `1.20` | 58,770,000.00 USD | 0.00 USD | 58,770,000.00 USD | 5,350.00 USD | 1,100,000.00 USD | 1,800,000.00 USD |
| `1D` | `1.20` | 56,590,000.00 USD | 0.00 USD | 56,590,000.00 USD | 112,900.00 USD | 934,870.00 USD | 1,510,000.00 USD |
| `7D` | `1.20` | 55,870,000.00 USD | 0.00 USD | 55,870,000.00 USD | 553,590.00 USD | 399,490.00 USD | 949,600.00 USD |
| `1D` | `1.20` | 54,030,000.00 USD | 0.00 USD | 54,030,000.00 USD | 730,270.00 USD | 464,920.00 USD | 1,630,000.00 USD |
| `7D` | `1.20` | 53,960,000.00 USD | 0.00 USD | 53,960,000.00 USD | 293,850.00 USD | 223,240.00 USD | 470,230.00 USD |
| `1D` | `1.20` | 51,200,000.00 USD | 0.00 USD | 51,200,000.00 USD | 314,820.00 USD | 47,550.00 USD | 740,300.00 USD |
| `7D` | `1.20` | 52,980,000.00 USD | 0.00 USD | 52,980,000.00 USD | 226,160.00 USD | 696,800.00 USD | 0.00 USD |
| `1D` | `1.21` | 50,100,000.00 USD | 0.00 USD | 50,100,000.00 USD | 295,960.00 USD | 920,650.00 USD | 246,560.00 USD |
| `7D` | `1.21` | 52,050,000.00 USD | 0.00 USD | 52,050,000.00 USD | 0.00 USD | 37,150.00 USD | 5,570.00 USD |
| `1D` | `1.21` | 48,640,000.00 USD | 0.00 USD | 48,640,000.00 USD | 825,290.00 USD | 104,970.00 USD | 1,330,000.00 USD |
| `7D` | `1.21` | 52,010,000.00 USD | 0.00 USD | 52,010,000.00 USD | 66,830.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.21` | 46,380,000.00 USD | 0.00 USD | 46,380,000.00 USD | 1,590,000.00 USD | 227,220.00 USD | 824,260.00 USD |
| `7D` | `1.21` | 51,940,000.00 USD | 0.00 USD | 51,940,000.00 USD | 576,740.00 USD | 84,270.00 USD | 1,620,000.00 USD |
| `1D` | `1.21` | 43,740,000.00 USD | 0.00 USD | 43,740,000.00 USD | 160,630.00 USD | 650,810.00 USD | 1,640,000.00 USD |
| `7D` | `1.21` | 49,670,000.00 USD | 0.00 USD | 49,670,000.00 USD | 1,100,000.00 USD | 408,100.00 USD | 1,470,000.00 USD |
| `1D` | `1.21` | 41,290,000.00 USD | 0.00 USD | 41,290,000.00 USD | 1,350,000.00 USD | 271,760.00 USD | 998,520.00 USD |
| `7D` | `1.21` | 46,690,000.00 USD | 0.00 USD | 46,690,000.00 USD | 302,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.22` | 38,670,000.00 USD | 0.00 USD | 38,670,000.00 USD | 52,290.00 USD | 154,650.00 USD | 685,980.00 USD |
| `7D` | `1.22` | 46,380,000.00 USD | 0.00 USD | 46,380,000.00 USD | 49,970.00 USD | 0.00 USD | 910,410.00 USD |
| `1D` | `1.22` | 37,780,000.00 USD | 0.00 USD | 37,780,000.00 USD | 307,460.00 USD | 26,150.00 USD | 176,390.00 USD |
| `7D` | `1.22` | 45,420,000.00 USD | 0.00 USD | 45,420,000.00 USD | 157,620.00 USD | 9,150.00 USD | 0.00 USD |
| `1D` | `1.22` | 37,270,000.00 USD | 0.00 USD | 37,270,000.00 USD | 203,470.00 USD | 49,690.00 USD | 10,770.00 USD |
| `7D` | `1.22` | 45,260,000.00 USD | 0.00 USD | 45,260,000.00 USD | 308,930.00 USD | 0.00 USD | 432,150.00 USD |
| `1D` | `1.22` | 37,000,000.00 USD | 0.00 USD | 37,000,000.00 USD | 64,370.00 USD | 321,780.00 USD | 300,620.00 USD |
| `7D` | `1.22` | 44,520,000.00 USD | 0.00 USD | 44,520,000.00 USD | 85,970.00 USD | 928,300.00 USD | 14,710.00 USD |
| `1D` | `1.22` | 36,320,000.00 USD | 0.00 USD | 36,320,000.00 USD | 106,100.00 USD | 0.00 USD | 348,120.00 USD |
| `7D` | `1.22` | 43,490,000.00 USD | 0.00 USD | 43,490,000.00 USD | 51,610.00 USD | 330,390.00 USD | 31,650.00 USD |
| `1D` | `1.23` | 35,860,000.00 USD | 0.00 USD | 35,860,000.00 USD | 270,600.00 USD | 510,520.00 USD | 2,640,000.00 USD |
| `7D` | `1.23` | 43,070,000.00 USD | 0.00 USD | 43,070,000.00 USD | 0.00 USD | 476,630.00 USD | 4,910.00 USD |
| `1D` | `1.23` | 32,440,000.00 USD | 0.00 USD | 32,440,000.00 USD | 107,280.00 USD | 64,900.00 USD | 86,210.00 USD |
| `7D` | `1.23` | 42,590,000.00 USD | 0.00 USD | 42,590,000.00 USD | 171,930.00 USD | 761,700.00 USD | 16,600.00 USD |
| `1D` | `1.23` | 32,180,000.00 USD | 0.00 USD | 32,180,000.00 USD | 556,720.00 USD | 1,090,000.00 USD | 2,450,000.00 USD |
| `7D` | `1.23` | 41,640,000.00 USD | 0.00 USD | 41,640,000.00 USD | 0.00 USD | 1,080,000.00 USD | 817,960.00 USD |
| `1D` | `1.23` | 28,080,000.00 USD | 0.00 USD | 28,080,000.00 USD | 66,520.00 USD | 1,250,000.00 USD | 2,350,000.00 USD |
| `7D` | `1.23` | 39,740,000.00 USD | 0.00 USD | 39,740,000.00 USD | 969,900.00 USD | 495,660.00 USD | 791,070.00 USD |
| `1D` | `1.23` | 24,410,000.00 USD | 0.00 USD | 24,410,000.00 USD | 1,480,000.00 USD | 505,910.00 USD | 2,220,000.00 USD |
| `7D` | `1.23` | 37,490,000.00 USD | 0.00 USD | 37,490,000.00 USD | 1,090,000.00 USD | 1,080,000.00 USD | 1,990,000.00 USD |
| `1D` | `1.24` | 20,210,000.00 USD | 0.00 USD | 20,210,000.00 USD | 241,040.00 USD | 1,490,000.00 USD | 1,770,000.00 USD |
| `7D` | `1.24` | 33,330,000.00 USD | 0.00 USD | 33,330,000.00 USD | 1,920,000.00 USD | 2,020,000.00 USD | 2,130,000.00 USD |
| `1D` | `1.24` | 16,710,000.00 USD | 0.00 USD | 16,710,000.00 USD | 18,660.00 USD | 428,450.00 USD | 134,110.00 USD |
| `7D` | `1.24` | 27,260,000.00 USD | 0.00 USD | 27,260,000.00 USD | 1,640,000.00 USD | 1,830,000.00 USD | 3,300,000.00 USD |
| `1D` | `1.24` | 16,130,000.00 USD | 0.00 USD | 16,130,000.00 USD | 15,170.00 USD | 220,870.00 USD | 931,900.00 USD |
| `7D` | `1.24` | 20,490,000.00 USD | 0.00 USD | 20,490,000.00 USD | 2,610,000.00 USD | 1,380,000.00 USD | 1,450,000.00 USD |
| `1D` | `1.24` | 14,960,000.00 USD | 0.00 USD | 14,960,000.00 USD | 734,030.00 USD | 182,970.00 USD | 651,390.00 USD |
| `7D` | `1.24` | 15,060,000.00 USD | 0.00 USD | 15,060,000.00 USD | 1,820,000.00 USD | 374,420.00 USD | 0.00 USD |
| `1D` | `1.24` | 13,390,000.00 USD | 0.00 USD | 13,390,000.00 USD | 658,110.00 USD | 818,040.00 USD | 994,950.00 USD |
| `7D` | `1.24` | 12,860,000.00 USD | 0.00 USD | 12,860,000.00 USD | 896,470.00 USD | 15,000.00 USD | 0.00 USD |
| `1D` | `1.25` | 10,920,000.00 USD | 0.00 USD | 10,920,000.00 USD | 1,640,000.00 USD | 134,980.00 USD | 379,170.00 USD |
| `7D` | `1.25` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 3,330,000.00 USD | 0.00 USD | 700,780.00 USD |
| `1D` | `1.25` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 700,330.00 USD | 712,880.00 USD | 997,240.00 USD |
| `7D` | `1.25` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 2,700,000.00 USD | 662,610.00 USD | 1,590,000.00 USD |
| `1D` | `1.25` | 6,350,000.00 USD | 0.00 USD | 6,350,000.00 USD | 331,570.00 USD | 602,270.00 USD | 356,590.00 USD |
| `1D` | `1.25` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 202,510.00 USD | 1,390.00 USD | 993,050.00 USD |
| `7D` | `1.25` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 0.00 USD | 9,140.00 USD | 455,200.00 USD |
| `1D` | `1.25` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 17,600.00 USD | 8,750.00 USD | 4,230.00 USD |
| `7D` | `1.25` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 860,180.00 USD |
| `1D` | `1.25` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 633,250.00 USD | 12,640.00 USD | 681,030.00 USD |
| `7D` | `1.25` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 213,660.00 USD | 39,910.00 USD | 801,800.00 USD |
| `1D` | `1.26` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 936,860.00 USD | 443,180.00 USD | 551,970.00 USD |
| `7D` | `1.26` | 593,100.00 USD | 0.00 USD | 593,100.00 USD | 0.00 USD | 249,600.00 USD | 239,910.00 USD |
| `1D` | `1.26` | 575,170.00 USD | 0.00 USD | 575,170.00 USD | 192,760.00 USD | 38,980.00 USD | 11,190.00 USD |
| `7D` | `1.26` | 103,580.00 USD | 0.00 USD | 103,580.00 USD | 0.00 USD | 21,230.00 USD | 82,350.00 USD |
| `1D` | `1.26` | 332,220.00 USD | 0.00 USD | 332,220.00 USD | 264,250.00 USD | 22,310.00 USD | 45,660.00 USD |
| `7D` | `1.26` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 144,170.00 USD | 23,560.00 USD | 2,580,000.00 USD |
| `7D` | `1.26` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 144,170.00 USD | 23,560.00 USD | 2,580,000.00 USD |
| `1D` | `1.26` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 1,250,000.00 USD | 819,120.00 USD | 1,770,000.00 USD |
| `7D` | `1.26` | 9,290,000.00 USD | 9,290,000.00 USD | 0.00 USD | 834,020.00 USD | 803,260.00 USD | 2,150,000.00 USD |
| `1D` | `1.26` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 479,740.00 USD | 980,510.00 USD | 2,160,000.00 USD |
| `7D` | `1.26` | 16,950,000.00 USD | 16,950,000.00 USD | 0.00 USD | 1,640,000.00 USD | 1,350,000.00 USD | 4,670,000.00 USD |
| `1D` | `1.27` | 11,770,000.00 USD | 11,770,000.00 USD | 0.00 USD | 745,260.00 USD | 1,270,000.00 USD | 2,300,000.00 USD |
| `7D` | `1.27` | 30,590,000.00 USD | 30,590,000.00 USD | 0.00 USD | 2,620,000.00 USD | 2,380,000.00 USD | 8,640,000.00 USD |
| `1D` | `1.27` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 466,250.00 USD | 2,030,000.00 USD | 697,890.00 USD |
| `7D` | `1.27` | 35,820,000.00 USD | 35,820,000.00 USD | 0.00 USD | 52,540.00 USD | 2,640,000.00 USD | 2,530,000.00 USD |
| `1D` | `1.27` | 18,960,000.00 USD | 18,960,000.00 USD | 0.00 USD | 647,480.00 USD | 1,080,000.00 USD | 2,260,000.00 USD |
| `7D` | `1.27` | 40,210,000.00 USD | 40,210,000.00 USD | 0.00 USD | 1,010,000.00 USD | 2,540,000.00 USD | 842,170.00 USD |
| `1D` | `1.27` | 23,790,000.00 USD | 23,790,000.00 USD | 0.00 USD | 1,840,000.00 USD | 1,040,000.00 USD | 1,960,000.00 USD |
| `7D` | `1.27` | 47,040,000.00 USD | 47,040,000.00 USD | 0.00 USD | 468,870.00 USD | 4,920,000.00 USD | 1,450,000.00 USD |
| `1D` | `1.27` | 29,810,000.00 USD | 29,810,000.00 USD | 0.00 USD | 814,880.00 USD | 2,270,000.00 USD | 2,940,000.00 USD |
| `7D` | `1.27` | 63,710,000.00 USD | 63,710,000.00 USD | 0.00 USD | 4,840,000.00 USD | 2,350,000.00 USD | 9,480,000.00 USD |
| `1D` | `1.28` | 36,800,000.00 USD | 36,800,000.00 USD | 0.00 USD | 1,940,000.00 USD | 1,760,000.00 USD | 3,290,000.00 USD |
| `7D` | `1.28` | 82,330,000.00 USD | 82,330,000.00 USD | 0.00 USD | 6,930,000.00 USD | 3,330,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 44,620,000.00 USD | 44,620,000.00 USD | 0.00 USD | 3,090,000.00 USD | 2,110,000.00 USD | 2,620,000.00 USD |
| `7D` | `1.28` | 88,630,000.00 USD | 88,630,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,950,000.00 USD | 1,090,000.00 USD |
| `1D` | `1.28` | 46,030,000.00 USD | 46,030,000.00 USD | 0.00 USD | 257,680.00 USD | 558,100.00 USD | 586,370.00 USD |
| `7D` | `1.28` | 89,590,000.00 USD | 89,590,000.00 USD | 0.00 USD | 0.00 USD | 883,970.00 USD | 79,220.00 USD |
| `1D` | `1.28` | 49,140,000.00 USD | 49,140,000.00 USD | 0.00 USD | 1,260,000.00 USD | 301,200.00 USD | 1,560,000.00 USD |
| `7D` | `1.28` | 91,650,000.00 USD | 91,650,000.00 USD | 0.00 USD | 1,510,000.00 USD | 480,590.00 USD | 67,480.00 USD |
| `1D` | `1.28` | 52,000,000.00 USD | 52,000,000.00 USD | 0.00 USD | 633,890.00 USD | 677,470.00 USD | 1,550,000.00 USD |
| `7D` | `1.28` | 96,090,000.00 USD | 96,090,000.00 USD | 0.00 USD | 712,000.00 USD | 1,720,000.00 USD | 2,000,000.00 USD |
| `1D` | `1.29` | 54,340,000.00 USD | 54,340,000.00 USD | 0.00 USD | 828,650.00 USD | 960,560.00 USD | 545,460.00 USD |
| `7D` | `1.29` | 97,250,000.00 USD | 97,250,000.00 USD | 0.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD |
| `1D` | `1.29` | 54,720,000.00 USD | 54,720,000.00 USD | 0.00 USD | 210,950.00 USD | 24,800.00 USD | 148,370.00 USD |
| `7D` | `1.29` | 97,370,000.00 USD | 97,370,000.00 USD | 0.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD |
| `1D` | `1.29` | 55,210,000.00 USD | 55,210,000.00 USD | 0.00 USD | 177,490.00 USD | 42,820.00 USD | 268,660.00 USD |
| `7D` | `1.29` | 99,660,000.00 USD | 99,660,000.00 USD | 0.00 USD | 1,060,000.00 USD | 202,640.00 USD | 1,030,000.00 USD |
| `1D` | `1.29` | 58,210,000.00 USD | 58,210,000.00 USD | 0.00 USD | 570,020.00 USD | 197,630.00 USD | 2,240,000.00 USD |
| `7D` | `1.29` | 100,280,000.00 USD | 100,280,000.00 USD | 0.00 USD | 119,390.00 USD | 0.00 USD | 497,400.00 USD |
| `1D` | `1.29` | 64,380,000.00 USD | 64,380,000.00 USD | 0.00 USD | 1,880,000.00 USD | 719,050.00 USD | 3,570,000.00 USD |
| `7D` | `1.29` | 109,980,000.00 USD | 109,980,000.00 USD | 0.00 USD | 3,420,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD |
| `1D` | `1.30` | 66,950,000.00 USD | 66,950,000.00 USD | 0.00 USD | 554,720.00 USD | 703,990.00 USD | 1,310,000.00 USD |
| `7D` | `1.30` | 111,300,000.00 USD | 111,300,000.00 USD | 0.00 USD | 209,360.00 USD | 480,300.00 USD | 628,450.00 USD |
| `1D` | `1.30` | 67,710,000.00 USD | 67,710,000.00 USD | 0.00 USD | 335,370.00 USD | 109,620.00 USD | 312,020.00 USD |
| `7D` | `1.30` | 113,470,000.00 USD | 113,470,000.00 USD | 0.00 USD | 25,800.00 USD | 183,900.00 USD | 1,960,000.00 USD |
| `1D` | `1.30` | 69,960,000.00 USD | 69,960,000.00 USD | 0.00 USD | 530,940.00 USD | 364,450.00 USD | 1,360,000.00 USD |
| `7D` | `1.30` | 115,190,000.00 USD | 115,190,000.00 USD | 0.00 USD | 264,890.00 USD | 486,620.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 71,990,000.00 USD | 71,990,000.00 USD | 0.00 USD | 761,460.00 USD | 808,970.00 USD | 455,310.00 USD |
| `7D` | `1.30` | 118,400,000.00 USD | 118,400,000.00 USD | 0.00 USD | 29,580.00 USD | 2,690,000.00 USD | 485,710.00 USD |
| `1D` | `1.30` | 73,270,000.00 USD | 73,270,000.00 USD | 0.00 USD | 304,340.00 USD | 649,450.00 USD | 327,890.00 USD |
| `7D` | `1.30` | 118,400,000.00 USD | 118,400,000.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD |
| `1D` | `1.31` | 75,640,000.00 USD | 75,640,000.00 USD | 0.00 USD | 736,330.00 USD | 147,250.00 USD | 1,490,000.00 USD |
| `7D` | `1.31` | 121,410,000.00 USD | 121,410,000.00 USD | 0.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD |
| `1D` | `1.31` | 79,060,000.00 USD | 79,060,000.00 USD | 0.00 USD | 1,160,000.00 USD | 424,760.00 USD | 1,830,000.00 USD |
| `7D` | `1.31` | 126,190,000.00 USD | 126,190,000.00 USD | 0.00 USD | 1,700,000.00 USD | 1,150,000.00 USD | 1,930,000.00 USD |
| `1D` | `1.31` | 81,320,000.00 USD | 81,320,000.00 USD | 0.00 USD | 899,580.00 USD | 565,300.00 USD | 801,010.00 USD |
| `7D` | `1.31` | 129,530,000.00 USD | 129,530,000.00 USD | 0.00 USD | 839,350.00 USD | 511,590.00 USD | 1,990,000.00 USD |
| `1D` | `1.31` | 83,340,000.00 USD | 83,340,000.00 USD | 0.00 USD | 729,330.00 USD | 341,030.00 USD | 944,450.00 USD |
| `7D` | `1.31` | 132,370,000.00 USD | 132,370,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD |
| `1D` | `1.31` | 85,610,000.00 USD | 85,610,000.00 USD | 0.00 USD | 342,500.00 USD | 387,380.00 USD | 1,540,000.00 USD |
| `7D` | `1.31` | 134,830,000.00 USD | 134,830,000.00 USD | 0.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 90,810,000.00 USD | 90,810,000.00 USD | 0.00 USD | 1,300,000.00 USD | 929,120.00 USD | 2,970,000.00 USD |
| `7D` | `1.32` | 139,450,000.00 USD | 139,450,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 95,690,000.00 USD | 95,690,000.00 USD | 0.00 USD | 1,680,000.00 USD | 733,340.00 USD | 2,460,000.00 USD |
| `7D` | `1.32` | 142,540,000.00 USD | 142,540,000.00 USD | 0.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 98,650,000.00 USD | 98,650,000.00 USD | 0.00 USD | 1,500,000.00 USD | 499,050.00 USD | 959,190.00 USD |
| `7D` | `1.32` | 144,370,000.00 USD | 144,370,000.00 USD | 0.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD |
| `1D` | `1.32` | 101,770,000.00 USD | 101,770,000.00 USD | 0.00 USD | 997,120.00 USD | 481,660.00 USD | 1,640,000.00 USD |
| `7D` | `1.32` | 148,820,000.00 USD | 148,820,000.00 USD | 0.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD |
| `1D` | `1.32` | 102,910,000.00 USD | 102,910,000.00 USD | 0.00 USD | 710,170.00 USD | 83,050.00 USD | 341,150.00 USD |
| `7D` | `1.32` | 151,190,000.00 USD | 151,190,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 104,050,000.00 USD | 104,050,000.00 USD | 0.00 USD | 481,530.00 USD | 225,260.00 USD | 436,220.00 USD |
| `7D` | `1.33` | 151,730,000.00 USD | 151,730,000.00 USD | 0.00 USD | 462,320.00 USD | 8,400.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 105,540,000.00 USD | 105,540,000.00 USD | 0.00 USD | 504,110.00 USD | 72,470.00 USD | 911,200.00 USD |
| `7D` | `1.33` | 153,020,000.00 USD | 153,020,000.00 USD | 0.00 USD | 90,750.00 USD | 110,720.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 107,710,000.00 USD | 107,710,000.00 USD | 0.00 USD | 848,670.00 USD | 101,110.00 USD | 1,220,000.00 USD |
| `7D` | `1.33` | 154,750,000.00 USD | 154,750,000.00 USD | 0.00 USD | 581,420.00 USD | 273,310.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 109,660,000.00 USD | 109,660,000.00 USD | 0.00 USD | 737,030.00 USD | 194,040.00 USD | 1,020,000.00 USD |
| `7D` | `1.33` | 158,840,000.00 USD | 158,840,000.00 USD | 0.00 USD | 1,450,000.00 USD | 406,200.00 USD | 2,230,000.00 USD |
| `1D` | `1.33` | 110,990,000.00 USD | 110,990,000.00 USD | 0.00 USD | 459,140.00 USD | 356,270.00 USD | 517,170.00 USD |
| `7D` | `1.33` | 159,380,000.00 USD | 159,380,000.00 USD | 0.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 111,740,000.00 USD | 111,740,000.00 USD | 0.00 USD | 388,720.00 USD | 23,420.00 USD | 332,450.00 USD |
| `7D` | `1.34` | 161,330,000.00 USD | 161,330,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD |
| `1D` | `1.34` | 112,340,000.00 USD | 112,340,000.00 USD | 0.00 USD | 179,460.00 USD | 83,160.00 USD | 334,340.00 USD |
| `7D` | `1.34` | 163,670,000.00 USD | 163,670,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD |
| `1D` | `1.34` | 113,850,000.00 USD | 113,850,000.00 USD | 0.00 USD | 701,920.00 USD | 312,600.00 USD | 499,950.00 USD |
| `7D` | `1.34` | 168,150,000.00 USD | 168,150,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,400,000.00 USD | 423,310.00 USD |
| `1D` | `1.34` | 115,900,000.00 USD | 115,900,000.00 USD | 0.00 USD | 963,900.00 USD | 368,440.00 USD | 716,420.00 USD |
| `7D` | `1.34` | 173,700,000.00 USD | 173,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 2,610,000.00 USD | 1,240,000.00 USD |
| `1D` | `1.34` | 117,470,000.00 USD | 117,470,000.00 USD | 0.00 USD | 556,930.00 USD | 328,690.00 USD | 683,630.00 USD |
| `7D` | `1.34` | 183,980,000.00 USD | 183,980,000.00 USD | 0.00 USD | 3,320,000.00 USD | 1,810,000.00 USD | 5,150,000.00 USD |
| `1D` | `1.35` | 118,060,000.00 USD | 118,060,000.00 USD | 0.00 USD | 206,540.00 USD | 183,280.00 USD | 204,210.00 USD |
| `7D` | `1.35` | 190,920,000.00 USD | 190,920,000.00 USD | 0.00 USD | 2,310,000.00 USD | 2,160,000.00 USD | 2,460,000.00 USD |
| `1D` | `1.35` | 118,720,000.00 USD | 118,720,000.00 USD | 0.00 USD | 305,090.00 USD | 33,600.00 USD | 316,830.00 USD |
| `7D` | `1.35` | 200,520,000.00 USD | 200,520,000.00 USD | 0.00 USD | 4,230,000.00 USD | 1,560,000.00 USD | 3,810,000.00 USD |
| `1D` | `1.35` | 119,200,000.00 USD | 119,200,000.00 USD | 0.00 USD | 201,390.00 USD | 41,110.00 USD | 237,640.00 USD |
| `7D` | `1.35` | 207,860,000.00 USD | 207,860,000.00 USD | 0.00 USD | 2,210,000.00 USD | 1,380,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 119,380,000.00 USD | 119,380,000.00 USD | 0.00 USD | 100,960.00 USD | 30,780.00 USD | 49,480.00 USD |
| `7D` | `1.35` | 215,640,000.00 USD | 215,640,000.00 USD | 0.00 USD | 2,610,000.00 USD | 1,030,000.00 USD | 4,150,000.00 USD |
| `1D` | `1.35` | 119,950,000.00 USD | 119,950,000.00 USD | 0.00 USD | 86,720.00 USD | 34,870.00 USD | 451,740.00 USD |
| `7D` | `1.35` | 222,970,000.00 USD | 222,970,000.00 USD | 0.00 USD | 3,390,000.00 USD | 710,240.00 USD | 3,230,000.00 USD |
| `1D` | `1.36` | 120,910,000.00 USD | 120,910,000.00 USD | 0.00 USD | 391,410.00 USD | 32,820.00 USD | 531,190.00 USD |
| `7D` | `1.36` | 226,750,000.00 USD | 226,750,000.00 USD | 0.00 USD | 1,340,000.00 USD | 802,060.00 USD | 1,640,000.00 USD |
| `1D` | `1.36` | 121,240,000.00 USD | 121,240,000.00 USD | 0.00 USD | 209,880.00 USD | 43,200.00 USD | 82,650.00 USD |
| `7D` | `1.36` | 230,540,000.00 USD | 230,540,000.00 USD | 0.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.36` | 121,900,000.00 USD | 121,900,000.00 USD | 0.00 USD | 225,120.00 USD | 162,390.00 USD | 269,830.00 USD |
| `7D` | `1.36` | 232,710,000.00 USD | 232,710,000.00 USD | 0.00 USD | 696,770.00 USD | 547,690.00 USD | 925,670.00 USD |
| `1D` | `1.36` | 122,200,000.00 USD | 122,200,000.00 USD | 0.00 USD | 130,140.00 USD | 3,300.00 USD | 166,000.00 USD |
| `7D` | `1.36` | 236,810,000.00 USD | 236,810,000.00 USD | 0.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD |
| `1D` | `1.36` | 122,320,000.00 USD | 122,320,000.00 USD | 0.00 USD | 0.00 USD | 12,740.00 USD | 107,470.00 USD |
| `7D` | `1.36` | 238,530,000.00 USD | 238,530,000.00 USD | 0.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD |
| `1D` | `1.37` | 122,570,000.00 USD | 122,570,000.00 USD | 0.00 USD | 59,970.00 USD | 89,800.00 USD | 103,780.00 USD |
| `7D` | `1.37` | 239,010,000.00 USD | 239,010,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD |
| `1D` | `1.37` | 122,720,000.00 USD | 122,720,000.00 USD | 0.00 USD | 93,070.00 USD | 21,460.00 USD | 28,340.00 USD |
| `7D` | `1.37` | 240,430,000.00 USD | 240,430,000.00 USD | 0.00 USD | 528,490.00 USD | 135,290.00 USD | 750,920.00 USD |
| `1D` | `1.37` | 122,820,000.00 USD | 122,820,000.00 USD | 0.00 USD | 5,340.00 USD | 39,430.00 USD | 60,120.00 USD |
| `7D` | `1.37` | 241,580,000.00 USD | 241,580,000.00 USD | 0.00 USD | 351,750.00 USD | 349,810.00 USD | 445,570.00 USD |
| `1D` | `1.37` | 122,910,000.00 USD | 122,910,000.00 USD | 0.00 USD | 5,470.00 USD | 1,530.00 USD | 84,110.00 USD |
| `7D` | `1.37` | 243,630,000.00 USD | 243,630,000.00 USD | 0.00 USD | 680,710.00 USD | 318,880.00 USD | 1,050,000.00 USD |
| `1D` | `1.38` | 123,080,000.00 USD | 123,080,000.00 USD | 0.00 USD | 79,690.00 USD | 29,190.00 USD | 63,290.00 USD |
| `7D` | `1.38` | 245,390,000.00 USD | 245,390,000.00 USD | 0.00 USD | 519,370.00 USD | 275,610.00 USD | 966,400.00 USD |
| `1D` | `1.38` | 123,200,000.00 USD | 123,200,000.00 USD | 0.00 USD | 12,370.00 USD | 1,260.00 USD | 105,870.00 USD |
| `7D` | `1.38` | 246,410,000.00 USD | 246,410,000.00 USD | 0.00 USD | 417,010.00 USD | 308,370.00 USD | 300,380.00 USD |
| `1D` | `1.38` | 123,480,000.00 USD | 123,480,000.00 USD | 0.00 USD | 69,610.00 USD | 60,790.00 USD | 142,490.00 USD |
| `7D` | `1.38` | 248,270,000.00 USD | 248,270,000.00 USD | 0.00 USD | 573,060.00 USD | 190,650.00 USD | 1,100,000.00 USD |
| `1D` | `1.38` | 123,540,000.00 USD | 123,540,000.00 USD | 0.00 USD | 0.00 USD | 65,520.00 USD | 0.00 USD |
| `7D` | `1.38` | 250,370,000.00 USD | 250,370,000.00 USD | 0.00 USD | 1,020,000.00 USD | 249,550.00 USD | 825,050.00 USD |
| `1D` | `1.38` | 123,710,000.00 USD | 123,710,000.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 168,450.00 USD |
| `7D` | `1.38` | 251,300,000.00 USD | 251,300,000.00 USD | 0.00 USD | 297,210.00 USD | 273,610.00 USD | 361,360.00 USD |
| `1D` | `1.39` | 123,820,000.00 USD | 123,820,000.00 USD | 0.00 USD | 63,980.00 USD | 37,600.00 USD | 5,920.00 USD |
| `7D` | `1.39` | 252,590,000.00 USD | 252,590,000.00 USD | 0.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 124,010,000.00 USD | 124,010,000.00 USD | 0.00 USD | 0.00 USD | 122,160.00 USD | 66,680.00 USD |
| `7D` | `1.39` | 253,130,000.00 USD | 253,130,000.00 USD | 0.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD |
| `1D` | `1.39` | 124,100,000.00 USD | 124,100,000.00 USD | 0.00 USD | 40,370.00 USD | 48,950.00 USD | 0.00 USD |
| `7D` | `1.39` | 254,230,000.00 USD | 254,230,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD |
| `7D` | `1.39` | 254,400,000.00 USD | 254,400,000.00 USD | 0.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD |
| `7D` | `1.39` | 254,720,000.00 USD | 254,720,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `7D` | `1.40` | 254,890,000.00 USD | 254,890,000.00 USD | 0.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD |
| `7D` | `1.40` | 255,010,000.00 USD | 255,010,000.00 USD | 0.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `7D` | `1.40` | 255,020,000.00 USD | 255,020,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 255,160,000.00 USD | 255,160,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 255,270,000.00 USD | 255,270,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `7D` | `1.41` | 255,510,000.00 USD | 255,510,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 255,680,000.00 USD | 255,680,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `7D` | `1.41` | 256,060,000.00 USD | 256,060,000.00 USD | 0.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `7D` | `1.41` | 256,710,000.00 USD | 256,710,000.00 USD | 0.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `7D` | `1.41` | 256,880,000.00 USD | 256,880,000.00 USD | 0.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD |
| `7D` | `1.42` | 257,510,000.00 USD | 257,510,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD |
| `7D` | `1.42` | 258,030,000.00 USD | 258,030,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `7D` | `1.42` | 259,050,000.00 USD | 259,050,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `7D` | `1.42` | 260,430,000.00 USD | 260,430,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `7D` | `1.42` | 261,040,000.00 USD | 261,040,000.00 USD | 0.00 USD | 202,370.00 USD | 161,570.00 USD | 244,040.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.87B` | Total OI Tokens: `2,274,685,420.2 XRP`
  * 1h OI Change: `+1.56%` | 4h OI Change: `+4.79%` | 24h OI Change: `-4.18%`
  * Exchange Breakdown: Binance=`436.15M` | Bybit=`319.63M` | OKX=`95.64M` | Hyperliquid=`199.41M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-53.72K` | Last 24h: `81.98K` | Last 3d: `547.43K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0077%` | **USDT OKX** | `-0.0123%` |
| **USDT Bybit** | `-0.0260%` | **USDT KuCoin** | `-0.0031%` |
| **USDT MEXC** | `0.0076%` | **USDT BingX** | `0.0075%` |
| **USDT Gate** | `-0.0011%` | **USDT Bitget** | `-0.0037%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `51.80%` | `48.20%` | `1.07` | 235,190,000.00 USD |
| `15M` | `Binance` | `52.84%` | `47.16%` | `1.12` | 82,450,000.00 USD |
| `15M` | `OKX` | `36.62%` | `63.38%` | `0.58` | 48,870,000.00 USD |
| `15M` | `Bybit` | `59.39%` | `40.61%` | `1.46` | 14,260,000.00 USD |
| `15M` | `KuCoin` | `32.9%` | `67.1%` | `0.49` | 845,870.00 USD |
| `15M` | `Gate` | `62.24%` | `37.76%` | `1.65` | 38,630,000.00 USD |
| `15M` | `Bitget` | `39.64%` | `60.36%` | `0.66` | 9,700,000.00 USD |
| `15M` | `BingX` | `37.89%` | `62.11%` | `0.61` | 2,980,000.00 USD |
| `15M` | `MEXC` | `51.44%` | `48.56%` | `1.06` | 7,390,000.00 USD |
| `15M` | `Bitunix` | `51.13%` | `48.87%` | `1.05` | 10,710,000.00 USD |
| `15M` | `Hyperliquid` | `12.2%` | `87.8%` | `0.14` | 4,490,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.15%` | `51.85%` | `0.93` | 2,250,000.00 USD |
| `15M` | `Crypto.com` | `51.58%` | `48.42%` | `1.07` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.61%` | `0.39%` | `255.41` | 1,270,000.00 USD |
| `15M` | `HTX` | `49.12%` | `50.88%` | `0.97` | 3,810,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 1,810,000.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 83,140.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `53.05%` | `46.95%` | `1.13` | 2,720,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.27%` | `55.73%` | `0.79` | 2,910,000.00 USD |
| `15M` | `Whale Positions` | `52.84%` | `47.16%` | `1.12` | 82,450,000.00 USD |
| `15M` | `Global Accounts` | `51.80%` | `48.20%` | `1.07` | 235,190,000.00 USD |
| `1H` | `XRP` | `50.85%` | `49.15%` | `1.03` | 2,260,000,000.00 USD |
| `1H` | `Binance` | `50.86%` | `49.14%` | `1.04` | 413,420,000.00 USD |
| `1H` | `OKX` | `45.35%` | `54.65%` | `0.83` | 262,830,000.00 USD |
| `1H` | `Bybit` | `47.24%` | `52.76%` | `0.90` | 112,420,000.00 USD |
| `1H` | `KuCoin` | `51.77%` | `48.23%` | `1.07` | 4,790,000.00 USD |
| `1H` | `Gate` | `51.68%` | `48.32%` | `1.07` | 225,380,000.00 USD |
| `1H` | `Bitget` | `44.5%` | `55.5%` | `0.80` | 74,830,000.00 USD |
| `1H` | `BingX` | `38.26%` | `61.74%` | `0.62` | 15,790,000.00 USD |
| `1H` | `MEXC` | `44.21%` | `55.79%` | `0.79` | 40,510,000.00 USD |
| `1H` | `Bitunix` | `52.71%` | `47.29%` | `1.11` | 45,760,000.00 USD |
| `1H` | `Hyperliquid` | `48.51%` | `51.49%` | `0.94` | 37,070,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `61.35%` | `38.65%` | `1.59` | 6,320,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `52.94%` | `47.06%` | `1.12` | 957,730,000.00 USD |
| `1H` | `HTX` | `75.57%` | `24.43%` | `3.09` | 25,890,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `54.02%` | `45.98%` | `1.17` | 8,520,000.00 USD |
| `1H` | `Bitfinex` | `15.81%` | `84.19%` | `0.19` | 878,470.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `40.25%` | `59.75%` | `0.67` | 9,410,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.96%` | `49.04%` | `1.04` | 15,480,000.00 USD |
| `1H` | `Whale Positions` | `50.86%` | `49.14%` | `1.04` | 413,420,000.00 USD |
| `1H` | `Global Accounts` | `50.85%` | `49.15%` | `1.03` | 2,260,000,000.00 USD |
| `4H` | `XRP` | `55.06%` | `44.94%` | `1.23` | 601,310,000.00 USD |
| `4H` | `Binance` | `54.12%` | `45.88%` | `1.18` | 206,020,000.00 USD |
| `4H` | `OKX` | `51.73%` | `48.27%` | `1.07` | 77,760,000.00 USD |
| `4H` | `Bybit` | `56.35%` | `43.65%` | `1.29` | 102,870,000.00 USD |
| `4H` | `KuCoin` | `51.37%` | `48.63%` | `1.06` | 6,500,000.00 USD |
| `4H` | `Gate` | `56.95%` | `43.05%` | `1.32` | 21,950,000.00 USD |
| `4H` | `Bitget` | `55.11%` | `44.89%` | `1.23` | 38,200,000.00 USD |
| `4H` | `BingX` | `49.01%` | `50.99%` | `0.96` | 13,690,000.00 USD |
| `4H` | `MEXC` | `55.93%` | `44.07%` | `1.27` | 78,940,000.00 USD |
| `4H` | `Bitunix` | `54.81%` | `45.19%` | `1.21` | 18,490,000.00 USD |
| `4H` | `Hyperliquid` | `55.58%` | `44.42%` | `1.25` | 20,580,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `63.55%` | `36.45%` | `1.74` | 2,460,000.00 USD |
| `4H` | `Crypto.com` | `55.6%` | `44.4%` | `1.25` | 991,230.00 USD |
| `4H` | `WhiteBIT` | `94.5%` | `5.5%` | `17.18` | 7,600,000.00 USD |
| `4H` | `HTX` | `49.48%` | `50.52%` | `0.98` | 692,510.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `54.9%` | `45.1%` | `1.22` | 160,020.00 USD |
| `4H` | `Aster` | `47.33%` | `52.67%` | `0.90` | 2,910,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `65.82%` | `34.18%` | `1.93` | 1,500,000.00 USD |
| `4H` | `Whale Positions` | `54.12%` | `45.88%` | `1.18` | 206,020,000.00 USD |
| `4H` | `Global Accounts` | `55.06%` | `44.94%` | `1.23` | 601,310,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `1.24` | `1.24` | `1.24` | `1.24` | `1.23` | 14,534,365.59 USD | 7,960,789.37 USD | 6,573,576.22 USD | 1,387,213.15 USD | `+9.54%` | `20B / 9S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.24` | 13,408,965.14 USD | 7,227,260.97 USD | 6,181,704.17 USD | 1,045,556.80 USD | `+7.80%` | `8B / 3S` |
| `0:00 UTC` | `1.24` | `1.25` | `1.24` | `1.25` | `1.24` | 11,613,568.18 USD | 6,301,411.52 USD | 5,312,156.67 USD | 989,254.85 USD | `+8.52%` | `26B / 9S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 11,339,015.88 USD | 5,463,329.20 USD | 5,875,686.68 USD | -412,357.48 USD | `-3.64%` | `7B / 6S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 9,975,142.90 USD | 5,917,919.57 USD | 4,057,223.33 USD | 1,860,696.23 USD | `+18.65%` | `9B / 2S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 6,812,599.45 USD | 3,905,481.96 USD | 2,907,117.49 USD | 998,364.47 USD | `+14.65%` | `4B / 3S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 9,935,673.56 USD | 6,437,809.71 USD | 3,497,863.85 USD | 2,939,945.86 USD | `+29.59%` | `23B / 7S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 6,138,672.69 USD | 3,294,606.36 USD | 2,844,066.33 USD | 450,540.03 USD | `+7.34%` | `3B / 1S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 5,482,004.91 USD | 2,916,488.83 USD | 2,565,516.08 USD | 350,972.75 USD | `+6.40%` | `2B / 2S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 1,594,404.11 USD | 884,797.47 USD | 709,606.64 USD | 175,190.82 USD | `+10.99%` | `3B / 4S` |

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
| `5m` | 37,150.00 USD | 439,330.00 USD | **`ACCUMULATION`** |
| `15m` | 455,500.00 USD | -1,650.00 USD | **`ACCUMULATION`** |
| `30m` | 1,290,000.00 USD | 954,250.00 USD | **`ACCUMULATION`** |
| `1h` | 3,160,000.00 USD | 6,070,000.00 USD | **`ACCUMULATION`** |
| `2h` | 7,170,000.00 USD | 19,340,000.00 USD | **`ACCUMULATION`** |
| `4h` | 18,940,000.00 USD | 32,870,000.00 USD | **`ACCUMULATION`** |
| `6h` | 28,130.00 USD | -1,770,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -16,120,000.00 USD | -73,770,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -49,050,000.00 USD | -115,320,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -52,900,000.00 USD | -131,410,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -122,220,000.00 USD | -213,830,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -597,680,000.00 USD | -1,290,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+37.15K` | 15m=`+455.50K` | 1h=`+3.16M` | 24h=`-52.90M`
* Futures Capital Netflows: 5m=`+439.33K` | 15m=`-1.65K` | 1h=`+6.07M` | 24h=`-131.41M`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:19:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:20:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.21` (Risk Distance: `0.0174` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.28` (Risk Distance: `0.0174` pts)
  * +2.5R Take Profit: `1.22`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
