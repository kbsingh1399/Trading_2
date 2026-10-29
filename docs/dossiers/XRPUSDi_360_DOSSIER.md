# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-29 23:40:50 IST` (`2026-10-29 18:10:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.29` | **Live Ask Quote**: `1.29` | **Mid Price**: `1.29`
- **Spread Points**: `3.00` | **Spread BPS**: `23.19 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.29` | VWAP Z-Score: `-0.32` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0065` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.07` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.32` | Lower -3.00σ Band: `1.27`
  * Upper +2.51σ Band: `1.31` | Lower -2.51σ Band: `1.27`
  * Upper +2.01σ Band: `1.31` | Lower -2.01σ Band: `1.28`
  * Upper +2.00σ Band: `1.31` | Lower -2.00σ Band: `1.28`
  * Upper +1.28σ Band: `1.30` | Lower -1.28σ Band: `1.28`
  * Upper +1.00σ Band: `1.30` | Lower -1.00σ Band: `1.29`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.30` | EMA-20=`1.30` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.30` (Slope: `+0.0000`) | EMA-100=`1.30`
  * Institutional Anchors: EMA-144=`1.30` | EMA-200=`1.30` (Slope: `-0.0382`) | EMA-233=`1.30`
- **Range Boundaries**: 24H High=`1.34` | 24H Low=`1.28` | Weekly High=`1.34` | Weekly Low=`1.28`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.30` (Distance: `-0.39%`)
  * Point of Control (POC) = `1.29` (Distance: `+0.36%`)
  * Value Area Low (VAL) = `1.28` (Distance: `+0.75%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `1.29` - `1.30`
  * Optimal Trade Entry (OTE 0.705): `1.30`
  * Structural Invalidation Anchor (0.786): `1.30`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.29` | `1.29` | `1.29` | `1.29` | `1,392,231` | 1,797,743.56 USD | 432,144.76 USD | `+24.04%` | -25,490,391.24 USD | `+0.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.29` | `1.29` | `1.29` | `1.29` | `1,493,410` | 1,930,712.99 USD | 172,343.29 USD | `+8.93%` | -25,318,047.96 USD | `+0.39` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `1.29` | `1.29` | `1.29` | `1.29` | `109,576` | 141,742.30 USD | 9,133.31 USD | `+6.44%` | -25,308,914.65 USD | `+0.15` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.30` | `1.30` | `1.29` | `1.29` | `6,849,188` | 8,857,459.31 USD | -2,585,235.17 USD | `-29.19%` | -27,569,508.46 USD | `-1.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.29` | `1.29` | `1.29` | `1.29` | `9,162,870` | 11,824,590.46 USD | 1,740,091.12 USD | `+14.72%` | -25,829,417.34 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.29` | `1.29` | `1.29` | `1.29` | `1,724,351` | 2,229,537.00 USD | 279,817.64 USD | `+12.55%` | -25,549,599.70 USD | `+0.35` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.31` | `1.32` | `1.30` | `1.30` | `30,534,069` | 39,864,527.69 USD | -3,664,960.48 USD | `-9.19%` | -24,545,254.96 USD | `-0.63` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.30` | `1.30` | `1.29` | `1.29` | `27,238,695` | 35,241,786.93 USD | -1,210,810.88 USD | `-3.44%` | -25,756,065.84 USD | `+0.08` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `1.29` | `1.29` | `1.29` | `1.29` | `1,602,985` | 2,072,455.29 USD | 181,476.59 USD | `+8.76%` | -25,574,589.25 USD | `+0.47` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.29` | `1.29` | `59,375,749` | 77,178,769.91 USD | -4,694,294.76 USD | `-6.08%` | -29,196,469.90 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.33` | `1.33` | `1.29` | `1.29` | `112,558,954` | 146,533,666.97 USD | -23,231,128.88 USD | `-15.85%` | -23,206,069.15 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `60,938,672` | 78,900,359.45 USD | -1,841,235.66 USD | `-2.33%` | -25,047,304.81 USD | `+0.62` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -26,364,168.80 USD | `+0.55` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -24,502,175.14 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.29` | `1.29` | `59,375,749` | 77,178,769.91 USD | -4,694,294.76 USD | `-6.08%` | -29,196,469.90 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `ASK` | `1.29` | `12992.0000` | 16,824.64 USD | 20,399.86 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `1.29` | `2761.0000` | 3,575.22 USD | 3,575.22 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.29` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.29` | `0.00%` | `-` |
| `BID` | `1.29` | `25458.0000` | 32,963.02 USD | 32,963.02 USD | `8 orders` | `-0.00%` | `-` |
| `BID` | `1.29` | `8623.0000` | 11,164.20 USD | 44,127.22 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `1.29` | `25887.0000` | 33,513.31 USD | 77,640.53 USD | `7 orders` | `-0.02%` | `-` |
| `BID` | `1.29` | `75455.0000` | 97,676.50 USD | 175,317.02 USD | `9 orders` | `-0.03%` | `-` |
| `BID` | `1.29` | `51113.0000` | 66,160.67 USD | 241,477.69 USD | `7 orders` | `-0.03%` | `-` |
| `BID` | `1.29` | `33140.0000` | 42,893.10 USD | 284,370.79 USD | `7 orders` | `-0.04%` | `-` |
| `BID` | `1.29` | `83586.0000` | 108,177.00 USD | 392,547.79 USD | `8 orders` | `-0.05%` | `-` |
| `BID` | `1.29` | `56332.0000` | 72,899.24 USD | 465,447.04 USD | `8 orders` | `-0.06%` | `-` |
| `BID` | `1.29` | `117010.0000` | 151,410.94 USD | 616,857.98 USD | `12 orders` | `-0.07%` | `-` |
| `BID` | `1.29` | `75731.0000` | 97,988.34 USD | 714,846.32 USD | `15 orders` | `-0.07%` | `-` |
| `BID` | `1.29` | `75301.0000` | 97,424.43 USD | 812,270.75 USD | `12 orders` | `-0.08%` | `-` |
| `BID` | `1.29` | `154000.0000` | 199,229.80 USD | 1,011,500.55 USD | `12 orders` | `-0.09%` | `-` |
| `BID` | `1.29` | `56667.0000` | 73,304.43 USD | 1,084,804.98 USD | `12 orders` | `-0.10%` | `-` |
| `BID` | `1.29` | `46652.0000` | 60,344.36 USD | 1,145,149.34 USD | `9 orders` | `-0.10%` | `-` |
| `BID` | `1.29` | `311260.0000` | 402,583.68 USD | 1,547,733.03 USD | `15 orders` | `-0.11%` | `-` |
| `BID` | `1.29` | `355900.0000` | 460,285.47 USD | 2,008,018.50 USD | `11 orders` | `-0.12%` | `-` |
| `BID` | `1.29` | `85760.0000` | 110,904.83 USD | 2,118,923.33 USD | `7 orders` | `-0.13%` | `-` |
| `BID` | `1.29` | `22336.0000` | 28,882.68 USD | 2,147,806.01 USD | `9 orders` | `-0.14%` | `-` |
| `BID` | `1.29` | `37653.0000` | 48,685.33 USD | 2,196,491.34 USD | `8 orders` | `-0.14%` | `-` |
| `BID` | `1.29` | `312665.0000` | 404,244.58 USD | 2,600,735.92 USD | `11 orders` | `-0.15%` | `-` |
| `ASK` | `1.30` | `552049.0000` | 715,897.14 USD | 3,380,597.82 USD | `5 orders` | `+0.15%` | `-` |
| `ASK` | `1.30` | `152369.0000` | 197,576.88 USD | 2,664,700.67 USD | `8 orders` | `+0.14%` | `-` |
| `ASK` | `1.30` | `108608.0000` | 140,821.13 USD | 2,467,123.79 USD | `6 orders` | `+0.14%` | `-` |
| `ASK` | `1.30` | `331477.0000` | 429,759.93 USD | 2,326,302.66 USD | `6 orders` | `+0.13%` | `-` |
| `ASK` | `1.30` | `235566.0000` | 305,387.76 USD | 1,896,542.73 USD | `9 orders` | `+0.12%` | `-` |
| `ASK` | `1.30` | `286623.0000` | 371,549.39 USD | 1,591,154.96 USD | `11 orders` | `+0.11%` | `-` |
| `ASK` | `1.30` | `214346.0000` | 277,835.29 USD | 1,219,605.57 USD | `8 orders` | `+0.10%` | `-` |
| `ASK` | `1.30` | `83606.0000` | 108,361.74 USD | 941,770.28 USD | `5 orders` | `+0.10%` | `-` |
| `ASK` | `1.30` | `49204.0000` | 63,768.38 USD | 833,408.55 USD | `11 orders` | `+0.09%` | `-` |
| `ASK` | `1.30` | `119113.0000` | 154,358.54 USD | 769,640.16 USD | `6 orders` | `+0.08%` | `-` |
| `ASK` | `1.30` | `46213.0000` | 59,882.81 USD | 615,281.63 USD | `9 orders` | `+0.07%` | `-` |
| `ASK` | `1.30` | `101393.0000` | 131,374.91 USD | 555,398.82 USD | `14 orders` | `+0.07%` | `-` |
| `ASK` | `1.30` | `69493.0000` | 90,035.13 USD | 424,023.91 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `1.30` | `72169.0000` | 93,494.94 USD | 333,988.78 USD | `11 orders` | `+0.05%` | `-` |
| `ASK` | `1.30` | `30751.0000` | 39,834.85 USD | 240,493.84 USD | `12 orders` | `+0.04%` | `-` |
| `ASK` | `1.30` | `89415.0000` | 115,819.25 USD | 200,659.00 USD | `12 orders` | `+0.03%` | `-` |
| `ASK` | `1.30` | `34821.0000` | 45,100.16 USD | 84,839.75 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `1.30` | `14933.0000` | 19,339.73 USD | 39,739.59 USD | `10 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `26` | `0x31b1...1434` | `LONG` | 45,351,689.28 USD | `35,031,430.00` | `1.13` | `1.29` | `0.9612` | 5,772,806.01 USD | `+12.73%` | `10X Cross` |
| `89` | `0x5b5d...c060` | `SHORT` | 20,399,699.37 USD | `15,762,401.00` | `1.44` | `1.29` | `11.14` | 2,257,314.62 USD | `+11.07%` | `5X Cross` |
| `145` | `0x58f0...0d20` | `LONG` | 14,150,993.74 USD | `10,931,629.00` | `1.36` | `1.29` | `1.26` | -714,159.22 USD | `-5.05%` | `20X Cross` |
| `153` | `0xb83d...6e36` | `SHORT` | 13,656,641.21 USD | `10,555,450.00` | `1.50` | `1.29` | `13.65` | 2,165,928.43 USD | `+15.86%` | `5X Cross` |
| `435` | `0xca49...53c8` | `SHORT` | 5,355,718.48 USD | `4,138,886.00` | `1.44` | `1.29` | `4.36` | 597,604.25 USD | `+11.16%` | `20X Cross` |
| `453` | `0xfc27...9d9d` | `SHORT` | 5,123,732.75 USD | `3,959,608.00` | `1.31` | `1.29` | `4.90` | 81,474.13 USD | `+1.59%` | `20X Cross` |
| `504` | `0x610b...b613` | `LONG` | 4,584,094.15 USD | `3,543,946.00` | `1.44` | `1.29` | `0.6991` | -515,898.46 USD | `-11.25%` | `5X Cross` |
| `534` | `0xc30c...a4c9` | `SHORT` | 4,272,064.77 USD | `3,302,753.00` | `1.42` | `1.29` | `1.61` | 427,822.08 USD | `+10.01%` | `8X Cross` |
| `546` | `0xdd53...2b13` | `SHORT` | 4,191,136.60 USD | `3,238,900.00` | `1.44` | `1.29` | `18.60` | 469,252.34 USD | `+11.20%` | `3X Cross` |
| `592` | `0x9946...0852` | `SHORT` | 3,914,493.63 USD | `3,025,111.00` | `1.43` | `1.29` | `1.63` | 398,690.92 USD | `+10.18%` | `20X Cross` |
| `613` | `0xecb6...2b00` | `SHORT` | 3,820,229.41 USD | `2,953,437.00` | `1.31` | `1.29` | `10.97` | 40,265.99 USD | `+1.05%` | `10X Cross` |
| `685` | `0x9aa5...58af` | `SHORT` | 3,370,204.22 USD | `2,604,083.00` | `1.46` | `1.29` | `4.14` | 427,516.44 USD | `+12.69%` | `20X Cross` |
| `698` | `0xf48f...10fe` | `LONG` | 3,319,604.87 USD | `2,565,779.00` | `1.53` | `1.29` | `0.9127` | -605,035.86 USD | `-18.23%` | `4X Cross` |
| `714` | `0x023a...2355` | `SHORT` | 3,241,139.28 USD | `2,504,938.00` | `1.33` | `1.29` | `4.59` | 84,443.58 USD | `+2.61%` | `20X Cross` |
| `736` | `0x45d2...4029` | `SHORT` | 3,174,182.00 USD | `2,453,000.00` | `1.48` | `1.29` | `16.14` | 464,098.42 USD | `+14.62%` | `20X Cross` |
| `1003` | `0xc179...e0c8` | `SHORT` | 2,277,020.42 USD | `1,760,375.00` | `1.30` | `1.29` | `4.69` | 13,858.58 USD | `+0.61%` | `10X Cross` |
| `1072` | `0xeadc...9d55` | `LONG` | 2,096,999.55 USD | `1,619,805.00` | `1.21` | `1.29` | `0.000000` | 138,156.53 USD | `+6.59%` | `20X Cross` |
| `1073` | `0xfc66...ca06` | `SHORT` | 2,094,988.59 USD | `1,619,002.00` | `1.31` | `1.29` | `22.87` | 26,414.09 USD | `+1.26%` | `20X Cross` |
| `1138` | `0x94b2...599e` | `SHORT` | 1,994,585.04 USD | `1,540,696.00` | `1.36` | `1.29` | `1.83` | 105,881.41 USD | `+5.31%` | `20X Cross` |
| `1153` | `0xbcd4...0dd2` | `SHORT` | 1,978,816.64 USD | `1,529,461.00` | `1.31` | `1.29` | `2.19` | 25,727.96 USD | `+1.30%` | `20X Cross` |
| `1174` | `0x3fc5...c0c1` | `SHORT` | 1,955,939.67 USD | `1,511,779.00` | `1.52` | `1.29` | `2.63` | 335,674.93 USD | `+17.16%` | `20X Cross` |
| `1197` | `0x31ef...f715` | `LONG` | 1,909,491.06 USD | `1,475,080.00` | `1.49` | `1.29` | `1.04` | -289,774.34 USD | `-15.18%` | `3X Isolated` |
| `1251` | `0x7737...bf66` | `SHORT` | 1,829,873.08 USD | `1,413,466.00` | `1.41` | `1.29` | `14.26` | 168,995.56 USD | `+9.24%` | `10X Cross` |
| `1271` | `0xef96...9383` | `SHORT` | 1,799,257.21 USD | `1,390,999.00` | `1.34` | `1.29` | `3.96` | 64,528.01 USD | `+3.59%` | `20X Cross` |
| `1346` | `0xee2b...d67e` | `LONG` | 1,690,200.87 USD | `1,306,284.00` | `1.55` | `1.29` | `0.2391` | -340,454.03 USD | `-20.14%` | `4X Cross` |
| `1396` | `0x215d...f80a` | `LONG` | 1,620,049.79 USD | `1,251,777.00` | `1.32` | `1.29` | `1.19` | -34,404.43 USD | `-2.12%` | `14X Cross` |
| `1447` | `0x123d...3bff` | `LONG` | 1,572,392.66 USD | `1,215,329.00` | `1.35` | `1.29` | `0.000000` | -64,676.56 USD | `-4.11%` | `10X Cross` |
| `1492` | `0x95da...2328` | `LONG` | 1,516,917.11 USD | `1,171,817.00` | `1.37` | `1.29` | `0.000000` | -84,858.88 USD | `-5.59%` | `5X Cross` |
| `1501` | `0xdf95...7d72` | `SHORT` | 1,501,168.11 USD | `1,160,099.00` | `1.37` | `1.29` | `32.83` | 92,170.62 USD | `+6.14%` | `20X Cross` |
| `1557` | `0x5fa3...35b7` | `SHORT` | 1,432,738.93 USD | `1,107,046.00` | `1.31` | `1.29` | `3.05` | 16,903.15 USD | `+1.18%` | `20X Cross` |
| `1651` | `0xb1ce...681b` | `LONG` | 1,322,162.62 USD | `1,021,764.00` | `1.49` | `1.29` | `1.16` | -201,893.88 USD | `-15.27%` | `4X Isolated` |
| `1657` | `0x4537...8732` | `SHORT` | 1,318,628.02 USD | `1,018,875.00` | `1.32` | `1.29` | `2.24` | 22,188.87 USD | `+1.68%` | `10X Cross` |
| `1752` | `0x3c36...461a` | `LONG` | 1,216,520.00 USD | `940,051.00` | `1.30` | `1.29` | `1.06` | -2,560.61 USD | `-0.21%` | `10X Cross` |
| `1972` | `0xbfc7...80b4` | `SHORT` | 1,035,360.00 USD | `800,000.00` | `1.48` | `1.29` | `6.76` | 148,094.65 USD | `+14.30%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.27` | 30.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 27.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 16,159.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 16.16K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 12.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 635.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.64K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 82.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.08K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 40.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 523.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.52K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 424.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.42K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 139.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.14K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,369.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.37K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 528.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.53K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 34.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 199.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 3,439.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.44K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 953.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.95K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 10.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 23,519.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 23.52K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 204.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 198.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 57.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.06K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 24.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,327.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.33K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 116.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.12K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 739.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.74K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 4,381.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.38K USD at 1.2700 USD [API] | `2026-10-17 21:38:08` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 107.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.11K USD at 1.3310 USD [API] | `2026-10-14 14:37:05` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 25.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.3310 USD [API] | `2026-10-14 14:37:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 2,500.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.50K USD at 1.3310 USD [API] | `2026-10-14 14:37:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 89.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.3310 USD [API] | `2026-10-14 14:37:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 246.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.25K USD at 1.3310 USD [API] | `2026-10-14 14:37:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 25.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.3340 USD [API] | `2026-10-14 14:31:12` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 33,375.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 33.38K USD at 1.3350 USD [API] | `2026-10-14 14:28:24` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,345.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.35K USD at 1.3288 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,266.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.27K USD at 1.3288 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,371.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.37K USD at 1.3289 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,939.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.94K USD at 1.3290 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,355.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.36K USD at 1.3290 USD [API] | `2026-10-27 21:37:26` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,633.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.63K USD at 1.3281 USD [API] | `2026-10-27 21:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 12,869.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 12.87K USD at 1.3253 USD [API] | `2026-10-27 21:41:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,391.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.39K USD at 1.3253 USD [API] | `2026-10-27 21:41:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,362.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.36K USD at 1.3256 USD [API] | `2026-10-27 21:42:55` |
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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.32` (Vol: 2,200,000.00 USD, Dist: `+2.36%`) | Long MP=`1.28` (Vol: 2,900,000.00 USD, Dist: `--1.07%`)
  * 48H Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+4.51%`) | Long MP=`1.28` (Vol: 2,900,000.00 USD, Dist: `--1.07%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,600,000.00 USD, Dist: `+4.51%`) | Long MP=`1.28` (Vol: 3,700,000.00 USD, Dist: `--0.60%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,200,000.00 USD, Dist: `+4.59%`) | Long MP=`1.28` (Vol: 4,400,000.00 USD, Dist: `--0.65%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2650` | 4,330.00 USD | 74,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 379.50 USD | 74,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 1,500.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 1,060.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 5,060.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 1,010.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 1,140.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 1,900.00 USD | 74,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 9,820.00 USD | 74,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 1,250.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 1,320.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 2,620.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 151,310.00 USD | 74,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 15,910.00 USD | 74,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 376.27 USD | 74,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 2,680.00 USD | 74,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 989.06 USD | 74,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 3,100.00 USD | 74,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 30,430.00 USD | 74,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 3,140.00 USD | 74,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 6,750.00 USD | 74,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 2,030.00 USD | 74,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 50,280.00 USD | 74,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 10,910.00 USD | 74,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 2,730.00 USD | 74,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 374.03 USD | 74,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 6,200.00 USD | 74,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 889.20 USD | 74,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 5,760.00 USD | 74,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 32,400.00 USD | 74,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 50,190.00 USD | 74,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 7,150.00 USD | 74,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 8,030.00 USD | 74,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 140,570.00 USD | 74,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 31,770.00 USD | 74,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 28,620.00 USD | 74,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 2,450,000.00 USD | 74,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 11,360.00 USD | 71,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 25,010.00 USD | 71,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 67,440.00 USD | 71,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 217,680.00 USD | 71,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 23,650.00 USD | 71,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 52,420.00 USD | 71,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 563,960.00 USD | 71,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 2,190.00 USD | 70,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 29,790.00 USD | 70,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 40,330.00 USD | 70,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 11,580.00 USD | 70,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 22,350.00 USD | 70,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 22,650.00 USD | 70,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 11,200.00 USD | 70,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 44,490.00 USD | 70,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 70,540.00 USD | 70,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 165,960.00 USD | 70,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 28,530.00 USD | 70,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 128,340.00 USD | 70,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 357,260.00 USD | 70,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 2,390,000.00 USD | 69,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 151,820.00 USD | 67,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 26,030.00 USD | 67,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 647,340.00 USD | 67,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 86,480.00 USD | 66,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 79,680.00 USD | 66,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 238,350.00 USD | 66,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 34,010,000.00 USD | 66,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 601,530.00 USD | 32,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 451,370.00 USD | 31,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 109,310.00 USD | 30,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 472,770.00 USD | 30,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 155,310.00 USD | 30,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 136,000.00 USD | 30,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,110,000.00 USD | 30,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 88,220.00 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,120,000.00 USD | 27,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 390,040.00 USD | 26,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 455,900.00 USD | 26,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 744,660.00 USD | 25,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 124,020.00 USD | 25,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 107,230.00 USD | 25,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 874,470.00 USD | 24,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 260,740.00 USD | 24,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 86,630.00 USD | 23,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 366,370.00 USD | 23,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.16` | 221,340,000.00 USD | 221,340,000.00 USD | 100,770.00 USD | 64,860.00 USD | 127,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 108,390.00 USD | 23,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 77,730,000.00 USD | 77,730,000.00 USD | 29,120.00 USD | 9,250.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 221,040,000.00 USD | 221,040,000.00 USD | 173,190.00 USD | 99,350.00 USD | 396,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 77,690,000.00 USD | 77,690,000.00 USD | 137,370.00 USD | 26,520.00 USD | 70,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 220,380,000.00 USD | 220,380,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 77,450,000.00 USD | 77,450,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 219,950,000.00 USD | 219,950,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 76,830,000.00 USD | 76,830,000.00 USD | 292,830.00 USD | 121,550.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 218,920,000.00 USD | 218,920,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 76,230,000.00 USD | 76,230,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 217,550,000.00 USD | 217,550,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,680,000.00 USD | 23,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 76,010,000.00 USD | 76,010,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 216,920,000.00 USD | 216,920,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 75,700,000.00 USD | 75,700,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 215,540,000.00 USD | 215,540,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 75,540,000.00 USD | 75,540,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 214,040,000.00 USD | 214,040,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 75,370,000.00 USD | 75,370,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 212,650,000.00 USD | 212,650,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 75,110,000.00 USD | 75,110,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 211,850,000.00 USD | 211,850,000.00 USD | 290,470.00 USD | 92,530.00 USD | 499,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 806,220.00 USD | 21,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 74,770,000.00 USD | 74,770,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 210,970,000.00 USD | 210,970,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 74,640,000.00 USD | 74,640,000.00 USD | 77,850.00 USD | 41,360.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 210,510,000.00 USD | 210,510,000.00 USD | 299,590.00 USD | 131,210.00 USD | 459,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 74,480,000.00 USD | 74,480,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 209,620,000.00 USD | 209,620,000.00 USD | 69,670.00 USD | 152,290.00 USD | 286,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 74,440,000.00 USD | 74,440,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 209,110,000.00 USD | 209,110,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 74,330,000.00 USD | 74,330,000.00 USD | 50,770.00 USD | 14,400.00 USD | 27,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 208,980,000.00 USD | 208,980,000.00 USD | 81,610.00 USD | 98,170.00 USD | 428,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 1,650,000.00 USD | 20,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 74,240,000.00 USD | 74,240,000.00 USD | 26,300.00 USD | 37,580.00 USD | 83,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 208,370,000.00 USD | 208,370,000.00 USD | 190,550.00 USD | 38,510.00 USD | 383,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 74,090,000.00 USD | 74,090,000.00 USD | 60,820.00 USD | 103.33 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 207,760,000.00 USD | 207,760,000.00 USD | 186,430.00 USD | 128,180.00 USD | 350,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 74,020,000.00 USD | 74,020,000.00 USD | 36,460.00 USD | 10,480.00 USD | 75,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 207,090,000.00 USD | 207,090,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 73,900,000.00 USD | 73,900,000.00 USD | 67,440.00 USD | 29,830.00 USD | 130,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 206,630,000.00 USD | 206,630,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 73,670,000.00 USD | 73,670,000.00 USD | 106,940.00 USD | 33,950.00 USD | 32,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 205,970,000.00 USD | 205,970,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 477,200.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 73,490,000.00 USD | 73,490,000.00 USD | 134,160.00 USD | 6,620.00 USD | 61,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 205,260,000.00 USD | 205,260,000.00 USD | 5,350.00 USD | 93,870.00 USD | 187,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 73,290,000.00 USD | 73,290,000.00 USD | 41,430.00 USD | 21,290.00 USD | 1,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 204,970,000.00 USD | 204,970,000.00 USD | 67,200.00 USD | 57,670.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 73,230,000.00 USD | 73,230,000.00 USD | 23,000.00 USD | 6,640.00 USD | 1,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 204,830,000.00 USD | 204,830,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 73,200,000.00 USD | 73,200,000.00 USD | 43,340.00 USD | 13,890.00 USD | 61,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 204,750,000.00 USD | 204,750,000.00 USD | 202,570.00 USD | 53,170.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 204,450,000.00 USD | 204,450,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 656,350.00 USD | 18,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 73,080,000.00 USD | 73,080,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 204,350,000.00 USD | 204,350,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 73,070,000.00 USD | 73,070,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 204,260,000.00 USD | 204,260,000.00 USD | 361,660.00 USD | 45,260.00 USD | 357,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 203,490,000.00 USD | 203,490,000.00 USD | 70,670.00 USD | 152,900.00 USD | 457,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 202,810,000.00 USD | 202,810,000.00 USD | 278,240.00 USD | 50,420.00 USD | 33,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 202,450,000.00 USD | 202,450,000.00 USD | 5,680.00 USD | 39,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 355,520.00 USD | 18,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.22` | 202,400,000.00 USD | 202,400,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 202,310,000.00 USD | 202,310,000.00 USD | 0.00 USD | 765.15 USD | 40,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 202,260,000.00 USD | 202,260,000.00 USD | 54,470.00 USD | 2,490.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 202,190,000.00 USD | 202,190,000.00 USD | 10,460.00 USD | 191,360.00 USD | 207,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 201,780,000.00 USD | 201,780,000.00 USD | 649,620.00 USD | 191,250.00 USD | 200,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 1,680,000.00 USD | 17,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.23` | 200,740,000.00 USD | 200,740,000.00 USD | 341,300.00 USD | 128,580.00 USD | 60,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 200,210,000.00 USD | 200,210,000.00 USD | 44,790.00 USD | 125,700.00 USD | 371,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 199,670,000.00 USD | 199,670,000.00 USD | 257,070.00 USD | 187,490.00 USD | 353,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 73,040,000.00 USD | 73,040,000.00 USD | 0.00 USD | 396.00 USD | 903.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 198,870,000.00 USD | 198,870,000.00 USD | 702,400.00 USD | 142,840.00 USD | 467,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 73,030,000.00 USD | 73,030,000.00 USD | 73,550.00 USD | 22,720.00 USD | 7,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 197,560,000.00 USD | 197,560,000.00 USD | 1,150,000.00 USD | 525,690.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 401,010.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 72,930,000.00 USD | 72,930,000.00 USD | 800,740.00 USD | 317,390.00 USD | 424,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 193,750,000.00 USD | 193,750,000.00 USD | 1,620,000.00 USD | 912,620.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 71,390,000.00 USD | 71,390,000.00 USD | 1,340,000.00 USD | 641,660.00 USD | 928,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 189,360,000.00 USD | 189,360,000.00 USD | 1,890,000.00 USD | 972,840.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 68,480,000.00 USD | 68,480,000.00 USD | 548,430.00 USD | 270,210.00 USD | 574,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 184,250,000.00 USD | 184,250,000.00 USD | 1,980,000.00 USD | 633,060.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 67,090,000.00 USD | 67,090,000.00 USD | 179,040.00 USD | 233,640.00 USD | 324,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 179,070,000.00 USD | 179,070,000.00 USD | 982,310.00 USD | 740,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 66,350,000.00 USD | 66,350,000.00 USD | 546,970.00 USD | 84,110.00 USD | 349,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 176,250,000.00 USD | 176,250,000.00 USD | 2,160,000.00 USD | 376,950.00 USD | 1,810,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 13,870,000.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.25` | 65,370,000.00 USD | 65,370,000.00 USD | 384,220.00 USD | 90,850.00 USD | 261,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 171,900,000.00 USD | 171,900,000.00 USD | 2,120,000.00 USD | 1,190,000.00 USD | 5,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 64,630,000.00 USD | 64,630,000.00 USD | 207,040.00 USD | 196,500.00 USD | 303,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 163,280,000.00 USD | 163,280,000.00 USD | 2,280,000.00 USD | 1,370,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 63,930,000.00 USD | 63,930,000.00 USD | 117,990.00 USD | 79,810.00 USD | 571,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 156,160,000.00 USD | 156,160,000.00 USD | 2,810,000.00 USD | 918,840.00 USD | 2,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 63,160,000.00 USD | 63,160,000.00 USD | 374,100.00 USD | 17,220.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 150,430,000.00 USD | 150,430,000.00 USD | 1,240,000.00 USD | 673,830.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 62,240,000.00 USD | 62,240,000.00 USD | 213,710.00 USD | 42,480.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 147,040,000.00 USD | 147,040,000.00 USD | 625,270.00 USD | 468,670.00 USD | 763,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.25` | 641,680.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.26` | 61,900,000.00 USD | 61,900,000.00 USD | 259,250.00 USD | 149,990.00 USD | 197,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 145,180,000.00 USD | 145,180,000.00 USD | 370,280.00 USD | 407,350.00 USD | 344,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 61,290,000.00 USD | 61,290,000.00 USD | 194,390.00 USD | 1,980.00 USD | 169,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 144,060,000.00 USD | 144,060,000.00 USD | 1,190,000.00 USD | 449,360.00 USD | 890,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 60,920,000.00 USD | 60,920,000.00 USD | 433,900.00 USD | 218,760.00 USD | 376,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 141,530,000.00 USD | 141,530,000.00 USD | 1,470,000.00 USD | 1,130,000.00 USD | 852,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 59,900,000.00 USD | 59,900,000.00 USD | 1,470,000.00 USD | 562,570.00 USD | 747,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 138,080,000.00 USD | 138,080,000.00 USD | 2,860,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 57,110,000.00 USD | 57,110,000.00 USD | 2,740,000.00 USD | 1,390,000.00 USD | 2,090,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 131,460,000.00 USD | 131,460,000.00 USD | 3,640,000.00 USD | 1,830,000.00 USD | 4,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.26` | 464,620.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.27` | 50,890,000.00 USD | 50,890,000.00 USD | 1,220,000.00 USD | 573,350.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 121,530,000.00 USD | 121,530,000.00 USD | 3,940,000.00 USD | 1,540,000.00 USD | 6,430,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 47,800,000.00 USD | 47,800,000.00 USD | 479,480.00 USD | 468,170.00 USD | 719,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 109,620,000.00 USD | 109,620,000.00 USD | 1,990,000.00 USD | 1,500,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 46,130,000.00 USD | 46,130,000.00 USD | 1,230,000.00 USD | 234,050.00 USD | 931,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 103,720,000.00 USD | 103,720,000.00 USD | 4,070,000.00 USD | 1,680,000.00 USD | 4,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 43,740,000.00 USD | 43,740,000.00 USD | 1,300,000.00 USD | 345,070.00 USD | 893,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 93,890,000.00 USD | 93,890,000.00 USD | 4,300,000.00 USD | 3,000,000.00 USD | 9,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.27` | 41,200,000.00 USD | 41,200,000.00 USD | 2,350,000.00 USD | 857,380.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.27` | 77,330,000.00 USD | 77,330,000.00 USD | 3,980,000.00 USD | 1,300,000.00 USD | 7,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.27` | 479,930.00 USD | 598,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.28` | 36,310,000.00 USD | 36,310,000.00 USD | 4,710,000.00 USD | 2,840,000.00 USD | 4,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 64,810,000.00 USD | 64,810,000.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 24,680,000.00 USD | 24,680,000.00 USD | 4,440,000.00 USD | 1,850,000.00 USD | 3,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 46,540,000.00 USD | 46,540,000.00 USD | 4,830,000.00 USD | 1,750,000.00 USD | 6,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 14,400,000.00 USD | 14,400,000.00 USD | 1,730,000.00 USD | 789,830.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 33,740,000.00 USD | 33,740,000.00 USD | 4,610,000.00 USD | 1,440,000.00 USD | 3,850,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 10,370,000.00 USD | 10,370,000.00 USD | 2,010,000.00 USD | 799,310.00 USD | 2,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 23,850,000.00 USD | 23,850,000.00 USD | 3,450,000.00 USD | 2,130,000.00 USD | 2,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.28` | 5,070,000.00 USD | 5,070,000.00 USD | 2,380,000.00 USD | 488,880.00 USD | 871,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.28` | 15,780,000.00 USD | 15,780,000.00 USD | 3,830,000.00 USD | 1,550,000.00 USD | 4,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.28` | 118,740.00 USD | 118,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.29` | 1,320,000.00 USD | 1,320,000.00 USD | 365,870.00 USD | 100,470.00 USD | 857,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 6,280,000.00 USD | 6,280,000.00 USD | 724,970.00 USD | 0.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 665,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.29` | 1,860,000.00 USD | 1,860,000.00 USD | 1,040,000.00 USD | 0.00 USD | 819,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 167,570.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 514,840.00 USD | 514,840.00 USD | 0.00 USD | 213,200.00 USD | 301,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 2,330,000.00 USD | 2,330,000.00 USD | 520,800.00 USD | 184,260.00 USD | 238,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 1,260,000.00 USD | 1,260,000.00 USD | 440,550.00 USD | 0.00 USD | 307,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 413,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 389,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 86,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 3,110,000.00 USD | 3,110,000.00 USD | 193,920.00 USD | 81,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 286,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 4,540,000.00 USD | 4,540,000.00 USD | 516,450.00 USD | 910,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 4,910,000.00 USD | 4,910,000.00 USD | 90,140.00 USD | 159,790.00 USD | 127,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 5,010,000.00 USD | 5,010,000.00 USD | 89,650.00 USD | 5,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 6,220,000.00 USD | 6,220,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 6,190,000.00 USD | 6,190,000.00 USD | 404,630.00 USD | 0.00 USD | 774,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 6,770,000.00 USD | 6,770,000.00 USD | 543,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 7,870,000.00 USD | 7,870,000.00 USD | 634,790.00 USD | 743,970.00 USD | 306,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 9,140,000.00 USD | 9,140,000.00 USD | 704,520.00 USD | 318,670.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 10,360,000.00 USD | 10,360,000.00 USD | 1,290,000.00 USD | 511,150.00 USD | 689,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 11,500,000.00 USD | 11,500,000.00 USD | 557,940.00 USD | 430,030.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 13,590,000.00 USD | 13,590,000.00 USD | 368,370.00 USD | 572,040.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 13,910,000.00 USD | 13,910,000.00 USD | 57,160.00 USD | 1,070,000.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 4,840.00 USD | 4,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 20,120,000.00 USD | 20,120,000.00 USD | 1,250,000.00 USD | 1,730,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 18,540,000.00 USD | 18,540,000.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 25,640,000.00 USD | 25,640,000.00 USD | 2,150,000.00 USD | 850,800.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 21,470,000.00 USD | 21,470,000.00 USD | 755,330.00 USD | 406,240.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 28,820,000.00 USD | 28,820,000.00 USD | 1,450,000.00 USD | 706,650.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 23,040,000.00 USD | 23,040,000.00 USD | 966,720.00 USD | 235,180.00 USD | 367,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 33,400,000.00 USD | 33,400,000.00 USD | 1,970,000.00 USD | 720,740.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 27,080,000.00 USD | 27,080,000.00 USD | 1,980,000.00 USD | 761,100.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 35,400,000.00 USD | 35,400,000.00 USD | 1,080,000.00 USD | 287,550.00 USD | 625,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 29,450,000.00 USD | 29,450,000.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 22,430.00 USD | 27,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 37,890,000.00 USD | 37,890,000.00 USD | 624,130.00 USD | 621,340.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 29,980,000.00 USD | 29,980,000.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 40,130,000.00 USD | 40,130,000.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 31,140,000.00 USD | 31,140,000.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 42,720,000.00 USD | 42,720,000.00 USD | 748,200.00 USD | 298,240.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 32,860,000.00 USD | 32,860,000.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 43,960,000.00 USD | 43,960,000.00 USD | 713,230.00 USD | 84,950.00 USD | 440,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 34,800,000.00 USD | 34,800,000.00 USD | 830,370.00 USD | 108,920.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 45,640,000.00 USD | 45,640,000.00 USD | 717,360.00 USD | 300,370.00 USD | 665,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 35,290,000.00 USD | 35,290,000.00 USD | 109,550.00 USD | 194,680.00 USD | 189,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 57,610.00 USD | 84,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 47,670,000.00 USD | 47,670,000.00 USD | 831,030.00 USD | 219,020.00 USD | 976,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 36,930,000.00 USD | 36,930,000.00 USD | 679,750.00 USD | 645,230.00 USD | 312,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 51,280,000.00 USD | 51,280,000.00 USD | 1,430,000.00 USD | 370,350.00 USD | 1,810,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 39,040,000.00 USD | 39,040,000.00 USD | 1,240,000.00 USD | 362,920.00 USD | 494,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 54,800,000.00 USD | 54,800,000.00 USD | 1,770,000.00 USD | 821,890.00 USD | 929,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 43,760,000.00 USD | 43,760,000.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 440,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 59,550,000.00 USD | 59,550,000.00 USD | 2,520,000.00 USD | 788,180.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 49,500,000.00 USD | 49,500,000.00 USD | 1,730,000.00 USD | 2,870,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 62,800,000.00 USD | 62,800,000.00 USD | 1,270,000.00 USD | 696,310.00 USD | 1,290,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 60,690,000.00 USD | 60,690,000.00 USD | 3,700,000.00 USD | 1,880,000.00 USD | 5,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 163,410.00 USD | 248,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 64,330,000.00 USD | 64,330,000.00 USD | 713,120.00 USD | 289,260.00 USD | 527,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 68,440,000.00 USD | 68,440,000.00 USD | 2,550,000.00 USD | 2,230,000.00 USD | 2,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 67,530,000.00 USD | 67,530,000.00 USD | 1,330,000.00 USD | 384,860.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 78,940,000.00 USD | 78,940,000.00 USD | 4,410,000.00 USD | 1,760,000.00 USD | 4,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 68,630,000.00 USD | 68,630,000.00 USD | 516,420.00 USD | 130,090.00 USD | 452,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 86,710,000.00 USD | 86,710,000.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 70,960,000.00 USD | 70,960,000.00 USD | 879,540.00 USD | 405,430.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 95,030,000.00 USD | 95,030,000.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 73,330,000.00 USD | 73,330,000.00 USD | 857,510.00 USD | 297,760.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 103,270,000.00 USD | 103,270,000.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 3,990.00 USD | 252,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 75,460,000.00 USD | 75,460,000.00 USD | 1,120,000.00 USD | 102,980.00 USD | 901,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 107,340,000.00 USD | 107,340,000.00 USD | 1,320,000.00 USD | 881,730.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 76,270,000.00 USD | 76,270,000.00 USD | 504,090.00 USD | 150,540.00 USD | 163,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 111,130,000.00 USD | 111,130,000.00 USD | 1,490,000.00 USD | 635,240.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 77,070,000.00 USD | 77,070,000.00 USD | 374,230.00 USD | 183,190.00 USD | 237,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 113,510,000.00 USD | 113,510,000.00 USD | 671,910.00 USD | 542,980.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 78,170,000.00 USD | 78,170,000.00 USD | 452,880.00 USD | 103,540.00 USD | 545,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 117,900,000.00 USD | 117,900,000.00 USD | 2,100,000.00 USD | 918,100.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 78,220,000.00 USD | 78,220,000.00 USD | 0.00 USD | 26,460.00 USD | 25,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 119,820,000.00 USD | 119,820,000.00 USD | 664,020.00 USD | 328,930.00 USD | 923,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 201,820.00 USD | 454,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 78,550,000.00 USD | 78,550,000.00 USD | 68,130.00 USD | 85,100.00 USD | 170,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 120,310,000.00 USD | 120,310,000.00 USD | 239,150.00 USD | 216,290.00 USD | 40,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 78,960,000.00 USD | 78,960,000.00 USD | 167,370.00 USD | 18,750.00 USD | 230,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 122,100,000.00 USD | 122,100,000.00 USD | 547,200.00 USD | 138,950.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 79,370,000.00 USD | 79,370,000.00 USD | 70,350.00 USD | 104,960.00 USD | 236,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 123,510,000.00 USD | 123,510,000.00 USD | 465,040.00 USD | 398,870.00 USD | 543,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 79,680,000.00 USD | 79,680,000.00 USD | 121,120.00 USD | 32,920.00 USD | 147,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 126,360,000.00 USD | 126,360,000.00 USD | 931,390.00 USD | 404,120.00 USD | 1,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 79,870,000.00 USD | 79,870,000.00 USD | 121,400.00 USD | 884.30 USD | 69,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 128,050,000.00 USD | 128,050,000.00 USD | 594,550.00 USD | 326,340.00 USD | 769,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 80,300,000.00 USD | 80,300,000.00 USD | 137,580.00 USD | 65,830.00 USD | 232,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 129,670,000.00 USD | 129,670,000.00 USD | 676,760.00 USD | 389,310.00 USD | 552,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 81,090,000.00 USD | 81,090,000.00 USD | 336,250.00 USD | 76,440.00 USD | 369,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 131,610,000.00 USD | 131,610,000.00 USD | 579,450.00 USD | 290,350.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 81,690,000.00 USD | 81,690,000.00 USD | 331,700.00 USD | 108,980.00 USD | 163,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 134,160,000.00 USD | 134,160,000.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 82,290,000.00 USD | 82,290,000.00 USD | 371,970.00 USD | 42,880.00 USD | 185,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 135,240,000.00 USD | 135,240,000.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 82,530,000.00 USD | 82,530,000.00 USD | 145,190.00 USD | 54,030.00 USD | 40,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 136,340,000.00 USD | 136,340,000.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 31,530.00 USD | 485,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 82,620,000.00 USD | 82,620,000.00 USD | 57,490.00 USD | 16,600.00 USD | 19,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 136,830,000.00 USD | 136,830,000.00 USD | 86,820.00 USD | 203,870.00 USD | 200,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 83,010,000.00 USD | 83,010,000.00 USD | 140,810.00 USD | 51,770.00 USD | 189,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 137,920,000.00 USD | 137,920,000.00 USD | 690,420.00 USD | 162,590.00 USD | 238,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 138,080,000.00 USD | 138,080,000.00 USD | 118,760.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 138,410,000.00 USD | 138,410,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.40` | 83,030,000.00 USD | 83,030,000.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 138,550,000.00 USD | 138,550,000.00 USD | 121,260.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 11,740.00 USD | 497,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.40` | 83,130,000.00 USD | 83,130,000.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 138,570,000.00 USD | 138,570,000.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 138,580,000.00 USD | 138,580,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 138,710,000.00 USD | 138,710,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 138,830,000.00 USD | 138,830,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 139,070,000.00 USD | 139,070,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 952.59 USD | 498,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 139,240,000.00 USD | 139,240,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 139,410,000.00 USD | 139,410,000.00 USD | 12,250.00 USD | 37,300.00 USD | 120,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 139,560,000.00 USD | 139,560,000.00 USD | 88,530.00 USD | 57,460.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.41` | 83,130,000.00 USD | 83,130,000.00 USD | 0.00 USD | 158.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 139,730,000.00 USD | 139,730,000.00 USD | 11,290.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 83,170,000.00 USD | 83,170,000.00 USD | 29,120.00 USD | 9,090.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 140,230,000.00 USD | 140,230,000.00 USD | 161,890.00 USD | 72,870.00 USD | 264,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,860.00 USD | 502,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.42` | 83,400,000.00 USD | 83,400,000.00 USD | 137,370.00 USD | 26,520.00 USD | 70,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 140,660,000.00 USD | 140,660,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 84,020,000.00 USD | 84,020,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 141,680,000.00 USD | 141,680,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 84,630,000.00 USD | 84,630,000.00 USD | 292,830.00 USD | 121,550.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 143,060,000.00 USD | 143,060,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.42` | 84,850,000.00 USD | 84,850,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 143,680,000.00 USD | 143,680,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 84,940,000.00 USD | 84,940,000.00 USD | 31,260.00 USD | 27,740.00 USD | 34,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 144,040,000.00 USD | 144,040,000.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 95,360.00 USD | 597,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.43` | 85,160,000.00 USD | 85,160,000.00 USD | 151,550.00 USD | 11,130.00 USD | 55,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 145,060,000.00 USD | 145,060,000.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 85,320,000.00 USD | 85,320,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 146,570,000.00 USD | 146,570,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 85,490,000.00 USD | 85,490,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 147,960,000.00 USD | 147,960,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.43` | 85,750,000.00 USD | 85,750,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 148,760,000.00 USD | 148,760,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 85,920,000.00 USD | 85,920,000.00 USD | 102,020.00 USD | 0.00 USD | 76,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 149,290,000.00 USD | 149,290,000.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 181,920.00 USD | 779,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.44` | 86,090,000.00 USD | 86,090,000.00 USD | 39,530.00 USD | 16,760.00 USD | 106,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 149,640,000.00 USD | 149,640,000.00 USD | 74,670.00 USD | 68,640.00 USD | 209,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 86,210,000.00 USD | 86,210,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 150,090,000.00 USD | 150,090,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 86,380,000.00 USD | 86,380,000.00 USD | 77,850.00 USD | 41,360.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 150,990,000.00 USD | 150,990,000.00 USD | 299,590.00 USD | 131,210.00 USD | 459,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.44` | 86,410,000.00 USD | 86,410,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 151,490,000.00 USD | 151,490,000.00 USD | 69,670.00 USD | 152,290.00 USD | 286,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.45` | 86,520,000.00 USD | 86,520,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 151,630,000.00 USD | 151,630,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 11,390.00 USD | 790,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.45` | 86,560,000.00 USD | 86,560,000.00 USD | 35,430.00 USD | 247.55 USD | 1,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 151,760,000.00 USD | 151,760,000.00 USD | 11,070.00 USD | 2,120.00 USD | 116,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.45` | 86,620,000.00 USD | 86,620,000.00 USD | 15,340.00 USD | 14,150.00 USD | 26,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 152,230,000.00 USD | 152,230,000.00 USD | 70,540.00 USD | 96,050.00 USD | 311,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.45` | 86,760,000.00 USD | 86,760,000.00 USD | 26,300.00 USD | 37,580.00 USD | 83,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 152,830,000.00 USD | 152,830,000.00 USD | 190,550.00 USD | 38,510.00 USD | 370,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.45` | 86,830,000.00 USD | 86,830,000.00 USD | 55,320.00 USD | 0.00 USD | 12,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 153,460,000.00 USD | 153,460,000.00 USD | 161,500.00 USD | 127,370.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.46` | 5,760.00 USD | 796,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 28,340.00 USD | 824,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 11,820.00 USD | 836,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 227.20 USD | 837,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,680.00 USD | 849,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 47,570.00 USD | 897,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 1,940.00 USD | 899,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 1,130.00 USD | 900,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 6,320.00 USD | 906,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 908,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 908,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,840.00 USD | 911,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 7,570.00 USD | 918,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 321,070.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 5,220,000.00 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 4,890,000.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 6,420.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 11,270.00 USD | 11,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 133,590.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 911.91 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 760.45 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 47,320.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 1,040.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 10,410.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 1,920.00 USD | 11,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 3,260.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 4,000.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 2,540.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.77` | 2,040.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 129,540.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 3,210.00 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 889.87 USD | 11,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 2,800,000.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 297.48 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 889.98 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 5,540.00 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 632.55 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,040.00 USD | 14,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 246,040.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 339.30 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,190.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 69,460.00 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 103.95 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 8,870.00 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.95` | 287.86 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 293.25 USD | 14,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 333,390.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 1,120.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 393,140.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 513.83 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 279,600.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 5,330.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 2,540.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 1,960.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 3,100.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,830.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 100.51 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 72,080.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 3,890.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 2,350,000.00 USD | 18,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 3,460,000.00 USD | 21,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 14,930.00 USD | 21,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 1,060,000.00 USD | 22,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 92,880.00 USD | 22,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 3,280.00 USD | 22,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 175,880.00 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 108.33 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 146.63 USD | 23,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 91,880.00 USD | 23,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 74,260.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 167.65 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 1,210.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 2,420.00 USD | 23,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 24,840.00 USD | 23,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 256,540.00 USD | 23,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 114.77 USD | 23,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 5,640.00 USD | 23,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 42,710.00 USD | 23,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.54` | 613.47 USD | 23,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 3,870,000.00 USD | 27,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.56` | 346.27 USD | 27,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.58` | 2,250.00 USD | 27,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.58` | 23,350.00 USD | 27,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `7D` | `1.16` | 221,650,000.00 USD | 0.00 USD | 221,650,000.00 USD | 100,770.00 USD | 64,860.00 USD | 127,210.00 USD |
| `7D` | `1.16` | 221,360,000.00 USD | 0.00 USD | 221,360,000.00 USD | 173,190.00 USD | 99,350.00 USD | 396,520.00 USD |
| `1D` | `1.16` | 79,230,000.00 USD | 0.00 USD | 79,230,000.00 USD | 66,460.00 USD | 27,440.00 USD | 27,240.00 USD |
| `7D` | `1.16` | 220,690,000.00 USD | 0.00 USD | 220,690,000.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD |
| `1D` | `1.16` | 79,110,000.00 USD | 0.00 USD | 79,110,000.00 USD | 196,530.00 USD | 76,020.00 USD | 79,970.00 USD |
| `7D` | `1.16` | 220,260,000.00 USD | 0.00 USD | 220,260,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.16` | 78,760,000.00 USD | 0.00 USD | 78,760,000.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.16` | 219,240,000.00 USD | 0.00 USD | 219,240,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.16` | 78,020,000.00 USD | 0.00 USD | 78,020,000.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.17` | 217,860,000.00 USD | 0.00 USD | 217,860,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.17` | 77,590,000.00 USD | 0.00 USD | 77,590,000.00 USD | 123,320.00 USD | 93,840.00 USD | 111,250.00 USD |
| `7D` | `1.17` | 217,230,000.00 USD | 0.00 USD | 217,230,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD |
| `1D` | `1.17` | 77,260,000.00 USD | 0.00 USD | 77,260,000.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.17` | 215,860,000.00 USD | 0.00 USD | 215,860,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 77,080,000.00 USD | 0.00 USD | 77,080,000.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.17` | 214,350,000.00 USD | 0.00 USD | 214,350,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 76,910,000.00 USD | 0.00 USD | 76,910,000.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.17` | 212,960,000.00 USD | 0.00 USD | 212,960,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.17` | 76,690,000.00 USD | 0.00 USD | 76,690,000.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.18` | 212,160,000.00 USD | 0.00 USD | 212,160,000.00 USD | 290,470.00 USD | 91,640.00 USD | 499,970.00 USD |
| `1D` | `1.18` | 76,420,000.00 USD | 0.00 USD | 76,420,000.00 USD | 69,320.00 USD | 16,990.00 USD | 135,940.00 USD |
| `7D` | `1.18` | 211,280,000.00 USD | 0.00 USD | 211,280,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `1D` | `1.18` | 76,200,000.00 USD | 0.00 USD | 76,200,000.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.18` | 210,820,000.00 USD | 0.00 USD | 210,820,000.00 USD | 299,590.00 USD | 131,210.00 USD | 459,970.00 USD |
| `1D` | `1.18` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.18` | 209,930,000.00 USD | 0.00 USD | 209,930,000.00 USD | 69,670.00 USD | 152,290.00 USD | 286,090.00 USD |
| `1D` | `1.18` | 75,940,000.00 USD | 0.00 USD | 75,940,000.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.18` | 209,420,000.00 USD | 0.00 USD | 209,420,000.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD |
| `1D` | `1.18` | 75,860,000.00 USD | 0.00 USD | 75,860,000.00 USD | 48,130.00 USD | 23,400.00 USD | 43,690.00 USD |
| `7D` | `1.19` | 209,290,000.00 USD | 0.00 USD | 209,290,000.00 USD | 81,610.00 USD | 98,170.00 USD | 428,040.00 USD |
| `1D` | `1.19` | 75,750,000.00 USD | 0.00 USD | 75,750,000.00 USD | 694.57 USD | 23,390.00 USD | 52,890.00 USD |
| `7D` | `1.19` | 208,680,000.00 USD | 0.00 USD | 208,680,000.00 USD | 190,550.00 USD | 38,510.00 USD | 383,280.00 USD |
| `1D` | `1.19` | 75,670,000.00 USD | 0.00 USD | 75,670,000.00 USD | 34,490.00 USD | 99.63 USD | 43,820.00 USD |
| `7D` | `1.19` | 208,070,000.00 USD | 0.00 USD | 208,070,000.00 USD | 186,430.00 USD | 128,180.00 USD | 350,400.00 USD |
| `1D` | `1.19` | 75,590,000.00 USD | 0.00 USD | 75,590,000.00 USD | 24,440.00 USD | 238.88 USD | 21,580.00 USD |
| `7D` | `1.19` | 207,410,000.00 USD | 0.00 USD | 207,410,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `1D` | `1.19` | 75,540,000.00 USD | 0.00 USD | 75,540,000.00 USD | 25,150.00 USD | 18,150.00 USD | 56,850.00 USD |
| `7D` | `1.19` | 206,940,000.00 USD | 0.00 USD | 206,940,000.00 USD | 218,910.00 USD | 107,850.00 USD | 335,240.00 USD |
| `1D` | `1.19` | 75,440,000.00 USD | 0.00 USD | 75,440,000.00 USD | 130,470.00 USD | 44,250.00 USD | 113,180.00 USD |
| `7D` | `1.20` | 206,280,000.00 USD | 0.00 USD | 206,280,000.00 USD | 338,060.00 USD | 79,070.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 75,160,000.00 USD | 0.00 USD | 75,160,000.00 USD | 89,360.00 USD | 18,340.00 USD | 72,750.00 USD |
| `7D` | `1.20` | 205,570,000.00 USD | 0.00 USD | 205,570,000.00 USD | 5,350.00 USD | 93,870.00 USD | 187,830.00 USD |
| `1D` | `1.20` | 74,980,000.00 USD | 0.00 USD | 74,980,000.00 USD | 112,660.00 USD | 7,010.00 USD | 10,750.00 USD |
| `7D` | `1.20` | 205,290,000.00 USD | 0.00 USD | 205,290,000.00 USD | 67,200.00 USD | 57,670.00 USD | 21,970.00 USD |
| `1D` | `1.20` | 74,840,000.00 USD | 0.00 USD | 74,840,000.00 USD | 26,800.00 USD | 20,630.00 USD | 1,060.00 USD |
| `7D` | `1.20` | 205,140,000.00 USD | 0.00 USD | 205,140,000.00 USD | 34,730.00 USD | 26,000.00 USD | 15,030.00 USD |
| `1D` | `1.20` | 74,800,000.00 USD | 0.00 USD | 74,800,000.00 USD | 55,140.00 USD | 14,180.00 USD | 61,870.00 USD |
| `7D` | `1.20` | 205,060,000.00 USD | 0.00 USD | 205,060,000.00 USD | 202,570.00 USD | 53,170.00 USD | 48,290.00 USD |
| `7D` | `1.21` | 204,760,000.00 USD | 0.00 USD | 204,760,000.00 USD | 0.00 USD | 14,550.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 74,670,000.00 USD | 0.00 USD | 74,670,000.00 USD | 2,880.00 USD | 5,600.00 USD | 814.23 USD |
| `7D` | `1.21` | 204,670,000.00 USD | 0.00 USD | 204,670,000.00 USD | 80,450.00 USD | 5,390.00 USD | 9,940.00 USD |
| `1D` | `1.21` | 74,660,000.00 USD | 0.00 USD | 74,660,000.00 USD | 0.00 USD | 0.00 USD | 32,130.00 USD |
| `7D` | `1.21` | 204,570,000.00 USD | 0.00 USD | 204,570,000.00 USD | 361,660.00 USD | 45,260.00 USD | 357,420.00 USD |
| `7D` | `1.21` | 203,810,000.00 USD | 0.00 USD | 203,810,000.00 USD | 70,670.00 USD | 152,900.00 USD | 457,650.00 USD |
| `7D` | `1.21` | 203,120,000.00 USD | 0.00 USD | 203,120,000.00 USD | 278,240.00 USD | 50,420.00 USD | 33,960.00 USD |
| `7D` | `1.22` | 202,760,000.00 USD | 0.00 USD | 202,760,000.00 USD | 5,680.00 USD | 39,860.00 USD | 0.00 USD |
| `7D` | `1.22` | 202,720,000.00 USD | 0.00 USD | 202,720,000.00 USD | 97,920.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.22` | 202,620,000.00 USD | 0.00 USD | 202,620,000.00 USD | 0.00 USD | 765.15 USD | 40,620.00 USD |
| `7D` | `1.22` | 202,580,000.00 USD | 0.00 USD | 202,580,000.00 USD | 54,470.00 USD | 2,490.00 USD | 14,710.00 USD |
| `7D` | `1.22` | 202,510,000.00 USD | 0.00 USD | 202,510,000.00 USD | 10,460.00 USD | 191,360.00 USD | 207,400.00 USD |
| `7D` | `1.23` | 202,100,000.00 USD | 0.00 USD | 202,100,000.00 USD | 649,620.00 USD | 191,250.00 USD | 200,510.00 USD |
| `7D` | `1.23` | 201,060,000.00 USD | 0.00 USD | 201,060,000.00 USD | 341,300.00 USD | 128,580.00 USD | 60,930.00 USD |
| `7D` | `1.23` | 200,520,000.00 USD | 0.00 USD | 200,520,000.00 USD | 44,790.00 USD | 125,700.00 USD | 371,190.00 USD |
| `7D` | `1.23` | 199,980,000.00 USD | 0.00 USD | 199,980,000.00 USD | 257,070.00 USD | 187,490.00 USD | 353,810.00 USD |
| `7D` | `1.23` | 199,180,000.00 USD | 0.00 USD | 199,180,000.00 USD | 702,400.00 USD | 142,840.00 USD | 467,410.00 USD |
| `1D` | `1.23` | 74,620,000.00 USD | 0.00 USD | 74,620,000.00 USD | 11,570.00 USD | 989.25 USD | 1,410.00 USD |
| `7D` | `1.24` | 197,870,000.00 USD | 0.00 USD | 197,870,000.00 USD | 1,150,000.00 USD | 525,690.00 USD | 2,130,000.00 USD |
| `1D` | `1.24` | 74,610,000.00 USD | 0.00 USD | 74,610,000.00 USD | 514,810.00 USD | 120,320.00 USD | 262,160.00 USD |
| `7D` | `1.24` | 194,060,000.00 USD | 0.00 USD | 194,060,000.00 USD | 1,620,000.00 USD | 912,620.00 USD | 1,860,000.00 USD |
| `1D` | `1.24` | 73,710,000.00 USD | 0.00 USD | 73,710,000.00 USD | 1,080,000.00 USD | 666,380.00 USD | 709,340.00 USD |
| `7D` | `1.24` | 189,680,000.00 USD | 0.00 USD | 189,680,000.00 USD | 1,890,000.00 USD | 972,840.00 USD | 2,250,000.00 USD |
| `1D` | `1.24` | 71,250,000.00 USD | 0.00 USD | 71,250,000.00 USD | 914,710.00 USD | 493,310.00 USD | 740,300.00 USD |
| `7D` | `1.24` | 184,560,000.00 USD | 0.00 USD | 184,560,000.00 USD | 1,980,000.00 USD | 677,720.00 USD | 2,560,000.00 USD |
| `1D` | `1.24` | 69,100,000.00 USD | 0.00 USD | 69,100,000.00 USD | 347,740.00 USD | 188,510.00 USD | 341,680.00 USD |
| `7D` | `1.24` | 179,330,000.00 USD | 0.00 USD | 179,330,000.00 USD | 982,310.00 USD | 740,000.00 USD | 1,100,000.00 USD |
| `1D` | `1.24` | 68,230,000.00 USD | 0.00 USD | 68,230,000.00 USD | 372,570.00 USD | 122,390.00 USD | 516,600.00 USD |
| `7D` | `1.25` | 176,520,000.00 USD | 0.00 USD | 176,520,000.00 USD | 2,160,000.00 USD | 376,950.00 USD | 1,810,000.00 USD |
| `1D` | `1.25` | 67,220,000.00 USD | 0.00 USD | 67,220,000.00 USD | 546,010.00 USD | 129,710.00 USD | 161,620.00 USD |
| `7D` | `1.25` | 172,170,000.00 USD | 0.00 USD | 172,170,000.00 USD | 2,120,000.00 USD | 1,190,000.00 USD | 5,300,000.00 USD |
| `1D` | `1.25` | 66,380,000.00 USD | 0.00 USD | 66,380,000.00 USD | 218,430.00 USD | 101,390.00 USD | 355,010.00 USD |
| `7D` | `1.25` | 163,550,000.00 USD | 0.00 USD | 163,550,000.00 USD | 2,280,000.00 USD | 1,370,000.00 USD | 3,470,000.00 USD |
| `1D` | `1.25` | 65,700,000.00 USD | 0.00 USD | 65,700,000.00 USD | 177,400.00 USD | 102,610.00 USD | 457,850.00 USD |
| `7D` | `1.25` | 156,430,000.00 USD | 0.00 USD | 156,430,000.00 USD | 2,810,000.00 USD | 918,840.00 USD | 2,000,000.00 USD |
| `1D` | `1.25` | 64,970,000.00 USD | 0.00 USD | 64,970,000.00 USD | 351,630.00 USD | 92,050.00 USD | 426,530.00 USD |
| `7D` | `1.25` | 150,700,000.00 USD | 0.00 USD | 150,700,000.00 USD | 1,240,000.00 USD | 673,830.00 USD | 1,480,000.00 USD |
| `1D` | `1.25` | 64,100,000.00 USD | 0.00 USD | 64,100,000.00 USD | 131,220.00 USD | 41,890.00 USD | 312,160.00 USD |
| `7D` | `1.25` | 147,300,000.00 USD | 0.00 USD | 147,300,000.00 USD | 625,270.00 USD | 468,670.00 USD | 763,070.00 USD |
| `1D` | `1.26` | 63,610,000.00 USD | 0.00 USD | 63,610,000.00 USD | 266,880.00 USD | 47,170.00 USD | 116,960.00 USD |
| `7D` | `1.26` | 145,450,000.00 USD | 0.00 USD | 145,450,000.00 USD | 370,280.00 USD | 407,350.00 USD | 344,360.00 USD |
| `1D` | `1.26` | 63,180,000.00 USD | 0.00 USD | 63,180,000.00 USD | 222,740.00 USD | 104,190.00 USD | 319,670.00 USD |
| `7D` | `1.26` | 144,320,000.00 USD | 0.00 USD | 144,320,000.00 USD | 1,190,000.00 USD | 449,360.00 USD | 890,430.00 USD |
| `1D` | `1.26` | 62,530,000.00 USD | 0.00 USD | 62,530,000.00 USD | 281,000.00 USD | 71,910.00 USD | 171,240.00 USD |
| `7D` | `1.26` | 141,800,000.00 USD | 0.00 USD | 141,800,000.00 USD | 1,470,000.00 USD | 1,130,000.00 USD | 852,870.00 USD |
| `1D` | `1.26` | 62,010,000.00 USD | 0.00 USD | 62,010,000.00 USD | 990,350.00 USD | 254,090.00 USD | 554,190.00 USD |
| `7D` | `1.26` | 138,340,000.00 USD | 0.00 USD | 138,340,000.00 USD | 2,860,000.00 USD | 1,720,000.00 USD | 2,030,000.00 USD |
| `1D` | `1.26` | 60,210,000.00 USD | 0.00 USD | 60,210,000.00 USD | 2,210,000.00 USD | 1,360,000.00 USD | 1,530,000.00 USD |
| `7D` | `1.26` | 131,730,000.00 USD | 0.00 USD | 131,730,000.00 USD | 3,640,000.00 USD | 1,830,000.00 USD | 4,470,000.00 USD |
| `1D` | `1.27` | 55,110,000.00 USD | 0.00 USD | 55,110,000.00 USD | 1,850,000.00 USD | 1,040,000.00 USD | 1,770,000.00 USD |
| `7D` | `1.27` | 121,800,000.00 USD | 0.00 USD | 121,800,000.00 USD | 3,940,000.00 USD | 1,630,000.00 USD | 6,430,000.00 USD |
| `1D` | `1.27` | 50,450,000.00 USD | 0.00 USD | 50,450,000.00 USD | 814,800.00 USD | 377,270.00 USD | 750,220.00 USD |
| `7D` | `1.27` | 109,800,000.00 USD | 0.00 USD | 109,800,000.00 USD | 1,990,000.00 USD | 1,500,000.00 USD | 2,410,000.00 USD |
| `1D` | `1.27` | 48,510,000.00 USD | 0.00 USD | 48,510,000.00 USD | 859,440.00 USD | 291,610.00 USD | 1,160,000.00 USD |
| `7D` | `1.27` | 103,900,000.00 USD | 0.00 USD | 103,900,000.00 USD | 4,070,000.00 USD | 1,680,000.00 USD | 4,080,000.00 USD |
| `1D` | `1.27` | 46,200,000.00 USD | 0.00 USD | 46,200,000.00 USD | 1,330,000.00 USD | 332,670.00 USD | 564,560.00 USD |
| `7D` | `1.27` | 94,060,000.00 USD | 0.00 USD | 94,060,000.00 USD | 4,300,000.00 USD | 3,000,000.00 USD | 9,250,000.00 USD |
| `1D` | `1.27` | 43,980,000.00 USD | 0.00 USD | 43,980,000.00 USD | 1,460,000.00 USD | 569,500.00 USD | 1,290,000.00 USD |
| `7D` | `1.27` | 77,510,000.00 USD | 0.00 USD | 77,510,000.00 USD | 3,980,000.00 USD | 1,300,000.00 USD | 7,240,000.00 USD |
| `1D` | `1.28` | 40,660,000.00 USD | 0.00 USD | 40,660,000.00 USD | 3,040,000.00 USD | 1,300,000.00 USD | 2,410,000.00 USD |
| `7D` | `1.28` | 64,990,000.00 USD | 0.00 USD | 64,990,000.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 33,910,000.00 USD | 0.00 USD | 33,910,000.00 USD | 6,210,000.00 USD | 2,760,000.00 USD | 4,540,000.00 USD |
| `7D` | `1.28` | 46,720,000.00 USD | 0.00 USD | 46,720,000.00 USD | 4,830,000.00 USD | 1,750,000.00 USD | 6,220,000.00 USD |
| `1D` | `1.28` | 20,400,000.00 USD | 0.00 USD | 20,400,000.00 USD | 2,450,000.00 USD | 1,460,000.00 USD | 2,910,000.00 USD |
| `7D` | `1.28` | 33,910,000.00 USD | 0.00 USD | 33,910,000.00 USD | 4,610,000.00 USD | 1,610,000.00 USD | 3,850,000.00 USD |
| `1D` | `1.28` | 13,580,000.00 USD | 0.00 USD | 13,580,000.00 USD | 1,420,000.00 USD | 1,040,000.00 USD | 1,500,000.00 USD |
| `7D` | `1.28` | 23,850,000.00 USD | 0.00 USD | 23,850,000.00 USD | 3,450,000.00 USD | 2,130,000.00 USD | 2,480,000.00 USD |
| `1D` | `1.28` | 9,620,000.00 USD | 0.00 USD | 9,620,000.00 USD | 2,490,000.00 USD | 530,190.00 USD | 2,050,000.00 USD |
| `7D` | `1.28` | 15,780,000.00 USD | 0.00 USD | 15,780,000.00 USD | 3,830,000.00 USD | 1,550,000.00 USD | 4,130,000.00 USD |
| `1D` | `1.29` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 1,390,000.00 USD | 327,360.00 USD | 975,970.00 USD |
| `7D` | `1.29` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 724,970.00 USD | 0.00 USD | 3,030,000.00 USD |
| `1D` | `1.29` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 221,930.00 USD | 100,470.00 USD | 305,580.00 USD |
| `7D` | `1.29` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 665,270.00 USD |
| `7D` | `1.29` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,040,000.00 USD | 0.00 USD | 819,130.00 USD |
| `1D` | `1.29` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 1,220,000.00 USD |
| `1D` | `1.29` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.29` | 301,640.00 USD | 301,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 301,640.00 USD |
| `7D` | `1.29` | 603,280.00 USD | 603,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 301,640.00 USD |
| `1D` | `1.29` | 238,060.00 USD | 238,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 238,060.00 USD |
| `7D` | `1.29` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 440,550.00 USD | 0.00 USD | 307,250.00 USD |
| `1D` | `1.30` | 835,920.00 USD | 835,920.00 USD | 0.00 USD | 0.00 USD | 597,860.00 USD | 0.00 USD |
| `7D` | `1.30` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 389,370.00 USD | 0.00 USD |
| `1D` | `1.30` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 168,250.00 USD | 0.00 USD |
| `7D` | `1.30` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 286,660.00 USD | 0.00 USD |
| `1D` | `1.30` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 521,850.00 USD | 910,560.00 USD | 0.00 USD |
| `7D` | `1.30` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD |
| `1D` | `1.30` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 188,510.00 USD | 98,100.00 USD | 127,330.00 USD |
| `1D` | `1.31` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 179,790.00 USD | 318,440.00 USD | 0.00 USD |
| `7D` | `1.31` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 1,770,000.00 USD | 178,660.00 USD | 0.00 USD |
| `1D` | `1.31` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 111,830.00 USD | 1,460.00 USD | 102,670.00 USD |
| `7D` | `1.31` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 543,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.31` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 607,350.00 USD | 344,570.00 USD | 796,330.00 USD |
| `7D` | `1.31` | 9,410,000.00 USD | 9,410,000.00 USD | 0.00 USD | 704,520.00 USD | 318,670.00 USD | 1,350,000.00 USD |
| `1D` | `1.31` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 1,570,000.00 USD | 443,660.00 USD | 688,860.00 USD |
| `7D` | `1.31` | 11,770,000.00 USD | 11,770,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,370,000.00 USD |
| `1D` | `1.31` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 462,940.00 USD | 483,320.00 USD | 181,970.00 USD |
| `7D` | `1.31` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 57,160.00 USD | 1,070,000.00 USD | 1,280,000.00 USD |
| `1D` | `1.32` | 15,360,000.00 USD | 15,360,000.00 USD | 0.00 USD | 210,800.00 USD | 1,830,000.00 USD | 4,170,000.00 USD |
| `7D` | `1.32` | 18,810,000.00 USD | 18,810,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 22,280,000.00 USD | 22,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,060,000.00 USD | 3,590,000.00 USD |
| `7D` | `1.32` | 21,830,000.00 USD | 21,830,000.00 USD | 0.00 USD | 755,330.00 USD | 495,580.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 25,810,000.00 USD | 25,810,000.00 USD | 0.00 USD | 1,720,000.00 USD | 742,480.00 USD | 1,060,000.00 USD |
| `7D` | `1.32` | 23,400,000.00 USD | 23,400,000.00 USD | 0.00 USD | 966,720.00 USD | 235,180.00 USD | 367,890.00 USD |
| `1D` | `1.32` | 30,330,000.00 USD | 30,330,000.00 USD | 0.00 USD | 1,830,000.00 USD | 981,550.00 USD | 1,710,000.00 USD |
| `7D` | `1.32` | 27,430,000.00 USD | 27,430,000.00 USD | 0.00 USD | 1,980,000.00 USD | 761,100.00 USD | 1,290,000.00 USD |
| `1D` | `1.32` | 33,330,000.00 USD | 33,330,000.00 USD | 0.00 USD | 1,770,000.00 USD | 259,410.00 USD | 968,180.00 USD |
| `7D` | `1.32` | 29,800,000.00 USD | 29,800,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 35,580,000.00 USD | 35,580,000.00 USD | 0.00 USD | 646,920.00 USD | 308,630.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 30,340,000.00 USD | 30,340,000.00 USD | 0.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 37,770,000.00 USD | 37,770,000.00 USD | 0.00 USD | 682,740.00 USD | 433,560.00 USD | 1,070,000.00 USD |
| `7D` | `1.33` | 31,490,000.00 USD | 31,490,000.00 USD | 0.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 40,160,000.00 USD | 40,160,000.00 USD | 0.00 USD | 822,840.00 USD | 283,020.00 USD | 1,290,000.00 USD |
| `7D` | `1.33` | 33,210,000.00 USD | 33,210,000.00 USD | 0.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 41,670,000.00 USD | 41,670,000.00 USD | 0.00 USD | 262,430.00 USD | 248,670.00 USD | 999,630.00 USD |
| `7D` | `1.33` | 35,160,000.00 USD | 35,160,000.00 USD | 0.00 USD | 830,370.00 USD | 108,920.00 USD | 1,000,000.00 USD |
| `1D` | `1.33` | 43,080,000.00 USD | 43,080,000.00 USD | 0.00 USD | 819,570.00 USD | 94,350.00 USD | 492,850.00 USD |
| `7D` | `1.33` | 35,650,000.00 USD | 35,650,000.00 USD | 0.00 USD | 109,550.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 45,370,000.00 USD | 45,370,000.00 USD | 0.00 USD | 842,300.00 USD | 333,220.00 USD | 1,110,000.00 USD |
| `7D` | `1.34` | 37,290,000.00 USD | 37,290,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 312,290.00 USD |
| `1D` | `1.34` | 48,060,000.00 USD | 48,060,000.00 USD | 0.00 USD | 1,230,000.00 USD | 398,480.00 USD | 1,070,000.00 USD |
| `7D` | `1.34` | 39,390,000.00 USD | 39,390,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 494,950.00 USD |
| `1D` | `1.34` | 51,970,000.00 USD | 51,970,000.00 USD | 0.00 USD | 1,730,000.00 USD | 549,090.00 USD | 1,630,000.00 USD |
| `7D` | `1.34` | 44,120,000.00 USD | 44,120,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 440,440.00 USD |
| `1D` | `1.34` | 55,680,000.00 USD | 55,680,000.00 USD | 0.00 USD | 1,630,000.00 USD | 878,740.00 USD | 1,200,000.00 USD |
| `7D` | `1.34` | 49,860,000.00 USD | 49,860,000.00 USD | 0.00 USD | 1,730,000.00 USD | 2,870,000.00 USD | 1,140,000.00 USD |
| `1D` | `1.34` | 60,040,000.00 USD | 60,040,000.00 USD | 0.00 USD | 2,230,000.00 USD | 721,440.00 USD | 1,410,000.00 USD |
| `7D` | `1.34` | 61,090,000.00 USD | 61,090,000.00 USD | 0.00 USD | 3,700,000.00 USD | 1,930,000.00 USD | 5,610,000.00 USD |
| `1D` | `1.35` | 62,160,000.00 USD | 62,160,000.00 USD | 0.00 USD | 887,130.00 USD | 386,900.00 USD | 847,370.00 USD |
| `7D` | `1.35` | 68,840,000.00 USD | 68,840,000.00 USD | 0.00 USD | 2,550,000.00 USD | 2,230,000.00 USD | 2,980,000.00 USD |
| `1D` | `1.35` | 64,070,000.00 USD | 64,070,000.00 USD | 0.00 USD | 854,690.00 USD | 263,070.00 USD | 799,350.00 USD |
| `7D` | `1.35` | 79,340,000.00 USD | 79,340,000.00 USD | 0.00 USD | 4,410,000.00 USD | 1,760,000.00 USD | 4,320,000.00 USD |
| `1D` | `1.35` | 66,660,000.00 USD | 66,660,000.00 USD | 0.00 USD | 1,150,000.00 USD | 329,530.00 USD | 1,100,000.00 USD |
| `7D` | `1.35` | 87,110,000.00 USD | 87,110,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,440,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 68,070,000.00 USD | 68,070,000.00 USD | 0.00 USD | 558,120.00 USD | 208,670.00 USD | 646,720.00 USD |
| `7D` | `1.35` | 95,430,000.00 USD | 95,430,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,230,000.00 USD | 4,480,000.00 USD |
| `1D` | `1.35` | 70,420,000.00 USD | 70,420,000.00 USD | 0.00 USD | 935,850.00 USD | 363,450.00 USD | 1,050,000.00 USD |
| `7D` | `1.35` | 103,670,000.00 USD | 103,670,000.00 USD | 0.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD |
| `1D` | `1.36` | 72,730,000.00 USD | 72,730,000.00 USD | 0.00 USD | 911,460.00 USD | 199,730.00 USD | 1,200,000.00 USD |
| `7D` | `1.36` | 107,740,000.00 USD | 107,740,000.00 USD | 0.00 USD | 1,320,000.00 USD | 879,500.00 USD | 1,870,000.00 USD |
| `1D` | `1.36` | 74,080,000.00 USD | 74,080,000.00 USD | 0.00 USD | 812,050.00 USD | 113,780.00 USD | 425,930.00 USD |
| `7D` | `1.36` | 111,530,000.00 USD | 111,530,000.00 USD | 0.00 USD | 1,490,000.00 USD | 635,240.00 USD | 1,670,000.00 USD |
| `1D` | `1.36` | 74,890,000.00 USD | 74,890,000.00 USD | 0.00 USD | 430,370.00 USD | 151,930.00 USD | 229,660.00 USD |
| `7D` | `1.36` | 113,910,000.00 USD | 113,910,000.00 USD | 0.00 USD | 671,910.00 USD | 542,980.00 USD | 1,170,000.00 USD |
| `1D` | `1.36` | 75,850,000.00 USD | 75,850,000.00 USD | 0.00 USD | 390,480.00 USD | 174,320.00 USD | 389,900.00 USD |
| `7D` | `1.36` | 118,300,000.00 USD | 118,300,000.00 USD | 0.00 USD | 2,100,000.00 USD | 918,100.00 USD | 1,380,000.00 USD |
| `1D` | `1.36` | 76,500,000.00 USD | 76,500,000.00 USD | 0.00 USD | 253,080.00 USD | 60,540.00 USD | 338,290.00 USD |
| `7D` | `1.36` | 120,220,000.00 USD | 120,220,000.00 USD | 0.00 USD | 664,020.00 USD | 328,930.00 USD | 923,440.00 USD |
| `1D` | `1.37` | 76,680,000.00 USD | 76,680,000.00 USD | 0.00 USD | 53,740.00 USD | 0.00 USD | 124,610.00 USD |
| `7D` | `1.37` | 120,710,000.00 USD | 120,710,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 40,350.00 USD |
| `1D` | `1.37` | 76,910,000.00 USD | 76,910,000.00 USD | 0.00 USD | 99,090.00 USD | 85,720.00 USD | 48,400.00 USD |
| `7D` | `1.37` | 122,500,000.00 USD | 122,500,000.00 USD | 0.00 USD | 547,200.00 USD | 138,950.00 USD | 1,100,000.00 USD |
| `1D` | `1.37` | 77,290,000.00 USD | 77,290,000.00 USD | 0.00 USD | 80,330.00 USD | 25,940.00 USD | 272,260.00 USD |
| `7D` | `1.37` | 123,910,000.00 USD | 123,910,000.00 USD | 0.00 USD | 465,040.00 USD | 398,870.00 USD | 543,240.00 USD |
| `1D` | `1.37` | 77,650,000.00 USD | 77,650,000.00 USD | 0.00 USD | 23,870.00 USD | 54,130.00 USD | 286,550.00 USD |
| `7D` | `1.37` | 126,760,000.00 USD | 126,760,000.00 USD | 0.00 USD | 931,390.00 USD | 404,120.00 USD | 1,520,000.00 USD |
| `1D` | `1.37` | 77,840,000.00 USD | 77,840,000.00 USD | 0.00 USD | 119,320.00 USD | 258.33 USD | 66,850.00 USD |
| `7D` | `1.38` | 128,450,000.00 USD | 128,450,000.00 USD | 0.00 USD | 594,550.00 USD | 326,340.00 USD | 769,660.00 USD |
| `1D` | `1.38` | 78,120,000.00 USD | 78,120,000.00 USD | 0.00 USD | 114,290.00 USD | 46,840.00 USD | 122,400.00 USD |
| `7D` | `1.38` | 130,070,000.00 USD | 130,070,000.00 USD | 0.00 USD | 676,760.00 USD | 389,310.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 78,670,000.00 USD | 78,670,000.00 USD | 0.00 USD | 235,940.00 USD | 73,260.00 USD | 241,330.00 USD |
| `7D` | `1.38` | 132,010,000.00 USD | 132,010,000.00 USD | 0.00 USD | 579,450.00 USD | 290,350.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 79,450,000.00 USD | 79,450,000.00 USD | 0.00 USD | 379,220.00 USD | 102,400.00 USD | 295,250.00 USD |
| `7D` | `1.38` | 134,550,000.00 USD | 134,550,000.00 USD | 0.00 USD | 1,210,000.00 USD | 330,740.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 79,970,000.00 USD | 79,970,000.00 USD | 0.00 USD | 241,850.00 USD | 53,840.00 USD | 224,750.00 USD |
| `7D` | `1.38` | 135,640,000.00 USD | 135,640,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.38` | 80,400,000.00 USD | 80,400,000.00 USD | 0.00 USD | 340,420.00 USD | 35,940.00 USD | 56,890.00 USD |
| `7D` | `1.39` | 136,740,000.00 USD | 136,740,000.00 USD | 0.00 USD | 505,510.00 USD | 190,450.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 80,590,000.00 USD | 80,590,000.00 USD | 0.00 USD | 81,750.00 USD | 52,380.00 USD | 56,350.00 USD |
| `7D` | `1.39` | 137,230,000.00 USD | 137,230,000.00 USD | 0.00 USD | 86,820.00 USD | 203,870.00 USD | 200,360.00 USD |
| `1D` | `1.39` | 80,750,000.00 USD | 80,750,000.00 USD | 0.00 USD | 83,870.00 USD | 35,460.00 USD | 36,020.00 USD |
| `7D` | `1.39` | 138,320,000.00 USD | 138,320,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 238,810.00 USD |
| `1D` | `1.39` | 81,010,000.00 USD | 81,010,000.00 USD | 0.00 USD | 86,460.00 USD | 17,040.00 USD | 153,570.00 USD |
| `7D` | `1.39` | 138,480,000.00 USD | 138,480,000.00 USD | 0.00 USD | 118,760.00 USD | 39,430.00 USD | 0.00 USD |
| `7D` | `1.39` | 138,810,000.00 USD | 138,810,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `1D` | `1.39` | 81,030,000.00 USD | 81,030,000.00 USD | 0.00 USD | 7,190.00 USD | 14,010.00 USD | 2,040.00 USD |
| `7D` | `1.40` | 138,950,000.00 USD | 138,950,000.00 USD | 0.00 USD | 121,260.00 USD | 22,660.00 USD | 0.00 USD |
| `1D` | `1.40` | 81,130,000.00 USD | 81,130,000.00 USD | 0.00 USD | 19,030.00 USD | 0.00 USD | 80,320.00 USD |
| `7D` | `1.40` | 138,970,000.00 USD | 138,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,250.00 USD |
| `7D` | `1.40` | 138,970,000.00 USD | 138,970,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 139,110,000.00 USD | 139,110,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 139,230,000.00 USD | 139,230,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `7D` | `1.41` | 139,470,000.00 USD | 139,470,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 139,640,000.00 USD | 139,640,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `7D` | `1.41` | 139,810,000.00 USD | 139,810,000.00 USD | 0.00 USD | 12,250.00 USD | 37,300.00 USD | 120,130.00 USD |
| `7D` | `1.41` | 139,960,000.00 USD | 139,960,000.00 USD | 0.00 USD | 88,530.00 USD | 57,460.00 USD | 7,070.00 USD |
| `1D` | `1.41` | 81,130,000.00 USD | 81,130,000.00 USD | 0.00 USD | 0.00 USD | 158.40 USD | 0.00 USD |
| `7D` | `1.41` | 140,130,000.00 USD | 140,130,000.00 USD | 0.00 USD | 11,290.00 USD | 26,480.00 USD | 132,120.00 USD |
| `1D` | `1.41` | 81,130,000.00 USD | 81,130,000.00 USD | 0.00 USD | 4,630.00 USD | 237.30 USD | 204.46 USD |
| `7D` | `1.42` | 140,630,000.00 USD | 140,630,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 264,400.00 USD |
| `1D` | `1.42` | 81,250,000.00 USD | 81,250,000.00 USD | 0.00 USD | 61,830.00 USD | 27,040.00 USD | 27,040.00 USD |
| `7D` | `1.42` | 141,060,000.00 USD | 141,060,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 204,770.00 USD |
| `1D` | `1.42` | 81,600,000.00 USD | 81,600,000.00 USD | 0.00 USD | 196,530.00 USD | 76,020.00 USD | 79,970.00 USD |
| `7D` | `1.42` | 142,080,000.00 USD | 142,080,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.42` | 82,340,000.00 USD | 82,340,000.00 USD | 0.00 USD | 381,490.00 USD | 157,870.00 USD | 200,700.00 USD |
| `7D` | `1.42` | 143,460,000.00 USD | 143,460,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.42` | 82,770,000.00 USD | 82,770,000.00 USD | 0.00 USD | 157,740.00 USD | 92,660.00 USD | 181,030.00 USD |
| `7D` | `1.42` | 144,080,000.00 USD | 144,080,000.00 USD | 0.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.42` | 82,860,000.00 USD | 82,860,000.00 USD | 0.00 USD | 9,670.00 USD | 55,100.00 USD | 21,210.00 USD |
| `7D` | `1.43` | 144,440,000.00 USD | 144,440,000.00 USD | 0.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD |
| `1D` | `1.43` | 83,100,000.00 USD | 83,100,000.00 USD | 0.00 USD | 113,650.00 USD | 38,740.00 USD | 90,040.00 USD |
| `7D` | `1.43` | 145,460,000.00 USD | 145,460,000.00 USD | 0.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD |
| `1D` | `1.43` | 83,280,000.00 USD | 83,280,000.00 USD | 0.00 USD | 140,210.00 USD | 31,180.00 USD | 7,770.00 USD |
| `7D` | `1.43` | 146,970,000.00 USD | 146,970,000.00 USD | 0.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.43` | 83,450,000.00 USD | 83,450,000.00 USD | 0.00 USD | 39,480.00 USD | 20,730.00 USD | 103,480.00 USD |
| `7D` | `1.43` | 148,360,000.00 USD | 148,360,000.00 USD | 0.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.43` | 83,670,000.00 USD | 83,670,000.00 USD | 0.00 USD | 29,740.00 USD | 31,270.00 USD | 158,290.00 USD |
| `7D` | `1.43` | 149,160,000.00 USD | 149,160,000.00 USD | 0.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.43` | 83,940,000.00 USD | 83,940,000.00 USD | 0.00 USD | 108,240.00 USD | 24,630.00 USD | 140,870.00 USD |
| `7D` | `1.44` | 149,680,000.00 USD | 149,680,000.00 USD | 0.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD |
| `1D` | `1.44` | 84,070,000.00 USD | 84,070,000.00 USD | 0.00 USD | 21,660.00 USD | 0.00 USD | 105,000.00 USD |
| `7D` | `1.44` | 150,040,000.00 USD | 150,040,000.00 USD | 0.00 USD | 74,670.00 USD | 67,750.00 USD | 209,840.00 USD |
| `1D` | `1.44` | 84,160,000.00 USD | 84,160,000.00 USD | 0.00 USD | 47,660.00 USD | 16,990.00 USD | 30,940.00 USD |
| `7D` | `1.44` | 150,490,000.00 USD | 150,490,000.00 USD | 0.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `1D` | `1.44` | 84,340,000.00 USD | 84,340,000.00 USD | 0.00 USD | 92,450.00 USD | 55,020.00 USD | 27,500.00 USD |
| `7D` | `1.44` | 151,380,000.00 USD | 151,380,000.00 USD | 0.00 USD | 299,590.00 USD | 131,210.00 USD | 459,970.00 USD |
| `1D` | `1.44` | 84,420,000.00 USD | 84,420,000.00 USD | 0.00 USD | 56,380.00 USD | 0.00 USD | 25,140.00 USD |
| `7D` | `1.44` | 151,890,000.00 USD | 151,890,000.00 USD | 0.00 USD | 69,670.00 USD | 152,290.00 USD | 286,090.00 USD |
| `1D` | `1.44` | 84,500,000.00 USD | 84,500,000.00 USD | 0.00 USD | 21,010.00 USD | 10,580.00 USD | 49,850.00 USD |
| `7D` | `1.45` | 152,020,000.00 USD | 152,020,000.00 USD | 0.00 USD | 67,200.00 USD | 53,830.00 USD | 12,180.00 USD |
| `1D` | `1.45` | 84,540,000.00 USD | 84,540,000.00 USD | 0.00 USD | 0.00 USD | 22,830.00 USD | 16,200.00 USD |
| `7D` | `1.45` | 152,150,000.00 USD | 152,150,000.00 USD | 0.00 USD | 11,070.00 USD | 2,120.00 USD | 116,410.00 USD |
| `1D` | `1.45` | 84,610,000.00 USD | 84,610,000.00 USD | 0.00 USD | 45,440.00 USD | 247.55 USD | 25,480.00 USD |
| `1D` | `1.45` | 84,620,000.00 USD | 84,620,000.00 USD | 0.00 USD | 0.00 USD | 6,730.00 USD | 0.00 USD |
| `7D` | `1.45` | 152,630,000.00 USD | 152,630,000.00 USD | 0.00 USD | 70,540.00 USD | 96,050.00 USD | 311,630.00 USD |
| `7D` | `1.45` | 153,230,000.00 USD | 153,230,000.00 USD | 0.00 USD | 190,550.00 USD | 38,510.00 USD | 370,320.00 USD |
| `7D` | `1.45` | 153,860,000.00 USD | 153,860,000.00 USD | 0.00 USD | 161,500.00 USD | 127,370.00 USD | 338,310.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `3.00B` | Total OI Tokens: `2,322,763,434.5 XRP`
  * 1h OI Change: `-0.29%` | 4h OI Change: `-1.03%` | 24h OI Change: `+1.59%`
  * Exchange Breakdown: Binance=`497.47M` | Bybit=`325.83M` | OKX=`101.83M` | Hyperliquid=`227.31M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `70.69K` | Last 24h: `142.09K` | Last 3d: `599.05K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0061%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0043%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `53.24%` | `46.76%` | `1.14` | 31,580,000.00 USD |
| `15M` | `Binance` | `54.58%` | `45.42%` | `1.20` | 9,270,000.00 USD |
| `15M` | `OKX` | `53.24%` | `46.76%` | `1.14` | 4,110,000.00 USD |
| `15M` | `Bybit` | `52.22%` | `47.78%` | `1.09` | 3,620,000.00 USD |
| `15M` | `KuCoin` | `45.52%` | `54.48%` | `0.84` | 515,040.00 USD |
| `15M` | `Gate` | `46.3%` | `53.7%` | `0.86` | 1,600,000.00 USD |
| `15M` | `Bitget` | `49.23%` | `50.77%` | `0.97` | 2,380,000.00 USD |
| `15M` | `BingX` | `38.53%` | `61.47%` | `0.63` | 967,120.00 USD |
| `15M` | `MEXC` | `61.5%` | `38.5%` | `1.60` | 4,280,000.00 USD |
| `15M` | `Bitunix` | `50.22%` | `49.78%` | `1.01` | 2,190,000.00 USD |
| `15M` | `Hyperliquid` | `81.09%` | `18.91%` | `4.29` | 538,300.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `63.1%` | `36.9%` | `1.71` | 170,100.00 USD |
| `15M` | `Crypto.com` | `47.88%` | `52.12%` | `0.92` | 49,160.00 USD |
| `15M` | `WhiteBIT` | `44.31%` | `55.69%` | `0.80` | 1,660,000.00 USD |
| `15M` | `HTX` | `67.08%` | `32.92%` | `2.04` | 7,990.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `43.65%` | `56.35%` | `0.77` | 118,060.00 USD |
| `15M` | `Aster` | `64.32%` | `35.68%` | `1.80` | 93,460.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `49.97%` | `50.03%` | `1.00` | 28,310.00 USD |
| `15M` | `Whale Positions` | `54.58%` | `45.42%` | `1.20` | 9,270,000.00 USD |
| `15M` | `Global Accounts` | `53.24%` | `46.76%` | `1.14` | 31,580,000.00 USD |
| `1H` | `XRP` | `43.94%` | `56.06%` | `0.78` | 116,600,000.00 USD |
| `1H` | `Binance` | `50.53%` | `49.47%` | `1.02` | 37,500,000.00 USD |
| `1H` | `OKX` | `43.62%` | `56.38%` | `0.77` | 11,750,000.00 USD |
| `1H` | `Bybit` | `42.11%` | `57.89%` | `0.73` | 16,680,000.00 USD |
| `1H` | `KuCoin` | `42.85%` | `57.15%` | `0.75` | 1,310,000.00 USD |
| `1H` | `Gate` | `46.18%` | `53.82%` | `0.86` | 5,230,000.00 USD |
| `1H` | `Bitget` | `46.84%` | `53.16%` | `0.88` | 8,930,000.00 USD |
| `1H` | `BingX` | `16.53%` | `83.47%` | `0.20` | 5,080,000.00 USD |
| `1H` | `MEXC` | `45.43%` | `54.57%` | `0.83` | 11,600,000.00 USD |
| `1H` | `Bitunix` | `48.22%` | `51.78%` | `0.93` | 7,050,000.00 USD |
| `1H` | `Hyperliquid` | `50.74%` | `49.26%` | `1.03` | 1,630,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.65%` | `46.35%` | `1.16` | 521,010.00 USD |
| `1H` | `Crypto.com` | `47.3%` | `52.7%` | `0.90` | 156,290.00 USD |
| `1H` | `WhiteBIT` | `20.27%` | `79.73%` | `0.25` | 6,700,000.00 USD |
| `1H` | `HTX` | `46.37%` | `53.63%` | `0.86` | 31,810.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `48.85%` | `51.15%` | `0.96` | 400,340.00 USD |
| `1H` | `Aster` | `34.49%` | `65.51%` | `0.53` | 1,940,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.92%` | `47.08%` | `1.12` | 104,160.00 USD |
| `1H` | `Whale Positions` | `50.53%` | `49.47%` | `1.02` | 37,500,000.00 USD |
| `1H` | `Global Accounts` | `43.94%` | `56.06%` | `0.78` | 116,600,000.00 USD |
| `4H` | `XRP` | `47.47%` | `52.53%` | `0.90` | 607,390,000.00 USD |
| `4H` | `Binance` | `49.29%` | `50.71%` | `0.97` | 192,450,000.00 USD |
| `4H` | `OKX` | `48.15%` | `51.85%` | `0.93` | 64,040,000.00 USD |
| `4H` | `Bybit` | `47.46%` | `52.54%` | `0.90` | 85,550,000.00 USD |
| `4H` | `KuCoin` | `50.9%` | `49.1%` | `1.04` | 6,700,000.00 USD |
| `4H` | `Gate` | `46.98%` | `53.02%` | `0.89` | 26,030,000.00 USD |
| `4H` | `Bitget` | `47.34%` | `52.66%` | `0.90` | 49,770,000.00 USD |
| `4H` | `BingX` | `34.19%` | `65.81%` | `0.52` | 13,890,000.00 USD |
| `4H` | `MEXC` | `49.75%` | `50.25%` | `0.99` | 83,530,000.00 USD |
| `4H` | `Bitunix` | `48%` | `52%` | `0.92` | 34,510,000.00 USD |
| `4H` | `Hyperliquid` | `54.4%` | `45.6%` | `1.19` | 15,900,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.85%` | `48.15%` | `1.08` | 3,300,000.00 USD |
| `4H` | `Crypto.com` | `48.05%` | `51.95%` | `0.92` | 771,040.00 USD |
| `4H` | `WhiteBIT` | `19.44%` | `80.56%` | `0.24` | 19,920,000.00 USD |
| `4H` | `HTX` | `51.79%` | `48.21%` | `1.07` | 254,360.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `60.34%` | `39.66%` | `1.52` | 3,600,000.00 USD |
| `4H` | `Aster` | `42.62%` | `57.38%` | `0.74` | 6,500,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.1%` | `54.9%` | `0.82` | 658,110.00 USD |
| `4H` | `Whale Positions` | `49.29%` | `50.71%` | `0.97` | 192,450,000.00 USD |
| `4H` | `Global Accounts` | `47.47%` | `52.53%` | `0.90` | 607,390,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.31` | `1.31` | `1.31` | `1.31` | `1.31` | 9,791,336.03 USD | 4,585,305.80 USD | 5,206,030.23 USD | -620,724.44 USD | `-6.34%` | `2B / 6S` |
| `0:00 UTC` | `1.31` | `1.31` | `1.31` | `1.32` | `1.31` | 13,794,897.02 USD | 7,005,423.08 USD | 6,789,473.94 USD | 215,949.13 USD | `+1.57%` | `17B / 16S` |
| `5:00 UTC` | `1.30` | `1.31` | `1.30` | `1.31` | `1.30` | 11,087,990.94 USD | 4,090,249.58 USD | 6,997,741.36 USD | -2,907,491.79 USD | `-26.22%` | `5B / 28S` |
| `0:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 10,205,311.65 USD | 4,505,902.50 USD | 5,699,409.15 USD | -1,193,506.66 USD | `-11.69%` | `6B / 11S` |
| `5:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.30` | 4,776,328.08 USD | 2,498,208.46 USD | 2,278,119.62 USD | 220,088.84 USD | `+4.61%` | `7B / 8S` |
| `0:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.29` | 9,199,982.08 USD | 4,187,578.87 USD | 5,012,403.21 USD | -824,824.35 USD | `-8.97%` | `4B / 7S` |
| `5:00 UTC` | `1.30` | `1.30` | `1.30` | `1.30` | `1.29` | 5,359,755.08 USD | 2,909,456.29 USD | 2,450,298.78 USD | 459,157.51 USD | `+8.57%` | `5B / 3S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.30` | `1.29` | 8,857,459.31 USD | 3,136,112.07 USD | 5,721,347.24 USD | -2,585,235.17 USD | `-29.19%` | `5B / 22S` |
| `5:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 11,824,590.46 USD | 6,782,340.79 USD | 5,042,249.67 USD | 1,740,091.12 USD | `+14.72%` | `12B / 8S` |
| `0:00 UTC` | `1.29` | `1.29` | `1.29` | `1.29` | `1.29` | 1,337,470.06 USD | 745,741.90 USD | 591,728.16 USD | 154,013.73 USD | `+11.52%` | `6B / 6S` |

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
| `5m` | 64,370.00 USD | 15,060.00 USD | **`ACCUMULATION`** |
| `15m` | 42,410.00 USD | 1,000,000.00 USD | **`ACCUMULATION`** |
| `30m` | -2,390,000.00 USD | -5,750,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,800,000.00 USD | -4,170,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -5,720,000.00 USD | -14,600,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,440,000.00 USD | -8,910,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -2,000,000.00 USD | -9,210,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,400,000.00 USD | -10,120,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,510,000.00 USD | -13,460,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -21,290,000.00 USD | -59,630,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -72,000,000.00 USD | -76,720,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -551,230,000.00 USD | -1,190,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+64.37K` | 15m=`+42.41K` | 1h=`-2.80M` | 24h=`-21.29M`
* Futures Capital Netflows: 5m=`+15.06K` | 15m=`+1.00M` | 1h=`-4.17M` | 24h=`-59.63M`
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
  * `2026-10-29 23:31:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:35 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:35 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:35 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:35 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:35 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:35 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0123` pts)
  * +2.5R Take Profit: `1.31`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.30` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.31` (Risk Distance: `0.0123` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.30`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
