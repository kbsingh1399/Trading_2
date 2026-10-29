# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 02:09:26 IST` (`2026-10-29 20:39:26 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.26` | **Live Ask Quote**: `1.26` | **Mid Price**: `1.26`
- **Spread Points**: `3.00` | **Spread BPS**: `23.78 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.29` | VWAP Z-Score: `-2.38` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0073` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `29.42` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.32` | Lower -3.00σ Band: `1.26`
  * Upper +2.51σ Band: `1.32` | Lower -2.51σ Band: `1.27`
  * Upper +2.01σ Band: `1.31` | Lower -2.01σ Band: `1.27`
  * Upper +2.00σ Band: `1.31` | Lower -2.00σ Band: `1.27`
  * Upper +1.28σ Band: `1.30` | Lower -1.28σ Band: `1.28`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.28`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.28` | EMA-20=`1.28` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.29` (Slope: `+0.0000`) | EMA-100=`1.30`
  * Institutional Anchors: EMA-144=`1.30` | EMA-200=`1.30` (Slope: `-0.1955`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.33` | 24H Low=`1.26` | Weekly High=`1.34` | Weekly Low=`1.26`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.30` (Distance: `-3.43%`)
  * Point of Control (POC) = `1.29` (Distance: `-2.45%`)
  * Value Area Low (VAL) = `1.28` (Distance: `-1.98%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.33` | POC=`1.33` | VAL=`1.32`
  * Prior Day Extremes: PDH=`1.34` | PDL=`1.30` | PDC=`1.33`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.31` | Weekly POC=`1.29` | Weekly VAL=`1.27`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.33` | Low=`1.28`
  * London Session (08:00-16:00 UTC): High=`1.30` | Low=`1.28`
  * New York Session (13:00-21:00 UTC): High=`1.31` | Low=`1.28`
  * Initial Balance (First Hour): IB High=`1.30` | IB Low=`1.29`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.26` - `1.27`
  * Optimal Trade Entry (OTE 0.705): `1.26`
  * Structural Invalidation Anchor (0.786): `1.27`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.27` | `1.27` | `1.27` | `1.27` | `2,046,040` | 2,601,963.17 USD | 157,441.35 USD | `+6.05%` | -50,388,048.51 USD | `+0.37` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `1.27` | `1.27` | `1.27` | `1.27` | `2,351,901` | 2,988,478.90 USD | 159,353.94 USD | `+5.33%` | -50,228,694.57 USD | `+0.36` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `1.27` | `1.27` | `1.26` | `1.26` | `10,899,628` | 13,768,479.83 USD | -3,242,746.31 USD | `-23.55%` | -53,471,440.88 USD | `-1.45` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.28` | `1.28` | `1.26` | `1.27` | `32,849,150` | 41,778,082.42 USD | -9,310,996.08 USD | `-22.29%` | -51,320,012.82 USD | `-2.67` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.27` | `1.27` | `1.27` | `1.27` | `7,235,170` | 9,197,225.16 USD | 81,069.66 USD | `+0.88%` | -51,238,943.16 USD | `+0.44` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `1.27` | `1.27` | `1.26` | `1.26` | `10,899,628` | 13,768,479.83 USD | -3,242,746.31 USD | `-23.55%` | -54,481,689.48 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.29` | `38,773,350` | 49,794,344.17 USD | -9,116,518.67 USD | `-18.31%` | -40,138,234.48 USD | `-1.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.28` | `17,509,907` | 22,469,016.48 USD | -1,419,504.92 USD | `-6.32%` | -41,557,739.40 USD | `+0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.28` | `1.28` | `1.26` | `1.26` | `50,983,948` | 64,743,787.41 USD | -12,472,672.74 USD | `-19.26%` | -54,030,412.14 USD | `-2.26` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.26` | `1.26` | `48,114,956` | 61,130,540.05 USD | -11,561,673.46 USD | `-18.91%` | -51,500,703.27 USD | `-0.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,072,364.54 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,389,228.53 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.26` | `1.26` | `48,114,956` | 61,130,540.05 USD | -11,561,673.46 USD | `-18.91%` | -51,500,703.27 USD | `-0.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `ASK` | `1.26` | `6326.0000` | 7,981.51 USD | 1,310,578.76 USD | `4 orders` | `+0.16%` | `-` |
| `ASK` | `1.26` | `77538.0000` | 97,821.94 USD | 1,302,597.24 USD | `4 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `13414.0000` | 16,921.76 USD | 1,204,775.30 USD | `4 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `422918.0000` | 533,468.77 USD | 1,187,853.54 USD | `8 orders` | `+0.14%` | `-` |
| `ASK` | `1.26` | `72673.0000` | 91,662.45 USD | 654,384.78 USD | `10 orders` | `+0.13%` | `-` |
| `ASK` | `1.26` | `3554.0000` | 4,482.30 USD | 562,722.32 USD | `3 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `6974.0000` | 8,794.91 USD | 558,240.02 USD | `3 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `11102.0000` | 13,999.62 USD | 549,445.10 USD | `7 orders` | `+0.11%` | `-` |
| `ASK` | `1.26` | `12860.0000` | 16,215.17 USD | 535,445.48 USD | `3 orders` | `+0.10%` | `-` |
| `ASK` | `1.26` | `38064.0000` | 47,991.09 USD | 519,230.31 USD | `4 orders` | `+0.09%` | `-` |
| `ASK` | `1.26` | `2634.0000` | 3,320.68 USD | 471,239.22 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `81216.0000` | 102,380.89 USD | 467,918.53 USD | `5 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `29220.0000` | 36,831.81 USD | 365,537.64 USD | `3 orders` | `+0.07%` | `-` |
| `ASK` | `1.26` | `30669.0000` | 38,655.21 USD | 328,705.83 USD | `4 orders` | `+0.06%` | `-` |
| `ASK` | `1.26` | `105380.0000` | 132,810.41 USD | 290,050.63 USD | `17 orders` | `+0.05%` | `-` |
| `ASK` | `1.26` | `57034.0000` | 71,874.25 USD | 157,240.21 USD | `30 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `15057.0000` | 18,973.33 USD | 85,365.97 USD | `24 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `22273.0000` | 28,063.98 USD | 66,392.64 USD | `25 orders` | `+0.03%` | `-` |
| `ASK` | `1.26` | `17642.0000` | 22,227.16 USD | 38,328.66 USD | `23 orders` | `+0.02%` | `-` |
| `ASK` | `1.26` | `12781.0000` | 16,101.50 USD | 16,101.50 USD | `19 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `1.26` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.26` | `0.00%` | `-` |
| `BID` | `1.26` | `1381.0000` | 1,739.37 USD | 1,739.37 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `1.26` | `22.0000` | 27.71 USD | 1,767.08 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `1.26` | `49447.0000` | 62,268.61 USD | 64,035.68 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `1.26` | `39.0000` | 49.11 USD | 64,084.79 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `2708.0000` | 3,409.64 USD | 67,494.43 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `187.0000` | 235.43 USD | 67,729.87 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `1.26` | `49437.0000` | 62,236.24 USD | 129,966.11 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `1.26` | `33378.0000` | 42,016.23 USD | 171,982.33 USD | `3 orders` | `-0.07%` | `-` |
| `BID` | `1.26` | `28498.0000` | 35,870.43 USD | 207,852.77 USD | `3 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `4401.0000` | 5,539.10 USD | 213,391.86 USD | `4 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `62466.0000` | 78,613.46 USD | 292,005.33 USD | `5 orders` | `-0.09%` | `-` |
| `BID` | `1.26` | `8297.0000` | 10,440.94 USD | 302,446.27 USD | `5 orders` | `-0.10%` | `-` |
| `BID` | `1.26` | `28237.0000` | 35,530.62 USD | 337,976.89 USD | `2 orders` | `-0.11%` | `-` |
| `BID` | `1.26` | `9739.0000` | 12,253.61 USD | 350,230.50 USD | `5 orders` | `-0.12%` | `-` |
| `BID` | `1.26` | `57996.0000` | 72,964.77 USD | 423,195.27 USD | `5 orders` | `-0.12%` | `-` |
| `BID` | `1.26` | `12564.0000` | 15,805.51 USD | 439,000.78 USD | `5 orders` | `-0.13%` | `-` |
| `BID` | `1.26` | `53555.0000` | 67,366.83 USD | 506,367.61 USD | `8 orders` | `-0.14%` | `-` |
| `BID` | `1.26` | `15983.0000` | 20,103.42 USD | 526,471.03 USD | `2 orders` | `-0.15%` | `-` |
| `BID` | `1.26` | `51239.0000` | 64,443.29 USD | 590,914.32 USD | `3 orders` | `-0.15%` | `-` |
| `BID` | `1.26` | `8689.0000` | 10,927.29 USD | 601,841.61 USD | `4 orders` | `-0.16%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:04:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `26` | `0x31b1...1434` | `LONG` | 44,528,450.67 USD | `35,031,430.00` | `1.13` | `1.26` | `0.9612` | 4,949,567.41 USD | `+11.12%` | `10X Cross` |
| `92` | `0x5b5d...c060` | `SHORT` | 20,095,799.16 USD | `15,964,251.00` | `1.44` | `1.26` | `11.91` | 2,820,269.55 USD | `+14.03%` | `5X Cross` |
| `151` | `0x58f0...0d20` | `LONG` | 13,900,659.44 USD | `10,931,629.00` | `1.36` | `1.26` | `1.25` | -964,493.52 USD | `-6.94%` | `20X Cross` |
| `156` | `0xb83d...6e36` | `SHORT` | 13,396,977.14 USD | `10,555,450.00` | `1.50` | `1.26` | `14.34` | 2,425,592.50 USD | `+18.11%` | `5X Cross` |
| `439` | `0xca49...53c8` | `SHORT` | 5,214,168.58 USD | `4,138,886.00` | `1.44` | `1.26` | `4.61` | 739,154.15 USD | `+14.18%` | `20X Cross` |
| `442` | `0x77ee...a018` | `LONG` | 5,161,914.92 USD | `4,103,271.00` | `1.27` | `1.26` | `0.1720` | -63,338.68 USD | `-1.23%` | `20X Cross` |
| `445` | `0xfc27...9d9d` | `SHORT` | 5,138,805.36 USD | `4,083,278.00` | `1.31` | `1.26` | `5.16` | 219,961.50 USD | `+4.28%` | `20X Cross` |
| `499` | `0x610b...b613` | `LONG` | 4,505,772.94 USD | `3,543,946.00` | `1.44` | `1.26` | `0.7449` | -594,219.66 USD | `-13.19%` | `5X Cross` |
| `543` | `0xdd53...2b13` | `SHORT` | 4,162,647.35 USD | `3,300,545.00` | `1.44` | `1.26` | `19.44` | 575,934.36 USD | `+13.84%` | `3X Cross` |
| `562` | `0xc30c...a4c9` | `SHORT` | 4,058,116.78 USD | `3,225,848.00` | `1.42` | `1.26` | `1.61` | 532,332.63 USD | `+13.12%` | `8X Cross` |
| `599` | `0xecb6...2b00` | `SHORT` | 3,859,725.54 USD | `3,064,977.00` | `1.30` | `1.26` | `10.87` | 139,509.30 USD | `+3.61%` | `10X Cross` |
| `603` | `0x9946...0852` | `SHORT` | 3,823,740.30 USD | `3,025,111.00` | `1.43` | `1.26` | `1.69` | 489,444.25 USD | `+12.80%` | `20X Cross` |
| `687` | `0x9aa5...58af` | `SHORT` | 3,307,445.82 USD | `2,604,083.00` | `1.46` | `1.26` | `4.33` | 490,274.84 USD | `+14.82%` | `20X Cross` |
| `699` | `0xf48f...10fe` | `LONG` | 3,256,486.71 USD | `2,565,779.00` | `1.53` | `1.26` | `0.9516` | -668,154.02 USD | `-20.52%` | `4X Cross` |
| `731` | `0x023a...2355` | `SHORT` | 3,156,269.80 USD | `2,507,364.00` | `1.33` | `1.26` | `4.55` | 170,516.56 USD | `+5.40%` | `20X Cross` |
| `748` | `0x45d2...4029` | `SHORT` | 3,087,100.50 USD | `2,453,000.00` | `1.48` | `1.26` | `17.68` | 551,179.92 USD | `+17.85%` | `20X Cross` |
| `908` | `0xfc66...ca06` | `SHORT` | 2,496,522.72 USD | `1,981,210.00` | `1.30` | `1.26` | `19.28` | 83,937.28 USD | `+3.36%` | `20X Cross` |
| `1041` | `0xc179...e0c8` | `SHORT` | 2,142,597.75 USD | `1,697,645.00` | `1.30` | `1.26` | `4.85` | 66,647.02 USD | `+3.11%` | `10X Cross` |
| `1083` | `0xeadc...9d55` | `LONG` | 2,054,949.42 USD | `1,619,805.00` | `1.21` | `1.26` | `0.000000` | 96,106.39 USD | `+4.68%` | `20X Cross` |
| `1162` | `0x94b2...599e` | `SHORT` | 1,954,588.57 USD | `1,540,696.00` | `1.36` | `1.26` | `1.85` | 145,877.88 USD | `+7.46%` | `20X Cross` |
| `1172` | `0xbcd4...0dd2` | `SHORT` | 1,941,191.90 USD | `1,529,461.00` | `1.31` | `1.26` | `2.08` | 63,352.70 USD | `+3.26%` | `20X Cross` |
| `1198` | `0x3fc5...c0c1` | `SHORT` | 1,901,817.98 USD | `1,511,779.00` | `1.52` | `1.26` | `2.80` | 389,796.62 USD | `+20.50%` | `20X Cross` |
| `1210` | `0x31ef...f715` | `LONG` | 1,871,305.66 USD | `1,475,080.00` | `1.49` | `1.26` | `1.04` | -327,959.74 USD | `-17.53%` | `3X Isolated` |
| `1274` | `0x7737...bf66` | `SHORT` | 1,795,525.86 USD | `1,413,466.00` | `1.41` | `1.26` | `13.87` | 203,342.79 USD | `+11.32%` | `10X Cross` |
| `1291` | `0xef96...9383` | `SHORT` | 1,752,797.84 USD | `1,390,999.00` | `1.34` | `1.26` | `4.22` | 110,987.38 USD | `+6.33%` | `20X Cross` |
| `1358` | `0xee2b...d67e` | `LONG` | 1,659,633.82 USD | `1,306,284.00` | `1.55` | `1.26` | `0.2871` | -371,021.08 USD | `-22.36%` | `4X Cross` |
| `1430` | `0x215d...f80a` | `LONG` | 1,591,133.74 USD | `1,251,777.00` | `1.32` | `1.26` | `1.15` | -63,320.48 USD | `-3.98%` | `14X Cross` |
| `1470` | `0x123d...3bff` | `LONG` | 1,541,887.90 USD | `1,215,329.00` | `1.35` | `1.26` | `0.000000` | -95,181.32 USD | `-6.17%` | `10X Cross` |
| `1482` | `0x95da...2328` | `LONG` | 1,528,436.36 USD | `1,204,809.00` | `1.36` | `1.26` | `0.000000` | -115,206.48 USD | `-7.54%` | `5X Cross` |
| `1532` | `0xdf95...7d72` | `SHORT` | 1,460,014.80 USD | `1,160,123.00` | `1.37` | `1.26` | `34.91` | 133,354.54 USD | `+9.13%` | `20X Cross` |
| `1553` | `0x5fa3...35b7` | `SHORT` | 1,435,290.44 USD | `1,139,029.00` | `1.31` | `1.26` | `3.27` | 55,211.57 USD | `+3.85%` | `20X Cross` |
| `1682` | `0xb1ce...681b` | `LONG` | 1,286,196.52 USD | `1,021,764.00` | `1.49` | `1.26` | `1.16` | -237,859.97 USD | `-18.49%` | `4X Isolated` |
| `1788` | `0x3c36...461a` | `LONG` | 1,185,216.30 USD | `940,051.00` | `1.30` | `1.26` | `1.06` | -33,864.31 USD | `-2.86%` | `10X Cross` |
| `1864` | `0xe9d1...d2d3` | `SHORT` | 1,118,653.27 USD | `887,961.00` | `1.30` | `1.26` | `2.48` | 39,258.49 USD | `+3.51%` | `10X Cross` |
| `1992` | `0xbfc7...80b4` | `SHORT` | 1,014,912.00 USD | `800,000.00` | `1.48` | `1.26` | `7.26` | 168,542.65 USD | `+16.61%` | `20X Cross` |

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
| `ANNOUNCEMENT` | `INFO` | `1.29` | 23,095.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 23.10K USD at 1.2927 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,127.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.13K USD at 1.2927 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,788.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.79K USD at 1.2927 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 99.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.10K USD at 1.2928 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.01K USD at 1.2929 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 139.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.14K USD at 1.2929 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,786.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.79K USD at 1.2929 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 50.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.2929 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 49.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.2929 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,798.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.80K USD at 1.2930 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,872.53 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.87K USD at 1.2930 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,687.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.69K USD at 1.2931 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 2,388.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.39K USD at 1.2931 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,777.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.78K USD at 1.2934 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 895.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.90K USD at 1.2934 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 895.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.90K USD at 1.2934 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 895.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.90K USD at 1.2934 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 895.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.90K USD at 1.2934 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 536.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.54K USD at 1.2934 USD [API] | `2026-10-15 02:24:27` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.32` (Vol: 2,000,000.00 USD, Dist: `+4.08%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`1.35` (Vol: 3,500,000.00 USD, Dist: `+6.18%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+6.24%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,200,000.00 USD, Dist: `+6.33%`) | Long MP=`1.27` (Vol: 2,800,000.00 USD, Dist: `--0.44%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 334,350.00 USD | 75,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 154.76 USD | 75,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 378.20 USD | 75,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 905.65 USD | 75,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 373.01 USD | 75,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 4,910.00 USD | 75,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 5,350.00 USD | 75,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 6,720.00 USD | 75,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 103.50 USD | 75,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 2,180.00 USD | 75,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 1,020.00 USD | 75,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 4,510.00 USD | 75,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 631.78 USD | 75,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 1,710.00 USD | 75,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 1,650.00 USD | 75,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 996.00 USD | 75,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 9,520.00 USD | 75,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 12,480.00 USD | 75,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 880.65 USD | 75,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 5,510.00 USD | 75,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 133,990.00 USD | 75,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 11,730.00 USD | 74,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 5,220.00 USD | 74,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 2,360.00 USD | 74,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 1,620.00 USD | 74,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 19,720.00 USD | 74,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 8,080.00 USD | 74,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 16,260.00 USD | 74,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 23,320.00 USD | 74,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 5,600.00 USD | 74,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 1,920.00 USD | 74,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 27,710.00 USD | 74,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 51,530.00 USD | 74,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 16,680.00 USD | 74,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 35,250.00 USD | 74,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 1,060.00 USD | 74,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 976.00 USD | 74,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 8,300.00 USD | 74,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 19,440.00 USD | 74,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 18,800.00 USD | 74,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 46,410.00 USD | 74,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 23,300.00 USD | 74,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 8,280.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 24,470.00 USD | 74,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 70,160.00 USD | 74,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 2,790,000.00 USD | 74,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 25,110.00 USD | 71,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 55,080.00 USD | 71,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 107,340.00 USD | 71,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 156,970.00 USD | 71,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 6,520.00 USD | 71,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 42,380.00 USD | 71,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 23,920.00 USD | 71,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 27,910.00 USD | 71,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 22,940.00 USD | 71,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 13,120.00 USD | 71,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 74,930.00 USD | 71,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 58,890.00 USD | 71,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 31,450.00 USD | 71,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 516,010.00 USD | 71,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 118,940.00 USD | 70,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 428,590.00 USD | 70,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 116,840.00 USD | 70,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 118,560.00 USD | 69,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 2,370,000.00 USD | 69,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 76,920.00 USD | 67,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 187,890.00 USD | 67,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 268,870.00 USD | 67,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 697,810.00 USD | 66,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,920,000.00 USD | 66,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 157,800.00 USD | 32,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 450,020.00 USD | 32,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 481,930.00 USD | 31,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 523,400.00 USD | 31,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 263,670.00 USD | 30,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 138,580.00 USD | 30,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,120,000.00 USD | 30,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 88,490.00 USD | 28,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,080,000.00 USD | 28,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 401,440.00 USD | 26,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 459,350.00 USD | 26,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 784,410.00 USD | 26,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 99,690.00 USD | 25,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 59,350.00 USD | 25,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 592,630.00 USD | 25,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 276,220.00 USD | 24,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.13` | 127,990,000.00 USD | 127,990,000.00 USD | 144,660.00 USD | 944.65 USD | 225,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 76,470.00 USD | 24,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.14` | 127,620,000.00 USD | 127,620,000.00 USD | 79,780.00 USD | 43,440.00 USD | 71,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 127,430,000.00 USD | 127,430,000.00 USD | 0.00 USD | 0.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 38,040,000.00 USD | 38,040,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 127,410,000.00 USD | 127,410,000.00 USD | 39,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 38,020,000.00 USD | 38,020,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 127,370,000.00 USD | 127,370,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 37,950,000.00 USD | 37,950,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 127,240,000.00 USD | 127,240,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 37,810,000.00 USD | 37,810,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 614,970.00 USD | 24,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 127,230,000.00 USD | 127,230,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 127,160,000.00 USD | 127,160,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 37,770,000.00 USD | 37,770,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 126,790,000.00 USD | 126,790,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 126,640,000.00 USD | 126,640,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 37,760,000.00 USD | 37,760,000.00 USD | 4,040.00 USD | 11,230.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 126,470,000.00 USD | 126,470,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 37,560,000.00 USD | 37,560,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 119,460.00 USD | 23,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 125,590,000.00 USD | 125,590,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 37,220,000.00 USD | 37,220,000.00 USD | 29,120.00 USD | 9,570.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 125,360,000.00 USD | 125,360,000.00 USD | 258,370.00 USD | 96,700.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 37,150,000.00 USD | 37,150,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 124,500,000.00 USD | 124,500,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 36,830,000.00 USD | 36,830,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 123,760,000.00 USD | 123,760,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 36,210,000.00 USD | 36,210,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 122,710,000.00 USD | 122,710,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 35,590,000.00 USD | 35,590,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,600,000.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.17` | 121,380,000.00 USD | 121,380,000.00 USD | 218,150.00 USD | 212,700.00 USD | 529,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 35,380,000.00 USD | 35,380,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 120,420,000.00 USD | 120,420,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 35,060,000.00 USD | 35,060,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 119,350,000.00 USD | 119,350,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 34,900,000.00 USD | 34,900,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 117,320,000.00 USD | 117,320,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 34,730,000.00 USD | 34,730,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 116,470,000.00 USD | 116,470,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 34,480,000.00 USD | 34,480,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 274,810.00 USD | 21,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.18` | 115,580,000.00 USD | 115,580,000.00 USD | 181,850.00 USD | 95,620.00 USD | 377,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 34,140,000.00 USD | 34,140,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 114,930,000.00 USD | 114,930,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 34,010,000.00 USD | 34,010,000.00 USD | 77,850.00 USD | 41,360.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 114,510,000.00 USD | 114,510,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 33,840,000.00 USD | 33,840,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 113,890,000.00 USD | 113,890,000.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 33,810,000.00 USD | 33,810,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 113,650,000.00 USD | 113,650,000.00 USD | 116,030.00 USD | 65,900.00 USD | 235,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 33,700,000.00 USD | 33,700,000.00 USD | 48,820.00 USD | 7,460.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 2,220,000.00 USD | 21,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.19` | 113,240,000.00 USD | 113,240,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 33,620,000.00 USD | 33,620,000.00 USD | 1,560.00 USD | 16,590.00 USD | 20,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 113,060,000.00 USD | 113,060,000.00 USD | 216,330.00 USD | 94,590.00 USD | 604,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 33,580,000.00 USD | 33,580,000.00 USD | 29,730.00 USD | 103.33 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 112,140,000.00 USD | 112,140,000.00 USD | 211,840.00 USD | 81,140.00 USD | 281,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 33,530,000.00 USD | 33,530,000.00 USD | 28,290.00 USD | 10,480.00 USD | 48,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 111,570,000.00 USD | 111,570,000.00 USD | 149,990.00 USD | 95,880.00 USD | 123,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 33,450,000.00 USD | 33,450,000.00 USD | 42,050.00 USD | 27,990.00 USD | 102,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 111,200,000.00 USD | 111,200,000.00 USD | 219,860.00 USD | 72,930.00 USD | 465,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 33,270,000.00 USD | 33,270,000.00 USD | 76,810.00 USD | 33,950.00 USD | 31,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 671,140.00 USD | 19,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.20` | 110,440,000.00 USD | 110,440,000.00 USD | 251,760.00 USD | 140,610.00 USD | 318,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 33,130,000.00 USD | 33,130,000.00 USD | 107,100.00 USD | 6,620.00 USD | 18,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 109,730,000.00 USD | 109,730,000.00 USD | 5,350.00 USD | 38,700.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 33,000,000.00 USD | 33,000,000.00 USD | 22,650.00 USD | 21,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 109,670,000.00 USD | 109,670,000.00 USD | 72,960.00 USD | 36,750.00 USD | 18,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 109,540,000.00 USD | 109,540,000.00 USD | 184,030.00 USD | 62,270.00 USD | 57,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 109,230,000.00 USD | 109,230,000.00 USD | 47,500.00 USD | 29,680.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 644,280.00 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.21` | 109,080,000.00 USD | 109,080,000.00 USD | 13,620.00 USD | 3,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 109,060,000.00 USD | 109,060,000.00 USD | 241,190.00 USD | 2,360.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 108,790,000.00 USD | 108,790,000.00 USD | 257,960.00 USD | 89,570.00 USD | 624,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 107,820,000.00 USD | 107,820,000.00 USD | 199,450.00 USD | 109,690.00 USD | 212,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 107,300,000.00 USD | 107,300,000.00 USD | 84,480.00 USD | 89,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 32,960,000.00 USD | 32,960,000.00 USD | 65,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 369,930.00 USD | 18,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 107,130,000.00 USD | 107,130,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 32,890,000.00 USD | 32,890,000.00 USD | 79,080.00 USD | 1,870.00 USD | 83,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 107,030,000.00 USD | 107,030,000.00 USD | 316,090.00 USD | 3,350.00 USD | 27,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 32,730,000.00 USD | 32,730,000.00 USD | 261,180.00 USD | 1,240.00 USD | 178,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 106,680,000.00 USD | 106,680,000.00 USD | 104,680.00 USD | 2,640.00 USD | 174,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 32,280,000.00 USD | 32,280,000.00 USD | 12,860.00 USD | 1,430.00 USD | 131,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 106,400,000.00 USD | 106,400,000.00 USD | 59,120.00 USD | 2,680.00 USD | 318,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 32,140,000.00 USD | 32,140,000.00 USD | 0.00 USD | 211.25 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 106,020,000.00 USD | 106,020,000.00 USD | 251,420.00 USD | 302,320.00 USD | 112,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 32,140,000.00 USD | 32,140,000.00 USD | 40,080.00 USD | 206.80 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,560,000.00 USD | 17,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 105,350,000.00 USD | 105,350,000.00 USD | 492,660.00 USD | 141,800.00 USD | 153,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 104,570,000.00 USD | 104,570,000.00 USD | 269,210.00 USD | 135,700.00 USD | 277,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 32,100,000.00 USD | 32,100,000.00 USD | 100,480.00 USD | 562.84 USD | 160,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 103,880,000.00 USD | 103,880,000.00 USD | 254,940.00 USD | 112,100.00 USD | 795,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 31,840,000.00 USD | 31,840,000.00 USD | 327,750.00 USD | 105,590.00 USD | 715,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 102,720,000.00 USD | 102,720,000.00 USD | 944,780.00 USD | 474,960.00 USD | 940,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 30,690,000.00 USD | 30,690,000.00 USD | 141,680.00 USD | 54,570.00 USD | 208,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 100,360,000.00 USD | 100,360,000.00 USD | 1,130,000.00 USD | 364,060.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 30,280,000.00 USD | 30,280,000.00 USD | 139,070.00 USD | 22,970.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 570,730.00 USD | 16,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.24` | 97,320,000.00 USD | 97,320,000.00 USD | 1,120,000.00 USD | 760,590.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 30,110,000.00 USD | 30,110,000.00 USD | 802,870.00 USD | 317,390.00 USD | 716,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 92,830,000.00 USD | 92,830,000.00 USD | 1,960,000.00 USD | 859,010.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 28,280,000.00 USD | 28,280,000.00 USD | 1,340,000.00 USD | 641,660.00 USD | 928,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 87,930,000.00 USD | 87,930,000.00 USD | 2,210,000.00 USD | 1,010,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 25,370,000.00 USD | 25,370,000.00 USD | 708,030.00 USD | 333,360.00 USD | 574,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 82,010,000.00 USD | 82,010,000.00 USD | 1,210,000.00 USD | 569,760.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 23,760,000.00 USD | 23,760,000.00 USD | 365,160.00 USD | 237,390.00 USD | 491,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 78,960,000.00 USD | 78,960,000.00 USD | 1,660,000.00 USD | 544,230.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 22,660,000.00 USD | 22,660,000.00 USD | 1,070,000.00 USD | 86,590.00 USD | 707,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 242,000.00 USD | 15,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.25` | 75,090,000.00 USD | 75,090,000.00 USD | 2,730,000.00 USD | 695,090.00 USD | 3,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 20,800,000.00 USD | 20,800,000.00 USD | 409,930.00 USD | 93,700.00 USD | 524,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 68,300,000.00 USD | 68,300,000.00 USD | 2,150,000.00 USD | 1,450,000.00 USD | 6,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 19,770,000.00 USD | 19,770,000.00 USD | 207,040.00 USD | 196,930.00 USD | 303,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 58,540,000.00 USD | 58,540,000.00 USD | 3,090,000.00 USD | 1,160,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 19,060,000.00 USD | 19,060,000.00 USD | 198,150.00 USD | 80,220.00 USD | 571,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 52,120,000.00 USD | 52,120,000.00 USD | 2,140,000.00 USD | 783,920.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 18,210,000.00 USD | 18,210,000.00 USD | 659,550.00 USD | 17,220.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 47,760,000.00 USD | 47,760,000.00 USD | 262,320.00 USD | 552,710.00 USD | 814,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 17,000,000.00 USD | 17,000,000.00 USD | 830,250.00 USD | 98,620.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 830,060.00 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.26` | 46,130,000.00 USD | 46,130,000.00 USD | 2,900,000.00 USD | 1,090,000.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 14,640,000.00 USD | 14,640,000.00 USD | 1,770,000.00 USD | 413,380.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 39,210,000.00 USD | 39,210,000.00 USD | 1,490,000.00 USD | 211,890.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 10,570,000.00 USD | 10,570,000.00 USD | 366,730.00 USD | 3,600.00 USD | 839,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 35,880,000.00 USD | 35,880,000.00 USD | 1,210,000.00 USD | 691,780.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 9,360,000.00 USD | 9,360,000.00 USD | 437,560.00 USD | 218,760.00 USD | 631,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 31,770,000.00 USD | 31,770,000.00 USD | 1,980,000.00 USD | 1,450,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 8,080,000.00 USD | 8,080,000.00 USD | 1,570,000.00 USD | 545,220.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 26,820,000.00 USD | 26,820,000.00 USD | 3,140,000.00 USD | 1,970,000.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 1,350,000.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.26` | 14,310,000.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.27` | 18,190,000.00 USD | 18,190,000.00 USD | 4,220,000.00 USD | 1,960,000.00 USD | 6,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 663,670.00 USD | 23,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 1,360,000.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 874,600.00 USD | 874,600.00 USD | 0.00 USD | 874,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 2,580,000.00 USD | 183,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 2,580,000.00 USD | 183,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 433,120.00 USD | 433,120.00 USD | 0.00 USD | 415,170.00 USD | 17,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 866,240.00 USD | 866,240.00 USD | 0.00 USD | 415,170.00 USD | 17,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 8,620,000.00 USD | 8,620,000.00 USD | 306,560.00 USD | 2,550,000.00 USD | 230,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 2,260,000.00 USD | 2,260,000.00 USD | 1,000,000.00 USD | 318,590.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 18,190,000.00 USD | 18,190,000.00 USD | 2,220,000.00 USD | 1,720,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 5,940,000.00 USD | 5,940,000.00 USD | 42,830.00 USD | 838,580.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.27` | 169,550.00 USD | 169,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.28` | 30,680,000.00 USD | 30,680,000.00 USD | 4,130,000.00 USD | 2,410,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 15,920,000.00 USD | 15,920,000.00 USD | 3,210,000.00 USD | 2,800,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 46,400,000.00 USD | 46,400,000.00 USD | 7,720,000.00 USD | 2,860,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 23,150,000.00 USD | 23,150,000.00 USD | 3,220,000.00 USD | 2,050,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 47,900,000.00 USD | 47,900,000.00 USD | 0.00 USD | 1,420,000.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 23,890,000.00 USD | 23,890,000.00 USD | 209,970.00 USD | 221,010.00 USD | 312,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 49,040,000.00 USD | 49,040,000.00 USD | 1,030,000.00 USD | 22,110.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 25,520,000.00 USD | 25,520,000.00 USD | 915,930.00 USD | 0.00 USD | 708,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 50,210,000.00 USD | 50,210,000.00 USD | 418,730.00 USD | 6,660.00 USD | 744,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 26,530,000.00 USD | 26,530,000.00 USD | 0.00 USD | 488,880.00 USD | 526,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 52,240,000.00 USD | 52,240,000.00 USD | 505,690.00 USD | 888,530.00 USD | 643,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 27,010,000.00 USD | 27,010,000.00 USD | 365,870.00 USD | 100,470.00 USD | 8,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 52,680,000.00 USD | 52,680,000.00 USD | 440,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 27,170,000.00 USD | 27,170,000.00 USD | 160,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 53,160,000.00 USD | 53,160,000.00 USD | 0.00 USD | 0.00 USD | 472,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 27,300,000.00 USD | 27,300,000.00 USD | 131,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 54,840,000.00 USD | 54,840,000.00 USD | 1,040,000.00 USD | 0.00 USD | 648,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 29,880,000.00 USD | 29,880,000.00 USD | 546,160.00 USD | 3,750.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 58,260,000.00 USD | 58,260,000.00 USD | 1,740,000.00 USD | 6,700.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 35,730,000.00 USD | 35,730,000.00 USD | 1,800,000.00 USD | 604,970.00 USD | 3,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.30` | 65,500,000.00 USD | 65,500,000.00 USD | 1,940,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 37,950,000.00 USD | 37,950,000.00 USD | 497,720.00 USD | 629,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 67,060,000.00 USD | 67,060,000.00 USD | 0.00 USD | 0.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 38,290,000.00 USD | 38,290,000.00 USD | 254,730.00 USD | 87,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 68,040,000.00 USD | 68,040,000.00 USD | 0.00 USD | 0.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 39,820,000.00 USD | 39,820,000.00 USD | 274,080.00 USD | 81,740.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 68,890,000.00 USD | 68,890,000.00 USD | 0.00 USD | 859,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 41,250,000.00 USD | 41,250,000.00 USD | 516,450.00 USD | 910,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 70,840,000.00 USD | 70,840,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 42,030,000.00 USD | 42,030,000.00 USD | 299,990.00 USD | 351,800.00 USD | 127,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 900.45 USD | 4,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.31` | 72,790,000.00 USD | 72,790,000.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 43,790,000.00 USD | 43,790,000.00 USD | 608,060.00 USD | 115,080.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 77,010,000.00 USD | 77,010,000.00 USD | 1,240,000.00 USD | 590,530.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 46,800,000.00 USD | 46,800,000.00 USD | 995,780.00 USD | 263,400.00 USD | 1,760,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 78,770,000.00 USD | 78,770,000.00 USD | 1,340,000.00 USD | 0.00 USD | 415,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 48,750,000.00 USD | 48,750,000.00 USD | 807,130.00 USD | 688,780.00 USD | 450,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 82,520,000.00 USD | 82,520,000.00 USD | 79,920.00 USD | 747,120.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 51,490,000.00 USD | 51,490,000.00 USD | 1,290,000.00 USD | 511,150.00 USD | 944,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 83,670,000.00 USD | 83,670,000.00 USD | 515,950.00 USD | 149,950.00 USD | 485,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 54,800,000.00 USD | 54,800,000.00 USD | 372,630.00 USD | 572,040.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 86,800.00 USD | 91,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.32` | 87,860,000.00 USD | 87,860,000.00 USD | 44,360.00 USD | 1,750,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 61,410,000.00 USD | 61,410,000.00 USD | 1,320,000.00 USD | 1,730,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 92,700,000.00 USD | 92,700,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 66,800,000.00 USD | 66,800,000.00 USD | 1,960,000.00 USD | 978,950.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 94,730,000.00 USD | 94,730,000.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 70,310,000.00 USD | 70,310,000.00 USD | 1,650,000.00 USD | 652,780.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 98,080,000.00 USD | 98,080,000.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 74,900,000.00 USD | 74,900,000.00 USD | 1,990,000.00 USD | 583,250.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 100,860,000.00 USD | 100,860,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 76,900,000.00 USD | 76,900,000.00 USD | 1,080,000.00 USD | 287,760.00 USD | 625,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 54,470.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.33` | 102,660,000.00 USD | 102,660,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 79,430,000.00 USD | 79,430,000.00 USD | 664,210.00 USD | 621,550.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 103,720,000.00 USD | 103,720,000.00 USD | 135,420.00 USD | 15,840.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 81,670,000.00 USD | 81,670,000.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 105,340,000.00 USD | 105,340,000.00 USD | 548,610.00 USD | 138,580.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 84,510,000.00 USD | 84,510,000.00 USD | 848,670.00 USD | 298,810.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 107,760,000.00 USD | 107,760,000.00 USD | 829,540.00 USD | 236,880.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 86,900,000.00 USD | 86,900,000.00 USD | 1,040,000.00 USD | 190,550.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 109,790,000.00 USD | 109,790,000.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 88,990,000.00 USD | 88,990,000.00 USD | 859,040.00 USD | 354,550.00 USD | 872,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 52,400.00 USD | 198,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.34` | 111,330,000.00 USD | 111,330,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 91,080,000.00 USD | 91,080,000.00 USD | 896,540.00 USD | 219,260.00 USD | 976,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 113,770,000.00 USD | 113,770,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 93,940,000.00 USD | 93,940,000.00 USD | 1,170,000.00 USD | 370,350.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 115,640,000.00 USD | 115,640,000.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 97,540,000.00 USD | 97,540,000.00 USD | 1,780,000.00 USD | 821,890.00 USD | 996,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 121,560,000.00 USD | 121,560,000.00 USD | 2,380,000.00 USD | 2,880,000.00 USD | 665,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 102,270,000.00 USD | 102,270,000.00 USD | 2,510,000.00 USD | 785,850.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 128,790,000.00 USD | 128,790,000.00 USD | 2,030,000.00 USD | 2,210,000.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 104,470,000.00 USD | 104,470,000.00 USD | 810,880.00 USD | 629,160.00 USD | 762,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 161,520.00 USD | 359,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.35` | 139,530,000.00 USD | 139,530,000.00 USD | 4,040,000.00 USD | 1,900,000.00 USD | 4,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 105,520,000.00 USD | 105,520,000.00 USD | 355,660.00 USD | 234,160.00 USD | 458,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 148,370,000.00 USD | 148,370,000.00 USD | 3,160,000.00 USD | 2,040,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 107,010,000.00 USD | 107,010,000.00 USD | 752,410.00 USD | 149,380.00 USD | 594,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 157,570,000.00 USD | 157,570,000.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 108,100,000.00 USD | 108,100,000.00 USD | 507,940.00 USD | 127,500.00 USD | 452,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 166,830,000.00 USD | 166,830,000.00 USD | 3,040,000.00 USD | 1,390,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 109,890,000.00 USD | 109,890,000.00 USD | 716,900.00 USD | 341,320.00 USD | 728,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 174,370,000.00 USD | 174,370,000.00 USD | 2,320,000.00 USD | 886,190.00 USD | 4,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 111,580,000.00 USD | 111,580,000.00 USD | 599,030.00 USD | 297,760.00 USD | 791,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 4,370.00 USD | 364,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.36` | 181,530,000.00 USD | 181,530,000.00 USD | 2,820,000.00 USD | 1,060,000.00 USD | 3,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 113,300,000.00 USD | 113,300,000.00 USD | 973,410.00 USD | 66,140.00 USD | 685,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 184,060,000.00 USD | 184,060,000.00 USD | 1,040,000.00 USD | 639,580.00 USD | 849,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 113,860,000.00 USD | 113,860,000.00 USD | 326,950.00 USD | 148,910.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 187,130,000.00 USD | 187,130,000.00 USD | 1,430,000.00 USD | 410,060.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 114,470,000.00 USD | 114,470,000.00 USD | 259,250.00 USD | 149,990.00 USD | 197,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 190,910,000.00 USD | 190,910,000.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 114,810,000.00 USD | 114,810,000.00 USD | 171,250.00 USD | 0.00 USD | 166,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 193,660,000.00 USD | 193,660,000.00 USD | 1,430,000.00 USD | 614,410.00 USD | 702,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 114,860,000.00 USD | 114,860,000.00 USD | 0.00 USD | 26,460.00 USD | 25,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 198,460.00 USD | 562,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.37` | 194,400,000.00 USD | 194,400,000.00 USD | 206,650.00 USD | 111,150.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 115,130,000.00 USD | 115,130,000.00 USD | 53,740.00 USD | 57,080.00 USD | 165,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 195,500,000.00 USD | 195,500,000.00 USD | 535,200.00 USD | 181,820.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 115,330,000.00 USD | 115,330,000.00 USD | 121,310.00 USD | 1,410.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 197,100,000.00 USD | 197,100,000.00 USD | 477,130.00 USD | 362,580.00 USD | 755,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 115,510,000.00 USD | 115,510,000.00 USD | 1,740.00 USD | 66,370.00 USD | 119,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 199,170,000.00 USD | 199,170,000.00 USD | 743,900.00 USD | 285,210.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 115,660,000.00 USD | 115,660,000.00 USD | 75,340.00 USD | 249.08 USD | 69,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 201,280,000.00 USD | 201,280,000.00 USD | 737,410.00 USD | 437,690.00 USD | 940,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 115,780,000.00 USD | 115,780,000.00 USD | 54,550.00 USD | 884.30 USD | 69,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 464.75 USD | 562,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.38` | 202,950,000.00 USD | 202,950,000.00 USD | 450,750.00 USD | 380,930.00 USD | 841,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 116,110,000.00 USD | 116,110,000.00 USD | 112,910.00 USD | 50,330.00 USD | 164,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 204,500,000.00 USD | 204,500,000.00 USD | 878,240.00 USD | 363,870.00 USD | 308,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 116,650,000.00 USD | 116,650,000.00 USD | 254,930.00 USD | 72,410.00 USD | 212,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 206,550,000.00 USD | 206,550,000.00 USD | 506,860.00 USD | 199,720.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 117,110,000.00 USD | 117,110,000.00 USD | 240,520.00 USD | 108,980.00 USD | 109,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 208,820,000.00 USD | 208,820,000.00 USD | 841,840.00 USD | 445,210.00 USD | 985,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 117,510,000.00 USD | 117,510,000.00 USD | 299,660.00 USD | 24,460.00 USD | 77,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 209,520,000.00 USD | 209,520,000.00 USD | 403,730.00 USD | 160,810.00 USD | 129,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 117,620,000.00 USD | 117,620,000.00 USD | 56,620.00 USD | 53,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 36,950.00 USD | 599,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.39` | 210,430,000.00 USD | 210,430,000.00 USD | 377,810.00 USD | 134,820.00 USD | 406,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 211,300,000.00 USD | 211,300,000.00 USD | 384,080.00 USD | 263,660.00 USD | 218,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 212,040,000.00 USD | 212,040,000.00 USD | 497,500.00 USD | 118,700.00 USD | 118,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 212,360,000.00 USD | 212,360,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 117,650,000.00 USD | 117,650,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 212,420,000.00 USD | 212,420,000.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 117,710,000.00 USD | 117,710,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 177,010.00 USD | 776,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 212,650,000.00 USD | 212,650,000.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 117,850,000.00 USD | 117,850,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 212,650,000.00 USD | 212,650,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 117,890,000.00 USD | 117,890,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 212,720,000.00 USD | 212,720,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 212,790,000.00 USD | 212,790,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 117,910,000.00 USD | 117,910,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 213,090,000.00 USD | 213,090,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 1,110.00 USD | 778,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 213,240,000.00 USD | 213,240,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 213,410,000.00 USD | 213,410,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 118,110,000.00 USD | 118,110,000.00 USD | 4,040.00 USD | 11,230.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 214,290,000.00 USD | 214,290,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 118,450,000.00 USD | 118,450,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 214,520,000.00 USD | 214,520,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 118,480,000.00 USD | 118,480,000.00 USD | 0.00 USD | 383.75 USD | 28,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 214,820,000.00 USD | 214,820,000.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 118,520,000.00 USD | 118,520,000.00 USD | 29,120.00 USD | 9,190.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 781,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.42` | 215,380,000.00 USD | 215,380,000.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 118,830,000.00 USD | 118,830,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 216,120,000.00 USD | 216,120,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 119,450,000.00 USD | 119,450,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 217,170,000.00 USD | 217,170,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 119,970,000.00 USD | 119,970,000.00 USD | 282,790.00 USD | 47,360.00 USD | 187,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 218,500,000.00 USD | 218,500,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 218,700,000.00 USD | 218,700,000.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 94,400.00 USD | 876,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.43` | 219,460,000.00 USD | 219,460,000.00 USD | 151,730.00 USD | 92,020.00 USD | 521,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 220,530,000.00 USD | 220,530,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 222,560,000.00 USD | 222,560,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 223,410,000.00 USD | 223,410,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 224,300,000.00 USD | 224,300,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 32,780.00 USD | 909,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 224,330,000.00 USD | 224,330,000.00 USD | 6,560.00 USD | 12,030.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 224,950,000.00 USD | 224,950,000.00 USD | 175,290.00 USD | 83,590.00 USD | 366,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 225,370,000.00 USD | 225,370,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 225,990,000.00 USD | 225,990,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 226,230,000.00 USD | 226,230,000.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 588,370.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.45` | 226,320,000.00 USD | 226,320,000.00 USD | 50,420.00 USD | 39,100.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 226,640,000.00 USD | 226,640,000.00 USD | 65,610.00 USD | 26,800.00 USD | 226,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 226,820,000.00 USD | 226,820,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 227,740,000.00 USD | 227,740,000.00 USD | 216,330.00 USD | 94,590.00 USD | 604,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 228,290,000.00 USD | 228,290,000.00 USD | 193,090.00 USD | 81,140.00 USD | 278,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 228,490,000.00 USD | 228,490,000.00 USD | 58,970.00 USD | 42,150.00 USD | 100,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.46` | 3,360.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 41,640.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 10,700.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 40,610.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 11,950.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 734.44 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 6,630.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.52` | 234.85 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 1,010.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 1,370.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,840.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 5,260,000.00 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 599.17 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 3,350.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 11,270.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 5,010,000.00 USD | 11,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 135,930.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 760.45 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 18,860.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 242.38 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 1,690.00 USD | 12,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 15,070.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,960.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 149.17 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 808.37 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 129,540.00 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 4,010.00 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 838.53 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 406.98 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 3,060,000.00 USD | 15,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 6,300.00 USD | 15,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 732.73 USD | 15,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,340.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 219.38 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 13,850.00 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 5,760.00 USD | 15,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 9,900.00 USD | 15,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 113,600.00 USD | 15,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 15,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 620,680.00 USD | 16,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 1,760.00 USD | 16,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.99` | 318,940.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 401.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 971.23 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 1,810.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 241,070.00 USD | 16,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 5,330.00 USD | 16,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.08` | 40,840.00 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 331.01 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 294.70 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,100.00 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,250,000.00 USD | 19,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.13` | 173,550.00 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 515.05 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,730.00 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 703.57 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 2,820.00 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 8,920.00 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 2,320,000.00 USD | 22,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 1,350.00 USD | 22,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 4,010.00 USD | 22,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 12,490.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 51,650.00 USD | 22,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 14,930.00 USD | 22,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 67,070.00 USD | 22,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 5,770.00 USD | 22,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 77,580.00 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 2,670.00 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 90,600.00 USD | 22,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 11,870.00 USD | 22,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 950,110.00 USD | 23,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 257.58 USD | 23,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 181,260.00 USD | 23,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 92,830.00 USD | 23,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 2,590.00 USD | 23,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 1,120.00 USD | 23,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 24,720.00 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 311.79 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 4,190.00 USD | 24,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 14,040.00 USD | 24,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 4,730.00 USD | 24,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 5,970.00 USD | 24,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 42,710.00 USD | 24,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.54` | 496.86 USD | 24,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.54` | 117.07 USD | 24,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 11,280.00 USD | 24,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 187.25 USD | 24,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 75,490,000.00 USD | 0.00 USD | 334,350.00 USD | `-80.11%` | `1,311,184.00` |
| `Live` | `Long` | `0.2650` | 75,160,000.00 USD | 0.00 USD | 154.76 USD | `-79.33%` | `584.00` |
| `Live` | `Long` | `0.2850` | 75,160,000.00 USD | 0.00 USD | 378.20 USD | `-77.77%` | `1,327.00` |
| `Live` | `Long` | `0.2950` | 75,160,000.00 USD | 0.00 USD | 905.65 USD | `-76.99%` | `3,070.00` |
| `Live` | `Long` | `0.3050` | 75,160,000.00 USD | 0.00 USD | 373.01 USD | `-76.21%` | `1,223.00` |
| `Live` | `Long` | `0.3150` | 75,150,000.00 USD | 0.00 USD | 4,910.00 USD | `-75.43%` | `15,577.00` |
| `Live` | `Long` | `0.3250` | 75,150,000.00 USD | 0.00 USD | 5,350.00 USD | `-74.65%` | `16,466.00` |
| `Live` | `Long` | `0.3350` | 75,140,000.00 USD | 0.00 USD | 6,720.00 USD | `-73.87%` | `20,071.00` |
| `Live` | `Long` | `0.3450` | 75,140,000.00 USD | 0.00 USD | 103.50 USD | `-73.09%` | `300.00` |
| `Live` | `Long` | `0.3550` | 75,140,000.00 USD | 0.00 USD | 2,180.00 USD | `-72.31%` | `6,137.00` |
| `Live` | `Long` | `0.3650` | 75,140,000.00 USD | 0.00 USD | 1,020.00 USD | `-71.53%` | `2,790.00` |
| `Live` | `Long` | `0.3750` | 75,130,000.00 USD | 0.00 USD | 4,510.00 USD | `-70.75%` | `12,021.00` |
| `Live` | `Long` | `0.3850` | 75,130,000.00 USD | 0.00 USD | 631.78 USD | `-69.97%` | `1,641.00` |
| `Live` | `Long` | `0.3950` | 75,130,000.00 USD | 0.00 USD | 1,710.00 USD | `-69.19%` | `4,340.00` |
| `Live` | `Long` | `0.4050` | 75,130,000.00 USD | 0.00 USD | 1,650.00 USD | `-68.41%` | `4,073.00` |
| `Live` | `Long` | `0.4150` | 75,130,000.00 USD | 0.00 USD | 996.00 USD | `-67.63%` | `2,400.00` |
| `Live` | `Long` | `0.4250` | 75,130,000.00 USD | 0.00 USD | 9,520.00 USD | `-66.85%` | `22,401.00` |
| `Live` | `Long` | `0.4350` | 75,120,000.00 USD | 0.00 USD | 12,480.00 USD | `-66.07%` | `28,690.00` |
| `Live` | `Long` | `0.4450` | 75,100,000.00 USD | 0.00 USD | 880.65 USD | `-65.29%` | `1,979.00` |
| `Live` | `Long` | `0.4550` | 75,100,000.00 USD | 0.00 USD | 5,510.00 USD | `-64.51%` | `12,100.00` |
| `Live` | `Long` | `0.4650` | 75,100,000.00 USD | 0.00 USD | 133,990.00 USD | `-63.73%` | `288,140.00` |
| `Live` | `Long` | `0.4750` | 74,960,000.00 USD | 0.00 USD | 11,730.00 USD | `-62.95%` | `24,687.00` |
| `Live` | `Long` | `0.4850` | 74,950,000.00 USD | 0.00 USD | 5,220.00 USD | `-62.17%` | `10,755.00` |
| `Live` | `Long` | `0.4950` | 74,950,000.00 USD | 0.00 USD | 2,360.00 USD | `-61.39%` | `4,766.00` |
| `Live` | `Long` | `0.5050` | 74,940,000.00 USD | 0.00 USD | 1,620.00 USD | `-60.61%` | `3,199.00` |
| `Live` | `Long` | `0.5150` | 74,940,000.00 USD | 0.00 USD | 19,720.00 USD | `-59.83%` | `38,298.00` |
| `Live` | `Long` | `0.5250` | 74,920,000.00 USD | 0.00 USD | 8,080.00 USD | `-59.05%` | `15,391.00` |
| `Live` | `Long` | `0.5350` | 74,910,000.00 USD | 0.00 USD | 16,260.00 USD | `-58.27%` | `30,395.00` |
| `Live` | `Long` | `0.5450` | 74,900,000.00 USD | 0.00 USD | 23,320.00 USD | `-57.49%` | `42,797.00` |
| `Live` | `Long` | `0.5550` | 74,870,000.00 USD | 0.00 USD | 5,600.00 USD | `-56.72%` | `10,087.00` |
| `Live` | `Long` | `0.5650` | 74,870,000.00 USD | 0.00 USD | 1,920.00 USD | `-55.94%` | `3,392.00` |
| `Live` | `Long` | `0.5750` | 74,870,000.00 USD | 0.00 USD | 27,710.00 USD | `-55.16%` | `48,190.00` |
| `Live` | `Long` | `0.5950` | 74,840,000.00 USD | 0.00 USD | 51,530.00 USD | `-53.60%` | `86,604.00` |
| `Live` | `Long` | `0.6050` | 74,790,000.00 USD | 0.00 USD | 16,680.00 USD | `-52.82%` | `27,571.00` |
| `Live` | `Long` | `0.6150` | 74,770,000.00 USD | 0.00 USD | 35,250.00 USD | `-52.04%` | `57,311.00` |
| `Live` | `Long` | `0.6250` | 74,740,000.00 USD | 0.00 USD | 1,060.00 USD | `-51.26%` | `1,704.00` |
| `Live` | `Long` | `0.6350` | 74,730,000.00 USD | 0.00 USD | 976.00 USD | `-50.48%` | `1,537.00` |
| `Live` | `Long` | `0.6450` | 74,730,000.00 USD | 0.00 USD | 8,300.00 USD | `-49.70%` | `12,875.00` |
| `Live` | `Long` | `0.6550` | 74,730,000.00 USD | 0.00 USD | 19,440.00 USD | `-48.92%` | `29,679.00` |
| `Live` | `Long` | `0.6650` | 74,710,000.00 USD | 0.00 USD | 18,800.00 USD | `-48.14%` | `28,277.00` |
| `Live` | `Long` | `0.6750` | 74,690,000.00 USD | 0.00 USD | 46,410.00 USD | `-47.36%` | `68,753.00` |
| `Live` | `Long` | `0.6850` | 74,640,000.00 USD | 0.00 USD | 23,300.00 USD | `-46.58%` | `34,021.00` |
| `Live` | `Long` | `0.6950` | 74,620,000.00 USD | 0.00 USD | 8,280.00 USD | `-45.80%` | `11,914.00` |
| `Live` | `Long` | `0.7050` | 74,610,000.00 USD | 0.00 USD | 24,470.00 USD | `-45.02%` | `34,716.00` |
| `Live` | `Long` | `0.7150` | 74,580,000.00 USD | 0.00 USD | 70,160.00 USD | `-44.24%` | `98,129.00` |
| `Live` | `Long` | `0.7250` | 74,510,000.00 USD | 0.00 USD | 2,790,000.00 USD | `-43.46%` | `3,847,640.00` |
| `Live` | `Long` | `0.7350` | 71,730,000.00 USD | 0.00 USD | 25,110.00 USD | `-42.68%` | `34,166.00` |
| `Live` | `Long` | `0.7450` | 71,700,000.00 USD | 0.00 USD | 55,080.00 USD | `-41.90%` | `73,927.00` |
| `Live` | `Long` | `0.7550` | 71,640,000.00 USD | 0.00 USD | 107,340.00 USD | `-41.12%` | `142,167.00` |
| `Live` | `Long` | `0.7650` | 71,540,000.00 USD | 0.00 USD | 156,970.00 USD | `-40.34%` | `205,196.00` |
| `Live` | `Long` | `0.7750` | 71,380,000.00 USD | 0.00 USD | 6,520.00 USD | `-39.56%` | `8,409.00` |
| `Live` | `Long` | `0.7850` | 71,370,000.00 USD | 0.00 USD | 42,380.00 USD | `-38.78%` | `53,984.00` |
| `Live` | `Long` | `0.7950` | 71,330,000.00 USD | 0.00 USD | 23,920.00 USD | `-38.00%` | `30,093.00` |
| `Live` | `Long` | `0.8050` | 71,310,000.00 USD | 0.00 USD | 27,910.00 USD | `-37.22%` | `34,674.00` |
| `Live` | `Long` | `0.8150` | 71,280,000.00 USD | 0.00 USD | 22,940.00 USD | `-36.44%` | `28,152.00` |
| `Live` | `Long` | `0.8250` | 71,260,000.00 USD | 0.00 USD | 13,120.00 USD | `-35.66%` | `15,905.00` |
| `Live` | `Long` | `0.8350` | 71,240,000.00 USD | 0.00 USD | 74,930.00 USD | `-34.88%` | `89,742.00` |
| `Live` | `Long` | `0.8450` | 71,170,000.00 USD | 0.00 USD | 58,890.00 USD | `-34.10%` | `69,688.00` |
| `Live` | `Long` | `0.8550` | 71,110,000.00 USD | 0.00 USD | 31,450.00 USD | `-33.32%` | `36,784.00` |
| `Live` | `Long` | `0.8650` | 71,080,000.00 USD | 0.00 USD | 516,010.00 USD | `-32.54%` | `596,538.00` |
| `Live` | `Long` | `0.8750` | 70,560,000.00 USD | 0.00 USD | 118,940.00 USD | `-31.76%` | `135,937.00` |
| `Live` | `Long` | `0.8850` | 70,440,000.00 USD | 0.00 USD | 428,590.00 USD | `-30.98%` | `484,277.00` |
| `Live` | `Long` | `0.8950` | 70,010,000.00 USD | 0.00 USD | 116,840.00 USD | `-30.20%` | `130,546.00` |
| `Live` | `Long` | `0.9050` | 69,900,000.00 USD | 0.00 USD | 118,560.00 USD | `-29.42%` | `131,002.00` |
| `Live` | `Long` | `0.9150` | 69,780,000.00 USD | 0.00 USD | 2,370,000.00 USD | `-28.64%` | `2,593,953.00` |
| `Live` | `Long` | `0.9250` | 67,410,000.00 USD | 0.00 USD | 76,920.00 USD | `-27.86%` | `83,155.00` |
| `Live` | `Long` | `0.9350` | 67,330,000.00 USD | 0.00 USD | 187,890.00 USD | `-27.08%` | `200,956.00` |
| `Live` | `Long` | `0.9450` | 67,140,000.00 USD | 0.00 USD | 268,870.00 USD | `-26.30%` | `284,522.00` |
| `Live` | `Long` | `0.9550` | 66,870,000.00 USD | 0.00 USD | 697,810.00 USD | `-25.52%` | `730,689.00` |
| `Live` | `Long` | `0.9650` | 66,170,000.00 USD | 0.00 USD | 33,920,000.00 USD | `-24.74%` | `35,153,532.00` |
| `Live` | `Long` | `0.9750` | 32,250,000.00 USD | 0.00 USD | 157,800.00 USD | `-23.96%` | `161,850.00` |
| `Live` | `Long` | `0.9850` | 32,090,000.00 USD | 0.00 USD | 450,020.00 USD | `-23.18%` | `456,870.00` |
| `Live` | `Long` | `0.9950` | 31,640,000.00 USD | 0.00 USD | 481,930.00 USD | `-22.40%` | `484,347.00` |
| `Live` | `Long` | `1.00` | 31,160,000.00 USD | 0.00 USD | 523,400.00 USD | `-21.62%` | `520,792.00` |
| `Live` | `Long` | `1.01` | 30,640,000.00 USD | 0.00 USD | 263,670.00 USD | `-20.84%` | `259,774.00` |
| `Live` | `Long` | `1.02` | 30,370,000.00 USD | 0.00 USD | 138,580.00 USD | `-20.06%` | `135,203.00` |
| `Live` | `Long` | `1.03` | 30,240,000.00 USD | 0.00 USD | 2,120,000.00 USD | `-19.28%` | `2,045,946.00` |
| `Live` | `Long` | `1.04` | 28,120,000.00 USD | 0.00 USD | 88,490.00 USD | `-18.50%` | `84,684.00` |
| `Live` | `Long` | `1.05` | 28,030,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-17.72%` | `1,021,357.00` |
| `Live` | `Long` | `1.06` | 26,950,000.00 USD | 0.00 USD | 401,440.00 USD | `-16.94%` | `376,943.00` |
| `Live` | `Long` | `1.07` | 26,550,000.00 USD | 0.00 USD | 459,350.00 USD | `-16.16%` | `427,300.00` |
| `Live` | `Long` | `1.08` | 26,090,000.00 USD | 0.00 USD | 784,410.00 USD | `-15.38%` | `722,954.00` |
| `Live` | `Long` | `1.09` | 25,310,000.00 USD | 0.00 USD | 99,690.00 USD | `-14.60%` | `91,042.00` |
| `Live` | `Long` | `1.10` | 25,210,000.00 USD | 0.00 USD | 59,350.00 USD | `-13.82%` | `53,706.00` |
| `Live` | `Long` | `1.11` | 25,150,000.00 USD | 0.00 USD | 592,630.00 USD | `-13.04%` | `531,506.00` |
| `Live` | `Long` | `1.12` | 24,560,000.00 USD | 0.00 USD | 276,220.00 USD | `-12.26%` | `245,528.00` |
| `Live` | `Long` | `1.14` | 24,280,000.00 USD | 0.00 USD | 76,470.00 USD | `-11.48%` | `67,372.00` |
| `Live` | `Long` | `1.15` | 24,200,000.00 USD | 0.00 USD | 614,970.00 USD | `-10.70%` | `537,095.00` |
| `Live` | `Long` | `1.16` | 23,590,000.00 USD | 0.00 USD | 119,460.00 USD | `-9.92%` | `103,428.00` |
| `Live` | `Long` | `1.17` | 23,470,000.00 USD | 0.00 USD | 1,600,000.00 USD | `-9.14%` | `1,375,427.00` |
| `Live` | `Long` | `1.18` | 21,870,000.00 USD | 0.00 USD | 274,810.00 USD | `-8.36%` | `233,878.00` |
| `Live` | `Long` | `1.19` | 21,590,000.00 USD | 0.00 USD | 2,220,000.00 USD | `-7.58%` | `1,874,152.00` |
| `Live` | `Long` | `1.20` | 19,370,000.00 USD | 0.00 USD | 671,140.00 USD | `-6.80%` | `561,627.00` |
| `Live` | `Long` | `1.21` | 18,700,000.00 USD | 0.00 USD | 644,280.00 USD | `-6.02%` | `534,673.00` |
| `Live` | `Long` | `1.22` | 18,050,000.00 USD | 0.00 USD | 369,930.00 USD | `-5.24%` | `304,470.00` |
| `Live` | `Long` | `1.23` | 17,690,000.00 USD | 0.00 USD | 1,560,000.00 USD | `-4.46%` | `1,273,262.00` |
| `Live` | `Long` | `1.24` | 16,130,000.00 USD | 0.00 USD | 570,730.00 USD | `-3.68%` | `462,127.00` |
| `Live` | `Long` | `1.25` | 15,550,000.00 USD | 0.00 USD | 242,000.00 USD | `-2.90%` | `194,380.00` |
| `Live` | `Long` | `1.25` | 15,310,000.00 USD | 0.00 USD | 830,060.00 USD | `-2.12%` | `661,400.00` |
| `Live` | `Long` | `1.26` | 14,480,000.00 USD | 0.00 USD | 14,310,000.00 USD | `-1.34%` | `11,314,602.00` |
| `Live` | `Long` | `1.27` | 169,550.00 USD | 0.00 USD | 169,550.00 USD | `-0.56%` | `132,978.00` |
| `Live` | `Short` | `1.29` | 3,590.00 USD | 3,590.00 USD | 0.00 USD | `+1.00%` | `2,770.00` |
| `Live` | `Short` | `1.30` | 4,490.00 USD | 900.45 USD | 0.00 USD | `+1.78%` | `690.00` |
| `Live` | `Short` | `1.31` | 91,290.00 USD | 86,800.00 USD | 0.00 USD | `+2.56%` | `66,008.00` |
| `Live` | `Short` | `1.32` | 145,760.00 USD | 54,470.00 USD | 0.00 USD | `+3.34%` | `41,110.00` |
| `Live` | `Short` | `1.33` | 198,160.00 USD | 52,400.00 USD | 0.00 USD | `+4.12%` | `39,254.00` |
| `Live` | `Short` | `1.34` | 359,680.00 USD | 161,520.00 USD | 0.00 USD | `+4.90%` | `120,086.00` |
| `Live` | `Short` | `1.35` | 364,050.00 USD | 4,370.00 USD | 0.00 USD | `+5.68%` | `3,224.00` |
| `Live` | `Short` | `1.36` | 562,510.00 USD | 198,460.00 USD | 0.00 USD | `+6.46%` | `145,394.00` |
| `Live` | `Short` | `1.38` | 562,970.00 USD | 464.75 USD | 0.00 USD | `+7.24%` | `338.00` |
| `Live` | `Short` | `1.39` | 599,920.00 USD | 36,950.00 USD | 0.00 USD | `+8.02%` | `26,678.00` |
| `Live` | `Short` | `1.40` | 776,940.00 USD | 177,010.00 USD | 0.00 USD | `+8.80%` | `126,891.00` |
| `Live` | `Short` | `1.41` | 778,050.00 USD | 1,110.00 USD | 0.00 USD | `+9.58%` | `793.00` |
| `Live` | `Short` | `1.42` | 781,910.00 USD | 3,860.00 USD | 0.00 USD | `+10.36%` | `2,727.00` |
| `Live` | `Short` | `1.43` | 876,310.00 USD | 94,400.00 USD | 0.00 USD | `+11.14%` | `66,249.00` |
| `Live` | `Short` | `1.44` | 909,100.00 USD | 32,780.00 USD | 0.00 USD | `+11.92%` | `22,845.00` |
| `Live` | `Short` | `1.45` | 1,500,000.00 USD | 588,370.00 USD | 0.00 USD | `+12.70%` | `407,175.00` |
| `Live` | `Short` | `1.46` | 1,500,000.00 USD | 3,360.00 USD | 0.00 USD | `+13.48%` | `2,310.00` |
| `Live` | `Short` | `1.47` | 1,540,000.00 USD | 41,640.00 USD | 0.00 USD | `+14.26%` | `28,425.00` |
| `Live` | `Short` | `1.48` | 1,550,000.00 USD | 10,700.00 USD | 0.00 USD | `+15.04%` | `7,254.00` |
| `Live` | `Short` | `1.49` | 1,590,000.00 USD | 40,610.00 USD | 0.00 USD | `+15.82%` | `27,347.00` |
| `Live` | `Short` | `1.50` | 1,610,000.00 USD | 11,950.00 USD | 0.00 USD | `+16.60%` | `7,994.00` |
| `Live` | `Short` | `1.50` | 1,610,000.00 USD | 734.44 USD | 0.00 USD | `+17.38%` | `488.00` |
| `Live` | `Short` | `1.51` | 1,610,000.00 USD | 6,630.00 USD | 0.00 USD | `+18.16%` | `4,373.00` |
| `Live` | `Short` | `1.52` | 1,610,000.00 USD | 234.85 USD | 0.00 USD | `+18.94%` | `154.00` |
| `Live` | `Short` | `1.53` | 1,610,000.00 USD | 1,010.00 USD | 0.00 USD | `+19.72%` | `658.00` |
| `Live` | `Short` | `1.54` | 1,620,000.00 USD | 1,370.00 USD | 0.00 USD | `+20.50%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,620,000.00 USD | 1,360.00 USD | 0.00 USD | `+21.28%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,620,000.00 USD | 555.57 USD | 0.00 USD | `+22.06%` | `355.00` |
| `Live` | `Short` | `1.57` | 1,620,000.00 USD | 2,840.00 USD | 0.00 USD | `+22.84%` | `1,800.00` |
| `Live` | `Short` | `1.58` | 6,880,000.00 USD | 5,260,000.00 USD | 0.00 USD | `+23.62%` | `3,320,020.00` |
| `Live` | `Short` | `1.61` | 6,880,000.00 USD | 599.17 USD | 0.00 USD | `+25.96%` | `371.00` |
| `Live` | `Short` | `1.62` | 6,890,000.00 USD | 3,350.00 USD | 0.00 USD | `+26.74%` | `2,063.00` |
| `Live` | `Short` | `1.64` | 6,900,000.00 USD | 11,270.00 USD | 0.00 USD | `+27.52%` | `6,892.00` |
| `Live` | `Short` | `1.66` | 11,900,000.00 USD | 5,010,000.00 USD | 0.00 USD | `+29.08%` | `3,025,200.00` |
| `Live` | `Short` | `1.67` | 12,040,000.00 USD | 135,930.00 USD | 0.00 USD | `+29.85%` | `81,640.00` |
| `Live` | `Short` | `1.68` | 12,040,000.00 USD | 760.45 USD | 0.00 USD | `+30.63%` | `454.00` |
| `Live` | `Short` | `1.69` | 12,060,000.00 USD | 18,860.00 USD | 0.00 USD | `+31.41%` | `11,195.00` |
| `Live` | `Short` | `1.70` | 12,060,000.00 USD | 242.38 USD | 0.00 USD | `+32.19%` | `143.00` |
| `Live` | `Short` | `1.71` | 12,060,000.00 USD | 1,980.00 USD | 0.00 USD | `+32.97%` | `1,163.00` |
| `Live` | `Short` | `1.73` | 12,060,000.00 USD | 1,690.00 USD | 0.00 USD | `+34.53%` | `977.00` |
| `Live` | `Short` | `1.74` | 12,080,000.00 USD | 15,070.00 USD | 0.00 USD | `+35.31%` | `8,683.00` |
| `Live` | `Short` | `1.75` | 12,080,000.00 USD | 2,960.00 USD | 0.00 USD | `+36.09%` | `1,699.00` |
| `Live` | `Short` | `1.75` | 12,080,000.00 USD | 149.17 USD | 0.00 USD | `+36.87%` | `85.00` |
| `Live` | `Short` | `1.76` | 12,080,000.00 USD | 808.37 USD | 0.00 USD | `+37.65%` | `458.00` |
| `Live` | `Short` | `1.78` | 12,210,000.00 USD | 129,540.00 USD | 0.00 USD | `+39.21%` | `72,574.00` |
| `Live` | `Short` | `1.79` | 12,220,000.00 USD | 4,010.00 USD | 0.00 USD | `+39.99%` | `2,232.00` |
| `Live` | `Short` | `1.80` | 12,220,000.00 USD | 889.87 USD | 0.00 USD | `+40.77%` | `493.00` |
| `Live` | `Short` | `1.81` | 12,220,000.00 USD | 838.53 USD | 0.00 USD | `+41.55%` | `462.00` |
| `Live` | `Short` | `1.82` | 12,220,000.00 USD | 406.98 USD | 0.00 USD | `+42.33%` | `223.00` |
| `Live` | `Short` | `1.83` | 15,280,000.00 USD | 3,060,000.00 USD | 0.00 USD | `+43.11%` | `1,666,029.00` |
| `Live` | `Short` | `1.84` | 15,280,000.00 USD | 6,300.00 USD | 0.00 USD | `+43.89%` | `3,415.00` |
| `Live` | `Short` | `1.85` | 15,280,000.00 USD | 732.73 USD | 0.00 USD | `+44.67%` | `395.00` |
| `Live` | `Short` | `1.86` | 15,290,000.00 USD | 2,340.00 USD | 0.00 USD | `+45.45%` | `1,255.00` |
| `Live` | `Short` | `1.88` | 15,290,000.00 USD | 219.38 USD | 0.00 USD | `+46.23%` | `117.00` |
| `Live` | `Short` | `1.89` | 15,300,000.00 USD | 13,850.00 USD | 0.00 USD | `+47.01%` | `7,347.00` |
| `Live` | `Short` | `1.90` | 15,310,000.00 USD | 5,760.00 USD | 0.00 USD | `+47.79%` | `3,039.00` |
| `Live` | `Short` | `1.91` | 15,320,000.00 USD | 9,900.00 USD | 0.00 USD | `+48.57%` | `5,196.00` |
| `Live` | `Short` | `1.94` | 15,430,000.00 USD | 113,600.00 USD | 0.00 USD | `+50.91%` | `58,706.00` |
| `Live` | `Short` | `1.96` | 15,430,000.00 USD | 293.25 USD | 0.00 USD | `+52.47%` | `150.00` |
| `Live` | `Short` | `1.97` | 16,050,000.00 USD | 620,680.00 USD | 0.00 USD | `+53.25%` | `315,869.00` |
| `Live` | `Short` | `1.98` | 16,050,000.00 USD | 1,760.00 USD | 0.00 USD | `+54.03%` | `891.00` |
| `Live` | `Short` | `1.99` | 16,370,000.00 USD | 318,940.00 USD | 0.00 USD | `+54.81%` | `160,677.00` |
| `Live` | `Short` | `2.00` | 16,370,000.00 USD | 401.00 USD | 0.00 USD | `+56.37%` | `200.00` |
| `Live` | `Short` | `2.02` | 16,370,000.00 USD | 971.23 USD | 0.00 USD | `+57.15%` | `482.00` |
| `Live` | `Short` | `2.04` | 16,370,000.00 USD | 1,810.00 USD | 0.00 USD | `+59.49%` | `886.00` |
| `Live` | `Short` | `2.06` | 16,610,000.00 USD | 241,070.00 USD | 0.00 USD | `+60.27%` | `117,308.00` |
| `Live` | `Short` | `2.06` | 16,620,000.00 USD | 5,330.00 USD | 0.00 USD | `+61.05%` | `2,583.00` |
| `Live` | `Short` | `2.08` | 16,660,000.00 USD | 40,840.00 USD | 0.00 USD | `+62.61%` | `19,588.00` |
| `Live` | `Short` | `2.10` | 16,660,000.00 USD | 331.01 USD | 0.00 USD | `+63.39%` | `158.00` |
| `Live` | `Short` | `2.10` | 16,660,000.00 USD | 294.70 USD | 0.00 USD | `+64.17%` | `140.00` |
| `Live` | `Short` | `2.12` | 16,660,000.00 USD | 3,100.00 USD | 0.00 USD | `+64.95%` | `1,468.00` |
| `Live` | `Short` | `2.12` | 19,910,000.00 USD | 3,250,000.00 USD | 0.00 USD | `+65.73%` | `1,529,461.00` |
| `Live` | `Short` | `2.13` | 20,090,000.00 USD | 173,550.00 USD | 0.00 USD | `+66.51%` | `81,287.00` |
| `Live` | `Short` | `2.15` | 20,090,000.00 USD | 515.05 USD | 0.00 USD | `+68.07%` | `239.00` |
| `Live` | `Short` | `2.17` | 20,090,000.00 USD | 2,730.00 USD | 0.00 USD | `+69.63%` | `1,253.00` |
| `Live` | `Short` | `2.19` | 20,090,000.00 USD | 703.57 USD | 0.00 USD | `+70.41%` | `322.00` |
| `Live` | `Short` | `2.19` | 20,090,000.00 USD | 2,820.00 USD | 0.00 USD | `+71.19%` | `1,286.00` |
| `Live` | `Short` | `2.21` | 20,100,000.00 USD | 8,920.00 USD | 0.00 USD | `+71.97%` | `4,046.00` |
| `Live` | `Short` | `2.23` | 22,420,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+73.53%` | `1,041,436.00` |
| `Live` | `Short` | `2.23` | 22,420,000.00 USD | 1,350.00 USD | 0.00 USD | `+74.31%` | `604.00` |
| `Live` | `Short` | `2.25` | 22,430,000.00 USD | 4,010.00 USD | 0.00 USD | `+75.09%` | `1,784.00` |
| `Live` | `Short` | `2.25` | 22,440,000.00 USD | 12,490.00 USD | 0.00 USD | `+75.87%` | `5,539.00` |
| `Live` | `Short` | `2.27` | 22,490,000.00 USD | 51,650.00 USD | 0.00 USD | `+76.65%` | `22,804.00` |
| `Live` | `Short` | `2.27` | 22,510,000.00 USD | 14,930.00 USD | 0.00 USD | `+77.43%` | `6,561.00` |
| `Live` | `Short` | `2.29` | 22,570,000.00 USD | 67,070.00 USD | 0.00 USD | `+78.99%` | `29,225.00` |
| `Live` | `Short` | `2.31` | 22,580,000.00 USD | 5,770.00 USD | 0.00 USD | `+79.77%` | `2,502.00` |
| `Live` | `Short` | `2.31` | 22,660,000.00 USD | 77,580.00 USD | 0.00 USD | `+80.55%` | `33,513.00` |
| `Live` | `Short` | `2.33` | 22,660,000.00 USD | 2,670.00 USD | 0.00 USD | `+81.33%` | `1,147.00` |
| `Live` | `Short` | `2.33` | 22,750,000.00 USD | 90,600.00 USD | 0.00 USD | `+82.11%` | `38,799.00` |
| `Live` | `Short` | `2.35` | 22,760,000.00 USD | 11,870.00 USD | 0.00 USD | `+82.89%` | `5,062.00` |
| `Live` | `Short` | `2.38` | 23,710,000.00 USD | 950,110.00 USD | 0.00 USD | `+85.23%` | `400,046.00` |
| `Live` | `Short` | `2.38` | 23,710,000.00 USD | 257.58 USD | 0.00 USD | `+86.01%` | `108.00` |
| `Live` | `Short` | `2.40` | 23,890,000.00 USD | 181,260.00 USD | 0.00 USD | `+87.57%` | `75,369.00` |
| `Live` | `Short` | `2.42` | 23,990,000.00 USD | 92,830.00 USD | 0.00 USD | `+88.35%` | `38,440.00` |
| `Live` | `Short` | `2.42` | 23,990,000.00 USD | 2,590.00 USD | 0.00 USD | `+89.13%` | `1,070.00` |
| `Live` | `Short` | `2.44` | 23,990,000.00 USD | 1,120.00 USD | 0.00 USD | `+89.91%` | `459.00` |
| `Live` | `Short` | `2.44` | 24,010,000.00 USD | 24,720.00 USD | 0.00 USD | `+90.69%` | `10,111.00` |
| `Live` | `Short` | `2.46` | 24,010,000.00 USD | 311.79 USD | 0.00 USD | `+91.47%` | `127.00` |
| `Live` | `Short` | `2.46` | 24,020,000.00 USD | 4,190.00 USD | 0.00 USD | `+92.25%` | `1,698.00` |
| `Live` | `Short` | `2.48` | 24,030,000.00 USD | 14,040.00 USD | 0.00 USD | `+93.81%` | `5,648.00` |
| `Live` | `Short` | `2.50` | 24,040,000.00 USD | 4,730.00 USD | 0.00 USD | `+95.37%` | `1,888.00` |
| `Live` | `Short` | `2.52` | 24,040,000.00 USD | 5,970.00 USD | 0.00 USD | `+96.15%` | `2,374.00` |
| `Live` | `Short` | `2.52` | 24,090,000.00 USD | 42,710.00 USD | 0.00 USD | `+96.93%` | `16,914.00` |
| `Live` | `Short` | `2.54` | 24,090,000.00 USD | 496.86 USD | 0.00 USD | `+97.71%` | `196.00` |
| `Live` | `Short` | `2.54` | 24,090,000.00 USD | 117.07 USD | 0.00 USD | `+98.49%` | `46.00` |
| `Live` | `Short` | `2.56` | 24,100,000.00 USD | 11,280.00 USD | 0.00 USD | `+99.27%` | `4,414.00` |
| `Live` | `Short` | `2.56` | 24,100,000.00 USD | 187.25 USD | 0.00 USD | `+100.05%` | `73.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 3,270,000.00 USD | 0.00 USD | 112.45 USD | `-80.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3050` | 3,270,000.00 USD | 0.00 USD | 147.62 USD | `-76.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 3,270,000.00 USD | 0.00 USD | 139.12 USD | `-70.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 3,270,000.00 USD | 0.00 USD | 200.86 USD | `-67.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 3,270,000.00 USD | 0.00 USD | 408.51 USD | `-65.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 3,270,000.00 USD | 0.00 USD | 520.52 USD | `-64.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 3,270,000.00 USD | 0.00 USD | 151.12 USD | `-63.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 3,270,000.00 USD | 0.00 USD | 190.00 USD | `-62.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 3,270,000.00 USD | 0.00 USD | 145.50 USD | `-62.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 3,270,000.00 USD | 0.00 USD | 1,030.00 USD | `-60.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 3,270,000.00 USD | 0.00 USD | 306.60 USD | `-59.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 3,270,000.00 USD | 0.00 USD | 6,750.00 USD | `-56.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 3,260,000.00 USD | 0.00 USD | 374.60 USD | `-55.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 3,260,000.00 USD | 0.00 USD | 100.62 USD | `-54.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 3,260,000.00 USD | 0.00 USD | 791.85 USD | `-50.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 3,260,000.00 USD | 0.00 USD | 573.40 USD | `-49.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 3,260,000.00 USD | 0.00 USD | 3,450.00 USD | `-48.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 3,260,000.00 USD | 0.00 USD | 3,010.00 USD | `-48.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 3,260,000.00 USD | 0.00 USD | 1,060.00 USD | `-45.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 3,260,000.00 USD | 0.00 USD | 1,590.00 USD | `-45.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 3,250,000.00 USD | 0.00 USD | 1,300.00 USD | `-41.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 3,250,000.00 USD | 0.00 USD | 2,880.00 USD | `-40.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 3,250,000.00 USD | 0.00 USD | 1,110.00 USD | `-38.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 3,250,000.00 USD | 0.00 USD | 798.57 USD | `-33.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 3,250,000.00 USD | 0.00 USD | 690.38 USD | `-31.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 3,250,000.00 USD | 0.00 USD | 1,420.00 USD | `-30.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 3,250,000.00 USD | 0.00 USD | 3,230.00 USD | `-30.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 3,240,000.00 USD | 0.00 USD | 838.94 USD | `-29.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 3,240,000.00 USD | 0.00 USD | 188.49 USD | `-28.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 3,240,000.00 USD | 0.00 USD | 2,730.00 USD | `-27.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 3,240,000.00 USD | 0.00 USD | 1,150.00 USD | `-27.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 3,240,000.00 USD | 0.00 USD | 112.46 USD | `-26.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 3,240,000.00 USD | 0.00 USD | 2,360.00 USD | `-25.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 3,230,000.00 USD | 0.00 USD | 3,910.00 USD | `-24.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 3,230,000.00 USD | 0.00 USD | 546,370.00 USD | `-23.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 2,680,000.00 USD | 0.00 USD | 5,250.00 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 2,680,000.00 USD | 0.00 USD | 897.49 USD | `-22.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 2,680,000.00 USD | 0.00 USD | 15,070.00 USD | `-21.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 2,660,000.00 USD | 0.00 USD | 4,330.00 USD | `-20.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 2,660,000.00 USD | 0.00 USD | 2,020.00 USD | `-20.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 2,660,000.00 USD | 0.00 USD | 38,000.00 USD | `-19.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 2,620,000.00 USD | 0.00 USD | 2,280.00 USD | `-18.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 2,620,000.00 USD | 0.00 USD | 7,090.00 USD | `-17.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 2,610,000.00 USD | 0.00 USD | 3,230.00 USD | `-16.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 2,610,000.00 USD | 0.00 USD | 34,770.00 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 2,570,000.00 USD | 0.00 USD | 973.25 USD | `-15.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 2,570,000.00 USD | 0.00 USD | 8,000.00 USD | `-14.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 2,560,000.00 USD | 0.00 USD | 2,970.00 USD | `-13.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 2,560,000.00 USD | 0.00 USD | 9,300.00 USD | `-13.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 2,550,000.00 USD | 0.00 USD | 79,110.00 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 2,470,000.00 USD | 0.00 USD | 12,910.00 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 2,460,000.00 USD | 0.00 USD | 16,630.00 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 2,440,000.00 USD | 0.00 USD | 31,630.00 USD | `-9.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 2,410,000.00 USD | 0.00 USD | 14,080.00 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 2,400,000.00 USD | 0.00 USD | 4,790.00 USD | `-8.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 2,390,000.00 USD | 0.00 USD | 90,010.00 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 2,300,000.00 USD | 0.00 USD | 12,570.00 USD | `-6.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 2,290,000.00 USD | 0.00 USD | 52,130.00 USD | `-6.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 2,240,000.00 USD | 0.00 USD | 57,160.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 2,180,000.00 USD | 0.00 USD | 146,570.00 USD | `-4.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 2,030,000.00 USD | 0.00 USD | 381,390.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 1,650,000.00 USD | 0.00 USD | 338,320.00 USD | `-2.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 1,310,000.00 USD | 0.00 USD | 684,480.00 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.26` | 628,350.00 USD | 0.00 USD | 137,880.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.27` | 490,470.00 USD | 0.00 USD | 490,470.00 USD | `-0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 2,280.00 USD | 2,280.00 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 167,680.00 USD | 165,400.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 261,700.00 USD | 94,020.00 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 473,630.00 USD | 211,930.00 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 718,280.00 USD | 244,650.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 815,950.00 USD | 97,670.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 992,180.00 USD | 176,230.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,020,000.00 USD | 27,390.00 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,300,000.00 USD | 281,080.00 USD | 0.00 USD | `+6.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,370,000.00 USD | 73,500.00 USD | 0.00 USD | `+7.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,450,000.00 USD | 73,380.00 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,520,000.00 USD | 71,640.00 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 5,860,000.00 USD | 4,340,000.00 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 5,890,000.00 USD | 30,880.00 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 5,910,000.00 USD | 19,640.00 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,000,000.00 USD | 82,400.00 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,190,000.00 USD | 193,480.00 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,230,000.00 USD | 43,500.00 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,260,000.00 USD | 27,080.00 USD | 0.00 USD | `+14.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,370,000.00 USD | 108,480.00 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,450,000.00 USD | 78,610.00 USD | 0.00 USD | `+15.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,460,000.00 USD | 14,970.00 USD | 0.00 USD | `+16.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,580,000.00 USD | 115,020.00 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,600,000.00 USD | 18,210.00 USD | 0.00 USD | `+18.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,700,000.00 USD | 103,290.00 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,760,000.00 USD | 57,450.00 USD | 0.00 USD | `+19.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,790,000.00 USD | 37,230.00 USD | 0.00 USD | `+20.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,800,000.00 USD | 6,110.00 USD | 0.00 USD | `+21.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,810,000.00 USD | 6,300.00 USD | 0.00 USD | `+22.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,810,000.00 USD | 6,080.00 USD | 0.00 USD | `+22.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,820,000.00 USD | 9,700.00 USD | 0.00 USD | `+23.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,960,000.00 USD | 141,350.00 USD | 0.00 USD | `+24.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,970,000.00 USD | 2,730.00 USD | 0.00 USD | `+25.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 7,050,000.00 USD | 81,600.00 USD | 0.00 USD | `+25.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 7,050,000.00 USD | 464.75 USD | 0.00 USD | `+26.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,250,000.00 USD | 199,230.00 USD | 0.00 USD | `+27.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,250,000.00 USD | 3,370.00 USD | 0.00 USD | `+28.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,280,000.00 USD | 33,550.00 USD | 0.00 USD | `+29.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,290,000.00 USD | 6,720.00 USD | 0.00 USD | `+29.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,310,000.00 USD | 18,770.00 USD | 0.00 USD | `+30.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,380,000.00 USD | 70,850.00 USD | 0.00 USD | `+31.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,390,000.00 USD | 8,570.00 USD | 0.00 USD | `+32.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,650,000.00 USD | 259,410.00 USD | 0.00 USD | `+32.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,660,000.00 USD | 14,030.00 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,680,000.00 USD | 14,560.00 USD | 0.00 USD | `+34.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,720,000.00 USD | 44,100.00 USD | 0.00 USD | `+35.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,730,000.00 USD | 4,710.00 USD | 0.00 USD | `+36.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,730,000.00 USD | 6,330.00 USD | 0.00 USD | `+36.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,750,000.00 USD | 21,720.00 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,880,000.00 USD | 122,650.00 USD | 0.00 USD | `+38.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,970,000.00 USD | 96,900.00 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 8,010,000.00 USD | 40,420.00 USD | 0.00 USD | `+39.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 8,010,000.00 USD | 254.51 USD | 0.00 USD | `+40.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 8,020,000.00 USD | 2,530.00 USD | 0.00 USD | `+41.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 8,020,000.00 USD | 1,830.00 USD | 0.00 USD | `+42.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 8,030,000.00 USD | 7,630.00 USD | 0.00 USD | `+43.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 8,030,000.00 USD | 1,900.00 USD | 0.00 USD | `+43.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 8,040,000.00 USD | 8,390.00 USD | 0.00 USD | `+44.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 8,040,000.00 USD | 4,550.00 USD | 0.00 USD | `+46.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 8,040,000.00 USD | 591.89 USD | 0.00 USD | `+47.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 8,090,000.00 USD | 44,350.00 USD | 0.00 USD | `+47.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 8,130,000.00 USD | 39,680.00 USD | 0.00 USD | `+48.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 8,130,000.00 USD | 7,410.00 USD | 0.00 USD | `+49.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 8,130,000.00 USD | 265.10 USD | 0.00 USD | `+50.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 8,140,000.00 USD | 2,040.00 USD | 0.00 USD | `+51.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 8,140,000.00 USD | 1,510.00 USD | 0.00 USD | `+52.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,150,000.00 USD | 14,120.00 USD | 0.00 USD | `+53.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,150,000.00 USD | 4,010.00 USD | 0.00 USD | `+54.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,160,000.00 USD | 325.54 USD | 0.00 USD | `+54.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,160,000.00 USD | 7,020.00 USD | 0.00 USD | `+55.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,300,000.00 USD | 138,900.00 USD | 0.00 USD | `+56.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,300,000.00 USD | 781.82 USD | 0.00 USD | `+57.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,300,000.00 USD | 222.75 USD | 0.00 USD | `+57.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,300,000.00 USD | 862.84 USD | 0.00 USD | `+58.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,310,000.00 USD | 3,490.00 USD | 0.00 USD | `+59.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,310,000.00 USD | 3,940.00 USD | 0.00 USD | `+61.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,310,000.00 USD | 661.93 USD | 0.00 USD | `+61.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,440,000.00 USD | 124,400.00 USD | 0.00 USD | `+63.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,440,000.00 USD | 1,580.00 USD | 0.00 USD | `+64.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,450,000.00 USD | 13,900.00 USD | 0.00 USD | `+65.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,480,000.00 USD | 24,840.00 USD | 0.00 USD | `+67.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,530,000.00 USD | 50,580.00 USD | 0.00 USD | `+68.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,530,000.00 USD | 1,710.00 USD | 0.00 USD | `+68.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,530,000.00 USD | 1,970.00 USD | 0.00 USD | `+71.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,680,000.00 USD | 151,380.00 USD | 0.00 USD | `+72.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 8,690,000.00 USD | 7,340.00 USD | 0.00 USD | `+74.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,690,000.00 USD | 3,120.00 USD | 0.00 USD | `+77.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,690,000.00 USD | 1,140.00 USD | 0.00 USD | `+78.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,710,000.00 USD | 12,150.00 USD | 0.00 USD | `+78.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,710,000.00 USD | 370.40 USD | 0.00 USD | `+80.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,710,000.00 USD | 733.19 USD | 0.00 USD | `+82.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,710,000.00 USD | 2,410.00 USD | 0.00 USD | `+84.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,710,000.00 USD | 475.00 USD | 0.00 USD | `+85.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,710,000.00 USD | 2,540.00 USD | 0.00 USD | `+86.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,960,000.00 USD | 251,200.00 USD | 0.00 USD | `+87.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,960,000.00 USD | 1,370.00 USD | 0.00 USD | `+88.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,960,000.00 USD | 564.92 USD | 0.00 USD | `+89.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,970,000.00 USD | 8,110.00 USD | 0.00 USD | `+91.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,980,000.00 USD | 3,420.00 USD | 0.00 USD | `+93.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,980,000.00 USD | 124.75 USD | 0.00 USD | `+94.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 9,020,000.00 USD | 42,600.00 USD | 0.00 USD | `+95.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.52` | 9,020,000.00 USD | 378.75 USD | 0.00 USD | `+96.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.56` | 9,020,000.00 USD | 389.88 USD | 0.00 USD | `+100.05%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.13` | 93,280,000.00 USD | 0.00 USD | 93,280,000.00 USD | 5,450.00 USD | 2,160.00 USD | 3,970.00 USD |
| `7D` | `1.13` | 93,260,000.00 USD | 0.00 USD | 93,260,000.00 USD | 144,660.00 USD | 0.00 USD | 142,970.00 USD |
| `1D` | `1.13` | 28,870,000.00 USD | 0.00 USD | 28,870,000.00 USD | 7,260.00 USD | 0.00 USD | 3,090.00 USD |
| `7D` | `1.14` | 92,980,000.00 USD | 0.00 USD | 92,980,000.00 USD | 0.00 USD | 43,440.00 USD | 150,130.00 USD |
| `1D` | `1.14` | 28,860,000.00 USD | 0.00 USD | 28,860,000.00 USD | 40,370.00 USD | 605.15 USD | 0.00 USD |
| `7D` | `1.14` | 92,780,000.00 USD | 0.00 USD | 92,780,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD |
| `7D` | `1.14` | 92,680,000.00 USD | 0.00 USD | 92,680,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 28,820,000.00 USD | 0.00 USD | 28,820,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD |
| `7D` | `1.14` | 92,670,000.00 USD | 0.00 USD | 92,670,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 28,750,000.00 USD | 0.00 USD | 28,750,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.14` | 92,610,000.00 USD | 0.00 USD | 92,610,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.14` | 28,680,000.00 USD | 0.00 USD | 28,680,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD |
| `7D` | `1.15` | 92,490,000.00 USD | 0.00 USD | 92,490,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.15` | 92,480,000.00 USD | 0.00 USD | 92,480,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `1D` | `1.15` | 28,550,000.00 USD | 0.00 USD | 28,550,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 92,350,000.00 USD | 0.00 USD | 92,350,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD |
| `7D` | `1.15` | 91,990,000.00 USD | 0.00 USD | 91,990,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.15` | 28,530,000.00 USD | 0.00 USD | 28,530,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.15` | 91,820,000.00 USD | 0.00 USD | 91,820,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `1D` | `1.15` | 28,460,000.00 USD | 0.00 USD | 28,460,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD |
| `7D` | `1.16` | 91,440,000.00 USD | 0.00 USD | 91,440,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `1D` | `1.16` | 28,090,000.00 USD | 0.00 USD | 28,090,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD |
| `7D` | `1.16` | 90,790,000.00 USD | 0.00 USD | 90,790,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD |
| `1D` | `1.16` | 27,960,000.00 USD | 0.00 USD | 27,960,000.00 USD | 66,460.00 USD | 27,380.00 USD | 78,320.00 USD |
| `7D` | `1.16` | 90,000,000.00 USD | 0.00 USD | 90,000,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `1D` | `1.16` | 27,790,000.00 USD | 0.00 USD | 27,790,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.16` | 89,470,000.00 USD | 0.00 USD | 89,470,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.16` | 27,410,000.00 USD | 0.00 USD | 27,410,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.16` | 88,450,000.00 USD | 0.00 USD | 88,450,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.16` | 26,670,000.00 USD | 0.00 USD | 26,670,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.17` | 87,070,000.00 USD | 0.00 USD | 87,070,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.17` | 26,240,000.00 USD | 0.00 USD | 26,240,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD |
| `7D` | `1.17` | 86,450,000.00 USD | 0.00 USD | 86,450,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD |
| `1D` | `1.17` | 25,910,000.00 USD | 0.00 USD | 25,910,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.17` | 85,070,000.00 USD | 0.00 USD | 85,070,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 25,730,000.00 USD | 0.00 USD | 25,730,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.17` | 83,560,000.00 USD | 0.00 USD | 83,560,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 25,570,000.00 USD | 0.00 USD | 25,570,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.17` | 82,170,000.00 USD | 0.00 USD | 82,170,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.17` | 25,350,000.00 USD | 0.00 USD | 25,350,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.18` | 81,370,000.00 USD | 0.00 USD | 81,370,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD |
| `1D` | `1.18` | 25,070,000.00 USD | 0.00 USD | 25,070,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD |
| `7D` | `1.18` | 80,490,000.00 USD | 0.00 USD | 80,490,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `1D` | `1.18` | 24,850,000.00 USD | 0.00 USD | 24,850,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.18` | 80,040,000.00 USD | 0.00 USD | 80,040,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `1D` | `1.18` | 24,680,000.00 USD | 0.00 USD | 24,680,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.18` | 79,320,000.00 USD | 0.00 USD | 79,320,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `1D` | `1.18` | 24,590,000.00 USD | 0.00 USD | 24,590,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.18` | 78,950,000.00 USD | 0.00 USD | 78,950,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `1D` | `1.18` | 24,510,000.00 USD | 0.00 USD | 24,510,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD |
| `7D` | `1.19` | 78,820,000.00 USD | 0.00 USD | 78,820,000.00 USD | 78,020.00 USD | 97,270.00 USD | 289,750.00 USD |
| `1D` | `1.19` | 24,400,000.00 USD | 0.00 USD | 24,400,000.00 USD | 694.57 USD | 23,390.00 USD | 20,370.00 USD |
| `7D` | `1.19` | 78,350,000.00 USD | 0.00 USD | 78,350,000.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD |
| `1D` | `1.19` | 24,350,000.00 USD | 0.00 USD | 24,350,000.00 USD | 30,140.00 USD | 99.63 USD | 12,880.00 USD |
| `7D` | `1.19` | 77,740,000.00 USD | 0.00 USD | 77,740,000.00 USD | 186,430.00 USD | 128,180.00 USD | 346,850.00 USD |
| `1D` | `1.19` | 24,310,000.00 USD | 0.00 USD | 24,310,000.00 USD | 10,800.00 USD | 238.88 USD | 21,580.00 USD |
| `7D` | `1.19` | 77,080,000.00 USD | 0.00 USD | 77,080,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `1D` | `1.19` | 24,280,000.00 USD | 0.00 USD | 24,280,000.00 USD | 20,520.00 USD | 17,640.00 USD | 56,850.00 USD |
| `7D` | `1.19` | 76,620,000.00 USD | 0.00 USD | 76,620,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD |
| `1D` | `1.19` | 24,180,000.00 USD | 0.00 USD | 24,180,000.00 USD | 98,310.00 USD | 31,420.00 USD | 82,720.00 USD |
| `7D` | `1.20` | 75,960,000.00 USD | 0.00 USD | 75,960,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 23,970,000.00 USD | 0.00 USD | 23,970,000.00 USD | 40,880.00 USD | 18,340.00 USD | 29,820.00 USD |
| `7D` | `1.20` | 75,250,000.00 USD | 0.00 USD | 75,250,000.00 USD | 5,350.00 USD | 93,870.00 USD | 187,830.00 USD |
| `1D` | `1.20` | 23,880,000.00 USD | 0.00 USD | 23,880,000.00 USD | 107,530.00 USD | 7,010.00 USD | 9,050.00 USD |
| `7D` | `1.20` | 74,960,000.00 USD | 0.00 USD | 74,960,000.00 USD | 67,200.00 USD | 57,670.00 USD | 21,970.00 USD |
| `1D` | `1.20` | 23,760,000.00 USD | 0.00 USD | 23,760,000.00 USD | 0.00 USD | 14,280.00 USD | 0.00 USD |
| `7D` | `1.20` | 74,810,000.00 USD | 0.00 USD | 74,810,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD |
| `7D` | `1.20` | 74,740,000.00 USD | 0.00 USD | 74,740,000.00 USD | 202,570.00 USD | 53,170.00 USD | 48,290.00 USD |
| `7D` | `1.21` | 74,430,000.00 USD | 0.00 USD | 74,430,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD |
| `7D` | `1.21` | 74,340,000.00 USD | 0.00 USD | 74,340,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD |
| `7D` | `1.21` | 74,240,000.00 USD | 0.00 USD | 74,240,000.00 USD | 361,660.00 USD | 45,260.00 USD | 357,420.00 USD |
| `1D` | `1.21` | 23,740,000.00 USD | 0.00 USD | 23,740,000.00 USD | 18,160.00 USD | 0.00 USD | 61,640.00 USD |
| `7D` | `1.21` | 73,480,000.00 USD | 0.00 USD | 73,480,000.00 USD | 179,800.00 USD | 152,900.00 USD | 457,650.00 USD |
| `1D` | `1.21` | 23,660,000.00 USD | 0.00 USD | 23,660,000.00 USD | 100,930.00 USD | 31,390.00 USD | 0.00 USD |
| `7D` | `1.21` | 72,690,000.00 USD | 0.00 USD | 72,690,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD |
| `1D` | `1.21` | 23,530,000.00 USD | 0.00 USD | 23,530,000.00 USD | 9,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.22` | 72,280,000.00 USD | 0.00 USD | 72,280,000.00 USD | 5,680.00 USD | 39,860.00 USD | 0.00 USD |
| `1D` | `1.22` | 23,520,000.00 USD | 0.00 USD | 23,520,000.00 USD | 77,860.00 USD | 0.00 USD | 78,080.00 USD |
| `7D` | `1.22` | 72,240,000.00 USD | 0.00 USD | 72,240,000.00 USD | 157,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.22` | 23,370,000.00 USD | 0.00 USD | 23,370,000.00 USD | 174,270.00 USD | 1,870.00 USD | 108,420.00 USD |
| `7D` | `1.22` | 72,080,000.00 USD | 0.00 USD | 72,080,000.00 USD | 256,390.00 USD | 4,120.00 USD | 40,620.00 USD |
| `1D` | `1.22` | 23,080,000.00 USD | 0.00 USD | 23,080,000.00 USD | 157,550.00 USD | 2,660.00 USD | 208,620.00 USD |
| `7D` | `1.22` | 71,780,000.00 USD | 0.00 USD | 71,780,000.00 USD | 159,150.00 USD | 2,490.00 USD | 328,940.00 USD |
| `1D` | `1.22` | 22,710,000.00 USD | 0.00 USD | 22,710,000.00 USD | 0.00 USD | 211.25 USD | 47,550.00 USD |
| `7D` | `1.22` | 71,290,000.00 USD | 0.00 USD | 71,290,000.00 USD | 10,460.00 USD | 191,360.00 USD | 207,400.00 USD |
| `1D` | `1.22` | 22,660,000.00 USD | 0.00 USD | 22,660,000.00 USD | 40,080.00 USD | 206.80 USD | 0.00 USD |
| `7D` | `1.23` | 70,880,000.00 USD | 0.00 USD | 70,880,000.00 USD | 649,620.00 USD | 191,250.00 USD | 200,510.00 USD |
| `7D` | `1.23` | 69,840,000.00 USD | 0.00 USD | 69,840,000.00 USD | 341,300.00 USD | 128,580.00 USD | 60,930.00 USD |
| `1D` | `1.23` | 22,620,000.00 USD | 0.00 USD | 22,620,000.00 USD | 48,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.23` | 69,310,000.00 USD | 0.00 USD | 69,310,000.00 USD | 44,790.00 USD | 125,700.00 USD | 371,190.00 USD |
| `1D` | `1.23` | 22,580,000.00 USD | 0.00 USD | 22,580,000.00 USD | 203,290.00 USD | 28,070.00 USD | 518,460.00 USD |
| `7D` | `1.23` | 68,770,000.00 USD | 0.00 USD | 68,770,000.00 USD | 876,350.00 USD | 482,760.00 USD | 1,550,000.00 USD |
| `1D` | `1.23` | 21,830,000.00 USD | 0.00 USD | 21,830,000.00 USD | 295,580.00 USD | 131,700.00 USD | 492,180.00 USD |
| `7D` | `1.23` | 65,860,000.00 USD | 0.00 USD | 65,860,000.00 USD | 750,810.00 USD | 142,840.00 USD | 467,410.00 USD |
| `1D` | `1.23` | 20,910,000.00 USD | 0.00 USD | 20,910,000.00 USD | 134,050.00 USD | 1,800.00 USD | 88,900.00 USD |
| `7D` | `1.24` | 64,500,000.00 USD | 0.00 USD | 64,500,000.00 USD | 1,150,000.00 USD | 525,690.00 USD | 2,440,000.00 USD |
| `1D` | `1.24` | 20,680,000.00 USD | 0.00 USD | 20,680,000.00 USD | 517,670.00 USD | 120,320.00 USD | 662,640.00 USD |
| `7D` | `1.24` | 60,380,000.00 USD | 0.00 USD | 60,380,000.00 USD | 1,830,000.00 USD | 912,620.00 USD | 2,100,000.00 USD |
| `1D` | `1.24` | 19,380,000.00 USD | 0.00 USD | 19,380,000.00 USD | 1,290,000.00 USD | 729,150.00 USD | 709,340.00 USD |
| `7D` | `1.24` | 55,530,000.00 USD | 0.00 USD | 55,530,000.00 USD | 1,940,000.00 USD | 975,570.00 USD | 2,280,000.00 USD |
| `1D` | `1.24` | 16,660,000.00 USD | 0.00 USD | 16,660,000.00 USD | 961,180.00 USD | 493,310.00 USD | 740,300.00 USD |
| `7D` | `1.24` | 50,330,000.00 USD | 0.00 USD | 50,330,000.00 USD | 1,980,000.00 USD | 677,720.00 USD | 2,560,000.00 USD |
| `1D` | `1.24` | 14,460,000.00 USD | 0.00 USD | 14,460,000.00 USD | 503,460.00 USD | 188,510.00 USD | 497,840.00 USD |
| `7D` | `1.24` | 45,100,000.00 USD | 0.00 USD | 45,100,000.00 USD | 1,100,000.00 USD | 740,000.00 USD | 1,100,000.00 USD |
| `1D` | `1.24` | 13,270,000.00 USD | 0.00 USD | 13,270,000.00 USD | 721,110.00 USD | 126,130.00 USD | 733,450.00 USD |
| `7D` | `1.25` | 42,160,000.00 USD | 0.00 USD | 42,160,000.00 USD | 2,670,000.00 USD | 383,660.00 USD | 1,810,000.00 USD |
| `1D` | `1.25` | 11,690,000.00 USD | 0.00 USD | 11,690,000.00 USD | 861,120.00 USD | 135,040.00 USD | 578,850.00 USD |
| `7D` | `1.25` | 37,300,000.00 USD | 0.00 USD | 37,300,000.00 USD | 2,330,000.00 USD | 1,190,000.00 USD | 5,930,000.00 USD |
| `1D` | `1.25` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 218,430.00 USD | 101,820.00 USD | 665,800.00 USD |
| `7D` | `1.25` | 27,840,000.00 USD | 0.00 USD | 27,840,000.00 USD | 2,710,000.00 USD | 1,370,000.00 USD | 3,470,000.00 USD |
| `1D` | `1.25` | 9,130,000.00 USD | 0.00 USD | 9,130,000.00 USD | 661,270.00 USD | 222,520.00 USD | 457,850.00 USD |
| `7D` | `1.25` | 20,280,000.00 USD | 0.00 USD | 20,280,000.00 USD | 2,810,000.00 USD | 918,840.00 USD | 2,000,000.00 USD |
| `1D` | `1.25` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 351,630.00 USD | 92,050.00 USD | 426,530.00 USD |
| `7D` | `1.25` | 14,550,000.00 USD | 0.00 USD | 14,550,000.00 USD | 1,240,000.00 USD | 673,830.00 USD | 1,480,000.00 USD |
| `1D` | `1.25` | 6,920,000.00 USD | 0.00 USD | 6,920,000.00 USD | 520,500.00 USD | 43,020.00 USD | 944,650.00 USD |
| `7D` | `1.25` | 11,160,000.00 USD | 0.00 USD | 11,160,000.00 USD | 998,540.00 USD | 468,670.00 USD | 1,420,000.00 USD |
| `1D` | `1.26` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 1,460,000.00 USD | 258,360.00 USD | 1,920,000.00 USD |
| `7D` | `1.26` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 2,180,000.00 USD | 992,480.00 USD | 1,970,000.00 USD |
| `1D` | `1.26` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,030,000.00 USD | 212,550.00 USD | 0.00 USD |
| `7D` | `1.26` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 0.00 USD | 436,080.00 USD | 2,690,000.00 USD |
| `1D` | `1.26` | 524,270.00 USD | 0.00 USD | 524,270.00 USD | 356,060.00 USD | 1,680.00 USD | 0.00 USD |
| `7D` | `1.26` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.26` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 1,110,000.00 USD | 1,200,000.00 USD |
| `1D` | `1.26` | 166,530.00 USD | 0.00 USD | 166,530.00 USD | 105,880.00 USD | 0.00 USD | 60,650.00 USD |
| `1D` | `1.26` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.26` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 1,690,000.00 USD | 1,910,000.00 USD |
| `1D` | `1.26` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 9,320.00 USD | 1,530,000.00 USD |
| `7D` | `1.26` | 13,620,000.00 USD | 13,620,000.00 USD | 0.00 USD | 1,600,000.00 USD | 1,780,000.00 USD | 4,330,000.00 USD |
| `1D` | `1.27` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 1,030,000.00 USD | 38,360.00 USD |
| `7D` | `1.27` | 24,140,000.00 USD | 24,140,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,600,000.00 USD | 6,300,000.00 USD |
| `1D` | `1.27` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 483,650.00 USD | 0.00 USD |
| `7D` | `1.27` | 28,910,000.00 USD | 28,910,000.00 USD | 0.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD |
| `1D` | `1.27` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 776,250.00 USD | 0.00 USD |
| `7D` | `1.27` | 30,820,000.00 USD | 30,820,000.00 USD | 0.00 USD | 178,380.00 USD | 1,610,000.00 USD | 123,930.00 USD |
| `1D` | `1.27` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 961,090.00 USD | 313,930.00 USD | 61,350.00 USD |
| `7D` | `1.27` | 34,220,000.00 USD | 34,220,000.00 USD | 0.00 USD | 186,960.00 USD | 3,000,000.00 USD | 207,690.00 USD |
| `1D` | `1.27` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 63,920.00 USD | 507,900.00 USD | 1,520,000.00 USD |
| `7D` | `1.27` | 48,150,000.00 USD | 48,150,000.00 USD | 0.00 USD | 4,420,000.00 USD | 1,300,000.00 USD | 8,210,000.00 USD |
| `1D` | `1.28` | 12,120,000.00 USD | 12,120,000.00 USD | 0.00 USD | 505,430.00 USD | 1,400,000.00 USD | 2,920,000.00 USD |
| `7D` | `1.28` | 66,420,000.00 USD | 66,420,000.00 USD | 0.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 25,540,000.00 USD | 25,540,000.00 USD | 0.00 USD | 6,170,000.00 USD | 2,740,000.00 USD | 4,520,000.00 USD |
| `7D` | `1.28` | 71,550,000.00 USD | 71,550,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,750,000.00 USD | 120,110.00 USD |
| `1D` | `1.28` | 27,490,000.00 USD | 27,490,000.00 USD | 0.00 USD | 188,330.00 USD | 1,450,000.00 USD | 312,320.00 USD |
| `7D` | `1.28` | 72,500,000.00 USD | 72,500,000.00 USD | 0.00 USD | 0.00 USD | 869,610.00 USD | 79,220.00 USD |
| `1D` | `1.28` | 28,440,000.00 USD | 28,440,000.00 USD | 0.00 USD | 547,110.00 USD | 0.00 USD | 405,670.00 USD |
| `7D` | `1.28` | 73,590,000.00 USD | 73,590,000.00 USD | 0.00 USD | 1,030,000.00 USD | 16,490.00 USD | 45,690.00 USD |
| `1D` | `1.28` | 30,070,000.00 USD | 30,070,000.00 USD | 0.00 USD | 615,090.00 USD | 161,530.00 USD | 849,910.00 USD |
| `7D` | `1.28` | 76,500,000.00 USD | 76,500,000.00 USD | 0.00 USD | 639,910.00 USD | 895,200.00 USD | 1,370,000.00 USD |
| `1D` | `1.29` | 30,840,000.00 USD | 30,840,000.00 USD | 0.00 USD | 143,950.00 USD | 327,360.00 USD | 298,050.00 USD |
| `7D` | `1.29` | 77,440,000.00 USD | 77,440,000.00 USD | 0.00 USD | 943,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.29` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 584,100.00 USD | 163,240.00 USD | 8,840.00 USD |
| `7D` | `1.29` | 77,530,000.00 USD | 77,530,000.00 USD | 0.00 USD | 48,320.00 USD | 2,730.00 USD | 33,260.00 USD |
| `1D` | `1.29` | 31,610,000.00 USD | 31,610,000.00 USD | 0.00 USD | 18,290.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.29` | 79,380,000.00 USD | 79,380,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 819,130.00 USD |
| `1D` | `1.29` | 33,340,000.00 USD | 33,340,000.00 USD | 0.00 USD | 349,940.00 USD | 0.00 USD | 1,380,000.00 USD |
| `7D` | `1.29` | 79,800,000.00 USD | 79,800,000.00 USD | 0.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD |
| `1D` | `1.29` | 37,100,000.00 USD | 37,100,000.00 USD | 0.00 USD | 1,110,000.00 USD | 113,790.00 USD | 2,530,000.00 USD |
| `7D` | `1.29` | 89,440,000.00 USD | 89,440,000.00 USD | 0.00 USD | 3,350,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD |
| `1D` | `1.30` | 42,000,000.00 USD | 42,000,000.00 USD | 0.00 USD | 1,400,000.00 USD | 1,120,000.00 USD | 2,380,000.00 USD |
| `7D` | `1.30` | 90,660,000.00 USD | 90,660,000.00 USD | 0.00 USD | 209,360.00 USD | 389,370.00 USD | 628,450.00 USD |
| `1D` | `1.30` | 42,730,000.00 USD | 42,730,000.00 USD | 0.00 USD | 344,680.00 USD | 422.50 USD | 383,310.00 USD |
| `7D` | `1.30` | 91,910,000.00 USD | 91,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `1.30` | 43,410,000.00 USD | 43,410,000.00 USD | 0.00 USD | 0.00 USD | 168,250.00 USD | 510,770.00 USD |
| `7D` | `1.30` | 93,160,000.00 USD | 93,160,000.00 USD | 0.00 USD | 0.00 USD | 286,660.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 45,580,000.00 USD | 45,580,000.00 USD | 0.00 USD | 602,010.00 USD | 910,970.00 USD | 659,740.00 USD |
| `7D` | `1.30` | 95,680,000.00 USD | 95,680,000.00 USD | 0.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD |
| `1D` | `1.30` | 46,000,000.00 USD | 46,000,000.00 USD | 0.00 USD | 188,510.00 USD | 98,100.00 USD | 127,330.00 USD |
| `1D` | `1.31` | 47,120,000.00 USD | 47,120,000.00 USD | 0.00 USD | 493,480.00 USD | 313,760.00 USD | 320,170.00 USD |
| `7D` | `1.31` | 98,680,000.00 USD | 98,680,000.00 USD | 0.00 USD | 2,140,000.00 USD | 178,660.00 USD | 684,370.00 USD |
| `1D` | `1.31` | 49,640,000.00 USD | 49,640,000.00 USD | 0.00 USD | 767,340.00 USD | 211,190.00 USD | 1,530,000.00 USD |
| `7D` | `1.31` | 102,470,000.00 USD | 102,470,000.00 USD | 0.00 USD | 1,480,000.00 USD | 590,530.00 USD | 1,710,000.00 USD |
| `1D` | `1.31` | 52,210,000.00 USD | 52,210,000.00 USD | 0.00 USD | 908,870.00 USD | 396,100.00 USD | 1,270,000.00 USD |
| `7D` | `1.31` | 105,590,000.00 USD | 105,590,000.00 USD | 0.00 USD | 838,890.00 USD | 318,670.00 USD | 1,970,000.00 USD |
| `1D` | `1.31` | 55,180,000.00 USD | 55,180,000.00 USD | 0.00 USD | 1,800,000.00 USD | 475,550.00 USD | 688,860.00 USD |
| `7D` | `1.31` | 108,440,000.00 USD | 108,440,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD |
| `1D` | `1.31` | 56,890,000.00 USD | 56,890,000.00 USD | 0.00 USD | 464,990.00 USD | 483,320.00 USD | 767,230.00 USD |
| `7D` | `1.31` | 110,900,000.00 USD | 110,900,000.00 USD | 0.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 62,870,000.00 USD | 62,870,000.00 USD | 0.00 USD | 222,150.00 USD | 1,830,000.00 USD | 3,920,000.00 USD |
| `7D` | `1.32` | 115,520,000.00 USD | 115,520,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 69,900,000.00 USD | 69,900,000.00 USD | 0.00 USD | 2,310,000.00 USD | 1,060,000.00 USD | 3,670,000.00 USD |
| `7D` | `1.32` | 118,600,000.00 USD | 118,600,000.00 USD | 0.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 73,290,000.00 USD | 73,290,000.00 USD | 0.00 USD | 1,680,000.00 USD | 689,260.00 USD | 1,030,000.00 USD |
| `7D` | `1.32` | 120,430,000.00 USD | 120,430,000.00 USD | 0.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD |
| `1D` | `1.32` | 77,930,000.00 USD | 77,930,000.00 USD | 0.00 USD | 1,870,000.00 USD | 845,300.00 USD | 1,920,000.00 USD |
| `7D` | `1.32` | 124,890,000.00 USD | 124,890,000.00 USD | 0.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD |
| `1D` | `1.32` | 80,980,000.00 USD | 80,980,000.00 USD | 0.00 USD | 1,770,000.00 USD | 259,620.00 USD | 1,020,000.00 USD |
| `7D` | `1.32` | 127,260,000.00 USD | 127,260,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 83,270,000.00 USD | 83,270,000.00 USD | 0.00 USD | 687,000.00 USD | 308,840.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 127,790,000.00 USD | 127,790,000.00 USD | 0.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 85,460,000.00 USD | 85,460,000.00 USD | 0.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD |
| `7D` | `1.33` | 128,950,000.00 USD | 128,950,000.00 USD | 0.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 87,900,000.00 USD | 87,900,000.00 USD | 0.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 130,670,000.00 USD | 130,670,000.00 USD | 0.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 90,160,000.00 USD | 90,160,000.00 USD | 0.00 USD | 465,720.00 USD | 276,750.00 USD | 1,520,000.00 USD |
| `7D` | `1.33` | 134,720,000.00 USD | 134,720,000.00 USD | 0.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD |
| `1D` | `1.33` | 92,490,000.00 USD | 92,490,000.00 USD | 0.00 USD | 1,120,000.00 USD | 226,040.00 USD | 985,030.00 USD |
| `7D` | `1.33` | 135,260,000.00 USD | 135,260,000.00 USD | 0.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 94,930,000.00 USD | 94,930,000.00 USD | 0.00 USD | 928,470.00 USD | 334,030.00 USD | 1,180,000.00 USD |
| `7D` | `1.34` | 137,210,000.00 USD | 137,210,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD |
| `1D` | `1.34` | 97,610,000.00 USD | 97,610,000.00 USD | 0.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,050,000.00 USD |
| `7D` | `1.34` | 139,560,000.00 USD | 139,560,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD |
| `1D` | `1.34` | 100,570,000.00 USD | 100,570,000.00 USD | 0.00 USD | 1,350,000.00 USD | 389,350.00 USD | 1,230,000.00 USD |
| `7D` | `1.34` | 144,260,000.00 USD | 144,260,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD |
| `1D` | `1.34` | 104,280,000.00 USD | 104,280,000.00 USD | 0.00 USD | 1,630,000.00 USD | 878,740.00 USD | 1,200,000.00 USD |
| `7D` | `1.34` | 149,950,000.00 USD | 149,950,000.00 USD | 0.00 USD | 1,730,000.00 USD | 2,810,000.00 USD | 1,140,000.00 USD |
| `1D` | `1.34` | 108,300,000.00 USD | 108,300,000.00 USD | 0.00 USD | 2,140,000.00 USD | 696,110.00 USD | 1,170,000.00 USD |
| `7D` | `1.34` | 161,010,000.00 USD | 161,010,000.00 USD | 0.00 USD | 3,700,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD |
| `1D` | `1.35` | 109,610,000.00 USD | 109,610,000.00 USD | 0.00 USD | 498,430.00 USD | 331,800.00 USD | 481,220.00 USD |
| `7D` | `1.35` | 168,750,000.00 USD | 168,750,000.00 USD | 0.00 USD | 2,550,000.00 USD | 2,230,000.00 USD | 2,960,000.00 USD |
| `1D` | `1.35` | 110,870,000.00 USD | 110,870,000.00 USD | 0.00 USD | 481,670.00 USD | 124,160.00 USD | 655,290.00 USD |
| `7D` | `1.35` | 179,180,000.00 USD | 179,180,000.00 USD | 0.00 USD | 4,410,000.00 USD | 1,700,000.00 USD | 4,320,000.00 USD |
| `1D` | `1.35` | 112,360,000.00 USD | 112,360,000.00 USD | 0.00 USD | 771,840.00 USD | 230,360.00 USD | 488,180.00 USD |
| `7D` | `1.35` | 186,950,000.00 USD | 186,950,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 113,690,000.00 USD | 113,690,000.00 USD | 0.00 USD | 558,120.00 USD | 208,670.00 USD | 565,330.00 USD |
| `7D` | `1.35` | 195,270,000.00 USD | 195,270,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD |
| `1D` | `1.35` | 115,340,000.00 USD | 115,340,000.00 USD | 0.00 USD | 672,330.00 USD | 219,470.00 USD | 753,540.00 USD |
| `7D` | `1.35` | 203,510,000.00 USD | 203,510,000.00 USD | 0.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD |
| `1D` | `1.36` | 116,710,000.00 USD | 116,710,000.00 USD | 0.00 USD | 558,510.00 USD | 199,730.00 USD | 611,840.00 USD |
| `7D` | `1.36` | 207,580,000.00 USD | 207,580,000.00 USD | 0.00 USD | 1,320,000.00 USD | 879,500.00 USD | 1,870,000.00 USD |
| `1D` | `1.36` | 117,930,000.00 USD | 117,930,000.00 USD | 0.00 USD | 732,680.00 USD | 76,930.00 USD | 416,300.00 USD |
| `7D` | `1.36` | 211,360,000.00 USD | 211,360,000.00 USD | 0.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.36` | 118,430,000.00 USD | 118,430,000.00 USD | 0.00 USD | 266,880.00 USD | 118,570.00 USD | 116,960.00 USD |
| `7D` | `1.36` | 213,500,000.00 USD | 213,500,000.00 USD | 0.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD |
| `1D` | `1.36` | 119,080,000.00 USD | 119,080,000.00 USD | 0.00 USD | 222,740.00 USD | 103,400.00 USD | 317,870.00 USD |
| `7D` | `1.36` | 217,580,000.00 USD | 217,580,000.00 USD | 0.00 USD | 2,100,000.00 USD | 752,200.00 USD | 1,240,000.00 USD |
| `1D` | `1.36` | 119,220,000.00 USD | 119,220,000.00 USD | 0.00 USD | 80,160.00 USD | 26,460.00 USD | 31,150.00 USD |
| `7D` | `1.36` | 219,220,000.00 USD | 219,220,000.00 USD | 0.00 USD | 660,170.00 USD | 270,780.00 USD | 707,350.00 USD |
| `1D` | `1.37` | 119,390,000.00 USD | 119,390,000.00 USD | 0.00 USD | 53,740.00 USD | 0.00 USD | 124,610.00 USD |
| `7D` | `1.37` | 219,710,000.00 USD | 219,710,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD |
| `1D` | `1.37` | 119,580,000.00 USD | 119,580,000.00 USD | 0.00 USD | 84,710.00 USD | 57,700.00 USD | 44,320.00 USD |
| `7D` | `1.37` | 221,140,000.00 USD | 221,140,000.00 USD | 0.00 USD | 538,230.00 USD | 136,720.00 USD | 753,550.00 USD |
| `1D` | `1.37` | 119,760,000.00 USD | 119,760,000.00 USD | 0.00 USD | 38,340.00 USD | 25,940.00 USD | 110,310.00 USD |
| `7D` | `1.37` | 222,380,000.00 USD | 222,380,000.00 USD | 0.00 USD | 403,920.00 USD | 370,870.00 USD | 464,810.00 USD |
| `1D` | `1.37` | 119,890,000.00 USD | 119,890,000.00 USD | 0.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD |
| `7D` | `1.37` | 225,220,000.00 USD | 225,220,000.00 USD | 0.00 USD | 931,390.00 USD | 404,120.00 USD | 1,510,000.00 USD |
| `1D` | `1.37` | 120,040,000.00 USD | 120,040,000.00 USD | 0.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD |
| `7D` | `1.38` | 226,880,000.00 USD | 226,880,000.00 USD | 0.00 USD | 594,550.00 USD | 294,500.00 USD | 769,660.00 USD |
| `1D` | `1.38` | 120,290,000.00 USD | 120,290,000.00 USD | 0.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD |
| `7D` | `1.38` | 228,500,000.00 USD | 228,500,000.00 USD | 0.00 USD | 676,760.00 USD | 389,310.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 120,800,000.00 USD | 120,800,000.00 USD | 0.00 USD | 231,710.00 USD | 71,960.00 USD | 199,430.00 USD |
| `7D` | `1.38` | 230,430,000.00 USD | 230,430,000.00 USD | 0.00 USD | 579,450.00 USD | 290,350.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 121,250,000.00 USD | 121,250,000.00 USD | 0.00 USD | 247,460.00 USD | 58,430.00 USD | 147,850.00 USD |
| `7D` | `1.38` | 232,980,000.00 USD | 232,980,000.00 USD | 0.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 121,500,000.00 USD | 121,500,000.00 USD | 0.00 USD | 103,440.00 USD | 53,840.00 USD | 92,660.00 USD |
| `7D` | `1.38` | 234,070,000.00 USD | 234,070,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.38` | 121,870,000.00 USD | 121,870,000.00 USD | 0.00 USD | 300,730.00 USD | 17,520.00 USD | 52,070.00 USD |
| `7D` | `1.39` | 235,160,000.00 USD | 235,160,000.00 USD | 0.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 121,920,000.00 USD | 121,920,000.00 USD | 0.00 USD | 7,260.00 USD | 35,700.00 USD | 3,090.00 USD |
| `7D` | `1.39` | 235,660,000.00 USD | 235,660,000.00 USD | 0.00 USD | 86,820.00 USD | 203,870.00 USD | 200,360.00 USD |
| `1D` | `1.39` | 121,960,000.00 USD | 121,960,000.00 USD | 0.00 USD | 40,370.00 USD | 605.15 USD | 0.00 USD |
| `7D` | `1.39` | 236,750,000.00 USD | 236,750,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD |
| `7D` | `1.39` | 236,920,000.00 USD | 236,920,000.00 USD | 0.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD |
| `1D` | `1.39` | 121,960,000.00 USD | 121,960,000.00 USD | 0.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.39` | 237,250,000.00 USD | 237,250,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.39` | 122,020,000.00 USD | 122,020,000.00 USD | 0.00 USD | 31,140.00 USD | 0.00 USD | 31,230.00 USD |
| `7D` | `1.40` | 237,420,000.00 USD | 237,420,000.00 USD | 0.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 122,090,000.00 USD | 122,090,000.00 USD | 0.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.40` | 237,540,000.00 USD | 237,540,000.00 USD | 0.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.40` | 122,230,000.00 USD | 122,230,000.00 USD | 0.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD |
| `7D` | `1.40` | 237,540,000.00 USD | 237,540,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 237,680,000.00 USD | 237,680,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 237,800,000.00 USD | 237,800,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `1D` | `1.40` | 122,240,000.00 USD | 122,240,000.00 USD | 0.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.41` | 238,040,000.00 USD | 238,040,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 238,210,000.00 USD | 238,210,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.41` | 122,310,000.00 USD | 122,310,000.00 USD | 0.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.41` | 238,590,000.00 USD | 238,590,000.00 USD | 0.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `1D` | `1.41` | 122,690,000.00 USD | 122,690,000.00 USD | 0.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD |
| `7D` | `1.41` | 239,230,000.00 USD | 239,230,000.00 USD | 0.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `1D` | `1.41` | 122,810,000.00 USD | 122,810,000.00 USD | 0.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD |
| `7D` | `1.41` | 239,410,000.00 USD | 239,410,000.00 USD | 0.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD |
| `1D` | `1.41` | 122,820,000.00 USD | 122,820,000.00 USD | 0.00 USD | 4,630.00 USD | 336.57 USD | 204.46 USD |
| `7D` | `1.42` | 240,030,000.00 USD | 240,030,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD |
| `1D` | `1.42` | 122,990,000.00 USD | 122,990,000.00 USD | 0.00 USD | 61,830.00 USD | 27,040.00 USD | 78,120.00 USD |
| `7D` | `1.42` | 240,560,000.00 USD | 240,560,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `1D` | `1.42` | 123,370,000.00 USD | 123,370,000.00 USD | 0.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.42` | 241,580,000.00 USD | 241,580,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.42` | 124,100,000.00 USD | 124,100,000.00 USD | 0.00 USD | 381,490.00 USD | 156,970.00 USD | 198,200.00 USD |
| `1D` | `1.42` | 124,400,000.00 USD | 124,400,000.00 USD | 0.00 USD | 98,200.00 USD | 87,070.00 USD | 107,210.00 USD |
| `7D` | `1.42` | 242,960,000.00 USD | 242,960,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `7D` | `1.42` | 243,580,000.00 USD | 243,580,000.00 USD | 0.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `7D` | `1.43` | 243,940,000.00 USD | 243,940,000.00 USD | 0.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD |
| `7D` | `1.43` | 244,960,000.00 USD | 244,960,000.00 USD | 0.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD |
| `7D` | `1.43` | 246,470,000.00 USD | 246,470,000.00 USD | 0.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `7D` | `1.43` | 247,860,000.00 USD | 247,860,000.00 USD | 0.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `7D` | `1.43` | 248,660,000.00 USD | 248,660,000.00 USD | 0.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `7D` | `1.44` | 249,190,000.00 USD | 249,190,000.00 USD | 0.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD |
| `7D` | `1.44` | 249,540,000.00 USD | 249,540,000.00 USD | 0.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD |
| `7D` | `1.44` | 249,990,000.00 USD | 249,990,000.00 USD | 0.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `7D` | `1.44` | 250,710,000.00 USD | 250,710,000.00 USD | 0.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `7D` | `1.44` | 251,080,000.00 USD | 251,080,000.00 USD | 0.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `7D` | `1.45` | 251,210,000.00 USD | 251,210,000.00 USD | 0.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `7D` | `1.45` | 251,340,000.00 USD | 251,340,000.00 USD | 0.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD |
| `7D` | `1.45` | 251,680,000.00 USD | 251,680,000.00 USD | 0.00 USD | 70,540.00 USD | 96,050.00 USD | 173,340.00 USD |
| `7D` | `1.45` | 252,290,000.00 USD | 252,290,000.00 USD | 0.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD |
| `7D` | `1.45` | 252,950,000.00 USD | 252,950,000.00 USD | 0.00 USD | 186,430.00 USD | 128,180.00 USD | 346,850.00 USD |
| `7D` | `1.46` | 253,400,000.00 USD | 253,400,000.00 USD | 0.00 USD | 125,020.00 USD | 67,850.00 USD | 260,640.00 USD |
| `7D` | `1.46` | 253,520,000.00 USD | 253,520,000.00 USD | 0.00 USD | 65,340.00 USD | 49,190.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.94B` | Total OI Tokens: `2,329,480,347.0 XRP`
  * 1h OI Change: `-2.66%` | 4h OI Change: `-2.52%` | 24h OI Change: `-1.10%`
  * Exchange Breakdown: Binance=`487.16M` | Bybit=`325.87M` | OKX=`96.51M` | Hyperliquid=`220.76M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `29.70K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0049%` | **USDT OKX** | `0.0085%` |
| **USDT Bybit** | `0.0002%` | **USDT KuCoin** | `0.0077%` |
| **USDT MEXC** | `0.0048%` | **USDT BingX** | `0.0088%` |
| **USDT Gate** | `0.0003%` | **USDT Bitget** | `0.0027%` |
| **CoinM Binance** | `0.0080%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `38.03%` | `61.97%` | `0.61` | 93,950,000.00 USD |
| `15M` | `Binance` | `40.68%` | `59.32%` | `0.69` | 32,770,000.00 USD |
| `15M` | `OKX` | `40.92%` | `59.08%` | `0.69` | 11,110,000.00 USD |
| `15M` | `Bybit` | `37.72%` | `62.28%` | `0.61` | 13,330,000.00 USD |
| `15M` | `KuCoin` | `44.79%` | `55.21%` | `0.81` | 1,740,000.00 USD |
| `15M` | `Gate` | `46.63%` | `53.37%` | `0.87` | 2,700,000.00 USD |
| `15M` | `Bitget` | `41.46%` | `58.54%` | `0.71` | 7,040,000.00 USD |
| `15M` | `BingX` | `41.98%` | `58.02%` | `0.72` | 1,490,000.00 USD |
| `15M` | `MEXC` | `38.12%` | `61.88%` | `0.62` | 7,290,000.00 USD |
| `15M` | `Bitunix` | `36.66%` | `63.34%` | `0.58` | 4,280,000.00 USD |
| `15M` | `Hyperliquid` | `9.31%` | `90.69%` | `0.10` | 8,680,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.68%` | `48.32%` | `1.07` | 682,460.00 USD |
| `15M` | `Crypto.com` | `54.95%` | `45.05%` | `1.22` | 167,250.00 USD |
| `15M` | `WhiteBIT` | `98.45%` | `1.55%` | `63.52` | 1,050,000.00 USD |
| `15M` | `HTX` | `44.28%` | `55.72%` | `0.79` | 24,460.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `40.28%` | `59.72%` | `0.67` | 619,250.00 USD |
| `15M` | `Aster` | `36.25%` | `63.75%` | `0.57` | 885,060.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `36.41%` | `63.59%` | `0.57` | 101,920.00 USD |
| `15M` | `Whale Positions` | `40.68%` | `59.32%` | `0.69` | 32,770,000.00 USD |
| `15M` | `Global Accounts` | `38.03%` | `61.97%` | `0.61` | 93,950,000.00 USD |
| `1H` | `XRP` | `39.77%` | `60.23%` | `0.66` | 263,850,000.00 USD |
| `1H` | `Binance` | `40.45%` | `59.55%` | `0.68` | 91,870,000.00 USD |
| `1H` | `OKX` | `36.64%` | `63.36%` | `0.58` | 32,960,000.00 USD |
| `1H` | `Bybit` | `38.79%` | `61.21%` | `0.63` | 34,230,000.00 USD |
| `1H` | `KuCoin` | `46.36%` | `53.64%` | `0.86` | 4,340,000.00 USD |
| `1H` | `Gate` | `41.18%` | `58.82%` | `0.70` | 9,470,000.00 USD |
| `1H` | `Bitget` | `38.55%` | `61.45%` | `0.63` | 19,900,000.00 USD |
| `1H` | `BingX` | `41.33%` | `58.67%` | `0.70` | 4,230,000.00 USD |
| `1H` | `MEXC` | `39.59%` | `60.41%` | `0.66` | 27,070,000.00 USD |
| `1H` | `Bitunix` | `39.22%` | `60.78%` | `0.65` | 13,740,000.00 USD |
| `1H` | `Hyperliquid` | `19.86%` | `80.14%` | `0.25` | 13,200,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `44.47%` | `55.53%` | `0.80` | 1,510,000.00 USD |
| `1H` | `Crypto.com` | `50.64%` | `49.36%` | `1.03` | 466,520.00 USD |
| `1H` | `WhiteBIT` | `98.29%` | `1.71%` | `57.48` | 5,800,000.00 USD |
| `1H` | `HTX` | `38.14%` | `61.86%` | `0.62` | 154,690.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `23.61%` | `76.39%` | `0.31` | 1,560,000.00 USD |
| `1H` | `Aster` | `38.49%` | `61.51%` | `0.63` | 3,020,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.12%` | `53.88%` | `0.86` | 344,000.00 USD |
| `1H` | `Whale Positions` | `40.45%` | `59.55%` | `0.68` | 91,870,000.00 USD |
| `1H` | `Global Accounts` | `39.77%` | `60.23%` | `0.66` | 263,850,000.00 USD |
| `4H` | `XRP` | `43.53%` | `56.47%` | `0.77` | 638,530,000.00 USD |
| `4H` | `Binance` | `43.6%` | `56.4%` | `0.77` | 213,430,000.00 USD |
| `4H` | `OKX` | `43.63%` | `56.37%` | `0.77` | 71,040,000.00 USD |
| `4H` | `Bybit` | `40.83%` | `59.17%` | `0.69` | 85,680,000.00 USD |
| `4H` | `KuCoin` | `45.77%` | `54.23%` | `0.84` | 7,580,000.00 USD |
| `4H` | `Gate` | `45.47%` | `54.53%` | `0.83` | 27,790,000.00 USD |
| `4H` | `Bitget` | `41.86%` | `58.14%` | `0.72` | 45,540,000.00 USD |
| `4H` | `BingX` | `30.82%` | `69.18%` | `0.45` | 16,640,000.00 USD |
| `4H` | `MEXC` | `46.46%` | `53.54%` | `0.87` | 70,990,000.00 USD |
| `4H` | `Bitunix` | `45.52%` | `54.48%` | `0.84` | 37,540,000.00 USD |
| `4H` | `Hyperliquid` | `24.94%` | `75.06%` | `0.33` | 19,390,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.91%` | `47.09%` | `1.12` | 3,270,000.00 USD |
| `4H` | `Crypto.com` | `52.09%` | `47.91%` | `1.09` | 1,010,000.00 USD |
| `4H` | `WhiteBIT` | `62.01%` | `37.99%` | `1.63` | 25,460,000.00 USD |
| `4H` | `HTX` | `60.13%` | `39.87%` | `1.51` | 538,300.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.68%` | `53.32%` | `0.88` | 3,960,000.00 USD |
| `4H` | `Aster` | `39.87%` | `60.13%` | `0.66` | 7,930,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.65%` | `55.35%` | `0.81` | 748,520.00 USD |
| `4H` | `Whale Positions` | `43.6%` | `56.4%` | `0.77` | 213,430,000.00 USD |
| `4H` | `Global Accounts` | `43.53%` | `56.47%` | `0.77` | 638,530,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 4,397,440.00 USD | 1,948,835.02 USD | 2,448,604.98 USD | -499,769.95 USD | `-11.37%` | `7B / 14S` |
| `0:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 30,348,241.89 USD | 10,177,546.51 USD | 20,170,695.38 USD | -9,993,148.87 USD | `-32.93%` | `4B / 38S` |
| `5:00 UTC` | `1.29` | `1.28` | `1.29` | `1.29` | `1.28` | 10,140,362.32 USD | 5,667,315.95 USD | 4,473,046.37 USD | 1,194,269.58 USD | `+11.78%` | `17B / 12S` |
| `0:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 5,885,752.93 USD | 2,814,674.62 USD | 3,071,078.30 USD | -256,403.68 USD | `-4.36%` | `5B / 13S` |
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 5,036,330.68 USD | 2,484,228.37 USD | 2,552,102.32 USD | -67,873.95 USD | `-1.35%` | `8B / 7S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.28` | 3,779,916.77 USD | 1,963,240.26 USD | 1,816,676.51 USD | 146,563.75 USD | `+3.88%` | `6B / 5S` |
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 7,767,016.10 USD | 3,262,612.53 USD | 4,504,403.57 USD | -1,241,791.04 USD | `-15.99%` | `7B / 12S` |
| `0:00 UTC` | `1.27` | `1.27` | `1.27` | `1.28` | `1.26` | 41,778,066.41 USD | 16,233,527.16 USD | 25,544,539.25 USD | -9,311,012.09 USD | `-22.29%` | `4B / 58S` |
| `5:00 UTC` | `1.27` | `1.27` | `1.27` | `1.27` | `1.27` | 9,197,225.16 USD | 4,639,147.41 USD | 4,558,077.75 USD | 81,069.66 USD | `+0.88%` | `4B / 5S` |
| `0:00 UTC` | `1.27` | `1.27` | `1.27` | `1.27` | `1.27` | 795,460.41 USD | 436,331.33 USD | 359,129.08 USD | 77,202.25 USD | `+9.71%` | `3B / 2S` |

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
| `5m` | -5,430,000.00 USD | 509,280.00 USD | **`DISTRIBUTION`** |
| `15m` | -5,310,000.00 USD | 1,340,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -7,070,000.00 USD | -16,160,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -9,200,000.00 USD | -26,080,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -10,680,000.00 USD | -25,420,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -19,580,000.00 USD | -51,510,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -15,600,000.00 USD | -54,140,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -18,200,000.00 USD | -52,370,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -16,400,000.00 USD | -52,310,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -39,170,000.00 USD | -108,950,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -86,720,000.00 USD | -109,220,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -566,510,000.00 USD | -1,220,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-5.43M` | 15m=`-5.31M` | 1h=`-9.20M` | 24h=`-39.17M`
* Futures Capital Netflows: 5m=`+509.28K` | 15m=`+1.34M` | 1h=`-26.08M` | 24h=`-108.95M`
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
  * `2026-10-30 01:35:49 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:00:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0133` pts)
  * +2.5R Take Profit: `1.32`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.30` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.32` (Risk Distance: `0.0133` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
