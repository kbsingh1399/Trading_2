# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 15:57:26 IST` (`2026-10-30 10:27:26 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.24` | **Live Ask Quote**: `1.25` | **Mid Price**: `1.24`
- **Spread Points**: `4.00` | **Spread BPS**: `32.18 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.24` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.25` | Lower -3.00σ Band: `1.23`
  * Upper +2.51σ Band: `1.25` | Lower -2.51σ Band: `1.24`
  * Upper +2.01σ Band: `1.25` | Lower -2.01σ Band: `1.24`
  * Upper +2.00σ Band: `1.25` | Lower -2.00σ Band: `1.24`
  * Upper +1.28σ Band: `1.25` | Lower -1.28σ Band: `1.24`
  * Upper +1.00σ Band: `1.25` | Lower -1.00σ Band: `1.24`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.24` | EMA-20=`1.24` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.24` (Slope: `+0.0000`) | EMA-100=`1.24`
  * Institutional Anchors: EMA-144=`1.24` | EMA-200=`1.24` (Slope: `+0.0000`) | EMA-233=`1.24`
- **Range Boundaries**: 24H High=`1.26` | 24H Low=`1.23` | Weekly High=`1.27` | Weekly Low=`1.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-1.36%`)
  * Point of Control (POC) = `1.25` (Distance: `-0.52%`)
  * Value Area Low (VAL) = `1.23` (Distance: `+0.87%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.33` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.19`
  * London Session (08:00-16:00 UTC): High=`1.27` | Low=`1.24`
  * New York Session (13:00-21:00 UTC): High=`1.25` | Low=`1.24`
  * Initial Balance (First Hour): IB High=`1.26` | IB Low=`1.25`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.24` - `1.25`
  * Optimal Trade Entry (OTE 0.705): `1.25`
  * Structural Invalidation Anchor (0.786): `1.25`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `1,681,672` | 2,099,856.08 USD | -731,684.07 USD | `-34.84%` | -41,473,685.59 USD | `-1.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.25` | `1.25` | `1.24` | `1.24` | `2,356,527` | 2,936,196.25 USD | -705,657.99 USD | `-24.03%` | -42,179,343.58 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.24` | `1.24` | `1.24` | `1.24` | `619,993` | 771,409.29 USD | -617,223.38 USD | `-80.01%` | -42,796,566.96 USD | `-0.79` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.25` | `4,186,103` | 5,245,669.17 USD | -349,085.92 USD | `-6.65%` | -39,666,531.83 USD | `-0.34` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.25` | `1.25` | `1.25` | `1.25` | `5,499,196` | 6,871,051.82 USD | -1,363,349.88 USD | `-19.84%` | -41,029,881.71 USD | `-1.16` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.25` | `1.25` | `1.24` | `1.24` | `2,981,937` | 3,714,347.90 USD | -1,327,333.60 USD | `-35.74%` | -42,357,215.31 USD | `-1.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.25` | `1.26` | `1.25` | `1.26` | `20,218,037` | 25,337,061.54 USD | 668,152.80 USD | `+2.64%` | -40,542,234.62 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.26` | `1.26` | `1.25` | `1.25` | `24,012,060` | 30,200,518.12 USD | -808,085.55 USD | `-2.68%` | -41,350,320.17 USD | `+0.13` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `1.25` | `1.25` | `1.24` | `1.24` | `8,481,133` | 10,585,399.72 USD | -2,690,683.48 USD | `-25.42%` | -44,041,003.65 USD | `-0.06` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -44,069,722.41 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.27` | `1.24` | `1.25` | `116,541,770` | 146,517,167.36 USD | 4,788,193.48 USD | `+3.27%` | -39,281,528.93 USD | `+1.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.24` | `52,705,812` | 66,116,237.03 USD | -2,826,164.00 USD | `-4.27%` | -42,107,692.93 USD | `+0.37` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -13,549,801.29 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -41,639,935.50 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -44,069,722.41 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.27` | `1.24` | `1.25` | `116,541,770` | 146,517,167.36 USD | 4,788,193.48 USD | `+3.27%` | -39,281,528.93 USD | `+1.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.24` | `52,705,812` | 66,116,237.03 USD | -2,826,164.00 USD | `-4.27%` | -42,107,692.93 USD | `+0.37` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `ASK` | `1.24` | `152554.0000` | 189,914.47 USD | 509,211.40 USD | `7 orders` | `+0.06%` | `-` |
| `ASK` | `1.24` | `11630.0000` | 14,477.02 USD | 319,296.92 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `1.24` | `74166.0000` | 92,314.42 USD | 304,819.90 USD | `12 orders` | `+0.04%` | `-` |
| `ASK` | `1.24` | `53782.0000` | 66,937.08 USD | 212,505.48 USD | `9 orders` | `+0.04%` | `-` |
| `ASK` | `1.24` | `75580.0000` | 94,059.31 USD | 145,568.40 USD | `8 orders` | `+0.03%` | `-` |
| `ASK` | `1.24` | `29002.0000` | 36,090.09 USD | 51,509.09 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `1.24` | `8754.0000` | 10,892.60 USD | 15,419.00 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `1.24` | `3638.0000` | 4,526.40 USD | 4,526.40 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.24` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.24` | `0.00%` | `-` |
| `BID` | `1.24` | `12526.0000` | 15,583.60 USD | 15,583.60 USD | `5 orders` | `-0.00%` | `-` |
| `BID` | `1.24` | `7960.0000` | 9,902.24 USD | 25,485.84 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `1.24` | `11546.0000` | 14,362.07 USD | 39,847.91 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `1.24` | `36688.0000` | 45,632.53 USD | 85,480.44 USD | `7 orders` | `-0.03%` | `-` |
| `BID` | `1.24` | `46582.0000` | 57,934.03 USD | 143,414.47 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `1.24` | `27818.0000` | 34,594.46 USD | 178,008.94 USD | `10 orders` | `-0.04%` | `-` |
| `BID` | `1.24` | `13399.0000` | 16,661.66 USD | 194,670.60 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `1.24` | `248846.0000` | 309,415.12 USD | 504,085.71 USD | `6 orders` | `-0.06%` | `-` |
| `BID` | `1.24` | `122195.0000` | 151,925.04 USD | 656,010.76 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `1.24` | `62139.0000` | 77,251.20 USD | 733,261.96 USD | `8 orders` | `-0.08%` | `-` |
| `BID` | `1.24` | `21393.0000` | 26,593.64 USD | 759,855.60 USD | `7 orders` | `-0.08%` | `-` |
| `BID` | `1.24` | `75378.0000` | 93,694.85 USD | 853,550.45 USD | `5 orders` | `-0.09%` | `-` |
| `BID` | `1.24` | `86828.0000` | 107,918.52 USD | 961,468.97 USD | `10 orders` | `-0.10%` | `-` |
| `BID` | `1.24` | `75554.0000` | 93,898.51 USD | 1,055,367.48 USD | `4 orders` | `-0.11%` | `-` |
| `BID` | `1.24` | `609362.0000` | 757,254.16 USD | 1,812,621.64 USD | `10 orders` | `-0.12%` | `-` |
| `BID` | `1.24` | `24993.0000` | 31,056.30 USD | 1,843,677.94 USD | `5 orders` | `-0.12%` | `-` |
| `BID` | `1.24` | `33879.0000` | 42,094.66 USD | 1,885,772.60 USD | `3 orders` | `-0.13%` | `-` |
| `BID` | `1.24` | `228268.0000` | 283,600.16 USD | 2,169,372.76 USD | `5 orders` | `-0.14%` | `-` |
| `BID` | `1.24` | `43097.0000` | 53,539.40 USD | 2,222,912.17 USD | `5 orders` | `-0.15%` | `-` |
| `BID` | `1.24` | `83782.0000` | 104,074.00 USD | 2,326,986.17 USD | `6 orders` | `-0.16%` | `-` |
| `ASK` | `1.25` | `202096.0000` | 251,831.83 USD | 2,669,358.42 USD | `4 orders` | `+0.16%` | `-` |
| `ASK` | `1.25` | `16176.0000` | 20,155.30 USD | 2,417,526.60 USD | `6 orders` | `+0.15%` | `-` |
| `ASK` | `1.25` | `118934.0000` | 148,179.87 USD | 2,397,371.30 USD | `11 orders` | `+0.14%` | `-` |
| `ASK` | `1.25` | `1834.0000` | 2,284.80 USD | 2,249,191.43 USD | `1 orders` | `+0.13%` | `-` |
| `ASK` | `1.25` | `42836.0000` | 53,360.81 USD | 2,246,906.63 USD | `9 orders` | `+0.12%` | `-` |
| `ASK` | `1.25` | `283152.0000` | 352,694.13 USD | 2,193,545.83 USD | `7 orders` | `+0.12%` | `-` |
| `ASK` | `1.25` | `368889.0000` | 459,451.25 USD | 1,840,851.70 USD | `7 orders` | `+0.11%` | `-` |
| `ASK` | `1.25` | `66104.0000` | 82,325.92 USD | 1,381,400.45 USD | `9 orders` | `+0.10%` | `-` |
| `ASK` | `1.25` | `243263.0000` | 302,935.41 USD | 1,299,074.52 USD | `13 orders` | `+0.09%` | `-` |
| `ASK` | `1.25` | `23821.0000` | 29,661.91 USD | 996,139.11 USD | `5 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `84297.0000` | 104,958.19 USD | 966,477.20 USD | `7 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `282978.0000` | 352,307.61 USD | 861,519.01 USD | `12 orders` | `+0.07%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:50:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `27` | `0x31b1...1434` | `LONG` | 43,589,608.35 USD | `35,031,430.00` | `1.13` | `1.25` | `0.9612` | 4,010,725.08 USD | `+9.20%` | `10X Cross` |
| `96` | `0x5b5d...c060` | `SHORT` | 19,338,538.67 USD | `15,519,251.00` | `1.44` | `1.25` | `11.06` | 2,938,749.64 USD | `+15.20%` | `5X Cross` |
| `166` | `0xb83d...6e36` | `SHORT` | 12,341,406.97 USD | `9,905,616.00` | `1.50` | `1.25` | `12.21` | 2,507,064.58 USD | `+20.31%` | `5X Cross` |
| `346` | `0x58f0...0d20` | `LONG` | 6,602,090.87 USD | `5,307,147.00` | `1.24` | `1.25` | `1.22` | -752.63 USD | `-0.01%` | `20X Cross` |
| `376` | `0xecb6...2b00` | `SHORT` | 6,124,359.69 USD | `4,914,822.00` | `1.27` | `1.25` | `7.25` | 111,203.28 USD | `+1.82%` | `10X Cross` |
| `424` | `0xca49...53c8` | `SHORT` | 5,149,601.96 USD | `4,138,886.00` | `1.44` | `1.25` | `4.98` | 803,720.77 USD | `+15.61%` | `20X Cross` |
| `438` | `0xdd53...2b13` | `SHORT` | 4,982,246.95 USD | `3,998,914.00` | `1.40` | `1.25` | `16.79` | 614,629.16 USD | `+12.34%` | `3X Cross` |
| `501` | `0x610b...b613` | `LONG` | 4,410,086.40 USD | `3,543,946.00` | `1.44` | `1.25` | `0.8516` | -689,906.21 USD | `-15.64%` | `5X Cross` |
| `585` | `0x9946...0852` | `SHORT` | 3,819,987.90 USD | `3,070,483.00` | `1.40` | `1.25` | `1.78` | 488,514.32 USD | `+12.79%` | `20X Cross` |
| `644` | `0xc30c...a4c9` | `SHORT` | 3,473,761.27 USD | `2,791,515.00` | `1.41` | `1.25` | `1.60` | 462,751.47 USD | `+13.32%` | `8X Cross` |
| `646` | `0xc179...e0c8` | `SHORT` | 3,450,182.99 USD | `2,768,785.00` | `1.27` | `1.25` | `3.29` | 58,233.90 USD | `+1.69%` | `10X Cross` |
| `651` | `0xfc27...9d9d` | `SHORT` | 3,416,314.77 USD | `2,746,013.00` | `1.29` | `1.25` | `8.32` | 134,869.15 USD | `+3.95%` | `20X Cross` |
| `694` | `0xf48f...10fe` | `LONG` | 3,195,421.17 USD | `2,565,779.00` | `1.53` | `1.25` | `1.02` | -729,219.56 USD | `-22.82%` | `4X Cross` |
| `739` | `0x023a...2355` | `SHORT` | 3,068,853.89 USD | `2,463,360.00` | `1.32` | `1.25` | `3.34` | 182,074.36 USD | `+5.93%` | `20X Cross` |
| `746` | `0x45d2...4029` | `SHORT` | 3,053,003.80 USD | `2,453,000.00` | `1.48` | `1.25` | `18.93` | 585,276.62 USD | `+19.17%` | `20X Cross` |
| `1068` | `0xeadc...9d55` | `LONG` | 2,015,523.36 USD | `1,619,805.00` | `1.21` | `1.25` | `0.000000` | 56,680.34 USD | `+2.81%` | `20X Cross` |
| `1139` | `0x94b2...599e` | `SHORT` | 1,917,088.03 USD | `1,540,696.00` | `1.36` | `1.25` | `1.88` | 183,378.42 USD | `+9.57%` | `20X Cross` |
| `1160` | `0x3fc5...c0c1` | `SHORT` | 1,883,374.28 USD | `1,511,779.00` | `1.52` | `1.25` | `2.45` | 408,240.32 USD | `+21.68%` | `20X Cross` |
| `1187` | `0x31ef...f715` | `LONG` | 1,835,589.55 USD | `1,475,080.00` | `1.49` | `1.25` | `1.04` | -363,675.85 USD | `-19.81%` | `3X Isolated` |
| `1246` | `0x7737...bf66` | `SHORT` | 1,761,461.33 USD | `1,413,466.00` | `1.41` | `1.25` | `14.09` | 237,407.32 USD | `+13.48%` | `10X Cross` |
| `1307` | `0x95da...2328` | `LONG` | 1,648,675.69 USD | `1,324,876.00` | `1.35` | `1.25` | `0.0922` | -144,965.40 USD | `-8.79%` | `5X Cross` |
| `1327` | `0xee2b...d67e` | `LONG` | 1,625,390.89 USD | `1,306,284.00` | `1.55` | `1.25` | `0.4681` | -405,264.01 USD | `-24.93%` | `4X Cross` |
| `1377` | `0x215d...f80a` | `LONG` | 1,557,460.94 USD | `1,251,777.00` | `1.32` | `1.25` | `1.13` | -96,993.28 USD | `-6.23%` | `14X Cross` |
| `1400` | `0x5fa3...35b7` | `SHORT` | 1,543,493.91 USD | `1,240,651.00` | `1.30` | `1.25` | `2.68` | 72,998.22 USD | `+4.73%` | `20X Cross` |
| `1433` | `0x123d...3bff` | `LONG` | 1,509,892.51 USD | `1,211,889.00` | `1.35` | `1.25` | `0.000000` | -122,542.98 USD | `-8.12%` | `10X Cross` |
| `1448` | `0xbcd4...0dd2` | `SHORT` | 1,490,132.52 USD | `1,196,125.00` | `1.31` | `1.25` | `2.02` | 77,534.72 USD | `+5.20%` | `20X Cross` |
| `1559` | `0xdf95...7d72` | `SHORT` | 1,370,478.54 USD | `1,099,726.00` | `1.37` | `1.25` | `37.13` | 139,120.26 USD | `+10.15%` | `20X Cross` |
| `1567` | `0x7fda...17d1` | `LONG` | 1,364,487.25 USD | `1,095,182.00` | `1.22` | `1.25` | `0.000000` | 30,046.35 USD | `+2.20%` | `20X Cross` |
| `1624` | `0xef96...9383` | `SHORT` | 1,291,601.84 USD | `1,036,765.00` | `1.34` | `1.25` | `4.63` | 95,917.51 USD | `+7.43%` | `20X Cross` |
| `1646` | `0xb1ce...681b` | `LONG` | 1,271,687.47 USD | `1,021,764.00` | `1.49` | `1.25` | `1.16` | -252,369.02 USD | `-19.85%` | `4X Isolated` |
| `1755` | `0x3c36...461a` | `LONG` | 1,169,611.45 USD | `940,051.00` | `1.30` | `1.25` | `1.05` | -49,469.16 USD | `-4.23%` | `10X Cross` |
| `1870` | `0x2577...4897` | `SHORT` | 1,084,026.44 USD | `870,075.00` | `1.24` | `1.25` | `5.01` | -1,342.72 USD | `-0.12%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,122.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.12K USD at 1.2887 USD [API] | `2026-10-29 10:13:41` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.2875 USD [API] | `2026-10-29 10:29:08` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,472.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.47K USD at 1.2902 USD [API] | `2026-10-29 10:34:37` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10,443.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.44K USD at 1.2920 USD [API] | `2026-10-29 10:38:44` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2920 USD [API] | `2026-10-29 10:38:44` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 16,342.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 16.34K USD at 1.2905 USD [API] | `2026-10-29 10:43:46` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,104.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.10K USD at 1.2905 USD [API] | `2026-10-29 10:43:46` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2931 USD [API] | `2026-10-29 10:46:40` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 14.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 44.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 11.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 154.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.15K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,957.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.96K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 70.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 47.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.05K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,567.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 7.57K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 355.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.36K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 19.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 90.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 11.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,358.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.36K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 187.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.19K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 982.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.98K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 146.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.15K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,959.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.96K USD at 1.3100 USD [API] | `2026-10-15 02:22:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.2901 USD [API] | `2026-10-29 11:31:10` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10,414.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.41K USD at 1.2902 USD [API] | `2026-10-29 11:31:10` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,159.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.16K USD at 1.2911 USD [API] | `2026-10-29 11:32:13` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,498.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.50K USD at 1.2924 USD [API] | `2026-10-29 11:39:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 8,228.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.23K USD at 1.2907 USD [API] | `2026-10-29 12:29:45` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,227.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.23K USD at 1.2906 USD [API] | `2026-10-29 12:29:45` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 20,952.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 20.95K USD at 1.2864 USD [API] | `2026-10-29 12:35:14` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,749.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.75K USD at 1.2923 USD [API] | `2026-10-29 12:44:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2913 USD [API] | `2026-10-29 12:45:48` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,573.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.57K USD at 1.2897 USD [API] | `2026-10-29 12:47:36` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,553.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.55K USD at 1.2906 USD [API] | `2026-10-29 12:49:50` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,463.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.46K USD at 1.2926 USD [API] | `2026-10-29 13:06:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.2918 USD [API] | `2026-10-29 13:05:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,869.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.87K USD at 1.2918 USD [API] | `2026-10-29 13:05:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 65.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.2866 USD [API] | `2026-10-29 04:06:15` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 14.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2882 USD [API] | `2026-10-29 04:02:21` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,106.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.11K USD at 1.2882 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 68.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.2890 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,721.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.72K USD at 1.2892 USD [API] | `2026-10-29 02:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 104.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.2892 USD [API] | `2026-10-29 02:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 14.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2892 USD [API] | `2026-10-29 02:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 478.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.48K USD at 1.2892 USD [API] | `2026-10-29 02:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 96.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.2894 USD [API] | `2026-10-29 02:31:00` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,805.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.81K USD at 1.2926 USD [API] | `2026-10-29 02:30:49` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 3,029.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.03K USD at 1.2952 USD [API] | `2026-10-29 02:16:03` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 192.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.19K USD at 1.2984 USD [API] | `2026-10-29 01:49:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 493.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.49K USD at 1.2984 USD [API] | `2026-10-29 01:49:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 131.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.13K USD at 1.2984 USD [API] | `2026-10-29 01:49:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 238.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.24K USD at 1.3016 USD [API] | `2026-10-29 01:48:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 101.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.3016 USD [API] | `2026-10-29 01:48:59` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 396.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.40K USD at 1.2920 USD [API] | `2026-10-29 06:47:28` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,558.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.56K USD at 1.2921 USD [API] | `2026-10-29 13:07:20` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 15,294.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 15.29K USD at 1.2949 USD [API] | `2026-10-29 13:17:10` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 17,335.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 17.34K USD at 1.2929 USD [API] | `2026-10-29 13:18:15` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,263.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.26K USD at 1.2931 USD [API] | `2026-10-29 13:23:39` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2941 USD [API] | `2026-10-29 13:29:53` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,825.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.83K USD at 1.2903 USD [API] | `2026-10-29 13:33:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2886 USD [API] | `2026-10-29 13:47:02` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,409.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.41K USD at 1.2897 USD [API] | `2026-10-29 13:53:35` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 972.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.97K USD at 1.3018 USD [API] | `2026-10-15 02:22:28` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 489.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.49K USD at 1.3715 USD [API] | `2026-10-12 14:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 1,001.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.00K USD at 1.3776 USD [API] | `2026-10-08 15:15:00` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 11.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.4139 USD [API] | `2026-10-07 17:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 500.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.4139 USD [API] | `2026-10-07 17:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 3,286.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.29K USD at 1.4140 USD [API] | `2026-10-07 17:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.41` | 398.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.4141 USD [API] | `2026-10-07 17:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 551.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.55K USD at 1.5100 USD [API] | `2026-09-29 15:27:11` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,115.53 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 9.12K USD at 1.2939 USD [API] | `2026-10-29 13:59:11` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2916 USD [API] | `2026-10-29 14:12:11` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2923 USD [API] | `2026-10-29 14:13:41` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 9,733.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.73K USD at 1.2978 USD [API] | `2026-10-29 17:21:47` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 29,134.57 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 29.13K USD at 1.2924 USD [API] | `2026-10-29 18:03:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,953.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.95K USD at 1.2924 USD [API] | `2026-10-29 18:03:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 38,693.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 38.69K USD at 1.2924 USD [API] | `2026-10-29 18:03:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 17,223.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 17.22K USD at 1.2924 USD [API] | `2026-10-29 18:03:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,439.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.44K USD at 1.2924 USD [API] | `2026-10-29 18:03:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 12,657.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 12.66K USD at 1.2924 USD [API] | `2026-10-29 18:11:20` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+3.65%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.06%`)
  * 48H Horizon: Short MP=`1.32` (Vol: 2,300,000.00 USD, Dist: `+5.88%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.07%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,800,000.00 USD, Dist: `+8.06%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.07%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 2,900,000.00 USD, Dist: `+7.94%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.07%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 1,970.00 USD | 64,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 3,860.00 USD | 64,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 3,350.00 USD | 64,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 864.41 USD | 64,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 235.16 USD | 64,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 4,910.00 USD | 64,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 1,220.00 USD | 64,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 6,180.00 USD | 64,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 2,470.00 USD | 64,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 53,790.00 USD | 64,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 7,140.00 USD | 64,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 8,020.00 USD | 64,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 174.59 USD | 64,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 167.27 USD | 64,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 967.78 USD | 64,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 30,360.00 USD | 64,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 12,330.00 USD | 64,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 1,540.00 USD | 64,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 595,960.00 USD | 64,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 2,200.00 USD | 63,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 987.52 USD | 63,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 170,070.00 USD | 63,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 3,990.00 USD | 63,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 371.18 USD | 63,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 2,620.00 USD | 63,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 2,000.00 USD | 63,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 3,430.00 USD | 63,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 14,250.00 USD | 63,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 177,740.00 USD | 63,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 6,200.00 USD | 63,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 5,800.00 USD | 63,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 32,730.00 USD | 63,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 37,700.00 USD | 63,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 9,170.00 USD | 63,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 10,510.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 19,340.00 USD | 63,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 1,830.00 USD | 63,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 17,310.00 USD | 63,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 29,510.00 USD | 63,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 4,230.00 USD | 63,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 152,040.00 USD | 63,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 32,690.00 USD | 63,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 67,660.00 USD | 63,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 216,840.00 USD | 63,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 41,820.00 USD | 62,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 77,980.00 USD | 62,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 115,930.00 USD | 62,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 64,620.00 USD | 62,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 5,930.00 USD | 62,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 16,840.00 USD | 62,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 11,250.00 USD | 62,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 520,520.00 USD | 62,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 47,390.00 USD | 62,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 19,520.00 USD | 62,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 37,780.00 USD | 61,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 58,470.00 USD | 61,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 3,080,000.00 USD | 61,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 34,850.00 USD | 58,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 100,640.00 USD | 58,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 409,130.00 USD | 58,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 149,180.00 USD | 58,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 141,240.00 USD | 58,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 78,240.00 USD | 57,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 73,880.00 USD | 57,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 98,970.00 USD | 57,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 58,620.00 USD | 57,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 83,870.00 USD | 57,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,980,000.00 USD | 57,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 153,270.00 USD | 23,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 447,720.00 USD | 23,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 120,630.00 USD | 22,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 471,340.00 USD | 22,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 303,520.00 USD | 22,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 2,710,000.00 USD | 22,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,130,000.00 USD | 19,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 241,120.00 USD | 17,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,660,000.00 USD | 17,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 386,620.00 USD | 15,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.07` | 101,020,000.00 USD | 101,020,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.07` | 1,260,000.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 199,330.00 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.09` | 101,020,000.00 USD | 101,020,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 100,980,000.00 USD | 100,980,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 100,880,000.00 USD | 100,880,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.09` | 411,770.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.10` | 100,840,000.00 USD | 100,840,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 100,840,000.00 USD | 100,840,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 100,550,000.00 USD | 100,550,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.10` | 101,190.00 USD | 13,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.11` | 100,550,000.00 USD | 100,550,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 100,540,000.00 USD | 100,540,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 100,540,000.00 USD | 100,540,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 285,030.00 USD | 12,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.12` | 100,490,000.00 USD | 100,490,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 100,470,000.00 USD | 100,470,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 100,390,000.00 USD | 100,390,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 95,210,000.00 USD | 95,210,000.00 USD | 22,700.00 USD | 44,260.00 USD | 175,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 100,370,000.00 USD | 100,370,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 94,970,000.00 USD | 94,970,000.00 USD | 97,300.00 USD | 58,310.00 USD | 172,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,150,000.00 USD | 12,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.13` | 100,160,000.00 USD | 100,160,000.00 USD | 0.00 USD | 53,430.00 USD | 94,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 94,640,000.00 USD | 94,640,000.00 USD | 33,730.00 USD | 42,100.00 USD | 236,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 100,010,000.00 USD | 100,010,000.00 USD | 0.00 USD | 0.00 USD | 295,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 94,330,000.00 USD | 94,330,000.00 USD | 74,730.00 USD | 82,870.00 USD | 192,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 99,720,000.00 USD | 99,720,000.00 USD | 5,450.00 USD | 55,710.00 USD | 98,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 93,980,000.00 USD | 93,980,000.00 USD | 9,300.00 USD | 110,430.00 USD | 421,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 99,560,000.00 USD | 99,560,000.00 USD | 69,750.00 USD | 93,260.00 USD | 205,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 93,440,000.00 USD | 93,440,000.00 USD | 88,690.00 USD | 52,980.00 USD | 41,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 99,190,000.00 USD | 99,190,000.00 USD | 74,920.00 USD | 187,750.00 USD | 224,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 93,250,000.00 USD | 93,250,000.00 USD | 4,270.00 USD | 166,580.00 USD | 224,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 464,270.00 USD | 10,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.14` | 98,710,000.00 USD | 98,710,000.00 USD | 79,780.00 USD | 88,050.00 USD | 370,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 92,860,000.00 USD | 92,860,000.00 USD | 81,050.00 USD | 49,560.00 USD | 97,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 98,170,000.00 USD | 98,170,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 92,630,000.00 USD | 92,630,000.00 USD | 26,280.00 USD | 52,050.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 98,140,000.00 USD | 98,140,000.00 USD | 39,170.00 USD | 54,580.00 USD | 250,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 92,440,000.00 USD | 92,440,000.00 USD | 29,510.00 USD | 10,830.00 USD | 153,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 97,790,000.00 USD | 97,790,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 92,250,000.00 USD | 92,250,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 97,650,000.00 USD | 97,650,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 92,110,000.00 USD | 92,110,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 284,740.00 USD | 10,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 97,640,000.00 USD | 97,640,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 97,580,000.00 USD | 97,580,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 92,070,000.00 USD | 92,070,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 97,210,000.00 USD | 97,210,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 97,060,000.00 USD | 97,060,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 92,060,000.00 USD | 92,060,000.00 USD | 4,040.00 USD | 14,590.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 96,890,000.00 USD | 96,890,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 91,850,000.00 USD | 91,850,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 361,700.00 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 96,010,000.00 USD | 96,010,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 91,510,000.00 USD | 91,510,000.00 USD | 72,570.00 USD | 16,310.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 95,780,000.00 USD | 95,780,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 91,390,000.00 USD | 91,390,000.00 USD | 123,360.00 USD | 15,500.00 USD | 433,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 94,910,000.00 USD | 94,910,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 90,820,000.00 USD | 90,820,000.00 USD | 180,710.00 USD | 57,350.00 USD | 117,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 93,830,000.00 USD | 93,830,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 90,460,000.00 USD | 90,460,000.00 USD | 111,610.00 USD | 269,990.00 USD | 256,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 92,530,000.00 USD | 92,530,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 89,830,000.00 USD | 89,830,000.00 USD | 59,160.00 USD | 11,100.00 USD | 473,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,290,000.00 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.17` | 90,860,000.00 USD | 90,860,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 89,280,000.00 USD | 89,280,000.00 USD | 121,070.00 USD | 101,750.00 USD | 85,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 89,520,000.00 USD | 89,520,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 88,970,000.00 USD | 88,970,000.00 USD | 101,220.00 USD | 95,020.00 USD | 206,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 88,450,000.00 USD | 88,450,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 88,570,000.00 USD | 88,570,000.00 USD | 361,890.00 USD | 3,910.00 USD | 415,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 86,410,000.00 USD | 86,410,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 87,790,000.00 USD | 87,790,000.00 USD | 104,550.00 USD | 79,710.00 USD | 338,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 85,210,000.00 USD | 85,210,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 87,270,000.00 USD | 87,270,000.00 USD | 396,370.00 USD | 140,700.00 USD | 416,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 274,850.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.18` | 83,640,000.00 USD | 83,640,000.00 USD | 181,850.00 USD | 71,240.00 USD | 311,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 86,310,000.00 USD | 86,310,000.00 USD | 71,610.00 USD | 44,040.00 USD | 250,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 83,080,000.00 USD | 83,080,000.00 USD | 85,020.00 USD | 27,270.00 USD | 483,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 85,950,000.00 USD | 85,950,000.00 USD | 90,040.00 USD | 42,260.00 USD | 198,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 82,480,000.00 USD | 82,480,000.00 USD | 267,580.00 USD | 112,520.00 USD | 194,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 85,620,000.00 USD | 85,620,000.00 USD | 144,240.00 USD | 19,410.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 81,910,000.00 USD | 81,910,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 85,450,000.00 USD | 85,450,000.00 USD | 150,010.00 USD | 19,860.00 USD | 660,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 81,640,000.00 USD | 81,640,000.00 USD | 297,510.00 USD | 570,360.00 USD | 235,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 84,610,000.00 USD | 84,610,000.00 USD | 225,800.00 USD | 63,560.00 USD | 143,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 530,310.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.19` | 80,540,000.00 USD | 80,540,000.00 USD | 76,370.00 USD | 69,240.00 USD | 706,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 84,180,000.00 USD | 84,180,000.00 USD | 109,160.00 USD | 518,680.00 USD | 653,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 79,690,000.00 USD | 79,690,000.00 USD | 216,820.00 USD | 93,330.00 USD | 477,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 82,900,000.00 USD | 82,900,000.00 USD | 360,560.00 USD | 90,130.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 78,900,000.00 USD | 78,900,000.00 USD | 179,980.00 USD | 69,020.00 USD | 728,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 81,160,000.00 USD | 81,160,000.00 USD | 61,250.00 USD | 47,660.00 USD | 373,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 77,920,000.00 USD | 77,920,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 80,680,000.00 USD | 80,680,000.00 USD | 157,580.00 USD | 502,360.00 USD | 448,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 76,560,000.00 USD | 76,560,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 79,570,000.00 USD | 79,570,000.00 USD | 381,040.00 USD | 157,690.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 591,080.00 USD | 7,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.20` | 75,730,000.00 USD | 75,730,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 76,990,000.00 USD | 76,990,000.00 USD | 748,570.00 USD | 88,090.00 USD | 797,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 74,140,000.00 USD | 74,140,000.00 USD | 31,150.00 USD | 373,690.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 75,350,000.00 USD | 75,350,000.00 USD | 217,630.00 USD | 935,370.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 71,130,000.00 USD | 71,130,000.00 USD | 736,290.00 USD | 466,100.00 USD | 255,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 72,650,000.00 USD | 72,650,000.00 USD | 873,590.00 USD | 591,600.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 69,670,000.00 USD | 69,670,000.00 USD | 264,000.00 USD | 144,630.00 USD | 618,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 69,060,000.00 USD | 69,060,000.00 USD | 385,750.00 USD | 149,360.00 USD | 940,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 68,650,000.00 USD | 68,650,000.00 USD | 47,500.00 USD | 723,100.00 USD | 407,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 67,580,000.00 USD | 67,580,000.00 USD | 363,980.00 USD | 950,710.00 USD | 376,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 3,290.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.21` | 67,470,000.00 USD | 67,470,000.00 USD | 0.00 USD | 77,080.00 USD | 245,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 65,890,000.00 USD | 65,890,000.00 USD | 892,680.00 USD | 240,460.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 67,150,000.00 USD | 67,150,000.00 USD | 556,190.00 USD | 0.00 USD | 635,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 62,710,000.00 USD | 62,710,000.00 USD | 1,710,000.00 USD | 279,800.00 USD | 953,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 65,950,000.00 USD | 65,950,000.00 USD | 257,960.00 USD | 719,110.00 USD | 3,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 59,770,000.00 USD | 59,770,000.00 USD | 227,840.00 USD | 776,280.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 61,750,000.00 USD | 61,750,000.00 USD | 1,350,000.00 USD | 0.00 USD | 899,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 56,730,000.00 USD | 56,730,000.00 USD | 1,480,000.00 USD | 334,090.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 59,500,000.00 USD | 59,500,000.00 USD | 108,640.00 USD | 136,460.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 53,620,000.00 USD | 53,620,000.00 USD | 56,590.00 USD | 268,640.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 81,730.00 USD | 6,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 57,970,000.00 USD | 57,970,000.00 USD | 142,210.00 USD | 9,150.00 USD | 253,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 52,290,000.00 USD | 52,290,000.00 USD | 307,460.00 USD | 66,380.00 USD | 536,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 57,560,000.00 USD | 57,560,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 51,380,000.00 USD | 51,380,000.00 USD | 203,470.00 USD | 49,690.00 USD | 10,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 56,830,000.00 USD | 56,830,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 51,110,000.00 USD | 51,110,000.00 USD | 64,370.00 USD | 321,780.00 USD | 300,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 55,740,000.00 USD | 55,740,000.00 USD | 0.00 USD | 167,460.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 50,420,000.00 USD | 50,420,000.00 USD | 128,220.00 USD | 6,680.00 USD | 443,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 55,560,000.00 USD | 55,560,000.00 USD | 51,610.00 USD | 170,590.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 49,850,000.00 USD | 49,850,000.00 USD | 658,900.00 USD | 656,100.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 6,620,000.00 USD | 6,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 55,310,000.00 USD | 55,310,000.00 USD | 112,770.00 USD | 802,580.00 USD | 790,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 45,340,000.00 USD | 45,340,000.00 USD | 274,000.00 USD | 297,600.00 USD | 830,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 53,600,000.00 USD | 53,600,000.00 USD | 59,160.00 USD | 950,550.00 USD | 528,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 43,940,000.00 USD | 43,940,000.00 USD | 679,470.00 USD | 1,210,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 52,060,000.00 USD | 52,060,000.00 USD | 198,530.00 USD | 1,150,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 39,250,000.00 USD | 39,250,000.00 USD | 255,250.00 USD | 1,320,000.00 USD | 3,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 49,110,000.00 USD | 49,110,000.00 USD | 1,020,000.00 USD | 1,070,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 34,330,000.00 USD | 34,330,000.00 USD | 1,560,000.00 USD | 805,160.00 USD | 2,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 45,420,000.00 USD | 45,420,000.00 USD | 1,660,000.00 USD | 1,990,000.00 USD | 4,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 29,120,000.00 USD | 29,120,000.00 USD | 511,510.00 USD | 1,640,000.00 USD | 2,150,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 59,060.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.24` | 37,400,000.00 USD | 37,400,000.00 USD | 2,040,000.00 USD | 2,080,000.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 24,820,000.00 USD | 24,820,000.00 USD | 429,020.00 USD | 567,990.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 30,250,000.00 USD | 30,250,000.00 USD | 2,870,000.00 USD | 2,120,000.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 22,790,000.00 USD | 22,790,000.00 USD | 918,230.00 USD | 1,100,000.00 USD | 3,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 20,210,000.00 USD | 20,210,000.00 USD | 2,070,000.00 USD | 1,220,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 16,930,000.00 USD | 16,930,000.00 USD | 924,500.00 USD | 624,890.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 14,620,000.00 USD | 14,620,000.00 USD | 1,130,000.00 USD | 510,590.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 13,400,000.00 USD | 13,400,000.00 USD | 889,130.00 USD | 1,030,000.00 USD | 3,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 10,920,000.00 USD | 10,920,000.00 USD | 1,420,000.00 USD | 232,940.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 7,920,000.00 USD | 7,920,000.00 USD | 1,700,000.00 USD | 728,820.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 7,720,000.00 USD | 7,720,000.00 USD | 3,770,000.00 USD | 688,040.00 USD | 3,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 3,880,000.00 USD | 3,880,000.00 USD | 1,200,000.00 USD | 979,690.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 6,650,000.00 USD | 6,650,000.00 USD | 1,630,000.00 USD | 857,970.00 USD | 4,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 13,300,000.00 USD | 13,300,000.00 USD | 1,630,000.00 USD | 857,970.00 USD | 4,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 709,140.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 13,790,000.00 USD | 13,790,000.00 USD | 489,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 1,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 13,860,000.00 USD | 13,860,000.00 USD | 63,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 7,650.00 USD | 242,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 14,010,000.00 USD | 14,010,000.00 USD | 150,010.00 USD | 8,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 14,030,000.00 USD | 14,030,000.00 USD | 0.00 USD | 19,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 24,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 10,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 2,440,000.00 USD | 2,440,000.00 USD | 145,070.00 USD | 8,660.00 USD | 156,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 14,190,000.00 USD | 14,190,000.00 USD | 144,170.00 USD | 3,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 4,390,000.00 USD | 4,390,000.00 USD | 409,480.00 USD | 391,950.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 16,370,000.00 USD | 16,370,000.00 USD | 0.00 USD | 542,940.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 6,970,000.00 USD | 6,970,000.00 USD | 636,140.00 USD | 479,570.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 21,670,000.00 USD | 21,670,000.00 USD | 4,260,000.00 USD | 9,150.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 8,810,000.00 USD | 8,810,000.00 USD | 927,130.00 USD | 221,950.00 USD | 682,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 27,630,000.00 USD | 27,630,000.00 USD | 0.00 USD | 1,870,000.00 USD | 4,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 13,730,000.00 USD | 13,730,000.00 USD | 791,030.00 USD | 1,850,000.00 USD | 2,280,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 32,420,000.00 USD | 32,420,000.00 USD | 138,500.00 USD | 2,750,000.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 19,610,000.00 USD | 19,610,000.00 USD | 734,620.00 USD | 1,660,000.00 USD | 3,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 41,830,000.00 USD | 41,830,000.00 USD | 1,680,000.00 USD | 5,310,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 26,030,000.00 USD | 26,030,000.00 USD | 2,360,000.00 USD | 1,290,000.00 USD | 2,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 59,170,000.00 USD | 59,170,000.00 USD | 2,710,000.00 USD | 3,400,000.00 USD | 11,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 34,650,000.00 USD | 34,650,000.00 USD | 1,200,000.00 USD | 2,670,000.00 USD | 4,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 14,460.00 USD | 14,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.28` | 74,350,000.00 USD | 74,350,000.00 USD | 5,150,000.00 USD | 3,080,000.00 USD | 6,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 41,960,000.00 USD | 41,960,000.00 USD | 2,090,000.00 USD | 1,420,000.00 USD | 3,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 94,010,000.00 USD | 94,010,000.00 USD | 7,780,000.00 USD | 3,760,000.00 USD | 8,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 49,960,000.00 USD | 49,960,000.00 USD | 2,330,000.00 USD | 1,960,000.00 USD | 3,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 97,600,000.00 USD | 97,600,000.00 USD | 0.00 USD | 1,700,000.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 54,200,000.00 USD | 54,200,000.00 USD | 446,410.00 USD | 789,690.00 USD | 3,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 99,630,000.00 USD | 99,630,000.00 USD | 1,030,000.00 USD | 139,170.00 USD | 861,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 58,320,000.00 USD | 58,320,000.00 USD | 1,340,000.00 USD | 600,450.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 103,880,000.00 USD | 103,880,000.00 USD | 1,100,000.00 USD | 1,300,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 61,900,000.00 USD | 61,900,000.00 USD | 904,370.00 USD | 745,190.00 USD | 1,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 243,660.00 USD | 258,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.29` | 109,010,000.00 USD | 109,010,000.00 USD | 796,960.00 USD | 1,560,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 65,150,000.00 USD | 65,150,000.00 USD | 864,310.00 USD | 1,100,000.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 109,730,000.00 USD | 109,730,000.00 USD | 685,300.00 USD | 2,730.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 66,270,000.00 USD | 66,270,000.00 USD | 454,460.00 USD | 148,440.00 USD | 518,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 111,330,000.00 USD | 111,330,000.00 USD | 70,460.00 USD | 277,240.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 67,650,000.00 USD | 67,650,000.00 USD | 186,090.00 USD | 270,800.00 USD | 919,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 113,930,000.00 USD | 113,930,000.00 USD | 1,040,000.00 USD | 202,640.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 71,460,000.00 USD | 71,460,000.00 USD | 570,020.00 USD | 278,090.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 117,570,000.00 USD | 117,570,000.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 77,620,000.00 USD | 77,620,000.00 USD | 1,880,000.00 USD | 719,050.00 USD | 3,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 56,490.00 USD | 314,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.30` | 124,860,000.00 USD | 124,860,000.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 80,210,000.00 USD | 80,210,000.00 USD | 554,720.00 USD | 707,340.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 126,810,000.00 USD | 126,810,000.00 USD | 25,800.00 USD | 173,700.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 81,110,000.00 USD | 81,110,000.00 USD | 440,100.00 USD | 110,110.00 USD | 352,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 129,190,000.00 USD | 129,190,000.00 USD | 208,510.00 USD | 434,510.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 84,130,000.00 USD | 84,130,000.00 USD | 674,250.00 USD | 491,130.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 130,370,000.00 USD | 130,370,000.00 USD | 85,960.00 USD | 944,610.00 USD | 153,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 86,170,000.00 USD | 86,170,000.00 USD | 832,380.00 USD | 554,060.00 USD | 655,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 133,430,000.00 USD | 133,430,000.00 USD | 0.00 USD | 2,170,000.00 USD | 887,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 87,680,000.00 USD | 87,680,000.00 USD | 372,370.00 USD | 679,520.00 USD | 458,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 5,520.00 USD | 320,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.31` | 135,680,000.00 USD | 135,680,000.00 USD | 1,770,000.00 USD | 238,140.00 USD | 245,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 90,980,000.00 USD | 90,980,000.00 USD | 803,720.00 USD | 282,740.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 141,100,000.00 USD | 141,100,000.00 USD | 1,550,000.00 USD | 821,310.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 94,690,000.00 USD | 94,690,000.00 USD | 1,270,000.00 USD | 477,330.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 143,870,000.00 USD | 143,870,000.00 USD | 1,340,000.00 USD | 635,040.00 USD | 789,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 97,460,000.00 USD | 97,460,000.00 USD | 966,790.00 USD | 610,460.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 148,740,000.00 USD | 148,740,000.00 USD | 189,510.00 USD | 858,660.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 99,380,000.00 USD | 99,380,000.00 USD | 515,120.00 USD | 340,250.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 150,040,000.00 USD | 150,040,000.00 USD | 638,380.00 USD | 151,320.00 USD | 501,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 101,450,000.00 USD | 101,450,000.00 USD | 418,640.00 USD | 267,510.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 55,110.00 USD | 375,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.32` | 154,750,000.00 USD | 154,750,000.00 USD | 68,520.00 USD | 1,890,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 106,060,000.00 USD | 106,060,000.00 USD | 1,260,000.00 USD | 633,720.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 159,850,000.00 USD | 159,850,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 110,210,000.00 USD | 110,210,000.00 USD | 1,180,000.00 USD | 585,090.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 161,870,000.00 USD | 161,870,000.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 112,460,000.00 USD | 112,460,000.00 USD | 1,320,000.00 USD | 190,640.00 USD | 744,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 165,230,000.00 USD | 165,230,000.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 115,370,000.00 USD | 115,370,000.00 USD | 885,300.00 USD | 460,840.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 168,010,000.00 USD | 168,010,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 116,370,000.00 USD | 116,370,000.00 USD | 599,940.00 USD | 61,650.00 USD | 341,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 7,390.00 USD | 382,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.33` | 169,810,000.00 USD | 169,810,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 117,450,000.00 USD | 117,450,000.00 USD | 412,050.00 USD | 225,260.00 USD | 436,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 170,910,000.00 USD | 170,910,000.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 118,820,000.00 USD | 118,820,000.00 USD | 504,110.00 USD | 72,470.00 USD | 798,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 172,620,000.00 USD | 172,620,000.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 120,990,000.00 USD | 120,990,000.00 USD | 848,670.00 USD | 101,110.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 175,090,000.00 USD | 175,090,000.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 122,950,000.00 USD | 122,950,000.00 USD | 737,030.00 USD | 194,040.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 177,120,000.00 USD | 177,120,000.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 124,280,000.00 USD | 124,280,000.00 USD | 459,140.00 USD | 356,270.00 USD | 517,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 43,550.00 USD | 426,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.34` | 178,660,000.00 USD | 178,660,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 125,020,000.00 USD | 125,020,000.00 USD | 388,720.00 USD | 23,420.00 USD | 332,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 181,100,000.00 USD | 181,100,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 125,570,000.00 USD | 125,570,000.00 USD | 179,460.00 USD | 82,510.00 USD | 282,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 182,960,000.00 USD | 182,960,000.00 USD | 804,660.00 USD | 463,950.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 126,800,000.00 USD | 126,800,000.00 USD | 572,260.00 USD | 216,630.00 USD | 438,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 188,420,000.00 USD | 188,420,000.00 USD | 2,380,000.00 USD | 2,430,000.00 USD | 660,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 127,980,000.00 USD | 127,980,000.00 USD | 602,090.00 USD | 163,750.00 USD | 420,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 195,550,000.00 USD | 195,550,000.00 USD | 2,000,000.00 USD | 1,890,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 128,990,000.00 USD | 128,990,000.00 USD | 303,380.00 USD | 234,450.00 USD | 470,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,570.00 USD | 432,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.35` | 203,800,000.00 USD | 203,800,000.00 USD | 3,270,000.00 USD | 1,640,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 129,230,000.00 USD | 129,230,000.00 USD | 112,770.00 USD | 29,080.00 USD | 96,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 211,550,000.00 USD | 211,550,000.00 USD | 2,780,000.00 USD | 1,820,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 129,780,000.00 USD | 129,780,000.00 USD | 249,180.00 USD | 23,180.00 USD | 275,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 219,570,000.00 USD | 219,570,000.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 130,190,000.00 USD | 130,190,000.00 USD | 146,270.00 USD | 30,410.00 USD | 237,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 228,690,000.00 USD | 228,690,000.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 130,340,000.00 USD | 130,340,000.00 USD | 66,220.00 USD | 30,780.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 235,440,000.00 USD | 235,440,000.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 130,860,000.00 USD | 130,860,000.00 USD | 86,720.00 USD | 34,870.00 USD | 395,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 7,930.00 USD | 440,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.36` | 241,780,000.00 USD | 241,780,000.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 131,810,000.00 USD | 131,810,000.00 USD | 391,410.00 USD | 32,820.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 244,320,000.00 USD | 244,320,000.00 USD | 1,060,000.00 USD | 639,580.00 USD | 837,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 132,150,000.00 USD | 132,150,000.00 USD | 209,880.00 USD | 43,200.00 USD | 82,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 246,960,000.00 USD | 246,960,000.00 USD | 1,300,000.00 USD | 282,890.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 132,800,000.00 USD | 132,800,000.00 USD | 225,120.00 USD | 162,390.00 USD | 269,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 250,490,000.00 USD | 250,490,000.00 USD | 1,480,000.00 USD | 652,340.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 133,100,000.00 USD | 133,100,000.00 USD | 130,140.00 USD | 3,300.00 USD | 166,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 253,230,000.00 USD | 253,230,000.00 USD | 1,420,000.00 USD | 616,140.00 USD | 698,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 133,220,000.00 USD | 133,220,000.00 USD | 0.00 USD | 12,740.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 99,580.00 USD | 540,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.37` | 254,050,000.00 USD | 254,050,000.00 USD | 206,650.00 USD | 189,790.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 133,480,000.00 USD | 133,480,000.00 USD | 59,970.00 USD | 89,800.00 USD | 103,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 255,100,000.00 USD | 255,100,000.00 USD | 486,840.00 USD | 176,380.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 133,620,000.00 USD | 133,620,000.00 USD | 93,070.00 USD | 21,460.00 USD | 28,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 256,410,000.00 USD | 256,410,000.00 USD | 367,350.00 USD | 211,750.00 USD | 733,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 133,720,000.00 USD | 133,720,000.00 USD | 5,340.00 USD | 39,430.00 USD | 60,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 257,650,000.00 USD | 257,650,000.00 USD | 393,010.00 USD | 171,680.00 USD | 667,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 133,820,000.00 USD | 133,820,000.00 USD | 6,270.00 USD | 2,870.00 USD | 86,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 259,320,000.00 USD | 259,320,000.00 USD | 563,840.00 USD | 386,690.00 USD | 717,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 134,150,000.00 USD | 134,150,000.00 USD | 97,300.00 USD | 58,310.00 USD | 172,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 3,780.00 USD | 544,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.38` | 260,340,000.00 USD | 260,340,000.00 USD | 242,030.00 USD | 273,360.00 USD | 514,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 134,460,000.00 USD | 134,460,000.00 USD | 33,730.00 USD | 42,100.00 USD | 236,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 261,910,000.00 USD | 261,910,000.00 USD | 692,200.00 USD | 267,730.00 USD | 600,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 134,810,000.00 USD | 134,810,000.00 USD | 74,730.00 USD | 82,870.00 USD | 192,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 263,610,000.00 USD | 263,610,000.00 USD | 436,360.00 USD | 195,830.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 134,880,000.00 USD | 134,880,000.00 USD | 2,300.00 USD | 65,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 265,570,000.00 USD | 265,570,000.00 USD | 710,620.00 USD | 348,810.00 USD | 900,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 135,350,000.00 USD | 135,350,000.00 USD | 7,000.00 USD | 44,910.00 USD | 421,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 266,550,000.00 USD | 266,550,000.00 USD | 403,730.00 USD | 253,120.00 USD | 325,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 135,540,000.00 USD | 135,540,000.00 USD | 88,690.00 USD | 52,980.00 USD | 41,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 649,900.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.39` | 267,660,000.00 USD | 267,660,000.00 USD | 377,810.00 USD | 322,570.00 USD | 413,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 135,930,000.00 USD | 135,930,000.00 USD | 4,270.00 USD | 166,580.00 USD | 224,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 268,870,000.00 USD | 268,870,000.00 USD | 384,080.00 USD | 308,280.00 USD | 518,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 136,160,000.00 USD | 136,160,000.00 USD | 81,050.00 USD | 49,560.00 USD | 97,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 269,620,000.00 USD | 269,620,000.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 136,180,000.00 USD | 136,180,000.00 USD | 0.00 USD | 18,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 270,150,000.00 USD | 270,150,000.00 USD | 82,350.00 USD | 90,970.00 USD | 358,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 270,320,000.00 USD | 270,320,000.00 USD | 39,170.00 USD | 22,660.00 USD | 101,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 2,310.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 270,540,000.00 USD | 270,540,000.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 270,550,000.00 USD | 270,550,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 270,610,000.00 USD | 270,610,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 270,690,000.00 USD | 270,690,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 270,980,000.00 USD | 270,980,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 858.46 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 271,140,000.00 USD | 271,140,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 271,280,000.00 USD | 271,280,000.00 USD | 4,390.00 USD | 15,880.00 USD | 120,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 271,560,000.00 USD | 271,560,000.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,690.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 1,220.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 284.66 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 129,900.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 551.65 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,150.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 11,820.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 323.30 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 174.99 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 1,370.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 1,790.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,900.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 13,390.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 4,580,000.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 239.15 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 2,530.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 401.38 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 8,640.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 5,020.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 4,060.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 232.21 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 110,470.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,870.00 USD | 6,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 1,160.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 808.37 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 5,450,000.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 130,160.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 7,940.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 4,240.00 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 747.78 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 12,290.00 USD | 11,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 30,700.00 USD | 11,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 9,340.00 USD | 11,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 428.50 USD | 11,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,010.00 USD | 11,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 2,930,000.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 309,780.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 373.38 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 1,410.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 945.17 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 230,510.00 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 2,410,000.00 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 178.20 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 198.36 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 460.50 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 296.73 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 331.01 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 673.60 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 426,100.00 USD | 18,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 331,410.00 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 433.29 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 52,320.00 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 201.02 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 438.80 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 2,140.00 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 82,220.00 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 102.81 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 224.50 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 11,380.00 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 248.94 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 358.05 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 49,200.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 180.56 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 13,230.00 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 18,290.00 USD | 18,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 81,970.00 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 4,080.00 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 678.62 USD | 18,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 24,250.00 USD | 18,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 657.45 USD | 18,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 3,740.00 USD | 18,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 3,710,000.00 USD | 22,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 2,310.00 USD | 22,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 1,860.00 USD | 22,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 1,530,000.00 USD | 24,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 59,380.00 USD | 24,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 64,650,000.00 USD | 0.00 USD | 1,970.00 USD | `-79.60%` | `7,717.00` |
| `Live` | `Long` | `0.2650` | 64,650,000.00 USD | 0.00 USD | 3,860.00 USD | `-78.79%` | `14,556.00` |
| `Live` | `Long` | `0.2750` | 64,650,000.00 USD | 0.00 USD | 3,350.00 USD | `-77.99%` | `12,190.00` |
| `Live` | `Long` | `0.2850` | 64,650,000.00 USD | 0.00 USD | 864.41 USD | `-77.19%` | `3,033.00` |
| `Live` | `Long` | `0.3050` | 64,640,000.00 USD | 0.00 USD | 235.16 USD | `-75.59%` | `771.00` |
| `Live` | `Long` | `0.3150` | 64,640,000.00 USD | 0.00 USD | 4,910.00 USD | `-74.79%` | `15,577.00` |
| `Live` | `Long` | `0.3350` | 64,640,000.00 USD | 0.00 USD | 1,220.00 USD | `-73.19%` | `3,636.00` |
| `Live` | `Long` | `0.3450` | 64,640,000.00 USD | 0.00 USD | 6,180.00 USD | `-72.39%` | `17,916.00` |
| `Live` | `Long` | `0.3550` | 64,630,000.00 USD | 0.00 USD | 2,470.00 USD | `-71.59%` | `6,970.00` |
| `Live` | `Long` | `0.3650` | 64,630,000.00 USD | 0.00 USD | 53,790.00 USD | `-70.79%` | `147,378.00` |
| `Live` | `Long` | `0.3750` | 64,580,000.00 USD | 0.00 USD | 7,140.00 USD | `-69.99%` | `19,043.00` |
| `Live` | `Long` | `0.3850` | 64,570,000.00 USD | 0.00 USD | 8,020.00 USD | `-69.19%` | `20,836.00` |
| `Live` | `Long` | `0.3950` | 64,560,000.00 USD | 0.00 USD | 174.59 USD | `-68.39%` | `442.00` |
| `Live` | `Long` | `0.4050` | 64,560,000.00 USD | 0.00 USD | 167.27 USD | `-67.59%` | `413.00` |
| `Live` | `Long` | `0.4150` | 64,560,000.00 USD | 0.00 USD | 967.78 USD | `-66.79%` | `2,332.00` |
| `Live` | `Long` | `0.4250` | 64,560,000.00 USD | 0.00 USD | 30,360.00 USD | `-65.99%` | `71,435.00` |
| `Live` | `Long` | `0.4350` | 64,530,000.00 USD | 0.00 USD | 12,330.00 USD | `-65.19%` | `28,353.00` |
| `Live` | `Long` | `0.4450` | 64,520,000.00 USD | 0.00 USD | 1,540.00 USD | `-64.39%` | `3,467.00` |
| `Live` | `Long` | `0.4550` | 64,510,000.00 USD | 0.00 USD | 595,960.00 USD | `-63.59%` | `1,309,807.00` |
| `Live` | `Long` | `0.4650` | 63,920,000.00 USD | 0.00 USD | 2,200.00 USD | `-62.79%` | `4,729.00` |
| `Live` | `Long` | `0.4750` | 63,920,000.00 USD | 0.00 USD | 987.52 USD | `-61.99%` | `2,079.00` |
| `Live` | `Long` | `0.4850` | 63,920,000.00 USD | 0.00 USD | 170,070.00 USD | `-61.19%` | `350,668.00` |
| `Live` | `Long` | `0.4950` | 63,750,000.00 USD | 0.00 USD | 3,990.00 USD | `-60.39%` | `8,062.00` |
| `Live` | `Long` | `0.5050` | 63,740,000.00 USD | 0.00 USD | 371.18 USD | `-59.59%` | `735.00` |
| `Live` | `Long` | `0.5250` | 63,740,000.00 USD | 0.00 USD | 2,620.00 USD | `-57.99%` | `4,991.00` |
| `Live` | `Long` | `0.5350` | 63,740,000.00 USD | 0.00 USD | 2,000.00 USD | `-57.19%` | `3,741.00` |
| `Live` | `Long` | `0.5450` | 63,740,000.00 USD | 0.00 USD | 3,430.00 USD | `-56.39%` | `6,293.00` |
| `Live` | `Long` | `0.5550` | 63,730,000.00 USD | 0.00 USD | 14,250.00 USD | `-55.59%` | `25,672.00` |
| `Live` | `Long` | `0.5650` | 63,720,000.00 USD | 0.00 USD | 177,740.00 USD | `-54.79%` | `314,578.00` |
| `Live` | `Long` | `0.5750` | 63,540,000.00 USD | 0.00 USD | 6,200.00 USD | `-53.99%` | `10,784.00` |
| `Live` | `Long` | `0.5850` | 63,530,000.00 USD | 0.00 USD | 5,800.00 USD | `-53.19%` | `9,907.00` |
| `Live` | `Long` | `0.6050` | 63,530,000.00 USD | 0.00 USD | 32,730.00 USD | `-51.59%` | `54,098.00` |
| `Live` | `Long` | `0.6150` | 63,500,000.00 USD | 0.00 USD | 37,700.00 USD | `-50.79%` | `61,305.00` |
| `Live` | `Long` | `0.6250` | 63,460,000.00 USD | 0.00 USD | 9,170.00 USD | `-49.99%` | `14,668.00` |
| `Live` | `Long` | `0.6350` | 63,450,000.00 USD | 0.00 USD | 10,510.00 USD | `-49.19%` | `16,554.00` |
| `Live` | `Long` | `0.6450` | 63,440,000.00 USD | 0.00 USD | 19,340.00 USD | `-48.39%` | `29,983.00` |
| `Live` | `Long` | `0.6550` | 63,420,000.00 USD | 0.00 USD | 1,830.00 USD | `-47.59%` | `2,788.00` |
| `Live` | `Long` | `0.6650` | 63,420,000.00 USD | 0.00 USD | 17,310.00 USD | `-46.79%` | `26,027.00` |
| `Live` | `Long` | `0.6750` | 63,400,000.00 USD | 0.00 USD | 29,510.00 USD | `-45.99%` | `43,712.00` |
| `Live` | `Long` | `0.6850` | 63,370,000.00 USD | 0.00 USD | 4,230.00 USD | `-45.19%` | `6,172.00` |
| `Live` | `Long` | `0.6950` | 63,370,000.00 USD | 0.00 USD | 152,040.00 USD | `-44.39%` | `218,767.00` |
| `Live` | `Long` | `0.7050` | 63,210,000.00 USD | 0.00 USD | 32,690.00 USD | `-43.59%` | `46,363.00` |
| `Live` | `Long` | `0.7150` | 63,180,000.00 USD | 0.00 USD | 67,660.00 USD | `-42.79%` | `94,630.00` |
| `Live` | `Long` | `0.7250` | 63,110,000.00 USD | 0.00 USD | 216,840.00 USD | `-41.99%` | `299,086.00` |
| `Live` | `Long` | `0.7350` | 62,900,000.00 USD | 0.00 USD | 41,820.00 USD | `-41.19%` | `56,895.00` |
| `Live` | `Long` | `0.7450` | 62,860,000.00 USD | 0.00 USD | 77,980.00 USD | `-40.39%` | `104,674.00` |
| `Live` | `Long` | `0.7550` | 62,780,000.00 USD | 0.00 USD | 115,930.00 USD | `-39.59%` | `153,553.00` |
| `Live` | `Long` | `0.7650` | 62,660,000.00 USD | 0.00 USD | 64,620.00 USD | `-38.79%` | `84,473.00` |
| `Live` | `Long` | `0.7750` | 62,600,000.00 USD | 0.00 USD | 5,930.00 USD | `-37.99%` | `7,651.00` |
| `Live` | `Long` | `0.7850` | 62,590,000.00 USD | 0.00 USD | 16,840.00 USD | `-37.18%` | `21,451.00` |
| `Live` | `Long` | `0.7950` | 62,570,000.00 USD | 0.00 USD | 11,250.00 USD | `-36.38%` | `14,145.00` |
| `Live` | `Long` | `0.8050` | 62,560,000.00 USD | 0.00 USD | 520,520.00 USD | `-35.58%` | `646,603.00` |
| `Live` | `Long` | `0.8150` | 62,040,000.00 USD | 0.00 USD | 47,390.00 USD | `-34.78%` | `58,149.00` |
| `Live` | `Long` | `0.8250` | 62,000,000.00 USD | 0.00 USD | 19,520.00 USD | `-33.98%` | `23,656.00` |
| `Live` | `Long` | `0.8350` | 61,980,000.00 USD | 0.00 USD | 37,780.00 USD | `-33.18%` | `45,244.00` |
| `Live` | `Long` | `0.8450` | 61,940,000.00 USD | 0.00 USD | 58,470.00 USD | `-32.38%` | `69,192.00` |
| `Live` | `Long` | `0.8550` | 61,880,000.00 USD | 0.00 USD | 3,080,000.00 USD | `-31.58%` | `3,606,628.00` |
| `Live` | `Long` | `0.8650` | 58,800,000.00 USD | 0.00 USD | 34,850.00 USD | `-30.78%` | `40,293.00` |
| `Live` | `Long` | `0.8750` | 58,760,000.00 USD | 0.00 USD | 100,640.00 USD | `-29.98%` | `115,016.00` |
| `Live` | `Long` | `0.8850` | 58,660,000.00 USD | 0.00 USD | 409,130.00 USD | `-29.18%` | `462,299.00` |
| `Live` | `Long` | `0.8950` | 58,250,000.00 USD | 0.00 USD | 149,180.00 USD | `-28.38%` | `166,676.00` |
| `Live` | `Long` | `0.9050` | 58,100,000.00 USD | 0.00 USD | 141,240.00 USD | `-27.58%` | `156,071.00` |
| `Live` | `Long` | `0.9150` | 57,960,000.00 USD | 0.00 USD | 78,240.00 USD | `-26.78%` | `85,507.00` |
| `Live` | `Long` | `0.9250` | 57,880,000.00 USD | 0.00 USD | 73,880.00 USD | `-25.98%` | `79,865.00` |
| `Live` | `Long` | `0.9350` | 57,810,000.00 USD | 0.00 USD | 98,970.00 USD | `-25.18%` | `105,845.00` |
| `Live` | `Long` | `0.9450` | 57,710,000.00 USD | 0.00 USD | 58,620.00 USD | `-24.38%` | `62,036.00` |
| `Live` | `Long` | `0.9550` | 57,650,000.00 USD | 0.00 USD | 83,870.00 USD | `-23.58%` | `87,821.00` |
| `Live` | `Long` | `0.9650` | 57,570,000.00 USD | 0.00 USD | 33,980,000.00 USD | `-22.78%` | `35,208,016.00` |
| `Live` | `Long` | `0.9750` | 23,590,000.00 USD | 0.00 USD | 153,270.00 USD | `-21.98%` | `157,196.00` |
| `Live` | `Long` | `0.9850` | 23,440,000.00 USD | 0.00 USD | 447,720.00 USD | `-21.18%` | `454,534.00` |
| `Live` | `Long` | `0.9950` | 22,990,000.00 USD | 0.00 USD | 120,630.00 USD | `-20.38%` | `121,234.00` |
| `Live` | `Long` | `1.00` | 22,870,000.00 USD | 0.00 USD | 471,340.00 USD | `-19.58%` | `468,997.00` |
| `Live` | `Long` | `1.01` | 22,400,000.00 USD | 0.00 USD | 303,520.00 USD | `-18.78%` | `299,030.00` |
| `Live` | `Long` | `1.02` | 22,100,000.00 USD | 0.00 USD | 2,710,000.00 USD | `-17.98%` | `2,642,875.00` |
| `Live` | `Long` | `1.03` | 19,390,000.00 USD | 0.00 USD | 2,130,000.00 USD | `-17.18%` | `2,062,761.00` |
| `Live` | `Long` | `1.04` | 17,250,000.00 USD | 0.00 USD | 241,120.00 USD | `-16.38%` | `230,733.00` |
| `Live` | `Long` | `1.05` | 17,010,000.00 USD | 0.00 USD | 1,660,000.00 USD | `-15.58%` | `1,575,028.00` |
| `Live` | `Long` | `1.06` | 15,350,000.00 USD | 0.00 USD | 386,620.00 USD | `-14.78%` | `363,022.00` |
| `Live` | `Long` | `1.07` | 14,960,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-13.98%` | `1,168,042.00` |
| `Live` | `Long` | `1.08` | 13,710,000.00 USD | 0.00 USD | 199,330.00 USD | `-13.18%` | `183,718.00` |
| `Live` | `Long` | `1.09` | 13,510,000.00 USD | 0.00 USD | 411,770.00 USD | `-12.38%` | `376,042.00` |
| `Live` | `Long` | `1.10` | 13,100,000.00 USD | 0.00 USD | 101,190.00 USD | `-11.58%` | `91,575.00` |
| `Live` | `Long` | `1.11` | 12,990,000.00 USD | 0.00 USD | 285,030.00 USD | `-10.78%` | `255,635.00` |
| `Live` | `Long` | `1.12` | 12,710,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-9.98%` | `1,913,541.00` |
| `Live` | `Long` | `1.14` | 10,560,000.00 USD | 0.00 USD | 464,270.00 USD | `-9.18%` | `409,052.00` |
| `Live` | `Long` | `1.15` | 10,090,000.00 USD | 0.00 USD | 284,740.00 USD | `-8.38%` | `248,677.00` |
| `Live` | `Long` | `1.16` | 9,810,000.00 USD | 0.00 USD | 361,700.00 USD | `-7.58%` | `313,158.00` |
| `Live` | `Long` | `1.17` | 9,450,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-6.78%` | `1,103,539.00` |
| `Live` | `Long` | `1.18` | 8,160,000.00 USD | 0.00 USD | 274,850.00 USD | `-5.98%` | `233,916.00` |
| `Live` | `Long` | `1.19` | 7,880,000.00 USD | 0.00 USD | 530,310.00 USD | `-5.18%` | `447,521.00` |
| `Live` | `Long` | `1.20` | 7,350,000.00 USD | 0.00 USD | 591,080.00 USD | `-4.38%` | `494,630.00` |
| `Live` | `Long` | `1.21` | 6,760,000.00 USD | 0.00 USD | 3,290.00 USD | `-3.58%` | `2,728.00` |
| `Live` | `Long` | `1.22` | 6,760,000.00 USD | 0.00 USD | 81,730.00 USD | `-2.78%` | `67,269.00` |
| `Live` | `Long` | `1.23` | 6,680,000.00 USD | 0.00 USD | 6,620,000.00 USD | `-1.98%` | `5,403,657.00` |
| `Live` | `Long` | `1.24` | 59,060.00 USD | 0.00 USD | 59,060.00 USD | `-1.18%` | `47,823.00` |
| `Live` | `Short` | `1.27` | 14,460.00 USD | 14,460.00 USD | 0.00 USD | `+2.02%` | `11,339.00` |
| `Live` | `Short` | `1.28` | 258,120.00 USD | 243,660.00 USD | 0.00 USD | `+2.82%` | `189,621.00` |
| `Live` | `Short` | `1.29` | 314,610.00 USD | 56,490.00 USD | 0.00 USD | `+3.62%` | `43,622.00` |
| `Live` | `Short` | `1.30` | 320,130.00 USD | 5,520.00 USD | 0.00 USD | `+4.43%` | `4,227.00` |
| `Live` | `Short` | `1.31` | 375,240.00 USD | 55,110.00 USD | 0.00 USD | `+5.23%` | `41,912.00` |
| `Live` | `Short` | `1.32` | 382,630.00 USD | 7,390.00 USD | 0.00 USD | `+6.03%` | `5,576.00` |
| `Live` | `Short` | `1.33` | 426,180.00 USD | 43,550.00 USD | 0.00 USD | `+6.83%` | `32,622.00` |
| `Live` | `Short` | `1.34` | 432,750.00 USD | 6,570.00 USD | 0.00 USD | `+7.63%` | `4,885.00` |
| `Live` | `Short` | `1.35` | 440,680.00 USD | 7,930.00 USD | 0.00 USD | `+8.43%` | `5,850.00` |
| `Live` | `Short` | `1.36` | 540,250.00 USD | 99,580.00 USD | 0.00 USD | `+9.23%` | `72,950.00` |
| `Live` | `Short` | `1.38` | 544,030.00 USD | 3,780.00 USD | 0.00 USD | `+10.03%` | `2,747.00` |
| `Live` | `Short` | `1.39` | 1,190,000.00 USD | 649,900.00 USD | 0.00 USD | `+10.83%` | `469,242.00` |
| `Live` | `Short` | `1.40` | 1,200,000.00 USD | 2,310.00 USD | 0.00 USD | `+11.63%` | `1,659.00` |
| `Live` | `Short` | `1.41` | 1,200,000.00 USD | 858.46 USD | 0.00 USD | `+12.43%` | `611.00` |
| `Live` | `Short` | `1.42` | 1,200,000.00 USD | 3,860.00 USD | 0.00 USD | `+13.23%` | `2,729.00` |
| `Live` | `Short` | `1.43` | 1,290,000.00 USD | 93,690.00 USD | 0.00 USD | `+14.03%` | `65,744.00` |
| `Live` | `Short` | `1.44` | 1,300,000.00 USD | 1,220.00 USD | 0.00 USD | `+14.83%` | `848.00` |
| `Live` | `Short` | `1.45` | 1,300,000.00 USD | 284.66 USD | 0.00 USD | `+15.63%` | `197.00` |
| `Live` | `Short` | `1.47` | 1,430,000.00 USD | 129,900.00 USD | 0.00 USD | `+17.23%` | `88,671.00` |
| `Live` | `Short` | `1.48` | 1,430,000.00 USD | 551.65 USD | 0.00 USD | `+18.03%` | `374.00` |
| `Live` | `Short` | `1.50` | 1,440,000.00 USD | 12,150.00 USD | 0.00 USD | `+19.63%` | `8,126.00` |
| `Live` | `Short` | `1.51` | 1,450,000.00 USD | 11,820.00 USD | 0.00 USD | `+21.23%` | `7,799.00` |
| `Live` | `Short` | `1.52` | 1,450,000.00 USD | 323.30 USD | 0.00 USD | `+22.03%` | `212.00` |
| `Live` | `Short` | `1.53` | 1,450,000.00 USD | 174.99 USD | 0.00 USD | `+22.83%` | `114.00` |
| `Live` | `Short` | `1.54` | 1,450,000.00 USD | 1,370.00 USD | 0.00 USD | `+23.63%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,450,000.00 USD | 1,360.00 USD | 0.00 USD | `+24.43%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,460,000.00 USD | 1,790.00 USD | 0.00 USD | `+25.23%` | `1,144.00` |
| `Live` | `Short` | `1.57` | 1,460,000.00 USD | 2,900.00 USD | 0.00 USD | `+26.03%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 1,470,000.00 USD | 13,390.00 USD | 0.00 USD | `+26.83%` | `8,445.00` |
| `Live` | `Short` | `1.59` | 6,050,000.00 USD | 4,580,000.00 USD | 0.00 USD | `+27.63%` | `2,872,725.00` |
| `Live` | `Short` | `1.60` | 6,050,000.00 USD | 239.15 USD | 0.00 USD | `+28.43%` | `149.00` |
| `Live` | `Short` | `1.61` | 6,060,000.00 USD | 2,530.00 USD | 0.00 USD | `+29.23%` | `1,567.00` |
| `Live` | `Short` | `1.62` | 6,060,000.00 USD | 401.38 USD | 0.00 USD | `+30.03%` | `247.00` |
| `Live` | `Short` | `1.64` | 6,070,000.00 USD | 8,640.00 USD | 0.00 USD | `+30.83%` | `5,284.00` |
| `Live` | `Short` | `1.66` | 6,070,000.00 USD | 147.30 USD | 0.00 USD | `+32.43%` | `89.00` |
| `Live` | `Short` | `1.67` | 6,070,000.00 USD | 586.08 USD | 0.00 USD | `+33.23%` | `352.00` |
| `Live` | `Short` | `1.68` | 6,070,000.00 USD | 5,020.00 USD | 0.00 USD | `+34.03%` | `3,000.00` |
| `Live` | `Short` | `1.69` | 6,080,000.00 USD | 4,060.00 USD | 0.00 USD | `+34.83%` | `2,409.00` |
| `Live` | `Short` | `1.70` | 6,080,000.00 USD | 232.21 USD | 0.00 USD | `+35.63%` | `137.00` |
| `Live` | `Short` | `1.71` | 6,080,000.00 USD | 1,980.00 USD | 0.00 USD | `+36.43%` | `1,163.00` |
| `Live` | `Short` | `1.73` | 6,190,000.00 USD | 110,470.00 USD | 0.00 USD | `+38.03%` | `64,043.00` |
| `Live` | `Short` | `1.74` | 6,190,000.00 USD | 2,970.00 USD | 0.00 USD | `+38.83%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 6,190,000.00 USD | 2,870.00 USD | 0.00 USD | `+39.63%` | `1,642.00` |
| `Live` | `Short` | `1.75` | 6,200,000.00 USD | 1,160.00 USD | 0.00 USD | `+40.43%` | `661.00` |
| `Live` | `Short` | `1.76` | 6,200,000.00 USD | 808.37 USD | 0.00 USD | `+41.23%` | `458.00` |
| `Live` | `Short` | `1.77` | 11,650,000.00 USD | 5,450,000.00 USD | 0.00 USD | `+42.03%` | `3,070,483.00` |
| `Live` | `Short` | `1.78` | 11,780,000.00 USD | 130,160.00 USD | 0.00 USD | `+42.83%` | `72,921.00` |
| `Live` | `Short` | `1.79` | 11,780,000.00 USD | 7,940.00 USD | 0.00 USD | `+43.63%` | `4,422.00` |
| `Live` | `Short` | `1.80` | 11,790,000.00 USD | 4,240.00 USD | 0.00 USD | `+44.43%` | `2,347.00` |
| `Live` | `Short` | `1.81` | 11,790,000.00 USD | 747.78 USD | 0.00 USD | `+45.23%` | `412.00` |
| `Live` | `Short` | `1.82` | 11,800,000.00 USD | 12,290.00 USD | 0.00 USD | `+46.04%` | `6,735.00` |
| `Live` | `Short` | `1.83` | 11,830,000.00 USD | 30,700.00 USD | 0.00 USD | `+46.84%` | `16,729.00` |
| `Live` | `Short` | `1.84` | 11,840,000.00 USD | 9,340.00 USD | 0.00 USD | `+47.64%` | `5,061.00` |
| `Live` | `Short` | `1.85` | 11,840,000.00 USD | 428.50 USD | 0.00 USD | `+48.44%` | `231.00` |
| `Live` | `Short` | `1.86` | 11,840,000.00 USD | 2,010.00 USD | 0.00 USD | `+49.24%` | `1,079.00` |
| `Live` | `Short` | `1.89` | 14,770,000.00 USD | 2,930,000.00 USD | 0.00 USD | `+50.84%` | `1,551,725.00` |
| `Live` | `Short` | `1.90` | 15,080,000.00 USD | 309,780.00 USD | 0.00 USD | `+51.64%` | `163,470.00` |
| `Live` | `Short` | `1.91` | 15,080,000.00 USD | 373.38 USD | 0.00 USD | `+52.44%` | `196.00` |
| `Live` | `Short` | `1.92` | 15,080,000.00 USD | 1,410.00 USD | 0.00 USD | `+53.24%` | `737.00` |
| `Live` | `Short` | `1.93` | 15,080,000.00 USD | 945.17 USD | 0.00 USD | `+54.04%` | `491.00` |
| `Live` | `Short` | `1.96` | 15,080,000.00 USD | 293.25 USD | 0.00 USD | `+56.44%` | `150.00` |
| `Live` | `Short` | `1.97` | 15,310,000.00 USD | 230,510.00 USD | 0.00 USD | `+57.24%` | `117,306.00` |
| `Live` | `Short` | `1.98` | 15,310,000.00 USD | 651.75 USD | 0.00 USD | `+58.04%` | `330.00` |
| `Live` | `Short` | `2.02` | 17,720,000.00 USD | 2,410,000.00 USD | 0.00 USD | `+61.24%` | `1,196,812.00` |
| `Live` | `Short` | `2.02` | 17,720,000.00 USD | 178.20 USD | 0.00 USD | `+62.04%` | `88.00` |
| `Live` | `Short` | `2.04` | 17,720,000.00 USD | 198.36 USD | 0.00 USD | `+63.64%` | `97.00` |
| `Live` | `Short` | `2.06` | 17,730,000.00 USD | 460.50 USD | 0.00 USD | `+65.24%` | `223.00` |
| `Live` | `Short` | `2.08` | 17,730,000.00 USD | 296.73 USD | 0.00 USD | `+66.04%` | `143.00` |
| `Live` | `Short` | `2.10` | 17,730,000.00 USD | 331.01 USD | 0.00 USD | `+67.64%` | `158.00` |
| `Live` | `Short` | `2.10` | 17,730,000.00 USD | 673.60 USD | 0.00 USD | `+68.44%` | `320.00` |
| `Live` | `Short` | `2.12` | 18,150,000.00 USD | 426,100.00 USD | 0.00 USD | `+69.24%` | `201,468.00` |
| `Live` | `Short` | `2.12` | 18,480,000.00 USD | 331,410.00 USD | 0.00 USD | `+70.04%` | `155,959.00` |
| `Live` | `Short` | `2.15` | 18,480,000.00 USD | 433.29 USD | 0.00 USD | `+71.64%` | `202.00` |
| `Live` | `Short` | `2.15` | 18,480,000.00 USD | 196.11 USD | 0.00 USD | `+72.44%` | `91.00` |
| `Live` | `Short` | `2.17` | 18,540,000.00 USD | 52,320.00 USD | 0.00 USD | `+74.04%` | `24,057.00` |
| `Live` | `Short` | `2.19` | 18,540,000.00 USD | 201.02 USD | 0.00 USD | `+74.84%` | `92.00` |
| `Live` | `Short` | `2.21` | 18,540,000.00 USD | 438.80 USD | 0.00 USD | `+76.44%` | `199.00` |
| `Live` | `Short` | `2.21` | 18,540,000.00 USD | 2,140.00 USD | 0.00 USD | `+77.24%` | `965.00` |
| `Live` | `Short` | `2.23` | 18,620,000.00 USD | 82,220.00 USD | 0.00 USD | `+78.04%` | `36,955.00` |
| `Live` | `Short` | `2.23` | 18,620,000.00 USD | 102.81 USD | 0.00 USD | `+78.84%` | `46.00` |
| `Live` | `Short` | `2.25` | 18,620,000.00 USD | 224.50 USD | 0.00 USD | `+79.64%` | `100.00` |
| `Live` | `Short` | `2.25` | 18,630,000.00 USD | 11,380.00 USD | 0.00 USD | `+80.44%` | `5,046.00` |
| `Live` | `Short` | `2.31` | 18,630,000.00 USD | 248.94 USD | 0.00 USD | `+84.44%` | `108.00` |
| `Live` | `Short` | `2.33` | 18,630,000.00 USD | 358.05 USD | 0.00 USD | `+86.04%` | `154.00` |
| `Live` | `Short` | `2.33` | 18,680,000.00 USD | 49,200.00 USD | 0.00 USD | `+86.84%` | `21,072.00` |
| `Live` | `Short` | `2.35` | 18,680,000.00 USD | 180.56 USD | 0.00 USD | `+87.65%` | `77.00` |
| `Live` | `Short` | `2.35` | 18,700,000.00 USD | 13,230.00 USD | 0.00 USD | `+88.45%` | `5,619.00` |
| `Live` | `Short` | `2.37` | 18,720,000.00 USD | 18,290.00 USD | 0.00 USD | `+89.25%` | `7,734.00` |
| `Live` | `Short` | `2.38` | 18,800,000.00 USD | 81,970.00 USD | 0.00 USD | `+90.05%` | `34,513.00` |
| `Live` | `Short` | `2.40` | 18,800,000.00 USD | 4,080.00 USD | 0.00 USD | `+92.45%` | `1,698.00` |
| `Live` | `Short` | `2.42` | 18,800,000.00 USD | 678.62 USD | 0.00 USD | `+93.25%` | `281.00` |
| `Live` | `Short` | `2.42` | 18,830,000.00 USD | 24,250.00 USD | 0.00 USD | `+94.05%` | `10,000.00` |
| `Live` | `Short` | `2.44` | 18,830,000.00 USD | 657.45 USD | 0.00 USD | `+94.85%` | `270.00` |
| `Live` | `Short` | `2.44` | 18,830,000.00 USD | 3,740.00 USD | 0.00 USD | `+95.65%` | `1,528.00` |
| `Live` | `Short` | `2.46` | 22,540,000.00 USD | 3,710,000.00 USD | 0.00 USD | `+96.45%` | `1,511,779.00` |
| `Live` | `Short` | `2.46` | 22,540,000.00 USD | 2,310.00 USD | 0.00 USD | `+97.25%` | `937.00` |
| `Live` | `Short` | `2.48` | 22,550,000.00 USD | 1,860.00 USD | 0.00 USD | `+98.05%` | `750.00` |
| `Live` | `Short` | `2.48` | 24,070,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+98.85%` | `613,782.00` |
| `Live` | `Short` | `2.50` | 24,130,000.00 USD | 59,380.00 USD | 0.00 USD | `+99.65%` | `23,798.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 3,900,000.00 USD | 0.00 USD | 102.00 USD | `-79.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3650` | 3,900,000.00 USD | 0.00 USD | 351.50 USD | `-70.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 3,900,000.00 USD | 0.00 USD | 139.12 USD | `-69.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3950` | 3,900,000.00 USD | 0.00 USD | 2,880.00 USD | `-68.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4050` | 3,900,000.00 USD | 0.00 USD | 2,950.00 USD | `-67.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 3,890,000.00 USD | 0.00 USD | 408.51 USD | `-64.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 3,890,000.00 USD | 0.00 USD | 273.00 USD | `-63.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 3,890,000.00 USD | 0.00 USD | 151.12 USD | `-62.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 3,890,000.00 USD | 0.00 USD | 142.50 USD | `-61.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 3,890,000.00 USD | 0.00 USD | 145.50 USD | `-61.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4950` | 3,890,000.00 USD | 0.00 USD | 562.81 USD | `-60.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 3,890,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 3,890,000.00 USD | 0.00 USD | 285.82 USD | `-58.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 3,890,000.00 USD | 0.00 USD | 306.60 USD | `-57.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 3,890,000.00 USD | 0.00 USD | 121.55 USD | `-55.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 3,890,000.00 USD | 0.00 USD | 656.53 USD | `-54.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 3,890,000.00 USD | 0.00 USD | 100.62 USD | `-53.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 3,890,000.00 USD | 0.00 USD | 203.75 USD | `-49.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 3,890,000.00 USD | 0.00 USD | 791.85 USD | `-49.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 3,890,000.00 USD | 0.00 USD | 573.40 USD | `-48.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 3,890,000.00 USD | 0.00 USD | 244.31 USD | `-47.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 3,890,000.00 USD | 0.00 USD | 29,530.00 USD | `-46.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 3,860,000.00 USD | 0.00 USD | 503.55 USD | `-45.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 3,860,000.00 USD | 0.00 USD | 480.19 USD | `-45.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 3,860,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 3,840,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 3,840,000.00 USD | 0.00 USD | 228.80 USD | `-42.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 3,840,000.00 USD | 0.00 USD | 536.50 USD | `-41.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 3,840,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 3,840,000.00 USD | 0.00 USD | 2,880.00 USD | `-38.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 3,840,000.00 USD | 0.00 USD | 25,490.00 USD | `-36.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 3,810,000.00 USD | 0.00 USD | 2,310,000.00 USD | `-33.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 1,500,000.00 USD | 0.00 USD | 1,260.00 USD | `-31.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 1,500,000.00 USD | 0.00 USD | 690.38 USD | `-29.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 1,500,000.00 USD | 0.00 USD | 1,400.00 USD | `-29.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 1,500,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 1,500,000.00 USD | 0.00 USD | 838.94 USD | `-27.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 1,500,000.00 USD | 0.00 USD | 338.55 USD | `-26.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 1,490,000.00 USD | 0.00 USD | 1,060.00 USD | `-25.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 1,490,000.00 USD | 0.00 USD | 1,090.00 USD | `-25.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 1,490,000.00 USD | 0.00 USD | 112.46 USD | `-24.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 1,490,000.00 USD | 0.00 USD | 2,500.00 USD | `-23.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 1,490,000.00 USD | 0.00 USD | 4,010.00 USD | `-22.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 1,490,000.00 USD | 0.00 USD | 6,300.00 USD | `-21.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 1,480,000.00 USD | 0.00 USD | 4,890.00 USD | `-21.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 1,470,000.00 USD | 0.00 USD | 902.47 USD | `-20.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 1,470,000.00 USD | 0.00 USD | 45,660.00 USD | `-19.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 1,430,000.00 USD | 0.00 USD | 4,760.00 USD | `-18.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 1,420,000.00 USD | 0.00 USD | 1,840.00 USD | `-17.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 1,420,000.00 USD | 0.00 USD | 48,180.00 USD | `-17.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 1,370,000.00 USD | 0.00 USD | 1,780.00 USD | `-16.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 1,370,000.00 USD | 0.00 USD | 27,270.00 USD | `-15.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,340,000.00 USD | 0.00 USD | 3,960.00 USD | `-14.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,340,000.00 USD | 0.00 USD | 48,460.00 USD | `-13.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,290,000.00 USD | 0.00 USD | 3,360.00 USD | `-13.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,290,000.00 USD | 0.00 USD | 16,710.00 USD | `-12.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 1,270,000.00 USD | 0.00 USD | 12,830.00 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 1,260,000.00 USD | 0.00 USD | 9,410.00 USD | `-10.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 1,250,000.00 USD | 0.00 USD | 77,260.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 1,170,000.00 USD | 0.00 USD | 13,250.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 1,160,000.00 USD | 0.00 USD | 118,970.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 1,040,000.00 USD | 0.00 USD | 58,820.00 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 981,440.00 USD | 0.00 USD | 17,890.00 USD | `-6.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 963,550.00 USD | 0.00 USD | 92,150.00 USD | `-5.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 871,400.00 USD | 0.00 USD | 251,790.00 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 619,610.00 USD | 0.00 USD | 201,940.00 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 417,670.00 USD | 0.00 USD | 93,320.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 324,340.00 USD | 0.00 USD | 23,110.00 USD | `-2.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 301,230.00 USD | 0.00 USD | 113,810.00 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 187,420.00 USD | 0.00 USD | 58,150.00 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 129,270.00 USD | 0.00 USD | 129,270.00 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 13,720.00 USD | 13,720.00 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 24,800.00 USD | 11,080.00 USD | 0.00 USD | `+1.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 133,190.00 USD | 108,390.00 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 434,540.00 USD | 301,350.00 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 485,480.00 USD | 50,940.00 USD | 0.00 USD | `+3.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 504,710.00 USD | 19,230.00 USD | 0.00 USD | `+4.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 1,120,000.00 USD | 611,440.00 USD | 0.00 USD | `+5.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,240,000.00 USD | 122,550.00 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,280,000.00 USD | 43,890.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,350,000.00 USD | 70,930.00 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,370,000.00 USD | 14,640.00 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,420,000.00 USD | 47,040.00 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,500,000.00 USD | 82,000.00 USD | 0.00 USD | `+10.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,550,000.00 USD | 55,590.00 USD | 0.00 USD | `+10.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,560,000.00 USD | 5,430.00 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 5,960,000.00 USD | 4,400,000.00 USD | 0.00 USD | `+12.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 5,970,000.00 USD | 3,230.00 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 5,970,000.00 USD | 6,460.00 USD | 0.00 USD | `+14.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 5,970,000.00 USD | 1,450.00 USD | 0.00 USD | `+14.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,220,000.00 USD | 242,580.00 USD | 0.00 USD | `+15.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,220,000.00 USD | 7,510.00 USD | 0.00 USD | `+16.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,240,000.00 USD | 21,280.00 USD | 0.00 USD | `+17.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,350,000.00 USD | 108,020.00 USD | 0.00 USD | `+18.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,370,000.00 USD | 14,870.00 USD | 0.00 USD | `+18.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,390,000.00 USD | 17,790.00 USD | 0.00 USD | `+19.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,460,000.00 USD | 70,600.00 USD | 0.00 USD | `+20.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,470,000.00 USD | 11,760.00 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,490,000.00 USD | 19,430.00 USD | 0.00 USD | `+22.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,530,000.00 USD | 45,620.00 USD | 0.00 USD | `+22.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,540,000.00 USD | 12,200.00 USD | 0.00 USD | `+23.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,550,000.00 USD | 2,380.00 USD | 0.00 USD | `+24.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,550,000.00 USD | 7,160.00 USD | 0.00 USD | `+25.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,560,000.00 USD | 5,570.00 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,570,000.00 USD | 10,570.00 USD | 0.00 USD | `+26.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,710,000.00 USD | 139,120.00 USD | 0.00 USD | `+27.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,710,000.00 USD | 1,840.00 USD | 0.00 USD | `+28.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 6,790,000.00 USD | 80,330.00 USD | 0.00 USD | `+29.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 6,790,000.00 USD | 464.75 USD | 0.00 USD | `+30.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 6,980,000.00 USD | 183,460.00 USD | 0.00 USD | `+30.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 6,980,000.00 USD | 2,670.00 USD | 0.00 USD | `+31.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,000,000.00 USD | 18,210.00 USD | 0.00 USD | `+32.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,000,000.00 USD | 6,080.00 USD | 0.00 USD | `+33.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,030,000.00 USD | 25,340.00 USD | 0.00 USD | `+34.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,100,000.00 USD | 70,850.00 USD | 0.00 USD | `+34.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,120,000.00 USD | 18,000.00 USD | 0.00 USD | `+35.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,370,000.00 USD | 251,050.00 USD | 0.00 USD | `+36.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,380,000.00 USD | 14,250.00 USD | 0.00 USD | `+37.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,380,000.00 USD | 534.75 USD | 0.00 USD | `+38.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,430,000.00 USD | 43,240.00 USD | 0.00 USD | `+38.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,430,000.00 USD | 3,330.00 USD | 0.00 USD | `+39.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,440,000.00 USD | 9,200.00 USD | 0.00 USD | `+40.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,460,000.00 USD | 21,720.00 USD | 0.00 USD | `+41.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,590,000.00 USD | 126,830.00 USD | 0.00 USD | `+42.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,680,000.00 USD | 96,600.00 USD | 0.00 USD | `+42.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 7,690,000.00 USD | 3,980.00 USD | 0.00 USD | `+43.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 7,690,000.00 USD | 254.51 USD | 0.00 USD | `+44.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 7,700,000.00 USD | 11,080.00 USD | 0.00 USD | `+45.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 7,700,000.00 USD | 3,970.00 USD | 0.00 USD | `+46.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 7,710,000.00 USD | 8,170.00 USD | 0.00 USD | `+46.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 7,710,000.00 USD | 843.17 USD | 0.00 USD | `+47.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 7,720,000.00 USD | 8,390.00 USD | 0.00 USD | `+48.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 7,720,000.00 USD | 4,420.00 USD | 0.00 USD | `+50.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 7,730,000.00 USD | 591.89 USD | 0.00 USD | `+50.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 7,770,000.00 USD | 46,370.00 USD | 0.00 USD | `+51.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 7,780,000.00 USD | 9,270.00 USD | 0.00 USD | `+52.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 7,780,000.00 USD | 265.10 USD | 0.00 USD | `+54.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 7,780,000.00 USD | 2,040.00 USD | 0.00 USD | `+55.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 7,780,000.00 USD | 807.42 USD | 0.00 USD | `+56.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 7,800,000.00 USD | 14,120.00 USD | 0.00 USD | `+57.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 7,800,000.00 USD | 4,010.00 USD | 0.00 USD | `+58.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 7,800,000.00 USD | 325.54 USD | 0.00 USD | `+58.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 7,810,000.00 USD | 7,020.00 USD | 0.00 USD | `+59.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 7,940,000.00 USD | 127,100.00 USD | 0.00 USD | `+60.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 7,940,000.00 USD | 3,350.00 USD | 0.00 USD | `+62.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 7,940,000.00 USD | 181.12 USD | 0.00 USD | `+62.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 7,940,000.00 USD | 382.41 USD | 0.00 USD | `+63.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 7,940,000.00 USD | 3,420.00 USD | 0.00 USD | `+65.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 7,940,000.00 USD | 661.93 USD | 0.00 USD | `+66.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,070,000.00 USD | 124,400.00 USD | 0.00 USD | `+67.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,070,000.00 USD | 1,580.00 USD | 0.00 USD | `+68.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,080,000.00 USD | 13,900.00 USD | 0.00 USD | `+70.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,110,000.00 USD | 24,840.00 USD | 0.00 USD | `+71.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,160,000.00 USD | 50,580.00 USD | 0.00 USD | `+72.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,160,000.00 USD | 2,690.00 USD | 0.00 USD | `+73.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,160,000.00 USD | 2,180.00 USD | 0.00 USD | `+75.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,320,000.00 USD | 151,380.00 USD | 0.00 USD | `+77.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,320,000.00 USD | 2,230.00 USD | 0.00 USD | `+82.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,320,000.00 USD | 1,140.00 USD | 0.00 USD | `+82.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,330,000.00 USD | 11,670.00 USD | 0.00 USD | `+83.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,330,000.00 USD | 370.40 USD | 0.00 USD | `+85.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,330,000.00 USD | 733.19 USD | 0.00 USD | `+86.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,330,000.00 USD | 2,410.00 USD | 0.00 USD | `+89.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,340,000.00 USD | 475.00 USD | 0.00 USD | `+90.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,340,000.00 USD | 1,190.00 USD | 0.00 USD | `+90.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,340,000.00 USD | 2,540.00 USD | 0.00 USD | `+91.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,340,000.00 USD | 1,590.00 USD | 0.00 USD | `+92.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,340,000.00 USD | 1,370.00 USD | 0.00 USD | `+93.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,360,000.00 USD | 19,590.00 USD | 0.00 USD | `+94.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,360,000.00 USD | 564.92 USD | 0.00 USD | `+94.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,370,000.00 USD | 3,420.00 USD | 0.00 USD | `+98.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,370,000.00 USD | 124.75 USD | 0.00 USD | `+99.65%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.07` | 101,880,000.00 USD | 0.00 USD | 101,880,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `1.09` | 101,880,000.00 USD | 0.00 USD | 101,880,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `1.09` | 101,840,000.00 USD | 0.00 USD | 101,840,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD |
| `7D` | `1.09` | 101,740,000.00 USD | 0.00 USD | 101,740,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD |
| `7D` | `1.10` | 101,700,000.00 USD | 0.00 USD | 101,700,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD |
| `7D` | `1.10` | 101,700,000.00 USD | 0.00 USD | 101,700,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD |
| `7D` | `1.10` | 101,410,000.00 USD | 0.00 USD | 101,410,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD |
| `7D` | `1.11` | 101,410,000.00 USD | 0.00 USD | 101,410,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD |
| `7D` | `1.11` | 101,400,000.00 USD | 0.00 USD | 101,400,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `7D` | `1.11` | 101,400,000.00 USD | 0.00 USD | 101,400,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD |
| `7D` | `1.12` | 101,350,000.00 USD | 0.00 USD | 101,350,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `7D` | `1.12` | 101,340,000.00 USD | 0.00 USD | 101,340,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 95,720,000.00 USD | 0.00 USD | 95,720,000.00 USD | 8,700.00 USD | 50,170.00 USD | 149,440.00 USD |
| `1D` | `1.12` | 95,510,000.00 USD | 0.00 USD | 95,510,000.00 USD | 17,600.00 USD | 60,880.00 USD | 233,760.00 USD |
| `7D` | `1.12` | 101,260,000.00 USD | 0.00 USD | 101,260,000.00 USD | 17,190.00 USD | 3,530.00 USD | 108,090.00 USD |
| `1D` | `1.12` | 95,200,000.00 USD | 0.00 USD | 95,200,000.00 USD | 6,270.00 USD | 2,870.00 USD | 86,640.00 USD |
| `7D` | `1.12` | 101,130,000.00 USD | 0.00 USD | 101,130,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.12` | 95,110,000.00 USD | 0.00 USD | 95,110,000.00 USD | 97,300.00 USD | 58,310.00 USD | 172,240.00 USD |
| `7D` | `1.13` | 100,920,000.00 USD | 0.00 USD | 100,920,000.00 USD | 0.00 USD | 53,430.00 USD | 94,670.00 USD |
| `1D` | `1.13` | 94,780,000.00 USD | 0.00 USD | 94,780,000.00 USD | 33,730.00 USD | 42,100.00 USD | 236,210.00 USD |
| `7D` | `1.13` | 100,770,000.00 USD | 0.00 USD | 100,770,000.00 USD | 0.00 USD | 0.00 USD | 295,180.00 USD |
| `1D` | `1.13` | 94,470,000.00 USD | 0.00 USD | 94,470,000.00 USD | 74,730.00 USD | 82,870.00 USD | 192,970.00 USD |
| `7D` | `1.13` | 100,470,000.00 USD | 0.00 USD | 100,470,000.00 USD | 5,450.00 USD | 55,710.00 USD | 98,170.00 USD |
| `1D` | `1.13` | 94,110,000.00 USD | 0.00 USD | 94,110,000.00 USD | 9,300.00 USD | 110,430.00 USD | 421,780.00 USD |
| `7D` | `1.13` | 100,310,000.00 USD | 0.00 USD | 100,310,000.00 USD | 69,750.00 USD | 93,260.00 USD | 205,230.00 USD |
| `1D` | `1.13` | 93,570,000.00 USD | 0.00 USD | 93,570,000.00 USD | 88,690.00 USD | 52,980.00 USD | 41,560.00 USD |
| `7D` | `1.13` | 99,950,000.00 USD | 0.00 USD | 99,950,000.00 USD | 74,920.00 USD | 187,750.00 USD | 224,140.00 USD |
| `1D` | `1.14` | 93,390,000.00 USD | 0.00 USD | 93,390,000.00 USD | 4,270.00 USD | 166,580.00 USD | 224,860.00 USD |
| `7D` | `1.14` | 99,460,000.00 USD | 0.00 USD | 99,460,000.00 USD | 79,780.00 USD | 88,050.00 USD | 370,800.00 USD |
| `1D` | `1.14` | 92,990,000.00 USD | 0.00 USD | 92,990,000.00 USD | 81,050.00 USD | 49,560.00 USD | 97,090.00 USD |
| `7D` | `1.14` | 98,920,000.00 USD | 0.00 USD | 98,920,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 92,770,000.00 USD | 0.00 USD | 92,770,000.00 USD | 26,280.00 USD | 52,050.00 USD | 107,470.00 USD |
| `7D` | `1.14` | 98,890,000.00 USD | 0.00 USD | 98,890,000.00 USD | 39,170.00 USD | 54,580.00 USD | 250,970.00 USD |
| `1D` | `1.14` | 92,580,000.00 USD | 0.00 USD | 92,580,000.00 USD | 29,510.00 USD | 10,830.00 USD | 153,170.00 USD |
| `7D` | `1.14` | 98,550,000.00 USD | 0.00 USD | 98,550,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD |
| `1D` | `1.14` | 92,390,000.00 USD | 0.00 USD | 92,390,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD |
| `7D` | `1.14` | 98,410,000.00 USD | 0.00 USD | 98,410,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `1D` | `1.15` | 92,250,000.00 USD | 0.00 USD | 92,250,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD |
| `7D` | `1.15` | 98,400,000.00 USD | 0.00 USD | 98,400,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.15` | 98,340,000.00 USD | 0.00 USD | 98,340,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD |
| `1D` | `1.15` | 92,210,000.00 USD | 0.00 USD | 92,210,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 97,960,000.00 USD | 0.00 USD | 97,960,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.15` | 97,810,000.00 USD | 0.00 USD | 97,810,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 92,190,000.00 USD | 0.00 USD | 92,190,000.00 USD | 4,040.00 USD | 14,590.00 USD | 185,060.00 USD |
| `7D` | `1.15` | 97,640,000.00 USD | 0.00 USD | 97,640,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `1D` | `1.16` | 91,990,000.00 USD | 0.00 USD | 91,990,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD |
| `7D` | `1.16` | 96,760,000.00 USD | 0.00 USD | 96,760,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 91,650,000.00 USD | 0.00 USD | 91,650,000.00 USD | 70,730.00 USD | 16,230.00 USD | 30,130.00 USD |
| `7D` | `1.16` | 96,530,000.00 USD | 0.00 USD | 96,530,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 91,530,000.00 USD | 0.00 USD | 91,530,000.00 USD | 111,450.00 USD | 10,060.00 USD | 409,700.00 USD |
| `7D` | `1.16` | 95,660,000.00 USD | 0.00 USD | 95,660,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 91,000,000.00 USD | 0.00 USD | 91,000,000.00 USD | 172,310.00 USD | 57,350.00 USD | 117,210.00 USD |
| `7D` | `1.16` | 94,580,000.00 USD | 0.00 USD | 94,580,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD |
| `1D` | `1.16` | 90,650,000.00 USD | 0.00 USD | 90,650,000.00 USD | 111,610.00 USD | 269,990.00 USD | 256,680.00 USD |
| `7D` | `1.16` | 93,280,000.00 USD | 0.00 USD | 93,280,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD |
| `1D` | `1.17` | 90,010,000.00 USD | 0.00 USD | 90,010,000.00 USD | 59,160.00 USD | 11,100.00 USD | 473,830.00 USD |
| `7D` | `1.17` | 91,620,000.00 USD | 0.00 USD | 91,620,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD |
| `1D` | `1.17` | 89,470,000.00 USD | 0.00 USD | 89,470,000.00 USD | 121,070.00 USD | 101,750.00 USD | 85,820.00 USD |
| `7D` | `1.17` | 90,270,000.00 USD | 0.00 USD | 90,270,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 89,160,000.00 USD | 0.00 USD | 89,160,000.00 USD | 101,220.00 USD | 95,020.00 USD | 206,520.00 USD |
| `7D` | `1.17` | 89,200,000.00 USD | 0.00 USD | 89,200,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 88,760,000.00 USD | 0.00 USD | 88,760,000.00 USD | 361,890.00 USD | 3,910.00 USD | 415,800.00 USD |
| `7D` | `1.17` | 87,170,000.00 USD | 0.00 USD | 87,170,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD |
| `1D` | `1.17` | 87,980,000.00 USD | 0.00 USD | 87,980,000.00 USD | 104,550.00 USD | 79,710.00 USD | 338,000.00 USD |
| `7D` | `1.17` | 85,970,000.00 USD | 0.00 USD | 85,970,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD |
| `1D` | `1.18` | 87,450,000.00 USD | 0.00 USD | 87,450,000.00 USD | 396,370.00 USD | 140,700.00 USD | 416,380.00 USD |
| `7D` | `1.18` | 84,400,000.00 USD | 0.00 USD | 84,400,000.00 USD | 181,850.00 USD | 71,240.00 USD | 311,840.00 USD |
| `1D` | `1.18` | 86,500,000.00 USD | 0.00 USD | 86,500,000.00 USD | 71,610.00 USD | 44,040.00 USD | 250,850.00 USD |
| `7D` | `1.18` | 83,830,000.00 USD | 0.00 USD | 83,830,000.00 USD | 85,020.00 USD | 27,270.00 USD | 479,420.00 USD |
| `1D` | `1.18` | 86,130,000.00 USD | 0.00 USD | 86,130,000.00 USD | 90,040.00 USD | 42,260.00 USD | 198,520.00 USD |
| `7D` | `1.18` | 83,240,000.00 USD | 0.00 USD | 83,240,000.00 USD | 267,580.00 USD | 112,520.00 USD | 194,450.00 USD |
| `1D` | `1.18` | 85,800,000.00 USD | 0.00 USD | 85,800,000.00 USD | 144,240.00 USD | 19,410.00 USD | 6,800.00 USD |
| `7D` | `1.18` | 82,670,000.00 USD | 0.00 USD | 82,670,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 85,630,000.00 USD | 0.00 USD | 85,630,000.00 USD | 150,010.00 USD | 19,860.00 USD | 660,810.00 USD |
| `7D` | `1.18` | 82,400,000.00 USD | 0.00 USD | 82,400,000.00 USD | 297,510.00 USD | 570,360.00 USD | 235,490.00 USD |
| `1D` | `1.19` | 84,800,000.00 USD | 0.00 USD | 84,800,000.00 USD | 225,800.00 USD | 63,560.00 USD | 143,880.00 USD |
| `7D` | `1.19` | 81,300,000.00 USD | 0.00 USD | 81,300,000.00 USD | 76,370.00 USD | 69,240.00 USD | 706,450.00 USD |
| `1D` | `1.19` | 84,370,000.00 USD | 0.00 USD | 84,370,000.00 USD | 109,160.00 USD | 518,680.00 USD | 653,320.00 USD |
| `7D` | `1.19` | 80,440,000.00 USD | 0.00 USD | 80,440,000.00 USD | 216,820.00 USD | 93,330.00 USD | 477,730.00 USD |
| `1D` | `1.19` | 83,090,000.00 USD | 0.00 USD | 83,090,000.00 USD | 360,560.00 USD | 90,130.00 USD | 1,290,000.00 USD |
| `7D` | `1.19` | 79,660,000.00 USD | 0.00 USD | 79,660,000.00 USD | 179,980.00 USD | 69,020.00 USD | 728,280.00 USD |
| `1D` | `1.19` | 81,350,000.00 USD | 0.00 USD | 81,350,000.00 USD | 61,250.00 USD | 47,660.00 USD | 373,810.00 USD |
| `7D` | `1.19` | 78,680,000.00 USD | 0.00 USD | 78,680,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD |
| `1D` | `1.19` | 80,860,000.00 USD | 0.00 USD | 80,860,000.00 USD | 161,950.00 USD | 502,360.00 USD | 449,720.00 USD |
| `7D` | `1.19` | 77,320,000.00 USD | 0.00 USD | 77,320,000.00 USD | 229,630.00 USD | 59,450.00 USD | 558,970.00 USD |
| `1D` | `1.20` | 79,750,000.00 USD | 0.00 USD | 79,750,000.00 USD | 383,970.00 USD | 157,690.00 USD | 2,250,000.00 USD |
| `7D` | `1.20` | 76,470,000.00 USD | 0.00 USD | 76,470,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 707,370.00 USD |
| `1D` | `1.20` | 76,960,000.00 USD | 0.00 USD | 76,960,000.00 USD | 749,510.00 USD | 88,090.00 USD | 1,010,000.00 USD |
| `7D` | `1.20` | 74,450,000.00 USD | 0.00 USD | 74,450,000.00 USD | 31,150.00 USD | 373,690.00 USD | 2,610,000.00 USD |
| `1D` | `1.20` | 75,110,000.00 USD | 0.00 USD | 75,110,000.00 USD | 217,630.00 USD | 935,370.00 USD | 1,550,000.00 USD |
| `7D` | `1.20` | 71,440,000.00 USD | 0.00 USD | 71,440,000.00 USD | 736,290.00 USD | 466,100.00 USD | 255,270.00 USD |
| `1D` | `1.20` | 72,410,000.00 USD | 0.00 USD | 72,410,000.00 USD | 873,590.00 USD | 591,600.00 USD | 2,130,000.00 USD |
| `7D` | `1.20` | 69,980,000.00 USD | 0.00 USD | 69,980,000.00 USD | 264,000.00 USD | 144,630.00 USD | 618,000.00 USD |
| `1D` | `1.20` | 68,820,000.00 USD | 0.00 USD | 68,820,000.00 USD | 385,750.00 USD | 149,360.00 USD | 940,180.00 USD |
| `7D` | `1.20` | 68,960,000.00 USD | 0.00 USD | 68,960,000.00 USD | 47,500.00 USD | 723,100.00 USD | 407,740.00 USD |
| `1D` | `1.21` | 67,340,000.00 USD | 0.00 USD | 67,340,000.00 USD | 363,980.00 USD | 950,710.00 USD | 376,690.00 USD |
| `7D` | `1.21` | 67,780,000.00 USD | 0.00 USD | 67,780,000.00 USD | 0.00 USD | 77,080.00 USD | 245,420.00 USD |
| `1D` | `1.21` | 65,650,000.00 USD | 0.00 USD | 65,650,000.00 USD | 892,680.00 USD | 240,460.00 USD | 2,050,000.00 USD |
| `7D` | `1.21` | 67,450,000.00 USD | 0.00 USD | 67,450,000.00 USD | 556,190.00 USD | 0.00 USD | 635,770.00 USD |
| `1D` | `1.21` | 62,470,000.00 USD | 0.00 USD | 62,470,000.00 USD | 1,710,000.00 USD | 279,800.00 USD | 953,880.00 USD |
| `7D` | `1.21` | 66,260,000.00 USD | 0.00 USD | 66,260,000.00 USD | 257,960.00 USD | 719,110.00 USD | 3,230,000.00 USD |
| `1D` | `1.21` | 59,530,000.00 USD | 0.00 USD | 59,530,000.00 USD | 227,840.00 USD | 776,280.00 USD | 2,040,000.00 USD |
| `7D` | `1.21` | 62,060,000.00 USD | 0.00 USD | 62,060,000.00 USD | 1,350,000.00 USD | 0.00 USD | 899,930.00 USD |
| `1D` | `1.21` | 56,490,000.00 USD | 0.00 USD | 56,490,000.00 USD | 1,480,000.00 USD | 334,090.00 USD | 1,300,000.00 USD |
| `7D` | `1.21` | 59,800,000.00 USD | 0.00 USD | 59,800,000.00 USD | 108,640.00 USD | 136,460.00 USD | 1,280,000.00 USD |
| `1D` | `1.22` | 53,380,000.00 USD | 0.00 USD | 53,380,000.00 USD | 56,590.00 USD | 268,640.00 USD | 1,010,000.00 USD |
| `7D` | `1.22` | 58,270,000.00 USD | 0.00 USD | 58,270,000.00 USD | 142,210.00 USD | 9,150.00 USD | 253,540.00 USD |
| `1D` | `1.22` | 52,040,000.00 USD | 0.00 USD | 52,040,000.00 USD | 307,460.00 USD | 66,380.00 USD | 538,990.00 USD |
| `7D` | `1.22` | 57,870,000.00 USD | 0.00 USD | 57,870,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD |
| `1D` | `1.22` | 51,130,000.00 USD | 0.00 USD | 51,130,000.00 USD | 212,220.00 USD | 49,690.00 USD | 422,030.00 USD |
| `7D` | `1.22` | 57,130,000.00 USD | 0.00 USD | 57,130,000.00 USD | 156,790.00 USD | 928,300.00 USD | 569,650.00 USD |
| `1D` | `1.22` | 50,440,000.00 USD | 0.00 USD | 50,440,000.00 USD | 70,250.00 USD | 321,780.00 USD | 735,560.00 USD |
| `7D` | `1.22` | 55,480,000.00 USD | 0.00 USD | 55,480,000.00 USD | 0.00 USD | 167,460.00 USD | 340,920.00 USD |
| `1D` | `1.22` | 49,320,000.00 USD | 0.00 USD | 49,320,000.00 USD | 130,100.00 USD | 6,680.00 USD | 443,430.00 USD |
| `7D` | `1.22` | 54,970,000.00 USD | 0.00 USD | 54,970,000.00 USD | 51,610.00 USD | 170,590.00 USD | 33,260.00 USD |
| `1D` | `1.23` | 48,740,000.00 USD | 0.00 USD | 48,740,000.00 USD | 658,900.00 USD | 656,100.00 USD | 3,190,000.00 USD |
| `7D` | `1.23` | 54,720,000.00 USD | 0.00 USD | 54,720,000.00 USD | 112,770.00 USD | 802,580.00 USD | 790,120.00 USD |
| `1D` | `1.23` | 44,230,000.00 USD | 0.00 USD | 44,230,000.00 USD | 274,000.00 USD | 297,600.00 USD | 830,870.00 USD |
| `7D` | `1.23` | 53,010,000.00 USD | 0.00 USD | 53,010,000.00 USD | 59,160.00 USD | 950,550.00 USD | 528,940.00 USD |
| `1D` | `1.23` | 42,830,000.00 USD | 0.00 USD | 42,830,000.00 USD | 679,470.00 USD | 1,210,000.00 USD | 2,810,000.00 USD |
| `7D` | `1.23` | 51,470,000.00 USD | 0.00 USD | 51,470,000.00 USD | 198,530.00 USD | 1,150,000.00 USD | 1,600,000.00 USD |
| `1D` | `1.23` | 38,140,000.00 USD | 0.00 USD | 38,140,000.00 USD | 255,250.00 USD | 1,320,000.00 USD | 3,340,000.00 USD |
| `7D` | `1.23` | 48,520,000.00 USD | 0.00 USD | 48,520,000.00 USD | 1,020,000.00 USD | 1,070,000.00 USD | 1,600,000.00 USD |
| `1D` | `1.23` | 33,220,000.00 USD | 0.00 USD | 33,220,000.00 USD | 1,560,000.00 USD | 805,160.00 USD | 3,670,000.00 USD |
| `7D` | `1.23` | 44,830,000.00 USD | 0.00 USD | 44,830,000.00 USD | 1,660,000.00 USD | 1,990,000.00 USD | 6,100,000.00 USD |
| `1D` | `1.24` | 27,190,000.00 USD | 0.00 USD | 27,190,000.00 USD | 511,510.00 USD | 1,640,000.00 USD | 3,010,000.00 USD |
| `7D` | `1.24` | 35,070,000.00 USD | 0.00 USD | 35,070,000.00 USD | 2,040,000.00 USD | 2,080,000.00 USD | 3,030,000.00 USD |
| `1D` | `1.24` | 22,030,000.00 USD | 0.00 USD | 22,030,000.00 USD | 429,020.00 USD | 567,990.00 USD | 1,030,000.00 USD |
| `7D` | `1.24` | 27,920,000.00 USD | 0.00 USD | 27,920,000.00 USD | 2,870,000.00 USD | 2,120,000.00 USD | 5,050,000.00 USD |
| `1D` | `1.24` | 20,000,000.00 USD | 0.00 USD | 20,000,000.00 USD | 918,230.00 USD | 1,100,000.00 USD | 3,850,000.00 USD |
| `7D` | `1.24` | 17,880,000.00 USD | 0.00 USD | 17,880,000.00 USD | 2,070,000.00 USD | 1,220,000.00 USD | 2,290,000.00 USD |
| `1D` | `1.24` | 14,140,000.00 USD | 0.00 USD | 14,140,000.00 USD | 924,500.00 USD | 624,890.00 USD | 1,990,000.00 USD |
| `7D` | `1.24` | 12,290,000.00 USD | 0.00 USD | 12,290,000.00 USD | 1,130,000.00 USD | 510,590.00 USD | 2,060,000.00 USD |
| `1D` | `1.24` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 889,130.00 USD | 1,030,000.00 USD | 3,560,000.00 USD |
| `7D` | `1.24` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 1,420,000.00 USD | 232,940.00 USD | 0.00 USD |
| `1D` | `1.25` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 1,700,000.00 USD | 728,820.00 USD | 525,240.00 USD |
| `7D` | `1.25` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 3,770,000.00 USD | 688,040.00 USD | 0.00 USD |
| `1D` | `1.25` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 1,200,000.00 USD | 979,690.00 USD | 0.00 USD |
| `7D` | `1.25` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 1,630,000.00 USD | 857,970.00 USD | 0.00 USD |
| `1D` | `1.25` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 709,140.00 USD | 1,140,000.00 USD |
| `1D` | `1.25` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 709,140.00 USD | 1,140,000.00 USD |
| `7D` | `1.25` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 489,680.00 USD | 489,680.00 USD | 0.00 USD | 489,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 1,390.00 USD | 0.00 USD |
| `7D` | `1.25` | 553,340.00 USD | 553,340.00 USD | 0.00 USD | 63,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 7,650.00 USD | 242,040.00 USD |
| `7D` | `1.26` | 712,160.00 USD | 712,160.00 USD | 0.00 USD | 150,010.00 USD | 8,810.00 USD | 0.00 USD |
| `1D` | `1.26` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 822,520.00 USD |
| `7D` | `1.26` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 19,840.00 USD | 1,740,000.00 USD |
| `1D` | `1.26` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 24,960.00 USD | 856,480.00 USD |
| `7D` | `1.26` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 10,110.00 USD | 0.00 USD |
| `1D` | `1.26` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 145,070.00 USD | 8,660.00 USD | 156,250.00 USD |
| `7D` | `1.26` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 144,170.00 USD | 3,390.00 USD | 0.00 USD |
| `1D` | `1.26` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 409,480.00 USD | 391,950.00 USD | 1,150,000.00 USD |
| `7D` | `1.26` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 542,940.00 USD | 1,640,000.00 USD |
| `1D` | `1.26` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 636,140.00 USD | 479,570.00 USD | 1,460,000.00 USD |
| `7D` | `1.27` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 4,260,000.00 USD | 9,150.00 USD | 1,030,000.00 USD |
| `1D` | `1.27` | 12,340,000.00 USD | 12,340,000.00 USD | 0.00 USD | 927,130.00 USD | 221,950.00 USD | 685,300.00 USD |
| `7D` | `1.27` | 16,070,000.00 USD | 16,070,000.00 USD | 0.00 USD | 0.00 USD | 1,870,000.00 USD | 4,090,000.00 USD |
| `1D` | `1.27` | 17,680,000.00 USD | 17,680,000.00 USD | 0.00 USD | 799,780.00 USD | 1,850,000.00 USD | 2,690,000.00 USD |
| `7D` | `1.27` | 21,430,000.00 USD | 21,430,000.00 USD | 0.00 USD | 156,790.00 USD | 2,750,000.00 USD | 2,450,000.00 USD |
| `1D` | `1.27` | 24,000,000.00 USD | 24,000,000.00 USD | 0.00 USD | 740,490.00 USD | 1,660,000.00 USD | 3,920,000.00 USD |
| `7D` | `1.27` | 31,170,000.00 USD | 31,170,000.00 USD | 0.00 USD | 1,680,000.00 USD | 5,310,000.00 USD | 2,750,000.00 USD |
| `1D` | `1.27` | 30,430,000.00 USD | 30,430,000.00 USD | 0.00 USD | 2,360,000.00 USD | 1,290,000.00 USD | 2,780,000.00 USD |
| `7D` | `1.27` | 48,510,000.00 USD | 48,510,000.00 USD | 0.00 USD | 2,710,000.00 USD | 3,400,000.00 USD | 11,230,000.00 USD |
| `1D` | `1.27` | 38,750,000.00 USD | 38,750,000.00 USD | 0.00 USD | 1,200,000.00 USD | 2,620,000.00 USD | 4,510,000.00 USD |
| `7D` | `1.28` | 63,690,000.00 USD | 63,690,000.00 USD | 0.00 USD | 5,150,000.00 USD | 3,080,000.00 USD | 6,950,000.00 USD |
| `1D` | `1.28` | 46,070,000.00 USD | 46,070,000.00 USD | 0.00 USD | 2,090,000.00 USD | 1,420,000.00 USD | 3,810,000.00 USD |
| `7D` | `1.28` | 83,340,000.00 USD | 83,340,000.00 USD | 0.00 USD | 7,780,000.00 USD | 3,760,000.00 USD | 8,120,000.00 USD |
| `1D` | `1.28` | 54,070,000.00 USD | 54,070,000.00 USD | 0.00 USD | 2,330,000.00 USD | 1,960,000.00 USD | 3,710,000.00 USD |
| `7D` | `1.28` | 86,930,000.00 USD | 86,930,000.00 USD | 0.00 USD | 0.00 USD | 1,700,000.00 USD | 1,890,000.00 USD |
| `1D` | `1.28` | 58,300,000.00 USD | 58,300,000.00 USD | 0.00 USD | 446,410.00 USD | 789,690.00 USD | 3,000,000.00 USD |
| `7D` | `1.28` | 88,960,000.00 USD | 88,960,000.00 USD | 0.00 USD | 1,030,000.00 USD | 139,170.00 USD | 861,600.00 USD |
| `1D` | `1.28` | 62,430,000.00 USD | 62,430,000.00 USD | 0.00 USD | 1,340,000.00 USD | 600,450.00 USD | 2,180,000.00 USD |
| `7D` | `1.28` | 93,220,000.00 USD | 93,220,000.00 USD | 0.00 USD | 1,100,000.00 USD | 1,300,000.00 USD | 1,850,000.00 USD |
| `1D` | `1.28` | 66,010,000.00 USD | 66,010,000.00 USD | 0.00 USD | 904,370.00 USD | 745,190.00 USD | 1,930,000.00 USD |
| `7D` | `1.29` | 98,340,000.00 USD | 98,340,000.00 USD | 0.00 USD | 796,960.00 USD | 1,560,000.00 USD | 2,760,000.00 USD |
| `1D` | `1.29` | 69,260,000.00 USD | 69,260,000.00 USD | 0.00 USD | 864,310.00 USD | 1,100,000.00 USD | 1,290,000.00 USD |
| `7D` | `1.29` | 99,060,000.00 USD | 99,060,000.00 USD | 0.00 USD | 685,300.00 USD | 2,730.00 USD | 33,260.00 USD |
| `1D` | `1.29` | 70,380,000.00 USD | 70,380,000.00 USD | 0.00 USD | 454,460.00 USD | 148,440.00 USD | 518,370.00 USD |
| `7D` | `1.29` | 100,670,000.00 USD | 100,670,000.00 USD | 0.00 USD | 70,460.00 USD | 277,240.00 USD | 1,260,000.00 USD |
| `1D` | `1.29` | 71,760,000.00 USD | 71,760,000.00 USD | 0.00 USD | 186,090.00 USD | 270,800.00 USD | 919,950.00 USD |
| `7D` | `1.29` | 103,260,000.00 USD | 103,260,000.00 USD | 0.00 USD | 1,040,000.00 USD | 202,640.00 USD | 1,350,000.00 USD |
| `1D` | `1.29` | 75,570,000.00 USD | 75,570,000.00 USD | 0.00 USD | 574,390.00 USD | 278,090.00 USD | 2,960,000.00 USD |
| `7D` | `1.29` | 106,920,000.00 USD | 106,920,000.00 USD | 0.00 USD | 1,780,000.00 USD | 8,810.00 USD | 1,880,000.00 USD |
| `1D` | `1.29` | 81,950,000.00 USD | 81,950,000.00 USD | 0.00 USD | 1,880,000.00 USD | 719,050.00 USD | 3,780,000.00 USD |
| `7D` | `1.30` | 114,650,000.00 USD | 114,650,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 4,170,000.00 USD |
| `1D` | `1.30` | 84,750,000.00 USD | 84,750,000.00 USD | 0.00 USD | 555,660.00 USD | 707,340.00 USD | 1,540,000.00 USD |
| `7D` | `1.30` | 116,600,000.00 USD | 116,600,000.00 USD | 0.00 USD | 25,800.00 USD | 173,700.00 USD | 1,750,000.00 USD |
| `1D` | `1.30` | 85,650,000.00 USD | 85,650,000.00 USD | 0.00 USD | 440,100.00 USD | 110,110.00 USD | 352,600.00 USD |
| `7D` | `1.30` | 118,970,000.00 USD | 118,970,000.00 USD | 0.00 USD | 208,510.00 USD | 434,510.00 USD | 1,730,000.00 USD |
| `1D` | `1.30` | 88,660,000.00 USD | 88,660,000.00 USD | 0.00 USD | 674,250.00 USD | 491,130.00 USD | 1,850,000.00 USD |
| `7D` | `1.30` | 120,160,000.00 USD | 120,160,000.00 USD | 0.00 USD | 85,960.00 USD | 944,610.00 USD | 153,770.00 USD |
| `1D` | `1.30` | 90,710,000.00 USD | 90,710,000.00 USD | 0.00 USD | 832,380.00 USD | 554,060.00 USD | 655,200.00 USD |
| `7D` | `1.30` | 123,210,000.00 USD | 123,210,000.00 USD | 0.00 USD | 0.00 USD | 2,170,000.00 USD | 887,870.00 USD |
| `1D` | `1.30` | 92,220,000.00 USD | 92,220,000.00 USD | 0.00 USD | 372,370.00 USD | 679,520.00 USD | 458,020.00 USD |
| `7D` | `1.31` | 125,470,000.00 USD | 125,470,000.00 USD | 0.00 USD | 1,770,000.00 USD | 238,140.00 USD | 245,420.00 USD |
| `1D` | `1.31` | 95,520,000.00 USD | 95,520,000.00 USD | 0.00 USD | 803,720.00 USD | 282,740.00 USD | 2,210,000.00 USD |
| `7D` | `1.31` | 130,880,000.00 USD | 130,880,000.00 USD | 0.00 USD | 1,550,000.00 USD | 821,310.00 USD | 3,040,000.00 USD |
| `1D` | `1.31` | 99,220,000.00 USD | 99,220,000.00 USD | 0.00 USD | 1,270,000.00 USD | 477,330.00 USD | 1,960,000.00 USD |
| `7D` | `1.31` | 133,650,000.00 USD | 133,650,000.00 USD | 0.00 USD | 1,340,000.00 USD | 635,040.00 USD | 789,810.00 USD |
| `1D` | `1.31` | 102,000,000.00 USD | 102,000,000.00 USD | 0.00 USD | 966,790.00 USD | 610,460.00 USD | 1,200,000.00 USD |
| `7D` | `1.31` | 138,530,000.00 USD | 138,530,000.00 USD | 0.00 USD | 189,510.00 USD | 858,660.00 USD | 3,830,000.00 USD |
| `1D` | `1.31` | 103,910,000.00 USD | 103,910,000.00 USD | 0.00 USD | 502,120.00 USD | 339,840.00 USD | 1,060,000.00 USD |
| `7D` | `1.31` | 139,820,000.00 USD | 139,820,000.00 USD | 0.00 USD | 638,380.00 USD | 151,320.00 USD | 501,780.00 USD |
| `1D` | `1.31` | 105,980,000.00 USD | 105,980,000.00 USD | 0.00 USD | 418,640.00 USD | 267,510.00 USD | 1,390,000.00 USD |
| `7D` | `1.32` | 144,540,000.00 USD | 144,540,000.00 USD | 0.00 USD | 68,520.00 USD | 1,890,000.00 USD | 2,760,000.00 USD |
| `1D` | `1.32` | 110,580,000.00 USD | 110,580,000.00 USD | 0.00 USD | 1,260,000.00 USD | 633,720.00 USD | 2,700,000.00 USD |
| `7D` | `1.32` | 149,640,000.00 USD | 149,640,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 3,080,000.00 USD |
| `1D` | `1.32` | 114,740,000.00 USD | 114,740,000.00 USD | 0.00 USD | 1,180,000.00 USD | 585,090.00 USD | 2,390,000.00 USD |
| `7D` | `1.32` | 151,660,000.00 USD | 151,660,000.00 USD | 0.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 116,990,000.00 USD | 116,990,000.00 USD | 0.00 USD | 1,320,000.00 USD | 190,640.00 USD | 744,150.00 USD |
| `7D` | `1.32` | 155,010,000.00 USD | 155,010,000.00 USD | 0.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 119,900,000.00 USD | 119,900,000.00 USD | 0.00 USD | 885,300.00 USD | 460,840.00 USD | 1,560,000.00 USD |
| `7D` | `1.32` | 157,790,000.00 USD | 157,790,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD |
| `1D` | `1.32` | 120,900,000.00 USD | 120,900,000.00 USD | 0.00 USD | 599,940.00 USD | 61,650.00 USD | 341,150.00 USD |
| `7D` | `1.33` | 159,600,000.00 USD | 159,600,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 121,970,000.00 USD | 121,970,000.00 USD | 0.00 USD | 412,050.00 USD | 225,260.00 USD | 436,220.00 USD |
| `7D` | `1.33` | 160,700,000.00 USD | 160,700,000.00 USD | 0.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 123,350,000.00 USD | 123,350,000.00 USD | 0.00 USD | 504,110.00 USD | 72,470.00 USD | 798,680.00 USD |
| `7D` | `1.33` | 162,410,000.00 USD | 162,410,000.00 USD | 0.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 125,520,000.00 USD | 125,520,000.00 USD | 0.00 USD | 848,670.00 USD | 101,110.00 USD | 1,220,000.00 USD |
| `7D` | `1.33` | 164,870,000.00 USD | 164,870,000.00 USD | 0.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD |
| `1D` | `1.33` | 127,470,000.00 USD | 127,470,000.00 USD | 0.00 USD | 737,030.00 USD | 194,040.00 USD | 1,020,000.00 USD |
| `7D` | `1.33` | 166,900,000.00 USD | 166,900,000.00 USD | 0.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD |
| `1D` | `1.33` | 128,800,000.00 USD | 128,800,000.00 USD | 0.00 USD | 459,140.00 USD | 356,270.00 USD | 517,170.00 USD |
| `7D` | `1.34` | 168,450,000.00 USD | 168,450,000.00 USD | 0.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 129,540,000.00 USD | 129,540,000.00 USD | 0.00 USD | 384,130.00 USD | 23,210.00 USD | 331,600.00 USD |
| `7D` | `1.34` | 170,880,000.00 USD | 170,880,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 130,030,000.00 USD | 130,030,000.00 USD | 0.00 USD | 147,770.00 USD | 82,510.00 USD | 260,940.00 USD |
| `7D` | `1.34` | 172,740,000.00 USD | 172,740,000.00 USD | 0.00 USD | 804,660.00 USD | 463,950.00 USD | 588,220.00 USD |
| `1D` | `1.34` | 131,180,000.00 USD | 131,180,000.00 USD | 0.00 USD | 540,000.00 USD | 203,030.00 USD | 401,080.00 USD |
| `7D` | `1.34` | 178,210,000.00 USD | 178,210,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,430,000.00 USD | 660,660.00 USD |
| `1D` | `1.34` | 132,360,000.00 USD | 132,360,000.00 USD | 0.00 USD | 602,090.00 USD | 163,750.00 USD | 420,510.00 USD |
| `7D` | `1.34` | 185,330,000.00 USD | 185,330,000.00 USD | 0.00 USD | 2,000,000.00 USD | 1,890,000.00 USD | 3,240,000.00 USD |
| `1D` | `1.34` | 133,370,000.00 USD | 133,370,000.00 USD | 0.00 USD | 303,380.00 USD | 234,450.00 USD | 470,510.00 USD |
| `7D` | `1.35` | 193,590,000.00 USD | 193,590,000.00 USD | 0.00 USD | 3,270,000.00 USD | 1,640,000.00 USD | 3,350,000.00 USD |
| `1D` | `1.35` | 133,610,000.00 USD | 133,610,000.00 USD | 0.00 USD | 112,770.00 USD | 29,080.00 USD | 96,690.00 USD |
| `7D` | `1.35` | 201,340,000.00 USD | 201,340,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,820,000.00 USD | 3,160,000.00 USD |
| `1D` | `1.35` | 134,160,000.00 USD | 134,160,000.00 USD | 0.00 USD | 249,180.00 USD | 23,180.00 USD | 275,620.00 USD |
| `7D` | `1.35` | 209,360,000.00 USD | 209,360,000.00 USD | 0.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD |
| `1D` | `1.35` | 134,570,000.00 USD | 134,570,000.00 USD | 0.00 USD | 146,270.00 USD | 30,410.00 USD | 237,640.00 USD |
| `7D` | `1.35` | 218,470,000.00 USD | 218,470,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 134,720,000.00 USD | 134,720,000.00 USD | 0.00 USD | 66,220.00 USD | 30,780.00 USD | 49,480.00 USD |
| `7D` | `1.35` | 225,220,000.00 USD | 225,220,000.00 USD | 0.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD |
| `1D` | `1.35` | 135,240,000.00 USD | 135,240,000.00 USD | 0.00 USD | 86,720.00 USD | 34,870.00 USD | 395,480.00 USD |
| `7D` | `1.36` | 231,560,000.00 USD | 231,560,000.00 USD | 0.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD |
| `1D` | `1.36` | 136,190,000.00 USD | 136,190,000.00 USD | 0.00 USD | 391,410.00 USD | 32,820.00 USD | 531,190.00 USD |
| `7D` | `1.36` | 234,100,000.00 USD | 234,100,000.00 USD | 0.00 USD | 1,060,000.00 USD | 639,580.00 USD | 837,310.00 USD |
| `1D` | `1.36` | 136,530,000.00 USD | 136,530,000.00 USD | 0.00 USD | 209,880.00 USD | 43,200.00 USD | 82,650.00 USD |
| `7D` | `1.36` | 236,740,000.00 USD | 236,740,000.00 USD | 0.00 USD | 1,300,000.00 USD | 282,890.00 USD | 1,060,000.00 USD |
| `1D` | `1.36` | 137,190,000.00 USD | 137,190,000.00 USD | 0.00 USD | 225,120.00 USD | 162,390.00 USD | 269,830.00 USD |
| `7D` | `1.36` | 240,270,000.00 USD | 240,270,000.00 USD | 0.00 USD | 1,480,000.00 USD | 652,340.00 USD | 1,390,000.00 USD |
| `1D` | `1.36` | 137,490,000.00 USD | 137,490,000.00 USD | 0.00 USD | 130,140.00 USD | 3,300.00 USD | 166,000.00 USD |
| `7D` | `1.36` | 243,000,000.00 USD | 243,000,000.00 USD | 0.00 USD | 1,420,000.00 USD | 616,140.00 USD | 698,940.00 USD |
| `1D` | `1.36` | 137,610,000.00 USD | 137,610,000.00 USD | 0.00 USD | 0.00 USD | 12,740.00 USD | 107,470.00 USD |
| `7D` | `1.37` | 243,820,000.00 USD | 243,820,000.00 USD | 0.00 USD | 206,650.00 USD | 189,790.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 137,860,000.00 USD | 137,860,000.00 USD | 0.00 USD | 61,210.00 USD | 89,800.00 USD | 103,780.00 USD |
| `7D` | `1.37` | 244,870,000.00 USD | 244,870,000.00 USD | 0.00 USD | 486,840.00 USD | 176,380.00 USD | 389,280.00 USD |
| `1D` | `1.37` | 138,060,000.00 USD | 138,060,000.00 USD | 0.00 USD | 93,070.00 USD | 21,460.00 USD | 86,650.00 USD |
| `7D` | `1.37` | 246,300,000.00 USD | 246,300,000.00 USD | 0.00 USD | 367,350.00 USD | 211,750.00 USD | 841,910.00 USD |
| `1D` | `1.37` | 138,250,000.00 USD | 138,250,000.00 USD | 0.00 USD | 6,510.00 USD | 39,430.00 USD | 147,110.00 USD |
| `7D` | `1.37` | 247,530,000.00 USD | 247,530,000.00 USD | 0.00 USD | 393,010.00 USD | 171,680.00 USD | 667,760.00 USD |
| `1D` | `1.37` | 138,350,000.00 USD | 138,350,000.00 USD | 0.00 USD | 6,270.00 USD | 2,870.00 USD | 86,640.00 USD |
| `7D` | `1.37` | 249,200,000.00 USD | 249,200,000.00 USD | 0.00 USD | 563,840.00 USD | 386,690.00 USD | 717,890.00 USD |
| `1D` | `1.38` | 138,680,000.00 USD | 138,680,000.00 USD | 0.00 USD | 97,300.00 USD | 58,310.00 USD | 172,240.00 USD |
| `7D` | `1.38` | 250,230,000.00 USD | 250,230,000.00 USD | 0.00 USD | 242,030.00 USD | 273,360.00 USD | 514,140.00 USD |
| `1D` | `1.38` | 138,990,000.00 USD | 138,990,000.00 USD | 0.00 USD | 33,730.00 USD | 42,100.00 USD | 236,210.00 USD |
| `7D` | `1.38` | 251,790,000.00 USD | 251,790,000.00 USD | 0.00 USD | 692,200.00 USD | 267,730.00 USD | 600,610.00 USD |
| `1D` | `1.38` | 139,340,000.00 USD | 139,340,000.00 USD | 0.00 USD | 74,730.00 USD | 82,870.00 USD | 192,970.00 USD |
| `7D` | `1.38` | 253,490,000.00 USD | 253,490,000.00 USD | 0.00 USD | 436,360.00 USD | 195,830.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 139,410,000.00 USD | 139,410,000.00 USD | 0.00 USD | 2,300.00 USD | 65,520.00 USD | 0.00 USD |
| `7D` | `1.38` | 255,450,000.00 USD | 255,450,000.00 USD | 0.00 USD | 710,620.00 USD | 348,810.00 USD | 900,700.00 USD |
| `1D` | `1.38` | 139,880,000.00 USD | 139,880,000.00 USD | 0.00 USD | 7,000.00 USD | 44,910.00 USD | 421,780.00 USD |
| `7D` | `1.38` | 256,430,000.00 USD | 256,430,000.00 USD | 0.00 USD | 403,730.00 USD | 253,120.00 USD | 325,550.00 USD |
| `1D` | `1.39` | 140,070,000.00 USD | 140,070,000.00 USD | 0.00 USD | 88,690.00 USD | 52,980.00 USD | 41,560.00 USD |
| `7D` | `1.39` | 257,540,000.00 USD | 257,540,000.00 USD | 0.00 USD | 377,810.00 USD | 322,570.00 USD | 413,510.00 USD |
| `1D` | `1.39` | 140,460,000.00 USD | 140,460,000.00 USD | 0.00 USD | 4,270.00 USD | 166,580.00 USD | 224,860.00 USD |
| `7D` | `1.39` | 258,750,000.00 USD | 258,750,000.00 USD | 0.00 USD | 384,080.00 USD | 308,280.00 USD | 518,070.00 USD |
| `1D` | `1.39` | 140,690,000.00 USD | 140,690,000.00 USD | 0.00 USD | 81,050.00 USD | 49,560.00 USD | 97,090.00 USD |
| `7D` | `1.39` | 259,500,000.00 USD | 259,500,000.00 USD | 0.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD |
| `1D` | `1.39` | 140,710,000.00 USD | 140,710,000.00 USD | 0.00 USD | 0.00 USD | 18,330.00 USD | 0.00 USD |
| `7D` | `1.39` | 260,040,000.00 USD | 260,040,000.00 USD | 0.00 USD | 82,350.00 USD | 90,970.00 USD | 358,080.00 USD |
| `7D` | `1.39` | 260,200,000.00 USD | 260,200,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 101,420.00 USD |
| `7D` | `1.40` | 260,420,000.00 USD | 260,420,000.00 USD | 0.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD |
| `7D` | `1.40` | 260,430,000.00 USD | 260,430,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 260,490,000.00 USD | 260,490,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 260,570,000.00 USD | 260,570,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `7D` | `1.40` | 260,860,000.00 USD | 260,860,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 261,020,000.00 USD | 261,020,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.41` | 261,160,000.00 USD | 261,160,000.00 USD | 0.00 USD | 4,390.00 USD | 15,880.00 USD | 120,660.00 USD |
| `7D` | `1.41` | 261,440,000.00 USD | 261,440,000.00 USD | 0.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.81B` | Total OI Tokens: `2,257,847,644.1 XRP`
  * 1h OI Change: `-0.76%` | 4h OI Change: `-2.07%` | 24h OI Change: `-5.91%`
  * Exchange Breakdown: Binance=`422.31M` | Bybit=`324.31M` | OKX=`96.01M` | Hyperliquid=`197.69M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-19.72K` | Last 24h: `21.94K` | Last 3d: `414.05K` | Last 7d: `1.06M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0129%` |
| **USDT Bybit** | `-0.0152%` | **USDT KuCoin** | `-0.0088%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0004%` | **USDT Bitget** | `-0.0042%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-0.0044%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `49.95%` | `50.05%` | `1.00` | 203,360,000.00 USD |
| `15M` | `Binance` | `49.73%` | `50.27%` | `0.99` | 63,970,000.00 USD |
| `15M` | `OKX` | `47.97%` | `52.03%` | `0.92` | 32,660,000.00 USD |
| `15M` | `Bybit` | `45.76%` | `54.24%` | `0.84` | 12,110,000.00 USD |
| `15M` | `KuCoin` | `54.15%` | `45.85%` | `1.18` | 593,900.00 USD |
| `15M` | `Gate` | `52.92%` | `47.08%` | `1.12` | 32,920,000.00 USD |
| `15M` | `Bitget` | `53.01%` | `46.99%` | `1.13` | 4,260,000.00 USD |
| `15M` | `BingX` | `36.96%` | `63.04%` | `0.59` | 3,410,000.00 USD |
| `15M` | `MEXC` | `47.72%` | `52.28%` | `0.91` | 8,340,000.00 USD |
| `15M` | `Bitunix` | `41.47%` | `58.53%` | `0.71` | 7,370,000.00 USD |
| `15M` | `Hyperliquid` | `54.73%` | `45.27%` | `1.21` | 26,690,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.38%` | `52.62%` | `0.90` | 564,760.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `97.54%` | `2.46%` | `39.65` | 659,160.00 USD |
| `15M` | `HTX` | `44.89%` | `55.11%` | `0.81` | 2,400,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `51.49%` | `48.51%` | `1.06` | 2,180,000.00 USD |
| `15M` | `Bitfinex` | `16.16%` | `83.84%` | `0.19` | 78,360.00 USD |
| `15M` | `Kraken` | `41.49%` | `58.51%` | `0.71` | 1,630,000.00 USD |
| `15M` | `Aster` | `64.75%` | `35.25%` | `1.84` | 1,160,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `46.62%` | `53.38%` | `0.87` | 2,360,000.00 USD |
| `15M` | `Whale Positions` | `49.73%` | `50.27%` | `0.99` | 63,970,000.00 USD |
| `15M` | `Global Accounts` | `49.95%` | `50.05%` | `1.00` | 203,360,000.00 USD |
| `1H` | `XRP` | `47.10%` | `52.90%` | `0.89` | 2,270,000,000.00 USD |
| `1H` | `Binance` | `41.69%` | `58.31%` | `0.71` | 700,160,000.00 USD |
| `1H` | `OKX` | `51.34%` | `48.66%` | `1.06` | 304,950,000.00 USD |
| `1H` | `Bybit` | `44.66%` | `55.34%` | `0.81` | 210,450,000.00 USD |
| `1H` | `KuCoin` | `66.25%` | `33.75%` | `1.96` | 10,600,000.00 USD |
| `1H` | `Gate` | `50.3%` | `49.7%` | `1.01` | 233,230,000.00 USD |
| `1H` | `Bitget` | `42.87%` | `57.13%` | `0.75` | 117,500,000.00 USD |
| `1H` | `BingX` | `56.64%` | `43.36%` | `1.31` | 49,880,000.00 USD |
| `1H` | `MEXC` | `47.89%` | `52.11%` | `0.92` | 132,840,000.00 USD |
| `1H` | `Bitunix` | `46.12%` | `53.88%` | `0.86` | 112,460,000.00 USD |
| `1H` | `Hyperliquid` | `59.26%` | `40.74%` | `1.45` | 160,280,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `58.86%` | `41.14%` | `1.43` | 24,100,000.00 USD |
| `1H` | `Crypto.com` | `50.93%` | `49.07%` | `1.04` | 7,740,000.00 USD |
| `1H` | `WhiteBIT` | `24.05%` | `75.95%` | `0.32` | 11,890,000.00 USD |
| `1H` | `HTX` | `40.38%` | `59.62%` | `0.68` | 9,980,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `47.55%` | `52.45%` | `0.91` | 105,510,000.00 USD |
| `1H` | `Bitfinex` | `67.5%` | `32.5%` | `2.08` | 1,570,000.00 USD |
| `1H` | `Kraken` | `55.61%` | `44.39%` | `1.25` | 21,110,000.00 USD |
| `1H` | `Aster` | `35.66%` | `64.34%` | `0.55` | 26,670,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `56.58%` | `43.42%` | `1.30` | 22,480,000.00 USD |
| `1H` | `Whale Positions` | `41.69%` | `58.31%` | `0.71` | 700,160,000.00 USD |
| `1H` | `Global Accounts` | `47.10%` | `52.90%` | `0.89` | 2,270,000,000.00 USD |
| `4H` | `XRP` | `45.02%` | `54.98%` | `0.82` | 10,110,000,000.00 USD |
| `4H` | `Binance` | `43.59%` | `56.41%` | `0.77` | 2,940,000,000.00 USD |
| `4H` | `OKX` | `47.19%` | `52.81%` | `0.89` | 1,430,000,000.00 USD |
| `4H` | `Bybit` | `42.42%` | `57.58%` | `0.74` | 883,560,000.00 USD |
| `4H` | `KuCoin` | `52.9%` | `47.1%` | `1.12` | 28,440,000.00 USD |
| `4H` | `Gate` | `50.08%` | `49.92%` | `1.00` | 978,540,000.00 USD |
| `4H` | `Bitget` | `42.72%` | `57.28%` | `0.75` | 466,100,000.00 USD |
| `4H` | `BingX` | `44.09%` | `55.91%` | `0.79` | 201,110,000.00 USD |
| `4H` | `MEXC` | `44.14%` | `55.86%` | `0.79` | 471,500,000.00 USD |
| `4H` | `Bitunix` | `45.53%` | `54.47%` | `0.84` | 408,110,000.00 USD |
| `4H` | `Hyperliquid` | `38.07%` | `61.93%` | `0.61` | 584,210,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.95%` | `49.05%` | `1.04` | 705,350,000.00 USD |
| `4H` | `Crypto.com` | `45.84%` | `54.16%` | `0.85` | 32,330,000.00 USD |
| `4H` | `WhiteBIT` | `20.6%` | `79.4%` | `0.26` | 196,590,000.00 USD |
| `4H` | `HTX` | `43.91%` | `56.09%` | `0.78` | 36,030,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.81%` | `48.19%` | `1.08` | 485,230,000.00 USD |
| `4H` | `Bitfinex` | `44.37%` | `55.63%` | `0.80` | 4,820,000.00 USD |
| `4H` | `Kraken` | `46.81%` | `53.19%` | `0.88` | 45,400,000.00 USD |
| `4H` | `Aster` | `45.84%` | `54.16%` | `0.85` | 93,570,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.96%` | `47.04%` | `1.13` | 111,000,000.00 USD |
| `4H` | `Whale Positions` | `43.59%` | `56.41%` | `0.77` | 2,940,000,000.00 USD |
| `4H` | `Global Accounts` | `45.02%` | `54.98%` | `0.82` | 10,110,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 8,443,326.41 USD | 4,197,283.82 USD | 4,246,042.59 USD | -48,758.76 USD | `-0.58%` | `16B / 5S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 7,390,743.66 USD | 4,309,267.00 USD | 3,081,476.65 USD | 1,227,790.35 USD | `+16.61%` | `9B / 4S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 5,021,258.97 USD | 2,177,548.60 USD | 2,843,710.37 USD | -666,161.77 USD | `-13.27%` | `1B / 5S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 4,481,732.50 USD | 2,318,507.74 USD | 2,163,224.76 USD | 155,282.98 USD | `+3.46%` | `9B / 5S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 12,807,415.42 USD | 6,692,980.18 USD | 6,114,435.24 USD | 578,544.93 USD | `+4.52%` | `12B / 4S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 7,616,675.33 USD | 3,341,703.26 USD | 4,274,972.07 USD | -933,268.81 USD | `-12.25%` | `11B / 16S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 4,530,946.41 USD | 2,213,429.43 USD | 2,317,516.98 USD | -104,087.54 USD | `-2.30%` | `0B / 9S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 5,245,480.96 USD | 2,448,103.42 USD | 2,797,377.55 USD | -349,274.13 USD | `-6.66%` | `3B / 8S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 6,871,051.82 USD | 2,753,850.97 USD | 4,117,200.85 USD | -1,363,349.88 USD | `-19.84%` | `6B / 18S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 1,403,713.72 USD | 581,576.78 USD | 822,136.94 USD | -240,560.16 USD | `-17.14%` | `1B / 5S` |

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
| `5m` | 19,710.00 USD | -3,020,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,080,000.00 USD | -7,920,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,110,000.00 USD | -10,270,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,390,000.00 USD | -17,030,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -154,260.00 USD | -16,150,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,770,000.00 USD | -21,050,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 8,360,000.00 USD | -7,430,000.00 USD | **`ACCUMULATION`** |
| `8h` | 22,040,000.00 USD | 322,330.00 USD | **`ACCUMULATION`** |
| `12h` | -11,620,000.00 USD | -21,780,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -48,670,000.00 USD | -145,240,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -114,720,000.00 USD | -232,980,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -594,650,000.00 USD | -1,310,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+19.71K` | 15m=`-1.08M` | 1h=`-2.39M` | 24h=`-48.67M`
* Futures Capital Netflows: 5m=`-3.02M` | 15m=`-7.92M` | 1h=`-17.03M` | 24h=`-145.24M`
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
  * `2026-10-30 15:33:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:17 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:17 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.0268` (Risk Distance: `1.21` pts)
  * +2.5R Take Profit: `4.25`
  * Mathematical Lot Sizing: **`8.29 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `2.47` (Risk Distance: `1.21` pts)
  * +2.5R Take Profit: `-1.75`
  * Mathematical Lot Sizing: **`8.29 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.25`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
