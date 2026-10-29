# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 00:26:16 IST` (`2026-10-29 18:56:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.29` | **Live Ask Quote**: `1.29` | **Mid Price**: `1.29`
- **Spread Points**: `3.00` | **Spread BPS**: `23.30 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.29` | VWAP Z-Score: `-1.58` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0066` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `35.10` (State: `NEUTRAL`)
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
  * Institutional Anchors: EMA-144=`1.30` | EMA-200=`1.30` (Slope: `-0.0823`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.28` | Weekly High=`1.34` | Weekly Low=`1.28`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.30` (Distance: `-0.88%`)
  * Point of Control (POC) = `1.29` (Distance: `-0.11%`)
  * Value Area Low (VAL) = `1.28` (Distance: `+0.27%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
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
  * Structural Invalidation Anchor (0.786): `1.30`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.28` | `1.28` | `1.28` | `1.28` | `3,936,770` | 5,038,932.50 USD | 218,440.86 USD | `+4.34%` | -36,068,672.28 USD | `+0.36` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `1.28` | `1.28` | `1.28` | `1.28` | `2,644,461` | 3,389,520.93 USD | -328,910.91 USD | `-9.70%` | -36,397,583.19 USD | `+0.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `1.28` | `1.29` | `1.28` | `1.29` | `3,006,295` | 3,864,770.97 USD | 1,470,634.89 USD | `+38.05%` | -34,926,948.29 USD | `+0.87` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.29` | `1.29` | `1.29` | `1.29` | `3,408,363` | 4,397,440.00 USD | -499,769.95 USD | `-11.37%` | -26,073,705.22 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.29` | `1.29` | `1.28` | `1.28` | `23,675,158` | 30,348,241.89 USD | -9,993,148.87 USD | `-32.93%` | -36,066,854.09 USD | `-3.75` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.28` | `1.29` | `1.28` | `1.29` | `5,650,756` | 7,254,291.90 USD | 1,141,723.98 USD | `+15.74%` | -34,925,130.10 USD | `+0.71` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `1.31` | `1.32` | `1.30` | `1.30` | `30,534,069` | 39,864,527.69 USD | -3,664,960.48 USD | `-9.19%` | -24,545,254.96 USD | `-0.63` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.30` | `1.30` | `1.29` | `1.29` | `27,238,695` | 35,241,786.93 USD | -1,210,810.88 USD | `-3.44%` | -25,756,065.84 USD | `+0.08` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.29` | `36,531,435` | 46,908,294.74 USD | -9,169,066.97 USD | `-19.55%` | -34,925,132.81 USD | `-1.90` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.29` | `94,304,182` | 122,014,588.36 USD | -14,044,835.62 USD | `-11.51%` | -38,547,010.76 USD | `-0.84` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.33` | `1.29` | `1.29` | `112,558,954` | 146,533,666.97 USD | -23,231,128.88 USD | `-15.85%` | -23,206,069.15 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,047,304.81 USD | `+0.62` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.29` | `94,304,182` | 122,014,588.36 USD | -14,044,835.62 USD | `-11.51%` | -38,547,010.76 USD | `-0.84` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`1.29`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `1.29` | `21903.0000` | 28,254.87 USD | 2,873,099.74 USD | `11 orders` | `+0.15%` | `-` |
| `ASK` | `1.29` | `90854.0000` | 117,192.57 USD | 2,844,844.87 USD | `4 orders` | `+0.14%` | `-` |
| `ASK` | `1.29` | `236913.0000` | 305,570.39 USD | 2,727,652.29 USD | `6 orders` | `+0.14%` | `-` |
| `ASK` | `1.29` | `372968.0000` | 481,016.83 USD | 2,422,081.91 USD | `9 orders` | `+0.13%` | `-` |
| `ASK` | `1.29` | `87503.0000` | 112,843.87 USD | 1,941,065.08 USD | `7 orders` | `+0.12%` | `-` |
| `ASK` | `1.29` | `297813.0000` | 384,029.86 USD | 1,828,221.21 USD | `8 orders` | `+0.11%` | `-` |
| `ASK` | `1.29` | `237932.0000` | 306,789.52 USD | 1,444,191.34 USD | `13 orders` | `+0.10%` | `-` |
| `ASK` | `1.29` | `114771.0000` | 147,974.25 USD | 1,137,401.82 USD | `10 orders` | `+0.10%` | `-` |
| `ASK` | `1.29` | `90523.0000` | 116,702.25 USD | 989,427.57 USD | `12 orders` | `+0.09%` | `-` |
| `ASK` | `1.29` | `149770.0000` | 193,068.51 USD | 872,725.32 USD | `14 orders` | `+0.08%` | `-` |
| `ASK` | `1.29` | `115831.0000` | 149,306.16 USD | 679,656.81 USD | `11 orders` | `+0.07%` | `-` |
| `ASK` | `1.29` | `30735.0000` | 39,614.34 USD | 530,350.65 USD | `13 orders` | `+0.07%` | `-` |
| `ASK` | `1.29` | `57018.0000` | 73,484.80 USD | 490,736.31 USD | `7 orders` | `+0.06%` | `-` |
| `ASK` | `1.29` | `116454.0000` | 150,074.27 USD | 417,251.51 USD | `12 orders` | `+0.05%` | `-` |
| `ASK` | `1.29` | `61202.0000` | 78,864.90 USD | 267,177.24 USD | `16 orders` | `+0.04%` | `-` |
| `ASK` | `1.29` | `49547.0000` | 63,841.31 USD | 188,312.35 USD | `14 orders` | `+0.03%` | `-` |
| `ASK` | `1.29` | `21055.0000` | 27,127.26 USD | 124,471.04 USD | `11 orders` | `+0.03%` | `-` |
| `ASK` | `1.29` | `48101.0000` | 61,968.52 USD | 97,343.78 USD | `12 orders` | `+0.02%` | `-` |
| `ASK` | `1.29` | `14556.0000` | 18,751.04 USD | 35,375.26 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `1.29` | `12906.0000` | 16,624.22 USD | 16,624.22 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.29` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.29` | `0.00%` | `-` |
| `BID` | `1.29` | `19154.0000` | 24,670.35 USD | 24,670.35 USD | `7 orders` | `-0.00%` | `-` |
| `BID` | `1.29` | `17768.0000` | 22,883.41 USD | 47,553.76 USD | `6 orders` | `-0.01%` | `-` |
| `BID` | `1.29` | `59021.0000` | 76,007.24 USD | 123,561.00 USD | `9 orders` | `-0.02%` | `-` |
| `BID` | `1.29` | `52431.0000` | 67,515.40 USD | 191,076.40 USD | `10 orders` | `-0.03%` | `-` |
| `BID` | `1.29` | `97067.0000` | 124,983.47 USD | 316,059.87 USD | `12 orders` | `-0.03%` | `-` |
| `BID` | `1.29` | `107998.0000` | 139,047.43 USD | 455,107.30 USD | `13 orders` | `-0.04%` | `-` |
| `BID` | `1.29` | `35549.0000` | 45,765.78 USD | 500,873.08 USD | `12 orders` | `-0.05%` | `-` |
| `BID` | `1.29` | `79882.0000` | 102,832.10 USD | 603,705.18 USD | `9 orders` | `-0.06%` | `-` |
| `BID` | `1.29` | `57269.0000` | 73,716.66 USD | 677,421.83 USD | `11 orders` | `-0.07%` | `-` |
| `BID` | `1.29` | `44839.0000` | 57,712.28 USD | 735,134.11 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `1.29` | `30980.0000` | 39,871.26 USD | 775,005.37 USD | `12 orders` | `-0.08%` | `-` |
| `BID` | `1.29` | `194004.0000` | 249,663.75 USD | 1,024,669.12 USD | `13 orders` | `-0.09%` | `-` |
| `BID` | `1.29` | `71342.0000` | 91,802.89 USD | 1,116,472.00 USD | `8 orders` | `-0.10%` | `-` |
| `BID` | `1.29` | `28058.0000` | 36,102.23 USD | 1,152,574.23 USD | `9 orders` | `-0.10%` | `-` |
| `BID` | `1.29` | `231929.0000` | 298,399.85 USD | 1,450,974.08 USD | `5 orders` | `-0.11%` | `-` |
| `BID` | `1.29` | `273786.0000` | 352,225.69 USD | 1,803,199.77 USD | `6 orders` | `-0.12%` | `-` |
| `BID` | `1.29` | `561979.0000` | 722,929.79 USD | 2,526,129.56 USD | `11 orders` | `-0.13%` | `-` |
| `BID` | `1.29` | `90854.0000` | 116,865.50 USD | 2,642,995.06 USD | `8 orders` | `-0.14%` | `-` |
| `BID` | `1.29` | `82859.0000` | 106,573.25 USD | 2,749,568.30 USD | `7 orders` | `-0.14%` | `-` |
| `BID` | `1.29` | `57023.0000` | 73,337.28 USD | 2,822,905.58 USD | `10 orders` | `-0.15%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:25:14 IST` |

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
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,374.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.37K USD at 1.3296 USD [API] | `2026-10-27 23:03:56` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,036.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.04K USD at 1.3303 USD [API] | `2026-10-27 23:15:51` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,692.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.69K USD at 1.3284 USD [API] | `2026-10-27 23:17:44` |


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
| `7D` | `Long Liquidation` | `1.15` | 191,160,000.00 USD | 191,160,000.00 USD | 237,280.00 USD | 98,230.00 USD | 109,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 190,710,000.00 USD | 190,710,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 66,270,000.00 USD | 66,270,000.00 USD | 1,390.00 USD | 149.67 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 190,560,000.00 USD | 190,560,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 66,200,000.00 USD | 66,200,000.00 USD | 48,490.00 USD | 414.70 USD | 112,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 190,390,000.00 USD | 190,390,000.00 USD | 139,270.00 USD | 55,690.00 USD | 328,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 116,500.00 USD | 23,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 66,040,000.00 USD | 66,040,000.00 USD | 1,740.00 USD | 158.40 USD | 28,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 189,870,000.00 USD | 189,870,000.00 USD | 39,530.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 66,010,000.00 USD | 66,010,000.00 USD | 66,460.00 USD | 27,280.00 USD | 27,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 189,650,000.00 USD | 189,650,000.00 USD | 258,370.00 USD | 96,700.00 USD | 406,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 65,890,000.00 USD | 65,890,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 188,880,000.00 USD | 188,880,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 65,510,000.00 USD | 65,510,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 188,150,000.00 USD | 188,150,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 64,770,000.00 USD | 64,770,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 187,100,000.00 USD | 187,100,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,600,000.00 USD | 23,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 64,340,000.00 USD | 64,340,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 185,760,000.00 USD | 185,760,000.00 USD | 218,150.00 USD | 212,700.00 USD | 529,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 64,010,000.00 USD | 64,010,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 184,800,000.00 USD | 184,800,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 63,830,000.00 USD | 63,830,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 183,730,000.00 USD | 183,730,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 63,670,000.00 USD | 63,670,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 181,710,000.00 USD | 181,710,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 63,450,000.00 USD | 63,450,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 180,850,000.00 USD | 180,850,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 925,770.00 USD | 21,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 63,170,000.00 USD | 63,170,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 179,970,000.00 USD | 179,970,000.00 USD | 181,850.00 USD | 95,620.00 USD | 377,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 62,950,000.00 USD | 62,950,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 179,310,000.00 USD | 179,310,000.00 USD | 85,020.00 USD | 74,230.00 USD | 358,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 62,780,000.00 USD | 62,780,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 178,790,000.00 USD | 178,790,000.00 USD | 270,280.00 USD | 180,410.00 USD | 209,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 62,700,000.00 USD | 62,700,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 178,130,000.00 USD | 178,130,000.00 USD | 78,320.00 USD | 47,010.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 62,610,000.00 USD | 62,610,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 177,890,000.00 USD | 177,890,000.00 USD | 119,620.00 USD | 66,800.00 USD | 377,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 1,720,000.00 USD | 20,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 62,500,000.00 USD | 62,500,000.00 USD | 694.57 USD | 23,390.00 USD | 20,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 177,330,000.00 USD | 177,330,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 62,450,000.00 USD | 62,450,000.00 USD | 30,140.00 USD | 99.63 USD | 12,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 177,150,000.00 USD | 177,150,000.00 USD | 216,330.00 USD | 94,590.00 USD | 606,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 62,410,000.00 USD | 62,410,000.00 USD | 10,800.00 USD | 238.88 USD | 21,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 176,230,000.00 USD | 176,230,000.00 USD | 211,840.00 USD | 81,140.00 USD | 281,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 62,380,000.00 USD | 62,380,000.00 USD | 20,520.00 USD | 18,150.00 USD | 56,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 175,660,000.00 USD | 175,660,000.00 USD | 149,990.00 USD | 95,880.00 USD | 123,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 62,280,000.00 USD | 62,280,000.00 USD | 130,470.00 USD | 44,250.00 USD | 112,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 175,290,000.00 USD | 175,290,000.00 USD | 219,860.00 USD | 72,930.00 USD | 465,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 496,770.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 62,000,000.00 USD | 62,000,000.00 USD | 64,240.00 USD | 18,340.00 USD | 29,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 174,530,000.00 USD | 174,530,000.00 USD | 251,760.00 USD | 140,610.00 USD | 318,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 61,880,000.00 USD | 61,880,000.00 USD | 112,660.00 USD | 7,010.00 USD | 10,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 173,820,000.00 USD | 173,820,000.00 USD | 5,350.00 USD | 38,700.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 61,750,000.00 USD | 61,750,000.00 USD | 26,800.00 USD | 20,630.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 173,750,000.00 USD | 173,750,000.00 USD | 72,960.00 USD | 36,750.00 USD | 18,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 61,710,000.00 USD | 61,710,000.00 USD | 55,140.00 USD | 14,180.00 USD | 61,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 173,630,000.00 USD | 173,630,000.00 USD | 184,030.00 USD | 62,270.00 USD | 57,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 173,320,000.00 USD | 173,320,000.00 USD | 47,500.00 USD | 29,680.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 664,010.00 USD | 18,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 61,570,000.00 USD | 61,570,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 173,170,000.00 USD | 173,170,000.00 USD | 13,620.00 USD | 3,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 61,560,000.00 USD | 61,560,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 173,150,000.00 USD | 173,150,000.00 USD | 241,190.00 USD | 2,360.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 172,880,000.00 USD | 172,880,000.00 USD | 257,960.00 USD | 89,570.00 USD | 624,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 171,910,000.00 USD | 171,910,000.00 USD | 199,450.00 USD | 109,690.00 USD | 212,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 171,390,000.00 USD | 171,390,000.00 USD | 84,480.00 USD | 89,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 366,920.00 USD | 17,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 171,220,000.00 USD | 171,220,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 171,120,000.00 USD | 171,120,000.00 USD | 0.00 USD | 0.00 USD | 27,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 171,090,000.00 USD | 171,090,000.00 USD | 0.00 USD | 2,640.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 171,070,000.00 USD | 171,070,000.00 USD | 59,120.00 USD | 2,680.00 USD | 159,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 170,850,000.00 USD | 170,850,000.00 USD | 251,420.00 USD | 302,320.00 USD | 112,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,440,000.00 USD | 17,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 170,180,000.00 USD | 170,180,000.00 USD | 492,660.00 USD | 141,800.00 USD | 153,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 61,530,000.00 USD | 61,530,000.00 USD | 48,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 169,390,000.00 USD | 169,390,000.00 USD | 269,210.00 USD | 135,700.00 USD | 277,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 61,480,000.00 USD | 61,480,000.00 USD | 102,730.00 USD | 374.17 USD | 215,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 168,710,000.00 USD | 168,710,000.00 USD | 235,350.00 USD | 112,100.00 USD | 795,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 61,170,000.00 USD | 61,170,000.00 USD | 125,570.00 USD | 1,040.00 USD | 280,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 167,570,000.00 USD | 167,570,000.00 USD | 596,400.00 USD | 225,830.00 USD | 410,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 60,760,000.00 USD | 60,760,000.00 USD | 11,570.00 USD | 989.25 USD | 73,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 166,340,000.00 USD | 166,340,000.00 USD | 1,120,000.00 USD | 364,060.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 692,280.00 USD | 16,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 60,670,000.00 USD | 60,670,000.00 USD | 515,840.00 USD | 120,320.00 USD | 331,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 163,310,000.00 USD | 163,310,000.00 USD | 1,120,000.00 USD | 760,590.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 59,700,000.00 USD | 59,700,000.00 USD | 1,080,000.00 USD | 666,380.00 USD | 709,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 159,060,000.00 USD | 159,060,000.00 USD | 1,960,000.00 USD | 859,010.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 57,240,000.00 USD | 57,240,000.00 USD | 942,890.00 USD | 493,310.00 USD | 740,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 154,160,000.00 USD | 154,160,000.00 USD | 2,210,000.00 USD | 1,010,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 55,070,000.00 USD | 55,070,000.00 USD | 347,740.00 USD | 188,510.00 USD | 341,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 148,240,000.00 USD | 148,240,000.00 USD | 1,210,000.00 USD | 569,760.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 54,190,000.00 USD | 54,190,000.00 USD | 372,570.00 USD | 122,390.00 USD | 516,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 145,190,000.00 USD | 145,190,000.00 USD | 1,020,000.00 USD | 537,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 250,530.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.25` | 53,180,000.00 USD | 53,180,000.00 USD | 546,010.00 USD | 129,710.00 USD | 161,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 141,960,000.00 USD | 141,960,000.00 USD | 2,520,000.00 USD | 695,090.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 52,340,000.00 USD | 52,340,000.00 USD | 218,430.00 USD | 101,390.00 USD | 355,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 135,690,000.00 USD | 135,690,000.00 USD | 2,150,000.00 USD | 1,450,000.00 USD | 5,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 51,670,000.00 USD | 51,670,000.00 USD | 177,400.00 USD | 102,610.00 USD | 457,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 126,240,000.00 USD | 126,240,000.00 USD | 3,090,000.00 USD | 1,160,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 50,930,000.00 USD | 50,930,000.00 USD | 351,630.00 USD | 92,050.00 USD | 426,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 119,830,000.00 USD | 119,830,000.00 USD | 2,140,000.00 USD | 783,920.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 50,060,000.00 USD | 50,060,000.00 USD | 332,170.00 USD | 42,640.00 USD | 632,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 115,470,000.00 USD | 115,470,000.00 USD | 262,320.00 USD | 552,710.00 USD | 814,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 14,240,000.00 USD | 15,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.26` | 49,050,000.00 USD | 49,050,000.00 USD | 610,960.00 USD | 49,250.00 USD | 790,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 113,840,000.00 USD | 113,840,000.00 USD | 1,170,000.00 USD | 588,800.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 47,600,000.00 USD | 47,600,000.00 USD | 231,420.00 USD | 104,190.00 USD | 463,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 110,210,000.00 USD | 110,210,000.00 USD | 1,020,000.00 USD | 211,890.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 46,800,000.00 USD | 46,800,000.00 USD | 281,000.00 USD | 71,910.00 USD | 171,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 107,980,000.00 USD | 107,980,000.00 USD | 1,220,000.00 USD | 691,780.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 46,280,000.00 USD | 46,280,000.00 USD | 992,410.00 USD | 254,090.00 USD | 693,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 104,490,000.00 USD | 104,490,000.00 USD | 1,980,000.00 USD | 1,450,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 44,340,000.00 USD | 44,340,000.00 USD | 2,210,000.00 USD | 1,360,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 100,020,000.00 USD | 100,020,000.00 USD | 3,500,000.00 USD | 1,970,000.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.26` | 431,470.00 USD | 983,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.27` | 39,240,000.00 USD | 39,240,000.00 USD | 2,080,000.00 USD | 1,030,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 91,030,000.00 USD | 91,030,000.00 USD | 4,470,000.00 USD | 1,960,000.00 USD | 6,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 34,550,000.00 USD | 34,550,000.00 USD | 1,160,000.00 USD | 377,270.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 78,050,000.00 USD | 78,050,000.00 USD | 2,890,000.00 USD | 1,380,000.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 31,400,000.00 USD | 31,400,000.00 USD | 1,330,000.00 USD | 277,410.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 69,680,000.00 USD | 69,680,000.00 USD | 2,710,000.00 USD | 1,640,000.00 USD | 4,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 27,520,000.00 USD | 27,520,000.00 USD | 1,320,000.00 USD | 332,670.00 USD | 815,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 60,990,000.00 USD | 60,990,000.00 USD | 4,570,000.00 USD | 2,590,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 25,050,000.00 USD | 25,050,000.00 USD | 1,460,000.00 USD | 568,780.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 46,700,000.00 USD | 46,700,000.00 USD | 4,600,000.00 USD | 1,720,000.00 USD | 10,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.27` | 432,580.00 USD | 552,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.28` | 21,740,000.00 USD | 21,740,000.00 USD | 2,960,000.00 USD | 1,280,000.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 29,820,000.00 USD | 29,820,000.00 USD | 4,130,000.00 USD | 2,410,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 14,930,000.00 USD | 14,930,000.00 USD | 6,210,000.00 USD | 2,740,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 17,330,000.00 USD | 17,330,000.00 USD | 7,720,000.00 USD | 2,860,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 1,420,000.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 108,100.00 USD | 108,100.00 USD | 0.00 USD | 22,110.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 5,090,000.00 USD | 5,090,000.00 USD | 2,480,000.00 USD | 530,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 6,530,000.00 USD | 6,530,000.00 USD | 4,990,000.00 USD | 1,420,000.00 USD | 123,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.28` | 119,630.00 USD | 119,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 6,810,000.00 USD | 6,810,000.00 USD | 1,390,000.00 USD | 327,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 7,930,000.00 USD | 7,930,000.00 USD | 505,690.00 USD | 888,530.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 7,140,000.00 USD | 7,140,000.00 USD | 221,930.00 USD | 100,470.00 USD | 8,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 8,370,000.00 USD | 8,370,000.00 USD | 440,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 8,560,000.00 USD | 8,560,000.00 USD | 194,230.00 USD | 0.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 11,190,000.00 USD | 11,190,000.00 USD | 1,040,000.00 USD | 0.00 USD | 648,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 10,050,000.00 USD | 10,050,000.00 USD | 389,390.00 USD | 0.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 13,980,000.00 USD | 13,980,000.00 USD | 1,110,000.00 USD | 0.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 12,650.00 USD | 12,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 12,250,000.00 USD | 12,250,000.00 USD | 484,930.00 USD | 597,860.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 16,240,000.00 USD | 16,240,000.00 USD | 393,030.00 USD | 573,900.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 0.00 USD | 288,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 17,490,000.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 12,710,000.00 USD | 12,710,000.00 USD | 0.00 USD | 168,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 14,420,000.00 USD | 14,420,000.00 USD | 521,850.00 USD | 910,560.00 USD | 278,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 18,350,000.00 USD | 18,350,000.00 USD | 0.00 USD | 859,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 14,830,000.00 USD | 14,830,000.00 USD | 188,510.00 USD | 98,100.00 USD | 127,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 2,560.00 USD | 15,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 15,960,000.00 USD | 15,960,000.00 USD | 493,480.00 USD | 319,190.00 USD | 320,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 22,240,000.00 USD | 22,240,000.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 17,200,000.00 USD | 17,200,000.00 USD | 455,910.00 USD | 3,540.00 USD | 776,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 24,190,000.00 USD | 24,190,000.00 USD | 530,610.00 USD | 92,270.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 19,040,000.00 USD | 19,040,000.00 USD | 616,030.00 USD | 287,750.00 USD | 940,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 25,900,000.00 USD | 25,900,000.00 USD | 1,290,000.00 USD | 0.00 USD | 415,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 21,740,000.00 USD | 21,740,000.00 USD | 1,570,000.00 USD | 443,660.00 USD | 688,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 29,660,000.00 USD | 29,660,000.00 USD | 79,920.00 USD | 747,120.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 23,010,000.00 USD | 23,010,000.00 USD | 464,990.00 USD | 483,320.00 USD | 321,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 30,320,000.00 USD | 30,320,000.00 USD | 515,950.00 USD | 149,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 269.57 USD | 15,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 29,230,000.00 USD | 29,230,000.00 USD | 213,000.00 USD | 1,830,000.00 USD | 4,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 34,500,000.00 USD | 34,500,000.00 USD | 44,360.00 USD | 1,750,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 36,210,000.00 USD | 36,210,000.00 USD | 2,340,000.00 USD | 1,060,000.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 39,350,000.00 USD | 39,350,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 39,740,000.00 USD | 39,740,000.00 USD | 1,720,000.00 USD | 742,480.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 41,050,000.00 USD | 41,050,000.00 USD | 823,190.00 USD | 430,400.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 44,260,000.00 USD | 44,260,000.00 USD | 1,830,000.00 USD | 981,550.00 USD | 1,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 44,150,000.00 USD | 44,150,000.00 USD | 1,090,000.00 USD | 855,190.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 47,260,000.00 USD | 47,260,000.00 USD | 1,770,000.00 USD | 259,410.00 USD | 968,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 46,770,000.00 USD | 46,770,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 392,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 101,940.00 USD | 117,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 49,510,000.00 USD | 49,510,000.00 USD | 646,920.00 USD | 308,630.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 48,570,000.00 USD | 48,570,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 51,700,000.00 USD | 51,700,000.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 49,630,000.00 USD | 49,630,000.00 USD | 135,420.00 USD | 15,840.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 54,140,000.00 USD | 54,140,000.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 51,240,000.00 USD | 51,240,000.00 USD | 548,610.00 USD | 138,580.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 55,970,000.00 USD | 55,970,000.00 USD | 365,160.00 USD | 249,050.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 53,650,000.00 USD | 53,650,000.00 USD | 809,950.00 USD | 236,880.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 57,780,000.00 USD | 57,780,000.00 USD | 945,140.00 USD | 95,380.00 USD | 773,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 54,550,000.00 USD | 54,550,000.00 USD | 340,330.00 USD | 48,450.00 USD | 512,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 58,590.00 USD | 176,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 60,140,000.00 USD | 60,140,000.00 USD | 842,300.00 USD | 333,220.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 56,080,000.00 USD | 56,080,000.00 USD | 639,650.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 62,690,000.00 USD | 62,690,000.00 USD | 1,230,000.00 USD | 398,480.00 USD | 924,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 58,280,000.00 USD | 58,280,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 261,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 66,660,000.00 USD | 66,660,000.00 USD | 1,730,000.00 USD | 549,090.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 60,160,000.00 USD | 60,160,000.00 USD | 804,660.00 USD | 472,920.00 USD | 605,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 70,380,000.00 USD | 70,380,000.00 USD | 1,630,000.00 USD | 878,740.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 66,080,000.00 USD | 66,080,000.00 USD | 2,380,000.00 USD | 2,880,000.00 USD | 665,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 74,500,000.00 USD | 74,500,000.00 USD | 2,250,000.00 USD | 696,110.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 73,530,000.00 USD | 73,530,000.00 USD | 2,030,000.00 USD | 2,270,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 165,000.00 USD | 341,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 76,400,000.00 USD | 76,400,000.00 USD | 825,410.00 USD | 386,900.00 USD | 692,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 84,280,000.00 USD | 84,280,000.00 USD | 4,040,000.00 USD | 1,900,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 78,250,000.00 USD | 78,250,000.00 USD | 786,490.00 USD | 263,070.00 USD | 799,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 93,120,000.00 USD | 93,120,000.00 USD | 3,160,000.00 USD | 2,040,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 80,770,000.00 USD | 80,770,000.00 USD | 1,120,000.00 USD | 301,120.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 102,320,000.00 USD | 102,320,000.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 82,110,000.00 USD | 82,110,000.00 USD | 558,120.00 USD | 208,670.00 USD | 571,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 111,580,000.00 USD | 111,580,000.00 USD | 3,040,000.00 USD | 1,390,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 84,450,000.00 USD | 84,450,000.00 USD | 935,850.00 USD | 362,020.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 119,120,000.00 USD | 119,120,000.00 USD | 2,320,000.00 USD | 886,190.00 USD | 4,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 3,990.00 USD | 345,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 86,390,000.00 USD | 86,390,000.00 USD | 758,190.00 USD | 199,730.00 USD | 978,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 126,280,000.00 USD | 126,280,000.00 USD | 2,820,000.00 USD | 1,060,000.00 USD | 3,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 87,700,000.00 USD | 87,700,000.00 USD | 812,050.00 USD | 76,930.00 USD | 425,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 128,810,000.00 USD | 128,810,000.00 USD | 1,040,000.00 USD | 639,580.00 USD | 849,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 88,520,000.00 USD | 88,520,000.00 USD | 430,370.00 USD | 151,930.00 USD | 229,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 131,880,000.00 USD | 131,880,000.00 USD | 1,440,000.00 USD | 410,060.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 89,470,000.00 USD | 89,470,000.00 USD | 390,480.00 USD | 174,320.00 USD | 389,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 135,970,000.00 USD | 135,970,000.00 USD | 1,520,000.00 USD | 824,190.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 90,120,000.00 USD | 90,120,000.00 USD | 253,080.00 USD | 60,540.00 USD | 338,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 138,810,000.00 USD | 138,810,000.00 USD | 1,430,000.00 USD | 701,190.00 USD | 708,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 201,820.00 USD | 546,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 90,300,000.00 USD | 90,300,000.00 USD | 53,740.00 USD | 0.00 USD | 124,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 139,550,000.00 USD | 139,550,000.00 USD | 206,650.00 USD | 111,150.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 90,530,000.00 USD | 90,530,000.00 USD | 99,090.00 USD | 85,720.00 USD | 48,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 140,670,000.00 USD | 140,670,000.00 USD | 544,160.00 USD | 184,050.00 USD | 397,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 90,910,000.00 USD | 90,910,000.00 USD | 76,400.00 USD | 25,940.00 USD | 270,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 142,700,000.00 USD | 142,700,000.00 USD | 538,260.00 USD | 390,570.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 91,050,000.00 USD | 91,050,000.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 144,860,000.00 USD | 144,860,000.00 USD | 743,900.00 USD | 285,210.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 91,190,000.00 USD | 91,190,000.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 146,970,000.00 USD | 146,970,000.00 USD | 737,410.00 USD | 437,690.00 USD | 940,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 91,450,000.00 USD | 91,450,000.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 148,640,000.00 USD | 148,640,000.00 USD | 450,750.00 USD | 380,930.00 USD | 841,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 91,960,000.00 USD | 91,960,000.00 USD | 231,710.00 USD | 73,260.00 USD | 203,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 150,190,000.00 USD | 150,190,000.00 USD | 878,240.00 USD | 363,870.00 USD | 308,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 92,730,000.00 USD | 92,730,000.00 USD | 379,220.00 USD | 101,680.00 USD | 292,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 152,240,000.00 USD | 152,240,000.00 USD | 506,860.00 USD | 199,720.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 93,060,000.00 USD | 93,060,000.00 USD | 165,220.00 USD | 53,840.00 USD | 115,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 154,510,000.00 USD | 154,510,000.00 USD | 841,840.00 USD | 445,210.00 USD | 985,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 93,480,000.00 USD | 93,480,000.00 USD | 340,420.00 USD | 17,520.00 USD | 56,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 155,210,000.00 USD | 155,210,000.00 USD | 403,730.00 USD | 160,810.00 USD | 129,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 31,650.00 USD | 578,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 93,670,000.00 USD | 93,670,000.00 USD | 81,750.00 USD | 52,380.00 USD | 56,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 156,120,000.00 USD | 156,120,000.00 USD | 377,810.00 USD | 134,820.00 USD | 406,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 93,820,000.00 USD | 93,820,000.00 USD | 83,870.00 USD | 35,460.00 USD | 36,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 156,990,000.00 USD | 156,990,000.00 USD | 384,080.00 USD | 263,660.00 USD | 218,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 94,080,000.00 USD | 94,080,000.00 USD | 86,460.00 USD | 17,040.00 USD | 153,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 157,730,000.00 USD | 157,730,000.00 USD | 497,500.00 USD | 118,700.00 USD | 118,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 158,050,000.00 USD | 158,050,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 94,100,000.00 USD | 94,100,000.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 158,110,000.00 USD | 158,110,000.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 11,960.00 USD | 590,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.40` | 94,200,000.00 USD | 94,200,000.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 158,210,000.00 USD | 158,210,000.00 USD | 82,090.00 USD | 0.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 158,220,000.00 USD | 158,220,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 158,280,000.00 USD | 158,280,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 158,360,000.00 USD | 158,360,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 158,650,000.00 USD | 158,650,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 2,610.00 USD | 593,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 158,810,000.00 USD | 158,810,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 94,270,000.00 USD | 94,270,000.00 USD | 1,390.00 USD | 149.67 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 158,970,000.00 USD | 158,970,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 94,430,000.00 USD | 94,430,000.00 USD | 48,490.00 USD | 414.70 USD | 112,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 159,490,000.00 USD | 159,490,000.00 USD | 139,270.00 USD | 55,690.00 USD | 328,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 94,460,000.00 USD | 94,460,000.00 USD | 1,740.00 USD | 158.40 USD | 28,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 159,720,000.00 USD | 159,720,000.00 USD | 39,530.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 94,470,000.00 USD | 94,470,000.00 USD | 4,630.00 USD | 237.30 USD | 204.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 160,020,000.00 USD | 160,020,000.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 596,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.42` | 94,580,000.00 USD | 94,580,000.00 USD | 61,830.00 USD | 27,040.00 USD | 27,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 160,480,000.00 USD | 160,480,000.00 USD | 174,510.00 USD | 51,350.00 USD | 237,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 94,960,000.00 USD | 94,960,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 161,220,000.00 USD | 161,220,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 95,700,000.00 USD | 95,700,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 162,260,000.00 USD | 162,260,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 96,130,000.00 USD | 96,130,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 163,600,000.00 USD | 163,600,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 96,220,000.00 USD | 96,220,000.00 USD | 9,670.00 USD | 55,100.00 USD | 21,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 163,790,000.00 USD | 163,790,000.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 96,220.00 USD | 693,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.43` | 96,460,000.00 USD | 96,460,000.00 USD | 113,650.00 USD | 38,740.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 164,560,000.00 USD | 164,560,000.00 USD | 151,730.00 USD | 92,020.00 USD | 521,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 96,640,000.00 USD | 96,640,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 165,630,000.00 USD | 165,630,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 96,810,000.00 USD | 96,810,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 167,660,000.00 USD | 167,660,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 97,000,000.00 USD | 97,000,000.00 USD | 18,490.00 USD | 28,360.00 USD | 151,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 168,510,000.00 USD | 168,510,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 169,400,000.00 USD | 169,400,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 32,780.00 USD | 725,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 169,430,000.00 USD | 169,430,000.00 USD | 6,560.00 USD | 12,030.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 170,050,000.00 USD | 170,050,000.00 USD | 175,290.00 USD | 83,590.00 USD | 366,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 170,570,000.00 USD | 170,570,000.00 USD | 85,020.00 USD | 74,230.00 USD | 358,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 171,230,000.00 USD | 171,230,000.00 USD | 270,280.00 USD | 180,410.00 USD | 209,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 171,470,000.00 USD | 171,470,000.00 USD | 78,320.00 USD | 47,010.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 143,010.00 USD | 868,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.45` | 171,570,000.00 USD | 171,570,000.00 USD | 50,420.00 USD | 39,100.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 172,030,000.00 USD | 172,030,000.00 USD | 69,200.00 USD | 27,700.00 USD | 365,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 172,220,000.00 USD | 172,220,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 173,120,000.00 USD | 173,120,000.00 USD | 216,330.00 USD | 94,590.00 USD | 598,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 173,660,000.00 USD | 173,660,000.00 USD | 176,550.00 USD | 81,140.00 USD | 274,660.00 USD | `Tier 1 CEX` |
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
| `7D` | `1.15` | 191,160,000.00 USD | 0.00 USD | 191,160,000.00 USD | 237,280.00 USD | 98,230.00 USD | 109,530.00 USD |
| `7D` | `1.15` | 190,710,000.00 USD | 0.00 USD | 190,710,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.15` | 66,270,000.00 USD | 0.00 USD | 66,270,000.00 USD | 1,390.00 USD | 149.67 USD | 64,030.00 USD |
| `7D` | `1.15` | 190,560,000.00 USD | 0.00 USD | 190,560,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 66,200,000.00 USD | 0.00 USD | 66,200,000.00 USD | 48,490.00 USD | 414.70 USD | 112,380.00 USD |
| `7D` | `1.15` | 190,390,000.00 USD | 0.00 USD | 190,390,000.00 USD | 139,270.00 USD | 55,690.00 USD | 328,550.00 USD |
| `1D` | `1.16` | 66,040,000.00 USD | 0.00 USD | 66,040,000.00 USD | 1,740.00 USD | 158.40 USD | 28,820.00 USD |
| `7D` | `1.16` | 189,870,000.00 USD | 0.00 USD | 189,870,000.00 USD | 39,530.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 66,010,000.00 USD | 0.00 USD | 66,010,000.00 USD | 66,460.00 USD | 27,280.00 USD | 27,240.00 USD |
| `7D` | `1.16` | 189,650,000.00 USD | 0.00 USD | 189,650,000.00 USD | 258,370.00 USD | 96,700.00 USD | 406,460.00 USD |
| `1D` | `1.16` | 65,890,000.00 USD | 0.00 USD | 65,890,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.16` | 188,880,000.00 USD | 0.00 USD | 188,880,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 65,510,000.00 USD | 0.00 USD | 65,510,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.16` | 188,150,000.00 USD | 0.00 USD | 188,150,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD |
| `1D` | `1.16` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.16` | 187,100,000.00 USD | 0.00 USD | 187,100,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD |
| `1D` | `1.17` | 64,340,000.00 USD | 0.00 USD | 64,340,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD |
| `7D` | `1.17` | 185,760,000.00 USD | 0.00 USD | 185,760,000.00 USD | 218,150.00 USD | 212,700.00 USD | 529,730.00 USD |
| `1D` | `1.17` | 64,010,000.00 USD | 0.00 USD | 64,010,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.17` | 184,800,000.00 USD | 0.00 USD | 184,800,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 63,830,000.00 USD | 0.00 USD | 63,830,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.17` | 183,730,000.00 USD | 0.00 USD | 183,730,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 63,670,000.00 USD | 0.00 USD | 63,670,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.17` | 181,710,000.00 USD | 0.00 USD | 181,710,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD |
| `1D` | `1.17` | 63,450,000.00 USD | 0.00 USD | 63,450,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.17` | 180,850,000.00 USD | 0.00 USD | 180,850,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD |
| `1D` | `1.18` | 63,170,000.00 USD | 0.00 USD | 63,170,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD |
| `7D` | `1.18` | 179,970,000.00 USD | 0.00 USD | 179,970,000.00 USD | 181,850.00 USD | 95,620.00 USD | 377,590.00 USD |
| `1D` | `1.18` | 62,950,000.00 USD | 0.00 USD | 62,950,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.18` | 179,310,000.00 USD | 0.00 USD | 179,310,000.00 USD | 85,020.00 USD | 74,230.00 USD | 358,360.00 USD |
| `1D` | `1.18` | 62,780,000.00 USD | 0.00 USD | 62,780,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.18` | 178,790,000.00 USD | 0.00 USD | 178,790,000.00 USD | 270,280.00 USD | 180,410.00 USD | 209,010.00 USD |
| `1D` | `1.18` | 62,700,000.00 USD | 0.00 USD | 62,700,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.18` | 178,130,000.00 USD | 0.00 USD | 178,130,000.00 USD | 78,320.00 USD | 47,010.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 62,610,000.00 USD | 0.00 USD | 62,610,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD |
| `7D` | `1.18` | 177,890,000.00 USD | 0.00 USD | 177,890,000.00 USD | 119,620.00 USD | 66,800.00 USD | 377,200.00 USD |
| `1D` | `1.19` | 62,500,000.00 USD | 0.00 USD | 62,500,000.00 USD | 694.57 USD | 23,390.00 USD | 20,370.00 USD |
| `7D` | `1.19` | 177,330,000.00 USD | 0.00 USD | 177,330,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD |
| `1D` | `1.19` | 62,450,000.00 USD | 0.00 USD | 62,450,000.00 USD | 30,140.00 USD | 99.63 USD | 12,880.00 USD |
| `7D` | `1.19` | 177,150,000.00 USD | 0.00 USD | 177,150,000.00 USD | 216,330.00 USD | 94,590.00 USD | 606,740.00 USD |
| `1D` | `1.19` | 62,410,000.00 USD | 0.00 USD | 62,410,000.00 USD | 10,800.00 USD | 238.88 USD | 21,580.00 USD |
| `7D` | `1.19` | 176,230,000.00 USD | 0.00 USD | 176,230,000.00 USD | 211,840.00 USD | 81,140.00 USD | 281,100.00 USD |
| `1D` | `1.19` | 62,380,000.00 USD | 0.00 USD | 62,380,000.00 USD | 20,520.00 USD | 18,150.00 USD | 56,850.00 USD |
| `7D` | `1.19` | 175,660,000.00 USD | 0.00 USD | 175,660,000.00 USD | 149,990.00 USD | 95,880.00 USD | 123,730.00 USD |
| `1D` | `1.19` | 62,280,000.00 USD | 0.00 USD | 62,280,000.00 USD | 130,470.00 USD | 44,250.00 USD | 112,000.00 USD |
| `7D` | `1.19` | 175,290,000.00 USD | 0.00 USD | 175,290,000.00 USD | 219,860.00 USD | 72,930.00 USD | 465,100.00 USD |
| `1D` | `1.20` | 62,000,000.00 USD | 0.00 USD | 62,000,000.00 USD | 64,240.00 USD | 18,340.00 USD | 29,820.00 USD |
| `7D` | `1.20` | 174,530,000.00 USD | 0.00 USD | 174,530,000.00 USD | 251,760.00 USD | 140,610.00 USD | 318,640.00 USD |
| `1D` | `1.20` | 61,880,000.00 USD | 0.00 USD | 61,880,000.00 USD | 112,660.00 USD | 7,010.00 USD | 10,750.00 USD |
| `7D` | `1.20` | 173,820,000.00 USD | 0.00 USD | 173,820,000.00 USD | 5,350.00 USD | 38,700.00 USD | 18,810.00 USD |
| `1D` | `1.20` | 61,750,000.00 USD | 0.00 USD | 61,750,000.00 USD | 26,800.00 USD | 20,630.00 USD | 1,060.00 USD |
| `7D` | `1.20` | 173,750,000.00 USD | 0.00 USD | 173,750,000.00 USD | 72,960.00 USD | 36,750.00 USD | 18,590.00 USD |
| `1D` | `1.20` | 61,710,000.00 USD | 0.00 USD | 61,710,000.00 USD | 55,140.00 USD | 14,180.00 USD | 61,870.00 USD |
| `7D` | `1.20` | 173,630,000.00 USD | 0.00 USD | 173,630,000.00 USD | 184,030.00 USD | 62,270.00 USD | 57,310.00 USD |
| `7D` | `1.20` | 173,320,000.00 USD | 0.00 USD | 173,320,000.00 USD | 47,500.00 USD | 29,680.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 61,570,000.00 USD | 0.00 USD | 61,570,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD |
| `7D` | `1.21` | 173,170,000.00 USD | 0.00 USD | 173,170,000.00 USD | 13,620.00 USD | 3,030.00 USD | 0.00 USD |
| `1D` | `1.21` | 61,560,000.00 USD | 0.00 USD | 61,560,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `1.21` | 173,150,000.00 USD | 0.00 USD | 173,150,000.00 USD | 241,190.00 USD | 2,360.00 USD | 22,480.00 USD |
| `7D` | `1.21` | 172,880,000.00 USD | 0.00 USD | 172,880,000.00 USD | 257,960.00 USD | 89,570.00 USD | 624,140.00 USD |
| `7D` | `1.21` | 171,910,000.00 USD | 0.00 USD | 171,910,000.00 USD | 199,450.00 USD | 109,690.00 USD | 212,340.00 USD |
| `7D` | `1.21` | 171,390,000.00 USD | 0.00 USD | 171,390,000.00 USD | 84,480.00 USD | 89,180.00 USD | 0.00 USD |
| `7D` | `1.22` | 171,220,000.00 USD | 0.00 USD | 171,220,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.22` | 171,120,000.00 USD | 0.00 USD | 171,120,000.00 USD | 0.00 USD | 0.00 USD | 27,810.00 USD |
| `7D` | `1.22` | 171,090,000.00 USD | 0.00 USD | 171,090,000.00 USD | 0.00 USD | 2,640.00 USD | 19,450.00 USD |
| `7D` | `1.22` | 171,070,000.00 USD | 0.00 USD | 171,070,000.00 USD | 59,120.00 USD | 2,680.00 USD | 159,270.00 USD |
| `7D` | `1.22` | 170,850,000.00 USD | 0.00 USD | 170,850,000.00 USD | 251,420.00 USD | 302,320.00 USD | 112,000.00 USD |
| `7D` | `1.23` | 170,180,000.00 USD | 0.00 USD | 170,180,000.00 USD | 492,660.00 USD | 141,800.00 USD | 153,930.00 USD |
| `1D` | `1.23` | 61,530,000.00 USD | 0.00 USD | 61,530,000.00 USD | 48,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.23` | 169,390,000.00 USD | 0.00 USD | 169,390,000.00 USD | 269,210.00 USD | 135,700.00 USD | 277,210.00 USD |
| `1D` | `1.23` | 61,480,000.00 USD | 0.00 USD | 61,480,000.00 USD | 102,730.00 USD | 374.17 USD | 215,900.00 USD |
| `7D` | `1.23` | 168,710,000.00 USD | 0.00 USD | 168,710,000.00 USD | 235,350.00 USD | 112,100.00 USD | 795,530.00 USD |
| `1D` | `1.23` | 61,170,000.00 USD | 0.00 USD | 61,170,000.00 USD | 125,570.00 USD | 1,040.00 USD | 280,940.00 USD |
| `7D` | `1.23` | 167,570,000.00 USD | 0.00 USD | 167,570,000.00 USD | 596,400.00 USD | 225,830.00 USD | 410,120.00 USD |
| `1D` | `1.23` | 60,760,000.00 USD | 0.00 USD | 60,760,000.00 USD | 11,570.00 USD | 989.25 USD | 73,470.00 USD |
| `7D` | `1.23` | 166,340,000.00 USD | 0.00 USD | 166,340,000.00 USD | 1,120,000.00 USD | 364,060.00 USD | 1,540,000.00 USD |
| `1D` | `1.24` | 60,670,000.00 USD | 0.00 USD | 60,670,000.00 USD | 515,840.00 USD | 120,320.00 USD | 331,740.00 USD |
| `7D` | `1.24` | 163,310,000.00 USD | 0.00 USD | 163,310,000.00 USD | 1,120,000.00 USD | 760,590.00 USD | 2,370,000.00 USD |
| `1D` | `1.24` | 59,700,000.00 USD | 0.00 USD | 59,700,000.00 USD | 1,080,000.00 USD | 666,380.00 USD | 709,340.00 USD |
| `7D` | `1.24` | 159,060,000.00 USD | 0.00 USD | 159,060,000.00 USD | 1,960,000.00 USD | 859,010.00 USD | 2,090,000.00 USD |
| `1D` | `1.24` | 57,240,000.00 USD | 0.00 USD | 57,240,000.00 USD | 942,890.00 USD | 493,310.00 USD | 740,300.00 USD |
| `7D` | `1.24` | 154,160,000.00 USD | 0.00 USD | 154,160,000.00 USD | 2,210,000.00 USD | 1,010,000.00 USD | 2,700,000.00 USD |
| `1D` | `1.24` | 55,070,000.00 USD | 0.00 USD | 55,070,000.00 USD | 347,740.00 USD | 188,510.00 USD | 341,680.00 USD |
| `7D` | `1.24` | 148,240,000.00 USD | 0.00 USD | 148,240,000.00 USD | 1,210,000.00 USD | 569,760.00 USD | 1,260,000.00 USD |
| `1D` | `1.24` | 54,190,000.00 USD | 0.00 USD | 54,190,000.00 USD | 372,570.00 USD | 122,390.00 USD | 516,600.00 USD |
| `7D` | `1.24` | 145,190,000.00 USD | 0.00 USD | 145,190,000.00 USD | 1,020,000.00 USD | 537,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.25` | 53,180,000.00 USD | 0.00 USD | 53,180,000.00 USD | 546,010.00 USD | 129,710.00 USD | 161,620.00 USD |
| `7D` | `1.25` | 141,960,000.00 USD | 0.00 USD | 141,960,000.00 USD | 2,520,000.00 USD | 695,090.00 USD | 3,060,000.00 USD |
| `1D` | `1.25` | 52,340,000.00 USD | 0.00 USD | 52,340,000.00 USD | 218,430.00 USD | 101,390.00 USD | 355,010.00 USD |
| `7D` | `1.25` | 135,690,000.00 USD | 0.00 USD | 135,690,000.00 USD | 2,150,000.00 USD | 1,450,000.00 USD | 5,850,000.00 USD |
| `1D` | `1.25` | 51,670,000.00 USD | 0.00 USD | 51,670,000.00 USD | 177,400.00 USD | 102,610.00 USD | 457,850.00 USD |
| `7D` | `1.25` | 126,240,000.00 USD | 0.00 USD | 126,240,000.00 USD | 3,090,000.00 USD | 1,160,000.00 USD | 2,170,000.00 USD |
| `1D` | `1.25` | 50,930,000.00 USD | 0.00 USD | 50,930,000.00 USD | 351,630.00 USD | 92,050.00 USD | 426,530.00 USD |
| `7D` | `1.25` | 119,830,000.00 USD | 0.00 USD | 119,830,000.00 USD | 2,140,000.00 USD | 783,920.00 USD | 1,440,000.00 USD |
| `1D` | `1.25` | 50,060,000.00 USD | 0.00 USD | 50,060,000.00 USD | 332,170.00 USD | 42,640.00 USD | 632,330.00 USD |
| `7D` | `1.25` | 115,470,000.00 USD | 0.00 USD | 115,470,000.00 USD | 262,320.00 USD | 552,710.00 USD | 814,990.00 USD |
| `1D` | `1.26` | 49,050,000.00 USD | 0.00 USD | 49,050,000.00 USD | 610,960.00 USD | 49,250.00 USD | 790,470.00 USD |
| `7D` | `1.26` | 113,840,000.00 USD | 0.00 USD | 113,840,000.00 USD | 1,170,000.00 USD | 588,800.00 USD | 1,880,000.00 USD |
| `1D` | `1.26` | 47,600,000.00 USD | 0.00 USD | 47,600,000.00 USD | 231,420.00 USD | 104,190.00 USD | 463,780.00 USD |
| `7D` | `1.26` | 110,210,000.00 USD | 0.00 USD | 110,210,000.00 USD | 1,020,000.00 USD | 211,890.00 USD | 1,000,000.00 USD |
| `1D` | `1.26` | 46,800,000.00 USD | 0.00 USD | 46,800,000.00 USD | 281,000.00 USD | 71,910.00 USD | 171,240.00 USD |
| `7D` | `1.26` | 107,980,000.00 USD | 0.00 USD | 107,980,000.00 USD | 1,220,000.00 USD | 691,780.00 USD | 1,580,000.00 USD |
| `1D` | `1.26` | 46,280,000.00 USD | 0.00 USD | 46,280,000.00 USD | 992,410.00 USD | 254,090.00 USD | 693,350.00 USD |
| `7D` | `1.26` | 104,490,000.00 USD | 0.00 USD | 104,490,000.00 USD | 1,980,000.00 USD | 1,450,000.00 USD | 1,040,000.00 USD |
| `1D` | `1.26` | 44,340,000.00 USD | 0.00 USD | 44,340,000.00 USD | 2,210,000.00 USD | 1,360,000.00 USD | 1,530,000.00 USD |
| `7D` | `1.26` | 100,020,000.00 USD | 0.00 USD | 100,020,000.00 USD | 3,500,000.00 USD | 1,970,000.00 USD | 3,520,000.00 USD |
| `1D` | `1.27` | 39,240,000.00 USD | 0.00 USD | 39,240,000.00 USD | 2,080,000.00 USD | 1,030,000.00 USD | 1,570,000.00 USD |
| `7D` | `1.27` | 91,030,000.00 USD | 0.00 USD | 91,030,000.00 USD | 4,470,000.00 USD | 1,960,000.00 USD | 6,550,000.00 USD |
| `1D` | `1.27` | 34,550,000.00 USD | 0.00 USD | 34,550,000.00 USD | 1,160,000.00 USD | 377,270.00 USD | 1,610,000.00 USD |
| `7D` | `1.27` | 78,050,000.00 USD | 0.00 USD | 78,050,000.00 USD | 2,890,000.00 USD | 1,380,000.00 USD | 4,100,000.00 USD |
| `1D` | `1.27` | 31,400,000.00 USD | 0.00 USD | 31,400,000.00 USD | 1,330,000.00 USD | 277,410.00 USD | 2,270,000.00 USD |
| `7D` | `1.27` | 69,680,000.00 USD | 0.00 USD | 69,680,000.00 USD | 2,710,000.00 USD | 1,640,000.00 USD | 4,340,000.00 USD |
| `1D` | `1.27` | 27,520,000.00 USD | 0.00 USD | 27,520,000.00 USD | 1,320,000.00 USD | 332,670.00 USD | 815,330.00 USD |
| `7D` | `1.27` | 60,990,000.00 USD | 0.00 USD | 60,990,000.00 USD | 4,570,000.00 USD | 2,590,000.00 USD | 7,120,000.00 USD |
| `1D` | `1.27` | 25,050,000.00 USD | 0.00 USD | 25,050,000.00 USD | 1,460,000.00 USD | 568,780.00 USD | 1,290,000.00 USD |
| `7D` | `1.27` | 46,700,000.00 USD | 0.00 USD | 46,700,000.00 USD | 4,600,000.00 USD | 1,720,000.00 USD | 10,570,000.00 USD |
| `1D` | `1.28` | 21,740,000.00 USD | 0.00 USD | 21,740,000.00 USD | 2,960,000.00 USD | 1,280,000.00 USD | 2,560,000.00 USD |
| `7D` | `1.28` | 29,820,000.00 USD | 0.00 USD | 29,820,000.00 USD | 4,130,000.00 USD | 2,410,000.00 USD | 5,940,000.00 USD |
| `1D` | `1.28` | 14,930,000.00 USD | 0.00 USD | 14,930,000.00 USD | 6,210,000.00 USD | 2,740,000.00 USD | 4,520,000.00 USD |
| `7D` | `1.28` | 17,330,000.00 USD | 0.00 USD | 17,330,000.00 USD | 7,720,000.00 USD | 2,860,000.00 USD | 5,150,000.00 USD |
| `1D` | `1.28` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD |
| `7D` | `1.28` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 0.00 USD | 1,420,000.00 USD | 84,070.00 USD |
| `1D` | `1.28` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD |
| `1D` | `1.28` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD |
| `7D` | `1.28` | 108,100.00 USD | 0.00 USD | 108,100.00 USD | 0.00 USD | 22,110.00 USD | 85,990.00 USD |
| `7D` | `1.28` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.28` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 2,480,000.00 USD | 530,190.00 USD | 0.00 USD |
| `7D` | `1.28` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 4,990,000.00 USD | 1,420,000.00 USD | 123,100.00 USD |
| `1D` | `1.29` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 1,390,000.00 USD | 327,360.00 USD | 0.00 USD |
| `7D` | `1.29` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 505,690.00 USD | 888,530.00 USD | 8,110.00 USD |
| `1D` | `1.29` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 221,930.00 USD | 100,470.00 USD | 8,840.00 USD |
| `7D` | `1.29` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 440,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.29` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,140,000.00 USD |
| `1D` | `1.29` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 194,230.00 USD | 0.00 USD | 1,220,000.00 USD |
| `7D` | `1.29` | 11,190,000.00 USD | 11,190,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 648,390.00 USD |
| `1D` | `1.29` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 389,390.00 USD | 0.00 USD | 1,100,000.00 USD |
| `7D` | `1.29` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 1,680,000.00 USD |
| `1D` | `1.30` | 12,250,000.00 USD | 12,250,000.00 USD | 0.00 USD | 484,930.00 USD | 597,860.00 USD | 1,110,000.00 USD |
| `7D` | `1.30` | 16,240,000.00 USD | 16,240,000.00 USD | 0.00 USD | 393,030.00 USD | 573,900.00 USD | 1,300,000.00 USD |
| `1D` | `1.30` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 288,210.00 USD |
| `7D` | `1.30` | 17,490,000.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `1.30` | 12,710,000.00 USD | 12,710,000.00 USD | 0.00 USD | 0.00 USD | 168,250.00 USD | 0.00 USD |
| `1D` | `1.30` | 14,420,000.00 USD | 14,420,000.00 USD | 0.00 USD | 521,850.00 USD | 910,560.00 USD | 278,310.00 USD |
| `7D` | `1.30` | 18,350,000.00 USD | 18,350,000.00 USD | 0.00 USD | 0.00 USD | 859,020.00 USD | 0.00 USD |
| `1D` | `1.30` | 14,830,000.00 USD | 14,830,000.00 USD | 0.00 USD | 188,510.00 USD | 98,100.00 USD | 127,330.00 USD |
| `7D` | `1.30` | 20,290,000.00 USD | 20,290,000.00 USD | 0.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD |
| `1D` | `1.31` | 15,960,000.00 USD | 15,960,000.00 USD | 0.00 USD | 493,480.00 USD | 319,190.00 USD | 320,170.00 USD |
| `7D` | `1.31` | 22,240,000.00 USD | 22,240,000.00 USD | 0.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD |
| `1D` | `1.31` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 455,910.00 USD | 3,540.00 USD | 776,190.00 USD |
| `7D` | `1.31` | 24,190,000.00 USD | 24,190,000.00 USD | 0.00 USD | 530,610.00 USD | 92,270.00 USD | 1,330,000.00 USD |
| `1D` | `1.31` | 19,040,000.00 USD | 19,040,000.00 USD | 0.00 USD | 616,030.00 USD | 287,750.00 USD | 940,430.00 USD |
| `7D` | `1.31` | 25,900,000.00 USD | 25,900,000.00 USD | 0.00 USD | 1,290,000.00 USD | 0.00 USD | 415,410.00 USD |
| `1D` | `1.31` | 21,740,000.00 USD | 21,740,000.00 USD | 0.00 USD | 1,570,000.00 USD | 443,660.00 USD | 688,860.00 USD |
| `7D` | `1.31` | 29,660,000.00 USD | 29,660,000.00 USD | 0.00 USD | 79,920.00 USD | 747,120.00 USD | 2,930,000.00 USD |
| `1D` | `1.31` | 23,010,000.00 USD | 23,010,000.00 USD | 0.00 USD | 464,990.00 USD | 483,320.00 USD | 321,130.00 USD |
| `7D` | `1.31` | 30,320,000.00 USD | 30,320,000.00 USD | 0.00 USD | 515,950.00 USD | 149,950.00 USD | 0.00 USD |
| `1D` | `1.32` | 29,230,000.00 USD | 29,230,000.00 USD | 0.00 USD | 213,000.00 USD | 1,830,000.00 USD | 4,170,000.00 USD |
| `7D` | `1.32` | 34,500,000.00 USD | 34,500,000.00 USD | 0.00 USD | 44,360.00 USD | 1,750,000.00 USD | 2,380,000.00 USD |
| `1D` | `1.32` | 36,210,000.00 USD | 36,210,000.00 USD | 0.00 USD | 2,340,000.00 USD | 1,060,000.00 USD | 3,590,000.00 USD |
| `7D` | `1.32` | 39,350,000.00 USD | 39,350,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD |
| `1D` | `1.32` | 39,740,000.00 USD | 39,740,000.00 USD | 0.00 USD | 1,720,000.00 USD | 742,480.00 USD | 1,060,000.00 USD |
| `7D` | `1.32` | 41,050,000.00 USD | 41,050,000.00 USD | 0.00 USD | 823,190.00 USD | 430,400.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 44,260,000.00 USD | 44,260,000.00 USD | 0.00 USD | 1,830,000.00 USD | 981,550.00 USD | 1,710,000.00 USD |
| `7D` | `1.32` | 44,150,000.00 USD | 44,150,000.00 USD | 0.00 USD | 1,090,000.00 USD | 855,190.00 USD | 1,140,000.00 USD |
| `1D` | `1.32` | 47,260,000.00 USD | 47,260,000.00 USD | 0.00 USD | 1,770,000.00 USD | 259,410.00 USD | 968,180.00 USD |
| `7D` | `1.32` | 46,770,000.00 USD | 46,770,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 392,360.00 USD |
| `1D` | `1.33` | 49,510,000.00 USD | 49,510,000.00 USD | 0.00 USD | 646,920.00 USD | 308,630.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 48,570,000.00 USD | 48,570,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 51,700,000.00 USD | 51,700,000.00 USD | 0.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD |
| `7D` | `1.33` | 49,630,000.00 USD | 49,630,000.00 USD | 0.00 USD | 135,420.00 USD | 15,840.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 54,140,000.00 USD | 54,140,000.00 USD | 0.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 51,240,000.00 USD | 51,240,000.00 USD | 0.00 USD | 548,610.00 USD | 138,580.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 55,970,000.00 USD | 55,970,000.00 USD | 0.00 USD | 365,160.00 USD | 249,050.00 USD | 1,220,000.00 USD |
| `7D` | `1.33` | 53,650,000.00 USD | 53,650,000.00 USD | 0.00 USD | 809,950.00 USD | 236,880.00 USD | 1,360,000.00 USD |
| `1D` | `1.33` | 57,780,000.00 USD | 57,780,000.00 USD | 0.00 USD | 945,140.00 USD | 95,380.00 USD | 773,790.00 USD |
| `7D` | `1.33` | 54,550,000.00 USD | 54,550,000.00 USD | 0.00 USD | 340,330.00 USD | 48,450.00 USD | 512,820.00 USD |
| `1D` | `1.34` | 60,140,000.00 USD | 60,140,000.00 USD | 0.00 USD | 842,300.00 USD | 333,220.00 USD | 1,180,000.00 USD |
| `7D` | `1.34` | 56,080,000.00 USD | 56,080,000.00 USD | 0.00 USD | 639,650.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 62,690,000.00 USD | 62,690,000.00 USD | 0.00 USD | 1,230,000.00 USD | 398,480.00 USD | 924,530.00 USD |
| `7D` | `1.34` | 58,280,000.00 USD | 58,280,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 261,320.00 USD |
| `1D` | `1.34` | 66,660,000.00 USD | 66,660,000.00 USD | 0.00 USD | 1,730,000.00 USD | 549,090.00 USD | 1,700,000.00 USD |
| `7D` | `1.34` | 60,160,000.00 USD | 60,160,000.00 USD | 0.00 USD | 804,660.00 USD | 472,920.00 USD | 605,360.00 USD |
| `1D` | `1.34` | 70,380,000.00 USD | 70,380,000.00 USD | 0.00 USD | 1,630,000.00 USD | 878,740.00 USD | 1,200,000.00 USD |
| `7D` | `1.34` | 66,080,000.00 USD | 66,080,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,880,000.00 USD | 665,920.00 USD |
| `1D` | `1.34` | 74,500,000.00 USD | 74,500,000.00 USD | 0.00 USD | 2,250,000.00 USD | 696,110.00 USD | 1,170,000.00 USD |
| `7D` | `1.34` | 73,530,000.00 USD | 73,530,000.00 USD | 0.00 USD | 2,030,000.00 USD | 2,270,000.00 USD | 3,140,000.00 USD |
| `1D` | `1.35` | 76,400,000.00 USD | 76,400,000.00 USD | 0.00 USD | 825,410.00 USD | 386,900.00 USD | 692,690.00 USD |
| `7D` | `1.35` | 84,280,000.00 USD | 84,280,000.00 USD | 0.00 USD | 4,040,000.00 USD | 1,900,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 78,250,000.00 USD | 78,250,000.00 USD | 0.00 USD | 786,490.00 USD | 263,070.00 USD | 799,350.00 USD |
| `7D` | `1.35` | 93,120,000.00 USD | 93,120,000.00 USD | 0.00 USD | 3,160,000.00 USD | 2,040,000.00 USD | 3,640,000.00 USD |
| `1D` | `1.35` | 80,770,000.00 USD | 80,770,000.00 USD | 0.00 USD | 1,120,000.00 USD | 301,120.00 USD | 1,100,000.00 USD |
| `7D` | `1.35` | 102,320,000.00 USD | 102,320,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 3,160,000.00 USD |
| `1D` | `1.35` | 82,110,000.00 USD | 82,110,000.00 USD | 0.00 USD | 558,120.00 USD | 208,670.00 USD | 571,840.00 USD |
| `7D` | `1.35` | 111,580,000.00 USD | 111,580,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,390,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 84,450,000.00 USD | 84,450,000.00 USD | 0.00 USD | 935,850.00 USD | 362,020.00 USD | 1,040,000.00 USD |
| `7D` | `1.35` | 119,120,000.00 USD | 119,120,000.00 USD | 0.00 USD | 2,320,000.00 USD | 886,190.00 USD | 4,330,000.00 USD |
| `1D` | `1.36` | 86,390,000.00 USD | 86,390,000.00 USD | 0.00 USD | 758,190.00 USD | 199,730.00 USD | 978,960.00 USD |
| `7D` | `1.36` | 126,280,000.00 USD | 126,280,000.00 USD | 0.00 USD | 2,820,000.00 USD | 1,060,000.00 USD | 3,290,000.00 USD |
| `1D` | `1.36` | 87,700,000.00 USD | 87,700,000.00 USD | 0.00 USD | 812,050.00 USD | 76,930.00 USD | 425,930.00 USD |
| `7D` | `1.36` | 128,810,000.00 USD | 128,810,000.00 USD | 0.00 USD | 1,040,000.00 USD | 639,580.00 USD | 849,400.00 USD |
| `1D` | `1.36` | 88,520,000.00 USD | 88,520,000.00 USD | 0.00 USD | 430,370.00 USD | 151,930.00 USD | 229,660.00 USD |
| `7D` | `1.36` | 131,880,000.00 USD | 131,880,000.00 USD | 0.00 USD | 1,440,000.00 USD | 410,060.00 USD | 1,230,000.00 USD |
| `1D` | `1.36` | 89,470,000.00 USD | 89,470,000.00 USD | 0.00 USD | 390,480.00 USD | 174,320.00 USD | 389,900.00 USD |
| `7D` | `1.36` | 135,970,000.00 USD | 135,970,000.00 USD | 0.00 USD | 1,520,000.00 USD | 824,190.00 USD | 1,740,000.00 USD |
| `1D` | `1.36` | 90,120,000.00 USD | 90,120,000.00 USD | 0.00 USD | 253,080.00 USD | 60,540.00 USD | 338,290.00 USD |
| `7D` | `1.36` | 138,810,000.00 USD | 138,810,000.00 USD | 0.00 USD | 1,430,000.00 USD | 701,190.00 USD | 708,120.00 USD |
| `1D` | `1.37` | 90,300,000.00 USD | 90,300,000.00 USD | 0.00 USD | 53,740.00 USD | 0.00 USD | 124,610.00 USD |
| `7D` | `1.37` | 139,550,000.00 USD | 139,550,000.00 USD | 0.00 USD | 206,650.00 USD | 111,150.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 90,530,000.00 USD | 90,530,000.00 USD | 0.00 USD | 99,090.00 USD | 85,720.00 USD | 48,400.00 USD |
| `7D` | `1.37` | 140,670,000.00 USD | 140,670,000.00 USD | 0.00 USD | 544,160.00 USD | 184,050.00 USD | 397,850.00 USD |
| `1D` | `1.37` | 90,910,000.00 USD | 90,910,000.00 USD | 0.00 USD | 76,400.00 USD | 25,940.00 USD | 270,940.00 USD |
| `7D` | `1.37` | 142,700,000.00 USD | 142,700,000.00 USD | 0.00 USD | 538,260.00 USD | 390,570.00 USD | 1,100,000.00 USD |
| `1D` | `1.37` | 91,050,000.00 USD | 91,050,000.00 USD | 0.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD |
| `7D` | `1.37` | 144,860,000.00 USD | 144,860,000.00 USD | 0.00 USD | 743,900.00 USD | 285,210.00 USD | 1,120,000.00 USD |
| `1D` | `1.37` | 91,190,000.00 USD | 91,190,000.00 USD | 0.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD |
| `7D` | `1.37` | 146,970,000.00 USD | 146,970,000.00 USD | 0.00 USD | 737,410.00 USD | 437,690.00 USD | 940,380.00 USD |
| `1D` | `1.38` | 91,450,000.00 USD | 91,450,000.00 USD | 0.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD |
| `7D` | `1.38` | 148,640,000.00 USD | 148,640,000.00 USD | 0.00 USD | 450,750.00 USD | 380,930.00 USD | 841,020.00 USD |
| `1D` | `1.38` | 91,960,000.00 USD | 91,960,000.00 USD | 0.00 USD | 231,710.00 USD | 73,260.00 USD | 203,900.00 USD |
| `7D` | `1.38` | 150,190,000.00 USD | 150,190,000.00 USD | 0.00 USD | 878,240.00 USD | 363,870.00 USD | 308,370.00 USD |
| `1D` | `1.38` | 92,730,000.00 USD | 92,730,000.00 USD | 0.00 USD | 379,220.00 USD | 101,680.00 USD | 292,290.00 USD |
| `7D` | `1.38` | 152,240,000.00 USD | 152,240,000.00 USD | 0.00 USD | 506,860.00 USD | 199,720.00 USD | 1,340,000.00 USD |
| `1D` | `1.38` | 93,060,000.00 USD | 93,060,000.00 USD | 0.00 USD | 165,220.00 USD | 53,840.00 USD | 115,580.00 USD |
| `7D` | `1.38` | 154,510,000.00 USD | 154,510,000.00 USD | 0.00 USD | 841,840.00 USD | 445,210.00 USD | 985,800.00 USD |
| `1D` | `1.38` | 93,480,000.00 USD | 93,480,000.00 USD | 0.00 USD | 340,420.00 USD | 17,520.00 USD | 56,890.00 USD |
| `7D` | `1.38` | 155,210,000.00 USD | 155,210,000.00 USD | 0.00 USD | 403,730.00 USD | 160,810.00 USD | 129,320.00 USD |
| `1D` | `1.39` | 93,670,000.00 USD | 93,670,000.00 USD | 0.00 USD | 81,750.00 USD | 52,380.00 USD | 56,350.00 USD |
| `7D` | `1.39` | 156,120,000.00 USD | 156,120,000.00 USD | 0.00 USD | 377,810.00 USD | 134,820.00 USD | 406,090.00 USD |
| `1D` | `1.39` | 93,820,000.00 USD | 93,820,000.00 USD | 0.00 USD | 83,870.00 USD | 35,460.00 USD | 36,020.00 USD |
| `7D` | `1.39` | 156,990,000.00 USD | 156,990,000.00 USD | 0.00 USD | 384,080.00 USD | 263,660.00 USD | 218,620.00 USD |
| `1D` | `1.39` | 94,080,000.00 USD | 94,080,000.00 USD | 0.00 USD | 86,460.00 USD | 17,040.00 USD | 153,570.00 USD |
| `7D` | `1.39` | 157,730,000.00 USD | 157,730,000.00 USD | 0.00 USD | 497,500.00 USD | 118,700.00 USD | 118,070.00 USD |
| `7D` | `1.39` | 158,050,000.00 USD | 158,050,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.39` | 94,100,000.00 USD | 94,100,000.00 USD | 0.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD |
| `7D` | `1.39` | 158,110,000.00 USD | 158,110,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 94,200,000.00 USD | 94,200,000.00 USD | 0.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `1.40` | 158,210,000.00 USD | 158,210,000.00 USD | 0.00 USD | 82,090.00 USD | 0.00 USD | 11,130.00 USD |
| `7D` | `1.40` | 158,220,000.00 USD | 158,220,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 158,280,000.00 USD | 158,280,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 158,360,000.00 USD | 158,360,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `7D` | `1.40` | 158,650,000.00 USD | 158,650,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 158,810,000.00 USD | 158,810,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.41` | 94,270,000.00 USD | 94,270,000.00 USD | 0.00 USD | 1,390.00 USD | 149.67 USD | 64,030.00 USD |
| `7D` | `1.41` | 158,970,000.00 USD | 158,970,000.00 USD | 0.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.41` | 94,430,000.00 USD | 94,430,000.00 USD | 0.00 USD | 48,490.00 USD | 414.70 USD | 112,380.00 USD |
| `7D` | `1.41` | 159,490,000.00 USD | 159,490,000.00 USD | 0.00 USD | 139,270.00 USD | 55,690.00 USD | 328,550.00 USD |
| `1D` | `1.41` | 94,460,000.00 USD | 94,460,000.00 USD | 0.00 USD | 1,740.00 USD | 158.40 USD | 28,820.00 USD |
| `7D` | `1.41` | 159,720,000.00 USD | 159,720,000.00 USD | 0.00 USD | 39,530.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.41` | 94,470,000.00 USD | 94,470,000.00 USD | 0.00 USD | 4,630.00 USD | 237.30 USD | 204.46 USD |
| `7D` | `1.41` | 160,020,000.00 USD | 160,020,000.00 USD | 0.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD |
| `1D` | `1.42` | 94,580,000.00 USD | 94,580,000.00 USD | 0.00 USD | 61,830.00 USD | 27,040.00 USD | 27,040.00 USD |
| `7D` | `1.42` | 160,480,000.00 USD | 160,480,000.00 USD | 0.00 USD | 174,510.00 USD | 51,350.00 USD | 237,640.00 USD |
| `1D` | `1.42` | 94,960,000.00 USD | 94,960,000.00 USD | 0.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.42` | 161,220,000.00 USD | 161,220,000.00 USD | 0.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD |
| `1D` | `1.42` | 95,700,000.00 USD | 95,700,000.00 USD | 0.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.42` | 162,260,000.00 USD | 162,260,000.00 USD | 0.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD |
| `1D` | `1.42` | 96,130,000.00 USD | 96,130,000.00 USD | 0.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.42` | 163,600,000.00 USD | 163,600,000.00 USD | 0.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD |
| `1D` | `1.42` | 96,220,000.00 USD | 96,220,000.00 USD | 0.00 USD | 9,670.00 USD | 55,100.00 USD | 21,210.00 USD |
| `7D` | `1.42` | 163,790,000.00 USD | 163,790,000.00 USD | 0.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD |
| `1D` | `1.43` | 96,460,000.00 USD | 96,460,000.00 USD | 0.00 USD | 113,650.00 USD | 38,740.00 USD | 90,040.00 USD |
| `7D` | `1.43` | 164,560,000.00 USD | 164,560,000.00 USD | 0.00 USD | 151,730.00 USD | 92,020.00 USD | 521,950.00 USD |
| `1D` | `1.43` | 96,640,000.00 USD | 96,640,000.00 USD | 0.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.43` | 165,630,000.00 USD | 165,630,000.00 USD | 0.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.43` | 96,810,000.00 USD | 96,810,000.00 USD | 0.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.43` | 167,660,000.00 USD | 167,660,000.00 USD | 0.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD |
| `1D` | `1.43` | 97,000,000.00 USD | 97,000,000.00 USD | 0.00 USD | 18,490.00 USD | 28,360.00 USD | 151,220.00 USD |
| `7D` | `1.43` | 168,510,000.00 USD | 168,510,000.00 USD | 0.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD |
| `7D` | `1.43` | 169,400,000.00 USD | 169,400,000.00 USD | 0.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD |
| `7D` | `1.44` | 169,430,000.00 USD | 169,430,000.00 USD | 0.00 USD | 6,560.00 USD | 12,030.00 USD | 11,180.00 USD |
| `7D` | `1.44` | 170,050,000.00 USD | 170,050,000.00 USD | 0.00 USD | 175,290.00 USD | 83,590.00 USD | 366,410.00 USD |
| `7D` | `1.44` | 170,570,000.00 USD | 170,570,000.00 USD | 0.00 USD | 85,020.00 USD | 74,230.00 USD | 358,360.00 USD |
| `7D` | `1.44` | 171,230,000.00 USD | 171,230,000.00 USD | 0.00 USD | 270,280.00 USD | 180,410.00 USD | 209,010.00 USD |
| `7D` | `1.44` | 171,470,000.00 USD | 171,470,000.00 USD | 0.00 USD | 78,320.00 USD | 47,010.00 USD | 116,120.00 USD |
| `7D` | `1.45` | 171,570,000.00 USD | 171,570,000.00 USD | 0.00 USD | 50,420.00 USD | 39,100.00 USD | 12,180.00 USD |
| `7D` | `1.45` | 172,030,000.00 USD | 172,030,000.00 USD | 0.00 USD | 69,200.00 USD | 27,700.00 USD | 365,030.00 USD |
| `7D` | `1.45` | 172,220,000.00 USD | 172,220,000.00 USD | 0.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD |
| `7D` | `1.45` | 173,120,000.00 USD | 173,120,000.00 USD | 0.00 USD | 216,330.00 USD | 94,590.00 USD | 598,610.00 USD |
| `7D` | `1.45` | 173,660,000.00 USD | 173,660,000.00 USD | 0.00 USD | 176,550.00 USD | 81,140.00 USD | 274,660.00 USD |

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
| `15M` | `XRP` | `59.08%` | `40.92%` | `1.44` | 288,130,000.00 USD |
| `15M` | `Binance` | `61.56%` | `38.44%` | `1.60` | 78,160,000.00 USD |
| `15M` | `OKX` | `62.58%` | `37.42%` | `1.67` | 44,250,000.00 USD |
| `15M` | `Bybit` | `67.69%` | `32.31%` | `2.10` | 17,970,000.00 USD |
| `15M` | `KuCoin` | `70%` | `30%` | `2.33` | 300,920.00 USD |
| `15M` | `Gate` | `56.62%` | `43.38%` | `1.31` | 53,550,000.00 USD |
| `15M` | `Bitget` | `69.45%` | `30.55%` | `2.27` | 26,380,000.00 USD |
| `15M` | `BingX` | `73.61%` | `26.39%` | `2.79` | 5,960,000.00 USD |
| `15M` | `MEXC` | `53.28%` | `46.72%` | `1.14` | 12,460,000.00 USD |
| `15M` | `Bitunix` | `59.3%` | `40.7%` | `1.46` | 9,120,000.00 USD |
| `15M` | `Hyperliquid` | `44.44%` | `55.56%` | `0.80` | 3,540,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `82.19%` | `17.81%` | `4.61` | 562,800.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `31.96%` | `68.04%` | `0.47` | 17,050,000.00 USD |
| `15M` | `HTX` | `43.09%` | `56.91%` | `0.76` | 3,520,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `53.1%` | `46.9%` | `1.13` | 801,220.00 USD |
| `15M` | `Bitfinex` | `59.95%` | `40.05%` | `1.50` | 8,330.00 USD |
| `15M` | `Kraken` | `88.78%` | `11.22%` | `7.91` | 1,640,000.00 USD |
| `15M` | `Aster` | `55.18%` | `44.82%` | `1.23` | 2,140,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `45.69%` | `54.31%` | `0.84` | 10,720,000.00 USD |
| `15M` | `Whale Positions` | `61.56%` | `38.44%` | `1.60` | 78,160,000.00 USD |
| `15M` | `Global Accounts` | `59.08%` | `40.92%` | `1.44` | 288,130,000.00 USD |
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
| `0:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 10,205,311.65 USD | 4,505,902.50 USD | 5,699,409.15 USD | -1,193,506.66 USD | `-11.69%` | `6B / 11S` |
| `5:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 4,776,328.08 USD | 2,498,208.46 USD | 2,278,119.62 USD | 220,088.84 USD | `+4.61%` | `7B / 8S` |
| `0:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.29` | 9,199,982.08 USD | 4,187,578.87 USD | 5,012,403.21 USD | -824,824.35 USD | `-8.97%` | `4B / 7S` |
| `5:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.29` | 5,359,755.08 USD | 2,909,456.29 USD | 2,450,298.78 USD | 459,157.51 USD | `+8.57%` | `5B / 3S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.30` | `1.29` | 8,857,459.31 USD | 3,136,112.07 USD | 5,721,347.24 USD | -2,585,235.17 USD | `-29.19%` | `5B / 22S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 11,824,590.46 USD | 6,782,340.79 USD | 5,042,249.67 USD | 1,740,091.12 USD | `+14.72%` | `12B / 8S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 4,908,299.96 USD | 2,545,215.27 USD | 2,363,084.69 USD | 182,130.57 USD | `+3.71%` | `7B / 8S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 4,397,440.00 USD | 1,948,835.02 USD | 2,448,604.98 USD | -499,769.95 USD | `-11.37%` | `7B / 14S` |
| `0:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 30,348,241.89 USD | 10,177,546.51 USD | 20,170,695.38 USD | -9,993,148.87 USD | `-32.93%` | `4B / 38S` |
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 5,208,468.14 USD | 2,712,514.86 USD | 2,495,953.28 USD | 216,561.58 USD | `+4.16%` | `13B / 8S` |

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
| `5m` | 602,970.00 USD | 2,420,000.00 USD | **`ACCUMULATION`** |
| `15m` | 124,090.00 USD | 2,420,000.00 USD | **`ACCUMULATION`** |
| `30m` | -6,520,000.00 USD | -15,070,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -5,760,000.00 USD | -12,940,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -9,640,000.00 USD | -22,000,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -9,150,000.00 USD | -28,510,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -7,910,000.00 USD | -20,400,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -9,120,000.00 USD | -25,710,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,560,000.00 USD | -23,850,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -29,330,000.00 USD | -74,770,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -77,090,000.00 USD | -91,870,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -559,950,000.00 USD | -1,200,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+602.97K` | 15m=`+124.09K` | 1h=`-5.76M` | 24h=`-29.33M`
* Futures Capital Netflows: 5m=`+2.42M` | 15m=`+2.42M` | 1h=`-12.94M` | 24h=`-74.77M`
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
  * `2026-10-30 00:16:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:45 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:20:45 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:19:45 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:21:45 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:21:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0124` pts)
  * +2.5R Take Profit: `1.32`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.30` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.31` (Risk Distance: `0.0124` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.30`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
