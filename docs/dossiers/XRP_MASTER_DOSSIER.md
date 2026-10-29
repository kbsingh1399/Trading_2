# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 03:43:28 IST` (`2026-10-29 22:13:28 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.25` | **Live Ask Quote**: `1.25` | **Mid Price**: `1.25`
- **Spread Points**: `3.00` | **Spread BPS**: `24.01 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.28` | VWAP Z-Score: `-1.64` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0119` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `34.13` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.34` | Lower -3.00σ Band: `1.22`
  * Upper +2.51σ Band: `1.33` | Lower -2.51σ Band: `1.23`
  * Upper +2.01σ Band: `1.32` | Lower -2.01σ Band: `1.24`
  * Upper +2.00σ Band: `1.32` | Lower -2.00σ Band: `1.24`
  * Upper +1.28σ Band: `1.31` | Lower -1.28σ Band: `1.26`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.26`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.26` | EMA-20=`1.27` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.28` (Slope: `+0.0000`) | EMA-100=`1.29`
  * Institutional Anchors: EMA-144=`1.30` | EMA-200=`1.30` (Slope: `-0.3692`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.33` | 24H Low=`1.22` | Weekly High=`1.34` | Weekly Low=`1.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-0.60%`)
  * Point of Control (POC) = `1.25` (Distance: `+0.11%`)
  * Value Area Low (VAL) = `1.25` (Distance: `+0.28%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.32` | Weekly POC=`1.29` | Weekly VAL=`1.27`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.23`
  * London Session (08:00-16:00 UTC): High=`1.25` | Low=`1.24`
  * New York Session (13:00-21:00 UTC): High=`1.26` | Low=`1.24`
  * Initial Balance (First Hour): IB High=`1.25` | IB Low=`1.25`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.24` - `1.25`
  * Optimal Trade Entry (OTE 0.705): `1.25`
  * Structural Invalidation Anchor (0.786): `1.26`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.26` | `1.26` | `1.25` | `1.25` | `2,555,947` | 3,206,024.98 USD | -251,078.33 USD | `-7.83%` | -76,883,323.89 USD | `+0.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `1.25` | `1.26` | `1.25` | `1.25` | `11,968,390` | 15,025,800.59 USD | 269,596.73 USD | `+1.79%` | -76,613,727.16 USD | `+0.40` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `1,456,804` | 1,822,360.11 USD | -564,554.09 USD | `-30.98%` | -77,178,281.25 USD | `+0.20` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.26` | `1.26` | `1.25` | `1.25` | `12,826,198` | 16,161,725.94 USD | 1,084,664.25 USD | `+6.71%` | -76,763,302.02 USD | `+0.58` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.25` | `10,406,661` | 13,078,738.26 USD | -163,908.89 USD | `-1.25%` | -76,927,210.91 USD | `+0.38` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.25` | `13,102,541` | 16,444,620.85 USD | -175,934.61 USD | `-1.07%` | -77,103,145.52 USD | `+0.37` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `1.28` | `1.28` | `1.22` | `1.24` | `208,906,305` | 260,797,546.37 USD | -37,805,029.03 USD | `-14.50%` | -77,339,869.93 USD | `-3.92` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.24` | `1.26` | `1.23` | `1.25` | `86,510,066` | 108,215,327.13 USD | 1,874,321.17 USD | `+1.73%` | -75,465,548.76 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.25` | `1.26` | `1.25` | `1.25` | `13,125,099` | 16,472,823.88 USD | -203,648.06 USD | `-1.24%` | -75,669,196.82 USD | `+0.30` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.25` | `308,541,471` | 385,485,697.37 USD | -36,134,355.92 USD | `-9.37%` | -76,073,385.74 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,072,364.54 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,389,228.53 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.25` | `308,541,471` | 385,485,697.37 USD | -36,134,355.92 USD | `-9.37%` | -76,073,385.74 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`1.25`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `1.25` | `45291.0000` | 56,781.33 USD | 2,019,119.32 USD | `7 orders` | `+0.17%` | `-` |
| `ASK` | `1.25` | `330518.0000` | 414,337.36 USD | 1,962,338.00 USD | `9 orders` | `+0.16%` | `-` |
| `ASK` | `1.25` | `30515.0000` | 38,250.55 USD | 1,548,000.63 USD | `7 orders` | `+0.16%` | `-` |
| `ASK` | `1.25` | `277654.0000` | 348,011.52 USD | 1,509,750.08 USD | `8 orders` | `+0.15%` | `-` |
| `ASK` | `1.25` | `6438.0000` | 8,068.75 USD | 1,161,738.56 USD | `3 orders` | `+0.14%` | `-` |
| `ASK` | `1.25` | `38417.0000` | 48,144.18 USD | 1,153,669.81 USD | `5 orders` | `+0.13%` | `-` |
| `ASK` | `1.25` | `221503.0000` | 277,565.41 USD | 1,105,525.63 USD | `10 orders` | `+0.12%` | `-` |
| `ASK` | `1.25` | `56908.0000` | 71,305.72 USD | 827,960.22 USD | `9 orders` | `+0.12%` | `-` |
| `ASK` | `1.25` | `31516.0000` | 39,486.40 USD | 756,654.49 USD | `7 orders` | `+0.11%` | `-` |
| `ASK` | `1.25` | `331404.0000` | 415,182.93 USD | 717,168.10 USD | `7 orders` | `+0.10%` | `-` |
| `ASK` | `1.25` | `67208.0000` | 84,191.46 USD | 301,985.17 USD | `8 orders` | `+0.09%` | `-` |
| `ASK` | `1.25` | `20032.0000` | 25,092.08 USD | 217,793.70 USD | `10 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `73642.0000` | 92,236.60 USD | 192,701.62 USD | `10 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `11297.0000` | 14,148.36 USD | 100,465.02 USD | `5 orders` | `+0.07%` | `-` |
| `ASK` | `1.25` | `25685.0000` | 32,165.33 USD | 86,316.65 USD | `5 orders` | `+0.06%` | `-` |
| `ASK` | `1.25` | `18042.0000` | 22,592.19 USD | 54,151.33 USD | `5 orders` | `+0.05%` | `-` |
| `ASK` | `1.25` | `7741.0000` | 9,692.51 USD | 31,559.13 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `11774.0000` | 14,741.05 USD | 21,866.63 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `4912.0000` | 6,149.33 USD | 7,125.58 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `1.25` | `780.0000` | 976.25 USD | 976.25 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.25` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.25` | `0.00%` | `-` |
| `BID` | `1.25` | `89960.0000` | 112,584.94 USD | 112,584.94 USD | `18 orders` | `-0.00%` | `-` |
| `BID` | `1.25` | `53813.0000` | 67,341.59 USD | 179,926.53 USD | `12 orders` | `-0.01%` | `-` |
| `BID` | `1.25` | `17402.0000` | 21,775.12 USD | 201,701.65 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `1.25` | `78733.0000` | 98,510.73 USD | 300,212.38 USD | `11 orders` | `-0.03%` | `-` |
| `BID` | `1.25` | `12633.0000` | 15,805.15 USD | 316,017.53 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `25615.0000` | 32,044.36 USD | 348,061.89 USD | `10 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `16084.0000` | 20,119.48 USD | 368,181.37 USD | `8 orders` | `-0.05%` | `-` |
| `BID` | `1.25` | `327549.0000` | 409,698.29 USD | 777,879.66 USD | `6 orders` | `-0.06%` | `-` |
| `BID` | `1.25` | `15419.0000` | 19,284.54 USD | 797,164.20 USD | `7 orders` | `-0.07%` | `-` |
| `BID` | `1.25` | `15386.0000` | 19,241.73 USD | 816,405.93 USD | `6 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `28167.0000` | 35,222.83 USD | 851,628.76 USD | `9 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `35589.0000` | 44,500.49 USD | 896,129.25 USD | `12 orders` | `-0.09%` | `-` |
| `BID` | `1.25` | `47539.0000` | 59,438.01 USD | 955,567.26 USD | `9 orders` | `-0.10%` | `-` |
| `BID` | `1.25` | `34347.0000` | 42,940.62 USD | 998,507.88 USD | `10 orders` | `-0.11%` | `-` |
| `BID` | `1.25` | `124019.0000` | 155,036.15 USD | 1,153,544.03 USD | `14 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `22379.0000` | 27,973.75 USD | 1,181,517.78 USD | `5 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `16770.0000` | 20,960.82 USD | 1,202,478.61 USD | `6 orders` | `-0.13%` | `-` |
| `BID` | `1.25` | `38840.0000` | 48,542.23 USD | 1,251,020.84 USD | `9 orders` | `-0.14%` | `-` |
| `BID` | `1.25` | `217561.0000` | 271,885.98 USD | 1,522,906.82 USD | `8 orders` | `-0.15%` | `-` |
| `BID` | `1.25` | `60315.0000` | 75,369.62 USD | 1,598,276.44 USD | `7 orders` | `-0.16%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `26` | `0x31b1...1434` | `LONG` | 43,764,765.50 USD | `35,031,430.00` | `1.13` | `1.25` | `0.9612` | 4,185,882.23 USD | `+9.56%` | `10X Cross` |
| `90` | `0x5b5d...c060` | `SHORT` | 20,052,695.68 USD | `15,964,251.00` | `1.44` | `1.25` | `12.23` | 2,863,373.03 USD | `+14.28%` | `5X Cross` |
| `157` | `0xb83d...6e36` | `SHORT` | 13,251,311.93 USD | `10,555,450.00` | `1.50` | `1.25` | `15.36` | 2,571,257.71 USD | `+19.40%` | `5X Cross` |
| `245` | `0x58f0...0d20` | `LONG` | 9,403,863.98 USD | `7,526,704.00` | `1.25` | `1.25` | `1.22` | 12,699.42 USD | `+0.14%` | `20X Cross` |
| `382` | `0x77ee...a018` | `LONG` | 6,223,080.12 USD | `4,943,700.00` | `1.27` | `1.25` | `0.3229` | -55,418.88 USD | `-0.89%` | `20X Cross` |
| `428` | `0xca49...53c8` | `SHORT` | 5,161,604.73 USD | `4,138,886.00` | `1.44` | `1.25` | `4.82` | 791,718.00 USD | `+15.34%` | `20X Cross` |
| `455` | `0xecb6...2b00` | `SHORT` | 4,868,914.10 USD | `3,904,189.00` | `1.29` | `1.25` | `8.75` | 156,590.32 USD | `+3.22%` | `10X Cross` |
| `495` | `0xfc27...9d9d` | `SHORT` | 4,469,251.88 USD | `3,576,546.00` | `1.30` | `1.25` | `6.14` | 196,623.85 USD | `+4.40%` | `20X Cross` |
| `498` | `0x610b...b613` | `LONG` | 4,458,638.46 USD | `3,543,946.00` | `1.44` | `1.25` | `0.8140` | -641,354.15 USD | `-14.38%` | `5X Cross` |
| `519` | `0xdd53...2b13` | `SHORT` | 4,216,844.17 USD | `3,381,320.00` | `1.43` | `1.25` | `20.19` | 619,426.12 USD | `+14.69%` | `3X Cross` |
| `610` | `0x9946...0852` | `SHORT` | 3,737,327.83 USD | `2,990,580.00` | `1.43` | `1.25` | `1.77` | 526,622.64 USD | `+14.09%` | `20X Cross` |
| `678` | `0xc30c...a4c9` | `SHORT` | 3,407,777.23 USD | `2,727,531.00` | `1.42` | `1.25` | `1.63` | 456,470.96 USD | `+13.39%` | `7X Cross` |
| `699` | `0x9aa5...58af` | `SHORT` | 3,264,389.91 USD | `2,604,083.00` | `1.46` | `1.25` | `4.71` | 533,330.75 USD | `+16.34%` | `20X Cross` |
| `712` | `0xf48f...10fe` | `LONG` | 3,228,006.56 USD | `2,565,779.00` | `1.53` | `1.25` | `1.01` | -696,634.17 USD | `-21.58%` | `4X Cross` |
| `747` | `0x023a...2355` | `SHORT` | 3,103,370.99 USD | `2,469,657.00` | `1.32` | `1.25` | `4.38` | 161,531.16 USD | `+5.21%` | `20X Cross` |
| `754` | `0x45d2...4029` | `SHORT` | 3,065,268.80 USD | `2,453,000.00` | `1.48` | `1.25` | `18.46` | 573,011.62 USD | `+18.69%` | `20X Cross` |
| `944` | `0xfc66...ca06` | `SHORT` | 2,406,885.39 USD | `1,926,433.00` | `1.30` | `1.25` | `16.11` | 99,008.81 USD | `+4.11%` | `20X Cross` |
| `1074` | `0xc179...e0c8` | `SHORT` | 2,066,565.82 USD | `1,654,179.00` | `1.30` | `1.25` | `5.05` | 85,823.96 USD | `+4.15%` | `10X Cross` |
| `1094` | `0xeadc...9d55` | `LONG` | 2,030,710.65 USD | `1,619,805.00` | `1.21` | `1.25` | `0.000000` | 71,867.63 USD | `+3.54%` | `20X Cross` |
| `1170` | `0x94b2...599e` | `SHORT` | 1,931,533.60 USD | `1,540,696.00` | `1.36` | `1.25` | `1.86` | 168,932.85 USD | `+8.75%` | `20X Cross` |
| `1177` | `0xbcd4...0dd2` | `SHORT` | 1,920,085.34 USD | `1,529,461.00` | `1.31` | `1.25` | `2.04` | 84,459.26 USD | `+4.40%` | `20X Cross` |
| `1200` | `0x3fc5...c0c1` | `SHORT` | 1,888,967.86 USD | `1,511,779.00` | `1.52` | `1.25` | `2.69` | 402,646.74 USD | `+21.32%` | `20X Cross` |
| `1214` | `0x31ef...f715` | `LONG` | 1,855,798.15 USD | `1,475,080.00` | `1.49` | `1.25` | `1.04` | -343,467.25 USD | `-18.51%` | `3X Isolated` |
| `1277` | `0x7737...bf66` | `SHORT` | 1,776,020.03 USD | `1,413,466.00` | `1.41` | `1.25` | `13.44` | 222,848.62 USD | `+12.55%` | `10X Cross` |
| `1322` | `0xe9d1...d2d3` | `SHORT` | 1,677,910.95 USD | `1,342,651.00` | `1.27` | `1.25` | `2.06` | 27,533.43 USD | `+1.64%` | `10X Cross` |
| `1337` | `0x95da...2328` | `LONG` | 1,663,116.84 USD | `1,324,876.00` | `1.35` | `1.25` | `0.1025` | -130,524.25 USD | `-7.85%` | `5X Cross` |
| `1356` | `0xef96...9383` | `SHORT` | 1,647,947.88 USD | `1,319,097.00` | `1.34` | `1.25` | `4.53` | 119,496.59 USD | `+7.25%` | `20X Cross` |
| `1365` | `0xee2b...d67e` | `LONG` | 1,640,303.43 USD | `1,306,284.00` | `1.55` | `1.25` | `0.3745` | -390,351.47 USD | `-23.80%` | `4X Cross` |
| `1425` | `0x215d...f80a` | `LONG` | 1,572,857.80 USD | `1,251,777.00` | `1.32` | `1.25` | `1.15` | -81,596.43 USD | `-5.19%` | `14X Cross` |
| `1440` | `0x2482...0e55` | `LONG` | 1,555,848.24 USD | `1,239,226.00` | `1.33` | `1.25` | `1.21` | -94,518.81 USD | `-6.08%` | `20X Isolated` |
| `1465` | `0x123d...3bff` | `LONG` | 1,529,005.41 USD | `1,215,329.00` | `1.35` | `1.25` | `0.000000` | -108,063.81 USD | `-7.07%` | `10X Cross` |
| `1506` | `0x5fa3...35b7` | `SHORT` | 1,472,735.25 USD | `1,178,754.00` | `1.31` | `1.25` | `3.45` | 67,463.93 USD | `+4.58%` | `20X Cross` |
| `1508` | `0x4537...8732` | `SHORT` | 1,470,593.51 USD | `1,177,134.00` | `1.25` | `1.25` | `2.10` | -1,905.37 USD | `-0.13%` | `10X Cross` |
| `1532` | `0xdf95...7d72` | `SHORT` | 1,447,249.57 USD | `1,160,492.00` | `1.37` | `1.25` | `36.39` | 146,182.05 USD | `+10.10%` | `20X Cross` |
| `1678` | `0xb1ce...681b` | `LONG` | 1,276,694.12 USD | `1,021,764.00` | `1.49` | `1.25` | `1.16` | -247,362.38 USD | `-19.38%` | `4X Isolated` |
| `1787` | `0x3c36...461a` | `LONG` | 1,175,721.79 USD | `940,051.00` | `1.30` | `1.25` | `1.05` | -43,358.83 USD | `-3.69%` | `10X Cross` |
| `2021` | `0xbfc7...80b4` | `SHORT` | 1,002,940.80 USD | `800,000.00` | `1.48` | `1.25` | `6.85` | 180,513.85 USD | `+18.00%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.32` | 19,275.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 19.28K USD at 1.3178 USD [API] | `2026-10-28 12:31:05` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 11,137.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.14K USD at 1.3176 USD [API] | `2026-10-28 12:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,665.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.67K USD at 1.3176 USD [API] | `2026-10-28 12:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,341.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.34K USD at 1.3176 USD [API] | `2026-10-28 12:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,386.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.39K USD at 1.3176 USD [API] | `2026-10-28 12:34:16` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,939.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.94K USD at 1.3153 USD [API] | `2026-10-28 12:36:13` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3153 USD [API] | `2026-10-28 12:36:13` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,055.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.06K USD at 1.3153 USD [API] | `2026-10-28 12:36:13` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3140 USD [API] | `2026-10-28 12:39:59` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 12,828.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 12.83K USD at 1.3147 USD [API] | `2026-10-28 12:40:33` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 12.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3330 USD [API] | `2026-10-27 23:48:33` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 12.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3330 USD [API] | `2026-10-27 23:48:33` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 53.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3330 USD [API] | `2026-10-27 23:48:29` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 224.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.22K USD at 1.3308 USD [API] | `2026-10-27 23:46:33` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,936.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.94K USD at 1.3160 USD [API] | `2026-10-28 12:44:11` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,897.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.90K USD at 1.3147 USD [API] | `2026-10-28 12:45:54` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,739.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.74K USD at 1.3147 USD [API] | `2026-10-28 12:45:54` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3147 USD [API] | `2026-10-28 12:45:54` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,007.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3149 USD [API] | `2026-10-28 12:49:56` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3150 USD [API] | `2026-10-28 12:49:56` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 13,385.45 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 13.39K USD at 1.3163 USD [API] | `2026-10-28 13:24:44` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,006.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3169 USD [API] | `2026-10-28 13:35:00` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,810.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.81K USD at 1.3211 USD [API] | `2026-10-28 13:40:07` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,784.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.78K USD at 1.3156 USD [API] | `2026-10-28 13:49:13` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 15,126.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 15.13K USD at 1.3156 USD [API] | `2026-10-28 13:51:21` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,367.65 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.37K USD at 1.3156 USD [API] | `2026-10-28 13:51:21` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 10,276.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.28K USD at 1.3150 USD [API] | `2026-10-28 13:52:34` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,104.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.10K USD at 1.3150 USD [API] | `2026-10-28 13:52:34` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 6,914.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.91K USD at 1.3150 USD [API] | `2026-10-28 13:52:34` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 11,323.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 11.32K USD at 1.3119 USD [API] | `2026-10-28 14:31:36` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 12,101.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 12.10K USD at 1.3104 USD [API] | `2026-10-28 14:35:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,762.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.76K USD at 1.3097 USD [API] | `2026-10-28 14:37:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,822.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.82K USD at 1.3097 USD [API] | `2026-10-28 14:37:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,048.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.05K USD at 1.3106 USD [API] | `2026-10-28 14:39:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3106 USD [API] | `2026-10-28 14:39:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,328.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.33K USD at 1.3108 USD [API] | `2026-10-28 14:40:55` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 85.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.09K USD at 1.2610 USD [API] | `2026-10-24 15:16:21` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 872.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.87K USD at 1.2610 USD [API] | `2026-10-24 15:16:21` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 3,747.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.75K USD at 1.2610 USD [API] | `2026-10-24 15:16:21` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,533.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.53K USD at 1.3116 USD [API] | `2026-10-28 14:41:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 6,016.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.02K USD at 1.3130 USD [API] | `2026-10-28 14:42:18` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3119 USD [API] | `2026-10-28 14:43:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 6,484.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.48K USD at 1.3121 USD [API] | `2026-10-28 14:47:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3122 USD [API] | `2026-10-28 14:47:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3115 USD [API] | `2026-10-28 14:46:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,186.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.19K USD at 1.3115 USD [API] | `2026-10-28 14:46:55` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 33.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.03K USD at 1.3444 USD [API] | `2026-10-28 02:18:25` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 22.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.3434 USD [API] | `2026-10-28 02:18:02` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 288.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.29K USD at 1.3434 USD [API] | `2026-10-28 02:18:02` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 406.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.41K USD at 1.3379 USD [API] | `2026-10-28 02:11:35` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 12.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3371 USD [API] | `2026-10-28 01:42:11` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3131 USD [API] | `2026-10-28 14:49:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3131 USD [API] | `2026-10-28 14:49:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3116 USD [API] | `2026-10-28 14:51:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3117 USD [API] | `2026-10-28 14:51:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 8,303.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.30K USD at 1.3118 USD [API] | `2026-10-28 14:58:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,005.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3118 USD [API] | `2026-10-28 14:58:25` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,411.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.41K USD at 1.3143 USD [API] | `2026-10-28 15:00:59` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,944.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.94K USD at 1.3143 USD [API] | `2026-10-28 15:00:59` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3143 USD [API] | `2026-10-28 15:00:59` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3143 USD [API] | `2026-10-28 15:00:59` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3143 USD [API] | `2026-10-28 15:00:59` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,259.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.26K USD at 1.3149 USD [API] | `2026-10-28 15:03:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,346.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.35K USD at 1.3149 USD [API] | `2026-10-28 15:03:55` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3115 USD [API] | `2026-10-28 15:37:48` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 2,448.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.45K USD at 1.2734 USD [API] | `2026-10-24 09:43:05` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,516.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.52K USD at 1.2734 USD [API] | `2026-10-24 09:43:05` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 384.57 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.38K USD at 1.2734 USD [API] | `2026-10-24 09:43:05` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,665.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.67K USD at 1.2896 USD [API] | `2026-10-15 02:24:32` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,535.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.54K USD at 1.3419 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,011.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.01K USD at 1.3419 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,593.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.59K USD at 1.3419 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 56.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.06K USD at 1.3419 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 688.45 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.69K USD at 1.3420 USD [API] | `2026-10-12 21:47:08` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 4,594.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.59K USD at 1.3687 USD [API] | `2026-10-08 15:20:54` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 75.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.08K USD at 1.3687 USD [API] | `2026-10-08 15:20:54` |
| `ANNOUNCEMENT` | `INFO` | `1.44` | 3,048.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.05K USD at 1.4364 USD [API] | `2026-10-07 13:34:46` |
| `ANNOUNCEMENT` | `INFO` | `1.53` | 2,943.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.94K USD at 1.5252 USD [API] | `2026-09-26 18:38:35` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3130 USD [API] | `2026-10-28 15:42:20` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 6,230.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.23K USD at 1.3108 USD [API] | `2026-10-28 15:48:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,372.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.37K USD at 1.3103 USD [API] | `2026-10-28 15:49:11` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3106 USD [API] | `2026-10-28 15:59:31` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3122 USD [API] | `2026-10-28 16:14:28` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,005.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3121 USD [API] | `2026-10-28 16:14:28` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,745.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.75K USD at 1.3111 USD [API] | `2026-10-28 16:19:56` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 5,071.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.07K USD at 1.4880 USD [API] | `2026-08-22 05:16:06` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 8,919.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.92K USD at 1.4750 USD [API] | `2026-08-22 05:10:38` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,005.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3104 USD [API] | `2026-10-28 16:37:56` |
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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+2.74%`) | Long MP=`1.22` (Vol: 512,900.00 USD, Dist: `--3.35%`)
  * 48H Horizon: Short MP=`1.35` (Vol: 3,500,000.00 USD, Dist: `+7.03%`) | Long MP=`1.22` (Vol: 512,900.00 USD, Dist: `--3.35%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 3,400,000.00 USD, Dist: `+7.03%`) | Long MP=`1.22` (Vol: 512,900.00 USD, Dist: `--3.35%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 4,100,000.00 USD, Dist: `+7.03%`) | Long MP=`1.21` (Vol: 536,100.00 USD, Dist: `--4.10%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 24,230.00 USD | 73,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 972.02 USD | 73,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 1,730.00 USD | 73,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 18,290.00 USD | 73,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 103,250.00 USD | 73,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 37,750.00 USD | 72,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 1,560,000.00 USD | 72,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 635.05 USD | 71,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 708.53 USD | 71,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 517.50 USD | 71,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 3,380.00 USD | 71,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 2,260.00 USD | 71,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 503,080.00 USD | 71,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 174.59 USD | 70,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 497.34 USD | 70,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 1,110.00 USD | 70,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 1,210.00 USD | 70,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 7,840.00 USD | 70,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 19,800.00 USD | 70,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 10,340.00 USD | 70,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 179.96 USD | 70,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 1,180.00 USD | 70,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 9,470.00 USD | 70,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 188.87 USD | 70,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 4,360.00 USD | 70,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 6,570.00 USD | 70,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 1,700.00 USD | 70,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 3,260.00 USD | 70,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 2,020.00 USD | 70,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 162,700.00 USD | 70,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 8,170.00 USD | 70,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 4,040.00 USD | 70,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 20,150.00 USD | 70,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 36,310.00 USD | 70,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 1,130.00 USD | 70,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 12,730.00 USD | 70,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 18,960.00 USD | 70,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 7,470.00 USD | 70,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 27,220.00 USD | 70,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 37,010.00 USD | 70,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 2,910.00 USD | 70,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 24,280.00 USD | 70,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 176,640.00 USD | 70,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 78,860.00 USD | 70,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 216,700.00 USD | 70,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 61,790.00 USD | 69,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 117,880.00 USD | 69,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 113,690.00 USD | 69,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 2,190.00 USD | 69,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 6,770.00 USD | 69,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 20,130.00 USD | 69,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 11,250.00 USD | 69,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 12,260.00 USD | 69,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 2,900,000.00 USD | 69,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 35,830.00 USD | 66,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 39,540.00 USD | 66,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 76,610.00 USD | 66,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 44,630.00 USD | 66,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 39,750.00 USD | 66,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 88,910.00 USD | 66,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 384,970.00 USD | 66,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 101,830.00 USD | 65,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 211,390.00 USD | 65,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 73,280.00 USD | 65,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 120,100.00 USD | 65,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 86,160.00 USD | 65,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 64,920.00 USD | 65,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 109,220.00 USD | 65,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,880,000.00 USD | 65,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 151,090.00 USD | 31,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 458,840.00 USD | 31,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 93,970.00 USD | 30,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 3,050,000.00 USD | 30,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 828,610.00 USD | 27,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 150,730.00 USD | 26,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,140,000.00 USD | 26,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 1,290,000.00 USD | 24,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,360,000.00 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 294,960.00 USD | 21,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 472,550.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 742,690.00 USD | 20,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 365,440.00 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 68,820.00 USD | 19,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.11` | 29,660,000.00 USD | 29,660,000.00 USD | 17,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 55,470,000.00 USD | 55,470,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 29,640,000.00 USD | 29,640,000.00 USD | 18,710.00 USD | 0.00 USD | 119,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 29,500,000.00 USD | 29,500,000.00 USD | 0.00 USD | 2,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 55,440,000.00 USD | 55,440,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 493,430.00 USD | 19,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.12` | 29,500,000.00 USD | 29,500,000.00 USD | 0.00 USD | 0.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 55,430,000.00 USD | 55,430,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 29,490,000.00 USD | 29,490,000.00 USD | 0.00 USD | 46,860.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 29,440,000.00 USD | 29,440,000.00 USD | 0.00 USD | 1,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 55,350,000.00 USD | 55,350,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 55,350,000.00 USD | 55,350,000.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 401,530.00 USD | 19,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 29,440,000.00 USD | 29,440,000.00 USD | 0.00 USD | 783.15 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 29,440,000.00 USD | 29,440,000.00 USD | 0.00 USD | 42,490.00 USD | 78,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 55,350,000.00 USD | 55,350,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 29,320,000.00 USD | 29,320,000.00 USD | 0.00 USD | 66,770.00 USD | 166,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 55,160,000.00 USD | 55,160,000.00 USD | 5,450.00 USD | 3,410.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 29,080,000.00 USD | 29,080,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 55,140,000.00 USD | 55,140,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 29,030,000.00 USD | 29,030,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 54,670,000.00 USD | 54,670,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 202,400.00 USD | 18,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.14` | 28,980,000.00 USD | 28,980,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 54,420,000.00 USD | 54,420,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 28,890,000.00 USD | 28,890,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 54,320,000.00 USD | 54,320,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 28,860,000.00 USD | 28,860,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 54,310,000.00 USD | 54,310,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 28,800,000.00 USD | 28,800,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 54,250,000.00 USD | 54,250,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 28,660,000.00 USD | 28,660,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 54,130,000.00 USD | 54,130,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 1,770,000.00 USD | 18,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 54,120,000.00 USD | 54,120,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 28,620,000.00 USD | 28,620,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 53,980,000.00 USD | 53,980,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 53,620,000.00 USD | 53,620,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 28,600,000.00 USD | 28,600,000.00 USD | 4,040.00 USD | 11,230.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 53,460,000.00 USD | 53,460,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 28,400,000.00 USD | 28,400,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 53,080,000.00 USD | 53,080,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 320,470.00 USD | 16,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 28,060,000.00 USD | 28,060,000.00 USD | 29,120.00 USD | 9,570.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 52,430,000.00 USD | 52,430,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 27,990,000.00 USD | 27,990,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 51,630,000.00 USD | 51,630,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 27,680,000.00 USD | 27,680,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 51,110,000.00 USD | 51,110,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 27,060,000.00 USD | 27,060,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 50,090,000.00 USD | 50,090,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 26,440,000.00 USD | 26,440,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 48,710,000.00 USD | 48,710,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,520,000.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 26,220,000.00 USD | 26,220,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 48,080,000.00 USD | 48,080,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 25,910,000.00 USD | 25,910,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 46,700,000.00 USD | 46,700,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 25,750,000.00 USD | 25,750,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 45,200,000.00 USD | 45,200,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 25,580,000.00 USD | 25,580,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 43,810,000.00 USD | 43,810,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 25,320,000.00 USD | 25,320,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 43,010,000.00 USD | 43,010,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 495,380.00 USD | 15,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 24,980,000.00 USD | 24,980,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 42,130,000.00 USD | 42,130,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 24,850,000.00 USD | 24,850,000.00 USD | 93,410.00 USD | 41,360.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 41,670,000.00 USD | 41,670,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 24,670,000.00 USD | 24,670,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 40,960,000.00 USD | 40,960,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 24,640,000.00 USD | 24,640,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 40,580,000.00 USD | 40,580,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 24,530,000.00 USD | 24,530,000.00 USD | 92,110.00 USD | 7,460.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 40,450,000.00 USD | 40,450,000.00 USD | 123,240.00 USD | 97,270.00 USD | 289,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 320,270.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 24,400,000.00 USD | 24,400,000.00 USD | 16,710.00 USD | 139,070.00 USD | 316,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 39,940,000.00 USD | 39,940,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 23,930,000.00 USD | 23,930,000.00 USD | 188,800.00 USD | 7,100.00 USD | 309,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 39,170,000.00 USD | 39,170,000.00 USD | 182,110.00 USD | 132,500.00 USD | 278,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 23,420,000.00 USD | 23,420,000.00 USD | 48,220.00 USD | 10,480.00 USD | 70,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 38,580,000.00 USD | 38,580,000.00 USD | 152,830.00 USD | 265,920.00 USD | 273,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 23,290,000.00 USD | 23,290,000.00 USD | 42,050.00 USD | 216,220.00 USD | 112,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 37,880,000.00 USD | 37,880,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 22,920,000.00 USD | 22,920,000.00 USD | 43,900.00 USD | 14,200.00 USD | 20,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 37,220,000.00 USD | 37,220,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 387,750.00 USD | 14,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 22,840,000.00 USD | 22,840,000.00 USD | 27,320.00 USD | 6,070.00 USD | 8,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 36,510,000.00 USD | 36,510,000.00 USD | 5,350.00 USD | 101,030.00 USD | 187,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 36,220,000.00 USD | 36,220,000.00 USD | 67,200.00 USD | 152,970.00 USD | 201,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 22,800,000.00 USD | 22,800,000.00 USD | 0.00 USD | 28,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 35,800,000.00 USD | 35,800,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 22,770,000.00 USD | 22,770,000.00 USD | 35,450.00 USD | 4,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 35,720,000.00 USD | 35,720,000.00 USD | 202,570.00 USD | 146,780.00 USD | 534,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 22,730,000.00 USD | 22,730,000.00 USD | 4,360.00 USD | 297,650.00 USD | 195,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 34,840,000.00 USD | 34,840,000.00 USD | 0.00 USD | 17,680.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 1,490,000.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 22,240,000.00 USD | 22,240,000.00 USD | 81,900.00 USD | 32,170.00 USD | 415,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 34,740,000.00 USD | 34,740,000.00 USD | 80,450.00 USD | 7,260.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 21,710,000.00 USD | 21,710,000.00 USD | 220,830.00 USD | 67,350.00 USD | 14,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 34,640,000.00 USD | 34,640,000.00 USD | 659,990.00 USD | 518,690.00 USD | 368,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 21,400,000.00 USD | 21,400,000.00 USD | 99,310.00 USD | 425,250.00 USD | 714,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 33,100,000.00 USD | 33,100,000.00 USD | 180,260.00 USD | 264,440.00 USD | 802,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 20,160,000.00 USD | 20,160,000.00 USD | 419,060.00 USD | 161,150.00 USD | 591,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 31,850,000.00 USD | 31,850,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 18,990,000.00 USD | 18,990,000.00 USD | 65,710.00 USD | 6,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 31,450,000.00 USD | 31,450,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 11,710,000.00 USD | 12,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.22` | 18,920,000.00 USD | 18,920,000.00 USD | 118,950.00 USD | 1,870.00 USD | 203,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 31,270,000.00 USD | 31,270,000.00 USD | 157,620.00 USD | 396,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 18,600,000.00 USD | 18,600,000.00 USD | 261,180.00 USD | 384,120.00 USD | 178,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 30,720,000.00 USD | 30,720,000.00 USD | 256,390.00 USD | 4,120.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 17,770,000.00 USD | 17,770,000.00 USD | 12,860.00 USD | 4,180.00 USD | 131,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 30,420,000.00 USD | 30,420,000.00 USD | 159,150.00 USD | 10,480.00 USD | 328,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 17,620,000.00 USD | 17,620,000.00 USD | 0.00 USD | 486,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 29,920,000.00 USD | 29,920,000.00 USD | 0.00 USD | 197,690.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 17,140,000.00 USD | 17,140,000.00 USD | 489,230.00 USD | 57,290.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 28,700,000.00 USD | 28,700,000.00 USD | 627,450.00 USD | 381,850.00 USD | 4,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 453,880.00 USD | 688,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.23` | 14,280,000.00 USD | 14,280,000.00 USD | 8,660.00 USD | 5,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 27,690,000.00 USD | 27,690,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 14,260,000.00 USD | 14,260,000.00 USD | 105,710.00 USD | 213,020.00 USD | 551,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 27,230,000.00 USD | 27,230,000.00 USD | 0.00 USD | 1,110,000.00 USD | 995,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 13,390,000.00 USD | 13,390,000.00 USD | 319,240.00 USD | 1,170,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 25,130,000.00 USD | 25,130,000.00 USD | 782,590.00 USD | 485,710.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 11,900,000.00 USD | 11,900,000.00 USD | 281,800.00 USD | 199,040.00 USD | 831,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 23,850,000.00 USD | 23,850,000.00 USD | 1,040,000.00 USD | 597,200.00 USD | 112,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 10,590,000.00 USD | 10,590,000.00 USD | 433,890.00 USD | 0.00 USD | 39,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 22,100,000.00 USD | 22,100,000.00 USD | 996,240.00 USD | 998,790.00 USD | 66,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 234,750.00 USD | 234,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 478,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 20,040,000.00 USD | 20,040,000.00 USD | 1,640,000.00 USD | 1,500,000.00 USD | 719,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 114,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 16,190,000.00 USD | 16,190,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 14,410,000.00 USD | 14,410,000.00 USD | 1,820,000.00 USD | 374,420.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 8,200,000.00 USD | 8,200,000.00 USD | 321,060.00 USD | 774,420.00 USD | 560,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 10,270,000.00 USD | 10,270,000.00 USD | 896,470.00 USD | 0.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 6,540,000.00 USD | 6,540,000.00 USD | 1,400,000.00 USD | 385,630.00 USD | 2,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 8,360,000.00 USD | 8,360,000.00 USD | 3,440,000.00 USD | 923,130.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 2,430,000.00 USD | 2,430,000.00 USD | 1,150,000.00 USD | 567,630.00 USD | 707,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 2,330,000.00 USD | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 4,620,000.00 USD | 4,620,000.00 USD | 1,060,000.00 USD | 815,140.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 2,770,000.00 USD | 2,770,000.00 USD | 2,720,000.00 USD | 0.00 USD | 51,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 5,540,000.00 USD | 5,540,000.00 USD | 2,720,000.00 USD | 0.00 USD | 51,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 4,830,000.00 USD | 4,830,000.00 USD | 198,150.00 USD | 0.00 USD | 6,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 8,390,000.00 USD | 8,390,000.00 USD | 2,810,000.00 USD | 0.00 USD | 44,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 5,470,000.00 USD | 5,470,000.00 USD | 635,790.00 USD | 0.00 USD | 4,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 9,740,000.00 USD | 9,740,000.00 USD | 1,240,000.00 USD | 0.00 USD | 104,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 6,260,000.00 USD | 6,260,000.00 USD | 794,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 9,930,000.00 USD | 9,930,000.00 USD | 172,030.00 USD | 0.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 7,070,000.00 USD | 7,070,000.00 USD | 803,540.00 USD | 2,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 7,160,000.00 USD | 7,160,000.00 USD | 86,570.00 USD | 3,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 10,040,000.00 USD | 10,040,000.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 7,830,000.00 USD | 7,830,000.00 USD | 63,380.00 USD | 2,060.00 USD | 611,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 381,210.00 USD | 485,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 9,370,000.00 USD | 9,370,000.00 USD | 390,940.00 USD | 121,550.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 12,820,000.00 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 446,110.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 19,750,000.00 USD | 19,750,000.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 4,420.00 USD | 4,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.27` | 12,940,000.00 USD | 12,940,000.00 USD | 39,860.00 USD | 1,080,000.00 USD | 861,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 32,990,000.00 USD | 32,990,000.00 USD | 2,620,000.00 USD | 2,370,000.00 USD | 8,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 14,970,000.00 USD | 14,970,000.00 USD | 0.00 USD | 2,030,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 37,760,000.00 USD | 37,760,000.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 17,780,000.00 USD | 17,780,000.00 USD | 327,600.00 USD | 803,550.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 41,370,000.00 USD | 41,370,000.00 USD | 943,110.00 USD | 2,540,000.00 USD | 123,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 20,130,000.00 USD | 20,130,000.00 USD | 1,740,000.00 USD | 318,590.00 USD | 285,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 46,100,000.00 USD | 46,100,000.00 USD | 186,960.00 USD | 3,980,000.00 USD | 567,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 25,690,000.00 USD | 25,690,000.00 USD | 439,850.00 USD | 2,150,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 60,670,000.00 USD | 60,670,000.00 USD | 4,420,000.00 USD | 1,940,000.00 USD | 8,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 5,770.00 USD | 10,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 35,450,000.00 USD | 35,450,000.00 USD | 3,050,000.00 USD | 2,800,000.00 USD | 3,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 78,940,000.00 USD | 78,940,000.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 43,180,000.00 USD | 43,180,000.00 USD | 3,180,000.00 USD | 2,210,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 85,230,000.00 USD | 85,230,000.00 USD | 3,260,000.00 USD | 1,940,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 44,510,000.00 USD | 44,510,000.00 USD | 209,970.00 USD | 608,220.00 USD | 507,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 86,190,000.00 USD | 86,190,000.00 USD | 0.00 USD | 879,610.00 USD | 79,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 47,370,000.00 USD | 47,370,000.00 USD | 1,120,000.00 USD | 199,040.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 88,200,000.00 USD | 88,200,000.00 USD | 1,460,000.00 USD | 478,060.00 USD | 67,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 49,390,000.00 USD | 49,390,000.00 USD | 421,680.00 USD | 611,360.00 USD | 985,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 91,790,000.00 USD | 91,790,000.00 USD | 639,910.00 USD | 1,380,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 10,130.00 USD | 20,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 51,300,000.00 USD | 51,300,000.00 USD | 726,790.00 USD | 768,570.00 USD | 418,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 92,960,000.00 USD | 92,960,000.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 51,470,000.00 USD | 51,470,000.00 USD | 160,320.00 USD | 7,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 93,070,000.00 USD | 93,070,000.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 51,640,000.00 USD | 51,640,000.00 USD | 151,350.00 USD | 0.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 95,160,000.00 USD | 95,160,000.00 USD | 1,060,000.00 USD | 198,070.00 USD | 829,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 54,520,000.00 USD | 54,520,000.00 USD | 546,160.00 USD | 193,100.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 95,580,000.00 USD | 95,580,000.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 60,380,000.00 USD | 60,380,000.00 USD | 1,800,000.00 USD | 608,440.00 USD | 3,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 105,220,000.00 USD | 105,220,000.00 USD | 3,350,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 11,500.00 USD | 31,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 62,600,000.00 USD | 62,600,000.00 USD | 497,720.00 USD | 629,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 106,450,000.00 USD | 106,450,000.00 USD | 209,360.00 USD | 396,530.00 USD | 628,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 62,940,000.00 USD | 62,940,000.00 USD | 254,730.00 USD | 87,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 107,970,000.00 USD | 107,970,000.00 USD | 0.00 USD | 95,300.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 64,500,000.00 USD | 64,500,000.00 USD | 274,080.00 USD | 110,280.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 109,230,000.00 USD | 109,230,000.00 USD | 0.00 USD | 286,660.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 65,920,000.00 USD | 65,920,000.00 USD | 520,770.00 USD | 899,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 112,320,000.00 USD | 112,320,000.00 USD | 0.00 USD | 2,610,000.00 USD | 485,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 67,190,000.00 USD | 67,190,000.00 USD | 304,340.00 USD | 649,450.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 112,320,000.00 USD | 112,320,000.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 11,730.00 USD | 43,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 69,480,000.00 USD | 69,480,000.00 USD | 689,960.00 USD | 147,250.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 115,330,000.00 USD | 115,330,000.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 72,720,000.00 USD | 72,720,000.00 USD | 1,130,000.00 USD | 330,750.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 119,790,000.00 USD | 119,790,000.00 USD | 1,670,000.00 USD | 1,060,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 75,040,000.00 USD | 75,040,000.00 USD | 876,130.00 USD | 869,070.00 USD | 573,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 123,050,000.00 USD | 123,050,000.00 USD | 839,350.00 USD | 430,210.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 78,030,000.00 USD | 78,030,000.00 USD | 1,390,000.00 USD | 664,910.00 USD | 944,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 125,890,000.00 USD | 125,890,000.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 81,170,000.00 USD | 81,170,000.00 USD | 372,630.00 USD | 454,810.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 128,350,000.00 USD | 128,350,000.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 4,910.00 USD | 48,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 87,740,000.00 USD | 87,740,000.00 USD | 1,320,000.00 USD | 1,700,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 132,970,000.00 USD | 132,970,000.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 92,820,000.00 USD | 92,820,000.00 USD | 1,740,000.00 USD | 836,160.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 136,050,000.00 USD | 136,050,000.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 96,320,000.00 USD | 96,320,000.00 USD | 1,650,000.00 USD | 652,780.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 137,880,000.00 USD | 137,880,000.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 100,910,000.00 USD | 100,910,000.00 USD | 1,990,000.00 USD | 583,250.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 142,340,000.00 USD | 142,340,000.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 102,910,000.00 USD | 102,910,000.00 USD | 1,080,000.00 USD | 287,760.00 USD | 625,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 144,710,000.00 USD | 144,710,000.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 56,840.00 USD | 105,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 105,440,000.00 USD | 105,440,000.00 USD | 664,210.00 USD | 621,550.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 145,240,000.00 USD | 145,240,000.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 107,680,000.00 USD | 107,680,000.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 146,400,000.00 USD | 146,400,000.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 110,530,000.00 USD | 110,530,000.00 USD | 848,670.00 USD | 298,810.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 148,120,000.00 USD | 148,120,000.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 112,910,000.00 USD | 112,910,000.00 USD | 1,040,000.00 USD | 190,550.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 152,170,000.00 USD | 152,170,000.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 115,000,000.00 USD | 115,000,000.00 USD | 859,040.00 USD | 354,550.00 USD | 872,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 152,720,000.00 USD | 152,720,000.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 3,240.00 USD | 108,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 117,090,000.00 USD | 117,090,000.00 USD | 896,540.00 USD | 219,260.00 USD | 976,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 154,660,000.00 USD | 154,660,000.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 119,960,000.00 USD | 119,960,000.00 USD | 1,170,000.00 USD | 370,350.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 157,010,000.00 USD | 157,010,000.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 122,600,000.00 USD | 122,600,000.00 USD | 1,330,000.00 USD | 518,530.00 USD | 792,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 161,720,000.00 USD | 161,720,000.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 126,330,000.00 USD | 126,330,000.00 USD | 1,750,000.00 USD | 754,220.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 167,360,000.00 USD | 167,360,000.00 USD | 1,700,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 128,100,000.00 USD | 128,100,000.00 USD | 584,400.00 USD | 416,300.00 USD | 762,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 178,430,000.00 USD | 178,430,000.00 USD | 3,700,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 2,240.00 USD | 110,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 129,150,000.00 USD | 129,150,000.00 USD | 355,660.00 USD | 234,160.00 USD | 458,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 185,540,000.00 USD | 185,540,000.00 USD | 2,410,000.00 USD | 2,230,000.00 USD | 2,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 130,640,000.00 USD | 130,640,000.00 USD | 752,410.00 USD | 149,380.00 USD | 594,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 195,850,000.00 USD | 195,850,000.00 USD | 4,290,000.00 USD | 1,700,000.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 131,730,000.00 USD | 131,730,000.00 USD | 507,940.00 USD | 126,620.00 USD | 450,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 203,620,000.00 USD | 203,620,000.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 133,490,000.00 USD | 133,490,000.00 USD | 716,900.00 USD | 334,990.00 USD | 716,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 211,950,000.00 USD | 211,950,000.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 134,680,000.00 USD | 134,680,000.00 USD | 363,860.00 USD | 145,570.00 USD | 673,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 220,180,000.00 USD | 220,180,000.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 8,910.00 USD | 119,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 135,860,000.00 USD | 135,860,000.00 USD | 560,800.00 USD | 47,560.00 USD | 572,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 224,270,000.00 USD | 224,270,000.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 136,200,000.00 USD | 136,200,000.00 USD | 213,710.00 USD | 42,480.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 228,060,000.00 USD | 228,060,000.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 136,940,000.00 USD | 136,940,000.00 USD | 277,960.00 USD | 149,990.00 USD | 316,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 230,190,000.00 USD | 230,190,000.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 137,280,000.00 USD | 137,280,000.00 USD | 171,250.00 USD | 2,260.00 USD | 166,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 234,290,000.00 USD | 234,290,000.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 137,340,000.00 USD | 137,340,000.00 USD | 0.00 USD | 26,460.00 USD | 34,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 236,010,000.00 USD | 236,010,000.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 261,140.00 USD | 380,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 137,670,000.00 USD | 137,670,000.00 USD | 53,740.00 USD | 103,940.00 USD | 171,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 236,500,000.00 USD | 236,500,000.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 137,860,000.00 USD | 137,860,000.00 USD | 121,310.00 USD | 2,250.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 237,910,000.00 USD | 237,910,000.00 USD | 528,490.00 USD | 136,720.00 USD | 753,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 138,050,000.00 USD | 138,050,000.00 USD | 1,740.00 USD | 66,920.00 USD | 119,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 239,080,000.00 USD | 239,080,000.00 USD | 334,560.00 USD | 372,470.00 USD | 461,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 138,200,000.00 USD | 138,200,000.00 USD | 75,340.00 USD | 249.08 USD | 69,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 241,680,000.00 USD | 241,680,000.00 USD | 920,600.00 USD | 405,390.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 138,320,000.00 USD | 138,320,000.00 USD | 54,550.00 USD | 884.30 USD | 69,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 243,270,000.00 USD | 243,270,000.00 USD | 536,130.00 USD | 294,500.00 USD | 759,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 138,650,000.00 USD | 138,650,000.00 USD | 112,910.00 USD | 50,670.00 USD | 163,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 244,830,000.00 USD | 244,830,000.00 USD | 617,230.00 USD | 389,310.00 USD | 552,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 139,300,000.00 USD | 139,300,000.00 USD | 254,930.00 USD | 111,730.00 USD | 284,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 246,960,000.00 USD | 246,960,000.00 USD | 579,450.00 USD | 290,350.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 139,570,000.00 USD | 139,570,000.00 USD | 122,940.00 USD | 98,400.00 USD | 50,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 249,510,000.00 USD | 249,510,000.00 USD | 1,210,000.00 USD | 331,990.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 139,860,000.00 USD | 139,860,000.00 USD | 84,700.00 USD | 16,420.00 USD | 186,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 250,600,000.00 USD | 250,600,000.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 139,920,000.00 USD | 139,920,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 251,880,000.00 USD | 251,880,000.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,280.00 USD | 382,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 139,970,000.00 USD | 139,970,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 252,430,000.00 USD | 252,430,000.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 140,060,000.00 USD | 140,060,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 253,530,000.00 USD | 253,530,000.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 253,690,000.00 USD | 253,690,000.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 140,080,000.00 USD | 140,080,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 254,020,000.00 USD | 254,020,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 140,150,000.00 USD | 140,150,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,190,000.00 USD | 254,190,000.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 4,180.00 USD | 386,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.40` | 140,290,000.00 USD | 140,290,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,310,000.00 USD | 254,310,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 140,330,000.00 USD | 140,330,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,320,000.00 USD | 254,320,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,450,000.00 USD | 254,450,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 140,340,000.00 USD | 140,340,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 254,570,000.00 USD | 254,570,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 254,810,000.00 USD | 254,810,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 795.23 USD | 387,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 254,980,000.00 USD | 254,980,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 255,360,000.00 USD | 255,360,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 256,010,000.00 USD | 256,010,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 256,180,000.00 USD | 256,180,000.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 256,800,000.00 USD | 256,800,000.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,600.00 USD | 390,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.42` | 257,330,000.00 USD | 257,330,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 258,350,000.00 USD | 258,350,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 259,730,000.00 USD | 259,730,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 260,350,000.00 USD | 260,350,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 260,710,000.00 USD | 260,710,000.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,610.00 USD | 484,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.43` | 261,730,000.00 USD | 261,730,000.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 263,240,000.00 USD | 263,240,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 264,630,000.00 USD | 264,630,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 265,430,000.00 USD | 265,430,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 265,960,000.00 USD | 265,960,000.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 258.30 USD | 484,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 266,310,000.00 USD | 266,310,000.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 266,760,000.00 USD | 266,760,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 267,480,000.00 USD | 267,480,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 267,850,000.00 USD | 267,850,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 267,980,000.00 USD | 267,980,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 268,110,000.00 USD | 268,110,000.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 268,440,000.00 USD | 268,440,000.00 USD | 62,180.00 USD | 96,050.00 USD | 173,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 269,050,000.00 USD | 269,050,000.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 269,610,000.00 USD | 269,610,000.00 USD | 182,110.00 USD | 128,180.00 USD | 251,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 270,070,000.00 USD | 270,070,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.46` | 1,590.00 USD | 486,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.46` | 270,230,000.00 USD | 270,230,000.00 USD | 85,350.00 USD | 51,250.00 USD | 20,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 270,700,000.00 USD | 270,700,000.00 USD | 119,110.00 USD | 56,610.00 USD | 296,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 270,910,000.00 USD | 270,910,000.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.47` | 697,740.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 18,070.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 128,990.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 11,950.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 915.06 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 776.71 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 2,130.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 6,800.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,900.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 123.63 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 129,530.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 117.16 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 108.21 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 4,430,000.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 3,800.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 2,170.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 4,180.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 1,160.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 3,960.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,730.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 5,250,000.00 USD | 11,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 7,340.00 USD | 11,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 351.45 USD | 11,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 129,540.00 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 2,850.00 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 747.78 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 2,020.00 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 128.45 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 9,340.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 428.50 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,880,000.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 113,220.00 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,190.00 USD | 14,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 552.45 USD | 14,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 794.73 USD | 14,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 309,300.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 8,870.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.95` | 3,320.00 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 14,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 227,680.00 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.99` | 119.10 USD | 14,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 401,000.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 1,290.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 2,010.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 5,960,000.00 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 460.50 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 1,200.00 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 2,680,000.00 USD | 23,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 331.01 USD | 23,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 247,230.00 USD | 24,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,100.00 USD | 24,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 1,390.00 USD | 24,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 3,000.00 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 301.53 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 201.94 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 873.18 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 2,750.00 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 75,280.00 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 205.62 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 103.27 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 103.73 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 208.38 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 44,140.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 459.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 2,860.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 11,850.00 USD | 24,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 2,540.00 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 144.77 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 222.77 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 108.79 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 56,430.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 225,350.00 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 155.68 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 481.00 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 27,800.00 USD | 24,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 18,830.00 USD | 24,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 2,840.00 USD | 24,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 94,260.00 USD | 24,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 337.96 USD | 24,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 4,370.00 USD | 24,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 73,050,000.00 USD | 0.00 USD | 24,230.00 USD | `-79.67%` | `95,000.00` |
| `Live` | `Long` | `0.2650` | 73,030,000.00 USD | 0.00 USD | 972.02 USD | `-78.87%` | `3,668.00` |
| `Live` | `Long` | `0.2750` | 73,030,000.00 USD | 0.00 USD | 1,730.00 USD | `-78.07%` | `6,284.00` |
| `Live` | `Long` | `0.2850` | 73,020,000.00 USD | 0.00 USD | 18,290.00 USD | `-77.27%` | `64,190.00` |
| `Live` | `Long` | `0.2950` | 73,010,000.00 USD | 0.00 USD | 103,250.00 USD | `-76.48%` | `350,000.00` |
| `Live` | `Long` | `0.3050` | 72,900,000.00 USD | 0.00 USD | 37,750.00 USD | `-75.68%` | `123,760.00` |
| `Live` | `Long` | `0.3150` | 72,860,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-74.88%` | `4,960,402.00` |
| `Live` | `Long` | `0.3250` | 71,300,000.00 USD | 0.00 USD | 635.05 USD | `-74.09%` | `1,954.00` |
| `Live` | `Long` | `0.3350` | 71,300,000.00 USD | 0.00 USD | 708.53 USD | `-73.29%` | `2,115.00` |
| `Live` | `Long` | `0.3450` | 71,300,000.00 USD | 0.00 USD | 517.50 USD | `-72.49%` | `1,500.00` |
| `Live` | `Long` | `0.3550` | 71,300,000.00 USD | 0.00 USD | 3,380.00 USD | `-71.69%` | `9,515.00` |
| `Live` | `Long` | `0.3650` | 71,300,000.00 USD | 0.00 USD | 2,260.00 USD | `-70.90%` | `6,200.00` |
| `Live` | `Long` | `0.3850` | 71,290,000.00 USD | 0.00 USD | 503,080.00 USD | `-69.30%` | `1,306,697.00` |
| `Live` | `Long` | `0.3950` | 70,790,000.00 USD | 0.00 USD | 174.59 USD | `-68.50%` | `442.00` |
| `Live` | `Long` | `0.4050` | 70,790,000.00 USD | 0.00 USD | 497.34 USD | `-67.71%` | `1,228.00` |
| `Live` | `Long` | `0.4150` | 70,790,000.00 USD | 0.00 USD | 1,110.00 USD | `-66.91%` | `2,686.00` |
| `Live` | `Long` | `0.4250` | 70,790,000.00 USD | 0.00 USD | 1,210.00 USD | `-66.11%` | `2,847.00` |
| `Live` | `Long` | `0.4350` | 70,790,000.00 USD | 0.00 USD | 7,840.00 USD | `-65.31%` | `18,023.00` |
| `Live` | `Long` | `0.4450` | 70,780,000.00 USD | 0.00 USD | 19,800.00 USD | `-64.52%` | `44,484.00` |
| `Live` | `Long` | `0.4550` | 70,760,000.00 USD | 0.00 USD | 10,340.00 USD | `-63.72%` | `22,719.00` |
| `Live` | `Long` | `0.4650` | 70,750,000.00 USD | 0.00 USD | 179.96 USD | `-62.92%` | `387.00` |
| `Live` | `Long` | `0.4750` | 70,750,000.00 USD | 0.00 USD | 1,180.00 USD | `-62.12%` | `2,475.00` |
| `Live` | `Long` | `0.4850` | 70,750,000.00 USD | 0.00 USD | 9,470.00 USD | `-61.33%` | `19,518.00` |
| `Live` | `Long` | `0.5050` | 70,740,000.00 USD | 0.00 USD | 188.87 USD | `-59.73%` | `374.00` |
| `Live` | `Long` | `0.5150` | 70,740,000.00 USD | 0.00 USD | 4,360.00 USD | `-58.93%` | `8,470.00` |
| `Live` | `Long` | `0.5250` | 70,730,000.00 USD | 0.00 USD | 6,570.00 USD | `-58.14%` | `12,505.00` |
| `Live` | `Long` | `0.5350` | 70,730,000.00 USD | 0.00 USD | 1,700.00 USD | `-57.34%` | `3,171.00` |
| `Live` | `Long` | `0.5450` | 70,730,000.00 USD | 0.00 USD | 3,260.00 USD | `-56.54%` | `5,989.00` |
| `Live` | `Long` | `0.5550` | 70,720,000.00 USD | 0.00 USD | 2,020.00 USD | `-55.75%` | `3,644.00` |
| `Live` | `Long` | `0.5650` | 70,720,000.00 USD | 0.00 USD | 162,700.00 USD | `-54.95%` | `287,957.00` |
| `Live` | `Long` | `0.5750` | 70,560,000.00 USD | 0.00 USD | 8,170.00 USD | `-54.15%` | `14,208.00` |
| `Live` | `Long` | `0.5950` | 70,550,000.00 USD | 0.00 USD | 4,040.00 USD | `-52.56%` | `6,788.00` |
| `Live` | `Long` | `0.6050` | 70,550,000.00 USD | 0.00 USD | 20,150.00 USD | `-51.76%` | `33,298.00` |
| `Live` | `Long` | `0.6150` | 70,530,000.00 USD | 0.00 USD | 36,310.00 USD | `-50.96%` | `59,041.00` |
| `Live` | `Long` | `0.6250` | 70,490,000.00 USD | 0.00 USD | 1,130.00 USD | `-50.16%` | `1,803.00` |
| `Live` | `Long` | `0.6350` | 70,490,000.00 USD | 0.00 USD | 12,730.00 USD | `-49.37%` | `20,044.00` |
| `Live` | `Long` | `0.6450` | 70,480,000.00 USD | 0.00 USD | 18,960.00 USD | `-48.57%` | `29,393.00` |
| `Live` | `Long` | `0.6550` | 70,460,000.00 USD | 0.00 USD | 7,470.00 USD | `-47.77%` | `11,401.00` |
| `Live` | `Long` | `0.6650` | 70,450,000.00 USD | 0.00 USD | 27,220.00 USD | `-46.97%` | `40,929.00` |
| `Live` | `Long` | `0.6750` | 70,420,000.00 USD | 0.00 USD | 37,010.00 USD | `-46.18%` | `54,836.00` |
| `Live` | `Long` | `0.6850` | 70,390,000.00 USD | 0.00 USD | 2,910.00 USD | `-45.38%` | `4,255.00` |
| `Live` | `Long` | `0.6950` | 70,380,000.00 USD | 0.00 USD | 24,280.00 USD | `-44.58%` | `34,940.00` |
| `Live` | `Long` | `0.7050` | 70,360,000.00 USD | 0.00 USD | 176,640.00 USD | `-43.78%` | `250,556.00` |
| `Live` | `Long` | `0.7150` | 70,180,000.00 USD | 0.00 USD | 78,860.00 USD | `-42.99%` | `110,288.00` |
| `Live` | `Long` | `0.7250` | 70,100,000.00 USD | 0.00 USD | 216,700.00 USD | `-42.19%` | `298,897.00` |
| `Live` | `Long` | `0.7350` | 69,890,000.00 USD | 0.00 USD | 61,790.00 USD | `-41.39%` | `84,072.00` |
| `Live` | `Long` | `0.7450` | 69,820,000.00 USD | 0.00 USD | 117,880.00 USD | `-40.60%` | `158,223.00` |
| `Live` | `Long` | `0.7550` | 69,710,000.00 USD | 0.00 USD | 113,690.00 USD | `-39.80%` | `150,580.00` |
| `Live` | `Long` | `0.7650` | 69,590,000.00 USD | 0.00 USD | 2,190.00 USD | `-39.00%` | `2,860.00` |
| `Live` | `Long` | `0.7750` | 69,590,000.00 USD | 0.00 USD | 6,770.00 USD | `-38.20%` | `8,730.00` |
| `Live` | `Long` | `0.7850` | 69,580,000.00 USD | 0.00 USD | 20,130.00 USD | `-37.41%` | `25,638.00` |
| `Live` | `Long` | `0.7950` | 69,560,000.00 USD | 0.00 USD | 11,250.00 USD | `-36.61%` | `14,145.00` |
| `Live` | `Long` | `0.8050` | 69,550,000.00 USD | 0.00 USD | 12,260.00 USD | `-35.81%` | `15,233.00` |
| `Live` | `Long` | `0.8150` | 69,540,000.00 USD | 0.00 USD | 2,900,000.00 USD | `-35.01%` | `3,558,215.00` |
| `Live` | `Long` | `0.8250` | 66,640,000.00 USD | 0.00 USD | 35,830.00 USD | `-34.22%` | `43,435.00` |
| `Live` | `Long` | `0.8350` | 66,600,000.00 USD | 0.00 USD | 39,540.00 USD | `-33.42%` | `47,355.00` |
| `Live` | `Long` | `0.8450` | 66,560,000.00 USD | 0.00 USD | 76,610.00 USD | `-32.62%` | `90,665.00` |
| `Live` | `Long` | `0.8550` | 66,490,000.00 USD | 0.00 USD | 44,630.00 USD | `-31.82%` | `52,196.00` |
| `Live` | `Long` | `0.8650` | 66,440,000.00 USD | 0.00 USD | 39,750.00 USD | `-31.03%` | `45,955.00` |
| `Live` | `Long` | `0.8750` | 66,400,000.00 USD | 0.00 USD | 88,910.00 USD | `-30.23%` | `101,615.00` |
| `Live` | `Long` | `0.8850` | 66,310,000.00 USD | 0.00 USD | 384,970.00 USD | `-29.43%` | `434,990.00` |
| `Live` | `Long` | `0.8950` | 65,930,000.00 USD | 0.00 USD | 101,830.00 USD | `-28.63%` | `113,780.00` |
| `Live` | `Long` | `0.9050` | 65,830,000.00 USD | 0.00 USD | 211,390.00 USD | `-27.84%` | `233,581.00` |
| `Live` | `Long` | `0.9150` | 65,620,000.00 USD | 0.00 USD | 73,280.00 USD | `-27.04%` | `80,086.00` |
| `Live` | `Long` | `0.9250` | 65,540,000.00 USD | 0.00 USD | 120,100.00 USD | `-26.24%` | `129,843.00` |
| `Live` | `Long` | `0.9350` | 65,420,000.00 USD | 0.00 USD | 86,160.00 USD | `-25.44%` | `92,148.00` |
| `Live` | `Long` | `0.9450` | 65,340,000.00 USD | 0.00 USD | 64,920.00 USD | `-24.65%` | `68,694.00` |
| `Live` | `Long` | `0.9550` | 65,270,000.00 USD | 0.00 USD | 109,220.00 USD | `-23.85%` | `114,369.00` |
| `Live` | `Long` | `0.9650` | 65,160,000.00 USD | 0.00 USD | 33,880,000.00 USD | `-23.05%` | `35,110,024.00` |
| `Live` | `Long` | `0.9750` | 31,280,000.00 USD | 0.00 USD | 151,090.00 USD | `-22.26%` | `154,965.00` |
| `Live` | `Long` | `0.9850` | 31,130,000.00 USD | 0.00 USD | 458,840.00 USD | `-21.46%` | `465,827.00` |
| `Live` | `Long` | `0.9950` | 30,670,000.00 USD | 0.00 USD | 93,970.00 USD | `-20.66%` | `94,439.00` |
| `Live` | `Long` | `1.00` | 30,580,000.00 USD | 0.00 USD | 3,050,000.00 USD | `-19.86%` | `3,039,105.00` |
| `Live` | `Long` | `1.01` | 27,520,000.00 USD | 0.00 USD | 828,610.00 USD | `-19.07%` | `816,367.00` |
| `Live` | `Long` | `1.02` | 26,690,000.00 USD | 0.00 USD | 150,730.00 USD | `-18.27%` | `147,055.00` |
| `Live` | `Long` | `1.03` | 26,540,000.00 USD | 0.00 USD | 2,140,000.00 USD | `-17.47%` | `2,064,373.00` |
| `Live` | `Long` | `1.04` | 24,410,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-16.67%` | `1,235,312.00` |
| `Live` | `Long` | `1.05` | 23,120,000.00 USD | 0.00 USD | 1,360,000.00 USD | `-15.88%` | `1,292,575.00` |
| `Live` | `Long` | `1.06` | 21,750,000.00 USD | 0.00 USD | 294,960.00 USD | `-15.08%` | `276,957.00` |
| `Live` | `Long` | `1.07` | 21,460,000.00 USD | 0.00 USD | 472,550.00 USD | `-14.28%` | `439,578.00` |
| `Live` | `Long` | `1.08` | 20,990,000.00 USD | 0.00 USD | 742,690.00 USD | `-13.48%` | `684,506.00` |
| `Live` | `Long` | `1.09` | 20,240,000.00 USD | 0.00 USD | 365,440.00 USD | `-12.69%` | `333,731.00` |
| `Live` | `Long` | `1.10` | 19,880,000.00 USD | 0.00 USD | 68,820.00 USD | `-11.89%` | `62,279.00` |
| `Live` | `Long` | `1.11` | 19,810,000.00 USD | 0.00 USD | 493,430.00 USD | `-11.09%` | `442,537.00` |
| `Live` | `Long` | `1.12` | 19,320,000.00 USD | 0.00 USD | 401,530.00 USD | `-10.29%` | `356,917.00` |
| `Live` | `Long` | `1.14` | 18,910,000.00 USD | 0.00 USD | 202,400.00 USD | `-9.50%` | `178,323.00` |
| `Live` | `Long` | `1.15` | 18,710,000.00 USD | 0.00 USD | 1,770,000.00 USD | `-8.70%` | `1,549,998.00` |
| `Live` | `Long` | `1.16` | 16,940,000.00 USD | 0.00 USD | 320,470.00 USD | `-7.90%` | `277,465.00` |
| `Live` | `Long` | `1.17` | 16,620,000.00 USD | 0.00 USD | 1,520,000.00 USD | `-7.11%` | `1,308,732.00` |
| `Live` | `Long` | `1.18` | 15,090,000.00 USD | 0.00 USD | 495,380.00 USD | `-6.31%` | `421,600.00` |
| `Live` | `Long` | `1.19` | 14,600,000.00 USD | 0.00 USD | 320,270.00 USD | `-5.51%` | `270,266.00` |
| `Live` | `Long` | `1.20` | 14,280,000.00 USD | 0.00 USD | 387,750.00 USD | `-4.71%` | `324,474.00` |
| `Live` | `Long` | `1.21` | 13,890,000.00 USD | 0.00 USD | 1,490,000.00 USD | `-3.92%` | `1,239,522.00` |
| `Live` | `Long` | `1.22` | 12,390,000.00 USD | 0.00 USD | 11,710,000.00 USD | `-3.12%` | `9,634,308.00` |
| `Live` | `Long` | `1.23` | 688,620.00 USD | 0.00 USD | 453,880.00 USD | `-2.32%` | `370,511.00` |
| `Live` | `Long` | `1.24` | 234,750.00 USD | 0.00 USD | 234,750.00 USD | `-1.52%` | `190,080.00` |
| `Live` | `Short` | `1.26` | 4,420.00 USD | 4,420.00 USD | 0.00 USD | `+0.87%` | `3,491.00` |
| `Live` | `Short` | `1.27` | 10,180.00 USD | 5,770.00 USD | 0.00 USD | `+1.67%` | `4,524.00` |
| `Live` | `Short` | `1.28` | 20,320.00 USD | 10,130.00 USD | 0.00 USD | `+2.46%` | `7,885.00` |
| `Live` | `Short` | `1.29` | 31,820.00 USD | 11,500.00 USD | 0.00 USD | `+3.26%` | `8,880.00` |
| `Live` | `Short` | `1.30` | 43,550.00 USD | 11,730.00 USD | 0.00 USD | `+4.06%` | `8,988.00` |
| `Live` | `Short` | `1.31` | 48,450.00 USD | 4,910.00 USD | 0.00 USD | `+4.86%` | `3,732.00` |
| `Live` | `Short` | `1.32` | 105,290.00 USD | 56,840.00 USD | 0.00 USD | `+5.65%` | `42,899.00` |
| `Live` | `Short` | `1.33` | 108,540.00 USD | 3,240.00 USD | 0.00 USD | `+6.45%` | `2,428.00` |
| `Live` | `Short` | `1.34` | 110,780.00 USD | 2,240.00 USD | 0.00 USD | `+7.25%` | `1,669.00` |
| `Live` | `Short` | `1.35` | 119,690.00 USD | 8,910.00 USD | 0.00 USD | `+8.05%` | `6,577.00` |
| `Live` | `Short` | `1.36` | 380,840.00 USD | 261,140.00 USD | 0.00 USD | `+8.84%` | `191,314.00` |
| `Live` | `Short` | `1.39` | 382,110.00 USD | 1,280.00 USD | 0.00 USD | `+10.44%` | `921.00` |
| `Live` | `Short` | `1.40` | 386,300.00 USD | 4,180.00 USD | 0.00 USD | `+11.23%` | `3,000.00` |
| `Live` | `Short` | `1.41` | 387,090.00 USD | 795.23 USD | 0.00 USD | `+12.03%` | `566.00` |
| `Live` | `Short` | `1.42` | 390,690.00 USD | 3,600.00 USD | 0.00 USD | `+12.83%` | `2,544.00` |
| `Live` | `Short` | `1.43` | 484,300.00 USD | 93,610.00 USD | 0.00 USD | `+13.63%` | `65,689.00` |
| `Live` | `Short` | `1.44` | 484,560.00 USD | 258.30 USD | 0.00 USD | `+14.42%` | `180.00` |
| `Live` | `Short` | `1.46` | 486,140.00 USD | 1,590.00 USD | 0.00 USD | `+16.02%` | `1,090.00` |
| `Live` | `Short` | `1.47` | 1,180,000.00 USD | 697,740.00 USD | 0.00 USD | `+16.82%` | `476,270.00` |
| `Live` | `Short` | `1.48` | 1,200,000.00 USD | 18,070.00 USD | 0.00 USD | `+17.61%` | `12,249.00` |
| `Live` | `Short` | `1.49` | 1,330,000.00 USD | 128,990.00 USD | 0.00 USD | `+18.41%` | `86,861.00` |
| `Live` | `Short` | `1.50` | 1,340,000.00 USD | 11,950.00 USD | 0.00 USD | `+19.21%` | `7,994.00` |
| `Live` | `Short` | `1.51` | 1,340,000.00 USD | 915.06 USD | 0.00 USD | `+20.80%` | `604.00` |
| `Live` | `Short` | `1.53` | 1,340,000.00 USD | 776.71 USD | 0.00 USD | `+22.40%` | `506.00` |
| `Live` | `Short` | `1.54` | 1,350,000.00 USD | 2,130.00 USD | 0.00 USD | `+23.20%` | `1,377.00` |
| `Live` | `Short` | `1.55` | 1,350,000.00 USD | 6,800.00 USD | 0.00 USD | `+23.99%` | `4,373.00` |
| `Live` | `Short` | `1.56` | 1,350,000.00 USD | 555.57 USD | 0.00 USD | `+24.79%` | `355.00` |
| `Live` | `Short` | `1.57` | 1,360,000.00 USD | 2,900.00 USD | 0.00 USD | `+25.59%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 1,360,000.00 USD | 123.63 USD | 0.00 USD | `+26.38%` | `78.00` |
| `Live` | `Short` | `1.59` | 1,490,000.00 USD | 129,530.00 USD | 0.00 USD | `+27.18%` | `81,210.00` |
| `Live` | `Short` | `1.60` | 1,490,000.00 USD | 117.16 USD | 0.00 USD | `+27.98%` | `73.00` |
| `Live` | `Short` | `1.61` | 1,490,000.00 USD | 108.21 USD | 0.00 USD | `+28.78%` | `67.00` |
| `Live` | `Short` | `1.62` | 5,920,000.00 USD | 4,430,000.00 USD | 0.00 USD | `+29.57%` | `2,727,698.00` |
| `Live` | `Short` | `1.64` | 5,920,000.00 USD | 3,800.00 USD | 0.00 USD | `+30.37%` | `2,326.00` |
| `Live` | `Short` | `1.66` | 5,920,000.00 USD | 147.30 USD | 0.00 USD | `+31.97%` | `89.00` |
| `Live` | `Short` | `1.67` | 5,920,000.00 USD | 586.08 USD | 0.00 USD | `+32.76%` | `352.00` |
| `Live` | `Short` | `1.68` | 5,930,000.00 USD | 2,170.00 USD | 0.00 USD | `+33.56%` | `1,297.00` |
| `Live` | `Short` | `1.69` | 5,930,000.00 USD | 4,180.00 USD | 0.00 USD | `+34.36%` | `2,483.00` |
| `Live` | `Short` | `1.70` | 5,930,000.00 USD | 1,160.00 USD | 0.00 USD | `+35.16%` | `686.00` |
| `Live` | `Short` | `1.71` | 5,930,000.00 USD | 1,980.00 USD | 0.00 USD | `+35.95%` | `1,163.00` |
| `Live` | `Short` | `1.74` | 5,940,000.00 USD | 3,960.00 USD | 0.00 USD | `+38.35%` | `2,285.00` |
| `Live` | `Short` | `1.75` | 5,940,000.00 USD | 2,730.00 USD | 0.00 USD | `+39.14%` | `1,564.00` |
| `Live` | `Short` | `1.75` | 11,190,000.00 USD | 5,250,000.00 USD | 0.00 USD | `+39.94%` | `2,990,665.00` |
| `Live` | `Short` | `1.76` | 11,200,000.00 USD | 7,340.00 USD | 0.00 USD | `+40.74%` | `4,157.00` |
| `Live` | `Short` | `1.77` | 11,200,000.00 USD | 351.45 USD | 0.00 USD | `+41.54%` | `198.00` |
| `Live` | `Short` | `1.78` | 11,330,000.00 USD | 129,540.00 USD | 0.00 USD | `+42.33%` | `72,574.00` |
| `Live` | `Short` | `1.79` | 11,330,000.00 USD | 2,850.00 USD | 0.00 USD | `+43.13%` | `1,590.00` |
| `Live` | `Short` | `1.80` | 11,330,000.00 USD | 889.87 USD | 0.00 USD | `+43.93%` | `493.00` |
| `Live` | `Short` | `1.81` | 11,330,000.00 USD | 747.78 USD | 0.00 USD | `+44.72%` | `412.00` |
| `Live` | `Short` | `1.82` | 11,330,000.00 USD | 2,020.00 USD | 0.00 USD | `+45.52%` | `1,107.00` |
| `Live` | `Short` | `1.83` | 11,330,000.00 USD | 128.45 USD | 0.00 USD | `+46.32%` | `70.00` |
| `Live` | `Short` | `1.84` | 11,340,000.00 USD | 9,340.00 USD | 0.00 USD | `+47.12%` | `5,061.00` |
| `Live` | `Short` | `1.85` | 11,340,000.00 USD | 428.50 USD | 0.00 USD | `+47.91%` | `231.00` |
| `Live` | `Short` | `1.86` | 14,220,000.00 USD | 2,880,000.00 USD | 0.00 USD | `+48.71%` | `1,541,791.00` |
| `Live` | `Short` | `1.88` | 14,330,000.00 USD | 113,220.00 USD | 0.00 USD | `+49.51%` | `60,386.00` |
| `Live` | `Short` | `1.90` | 14,340,000.00 USD | 4,190.00 USD | 0.00 USD | `+51.10%` | `2,211.00` |
| `Live` | `Short` | `1.91` | 14,340,000.00 USD | 552.45 USD | 0.00 USD | `+51.90%` | `290.00` |
| `Live` | `Short` | `1.92` | 14,340,000.00 USD | 794.73 USD | 0.00 USD | `+52.70%` | `415.00` |
| `Live` | `Short` | `1.93` | 14,650,000.00 USD | 309,300.00 USD | 0.00 USD | `+53.50%` | `160,677.00` |
| `Live` | `Short` | `1.94` | 14,650,000.00 USD | 8,870.00 USD | 0.00 USD | `+54.29%` | `4,584.00` |
| `Live` | `Short` | `1.95` | 14,660,000.00 USD | 3,320.00 USD | 0.00 USD | `+55.09%` | `1,709.00` |
| `Live` | `Short` | `1.96` | 14,660,000.00 USD | 293.25 USD | 0.00 USD | `+55.89%` | `150.00` |
| `Live` | `Short` | `1.97` | 14,890,000.00 USD | 227,680.00 USD | 0.00 USD | `+56.69%` | `115,869.00` |
| `Live` | `Short` | `1.98` | 14,890,000.00 USD | 651.75 USD | 0.00 USD | `+57.48%` | `330.00` |
| `Live` | `Short` | `1.99` | 14,890,000.00 USD | 119.10 USD | 0.00 USD | `+58.28%` | `60.00` |
| `Live` | `Short` | `2.00` | 15,290,000.00 USD | 401,000.00 USD | 0.00 USD | `+59.87%` | `200,000.00` |
| `Live` | `Short` | `2.02` | 15,290,000.00 USD | 1,290.00 USD | 0.00 USD | `+60.67%` | `642.00` |
| `Live` | `Short` | `2.04` | 15,290,000.00 USD | 2,010.00 USD | 0.00 USD | `+62.27%` | `989.00` |
| `Live` | `Short` | `2.04` | 21,250,000.00 USD | 5,960,000.00 USD | 0.00 USD | `+63.06%` | `2,912,713.00` |
| `Live` | `Short` | `2.06` | 21,250,000.00 USD | 460.50 USD | 0.00 USD | `+64.66%` | `223.00` |
| `Live` | `Short` | `2.08` | 21,250,000.00 USD | 1,200.00 USD | 0.00 USD | `+65.46%` | `577.00` |
| `Live` | `Short` | `2.08` | 23,930,000.00 USD | 2,680,000.00 USD | 0.00 USD | `+66.25%` | `1,286,016.00` |
| `Live` | `Short` | `2.10` | 23,930,000.00 USD | 331.01 USD | 0.00 USD | `+67.05%` | `158.00` |
| `Live` | `Short` | `2.10` | 24,180,000.00 USD | 247,230.00 USD | 0.00 USD | `+67.85%` | `117,448.00` |
| `Live` | `Short` | `2.12` | 24,180,000.00 USD | 3,100.00 USD | 0.00 USD | `+68.65%` | `1,468.00` |
| `Live` | `Short` | `2.15` | 24,180,000.00 USD | 1,390.00 USD | 0.00 USD | `+71.84%` | `646.00` |
| `Live` | `Short` | `2.17` | 24,190,000.00 USD | 3,000.00 USD | 0.00 USD | `+73.43%` | `1,379.00` |
| `Live` | `Short` | `2.19` | 24,190,000.00 USD | 301.53 USD | 0.00 USD | `+74.23%` | `138.00` |
| `Live` | `Short` | `2.19` | 24,190,000.00 USD | 201.94 USD | 0.00 USD | `+75.03%` | `92.00` |
| `Live` | `Short` | `2.21` | 24,190,000.00 USD | 873.18 USD | 0.00 USD | `+75.82%` | `396.00` |
| `Live` | `Short` | `2.21` | 24,190,000.00 USD | 2,750.00 USD | 0.00 USD | `+76.62%` | `1,243.00` |
| `Live` | `Short` | `2.23` | 24,270,000.00 USD | 75,280.00 USD | 0.00 USD | `+77.42%` | `33,833.00` |
| `Live` | `Short` | `2.23` | 24,270,000.00 USD | 205.62 USD | 0.00 USD | `+78.21%` | `92.00` |
| `Live` | `Short` | `2.25` | 24,270,000.00 USD | 103.27 USD | 0.00 USD | `+79.01%` | `46.00` |
| `Live` | `Short` | `2.25` | 24,270,000.00 USD | 103.73 USD | 0.00 USD | `+79.81%` | `46.00` |
| `Live` | `Short` | `2.27` | 24,270,000.00 USD | 208.38 USD | 0.00 USD | `+80.61%` | `92.00` |
| `Live` | `Short` | `2.29` | 24,310,000.00 USD | 44,140.00 USD | 0.00 USD | `+82.20%` | `19,317.00` |
| `Live` | `Short` | `2.29` | 24,310,000.00 USD | 459.00 USD | 0.00 USD | `+83.00%` | `200.00` |
| `Live` | `Short` | `2.31` | 24,310,000.00 USD | 2,860.00 USD | 0.00 USD | `+83.80%` | `1,239.00` |
| `Live` | `Short` | `2.31` | 24,320,000.00 USD | 11,850.00 USD | 0.00 USD | `+84.59%` | `5,119.00` |
| `Live` | `Short` | `2.33` | 24,330,000.00 USD | 2,540.00 USD | 0.00 USD | `+85.39%` | `1,093.00` |
| `Live` | `Short` | `2.33` | 24,330,000.00 USD | 144.77 USD | 0.00 USD | `+86.19%` | `62.00` |
| `Live` | `Short` | `2.35` | 24,330,000.00 USD | 222.77 USD | 0.00 USD | `+86.99%` | `95.00` |
| `Live` | `Short` | `2.37` | 24,330,000.00 USD | 108.79 USD | 0.00 USD | `+88.58%` | `46.00` |
| `Live` | `Short` | `2.38` | 24,380,000.00 USD | 56,430.00 USD | 0.00 USD | `+89.38%` | `23,758.00` |
| `Live` | `Short` | `2.38` | 24,610,000.00 USD | 225,350.00 USD | 0.00 USD | `+90.18%` | `94,485.00` |
| `Live` | `Short` | `2.40` | 24,610,000.00 USD | 155.68 USD | 0.00 USD | `+90.97%` | `65.00` |
| `Live` | `Short` | `2.40` | 24,610,000.00 USD | 481.00 USD | 0.00 USD | `+91.77%` | `200.00` |
| `Live` | `Short` | `2.42` | 24,640,000.00 USD | 27,800.00 USD | 0.00 USD | `+93.36%` | `11,463.00` |
| `Live` | `Short` | `2.44` | 24,660,000.00 USD | 18,830.00 USD | 0.00 USD | `+94.16%` | `7,734.00` |
| `Live` | `Short` | `2.44` | 24,660,000.00 USD | 2,840.00 USD | 0.00 USD | `+94.96%` | `1,160.00` |
| `Live` | `Short` | `2.46` | 24,750,000.00 USD | 94,260.00 USD | 0.00 USD | `+95.76%` | `38,397.00` |
| `Live` | `Short` | `2.48` | 24,750,000.00 USD | 337.96 USD | 0.00 USD | `+98.15%` | `136.00` |
| `Live` | `Short` | `2.50` | 24,760,000.00 USD | 4,370.00 USD | 0.00 USD | `+99.74%` | `1,744.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 1,210,000.00 USD | 0.00 USD | 112.45 USD | `-79.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 1,210,000.00 USD | 0.00 USD | 139.12 USD | `-70.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 1,210,000.00 USD | 0.00 USD | 200.86 USD | `-66.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 1,210,000.00 USD | 0.00 USD | 408.51 USD | `-64.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 1,210,000.00 USD | 0.00 USD | 273.00 USD | `-63.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 1,210,000.00 USD | 0.00 USD | 151.12 USD | `-62.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 1,210,000.00 USD | 0.00 USD | 142.50 USD | `-62.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 1,210,000.00 USD | 0.00 USD | 145.50 USD | `-61.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 1,210,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 1,210,000.00 USD | 0.00 USD | 285.82 USD | `-58.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 1,210,000.00 USD | 0.00 USD | 306.60 USD | `-58.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 1,210,000.00 USD | 0.00 USD | 121.55 USD | `-55.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 1,210,000.00 USD | 0.00 USD | 374.60 USD | `-54.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 1,210,000.00 USD | 0.00 USD | 100.62 USD | `-53.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 1,210,000.00 USD | 0.00 USD | 203.75 USD | `-50.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 1,210,000.00 USD | 0.00 USD | 791.85 USD | `-49.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 1,210,000.00 USD | 0.00 USD | 573.40 USD | `-48.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 1,210,000.00 USD | 0.00 USD | 364.18 USD | `-47.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 1,210,000.00 USD | 0.00 USD | 3,220.00 USD | `-46.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 1,200,000.00 USD | 0.00 USD | 503.55 USD | `-46.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 1,200,000.00 USD | 0.00 USD | 480.19 USD | `-45.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 1,200,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 1,190,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 1,190,000.00 USD | 0.00 USD | 228.80 USD | `-42.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 1,190,000.00 USD | 0.00 USD | 536.50 USD | `-42.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 1,190,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 1,190,000.00 USD | 0.00 USD | 2,880.00 USD | `-39.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 1,180,000.00 USD | 0.00 USD | 1,080.00 USD | `-36.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 1,180,000.00 USD | 0.00 USD | 798.57 USD | `-31.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 1,180,000.00 USD | 0.00 USD | 690.38 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 1,180,000.00 USD | 0.00 USD | 1,210.00 USD | `-29.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 1,180,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 1,180,000.00 USD | 0.00 USD | 838.94 USD | `-27.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 1,170,000.00 USD | 0.00 USD | 338.55 USD | `-27.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 1,170,000.00 USD | 0.00 USD | 1,060.00 USD | `-26.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 1,170,000.00 USD | 0.00 USD | 1,180.00 USD | `-25.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 1,170,000.00 USD | 0.00 USD | 112.46 USD | `-24.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 1,170,000.00 USD | 0.00 USD | 2,360.00 USD | `-23.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 1,170,000.00 USD | 0.00 USD | 3,910.00 USD | `-23.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 1,170,000.00 USD | 0.00 USD | 7,230.00 USD | `-22.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 1,160,000.00 USD | 0.00 USD | 5,000.00 USD | `-21.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 1,150,000.00 USD | 0.00 USD | 661.67 USD | `-20.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 1,150,000.00 USD | 0.00 USD | 16,410.00 USD | `-19.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 1,140,000.00 USD | 0.00 USD | 6,900.00 USD | `-19.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 1,130,000.00 USD | 0.00 USD | 2,020.00 USD | `-18.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 1,130,000.00 USD | 0.00 USD | 38,000.00 USD | `-17.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 1,090,000.00 USD | 0.00 USD | 3,490.00 USD | `-16.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 1,090,000.00 USD | 0.00 USD | 2,110.00 USD | `-15.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,080,000.00 USD | 0.00 USD | 3,960.00 USD | `-15.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,080,000.00 USD | 0.00 USD | 48,460.00 USD | `-14.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,030,000.00 USD | 0.00 USD | 868.00 USD | `-13.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,030,000.00 USD | 0.00 USD | 38,150.00 USD | `-12.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 992,730.00 USD | 0.00 USD | 3,700.00 USD | `-11.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 989,030.00 USD | 0.00 USD | 11,630.00 USD | `-11.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 977,400.00 USD | 0.00 USD | 80,050.00 USD | `-10.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 897,350.00 USD | 0.00 USD | 13,830.00 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 883,520.00 USD | 0.00 USD | 14,460.00 USD | `-8.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 869,060.00 USD | 0.00 USD | 30,090.00 USD | `-7.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 838,970.00 USD | 0.00 USD | 38,810.00 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 800,160.00 USD | 0.00 USD | 7,640.00 USD | `-6.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 792,520.00 USD | 0.00 USD | 145,060.00 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 647,460.00 USD | 0.00 USD | 145,280.00 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 502,180.00 USD | 0.00 USD | 214,020.00 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 288,160.00 USD | 0.00 USD | 122,190.00 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 165,970.00 USD | 0.00 USD | 57,920.00 USD | `-2.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 108,050.00 USD | 0.00 USD | 77,520.00 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 30,530.00 USD | 0.00 USD | 30,530.00 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 15,880.00 USD | 15,880.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 110,030.00 USD | 94,150.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 117,350.00 USD | 7,310.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 356,080.00 USD | 238,730.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 419,040.00 USD | 62,960.00 USD | 0.00 USD | `+3.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 467,000.00 USD | 47,960.00 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 860,930.00 USD | 393,930.00 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,070,000.00 USD | 207,660.00 USD | 0.00 USD | `+5.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,100,000.00 USD | 36,000.00 USD | 0.00 USD | `+6.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,300,000.00 USD | 196,480.00 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,320,000.00 USD | 15,250.00 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,590,000.00 USD | 275,680.00 USD | 0.00 USD | `+8.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,670,000.00 USD | 82,920.00 USD | 0.00 USD | `+9.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,730,000.00 USD | 50,450.00 USD | 0.00 USD | `+10.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,730,000.00 USD | 6,060.00 USD | 0.00 USD | `+11.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 6,090,000.00 USD | 4,360,000.00 USD | 0.00 USD | `+12.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 6,090,000.00 USD | 1,980.00 USD | 0.00 USD | `+12.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 6,100,000.00 USD | 6,850.00 USD | 0.00 USD | `+13.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,180,000.00 USD | 80,260.00 USD | 0.00 USD | `+14.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,390,000.00 USD | 213,140.00 USD | 0.00 USD | `+15.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,400,000.00 USD | 7,510.00 USD | 0.00 USD | `+16.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,420,000.00 USD | 22,800.00 USD | 0.00 USD | `+16.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,530,000.00 USD | 107,960.00 USD | 0.00 USD | `+17.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,580,000.00 USD | 55,680.00 USD | 0.00 USD | `+18.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,600,000.00 USD | 13,980.00 USD | 0.00 USD | `+19.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,640,000.00 USD | 43,080.00 USD | 0.00 USD | `+20.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,650,000.00 USD | 10,320.00 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,740,000.00 USD | 93,330.00 USD | 0.00 USD | `+21.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,790,000.00 USD | 45,620.00 USD | 0.00 USD | `+22.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,810,000.00 USD | 22,220.00 USD | 0.00 USD | `+23.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,810,000.00 USD | 2,690.00 USD | 0.00 USD | `+23.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,820,000.00 USD | 7,340.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,830,000.00 USD | 5,940.00 USD | 0.00 USD | `+25.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,840,000.00 USD | 11,870.00 USD | 0.00 USD | `+26.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,990,000.00 USD | 148,780.00 USD | 0.00 USD | `+27.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,990,000.00 USD | 1,840.00 USD | 0.00 USD | `+27.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 7,070,000.00 USD | 80,320.00 USD | 0.00 USD | `+28.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 7,070,000.00 USD | 464.75 USD | 0.00 USD | `+29.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,260,000.00 USD | 184,610.00 USD | 0.00 USD | `+30.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,260,000.00 USD | 2,670.00 USD | 0.00 USD | `+31.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,280,000.00 USD | 18,210.00 USD | 0.00 USD | `+31.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,280,000.00 USD | 6,080.00 USD | 0.00 USD | `+32.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,300,000.00 USD | 18,400.00 USD | 0.00 USD | `+33.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,370,000.00 USD | 70,850.00 USD | 0.00 USD | `+34.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,370,000.00 USD | 2,770.00 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,610,000.00 USD | 240,380.00 USD | 0.00 USD | `+35.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,630,000.00 USD | 14,030.00 USD | 0.00 USD | `+36.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,630,000.00 USD | 5,910.00 USD | 0.00 USD | `+37.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,680,000.00 USD | 44,100.00 USD | 0.00 USD | `+38.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,680,000.00 USD | 4,710.00 USD | 0.00 USD | `+39.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,690,000.00 USD | 5,510.00 USD | 0.00 USD | `+39.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,710,000.00 USD | 21,720.00 USD | 0.00 USD | `+40.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,840,000.00 USD | 124,780.00 USD | 0.00 USD | `+41.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,930,000.00 USD | 96,600.00 USD | 0.00 USD | `+42.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 7,970,000.00 USD | 36,490.00 USD | 0.00 USD | `+43.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 7,970,000.00 USD | 254.51 USD | 0.00 USD | `+43.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 7,970,000.00 USD | 2,530.00 USD | 0.00 USD | `+44.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 7,970,000.00 USD | 1,830.00 USD | 0.00 USD | `+45.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 7,980,000.00 USD | 7,280.00 USD | 0.00 USD | `+46.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 7,980,000.00 USD | 1,010.00 USD | 0.00 USD | `+47.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 7,990,000.00 USD | 8,390.00 USD | 0.00 USD | `+47.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 7,990,000.00 USD | 4,250.00 USD | 0.00 USD | `+49.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 7,990,000.00 USD | 591.89 USD | 0.00 USD | `+50.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 8,030,000.00 USD | 38,610.00 USD | 0.00 USD | `+51.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 8,070,000.00 USD | 38,940.00 USD | 0.00 USD | `+51.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 8,080,000.00 USD | 7,410.00 USD | 0.00 USD | `+52.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 8,080,000.00 USD | 265.10 USD | 0.00 USD | `+54.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 8,080,000.00 USD | 2,040.00 USD | 0.00 USD | `+55.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 8,080,000.00 USD | 1,070.00 USD | 0.00 USD | `+55.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,100,000.00 USD | 14,120.00 USD | 0.00 USD | `+56.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,100,000.00 USD | 4,010.00 USD | 0.00 USD | `+57.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,100,000.00 USD | 325.54 USD | 0.00 USD | `+58.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,110,000.00 USD | 7,020.00 USD | 0.00 USD | `+59.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,230,000.00 USD | 123,150.00 USD | 0.00 USD | `+59.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,230,000.00 USD | 781.82 USD | 0.00 USD | `+60.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,230,000.00 USD | 222.75 USD | 0.00 USD | `+61.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,230,000.00 USD | 862.84 USD | 0.00 USD | `+62.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,230,000.00 USD | 382.41 USD | 0.00 USD | `+63.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,240,000.00 USD | 3,420.00 USD | 0.00 USD | `+64.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,240,000.00 USD | 661.93 USD | 0.00 USD | `+65.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,360,000.00 USD | 124,400.00 USD | 0.00 USD | `+67.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,360,000.00 USD | 1,580.00 USD | 0.00 USD | `+67.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,380,000.00 USD | 13,900.00 USD | 0.00 USD | `+69.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,400,000.00 USD | 24,840.00 USD | 0.00 USD | `+71.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,450,000.00 USD | 50,580.00 USD | 0.00 USD | `+71.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,460,000.00 USD | 2,690.00 USD | 0.00 USD | `+72.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,480,000.00 USD | 20,370.00 USD | 0.00 USD | `+75.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,630,000.00 USD | 151,380.00 USD | 0.00 USD | `+76.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 8,640,000.00 USD | 7,340.00 USD | 0.00 USD | `+78.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,640,000.00 USD | 3,120.00 USD | 0.00 USD | `+81.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,640,000.00 USD | 1,140.00 USD | 0.00 USD | `+82.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,650,000.00 USD | 12,150.00 USD | 0.00 USD | `+83.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,650,000.00 USD | 370.40 USD | 0.00 USD | `+84.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,650,000.00 USD | 733.19 USD | 0.00 USD | `+86.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,650,000.00 USD | 2,410.00 USD | 0.00 USD | `+88.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,660,000.00 USD | 475.00 USD | 0.00 USD | `+89.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,660,000.00 USD | 2,540.00 USD | 0.00 USD | `+90.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,660,000.00 USD | 1,590.00 USD | 0.00 USD | `+91.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,660,000.00 USD | 1,370.00 USD | 0.00 USD | `+92.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,680,000.00 USD | 19,590.00 USD | 0.00 USD | `+93.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,690,000.00 USD | 4,580.00 USD | 0.00 USD | `+94.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,690,000.00 USD | 8,110.00 USD | 0.00 USD | `+95.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,700,000.00 USD | 3,420.00 USD | 0.00 USD | `+98.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,700,000.00 USD | 124.75 USD | 0.00 USD | `+98.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,730,000.00 USD | 30,920.00 USD | 0.00 USD | `+99.74%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `1.11` | 29,660,000.00 USD | 0.00 USD | 29,660,000.00 USD | 17,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.11` | 55,470,000.00 USD | 0.00 USD | 55,470,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.11` | 29,640,000.00 USD | 0.00 USD | 29,640,000.00 USD | 18,710.00 USD | 0.00 USD | 119,620.00 USD |
| `1D` | `1.11` | 29,500,000.00 USD | 0.00 USD | 29,500,000.00 USD | 0.00 USD | 2,260.00 USD | 0.00 USD |
| `7D` | `1.11` | 55,440,000.00 USD | 0.00 USD | 55,440,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `1D` | `1.12` | 29,500,000.00 USD | 0.00 USD | 29,500,000.00 USD | 0.00 USD | 0.00 USD | 8,820.00 USD |
| `7D` | `1.12` | 55,430,000.00 USD | 0.00 USD | 55,430,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 29,490,000.00 USD | 0.00 USD | 29,490,000.00 USD | 0.00 USD | 46,860.00 USD | 5,360.00 USD |
| `1D` | `1.12` | 29,440,000.00 USD | 0.00 USD | 29,440,000.00 USD | 0.00 USD | 1,390.00 USD | 0.00 USD |
| `7D` | `1.12` | 55,350,000.00 USD | 0.00 USD | 55,350,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD |
| `7D` | `1.12` | 55,350,000.00 USD | 0.00 USD | 55,350,000.00 USD | 0.00 USD | 1,270.00 USD | 0.00 USD |
| `1D` | `1.13` | 29,440,000.00 USD | 0.00 USD | 29,440,000.00 USD | 0.00 USD | 783.15 USD | 0.00 USD |
| `1D` | `1.13` | 29,440,000.00 USD | 0.00 USD | 29,440,000.00 USD | 0.00 USD | 42,490.00 USD | 78,200.00 USD |
| `7D` | `1.13` | 55,350,000.00 USD | 0.00 USD | 55,350,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 29,320,000.00 USD | 0.00 USD | 29,320,000.00 USD | 0.00 USD | 66,770.00 USD | 166,310.00 USD |
| `7D` | `1.13` | 55,160,000.00 USD | 0.00 USD | 55,160,000.00 USD | 5,450.00 USD | 3,410.00 USD | 3,970.00 USD |
| `1D` | `1.13` | 29,080,000.00 USD | 0.00 USD | 29,080,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD |
| `7D` | `1.13` | 55,140,000.00 USD | 0.00 USD | 55,140,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD |
| `1D` | `1.14` | 29,030,000.00 USD | 0.00 USD | 29,030,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD |
| `7D` | `1.14` | 54,670,000.00 USD | 0.00 USD | 54,670,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD |
| `1D` | `1.14` | 28,980,000.00 USD | 0.00 USD | 28,980,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD |
| `7D` | `1.14` | 54,420,000.00 USD | 0.00 USD | 54,420,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 28,890,000.00 USD | 0.00 USD | 28,890,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.14` | 54,320,000.00 USD | 0.00 USD | 54,320,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 28,860,000.00 USD | 0.00 USD | 28,860,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD |
| `7D` | `1.14` | 54,310,000.00 USD | 0.00 USD | 54,310,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 28,800,000.00 USD | 0.00 USD | 28,800,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD |
| `7D` | `1.14` | 54,250,000.00 USD | 0.00 USD | 54,250,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.15` | 28,660,000.00 USD | 0.00 USD | 28,660,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD |
| `7D` | `1.15` | 54,130,000.00 USD | 0.00 USD | 54,130,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.15` | 54,120,000.00 USD | 0.00 USD | 54,120,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `1D` | `1.15` | 28,620,000.00 USD | 0.00 USD | 28,620,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 53,980,000.00 USD | 0.00 USD | 53,980,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD |
| `7D` | `1.15` | 53,620,000.00 USD | 0.00 USD | 53,620,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.15` | 28,600,000.00 USD | 0.00 USD | 28,600,000.00 USD | 4,040.00 USD | 11,230.00 USD | 185,060.00 USD |
| `7D` | `1.15` | 53,460,000.00 USD | 0.00 USD | 53,460,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `1D` | `1.16` | 28,400,000.00 USD | 0.00 USD | 28,400,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD |
| `7D` | `1.16` | 53,080,000.00 USD | 0.00 USD | 53,080,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `1D` | `1.16` | 28,060,000.00 USD | 0.00 USD | 28,060,000.00 USD | 29,120.00 USD | 9,570.00 USD | 31,170.00 USD |
| `7D` | `1.16` | 52,430,000.00 USD | 0.00 USD | 52,430,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD |
| `1D` | `1.16` | 27,990,000.00 USD | 0.00 USD | 27,990,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD |
| `7D` | `1.16` | 51,630,000.00 USD | 0.00 USD | 51,630,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `1D` | `1.16` | 27,680,000.00 USD | 0.00 USD | 27,680,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD |
| `7D` | `1.16` | 51,110,000.00 USD | 0.00 USD | 51,110,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.16` | 27,060,000.00 USD | 0.00 USD | 27,060,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD |
| `7D` | `1.16` | 50,090,000.00 USD | 0.00 USD | 50,090,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.17` | 26,440,000.00 USD | 0.00 USD | 26,440,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD |
| `7D` | `1.17` | 48,710,000.00 USD | 0.00 USD | 48,710,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.17` | 26,220,000.00 USD | 0.00 USD | 26,220,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD |
| `7D` | `1.17` | 48,080,000.00 USD | 0.00 USD | 48,080,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD |
| `1D` | `1.17` | 25,910,000.00 USD | 0.00 USD | 25,910,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD |
| `7D` | `1.17` | 46,700,000.00 USD | 0.00 USD | 46,700,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 25,750,000.00 USD | 0.00 USD | 25,750,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD |
| `7D` | `1.17` | 45,200,000.00 USD | 0.00 USD | 45,200,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 25,580,000.00 USD | 0.00 USD | 25,580,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD |
| `7D` | `1.17` | 43,810,000.00 USD | 0.00 USD | 43,810,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.18` | 25,320,000.00 USD | 0.00 USD | 25,320,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD |
| `7D` | `1.18` | 43,010,000.00 USD | 0.00 USD | 43,010,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD |
| `1D` | `1.18` | 24,980,000.00 USD | 0.00 USD | 24,980,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD |
| `7D` | `1.18` | 42,130,000.00 USD | 0.00 USD | 42,130,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `1D` | `1.18` | 24,850,000.00 USD | 0.00 USD | 24,850,000.00 USD | 93,410.00 USD | 41,360.00 USD | 49,320.00 USD |
| `7D` | `1.18` | 41,670,000.00 USD | 0.00 USD | 41,670,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `1D` | `1.18` | 24,670,000.00 USD | 0.00 USD | 24,670,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD |
| `7D` | `1.18` | 40,960,000.00 USD | 0.00 USD | 40,960,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `1D` | `1.18` | 24,640,000.00 USD | 0.00 USD | 24,640,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD |
| `7D` | `1.18` | 40,580,000.00 USD | 0.00 USD | 40,580,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `1D` | `1.19` | 24,530,000.00 USD | 0.00 USD | 24,530,000.00 USD | 92,110.00 USD | 7,460.00 USD | 27,490.00 USD |
| `7D` | `1.19` | 40,450,000.00 USD | 0.00 USD | 40,450,000.00 USD | 123,240.00 USD | 97,270.00 USD | 289,750.00 USD |
| `1D` | `1.19` | 24,400,000.00 USD | 0.00 USD | 24,400,000.00 USD | 16,710.00 USD | 139,070.00 USD | 316,290.00 USD |
| `7D` | `1.19` | 39,940,000.00 USD | 0.00 USD | 39,940,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD |
| `1D` | `1.19` | 23,930,000.00 USD | 0.00 USD | 23,930,000.00 USD | 188,800.00 USD | 7,100.00 USD | 309,220.00 USD |
| `7D` | `1.19` | 39,170,000.00 USD | 0.00 USD | 39,170,000.00 USD | 182,110.00 USD | 132,500.00 USD | 278,870.00 USD |
| `1D` | `1.19` | 23,420,000.00 USD | 0.00 USD | 23,420,000.00 USD | 48,220.00 USD | 10,480.00 USD | 70,380.00 USD |
| `7D` | `1.19` | 38,580,000.00 USD | 0.00 USD | 38,580,000.00 USD | 152,830.00 USD | 265,920.00 USD | 273,010.00 USD |
| `1D` | `1.19` | 23,290,000.00 USD | 0.00 USD | 23,290,000.00 USD | 42,050.00 USD | 216,220.00 USD | 112,870.00 USD |
| `7D` | `1.19` | 37,880,000.00 USD | 0.00 USD | 37,880,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD |
| `1D` | `1.20` | 22,920,000.00 USD | 0.00 USD | 22,920,000.00 USD | 43,900.00 USD | 14,200.00 USD | 20,370.00 USD |
| `7D` | `1.20` | 37,220,000.00 USD | 0.00 USD | 37,220,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 22,840,000.00 USD | 0.00 USD | 22,840,000.00 USD | 27,320.00 USD | 6,070.00 USD | 8,200.00 USD |
| `7D` | `1.20` | 36,510,000.00 USD | 0.00 USD | 36,510,000.00 USD | 5,350.00 USD | 101,030.00 USD | 187,830.00 USD |
| `7D` | `1.20` | 36,220,000.00 USD | 0.00 USD | 36,220,000.00 USD | 67,200.00 USD | 152,970.00 USD | 201,810.00 USD |
| `1D` | `1.20` | 22,800,000.00 USD | 0.00 USD | 22,800,000.00 USD | 0.00 USD | 28,540.00 USD | 0.00 USD |
| `7D` | `1.20` | 35,800,000.00 USD | 0.00 USD | 35,800,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD |
| `1D` | `1.20` | 22,770,000.00 USD | 0.00 USD | 22,770,000.00 USD | 35,450.00 USD | 4,970.00 USD | 0.00 USD |
| `7D` | `1.20` | 35,720,000.00 USD | 0.00 USD | 35,720,000.00 USD | 202,570.00 USD | 146,780.00 USD | 534,000.00 USD |
| `1D` | `1.21` | 22,730,000.00 USD | 0.00 USD | 22,730,000.00 USD | 4,360.00 USD | 297,650.00 USD | 195,510.00 USD |
| `7D` | `1.21` | 34,840,000.00 USD | 0.00 USD | 34,840,000.00 USD | 0.00 USD | 17,680.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 22,240,000.00 USD | 0.00 USD | 22,240,000.00 USD | 81,900.00 USD | 32,170.00 USD | 415,780.00 USD |
| `7D` | `1.21` | 34,740,000.00 USD | 0.00 USD | 34,740,000.00 USD | 80,450.00 USD | 7,260.00 USD | 9,940.00 USD |
| `1D` | `1.21` | 21,710,000.00 USD | 0.00 USD | 21,710,000.00 USD | 220,830.00 USD | 67,350.00 USD | 14,960.00 USD |
| `7D` | `1.21` | 34,640,000.00 USD | 0.00 USD | 34,640,000.00 USD | 659,990.00 USD | 518,690.00 USD | 368,310.00 USD |
| `1D` | `1.21` | 21,400,000.00 USD | 0.00 USD | 21,400,000.00 USD | 99,310.00 USD | 425,250.00 USD | 714,910.00 USD |
| `7D` | `1.21` | 33,100,000.00 USD | 0.00 USD | 33,100,000.00 USD | 180,260.00 USD | 264,440.00 USD | 802,150.00 USD |
| `1D` | `1.21` | 20,160,000.00 USD | 0.00 USD | 20,160,000.00 USD | 419,060.00 USD | 161,150.00 USD | 591,990.00 USD |
| `7D` | `1.21` | 31,850,000.00 USD | 0.00 USD | 31,850,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD |
| `1D` | `1.22` | 18,990,000.00 USD | 0.00 USD | 18,990,000.00 USD | 65,710.00 USD | 6,610.00 USD | 0.00 USD |
| `7D` | `1.22` | 31,450,000.00 USD | 0.00 USD | 31,450,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD |
| `1D` | `1.22` | 18,920,000.00 USD | 0.00 USD | 18,920,000.00 USD | 118,950.00 USD | 1,870.00 USD | 203,120.00 USD |
| `7D` | `1.22` | 31,270,000.00 USD | 0.00 USD | 31,270,000.00 USD | 157,620.00 USD | 396,140.00 USD | 0.00 USD |
| `1D` | `1.22` | 18,600,000.00 USD | 0.00 USD | 18,600,000.00 USD | 261,180.00 USD | 384,120.00 USD | 178,880.00 USD |
| `7D` | `1.22` | 30,720,000.00 USD | 0.00 USD | 30,720,000.00 USD | 256,390.00 USD | 4,120.00 USD | 40,620.00 USD |
| `1D` | `1.22` | 17,770,000.00 USD | 0.00 USD | 17,770,000.00 USD | 12,860.00 USD | 4,180.00 USD | 131,570.00 USD |
| `7D` | `1.22` | 30,420,000.00 USD | 0.00 USD | 30,420,000.00 USD | 159,150.00 USD | 10,480.00 USD | 328,940.00 USD |
| `1D` | `1.22` | 17,620,000.00 USD | 0.00 USD | 17,620,000.00 USD | 0.00 USD | 486,010.00 USD | 0.00 USD |
| `7D` | `1.22` | 29,920,000.00 USD | 0.00 USD | 29,920,000.00 USD | 0.00 USD | 197,690.00 USD | 1,020,000.00 USD |
| `1D` | `1.23` | 17,140,000.00 USD | 0.00 USD | 17,140,000.00 USD | 489,230.00 USD | 57,290.00 USD | 2,320,000.00 USD |
| `7D` | `1.23` | 28,700,000.00 USD | 0.00 USD | 28,700,000.00 USD | 627,450.00 USD | 381,850.00 USD | 4,910.00 USD |
| `1D` | `1.23` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 8,660.00 USD | 5,580.00 USD | 0.00 USD |
| `7D` | `1.23` | 27,690,000.00 USD | 0.00 USD | 27,690,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD |
| `1D` | `1.23` | 14,260,000.00 USD | 0.00 USD | 14,260,000.00 USD | 105,710.00 USD | 213,020.00 USD | 551,100.00 USD |
| `7D` | `1.23` | 27,230,000.00 USD | 0.00 USD | 27,230,000.00 USD | 0.00 USD | 1,110,000.00 USD | 995,690.00 USD |
| `1D` | `1.23` | 13,390,000.00 USD | 0.00 USD | 13,390,000.00 USD | 319,240.00 USD | 1,170,000.00 USD | 0.00 USD |
| `7D` | `1.23` | 25,130,000.00 USD | 0.00 USD | 25,130,000.00 USD | 782,590.00 USD | 485,710.00 USD | 8,010.00 USD |
| `1D` | `1.23` | 11,900,000.00 USD | 0.00 USD | 11,900,000.00 USD | 281,800.00 USD | 199,040.00 USD | 831,560.00 USD |
| `7D` | `1.23` | 23,850,000.00 USD | 0.00 USD | 23,850,000.00 USD | 1,040,000.00 USD | 597,200.00 USD | 112,990.00 USD |
| `1D` | `1.24` | 10,590,000.00 USD | 0.00 USD | 10,590,000.00 USD | 433,890.00 USD | 0.00 USD | 39,570.00 USD |
| `7D` | `1.24` | 22,100,000.00 USD | 0.00 USD | 22,100,000.00 USD | 996,240.00 USD | 998,790.00 USD | 66,130.00 USD |
| `1D` | `1.24` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 0.00 USD | 478,500.00 USD | 0.00 USD |
| `7D` | `1.24` | 20,040,000.00 USD | 0.00 USD | 20,040,000.00 USD | 1,640,000.00 USD | 1,500,000.00 USD | 719,360.00 USD |
| `1D` | `1.24` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 0.00 USD | 114,160.00 USD | 0.00 USD |
| `7D` | `1.24` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.24` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 1,320,000.00 USD |
| `7D` | `1.24` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 1,820,000.00 USD | 374,420.00 USD | 1,940,000.00 USD |
| `1D` | `1.24` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 321,060.00 USD | 774,420.00 USD | 560,940.00 USD |
| `7D` | `1.24` | 10,270,000.00 USD | 0.00 USD | 10,270,000.00 USD | 896,470.00 USD | 0.00 USD | 1,020,000.00 USD |
| `1D` | `1.25` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 1,400,000.00 USD | 385,630.00 USD | 2,330,000.00 USD |
| `7D` | `1.25` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 3,440,000.00 USD | 923,130.00 USD | 1,670,000.00 USD |
| `1D` | `1.25` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 1,150,000.00 USD | 567,630.00 USD | 707,240.00 USD |
| `7D` | `1.25` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 1,060,000.00 USD | 815,140.00 USD | 2,750,000.00 USD |
| `7D` | `1.25` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 2,720,000.00 USD | 0.00 USD | 51,920.00 USD |
| `7D` | `1.25` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 2,720,000.00 USD | 0.00 USD | 51,920.00 USD |
| `1D` | `1.25` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 198,150.00 USD | 0.00 USD | 6,920.00 USD |
| `7D` | `1.25` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 2,810,000.00 USD | 0.00 USD | 44,180.00 USD |
| `1D` | `1.25` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 635,790.00 USD | 0.00 USD | 4,230.00 USD |
| `7D` | `1.25` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 1,240,000.00 USD | 0.00 USD | 104,700.00 USD |
| `1D` | `1.25` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 794,390.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 172,030.00 USD | 0.00 USD | 18,740.00 USD |
| `1D` | `1.26` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 803,540.00 USD | 2,600.00 USD | 0.00 USD |
| `1D` | `1.26` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 86,570.00 USD | 3,600.00 USD | 0.00 USD |
| `7D` | `1.26` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 63,380.00 USD | 2,060.00 USD | 611,230.00 USD |
| `7D` | `1.26` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 381,210.00 USD | 485,150.00 USD |
| `1D` | `1.26` | 9,370,000.00 USD | 9,370,000.00 USD | 0.00 USD | 390,940.00 USD | 121,550.00 USD | 1,030,000.00 USD |
| `7D` | `1.26` | 12,820,000.00 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,910,000.00 USD |
| `1D` | `1.26` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 0.00 USD | 446,110.00 USD | 1,140,000.00 USD |
| `7D` | `1.26` | 19,750,000.00 USD | 19,750,000.00 USD | 0.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD |
| `1D` | `1.27` | 12,940,000.00 USD | 12,940,000.00 USD | 0.00 USD | 39,860.00 USD | 1,080,000.00 USD | 861,210.00 USD |
| `7D` | `1.27` | 32,990,000.00 USD | 32,990,000.00 USD | 0.00 USD | 2,620,000.00 USD | 2,370,000.00 USD | 8,250,000.00 USD |
| `1D` | `1.27` | 14,970,000.00 USD | 14,970,000.00 USD | 0.00 USD | 0.00 USD | 2,030,000.00 USD | 0.00 USD |
| `7D` | `1.27` | 37,760,000.00 USD | 37,760,000.00 USD | 0.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD |
| `1D` | `1.27` | 17,780,000.00 USD | 17,780,000.00 USD | 0.00 USD | 327,600.00 USD | 803,550.00 USD | 1,680,000.00 USD |
| `7D` | `1.27` | 41,370,000.00 USD | 41,370,000.00 USD | 0.00 USD | 943,110.00 USD | 2,540,000.00 USD | 123,930.00 USD |
| `1D` | `1.27` | 20,130,000.00 USD | 20,130,000.00 USD | 0.00 USD | 1,740,000.00 USD | 318,590.00 USD | 285,020.00 USD |
| `7D` | `1.27` | 46,100,000.00 USD | 46,100,000.00 USD | 0.00 USD | 186,960.00 USD | 3,980,000.00 USD | 567,370.00 USD |
| `1D` | `1.27` | 25,690,000.00 USD | 25,690,000.00 USD | 0.00 USD | 439,850.00 USD | 2,150,000.00 USD | 2,960,000.00 USD |
| `7D` | `1.27` | 60,670,000.00 USD | 60,670,000.00 USD | 0.00 USD | 4,420,000.00 USD | 1,940,000.00 USD | 8,210,000.00 USD |
| `1D` | `1.28` | 35,450,000.00 USD | 35,450,000.00 USD | 0.00 USD | 3,050,000.00 USD | 2,800,000.00 USD | 3,910,000.00 USD |
| `7D` | `1.28` | 78,940,000.00 USD | 78,940,000.00 USD | 0.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 43,180,000.00 USD | 43,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 2,210,000.00 USD | 2,350,000.00 USD |
| `7D` | `1.28` | 85,230,000.00 USD | 85,230,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,940,000.00 USD | 1,090,000.00 USD |
| `1D` | `1.28` | 44,510,000.00 USD | 44,510,000.00 USD | 0.00 USD | 209,970.00 USD | 608,220.00 USD | 507,970.00 USD |
| `7D` | `1.28` | 86,190,000.00 USD | 86,190,000.00 USD | 0.00 USD | 0.00 USD | 879,610.00 USD | 79,220.00 USD |
| `1D` | `1.28` | 47,370,000.00 USD | 47,370,000.00 USD | 0.00 USD | 1,120,000.00 USD | 199,040.00 USD | 1,540,000.00 USD |
| `7D` | `1.28` | 88,200,000.00 USD | 88,200,000.00 USD | 0.00 USD | 1,460,000.00 USD | 478,060.00 USD | 67,480.00 USD |
| `1D` | `1.28` | 49,390,000.00 USD | 49,390,000.00 USD | 0.00 USD | 421,680.00 USD | 611,360.00 USD | 985,040.00 USD |
| `7D` | `1.28` | 91,790,000.00 USD | 91,790,000.00 USD | 0.00 USD | 639,910.00 USD | 1,380,000.00 USD | 1,570,000.00 USD |
| `1D` | `1.29` | 51,300,000.00 USD | 51,300,000.00 USD | 0.00 USD | 726,790.00 USD | 768,570.00 USD | 418,070.00 USD |
| `7D` | `1.29` | 92,960,000.00 USD | 92,960,000.00 USD | 0.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD |
| `1D` | `1.29` | 51,470,000.00 USD | 51,470,000.00 USD | 0.00 USD | 160,320.00 USD | 7,000.00 USD | 0.00 USD |
| `7D` | `1.29` | 93,070,000.00 USD | 93,070,000.00 USD | 0.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD |
| `1D` | `1.29` | 51,640,000.00 USD | 51,640,000.00 USD | 0.00 USD | 151,350.00 USD | 0.00 USD | 22,040.00 USD |
| `7D` | `1.29` | 95,160,000.00 USD | 95,160,000.00 USD | 0.00 USD | 1,060,000.00 USD | 198,070.00 USD | 829,400.00 USD |
| `1D` | `1.29` | 54,520,000.00 USD | 54,520,000.00 USD | 0.00 USD | 546,160.00 USD | 193,100.00 USD | 2,140,000.00 USD |
| `7D` | `1.29` | 95,580,000.00 USD | 95,580,000.00 USD | 0.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD |
| `1D` | `1.29` | 60,380,000.00 USD | 60,380,000.00 USD | 0.00 USD | 1,800,000.00 USD | 608,440.00 USD | 3,450,000.00 USD |
| `7D` | `1.29` | 105,220,000.00 USD | 105,220,000.00 USD | 0.00 USD | 3,350,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD |
| `1D` | `1.30` | 62,600,000.00 USD | 62,600,000.00 USD | 0.00 USD | 497,720.00 USD | 629,370.00 USD | 1,090,000.00 USD |
| `7D` | `1.30` | 106,450,000.00 USD | 106,450,000.00 USD | 0.00 USD | 209,360.00 USD | 396,530.00 USD | 628,450.00 USD |
| `1D` | `1.30` | 62,940,000.00 USD | 62,940,000.00 USD | 0.00 USD | 254,730.00 USD | 87,350.00 USD | 0.00 USD |
| `7D` | `1.30` | 107,970,000.00 USD | 107,970,000.00 USD | 0.00 USD | 0.00 USD | 95,300.00 USD | 1,420,000.00 USD |
| `1D` | `1.30` | 64,500,000.00 USD | 64,500,000.00 USD | 0.00 USD | 274,080.00 USD | 110,280.00 USD | 1,170,000.00 USD |
| `7D` | `1.30` | 109,230,000.00 USD | 109,230,000.00 USD | 0.00 USD | 0.00 USD | 286,660.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 65,920,000.00 USD | 65,920,000.00 USD | 0.00 USD | 520,770.00 USD | 899,720.00 USD | 0.00 USD |
| `7D` | `1.30` | 112,320,000.00 USD | 112,320,000.00 USD | 0.00 USD | 0.00 USD | 2,610,000.00 USD | 485,710.00 USD |
| `1D` | `1.30` | 67,190,000.00 USD | 67,190,000.00 USD | 0.00 USD | 304,340.00 USD | 649,450.00 USD | 322,840.00 USD |
| `7D` | `1.30` | 112,320,000.00 USD | 112,320,000.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD |
| `1D` | `1.31` | 69,480,000.00 USD | 69,480,000.00 USD | 0.00 USD | 689,960.00 USD | 147,250.00 USD | 1,450,000.00 USD |
| `7D` | `1.31` | 115,330,000.00 USD | 115,330,000.00 USD | 0.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD |
| `1D` | `1.31` | 72,720,000.00 USD | 72,720,000.00 USD | 0.00 USD | 1,130,000.00 USD | 330,750.00 USD | 1,770,000.00 USD |
| `7D` | `1.31` | 119,790,000.00 USD | 119,790,000.00 USD | 0.00 USD | 1,670,000.00 USD | 1,060,000.00 USD | 1,720,000.00 USD |
| `1D` | `1.31` | 75,040,000.00 USD | 75,040,000.00 USD | 0.00 USD | 876,130.00 USD | 869,070.00 USD | 573,540.00 USD |
| `7D` | `1.31` | 123,050,000.00 USD | 123,050,000.00 USD | 0.00 USD | 839,350.00 USD | 430,210.00 USD | 1,990,000.00 USD |
| `1D` | `1.31` | 78,030,000.00 USD | 78,030,000.00 USD | 0.00 USD | 1,390,000.00 USD | 664,910.00 USD | 944,450.00 USD |
| `7D` | `1.31` | 125,890,000.00 USD | 125,890,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD |
| `1D` | `1.31` | 81,170,000.00 USD | 81,170,000.00 USD | 0.00 USD | 372,630.00 USD | 454,810.00 USD | 2,310,000.00 USD |
| `7D` | `1.31` | 128,350,000.00 USD | 128,350,000.00 USD | 0.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 87,740,000.00 USD | 87,740,000.00 USD | 0.00 USD | 1,320,000.00 USD | 1,700,000.00 USD | 3,550,000.00 USD |
| `7D` | `1.32` | 132,970,000.00 USD | 132,970,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 92,820,000.00 USD | 92,820,000.00 USD | 0.00 USD | 1,740,000.00 USD | 836,160.00 USD | 2,510,000.00 USD |
| `7D` | `1.32` | 136,050,000.00 USD | 136,050,000.00 USD | 0.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 96,320,000.00 USD | 96,320,000.00 USD | 0.00 USD | 1,650,000.00 USD | 652,780.00 USD | 1,200,000.00 USD |
| `7D` | `1.32` | 137,880,000.00 USD | 137,880,000.00 USD | 0.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD |
| `1D` | `1.32` | 100,910,000.00 USD | 100,910,000.00 USD | 0.00 USD | 1,990,000.00 USD | 583,250.00 USD | 2,020,000.00 USD |
| `7D` | `1.32` | 142,340,000.00 USD | 142,340,000.00 USD | 0.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD |
| `1D` | `1.32` | 102,910,000.00 USD | 102,910,000.00 USD | 0.00 USD | 1,080,000.00 USD | 287,760.00 USD | 625,660.00 USD |
| `7D` | `1.32` | 144,710,000.00 USD | 144,710,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 105,440,000.00 USD | 105,440,000.00 USD | 0.00 USD | 664,210.00 USD | 621,550.00 USD | 1,240,000.00 USD |
| `7D` | `1.33` | 145,240,000.00 USD | 145,240,000.00 USD | 0.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 107,680,000.00 USD | 107,680,000.00 USD | 0.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD |
| `7D` | `1.33` | 146,400,000.00 USD | 146,400,000.00 USD | 0.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 110,530,000.00 USD | 110,530,000.00 USD | 0.00 USD | 848,670.00 USD | 298,810.00 USD | 1,700,000.00 USD |
| `7D` | `1.33` | 148,120,000.00 USD | 148,120,000.00 USD | 0.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 112,910,000.00 USD | 112,910,000.00 USD | 0.00 USD | 1,040,000.00 USD | 190,550.00 USD | 1,160,000.00 USD |
| `7D` | `1.33` | 152,170,000.00 USD | 152,170,000.00 USD | 0.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD |
| `1D` | `1.33` | 115,000,000.00 USD | 115,000,000.00 USD | 0.00 USD | 859,040.00 USD | 354,550.00 USD | 872,500.00 USD |
| `7D` | `1.33` | 152,720,000.00 USD | 152,720,000.00 USD | 0.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 117,090,000.00 USD | 117,090,000.00 USD | 0.00 USD | 896,540.00 USD | 219,260.00 USD | 976,640.00 USD |
| `7D` | `1.34` | 154,660,000.00 USD | 154,660,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD |
| `1D` | `1.34` | 119,960,000.00 USD | 119,960,000.00 USD | 0.00 USD | 1,170,000.00 USD | 370,350.00 USD | 1,330,000.00 USD |
| `7D` | `1.34` | 157,010,000.00 USD | 157,010,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD |
| `1D` | `1.34` | 122,600,000.00 USD | 122,600,000.00 USD | 0.00 USD | 1,330,000.00 USD | 518,530.00 USD | 792,900.00 USD |
| `7D` | `1.34` | 161,720,000.00 USD | 161,720,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD |
| `1D` | `1.34` | 126,330,000.00 USD | 126,330,000.00 USD | 0.00 USD | 1,750,000.00 USD | 754,220.00 USD | 1,230,000.00 USD |
| `7D` | `1.34` | 167,360,000.00 USD | 167,360,000.00 USD | 0.00 USD | 1,700,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD |
| `1D` | `1.34` | 128,100,000.00 USD | 128,100,000.00 USD | 0.00 USD | 584,400.00 USD | 416,300.00 USD | 762,530.00 USD |
| `7D` | `1.34` | 178,430,000.00 USD | 178,430,000.00 USD | 0.00 USD | 3,700,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD |
| `1D` | `1.35` | 129,150,000.00 USD | 129,150,000.00 USD | 0.00 USD | 355,660.00 USD | 234,160.00 USD | 458,570.00 USD |
| `7D` | `1.35` | 185,540,000.00 USD | 185,540,000.00 USD | 0.00 USD | 2,410,000.00 USD | 2,230,000.00 USD | 2,470,000.00 USD |
| `1D` | `1.35` | 130,640,000.00 USD | 130,640,000.00 USD | 0.00 USD | 752,410.00 USD | 149,380.00 USD | 594,360.00 USD |
| `7D` | `1.35` | 195,850,000.00 USD | 195,850,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,700,000.00 USD | 4,320,000.00 USD |
| `1D` | `1.35` | 131,730,000.00 USD | 131,730,000.00 USD | 0.00 USD | 507,940.00 USD | 126,620.00 USD | 450,130.00 USD |
| `7D` | `1.35` | 203,620,000.00 USD | 203,620,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 133,490,000.00 USD | 133,490,000.00 USD | 0.00 USD | 716,900.00 USD | 334,990.00 USD | 716,090.00 USD |
| `7D` | `1.35` | 211,950,000.00 USD | 211,950,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD |
| `1D` | `1.35` | 134,680,000.00 USD | 134,680,000.00 USD | 0.00 USD | 363,860.00 USD | 145,570.00 USD | 673,510.00 USD |
| `7D` | `1.35` | 220,180,000.00 USD | 220,180,000.00 USD | 0.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD |
| `1D` | `1.36` | 135,860,000.00 USD | 135,860,000.00 USD | 0.00 USD | 560,800.00 USD | 47,560.00 USD | 572,200.00 USD |
| `7D` | `1.36` | 224,270,000.00 USD | 224,270,000.00 USD | 0.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD |
| `1D` | `1.36` | 136,200,000.00 USD | 136,200,000.00 USD | 0.00 USD | 213,710.00 USD | 42,480.00 USD | 82,390.00 USD |
| `7D` | `1.36` | 228,060,000.00 USD | 228,060,000.00 USD | 0.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.36` | 136,940,000.00 USD | 136,940,000.00 USD | 0.00 USD | 277,960.00 USD | 149,990.00 USD | 316,940.00 USD |
| `7D` | `1.36` | 230,190,000.00 USD | 230,190,000.00 USD | 0.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD |
| `1D` | `1.36` | 137,280,000.00 USD | 137,280,000.00 USD | 0.00 USD | 171,250.00 USD | 2,260.00 USD | 166,760.00 USD |
| `7D` | `1.36` | 234,290,000.00 USD | 234,290,000.00 USD | 0.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD |
| `1D` | `1.36` | 137,340,000.00 USD | 137,340,000.00 USD | 0.00 USD | 0.00 USD | 26,460.00 USD | 34,440.00 USD |
| `7D` | `1.36` | 236,010,000.00 USD | 236,010,000.00 USD | 0.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD |
| `1D` | `1.37` | 137,670,000.00 USD | 137,670,000.00 USD | 0.00 USD | 53,740.00 USD | 103,940.00 USD | 171,320.00 USD |
| `7D` | `1.37` | 236,500,000.00 USD | 236,500,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD |
| `1D` | `1.37` | 137,860,000.00 USD | 137,860,000.00 USD | 0.00 USD | 121,310.00 USD | 2,250.00 USD | 68,720.00 USD |
| `7D` | `1.37` | 237,910,000.00 USD | 237,910,000.00 USD | 0.00 USD | 528,490.00 USD | 136,720.00 USD | 753,550.00 USD |
| `1D` | `1.37` | 138,050,000.00 USD | 138,050,000.00 USD | 0.00 USD | 1,740.00 USD | 66,920.00 USD | 119,540.00 USD |
| `7D` | `1.37` | 239,080,000.00 USD | 239,080,000.00 USD | 0.00 USD | 334,560.00 USD | 372,470.00 USD | 461,160.00 USD |
| `1D` | `1.37` | 138,200,000.00 USD | 138,200,000.00 USD | 0.00 USD | 75,340.00 USD | 249.08 USD | 69,770.00 USD |
| `7D` | `1.37` | 241,680,000.00 USD | 241,680,000.00 USD | 0.00 USD | 920,600.00 USD | 405,390.00 USD | 1,270,000.00 USD |
| `1D` | `1.38` | 138,320,000.00 USD | 138,320,000.00 USD | 0.00 USD | 54,550.00 USD | 884.30 USD | 69,340.00 USD |
| `7D` | `1.38` | 243,270,000.00 USD | 243,270,000.00 USD | 0.00 USD | 536,130.00 USD | 294,500.00 USD | 759,750.00 USD |
| `1D` | `1.38` | 138,650,000.00 USD | 138,650,000.00 USD | 0.00 USD | 112,910.00 USD | 50,670.00 USD | 163,280.00 USD |
| `7D` | `1.38` | 244,830,000.00 USD | 244,830,000.00 USD | 0.00 USD | 617,230.00 USD | 389,310.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 139,300,000.00 USD | 139,300,000.00 USD | 0.00 USD | 254,930.00 USD | 111,730.00 USD | 284,400.00 USD |
| `7D` | `1.38` | 246,960,000.00 USD | 246,960,000.00 USD | 0.00 USD | 579,450.00 USD | 290,350.00 USD | 1,260,000.00 USD |
| `1D` | `1.38` | 139,570,000.00 USD | 139,570,000.00 USD | 0.00 USD | 122,940.00 USD | 98,400.00 USD | 50,930.00 USD |
| `7D` | `1.38` | 249,510,000.00 USD | 249,510,000.00 USD | 0.00 USD | 1,210,000.00 USD | 331,990.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 139,860,000.00 USD | 139,860,000.00 USD | 0.00 USD | 84,700.00 USD | 16,420.00 USD | 186,810.00 USD |
| `7D` | `1.38` | 250,600,000.00 USD | 250,600,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.39` | 139,920,000.00 USD | 139,920,000.00 USD | 0.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD |
| `7D` | `1.39` | 251,880,000.00 USD | 251,880,000.00 USD | 0.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 139,970,000.00 USD | 139,970,000.00 USD | 0.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD |
| `7D` | `1.39` | 252,430,000.00 USD | 252,430,000.00 USD | 0.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD |
| `1D` | `1.39` | 140,060,000.00 USD | 140,060,000.00 USD | 0.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD |
| `7D` | `1.39` | 253,530,000.00 USD | 253,530,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD |
| `7D` | `1.39` | 253,690,000.00 USD | 253,690,000.00 USD | 0.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD |
| `1D` | `1.39` | 140,080,000.00 USD | 140,080,000.00 USD | 0.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.39` | 254,020,000.00 USD | 254,020,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.40` | 140,150,000.00 USD | 140,150,000.00 USD | 0.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD |
| `7D` | `1.40` | 254,190,000.00 USD | 254,190,000.00 USD | 0.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 140,290,000.00 USD | 140,290,000.00 USD | 0.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD |
| `7D` | `1.40` | 254,310,000.00 USD | 254,310,000.00 USD | 0.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.40` | 140,330,000.00 USD | 140,330,000.00 USD | 0.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD |
| `7D` | `1.40` | 254,320,000.00 USD | 254,320,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 254,450,000.00 USD | 254,450,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `1D` | `1.40` | 140,340,000.00 USD | 140,340,000.00 USD | 0.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.40` | 254,570,000.00 USD | 254,570,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `7D` | `1.41` | 254,810,000.00 USD | 254,810,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 254,980,000.00 USD | 254,980,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `7D` | `1.41` | 255,360,000.00 USD | 255,360,000.00 USD | 0.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `7D` | `1.41` | 256,010,000.00 USD | 256,010,000.00 USD | 0.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `7D` | `1.41` | 256,180,000.00 USD | 256,180,000.00 USD | 0.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD |
| `7D` | `1.42` | 256,800,000.00 USD | 256,800,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD |
| `7D` | `1.42` | 257,330,000.00 USD | 257,330,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `7D` | `1.42` | 258,350,000.00 USD | 258,350,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `7D` | `1.42` | 259,730,000.00 USD | 259,730,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `7D` | `1.42` | 260,350,000.00 USD | 260,350,000.00 USD | 0.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `7D` | `1.43` | 260,710,000.00 USD | 260,710,000.00 USD | 0.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD |
| `7D` | `1.43` | 261,730,000.00 USD | 261,730,000.00 USD | 0.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD |
| `7D` | `1.43` | 263,240,000.00 USD | 263,240,000.00 USD | 0.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `7D` | `1.43` | 264,630,000.00 USD | 264,630,000.00 USD | 0.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `7D` | `1.43` | 265,430,000.00 USD | 265,430,000.00 USD | 0.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `7D` | `1.44` | 265,960,000.00 USD | 265,960,000.00 USD | 0.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD |
| `7D` | `1.44` | 266,310,000.00 USD | 266,310,000.00 USD | 0.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD |
| `7D` | `1.44` | 266,760,000.00 USD | 266,760,000.00 USD | 0.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `7D` | `1.44` | 267,480,000.00 USD | 267,480,000.00 USD | 0.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `7D` | `1.44` | 267,850,000.00 USD | 267,850,000.00 USD | 0.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `7D` | `1.45` | 267,980,000.00 USD | 267,980,000.00 USD | 0.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `7D` | `1.45` | 268,110,000.00 USD | 268,110,000.00 USD | 0.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD |
| `7D` | `1.45` | 268,440,000.00 USD | 268,440,000.00 USD | 0.00 USD | 62,180.00 USD | 96,050.00 USD | 173,340.00 USD |
| `7D` | `1.45` | 269,050,000.00 USD | 269,050,000.00 USD | 0.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD |
| `7D` | `1.45` | 269,610,000.00 USD | 269,610,000.00 USD | 0.00 USD | 182,110.00 USD | 128,180.00 USD | 251,300.00 USD |
| `7D` | `1.46` | 270,070,000.00 USD | 270,070,000.00 USD | 0.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `7D` | `1.46` | 270,230,000.00 USD | 270,230,000.00 USD | 0.00 USD | 85,350.00 USD | 51,250.00 USD | 20,990.00 USD |
| `7D` | `1.46` | 270,700,000.00 USD | 270,700,000.00 USD | 0.00 USD | 119,110.00 USD | 56,610.00 USD | 296,470.00 USD |
| `7D` | `1.46` | 270,910,000.00 USD | 270,910,000.00 USD | 0.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.86B` | Total OI Tokens: `2,290,766,176.1 XRP`
  * 1h OI Change: `+0.85%` | 4h OI Change: `-4.96%` | 24h OI Change: `-4.33%`
  * Exchange Breakdown: Binance=`461.86M` | Bybit=`319.76M` | OKX=`98.20M` | Hyperliquid=`220.02M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-19.75K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0007%` | **USDT OKX** | `0.0011%` |
| **USDT Bybit** | `-0.0095%` | **USDT KuCoin** | `0.0003%` |
| **USDT MEXC** | `0.0006%` | **USDT BingX** | `0.0013%` |
| **USDT Gate** | `-0.0019%` | **USDT Bitget** | `-0.0026%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `46.41%` | `53.59%` | `0.87` | 977,050,000.00 USD |
| `15M` | `Binance` | `46.29%` | `53.71%` | `0.86` | 291,670,000.00 USD |
| `15M` | `OKX` | `48.48%` | `51.52%` | `0.94` | 166,850,000.00 USD |
| `15M` | `Bybit` | `47.51%` | `52.49%` | `0.91` | 72,880,000.00 USD |
| `15M` | `KuCoin` | `54.49%` | `45.51%` | `1.20` | 4,440,000.00 USD |
| `15M` | `Gate` | `47.4%` | `52.6%` | `0.90` | 150,180,000.00 USD |
| `15M` | `Bitget` | `59.71%` | `40.29%` | `1.48` | 34,780,000.00 USD |
| `15M` | `BingX` | `46.74%` | `53.26%` | `0.88` | 5,630,000.00 USD |
| `15M` | `MEXC` | `51.43%` | `48.57%` | `1.06` | 58,640,000.00 USD |
| `15M` | `Bitunix` | `49.42%` | `50.58%` | `0.98` | 30,860,000.00 USD |
| `15M` | `Hyperliquid` | `28.06%` | `71.94%` | `0.39` | 62,530,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.03%` | `55.97%` | `0.79` | 2,160,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `67.88%` | `32.12%` | `2.11` | 23,330,000.00 USD |
| `15M` | `HTX` | `12.69%` | `87.31%` | `0.15` | 27,570,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `56.47%` | `43.53%` | `1.30` | 16,730,000.00 USD |
| `15M` | `Bitfinex` | `12.52%` | `87.48%` | `0.14` | 260,700.00 USD |
| `15M` | `Kraken` | `47.71%` | `52.29%` | `0.91` | 5,820,000.00 USD |
| `15M` | `Aster` | `47.89%` | `52.11%` | `0.92` | 5,580,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `45.36%` | `54.64%` | `0.83` | 17,150,000.00 USD |
| `15M` | `Whale Positions` | `46.29%` | `53.71%` | `0.86` | 291,670,000.00 USD |
| `15M` | `Global Accounts` | `46.41%` | `53.59%` | `0.87` | 977,050,000.00 USD |
| `1H` | `XRP` | `50.73%` | `49.27%` | `1.03` | 5,660,000,000.00 USD |
| `1H` | `Binance` | `49.05%` | `50.95%` | `0.96` | 1,730,000,000.00 USD |
| `1H` | `OKX` | `48.71%` | `51.29%` | `0.95` | 886,640,000.00 USD |
| `1H` | `Bybit` | `48.77%` | `51.23%` | `0.95` | 463,090,000.00 USD |
| `1H` | `KuCoin` | `57.24%` | `42.76%` | `1.34` | 37,230,000.00 USD |
| `1H` | `Gate` | `50.2%` | `49.8%` | `1.01` | 799,120,000.00 USD |
| `1H` | `Bitget` | `53.27%` | `46.73%` | `1.14` | 221,540,000.00 USD |
| `1H` | `BingX` | `50.53%` | `49.47%` | `1.02` | 47,480,000.00 USD |
| `1H` | `MEXC` | `49.31%` | `50.69%` | `0.97` | 227,570,000.00 USD |
| `1H` | `Bitunix` | `50.23%` | `49.77%` | `1.01` | 178,020,000.00 USD |
| `1H` | `Hyperliquid` | `38.13%` | `61.87%` | `0.62` | 376,190,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.01%` | `46.99%` | `1.13` | 12,410,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `81.66%` | `18.34%` | `4.45` | 400,470,000.00 USD |
| `1H` | `HTX` | `26%` | `74%` | `0.35` | 71,960,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `55.75%` | `44.25%` | `1.26` | 43,000,000.00 USD |
| `1H` | `Bitfinex` | `30.18%` | `69.82%` | `0.43` | 951,940.00 USD |
| `1H` | `Kraken` | `47.7%` | `52.3%` | `0.91` | 28,030,000.00 USD |
| `1H` | `Aster` | `47.3%` | `52.7%` | `0.90` | 42,880,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `48.14%` | `51.86%` | `0.93` | 83,270,000.00 USD |
| `1H` | `Whale Positions` | `49.05%` | `50.95%` | `0.96` | 1,730,000,000.00 USD |
| `1H` | `Global Accounts` | `50.73%` | `49.27%` | `1.03` | 5,660,000,000.00 USD |
| `4H` | `XRP` | `46.81%` | `53.19%` | `0.88` | 23,150,000,000.00 USD |
| `4H` | `Binance` | `44.88%` | `55.12%` | `0.81` | 6,990,000,000.00 USD |
| `4H` | `OKX` | `45.24%` | `54.76%` | `0.83` | 3,910,000,000.00 USD |
| `4H` | `Bybit` | `44.26%` | `55.74%` | `0.79` | 1,720,000,000.00 USD |
| `4H` | `KuCoin` | `53.69%` | `46.31%` | `1.16` | 211,760,000.00 USD |
| `4H` | `Gate` | `49.27%` | `50.73%` | `0.97` | 2,360,000,000.00 USD |
| `4H` | `Bitget` | `51.25%` | `48.75%` | `1.05` | 1,070,000,000.00 USD |
| `4H` | `BingX` | `49.8%` | `50.2%` | `0.99` | 240,820,000.00 USD |
| `4H` | `MEXC` | `48.72%` | `51.28%` | `0.95` | 698,200,000.00 USD |
| `4H` | `Bitunix` | `47.4%` | `52.6%` | `0.90` | 731,010,000.00 USD |
| `4H` | `Hyperliquid` | `44.37%` | `55.63%` | `0.80` | 1,230,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.38%` | `49.62%` | `1.02` | 54,840,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `51.53%` | `48.47%` | `1.06` | 2,970,000,000.00 USD |
| `4H` | `HTX` | `34.44%` | `65.56%` | `0.53` | 221,580,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `49.78%` | `50.22%` | `0.99` | 135,020,000.00 USD |
| `4H` | `Bitfinex` | `26.5%` | `73.5%` | `0.36` | 8,070,000.00 USD |
| `4H` | `Kraken` | `48%` | `52%` | `0.92` | 82,970,000.00 USD |
| `4H` | `Aster` | `46.51%` | `53.49%` | `0.87` | 191,900,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49%` | `51%` | `0.96` | 322,600,000.00 USD |
| `4H` | `Whale Positions` | `44.88%` | `55.12%` | `0.81` | 6,990,000,000.00 USD |
| `4H` | `Global Accounts` | `46.81%` | `53.19%` | `0.88` | 23,150,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 7,767,016.10 USD | 3,262,612.53 USD | 4,504,403.57 USD | -1,241,791.04 USD | `-15.99%` | `7B / 12S` |
| `0:00 UTC` | `1.27` | `1.27` | `1.27` | `1.28` | `1.26` | 41,778,066.41 USD | 16,233,527.16 USD | 25,544,539.25 USD | -9,311,012.09 USD | `-22.29%` | `4B / 58S` |
| `5:00 UTC` | `1.27` | `1.27` | `1.27` | `1.27` | `1.27` | 9,197,225.16 USD | 4,639,147.41 USD | 4,558,077.75 USD | 81,069.66 USD | `+0.88%` | `4B / 5S` |
| `0:00 UTC` | `1.24` | `1.25` | `1.24` | `1.27` | `1.23` | 112,851,214.34 USD | 44,440,734.72 USD | 68,410,479.62 USD | -23,969,744.90 USD | `-21.24%` | `0B / 35S` |
| `5:00 UTC` | `1.24` | `1.24` | `1.24` | `1.25` | `1.22` | 96,971,024.45 USD | 46,182,833.37 USD | 50,788,191.08 USD | -4,605,357.71 USD | `-4.75%` | `1B / 8S` |
| `0:00 UTC` | `1.25` | `1.24` | `1.25` | `1.25` | `1.23` | 42,899,530.36 USD | 22,765,315.89 USD | 20,134,214.47 USD | 2,631,101.42 USD | `+6.13%` | `25B / 6S` |
| `5:00 UTC` | `1.25` | `1.26` | `1.25` | `1.26` | `1.25` | 36,075,332.57 USD | 17,198,898.48 USD | 18,876,434.09 USD | -1,677,535.61 USD | `-4.65%` | `12B / 8S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 16,161,725.94 USD | 8,623,195.09 USD | 7,538,530.84 USD | 1,084,664.25 USD | `+6.71%` | `17B / 20S` |
| `5:00 UTC` | `1.25` | `1.26` | `1.25` | `1.26` | `1.25` | 13,078,738.26 USD | 6,457,414.69 USD | 6,621,323.57 USD | -163,908.89 USD | `-1.25%` | `11B / 13S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 33,070,568.52 USD | 15,710,948.50 USD | 17,359,620.02 USD | -1,648,671.52 USD | `-4.99%` | `12B / 11S` |

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
| `5m` | -9,350.00 USD | -662,050.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,070,000.00 USD | -5,360,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,430,000.00 USD | -5,810,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 2,660,000.00 USD | 1,330,000.00 USD | **`ACCUMULATION`** |
| `2h` | -25,060,000.00 USD | -73,010,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -33,630,000.00 USD | -110,550,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -38,590,000.00 USD | -125,300,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -32,260,000.00 USD | -115,700,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -36,100,000.00 USD | -122,440,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -56,830,000.00 USD | -177,790,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -103,120,000.00 USD | -188,370,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -581,780,000.00 USD | -1,290,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-9.35K` | 15m=`-1.07M` | 1h=`+2.66M` | 24h=`-56.83M`
* Futures Capital Netflows: 5m=`-662.05K` | 15m=`-5.36M` | 1h=`+1.33M` | 24h=`-177.79M`
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
  * `2026-10-30 03:29:57 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:57 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:40:57 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:57 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:41:57 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:57 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:57 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.25` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.23` (Risk Distance: `0.0188` pts)
  * +2.5R Take Profit: `1.29`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.28` (Risk Distance: `0.0188` pts)
  * +2.5R Take Profit: `1.21`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.26`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
