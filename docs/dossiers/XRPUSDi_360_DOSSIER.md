# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 01:39:05 IST` (`2026-10-29 20:09:05 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.27` | **Live Ask Quote**: `1.28` | **Mid Price**: `1.28`
- **Spread Points**: `4.00` | **Spread BPS**: `31.35 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.29` | VWAP Z-Score: `-1.61` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0064` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `37.28` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.32` | Lower -3.00σ Band: `1.27`
  * Upper +2.51σ Band: `1.31` | Lower -2.51σ Band: `1.27`
  * Upper +2.01σ Band: `1.31` | Lower -2.01σ Band: `1.28`
  * Upper +2.00σ Band: `1.31` | Lower -2.00σ Band: `1.28`
  * Upper +1.28σ Band: `1.30` | Lower -1.28σ Band: `1.28`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.28`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.28` | EMA-20=`1.29` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.29` (Slope: `+0.0000`) | EMA-100=`1.30`
  * Institutional Anchors: EMA-144=`1.30` | EMA-200=`1.30` (Slope: `-0.1599`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.28` | Weekly High=`1.34` | Weekly Low=`1.28`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.30` (Distance: `-1.78%`)
  * Point of Control (POC) = `1.29` (Distance: `-0.93%`)
  * Value Area Low (VAL) = `1.28` (Distance: `-0.53%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `1.27` - `1.28`
  * Optimal Trade Entry (OTE 0.705): `1.28`
  * Structural Invalidation Anchor (0.786): `1.29`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.28` | `1.29` | `1.28` | `1.28` | `817,606` | 1,050,012.56 USD | 105,282.69 USD | `+10.03%` | -42,318,230.75 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `1.28` | `1.28` | `1.28` | `1.28` | `4,274,379` | 5,479,063.68 USD | -1,263,127.61 USD | `-23.05%` | -43,581,358.36 USD | `-0.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.28` | `1.28` | `1.27` | `1.28` | `7,603,106` | 9,719,906.87 USD | -4,004,785.53 USD | `-41.20%` | -47,586,143.89 USD | `-1.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.28` | `1.29` | `1.28` | `1.29` | `2,940,674` | 3,779,916.77 USD | 146,563.75 USD | `+3.88%` | -41,133,315.92 USD | `+0.38` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `1.28` | `1.29` | `1.28` | `1.28` | `6,055,937` | 7,767,016.10 USD | -1,241,791.04 USD | `-15.99%` | -42,375,106.96 USD | `-0.20` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.28` | `1.28` | `1.27` | `1.28` | `7,560,269` | 9,665,212.77 USD | -3,960,798.43 USD | `-40.98%` | -46,335,905.39 USD | `-1.19` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.29` | `38,773,350` | 49,794,344.17 USD | -9,116,518.67 USD | `-18.31%` | -40,138,234.48 USD | `-1.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `1.29` | `1.29` | `1.28` | `1.28` | `17,509,907` | 22,469,016.48 USD | -1,419,504.92 USD | `-6.32%` | -41,557,739.40 USD | `+0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.28` | `1.28` | `1.27` | `1.28` | `7,546,136` | 9,647,170.43 USD | -3,971,609.40 USD | `-41.17%` | -45,529,348.80 USD | `-0.50` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.27` | `1.28` | `7,560,269` | 9,665,212.77 USD | -3,960,798.43 USD | `-40.98%` | -43,899,828.25 USD | `+0.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,072,364.54 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,389,228.53 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,527,234.86 USD | `+0.80` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -39,939,029.81 USD | `-0.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.27` | `1.28` | `7,560,269` | 9,665,212.77 USD | -3,960,798.43 USD | `-40.98%` | -43,899,828.25 USD | `+0.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:33:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `26` | `0x31b1...1434` | `LONG` | 44,920,802.69 USD | `35,031,430.00` | `1.13` | `1.27` | `0.9612` | 5,341,919.42 USD | `+11.89%` | `10X Cross` |
| `88` | `0x5b5d...c060` | `SHORT` | 20,213,934.62 USD | `15,964,251.00` | `1.44` | `1.27` | `11.70` | 2,702,134.09 USD | `+13.37%` | `5X Cross` |
| `153` | `0x58f0...0d20` | `LONG` | 13,910,497.90 USD | `10,931,629.00` | `1.36` | `1.27` | `1.26` | -954,655.06 USD | `-6.86%` | `20X Cross` |
| `155` | `0xb83d...6e36` | `SHORT` | 13,528,593.05 USD | `10,555,450.00` | `1.50` | `1.27` | `13.79` | 2,293,976.60 USD | `+16.96%` | `5X Cross` |
| `439` | `0xca49...53c8` | `SHORT` | 5,260,524.11 USD | `4,138,886.00` | `1.44` | `1.27` | `4.52` | 692,798.63 USD | `+13.17%` | `20X Cross` |
| `447` | `0xfc27...9d9d` | `SHORT` | 5,122,086.66 USD | `4,030,283.00` | `1.31` | `1.27` | `5.04` | 173,328.49 USD | `+3.38%` | `20X Cross` |
| `496` | `0x610b...b613` | `LONG` | 4,544,401.96 USD | `3,543,946.00` | `1.44` | `1.27` | `0.7203` | -555,590.65 USD | `-12.23%` | `5X Cross` |
| `529` | `0xc30c...a4c9` | `SHORT` | 4,233,468.80 USD | `3,302,753.00` | `1.42` | `1.27` | `1.59` | 466,418.05 USD | `+11.02%` | `8X Cross` |
| `546` | `0xdd53...2b13` | `SHORT` | 4,153,348.36 USD | `3,262,646.00` | `1.44` | `1.27` | `19.21` | 537,347.35 USD | `+12.94%` | `3X Cross` |
| `577` | `0xecb6...2b00` | `SHORT` | 3,978,296.33 USD | `3,136,859.00` | `1.31` | `1.27` | `10.39` | 116,749.46 USD | `+2.93%` | `10X Cross` |
| `601` | `0x9946...0852` | `SHORT` | 3,850,966.30 USD | `3,025,111.00` | `1.43` | `1.27` | `1.68` | 462,218.25 USD | `+12.00%` | `20X Cross` |
| `641` | `0x77ee...a018` | `LONG` | 3,588,067.63 USD | `2,829,037.00` | `1.28` | `1.27` | `0.000000` | -29,262.12 USD | `-0.82%` | `20X Cross` |
| `695` | `0x9aa5...58af` | `SHORT` | 3,335,049.10 USD | `2,604,083.00` | `1.46` | `1.27` | `4.23` | 462,671.56 USD | `+13.87%` | `20X Cross` |
| `707` | `0xf48f...10fe` | `LONG` | 3,289,841.83 USD | `2,565,779.00` | `1.53` | `1.27` | `0.9181` | -634,798.89 USD | `-19.30%` | `4X Cross` |
| `718` | `0x023a...2355` | `SHORT` | 3,217,974.99 USD | `2,538,636.00` | `1.33` | `1.27` | `4.52` | 150,872.60 USD | `+4.69%` | `20X Cross` |
| `755` | `0x45d2...4029` | `SHORT` | 3,111,630.50 USD | `2,453,000.00` | `1.48` | `1.27` | `17.10` | 526,649.92 USD | `+16.93%` | `20X Cross` |
| `1021` | `0xfc66...ca06` | `SHORT` | 2,196,066.30 USD | `1,732,460.00` | `1.31` | `1.27` | `21.80` | 69,905.05 USD | `+3.18%` | `20X Cross` |
| `1035` | `0xc179...e0c8` | `SHORT` | 2,160,186.35 USD | `1,704,558.00` | `1.30` | `1.27` | `4.74` | 58,054.71 USD | `+2.69%` | `10X Cross` |
| `1080` | `0xeadc...9d55` | `LONG` | 2,077,075.95 USD | `1,619,805.00` | `1.21` | `1.27` | `0.000000` | 118,232.93 USD | `+5.69%` | `20X Cross` |
| `1151` | `0x94b2...599e` | `SHORT` | 1,975,634.48 USD | `1,540,696.00` | `1.36` | `1.27` | `1.83` | 124,831.97 USD | `+6.32%` | `20X Cross` |
| `1163` | `0xbcd4...0dd2` | `SHORT` | 1,961,074.89 USD | `1,529,461.00` | `1.31` | `1.27` | `2.13` | 43,469.70 USD | `+2.22%` | `20X Cross` |
| `1182` | `0x3fc5...c0c1` | `SHORT` | 1,938,461.99 USD | `1,511,779.00` | `1.52` | `1.27` | `2.66` | 353,152.61 USD | `+18.22%` | `20X Cross` |
| `1203` | `0x31ef...f715` | `LONG` | 1,894,150.23 USD | `1,475,080.00` | `1.49` | `1.27` | `1.04` | -305,115.17 USD | `-16.11%` | `3X Isolated` |
| `1265` | `0x7737...bf66` | `SHORT` | 1,811,780.72 USD | `1,413,466.00` | `1.41` | `1.27` | `13.94` | 187,087.93 USD | `+10.33%` | `10X Cross` |
| `1291` | `0xef96...9383` | `SHORT` | 1,763,230.33 USD | `1,390,999.00` | `1.34` | `1.27` | `4.15` | 100,554.89 USD | `+5.70%` | `20X Cross` |
| `1368` | `0xee2b...d67e` | `LONG` | 1,656,498.74 USD | `1,306,284.00` | `1.55` | `1.27` | `0.3025` | -374,156.16 USD | `-22.59%` | `4X Cross` |
| `1423` | `0x215d...f80a` | `LONG` | 1,604,527.76 USD | `1,251,777.00` | `1.32` | `1.27` | `1.19` | -49,926.47 USD | `-3.11%` | `14X Cross` |
| `1438` | `0x4537...8732` | `SHORT` | 1,580,132.86 USD | `1,245,474.00` | `1.31` | `1.27` | `2.06` | 48,995.89 USD | `+3.10%` | `10X Cross` |
| `1469` | `0x123d...3bff` | `LONG` | 1,541,158.70 USD | `1,215,329.00` | `1.35` | `1.27` | `0.000000` | -95,910.52 USD | `-6.22%` | `10X Cross` |
| `1504` | `0x95da...2328` | `LONG` | 1,504,730.21 USD | `1,171,817.00` | `1.37` | `1.27` | `0.000000` | -97,045.78 USD | `-6.45%` | `5X Cross` |
| `1523` | `0xdf95...7d72` | `SHORT` | 1,471,141.83 USD | `1,160,115.00` | `1.37` | `1.27` | `34.13` | 122,217.43 USD | `+8.31%` | `20X Cross` |
| `1559` | `0x5fa3...35b7` | `SHORT` | 1,428,497.74 USD | `1,126,931.00` | `1.31` | `1.27` | `3.18` | 46,644.89 USD | `+3.27%` | `20X Cross` |
| `1685` | `0xb1ce...681b` | `LONG` | 1,296,311.99 USD | `1,021,764.00` | `1.49` | `1.27` | `1.16` | -227,744.51 USD | `-17.57%` | `4X Isolated` |
| `1777` | `0x3c36...461a` | `LONG` | 1,195,744.87 USD | `940,051.00` | `1.30` | `1.27` | `1.06` | -23,335.74 USD | `-1.95%` | `10X Cross` |
| `1988` | `0xbfc7...80b4` | `SHORT` | 1,024,560.00 USD | `800,000.00` | `1.48` | `1.27` | `6.98` | 158,894.65 USD | `+15.51%` | `20X Cross` |
| `1989` | `0xe9d1...d2d3` | `SHORT` | 1,023,845.52 USD | `808,597.00` | `1.31` | `1.27` | `2.60` | 33,434.95 USD | `+3.27%` | `10X Cross` |

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
| `7D` | `Long Liquidation` | `1.15` | 197,700,000.00 USD | 197,700,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 73,250,000.00 USD | 73,250,000.00 USD | 1,390.00 USD | 11,150.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 197,540,000.00 USD | 197,540,000.00 USD | 139,270.00 USD | 107,710.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 73,050,000.00 USD | 73,050,000.00 USD | 56,830.00 USD | 37,210.00 USD | 166,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 160,170.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 196,810,000.00 USD | 196,810,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 72,790,000.00 USD | 72,790,000.00 USD | 29,120.00 USD | 9,570.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 196,580,000.00 USD | 196,580,000.00 USD | 258,370.00 USD | 96,700.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 72,720,000.00 USD | 72,720,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 195,720,000.00 USD | 195,720,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 72,410,000.00 USD | 72,410,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 194,980,000.00 USD | 194,980,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 71,790,000.00 USD | 71,790,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 193,930,000.00 USD | 193,930,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 71,170,000.00 USD | 71,170,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,590,000.00 USD | 23,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.17` | 192,600,000.00 USD | 192,600,000.00 USD | 218,150.00 USD | 212,700.00 USD | 529,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 70,950,000.00 USD | 70,950,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 191,640,000.00 USD | 191,640,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 70,640,000.00 USD | 70,640,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 190,570,000.00 USD | 190,570,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 70,480,000.00 USD | 70,480,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 188,540,000.00 USD | 188,540,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 70,310,000.00 USD | 70,310,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 187,690,000.00 USD | 187,690,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 70,050,000.00 USD | 70,050,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 287,030.00 USD | 21,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.18` | 186,800,000.00 USD | 186,800,000.00 USD | 181,850.00 USD | 95,620.00 USD | 377,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 69,710,000.00 USD | 69,710,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 186,140,000.00 USD | 186,140,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 69,590,000.00 USD | 69,590,000.00 USD | 77,850.00 USD | 41,360.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 185,720,000.00 USD | 185,720,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 69,420,000.00 USD | 69,420,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 185,110,000.00 USD | 185,110,000.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 69,380,000.00 USD | 69,380,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 184,870,000.00 USD | 184,870,000.00 USD | 119,620.00 USD | 65,900.00 USD | 286,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 69,270,000.00 USD | 69,270,000.00 USD | 48,820.00 USD | 7,460.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 2,180,000.00 USD | 21,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.19` | 184,400,000.00 USD | 184,400,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 69,190,000.00 USD | 69,190,000.00 USD | 1,560.00 USD | 16,590.00 USD | 20,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 184,220,000.00 USD | 184,220,000.00 USD | 216,330.00 USD | 94,590.00 USD | 606,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 69,150,000.00 USD | 69,150,000.00 USD | 29,730.00 USD | 103.33 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 183,300,000.00 USD | 183,300,000.00 USD | 211,840.00 USD | 81,140.00 USD | 281,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 69,110,000.00 USD | 69,110,000.00 USD | 28,290.00 USD | 10,480.00 USD | 48,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 182,730,000.00 USD | 182,730,000.00 USD | 149,990.00 USD | 95,880.00 USD | 123,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 69,020,000.00 USD | 69,020,000.00 USD | 48,530.00 USD | 27,990.00 USD | 102,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 182,360,000.00 USD | 182,360,000.00 USD | 219,860.00 USD | 72,930.00 USD | 465,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 68,840,000.00 USD | 68,840,000.00 USD | 83,580.00 USD | 33,950.00 USD | 31,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 472,230.00 USD | 19,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.20` | 181,600,000.00 USD | 181,600,000.00 USD | 251,760.00 USD | 140,610.00 USD | 318,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 68,690,000.00 USD | 68,690,000.00 USD | 109,050.00 USD | 6,620.00 USD | 18,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 180,890,000.00 USD | 180,890,000.00 USD | 5,350.00 USD | 38,700.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 68,560,000.00 USD | 68,560,000.00 USD | 24,520.00 USD | 21,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 180,820,000.00 USD | 180,820,000.00 USD | 72,960.00 USD | 36,750.00 USD | 18,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 68,510,000.00 USD | 68,510,000.00 USD | 11,810.00 USD | 1,130.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 180,700,000.00 USD | 180,700,000.00 USD | 184,030.00 USD | 62,270.00 USD | 57,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 68,500,000.00 USD | 68,500,000.00 USD | 43,340.00 USD | 13,890.00 USD | 61,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 180,390,000.00 USD | 180,390,000.00 USD | 47,500.00 USD | 29,680.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 838,010.00 USD | 18,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.21` | 180,240,000.00 USD | 180,240,000.00 USD | 13,620.00 USD | 3,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 68,380,000.00 USD | 68,380,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 180,220,000.00 USD | 180,220,000.00 USD | 241,190.00 USD | 2,360.00 USD | 22,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 68,370,000.00 USD | 68,370,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD | `Tier 1 CEX` |
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
| `1D` | `Long Liquidation` | `1.23` | 68,340,000.00 USD | 68,340,000.00 USD | 100,480.00 USD | 374.17 USD | 160,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 175,780,000.00 USD | 175,780,000.00 USD | 235,350.00 USD | 112,100.00 USD | 795,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 68,080,000.00 USD | 68,080,000.00 USD | 265,980.00 USD | 67,310.00 USD | 639,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 174,640,000.00 USD | 174,640,000.00 USD | 706,530.00 USD | 355,960.00 USD | 940,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 67,110,000.00 USD | 67,110,000.00 USD | 93,200.00 USD | 54,570.00 USD | 208,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 172,640,000.00 USD | 172,640,000.00 USD | 1,130,000.00 USD | 364,060.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 66,750,000.00 USD | 66,750,000.00 USD | 139,070.00 USD | 22,970.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 556,980.00 USD | 16,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.24` | 169,600,000.00 USD | 169,600,000.00 USD | 1,120,000.00 USD | 760,590.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 66,580,000.00 USD | 66,580,000.00 USD | 802,870.00 USD | 317,390.00 USD | 716,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 165,110,000.00 USD | 165,110,000.00 USD | 1,960,000.00 USD | 859,010.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 64,740,000.00 USD | 64,740,000.00 USD | 1,340,000.00 USD | 641,660.00 USD | 928,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 160,200,000.00 USD | 160,200,000.00 USD | 2,210,000.00 USD | 1,010,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 61,840,000.00 USD | 61,840,000.00 USD | 576,610.00 USD | 333,360.00 USD | 574,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 154,290,000.00 USD | 154,290,000.00 USD | 1,210,000.00 USD | 569,760.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 60,350,000.00 USD | 60,350,000.00 USD | 207,000.00 USD | 233,640.00 USD | 324,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 151,240,000.00 USD | 151,240,000.00 USD | 1,020,000.00 USD | 537,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 59,590,000.00 USD | 59,590,000.00 USD | 546,970.00 USD | 84,110.00 USD | 349,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 263,760.00 USD | 15,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.25` | 148,000,000.00 USD | 148,000,000.00 USD | 2,520,000.00 USD | 695,090.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 58,610,000.00 USD | 58,610,000.00 USD | 384,220.00 USD | 90,850.00 USD | 261,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 141,740,000.00 USD | 141,740,000.00 USD | 2,150,000.00 USD | 1,450,000.00 USD | 5,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 57,870,000.00 USD | 57,870,000.00 USD | 207,040.00 USD | 196,500.00 USD | 303,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 132,290,000.00 USD | 132,290,000.00 USD | 3,090,000.00 USD | 1,160,000.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 57,160,000.00 USD | 57,160,000.00 USD | 117,990.00 USD | 79,810.00 USD | 571,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 125,870,000.00 USD | 125,870,000.00 USD | 2,140,000.00 USD | 783,920.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 56,390,000.00 USD | 56,390,000.00 USD | 471,210.00 USD | 17,220.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 121,510,000.00 USD | 121,510,000.00 USD | 262,320.00 USD | 552,710.00 USD | 814,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 55,370,000.00 USD | 55,370,000.00 USD | 607,050.00 USD | 98,250.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 553,020.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.26` | 119,880,000.00 USD | 119,880,000.00 USD | 1,360,000.00 USD | 849,040.00 USD | 2,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 53,550,000.00 USD | 53,550,000.00 USD | 643,140.00 USD | 336,810.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 114,740,000.00 USD | 114,740,000.00 USD | 1,070,000.00 USD | 211,890.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 51,540,000.00 USD | 51,540,000.00 USD | 366,730.00 USD | 3,600.00 USD | 313,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 112,450,000.00 USD | 112,450,000.00 USD | 1,210,000.00 USD | 691,780.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 50,850,000.00 USD | 50,850,000.00 USD | 437,560.00 USD | 218,760.00 USD | 631,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 108,970,000.00 USD | 108,970,000.00 USD | 1,980,000.00 USD | 1,450,000.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 49,570,000.00 USD | 49,570,000.00 USD | 1,470,000.00 USD | 545,220.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 104,020,000.00 USD | 104,020,000.00 USD | 3,500,000.00 USD | 1,970,000.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 46,470,000.00 USD | 46,470,000.00 USD | 2,670,000.00 USD | 1,350,000.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.26` | 14,450,000.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.27` | 95,020,000.00 USD | 95,020,000.00 USD | 4,470,000.00 USD | 1,960,000.00 USD | 6,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 40,480,000.00 USD | 40,480,000.00 USD | 1,620,000.00 USD | 666,960.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 82,050,000.00 USD | 82,050,000.00 USD | 2,890,000.00 USD | 1,380,000.00 USD | 4,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 36,330,000.00 USD | 36,330,000.00 USD | 1,520,000.00 USD | 733,250.00 USD | 3,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 73,670,000.00 USD | 73,670,000.00 USD | 3,090,000.00 USD | 2,160,000.00 USD | 6,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 30,810,000.00 USD | 30,810,000.00 USD | 1,480,000.00 USD | 431,480.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 61,960,000.00 USD | 61,960,000.00 USD | 4,570,000.00 USD | 2,590,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 27,200,000.00 USD | 27,200,000.00 USD | 1,490,000.00 USD | 341,030.00 USD | 735,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 47,670,000.00 USD | 47,670,000.00 USD | 4,600,000.00 USD | 1,720,000.00 USD | 11,540,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 24,630,000.00 USD | 24,630,000.00 USD | 2,290,000.00 USD | 848,600.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.27` | 169,550.00 USD | 173,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.28` | 29,820,000.00 USD | 29,820,000.00 USD | 4,130,000.00 USD | 2,410,000.00 USD | 5,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 18,700,000.00 USD | 18,700,000.00 USD | 4,640,000.00 USD | 2,800,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 17,330,000.00 USD | 17,330,000.00 USD | 7,720,000.00 USD | 2,860,000.00 USD | 5,150,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 7,300,000.00 USD | 7,300,000.00 USD | 3,070,000.00 USD | 2,050,000.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 1,420,000.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 221,010.00 USD | 221,010.00 USD | 0.00 USD | 221,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 108,100.00 USD | 108,100.00 USD | 0.00 USD | 22,110.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 4,390,000.00 USD | 4,390,000.00 USD | 3,610,000.00 USD | 657,250.00 USD | 123,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 488,880.00 USD | 488,880.00 USD | 0.00 USD | 488,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.28` | 3,680.00 USD | 3,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.29` | 5,790,000.00 USD | 5,790,000.00 USD | 505,690.00 USD | 888,530.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 964,060.00 USD | 964,060.00 USD | 365,870.00 USD | 100,470.00 USD | 8,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 6,230,000.00 USD | 6,230,000.00 USD | 440,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 472,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 8,390,000.00 USD | 8,390,000.00 USD | 1,040,000.00 USD | 0.00 USD | 648,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 3,220,000.00 USD | 3,220,000.00 USD | 388,000.00 USD | 0.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 11,170,000.00 USD | 11,170,000.00 USD | 1,110,000.00 USD | 0.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 7,510,000.00 USD | 7,510,000.00 USD | 1,060,000.00 USD | 449,340.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 27,590.00 USD | 27,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.30` | 16,460,000.00 USD | 16,460,000.00 USD | 777,570.00 USD | 1,090,000.00 USD | 3,420,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 9,240,000.00 USD | 9,240,000.00 USD | 278,090.00 USD | 626,520.00 USD | 829,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 17,710,000.00 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 9,580,000.00 USD | 9,580,000.00 USD | 254,730.00 USD | 86,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 18,680,000.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 11,030,000.00 USD | 11,030,000.00 USD | 193,920.00 USD | 81,320.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 19,530,000.00 USD | 19,530,000.00 USD | 0.00 USD | 859,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 12,460,000.00 USD | 12,460,000.00 USD | 516,450.00 USD | 910,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 21,480,000.00 USD | 21,480,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 13,240,000.00 USD | 13,240,000.00 USD | 299,990.00 USD | 353,430.00 USD | 127,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 291.02 USD | 27,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.31` | 23,430,000.00 USD | 23,430,000.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 14,990,000.00 USD | 14,990,000.00 USD | 594,820.00 USD | 120,350.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 26,900,000.00 USD | 26,900,000.00 USD | 722,880.00 USD | 352,510.00 USD | 2,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 17,570,000.00 USD | 17,570,000.00 USD | 788,510.00 USD | 186,820.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 28,660,000.00 USD | 28,660,000.00 USD | 1,340,000.00 USD | 0.00 USD | 415,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 19,520,000.00 USD | 19,520,000.00 USD | 807,130.00 USD | 688,780.00 USD | 450,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 32,410,000.00 USD | 32,410,000.00 USD | 79,920.00 USD | 747,120.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 22,260,000.00 USD | 22,260,000.00 USD | 1,290,000.00 USD | 511,150.00 USD | 944,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 33,560,000.00 USD | 33,560,000.00 USD | 515,950.00 USD | 149,950.00 USD | 485,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 25,730,000.00 USD | 25,730,000.00 USD | 372,630.00 USD | 572,040.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 24,240.00 USD | 52,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.32` | 37,740,000.00 USD | 37,740,000.00 USD | 44,360.00 USD | 1,750,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 32,270,000.00 USD | 32,270,000.00 USD | 1,250,000.00 USD | 1,730,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 42,590,000.00 USD | 42,590,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 37,750,000.00 USD | 37,750,000.00 USD | 1,990,000.00 USD | 977,080.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 44,290,000.00 USD | 44,290,000.00 USD | 823,190.00 USD | 430,400.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 40,930,000.00 USD | 40,930,000.00 USD | 1,510,000.00 USD | 651,550.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 47,390,000.00 USD | 47,390,000.00 USD | 1,090,000.00 USD | 855,190.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 45,520,000.00 USD | 45,520,000.00 USD | 1,970,000.00 USD | 720,740.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 50,010,000.00 USD | 50,010,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 392,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 47,510,000.00 USD | 47,510,000.00 USD | 1,080,000.00 USD | 287,550.00 USD | 625,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 70,310.00 USD | 122,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.33` | 51,810,000.00 USD | 51,810,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 50,000,000.00 USD | 50,000,000.00 USD | 624,130.00 USD | 621,340.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 52,870,000.00 USD | 52,870,000.00 USD | 135,420.00 USD | 15,840.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 52,250,000.00 USD | 52,250,000.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 54,480,000.00 USD | 54,480,000.00 USD | 548,610.00 USD | 138,580.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 55,090,000.00 USD | 55,090,000.00 USD | 848,670.00 USD | 298,620.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 56,890,000.00 USD | 56,890,000.00 USD | 809,950.00 USD | 236,880.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 57,300,000.00 USD | 57,300,000.00 USD | 979,210.00 USD | 152,260.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 58,560,000.00 USD | 58,560,000.00 USD | 450,460.00 USD | 178,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 59,340,000.00 USD | 59,340,000.00 USD | 810,560.00 USD | 354,550.00 USD | 872,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 52,610.00 USD | 175,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.34` | 60,100,000.00 USD | 60,100,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 61,430,000.00 USD | 61,430,000.00 USD | 896,540.00 USD | 219,260.00 USD | 976,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 62,540,000.00 USD | 62,540,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 64,300,000.00 USD | 64,300,000.00 USD | 1,170,000.00 USD | 370,350.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 64,410,000.00 USD | 64,410,000.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 67,890,000.00 USD | 67,890,000.00 USD | 1,780,000.00 USD | 821,890.00 USD | 996,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 70,330,000.00 USD | 70,330,000.00 USD | 2,380,000.00 USD | 2,880,000.00 USD | 665,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 72,620,000.00 USD | 72,620,000.00 USD | 2,510,000.00 USD | 785,850.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 77,720,000.00 USD | 77,720,000.00 USD | 2,030,000.00 USD | 2,210,000.00 USD | 3,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 75,070,000.00 USD | 75,070,000.00 USD | 918,290.00 USD | 629,160.00 USD | 904,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 167,450.00 USD | 342,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.35` | 88,470,000.00 USD | 88,470,000.00 USD | 4,040,000.00 USD | 1,900,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 76,240,000.00 USD | 76,240,000.00 USD | 473,710.00 USD | 234,160.00 USD | 458,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 97,310,000.00 USD | 97,310,000.00 USD | 3,160,000.00 USD | 2,040,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 79,230,000.00 USD | 79,230,000.00 USD | 1,290,000.00 USD | 356,450.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 106,510,000.00 USD | 106,510,000.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 80,320,000.00 USD | 80,320,000.00 USD | 507,940.00 USD | 127,500.00 USD | 452,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 115,770,000.00 USD | 115,770,000.00 USD | 3,040,000.00 USD | 1,390,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 82,200,000.00 USD | 82,200,000.00 USD | 749,290.00 USD | 397,350.00 USD | 728,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 123,310,000.00 USD | 123,310,000.00 USD | 2,320,000.00 USD | 886,190.00 USD | 4,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 84,330,000.00 USD | 84,330,000.00 USD | 722,260.00 USD | 297,760.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 3,990.00 USD | 346,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.36` | 130,470,000.00 USD | 130,470,000.00 USD | 2,820,000.00 USD | 1,060,000.00 USD | 3,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 86,070,000.00 USD | 86,070,000.00 USD | 983,180.00 USD | 66,140.00 USD | 685,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 133,000,000.00 USD | 133,000,000.00 USD | 1,040,000.00 USD | 639,580.00 USD | 849,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 86,760,000.00 USD | 86,760,000.00 USD | 390,030.00 USD | 150,540.00 USD | 153,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 136,070,000.00 USD | 136,070,000.00 USD | 1,430,000.00 USD | 410,060.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 87,440,000.00 USD | 87,440,000.00 USD | 318,280.00 USD | 155,640.00 USD | 202,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 139,850,000.00 USD | 139,850,000.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 88,540,000.00 USD | 88,540,000.00 USD | 452,880.00 USD | 103,540.00 USD | 545,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 142,600,000.00 USD | 142,600,000.00 USD | 1,430,000.00 USD | 614,410.00 USD | 702,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 88,590,000.00 USD | 88,590,000.00 USD | 0.00 USD | 26,460.00 USD | 25,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 198,460.00 USD | 544,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.37` | 143,340,000.00 USD | 143,340,000.00 USD | 206,650.00 USD | 111,150.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 88,910,000.00 USD | 88,910,000.00 USD | 68,130.00 USD | 85,100.00 USD | 170,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 144,450,000.00 USD | 144,450,000.00 USD | 544,160.00 USD | 181,820.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 89,300,000.00 USD | 89,300,000.00 USD | 159,370.00 USD | 1,410.00 USD | 229,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 146,170,000.00 USD | 146,170,000.00 USD | 477,130.00 USD | 362,580.00 USD | 883,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 89,490,000.00 USD | 89,490,000.00 USD | 1,740.00 USD | 66,370.00 USD | 119,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 148,330,000.00 USD | 148,330,000.00 USD | 743,900.00 USD | 285,210.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 89,640,000.00 USD | 89,640,000.00 USD | 75,340.00 USD | 249.08 USD | 69,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 150,440,000.00 USD | 150,440,000.00 USD | 737,410.00 USD | 437,690.00 USD | 940,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 89,760,000.00 USD | 89,760,000.00 USD | 54,550.00 USD | 884.30 USD | 69,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 323.12 USD | 545,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.38` | 152,110,000.00 USD | 152,110,000.00 USD | 450,750.00 USD | 380,930.00 USD | 841,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 90,090,000.00 USD | 90,090,000.00 USD | 112,910.00 USD | 50,330.00 USD | 164,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 153,670,000.00 USD | 153,670,000.00 USD | 878,240.00 USD | 363,870.00 USD | 308,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 90,650,000.00 USD | 90,650,000.00 USD | 271,120.00 USD | 72,410.00 USD | 212,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 155,710,000.00 USD | 155,710,000.00 USD | 506,860.00 USD | 199,720.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 91,130,000.00 USD | 91,130,000.00 USD | 264,080.00 USD | 108,980.00 USD | 109,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 157,980,000.00 USD | 157,980,000.00 USD | 841,840.00 USD | 445,210.00 USD | 985,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 91,530,000.00 USD | 91,530,000.00 USD | 304,540.00 USD | 24,460.00 USD | 77,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 158,680,000.00 USD | 158,680,000.00 USD | 403,730.00 USD | 160,810.00 USD | 129,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 91,710,000.00 USD | 91,710,000.00 USD | 88,160.00 USD | 54,030.00 USD | 35,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 31,550.00 USD | 576,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.39` | 159,600,000.00 USD | 159,600,000.00 USD | 377,810.00 USD | 134,820.00 USD | 406,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 91,750,000.00 USD | 91,750,000.00 USD | 29,510.00 USD | 2,820.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 160,460,000.00 USD | 160,460,000.00 USD | 384,080.00 USD | 263,660.00 USD | 218,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 92,130,000.00 USD | 92,130,000.00 USD | 140,810.00 USD | 51,770.00 USD | 189,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 161,200,000.00 USD | 161,200,000.00 USD | 497,500.00 USD | 118,700.00 USD | 118,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 161,520,000.00 USD | 161,520,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 161,580,000.00 USD | 161,580,000.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 92,150,000.00 USD | 92,150,000.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 177,010.00 USD | 753,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 161,680,000.00 USD | 161,680,000.00 USD | 82,090.00 USD | 0.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 92,250,000.00 USD | 92,250,000.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 161,690,000.00 USD | 161,690,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 161,750,000.00 USD | 161,750,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 161,830,000.00 USD | 161,830,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 162,120,000.00 USD | 162,120,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 1,310.00 USD | 755,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 162,280,000.00 USD | 162,280,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 162,440,000.00 USD | 162,440,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 92,450,000.00 USD | 92,450,000.00 USD | 1,390.00 USD | 11,150.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 163,170,000.00 USD | 163,170,000.00 USD | 139,270.00 USD | 107,710.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 92,710,000.00 USD | 92,710,000.00 USD | 56,830.00 USD | 37,210.00 USD | 166,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 163,400,000.00 USD | 163,400,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 92,740,000.00 USD | 92,740,000.00 USD | 0.00 USD | 383.75 USD | 28,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 163,700,000.00 USD | 163,700,000.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 92,780,000.00 USD | 92,780,000.00 USD | 29,120.00 USD | 9,190.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 758,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.42` | 164,260,000.00 USD | 164,260,000.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 93,090,000.00 USD | 93,090,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 165,000,000.00 USD | 165,000,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 93,710,000.00 USD | 93,710,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 166,050,000.00 USD | 166,050,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 94,330,000.00 USD | 94,330,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 167,380,000.00 USD | 167,380,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 94,550,000.00 USD | 94,550,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 167,580,000.00 USD | 167,580,000.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 94,630,000.00 USD | 94,630,000.00 USD | 29,370.00 USD | 27,060.00 USD | 28,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 94,400.00 USD | 853,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.43` | 94,760,000.00 USD | 94,760,000.00 USD | 70,500.00 USD | 8,390.00 USD | 44,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 168,340,000.00 USD | 168,340,000.00 USD | 151,730.00 USD | 92,020.00 USD | 521,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 169,410,000.00 USD | 169,410,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 171,440,000.00 USD | 171,440,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 172,290,000.00 USD | 172,290,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 173,180,000.00 USD | 173,180,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 33,430.00 USD | 886,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 173,210,000.00 USD | 173,210,000.00 USD | 6,560.00 USD | 12,030.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 173,840,000.00 USD | 173,840,000.00 USD | 175,290.00 USD | 83,590.00 USD | 366,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 174,260,000.00 USD | 174,260,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 174,870,000.00 USD | 174,870,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 175,110,000.00 USD | 175,110,000.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 599,610.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.45` | 175,210,000.00 USD | 175,210,000.00 USD | 50,420.00 USD | 39,100.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 175,580,000.00 USD | 175,580,000.00 USD | 69,200.00 USD | 26,800.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 175,760,000.00 USD | 175,760,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 176,670,000.00 USD | 176,670,000.00 USD | 216,330.00 USD | 94,590.00 USD | 598,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 177,200,000.00 USD | 177,200,000.00 USD | 176,550.00 USD | 81,140.00 USD | 274,660.00 USD | `Tier 1 CEX` |
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
| `Sell Stop` | `0.3050` | 3,110,000.00 USD | 0.00 USD | 147.62 USD | `-76.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 3,110,000.00 USD | 0.00 USD | 139.12 USD | `-70.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4150` | 3,110,000.00 USD | 0.00 USD | 200.86 USD | `-67.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 3,110,000.00 USD | 0.00 USD | 408.51 USD | `-65.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 3,110,000.00 USD | 0.00 USD | 520.52 USD | `-64.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 3,100,000.00 USD | 0.00 USD | 151.12 USD | `-63.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 3,100,000.00 USD | 0.00 USD | 190.00 USD | `-62.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 3,100,000.00 USD | 0.00 USD | 145.50 USD | `-62.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 3,100,000.00 USD | 0.00 USD | 1,030.00 USD | `-60.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 3,100,000.00 USD | 0.00 USD | 306.60 USD | `-59.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 3,100,000.00 USD | 0.00 USD | 6,750.00 USD | `-56.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 3,100,000.00 USD | 0.00 USD | 374.60 USD | `-55.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 3,100,000.00 USD | 0.00 USD | 100.62 USD | `-54.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 3,100,000.00 USD | 0.00 USD | 791.85 USD | `-50.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 3,100,000.00 USD | 0.00 USD | 573.40 USD | `-49.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 3,090,000.00 USD | 0.00 USD | 3,450.00 USD | `-48.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 3,090,000.00 USD | 0.00 USD | 3,010.00 USD | `-48.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 3,090,000.00 USD | 0.00 USD | 1,060.00 USD | `-45.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 3,090,000.00 USD | 0.00 USD | 1,590.00 USD | `-45.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 3,090,000.00 USD | 0.00 USD | 1,300.00 USD | `-41.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 3,080,000.00 USD | 0.00 USD | 2,880.00 USD | `-40.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 3,080,000.00 USD | 0.00 USD | 1,110.00 USD | `-38.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 3,080,000.00 USD | 0.00 USD | 798.57 USD | `-33.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 3,080,000.00 USD | 0.00 USD | 690.38 USD | `-31.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 3,080,000.00 USD | 0.00 USD | 1,420.00 USD | `-30.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 3,080,000.00 USD | 0.00 USD | 3,230.00 USD | `-30.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 3,070,000.00 USD | 0.00 USD | 838.94 USD | `-29.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 3,070,000.00 USD | 0.00 USD | 188.49 USD | `-28.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 3,070,000.00 USD | 0.00 USD | 2,730.00 USD | `-27.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 3,070,000.00 USD | 0.00 USD | 1,150.00 USD | `-27.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 3,070,000.00 USD | 0.00 USD | 112.46 USD | `-26.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 3,070,000.00 USD | 0.00 USD | 2,360.00 USD | `-25.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 3,070,000.00 USD | 0.00 USD | 3,910.00 USD | `-24.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 3,060,000.00 USD | 0.00 USD | 546,370.00 USD | `-23.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 2,520,000.00 USD | 0.00 USD | 5,250.00 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 2,510,000.00 USD | 0.00 USD | 897.49 USD | `-22.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 2,510,000.00 USD | 0.00 USD | 15,070.00 USD | `-21.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 2,500,000.00 USD | 0.00 USD | 4,330.00 USD | `-20.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 2,490,000.00 USD | 0.00 USD | 2,020.00 USD | `-20.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 2,490,000.00 USD | 0.00 USD | 38,000.00 USD | `-19.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 2,450,000.00 USD | 0.00 USD | 3,970.00 USD | `-18.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 2,450,000.00 USD | 0.00 USD | 7,090.00 USD | `-17.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 2,440,000.00 USD | 0.00 USD | 3,230.00 USD | `-16.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 2,440,000.00 USD | 0.00 USD | 34,770.00 USD | `-16.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 2,400,000.00 USD | 0.00 USD | 973.25 USD | `-15.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 2,400,000.00 USD | 0.00 USD | 8,000.00 USD | `-14.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 2,390,000.00 USD | 0.00 USD | 2,970.00 USD | `-13.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 2,390,000.00 USD | 0.00 USD | 9,300.00 USD | `-13.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 2,380,000.00 USD | 0.00 USD | 79,020.00 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 2,300,000.00 USD | 0.00 USD | 12,910.00 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 2,290,000.00 USD | 0.00 USD | 16,630.00 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 2,270,000.00 USD | 0.00 USD | 32,100.00 USD | `-9.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 2,240,000.00 USD | 0.00 USD | 14,080.00 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 2,230,000.00 USD | 0.00 USD | 4,790.00 USD | `-8.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 2,220,000.00 USD | 0.00 USD | 90,010.00 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 2,130,000.00 USD | 0.00 USD | 12,570.00 USD | `-6.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 2,120,000.00 USD | 0.00 USD | 52,130.00 USD | `-6.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 2,070,000.00 USD | 0.00 USD | 57,160.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 2,010,000.00 USD | 0.00 USD | 146,570.00 USD | `-4.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 1,860,000.00 USD | 0.00 USD | 382,250.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 1,480,000.00 USD | 0.00 USD | 291,800.00 USD | `-2.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 1,190,000.00 USD | 0.00 USD | 486,130.00 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.26` | 702,270.00 USD | 0.00 USD | 140,870.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.27` | 561,400.00 USD | 0.00 USD | 561,400.00 USD | `-0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 3,410.00 USD | 3,410.00 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 161,970.00 USD | 158,560.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 198,650.00 USD | 36,680.00 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 311,670.00 USD | 113,020.00 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 556,310.00 USD | 244,650.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 652,730.00 USD | 96,420.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 824,230.00 USD | 171,500.00 USD | 0.00 USD | `+4.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 851,630.00 USD | 27,390.00 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,130,000.00 USD | 281,080.00 USD | 0.00 USD | `+6.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,200,000.00 USD | 71,800.00 USD | 0.00 USD | `+7.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,280,000.00 USD | 73,090.00 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,350,000.00 USD | 71,640.00 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 5,690,000.00 USD | 4,340,000.00 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 5,720,000.00 USD | 30,770.00 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 5,740,000.00 USD | 19,640.00 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 5,820,000.00 USD | 82,400.00 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,010,000.00 USD | 193,480.00 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,060,000.00 USD | 43,500.00 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,080,000.00 USD | 27,080.00 USD | 0.00 USD | `+14.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,190,000.00 USD | 108,480.00 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,280,000.00 USD | 84,290.00 USD | 0.00 USD | `+15.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,290,000.00 USD | 14,970.00 USD | 0.00 USD | `+16.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,380,000.00 USD | 84,920.00 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,390,000.00 USD | 18,210.00 USD | 0.00 USD | `+18.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,500,000.00 USD | 103,290.00 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,550,000.00 USD | 57,450.00 USD | 0.00 USD | `+19.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,590,000.00 USD | 36,160.00 USD | 0.00 USD | `+20.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,600,000.00 USD | 6,110.00 USD | 0.00 USD | `+21.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,600,000.00 USD | 6,300.00 USD | 0.00 USD | `+22.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,610,000.00 USD | 6,410.00 USD | 0.00 USD | `+22.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,620,000.00 USD | 9,700.00 USD | 0.00 USD | `+23.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 6,750,000.00 USD | 128,920.00 USD | 0.00 USD | `+24.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 6,750,000.00 USD | 1,130.00 USD | 0.00 USD | `+25.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 6,830,000.00 USD | 81,600.00 USD | 0.00 USD | `+25.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 6,830,000.00 USD | 464.75 USD | 0.00 USD | `+26.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,030,000.00 USD | 199,230.00 USD | 0.00 USD | `+27.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,030,000.00 USD | 3,370.00 USD | 0.00 USD | `+28.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,070,000.00 USD | 33,550.00 USD | 0.00 USD | `+29.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,080,000.00 USD | 8,220.00 USD | 0.00 USD | `+29.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,080,000.00 USD | 5,760.00 USD | 0.00 USD | `+30.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,150,000.00 USD | 70,850.00 USD | 0.00 USD | `+31.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,160,000.00 USD | 8,570.00 USD | 0.00 USD | `+32.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,420,000.00 USD | 259,410.00 USD | 0.00 USD | `+32.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,430,000.00 USD | 14,030.00 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,450,000.00 USD | 14,560.00 USD | 0.00 USD | `+34.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,490,000.00 USD | 44,100.00 USD | 0.00 USD | `+35.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,500,000.00 USD | 4,710.00 USD | 0.00 USD | `+36.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,500,000.00 USD | 6,330.00 USD | 0.00 USD | `+36.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,530,000.00 USD | 21,720.00 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,650,000.00 USD | 122,650.00 USD | 0.00 USD | `+38.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 7,740,000.00 USD | 96,900.00 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 7,790,000.00 USD | 40,420.00 USD | 0.00 USD | `+39.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 7,790,000.00 USD | 254.51 USD | 0.00 USD | `+40.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 7,790,000.00 USD | 2,530.00 USD | 0.00 USD | `+41.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 7,790,000.00 USD | 1,830.00 USD | 0.00 USD | `+42.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 7,800,000.00 USD | 7,630.00 USD | 0.00 USD | `+43.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 7,800,000.00 USD | 1,900.00 USD | 0.00 USD | `+43.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 7,810,000.00 USD | 8,390.00 USD | 0.00 USD | `+44.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 7,810,000.00 USD | 4,550.00 USD | 0.00 USD | `+46.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 7,810,000.00 USD | 591.89 USD | 0.00 USD | `+47.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 7,860,000.00 USD | 44,350.00 USD | 0.00 USD | `+47.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 7,870,000.00 USD | 10,020.00 USD | 0.00 USD | `+48.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.92` | 7,870,000.00 USD | 7,410.00 USD | 0.00 USD | `+49.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 7,870,000.00 USD | 265.10 USD | 0.00 USD | `+50.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 7,880,000.00 USD | 2,040.00 USD | 0.00 USD | `+51.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 7,880,000.00 USD | 1,510.00 USD | 0.00 USD | `+52.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 7,890,000.00 USD | 14,120.00 USD | 0.00 USD | `+53.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 7,900,000.00 USD | 4,010.00 USD | 0.00 USD | `+54.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 7,900,000.00 USD | 325.54 USD | 0.00 USD | `+54.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 7,900,000.00 USD | 7,020.00 USD | 0.00 USD | `+55.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,040,000.00 USD | 138,900.00 USD | 0.00 USD | `+56.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,040,000.00 USD | 781.82 USD | 0.00 USD | `+57.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,040,000.00 USD | 222.75 USD | 0.00 USD | `+57.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,040,000.00 USD | 862.84 USD | 0.00 USD | `+58.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,050,000.00 USD | 3,490.00 USD | 0.00 USD | `+59.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,050,000.00 USD | 3,940.00 USD | 0.00 USD | `+61.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,050,000.00 USD | 661.93 USD | 0.00 USD | `+61.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,180,000.00 USD | 124,400.00 USD | 0.00 USD | `+63.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,180,000.00 USD | 1,580.00 USD | 0.00 USD | `+64.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,190,000.00 USD | 13,900.00 USD | 0.00 USD | `+65.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,220,000.00 USD | 24,840.00 USD | 0.00 USD | `+67.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,270,000.00 USD | 50,580.00 USD | 0.00 USD | `+68.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,270,000.00 USD | 1,710.00 USD | 0.00 USD | `+68.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,270,000.00 USD | 1,970.00 USD | 0.00 USD | `+71.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,420,000.00 USD | 151,380.00 USD | 0.00 USD | `+72.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.23` | 8,430,000.00 USD | 7,340.00 USD | 0.00 USD | `+74.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,430,000.00 USD | 3,120.00 USD | 0.00 USD | `+77.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,430,000.00 USD | 1,140.00 USD | 0.00 USD | `+78.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,450,000.00 USD | 12,150.00 USD | 0.00 USD | `+78.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,450,000.00 USD | 370.40 USD | 0.00 USD | `+80.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,450,000.00 USD | 733.19 USD | 0.00 USD | `+82.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,450,000.00 USD | 2,410.00 USD | 0.00 USD | `+84.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,450,000.00 USD | 475.00 USD | 0.00 USD | `+85.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,450,000.00 USD | 2,540.00 USD | 0.00 USD | `+86.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,700,000.00 USD | 251,200.00 USD | 0.00 USD | `+87.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,710,000.00 USD | 1,370.00 USD | 0.00 USD | `+88.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,710,000.00 USD | 564.92 USD | 0.00 USD | `+89.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.46` | 8,710,000.00 USD | 8,110.00 USD | 0.00 USD | `+91.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,720,000.00 USD | 3,420.00 USD | 0.00 USD | `+93.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,720,000.00 USD | 124.75 USD | 0.00 USD | `+94.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,760,000.00 USD | 42,600.00 USD | 0.00 USD | `+95.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.52` | 8,760,000.00 USD | 378.75 USD | 0.00 USD | `+96.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.56` | 8,760,000.00 USD | 389.88 USD | 0.00 USD | `+100.05%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `1.14` | 38,870,000.00 USD | 0.00 USD | 38,870,000.00 USD | 26,280.00 USD | 0.00 USD | 31,230.00 USD |
| `1D` | `1.14` | 38,810,000.00 USD | 0.00 USD | 38,810,000.00 USD | 0.00 USD | 304.00 USD | 0.00 USD |
| `1D` | `1.14` | 38,810,000.00 USD | 0.00 USD | 38,810,000.00 USD | 5,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.15` | 38,800,000.00 USD | 0.00 USD | 38,800,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 198,300,000.00 USD | 0.00 USD | 198,300,000.00 USD | 237,280.00 USD | 98,230.00 USD | 109,530.00 USD |
| `7D` | `1.15` | 197,860,000.00 USD | 0.00 USD | 197,860,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.15` | 38,790,000.00 USD | 0.00 USD | 38,790,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.15` | 197,700,000.00 USD | 0.00 USD | 197,700,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 38,720,000.00 USD | 0.00 USD | 38,720,000.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD |
| `7D` | `1.15` | 197,540,000.00 USD | 0.00 USD | 197,540,000.00 USD | 139,270.00 USD | 107,710.00 USD | 482,250.00 USD |
| `1D` | `1.16` | 38,340,000.00 USD | 0.00 USD | 38,340,000.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD |
| `7D` | `1.16` | 196,810,000.00 USD | 0.00 USD | 196,810,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 38,220,000.00 USD | 0.00 USD | 38,220,000.00 USD | 66,460.00 USD | 27,380.00 USD | 78,320.00 USD |
| `7D` | `1.16` | 196,580,000.00 USD | 0.00 USD | 196,580,000.00 USD | 258,370.00 USD | 96,700.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 38,040,000.00 USD | 0.00 USD | 38,040,000.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.16` | 195,720,000.00 USD | 0.00 USD | 195,720,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 37,660,000.00 USD | 0.00 USD | 37,660,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.16` | 194,980,000.00 USD | 0.00 USD | 194,980,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD |
| `1D` | `1.16` | 36,920,000.00 USD | 0.00 USD | 36,920,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.16` | 193,930,000.00 USD | 0.00 USD | 193,930,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD |
| `1D` | `1.17` | 36,490,000.00 USD | 0.00 USD | 36,490,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD |
| `7D` | `1.17` | 192,600,000.00 USD | 0.00 USD | 192,600,000.00 USD | 218,150.00 USD | 212,700.00 USD | 529,730.00 USD |
| `1D` | `1.17` | 36,160,000.00 USD | 0.00 USD | 36,160,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.17` | 191,640,000.00 USD | 0.00 USD | 191,640,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 35,980,000.00 USD | 0.00 USD | 35,980,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.17` | 190,570,000.00 USD | 0.00 USD | 190,570,000.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 35,820,000.00 USD | 0.00 USD | 35,820,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.17` | 188,540,000.00 USD | 0.00 USD | 188,540,000.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD |
| `1D` | `1.17` | 35,600,000.00 USD | 0.00 USD | 35,600,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.17` | 187,690,000.00 USD | 0.00 USD | 187,690,000.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD |
| `1D` | `1.18` | 35,330,000.00 USD | 0.00 USD | 35,330,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD |
| `7D` | `1.18` | 186,800,000.00 USD | 0.00 USD | 186,800,000.00 USD | 181,850.00 USD | 95,620.00 USD | 377,590.00 USD |
| `1D` | `1.18` | 35,110,000.00 USD | 0.00 USD | 35,110,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.18` | 186,140,000.00 USD | 0.00 USD | 186,140,000.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD |
| `1D` | `1.18` | 34,930,000.00 USD | 0.00 USD | 34,930,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.18` | 185,720,000.00 USD | 0.00 USD | 185,720,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD |
| `1D` | `1.18` | 34,850,000.00 USD | 0.00 USD | 34,850,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.18` | 185,110,000.00 USD | 0.00 USD | 185,110,000.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 34,770,000.00 USD | 0.00 USD | 34,770,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD |
| `7D` | `1.18` | 184,870,000.00 USD | 0.00 USD | 184,870,000.00 USD | 119,620.00 USD | 65,900.00 USD | 286,750.00 USD |
| `1D` | `1.19` | 34,650,000.00 USD | 0.00 USD | 34,650,000.00 USD | 694.57 USD | 23,390.00 USD | 20,370.00 USD |
| `7D` | `1.19` | 184,400,000.00 USD | 0.00 USD | 184,400,000.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD |
| `1D` | `1.19` | 34,610,000.00 USD | 0.00 USD | 34,610,000.00 USD | 30,140.00 USD | 99.63 USD | 12,880.00 USD |
| `7D` | `1.19` | 184,220,000.00 USD | 0.00 USD | 184,220,000.00 USD | 216,330.00 USD | 94,590.00 USD | 606,740.00 USD |
| `1D` | `1.19` | 34,570,000.00 USD | 0.00 USD | 34,570,000.00 USD | 10,800.00 USD | 238.88 USD | 21,580.00 USD |
| `7D` | `1.19` | 183,300,000.00 USD | 0.00 USD | 183,300,000.00 USD | 211,840.00 USD | 81,140.00 USD | 281,100.00 USD |
| `1D` | `1.19` | 34,530,000.00 USD | 0.00 USD | 34,530,000.00 USD | 20,520.00 USD | 17,640.00 USD | 56,850.00 USD |
| `7D` | `1.19` | 182,730,000.00 USD | 0.00 USD | 182,730,000.00 USD | 149,990.00 USD | 95,880.00 USD | 123,730.00 USD |
| `1D` | `1.19` | 34,440,000.00 USD | 0.00 USD | 34,440,000.00 USD | 111,560.00 USD | 42,920.00 USD | 83,580.00 USD |
| `7D` | `1.19` | 182,360,000.00 USD | 0.00 USD | 182,360,000.00 USD | 219,860.00 USD | 72,930.00 USD | 465,100.00 USD |
| `1D` | `1.20` | 34,200,000.00 USD | 0.00 USD | 34,200,000.00 USD | 40,880.00 USD | 18,340.00 USD | 29,820.00 USD |
| `7D` | `1.20` | 181,600,000.00 USD | 0.00 USD | 181,600,000.00 USD | 251,760.00 USD | 140,610.00 USD | 318,640.00 USD |
| `1D` | `1.20` | 34,110,000.00 USD | 0.00 USD | 34,110,000.00 USD | 111,360.00 USD | 7,010.00 USD | 9,050.00 USD |
| `7D` | `1.20` | 180,890,000.00 USD | 0.00 USD | 180,890,000.00 USD | 5,350.00 USD | 38,700.00 USD | 18,810.00 USD |
| `1D` | `1.20` | 33,980,000.00 USD | 0.00 USD | 33,980,000.00 USD | 0.00 USD | 15,120.00 USD | 0.00 USD |
| `7D` | `1.20` | 180,820,000.00 USD | 0.00 USD | 180,820,000.00 USD | 72,960.00 USD | 36,750.00 USD | 18,590.00 USD |
| `1D` | `1.20` | 33,970,000.00 USD | 0.00 USD | 33,970,000.00 USD | 0.00 USD | 0.00 USD | 23,890.00 USD |
| `7D` | `1.20` | 180,700,000.00 USD | 0.00 USD | 180,700,000.00 USD | 184,030.00 USD | 62,270.00 USD | 57,310.00 USD |
| `7D` | `1.20` | 180,390,000.00 USD | 0.00 USD | 180,390,000.00 USD | 47,500.00 USD | 29,680.00 USD | 79,720.00 USD |
| `7D` | `1.21` | 180,240,000.00 USD | 0.00 USD | 180,240,000.00 USD | 13,620.00 USD | 3,030.00 USD | 0.00 USD |
| `7D` | `1.21` | 180,220,000.00 USD | 0.00 USD | 180,220,000.00 USD | 241,190.00 USD | 2,360.00 USD | 22,480.00 USD |
| `7D` | `1.21` | 179,950,000.00 USD | 0.00 USD | 179,950,000.00 USD | 257,960.00 USD | 89,570.00 USD | 624,140.00 USD |
| `7D` | `1.21` | 178,980,000.00 USD | 0.00 USD | 178,980,000.00 USD | 199,450.00 USD | 109,690.00 USD | 212,340.00 USD |
| `1D` | `1.21` | 33,940,000.00 USD | 0.00 USD | 33,940,000.00 USD | 9,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.21` | 178,460,000.00 USD | 0.00 USD | 178,460,000.00 USD | 84,480.00 USD | 89,180.00 USD | 0.00 USD |
| `1D` | `1.22` | 33,930,000.00 USD | 0.00 USD | 33,930,000.00 USD | 56,560.00 USD | 0.00 USD | 78,080.00 USD |
| `7D` | `1.22` | 178,290,000.00 USD | 0.00 USD | 178,290,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.22` | 33,800,000.00 USD | 0.00 USD | 33,800,000.00 USD | 5,300.00 USD | 760.00 USD | 0.00 USD |
| `7D` | `1.22` | 178,190,000.00 USD | 0.00 USD | 178,190,000.00 USD | 0.00 USD | 0.00 USD | 27,810.00 USD |
| `1D` | `1.22` | 33,790,000.00 USD | 0.00 USD | 33,790,000.00 USD | 12,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.22` | 178,160,000.00 USD | 0.00 USD | 178,160,000.00 USD | 0.00 USD | 2,640.00 USD | 19,450.00 USD |
| `1D` | `1.22` | 33,780,000.00 USD | 0.00 USD | 33,780,000.00 USD | 0.00 USD | 211.25 USD | 0.00 USD |
| `7D` | `1.22` | 178,140,000.00 USD | 0.00 USD | 178,140,000.00 USD | 59,120.00 USD | 2,680.00 USD | 159,270.00 USD |
| `1D` | `1.22` | 33,780,000.00 USD | 0.00 USD | 33,780,000.00 USD | 40,080.00 USD | 206.80 USD | 0.00 USD |
| `7D` | `1.22` | 177,920,000.00 USD | 0.00 USD | 177,920,000.00 USD | 251,420.00 USD | 302,320.00 USD | 112,000.00 USD |
| `7D` | `1.23` | 177,250,000.00 USD | 0.00 USD | 177,250,000.00 USD | 492,660.00 USD | 141,800.00 USD | 153,930.00 USD |
| `1D` | `1.23` | 33,740,000.00 USD | 0.00 USD | 33,740,000.00 USD | 48,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.23` | 176,460,000.00 USD | 0.00 USD | 176,460,000.00 USD | 269,210.00 USD | 135,700.00 USD | 277,210.00 USD |
| `1D` | `1.23` | 33,690,000.00 USD | 0.00 USD | 33,690,000.00 USD | 203,290.00 USD | 28,070.00 USD | 518,460.00 USD |
| `7D` | `1.23` | 175,780,000.00 USD | 0.00 USD | 175,780,000.00 USD | 235,350.00 USD | 112,100.00 USD | 795,530.00 USD |
| `1D` | `1.23` | 32,940,000.00 USD | 0.00 USD | 32,940,000.00 USD | 295,580.00 USD | 131,700.00 USD | 492,180.00 USD |
| `7D` | `1.23` | 174,640,000.00 USD | 0.00 USD | 174,640,000.00 USD | 706,530.00 USD | 355,960.00 USD | 940,390.00 USD |
| `1D` | `1.23` | 32,020,000.00 USD | 0.00 USD | 32,020,000.00 USD | 97,740.00 USD | 1,800.00 USD | 73,470.00 USD |
| `7D` | `1.23` | 172,640,000.00 USD | 0.00 USD | 172,640,000.00 USD | 1,130,000.00 USD | 364,060.00 USD | 1,540,000.00 USD |
| `1D` | `1.24` | 31,850,000.00 USD | 0.00 USD | 31,850,000.00 USD | 517,670.00 USD | 120,320.00 USD | 554,790.00 USD |
| `7D` | `1.24` | 169,600,000.00 USD | 0.00 USD | 169,600,000.00 USD | 1,120,000.00 USD | 760,590.00 USD | 2,610,000.00 USD |
| `1D` | `1.24` | 30,660,000.00 USD | 0.00 USD | 30,660,000.00 USD | 1,080,000.00 USD | 666,380.00 USD | 709,340.00 USD |
| `7D` | `1.24` | 165,110,000.00 USD | 0.00 USD | 165,110,000.00 USD | 1,960,000.00 USD | 859,010.00 USD | 2,090,000.00 USD |
| `1D` | `1.24` | 28,200,000.00 USD | 0.00 USD | 28,200,000.00 USD | 961,180.00 USD | 493,310.00 USD | 740,300.00 USD |
| `7D` | `1.24` | 160,200,000.00 USD | 0.00 USD | 160,200,000.00 USD | 2,210,000.00 USD | 1,010,000.00 USD | 2,700,000.00 USD |
| `1D` | `1.24` | 26,000,000.00 USD | 0.00 USD | 26,000,000.00 USD | 460,870.00 USD | 188,510.00 USD | 497,840.00 USD |
| `7D` | `1.24` | 154,290,000.00 USD | 0.00 USD | 154,290,000.00 USD | 1,210,000.00 USD | 569,760.00 USD | 1,260,000.00 USD |
| `1D` | `1.24` | 24,850,000.00 USD | 0.00 USD | 24,850,000.00 USD | 383,160.00 USD | 123,910.00 USD | 516,600.00 USD |
| `7D` | `1.24` | 151,240,000.00 USD | 0.00 USD | 151,240,000.00 USD | 1,020,000.00 USD | 537,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.25` | 23,830,000.00 USD | 0.00 USD | 23,830,000.00 USD | 571,730.00 USD | 129,710.00 USD | 161,620.00 USD |
| `7D` | `1.25` | 148,000,000.00 USD | 0.00 USD | 148,000,000.00 USD | 2,520,000.00 USD | 695,090.00 USD | 3,060,000.00 USD |
| `1D` | `1.25` | 22,970,000.00 USD | 0.00 USD | 22,970,000.00 USD | 218,430.00 USD | 101,820.00 USD | 355,010.00 USD |
| `7D` | `1.25` | 141,740,000.00 USD | 0.00 USD | 141,740,000.00 USD | 2,150,000.00 USD | 1,450,000.00 USD | 5,850,000.00 USD |
| `1D` | `1.25` | 22,290,000.00 USD | 0.00 USD | 22,290,000.00 USD | 257,560.00 USD | 103,030.00 USD | 457,850.00 USD |
| `7D` | `1.25` | 132,290,000.00 USD | 0.00 USD | 132,290,000.00 USD | 3,090,000.00 USD | 1,160,000.00 USD | 2,170,000.00 USD |
| `1D` | `1.25` | 21,470,000.00 USD | 0.00 USD | 21,470,000.00 USD | 351,630.00 USD | 92,050.00 USD | 426,530.00 USD |
| `7D` | `1.25` | 125,870,000.00 USD | 0.00 USD | 125,870,000.00 USD | 2,140,000.00 USD | 783,920.00 USD | 1,440,000.00 USD |
| `1D` | `1.25` | 20,600,000.00 USD | 0.00 USD | 20,600,000.00 USD | 520,500.00 USD | 43,020.00 USD | 944,650.00 USD |
| `7D` | `1.25` | 121,510,000.00 USD | 0.00 USD | 121,510,000.00 USD | 262,320.00 USD | 552,710.00 USD | 814,990.00 USD |
| `1D` | `1.26` | 19,100,000.00 USD | 0.00 USD | 19,100,000.00 USD | 922,390.00 USD | 258,360.00 USD | 1,550,000.00 USD |
| `7D` | `1.26` | 119,880,000.00 USD | 0.00 USD | 119,880,000.00 USD | 1,360,000.00 USD | 849,040.00 USD | 2,940,000.00 USD |
| `1D` | `1.26` | 16,370,000.00 USD | 0.00 USD | 16,370,000.00 USD | 506,100.00 USD | 212,550.00 USD | 734,200.00 USD |
| `7D` | `1.26` | 114,740,000.00 USD | 0.00 USD | 114,740,000.00 USD | 1,070,000.00 USD | 211,890.00 USD | 1,000,000.00 USD |
| `1D` | `1.26` | 14,910,000.00 USD | 0.00 USD | 14,910,000.00 USD | 412,030.00 USD | 72,400.00 USD | 171,240.00 USD |
| `7D` | `1.26` | 112,450,000.00 USD | 0.00 USD | 112,450,000.00 USD | 1,210,000.00 USD | 691,780.00 USD | 1,580,000.00 USD |
| `1D` | `1.26` | 14,260,000.00 USD | 0.00 USD | 14,260,000.00 USD | 1,150,000.00 USD | 254,090.00 USD | 1,140,000.00 USD |
| `7D` | `1.26` | 108,970,000.00 USD | 0.00 USD | 108,970,000.00 USD | 1,980,000.00 USD | 1,450,000.00 USD | 1,520,000.00 USD |
| `1D` | `1.26` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 670,330.00 USD | 1,360,000.00 USD | 1,530,000.00 USD |
| `7D` | `1.26` | 104,020,000.00 USD | 0.00 USD | 104,020,000.00 USD | 3,500,000.00 USD | 1,970,000.00 USD | 3,520,000.00 USD |
| `1D` | `1.27` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 0.00 USD | 1,030,000.00 USD | 874,390.00 USD |
| `7D` | `1.27` | 95,020,000.00 USD | 0.00 USD | 95,020,000.00 USD | 4,470,000.00 USD | 1,960,000.00 USD | 6,550,000.00 USD |
| `1D` | `1.27` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 0.00 USD | 483,650.00 USD | 21,070.00 USD |
| `7D` | `1.27` | 82,050,000.00 USD | 0.00 USD | 82,050,000.00 USD | 2,890,000.00 USD | 1,380,000.00 USD | 4,100,000.00 USD |
| `1D` | `1.27` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 1,860,000.00 USD | 776,250.00 USD | 3,110,000.00 USD |
| `7D` | `1.27` | 73,670,000.00 USD | 0.00 USD | 73,670,000.00 USD | 3,090,000.00 USD | 2,160,000.00 USD | 6,460,000.00 USD |
| `1D` | `1.27` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.27` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 1,590,000.00 USD | 316,540.00 USD | 812,070.00 USD |
| `7D` | `1.27` | 61,960,000.00 USD | 0.00 USD | 61,960,000.00 USD | 4,570,000.00 USD | 2,590,000.00 USD | 7,120,000.00 USD |
| `1D` | `1.27` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 100,310.00 USD | 547,830.00 USD | 1,660,000.00 USD |
| `7D` | `1.27` | 47,670,000.00 USD | 0.00 USD | 47,670,000.00 USD | 4,600,000.00 USD | 1,720,000.00 USD | 11,540,000.00 USD |
| `1D` | `1.28` | 9,330,000.00 USD | 9,330,000.00 USD | 0.00 USD | 105,090.00 USD | 1,280,000.00 USD | 2,920,000.00 USD |
| `7D` | `1.28` | 29,820,000.00 USD | 0.00 USD | 29,820,000.00 USD | 4,130,000.00 USD | 2,410,000.00 USD | 5,940,000.00 USD |
| `1D` | `1.28` | 22,790,000.00 USD | 22,790,000.00 USD | 0.00 USD | 6,200,000.00 USD | 2,740,000.00 USD | 4,520,000.00 USD |
| `7D` | `1.28` | 17,330,000.00 USD | 0.00 USD | 17,330,000.00 USD | 7,720,000.00 USD | 2,860,000.00 USD | 5,150,000.00 USD |
| `1D` | `1.28` | 24,740,000.00 USD | 24,740,000.00 USD | 0.00 USD | 188,330.00 USD | 1,450,000.00 USD | 312,320.00 USD |
| `7D` | `1.28` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 0.00 USD | 1,420,000.00 USD | 84,070.00 USD |
| `7D` | `1.28` | 108,100.00 USD | 0.00 USD | 108,100.00 USD | 0.00 USD | 22,110.00 USD | 85,990.00 USD |
| `7D` | `1.28` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.28` | 24,900,000.00 USD | 24,900,000.00 USD | 0.00 USD | 0.00 USD | 161,530.00 USD | 0.00 USD |
| `7D` | `1.28` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 3,610,000.00 USD | 657,250.00 USD | 123,100.00 USD |
| `1D` | `1.29` | 25,370,000.00 USD | 25,370,000.00 USD | 0.00 USD | 143,950.00 USD | 327,360.00 USD | 0.00 USD |
| `7D` | `1.29` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 505,690.00 USD | 888,530.00 USD | 8,110.00 USD |
| `1D` | `1.29` | 25,860,000.00 USD | 25,860,000.00 USD | 0.00 USD | 382,250.00 USD | 100,470.00 USD | 8,840.00 USD |
| `7D` | `1.29` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 440,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.29` | 25,880,000.00 USD | 25,880,000.00 USD | 0.00 USD | 18,290.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.29` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 472,370.00 USD |
| `1D` | `1.29` | 27,570,000.00 USD | 27,570,000.00 USD | 0.00 USD | 307,350.00 USD | 0.00 USD | 1,380,000.00 USD |
| `7D` | `1.29` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 648,390.00 USD |
| `1D` | `1.29` | 30,770,000.00 USD | 30,770,000.00 USD | 0.00 USD | 775,760.00 USD | 111,560.00 USD | 2,310,000.00 USD |
| `7D` | `1.29` | 11,170,000.00 USD | 11,170,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 1,680,000.00 USD |
| `1D` | `1.30` | 34,960,000.00 USD | 34,960,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,120,000.00 USD | 1,960,000.00 USD |
| `7D` | `1.30` | 16,460,000.00 USD | 16,460,000.00 USD | 0.00 USD | 777,570.00 USD | 1,090,000.00 USD | 3,420,000.00 USD |
| `1D` | `1.30` | 35,590,000.00 USD | 35,590,000.00 USD | 0.00 USD | 344,680.00 USD | 422.50 USD | 288,210.00 USD |
| `7D` | `1.30` | 17,710,000.00 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `1.30` | 36,270,000.00 USD | 36,270,000.00 USD | 0.00 USD | 0.00 USD | 168,250.00 USD | 510,770.00 USD |
| `7D` | `1.30` | 18,680,000.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 38,450,000.00 USD | 38,450,000.00 USD | 0.00 USD | 602,010.00 USD | 910,970.00 USD | 659,740.00 USD |
| `7D` | `1.30` | 19,530,000.00 USD | 19,530,000.00 USD | 0.00 USD | 0.00 USD | 859,020.00 USD | 0.00 USD |
| `1D` | `1.30` | 38,860,000.00 USD | 38,860,000.00 USD | 0.00 USD | 188,510.00 USD | 98,100.00 USD | 127,330.00 USD |
| `7D` | `1.30` | 21,480,000.00 USD | 21,480,000.00 USD | 0.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD |
| `1D` | `1.31` | 39,990,000.00 USD | 39,990,000.00 USD | 0.00 USD | 493,480.00 USD | 319,570.00 USD | 320,170.00 USD |
| `7D` | `1.31` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD |
| `1D` | `1.31` | 42,500,000.00 USD | 42,500,000.00 USD | 0.00 USD | 767,340.00 USD | 211,190.00 USD | 1,530,000.00 USD |
| `7D` | `1.31` | 26,900,000.00 USD | 26,900,000.00 USD | 0.00 USD | 722,880.00 USD | 352,510.00 USD | 2,390,000.00 USD |
| `1D` | `1.31` | 45,000,000.00 USD | 45,000,000.00 USD | 0.00 USD | 890,710.00 USD | 396,100.00 USD | 1,210,000.00 USD |
| `7D` | `1.31` | 28,660,000.00 USD | 28,660,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | 415,410.00 USD |
| `1D` | `1.31` | 47,830,000.00 USD | 47,830,000.00 USD | 0.00 USD | 1,700,000.00 USD | 444,160.00 USD | 688,860.00 USD |
| `7D` | `1.31` | 32,410,000.00 USD | 32,410,000.00 USD | 0.00 USD | 79,920.00 USD | 747,120.00 USD | 2,930,000.00 USD |
| `1D` | `1.31` | 49,550,000.00 USD | 49,550,000.00 USD | 0.00 USD | 464,990.00 USD | 483,320.00 USD | 767,230.00 USD |
| `7D` | `1.31` | 33,560,000.00 USD | 33,560,000.00 USD | 0.00 USD | 515,950.00 USD | 149,950.00 USD | 485,150.00 USD |
| `1D` | `1.32` | 55,530,000.00 USD | 55,530,000.00 USD | 0.00 USD | 222,150.00 USD | 1,830,000.00 USD | 3,920,000.00 USD |
| `7D` | `1.32` | 37,740,000.00 USD | 37,740,000.00 USD | 0.00 USD | 44,360.00 USD | 1,750,000.00 USD | 2,380,000.00 USD |
| `1D` | `1.32` | 62,640,000.00 USD | 62,640,000.00 USD | 0.00 USD | 2,390,000.00 USD | 1,060,000.00 USD | 3,670,000.00 USD |
| `7D` | `1.32` | 42,590,000.00 USD | 42,590,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD |
| `1D` | `1.32` | 65,900,000.00 USD | 65,900,000.00 USD | 0.00 USD | 1,510,000.00 USD | 688,140.00 USD | 1,060,000.00 USD |
| `7D` | `1.32` | 44,290,000.00 USD | 44,290,000.00 USD | 0.00 USD | 823,190.00 USD | 430,400.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 70,180,000.00 USD | 70,180,000.00 USD | 0.00 USD | 1,730,000.00 USD | 842,630.00 USD | 1,710,000.00 USD |
| `7D` | `1.32` | 47,390,000.00 USD | 47,390,000.00 USD | 0.00 USD | 1,090,000.00 USD | 855,190.00 USD | 1,140,000.00 USD |
| `1D` | `1.32` | 73,180,000.00 USD | 73,180,000.00 USD | 0.00 USD | 1,770,000.00 USD | 259,620.00 USD | 968,180.00 USD |
| `7D` | `1.32` | 50,010,000.00 USD | 50,010,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 392,360.00 USD |
| `1D` | `1.33` | 75,470,000.00 USD | 75,470,000.00 USD | 0.00 USD | 687,000.00 USD | 308,840.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 51,810,000.00 USD | 51,810,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 77,660,000.00 USD | 77,660,000.00 USD | 0.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD |
| `7D` | `1.33` | 52,870,000.00 USD | 52,870,000.00 USD | 0.00 USD | 135,420.00 USD | 15,840.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 80,100,000.00 USD | 80,100,000.00 USD | 0.00 USD | 871,400.00 USD | 283,020.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 54,480,000.00 USD | 54,480,000.00 USD | 0.00 USD | 548,610.00 USD | 138,580.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 82,360,000.00 USD | 82,360,000.00 USD | 0.00 USD | 465,720.00 USD | 276,750.00 USD | 1,520,000.00 USD |
| `7D` | `1.33` | 56,890,000.00 USD | 56,890,000.00 USD | 0.00 USD | 809,950.00 USD | 236,880.00 USD | 1,360,000.00 USD |
| `1D` | `1.33` | 84,690,000.00 USD | 84,690,000.00 USD | 0.00 USD | 1,120,000.00 USD | 226,040.00 USD | 985,030.00 USD |
| `7D` | `1.33` | 58,560,000.00 USD | 58,560,000.00 USD | 0.00 USD | 450,460.00 USD | 178,580.00 USD | 1,040,000.00 USD |
| `1D` | `1.34` | 87,130,000.00 USD | 87,130,000.00 USD | 0.00 USD | 928,470.00 USD | 334,030.00 USD | 1,180,000.00 USD |
| `7D` | `1.34` | 60,100,000.00 USD | 60,100,000.00 USD | 0.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 89,810,000.00 USD | 89,810,000.00 USD | 0.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,050,000.00 USD |
| `7D` | `1.34` | 62,540,000.00 USD | 62,540,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 93,050,000.00 USD | 93,050,000.00 USD | 0.00 USD | 1,470,000.00 USD | 549,090.00 USD | 1,230,000.00 USD |
| `7D` | `1.34` | 64,410,000.00 USD | 64,410,000.00 USD | 0.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD |
| `1D` | `1.34` | 96,770,000.00 USD | 96,770,000.00 USD | 0.00 USD | 1,630,000.00 USD | 878,740.00 USD | 1,200,000.00 USD |
| `7D` | `1.34` | 70,330,000.00 USD | 70,330,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,880,000.00 USD | 665,920.00 USD |
| `1D` | `1.34` | 100,890,000.00 USD | 100,890,000.00 USD | 0.00 USD | 2,250,000.00 USD | 696,110.00 USD | 1,170,000.00 USD |
| `7D` | `1.34` | 77,720,000.00 USD | 77,720,000.00 USD | 0.00 USD | 2,030,000.00 USD | 2,210,000.00 USD | 3,140,000.00 USD |
| `1D` | `1.35` | 102,340,000.00 USD | 102,340,000.00 USD | 0.00 USD | 498,430.00 USD | 331,800.00 USD | 623,380.00 USD |
| `7D` | `1.35` | 88,470,000.00 USD | 88,470,000.00 USD | 0.00 USD | 4,040,000.00 USD | 1,900,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 103,600,000.00 USD | 103,600,000.00 USD | 0.00 USD | 481,670.00 USD | 124,160.00 USD | 655,290.00 USD |
| `7D` | `1.35` | 97,310,000.00 USD | 97,310,000.00 USD | 0.00 USD | 3,160,000.00 USD | 2,040,000.00 USD | 3,640,000.00 USD |
| `1D` | `1.35` | 105,370,000.00 USD | 105,370,000.00 USD | 0.00 USD | 771,840.00 USD | 265,500.00 USD | 729,530.00 USD |
| `7D` | `1.35` | 106,510,000.00 USD | 106,510,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,760,000.00 USD | 3,160,000.00 USD |
| `1D` | `1.35` | 106,700,000.00 USD | 106,700,000.00 USD | 0.00 USD | 558,120.00 USD | 208,670.00 USD | 565,330.00 USD |
| `7D` | `1.35` | 115,770,000.00 USD | 115,770,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,390,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 108,560,000.00 USD | 108,560,000.00 USD | 0.00 USD | 805,600.00 USD | 299,340.00 USD | 757,810.00 USD |
| `7D` | `1.35` | 123,310,000.00 USD | 123,310,000.00 USD | 0.00 USD | 2,320,000.00 USD | 886,190.00 USD | 4,330,000.00 USD |
| `1D` | `1.36` | 109,940,000.00 USD | 109,940,000.00 USD | 0.00 USD | 565,230.00 USD | 199,730.00 USD | 611,840.00 USD |
| `7D` | `1.36` | 130,470,000.00 USD | 130,470,000.00 USD | 0.00 USD | 2,820,000.00 USD | 1,060,000.00 USD | 3,290,000.00 USD |
| `1D` | `1.36` | 111,240,000.00 USD | 111,240,000.00 USD | 0.00 USD | 805,530.00 USD | 76,930.00 USD | 416,300.00 USD |
| `7D` | `1.36` | 133,000,000.00 USD | 133,000,000.00 USD | 0.00 USD | 1,040,000.00 USD | 639,580.00 USD | 849,400.00 USD |
| `1D` | `1.36` | 111,820,000.00 USD | 111,820,000.00 USD | 0.00 USD | 266,880.00 USD | 124,380.00 USD | 188,040.00 USD |
| `7D` | `1.36` | 136,070,000.00 USD | 136,070,000.00 USD | 0.00 USD | 1,430,000.00 USD | 410,060.00 USD | 1,230,000.00 USD |
| `1D` | `1.36` | 112,470,000.00 USD | 112,470,000.00 USD | 0.00 USD | 228,020.00 USD | 103,400.00 USD | 317,870.00 USD |
| `7D` | `1.36` | 139,850,000.00 USD | 139,850,000.00 USD | 0.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD |
| `1D` | `1.36` | 112,740,000.00 USD | 112,740,000.00 USD | 0.00 USD | 80,160.00 USD | 44,030.00 USD | 150,610.00 USD |
| `7D` | `1.36` | 142,600,000.00 USD | 142,600,000.00 USD | 0.00 USD | 1,430,000.00 USD | 614,410.00 USD | 702,320.00 USD |
| `1D` | `1.37` | 112,920,000.00 USD | 112,920,000.00 USD | 0.00 USD | 53,740.00 USD | 0.00 USD | 124,610.00 USD |
| `7D` | `1.37` | 143,340,000.00 USD | 143,340,000.00 USD | 0.00 USD | 206,650.00 USD | 111,150.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 113,110,000.00 USD | 113,110,000.00 USD | 0.00 USD | 84,710.00 USD | 57,700.00 USD | 44,320.00 USD |
| `7D` | `1.37` | 144,450,000.00 USD | 144,450,000.00 USD | 0.00 USD | 544,160.00 USD | 181,820.00 USD | 389,280.00 USD |
| `1D` | `1.37` | 113,280,000.00 USD | 113,280,000.00 USD | 0.00 USD | 38,340.00 USD | 25,940.00 USD | 110,310.00 USD |
| `7D` | `1.37` | 146,170,000.00 USD | 146,170,000.00 USD | 0.00 USD | 477,130.00 USD | 362,580.00 USD | 883,840.00 USD |
| `1D` | `1.37` | 113,420,000.00 USD | 113,420,000.00 USD | 0.00 USD | 3,890.00 USD | 41,470.00 USD | 93,830.00 USD |
| `7D` | `1.37` | 148,330,000.00 USD | 148,330,000.00 USD | 0.00 USD | 743,900.00 USD | 285,210.00 USD | 1,120,000.00 USD |
| `1D` | `1.37` | 113,560,000.00 USD | 113,560,000.00 USD | 0.00 USD | 74,330.00 USD | 258.33 USD | 66,850.00 USD |
| `7D` | `1.37` | 150,440,000.00 USD | 150,440,000.00 USD | 0.00 USD | 737,410.00 USD | 437,690.00 USD | 940,380.00 USD |
| `1D` | `1.38` | 113,820,000.00 USD | 113,820,000.00 USD | 0.00 USD | 102,720.00 USD | 32,630.00 USD | 122,400.00 USD |
| `7D` | `1.38` | 152,110,000.00 USD | 152,110,000.00 USD | 0.00 USD | 450,750.00 USD | 380,930.00 USD | 841,020.00 USD |
| `1D` | `1.38` | 114,320,000.00 USD | 114,320,000.00 USD | 0.00 USD | 231,710.00 USD | 71,960.00 USD | 200,640.00 USD |
| `7D` | `1.38` | 153,670,000.00 USD | 153,670,000.00 USD | 0.00 USD | 878,240.00 USD | 363,870.00 USD | 308,370.00 USD |
| `1D` | `1.38` | 114,890,000.00 USD | 114,890,000.00 USD | 0.00 USD | 314,100.00 USD | 98,360.00 USD | 149,980.00 USD |
| `7D` | `1.38` | 155,710,000.00 USD | 155,710,000.00 USD | 0.00 USD | 506,860.00 USD | 199,720.00 USD | 1,340,000.00 USD |
| `1D` | `1.38` | 115,140,000.00 USD | 115,140,000.00 USD | 0.00 USD | 106,800.00 USD | 53,840.00 USD | 92,660.00 USD |
| `7D` | `1.38` | 157,980,000.00 USD | 157,980,000.00 USD | 0.00 USD | 841,840.00 USD | 445,210.00 USD | 985,800.00 USD |
| `1D` | `1.38` | 115,550,000.00 USD | 115,550,000.00 USD | 0.00 USD | 337,160.00 USD | 17,520.00 USD | 52,070.00 USD |
| `7D` | `1.38` | 158,680,000.00 USD | 158,680,000.00 USD | 0.00 USD | 403,730.00 USD | 160,810.00 USD | 129,320.00 USD |
| `1D` | `1.39` | 115,620,000.00 USD | 115,620,000.00 USD | 0.00 USD | 0.00 USD | 38,600.00 USD | 35,540.00 USD |
| `7D` | `1.39` | 159,600,000.00 USD | 159,600,000.00 USD | 0.00 USD | 377,810.00 USD | 134,820.00 USD | 406,090.00 USD |
| `1D` | `1.39` | 115,620,000.00 USD | 115,620,000.00 USD | 0.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.39` | 160,460,000.00 USD | 160,460,000.00 USD | 0.00 USD | 384,080.00 USD | 263,660.00 USD | 218,620.00 USD |
| `1D` | `1.39` | 115,690,000.00 USD | 115,690,000.00 USD | 0.00 USD | 0.00 USD | 8,790.00 USD | 59,730.00 USD |
| `7D` | `1.39` | 161,200,000.00 USD | 161,200,000.00 USD | 0.00 USD | 497,500.00 USD | 118,700.00 USD | 118,070.00 USD |
| `1D` | `1.39` | 115,700,000.00 USD | 115,700,000.00 USD | 0.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.39` | 161,520,000.00 USD | 161,520,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.39` | 115,750,000.00 USD | 115,750,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 31,230.00 USD |
| `7D` | `1.39` | 161,580,000.00 USD | 161,580,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 115,750,000.00 USD | 115,750,000.00 USD | 0.00 USD | 0.00 USD | 304.00 USD | 0.00 USD |
| `7D` | `1.40` | 161,680,000.00 USD | 161,680,000.00 USD | 0.00 USD | 82,090.00 USD | 0.00 USD | 11,130.00 USD |
| `1D` | `1.40` | 115,750,000.00 USD | 115,750,000.00 USD | 0.00 USD | 5,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.40` | 161,690,000.00 USD | 161,690,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 161,750,000.00 USD | 161,750,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 161,830,000.00 USD | 161,830,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `1D` | `1.40` | 115,770,000.00 USD | 115,770,000.00 USD | 0.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.40` | 162,120,000.00 USD | 162,120,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 162,280,000.00 USD | 162,280,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.41` | 115,840,000.00 USD | 115,840,000.00 USD | 0.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.41` | 162,440,000.00 USD | 162,440,000.00 USD | 0.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.41` | 116,220,000.00 USD | 116,220,000.00 USD | 0.00 USD | 73,200.00 USD | 42,240.00 USD | 263,680.00 USD |
| `7D` | `1.41` | 163,170,000.00 USD | 163,170,000.00 USD | 0.00 USD | 139,270.00 USD | 107,710.00 USD | 482,250.00 USD |
| `1D` | `1.41` | 116,340,000.00 USD | 116,340,000.00 USD | 0.00 USD | 20,480.00 USD | 21,680.00 USD | 82,910.00 USD |
| `7D` | `1.41` | 163,400,000.00 USD | 163,400,000.00 USD | 0.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.41` | 116,350,000.00 USD | 116,350,000.00 USD | 0.00 USD | 4,630.00 USD | 336.57 USD | 204.46 USD |
| `7D` | `1.41` | 163,700,000.00 USD | 163,700,000.00 USD | 0.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD |
| `1D` | `1.42` | 116,510,000.00 USD | 116,510,000.00 USD | 0.00 USD | 61,830.00 USD | 27,040.00 USD | 78,120.00 USD |
| `7D` | `1.42` | 164,260,000.00 USD | 164,260,000.00 USD | 0.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD |
| `1D` | `1.42` | 116,890,000.00 USD | 116,890,000.00 USD | 0.00 USD | 196,530.00 USD | 76,020.00 USD | 107,810.00 USD |
| `7D` | `1.42` | 165,000,000.00 USD | 165,000,000.00 USD | 0.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD |
| `1D` | `1.42` | 117,630,000.00 USD | 117,630,000.00 USD | 0.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.42` | 166,050,000.00 USD | 166,050,000.00 USD | 0.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD |
| `1D` | `1.42` | 118,060,000.00 USD | 118,060,000.00 USD | 0.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.42` | 167,380,000.00 USD | 167,380,000.00 USD | 0.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD |
| `1D` | `1.42` | 118,150,000.00 USD | 118,150,000.00 USD | 0.00 USD | 9,670.00 USD | 55,100.00 USD | 21,210.00 USD |
| `7D` | `1.42` | 167,580,000.00 USD | 167,580,000.00 USD | 0.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD |
| `1D` | `1.43` | 118,360,000.00 USD | 118,360,000.00 USD | 0.00 USD | 99,870.00 USD | 35,450.00 USD | 73,570.00 USD |
| `7D` | `1.43` | 168,340,000.00 USD | 168,340,000.00 USD | 0.00 USD | 151,730.00 USD | 92,020.00 USD | 521,950.00 USD |
| `7D` | `1.43` | 169,410,000.00 USD | 169,410,000.00 USD | 0.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `7D` | `1.43` | 171,440,000.00 USD | 171,440,000.00 USD | 0.00 USD | 511,610.00 USD | 293,790.00 USD | 1,220,000.00 USD |
| `7D` | `1.43` | 172,290,000.00 USD | 172,290,000.00 USD | 0.00 USD | 335,720.00 USD | 94,140.00 USD | 421,650.00 USD |
| `7D` | `1.43` | 173,180,000.00 USD | 173,180,000.00 USD | 0.00 USD | 374,750.00 USD | 46,230.00 USD | 467,690.00 USD |
| `7D` | `1.44` | 173,210,000.00 USD | 173,210,000.00 USD | 0.00 USD | 6,560.00 USD | 12,030.00 USD | 11,180.00 USD |
| `7D` | `1.44` | 173,840,000.00 USD | 173,840,000.00 USD | 0.00 USD | 175,290.00 USD | 83,590.00 USD | 366,410.00 USD |
| `7D` | `1.44` | 174,260,000.00 USD | 174,260,000.00 USD | 0.00 USD | 85,020.00 USD | 74,230.00 USD | 261,710.00 USD |
| `7D` | `1.44` | 174,870,000.00 USD | 174,870,000.00 USD | 0.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD |
| `7D` | `1.44` | 175,110,000.00 USD | 175,110,000.00 USD | 0.00 USD | 78,320.00 USD | 46,380.00 USD | 116,120.00 USD |
| `7D` | `1.45` | 175,210,000.00 USD | 175,210,000.00 USD | 0.00 USD | 50,420.00 USD | 39,100.00 USD | 8,750.00 USD |
| `7D` | `1.45` | 175,580,000.00 USD | 175,580,000.00 USD | 0.00 USD | 69,200.00 USD | 26,800.00 USD | 278,000.00 USD |
| `7D` | `1.45` | 175,760,000.00 USD | 175,760,000.00 USD | 0.00 USD | 27,260.00 USD | 84,650.00 USD | 68,850.00 USD |
| `7D` | `1.45` | 176,670,000.00 USD | 176,670,000.00 USD | 0.00 USD | 216,330.00 USD | 94,590.00 USD | 598,610.00 USD |
| `7D` | `1.45` | 177,200,000.00 USD | 177,200,000.00 USD | 0.00 USD | 176,550.00 USD | 81,140.00 USD | 274,660.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.95B` | Total OI Tokens: `2,332,207,633.8 XRP`
  * 1h OI Change: `-1.38%` | 4h OI Change: `-3.07%` | 24h OI Change: `-1.16%`
  * Exchange Breakdown: Binance=`486.57M` | Bybit=`325.00M` | OKX=`97.34M` | Hyperliquid=`227.06M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `46.38K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0063%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0024%` | **USDT KuCoin** | `0.0082%` |
| **USDT MEXC** | `0.0063%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0015%` | **USDT Bitget** | `0.0035%` |
| **CoinM Binance** | `0.0093%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `31.10%` | `68.90%` | `0.45` | 105,520,000.00 USD |
| `15M` | `Binance` | `34.32%` | `65.68%` | `0.52` | 36,890,000.00 USD |
| `15M` | `OKX` | `25.15%` | `74.85%` | `0.34` | 16,650,000.00 USD |
| `15M` | `Bybit` | `26.58%` | `73.42%` | `0.36` | 14,140,000.00 USD |
| `15M` | `KuCoin` | `38.61%` | `61.39%` | `0.63` | 1,510,000.00 USD |
| `15M` | `Gate` | `34.24%` | `65.76%` | `0.52` | 3,480,000.00 USD |
| `15M` | `Bitget` | `30.15%` | `69.85%` | `0.43` | 7,720,000.00 USD |
| `15M` | `BingX` | `24.31%` | `75.69%` | `0.32` | 1,680,000.00 USD |
| `15M` | `MEXC` | `26.27%` | `73.73%` | `0.36` | 9,970,000.00 USD |
| `15M` | `Bitunix` | `27.62%` | `72.38%` | `0.38` | 5,140,000.00 USD |
| `15M` | `Hyperliquid` | `23.18%` | `76.82%` | `0.30` | 3,230,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `27.5%` | `72.5%` | `0.38` | 319,540.00 USD |
| `15M` | `Crypto.com` | `48.04%` | `51.96%` | `0.92` | 194,130.00 USD |
| `15M` | `WhiteBIT` | `97.52%` | `2.48%` | `39.32` | 2,090,000.00 USD |
| `15M` | `HTX` | `29.72%` | `70.28%` | `0.42` | 111,410.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `10.12%` | `89.88%` | `0.11` | 825,600.00 USD |
| `15M` | `Aster` | `35.19%` | `64.81%` | `0.54` | 1,450,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `53.03%` | `46.97%` | `1.13` | 152,370.00 USD |
| `15M` | `Whale Positions` | `34.32%` | `65.68%` | `0.52` | 36,890,000.00 USD |
| `15M` | `Global Accounts` | `31.10%` | `68.90%` | `0.45` | 105,520,000.00 USD |
| `1H` | `XRP` | `39.67%` | `60.33%` | `0.66` | 152,570,000.00 USD |
| `1H` | `Binance` | `38.72%` | `61.28%` | `0.63` | 48,350,000.00 USD |
| `1H` | `OKX` | `34.7%` | `65.3%` | `0.53` | 21,320,000.00 USD |
| `1H` | `Bybit` | `33.88%` | `66.12%` | `0.51` | 20,770,000.00 USD |
| `1H` | `KuCoin` | `39.1%` | `60.9%` | `0.64` | 1,640,000.00 USD |
| `1H` | `Gate` | `44.69%` | `55.31%` | `0.81` | 7,280,000.00 USD |
| `1H` | `Bitget` | `37.06%` | `62.94%` | `0.59` | 9,100,000.00 USD |
| `1H` | `BingX` | `18.05%` | `81.95%` | `0.22` | 5,100,000.00 USD |
| `1H` | `MEXC` | `36.32%` | `63.68%` | `0.57` | 15,670,000.00 USD |
| `1H` | `Bitunix` | `38.31%` | `61.69%` | `0.62` | 8,910,000.00 USD |
| `1H` | `Hyperliquid` | `33.84%` | `66.16%` | `0.51` | 3,420,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.81%` | `48.19%` | `1.08` | 478,600.00 USD |
| `1H` | `Crypto.com` | `54.86%` | `45.14%` | `1.22` | 281,830.00 USD |
| `1H` | `WhiteBIT` | `99.37%` | `0.63%` | `157.73` | 7,490,000.00 USD |
| `1H` | `HTX` | `30.91%` | `69.09%` | `0.45` | 120,440.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `30.49%` | `69.51%` | `0.44` | 605,840.00 USD |
| `1H` | `Aster` | `42.29%` | `57.71%` | `0.73` | 1,820,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `44.17%` | `55.83%` | `0.79` | 226,020.00 USD |
| `1H` | `Whale Positions` | `38.72%` | `61.28%` | `0.63` | 48,350,000.00 USD |
| `1H` | `Global Accounts` | `39.67%` | `60.33%` | `0.66` | 152,570,000.00 USD |
| `4H` | `XRP` | `42.41%` | `57.59%` | `0.74` | 615,440,000.00 USD |
| `4H` | `Binance` | `43.46%` | `56.54%` | `0.77` | 201,920,000.00 USD |
| `4H` | `OKX` | `39.03%` | `60.97%` | `0.64` | 69,180,000.00 USD |
| `4H` | `Bybit` | `39.6%` | `60.4%` | `0.66` | 87,140,000.00 USD |
| `4H` | `KuCoin` | `43.37%` | `56.63%` | `0.77` | 5,880,000.00 USD |
| `4H` | `Gate` | `45.33%` | `54.67%` | `0.83` | 26,940,000.00 USD |
| `4H` | `Bitget` | `40.98%` | `59.02%` | `0.69` | 43,950,000.00 USD |
| `4H` | `BingX` | `28.82%` | `71.18%` | `0.40` | 16,630,000.00 USD |
| `4H` | `MEXC` | `45.06%` | `54.94%` | `0.82` | 74,670,000.00 USD |
| `4H` | `Bitunix` | `43.31%` | `56.69%` | `0.76` | 35,800,000.00 USD |
| `4H` | `Hyperliquid` | `33.07%` | `66.93%` | `0.49` | 12,000,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `54.2%` | `45.8%` | `1.18` | 2,570,000.00 USD |
| `4H` | `Crypto.com` | `51.48%` | `48.52%` | `1.06` | 868,560.00 USD |
| `4H` | `WhiteBIT` | `55.71%` | `44.29%` | `1.26` | 25,760,000.00 USD |
| `4H` | `HTX` | `58.4%` | `41.6%` | `1.40` | 537,220.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `40.34%` | `59.66%` | `0.68` | 3,450,000.00 USD |
| `4H` | `Aster` | `38.36%` | `61.64%` | `0.62` | 7,410,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `46.19%` | `53.81%` | `0.86` | 721,650.00 USD |
| `4H` | `Whale Positions` | `43.46%` | `56.54%` | `0.77` | 201,920,000.00 USD |
| `4H` | `Global Accounts` | `42.41%` | `57.59%` | `0.74` | 615,440,000.00 USD |


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
| `5:00 UTC` | `1.28` | `1.28` | `1.28` | `1.29` | `1.28` | 6,927,404.76 USD | 2,828,471.62 USD | 4,098,933.15 USD | -1,270,461.53 USD | `-18.34%` | `7B / 15S` |

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
| `5m` | -2,060,000.00 USD | -13,150,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -3,350,000.00 USD | -12,770,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,820,000.00 USD | -12,810,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,420,000.00 USD | -12,660,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -8,690,000.00 USD | -28,300,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -14,390,000.00 USD | -42,400,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -7,440,000.00 USD | -36,460,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -10,840,000.00 USD | -38,650,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,900,000.00 USD | -36,590,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -34,450,000.00 USD | -102,170,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -82,000,000.00 USD | -95,580,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -560,270,000.00 USD | -1,200,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-2.06M` | 15m=`-3.35M` | 1h=`-2.42M` | 24h=`-34.45M`
* Futures Capital Netflows: 5m=`-13.15M` | 15m=`-12.77M` | 1h=`-12.66M` | 24h=`-102.17M`
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
  * `2026-10-30 00:58:24 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:29:24 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:29:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0137` pts)
  * +2.5R Take Profit: `1.32`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.30` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.31` (Risk Distance: `0.0137` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.29`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
