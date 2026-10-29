# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 04:44:06 IST` (`2026-10-29 23:14:06 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.23` | **Live Ask Quote**: `1.24` | **Mid Price**: `1.24`
- **Spread Points**: `3.00` | **Spread BPS**: `24.28 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.28` | VWAP Z-Score: `-1.56` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0114` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `31.30` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.35` | Lower -3.00σ Band: `1.21`
  * Upper +2.51σ Band: `1.33` | Lower -2.51σ Band: `1.22`
  * Upper +2.01σ Band: `1.32` | Lower -2.01σ Band: `1.23`
  * Upper +2.00σ Band: `1.32` | Lower -2.00σ Band: `1.23`
  * Upper +1.28σ Band: `1.31` | Lower -1.28σ Band: `1.25`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.25`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.25` | EMA-20=`1.26` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.28` (Slope: `+0.0000`) | EMA-100=`1.29`
  * Institutional Anchors: EMA-144=`1.29` | EMA-200=`1.30` (Slope: `-0.4638`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.33` | 24H Low=`1.22` | Weekly High=`1.34` | Weekly Low=`1.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.25` (Distance: `-1.37%`)
  * Point of Control (POC) = `1.25` (Distance: `-0.80%`)
  * Value Area Low (VAL) = `1.24` (Distance: `-0.32%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.32` | Weekly POC=`1.29` | Weekly VAL=`1.27`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.23`
  * London Session (08:00-16:00 UTC): High=`1.24` | Low=`1.23`
  * New York Session (13:00-21:00 UTC): High=`1.24` | Low=`1.23`
  * Initial Balance (First Hour): IB High=`1.24` | IB Low=`1.23`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.23` - `1.24`
  * Optimal Trade Entry (OTE 0.705): `1.24`
  * Structural Invalidation Anchor (0.786): `1.25`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.25` | `1.25` | `1.24` | `1.25` | `3,586,250` | 4,464,822.32 USD | 256,232.13 USD | `+5.74%` | -74,019,858.47 USD | `+0.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `1.25` | `1.25` | `1.24` | `1.24` | `7,210,185` | 8,949,509.60 USD | -1,949,929.73 USD | `-21.79%` | -75,969,788.20 USD | `-2.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.24` | `1.24` | `1.24` | `1.24` | `609,822` | 754,863.37 USD | 170,467.89 USD | `+22.58%` | -75,799,320.31 USD | `+0.15` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.25` | `12,664,504` | 15,839,415.33 USD | 2,205,693.26 USD | `+13.93%` | -75,537,544.02 USD | `+0.75` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.25` | `1.25` | `1.24` | `1.25` | `10,523,334` | 13,112,458.20 USD | 1,607,415.65 USD | `+12.26%` | -73,930,128.37 USD | `+0.65` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `1.25` | `1.25` | `1.24` | `1.24` | `7,840,481` | 9,729,709.03 USD | -1,768,067.45 USD | `-18.17%` | -75,698,195.82 USD | `+0.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.24` | `1.26` | `1.23` | `1.25` | `86,510,066` | 108,215,327.13 USD | 1,874,321.17 USD | `+1.73%` | -75,869,737.67 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.25` | `1.26` | `1.24` | `1.25` | `77,433,234` | 96,832,550.27 USD | 1,578,504.39 USD | `+1.63%` | -74,291,233.29 USD | `+0.50` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `1.25` | `1.25` | `1.24` | `1.24` | `7,840,481` | 9,729,709.03 USD | -1,768,067.45 USD | `-18.17%` | -76,059,300.74 USD | `+0.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `380,669,613` | 475,549,796.73 USD | -36,131,665.32 USD | `-7.60%` | -76,070,695.13 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,072,364.54 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,389,228.53 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `380,669,613` | 475,549,796.73 USD | -36,131,665.32 USD | `-7.60%` | -76,070,695.13 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`1.24`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `1.24` | `22738.0000` | 28,176.93 USD | 1,683,594.54 USD | `6 orders` | `+0.16%` | `-` |
| `ASK` | `1.24` | `27954.0000` | 34,637.80 USD | 1,655,417.61 USD | `3 orders` | `+0.15%` | `-` |
| `ASK` | `1.24` | `46928.0000` | 58,143.79 USD | 1,620,779.81 USD | `7 orders` | `+0.14%` | `-` |
| `ASK` | `1.24` | `95160.0000` | 117,893.72 USD | 1,562,636.01 USD | `7 orders` | `+0.13%` | `-` |
| `ASK` | `1.24` | `28658.0000` | 35,501.53 USD | 1,444,742.29 USD | `11 orders` | `+0.13%` | `-` |
| `ASK` | `1.24` | `366709.0000` | 454,242.44 USD | 1,409,240.76 USD | `10 orders` | `+0.12%` | `-` |
| `ASK` | `1.24` | `53845.0000` | 66,692.42 USD | 954,998.32 USD | `8 orders` | `+0.11%` | `-` |
| `ASK` | `1.24` | `20167.0000` | 24,976.83 USD | 888,305.90 USD | `3 orders` | `+0.10%` | `-` |
| `ASK` | `1.24` | `23553.0000` | 29,168.04 USD | 863,329.08 USD | `5 orders` | `+0.09%` | `-` |
| `ASK` | `1.24` | `41075.0000` | 50,863.17 USD | 834,161.04 USD | `8 orders` | `+0.08%` | `-` |
| `ASK` | `1.24` | `23252.0000` | 28,790.63 USD | 783,297.87 USD | `8 orders` | `+0.08%` | `-` |
| `ASK` | `1.24` | `301346.0000` | 373,096.48 USD | 754,507.24 USD | `8 orders` | `+0.07%` | `-` |
| `ASK` | `1.24` | `22245.0000` | 27,539.31 USD | 381,410.76 USD | `6 orders` | `+0.06%` | `-` |
| `ASK` | `1.24` | `16731.0000` | 20,711.30 USD | 353,871.45 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `1.24` | `26393.0000` | 32,669.26 USD | 333,160.14 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `1.24` | `52449.0000` | 64,916.13 USD | 300,490.89 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `1.24` | `65637.0000` | 81,232.35 USD | 235,574.76 USD | `15 orders` | `+0.03%` | `-` |
| `ASK` | `1.24` | `34941.0000` | 43,239.49 USD | 154,342.41 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `1.24` | `45178.0000` | 55,903.26 USD | 111,102.92 USD | `8 orders` | `+0.01%` | `-` |
| `ASK` | `1.24` | `44613.0000` | 55,199.66 USD | 55,199.66 USD | `11 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.24` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.24` | `0.00%` | `-` |
| `BID` | `1.24` | `5935.0000` | 7,342.78 USD | 7,342.78 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `1.24` | `7156.0000` | 8,852.69 USD | 16,195.47 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `1.24` | `8610.0000` | 10,650.57 USD | 26,846.04 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `1.24` | `79091.0000` | 97,827.66 USD | 124,673.70 USD | `8 orders` | `-0.03%` | `-` |
| `BID` | `1.24` | `24019.0000` | 29,706.70 USD | 154,380.40 USD | `12 orders` | `-0.04%` | `-` |
| `BID` | `1.24` | `74162.0000` | 91,716.15 USD | 246,096.54 USD | `10 orders` | `-0.04%` | `-` |
| `BID` | `1.24` | `35169.0000` | 43,489.99 USD | 289,586.53 USD | `11 orders` | `-0.05%` | `-` |
| `BID` | `1.24` | `56730.0000` | 70,146.64 USD | 359,733.17 USD | `10 orders` | `-0.06%` | `-` |
| `BID` | `1.24` | `356594.0000` | 440,892.82 USD | 800,625.99 USD | `15 orders` | `-0.07%` | `-` |
| `BID` | `1.24` | `65994.0000` | 81,588.38 USD | 882,214.38 USD | `14 orders` | `-0.08%` | `-` |
| `BID` | `1.24` | `229222.0000` | 283,364.24 USD | 1,165,578.61 USD | `7 orders` | `-0.08%` | `-` |
| `BID` | `1.24` | `55932.0000` | 69,137.55 USD | 1,234,716.16 USD | `9 orders` | `-0.09%` | `-` |
| `BID` | `1.24` | `29712.0000` | 36,724.03 USD | 1,271,440.19 USD | `11 orders` | `-0.10%` | `-` |
| `BID` | `1.24` | `51440.0000` | 63,574.70 USD | 1,335,014.89 USD | `4 orders` | `-0.11%` | `-` |
| `BID` | `1.24` | `245766.0000` | 303,717.62 USD | 1,638,732.51 USD | `3 orders` | `-0.12%` | `-` |
| `BID` | `1.24` | `78345.0000` | 96,810.92 USD | 1,735,543.43 USD | `9 orders` | `-0.13%` | `-` |
| `BID` | `1.24` | `353777.0000` | 437,126.86 USD | 2,172,670.29 USD | `5 orders` | `-0.13%` | `-` |
| `BID` | `1.24` | `89059.0000` | 110,032.39 USD | 2,282,702.68 USD | `8 orders` | `-0.14%` | `-` |
| `BID` | `1.24` | `53496.0000` | 66,088.96 USD | 2,348,791.64 USD | `11 orders` | `-0.15%` | `-` |
| `BID` | `1.24` | `8048.0000` | 9,941.69 USD | 2,358,733.33 USD | `3 orders` | `-0.16%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `27` | `0x31b1...1434` | `LONG` | 43,564,315.66 USD | `35,031,430.00` | `1.13` | `1.24` | `0.9612` | 3,985,432.39 USD | `+9.15%` | `10X Cross` |
| `94` | `0x5b5d...c060` | `SHORT` | 19,768,532.01 USD | `15,964,251.00` | `1.44` | `1.24` | `12.65` | 3,147,536.69 USD | `+15.92%` | `5X Cross` |
| `160` | `0xb83d...6e36` | `SHORT` | 13,066,591.55 USD | `10,555,450.00` | `1.50` | `1.24` | `16.00` | 2,755,978.09 USD | `+21.09%` | `5X Cross` |
| `242` | `0x58f0...0d20` | `LONG` | 9,317,306.88 USD | `7,526,704.00` | `1.25` | `1.24` | `1.22` | -73,857.67 USD | `-0.79%` | `20X Cross` |
| `380` | `0x77ee...a018` | `LONG` | 6,153,917.76 USD | `4,943,700.00` | `1.27` | `1.24` | `0.2919` | -124,581.24 USD | `-2.02%` | `20X Cross` |
| `399` | `0xecb6...2b00` | `SHORT` | 5,784,977.58 USD | `4,667,563.00` | `1.28` | `1.24` | `7.55` | 195,373.79 USD | `+3.38%` | `10X Cross` |
| `428` | `0xca49...53c8` | `SHORT` | 5,122,699.20 USD | `4,138,886.00` | `1.44` | `1.24` | `4.79` | 830,623.53 USD | `+16.21%` | `20X Cross` |
| `477` | `0xfc27...9d9d` | `SHORT` | 4,571,355.10 USD | `3,688,659.00` | `1.30` | `1.24` | `6.03` | 233,552.56 USD | `+5.11%` | `20X Cross` |
| `503` | `0xdd53...2b13` | `SHORT` | 4,398,070.79 USD | `3,551,127.00` | `1.42` | `1.24` | `19.53` | 650,338.68 USD | `+14.79%` | `3X Cross` |
| `504` | `0x610b...b613` | `LONG` | 4,387,050.75 USD | `3,543,946.00` | `1.44` | `1.24` | `0.8446` | -712,941.86 USD | `-16.25%` | `5X Cross` |
| `607` | `0x9946...0852` | `SHORT` | 3,702,038.98 USD | `2,990,580.00` | `1.43` | `1.24` | `1.77` | 561,911.49 USD | `+15.18%` | `20X Cross` |
| `667` | `0xc30c...a4c9` | `SHORT` | 3,376,410.62 USD | `2,727,531.00` | `1.42` | `1.24` | `1.61` | 487,837.57 USD | `+14.45%` | `8X Cross` |
| `691` | `0x9aa5...58af` | `SHORT` | 3,227,500.47 USD | `2,604,083.00` | `1.46` | `1.24` | `4.84` | 570,220.19 USD | `+17.67%` | `20X Cross` |
| `702` | `0xf48f...10fe` | `LONG` | 3,176,947.56 USD | `2,565,779.00` | `1.53` | `1.24` | `1.04` | -747,693.17 USD | `-23.53%` | `4X Cross` |
| `743` | `0x023a...2355` | `SHORT` | 3,057,188.40 USD | `2,469,657.00` | `1.32` | `1.24` | `4.09` | 207,713.75 USD | `+6.79%` | `20X Cross` |
| `744` | `0x45d2...4029` | `SHORT` | 3,044,418.30 USD | `2,453,000.00` | `1.48` | `1.24` | `18.88` | 593,862.12 USD | `+19.51%` | `20X Cross` |
| `1082` | `0xc179...e0c8` | `SHORT` | 2,029,549.52 USD | `1,639,775.00` | `1.30` | `1.24` | `5.09` | 104,098.03 USD | `+5.13%` | `10X Cross` |
| `1096` | `0xeadc...9d55` | `LONG` | 2,014,676.20 USD | `1,619,805.00` | `1.21` | `1.24` | `0.000000` | 55,833.18 USD | `+2.77%` | `20X Cross` |
| `1168` | `0x94b2...599e` | `SHORT` | 1,916,282.25 USD | `1,540,696.00` | `1.36` | `1.24` | `1.87` | 184,184.20 USD | `+9.61%` | `20X Cross` |
| `1186` | `0xbcd4...0dd2` | `SHORT` | 1,895,613.96 USD | `1,529,461.00` | `1.31` | `1.24` | `1.96` | 108,930.63 USD | `+5.75%` | `20X Cross` |
| `1199` | `0x3fc5...c0c1` | `SHORT` | 1,872,187.11 USD | `1,511,779.00` | `1.52` | `1.24` | `2.74` | 419,427.49 USD | `+22.40%` | `20X Cross` |
| `1223` | `0x31ef...f715` | `LONG` | 1,826,591.56 USD | `1,475,080.00` | `1.49` | `1.24` | `1.04` | -372,673.84 USD | `-20.40%` | `3X Isolated` |
| `1274` | `0x7737...bf66` | `SHORT` | 1,757,362.28 USD | `1,413,466.00` | `1.41` | `1.24` | `13.20` | 241,506.37 USD | `+13.74%` | `10X Cross` |
| `1334` | `0x95da...2328` | `LONG` | 1,647,850.30 USD | `1,324,876.00` | `1.35` | `1.24` | `0.1351` | -145,790.80 USD | `-8.85%` | `5X Cross` |
| `1343` | `0xef96...9383` | `SHORT` | 1,639,023.47 USD | `1,323,394.00` | `1.34` | `1.24` | `4.54` | 133,767.51 USD | `+8.16%` | `20X Cross` |
| `1362` | `0xee2b...d67e` | `LONG` | 1,617,048.96 USD | `1,306,284.00` | `1.55` | `1.24` | `0.4073` | -413,605.94 USD | `-25.58%` | `4X Cross` |
| `1411` | `0x215d...f80a` | `LONG` | 1,556,682.34 USD | `1,251,777.00` | `1.32` | `1.24` | `1.15` | -97,771.89 USD | `-6.28%` | `14X Cross` |
| `1440` | `0x2482...0e55` | `LONG` | 1,534,409.63 USD | `1,239,226.00` | `1.33` | `1.24` | `1.21` | -115,957.42 USD | `-7.56%` | `20X Isolated` |
| `1458` | `0x123d...3bff` | `LONG` | 1,504,455.77 USD | `1,215,329.00` | `1.35` | `1.24` | `0.000000` | -132,613.45 USD | `-8.81%` | `10X Cross` |
| `1472` | `0x5fa3...35b7` | `SHORT` | 1,485,796.94 USD | `1,200,353.00` | `1.31` | `1.24` | `3.44` | 81,347.62 USD | `+5.48%` | `20X Cross` |
| `1483` | `0xe9d1...d2d3` | `SHORT` | 1,473,736.27 USD | `1,190,898.00` | `1.27` | `1.24` | `2.16` | 38,470.54 USD | `+2.61%` | `10X Cross` |
| `1513` | `0xdf95...7d72` | `SHORT` | 1,436,457.00 USD | `1,160,492.00` | `1.37` | `1.24` | `36.29` | 156,974.63 USD | `+10.93%` | `20X Cross` |
| `1612` | `0x4537...8732` | `SHORT` | 1,334,551.52 USD | `1,078,077.00` | `1.25` | `1.24` | `2.18` | 10,575.87 USD | `+0.79%` | `10X Cross` |
| `1675` | `0xb1ce...681b` | `LONG` | 1,264,126.42 USD | `1,021,764.00` | `1.49` | `1.24` | `1.16` | -259,930.07 USD | `-20.56%` | `4X Isolated` |
| `1787` | `0x3c36...461a` | `LONG` | 1,163,595.13 USD | `940,051.00` | `1.30` | `1.24` | `1.05` | -55,485.49 USD | `-4.77%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3103 USD [API] | `2026-10-28 16:37:56` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3102 USD [API] | `2026-10-28 16:37:56` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 13,015.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 13.02K USD at 1.3164 USD [API] | `2026-10-28 16:55:05` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,141.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.14K USD at 1.3127 USD [API] | `2026-10-28 17:32:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 10,189.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.19K USD at 1.3127 USD [API] | `2026-10-28 17:32:23` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,057.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.06K USD at 1.3158 USD [API] | `2026-10-28 17:36:13` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,892.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.89K USD at 1.3172 USD [API] | `2026-10-28 17:44:02` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3200 USD [API] | `2026-10-28 17:50:51` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,004.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.3193 USD [API] | `2026-10-28 17:54:39` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,972.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.97K USD at 1.3186 USD [API] | `2026-10-28 17:56:50` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,452.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.45K USD at 1.3186 USD [API] | `2026-10-28 18:00:22` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,380.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.38K USD at 1.3243 USD [API] | `2026-10-28 18:04:24` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 9,315.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.32K USD at 1.3211 USD [API] | `2026-10-28 18:06:08` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 47,579.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 47.58K USD at 1.3177 USD [API] | `2026-10-28 18:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,004.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.00K USD at 1.3177 USD [API] | `2026-10-28 18:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,004.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.00K USD at 1.3177 USD [API] | `2026-10-28 18:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 9,273.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.27K USD at 1.3177 USD [API] | `2026-10-28 18:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,430.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.43K USD at 1.3177 USD [API] | `2026-10-28 18:15:44` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,677.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.68K USD at 1.3198 USD [API] | `2026-10-28 18:19:21` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,004.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.3198 USD [API] | `2026-10-28 18:19:21` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,003.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.00K USD at 1.3195 USD [API] | `2026-10-28 18:21:46` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,920.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 7.92K USD at 1.3200 USD [API] | `2026-10-27 12:48:45` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 496.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.50K USD at 1.3445 USD [API] | `2026-10-20 22:40:11` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 505.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.51K USD at 1.3444 USD [API] | `2026-10-20 22:40:11` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,445.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.45K USD at 1.3443 USD [API] | `2026-10-20 22:40:11` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,850.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.85K USD at 1.3443 USD [API] | `2026-10-20 22:40:11` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 457.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.46K USD at 1.3443 USD [API] | `2026-10-20 22:40:11` |
| `ANNOUNCEMENT` | `INFO` | `1.52` | 1,301.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.30K USD at 1.5200 USD [API] | `2026-09-28 16:26:54` |
| `ANNOUNCEMENT` | `INFO` | `1.52` | 7,742.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 7.74K USD at 1.5200 USD [API] | `2026-09-28 16:26:54` |
| `ANNOUNCEMENT` | `INFO` | `1.52` | 76.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.08K USD at 1.5200 USD [API] | `2026-09-28 16:26:54` |
| `ANNOUNCEMENT` | `INFO` | `1.53` | 2,498.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.50K USD at 1.5345 USD [API] | `2026-09-24 16:48:05` |
| `ANNOUNCEMENT` | `INFO` | `1.53` | 5,174.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.17K USD at 1.5345 USD [API] | `2026-09-24 16:48:05` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,315.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.32K USD at 1.3275 USD [API] | `2026-10-28 18:37:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,400.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.40K USD at 1.3263 USD [API] | `2026-10-28 18:40:10` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,228.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.23K USD at 1.3264 USD [API] | `2026-10-28 18:40:10` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,973.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.97K USD at 1.3289 USD [API] | `2026-10-28 18:41:59` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,077.07 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.08K USD at 1.3290 USD [API] | `2026-10-28 18:41:55` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,681.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.68K USD at 1.3309 USD [API] | `2026-10-28 18:44:04` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 11,451.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.45K USD at 1.3309 USD [API] | `2026-10-28 18:44:04` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 46,926.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 46.93K USD at 1.3306 USD [API] | `2026-10-28 18:50:53` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,005.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.01K USD at 1.3306 USD [API] | `2026-10-28 18:50:53` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,621.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.62K USD at 1.3273 USD [API] | `2026-10-28 18:59:08` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,004.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.3277 USD [API] | `2026-10-28 18:58:43` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,004.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.3275 USD [API] | `2026-10-28 19:01:57` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,899.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.90K USD at 1.3265 USD [API] | `2026-10-28 19:01:19` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,412.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 7.41K USD at 1.3087 USD [API] | `2026-10-25 02:05:20` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,486.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.49K USD at 1.3087 USD [API] | `2026-10-25 02:05:20` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,565.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.57K USD at 1.3085 USD [API] | `2026-10-25 02:05:20` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 1,076.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.08K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 247.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.25K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 3,999.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 9,709.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.71K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 2,644.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.64K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 2,644.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.64K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 1,880.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.88K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 2,737.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.74K USD at 1.2775 USD [API] | `2026-10-24 09:04:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,546.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.55K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 245.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.25K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,830.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.83K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 693.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.69K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,485.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.49K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 128.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.13K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 6,492.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.49K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,519.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.52K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,485.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.49K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,555.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.56K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,010.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.01K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,626.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.63K USD at 1.3353 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,674.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.67K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 404.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 245.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.25K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,005.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.01K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,876.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.88K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,509.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.51K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,508.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.51K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,425.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.43K USD at 1.3354 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,262.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.26K USD at 1.3355 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,568.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.57K USD at 1.3355 USD [API] | `2026-10-22 08:02:53` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,783.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.78K USD at 1.2930 USD [API] | `2026-10-15 02:24:20` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,999.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.2930 USD [API] | `2026-10-15 02:24:20` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,997.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.00K USD at 1.2930 USD [API] | `2026-10-15 02:24:20` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,376.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.38K USD at 1.2930 USD [API] | `2026-10-15 02:24:20` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,239.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.24K USD at 1.2930 USD [API] | `2026-10-15 02:24:20` |
| `ANNOUNCEMENT` | `INFO` | `1.39` | 11,492.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 11.49K USD at 1.3865 USD [API] | `2026-10-12 12:37:31` |
| `ANNOUNCEMENT` | `INFO` | `1.39` | 2,086.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.09K USD at 1.3866 USD [API] | `2026-10-12 12:37:31` |
| `ANNOUNCEMENT` | `INFO` | `1.39` | 28,219.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 28.22K USD at 1.3917 USD [API] | `2026-10-08 04:20:41` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 7,770.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.77K USD at 1.4855 USD [API] | `2026-09-28 03:32:45` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,920.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.92K USD at 1.3257 USD [API] | `2026-10-28 19:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,046.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.05K USD at 1.3270 USD [API] | `2026-10-28 19:14:57` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,617.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 9.62K USD at 1.3268 USD [API] | `2026-10-28 19:17:15` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 14,519.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 14.52K USD at 1.3268 USD [API] | `2026-10-28 19:26:42` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,514.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.51K USD at 1.3291 USD [API] | `2026-10-28 19:32:08` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,825.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.83K USD at 1.3291 USD [API] | `2026-10-28 19:32:08` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,003.53 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.3279 USD [API] | `2026-10-28 19:34:11` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,738.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.74K USD at 1.3285 USD [API] | `2026-10-28 19:35:23` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,818.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.82K USD at 1.3285 USD [API] | `2026-10-28 19:35:23` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,971.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.97K USD at 1.3286 USD [API] | `2026-10-28 19:35:23` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,863.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.86K USD at 1.3286 USD [API] | `2026-10-28 19:35:23` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,863.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.86K USD at 1.3287 USD [API] | `2026-10-28 19:35:23` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,384.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.38K USD at 1.3270 USD [API] | `2026-10-28 19:37:59` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,795.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.80K USD at 1.3275 USD [API] | `2026-10-28 19:40:01` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 18,152.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 18.15K USD at 1.3316 USD [API] | `2026-10-28 19:44:10` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,003.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.3315 USD [API] | `2026-10-28 19:44:10` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,834.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.83K USD at 1.3315 USD [API] | `2026-10-28 19:44:10` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,144.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.14K USD at 1.3315 USD [API] | `2026-10-28 19:44:10` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,433.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.43K USD at 1.3334 USD [API] | `2026-10-28 19:47:22` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 4,088.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.09K USD at 1.3627 USD [API] | `2026-10-08 15:22:32` |
| `ANNOUNCEMENT` | `INFO` | `1.21` | 35.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.04K USD at 1.2100 USD [API] | `2026-06-15 11:09:20` |
| `ANNOUNCEMENT` | `INFO` | `1.21` | 629.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.63K USD at 1.2100 USD [API] | `2026-06-15 11:09:20` |
| `ANNOUNCEMENT` | `INFO` | `1.21` | 99.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.10K USD at 1.2100 USD [API] | `2026-06-15 11:09:20` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 150.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.15K USD at 1.3690 USD [API] | `2026-03-12 03:47:44` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 12.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3690 USD [API] | `2026-03-12 03:47:44` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 21.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.3690 USD [API] | `2026-03-12 03:47:44` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 2,211.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.21K USD at 1.3691 USD [API] | `2026-03-12 03:47:44` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 2,721.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.72K USD at 1.3605 USD [API] | `2026-03-06 14:09:58` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 704.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.70K USD at 1.4096 USD [API] | `2026-02-13 15:31:03` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 2,165.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.17K USD at 1.4434 USD [API] | `2026-02-09 15:05:07` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 581.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.58K USD at 1.4249 USD [API] | `2026-02-07 07:07:55` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 1,449.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.45K USD at 1.4490 USD [API] | `2026-02-06 14:34:09` |
| `ANNOUNCEMENT` | `INFO` | `1.15` | 2,308.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.31K USD at 1.1541 USD [API] | `2026-02-06 00:14:07` |
| `ANNOUNCEMENT` | `INFO` | `1.65` | 369.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.37K USD at 1.6489 USD [API] | `2026-01-31 14:23:25` |
| `ANNOUNCEMENT` | `INFO` | `1.65` | 479.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.48K USD at 1.6489 USD [API] | `2026-01-31 14:23:25` |
| `ANNOUNCEMENT` | `INFO` | `1.65` | 1,769.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.77K USD at 1.6489 USD [API] | `2026-01-31 14:23:25` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,124.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.12K USD at 1.3339 USD [API] | `2026-10-28 19:49:32` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,509.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.51K USD at 1.3350 USD [API] | `2026-10-28 19:56:30` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 10,341.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.34K USD at 1.3379 USD [API] | `2026-10-28 20:04:50` |
| `ANNOUNCEMENT` | `INFO` | `1.10` | 2,462.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.46K USD at 1.1046 USD [API] | `2026-06-05 06:19:52` |
| `ANNOUNCEMENT` | `INFO` | `1.10` | 929.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.93K USD at 1.1047 USD [API] | `2026-06-05 06:19:52` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 6,138.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.14K USD at 1.3360 USD [API] | `2026-10-28 20:06:28` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 6,677.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.68K USD at 1.3355 USD [API] | `2026-10-28 20:10:16` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 7,976.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.98K USD at 1.3358 USD [API] | `2026-10-28 20:10:16` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,661.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.66K USD at 1.3347 USD [API] | `2026-10-28 20:12:28` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 13,654.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 13.65K USD at 1.3318 USD [API] | `2026-10-28 20:16:14` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 17,313.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 17.31K USD at 1.3318 USD [API] | `2026-10-28 20:16:14` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,290.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.29K USD at 1.3318 USD [API] | `2026-10-28 20:16:14` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 33,336.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 33.34K USD at 1.3318 USD [API] | `2026-10-28 20:16:14` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,879.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.88K USD at 1.3300 USD [API] | `2026-10-28 20:18:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 869.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.87K USD at 1.2922 USD [API] | `2026-10-23 22:47:54` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 969.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.97K USD at 1.2922 USD [API] | `2026-10-23 22:47:54` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 1,034.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.03K USD at 1.2564 USD [API] | `2026-10-18 19:45:49` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 3,589.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.59K USD at 1.2801 USD [API] | `2026-10-17 21:30:01` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 8,021.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 8.02K USD at 1.3381 USD [API] | `2026-10-15 15:17:47` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 5,400.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.40K USD at 1.2984 USD [API] | `2026-10-15 02:23:51` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,566.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.57K USD at 1.3283 USD [API] | `2026-10-28 20:20:22` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,003.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.00K USD at 1.3283 USD [API] | `2026-10-28 20:20:22` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,002.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.00K USD at 1.3284 USD [API] | `2026-10-28 20:20:22` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+3.86%`) | Long MP=`1.24` (Vol: 1,700,000.00 USD, Dist: `--0.76%`)
  * 48H Horizon: Short MP=`1.35` (Vol: 3,500,000.00 USD, Dist: `+8.21%`) | Long MP=`1.25` (Vol: 1,500,000.00 USD, Dist: `--0.12%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 3,400,000.00 USD, Dist: `+8.21%`) | Long MP=`1.25` (Vol: 1,500,000.00 USD, Dist: `--0.12%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 4,100,000.00 USD, Dist: `+8.21%`) | Long MP=`1.25` (Vol: 1,500,000.00 USD, Dist: `--0.12%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 1,270.00 USD | 73,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 25,540.00 USD | 73,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 1,250.00 USD | 73,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 111,160.00 USD | 73,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 1,480,000.00 USD | 72,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 4,320.00 USD | 71,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 5,010.00 USD | 71,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 15,720.00 USD | 71,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 376.88 USD | 71,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 517.50 USD | 71,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 3,520.00 USD | 71,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 3,560.00 USD | 71,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 183.00 USD | 71,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 503,890.00 USD | 71,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 174.59 USD | 70,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 612.36 USD | 70,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 810.91 USD | 70,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 297.50 USD | 70,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 8,710.00 USD | 70,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 1,070.00 USD | 70,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 10,030.00 USD | 70,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 198.55 USD | 70,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 1,870.00 USD | 70,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 8,100.00 USD | 70,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 175.10 USD | 70,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 6,590.00 USD | 70,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 985.47 USD | 70,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 2,740.00 USD | 70,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 6,220.00 USD | 70,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 2,060.00 USD | 70,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 171,380.00 USD | 70,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 34,990.00 USD | 70,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 5,160.00 USD | 70,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 23,750.00 USD | 70,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 36,660.00 USD | 70,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 1,440.00 USD | 70,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 11,440.00 USD | 70,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 21,480.00 USD | 70,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 1,030.00 USD | 70,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 27,220.00 USD | 70,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 30,660.00 USD | 70,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 2,810.00 USD | 70,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 3,780.00 USD | 70,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 182,630.00 USD | 70,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 68,160.00 USD | 70,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 223,880.00 USD | 70,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 36,750.00 USD | 69,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 52,300.00 USD | 69,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 92,400.00 USD | 69,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 4,070.00 USD | 69,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 32,360.00 USD | 69,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 80,500.00 USD | 69,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 11,250.00 USD | 69,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 14,340.00 USD | 69,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 22,410.00 USD | 69,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 906.68 USD | 69,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 3,000,000.00 USD | 69,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 82,680.00 USD | 66,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 87,630.00 USD | 66,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 50,330.00 USD | 66,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 85,410.00 USD | 66,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 380,130.00 USD | 66,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 99,910.00 USD | 65,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 211,180.00 USD | 65,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 75,210.00 USD | 65,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 73,840.00 USD | 65,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 89,340.00 USD | 65,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 121,380.00 USD | 65,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 116,660.00 USD | 65,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,880,000.00 USD | 65,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 150,030.00 USD | 31,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 456,880.00 USD | 31,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 90,130.00 USD | 30,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 440,870.00 USD | 30,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 867,160.00 USD | 30,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 2,690,000.00 USD | 29,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,120,000.00 USD | 26,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 689,860.00 USD | 24,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,140,000.00 USD | 23,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 430,460.00 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 491,560.00 USD | 22,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 723,650.00 USD | 21,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 570,310.00 USD | 21,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 73,910.00 USD | 20,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.11` | 27,640,000.00 USD | 27,640,000.00 USD | 17,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 45,830,000.00 USD | 45,830,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 27,620,000.00 USD | 27,620,000.00 USD | 18,710.00 USD | 0.00 USD | 121,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 27,480,000.00 USD | 27,480,000.00 USD | 0.00 USD | 2,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 45,810,000.00 USD | 45,810,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 867,550.00 USD | 20,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.12` | 27,480,000.00 USD | 27,480,000.00 USD | 0.00 USD | 0.00 USD | 61,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 45,800,000.00 USD | 45,800,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 27,420,000.00 USD | 27,420,000.00 USD | 0.00 USD | 47,340.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 27,360,000.00 USD | 27,360,000.00 USD | 0.00 USD | 2,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 45,720,000.00 USD | 45,720,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 27,360,000.00 USD | 27,360,000.00 USD | 0.00 USD | 1,530.00 USD | 57,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 45,720,000.00 USD | 45,720,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 27,300,000.00 USD | 27,300,000.00 USD | 66,330.00 USD | 29,190.00 USD | 56,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 45,710,000.00 USD | 45,710,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 268,460.00 USD | 19,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 27,150,000.00 USD | 27,150,000.00 USD | 0.00 USD | 783.15 USD | 104,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 27,050,000.00 USD | 27,050,000.00 USD | 0.00 USD | 42,490.00 USD | 78,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 45,500,000.00 USD | 45,500,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 26,930,000.00 USD | 26,930,000.00 USD | 0.00 USD | 66,770.00 USD | 166,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 45,310,000.00 USD | 45,310,000.00 USD | 5,450.00 USD | 3,410.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 26,690,000.00 USD | 26,690,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 45,300,000.00 USD | 45,300,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 26,640,000.00 USD | 26,640,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 44,820,000.00 USD | 44,820,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 327,020.00 USD | 19,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.14` | 26,580,000.00 USD | 26,580,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 44,570,000.00 USD | 44,570,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 26,490,000.00 USD | 26,490,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 44,470,000.00 USD | 44,470,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 26,470,000.00 USD | 26,470,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 44,460,000.00 USD | 44,460,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 26,400,000.00 USD | 26,400,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 44,400,000.00 USD | 44,400,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 26,260,000.00 USD | 26,260,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 44,280,000.00 USD | 44,280,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 2,050,000.00 USD | 18,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 44,270,000.00 USD | 44,270,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 26,220,000.00 USD | 26,220,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 44,140,000.00 USD | 44,140,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 43,780,000.00 USD | 43,780,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 26,210,000.00 USD | 26,210,000.00 USD | 4,040.00 USD | 11,230.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 43,610,000.00 USD | 43,610,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 26,010,000.00 USD | 26,010,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 43,230,000.00 USD | 43,230,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 341,520.00 USD | 16,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 25,670,000.00 USD | 25,670,000.00 USD | 29,120.00 USD | 9,570.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 42,580,000.00 USD | 42,580,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 25,600,000.00 USD | 25,600,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 41,790,000.00 USD | 41,790,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 25,280,000.00 USD | 25,280,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 41,260,000.00 USD | 41,260,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 24,670,000.00 USD | 24,670,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 40,240,000.00 USD | 40,240,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 24,040,000.00 USD | 24,040,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 38,860,000.00 USD | 38,860,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,540,000.00 USD | 16,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 23,830,000.00 USD | 23,830,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 38,240,000.00 USD | 38,240,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 23,520,000.00 USD | 23,520,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 36,860,000.00 USD | 36,860,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 23,360,000.00 USD | 23,360,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 35,350,000.00 USD | 35,350,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 23,180,000.00 USD | 23,180,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 33,960,000.00 USD | 33,960,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 22,930,000.00 USD | 22,930,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 33,160,000.00 USD | 33,160,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 568,000.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 22,590,000.00 USD | 22,590,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 32,280,000.00 USD | 32,280,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 22,460,000.00 USD | 22,460,000.00 USD | 93,410.00 USD | 41,360.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 31,830,000.00 USD | 31,830,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 22,280,000.00 USD | 22,280,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 31,110,000.00 USD | 31,110,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 22,250,000.00 USD | 22,250,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 30,740,000.00 USD | 30,740,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 22,140,000.00 USD | 22,140,000.00 USD | 92,110.00 USD | 7,460.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 30,610,000.00 USD | 30,610,000.00 USD | 123,240.00 USD | 97,270.00 USD | 289,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 304,200.00 USD | 14,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 22,010,000.00 USD | 22,010,000.00 USD | 16,710.00 USD | 139,070.00 USD | 324,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 30,100,000.00 USD | 30,100,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 21,530,000.00 USD | 21,530,000.00 USD | 239,430.00 USD | 7,840.00 USD | 407,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 29,320,000.00 USD | 29,320,000.00 USD | 182,110.00 USD | 132,500.00 USD | 276,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 20,870,000.00 USD | 20,870,000.00 USD | 48,220.00 USD | 10,480.00 USD | 202,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 28,730,000.00 USD | 28,730,000.00 USD | 152,830.00 USD | 265,920.00 USD | 471,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 20,610,000.00 USD | 20,610,000.00 USD | 37,320.00 USD | 217,630.00 USD | 87,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 27,840,000.00 USD | 27,840,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 20,270,000.00 USD | 20,270,000.00 USD | 18,390.00 USD | 21,090.00 USD | 48,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 27,180,000.00 USD | 27,180,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 375,200.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 20,180,000.00 USD | 20,180,000.00 USD | 3,560.00 USD | 3,620.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 26,470,000.00 USD | 26,470,000.00 USD | 5,350.00 USD | 102,680.00 USD | 187,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 20,170,000.00 USD | 20,170,000.00 USD | 66,960.00 USD | 22,280.00 USD | 291,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 26,170,000.00 USD | 26,170,000.00 USD | 67,200.00 USD | 158,480.00 USD | 738,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 19,790,000.00 USD | 19,790,000.00 USD | 169,810.00 USD | 250,260.00 USD | 180,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 25,210,000.00 USD | 25,210,000.00 USD | 243,240.00 USD | 225,970.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 19,190,000.00 USD | 19,190,000.00 USD | 102,120.00 USD | 4,970.00 USD | 260,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 24,730,000.00 USD | 24,730,000.00 USD | 202,570.00 USD | 146,780.00 USD | 534,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 18,820,000.00 USD | 18,820,000.00 USD | 4,360.00 USD | 297,650.00 USD | 195,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 23,840,000.00 USD | 23,840,000.00 USD | 0.00 USD | 17,680.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 1,260,000.00 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 18,330,000.00 USD | 18,330,000.00 USD | 81,900.00 USD | 32,170.00 USD | 415,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 23,750,000.00 USD | 23,750,000.00 USD | 80,450.00 USD | 7,260.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 17,800,000.00 USD | 17,800,000.00 USD | 220,830.00 USD | 67,350.00 USD | 14,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 23,650,000.00 USD | 23,650,000.00 USD | 659,990.00 USD | 518,690.00 USD | 368,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 17,490,000.00 USD | 17,490,000.00 USD | 99,310.00 USD | 425,250.00 USD | 731,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 22,100,000.00 USD | 22,100,000.00 USD | 180,260.00 USD | 264,440.00 USD | 802,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 16,240,000.00 USD | 16,240,000.00 USD | 419,060.00 USD | 162,630.00 USD | 692,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 20,850,000.00 USD | 20,850,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 14,960,000.00 USD | 14,960,000.00 USD | 166,960.00 USD | 6,610.00 USD | 96,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 20,450,000.00 USD | 20,450,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 11,700,000.00 USD | 12,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.22` | 14,690,000.00 USD | 14,690,000.00 USD | 118,950.00 USD | 5,680.00 USD | 467,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 20,280,000.00 USD | 20,280,000.00 USD | 157,620.00 USD | 396,140.00 USD | 396,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 14,100,000.00 USD | 14,100,000.00 USD | 261,180.00 USD | 419,370.00 USD | 178,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 19,320,000.00 USD | 19,320,000.00 USD | 256,390.00 USD | 4,120.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 13,240,000.00 USD | 13,240,000.00 USD | 19,340.00 USD | 8,500.00 USD | 228,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 19,020,000.00 USD | 19,020,000.00 USD | 159,150.00 USD | 10,480.00 USD | 328,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 12,990,000.00 USD | 12,990,000.00 USD | 141,030.00 USD | 525,900.00 USD | 394,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 18,520,000.00 USD | 18,520,000.00 USD | 0.00 USD | 205,130.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 11,920,000.00 USD | 11,920,000.00 USD | 828,850.00 USD | 352,590.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 17,280,000.00 USD | 17,280,000.00 USD | 1,040,000.00 USD | 788,680.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 522,070.00 USD | 752,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.23` | 7,990,000.00 USD | 7,990,000.00 USD | 344,500.00 USD | 161,310.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 14,390,000.00 USD | 14,390,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 6,450,000.00 USD | 6,450,000.00 USD | 105,710.00 USD | 213,020.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 13,930,000.00 USD | 13,930,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 5,050,000.00 USD | 5,050,000.00 USD | 319,240.00 USD | 1,170,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 11,040,000.00 USD | 11,040,000.00 USD | 782,590.00 USD | 485,710.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 3,560,000.00 USD | 3,560,000.00 USD | 281,800.00 USD | 269,520.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 9,760,000.00 USD | 9,760,000.00 USD | 1,040,000.00 USD | 597,200.00 USD | 112,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 1,980,000.00 USD | 1,980,000.00 USD | 433,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 8,010,000.00 USD | 8,010,000.00 USD | 996,240.00 USD | 998,790.00 USD | 66,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 230,790.00 USD | 230,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 1,550,000.00 USD | 1,550,000.00 USD | 267,830.00 USD | 542,950.00 USD | 739,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 5,950,000.00 USD | 5,950,000.00 USD | 1,640,000.00 USD | 1,500,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.24` | 1,660,000.00 USD | 1,660,000.00 USD | 663,280.00 USD | 998,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.24` | 3,320,000.00 USD | 3,320,000.00 USD | 663,280.00 USD | 998,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.24` | 3,410,000.00 USD | 3,410,000.00 USD | 2,610,000.00 USD | 799,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.24` | 6,810,000.00 USD | 6,810,000.00 USD | 2,610,000.00 USD | 799,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.24` | 9,010,000.00 USD | 9,010,000.00 USD | 1,820,000.00 USD | 374,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.24` | 4,980,000.00 USD | 4,980,000.00 USD | 321,060.00 USD | 774,420.00 USD | 560,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.24` | 9,910,000.00 USD | 9,910,000.00 USD | 896,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 8,580,000.00 USD | 8,580,000.00 USD | 1,270,000.00 USD | 269,400.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 14,270,000.00 USD | 14,270,000.00 USD | 3,440,000.00 USD | 923,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 9,760,000.00 USD | 9,760,000.00 USD | 1,100,000.00 USD | 81,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 16,600,000.00 USD | 16,600,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 16,740,000.00 USD | 16,740,000.00 USD | 140,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 10,360,000.00 USD | 10,360,000.00 USD | 202,510.00 USD | 0.00 USD | 392,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 16,920,000.00 USD | 16,920,000.00 USD | 180,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 532,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 17,860,000.00 USD | 17,860,000.00 USD | 74,170.00 USD | 0.00 USD | 860,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 11,690,000.00 USD | 11,690,000.00 USD | 794,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 18,050,000.00 USD | 18,050,000.00 USD | 172,030.00 USD | 0.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.25` | 3,050.00 USD | 3,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.26` | 12,760,000.00 USD | 12,760,000.00 USD | 803,540.00 USD | 73,080.00 USD | 193,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 12,850,000.00 USD | 12,850,000.00 USD | 86,570.00 USD | 3,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 18,150,000.00 USD | 18,150,000.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 14,930,000.00 USD | 14,930,000.00 USD | 331,210.00 USD | 66,520.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 381,520.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 18,290,000.00 USD | 18,290,000.00 USD | 1,050,000.00 USD | 696,320.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 24,660,000.00 USD | 24,660,000.00 USD | 834,020.00 USD | 799,870.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 21,930,000.00 USD | 21,930,000.00 USD | 367,910.00 USD | 757,570.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 31,600,000.00 USD | 31,600,000.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 459.20 USD | 3,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.27` | 24,180,000.00 USD | 24,180,000.00 USD | 39,860.00 USD | 1,080,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 45,230,000.00 USD | 45,230,000.00 USD | 2,620,000.00 USD | 2,370,000.00 USD | 8,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 26,250,000.00 USD | 26,250,000.00 USD | 0.00 USD | 2,070,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 50,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 29,170,000.00 USD | 29,170,000.00 USD | 334,080.00 USD | 807,870.00 USD | 1,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 53,550,000.00 USD | 53,550,000.00 USD | 943,110.00 USD | 2,480,000.00 USD | 123,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 32,060,000.00 USD | 32,060,000.00 USD | 1,860,000.00 USD | 358,480.00 USD | 678,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 58,320,000.00 USD | 58,320,000.00 USD | 186,960.00 USD | 3,990,000.00 USD | 591,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 38,610,000.00 USD | 38,610,000.00 USD | 778,390.00 USD | 2,410,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 74,760,000.00 USD | 74,760,000.00 USD | 4,840,000.00 USD | 2,340,000.00 USD | 9,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 21,960.00 USD | 25,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 49,180,000.00 USD | 49,180,000.00 USD | 3,100,000.00 USD | 2,940,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 93,030,000.00 USD | 93,030,000.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 56,910,000.00 USD | 56,910,000.00 USD | 3,180,000.00 USD | 2,210,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 99,320,000.00 USD | 99,320,000.00 USD | 3,260,000.00 USD | 1,940,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 58,240,000.00 USD | 58,240,000.00 USD | 209,970.00 USD | 608,220.00 USD | 507,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 100,280,000.00 USD | 100,280,000.00 USD | 0.00 USD | 879,610.00 USD | 79,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 61,100,000.00 USD | 61,100,000.00 USD | 1,120,000.00 USD | 199,040.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 102,280,000.00 USD | 102,280,000.00 USD | 1,460,000.00 USD | 478,060.00 USD | 67,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 63,130,000.00 USD | 63,130,000.00 USD | 421,680.00 USD | 611,360.00 USD | 993,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 105,880,000.00 USD | 105,880,000.00 USD | 639,910.00 USD | 1,380,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 89,170.00 USD | 114,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 65,040,000.00 USD | 65,040,000.00 USD | 726,790.00 USD | 768,570.00 USD | 418,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 107,040,000.00 USD | 107,040,000.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 65,360,000.00 USD | 65,360,000.00 USD | 210,950.00 USD | 7,740.00 USD | 98,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 107,160,000.00 USD | 107,160,000.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 65,660,000.00 USD | 65,660,000.00 USD | 151,350.00 USD | 0.00 USD | 154,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 109,450,000.00 USD | 109,450,000.00 USD | 1,060,000.00 USD | 198,070.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 68,550,000.00 USD | 68,550,000.00 USD | 546,160.00 USD | 195,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 109,870,000.00 USD | 109,870,000.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 74,470,000.00 USD | 74,470,000.00 USD | 1,800,000.00 USD | 626,060.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 119,500,000.00 USD | 119,500,000.00 USD | 3,350,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 16,570.00 USD | 131,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 76,700,000.00 USD | 76,700,000.00 USD | 501,280.00 USD | 633,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 120,740,000.00 USD | 120,740,000.00 USD | 209,360.00 USD | 398,190.00 USD | 628,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 77,420,000.00 USD | 77,420,000.00 USD | 321,680.00 USD | 109,620.00 USD | 291,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 122,800,000.00 USD | 122,800,000.00 USD | 0.00 USD | 100,810.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 79,550,000.00 USD | 79,550,000.00 USD | 443,890.00 USD | 332,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 124,460,000.00 USD | 124,460,000.00 USD | 208,510.00 USD | 486,620.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 81,270,000.00 USD | 81,270,000.00 USD | 587,440.00 USD | 869,380.00 USD | 260,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 127,560,000.00 USD | 127,560,000.00 USD | 0.00 USD | 2,610,000.00 USD | 485,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 82,540,000.00 USD | 82,540,000.00 USD | 304,340.00 USD | 649,450.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 127,560,000.00 USD | 127,560,000.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 11,730.00 USD | 142,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 84,830,000.00 USD | 84,830,000.00 USD | 689,960.00 USD | 147,250.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 130,570,000.00 USD | 130,570,000.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 88,070,000.00 USD | 88,070,000.00 USD | 1,130,000.00 USD | 330,750.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 135,020,000.00 USD | 135,020,000.00 USD | 1,670,000.00 USD | 1,060,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 90,390,000.00 USD | 90,390,000.00 USD | 876,130.00 USD | 869,070.00 USD | 573,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 138,280,000.00 USD | 138,280,000.00 USD | 839,350.00 USD | 430,210.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 93,320,000.00 USD | 93,320,000.00 USD | 1,320,000.00 USD | 664,910.00 USD | 944,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 141,130,000.00 USD | 141,130,000.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 96,250,000.00 USD | 96,250,000.00 USD | 372,630.00 USD | 454,810.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 143,580,000.00 USD | 143,580,000.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 4,010.00 USD | 146,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 102,760,000.00 USD | 102,760,000.00 USD | 1,320,000.00 USD | 1,640,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 148,210,000.00 USD | 148,210,000.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 107,840,000.00 USD | 107,840,000.00 USD | 1,740,000.00 USD | 836,160.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 151,290,000.00 USD | 151,290,000.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 111,340,000.00 USD | 111,340,000.00 USD | 1,650,000.00 USD | 652,780.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 153,120,000.00 USD | 153,120,000.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 115,930,000.00 USD | 115,930,000.00 USD | 1,990,000.00 USD | 583,250.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 157,580,000.00 USD | 157,580,000.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 117,930,000.00 USD | 117,930,000.00 USD | 1,080,000.00 USD | 287,760.00 USD | 625,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 159,940,000.00 USD | 159,940,000.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 58,110.00 USD | 205,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 120,460,000.00 USD | 120,460,000.00 USD | 664,210.00 USD | 621,550.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 160,480,000.00 USD | 160,480,000.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 122,700,000.00 USD | 122,700,000.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 161,640,000.00 USD | 161,640,000.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 125,550,000.00 USD | 125,550,000.00 USD | 848,670.00 USD | 298,810.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 163,360,000.00 USD | 163,360,000.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 127,940,000.00 USD | 127,940,000.00 USD | 1,040,000.00 USD | 190,550.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 167,410,000.00 USD | 167,410,000.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 130,020,000.00 USD | 130,020,000.00 USD | 859,040.00 USD | 354,550.00 USD | 872,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 167,950,000.00 USD | 167,950,000.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 2,660.00 USD | 207,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 132,000,000.00 USD | 132,000,000.00 USD | 829,900.00 USD | 219,260.00 USD | 927,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 169,900,000.00 USD | 169,900,000.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 134,490,000.00 USD | 134,490,000.00 USD | 1,100,000.00 USD | 370,350.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 172,250,000.00 USD | 172,250,000.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 136,510,000.00 USD | 136,510,000.00 USD | 1,040,000.00 USD | 387,310.00 USD | 592,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 176,950,000.00 USD | 176,950,000.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 139,770,000.00 USD | 139,770,000.00 USD | 1,410,000.00 USD | 693,530.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 182,600,000.00 USD | 182,600,000.00 USD | 1,700,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 141,530,000.00 USD | 141,530,000.00 USD | 584,400.00 USD | 416,300.00 USD | 762,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 193,560,000.00 USD | 193,560,000.00 USD | 3,600,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 19,520.00 USD | 227,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 142,580,000.00 USD | 142,580,000.00 USD | 355,660.00 USD | 234,160.00 USD | 458,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 200,510,000.00 USD | 200,510,000.00 USD | 2,310,000.00 USD | 2,170,000.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 144,070,000.00 USD | 144,070,000.00 USD | 749,450.00 USD | 149,380.00 USD | 591,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 210,760,000.00 USD | 210,760,000.00 USD | 4,290,000.00 USD | 1,640,000.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 145,090,000.00 USD | 145,090,000.00 USD | 471,590.00 USD | 126,450.00 USD | 425,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 218,470,000.00 USD | 218,470,000.00 USD | 2,580,000.00 USD | 1,380,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 146,650,000.00 USD | 146,650,000.00 USD | 660,420.00 USD | 332,480.00 USD | 562,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 226,800,000.00 USD | 226,800,000.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 147,520,000.00 USD | 147,520,000.00 USD | 217,930.00 USD | 79,810.00 USD | 571,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 235,030,000.00 USD | 235,030,000.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 3,870.00 USD | 231,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 148,460,000.00 USD | 148,460,000.00 USD | 391,410.00 USD | 17,220.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 239,120,000.00 USD | 239,120,000.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 148,800,000.00 USD | 148,800,000.00 USD | 213,710.00 USD | 42,480.00 USD | 84,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 242,910,000.00 USD | 242,910,000.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 149,540,000.00 USD | 149,540,000.00 USD | 277,960.00 USD | 149,990.00 USD | 316,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 245,040,000.00 USD | 245,040,000.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 149,880,000.00 USD | 149,880,000.00 USD | 171,250.00 USD | 2,260.00 USD | 166,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 249,140,000.00 USD | 249,140,000.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 150,000,000.00 USD | 150,000,000.00 USD | 0.00 USD | 26,460.00 USD | 87,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 250,860,000.00 USD | 250,860,000.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 261,360.00 USD | 492,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 150,330,000.00 USD | 150,330,000.00 USD | 53,740.00 USD | 104,420.00 USD | 171,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 251,350,000.00 USD | 251,350,000.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 150,520,000.00 USD | 150,520,000.00 USD | 121,310.00 USD | 2,250.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 252,770,000.00 USD | 252,770,000.00 USD | 528,490.00 USD | 135,750.00 USD | 753,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 150,710,000.00 USD | 150,710,000.00 USD | 1,740.00 USD | 67,780.00 USD | 119,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 253,930,000.00 USD | 253,930,000.00 USD | 334,560.00 USD | 372,470.00 USD | 461,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 150,910,000.00 USD | 150,910,000.00 USD | 75,340.00 USD | 1,780.00 USD | 126,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 256,400,000.00 USD | 256,400,000.00 USD | 821,620.00 USD | 376,730.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 151,190,000.00 USD | 151,190,000.00 USD | 120,880.00 USD | 30,080.00 USD | 125,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 258,200,000.00 USD | 258,200,000.00 USD | 536,130.00 USD | 295,850.00 USD | 969,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 220.00 USD | 492,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.38` | 151,590,000.00 USD | 151,590,000.00 USD | 93,260.00 USD | 50,590.00 USD | 254,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 259,700,000.00 USD | 259,700,000.00 USD | 617,230.00 USD | 330,890.00 USD | 552,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 152,130,000.00 USD | 152,130,000.00 USD | 226,690.00 USD | 110,480.00 USD | 207,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 261,840,000.00 USD | 261,840,000.00 USD | 579,450.00 USD | 290,350.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 152,250,000.00 USD | 152,250,000.00 USD | 49,970.00 USD | 65,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 264,380,000.00 USD | 264,380,000.00 USD | 1,210,000.00 USD | 331,990.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 152,410,000.00 USD | 152,410,000.00 USD | 0.00 USD | 1,250.00 USD | 166,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 265,470,000.00 USD | 265,470,000.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 152,470,000.00 USD | 152,470,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 266,760,000.00 USD | 266,760,000.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,280.00 USD | 493,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 152,520,000.00 USD | 152,520,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 267,300,000.00 USD | 267,300,000.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 152,610,000.00 USD | 152,610,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 268,400,000.00 USD | 268,400,000.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 268,570,000.00 USD | 268,570,000.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 152,630,000.00 USD | 152,630,000.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 268,890,000.00 USD | 268,890,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 269,060,000.00 USD | 269,060,000.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 4,180.00 USD | 498,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 269,180,000.00 USD | 269,180,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 269,190,000.00 USD | 269,190,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 269,320,000.00 USD | 269,320,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 269,440,000.00 USD | 269,440,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 269,680,000.00 USD | 269,680,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 795.23 USD | 498,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 269,850,000.00 USD | 269,850,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 270,230,000.00 USD | 270,230,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 270,880,000.00 USD | 270,880,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 271,050,000.00 USD | 271,050,000.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 271,680,000.00 USD | 271,680,000.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,600.00 USD | 502,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.42` | 272,200,000.00 USD | 272,200,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 273,220,000.00 USD | 273,220,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 274,600,000.00 USD | 274,600,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 275,230,000.00 USD | 275,230,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 275,590,000.00 USD | 275,590,000.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,960.00 USD | 596,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.43` | 276,600,000.00 USD | 276,600,000.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 278,110,000.00 USD | 278,110,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 279,500,000.00 USD | 279,500,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 280,300,000.00 USD | 280,300,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 280,830,000.00 USD | 280,830,000.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 14,610.00 USD | 611,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 281,180,000.00 USD | 281,180,000.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 281,640,000.00 USD | 281,640,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 282,350,000.00 USD | 282,350,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 282,730,000.00 USD | 282,730,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 282,860,000.00 USD | 282,860,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 125,510.00 USD | 736,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.45` | 282,980,000.00 USD | 282,980,000.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 283,310,000.00 USD | 283,310,000.00 USD | 62,180.00 USD | 96,050.00 USD | 173,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 283,920,000.00 USD | 283,920,000.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 284,480,000.00 USD | 284,480,000.00 USD | 182,110.00 USD | 128,180.00 USD | 249,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 284,940,000.00 USD | 284,940,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.46` | 1,590.00 USD | 738,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.46` | 285,100,000.00 USD | 285,100,000.00 USD | 85,350.00 USD | 51,250.00 USD | 20,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 285,570,000.00 USD | 285,570,000.00 USD | 119,110.00 USD | 56,610.00 USD | 296,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 285,780,000.00 USD | 285,780,000.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.47` | 130,050.00 USD | 868,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 583,330.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 23,580.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 915.06 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 300.42 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 776.71 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 2,130.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 6,800.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 127,650.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,900.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 123.63 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 4,380,000.00 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 108.21 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 271.38 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 3,530.00 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 2,350.00 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 177.55 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 6,190.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 110.17 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 4,150.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 3,410.00 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,870.00 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 6,280.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 5,280,000.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 129,540.00 USD | 11,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 2,850.00 USD | 11,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 1,240.00 USD | 11,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 851.24 USD | 11,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 6,160.00 USD | 11,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 266.07 USD | 11,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 9,340.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 100,220.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,040.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 2,890,000.00 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 313,400.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 16,680.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 552.45 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 794.73 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 8,870.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 2,990,000.00 USD | 17,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 244,080.00 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.99` | 1,570.00 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 120.30 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 1,390.00 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 1,550.00 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 2,720,000.00 USD | 20,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 1,880.00 USD | 20,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 419,330.00 USD | 21,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 248,040.00 USD | 21,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,650.00 USD | 21,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 2,400,000.00 USD | 23,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 23,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 12,800.00 USD | 23,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 301.53 USD | 23,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 746.30 USD | 23,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 326.34 USD | 23,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 2,960.00 USD | 23,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 645.25 USD | 23,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 309.81 USD | 23,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 76,900.00 USD | 23,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 209.30 USD | 23,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 11,620.00 USD | 23,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 147,750.00 USD | 24,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 64,500.00 USD | 24,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 220,670.00 USD | 24,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 1,550.00 USD | 24,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 199.32 USD | 24,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 4,300.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 2,510.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 109.25 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 155.68 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 481.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 30,440.00 USD | 24,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 1,380.00 USD | 24,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 94,050.00 USD | 24,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 337.96 USD | 24,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 114.77 USD | 24,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 73,040,000.00 USD | 0.00 USD | 1,270.00 USD | `-79.52%` | `4,993.00` |
| `Live` | `Long` | `0.2650` | 73,040,000.00 USD | 0.00 USD | 25,540.00 USD | `-78.71%` | `96,370.00` |
| `Live` | `Long` | `0.2750` | 73,020,000.00 USD | 0.00 USD | 1,250.00 USD | `-77.91%` | `4,528.00` |
| `Live` | `Long` | `0.2850` | 73,010,000.00 USD | 0.00 USD | 111,160.00 USD | `-77.11%` | `390,050.00` |
| `Live` | `Long` | `0.2950` | 72,900,000.00 USD | 0.00 USD | 1,480,000.00 USD | `-76.31%` | `5,026,731.00` |
| `Live` | `Long` | `0.3050` | 71,420,000.00 USD | 0.00 USD | 4,320.00 USD | `-75.50%` | `14,152.00` |
| `Live` | `Long` | `0.3150` | 71,420,000.00 USD | 0.00 USD | 5,010.00 USD | `-74.70%` | `15,902.00` |
| `Live` | `Long` | `0.3250` | 71,410,000.00 USD | 0.00 USD | 15,720.00 USD | `-73.90%` | `48,379.00` |
| `Live` | `Long` | `0.3350` | 71,400,000.00 USD | 0.00 USD | 376.88 USD | `-73.09%` | `1,125.00` |
| `Live` | `Long` | `0.3450` | 71,400,000.00 USD | 0.00 USD | 517.50 USD | `-72.29%` | `1,500.00` |
| `Live` | `Long` | `0.3550` | 71,390,000.00 USD | 0.00 USD | 3,520.00 USD | `-71.49%` | `9,915.00` |
| `Live` | `Long` | `0.3650` | 71,390,000.00 USD | 0.00 USD | 3,560.00 USD | `-70.68%` | `9,752.00` |
| `Live` | `Long` | `0.3750` | 71,390,000.00 USD | 0.00 USD | 183.00 USD | `-69.88%` | `488.00` |
| `Live` | `Long` | `0.3850` | 71,390,000.00 USD | 0.00 USD | 503,890.00 USD | `-69.08%` | `1,308,812.00` |
| `Live` | `Long` | `0.3950` | 70,880,000.00 USD | 0.00 USD | 174.59 USD | `-68.27%` | `442.00` |
| `Live` | `Long` | `0.4050` | 70,880,000.00 USD | 0.00 USD | 612.36 USD | `-67.47%` | `1,512.00` |
| `Live` | `Long` | `0.4150` | 70,880,000.00 USD | 0.00 USD | 810.91 USD | `-66.67%` | `1,954.00` |
| `Live` | `Long` | `0.4250` | 70,880,000.00 USD | 0.00 USD | 297.50 USD | `-65.86%` | `700.00` |
| `Live` | `Long` | `0.4350` | 70,880,000.00 USD | 0.00 USD | 8,710.00 USD | `-65.06%` | `20,024.00` |
| `Live` | `Long` | `0.4450` | 70,870,000.00 USD | 0.00 USD | 1,070.00 USD | `-64.26%` | `2,400.00` |
| `Live` | `Long` | `0.4550` | 70,870,000.00 USD | 0.00 USD | 10,030.00 USD | `-63.45%` | `22,037.00` |
| `Live` | `Long` | `0.4750` | 70,860,000.00 USD | 0.00 USD | 198.55 USD | `-61.85%` | `418.00` |
| `Live` | `Long` | `0.4850` | 70,860,000.00 USD | 0.00 USD | 1,870.00 USD | `-61.04%` | `3,846.00` |
| `Live` | `Long` | `0.5050` | 70,860,000.00 USD | 0.00 USD | 8,100.00 USD | `-59.44%` | `16,046.00` |
| `Live` | `Long` | `0.5150` | 70,850,000.00 USD | 0.00 USD | 175.10 USD | `-58.63%` | `340.00` |
| `Live` | `Long` | `0.5250` | 70,850,000.00 USD | 0.00 USD | 6,590.00 USD | `-57.83%` | `12,557.00` |
| `Live` | `Long` | `0.5350` | 70,840,000.00 USD | 0.00 USD | 985.47 USD | `-57.03%` | `1,842.00` |
| `Live` | `Long` | `0.5450` | 70,840,000.00 USD | 0.00 USD | 2,740.00 USD | `-56.22%` | `5,024.00` |
| `Live` | `Long` | `0.5550` | 70,840,000.00 USD | 0.00 USD | 6,220.00 USD | `-55.42%` | `11,216.00` |
| `Live` | `Long` | `0.5650` | 70,830,000.00 USD | 0.00 USD | 2,060.00 USD | `-54.62%` | `3,651.00` |
| `Live` | `Long` | `0.5750` | 70,830,000.00 USD | 0.00 USD | 171,380.00 USD | `-53.82%` | `298,059.00` |
| `Live` | `Long` | `0.5850` | 70,660,000.00 USD | 0.00 USD | 34,990.00 USD | `-53.01%` | `59,818.00` |
| `Live` | `Long` | `0.5950` | 70,630,000.00 USD | 0.00 USD | 5,160.00 USD | `-52.21%` | `8,679.00` |
| `Live` | `Long` | `0.6050` | 70,620,000.00 USD | 0.00 USD | 23,750.00 USD | `-51.41%` | `39,260.00` |
| `Live` | `Long` | `0.6150` | 70,600,000.00 USD | 0.00 USD | 36,660.00 USD | `-50.60%` | `59,614.00` |
| `Live` | `Long` | `0.6250` | 70,560,000.00 USD | 0.00 USD | 1,440.00 USD | `-49.80%` | `2,303.00` |
| `Live` | `Long` | `0.6350` | 70,560,000.00 USD | 0.00 USD | 11,440.00 USD | `-49.00%` | `18,014.00` |
| `Live` | `Long` | `0.6450` | 70,550,000.00 USD | 0.00 USD | 21,480.00 USD | `-48.19%` | `33,302.00` |
| `Live` | `Long` | `0.6550` | 70,530,000.00 USD | 0.00 USD | 1,030.00 USD | `-47.39%` | `1,579.00` |
| `Live` | `Long` | `0.6650` | 70,530,000.00 USD | 0.00 USD | 27,220.00 USD | `-46.59%` | `40,929.00` |
| `Live` | `Long` | `0.6750` | 70,500,000.00 USD | 0.00 USD | 30,660.00 USD | `-45.78%` | `45,429.00` |
| `Live` | `Long` | `0.6850` | 70,470,000.00 USD | 0.00 USD | 2,810.00 USD | `-44.98%` | `4,104.00` |
| `Live` | `Long` | `0.6950` | 70,460,000.00 USD | 0.00 USD | 3,780.00 USD | `-44.18%` | `5,435.00` |
| `Live` | `Long` | `0.7050` | 70,460,000.00 USD | 0.00 USD | 182,630.00 USD | `-43.37%` | `259,047.00` |
| `Live` | `Long` | `0.7150` | 70,280,000.00 USD | 0.00 USD | 68,160.00 USD | `-42.57%` | `95,327.00` |
| `Live` | `Long` | `0.7250` | 70,210,000.00 USD | 0.00 USD | 223,880.00 USD | `-41.77%` | `308,796.00` |
| `Live` | `Long` | `0.7350` | 69,990,000.00 USD | 0.00 USD | 36,750.00 USD | `-40.96%` | `49,994.00` |
| `Live` | `Long` | `0.7450` | 69,950,000.00 USD | 0.00 USD | 52,300.00 USD | `-40.16%` | `70,200.00` |
| `Live` | `Long` | `0.7550` | 69,900,000.00 USD | 0.00 USD | 92,400.00 USD | `-39.36%` | `122,387.00` |
| `Live` | `Long` | `0.7650` | 69,800,000.00 USD | 0.00 USD | 4,070.00 USD | `-38.55%` | `5,321.00` |
| `Live` | `Long` | `0.7750` | 69,800,000.00 USD | 0.00 USD | 32,360.00 USD | `-37.75%` | `41,752.00` |
| `Live` | `Long` | `0.7850` | 69,770,000.00 USD | 0.00 USD | 80,500.00 USD | `-36.95%` | `102,546.00` |
| `Live` | `Long` | `0.7950` | 69,690,000.00 USD | 0.00 USD | 11,250.00 USD | `-36.14%` | `14,145.00` |
| `Live` | `Long` | `0.8050` | 69,680,000.00 USD | 0.00 USD | 14,340.00 USD | `-35.34%` | `17,811.00` |
| `Live` | `Long` | `0.8150` | 69,660,000.00 USD | 0.00 USD | 22,410.00 USD | `-34.54%` | `27,499.00` |
| `Live` | `Long` | `0.8250` | 69,640,000.00 USD | 0.00 USD | 906.68 USD | `-33.73%` | `1,099.00` |
| `Live` | `Long` | `0.8350` | 69,640,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-32.93%` | `3,592,037.00` |
| `Live` | `Long` | `0.8450` | 66,640,000.00 USD | 0.00 USD | 82,680.00 USD | `-32.13%` | `97,848.00` |
| `Live` | `Long` | `0.8550` | 66,560,000.00 USD | 0.00 USD | 87,630.00 USD | `-31.33%` | `102,496.00` |
| `Live` | `Long` | `0.8650` | 66,470,000.00 USD | 0.00 USD | 50,330.00 USD | `-30.52%` | `58,187.00` |
| `Live` | `Long` | `0.8750` | 66,420,000.00 USD | 0.00 USD | 85,410.00 USD | `-29.72%` | `97,610.00` |
| `Live` | `Long` | `0.8850` | 66,330,000.00 USD | 0.00 USD | 380,130.00 USD | `-28.92%` | `429,531.00` |
| `Live` | `Long` | `0.8950` | 65,950,000.00 USD | 0.00 USD | 99,910.00 USD | `-28.11%` | `111,636.00` |
| `Live` | `Long` | `0.9050` | 65,850,000.00 USD | 0.00 USD | 211,180.00 USD | `-27.31%` | `233,352.00` |
| `Live` | `Long` | `0.9150` | 65,640,000.00 USD | 0.00 USD | 75,210.00 USD | `-26.51%` | `82,195.00` |
| `Live` | `Long` | `0.9250` | 65,570,000.00 USD | 0.00 USD | 73,840.00 USD | `-25.70%` | `79,826.00` |
| `Live` | `Long` | `0.9350` | 65,490,000.00 USD | 0.00 USD | 89,340.00 USD | `-24.90%` | `95,555.00` |
| `Live` | `Long` | `0.9450` | 65,400,000.00 USD | 0.00 USD | 121,380.00 USD | `-24.10%` | `128,442.00` |
| `Live` | `Long` | `0.9550` | 65,280,000.00 USD | 0.00 USD | 116,660.00 USD | `-23.29%` | `122,162.00` |
| `Live` | `Long` | `0.9650` | 65,170,000.00 USD | 0.00 USD | 33,880,000.00 USD | `-22.49%` | `35,113,160.00` |
| `Live` | `Long` | `0.9750` | 31,280,000.00 USD | 0.00 USD | 150,030.00 USD | `-21.69%` | `153,875.00` |
| `Live` | `Long` | `0.9850` | 31,130,000.00 USD | 0.00 USD | 456,880.00 USD | `-20.88%` | `463,839.00` |
| `Live` | `Long` | `0.9950` | 30,670,000.00 USD | 0.00 USD | 90,130.00 USD | `-20.08%` | `90,583.00` |
| `Live` | `Long` | `1.00` | 30,580,000.00 USD | 0.00 USD | 440,870.00 USD | `-19.28%` | `438,676.00` |
| `Live` | `Long` | `1.01` | 30,140,000.00 USD | 0.00 USD | 867,160.00 USD | `-18.47%` | `854,345.00` |
| `Live` | `Long` | `1.02` | 29,280,000.00 USD | 0.00 USD | 2,690,000.00 USD | `-17.67%` | `2,620,310.00` |
| `Live` | `Long` | `1.03` | 26,590,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-16.87%` | `2,049,721.00` |
| `Live` | `Long` | `1.04` | 24,470,000.00 USD | 0.00 USD | 689,860.00 USD | `-16.06%` | `660,151.00` |
| `Live` | `Long` | `1.05` | 23,780,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-15.26%` | `1,076,322.00` |
| `Live` | `Long` | `1.06` | 22,640,000.00 USD | 0.00 USD | 430,460.00 USD | `-14.46%` | `404,185.00` |
| `Live` | `Long` | `1.07` | 22,210,000.00 USD | 0.00 USD | 491,560.00 USD | `-13.65%` | `457,267.00` |
| `Live` | `Long` | `1.08` | 21,720,000.00 USD | 0.00 USD | 723,650.00 USD | `-12.85%` | `666,955.00` |
| `Live` | `Long` | `1.09` | 21,000,000.00 USD | 0.00 USD | 570,310.00 USD | `-12.05%` | `520,834.00` |
| `Live` | `Long` | `1.10` | 20,430,000.00 USD | 0.00 USD | 73,910.00 USD | `-11.24%` | `66,887.00` |
| `Live` | `Long` | `1.11` | 20,350,000.00 USD | 0.00 USD | 867,550.00 USD | `-10.44%` | `778,069.00` |
| `Live` | `Long` | `1.12` | 19,490,000.00 USD | 0.00 USD | 268,460.00 USD | `-9.64%` | `238,628.00` |
| `Live` | `Long` | `1.14` | 19,220,000.00 USD | 0.00 USD | 327,020.00 USD | `-8.84%` | `288,127.00` |
| `Live` | `Long` | `1.15` | 18,890,000.00 USD | 0.00 USD | 2,050,000.00 USD | `-8.03%` | `1,788,776.00` |
| `Live` | `Long` | `1.16` | 16,840,000.00 USD | 0.00 USD | 341,520.00 USD | `-7.23%` | `295,688.00` |
| `Live` | `Long` | `1.17` | 16,500,000.00 USD | 0.00 USD | 1,540,000.00 USD | `-6.43%` | `1,321,387.00` |
| `Live` | `Long` | `1.18` | 14,960,000.00 USD | 0.00 USD | 568,000.00 USD | `-5.62%` | `483,406.00` |
| `Live` | `Long` | `1.19` | 14,390,000.00 USD | 0.00 USD | 304,200.00 USD | `-4.82%` | `256,711.00` |
| `Live` | `Long` | `1.20` | 14,090,000.00 USD | 0.00 USD | 375,200.00 USD | `-4.02%` | `313,972.00` |
| `Live` | `Long` | `1.21` | 13,710,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-3.21%` | `1,043,831.00` |
| `Live` | `Long` | `1.22` | 12,460,000.00 USD | 0.00 USD | 11,700,000.00 USD | `-2.41%` | `9,632,828.00` |
| `Live` | `Long` | `1.23` | 752,860.00 USD | 0.00 USD | 522,070.00 USD | `-1.61%` | `426,178.00` |
| `Live` | `Long` | `1.24` | 230,790.00 USD | 0.00 USD | 230,790.00 USD | `-0.80%` | `186,878.00` |
| `Live` | `Short` | `1.25` | 3,050.00 USD | 3,050.00 USD | 0.00 USD | `+0.80%` | `2,433.00` |
| `Live` | `Short` | `1.26` | 3,510.00 USD | 459.20 USD | 0.00 USD | `+1.61%` | `363.00` |
| `Live` | `Short` | `1.27` | 25,470.00 USD | 21,960.00 USD | 0.00 USD | `+2.41%` | `17,220.00` |
| `Live` | `Short` | `1.28` | 114,640.00 USD | 89,170.00 USD | 0.00 USD | `+3.21%` | `69,395.00` |
| `Live` | `Short` | `1.29` | 131,210.00 USD | 16,570.00 USD | 0.00 USD | `+4.02%` | `12,792.00` |
| `Live` | `Short` | `1.30` | 142,940.00 USD | 11,730.00 USD | 0.00 USD | `+4.82%` | `8,988.00` |
| `Live` | `Short` | `1.31` | 146,950.00 USD | 4,010.00 USD | 0.00 USD | `+5.62%` | `3,050.00` |
| `Live` | `Short` | `1.32` | 205,060.00 USD | 58,110.00 USD | 0.00 USD | `+6.43%` | `43,856.00` |
| `Live` | `Short` | `1.33` | 207,720.00 USD | 2,660.00 USD | 0.00 USD | `+7.23%` | `1,995.00` |
| `Live` | `Short` | `1.34` | 227,240.00 USD | 19,520.00 USD | 0.00 USD | `+8.03%` | `14,512.00` |
| `Live` | `Short` | `1.35` | 231,110.00 USD | 3,870.00 USD | 0.00 USD | `+8.84%` | `2,858.00` |
| `Live` | `Short` | `1.36` | 492,470.00 USD | 261,360.00 USD | 0.00 USD | `+9.64%` | `191,474.00` |
| `Live` | `Short` | `1.38` | 492,690.00 USD | 220.00 USD | 0.00 USD | `+10.44%` | `160.00` |
| `Live` | `Short` | `1.39` | 493,970.00 USD | 1,280.00 USD | 0.00 USD | `+11.24%` | `921.00` |
| `Live` | `Short` | `1.40` | 498,150.00 USD | 4,180.00 USD | 0.00 USD | `+12.05%` | `3,000.00` |
| `Live` | `Short` | `1.41` | 498,950.00 USD | 795.23 USD | 0.00 USD | `+12.85%` | `566.00` |
| `Live` | `Short` | `1.42` | 502,550.00 USD | 3,600.00 USD | 0.00 USD | `+13.65%` | `2,544.00` |
| `Live` | `Short` | `1.43` | 596,510.00 USD | 93,960.00 USD | 0.00 USD | `+14.46%` | `65,937.00` |
| `Live` | `Short` | `1.44` | 611,120.00 USD | 14,610.00 USD | 0.00 USD | `+15.26%` | `10,180.00` |
| `Live` | `Short` | `1.45` | 736,630.00 USD | 125,510.00 USD | 0.00 USD | `+16.06%` | `86,861.00` |
| `Live` | `Short` | `1.46` | 738,220.00 USD | 1,590.00 USD | 0.00 USD | `+16.87%` | `1,090.00` |
| `Live` | `Short` | `1.47` | 868,270.00 USD | 130,050.00 USD | 0.00 USD | `+17.67%` | `88,774.00` |
| `Live` | `Short` | `1.49` | 1,450,000.00 USD | 583,330.00 USD | 0.00 USD | `+19.28%` | `392,815.00` |
| `Live` | `Short` | `1.50` | 1,480,000.00 USD | 23,580.00 USD | 0.00 USD | `+20.08%` | `15,772.00` |
| `Live` | `Short` | `1.51` | 1,480,000.00 USD | 915.06 USD | 0.00 USD | `+21.69%` | `604.00` |
| `Live` | `Short` | `1.52` | 1,480,000.00 USD | 300.42 USD | 0.00 USD | `+22.49%` | `197.00` |
| `Live` | `Short` | `1.53` | 1,480,000.00 USD | 776.71 USD | 0.00 USD | `+23.29%` | `506.00` |
| `Live` | `Short` | `1.54` | 1,480,000.00 USD | 2,130.00 USD | 0.00 USD | `+24.10%` | `1,377.00` |
| `Live` | `Short` | `1.55` | 1,490,000.00 USD | 6,800.00 USD | 0.00 USD | `+24.90%` | `4,373.00` |
| `Live` | `Short` | `1.56` | 1,610,000.00 USD | 127,650.00 USD | 0.00 USD | `+25.70%` | `81,565.00` |
| `Live` | `Short` | `1.57` | 1,620,000.00 USD | 2,900.00 USD | 0.00 USD | `+26.51%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 1,620,000.00 USD | 123.63 USD | 0.00 USD | `+27.31%` | `78.00` |
| `Live` | `Short` | `1.60` | 6,000,000.00 USD | 4,380,000.00 USD | 0.00 USD | `+28.92%` | `2,728,104.00` |
| `Live` | `Short` | `1.61` | 6,000,000.00 USD | 108.21 USD | 0.00 USD | `+29.72%` | `67.00` |
| `Live` | `Short` | `1.62` | 6,000,000.00 USD | 271.38 USD | 0.00 USD | `+30.52%` | `167.00` |
| `Live` | `Short` | `1.64` | 6,000,000.00 USD | 3,530.00 USD | 0.00 USD | `+31.33%` | `2,160.00` |
| `Live` | `Short` | `1.65` | 6,000,000.00 USD | 2,350.00 USD | 0.00 USD | `+32.13%` | `1,429.00` |
| `Live` | `Short` | `1.66` | 6,000,000.00 USD | 147.30 USD | 0.00 USD | `+32.93%` | `89.00` |
| `Live` | `Short` | `1.67` | 6,000,000.00 USD | 586.08 USD | 0.00 USD | `+33.73%` | `352.00` |
| `Live` | `Short` | `1.68` | 6,000,000.00 USD | 177.55 USD | 0.00 USD | `+34.54%` | `106.00` |
| `Live` | `Short` | `1.69` | 6,010,000.00 USD | 6,190.00 USD | 0.00 USD | `+35.34%` | `3,674.00` |
| `Live` | `Short` | `1.70` | 6,010,000.00 USD | 110.17 USD | 0.00 USD | `+36.14%` | `65.00` |
| `Live` | `Short` | `1.71` | 6,010,000.00 USD | 1,980.00 USD | 0.00 USD | `+36.95%` | `1,163.00` |
| `Live` | `Short` | `1.72` | 6,010,000.00 USD | 4,150.00 USD | 0.00 USD | `+37.75%` | `2,417.00` |
| `Live` | `Short` | `1.74` | 6,020,000.00 USD | 3,410.00 USD | 0.00 USD | `+39.36%` | `1,965.00` |
| `Live` | `Short` | `1.75` | 6,020,000.00 USD | 2,870.00 USD | 0.00 USD | `+40.16%` | `1,642.00` |
| `Live` | `Short` | `1.75` | 6,030,000.00 USD | 6,280.00 USD | 0.00 USD | `+40.96%` | `3,579.00` |
| `Live` | `Short` | `1.76` | 11,310,000.00 USD | 5,280,000.00 USD | 0.00 USD | `+41.77%` | `2,991,680.00` |
| `Live` | `Short` | `1.78` | 11,440,000.00 USD | 129,540.00 USD | 0.00 USD | `+43.37%` | `72,574.00` |
| `Live` | `Short` | `1.79` | 11,440,000.00 USD | 2,850.00 USD | 0.00 USD | `+44.18%` | `1,590.00` |
| `Live` | `Short` | `1.80` | 11,440,000.00 USD | 1,240.00 USD | 0.00 USD | `+44.98%` | `686.00` |
| `Live` | `Short` | `1.81` | 11,440,000.00 USD | 851.24 USD | 0.00 USD | `+45.78%` | `469.00` |
| `Live` | `Short` | `1.82` | 11,450,000.00 USD | 6,160.00 USD | 0.00 USD | `+46.59%` | `3,377.00` |
| `Live` | `Short` | `1.83` | 11,450,000.00 USD | 266.07 USD | 0.00 USD | `+47.39%` | `145.00` |
| `Live` | `Short` | `1.84` | 11,460,000.00 USD | 9,340.00 USD | 0.00 USD | `+48.19%` | `5,061.00` |
| `Live` | `Short` | `1.85` | 11,560,000.00 USD | 100,220.00 USD | 0.00 USD | `+49.00%` | `54,025.00` |
| `Live` | `Short` | `1.86` | 11,560,000.00 USD | 2,040.00 USD | 0.00 USD | `+49.80%` | `1,095.00` |
| `Live` | `Short` | `1.88` | 14,450,000.00 USD | 2,890,000.00 USD | 0.00 USD | `+50.60%` | `1,540,696.00` |
| `Live` | `Short` | `1.89` | 14,760,000.00 USD | 313,400.00 USD | 0.00 USD | `+51.41%` | `166,259.00` |
| `Live` | `Short` | `1.90` | 14,780,000.00 USD | 16,680.00 USD | 0.00 USD | `+52.21%` | `8,803.00` |
| `Live` | `Short` | `1.91` | 14,780,000.00 USD | 552.45 USD | 0.00 USD | `+53.01%` | `290.00` |
| `Live` | `Short` | `1.92` | 14,780,000.00 USD | 794.73 USD | 0.00 USD | `+53.82%` | `415.00` |
| `Live` | `Short` | `1.94` | 14,790,000.00 USD | 8,870.00 USD | 0.00 USD | `+55.42%` | `4,584.00` |
| `Live` | `Short` | `1.96` | 17,780,000.00 USD | 2,990,000.00 USD | 0.00 USD | `+57.03%` | `1,530,759.00` |
| `Live` | `Short` | `1.97` | 18,030,000.00 USD | 244,080.00 USD | 0.00 USD | `+57.83%` | `124,214.00` |
| `Live` | `Short` | `1.98` | 18,030,000.00 USD | 651.75 USD | 0.00 USD | `+58.63%` | `330.00` |
| `Live` | `Short` | `1.99` | 18,030,000.00 USD | 1,570.00 USD | 0.00 USD | `+59.44%` | `789.00` |
| `Live` | `Short` | `2.00` | 18,030,000.00 USD | 120.30 USD | 0.00 USD | `+61.04%` | `60.00` |
| `Live` | `Short` | `2.02` | 18,030,000.00 USD | 1,390.00 USD | 0.00 USD | `+61.85%` | `689.00` |
| `Live` | `Short` | `2.04` | 18,030,000.00 USD | 1,550.00 USD | 0.00 USD | `+64.26%` | `758.00` |
| `Live` | `Short` | `2.06` | 20,760,000.00 USD | 2,720,000.00 USD | 0.00 USD | `+65.86%` | `1,319,080.00` |
| `Live` | `Short` | `2.08` | 20,760,000.00 USD | 1,880.00 USD | 0.00 USD | `+66.67%` | `905.00` |
| `Live` | `Short` | `2.10` | 21,180,000.00 USD | 419,330.00 USD | 0.00 USD | `+68.27%` | `200,158.00` |
| `Live` | `Short` | `2.10` | 21,420,000.00 USD | 248,040.00 USD | 0.00 USD | `+69.08%` | `117,835.00` |
| `Live` | `Short` | `2.12` | 21,430,000.00 USD | 3,650.00 USD | 0.00 USD | `+69.88%` | `1,728.00` |
| `Live` | `Short` | `2.15` | 23,830,000.00 USD | 2,400,000.00 USD | 0.00 USD | `+72.29%` | `1,120,344.00` |
| `Live` | `Short` | `2.15` | 23,830,000.00 USD | 196.11 USD | 0.00 USD | `+73.09%` | `91.00` |
| `Live` | `Short` | `2.17` | 23,840,000.00 USD | 12,800.00 USD | 0.00 USD | `+74.70%` | `5,885.00` |
| `Live` | `Short` | `2.19` | 23,840,000.00 USD | 301.53 USD | 0.00 USD | `+75.50%` | `138.00` |
| `Live` | `Short` | `2.19` | 23,850,000.00 USD | 746.30 USD | 0.00 USD | `+76.31%` | `340.00` |
| `Live` | `Short` | `2.21` | 23,850,000.00 USD | 326.34 USD | 0.00 USD | `+77.11%` | `148.00` |
| `Live` | `Short` | `2.21` | 23,850,000.00 USD | 2,960.00 USD | 0.00 USD | `+77.91%` | `1,335.00` |
| `Live` | `Short` | `2.23` | 23,850,000.00 USD | 645.25 USD | 0.00 USD | `+78.71%` | `290.00` |
| `Live` | `Short` | `2.25` | 23,850,000.00 USD | 309.81 USD | 0.00 USD | `+80.32%` | `138.00` |
| `Live` | `Short` | `2.25` | 23,930,000.00 USD | 76,900.00 USD | 0.00 USD | `+81.12%` | `34,101.00` |
| `Live` | `Short` | `2.27` | 23,930,000.00 USD | 209.30 USD | 0.00 USD | `+82.73%` | `92.00` |
| `Live` | `Short` | `2.29` | 23,940,000.00 USD | 11,620.00 USD | 0.00 USD | `+84.34%` | `5,062.00` |
| `Live` | `Short` | `2.31` | 24,090,000.00 USD | 147,750.00 USD | 0.00 USD | `+85.14%` | `64,100.00` |
| `Live` | `Short` | `2.31` | 24,150,000.00 USD | 64,500.00 USD | 0.00 USD | `+85.94%` | `27,861.00` |
| `Live` | `Short` | `2.33` | 24,370,000.00 USD | 220,670.00 USD | 0.00 USD | `+86.75%` | `94,913.00` |
| `Live` | `Short` | `2.33` | 24,370,000.00 USD | 1,550.00 USD | 0.00 USD | `+87.55%` | `665.00` |
| `Live` | `Short` | `2.35` | 24,370,000.00 USD | 199.32 USD | 0.00 USD | `+88.35%` | `85.00` |
| `Live` | `Short` | `2.35` | 24,380,000.00 USD | 4,300.00 USD | 0.00 USD | `+89.16%` | `1,826.00` |
| `Live` | `Short` | `2.37` | 24,380,000.00 USD | 2,510.00 USD | 0.00 USD | `+89.96%` | `1,062.00` |
| `Live` | `Short` | `2.38` | 24,380,000.00 USD | 109.25 USD | 0.00 USD | `+90.76%` | `46.00` |
| `Live` | `Short` | `2.40` | 24,380,000.00 USD | 155.68 USD | 0.00 USD | `+92.37%` | `65.00` |
| `Live` | `Short` | `2.40` | 24,380,000.00 USD | 481.00 USD | 0.00 USD | `+93.17%` | `200.00` |
| `Live` | `Short` | `2.42` | 24,410,000.00 USD | 30,440.00 USD | 0.00 USD | `+94.78%` | `12,553.00` |
| `Live` | `Short` | `2.44` | 24,410,000.00 USD | 1,380.00 USD | 0.00 USD | `+95.58%` | `566.00` |
| `Live` | `Short` | `2.44` | 24,510,000.00 USD | 94,050.00 USD | 0.00 USD | `+96.39%` | `38,467.00` |
| `Live` | `Short` | `2.48` | 24,510,000.00 USD | 337.96 USD | 0.00 USD | `+99.60%` | `136.00` |
| `Live` | `Short` | `2.50` | 24,510,000.00 USD | 114.77 USD | 0.00 USD | `+100.40%` | `46.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 1,210,000.00 USD | 0.00 USD | 112.45 USD | `-79.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3650` | 1,210,000.00 USD | 0.00 USD | 351.50 USD | `-70.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 1,210,000.00 USD | 0.00 USD | 139.12 USD | `-69.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4050` | 1,210,000.00 USD | 0.00 USD | 2,950.00 USD | `-67.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 1,200,000.00 USD | 0.00 USD | 200.86 USD | `-66.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 1,200,000.00 USD | 0.00 USD | 408.51 USD | `-64.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 1,200,000.00 USD | 0.00 USD | 273.00 USD | `-63.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 1,200,000.00 USD | 0.00 USD | 151.12 USD | `-62.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 1,200,000.00 USD | 0.00 USD | 142.50 USD | `-61.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 1,200,000.00 USD | 0.00 USD | 145.50 USD | `-61.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 1,200,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 1,200,000.00 USD | 0.00 USD | 285.82 USD | `-58.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 1,200,000.00 USD | 0.00 USD | 306.60 USD | `-57.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 1,200,000.00 USD | 0.00 USD | 121.55 USD | `-55.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 1,200,000.00 USD | 0.00 USD | 374.60 USD | `-54.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 1,200,000.00 USD | 0.00 USD | 100.62 USD | `-53.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 1,200,000.00 USD | 0.00 USD | 203.75 USD | `-49.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 1,200,000.00 USD | 0.00 USD | 791.85 USD | `-49.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 1,200,000.00 USD | 0.00 USD | 573.40 USD | `-48.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 1,200,000.00 USD | 0.00 USD | 348.46 USD | `-47.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 1,200,000.00 USD | 0.00 USD | 3,220.00 USD | `-46.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 1,190,000.00 USD | 0.00 USD | 503.55 USD | `-45.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 1,190,000.00 USD | 0.00 USD | 480.19 USD | `-44.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 1,190,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 1,180,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 1,180,000.00 USD | 0.00 USD | 228.80 USD | `-42.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 1,180,000.00 USD | 0.00 USD | 536.50 USD | `-41.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 1,180,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 1,180,000.00 USD | 0.00 USD | 2,880.00 USD | `-38.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 1,170,000.00 USD | 0.00 USD | 1,080.00 USD | `-36.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 1,170,000.00 USD | 0.00 USD | 798.57 USD | `-31.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 1,170,000.00 USD | 0.00 USD | 690.38 USD | `-29.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 1,170,000.00 USD | 0.00 USD | 1,210.00 USD | `-28.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 1,170,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 1,170,000.00 USD | 0.00 USD | 838.94 USD | `-27.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 1,170,000.00 USD | 0.00 USD | 338.55 USD | `-26.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 1,170,000.00 USD | 0.00 USD | 1,060.00 USD | `-25.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 1,170,000.00 USD | 0.00 USD | 1,180.00 USD | `-24.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 1,160,000.00 USD | 0.00 USD | 112.46 USD | `-24.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 1,160,000.00 USD | 0.00 USD | 1,730.00 USD | `-23.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 1,160,000.00 USD | 0.00 USD | 3,910.00 USD | `-22.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 1,160,000.00 USD | 0.00 USD | 7,230.00 USD | `-21.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 1,150,000.00 USD | 0.00 USD | 5,000.00 USD | `-20.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 1,150,000.00 USD | 0.00 USD | 661.67 USD | `-20.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 1,150,000.00 USD | 0.00 USD | 16,020.00 USD | `-19.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 1,130,000.00 USD | 0.00 USD | 6,900.00 USD | `-18.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 1,120,000.00 USD | 0.00 USD | 2,020.00 USD | `-17.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 1,120,000.00 USD | 0.00 USD | 38,000.00 USD | `-16.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 1,080,000.00 USD | 0.00 USD | 1,900.00 USD | `-16.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 1,080,000.00 USD | 0.00 USD | 2,110.00 USD | `-15.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,080,000.00 USD | 0.00 USD | 3,960.00 USD | `-14.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,070,000.00 USD | 0.00 USD | 48,460.00 USD | `-13.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,030,000.00 USD | 0.00 USD | 1,680.00 USD | `-12.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,020,000.00 USD | 0.00 USD | 38,150.00 USD | `-12.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 986,590.00 USD | 0.00 USD | 6,230.00 USD | `-11.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 980,350.00 USD | 0.00 USD | 9,120.00 USD | `-10.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 971,240.00 USD | 0.00 USD | 80,050.00 USD | `-9.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 891,190.00 USD | 0.00 USD | 13,830.00 USD | `-8.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 877,360.00 USD | 0.00 USD | 14,460.00 USD | `-8.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 862,890.00 USD | 0.00 USD | 30,960.00 USD | `-7.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 831,940.00 USD | 0.00 USD | 41,740.00 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 790,200.00 USD | 0.00 USD | 9,750.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 780,440.00 USD | 0.00 USD | 154,560.00 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 625,880.00 USD | 0.00 USD | 144,420.00 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 481,470.00 USD | 0.00 USD | 118,240.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 363,230.00 USD | 0.00 USD | 218,120.00 USD | `-2.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 145,110.00 USD | 0.00 USD | 71,740.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 73,370.00 USD | 0.00 USD | 72,570.00 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 798.05 USD | 0.00 USD | 798.05 USD | `+0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 3,440.00 USD | 3,440.00 USD | 0.00 USD | `+0.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 122,780.00 USD | 119,340.00 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 131,760.00 USD | 8,980.00 USD | 0.00 USD | `+2.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 374,550.00 USD | 242,800.00 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 439,500.00 USD | 64,940.00 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 483,730.00 USD | 44,230.00 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 902,100.00 USD | 418,370.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,100,000.00 USD | 201,670.00 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,140,000.00 USD | 38,980.00 USD | 0.00 USD | `+7.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,350,000.00 USD | 209,840.00 USD | 0.00 USD | `+8.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,370,000.00 USD | 15,250.00 USD | 0.00 USD | `+8.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,640,000.00 USD | 275,680.00 USD | 0.00 USD | `+9.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,730,000.00 USD | 83,030.00 USD | 0.00 USD | `+10.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,780,000.00 USD | 50,450.00 USD | 0.00 USD | `+11.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,780,000.00 USD | 6,060.00 USD | 0.00 USD | `+12.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 6,140,000.00 USD | 4,360,000.00 USD | 0.00 USD | `+12.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 6,140,000.00 USD | 1,980.00 USD | 0.00 USD | `+13.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 6,150,000.00 USD | 5,790.00 USD | 0.00 USD | `+14.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,230,000.00 USD | 79,310.00 USD | 0.00 USD | `+15.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,450,000.00 USD | 222,430.00 USD | 0.00 USD | `+16.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,460,000.00 USD | 7,510.00 USD | 0.00 USD | `+16.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,480,000.00 USD | 22,800.00 USD | 0.00 USD | `+17.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,590,000.00 USD | 107,960.00 USD | 0.00 USD | `+18.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,640,000.00 USD | 55,700.00 USD | 0.00 USD | `+19.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,660,000.00 USD | 13,980.00 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,710,000.00 USD | 57,630.00 USD | 0.00 USD | `+20.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,720,000.00 USD | 10,320.00 USD | 0.00 USD | `+21.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,820,000.00 USD | 93,330.00 USD | 0.00 USD | `+22.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,860,000.00 USD | 45,620.00 USD | 0.00 USD | `+23.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,890,000.00 USD | 22,220.00 USD | 0.00 USD | `+24.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,890,000.00 USD | 2,690.00 USD | 0.00 USD | `+24.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,900,000.00 USD | 7,340.00 USD | 0.00 USD | `+25.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,900,000.00 USD | 5,940.00 USD | 0.00 USD | `+26.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,910,000.00 USD | 12,880.00 USD | 0.00 USD | `+27.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 7,060,000.00 USD | 149,190.00 USD | 0.00 USD | `+28.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 7,070,000.00 USD | 1,840.00 USD | 0.00 USD | `+28.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 7,150,000.00 USD | 80,320.00 USD | 0.00 USD | `+29.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 7,150,000.00 USD | 464.75 USD | 0.00 USD | `+30.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,330,000.00 USD | 184,610.00 USD | 0.00 USD | `+31.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,330,000.00 USD | 2,670.00 USD | 0.00 USD | `+32.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,350,000.00 USD | 19,450.00 USD | 0.00 USD | `+32.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,360,000.00 USD | 6,080.00 USD | 0.00 USD | `+33.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,380,000.00 USD | 18,400.00 USD | 0.00 USD | `+34.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,450,000.00 USD | 70,850.00 USD | 0.00 USD | `+35.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,450,000.00 USD | 3,190.00 USD | 0.00 USD | `+36.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,690,000.00 USD | 240,380.00 USD | 0.00 USD | `+36.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,710,000.00 USD | 14,030.00 USD | 0.00 USD | `+37.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,710,000.00 USD | 5,910.00 USD | 0.00 USD | `+38.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,760,000.00 USD | 44,100.00 USD | 0.00 USD | `+39.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,760,000.00 USD | 4,710.00 USD | 0.00 USD | `+40.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,770,000.00 USD | 5,510.00 USD | 0.00 USD | `+40.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,790,000.00 USD | 21,720.00 USD | 0.00 USD | `+41.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,910,000.00 USD | 124,780.00 USD | 0.00 USD | `+42.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 8,010,000.00 USD | 96,600.00 USD | 0.00 USD | `+43.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 8,050,000.00 USD | 38,570.00 USD | 0.00 USD | `+44.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 8,050,000.00 USD | 254.51 USD | 0.00 USD | `+44.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 8,050,000.00 USD | 2,530.00 USD | 0.00 USD | `+45.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 8,050,000.00 USD | 1,830.00 USD | 0.00 USD | `+46.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 8,060,000.00 USD | 7,280.00 USD | 0.00 USD | `+47.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 8,060,000.00 USD | 1,010.00 USD | 0.00 USD | `+48.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 8,070,000.00 USD | 8,390.00 USD | 0.00 USD | `+49.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 8,070,000.00 USD | 4,250.00 USD | 0.00 USD | `+50.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 8,070,000.00 USD | 591.89 USD | 0.00 USD | `+51.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 8,110,000.00 USD | 38,610.00 USD | 0.00 USD | `+52.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 8,120,000.00 USD | 9,270.00 USD | 0.00 USD | `+53.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 8,130,000.00 USD | 7,410.00 USD | 0.00 USD | `+53.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 8,130,000.00 USD | 265.10 USD | 0.00 USD | `+55.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 8,130,000.00 USD | 2,040.00 USD | 0.00 USD | `+56.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 8,130,000.00 USD | 1,070.00 USD | 0.00 USD | `+57.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,150,000.00 USD | 14,120.00 USD | 0.00 USD | `+57.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,150,000.00 USD | 4,010.00 USD | 0.00 USD | `+58.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,150,000.00 USD | 325.54 USD | 0.00 USD | `+59.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,160,000.00 USD | 7,020.00 USD | 0.00 USD | `+60.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,280,000.00 USD | 123,150.00 USD | 0.00 USD | `+61.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,280,000.00 USD | 781.82 USD | 0.00 USD | `+61.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,280,000.00 USD | 222.75 USD | 0.00 USD | `+62.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,280,000.00 USD | 862.84 USD | 0.00 USD | `+63.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,280,000.00 USD | 382.41 USD | 0.00 USD | `+64.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,290,000.00 USD | 3,420.00 USD | 0.00 USD | `+65.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,290,000.00 USD | 661.93 USD | 0.00 USD | `+66.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,410,000.00 USD | 124,400.00 USD | 0.00 USD | `+68.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,410,000.00 USD | 1,580.00 USD | 0.00 USD | `+69.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,430,000.00 USD | 13,900.00 USD | 0.00 USD | `+70.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,450,000.00 USD | 24,840.00 USD | 0.00 USD | `+72.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,500,000.00 USD | 50,580.00 USD | 0.00 USD | `+73.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,510,000.00 USD | 2,690.00 USD | 0.00 USD | `+73.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,530,000.00 USD | 20,370.00 USD | 0.00 USD | `+76.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,680,000.00 USD | 151,380.00 USD | 0.00 USD | `+77.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 8,680,000.00 USD | 7,340.00 USD | 0.00 USD | `+79.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,690,000.00 USD | 3,120.00 USD | 0.00 USD | `+82.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,690,000.00 USD | 1,140.00 USD | 0.00 USD | `+83.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,700,000.00 USD | 12,150.00 USD | 0.00 USD | `+84.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,700,000.00 USD | 370.40 USD | 0.00 USD | `+85.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,700,000.00 USD | 733.19 USD | 0.00 USD | `+87.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,700,000.00 USD | 2,410.00 USD | 0.00 USD | `+89.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,710,000.00 USD | 475.00 USD | 0.00 USD | `+90.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,710,000.00 USD | 2,540.00 USD | 0.00 USD | `+92.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,710,000.00 USD | 1,590.00 USD | 0.00 USD | `+93.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,710,000.00 USD | 1,370.00 USD | 0.00 USD | `+93.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,730,000.00 USD | 19,590.00 USD | 0.00 USD | `+94.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,740,000.00 USD | 4,580.00 USD | 0.00 USD | `+95.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,740,000.00 USD | 8,110.00 USD | 0.00 USD | `+97.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,750,000.00 USD | 3,420.00 USD | 0.00 USD | `+99.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,750,000.00 USD | 124.75 USD | 0.00 USD | `+100.40%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `1.11` | 27,640,000.00 USD | 0.00 USD | 27,640,000.00 USD | 17,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.11` | 45,830,000.00 USD | 0.00 USD | 45,830,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.11` | 27,620,000.00 USD | 0.00 USD | 27,620,000.00 USD | 18,710.00 USD | 0.00 USD | 121,720.00 USD |
| `1D` | `1.11` | 27,480,000.00 USD | 0.00 USD | 27,480,000.00 USD | 0.00 USD | 2,260.00 USD | 0.00 USD |
| `7D` | `1.11` | 45,810,000.00 USD | 0.00 USD | 45,810,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `1D` | `1.12` | 27,480,000.00 USD | 0.00 USD | 27,480,000.00 USD | 0.00 USD | 0.00 USD | 61,610.00 USD |
| `7D` | `1.12` | 45,800,000.00 USD | 0.00 USD | 45,800,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 27,420,000.00 USD | 0.00 USD | 27,420,000.00 USD | 0.00 USD | 47,340.00 USD | 5,360.00 USD |
| `1D` | `1.12` | 27,360,000.00 USD | 0.00 USD | 27,360,000.00 USD | 0.00 USD | 2,250.00 USD | 0.00 USD |
| `7D` | `1.12` | 45,720,000.00 USD | 0.00 USD | 45,720,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `1.12` | 27,360,000.00 USD | 0.00 USD | 27,360,000.00 USD | 0.00 USD | 1,530.00 USD | 57,100.00 USD |
| `7D` | `1.12` | 45,720,000.00 USD | 0.00 USD | 45,720,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD |
| `1D` | `1.12` | 27,300,000.00 USD | 0.00 USD | 27,300,000.00 USD | 66,330.00 USD | 29,190.00 USD | 56,030.00 USD |
| `7D` | `1.12` | 45,710,000.00 USD | 0.00 USD | 45,710,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.13` | 27,150,000.00 USD | 0.00 USD | 27,150,000.00 USD | 0.00 USD | 783.15 USD | 104,240.00 USD |
| `1D` | `1.13` | 27,050,000.00 USD | 0.00 USD | 27,050,000.00 USD | 0.00 USD | 42,490.00 USD | 78,200.00 USD |
| `7D` | `1.13` | 45,500,000.00 USD | 0.00 USD | 45,500,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 26,930,000.00 USD | 0.00 USD | 26,930,000.00 USD | 0.00 USD | 66,770.00 USD | 166,310.00 USD |
| `7D` | `1.13` | 45,310,000.00 USD | 0.00 USD | 45,310,000.00 USD | 5,450.00 USD | 3,410.00 USD | 3,970.00 USD |
| `1D` | `1.13` | 26,690,000.00 USD | 0.00 USD | 26,690,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD |
| `7D` | `1.13` | 45,300,000.00 USD | 0.00 USD | 45,300,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD |
| `1D` | `1.14` | 26,640,000.00 USD | 0.00 USD | 26,640,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD |
| `7D` | `1.14` | 44,820,000.00 USD | 0.00 USD | 44,820,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD |
| `1D` | `1.14` | 26,580,000.00 USD | 0.00 USD | 26,580,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD |
| `7D` | `1.14` | 44,570,000.00 USD | 0.00 USD | 44,570,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 26,490,000.00 USD | 0.00 USD | 26,490,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.14` | 44,470,000.00 USD | 0.00 USD | 44,470,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 26,470,000.00 USD | 0.00 USD | 26,470,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD |
| `7D` | `1.14` | 44,460,000.00 USD | 0.00 USD | 44,460,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 26,400,000.00 USD | 0.00 USD | 26,400,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD |
| `7D` | `1.14` | 44,400,000.00 USD | 0.00 USD | 44,400,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.15` | 26,260,000.00 USD | 0.00 USD | 26,260,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD |
| `7D` | `1.15` | 44,280,000.00 USD | 0.00 USD | 44,280,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.15` | 44,270,000.00 USD | 0.00 USD | 44,270,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `1D` | `1.15` | 26,220,000.00 USD | 0.00 USD | 26,220,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 44,140,000.00 USD | 0.00 USD | 44,140,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD |
| `7D` | `1.15` | 43,780,000.00 USD | 0.00 USD | 43,780,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.15` | 26,210,000.00 USD | 0.00 USD | 26,210,000.00 USD | 4,040.00 USD | 11,230.00 USD | 185,060.00 USD |
| `7D` | `1.15` | 43,610,000.00 USD | 0.00 USD | 43,610,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `1D` | `1.16` | 26,010,000.00 USD | 0.00 USD | 26,010,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD |
| `7D` | `1.16` | 43,230,000.00 USD | 0.00 USD | 43,230,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `1D` | `1.16` | 25,670,000.00 USD | 0.00 USD | 25,670,000.00 USD | 29,120.00 USD | 9,570.00 USD | 31,170.00 USD |
| `7D` | `1.16` | 42,580,000.00 USD | 0.00 USD | 42,580,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD |
| `1D` | `1.16` | 25,600,000.00 USD | 0.00 USD | 25,600,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD |
| `7D` | `1.16` | 41,790,000.00 USD | 0.00 USD | 41,790,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `1D` | `1.16` | 25,280,000.00 USD | 0.00 USD | 25,280,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD |
| `7D` | `1.16` | 41,260,000.00 USD | 0.00 USD | 41,260,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.16` | 24,670,000.00 USD | 0.00 USD | 24,670,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD |
| `7D` | `1.16` | 40,240,000.00 USD | 0.00 USD | 40,240,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.17` | 24,040,000.00 USD | 0.00 USD | 24,040,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD |
| `7D` | `1.17` | 38,860,000.00 USD | 0.00 USD | 38,860,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.17` | 23,830,000.00 USD | 0.00 USD | 23,830,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD |
| `7D` | `1.17` | 38,240,000.00 USD | 0.00 USD | 38,240,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD |
| `1D` | `1.17` | 23,520,000.00 USD | 0.00 USD | 23,520,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD |
| `7D` | `1.17` | 36,860,000.00 USD | 0.00 USD | 36,860,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 23,360,000.00 USD | 0.00 USD | 23,360,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD |
| `7D` | `1.17` | 35,350,000.00 USD | 0.00 USD | 35,350,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 23,180,000.00 USD | 0.00 USD | 23,180,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD |
| `7D` | `1.17` | 33,960,000.00 USD | 0.00 USD | 33,960,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.18` | 22,930,000.00 USD | 0.00 USD | 22,930,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD |
| `7D` | `1.18` | 33,160,000.00 USD | 0.00 USD | 33,160,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD |
| `1D` | `1.18` | 22,590,000.00 USD | 0.00 USD | 22,590,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD |
| `7D` | `1.18` | 32,280,000.00 USD | 0.00 USD | 32,280,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `1D` | `1.18` | 22,460,000.00 USD | 0.00 USD | 22,460,000.00 USD | 93,410.00 USD | 41,360.00 USD | 49,320.00 USD |
| `7D` | `1.18` | 31,830,000.00 USD | 0.00 USD | 31,830,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `1D` | `1.18` | 22,280,000.00 USD | 0.00 USD | 22,280,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD |
| `7D` | `1.18` | 31,110,000.00 USD | 0.00 USD | 31,110,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `1D` | `1.18` | 22,250,000.00 USD | 0.00 USD | 22,250,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD |
| `7D` | `1.18` | 30,740,000.00 USD | 0.00 USD | 30,740,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `1D` | `1.19` | 22,140,000.00 USD | 0.00 USD | 22,140,000.00 USD | 92,110.00 USD | 7,460.00 USD | 27,490.00 USD |
| `7D` | `1.19` | 30,610,000.00 USD | 0.00 USD | 30,610,000.00 USD | 123,240.00 USD | 97,270.00 USD | 289,750.00 USD |
| `1D` | `1.19` | 22,010,000.00 USD | 0.00 USD | 22,010,000.00 USD | 16,710.00 USD | 139,070.00 USD | 324,370.00 USD |
| `7D` | `1.19` | 30,100,000.00 USD | 0.00 USD | 30,100,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD |
| `1D` | `1.19` | 21,530,000.00 USD | 0.00 USD | 21,530,000.00 USD | 239,430.00 USD | 7,840.00 USD | 407,470.00 USD |
| `7D` | `1.19` | 29,320,000.00 USD | 0.00 USD | 29,320,000.00 USD | 182,110.00 USD | 132,500.00 USD | 276,980.00 USD |
| `1D` | `1.19` | 20,870,000.00 USD | 0.00 USD | 20,870,000.00 USD | 48,220.00 USD | 10,480.00 USD | 202,220.00 USD |
| `7D` | `1.19` | 28,730,000.00 USD | 0.00 USD | 28,730,000.00 USD | 152,830.00 USD | 265,920.00 USD | 471,430.00 USD |
| `1D` | `1.19` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 37,320.00 USD | 217,630.00 USD | 87,350.00 USD |
| `7D` | `1.19` | 27,840,000.00 USD | 0.00 USD | 27,840,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD |
| `1D` | `1.20` | 20,270,000.00 USD | 0.00 USD | 20,270,000.00 USD | 18,390.00 USD | 21,090.00 USD | 48,430.00 USD |
| `7D` | `1.20` | 27,180,000.00 USD | 0.00 USD | 27,180,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 20,180,000.00 USD | 0.00 USD | 20,180,000.00 USD | 3,560.00 USD | 3,620.00 USD | 3,770.00 USD |
| `7D` | `1.20` | 26,470,000.00 USD | 0.00 USD | 26,470,000.00 USD | 5,350.00 USD | 102,680.00 USD | 187,830.00 USD |
| `1D` | `1.20` | 20,170,000.00 USD | 0.00 USD | 20,170,000.00 USD | 66,960.00 USD | 22,280.00 USD | 291,610.00 USD |
| `7D` | `1.20` | 26,170,000.00 USD | 0.00 USD | 26,170,000.00 USD | 67,200.00 USD | 158,480.00 USD | 738,030.00 USD |
| `1D` | `1.20` | 19,790,000.00 USD | 0.00 USD | 19,790,000.00 USD | 169,810.00 USD | 250,260.00 USD | 180,340.00 USD |
| `7D` | `1.20` | 25,210,000.00 USD | 0.00 USD | 25,210,000.00 USD | 243,240.00 USD | 225,970.00 USD | 15,030.00 USD |
| `1D` | `1.20` | 19,190,000.00 USD | 0.00 USD | 19,190,000.00 USD | 102,120.00 USD | 4,970.00 USD | 260,610.00 USD |
| `7D` | `1.20` | 24,730,000.00 USD | 0.00 USD | 24,730,000.00 USD | 202,570.00 USD | 146,780.00 USD | 534,000.00 USD |
| `1D` | `1.21` | 18,820,000.00 USD | 0.00 USD | 18,820,000.00 USD | 4,360.00 USD | 297,650.00 USD | 195,510.00 USD |
| `7D` | `1.21` | 23,840,000.00 USD | 0.00 USD | 23,840,000.00 USD | 0.00 USD | 17,680.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 18,330,000.00 USD | 0.00 USD | 18,330,000.00 USD | 81,900.00 USD | 32,170.00 USD | 415,780.00 USD |
| `7D` | `1.21` | 23,750,000.00 USD | 0.00 USD | 23,750,000.00 USD | 80,450.00 USD | 7,260.00 USD | 9,940.00 USD |
| `1D` | `1.21` | 17,800,000.00 USD | 0.00 USD | 17,800,000.00 USD | 220,830.00 USD | 67,350.00 USD | 14,960.00 USD |
| `7D` | `1.21` | 23,650,000.00 USD | 0.00 USD | 23,650,000.00 USD | 659,990.00 USD | 518,690.00 USD | 368,310.00 USD |
| `1D` | `1.21` | 17,490,000.00 USD | 0.00 USD | 17,490,000.00 USD | 99,310.00 USD | 425,250.00 USD | 731,080.00 USD |
| `7D` | `1.21` | 22,100,000.00 USD | 0.00 USD | 22,100,000.00 USD | 180,260.00 USD | 264,440.00 USD | 802,150.00 USD |
| `1D` | `1.21` | 16,240,000.00 USD | 0.00 USD | 16,240,000.00 USD | 419,060.00 USD | 162,630.00 USD | 692,340.00 USD |
| `7D` | `1.21` | 20,850,000.00 USD | 0.00 USD | 20,850,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD |
| `1D` | `1.22` | 14,960,000.00 USD | 0.00 USD | 14,960,000.00 USD | 166,960.00 USD | 6,610.00 USD | 96,140.00 USD |
| `7D` | `1.22` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD |
| `1D` | `1.22` | 14,690,000.00 USD | 0.00 USD | 14,690,000.00 USD | 118,950.00 USD | 5,680.00 USD | 467,110.00 USD |
| `7D` | `1.22` | 20,280,000.00 USD | 0.00 USD | 20,280,000.00 USD | 157,620.00 USD | 396,140.00 USD | 396,840.00 USD |
| `1D` | `1.22` | 14,100,000.00 USD | 0.00 USD | 14,100,000.00 USD | 261,180.00 USD | 419,370.00 USD | 178,880.00 USD |
| `7D` | `1.22` | 19,320,000.00 USD | 0.00 USD | 19,320,000.00 USD | 256,390.00 USD | 4,120.00 USD | 40,620.00 USD |
| `1D` | `1.22` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 19,340.00 USD | 8,500.00 USD | 228,420.00 USD |
| `7D` | `1.22` | 19,020,000.00 USD | 0.00 USD | 19,020,000.00 USD | 159,150.00 USD | 10,480.00 USD | 328,940.00 USD |
| `1D` | `1.22` | 12,990,000.00 USD | 0.00 USD | 12,990,000.00 USD | 141,030.00 USD | 525,900.00 USD | 394,250.00 USD |
| `7D` | `1.22` | 18,520,000.00 USD | 0.00 USD | 18,520,000.00 USD | 0.00 USD | 205,130.00 USD | 1,040,000.00 USD |
| `1D` | `1.23` | 11,920,000.00 USD | 0.00 USD | 11,920,000.00 USD | 828,850.00 USD | 352,590.00 USD | 2,750,000.00 USD |
| `7D` | `1.23` | 17,280,000.00 USD | 0.00 USD | 17,280,000.00 USD | 1,040,000.00 USD | 788,680.00 USD | 1,050,000.00 USD |
| `1D` | `1.23` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 344,500.00 USD | 161,310.00 USD | 1,030,000.00 USD |
| `7D` | `1.23` | 14,390,000.00 USD | 0.00 USD | 14,390,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD |
| `1D` | `1.23` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 105,710.00 USD | 213,020.00 USD | 1,080,000.00 USD |
| `7D` | `1.23` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,790,000.00 USD |
| `1D` | `1.23` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 319,240.00 USD | 1,170,000.00 USD | 0.00 USD |
| `7D` | `1.23` | 11,040,000.00 USD | 0.00 USD | 11,040,000.00 USD | 782,590.00 USD | 485,710.00 USD | 8,010.00 USD |
| `1D` | `1.23` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 281,800.00 USD | 269,520.00 USD | 1,030,000.00 USD |
| `7D` | `1.23` | 9,760,000.00 USD | 0.00 USD | 9,760,000.00 USD | 1,040,000.00 USD | 597,200.00 USD | 112,990.00 USD |
| `1D` | `1.24` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 433,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.24` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 996,240.00 USD | 998,790.00 USD | 66,130.00 USD |
| `1D` | `1.24` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 267,830.00 USD | 542,950.00 USD | 739,970.00 USD |
| `7D` | `1.24` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 1,640,000.00 USD | 1,500,000.00 USD | 2,820,000.00 USD |
| `1D` | `1.24` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 663,280.00 USD | 998,910.00 USD | 0.00 USD |
| `1D` | `1.24` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 663,280.00 USD | 998,910.00 USD | 0.00 USD |
| `7D` | `1.24` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 2,610,000.00 USD | 799,870.00 USD | 0.00 USD |
| `7D` | `1.24` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 2,610,000.00 USD | 799,870.00 USD | 0.00 USD |
| `7D` | `1.24` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 1,820,000.00 USD | 374,420.00 USD | 0.00 USD |
| `1D` | `1.24` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 321,060.00 USD | 774,420.00 USD | 560,940.00 USD |
| `7D` | `1.24` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 896,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 1,270,000.00 USD | 269,400.00 USD | 2,050,000.00 USD |
| `7D` | `1.25` | 14,270,000.00 USD | 14,270,000.00 USD | 0.00 USD | 3,440,000.00 USD | 923,130.00 USD | 0.00 USD |
| `1D` | `1.25` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 1,100,000.00 USD | 81,840.00 USD | 0.00 USD |
| `7D` | `1.25` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 16,740,000.00 USD | 16,740,000.00 USD | 0.00 USD | 140,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 202,510.00 USD | 0.00 USD | 392,980.00 USD |
| `7D` | `1.25` | 16,920,000.00 USD | 16,920,000.00 USD | 0.00 USD | 180,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 532,200.00 USD |
| `7D` | `1.25` | 17,860,000.00 USD | 17,860,000.00 USD | 0.00 USD | 74,170.00 USD | 0.00 USD | 860,180.00 USD |
| `1D` | `1.25` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 794,390.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 18,050,000.00 USD | 18,050,000.00 USD | 0.00 USD | 172,030.00 USD | 0.00 USD | 18,740.00 USD |
| `1D` | `1.26` | 12,760,000.00 USD | 12,760,000.00 USD | 0.00 USD | 803,540.00 USD | 73,080.00 USD | 193,710.00 USD |
| `1D` | `1.26` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 86,570.00 USD | 3,600.00 USD | 0.00 USD |
| `7D` | `1.26` | 18,150,000.00 USD | 18,150,000.00 USD | 0.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 331,210.00 USD | 66,520.00 USD | 1,690,000.00 USD |
| `7D` | `1.26` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 0.00 USD | 381,520.00 USD | 2,580,000.00 USD |
| `1D` | `1.26` | 18,290,000.00 USD | 18,290,000.00 USD | 0.00 USD | 1,050,000.00 USD | 696,320.00 USD | 1,610,000.00 USD |
| `7D` | `1.26` | 24,660,000.00 USD | 24,660,000.00 USD | 0.00 USD | 834,020.00 USD | 799,870.00 USD | 1,910,000.00 USD |
| `1D` | `1.26` | 21,930,000.00 USD | 21,930,000.00 USD | 0.00 USD | 367,910.00 USD | 757,570.00 USD | 2,520,000.00 USD |
| `7D` | `1.26` | 31,600,000.00 USD | 31,600,000.00 USD | 0.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD |
| `1D` | `1.27` | 24,180,000.00 USD | 24,180,000.00 USD | 0.00 USD | 39,860.00 USD | 1,080,000.00 USD | 1,130,000.00 USD |
| `7D` | `1.27` | 45,230,000.00 USD | 45,230,000.00 USD | 0.00 USD | 2,620,000.00 USD | 2,370,000.00 USD | 8,640,000.00 USD |
| `1D` | `1.27` | 26,250,000.00 USD | 26,250,000.00 USD | 0.00 USD | 0.00 USD | 2,070,000.00 USD | 0.00 USD |
| `7D` | `1.27` | 50,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD |
| `1D` | `1.27` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 334,080.00 USD | 807,870.00 USD | 1,780,000.00 USD |
| `7D` | `1.27` | 53,550,000.00 USD | 53,550,000.00 USD | 0.00 USD | 943,110.00 USD | 2,480,000.00 USD | 123,930.00 USD |
| `1D` | `1.27` | 32,060,000.00 USD | 32,060,000.00 USD | 0.00 USD | 1,860,000.00 USD | 358,480.00 USD | 678,140.00 USD |
| `7D` | `1.27` | 58,320,000.00 USD | 58,320,000.00 USD | 0.00 USD | 186,960.00 USD | 3,990,000.00 USD | 591,560.00 USD |
| `1D` | `1.27` | 38,610,000.00 USD | 38,610,000.00 USD | 0.00 USD | 778,390.00 USD | 2,410,000.00 USD | 3,350,000.00 USD |
| `7D` | `1.27` | 74,760,000.00 USD | 74,760,000.00 USD | 0.00 USD | 4,840,000.00 USD | 2,340,000.00 USD | 9,260,000.00 USD |
| `1D` | `1.28` | 49,180,000.00 USD | 49,180,000.00 USD | 0.00 USD | 3,100,000.00 USD | 2,940,000.00 USD | 4,520,000.00 USD |
| `7D` | `1.28` | 93,030,000.00 USD | 93,030,000.00 USD | 0.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 56,910,000.00 USD | 56,910,000.00 USD | 0.00 USD | 3,180,000.00 USD | 2,210,000.00 USD | 2,350,000.00 USD |
| `7D` | `1.28` | 99,320,000.00 USD | 99,320,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,940,000.00 USD | 1,090,000.00 USD |
| `1D` | `1.28` | 58,240,000.00 USD | 58,240,000.00 USD | 0.00 USD | 209,970.00 USD | 608,220.00 USD | 507,970.00 USD |
| `7D` | `1.28` | 100,280,000.00 USD | 100,280,000.00 USD | 0.00 USD | 0.00 USD | 879,610.00 USD | 79,220.00 USD |
| `1D` | `1.28` | 61,100,000.00 USD | 61,100,000.00 USD | 0.00 USD | 1,120,000.00 USD | 199,040.00 USD | 1,540,000.00 USD |
| `7D` | `1.28` | 102,280,000.00 USD | 102,280,000.00 USD | 0.00 USD | 1,460,000.00 USD | 478,060.00 USD | 67,480.00 USD |
| `1D` | `1.28` | 63,130,000.00 USD | 63,130,000.00 USD | 0.00 USD | 421,680.00 USD | 611,360.00 USD | 993,120.00 USD |
| `7D` | `1.28` | 105,880,000.00 USD | 105,880,000.00 USD | 0.00 USD | 639,910.00 USD | 1,380,000.00 USD | 1,570,000.00 USD |
| `1D` | `1.29` | 65,040,000.00 USD | 65,040,000.00 USD | 0.00 USD | 726,790.00 USD | 768,570.00 USD | 418,070.00 USD |
| `7D` | `1.29` | 107,040,000.00 USD | 107,040,000.00 USD | 0.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD |
| `1D` | `1.29` | 65,360,000.00 USD | 65,360,000.00 USD | 0.00 USD | 210,950.00 USD | 7,740.00 USD | 98,250.00 USD |
| `7D` | `1.29` | 107,160,000.00 USD | 107,160,000.00 USD | 0.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD |
| `1D` | `1.29` | 65,660,000.00 USD | 65,660,000.00 USD | 0.00 USD | 151,350.00 USD | 0.00 USD | 154,040.00 USD |
| `7D` | `1.29` | 109,450,000.00 USD | 109,450,000.00 USD | 0.00 USD | 1,060,000.00 USD | 198,070.00 USD | 1,030,000.00 USD |
| `1D` | `1.29` | 68,550,000.00 USD | 68,550,000.00 USD | 0.00 USD | 546,160.00 USD | 195,000.00 USD | 2,140,000.00 USD |
| `7D` | `1.29` | 109,870,000.00 USD | 109,870,000.00 USD | 0.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD |
| `1D` | `1.29` | 74,470,000.00 USD | 74,470,000.00 USD | 0.00 USD | 1,800,000.00 USD | 626,060.00 USD | 3,500,000.00 USD |
| `7D` | `1.29` | 119,500,000.00 USD | 119,500,000.00 USD | 0.00 USD | 3,350,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD |
| `1D` | `1.30` | 76,700,000.00 USD | 76,700,000.00 USD | 0.00 USD | 501,280.00 USD | 633,000.00 USD | 1,100,000.00 USD |
| `7D` | `1.30` | 120,740,000.00 USD | 120,740,000.00 USD | 0.00 USD | 209,360.00 USD | 398,190.00 USD | 628,450.00 USD |
| `1D` | `1.30` | 77,420,000.00 USD | 77,420,000.00 USD | 0.00 USD | 321,680.00 USD | 109,620.00 USD | 291,610.00 USD |
| `7D` | `1.30` | 122,800,000.00 USD | 122,800,000.00 USD | 0.00 USD | 0.00 USD | 100,810.00 USD | 1,960,000.00 USD |
| `1D` | `1.30` | 79,550,000.00 USD | 79,550,000.00 USD | 0.00 USD | 443,890.00 USD | 332,000.00 USD | 1,350,000.00 USD |
| `7D` | `1.30` | 124,460,000.00 USD | 124,460,000.00 USD | 0.00 USD | 208,510.00 USD | 486,620.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 81,270,000.00 USD | 81,270,000.00 USD | 0.00 USD | 587,440.00 USD | 869,380.00 USD | 260,610.00 USD |
| `7D` | `1.30` | 127,560,000.00 USD | 127,560,000.00 USD | 0.00 USD | 0.00 USD | 2,610,000.00 USD | 485,710.00 USD |
| `1D` | `1.30` | 82,540,000.00 USD | 82,540,000.00 USD | 0.00 USD | 304,340.00 USD | 649,450.00 USD | 322,840.00 USD |
| `7D` | `1.30` | 127,560,000.00 USD | 127,560,000.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD |
| `1D` | `1.31` | 84,830,000.00 USD | 84,830,000.00 USD | 0.00 USD | 689,960.00 USD | 147,250.00 USD | 1,450,000.00 USD |
| `7D` | `1.31` | 130,570,000.00 USD | 130,570,000.00 USD | 0.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD |
| `1D` | `1.31` | 88,070,000.00 USD | 88,070,000.00 USD | 0.00 USD | 1,130,000.00 USD | 330,750.00 USD | 1,770,000.00 USD |
| `7D` | `1.31` | 135,020,000.00 USD | 135,020,000.00 USD | 0.00 USD | 1,670,000.00 USD | 1,060,000.00 USD | 1,720,000.00 USD |
| `1D` | `1.31` | 90,390,000.00 USD | 90,390,000.00 USD | 0.00 USD | 876,130.00 USD | 869,070.00 USD | 573,540.00 USD |
| `7D` | `1.31` | 138,280,000.00 USD | 138,280,000.00 USD | 0.00 USD | 839,350.00 USD | 430,210.00 USD | 1,990,000.00 USD |
| `1D` | `1.31` | 93,320,000.00 USD | 93,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 664,910.00 USD | 944,450.00 USD |
| `7D` | `1.31` | 141,130,000.00 USD | 141,130,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD |
| `1D` | `1.31` | 96,250,000.00 USD | 96,250,000.00 USD | 0.00 USD | 372,630.00 USD | 454,810.00 USD | 2,110,000.00 USD |
| `7D` | `1.31` | 143,580,000.00 USD | 143,580,000.00 USD | 0.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 102,760,000.00 USD | 102,760,000.00 USD | 0.00 USD | 1,320,000.00 USD | 1,640,000.00 USD | 3,550,000.00 USD |
| `7D` | `1.32` | 148,210,000.00 USD | 148,210,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 107,840,000.00 USD | 107,840,000.00 USD | 0.00 USD | 1,740,000.00 USD | 836,160.00 USD | 2,510,000.00 USD |
| `7D` | `1.32` | 151,290,000.00 USD | 151,290,000.00 USD | 0.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 111,340,000.00 USD | 111,340,000.00 USD | 0.00 USD | 1,650,000.00 USD | 652,780.00 USD | 1,200,000.00 USD |
| `7D` | `1.32` | 153,120,000.00 USD | 153,120,000.00 USD | 0.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD |
| `1D` | `1.32` | 115,930,000.00 USD | 115,930,000.00 USD | 0.00 USD | 1,990,000.00 USD | 583,250.00 USD | 2,020,000.00 USD |
| `7D` | `1.32` | 157,580,000.00 USD | 157,580,000.00 USD | 0.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD |
| `1D` | `1.32` | 117,930,000.00 USD | 117,930,000.00 USD | 0.00 USD | 1,080,000.00 USD | 287,760.00 USD | 625,660.00 USD |
| `7D` | `1.32` | 159,940,000.00 USD | 159,940,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 120,460,000.00 USD | 120,460,000.00 USD | 0.00 USD | 664,210.00 USD | 621,550.00 USD | 1,240,000.00 USD |
| `7D` | `1.33` | 160,480,000.00 USD | 160,480,000.00 USD | 0.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 122,700,000.00 USD | 122,700,000.00 USD | 0.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD |
| `7D` | `1.33` | 161,640,000.00 USD | 161,640,000.00 USD | 0.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 125,550,000.00 USD | 125,550,000.00 USD | 0.00 USD | 848,670.00 USD | 298,810.00 USD | 1,700,000.00 USD |
| `7D` | `1.33` | 163,360,000.00 USD | 163,360,000.00 USD | 0.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 127,940,000.00 USD | 127,940,000.00 USD | 0.00 USD | 1,040,000.00 USD | 190,550.00 USD | 1,160,000.00 USD |
| `7D` | `1.33` | 167,410,000.00 USD | 167,410,000.00 USD | 0.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD |
| `1D` | `1.33` | 130,020,000.00 USD | 130,020,000.00 USD | 0.00 USD | 859,040.00 USD | 354,550.00 USD | 872,500.00 USD |
| `7D` | `1.33` | 167,950,000.00 USD | 167,950,000.00 USD | 0.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 132,000,000.00 USD | 132,000,000.00 USD | 0.00 USD | 829,900.00 USD | 219,260.00 USD | 927,340.00 USD |
| `7D` | `1.34` | 169,900,000.00 USD | 169,900,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD |
| `1D` | `1.34` | 134,490,000.00 USD | 134,490,000.00 USD | 0.00 USD | 1,100,000.00 USD | 370,350.00 USD | 1,020,000.00 USD |
| `7D` | `1.34` | 172,250,000.00 USD | 172,250,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD |
| `1D` | `1.34` | 136,510,000.00 USD | 136,510,000.00 USD | 0.00 USD | 1,040,000.00 USD | 387,310.00 USD | 592,540.00 USD |
| `7D` | `1.34` | 176,950,000.00 USD | 176,950,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD |
| `1D` | `1.34` | 139,770,000.00 USD | 139,770,000.00 USD | 0.00 USD | 1,410,000.00 USD | 693,530.00 USD | 1,150,000.00 USD |
| `7D` | `1.34` | 182,600,000.00 USD | 182,600,000.00 USD | 0.00 USD | 1,700,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD |
| `1D` | `1.34` | 141,530,000.00 USD | 141,530,000.00 USD | 0.00 USD | 584,400.00 USD | 416,300.00 USD | 762,530.00 USD |
| `7D` | `1.34` | 193,560,000.00 USD | 193,560,000.00 USD | 0.00 USD | 3,600,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD |
| `1D` | `1.35` | 142,580,000.00 USD | 142,580,000.00 USD | 0.00 USD | 355,660.00 USD | 234,160.00 USD | 458,570.00 USD |
| `7D` | `1.35` | 200,510,000.00 USD | 200,510,000.00 USD | 0.00 USD | 2,310,000.00 USD | 2,170,000.00 USD | 2,460,000.00 USD |
| `1D` | `1.35` | 144,070,000.00 USD | 144,070,000.00 USD | 0.00 USD | 749,450.00 USD | 149,380.00 USD | 591,590.00 USD |
| `7D` | `1.35` | 210,760,000.00 USD | 210,760,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,640,000.00 USD | 4,320,000.00 USD |
| `1D` | `1.35` | 145,090,000.00 USD | 145,090,000.00 USD | 0.00 USD | 471,590.00 USD | 126,450.00 USD | 425,480.00 USD |
| `7D` | `1.35` | 218,470,000.00 USD | 218,470,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,380,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 146,650,000.00 USD | 146,650,000.00 USD | 0.00 USD | 660,420.00 USD | 332,480.00 USD | 562,550.00 USD |
| `7D` | `1.35` | 226,800,000.00 USD | 226,800,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD |
| `1D` | `1.35` | 147,520,000.00 USD | 147,520,000.00 USD | 0.00 USD | 217,930.00 USD | 79,810.00 USD | 571,660.00 USD |
| `7D` | `1.35` | 235,030,000.00 USD | 235,030,000.00 USD | 0.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD |
| `1D` | `1.36` | 148,460,000.00 USD | 148,460,000.00 USD | 0.00 USD | 391,410.00 USD | 17,220.00 USD | 531,190.00 USD |
| `7D` | `1.36` | 239,120,000.00 USD | 239,120,000.00 USD | 0.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD |
| `1D` | `1.36` | 148,800,000.00 USD | 148,800,000.00 USD | 0.00 USD | 213,710.00 USD | 42,480.00 USD | 84,480.00 USD |
| `7D` | `1.36` | 242,910,000.00 USD | 242,910,000.00 USD | 0.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.36` | 149,540,000.00 USD | 149,540,000.00 USD | 0.00 USD | 277,960.00 USD | 149,990.00 USD | 316,940.00 USD |
| `7D` | `1.36` | 245,040,000.00 USD | 245,040,000.00 USD | 0.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD |
| `1D` | `1.36` | 149,880,000.00 USD | 149,880,000.00 USD | 0.00 USD | 171,250.00 USD | 2,260.00 USD | 166,760.00 USD |
| `7D` | `1.36` | 249,140,000.00 USD | 249,140,000.00 USD | 0.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD |
| `1D` | `1.36` | 150,000,000.00 USD | 150,000,000.00 USD | 0.00 USD | 0.00 USD | 26,460.00 USD | 87,240.00 USD |
| `7D` | `1.36` | 250,860,000.00 USD | 250,860,000.00 USD | 0.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD |
| `1D` | `1.37` | 150,330,000.00 USD | 150,330,000.00 USD | 0.00 USD | 53,740.00 USD | 104,420.00 USD | 171,320.00 USD |
| `7D` | `1.37` | 251,350,000.00 USD | 251,350,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD |
| `1D` | `1.37` | 150,520,000.00 USD | 150,520,000.00 USD | 0.00 USD | 121,310.00 USD | 2,250.00 USD | 68,720.00 USD |
| `7D` | `1.37` | 252,770,000.00 USD | 252,770,000.00 USD | 0.00 USD | 528,490.00 USD | 135,750.00 USD | 753,550.00 USD |
| `1D` | `1.37` | 150,710,000.00 USD | 150,710,000.00 USD | 0.00 USD | 1,740.00 USD | 67,780.00 USD | 119,540.00 USD |
| `7D` | `1.37` | 253,930,000.00 USD | 253,930,000.00 USD | 0.00 USD | 334,560.00 USD | 372,470.00 USD | 461,160.00 USD |
| `1D` | `1.37` | 150,910,000.00 USD | 150,910,000.00 USD | 0.00 USD | 75,340.00 USD | 1,780.00 USD | 126,860.00 USD |
| `7D` | `1.37` | 256,400,000.00 USD | 256,400,000.00 USD | 0.00 USD | 821,620.00 USD | 376,730.00 USD | 1,270,000.00 USD |
| `1D` | `1.38` | 151,190,000.00 USD | 151,190,000.00 USD | 0.00 USD | 120,880.00 USD | 30,080.00 USD | 125,000.00 USD |
| `7D` | `1.38` | 258,200,000.00 USD | 258,200,000.00 USD | 0.00 USD | 536,130.00 USD | 295,850.00 USD | 969,400.00 USD |
| `1D` | `1.38` | 151,590,000.00 USD | 151,590,000.00 USD | 0.00 USD | 93,260.00 USD | 50,590.00 USD | 254,190.00 USD |
| `7D` | `1.38` | 259,700,000.00 USD | 259,700,000.00 USD | 0.00 USD | 617,230.00 USD | 330,890.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 152,130,000.00 USD | 152,130,000.00 USD | 0.00 USD | 226,690.00 USD | 110,480.00 USD | 207,630.00 USD |
| `7D` | `1.38` | 261,840,000.00 USD | 261,840,000.00 USD | 0.00 USD | 579,450.00 USD | 290,350.00 USD | 1,260,000.00 USD |
| `1D` | `1.38` | 152,250,000.00 USD | 152,250,000.00 USD | 0.00 USD | 49,970.00 USD | 65,520.00 USD | 0.00 USD |
| `7D` | `1.38` | 264,380,000.00 USD | 264,380,000.00 USD | 0.00 USD | 1,210,000.00 USD | 331,990.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 152,410,000.00 USD | 152,410,000.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 166,310.00 USD |
| `7D` | `1.38` | 265,470,000.00 USD | 265,470,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.39` | 152,470,000.00 USD | 152,470,000.00 USD | 0.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD |
| `7D` | `1.39` | 266,760,000.00 USD | 266,760,000.00 USD | 0.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 152,520,000.00 USD | 152,520,000.00 USD | 0.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD |
| `7D` | `1.39` | 267,300,000.00 USD | 267,300,000.00 USD | 0.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD |
| `1D` | `1.39` | 152,610,000.00 USD | 152,610,000.00 USD | 0.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD |
| `7D` | `1.39` | 268,400,000.00 USD | 268,400,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD |
| `7D` | `1.39` | 268,570,000.00 USD | 268,570,000.00 USD | 0.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD |
| `1D` | `1.39` | 152,630,000.00 USD | 152,630,000.00 USD | 0.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.39` | 268,890,000.00 USD | 268,890,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `7D` | `1.40` | 269,060,000.00 USD | 269,060,000.00 USD | 0.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD |
| `7D` | `1.40` | 269,180,000.00 USD | 269,180,000.00 USD | 0.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `7D` | `1.40` | 269,190,000.00 USD | 269,190,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 269,320,000.00 USD | 269,320,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 269,440,000.00 USD | 269,440,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `7D` | `1.41` | 269,680,000.00 USD | 269,680,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 269,850,000.00 USD | 269,850,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `7D` | `1.41` | 270,230,000.00 USD | 270,230,000.00 USD | 0.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `7D` | `1.41` | 270,880,000.00 USD | 270,880,000.00 USD | 0.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `7D` | `1.41` | 271,050,000.00 USD | 271,050,000.00 USD | 0.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD |
| `7D` | `1.42` | 271,680,000.00 USD | 271,680,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD |
| `7D` | `1.42` | 272,200,000.00 USD | 272,200,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `7D` | `1.42` | 273,220,000.00 USD | 273,220,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `7D` | `1.42` | 274,600,000.00 USD | 274,600,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `7D` | `1.42` | 275,230,000.00 USD | 275,230,000.00 USD | 0.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `7D` | `1.43` | 275,590,000.00 USD | 275,590,000.00 USD | 0.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD |
| `7D` | `1.43` | 276,600,000.00 USD | 276,600,000.00 USD | 0.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD |
| `7D` | `1.43` | 278,110,000.00 USD | 278,110,000.00 USD | 0.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `7D` | `1.43` | 279,500,000.00 USD | 279,500,000.00 USD | 0.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `7D` | `1.43` | 280,300,000.00 USD | 280,300,000.00 USD | 0.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `7D` | `1.44` | 280,830,000.00 USD | 280,830,000.00 USD | 0.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD |
| `7D` | `1.44` | 281,180,000.00 USD | 281,180,000.00 USD | 0.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD |
| `7D` | `1.44` | 281,640,000.00 USD | 281,640,000.00 USD | 0.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `7D` | `1.44` | 282,350,000.00 USD | 282,350,000.00 USD | 0.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `7D` | `1.44` | 282,730,000.00 USD | 282,730,000.00 USD | 0.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `7D` | `1.45` | 282,860,000.00 USD | 282,860,000.00 USD | 0.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `7D` | `1.45` | 282,980,000.00 USD | 282,980,000.00 USD | 0.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD |
| `7D` | `1.45` | 283,310,000.00 USD | 283,310,000.00 USD | 0.00 USD | 62,180.00 USD | 96,050.00 USD | 173,340.00 USD |
| `7D` | `1.45` | 283,920,000.00 USD | 283,920,000.00 USD | 0.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD |
| `7D` | `1.45` | 284,480,000.00 USD | 284,480,000.00 USD | 0.00 USD | 182,110.00 USD | 128,180.00 USD | 249,400.00 USD |
| `7D` | `1.46` | 284,940,000.00 USD | 284,940,000.00 USD | 0.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `7D` | `1.46` | 285,100,000.00 USD | 285,100,000.00 USD | 0.00 USD | 85,350.00 USD | 51,250.00 USD | 20,990.00 USD |
| `7D` | `1.46` | 285,570,000.00 USD | 285,570,000.00 USD | 0.00 USD | 119,110.00 USD | 56,610.00 USD | 296,470.00 USD |
| `7D` | `1.46` | 285,780,000.00 USD | 285,780,000.00 USD | 0.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.85B` | Total OI Tokens: `2,303,772,771.5 XRP`
  * 1h OI Change: `-0.11%` | 4h OI Change: `-4.65%` | 24h OI Change: `-4.24%`
  * Exchange Breakdown: Binance=`455.78M` | Bybit=`323.03M` | OKX=`98.53M` | Hyperliquid=`216.62M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `7.36K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0061%` | **USDT OKX** | `0.0012%` |
| **USDT Bybit** | `-0.0070%` | **USDT KuCoin** | `-0.0015%` |
| **USDT MEXC** | `0.0060%` | **USDT BingX** | `0.0060%` |
| **USDT Gate** | `-0.0002%` | **USDT Bitget** | `-0.0045%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `50.26%` | `49.74%` | `1.01` | 546,300,000.00 USD |
| `15M` | `Binance` | `50.31%` | `49.69%` | `1.01` | 157,380,000.00 USD |
| `15M` | `OKX` | `57.17%` | `42.83%` | `1.33` | 92,590,000.00 USD |
| `15M` | `Bybit` | `51.28%` | `48.72%` | `1.05` | 35,880,000.00 USD |
| `15M` | `KuCoin` | `44.14%` | `55.86%` | `0.79` | 4,400,000.00 USD |
| `15M` | `Gate` | `42.99%` | `57.01%` | `0.75` | 83,440,000.00 USD |
| `15M` | `Bitget` | `54.3%` | `45.7%` | `1.19` | 17,770,000.00 USD |
| `15M` | `BingX` | `64.5%` | `35.5%` | `1.82` | 9,470,000.00 USD |
| `15M` | `MEXC` | `46.3%` | `53.7%` | `0.86` | 26,890,000.00 USD |
| `15M` | `Bitunix` | `52.62%` | `47.38%` | `1.11` | 15,830,000.00 USD |
| `15M` | `Hyperliquid` | `37.72%` | `62.28%` | `0.61` | 69,280,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `45.68%` | `54.32%` | `0.84` | 1,150,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.98%` | `0.02%` | `4999.00` | 11,360,000.00 USD |
| `15M` | `HTX` | `80.27%` | `19.73%` | `4.07` | 6,400,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `61.9%` | `38.1%` | `1.62` | 1,820,000.00 USD |
| `15M` | `Bitfinex` | `41.53%` | `58.47%` | `0.71` | 933,910.00 USD |
| `15M` | `Kraken` | `35.72%` | `64.28%` | `0.56` | 1,190,000.00 USD |
| `15M` | `Aster` | `59.2%` | `40.8%` | `1.45` | 2,520,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `38.95%` | `61.05%` | `0.64` | 7,990,000.00 USD |
| `15M` | `Whale Positions` | `50.31%` | `49.69%` | `1.01` | 157,380,000.00 USD |
| `15M` | `Global Accounts` | `50.26%` | `49.74%` | `1.01` | 546,300,000.00 USD |
| `1H` | `XRP` | `55.78%` | `44.22%` | `1.26` | 3,340,000,000.00 USD |
| `1H` | `Binance` | `50.14%` | `49.86%` | `1.01` | 929,610,000.00 USD |
| `1H` | `OKX` | `52.36%` | `47.64%` | `1.10` | 513,220,000.00 USD |
| `1H` | `Bybit` | `53.92%` | `46.08%` | `1.17` | 215,250,000.00 USD |
| `1H` | `KuCoin` | `55.58%` | `44.42%` | `1.25` | 21,160,000.00 USD |
| `1H` | `Gate` | `48.04%` | `51.96%` | `0.92` | 449,160,000.00 USD |
| `1H` | `Bitget` | `55.02%` | `44.98%` | `1.22` | 100,820,000.00 USD |
| `1H` | `BingX` | `53.91%` | `46.09%` | `1.17` | 31,420,000.00 USD |
| `1H` | `MEXC` | `48.2%` | `51.8%` | `0.93` | 144,220,000.00 USD |
| `1H` | `Bitunix` | `51.61%` | `48.39%` | `1.07` | 95,560,000.00 USD |
| `1H` | `Hyperliquid` | `47.22%` | `52.78%` | `0.89` | 220,750,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.81%` | `48.19%` | `1.08` | 6,620,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `87.75%` | `12.25%` | `7.16` | 476,610,000.00 USD |
| `1H` | `HTX` | `47.22%` | `52.78%` | `0.89` | 49,570,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `51.81%` | `48.19%` | `1.08` | 20,710,000.00 USD |
| `1H` | `Bitfinex` | `40.66%` | `59.34%` | `0.69` | 2,730,000.00 USD |
| `1H` | `Kraken` | `50.52%` | `49.48%` | `1.02` | 10,780,000.00 USD |
| `1H` | `Aster` | `52.25%` | `47.75%` | `1.09` | 16,940,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.09%` | `48.91%` | `1.04` | 32,880,000.00 USD |
| `1H` | `Whale Positions` | `50.14%` | `49.86%` | `1.01` | 929,610,000.00 USD |
| `1H` | `Global Accounts` | `55.78%` | `44.22%` | `1.26` | 3,340,000,000.00 USD |
| `4H` | `XRP` | `48.04%` | `51.96%` | `0.92` | 24,940,000,000.00 USD |
| `4H` | `Binance` | `45.59%` | `54.41%` | `0.84` | 7,460,000,000.00 USD |
| `4H` | `OKX` | `46.23%` | `53.77%` | `0.86` | 4,150,000,000.00 USD |
| `4H` | `Bybit` | `45.35%` | `54.65%` | `0.83` | 1,800,000,000.00 USD |
| `4H` | `KuCoin` | `54.04%` | `45.96%` | `1.18` | 230,570,000.00 USD |
| `4H` | `Gate` | `49.03%` | `50.97%` | `0.96` | 2,550,000,000.00 USD |
| `4H` | `Bitget` | `51.66%` | `48.34%` | `1.07` | 1,070,000,000.00 USD |
| `4H` | `BingX` | `49.36%` | `50.64%` | `0.97` | 248,020,000.00 USD |
| `4H` | `MEXC` | `48.42%` | `51.58%` | `0.94` | 772,340,000.00 USD |
| `4H` | `Bitunix` | `47.76%` | `52.24%` | `0.91` | 775,570,000.00 USD |
| `4H` | `Hyperliquid` | `44.87%` | `55.13%` | `0.81` | 1,430,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.24%` | `49.76%` | `1.01` | 56,840,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `56.78%` | `43.22%` | `1.31` | 3,360,000,000.00 USD |
| `4H` | `HTX` | `36.5%` | `63.5%` | `0.57` | 251,160,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `50.31%` | `49.69%` | `1.01` | 148,800,000.00 USD |
| `4H` | `Bitfinex` | `29.63%` | `70.37%` | `0.42` | 10,880,000.00 USD |
| `4H` | `Kraken` | `47.98%` | `52.02%` | `0.92` | 87,830,000.00 USD |
| `4H` | `Aster` | `47.02%` | `52.98%` | `0.89` | 197,580,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.9%` | `51.1%` | `0.96` | 327,100,000.00 USD |
| `4H` | `Whale Positions` | `45.59%` | `54.41%` | `0.84` | 7,460,000,000.00 USD |
| `4H` | `Global Accounts` | `48.04%` | `51.96%` | `0.92` | 24,940,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.24` | `1.24` | `1.24` | `1.25` | `1.22` | 96,971,024.45 USD | 46,182,833.37 USD | 50,788,191.08 USD | -4,605,357.71 USD | `-4.75%` | `1B / 8S` |
| `0:00 UTC` | `1.25` | `1.24` | `1.25` | `1.25` | `1.23` | 42,899,530.36 USD | 22,765,315.89 USD | 20,134,214.47 USD | 2,631,101.42 USD | `+6.13%` | `25B / 6S` |
| `5:00 UTC` | `1.25` | `1.26` | `1.25` | `1.26` | `1.25` | 36,075,332.57 USD | 17,198,898.48 USD | 18,876,434.09 USD | -1,677,535.61 USD | `-4.65%` | `12B / 8S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 16,161,725.94 USD | 8,623,195.09 USD | 7,538,530.84 USD | 1,084,664.25 USD | `+6.71%` | `17B / 20S` |
| `5:00 UTC` | `1.25` | `1.26` | `1.25` | `1.26` | `1.25` | 13,078,738.26 USD | 6,457,414.69 USD | 6,621,323.57 USD | -163,908.89 USD | `-1.25%` | `11B / 13S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 37,964,913.08 USD | 18,376,664.94 USD | 19,588,248.14 USD | -1,211,583.20 USD | `-3.19%` | `12B / 11S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 29,915,763.66 USD | 14,446,371.17 USD | 15,469,392.49 USD | -1,023,021.32 USD | `-3.42%` | `7B / 11S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 15,839,415.33 USD | 9,022,554.30 USD | 6,816,861.04 USD | 2,205,693.26 USD | `+13.93%` | `13B / 3S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.24` | 13,112,458.20 USD | 7,359,936.93 USD | 5,752,521.27 USD | 1,607,415.65 USD | `+12.26%` | `7B / 2S` |
| `0:00 UTC` | `1.24` | `1.24` | `1.24` | `1.25` | `1.24` | 17,222,703.75 USD | 8,825,033.67 USD | 8,397,670.08 USD | 427,363.59 USD | `+2.48%` | `12B / 15S` |

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
| `5m` | -895,750.00 USD | -4,660,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -3,500,000.00 USD | -6,420,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -7,410,000.00 USD | -3,690,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -9,410,000.00 USD | -5,590,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -6,590,000.00 USD | -5,060,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -37,600,000.00 USD | -101,930,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -46,170,000.00 USD | -121,620,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -47,200,000.00 USD | -122,970,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -46,350,000.00 USD | -128,130,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -65,810,000.00 USD | -180,850,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -111,800,000.00 USD | -195,420,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -589,450,000.00 USD | -1,290,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-895.75K` | 15m=`-3.50M` | 1h=`-9.41M` | 24h=`-65.81M`
* Futures Capital Netflows: 5m=`-4.66M` | 15m=`-6.42M` | 1h=`-5.59M` | 24h=`-180.85M`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.22` (Risk Distance: `0.0182` pts)
  * +2.5R Take Profit: `1.29`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.25` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0182` pts)
  * +2.5R Take Profit: `1.21`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.25`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
