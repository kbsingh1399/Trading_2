# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 14:38:46 IST` (`2026-10-30 09:08:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.25` | **Live Ask Quote**: `1.26` | **Mid Price**: `1.26`
- **Spread Points**: `3.00` | **Spread BPS**: `23.89 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.24` | VWAP Z-Score: `+0.80` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0081` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `54.02` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.29` | Lower -3.00σ Band: `1.18`
  * Upper +2.51σ Band: `1.29` | Lower -2.51σ Band: `1.19`
  * Upper +2.01σ Band: `1.28` | Lower -2.01σ Band: `1.20`
  * Upper +2.00σ Band: `1.28` | Lower -2.00σ Band: `1.20`
  * Upper +1.28σ Band: `1.26` | Lower -1.28σ Band: `1.21`
  * Upper +1.00σ Band: `1.26` | Lower -1.00σ Band: `1.22`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.25` | EMA-20=`1.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.25` (Slope: `+0.0000`) | EMA-100=`1.26`
  * Institutional Anchors: EMA-144=`1.27` | EMA-200=`1.28` (Slope: `-0.2508`) | EMA-233=`1.28`
- **Range Boundaries**: 24H High=`1.31` | 24H Low=`1.19` | Weekly High=`1.34` | Weekly Low=`1.19`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-0.45%`)
  * Point of Control (POC) = `1.25` (Distance: `+0.48%`)
  * Value Area Low (VAL) = `1.23` (Distance: `+1.97%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.33` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.19`
  * London Session (08:00-16:00 UTC): High=`1.27` | Low=`1.24`
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
| `5m` | `1.25` | `1.26` | `1.25` | `1.26` | `1,323,124` | 1,657,691.48 USD | 363,177.86 USD | `+21.91%` | -40,587,926.37 USD | `+1.11` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.26` | `1.26` | `1.25` | `1.26` | `1,069,896` | 1,341,936.96 USD | -99,247.93 USD | `-7.40%` | -40,687,174.30 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `1,157,184` | 1,454,678.08 USD | 25,268.62 USD | `+1.74%` | -40,661,905.68 USD | `+0.33` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.25` | `4,005,556` | 5,021,258.97 USD | -666,161.77 USD | `-13.27%` | -41,010,716.32 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.26` | `3,576,596` | 4,481,732.50 USD | 155,282.98 USD | `+3.46%` | -40,855,433.34 USD | `-0.09` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `1.26` | `1.26` | `1.26` | `1.26` | `1,157,229` | 1,454,735.04 USD | 25,325.58 USD | `+1.74%` | -40,830,107.76 USD | `-0.16` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.27` | `1.27` | `1.25` | `1.25` | `31,555,138` | 39,629,532.33 USD | -5,613,699.06 USD | `-14.17%` | -41,162,507.62 USD | `-0.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.25` | `1.26` | `1.25` | `1.26` | `20,218,037` | 25,337,061.54 USD | 668,152.80 USD | `+2.64%` | -40,494,354.82 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.26` | `1.26` | `1.26` | `1.26` | `1,157,229` | 1,454,735.04 USD | 25,325.58 USD | `+1.74%` | -40,469,029.24 USD | `+0.22` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -44,069,722.41 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.27` | `1.24` | `1.25` | `116,541,770` | 146,517,167.36 USD | 4,788,193.48 USD | `+3.27%` | -39,281,528.93 USD | `+1.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.25` | `1.26` | `1.25` | `1.26` | `21,408,592` | 26,833,704.05 USD | 735,203.02 USD | `+2.74%` | -38,546,325.91 USD | `+0.62` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -13,549,801.29 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -41,639,935.50 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -44,069,722.41 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.27` | `1.24` | `1.25` | `116,541,770` | 146,517,167.36 USD | 4,788,193.48 USD | `+3.27%` | -39,281,528.93 USD | `+1.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.25` | `1.26` | `1.25` | `1.26` | `21,408,592` | 26,833,704.05 USD | 735,203.02 USD | `+2.74%` | -38,546,325.91 USD | `+0.62` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `ASK` | `1.26` | `78919.0000` | 99,406.37 USD | 2,855,718.41 USD | `3 orders` | `+0.16%` | `-` |
| `ASK` | `1.26` | `65487.0000` | 82,480.88 USD | 2,756,312.03 USD | `4 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `10796.0000` | 13,596.48 USD | 2,673,831.16 USD | `6 orders` | `+0.14%` | `-` |
| `ASK` | `1.26` | `196890.0000` | 247,943.58 USD | 2,660,234.67 USD | `6 orders` | `+0.13%` | `-` |
| `ASK` | `1.26` | `365616.0000` | 460,383.67 USD | 2,412,291.10 USD | `5 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `52982.0000` | 66,709.64 USD | 1,951,907.43 USD | `9 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `233714.0000` | 294,245.93 USD | 1,885,197.79 USD | `5 orders` | `+0.11%` | `-` |
| `ASK` | `1.26` | `276532.0000` | 348,126.13 USD | 1,590,951.87 USD | `6 orders` | `+0.10%` | `-` |
| `ASK` | `1.26` | `140669.0000` | 177,074.14 USD | 1,242,825.73 USD | `9 orders` | `+0.09%` | `-` |
| `ASK` | `1.26` | `110969.0000` | 139,676.68 USD | 1,065,751.60 USD | `9 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `56260.0000` | 70,808.84 USD | 926,074.92 USD | `6 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `85892.0000` | 108,095.08 USD | 855,266.08 USD | `8 orders` | `+0.07%` | `-` |
| `ASK` | `1.26` | `64971.0000` | 81,759.51 USD | 747,171.00 USD | `13 orders` | `+0.06%` | `-` |
| `ASK` | `1.26` | `283979.0000` | 357,330.78 USD | 665,411.49 USD | `11 orders` | `+0.05%` | `-` |
| `ASK` | `1.26` | `94307.0000` | 118,657.07 USD | 308,080.72 USD | `14 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `66772.0000` | 84,005.85 USD | 189,423.65 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `19545.0000` | 24,587.61 USD | 105,417.79 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `1.26` | `21870.0000` | 27,510.27 USD | 80,830.18 USD | `8 orders` | `+0.02%` | `-` |
| `ASK` | `1.26` | `34931.0000` | 43,936.21 USD | 53,319.91 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `1.26` | `7461.0000` | 9,383.70 USD | 9,383.70 USD | `3 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.26` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.26` | `0.00%` | `-` |
| `BID` | `1.26` | `33307.0000` | 41,886.88 USD | 41,886.88 USD | `10 orders` | `-0.00%` | `-` |
| `BID` | `1.26` | `33225.0000` | 41,780.44 USD | 83,667.32 USD | `23 orders` | `-0.01%` | `-` |
| `BID` | `1.26` | `34157.0000` | 42,949.01 USD | 126,616.33 USD | `22 orders` | `-0.02%` | `-` |
| `BID` | `1.26` | `24984.0000` | 31,412.38 USD | 158,028.72 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `1.26` | `37999.0000` | 47,772.34 USD | 205,801.06 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `52774.0000` | 66,342.20 USD | 272,143.25 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `46559.0000` | 58,524.66 USD | 330,667.92 USD | `9 orders` | `-0.05%` | `-` |
| `BID` | `1.26` | `69363.0000` | 87,182.35 USD | 417,850.27 USD | `7 orders` | `-0.06%` | `-` |
| `BID` | `1.26` | `65642.0000` | 82,498.87 USD | 500,349.14 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `1.26` | `57923.0000` | 72,791.83 USD | 573,140.97 USD | `8 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `271929.0000` | 341,705.98 USD | 914,846.95 USD | `9 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `72150.0000` | 90,656.47 USD | 1,005,503.43 USD | `7 orders` | `-0.09%` | `-` |
| `BID` | `1.26` | `106115.0000` | 133,322.89 USD | 1,138,826.31 USD | `7 orders` | `-0.10%` | `-` |
| `BID` | `1.26` | `70456.0000` | 88,513.87 USD | 1,227,340.19 USD | `8 orders` | `-0.11%` | `-` |
| `BID` | `1.26` | `7764.0000` | 9,753.14 USD | 1,237,093.32 USD | `3 orders` | `-0.12%` | `-` |
| `BID` | `1.26` | `13107.0000` | 16,463.70 USD | 1,253,557.03 USD | `5 orders` | `-0.12%` | `-` |
| `BID` | `1.26` | `767127.0000` | 963,511.51 USD | 2,217,068.54 USD | `5 orders` | `-0.13%` | `-` |
| `BID` | `1.26` | `106434.0000` | 133,670.46 USD | 2,350,739.00 USD | `7 orders` | `-0.14%` | `-` |
| `BID` | `1.26` | `55075.0000` | 69,163.18 USD | 2,419,902.18 USD | `7 orders` | `-0.15%` | `-` |
| `BID` | `1.26` | `5641.0000` | 7,083.40 USD | 2,426,985.59 USD | `3 orders` | `-0.16%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `26` | `0x31b1...1434` | `LONG` | 44,129,092.37 USD | `35,031,430.00` | `1.13` | `1.26` | `0.9612` | 4,550,209.10 USD | `+10.31%` | `10X Cross` |
| `90` | `0x5b5d...c060` | `SHORT` | 20,025,991.31 USD | `15,897,429.00` | `1.44` | `1.26` | `11.18` | 2,794,156.98 USD | `+13.95%` | `5X Cross` |
| `155` | `0xb83d...6e36` | `SHORT` | 13,198,530.68 USD | `10,477,519.00` | `1.50` | `1.26` | `13.61` | 2,507,220.76 USD | `+19.00%` | `5X Cross` |
| `346` | `0x58f0...0d20` | `LONG` | 6,673,737.35 USD | `5,307,147.00` | `1.24` | `1.26` | `1.22` | 70,893.85 USD | `+1.06%` | `20X Cross` |
| `383` | `0xecb6...2b00` | `SHORT` | 6,065,631.86 USD | `4,815,140.00` | `1.27` | `1.26` | `8.08` | 46,387.86 USD | `+0.76%` | `10X Cross` |
| `425` | `0xca49...53c8` | `SHORT` | 5,217,434.16 USD | `4,138,886.00` | `1.44` | `1.26` | `4.90` | 735,888.57 USD | `+14.10%` | `20X Cross` |
| `436` | `0xdd53...2b13` | `SHORT` | 5,041,430.88 USD | `3,998,914.00` | `1.40` | `1.26` | `16.75` | 555,445.23 USD | `+11.02%` | `3X Cross` |
| `504` | `0x610b...b613` | `LONG` | 4,454,740.12 USD | `3,543,946.00` | `1.44` | `1.26` | `0.8403` | -645,252.49 USD | `-14.48%` | `5X Cross` |
| `595` | `0x9946...0852` | `SHORT` | 3,871,264.97 USD | `3,070,483.00` | `1.40` | `1.26` | `1.76` | 437,237.25 USD | `+11.29%` | `20X Cross` |
| `649` | `0xc30c...a4c9` | `SHORT` | 3,509,771.81 USD | `2,791,515.00` | `1.41` | `1.26` | `1.59` | 426,740.92 USD | `+12.16%` | `8X Cross` |
| `654` | `0xc179...e0c8` | `SHORT` | 3,488,134.49 USD | `2,769,020.00` | `1.27` | `1.26` | `3.43` | 20,580.17 USD | `+0.59%` | `10X Cross` |
| `657` | `0xfc27...9d9d` | `SHORT` | 3,449,899.30 USD | `2,736,736.00` | `1.29` | `1.26` | `8.03` | 89,619.72 USD | `+2.60%` | `20X Cross` |
| `699` | `0xf48f...10fe` | `LONG` | 3,233,376.74 USD | `2,565,779.00` | `1.53` | `1.26` | `1.02` | -691,263.99 USD | `-21.38%` | `4X Cross` |
| `741` | `0x023a...2355` | `SHORT` | 3,103,200.52 USD | `2,463,360.00` | `1.32` | `1.26` | `3.35` | 147,727.73 USD | `+4.76%` | `20X Cross` |
| `745` | `0x45d2...4029` | `SHORT` | 3,092,224.82 USD | `2,453,000.00` | `1.48` | `1.26` | `18.68` | 546,055.61 USD | `+17.66%` | `20X Cross` |
| `1073` | `0xeadc...9d55` | `LONG` | 2,040,468.36 USD | `1,619,805.00` | `1.21` | `1.26` | `0.000000` | 81,625.34 USD | `+4.00%` | `20X Cross` |
| `1152` | `0x94b2...599e` | `SHORT` | 1,937,117.08 USD | `1,540,696.00` | `1.36` | `1.26` | `1.87` | 163,349.37 USD | `+8.43%` | `20X Cross` |
| `1171` | `0x3fc5...c0c1` | `SHORT` | 1,904,453.01 USD | `1,511,779.00` | `1.52` | `1.26` | `2.42` | 387,161.59 USD | `+20.33%` | `20X Cross` |
| `1194` | `0x31ef...f715` | `LONG` | 1,858,158.28 USD | `1,475,080.00` | `1.49` | `1.26` | `1.04` | -341,107.13 USD | `-18.36%` | `3X Isolated` |
| `1260` | `0x7737...bf66` | `SHORT` | 1,777,574.84 USD | `1,413,466.00` | `1.41` | `1.26` | `14.10` | 221,293.81 USD | `+12.45%` | `10X Cross` |
| `1316` | `0x95da...2328` | `LONG` | 1,665,110.78 USD | `1,324,876.00` | `1.35` | `1.26` | `0.0953` | -128,530.32 USD | `-7.72%` | `5X Cross` |
| `1330` | `0xee2b...d67e` | `LONG` | 1,646,962.87 USD | `1,306,284.00` | `1.55` | `1.26` | `0.4252` | -383,692.03 USD | `-23.30%` | `4X Cross` |
| `1375` | `0x215d...f80a` | `LONG` | 1,574,485.11 USD | `1,251,777.00` | `1.32` | `1.26` | `1.13` | -79,969.12 USD | `-5.08%` | `14X Cross` |
| `1386` | `0x5fa3...35b7` | `SHORT` | 1,562,848.06 USD | `1,240,651.00` | `1.30` | `1.26` | `2.65` | 53,644.07 USD | `+3.43%` | `20X Cross` |
| `1436` | `0x123d...3bff` | `LONG` | 1,526,668.68 USD | `1,211,889.00` | `1.35` | `1.26` | `0.000000` | -105,766.80 USD | `-6.93%` | `10X Cross` |
| `1459` | `0xbcd4...0dd2` | `SHORT` | 1,506,810.10 USD | `1,196,125.00` | `1.31` | `1.26` | `2.06` | 60,857.15 USD | `+4.04%` | `20X Cross` |
| `1537` | `0x7fda...17d1` | `LONG` | 1,408,370.00 USD | `1,117,982.00` | `1.22` | `1.26` | `0.000000` | 46,233.59 USD | `+3.28%` | `20X Cross` |
| `1559` | `0xdf95...7d72` | `SHORT` | 1,385,574.26 USD | `1,099,924.00` | `1.37` | `1.26` | `36.74` | 124,296.33 USD | `+8.97%` | `20X Cross` |
| `1635` | `0xef96...9383` | `SHORT` | 1,306,012.87 USD | `1,036,765.00` | `1.34` | `1.26` | `4.66` | 81,506.48 USD | `+6.24%` | `20X Cross` |
| `1656` | `0xb1ce...681b` | `LONG` | 1,288,137.87 USD | `1,021,764.00` | `1.49` | `1.26` | `1.16` | -235,918.62 USD | `-18.31%` | `4X Isolated` |
| `1730` | `0x9a31...6525` | `LONG` | 1,223,370.25 USD | `971,160.00` | `1.25` | `1.26` | `0.0430` | 6,675.74 USD | `+0.55%` | `5X Cross` |
| `1760` | `0x3c36...461a` | `LONG` | 1,185,122.30 USD | `940,051.00` | `1.30` | `1.26` | `1.05` | -33,958.32 USD | `-2.87%` | `10X Cross` |
| `1884` | `0x2577...4897` | `SHORT` | 1,089,082.45 USD | `864,557.00` | `1.24` | `1.26` | `5.10` | -14,174.78 USD | `-1.30%` | `20X Cross` |
| `2004` | `0xbfc7...80b4` | `SHORT` | 1,006,240.00 USD | `800,000.00` | `1.48` | `1.26` | `3.18` | 177,214.65 USD | `+17.61%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.32` | 4,209.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.21K USD at 1.3152 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 3,999.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3152 USD [API] | `2026-10-22 15:12:49` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 3,140.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.14K USD at 1.3009 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 3,998.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3009 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 166.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.17K USD at 1.3009 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 9,520.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.52K USD at 1.3010 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 9,520.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.52K USD at 1.3010 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 50.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3010 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 3,999.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3010 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,127.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.13K USD at 1.3010 USD [API] | `2026-10-15 02:23:11` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 640.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.64K USD at 1.3656 USD [API] | `2026-10-12 16:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 501.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.3656 USD [API] | `2026-10-12 16:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,998.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3657 USD [API] | `2026-10-12 16:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,999.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3658 USD [API] | `2026-10-12 16:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 19,998.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 20.00K USD at 1.3658 USD [API] | `2026-10-12 16:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 868.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.87K USD at 1.3658 USD [API] | `2026-10-12 16:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 9,316.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.32K USD at 1.4543 USD [API] | `2026-10-07 02:01:14` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 261.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.26K USD at 1.4543 USD [API] | `2026-10-07 02:01:14` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 2,056.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.06K USD at 1.4544 USD [API] | `2026-10-07 02:01:14` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 8,237.57 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.24K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 20.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 6,140.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.14K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 399.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,725.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.73K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,441.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.44K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,998.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3727 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 2,103.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.10K USD at 1.3728 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 411.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.41K USD at 1.3728 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 4,176.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.18K USD at 1.3728 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 20.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.3728 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,998.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3728 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 49.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3728 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,999.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3729 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 399.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3730 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 189.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.19K USD at 1.3730 USD [API] | `2026-09-20 02:54:10` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 199.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.20K USD at 1.2532 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 2,911.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.91K USD at 1.2532 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 5,004.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.2532 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 58.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.06K USD at 1.2532 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 2,990.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.99K USD at 1.2533 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 30.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.03K USD at 1.2533 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.25` | 2,981.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.98K USD at 1.2533 USD [API] | `2026-09-16 17:43:22` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10,394.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.39K USD at 1.2925 USD [API] | `2026-10-29 09:16:12` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,645.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.65K USD at 1.2925 USD [API] | `2026-10-29 09:16:12` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10,074.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.07K USD at 1.2927 USD [API] | `2026-10-29 09:17:46` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,064.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.06K USD at 1.2894 USD [API] | `2026-10-29 09:35:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,778.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.78K USD at 1.2894 USD [API] | `2026-10-29 09:35:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 8,858.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.86K USD at 1.2892 USD [API] | `2026-10-29 09:36:34` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2906 USD [API] | `2026-10-29 09:41:44` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,461.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.46K USD at 1.3409 USD [API] | `2026-10-14 14:11:09` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,195.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.20K USD at 1.3409 USD [API] | `2026-10-14 14:11:09` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 929.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.93K USD at 1.4622 USD [API] | `2026-10-07 02:00:59` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 11,087.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.09K USD at 1.2901 USD [API] | `2026-10-29 09:43:08` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 13,935.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 13.94K USD at 1.2901 USD [API] | `2026-10-29 09:47:30` |
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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+3.48%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.22%`)
  * 48H Horizon: Short MP=`1.32` (Vol: 2,300,000.00 USD, Dist: `+5.70%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.23%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+7.87%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.23%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 2,900,000.00 USD, Dist: `+7.76%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.23%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 827.48 USD | 64,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 1,400.00 USD | 64,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 1,090.00 USD | 64,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 3,800.00 USD | 64,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 120.36 USD | 64,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 122.00 USD | 64,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 16,150.00 USD | 64,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 19,750.00 USD | 64,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 59,960.00 USD | 64,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 439.88 USD | 64,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 8,430.00 USD | 64,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 4,990.00 USD | 64,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 6,590.00 USD | 64,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 269.50 USD | 64,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 174.59 USD | 64,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 2,640.00 USD | 64,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 688,700.00 USD | 64,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 23,930.00 USD | 63,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 16,860.00 USD | 63,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 1,540.00 USD | 63,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 5,160.00 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 283.72 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 1,480.00 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 1,160.00 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 12,250.00 USD | 63,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 14,270.00 USD | 63,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 966.75 USD | 63,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 159,160.00 USD | 63,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 720.39 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 7,030.00 USD | 63,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 7,770.00 USD | 63,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 3,310.00 USD | 63,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 4,540.00 USD | 63,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 27,410.00 USD | 63,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 31,360.00 USD | 63,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 1,130.00 USD | 63,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 10,810.00 USD | 63,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 19,650.00 USD | 63,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 2,310.00 USD | 63,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 18,150.00 USD | 63,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 26,710.00 USD | 63,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 6,600.00 USD | 63,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 194,370.00 USD | 63,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 24,740.00 USD | 63,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 86,300.00 USD | 63,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 216,840.00 USD | 62,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 44,260.00 USD | 62,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 111,510.00 USD | 62,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 147,570.00 USD | 62,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 2,190.00 USD | 62,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 7,110.00 USD | 62,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 16,330.00 USD | 62,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 508,640.00 USD | 62,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 5,330.00 USD | 61,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 77,140.00 USD | 61,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 6,620.00 USD | 61,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 3,000,000.00 USD | 61,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 59,990.00 USD | 58,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 75,770.00 USD | 58,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 22,360.00 USD | 58,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 95,970.00 USD | 58,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 367,410.00 USD | 58,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 96,190.00 USD | 58,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 137,830.00 USD | 58,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 134,950.00 USD | 57,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 79,310.00 USD | 57,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 92,190.00 USD | 57,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 55,870.00 USD | 57,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 156,170.00 USD | 57,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,890,000.00 USD | 57,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 152,440.00 USD | 23,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 452,590.00 USD | 23,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 117,230.00 USD | 22,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 497,840.00 USD | 22,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 287,950.00 USD | 22,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 2,680,000.00 USD | 22,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,130,000.00 USD | 19,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 180,980.00 USD | 17,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,650,000.00 USD | 17,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 382,300.00 USD | 15,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.07` | 99,070,000.00 USD | 99,070,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.07` | 1,310,000.00 USD | 15,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 176,480.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.09` | 99,070,000.00 USD | 99,070,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 99,030,000.00 USD | 99,030,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 98,930,000.00 USD | 98,930,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.09` | 390,190.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.10` | 98,890,000.00 USD | 98,890,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 98,890,000.00 USD | 98,890,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 98,600,000.00 USD | 98,600,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.10` | 109,910.00 USD | 13,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.11` | 98,600,000.00 USD | 98,600,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 98,600,000.00 USD | 98,600,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 98,590,000.00 USD | 98,590,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 578,850.00 USD | 13,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.12` | 98,540,000.00 USD | 98,540,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 98,530,000.00 USD | 98,530,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 98,450,000.00 USD | 98,450,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 90,580,000.00 USD | 90,580,000.00 USD | 25,830.00 USD | 44,000.00 USD | 175,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 98,430,000.00 USD | 98,430,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 90,340,000.00 USD | 90,340,000.00 USD | 97,300.00 USD | 49,730.00 USD | 172,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,180,000.00 USD | 12,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.13` | 98,210,000.00 USD | 98,210,000.00 USD | 0.00 USD | 53,430.00 USD | 94,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 90,020,000.00 USD | 90,020,000.00 USD | 31,450.00 USD | 41,790.00 USD | 153,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 98,070,000.00 USD | 98,070,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 89,790,000.00 USD | 89,790,000.00 USD | 74,730.00 USD | 82,720.00 USD | 192,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 97,870,000.00 USD | 97,870,000.00 USD | 5,450.00 USD | 55,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 89,440,000.00 USD | 89,440,000.00 USD | 6,330.00 USD | 101,970.00 USD | 318,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 97,810,000.00 USD | 97,810,000.00 USD | 69,750.00 USD | 93,260.00 USD | 108,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 89,010,000.00 USD | 89,010,000.00 USD | 88,690.00 USD | 39,080.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 97,540,000.00 USD | 97,540,000.00 USD | 74,920.00 USD | 99,410.00 USD | 224,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 88,850,000.00 USD | 88,850,000.00 USD | 4,270.00 USD | 151,320.00 USD | 175,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 165,490.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.14` | 97,140,000.00 USD | 97,140,000.00 USD | 79,780.00 USD | 88,050.00 USD | 370,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 88,510,000.00 USD | 88,510,000.00 USD | 81,050.00 USD | 49,560.00 USD | 97,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 96,600,000.00 USD | 96,600,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 88,290,000.00 USD | 88,290,000.00 USD | 26,280.00 USD | 52,050.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 96,570,000.00 USD | 96,570,000.00 USD | 39,170.00 USD | 54,580.00 USD | 250,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 88,100,000.00 USD | 88,100,000.00 USD | 29,510.00 USD | 10,830.00 USD | 153,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 96,230,000.00 USD | 96,230,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 87,910,000.00 USD | 87,910,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 96,090,000.00 USD | 96,090,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 87,770,000.00 USD | 87,770,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 280,040.00 USD | 10,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 96,080,000.00 USD | 96,080,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 96,020,000.00 USD | 96,020,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 87,730,000.00 USD | 87,730,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 95,640,000.00 USD | 95,640,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 95,490,000.00 USD | 95,490,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 87,710,000.00 USD | 87,710,000.00 USD | 4,040.00 USD | 14,590.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 95,330,000.00 USD | 95,330,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 87,510,000.00 USD | 87,510,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 359,890.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 94,450,000.00 USD | 94,450,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 87,170,000.00 USD | 87,170,000.00 USD | 72,570.00 USD | 16,310.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 94,210,000.00 USD | 94,210,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 87,050,000.00 USD | 87,050,000.00 USD | 125,390.00 USD | 15,500.00 USD | 433,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 93,350,000.00 USD | 93,350,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 86,470,000.00 USD | 86,470,000.00 USD | 196,310.00 USD | 74,700.00 USD | 134,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 92,270,000.00 USD | 92,270,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 86,070,000.00 USD | 86,070,000.00 USD | 189,220.00 USD | 289,860.00 USD | 292,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 90,970,000.00 USD | 90,970,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 85,300,000.00 USD | 85,300,000.00 USD | 73,960.00 USD | 29,590.00 USD | 473,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,300,000.00 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.17` | 89,300,000.00 USD | 89,300,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 84,720,000.00 USD | 84,720,000.00 USD | 121,070.00 USD | 109,760.00 USD | 102,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 87,960,000.00 USD | 87,960,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 84,390,000.00 USD | 84,390,000.00 USD | 101,220.00 USD | 95,020.00 USD | 206,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 86,890,000.00 USD | 86,890,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 83,980,000.00 USD | 83,980,000.00 USD | 361,890.00 USD | 3,910.00 USD | 415,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 84,850,000.00 USD | 84,850,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 83,200,000.00 USD | 83,200,000.00 USD | 104,550.00 USD | 79,710.00 USD | 338,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 83,650,000.00 USD | 83,650,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 82,680,000.00 USD | 82,680,000.00 USD | 396,370.00 USD | 140,700.00 USD | 416,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 274,310.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.18` | 82,080,000.00 USD | 82,080,000.00 USD | 181,850.00 USD | 71,240.00 USD | 372,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 81,730,000.00 USD | 81,730,000.00 USD | 71,610.00 USD | 44,040.00 USD | 250,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 81,450,000.00 USD | 81,450,000.00 USD | 85,020.00 USD | 73,410.00 USD | 483,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 81,360,000.00 USD | 81,360,000.00 USD | 90,040.00 USD | 42,260.00 USD | 198,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 80,810,000.00 USD | 80,810,000.00 USD | 267,580.00 USD | 112,520.00 USD | 200,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 81,030,000.00 USD | 81,030,000.00 USD | 144,240.00 USD | 19,410.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 80,230,000.00 USD | 80,230,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 80,860,000.00 USD | 80,860,000.00 USD | 150,010.00 USD | 19,860.00 USD | 660,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 79,960,000.00 USD | 79,960,000.00 USD | 297,510.00 USD | 570,360.00 USD | 235,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 80,030,000.00 USD | 80,030,000.00 USD | 225,800.00 USD | 63,560.00 USD | 143,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 568,290.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.19` | 78,860,000.00 USD | 78,860,000.00 USD | 76,370.00 USD | 69,240.00 USD | 706,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 79,590,000.00 USD | 79,590,000.00 USD | 109,160.00 USD | 518,680.00 USD | 653,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 78,010,000.00 USD | 78,010,000.00 USD | 216,820.00 USD | 93,330.00 USD | 477,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 78,310,000.00 USD | 78,310,000.00 USD | 360,560.00 USD | 90,130.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 77,220,000.00 USD | 77,220,000.00 USD | 179,980.00 USD | 69,020.00 USD | 728,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 76,570,000.00 USD | 76,570,000.00 USD | 61,250.00 USD | 47,660.00 USD | 373,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 76,240,000.00 USD | 76,240,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 76,090,000.00 USD | 76,090,000.00 USD | 157,580.00 USD | 502,360.00 USD | 448,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 74,880,000.00 USD | 74,880,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 74,980,000.00 USD | 74,980,000.00 USD | 381,040.00 USD | 157,690.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 607,930.00 USD | 7,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.20` | 74,050,000.00 USD | 74,050,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 72,400,000.00 USD | 72,400,000.00 USD | 748,570.00 USD | 87,450.00 USD | 794,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 72,470,000.00 USD | 72,470,000.00 USD | 31,150.00 USD | 372,080.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 70,770,000.00 USD | 70,770,000.00 USD | 179,370.00 USD | 934,870.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 69,460,000.00 USD | 69,460,000.00 USD | 736,290.00 USD | 466,100.00 USD | 255,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 68,140,000.00 USD | 68,140,000.00 USD | 873,590.00 USD | 570,220.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 68,000,000.00 USD | 68,000,000.00 USD | 264,000.00 USD | 144,630.00 USD | 464,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 64,680,000.00 USD | 64,680,000.00 USD | 356,900.00 USD | 134,770.00 USD | 839,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 67,120,000.00 USD | 67,120,000.00 USD | 47,500.00 USD | 723,100.00 USD | 155,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 63,350,000.00 USD | 63,350,000.00 USD | 363,980.00 USD | 935,640.00 USD | 376,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 11,860.00 USD | 6,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.21` | 66,200,000.00 USD | 66,200,000.00 USD | 0.00 USD | 77,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 61,680,000.00 USD | 61,680,000.00 USD | 866,390.00 USD | 210,790.00 USD | 1,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 66,120,000.00 USD | 66,120,000.00 USD | 556,190.00 USD | 0.00 USD | 387,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 58,810,000.00 USD | 58,810,000.00 USD | 1,680,000.00 USD | 245,020.00 USD | 950,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 65,180,000.00 USD | 65,180,000.00 USD | 257,960.00 USD | 498,260.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 55,940,000.00 USD | 55,940,000.00 USD | 205,850.00 USD | 723,700.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 61,330,000.00 USD | 61,330,000.00 USD | 1,350,000.00 USD | 0.00 USD | 899,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 53,100,000.00 USD | 53,100,000.00 USD | 1,480,000.00 USD | 334,090.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 59,080,000.00 USD | 59,080,000.00 USD | 108,640.00 USD | 136,460.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 49,990,000.00 USD | 49,990,000.00 USD | 56,590.00 USD | 268,640.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 54,190.00 USD | 6,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 57,550,000.00 USD | 57,550,000.00 USD | 142,210.00 USD | 9,150.00 USD | 253,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 48,650,000.00 USD | 48,650,000.00 USD | 307,460.00 USD | 66,380.00 USD | 536,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 57,150,000.00 USD | 57,150,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 47,740,000.00 USD | 47,740,000.00 USD | 203,470.00 USD | 49,690.00 USD | 10,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 56,410,000.00 USD | 56,410,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 47,480,000.00 USD | 47,480,000.00 USD | 64,370.00 USD | 321,780.00 USD | 300,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 55,330,000.00 USD | 55,330,000.00 USD | 0.00 USD | 164,230.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 46,790,000.00 USD | 46,790,000.00 USD | 124,230.00 USD | 5,400.00 USD | 359,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 55,150,000.00 USD | 55,150,000.00 USD | 51,610.00 USD | 170,590.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 46,300,000.00 USD | 46,300,000.00 USD | 586,370.00 USD | 613,210.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 6,610,000.00 USD | 6,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 54,900,000.00 USD | 54,900,000.00 USD | 112,770.00 USD | 802,580.00 USD | 482,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 41,910,000.00 USD | 41,910,000.00 USD | 256,900.00 USD | 267,560.00 USD | 415,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 53,500,000.00 USD | 53,500,000.00 USD | 59,160.00 USD | 950,550.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 40,970,000.00 USD | 40,970,000.00 USD | 638,880.00 USD | 1,200,000.00 USD | 2,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 52,460,000.00 USD | 52,460,000.00 USD | 198,530.00 USD | 1,150,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 36,320,000.00 USD | 36,320,000.00 USD | 202,670.00 USD | 1,290,000.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 50,000,000.00 USD | 50,000,000.00 USD | 1,020,000.00 USD | 1,070,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 31,850,000.00 USD | 31,850,000.00 USD | 1,550,000.00 USD | 677,020.00 USD | 2,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 46,310,000.00 USD | 46,310,000.00 USD | 1,660,000.00 USD | 1,820,000.00 USD | 3,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 26,940,000.00 USD | 26,940,000.00 USD | 424,470.00 USD | 1,530,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 62,550.00 USD | 62,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.24` | 38,970,000.00 USD | 38,970,000.00 USD | 2,040,000.00 USD | 1,820,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 22,850,000.00 USD | 22,850,000.00 USD | 283,950.00 USD | 567,990.00 USD | 632,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 32,370,000.00 USD | 32,370,000.00 USD | 2,870,000.00 USD | 2,120,000.00 USD | 4,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 21,360,000.00 USD | 21,360,000.00 USD | 918,230.00 USD | 955,200.00 USD | 3,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 22,940,000.00 USD | 22,940,000.00 USD | 2,070,000.00 USD | 1,220,000.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 16,460,000.00 USD | 16,460,000.00 USD | 843,320.00 USD | 624,890.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 18,360,000.00 USD | 18,360,000.00 USD | 1,130,000.00 USD | 510,590.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 13,010,000.00 USD | 13,010,000.00 USD | 828,020.00 USD | 969,790.00 USD | 2,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 15,640,000.00 USD | 15,640,000.00 USD | 1,420,000.00 USD | 232,940.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 8,320,000.00 USD | 8,320,000.00 USD | 1,700,000.00 USD | 472,540.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 12,440,000.00 USD | 12,440,000.00 USD | 3,770,000.00 USD | 337,070.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 4,870,000.00 USD | 4,870,000.00 USD | 1,020,000.00 USD | 769,380.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 6,040,000.00 USD | 6,040,000.00 USD | 1,630,000.00 USD | 325,530.00 USD | 3,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 712,500.00 USD | 652,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 489,680.00 USD | 489,680.00 USD | 489,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 4,760.00 USD | 4,760.00 USD | 0.00 USD | 1,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 3,370.00 USD | 3,370.00 USD | 0.00 USD | 3,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 63,660.00 USD | 63,660.00 USD | 63,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 127,310.00 USD | 127,310.00 USD | 63,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 254,670.00 USD | 254,670.00 USD | 0.00 USD | 12,640.00 USD | 242,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 286,130.00 USD | 286,130.00 USD | 150,010.00 USD | 8,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 339,940.00 USD | 339,940.00 USD | 73,940.00 USD | 11,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 305,970.00 USD | 305,970.00 USD | 0.00 USD | 19,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 376,090.00 USD | 376,090.00 USD | 0.00 USD | 24,960.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 398,430.00 USD | 398,430.00 USD | 0.00 USD | 10,110.00 USD | 82,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 627,970.00 USD | 627,970.00 USD | 229,640.00 USD | 8,660.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 545,980.00 USD | 545,980.00 USD | 144,170.00 USD | 3,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 2,500,000.00 USD | 2,500,000.00 USD | 409,480.00 USD | 308,120.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 542,940.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 4,200,000.00 USD | 4,200,000.00 USD | 636,140.00 USD | 423,290.00 USD | 643,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 1,010.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.27` | 6,400,000.00 USD | 6,400,000.00 USD | 4,260,000.00 USD | 9,150.00 USD | 20,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 5,960,000.00 USD | 5,960,000.00 USD | 845,960.00 USD | 221,950.00 USD | 682,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 1,870,000.00 USD | 3,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 10,180,000.00 USD | 10,180,000.00 USD | 715,560.00 USD | 1,940,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 16,170,000.00 USD | 16,170,000.00 USD | 138,500.00 USD | 2,750,000.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 15,480,000.00 USD | 15,480,000.00 USD | 734,620.00 USD | 1,400,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 24,250,000.00 USD | 24,250,000.00 USD | 1,680,000.00 USD | 4,950,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 21,430,000.00 USD | 21,430,000.00 USD | 2,180,000.00 USD | 1,080,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 40,500,000.00 USD | 40,500,000.00 USD | 2,710,000.00 USD | 2,870,000.00 USD | 10,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 29,440,000.00 USD | 29,440,000.00 USD | 1,130,000.00 USD | 2,630,000.00 USD | 4,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 5,670.00 USD | 6,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.28` | 55,370,000.00 USD | 55,370,000.00 USD | 5,150,000.00 USD | 3,080,000.00 USD | 6,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 36,890,000.00 USD | 36,890,000.00 USD | 2,160,000.00 USD | 1,560,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 74,520,000.00 USD | 74,520,000.00 USD | 7,780,000.00 USD | 3,760,000.00 USD | 7,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 45,870,000.00 USD | 45,870,000.00 USD | 2,550,000.00 USD | 2,330,000.00 USD | 4,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 77,620,000.00 USD | 77,620,000.00 USD | 0.00 USD | 1,700,000.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 49,670,000.00 USD | 49,670,000.00 USD | 393,830.00 USD | 759,560.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 79,650,000.00 USD | 79,650,000.00 USD | 1,030,000.00 USD | 139,170.00 USD | 861,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 53,480,000.00 USD | 53,480,000.00 USD | 1,330,000.00 USD | 472,310.00 USD | 2,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 83,230,000.00 USD | 83,230,000.00 USD | 1,100,000.00 USD | 1,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 56,860,000.00 USD | 56,860,000.00 USD | 817,320.00 USD | 640,040.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 6,190.00 USD | 12,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.29` | 87,810,000.00 USD | 87,810,000.00 USD | 796,960.00 USD | 1,300,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 59,870,000.00 USD | 59,870,000.00 USD | 864,310.00 USD | 1,100,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 88,530,000.00 USD | 88,530,000.00 USD | 685,300.00 USD | 2,730.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 60,990,000.00 USD | 60,990,000.00 USD | 454,460.00 USD | 148,440.00 USD | 518,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 90,130,000.00 USD | 90,130,000.00 USD | 70,460.00 USD | 277,240.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 62,370,000.00 USD | 62,370,000.00 USD | 186,090.00 USD | 270,800.00 USD | 919,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 92,730,000.00 USD | 92,730,000.00 USD | 1,040,000.00 USD | 202,640.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 66,170,000.00 USD | 66,170,000.00 USD | 570,020.00 USD | 278,090.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 96,370,000.00 USD | 96,370,000.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 72,340,000.00 USD | 72,340,000.00 USD | 1,880,000.00 USD | 719,050.00 USD | 3,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 51,250.00 USD | 64,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.30` | 103,660,000.00 USD | 103,660,000.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 74,920,000.00 USD | 74,920,000.00 USD | 554,720.00 USD | 706,700.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 105,610,000.00 USD | 105,610,000.00 USD | 25,800.00 USD | 172,080.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 75,740,000.00 USD | 75,740,000.00 USD | 401,840.00 USD | 109,620.00 USD | 313,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 107,990,000.00 USD | 107,990,000.00 USD | 208,510.00 USD | 434,510.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 78,630,000.00 USD | 78,630,000.00 USD | 674,250.00 USD | 469,750.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 109,020,000.00 USD | 109,020,000.00 USD | 85,960.00 USD | 944,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 80,630,000.00 USD | 80,630,000.00 USD | 803,540.00 USD | 645,090.00 USD | 554,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 111,820,000.00 USD | 111,820,000.00 USD | 0.00 USD | 2,170,000.00 USD | 635,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 82,130,000.00 USD | 82,130,000.00 USD | 372,370.00 USD | 664,450.00 USD | 458,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 1,630.00 USD | 65,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.31` | 113,830,000.00 USD | 113,830,000.00 USD | 1,770,000.00 USD | 238,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 85,110,000.00 USD | 85,110,000.00 USD | 777,430.00 USD | 253,070.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 119,000,000.00 USD | 119,000,000.00 USD | 1,550,000.00 USD | 821,310.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 88,750,000.00 USD | 88,750,000.00 USD | 1,240,000.00 USD | 442,560.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 121,400,000.00 USD | 121,400,000.00 USD | 1,340,000.00 USD | 414,180.00 USD | 647,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 91,330,000.00 USD | 91,330,000.00 USD | 944,800.00 USD | 557,880.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 126,280,000.00 USD | 126,280,000.00 USD | 189,510.00 USD | 858,660.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 93,250,000.00 USD | 93,250,000.00 USD | 515,120.00 USD | 340,250.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 127,570,000.00 USD | 127,570,000.00 USD | 638,380.00 USD | 151,320.00 USD | 501,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 95,390,000.00 USD | 95,390,000.00 USD | 437,130.00 USD | 320,320.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 62,960.00 USD | 128,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.32` | 132,290,000.00 USD | 132,290,000.00 USD | 68,520.00 USD | 1,890,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 100,510,000.00 USD | 100,510,000.00 USD | 1,280,000.00 USD | 753,370.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 137,390,000.00 USD | 137,390,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 105,260,000.00 USD | 105,260,000.00 USD | 1,560,000.00 USD | 684,990.00 USD | 2,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 139,410,000.00 USD | 139,410,000.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 107,810,000.00 USD | 107,810,000.00 USD | 1,340,000.00 USD | 339,190.00 USD | 867,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 142,760,000.00 USD | 142,760,000.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 110,720,000.00 USD | 110,720,000.00 USD | 885,300.00 USD | 460,840.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 145,540,000.00 USD | 145,540,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 111,720,000.00 USD | 111,720,000.00 USD | 599,940.00 USD | 61,650.00 USD | 341,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 7,390.00 USD | 136,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.33` | 147,350,000.00 USD | 147,350,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 112,790,000.00 USD | 112,790,000.00 USD | 412,050.00 USD | 225,260.00 USD | 436,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 148,450,000.00 USD | 148,450,000.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 114,170,000.00 USD | 114,170,000.00 USD | 504,110.00 USD | 72,470.00 USD | 798,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 150,160,000.00 USD | 150,160,000.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 116,340,000.00 USD | 116,340,000.00 USD | 848,670.00 USD | 101,110.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 152,620,000.00 USD | 152,620,000.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 118,290,000.00 USD | 118,290,000.00 USD | 737,030.00 USD | 194,040.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 154,650,000.00 USD | 154,650,000.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 119,630,000.00 USD | 119,630,000.00 USD | 459,140.00 USD | 356,270.00 USD | 517,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 44,630.00 USD | 180,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.34` | 156,200,000.00 USD | 156,200,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 120,370,000.00 USD | 120,370,000.00 USD | 388,720.00 USD | 23,420.00 USD | 332,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 158,640,000.00 USD | 158,640,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 120,910,000.00 USD | 120,910,000.00 USD | 179,460.00 USD | 82,510.00 USD | 282,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 160,490,000.00 USD | 160,490,000.00 USD | 804,660.00 USD | 463,950.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 122,230,000.00 USD | 122,230,000.00 USD | 629,770.00 USD | 243,030.00 USD | 439,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 165,960,000.00 USD | 165,960,000.00 USD | 2,380,000.00 USD | 2,430,000.00 USD | 660,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 123,750,000.00 USD | 123,750,000.00 USD | 697,160.00 USD | 223,580.00 USD | 606,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 173,080,000.00 USD | 173,080,000.00 USD | 2,000,000.00 USD | 1,890,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 125,060,000.00 USD | 125,060,000.00 USD | 497,250.00 USD | 284,400.00 USD | 524,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 4,170.00 USD | 184,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.35` | 181,340,000.00 USD | 181,340,000.00 USD | 3,270,000.00 USD | 1,640,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 125,450,000.00 USD | 125,450,000.00 USD | 127,140.00 USD | 103,350.00 USD | 158,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 189,090,000.00 USD | 189,090,000.00 USD | 2,780,000.00 USD | 1,820,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 126,000,000.00 USD | 126,000,000.00 USD | 249,180.00 USD | 23,180.00 USD | 275,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 197,110,000.00 USD | 197,110,000.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 126,410,000.00 USD | 126,410,000.00 USD | 146,270.00 USD | 30,410.00 USD | 237,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 206,230,000.00 USD | 206,230,000.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 126,560,000.00 USD | 126,560,000.00 USD | 66,220.00 USD | 30,780.00 USD | 49,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 212,970,000.00 USD | 212,970,000.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 127,070,000.00 USD | 127,070,000.00 USD | 86,720.00 USD | 34,870.00 USD | 395,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 5,020.00 USD | 189,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.36` | 219,310,000.00 USD | 219,310,000.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 128,030,000.00 USD | 128,030,000.00 USD | 391,410.00 USD | 32,820.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 221,850,000.00 USD | 221,850,000.00 USD | 1,060,000.00 USD | 639,580.00 USD | 837,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 128,370,000.00 USD | 128,370,000.00 USD | 209,880.00 USD | 43,200.00 USD | 82,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 224,870,000.00 USD | 224,870,000.00 USD | 1,460,000.00 USD | 339,580.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 129,020,000.00 USD | 129,020,000.00 USD | 225,120.00 USD | 162,390.00 USD | 269,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 228,470,000.00 USD | 228,470,000.00 USD | 1,480,000.00 USD | 711,020.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 129,320,000.00 USD | 129,320,000.00 USD | 130,140.00 USD | 3,300.00 USD | 166,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 231,210,000.00 USD | 231,210,000.00 USD | 1,420,000.00 USD | 616,140.00 USD | 698,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 129,440,000.00 USD | 129,440,000.00 USD | 0.00 USD | 12,740.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 99,140.00 USD | 289,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.37` | 232,030,000.00 USD | 232,030,000.00 USD | 206,650.00 USD | 189,790.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 129,700,000.00 USD | 129,700,000.00 USD | 59,970.00 USD | 89,800.00 USD | 103,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 233,080,000.00 USD | 233,080,000.00 USD | 486,840.00 USD | 176,380.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 129,840,000.00 USD | 129,840,000.00 USD | 93,070.00 USD | 21,460.00 USD | 28,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 234,400,000.00 USD | 234,400,000.00 USD | 367,350.00 USD | 211,750.00 USD | 733,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 129,940,000.00 USD | 129,940,000.00 USD | 5,340.00 USD | 39,430.00 USD | 60,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 235,630,000.00 USD | 235,630,000.00 USD | 393,010.00 USD | 171,680.00 USD | 667,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 130,040,000.00 USD | 130,040,000.00 USD | 5,470.00 USD | 2,610.00 USD | 85,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 237,300,000.00 USD | 237,300,000.00 USD | 563,840.00 USD | 386,690.00 USD | 717,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 130,360,000.00 USD | 130,360,000.00 USD | 97,300.00 USD | 49,730.00 USD | 172,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 3,780.00 USD | 292,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.38` | 238,330,000.00 USD | 238,330,000.00 USD | 242,030.00 USD | 273,360.00 USD | 514,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 130,580,000.00 USD | 130,580,000.00 USD | 31,450.00 USD | 41,790.00 USD | 153,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 239,790,000.00 USD | 239,790,000.00 USD | 692,200.00 USD | 267,730.00 USD | 499,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 130,930,000.00 USD | 130,930,000.00 USD | 74,730.00 USD | 82,720.00 USD | 192,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 241,490,000.00 USD | 241,490,000.00 USD | 436,360.00 USD | 195,830.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 131,000,000.00 USD | 131,000,000.00 USD | 2,300.00 USD | 65,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 243,350,000.00 USD | 243,350,000.00 USD | 710,620.00 USD | 348,810.00 USD | 802,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 131,360,000.00 USD | 131,360,000.00 USD | 4,030.00 USD | 36,450.00 USD | 318,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 244,230,000.00 USD | 244,230,000.00 USD | 403,730.00 USD | 253,120.00 USD | 228,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 131,530,000.00 USD | 131,530,000.00 USD | 88,690.00 USD | 39,080.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,130.00 USD | 293,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.39` | 245,260,000.00 USD | 245,260,000.00 USD | 377,810.00 USD | 234,230.00 USD | 413,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 131,860,000.00 USD | 131,860,000.00 USD | 4,270.00 USD | 151,320.00 USD | 175,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 246,470,000.00 USD | 246,470,000.00 USD | 384,080.00 USD | 308,280.00 USD | 518,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 132,090,000.00 USD | 132,090,000.00 USD | 81,050.00 USD | 49,560.00 USD | 97,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 247,220,000.00 USD | 247,220,000.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 132,110,000.00 USD | 132,110,000.00 USD | 0.00 USD | 18,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 247,750,000.00 USD | 247,750,000.00 USD | 82,350.00 USD | 90,970.00 USD | 358,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 132,270,000.00 USD | 132,270,000.00 USD | 26,280.00 USD | 33,400.00 USD | 107,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 247,910,000.00 USD | 247,910,000.00 USD | 39,170.00 USD | 22,660.00 USD | 101,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 132,460,000.00 USD | 132,460,000.00 USD | 29,510.00 USD | 10,080.00 USD | 151,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 2,090.00 USD | 296,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 248,130,000.00 USD | 248,130,000.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 132,590,000.00 USD | 132,590,000.00 USD | 77,100.00 USD | 0.00 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 248,140,000.00 USD | 248,140,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 248,210,000.00 USD | 248,210,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 248,280,000.00 USD | 248,280,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 248,580,000.00 USD | 248,580,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 635.06 USD | 296,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 248,730,000.00 USD | 248,730,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 248,870,000.00 USD | 248,870,000.00 USD | 4,390.00 USD | 15,880.00 USD | 120,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 249,150,000.00 USD | 249,150,000.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,730.00 USD | 300,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,510.00 USD | 393,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 988.72 USD | 394,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 561,440.00 USD | 956,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 129,320.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 551.65 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,470.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 11,570.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 174.99 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 1,370.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 4,400,000.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 3,290.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 130,580.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 2,660.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 1,300.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 6,710.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 2,580.00 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 5,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 5,020.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 4,180.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 110.17 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 1,100.00 USD | 5,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 7,300.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,730.00 USD | 5,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,490.00 USD | 5,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 5,420,000.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 131,990.00 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 3,680.00 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 1,340.00 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 260.98 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 99,280.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 2,730,000.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 12,810.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,010.00 USD | 14,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 2,890,000.00 USD | 16,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,190.00 USD | 16,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 307,570.00 USD | 17,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 1,410.00 USD | 17,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 17,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 227,560.00 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.99` | 694.75 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 164.41 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 513.83 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 1,060.00 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 198.36 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 123.30 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 413,630.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 373.50 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 4,870.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 294.70 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,100.00 USD | 17,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 249,280.00 USD | 18,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 631.42 USD | 18,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,830.00 USD | 18,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 51,830.00 USD | 18,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 100.97 USD | 18,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 81,150.00 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 101.89 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 338.20 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 102.81 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 11,330.00 USD | 18,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 141.67 USD | 18,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 105.57 USD | 18,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 77,210.00 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 44,970.00 USD | 18,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 2,850.00 USD | 18,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 2,550.00 USD | 18,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 11,860.00 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 146.63 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 2,380.00 USD | 18,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 3,700,000.00 USD | 22,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 18,600.00 USD | 22,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 1,160.00 USD | 22,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 24,420.00 USD | 22,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 645.27 USD | 22,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 370,330.00 USD | 22,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 227.70 USD | 22,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 337.96 USD | 22,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 1,590,000.00 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 1,880.00 USD | 24,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 64,650,000.00 USD | 0.00 USD | 1,360.00 USD | `-79.69%` | `5,324.00` |
| `Live` | `Long` | `0.2650` | 64,650,000.00 USD | 0.00 USD | 1,720.00 USD | `-78.89%` | `6,474.00` |
| `Live` | `Long` | `0.2750` | 64,650,000.00 USD | 0.00 USD | 3,220.00 USD | `-78.10%` | `11,707.00` |
| `Live` | `Long` | `0.2850` | 64,640,000.00 USD | 0.00 USD | 378.20 USD | `-77.30%` | `1,327.00` |
| `Live` | `Long` | `0.2950` | 64,640,000.00 USD | 0.00 USD | 28,780.00 USD | `-76.51%` | `97,549.00` |
| `Live` | `Long` | `0.3050` | 64,610,000.00 USD | 0.00 USD | 235.16 USD | `-75.71%` | `771.00` |
| `Live` | `Long` | `0.3150` | 64,610,000.00 USD | 0.00 USD | 5,320.00 USD | `-74.91%` | `16,894.00` |
| `Live` | `Long` | `0.3250` | 64,610,000.00 USD | 0.00 USD | 4,710.00 USD | `-74.12%` | `14,484.00` |
| `Live` | `Long` | `0.3350` | 64,600,000.00 USD | 0.00 USD | 1,930.00 USD | `-73.32%` | `5,751.00` |
| `Live` | `Long` | `0.3450` | 64,600,000.00 USD | 0.00 USD | 16,980.00 USD | `-72.52%` | `49,212.00` |
| `Live` | `Long` | `0.3550` | 64,580,000.00 USD | 0.00 USD | 2,180.00 USD | `-71.73%` | `6,137.00` |
| `Live` | `Long` | `0.3650` | 64,580,000.00 USD | 0.00 USD | 49,350.00 USD | `-70.93%` | `135,212.00` |
| `Live` | `Long` | `0.3750` | 64,530,000.00 USD | 0.00 USD | 3,160.00 USD | `-70.13%` | `8,418.00` |
| `Live` | `Long` | `0.3950` | 64,530,000.00 USD | 0.00 USD | 2,170.00 USD | `-68.54%` | `5,496.00` |
| `Live` | `Long` | `0.4050` | 64,530,000.00 USD | 0.00 USD | 614.38 USD | `-67.74%` | `1,517.00` |
| `Live` | `Long` | `0.4150` | 64,530,000.00 USD | 0.00 USD | 1,170.00 USD | `-66.95%` | `2,821.00` |
| `Live` | `Long` | `0.4250` | 64,520,000.00 USD | 0.00 USD | 29,680.00 USD | `-66.15%` | `69,842.00` |
| `Live` | `Long` | `0.4350` | 64,500,000.00 USD | 0.00 USD | 577,120.00 USD | `-65.36%` | `1,326,707.00` |
| `Live` | `Long` | `0.4450` | 63,920,000.00 USD | 0.00 USD | 883.77 USD | `-64.56%` | `1,986.00` |
| `Live` | `Long` | `0.4550` | 63,920,000.00 USD | 0.00 USD | 160,020.00 USD | `-63.76%` | `351,693.00` |
| `Live` | `Long` | `0.4650` | 63,760,000.00 USD | 0.00 USD | 397.11 USD | `-62.97%` | `854.00` |
| `Live` | `Long` | `0.4750` | 63,760,000.00 USD | 0.00 USD | 2,000.00 USD | `-62.17%` | `4,211.00` |
| `Live` | `Long` | `0.4850` | 63,750,000.00 USD | 0.00 USD | 323.98 USD | `-61.37%` | `668.00` |
| `Live` | `Long` | `0.4950` | 63,750,000.00 USD | 0.00 USD | 6,470.00 USD | `-60.58%` | `13,074.00` |
| `Live` | `Long` | `0.5050` | 63,750,000.00 USD | 0.00 USD | 188.87 USD | `-59.78%` | `374.00` |
| `Live` | `Long` | `0.5150` | 63,750,000.00 USD | 0.00 USD | 9,050.00 USD | `-58.98%` | `17,571.00` |
| `Live` | `Long` | `0.5250` | 63,740,000.00 USD | 0.00 USD | 2,810.00 USD | `-58.19%` | `5,352.00` |
| `Live` | `Long` | `0.5350` | 63,740,000.00 USD | 0.00 USD | 3,530.00 USD | `-57.39%` | `6,591.00` |
| `Live` | `Long` | `0.5450` | 63,730,000.00 USD | 0.00 USD | 27,050.00 USD | `-56.59%` | `49,627.00` |
| `Live` | `Long` | `0.5550` | 63,710,000.00 USD | 0.00 USD | 160,990.00 USD | `-55.80%` | `290,074.00` |
| `Live` | `Long` | `0.5650` | 63,540,000.00 USD | 0.00 USD | 2,070.00 USD | `-55.00%` | `3,667.00` |
| `Live` | `Long` | `0.5750` | 63,540,000.00 USD | 0.00 USD | 8,760.00 USD | `-54.21%` | `15,235.00` |
| `Live` | `Long` | `0.5850` | 63,530,000.00 USD | 0.00 USD | 4,900.00 USD | `-53.41%` | `8,376.00` |
| `Live` | `Long` | `0.5950` | 63,530,000.00 USD | 0.00 USD | 198.13 USD | `-52.61%` | `333.00` |
| `Live` | `Long` | `0.6050` | 63,530,000.00 USD | 0.00 USD | 23,080.00 USD | `-51.82%` | `38,148.00` |
| `Live` | `Long` | `0.6150` | 63,510,000.00 USD | 0.00 USD | 39,120.00 USD | `-51.02%` | `63,607.00` |
| `Live` | `Long` | `0.6250` | 63,470,000.00 USD | 0.00 USD | 1,130.00 USD | `-50.22%` | `1,803.00` |
| `Live` | `Long` | `0.6350` | 63,470,000.00 USD | 0.00 USD | 10,510.00 USD | `-49.43%` | `16,554.00` |
| `Live` | `Long` | `0.6450` | 63,450,000.00 USD | 0.00 USD | 21,730.00 USD | `-48.63%` | `33,694.00` |
| `Live` | `Long` | `0.6550` | 63,430,000.00 USD | 0.00 USD | 2,630.00 USD | `-47.83%` | `4,011.00` |
| `Live` | `Long` | `0.6650` | 63,430,000.00 USD | 0.00 USD | 17,790.00 USD | `-47.04%` | `26,754.00` |
| `Live` | `Long` | `0.6750` | 63,410,000.00 USD | 0.00 USD | 26,110.00 USD | `-46.24%` | `38,677.00` |
| `Live` | `Long` | `0.6850` | 63,390,000.00 USD | 0.00 USD | 2,980.00 USD | `-45.44%` | `4,356.00` |
| `Live` | `Long` | `0.6950` | 63,380,000.00 USD | 0.00 USD | 160,780.00 USD | `-44.65%` | `231,342.00` |
| `Live` | `Long` | `0.7050` | 63,220,000.00 USD | 0.00 USD | 23,200.00 USD | `-43.85%` | `32,902.00` |
| `Live` | `Long` | `0.7150` | 63,200,000.00 USD | 0.00 USD | 68,280.00 USD | `-43.06%` | `95,503.00` |
| `Live` | `Long` | `0.7250` | 63,130,000.00 USD | 0.00 USD | 235,740.00 USD | `-42.26%` | `325,156.00` |
| `Live` | `Long` | `0.7350` | 62,900,000.00 USD | 0.00 USD | 45,360.00 USD | `-41.46%` | `61,711.00` |
| `Live` | `Long` | `0.7450` | 62,850,000.00 USD | 0.00 USD | 81,440.00 USD | `-40.67%` | `109,317.00` |
| `Live` | `Long` | `0.7550` | 62,770,000.00 USD | 0.00 USD | 147,720.00 USD | `-39.87%` | `195,652.00` |
| `Live` | `Long` | `0.7650` | 62,620,000.00 USD | 0.00 USD | 2,190.00 USD | `-39.07%` | `2,860.00` |
| `Live` | `Long` | `0.7750` | 62,620,000.00 USD | 0.00 USD | 5,930.00 USD | `-38.28%` | `7,652.00` |
| `Live` | `Long` | `0.7850` | 62,610,000.00 USD | 0.00 USD | 16,460.00 USD | `-37.48%` | `20,966.00` |
| `Live` | `Long` | `0.7950` | 62,600,000.00 USD | 0.00 USD | 44,850.00 USD | `-36.68%` | `56,417.00` |
| `Live` | `Long` | `0.8050` | 62,550,000.00 USD | 0.00 USD | 511,010.00 USD | `-35.89%` | `634,796.00` |
| `Live` | `Long` | `0.8150` | 62,040,000.00 USD | 0.00 USD | 61,010.00 USD | `-35.09%` | `74,853.00` |
| `Live` | `Long` | `0.8250` | 61,980,000.00 USD | 0.00 USD | 23,130.00 USD | `-34.29%` | `28,036.00` |
| `Live` | `Long` | `0.8350` | 61,960,000.00 USD | 0.00 USD | 32,170.00 USD | `-33.50%` | `38,528.00` |
| `Live` | `Long` | `0.8450` | 61,920,000.00 USD | 0.00 USD | 3,050,000.00 USD | `-32.70%` | `3,614,999.00` |
| `Live` | `Long` | `0.8550` | 58,870,000.00 USD | 0.00 USD | 61,290.00 USD | `-31.91%` | `71,682.00` |
| `Live` | `Long` | `0.8650` | 58,810,000.00 USD | 0.00 USD | 38,050.00 USD | `-31.11%` | `43,985.00` |
| `Live` | `Long` | `0.8750` | 58,770,000.00 USD | 0.00 USD | 93,870.00 USD | `-30.31%` | `107,279.00` |
| `Live` | `Long` | `0.8850` | 58,680,000.00 USD | 0.00 USD | 358,270.00 USD | `-29.52%` | `404,830.00` |
| `Live` | `Long` | `0.8950` | 58,320,000.00 USD | 0.00 USD | 97,380.00 USD | `-28.72%` | `108,809.00` |
| `Live` | `Long` | `0.9050` | 58,220,000.00 USD | 0.00 USD | 231,270.00 USD | `-27.92%` | `255,546.00` |
| `Live` | `Long` | `0.9150` | 57,990,000.00 USD | 0.00 USD | 87,390.00 USD | `-27.13%` | `95,507.00` |
| `Live` | `Long` | `0.9250` | 57,900,000.00 USD | 0.00 USD | 76,320.00 USD | `-26.33%` | `82,511.00` |
| `Live` | `Long` | `0.9350` | 57,830,000.00 USD | 0.00 USD | 97,440.00 USD | `-25.53%` | `104,213.00` |
| `Live` | `Long` | `0.9450` | 57,730,000.00 USD | 0.00 USD | 56,350.00 USD | `-24.74%` | `59,627.00` |
| `Live` | `Long` | `0.9550` | 57,670,000.00 USD | 0.00 USD | 153,860.00 USD | `-23.94%` | `161,112.00` |
| `Live` | `Long` | `0.9650` | 57,520,000.00 USD | 0.00 USD | 33,890,000.00 USD | `-23.14%` | `35,121,908.00` |
| `Live` | `Long` | `0.9750` | 23,630,000.00 USD | 0.00 USD | 155,450.00 USD | `-22.35%` | `159,439.00` |
| `Live` | `Long` | `0.9850` | 23,470,000.00 USD | 0.00 USD | 455,050.00 USD | `-21.55%` | `461,984.00` |
| `Live` | `Long` | `0.9950` | 23,010,000.00 USD | 0.00 USD | 113,040.00 USD | `-20.76%` | `113,607.00` |
| `Live` | `Long` | `1.00` | 22,900,000.00 USD | 0.00 USD | 506,580.00 USD | `-19.96%` | `504,061.00` |
| `Live` | `Long` | `1.01` | 22,400,000.00 USD | 0.00 USD | 304,640.00 USD | `-19.16%` | `300,135.00` |
| `Live` | `Long` | `1.02` | 22,090,000.00 USD | 0.00 USD | 2,710,000.00 USD | `-18.37%` | `2,643,366.00` |
| `Live` | `Long` | `1.03` | 19,380,000.00 USD | 0.00 USD | 2,130,000.00 USD | `-17.57%` | `2,061,017.00` |
| `Live` | `Long` | `1.04` | 17,250,000.00 USD | 0.00 USD | 178,070.00 USD | `-16.77%` | `170,398.00` |
| `Live` | `Long` | `1.05` | 17,070,000.00 USD | 0.00 USD | 1,640,000.00 USD | `-15.98%` | `1,556,547.00` |
| `Live` | `Long` | `1.06` | 15,430,000.00 USD | 0.00 USD | 388,560.00 USD | `-15.18%` | `364,841.00` |
| `Live` | `Long` | `1.07` | 15,040,000.00 USD | 0.00 USD | 1,340,000.00 USD | `-14.38%` | `1,246,853.00` |
| `Live` | `Long` | `1.08` | 13,700,000.00 USD | 0.00 USD | 178,030.00 USD | `-13.59%` | `164,087.00` |
| `Live` | `Long` | `1.09` | 13,520,000.00 USD | 0.00 USD | 377,320.00 USD | `-12.79%` | `344,587.00` |
| `Live` | `Long` | `1.10` | 13,140,000.00 USD | 0.00 USD | 101,470.00 USD | `-11.99%` | `91,829.00` |
| `Live` | `Long` | `1.11` | 13,040,000.00 USD | 0.00 USD | 278,180.00 USD | `-11.20%` | `249,487.00` |
| `Live` | `Long` | `1.12` | 12,760,000.00 USD | 0.00 USD | 2,410,000.00 USD | `-10.40%` | `2,145,674.00` |
| `Live` | `Long` | `1.14` | 10,350,000.00 USD | 0.00 USD | 185,410.00 USD | `-9.60%` | `163,353.00` |
| `Live` | `Long` | `1.15` | 10,160,000.00 USD | 0.00 USD | 284,790.00 USD | `-8.81%` | `248,727.00` |
| `Live` | `Long` | `1.16` | 9,880,000.00 USD | 0.00 USD | 361,410.00 USD | `-8.01%` | `312,909.00` |
| `Live` | `Long` | `1.17` | 9,520,000.00 USD | 0.00 USD | 1,280,000.00 USD | `-7.22%` | `1,102,296.00` |
| `Live` | `Long` | `1.18` | 8,230,000.00 USD | 0.00 USD | 276,740.00 USD | `-6.42%` | `235,527.00` |
| `Live` | `Long` | `1.19` | 7,960,000.00 USD | 0.00 USD | 568,820.00 USD | `-5.62%` | `480,017.00` |
| `Live` | `Long` | `1.20` | 7,390,000.00 USD | 0.00 USD | 591,080.00 USD | `-4.83%` | `494,630.00` |
| `Live` | `Long` | `1.21` | 6,800,000.00 USD | 0.00 USD | 2,340.00 USD | `-4.03%` | `1,944.00` |
| `Live` | `Long` | `1.22` | 6,800,000.00 USD | 0.00 USD | 88,230.00 USD | `-3.23%` | `72,621.00` |
| `Live` | `Long` | `1.23` | 6,710,000.00 USD | 0.00 USD | 6,650,000.00 USD | `-2.44%` | `5,427,233.00` |
| `Live` | `Long` | `1.24` | 58,510.00 USD | 0.00 USD | 58,510.00 USD | `-1.64%` | `47,377.00` |
| `Live` | `Short` | `1.27` | 11,660.00 USD | 11,660.00 USD | 0.00 USD | `+1.55%` | `9,146.00` |
| `Live` | `Short` | `1.28` | 248,500.00 USD | 236,840.00 USD | 0.00 USD | `+2.34%` | `184,310.00` |
| `Live` | `Short` | `1.29` | 297,510.00 USD | 49,010.00 USD | 0.00 USD | `+3.14%` | `37,848.00` |
| `Live` | `Short` | `1.30` | 299,770.00 USD | 2,250.00 USD | 0.00 USD | `+3.93%` | `1,726.00` |
| `Live` | `Short` | `1.31` | 354,880.00 USD | 55,110.00 USD | 0.00 USD | `+4.73%` | `41,912.00` |
| `Live` | `Short` | `1.32` | 362,270.00 USD | 7,390.00 USD | 0.00 USD | `+5.53%` | `5,576.00` |
| `Live` | `Short` | `1.33` | 407,030.00 USD | 44,760.00 USD | 0.00 USD | `+6.32%` | `33,531.00` |
| `Live` | `Short` | `1.34` | 413,410.00 USD | 6,380.00 USD | 0.00 USD | `+7.12%` | `4,742.00` |
| `Live` | `Short` | `1.35` | 427,820.00 USD | 14,410.00 USD | 0.00 USD | `+7.92%` | `10,638.00` |
| `Live` | `Short` | `1.36` | 527,400.00 USD | 99,580.00 USD | 0.00 USD | `+8.71%` | `72,950.00` |
| `Live` | `Short` | `1.38` | 531,180.00 USD | 3,780.00 USD | 0.00 USD | `+9.51%` | `2,747.00` |
| `Live` | `Short` | `1.39` | 532,970.00 USD | 1,790.00 USD | 0.00 USD | `+10.31%` | `1,293.00` |
| `Live` | `Short` | `1.40` | 535,280.00 USD | 2,310.00 USD | 0.00 USD | `+11.10%` | `1,659.00` |
| `Live` | `Short` | `1.41` | 536,140.00 USD | 858.46 USD | 0.00 USD | `+11.90%` | `611.00` |
| `Live` | `Short` | `1.42` | 539,870.00 USD | 3,730.00 USD | 0.00 USD | `+12.70%` | `2,635.00` |
| `Live` | `Short` | `1.43` | 633,380.00 USD | 93,510.00 USD | 0.00 USD | `+13.49%` | `65,619.00` |
| `Live` | `Short` | `1.44` | 1,210,000.00 USD | 581,410.00 USD | 0.00 USD | `+14.29%` | `405,163.00` |
| `Live` | `Short` | `1.45` | 1,220,000.00 USD | 284.66 USD | 0.00 USD | `+15.08%` | `197.00` |
| `Live` | `Short` | `1.47` | 1,350,000.00 USD | 131,660.00 USD | 0.00 USD | `+16.68%` | `89,871.00` |
| `Live` | `Short` | `1.48` | 1,350,000.00 USD | 551.65 USD | 0.00 USD | `+17.47%` | `374.00` |
| `Live` | `Short` | `1.50` | 1,360,000.00 USD | 12,150.00 USD | 0.00 USD | `+19.07%` | `8,126.00` |
| `Live` | `Short` | `1.50` | 1,360,000.00 USD | 445.48 USD | 0.00 USD | `+19.86%` | `296.00` |
| `Live` | `Short` | `1.51` | 1,370,000.00 USD | 12,020.00 USD | 0.00 USD | `+20.66%` | `7,935.00` |
| `Live` | `Short` | `1.53` | 1,370,000.00 USD | 174.99 USD | 0.00 USD | `+22.25%` | `114.00` |
| `Live` | `Short` | `1.54` | 1,370,000.00 USD | 1,370.00 USD | 0.00 USD | `+23.05%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,370,000.00 USD | 1,360.00 USD | 0.00 USD | `+23.85%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,380,000.00 USD | 555.57 USD | 0.00 USD | `+24.64%` | `355.00` |
| `Live` | `Short` | `1.57` | 1,380,000.00 USD | 2,900.00 USD | 0.00 USD | `+25.44%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 5,810,000.00 USD | 4,430,000.00 USD | 0.00 USD | `+26.23%` | `2,793,593.00` |
| `Live` | `Short` | `1.59` | 5,810,000.00 USD | 1,260.00 USD | 0.00 USD | `+27.03%` | `789.00` |
| `Live` | `Short` | `1.60` | 5,940,000.00 USD | 130,580.00 USD | 0.00 USD | `+27.83%` | `81,359.00` |
| `Live` | `Short` | `1.61` | 5,940,000.00 USD | 2,530.00 USD | 0.00 USD | `+28.62%` | `1,567.00` |
| `Live` | `Short` | `1.62` | 5,940,000.00 USD | 1,300.00 USD | 0.00 USD | `+29.42%` | `798.00` |
| `Live` | `Short` | `1.64` | 5,950,000.00 USD | 7,750.00 USD | 0.00 USD | `+30.22%` | `4,742.00` |
| `Live` | `Short` | `1.65` | 5,950,000.00 USD | 233.59 USD | 0.00 USD | `+31.01%` | `142.00` |
| `Live` | `Short` | `1.66` | 5,950,000.00 USD | 147.30 USD | 0.00 USD | `+31.81%` | `89.00` |
| `Live` | `Short` | `1.67` | 5,950,000.00 USD | 586.08 USD | 0.00 USD | `+32.61%` | `352.00` |
| `Live` | `Short` | `1.68` | 5,960,000.00 USD | 5,020.00 USD | 0.00 USD | `+33.40%` | `3,000.00` |
| `Live` | `Short` | `1.69` | 5,960,000.00 USD | 4,180.00 USD | 0.00 USD | `+34.20%` | `2,481.00` |
| `Live` | `Short` | `1.70` | 5,960,000.00 USD | 110.17 USD | 0.00 USD | `+35.00%` | `65.00` |
| `Live` | `Short` | `1.71` | 5,960,000.00 USD | 1,980.00 USD | 0.00 USD | `+35.79%` | `1,163.00` |
| `Live` | `Short` | `1.72` | 5,960,000.00 USD | 1,100.00 USD | 0.00 USD | `+36.59%` | `642.00` |
| `Live` | `Short` | `1.74` | 5,970,000.00 USD | 2,970.00 USD | 0.00 USD | `+38.18%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 6,080,000.00 USD | 113,500.00 USD | 0.00 USD | `+38.98%` | `65,043.00` |
| `Live` | `Short` | `1.75` | 6,080,000.00 USD | 591.43 USD | 0.00 USD | `+39.77%` | `337.00` |
| `Live` | `Short` | `1.76` | 6,080,000.00 USD | 808.37 USD | 0.00 USD | `+40.57%` | `458.00` |
| `Live` | `Short` | `1.77` | 11,540,000.00 USD | 5,450,000.00 USD | 0.00 USD | `+41.37%` | `3,073,224.00` |
| `Live` | `Short` | `1.78` | 11,670,000.00 USD | 130,160.00 USD | 0.00 USD | `+42.16%` | `72,921.00` |
| `Live` | `Short` | `1.79` | 11,670,000.00 USD | 6,020.00 USD | 0.00 USD | `+42.96%` | `3,354.00` |
| `Live` | `Short` | `1.80` | 11,670,000.00 USD | 889.87 USD | 0.00 USD | `+43.76%` | `493.00` |
| `Live` | `Short` | `1.81` | 11,670,000.00 USD | 1,750.00 USD | 0.00 USD | `+44.55%` | `963.00` |
| `Live` | `Short` | `1.82` | 11,670,000.00 USD | 260.98 USD | 0.00 USD | `+45.35%` | `143.00` |
| `Live` | `Short` | `1.83` | 11,710,000.00 USD | 32,740.00 USD | 0.00 USD | `+46.15%` | `17,842.00` |
| `Live` | `Short` | `1.84` | 11,720,000.00 USD | 9,340.00 USD | 0.00 USD | `+46.94%` | `5,061.00` |
| `Live` | `Short` | `1.85` | 11,720,000.00 USD | 428.50 USD | 0.00 USD | `+47.74%` | `231.00` |
| `Live` | `Short` | `1.86` | 11,720,000.00 USD | 2,010.00 USD | 0.00 USD | `+48.53%` | `1,079.00` |
| `Live` | `Short` | `1.88` | 14,610,000.00 USD | 2,890,000.00 USD | 0.00 USD | `+49.33%` | `1,540,696.00` |
| `Live` | `Short` | `1.90` | 14,920,000.00 USD | 309,780.00 USD | 0.00 USD | `+50.92%` | `163,470.00` |
| `Live` | `Short` | `1.91` | 14,920,000.00 USD | 373.38 USD | 0.00 USD | `+51.72%` | `196.00` |
| `Live` | `Short` | `1.92` | 14,920,000.00 USD | 1,410.00 USD | 0.00 USD | `+52.52%` | `737.00` |
| `Live` | `Short` | `1.95` | 14,920,000.00 USD | 844.13 USD | 0.00 USD | `+54.91%` | `434.00` |
| `Live` | `Short` | `1.96` | 14,920,000.00 USD | 293.25 USD | 0.00 USD | `+55.70%` | `150.00` |
| `Live` | `Short` | `1.97` | 15,150,000.00 USD | 227,560.00 USD | 0.00 USD | `+56.50%` | `115,806.00` |
| `Live` | `Short` | `1.98` | 15,150,000.00 USD | 651.75 USD | 0.00 USD | `+57.30%` | `330.00` |
| `Live` | `Short` | `2.00` | 15,150,000.00 USD | 701.75 USD | 0.00 USD | `+59.68%` | `350.00` |
| `Live` | `Short` | `2.02` | 15,150,000.00 USD | 679.06 USD | 0.00 USD | `+60.48%` | `337.00` |
| `Live` | `Short` | `2.02` | 15,150,000.00 USD | 178.20 USD | 0.00 USD | `+61.28%` | `88.00` |
| `Live` | `Short` | `2.04` | 17,600,000.00 USD | 2,450,000.00 USD | 0.00 USD | `+62.87%` | `1,196,222.00` |
| `Live` | `Short` | `2.06` | 17,600,000.00 USD | 460.50 USD | 0.00 USD | `+64.46%` | `223.00` |
| `Live` | `Short` | `2.08` | 17,600,000.00 USD | 124.50 USD | 0.00 USD | `+65.26%` | `60.00` |
| `Live` | `Short` | `2.08` | 17,600,000.00 USD | 548.36 USD | 0.00 USD | `+66.06%` | `263.00` |
| `Live` | `Short` | `2.10` | 18,020,000.00 USD | 419,330.00 USD | 0.00 USD | `+66.85%` | `200,158.00` |
| `Live` | `Short` | `2.10` | 18,020,000.00 USD | 294.70 USD | 0.00 USD | `+67.65%` | `140.00` |
| `Live` | `Short` | `2.12` | 18,040,000.00 USD | 23,880.00 USD | 0.00 USD | `+68.45%` | `11,293.00` |
| `Live` | `Short` | `2.12` | 18,290,000.00 USD | 249,280.00 USD | 0.00 USD | `+69.24%` | `117,308.00` |
| `Live` | `Short` | `2.15` | 18,290,000.00 USD | 631.42 USD | 0.00 USD | `+71.63%` | `293.00` |
| `Live` | `Short` | `2.17` | 18,340,000.00 USD | 52,120.00 USD | 0.00 USD | `+73.22%` | `23,965.00` |
| `Live` | `Short` | `2.19` | 18,340,000.00 USD | 201.02 USD | 0.00 USD | `+74.02%` | `92.00` |
| `Live` | `Short` | `2.21` | 18,350,000.00 USD | 2,230.00 USD | 0.00 USD | `+75.61%` | `1,011.00` |
| `Live` | `Short` | `2.23` | 18,430,000.00 USD | 82,330.00 USD | 0.00 USD | `+77.21%` | `37,001.00` |
| `Live` | `Short` | `2.23` | 18,430,000.00 USD | 102.81 USD | 0.00 USD | `+78.00%` | `46.00` |
| `Live` | `Short` | `2.25` | 18,430,000.00 USD | 103.27 USD | 0.00 USD | `+78.80%` | `46.00` |
| `Live` | `Short` | `2.25` | 18,440,000.00 USD | 11,280.00 USD | 0.00 USD | `+79.60%` | `5,000.00` |
| `Live` | `Short` | `2.27` | 18,440,000.00 USD | 122.31 USD | 0.00 USD | `+80.39%` | `54.00` |
| `Live` | `Short` | `2.29` | 18,440,000.00 USD | 142.29 USD | 0.00 USD | `+82.78%` | `62.00` |
| `Live` | `Short` | `2.31` | 18,440,000.00 USD | 106.03 USD | 0.00 USD | `+83.58%` | `46.00` |
| `Live` | `Short` | `2.31` | 18,490,000.00 USD | 44,930.00 USD | 0.00 USD | `+84.37%` | `19,409.00` |
| `Live` | `Short` | `2.33` | 18,490,000.00 USD | 144.15 USD | 0.00 USD | `+85.17%` | `62.00` |
| `Live` | `Short` | `2.33` | 18,570,000.00 USD | 82,210.00 USD | 0.00 USD | `+85.97%` | `35,206.00` |
| `Live` | `Short` | `2.35` | 18,570,000.00 USD | 1,320.00 USD | 0.00 USD | `+86.76%` | `562.00` |
| `Live` | `Short` | `2.35` | 18,580,000.00 USD | 11,910.00 USD | 0.00 USD | `+87.56%` | `5,057.00` |
| `Live` | `Short` | `2.38` | 18,600,000.00 USD | 20,890.00 USD | 0.00 USD | `+89.15%` | `8,796.00` |
| `Live` | `Short` | `2.38` | 18,600,000.00 USD | 477.00 USD | 0.00 USD | `+89.95%` | `200.00` |
| `Live` | `Short` | `2.40` | 18,700,000.00 USD | 96,030.00 USD | 0.00 USD | `+90.75%` | `40,095.00` |
| `Live` | `Short` | `2.42` | 18,700,000.00 USD | 678.62 USD | 0.00 USD | `+92.34%` | `281.00` |
| `Live` | `Short` | `2.42` | 18,700,000.00 USD | 654.75 USD | 0.00 USD | `+93.13%` | `270.00` |
| `Live` | `Short` | `2.44` | 18,720,000.00 USD | 24,350.00 USD | 0.00 USD | `+93.93%` | `10,000.00` |
| `Live` | `Short` | `2.44` | 22,430,000.00 USD | 3,700,000.00 USD | 0.00 USD | `+94.73%` | `1,514,056.00` |
| `Live` | `Short` | `2.46` | 22,480,000.00 USD | 58,200.00 USD | 0.00 USD | `+95.52%` | `23,706.00` |
| `Live` | `Short` | `2.48` | 24,380,000.00 USD | 1,900,000.00 USD | 0.00 USD | `+97.91%` | `763,874.00` |
| `Live` | `Short` | `2.50` | 24,380,000.00 USD | 1,870.00 USD | 0.00 USD | `+98.71%` | `750.00` |
| `Live` | `Short` | `2.52` | 24,390,000.00 USD | 5,630.00 USD | 0.00 USD | `+100.30%` | `2,240.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 4,020,000.00 USD | 0.00 USD | 102.00 USD | `-79.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3650` | 4,020,000.00 USD | 0.00 USD | 351.50 USD | `-70.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 4,020,000.00 USD | 0.00 USD | 139.12 USD | `-70.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3950` | 4,020,000.00 USD | 0.00 USD | 2,880.00 USD | `-68.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4050` | 4,020,000.00 USD | 0.00 USD | 2,950.00 USD | `-67.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 4,020,000.00 USD | 0.00 USD | 408.51 USD | `-64.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 4,020,000.00 USD | 0.00 USD | 273.00 USD | `-63.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 4,020,000.00 USD | 0.00 USD | 151.12 USD | `-62.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 4,020,000.00 USD | 0.00 USD | 142.50 USD | `-62.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 4,020,000.00 USD | 0.00 USD | 145.50 USD | `-61.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4950` | 4,020,000.00 USD | 0.00 USD | 562.81 USD | `-60.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 4,020,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 4,020,000.00 USD | 0.00 USD | 285.82 USD | `-58.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 4,020,000.00 USD | 0.00 USD | 306.60 USD | `-58.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 4,020,000.00 USD | 0.00 USD | 121.55 USD | `-55.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 4,020,000.00 USD | 0.00 USD | 656.53 USD | `-55.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 4,010,000.00 USD | 0.00 USD | 100.62 USD | `-53.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 4,010,000.00 USD | 0.00 USD | 203.75 USD | `-50.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 4,010,000.00 USD | 0.00 USD | 791.85 USD | `-49.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 4,010,000.00 USD | 0.00 USD | 573.40 USD | `-48.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 4,010,000.00 USD | 0.00 USD | 244.31 USD | `-47.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 4,010,000.00 USD | 0.00 USD | 29,530.00 USD | `-47.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 3,980,000.00 USD | 0.00 USD | 503.55 USD | `-46.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 3,980,000.00 USD | 0.00 USD | 480.19 USD | `-45.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 3,980,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 3,970,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 3,970,000.00 USD | 0.00 USD | 228.80 USD | `-43.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 3,970,000.00 USD | 0.00 USD | 536.50 USD | `-42.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 3,970,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 3,970,000.00 USD | 0.00 USD | 2,880.00 USD | `-39.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 3,960,000.00 USD | 0.00 USD | 25,490.00 USD | `-36.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 3,940,000.00 USD | 0.00 USD | 2,310,000.00 USD | `-34.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 1,630,000.00 USD | 0.00 USD | 1,260.00 USD | `-31.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 1,630,000.00 USD | 0.00 USD | 690.38 USD | `-30.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 1,630,000.00 USD | 0.00 USD | 1,400.00 USD | `-29.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 1,630,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 1,620,000.00 USD | 0.00 USD | 838.94 USD | `-27.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 1,620,000.00 USD | 0.00 USD | 338.55 USD | `-27.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 1,620,000.00 USD | 0.00 USD | 1,840.00 USD | `-26.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 1,620,000.00 USD | 0.00 USD | 1,090.00 USD | `-25.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 1,620,000.00 USD | 0.00 USD | 112.46 USD | `-24.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 1,620,000.00 USD | 0.00 USD | 1,730.00 USD | `-23.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 1,620,000.00 USD | 0.00 USD | 4,010.00 USD | `-23.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 1,610,000.00 USD | 0.00 USD | 6,300.00 USD | `-22.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 1,610,000.00 USD | 0.00 USD | 4,890.00 USD | `-21.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 1,600,000.00 USD | 0.00 USD | 902.47 USD | `-20.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 1,600,000.00 USD | 0.00 USD | 45,660.00 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 1,550,000.00 USD | 0.00 USD | 4,760.00 USD | `-19.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 1,550,000.00 USD | 0.00 USD | 1,840.00 USD | `-18.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 1,550,000.00 USD | 0.00 USD | 48,180.00 USD | `-17.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 1,500,000.00 USD | 0.00 USD | 1,780.00 USD | `-16.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 1,500,000.00 USD | 0.00 USD | 23,530.00 USD | `-15.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,470,000.00 USD | 0.00 USD | 3,960.00 USD | `-15.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,470,000.00 USD | 0.00 USD | 48,460.00 USD | `-14.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,420,000.00 USD | 0.00 USD | 3,360.00 USD | `-13.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,420,000.00 USD | 0.00 USD | 16,830.00 USD | `-12.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 1,400,000.00 USD | 0.00 USD | 12,830.00 USD | `-11.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 1,390,000.00 USD | 0.00 USD | 9,780.00 USD | `-11.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 1,380,000.00 USD | 0.00 USD | 77,260.00 USD | `-10.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 1,300,000.00 USD | 0.00 USD | 13,380.00 USD | `-9.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 1,290,000.00 USD | 0.00 USD | 124,570.00 USD | `-8.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 1,160,000.00 USD | 0.00 USD | 58,820.00 USD | `-8.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 1,100,000.00 USD | 0.00 USD | 37,230.00 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 1,070,000.00 USD | 0.00 USD | 103,110.00 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 964,460.00 USD | 0.00 USD | 248,520.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 715,940.00 USD | 0.00 USD | 190,020.00 USD | `-4.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 525,920.00 USD | 0.00 USD | 138,380.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 387,540.00 USD | 0.00 USD | 28,670.00 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 358,880.00 USD | 0.00 USD | 115,990.00 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 242,890.00 USD | 0.00 USD | 59,190.00 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 183,700.00 USD | 0.00 USD | 145,000.00 USD | `-0.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 38,700.00 USD | 0.00 USD | 38,700.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 1,660.00 USD | 1,660.00 USD | 0.00 USD | `+0.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 57,270.00 USD | 55,620.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 365,440.00 USD | 308,160.00 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 408,880.00 USD | 43,440.00 USD | 0.00 USD | `+3.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 429,110.00 USD | 20,230.00 USD | 0.00 USD | `+3.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 1,040,000.00 USD | 611,420.00 USD | 0.00 USD | `+4.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,160,000.00 USD | 123,090.00 USD | 0.00 USD | `+5.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,210,000.00 USD | 43,890.00 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,270,000.00 USD | 65,480.00 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,290,000.00 USD | 14,640.00 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,540,000.00 USD | 249,090.00 USD | 0.00 USD | `+8.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,620,000.00 USD | 81,760.00 USD | 0.00 USD | `+9.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,670,000.00 USD | 55,590.00 USD | 0.00 USD | `+10.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,680,000.00 USD | 3,960.00 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 6,080,000.00 USD | 4,400,000.00 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 6,080,000.00 USD | 3,230.00 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 6,090,000.00 USD | 6,460.00 USD | 0.00 USD | `+13.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,090,000.00 USD | 1,450.00 USD | 0.00 USD | `+14.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,340,000.00 USD | 242,580.00 USD | 0.00 USD | `+15.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,340,000.00 USD | 7,510.00 USD | 0.00 USD | `+15.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,360,000.00 USD | 21,430.00 USD | 0.00 USD | `+16.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,470,000.00 USD | 108,020.00 USD | 0.00 USD | `+17.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,490,000.00 USD | 14,870.00 USD | 0.00 USD | `+18.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,510,000.00 USD | 17,790.00 USD | 0.00 USD | `+19.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,590,000.00 USD | 85,390.00 USD | 0.00 USD | `+19.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,600,000.00 USD | 11,760.00 USD | 0.00 USD | `+20.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,620,000.00 USD | 19,430.00 USD | 0.00 USD | `+21.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,670,000.00 USD | 45,620.00 USD | 0.00 USD | `+22.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,680,000.00 USD | 12,200.00 USD | 0.00 USD | `+23.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,680,000.00 USD | 2,380.00 USD | 0.00 USD | `+23.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,690,000.00 USD | 7,160.00 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,690,000.00 USD | 5,570.00 USD | 0.00 USD | `+25.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,710,000.00 USD | 10,570.00 USD | 0.00 USD | `+26.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,840,000.00 USD | 139,120.00 USD | 0.00 USD | `+27.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,850,000.00 USD | 1,840.00 USD | 0.00 USD | `+27.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 6,930,000.00 USD | 80,330.00 USD | 0.00 USD | `+28.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 6,930,000.00 USD | 464.75 USD | 0.00 USD | `+29.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,110,000.00 USD | 179,860.00 USD | 0.00 USD | `+30.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,110,000.00 USD | 2,670.00 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,190,000.00 USD | 85,010.00 USD | 0.00 USD | `+31.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,200,000.00 USD | 6,080.00 USD | 0.00 USD | `+32.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,220,000.00 USD | 18,400.00 USD | 0.00 USD | `+33.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,290,000.00 USD | 70,850.00 USD | 0.00 USD | `+34.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,310,000.00 USD | 18,000.00 USD | 0.00 USD | `+35.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,540,000.00 USD | 231,640.00 USD | 0.00 USD | `+35.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,550,000.00 USD | 14,250.00 USD | 0.00 USD | `+36.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,550,000.00 USD | 534.75 USD | 0.00 USD | `+37.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,600,000.00 USD | 43,240.00 USD | 0.00 USD | `+38.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,600,000.00 USD | 3,330.00 USD | 0.00 USD | `+38.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,610,000.00 USD | 9,200.00 USD | 0.00 USD | `+39.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,630,000.00 USD | 21,720.00 USD | 0.00 USD | `+40.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,760,000.00 USD | 126,830.00 USD | 0.00 USD | `+41.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,880,000.00 USD | 124,660.00 USD | 0.00 USD | `+42.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 7,890,000.00 USD | 3,980.00 USD | 0.00 USD | `+42.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 7,890,000.00 USD | 254.51 USD | 0.00 USD | `+43.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 7,900,000.00 USD | 11,080.00 USD | 0.00 USD | `+44.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 7,900,000.00 USD | 3,970.00 USD | 0.00 USD | `+45.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 7,910,000.00 USD | 8,170.00 USD | 0.00 USD | `+46.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 7,910,000.00 USD | 843.17 USD | 0.00 USD | `+46.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 7,920,000.00 USD | 8,390.00 USD | 0.00 USD | `+47.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 7,920,000.00 USD | 4,420.00 USD | 0.00 USD | `+49.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 7,920,000.00 USD | 591.89 USD | 0.00 USD | `+50.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 7,970,000.00 USD | 46,370.00 USD | 0.00 USD | `+50.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 7,980,000.00 USD | 9,270.00 USD | 0.00 USD | `+51.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 7,980,000.00 USD | 265.10 USD | 0.00 USD | `+54.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 7,980,000.00 USD | 2,040.00 USD | 0.00 USD | `+54.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 7,980,000.00 USD | 807.42 USD | 0.00 USD | `+55.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,000,000.00 USD | 14,120.00 USD | 0.00 USD | `+56.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,000,000.00 USD | 4,010.00 USD | 0.00 USD | `+57.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,000,000.00 USD | 325.54 USD | 0.00 USD | `+58.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,010,000.00 USD | 7,020.00 USD | 0.00 USD | `+58.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,190,000.00 USD | 184,840.00 USD | 0.00 USD | `+59.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,200,000.00 USD | 3,350.00 USD | 0.00 USD | `+61.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,200,000.00 USD | 181.12 USD | 0.00 USD | `+62.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,200,000.00 USD | 382.41 USD | 0.00 USD | `+62.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,200,000.00 USD | 3,420.00 USD | 0.00 USD | `+64.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,200,000.00 USD | 661.93 USD | 0.00 USD | `+65.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,330,000.00 USD | 124,400.00 USD | 0.00 USD | `+66.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,330,000.00 USD | 1,580.00 USD | 0.00 USD | `+67.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,340,000.00 USD | 13,900.00 USD | 0.00 USD | `+69.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,370,000.00 USD | 24,840.00 USD | 0.00 USD | `+70.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,420,000.00 USD | 50,580.00 USD | 0.00 USD | `+71.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,420,000.00 USD | 2,690.00 USD | 0.00 USD | `+72.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,420,000.00 USD | 2,180.00 USD | 0.00 USD | `+74.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,570,000.00 USD | 151,380.00 USD | 0.00 USD | `+76.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,580,000.00 USD | 2,230.00 USD | 0.00 USD | `+81.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,580,000.00 USD | 1,140.00 USD | 0.00 USD | `+81.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,590,000.00 USD | 11,670.00 USD | 0.00 USD | `+82.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,590,000.00 USD | 370.40 USD | 0.00 USD | `+84.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,590,000.00 USD | 733.19 USD | 0.00 USD | `+85.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,590,000.00 USD | 2,410.00 USD | 0.00 USD | `+88.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,590,000.00 USD | 475.00 USD | 0.00 USD | `+89.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,590,000.00 USD | 1,190.00 USD | 0.00 USD | `+89.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,600,000.00 USD | 2,540.00 USD | 0.00 USD | `+90.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,600,000.00 USD | 1,590.00 USD | 0.00 USD | `+91.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,600,000.00 USD | 1,370.00 USD | 0.00 USD | `+92.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,620,000.00 USD | 19,590.00 USD | 0.00 USD | `+93.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,620,000.00 USD | 564.92 USD | 0.00 USD | `+93.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,620,000.00 USD | 3,420.00 USD | 0.00 USD | `+97.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,620,000.00 USD | 124.75 USD | 0.00 USD | `+98.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,650,000.00 USD | 29,920.00 USD | 0.00 USD | `+99.51%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.07` | 99,290,000.00 USD | 0.00 USD | 99,290,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `1.09` | 99,290,000.00 USD | 0.00 USD | 99,290,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `1.09` | 99,250,000.00 USD | 0.00 USD | 99,250,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD |
| `7D` | `1.09` | 99,150,000.00 USD | 0.00 USD | 99,150,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD |
| `7D` | `1.10` | 99,110,000.00 USD | 0.00 USD | 99,110,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD |
| `7D` | `1.10` | 99,110,000.00 USD | 0.00 USD | 99,110,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD |
| `7D` | `1.10` | 98,820,000.00 USD | 0.00 USD | 98,820,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD |
| `7D` | `1.11` | 98,820,000.00 USD | 0.00 USD | 98,820,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD |
| `7D` | `1.11` | 98,820,000.00 USD | 0.00 USD | 98,820,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `7D` | `1.11` | 98,810,000.00 USD | 0.00 USD | 98,810,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD |
| `7D` | `1.12` | 98,760,000.00 USD | 0.00 USD | 98,760,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `7D` | `1.12` | 98,750,000.00 USD | 0.00 USD | 98,750,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `7D` | `1.12` | 98,670,000.00 USD | 0.00 USD | 98,670,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `1.12` | 91,100,000.00 USD | 0.00 USD | 91,100,000.00 USD | 21,900.00 USD | 43,210.00 USD | 161,640.00 USD |
| `7D` | `1.12` | 98,650,000.00 USD | 0.00 USD | 98,650,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.13` | 90,870,000.00 USD | 0.00 USD | 90,870,000.00 USD | 126,800.00 USD | 71,930.00 USD | 204,850.00 USD |
| `7D` | `1.13` | 98,430,000.00 USD | 0.00 USD | 98,430,000.00 USD | 0.00 USD | 53,430.00 USD | 94,670.00 USD |
| `1D` | `1.13` | 90,470,000.00 USD | 0.00 USD | 90,470,000.00 USD | 74,360.00 USD | 55,110.00 USD | 167,980.00 USD |
| `7D` | `1.13` | 98,290,000.00 USD | 0.00 USD | 98,290,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 90,170,000.00 USD | 0.00 USD | 90,170,000.00 USD | 7,580.00 USD | 113,140.00 USD | 240,710.00 USD |
| `7D` | `1.13` | 98,090,000.00 USD | 0.00 USD | 98,090,000.00 USD | 5,450.00 USD | 55,710.00 USD | 0.00 USD |
| `1D` | `1.13` | 89,810,000.00 USD | 0.00 USD | 89,810,000.00 USD | 5,520.00 USD | 58,610.00 USD | 243,160.00 USD |
| `7D` | `1.13` | 98,030,000.00 USD | 0.00 USD | 98,030,000.00 USD | 69,750.00 USD | 93,260.00 USD | 108,230.00 USD |
| `1D` | `1.13` | 89,500,000.00 USD | 0.00 USD | 89,500,000.00 USD | 91,470.00 USD | 71,570.00 USD | 115,470.00 USD |
| `7D` | `1.13` | 97,760,000.00 USD | 0.00 USD | 97,760,000.00 USD | 74,920.00 USD | 99,410.00 USD | 224,140.00 USD |
| `1D` | `1.14` | 89,220,000.00 USD | 0.00 USD | 89,220,000.00 USD | 42,870.00 USD | 153,950.00 USD | 114,290.00 USD |
| `7D` | `1.14` | 97,360,000.00 USD | 0.00 USD | 97,360,000.00 USD | 79,780.00 USD | 88,050.00 USD | 370,800.00 USD |
| `1D` | `1.14` | 88,910,000.00 USD | 0.00 USD | 88,910,000.00 USD | 38,180.00 USD | 18,330.00 USD | 49,660.00 USD |
| `7D` | `1.14` | 96,820,000.00 USD | 0.00 USD | 96,820,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 88,810,000.00 USD | 0.00 USD | 88,810,000.00 USD | 34,800.00 USD | 43,480.00 USD | 258,540.00 USD |
| `7D` | `1.14` | 96,790,000.00 USD | 0.00 USD | 96,790,000.00 USD | 39,170.00 USD | 54,580.00 USD | 250,970.00 USD |
| `1D` | `1.14` | 88,470,000.00 USD | 0.00 USD | 88,470,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.14` | 96,450,000.00 USD | 0.00 USD | 96,450,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD |
| `1D` | `1.14` | 88,400,000.00 USD | 0.00 USD | 88,400,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD |
| `7D` | `1.14` | 96,310,000.00 USD | 0.00 USD | 96,310,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `1D` | `1.15` | 88,270,000.00 USD | 0.00 USD | 88,270,000.00 USD | 0.00 USD | 75.47 USD | 0.00 USD |
| `7D` | `1.15` | 96,300,000.00 USD | 0.00 USD | 96,300,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `1D` | `1.15` | 88,270,000.00 USD | 0.00 USD | 88,270,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 96,240,000.00 USD | 0.00 USD | 96,240,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD |
| `7D` | `1.15` | 95,860,000.00 USD | 0.00 USD | 95,860,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.15` | 88,250,000.00 USD | 0.00 USD | 88,250,000.00 USD | 1,390.00 USD | 0.00 USD | 64,030.00 USD |
| `7D` | `1.15` | 95,710,000.00 USD | 0.00 USD | 95,710,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 88,180,000.00 USD | 0.00 USD | 88,180,000.00 USD | 73,200.00 USD | 45,870.00 USD | 263,680.00 USD |
| `7D` | `1.15` | 95,550,000.00 USD | 0.00 USD | 95,550,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `1D` | `1.16` | 87,800,000.00 USD | 0.00 USD | 87,800,000.00 USD | 20,480.00 USD | 25,320.00 USD | 82,910.00 USD |
| `7D` | `1.16` | 94,670,000.00 USD | 0.00 USD | 94,670,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 87,670,000.00 USD | 0.00 USD | 87,670,000.00 USD | 122,170.00 USD | 20,900.00 USD | 380,500.00 USD |
| `7D` | `1.16` | 94,430,000.00 USD | 0.00 USD | 94,430,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 87,150,000.00 USD | 0.00 USD | 87,150,000.00 USD | 185,400.00 USD | 53,000.00 USD | 142,740.00 USD |
| `7D` | `1.16` | 93,570,000.00 USD | 0.00 USD | 93,570,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 86,770,000.00 USD | 0.00 USD | 86,770,000.00 USD | 173,630.00 USD | 254,210.00 USD | 127,640.00 USD |
| `7D` | `1.16` | 92,480,000.00 USD | 0.00 USD | 92,480,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD |
| `1D` | `1.16` | 86,210,000.00 USD | 0.00 USD | 86,210,000.00 USD | 151,470.00 USD | 77,470.00 USD | 664,650.00 USD |
| `7D` | `1.16` | 91,190,000.00 USD | 0.00 USD | 91,190,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD |
| `1D` | `1.17` | 85,320,000.00 USD | 0.00 USD | 85,320,000.00 USD | 62,000.00 USD | 37,870.00 USD | 122,700.00 USD |
| `7D` | `1.17` | 89,520,000.00 USD | 0.00 USD | 89,520,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD |
| `1D` | `1.17` | 85,100,000.00 USD | 0.00 USD | 85,100,000.00 USD | 104,050.00 USD | 169,450.00 USD | 170,840.00 USD |
| `7D` | `1.17` | 88,180,000.00 USD | 0.00 USD | 88,180,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 84,650,000.00 USD | 0.00 USD | 84,650,000.00 USD | 152,210.00 USD | 19,750.00 USD | 358,690.00 USD |
| `7D` | `1.17` | 87,110,000.00 USD | 0.00 USD | 87,110,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 84,120,000.00 USD | 0.00 USD | 84,120,000.00 USD | 371,850.00 USD | 5,570.00 USD | 266,890.00 USD |
| `7D` | `1.17` | 85,070,000.00 USD | 0.00 USD | 85,070,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD |
| `1D` | `1.17` | 83,480,000.00 USD | 0.00 USD | 83,480,000.00 USD | 124,360.00 USD | 130,470.00 USD | 474,190.00 USD |
| `7D` | `1.17` | 83,870,000.00 USD | 0.00 USD | 83,870,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD |
| `1D` | `1.18` | 82,750,000.00 USD | 0.00 USD | 82,750,000.00 USD | 304,390.00 USD | 85,830.00 USD | 356,950.00 USD |
| `7D` | `1.18` | 82,300,000.00 USD | 0.00 USD | 82,300,000.00 USD | 181,850.00 USD | 71,240.00 USD | 372,750.00 USD |
| `1D` | `1.18` | 82,000,000.00 USD | 0.00 USD | 82,000,000.00 USD | 71,040.00 USD | 84,060.00 USD | 175,590.00 USD |
| `7D` | `1.18` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 85,020.00 USD | 50,740.00 USD | 483,980.00 USD |
| `1D` | `1.18` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 113,290.00 USD | 10,090.00 USD | 24,100.00 USD |
| `7D` | `1.18` | 81,050,000.00 USD | 0.00 USD | 81,050,000.00 USD | 267,580.00 USD | 112,520.00 USD | 200,920.00 USD |
| `1D` | `1.18` | 81,520,000.00 USD | 0.00 USD | 81,520,000.00 USD | 222,930.00 USD | 12,250.00 USD | 666,440.00 USD |
| `7D` | `1.18` | 80,470,000.00 USD | 0.00 USD | 80,470,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 80,620,000.00 USD | 0.00 USD | 80,620,000.00 USD | 196,910.00 USD | 70,210.00 USD | 143,880.00 USD |
| `7D` | `1.18` | 80,210,000.00 USD | 0.00 USD | 80,210,000.00 USD | 297,510.00 USD | 570,360.00 USD | 235,490.00 USD |
| `1D` | `1.19` | 80,210,000.00 USD | 0.00 USD | 80,210,000.00 USD | 86,540.00 USD | 513,570.00 USD | 65,030.00 USD |
| `7D` | `1.19` | 79,100,000.00 USD | 0.00 USD | 79,100,000.00 USD | 76,370.00 USD | 69,240.00 USD | 706,450.00 USD |
| `1D` | `1.19` | 79,550,000.00 USD | 0.00 USD | 79,550,000.00 USD | 365,260.00 USD | 93,190.00 USD | 1,570,000.00 USD |
| `7D` | `1.19` | 78,250,000.00 USD | 0.00 USD | 78,250,000.00 USD | 216,820.00 USD | 93,330.00 USD | 477,730.00 USD |
| `1D` | `1.19` | 77,520,000.00 USD | 0.00 USD | 77,520,000.00 USD | 110,600.00 USD | 50,600.00 USD | 319,610.00 USD |
| `7D` | `1.19` | 77,460,000.00 USD | 0.00 USD | 77,460,000.00 USD | 179,980.00 USD | 69,020.00 USD | 728,280.00 USD |
| `1D` | `1.19` | 77,040,000.00 USD | 0.00 USD | 77,040,000.00 USD | 147,820.00 USD | 203,910.00 USD | 469,390.00 USD |
| `7D` | `1.19` | 76,490,000.00 USD | 0.00 USD | 76,490,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD |
| `1D` | `1.19` | 76,220,000.00 USD | 0.00 USD | 76,220,000.00 USD | 190,850.00 USD | 424,970.00 USD | 1,690,000.00 USD |
| `7D` | `1.19` | 75,120,000.00 USD | 0.00 USD | 75,120,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD |
| `1D` | `1.20` | 73,910,000.00 USD | 0.00 USD | 73,910,000.00 USD | 784,530.00 USD | 116,250.00 USD | 1,220,000.00 USD |
| `7D` | `1.20` | 74,290,000.00 USD | 0.00 USD | 74,290,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD |
| `1D` | `1.20` | 71,790,000.00 USD | 0.00 USD | 71,790,000.00 USD | 273,620.00 USD | 836,790.00 USD | 663,320.00 USD |
| `7D` | `1.20` | 72,710,000.00 USD | 0.00 USD | 72,710,000.00 USD | 31,150.00 USD | 372,080.00 USD | 2,610,000.00 USD |
| `1D` | `1.20` | 70,020,000.00 USD | 0.00 USD | 70,020,000.00 USD | 866,770.00 USD | 476,370.00 USD | 2,580,000.00 USD |
| `7D` | `1.20` | 69,700,000.00 USD | 0.00 USD | 69,700,000.00 USD | 736,290.00 USD | 466,100.00 USD | 255,270.00 USD |
| `1D` | `1.20` | 66,100,000.00 USD | 0.00 USD | 66,100,000.00 USD | 215,570.00 USD | 255,940.00 USD | 985,010.00 USD |
| `7D` | `1.20` | 68,240,000.00 USD | 0.00 USD | 68,240,000.00 USD | 264,000.00 USD | 144,630.00 USD | 464,230.00 USD |
| `1D` | `1.20` | 64,640,000.00 USD | 0.00 USD | 64,640,000.00 USD | 567,590.00 USD | 566,300.00 USD | 551,700.00 USD |
| `7D` | `1.20` | 67,370,000.00 USD | 0.00 USD | 67,370,000.00 USD | 47,500.00 USD | 723,100.00 USD | 155,510.00 USD |
| `1D` | `1.21` | 62,960,000.00 USD | 0.00 USD | 62,960,000.00 USD | 403,550.00 USD | 552,170.00 USD | 591,790.00 USD |
| `7D` | `1.21` | 66,440,000.00 USD | 0.00 USD | 66,440,000.00 USD | 0.00 USD | 77,080.00 USD | 0.00 USD |
| `1D` | `1.21` | 61,410,000.00 USD | 0.00 USD | 61,410,000.00 USD | 1,700,000.00 USD | 314,740.00 USD | 1,900,000.00 USD |
| `7D` | `1.21` | 66,360,000.00 USD | 0.00 USD | 66,360,000.00 USD | 556,190.00 USD | 0.00 USD | 387,800.00 USD |
| `1D` | `1.21` | 57,490,000.00 USD | 0.00 USD | 57,490,000.00 USD | 625,020.00 USD | 429,390.00 USD | 1,310,000.00 USD |
| `7D` | `1.21` | 65,420,000.00 USD | 0.00 USD | 65,420,000.00 USD | 257,960.00 USD | 498,260.00 USD | 3,090,000.00 USD |
| `1D` | `1.21` | 55,130,000.00 USD | 0.00 USD | 55,130,000.00 USD | 1,520,000.00 USD | 655,080.00 USD | 1,430,000.00 USD |
| `7D` | `1.21` | 61,580,000.00 USD | 0.00 USD | 61,580,000.00 USD | 1,350,000.00 USD | 0.00 USD | 899,930.00 USD |
| `1D` | `1.21` | 51,520,000.00 USD | 0.00 USD | 51,520,000.00 USD | 30,610.00 USD | 182,450.00 USD | 1,100,000.00 USD |
| `7D` | `1.21` | 59,320,000.00 USD | 0.00 USD | 59,320,000.00 USD | 108,640.00 USD | 136,460.00 USD | 1,280,000.00 USD |
| `1D` | `1.22` | 50,210,000.00 USD | 0.00 USD | 50,210,000.00 USD | 226,520.00 USD | 196,610.00 USD | 1,170,000.00 USD |
| `7D` | `1.22` | 57,800,000.00 USD | 0.00 USD | 57,800,000.00 USD | 142,210.00 USD | 9,150.00 USD | 253,540.00 USD |
| `1D` | `1.22` | 48,620,000.00 USD | 0.00 USD | 48,620,000.00 USD | 143,650.00 USD | 0.00 USD | 243,580.00 USD |
| `7D` | `1.22` | 57,390,000.00 USD | 0.00 USD | 57,390,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD |
| `1D` | `1.22` | 48,230,000.00 USD | 0.00 USD | 48,230,000.00 USD | 222,150.00 USD | 101,950.00 USD | 4,090.00 USD |
| `7D` | `1.22` | 56,650,000.00 USD | 0.00 USD | 56,650,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD |
| `1D` | `1.22` | 47,900,000.00 USD | 0.00 USD | 47,900,000.00 USD | 113,990.00 USD | 273,720.00 USD | 446,620.00 USD |
| `7D` | `1.22` | 55,570,000.00 USD | 0.00 USD | 55,570,000.00 USD | 0.00 USD | 164,230.00 USD | 11,370.00 USD |
| `1D` | `1.22` | 47,070,000.00 USD | 0.00 USD | 47,070,000.00 USD | 256,850.00 USD | 0.00 USD | 2,640,000.00 USD |
| `7D` | `1.22` | 55,390,000.00 USD | 0.00 USD | 55,390,000.00 USD | 51,610.00 USD | 170,590.00 USD | 33,260.00 USD |
| `1D` | `1.23` | 44,170,000.00 USD | 0.00 USD | 44,170,000.00 USD | 567,980.00 USD | 800,860.00 USD | 996,900.00 USD |
| `7D` | `1.23` | 55,140,000.00 USD | 0.00 USD | 55,140,000.00 USD | 112,770.00 USD | 802,580.00 USD | 482,570.00 USD |
| `1D` | `1.23` | 41,800,000.00 USD | 0.00 USD | 41,800,000.00 USD | 542,470.00 USD | 764,560.00 USD | 587,330.00 USD |
| `7D` | `1.23` | 53,740,000.00 USD | 0.00 USD | 53,740,000.00 USD | 59,160.00 USD | 950,550.00 USD | 24,470.00 USD |
| `1D` | `1.23` | 39,910,000.00 USD | 0.00 USD | 39,910,000.00 USD | 306,680.00 USD | 1,030,000.00 USD | 3,390,000.00 USD |
| `7D` | `1.23` | 52,710,000.00 USD | 0.00 USD | 52,710,000.00 USD | 198,530.00 USD | 1,150,000.00 USD | 1,110,000.00 USD |
| `1D` | `1.23` | 35,180,000.00 USD | 0.00 USD | 35,180,000.00 USD | 1,280,000.00 USD | 1,360,000.00 USD | 3,910,000.00 USD |
| `7D` | `1.23` | 50,250,000.00 USD | 0.00 USD | 50,250,000.00 USD | 1,020,000.00 USD | 1,070,000.00 USD | 1,600,000.00 USD |
| `1D` | `1.23` | 28,620,000.00 USD | 0.00 USD | 28,620,000.00 USD | 513,930.00 USD | 1,230,000.00 USD | 1,950,000.00 USD |
| `7D` | `1.23` | 46,550,000.00 USD | 0.00 USD | 46,550,000.00 USD | 1,660,000.00 USD | 1,820,000.00 USD | 3,860,000.00 USD |
| `1D` | `1.24` | 24,930,000.00 USD | 0.00 USD | 24,930,000.00 USD | 280,110.00 USD | 1,040,000.00 USD | 1,300,000.00 USD |
| `7D` | `1.24` | 39,210,000.00 USD | 0.00 USD | 39,210,000.00 USD | 2,040,000.00 USD | 1,820,000.00 USD | 2,740,000.00 USD |
| `1D` | `1.24` | 22,310,000.00 USD | 0.00 USD | 22,310,000.00 USD | 1,040,000.00 USD | 685,750.00 USD | 2,080,000.00 USD |
| `7D` | `1.24` | 32,610,000.00 USD | 0.00 USD | 32,610,000.00 USD | 2,870,000.00 USD | 2,120,000.00 USD | 4,430,000.00 USD |
| `1D` | `1.24` | 18,500,000.00 USD | 0.00 USD | 18,500,000.00 USD | 765,930.00 USD | 715,020.00 USD | 2,330,000.00 USD |
| `7D` | `1.24` | 23,180,000.00 USD | 0.00 USD | 23,180,000.00 USD | 2,070,000.00 USD | 1,220,000.00 USD | 1,280,000.00 USD |
| `1D` | `1.24` | 14,690,000.00 USD | 0.00 USD | 14,690,000.00 USD | 505,370.00 USD | 1,090,000.00 USD | 1,500,000.00 USD |
| `7D` | `1.24` | 18,600,000.00 USD | 0.00 USD | 18,600,000.00 USD | 1,130,000.00 USD | 510,590.00 USD | 1,080,000.00 USD |
| `1D` | `1.24` | 11,590,000.00 USD | 0.00 USD | 11,590,000.00 USD | 1,860,000.00 USD | 526,050.00 USD | 3,040,000.00 USD |
| `7D` | `1.24` | 15,880,000.00 USD | 0.00 USD | 15,880,000.00 USD | 1,420,000.00 USD | 232,940.00 USD | 1,550,000.00 USD |
| `1D` | `1.25` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 1,170,000.00 USD | 437,530.00 USD | 895,030.00 USD |
| `7D` | `1.25` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 3,770,000.00 USD | 337,070.00 USD | 2,290,000.00 USD |
| `1D` | `1.25` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 225,570.00 USD | 1,170,000.00 USD | 1,990,000.00 USD |
| `7D` | `1.25` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 1,630,000.00 USD | 325,530.00 USD | 3,600,000.00 USD |
| `1D` | `1.25` | 273,850.00 USD | 0.00 USD | 273,850.00 USD | 0.00 USD | 3,250.00 USD | 0.00 USD |
| `7D` | `1.25` | 732,000.00 USD | 0.00 USD | 732,000.00 USD | 489,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 270,590.00 USD | 0.00 USD | 270,590.00 USD | 0.00 USD | 3,930.00 USD | 0.00 USD |
| `1D` | `1.25` | 266,660.00 USD | 0.00 USD | 266,660.00 USD | 0.00 USD | 6,330.00 USD | 0.00 USD |
| `7D` | `1.25` | 242,310.00 USD | 0.00 USD | 242,310.00 USD | 63,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 260,330.00 USD | 0.00 USD | 260,330.00 USD | 0.00 USD | 18,300.00 USD | 242,040.00 USD |
| `7D` | `1.26` | 178,660.00 USD | 0.00 USD | 178,660.00 USD | 150,010.00 USD | 8,810.00 USD | 0.00 USD |
| `7D` | `1.26` | 19,840.00 USD | 0.00 USD | 19,840.00 USD | 0.00 USD | 19,840.00 USD | 0.00 USD |
| `1D` | `1.26` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.26` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 13,580.00 USD | 13,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,580.00 USD |
| `7D` | `1.26` | 92,460.00 USD | 92,460.00 USD | 0.00 USD | 0.00 USD | 10,110.00 USD | 82,350.00 USD |
| `1D` | `1.26` | 398,690.00 USD | 398,690.00 USD | 0.00 USD | 229,640.00 USD | 98,730.00 USD | 56,740.00 USD |
| `7D` | `1.26` | 240,010.00 USD | 240,010.00 USD | 0.00 USD | 144,170.00 USD | 3,390.00 USD | 0.00 USD |
| `1D` | `1.26` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 580,850.00 USD | 431,450.00 USD | 1,560,000.00 USD |
| `7D` | `1.26` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 542,940.00 USD | 1,020,000.00 USD |
| `1D` | `1.27` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 1,130,000.00 USD | 347,350.00 USD | 381,140.00 USD |
| `7D` | `1.27` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 4,260,000.00 USD | 9,150.00 USD | 20,550.00 USD |
| `1D` | `1.27` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 424,040.00 USD | 1,420,000.00 USD | 487,620.00 USD |
| `7D` | `1.27` | 11,070,000.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 1,870,000.00 USD | 3,110,000.00 USD |
| `1D` | `1.27` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 1,080,000.00 USD | 1,490,000.00 USD | 4,000,000.00 USD |
| `7D` | `1.27` | 15,860,000.00 USD | 15,860,000.00 USD | 0.00 USD | 138,500.00 USD | 2,750,000.00 USD | 1,900,000.00 USD |
| `1D` | `1.27` | 17,630,000.00 USD | 17,630,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,030,000.00 USD | 1,490,000.00 USD |
| `7D` | `1.27` | 23,950,000.00 USD | 23,950,000.00 USD | 0.00 USD | 1,680,000.00 USD | 4,950,000.00 USD | 1,450,000.00 USD |
| `1D` | `1.27` | 24,730,000.00 USD | 24,730,000.00 USD | 0.00 USD | 1,040,000.00 USD | 2,080,000.00 USD | 3,970,000.00 USD |
| `7D` | `1.27` | 40,190,000.00 USD | 40,190,000.00 USD | 0.00 USD | 2,710,000.00 USD | 2,870,000.00 USD | 10,660,000.00 USD |
| `1D` | `1.28` | 32,340,000.00 USD | 32,340,000.00 USD | 0.00 USD | 1,650,000.00 USD | 2,110,000.00 USD | 3,860,000.00 USD |
| `7D` | `1.28` | 55,060,000.00 USD | 55,060,000.00 USD | 0.00 USD | 5,150,000.00 USD | 3,080,000.00 USD | 6,640,000.00 USD |
| `1D` | `1.28` | 42,420,000.00 USD | 42,420,000.00 USD | 0.00 USD | 3,810,000.00 USD | 1,540,000.00 USD | 4,710,000.00 USD |
| `7D` | `1.28` | 74,210,000.00 USD | 74,210,000.00 USD | 0.00 USD | 7,780,000.00 USD | 3,760,000.00 USD | 7,620,000.00 USD |
| `1D` | `1.28` | 47,740,000.00 USD | 47,740,000.00 USD | 0.00 USD | 373,090.00 USD | 2,040,000.00 USD | 2,900,000.00 USD |
| `7D` | `1.28` | 77,310,000.00 USD | 77,310,000.00 USD | 0.00 USD | 0.00 USD | 1,700,000.00 USD | 1,400,000.00 USD |
| `1D` | `1.28` | 51,530,000.00 USD | 51,530,000.00 USD | 0.00 USD | 943,390.00 USD | 365,080.00 USD | 2,480,000.00 USD |
| `7D` | `1.28` | 79,340,000.00 USD | 79,340,000.00 USD | 0.00 USD | 1,030,000.00 USD | 139,170.00 USD | 861,600.00 USD |
| `1D` | `1.28` | 54,490,000.00 USD | 54,490,000.00 USD | 0.00 USD | 1,160,000.00 USD | 501,060.00 USD | 1,310,000.00 USD |
| `7D` | `1.28` | 82,920,000.00 USD | 82,920,000.00 USD | 0.00 USD | 1,100,000.00 USD | 1,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `1.29` | 58,400,000.00 USD | 58,400,000.00 USD | 0.00 USD | 774,140.00 USD | 1,040,000.00 USD | 2,090,000.00 USD |
| `7D` | `1.29` | 87,500,000.00 USD | 87,500,000.00 USD | 0.00 USD | 796,960.00 USD | 1,300,000.00 USD | 2,480,000.00 USD |
| `1D` | `1.29` | 60,240,000.00 USD | 60,240,000.00 USD | 0.00 USD | 787,490.00 USD | 453,410.00 USD | 591,760.00 USD |
| `7D` | `1.29` | 88,220,000.00 USD | 88,220,000.00 USD | 0.00 USD | 685,300.00 USD | 2,730.00 USD | 33,260.00 USD |
| `1D` | `1.29` | 61,060,000.00 USD | 61,060,000.00 USD | 0.00 USD | 156,280.00 USD | 211,020.00 USD | 456,570.00 USD |
| `7D` | `1.29` | 89,830,000.00 USD | 89,830,000.00 USD | 0.00 USD | 70,460.00 USD | 277,240.00 USD | 1,260,000.00 USD |
| `1D` | `1.29` | 64,390,000.00 USD | 64,390,000.00 USD | 0.00 USD | 378,690.00 USD | 236,430.00 USD | 2,720,000.00 USD |
| `7D` | `1.29` | 92,420,000.00 USD | 92,420,000.00 USD | 0.00 USD | 1,040,000.00 USD | 202,640.00 USD | 1,350,000.00 USD |
| `1D` | `1.29` | 68,660,000.00 USD | 68,660,000.00 USD | 0.00 USD | 1,170,000.00 USD | 372,720.00 USD | 2,730,000.00 USD |
| `7D` | `1.29` | 96,070,000.00 USD | 96,070,000.00 USD | 0.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD |
| `1D` | `1.30` | 73,940,000.00 USD | 73,940,000.00 USD | 0.00 USD | 1,460,000.00 USD | 1,240,000.00 USD | 2,570,000.00 USD |
| `7D` | `1.30` | 103,360,000.00 USD | 103,360,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD |
| `1D` | `1.30` | 75,090,000.00 USD | 75,090,000.00 USD | 0.00 USD | 473,750.00 USD | 22,860.00 USD | 653,440.00 USD |
| `7D` | `1.30` | 105,310,000.00 USD | 105,310,000.00 USD | 0.00 USD | 25,800.00 USD | 172,080.00 USD | 1,750,000.00 USD |
| `1D` | `1.30` | 76,870,000.00 USD | 76,870,000.00 USD | 0.00 USD | 361,100.00 USD | 397,510.00 USD | 1,030,000.00 USD |
| `7D` | `1.30` | 107,680,000.00 USD | 107,680,000.00 USD | 0.00 USD | 208,510.00 USD | 434,510.00 USD | 1,730,000.00 USD |
| `1D` | `1.30` | 79,580,000.00 USD | 79,580,000.00 USD | 0.00 USD | 804,300.00 USD | 719,080.00 USD | 1,190,000.00 USD |
| `7D` | `1.30` | 108,710,000.00 USD | 108,710,000.00 USD | 0.00 USD | 85,960.00 USD | 944,610.00 USD | 0.00 USD |
| `1D` | `1.30` | 80,960,000.00 USD | 80,960,000.00 USD | 0.00 USD | 407,960.00 USD | 308,370.00 USD | 660,580.00 USD |
| `7D` | `1.30` | 111,510,000.00 USD | 111,510,000.00 USD | 0.00 USD | 0.00 USD | 2,170,000.00 USD | 635,640.00 USD |
| `1D` | `1.31` | 82,730,000.00 USD | 82,730,000.00 USD | 0.00 USD | 568,970.00 USD | 524,060.00 USD | 674,130.00 USD |
| `7D` | `1.31` | 113,520,000.00 USD | 113,520,000.00 USD | 0.00 USD | 1,770,000.00 USD | 238,140.00 USD | 0.00 USD |
| `1D` | `1.31` | 86,310,000.00 USD | 86,310,000.00 USD | 0.00 USD | 934,360.00 USD | 464,600.00 USD | 2,190,000.00 USD |
| `7D` | `1.31` | 118,690,000.00 USD | 118,690,000.00 USD | 0.00 USD | 1,550,000.00 USD | 821,310.00 USD | 2,790,000.00 USD |
| `1D` | `1.31` | 89,590,000.00 USD | 89,590,000.00 USD | 0.00 USD | 1,240,000.00 USD | 300,820.00 USD | 1,730,000.00 USD |
| `7D` | `1.31` | 121,100,000.00 USD | 121,100,000.00 USD | 0.00 USD | 1,340,000.00 USD | 414,180.00 USD | 647,870.00 USD |
| `1D` | `1.31` | 92,180,000.00 USD | 92,180,000.00 USD | 0.00 USD | 928,510.00 USD | 636,370.00 USD | 1,030,000.00 USD |
| `7D` | `1.31` | 125,970,000.00 USD | 125,970,000.00 USD | 0.00 USD | 189,510.00 USD | 858,660.00 USD | 3,830,000.00 USD |
| `1D` | `1.31` | 93,750,000.00 USD | 93,750,000.00 USD | 0.00 USD | 520,400.00 USD | 157,870.00 USD | 891,380.00 USD |
| `7D` | `1.31` | 127,260,000.00 USD | 127,260,000.00 USD | 0.00 USD | 638,380.00 USD | 151,320.00 USD | 501,780.00 USD |
| `1D` | `1.32` | 96,850,000.00 USD | 96,850,000.00 USD | 0.00 USD | 190,130.00 USD | 636,220.00 USD | 2,270,000.00 USD |
| `7D` | `1.32` | 131,980,000.00 USD | 131,980,000.00 USD | 0.00 USD | 68,520.00 USD | 1,890,000.00 USD | 2,760,000.00 USD |
| `1D` | `1.32` | 103,360,000.00 USD | 103,360,000.00 USD | 0.00 USD | 1,980,000.00 USD | 826,670.00 USD | 3,700,000.00 USD |
| `7D` | `1.32` | 137,080,000.00 USD | 137,080,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 3,080,000.00 USD |
| `1D` | `1.32` | 105,970,000.00 USD | 105,970,000.00 USD | 0.00 USD | 1,370,000.00 USD | 309,290.00 USD | 926,390.00 USD |
| `7D` | `1.32` | 139,100,000.00 USD | 139,100,000.00 USD | 0.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 109,070,000.00 USD | 109,070,000.00 USD | 0.00 USD | 1,160,000.00 USD | 702,830.00 USD | 1,240,000.00 USD |
| `7D` | `1.32` | 142,460,000.00 USD | 142,460,000.00 USD | 0.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 110,850,000.00 USD | 110,850,000.00 USD | 0.00 USD | 867,870.00 USD | 63,660.00 USD | 851,430.00 USD |
| `7D` | `1.32` | 145,240,000.00 USD | 145,240,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD |
| `1D` | `1.33` | 111,890,000.00 USD | 111,890,000.00 USD | 0.00 USD | 405,790.00 USD | 55,140.00 USD | 578,770.00 USD |
| `7D` | `1.33` | 147,040,000.00 USD | 147,040,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 113,100,000.00 USD | 113,100,000.00 USD | 0.00 USD | 545,530.00 USD | 171,300.00 USD | 494,230.00 USD |
| `7D` | `1.33` | 148,140,000.00 USD | 148,140,000.00 USD | 0.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 114,800,000.00 USD | 114,800,000.00 USD | 0.00 USD | 729,070.00 USD | 103,810.00 USD | 862,480.00 USD |
| `7D` | `1.33` | 149,850,000.00 USD | 149,850,000.00 USD | 0.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 116,620,000.00 USD | 116,620,000.00 USD | 0.00 USD | 465,720.00 USD | 181,920.00 USD | 1,180,000.00 USD |
| `7D` | `1.33` | 152,320,000.00 USD | 152,320,000.00 USD | 0.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD |
| `1D` | `1.33` | 118,480,000.00 USD | 118,480,000.00 USD | 0.00 USD | 783,210.00 USD | 229,200.00 USD | 838,970.00 USD |
| `7D` | `1.33` | 154,350,000.00 USD | 154,350,000.00 USD | 0.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD |
| `1D` | `1.34` | 119,590,000.00 USD | 119,590,000.00 USD | 0.00 USD | 286,040.00 USD | 206,950.00 USD | 616,920.00 USD |
| `7D` | `1.34` | 155,890,000.00 USD | 155,890,000.00 USD | 0.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 120,120,000.00 USD | 120,120,000.00 USD | 0.00 USD | 289,820.00 USD | 80,670.00 USD | 164,110.00 USD |
| `7D` | `1.34` | 158,330,000.00 USD | 158,330,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 120,980,000.00 USD | 120,980,000.00 USD | 0.00 USD | 347,480.00 USD | 138,400.00 USD | 373,260.00 USD |
| `7D` | `1.34` | 160,190,000.00 USD | 160,190,000.00 USD | 0.00 USD | 804,660.00 USD | 463,950.00 USD | 588,220.00 USD |
| `1D` | `1.34` | 122,380,000.00 USD | 122,380,000.00 USD | 0.00 USD | 755,550.00 USD | 209,760.00 USD | 430,320.00 USD |
| `7D` | `1.34` | 165,650,000.00 USD | 165,650,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,430,000.00 USD | 660,660.00 USD |
| `1D` | `1.34` | 123,940,000.00 USD | 123,940,000.00 USD | 0.00 USD | 620,540.00 USD | 350,020.00 USD | 593,010.00 USD |
| `7D` | `1.34` | 172,780,000.00 USD | 172,780,000.00 USD | 0.00 USD | 2,000,000.00 USD | 1,890,000.00 USD | 3,240,000.00 USD |
| `1D` | `1.35` | 124,690,000.00 USD | 124,690,000.00 USD | 0.00 USD | 274,120.00 USD | 119,670.00 USD | 353,100.00 USD |
| `7D` | `1.35` | 181,030,000.00 USD | 181,030,000.00 USD | 0.00 USD | 3,270,000.00 USD | 1,640,000.00 USD | 3,350,000.00 USD |
| `1D` | `1.35` | 125,260,000.00 USD | 125,260,000.00 USD | 0.00 USD | 192,130.00 USD | 50,500.00 USD | 329,150.00 USD |
| `7D` | `1.35` | 188,780,000.00 USD | 188,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,820,000.00 USD | 3,160,000.00 USD |
| `1D` | `1.35` | 125,610,000.00 USD | 125,610,000.00 USD | 0.00 USD | 177,170.00 USD | 30,950.00 USD | 146,530.00 USD |
| `7D` | `1.35` | 196,800,000.00 USD | 196,800,000.00 USD | 0.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD |
| `1D` | `1.35` | 125,890,000.00 USD | 125,890,000.00 USD | 0.00 USD | 69,740.00 USD | 28,460.00 USD | 174,610.00 USD |
| `7D` | `1.35` | 205,920,000.00 USD | 205,920,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 126,190,000.00 USD | 126,190,000.00 USD | 0.00 USD | 105,080.00 USD | 4,520.00 USD | 194,110.00 USD |
| `7D` | `1.35` | 212,670,000.00 USD | 212,670,000.00 USD | 0.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD |
| `1D` | `1.36` | 127,020,000.00 USD | 127,020,000.00 USD | 0.00 USD | 335,960.00 USD | 63,960.00 USD | 426,530.00 USD |
| `7D` | `1.36` | 219,010,000.00 USD | 219,010,000.00 USD | 0.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD |
| `1D` | `1.36` | 127,520,000.00 USD | 127,520,000.00 USD | 0.00 USD | 148,530.00 USD | 43,910.00 USD | 310,320.00 USD |
| `7D` | `1.36` | 221,550,000.00 USD | 221,550,000.00 USD | 0.00 USD | 1,060,000.00 USD | 639,580.00 USD | 837,310.00 USD |
| `1D` | `1.36` | 128,070,000.00 USD | 128,070,000.00 USD | 0.00 USD | 269,010.00 USD | 49,930.00 USD | 234,460.00 USD |
| `7D` | `1.36` | 224,420,000.00 USD | 224,420,000.00 USD | 0.00 USD | 1,380,000.00 USD | 282,890.00 USD | 1,210,000.00 USD |
| `1D` | `1.36` | 128,610,000.00 USD | 128,610,000.00 USD | 0.00 USD | 143,090.00 USD | 115,970.00 USD | 276,810.00 USD |
| `7D` | `1.36` | 228,030,000.00 USD | 228,030,000.00 USD | 0.00 USD | 1,480,000.00 USD | 711,020.00 USD | 1,420,000.00 USD |
| `1D` | `1.36` | 128,710,000.00 USD | 128,710,000.00 USD | 0.00 USD | 78,610.00 USD | 12,970.00 USD | 6,070.00 USD |
| `7D` | `1.36` | 230,770,000.00 USD | 230,770,000.00 USD | 0.00 USD | 1,420,000.00 USD | 616,140.00 USD | 698,940.00 USD |
| `1D` | `1.37` | 128,970,000.00 USD | 128,970,000.00 USD | 0.00 USD | 56,040.00 USD | 912.76 USD | 206,760.00 USD |
| `7D` | `1.37` | 231,590,000.00 USD | 231,590,000.00 USD | 0.00 USD | 206,650.00 USD | 189,790.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 129,200,000.00 USD | 129,200,000.00 USD | 0.00 USD | 97,000.00 USD | 109,100.00 USD | 29,680.00 USD |
| `7D` | `1.37` | 232,640,000.00 USD | 232,640,000.00 USD | 0.00 USD | 486,840.00 USD | 176,380.00 USD | 389,280.00 USD |
| `1D` | `1.37` | 129,220,000.00 USD | 129,220,000.00 USD | 0.00 USD | 0.00 USD | 10,920.00 USD | 0.00 USD |
| `7D` | `1.37` | 233,950,000.00 USD | 233,950,000.00 USD | 0.00 USD | 367,350.00 USD | 211,750.00 USD | 733,820.00 USD |
| `1D` | `1.37` | 129,340,000.00 USD | 129,340,000.00 USD | 0.00 USD | 5,340.00 USD | 29,920.00 USD | 88,420.00 USD |
| `7D` | `1.37` | 235,180,000.00 USD | 235,180,000.00 USD | 0.00 USD | 393,010.00 USD | 171,680.00 USD | 667,760.00 USD |
| `1D` | `1.37` | 129,420,000.00 USD | 129,420,000.00 USD | 0.00 USD | 5,470.00 USD | 1,890.00 USD | 71,880.00 USD |
| `7D` | `1.37` | 236,850,000.00 USD | 236,850,000.00 USD | 0.00 USD | 563,840.00 USD | 386,690.00 USD | 717,890.00 USD |
| `1D` | `1.38` | 129,820,000.00 USD | 129,820,000.00 USD | 0.00 USD | 126,800.00 USD | 71,930.00 USD | 204,850.00 USD |
| `7D` | `1.38` | 237,880,000.00 USD | 237,880,000.00 USD | 0.00 USD | 242,030.00 USD | 273,360.00 USD | 514,140.00 USD |
| `1D` | `1.38` | 130,120,000.00 USD | 130,120,000.00 USD | 0.00 USD | 74,360.00 USD | 55,110.00 USD | 167,980.00 USD |
| `7D` | `1.38` | 239,340,000.00 USD | 239,340,000.00 USD | 0.00 USD | 692,200.00 USD | 267,730.00 USD | 499,710.00 USD |
| `1D` | `1.38` | 130,300,000.00 USD | 130,300,000.00 USD | 0.00 USD | 2,320.00 USD | 47,610.00 USD | 130,700.00 USD |
| `7D` | `1.38` | 241,040,000.00 USD | 241,040,000.00 USD | 0.00 USD | 436,360.00 USD | 195,830.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 130,480,000.00 USD | 130,480,000.00 USD | 0.00 USD | 5,270.00 USD | 65,520.00 USD | 110,010.00 USD |
| `7D` | `1.38` | 242,900,000.00 USD | 242,900,000.00 USD | 0.00 USD | 710,620.00 USD | 348,810.00 USD | 802,530.00 USD |
| `1D` | `1.38` | 130,790,000.00 USD | 130,790,000.00 USD | 0.00 USD | 5,520.00 USD | 58,610.00 USD | 243,160.00 USD |
| `7D` | `1.38` | 243,790,000.00 USD | 243,790,000.00 USD | 0.00 USD | 403,730.00 USD | 253,120.00 USD | 228,560.00 USD |
| `1D` | `1.39` | 131,070,000.00 USD | 131,070,000.00 USD | 0.00 USD | 91,470.00 USD | 71,570.00 USD | 115,470.00 USD |
| `7D` | `1.39` | 244,820,000.00 USD | 244,820,000.00 USD | 0.00 USD | 377,810.00 USD | 234,230.00 USD | 413,510.00 USD |
| `1D` | `1.39` | 131,380,000.00 USD | 131,380,000.00 USD | 0.00 USD | 42,870.00 USD | 153,950.00 USD | 114,290.00 USD |
| `7D` | `1.39` | 246,030,000.00 USD | 246,030,000.00 USD | 0.00 USD | 384,080.00 USD | 308,280.00 USD | 518,070.00 USD |
| `1D` | `1.39` | 131,480,000.00 USD | 131,480,000.00 USD | 0.00 USD | 38,180.00 USD | 18,330.00 USD | 49,660.00 USD |
| `7D` | `1.39` | 246,780,000.00 USD | 246,780,000.00 USD | 0.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD |
| `7D` | `1.39` | 247,310,000.00 USD | 247,310,000.00 USD | 0.00 USD | 82,350.00 USD | 90,970.00 USD | 358,080.00 USD |
| `7D` | `1.39` | 247,470,000.00 USD | 247,470,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 101,420.00 USD |
| `7D` | `1.40` | 247,690,000.00 USD | 247,690,000.00 USD | 0.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD |
| `7D` | `1.40` | 247,700,000.00 USD | 247,700,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 247,760,000.00 USD | 247,760,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 247,840,000.00 USD | 247,840,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `7D` | `1.40` | 248,140,000.00 USD | 248,140,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 248,290,000.00 USD | 248,290,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.41` | 248,430,000.00 USD | 248,430,000.00 USD | 0.00 USD | 4,390.00 USD | 15,880.00 USD | 120,660.00 USD |
| `7D` | `1.41` | 248,710,000.00 USD | 248,710,000.00 USD | 0.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.84B` | Total OI Tokens: `2,256,869,433.5 XRP`
  * 1h OI Change: `+0.43%` | 4h OI Change: `+0.58%` | 24h OI Change: `-4.52%`
  * Exchange Breakdown: Binance=`428.47M` | Bybit=`323.61M` | OKX=`96.35M` | Hyperliquid=`201.27M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-67.23K` | Last 24h: `21.94K` | Last 3d: `414.05K` | Last 7d: `1.06M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0082%` | **USDT OKX** | `-0.0154%` |
| **USDT Bybit** | `-0.0284%` | **USDT KuCoin** | `-0.0105%` |
| **USDT MEXC** | `0.0081%` | **USDT BingX** | `0.0083%` |
| **USDT Gate** | `-0.0015%` | **USDT Bitget** | `-0.0065%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0028%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `50.11%` | `49.89%` | `1.00` | 477,760,000.00 USD |
| `15M` | `Binance` | `44.39%` | `55.61%` | `0.80` | 123,060,000.00 USD |
| `15M` | `OKX` | `51.23%` | `48.77%` | `1.05` | 76,830,000.00 USD |
| `15M` | `Bybit` | `56.47%` | `43.53%` | `1.30` | 53,960,000.00 USD |
| `15M` | `KuCoin` | `63.55%` | `36.45%` | `1.74` | 1,670,000.00 USD |
| `15M` | `Gate` | `54.78%` | `45.22%` | `1.21` | 42,090,000.00 USD |
| `15M` | `Bitget` | `52.04%` | `47.96%` | `1.09` | 17,740,000.00 USD |
| `15M` | `BingX` | `43.67%` | `56.33%` | `0.78` | 6,870,000.00 USD |
| `15M` | `MEXC` | `30.64%` | `69.36%` | `0.44` | 38,470,000.00 USD |
| `15M` | `Bitunix` | `60.62%` | `39.38%` | `1.54` | 28,520,000.00 USD |
| `15M` | `Hyperliquid` | `67.49%` | `32.51%` | `2.08` | 30,450,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `47.8%` | `52.2%` | `0.92` | 9,440,000.00 USD |
| `15M` | `Crypto.com` | `43.21%` | `56.79%` | `0.76` | 1,210,000.00 USD |
| `15M` | `WhiteBIT` | `35.49%` | `64.51%` | `0.55` | 4,820,000.00 USD |
| `15M` | `HTX` | `63.69%` | `36.31%` | `1.75` | 1,530,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `56.55%` | `43.45%` | `1.30` | 28,460,000.00 USD |
| `15M` | `Bitfinex` | `58.12%` | `41.88%` | `1.39` | 160,980.00 USD |
| `15M` | `Kraken` | `28.82%` | `71.18%` | `0.40` | 5,030,000.00 USD |
| `15M` | `Aster` | `45.18%` | `54.82%` | `0.82` | 2,900,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `50.13%` | `49.87%` | `1.01` | 4,530,000.00 USD |
| `15M` | `Whale Positions` | `44.39%` | `55.61%` | `0.80` | 123,060,000.00 USD |
| `15M` | `Global Accounts` | `50.11%` | `49.89%` | `1.00` | 477,760,000.00 USD |
| `1H` | `XRP` | `47.03%` | `52.97%` | `0.89` | 2,210,000,000.00 USD |
| `1H` | `Binance` | `43.98%` | `56.02%` | `0.79` | 588,100,000.00 USD |
| `1H` | `OKX` | `50.9%` | `49.1%` | `1.04` | 341,910,000.00 USD |
| `1H` | `Bybit` | `50.14%` | `49.86%` | `1.01` | 170,630,000.00 USD |
| `1H` | `KuCoin` | `54.41%` | `45.59%` | `1.19` | 5,880,000.00 USD |
| `1H` | `Gate` | `51.69%` | `48.31%` | `1.07` | 208,950,000.00 USD |
| `1H` | `Bitget` | `45.15%` | `54.85%` | `0.82` | 100,220,000.00 USD |
| `1H` | `BingX` | `45.78%` | `54.22%` | `0.84` | 40,170,000.00 USD |
| `1H` | `MEXC` | `38.48%` | `61.52%` | `0.63` | 121,730,000.00 USD |
| `1H` | `Bitunix` | `51.56%` | `48.44%` | `1.06` | 98,740,000.00 USD |
| `1H` | `Hyperliquid` | `28.41%` | `71.59%` | `0.40` | 145,590,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.94%` | `50.06%` | `1.00` | 174,380,000.00 USD |
| `1H` | `Crypto.com` | `43.66%` | `56.34%` | `0.77` | 7,490,000.00 USD |
| `1H` | `WhiteBIT` | `85.21%` | `14.79%` | `5.76` | 22,560,000.00 USD |
| `1H` | `HTX` | `49.59%` | `50.41%` | `0.98` | 9,160,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `55.14%` | `44.86%` | `1.23` | 119,360,000.00 USD |
| `1H` | `Bitfinex` | `40.45%` | `59.55%` | `0.68` | 870,200.00 USD |
| `1H` | `Kraken` | `51.4%` | `48.6%` | `1.06` | 15,460,000.00 USD |
| `1H` | `Aster` | `44.21%` | `55.79%` | `0.79` | 15,020,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.11%` | `47.89%` | `1.09` | 20,820,000.00 USD |
| `1H` | `Whale Positions` | `43.98%` | `56.02%` | `0.79` | 588,100,000.00 USD |
| `1H` | `Global Accounts` | `47.03%` | `52.97%` | `0.89` | 2,210,000,000.00 USD |
| `4H` | `XRP` | `45.85%` | `54.15%` | `0.85` | 9,640,000,000.00 USD |
| `4H` | `Binance` | `44%` | `56%` | `0.79` | 2,950,000,000.00 USD |
| `4H` | `OKX` | `47.51%` | `52.49%` | `0.91` | 1,400,000,000.00 USD |
| `4H` | `Bybit` | `45.51%` | `54.49%` | `0.84` | 834,650,000.00 USD |
| `4H` | `KuCoin` | `48.49%` | `51.51%` | `0.94` | 22,070,000.00 USD |
| `4H` | `Gate` | `49.76%` | `50.24%` | `0.99` | 982,710,000.00 USD |
| `4H` | `Bitget` | `45.47%` | `54.53%` | `0.83` | 447,010,000.00 USD |
| `4H` | `BingX` | `39.41%` | `60.59%` | `0.65` | 177,550,000.00 USD |
| `4H` | `MEXC` | `42.75%` | `57.25%` | `0.75` | 423,460,000.00 USD |
| `4H` | `Bitunix` | `45.72%` | `54.28%` | `0.84` | 368,140,000.00 USD |
| `4H` | `Hyperliquid` | `36.2%` | `63.8%` | `0.57` | 509,840,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.38%` | `49.62%` | `1.02` | 688,540,000.00 USD |
| `4H` | `Crypto.com` | `46.28%` | `53.72%` | `0.86` | 27,790,000.00 USD |
| `4H` | `WhiteBIT` | `45.77%` | `54.23%` | `0.84` | 119,630,000.00 USD |
| `4H` | `HTX` | `46.2%` | `53.8%` | `0.86` | 34,870,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `52.06%` | `47.94%` | `1.09` | 439,140,000.00 USD |
| `4H` | `Bitfinex` | `34.46%` | `65.54%` | `0.53` | 5,260,000.00 USD |
| `4H` | `Kraken` | `51.6%` | `48.4%` | `1.07` | 15,600,000.00 USD |
| `4H` | `Aster` | `51.38%` | `48.62%` | `1.06` | 85,510,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.48%` | `47.52%` | `1.10` | 113,880,000.00 USD |
| `4H` | `Whale Positions` | `44%` | `56%` | `0.79` | 2,950,000,000.00 USD |
| `4H` | `Global Accounts` | `45.85%` | `54.15%` | `0.85` | 9,640,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `1.27` | `1.27` | `1.27` | `1.27` | `1.26` | 12,144,743.65 USD | 6,990,191.91 USD | 5,154,551.74 USD | 1,835,640.16 USD | `+15.11%` | `14B / 14S` |
| `5:00 UTC` | `1.27` | `1.27` | `1.27` | `1.27` | `1.26` | 6,182,046.10 USD | 3,146,565.70 USD | 3,035,480.40 USD | 111,085.31 USD | `+1.80%` | `10B / 10S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.27` | `1.26` | 7,034,590.80 USD | 2,893,991.39 USD | 4,140,599.40 USD | -1,246,608.01 USD | `-17.72%` | `5B / 17S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 7,492,630.91 USD | 2,570,238.18 USD | 4,922,392.73 USD | -2,352,154.55 USD | `-31.39%` | `6B / 29S` |
| `0:00 UTC` | `1.26` | `1.25` | `1.26` | `1.26` | `1.25` | 16,486,336.19 USD | 7,622,620.76 USD | 8,863,715.43 USD | -1,241,094.67 USD | `-7.53%` | `10B / 24S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 8,615,974.43 USD | 3,921,066.30 USD | 4,694,908.13 USD | -773,841.83 USD | `-8.98%` | `6B / 4S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 8,443,326.41 USD | 4,197,283.82 USD | 4,246,042.59 USD | -48,758.76 USD | `-0.58%` | `16B / 5S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 7,390,743.66 USD | 4,309,267.00 USD | 3,081,476.65 USD | 1,227,790.35 USD | `+16.61%` | `9B / 4S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 5,021,258.97 USD | 2,177,548.60 USD | 2,843,710.37 USD | -666,161.77 USD | `-13.27%` | `1B / 5S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 4,170,924.01 USD | 2,148,582.90 USD | 2,022,341.12 USD | 126,241.78 USD | `+3.03%` | `5B / 3S` |

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
| `5m` | 424,030.00 USD | 605,000.00 USD | **`ACCUMULATION`** |
| `15m` | 840,630.00 USD | 1,350,000.00 USD | **`ACCUMULATION`** |
| `30m` | 1,850,000.00 USD | 664,150.00 USD | **`ACCUMULATION`** |
| `1h` | 3,100,000.00 USD | 4,370,000.00 USD | **`ACCUMULATION`** |
| `2h` | 1,100,000.00 USD | -11,740,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 7,580,000.00 USD | 1,790,000.00 USD | **`ACCUMULATION`** |
| `6h` | 20,630,000.00 USD | 28,410,000.00 USD | **`ACCUMULATION`** |
| `8h` | 21,010,000.00 USD | -7,960,000.00 USD | **`ACCUMULATION`** |
| `12h` | -8,530,000.00 USD | -5,820,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -47,550,000.00 USD | -131,620,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -114,980,000.00 USD | -211,710,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -592,090,000.00 USD | -1,300,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+424.03K` | 15m=`+840.63K` | 1h=`+3.10M` | 24h=`-47.55M`
* Futures Capital Netflows: 5m=`+605.00K` | 15m=`+1.35M` | 1h=`+4.37M` | 24h=`-131.62M`
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
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.22` (Risk Distance: `0.0142` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.28` (Risk Distance: `0.0142` pts)
  * +2.5R Take Profit: `1.23`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
