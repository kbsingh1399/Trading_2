# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 11:11:08 IST` (`2026-10-30 05:41:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `1.23` | VWAP Z-Score: `+1.60` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0098` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `65.28` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.28` | Lower -3.00σ Band: `1.17`
  * Upper +2.51σ Band: `1.27` | Lower -2.51σ Band: `1.18`
  * Upper +2.01σ Band: `1.26` | Lower -2.01σ Band: `1.19`
  * Upper +2.00σ Band: `1.26` | Lower -2.00σ Band: `1.19`
  * Upper +1.28σ Band: `1.25` | Lower -1.28σ Band: `1.21`
  * Upper +1.00σ Band: `1.25` | Lower -1.00σ Band: `1.21`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.25` | EMA-20=`1.24` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.25` (Slope: `+0.0000`) | EMA-100=`1.26`
  * Institutional Anchors: EMA-144=`1.27` | EMA-200=`1.28` (Slope: `-0.4188`) | EMA-233=`1.29`
- **Range Boundaries**: 24H High=`1.31` | 24H Low=`1.19` | Weekly High=`1.34` | Weekly Low=`1.19`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-0.18%`)
  * Point of Control (POC) = `1.25` (Distance: `+0.98%`)
  * Value Area Low (VAL) = `1.23` (Distance: `+2.62%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
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
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `1,386,947` | 1,747,664.27 USD | 136,187.84 USD | `+7.79%` | -41,216,540.03 USD | `-0.47` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `1,613,250` | 2,032,520.55 USD | 71,948.81 USD | `+3.54%` | -41,144,591.22 USD | `-0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `1.26` | `1.26` | `1.26` | `1.26` | `1,097,578` | 1,382,867.56 USD | 95,822.86 USD | `+6.93%` | -41,048,768.36 USD | `-0.44` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.25` | `1.26` | `1.25` | `1.26` | `7,899,972` | 9,935,673.56 USD | 2,939,945.86 USD | `+29.59%` | -41,063,393.39 USD | `+1.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.26` | `1.26` | `1.26` | `1.26` | `4,871,938` | 6,138,672.69 USD | 450,540.03 USD | `+7.34%` | -40,612,853.36 USD | `-0.02` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `1.26` | `1.26` | `1.26` | `1.26` | `1,087,180` | 1,369,755.47 USD | 100,610.56 USD | `+7.35%` | -40,512,242.80 USD | `-0.17` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.22` | `1.25` | `1.22` | `1.25` | `36,941,941` | 45,661,386.25 USD | 4,453,356.28 USD | `+9.75%` | -46,975,781.11 USD | `+0.76` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.25` | `1.26` | `1.24` | `1.25` | `31,772,661` | 39,740,326.41 USD | 3,435,958.07 USD | `+8.65%` | -43,539,823.04 USD | `+0.62` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.25` | `1.26` | `1.25` | `1.26` | `13,859,950` | 17,445,184.70 USD | 3,490,696.73 USD | `+20.01%` | -40,049,126.31 USD | `+0.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -42,956,799.49 USD | `-1.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -45,386,586.40 USD | `+0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.26` | `45,636,690` | 57,190,655.61 USD | 6,927,873.31 USD | `+12.11%` | -38,458,713.09 USD | `+1.13` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | 545,129.68 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -14,866,665.27 USD | `-1.39` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -42,956,799.49 USD | `-1.45` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -45,386,586.40 USD | `+0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.26` | `45,636,690` | 57,190,655.61 USD | 6,927,873.31 USD | `+12.11%` | -38,458,713.09 USD | `+1.13` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `ASK` | `1.26` | `19701.0000` | 24,880.39 USD | 1,940,040.04 USD | `2 orders` | `+0.16%` | `-` |
| `ASK` | `1.26` | `16523.0000` | 20,865.24 USD | 1,915,159.64 USD | `2 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `197650.0000` | 249,572.65 USD | 1,894,294.40 USD | `9 orders` | `+0.15%` | `-` |
| `ASK` | `1.26` | `369170.0000` | 466,114.04 USD | 1,644,721.74 USD | `7 orders` | `+0.14%` | `-` |
| `ASK` | `1.26` | `25701.0000` | 32,447.51 USD | 1,178,607.70 USD | `3 orders` | `+0.13%` | `-` |
| `ASK` | `1.26` | `71103.0000` | 89,760.43 USD | 1,146,160.19 USD | `5 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `53183.0000` | 67,132.90 USD | 1,056,399.76 USD | `8 orders` | `+0.12%` | `-` |
| `ASK` | `1.26` | `101301.0000` | 127,862.12 USD | 989,266.86 USD | `9 orders` | `+0.11%` | `-` |
| `ASK` | `1.26` | `63228.0000` | 79,800.06 USD | 861,404.74 USD | `7 orders` | `+0.10%` | `-` |
| `ASK` | `1.26` | `103671.0000` | 130,832.80 USD | 781,604.68 USD | `7 orders` | `+0.09%` | `-` |
| `ASK` | `1.26` | `249752.0000` | 315,162.05 USD | 650,771.88 USD | `6 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `41737.0000` | 52,663.75 USD | 335,609.83 USD | `7 orders` | `+0.08%` | `-` |
| `ASK` | `1.26` | `58452.0000` | 73,748.89 USD | 282,946.08 USD | `10 orders` | `+0.07%` | `-` |
| `ASK` | `1.26` | `87583.0000` | 110,494.71 USD | 209,197.19 USD | `9 orders` | `+0.06%` | `-` |
| `ASK` | `1.26` | `17612.0000` | 22,217.54 USD | 98,702.48 USD | `10 orders` | `+0.05%` | `-` |
| `ASK` | `1.26` | `25570.0000` | 32,254.00 USD | 76,484.94 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `11005.0000` | 13,880.61 USD | 44,230.95 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `1.26` | `11188.0000` | 14,110.31 USD | 30,350.34 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `1.26` | `8751.0000` | 11,035.89 USD | 16,240.03 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `1.26` | `4127.0000` | 5,204.15 USD | 5,204.15 USD | `2 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `1.26` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.26` | `0.00%` | `-` |
| `BID` | `1.26` | `70728.0000` | 89,166.79 USD | 89,166.79 USD | `18 orders` | `-0.01%` | `-` |
| `BID` | `1.26` | `51986.0000` | 65,533.55 USD | 154,700.34 USD | `12 orders` | `-0.02%` | `-` |
| `BID` | `1.26` | `26270.0000` | 33,113.33 USD | 187,813.68 USD | `7 orders` | `-0.03%` | `-` |
| `BID` | `1.26` | `45933.0000` | 57,893.95 USD | 245,707.63 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `85834.0000` | 108,176.59 USD | 353,884.22 USD | `9 orders` | `-0.04%` | `-` |
| `BID` | `1.26` | `94712.0000` | 119,356.06 USD | 473,240.28 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `1.26` | `37848.0000` | 47,692.26 USD | 520,932.55 USD | `6 orders` | `-0.06%` | `-` |
| `BID` | `1.26` | `273326.0000` | 344,390.76 USD | 865,323.31 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `1.26` | `252775.0000` | 318,471.22 USD | 1,183,794.53 USD | `7 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `97177.0000` | 122,423.58 USD | 1,306,218.11 USD | `6 orders` | `-0.08%` | `-` |
| `BID` | `1.26` | `24149.0000` | 30,420.50 USD | 1,336,638.61 USD | `7 orders` | `-0.09%` | `-` |
| `BID` | `1.26` | `54124.0000` | 68,174.59 USD | 1,404,813.20 USD | `4 orders` | `-0.10%` | `-` |
| `BID` | `1.26` | `13954.0000` | 17,575.06 USD | 1,422,388.26 USD | `3 orders` | `-0.11%` | `-` |
| `BID` | `1.26` | `74052.0000` | 93,261.09 USD | 1,515,649.35 USD | `8 orders` | `-0.12%` | `-` |
| `BID` | `1.26` | `21483.0000` | 27,053.54 USD | 1,542,702.89 USD | `2 orders` | `-0.12%` | `-` |
| `BID` | `1.26` | `363278.0000` | 457,439.66 USD | 2,000,142.55 USD | `5 orders` | `-0.13%` | `-` |
| `BID` | `1.26` | `61293.0000` | 77,174.02 USD | 2,077,316.57 USD | `6 orders` | `-0.14%` | `-` |
| `BID` | `1.26` | `49274.0000` | 62,035.97 USD | 2,139,352.53 USD | `3 orders` | `-0.15%` | `-` |
| `BID` | `1.26` | `46186.0000` | 58,143.56 USD | 2,197,496.09 USD | `5 orders` | `-0.15%` | `-` |
| `BID` | `1.26` | `33836.0000` | 42,592.76 USD | 2,240,088.85 USD | `6 orders` | `-0.16%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:04:06 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `28` | `0x31b1...1434` | `LONG` | 44,132,595.51 USD | `35,031,430.00` | `1.13` | `1.26` | `0.9612` | 4,553,712.25 USD | `+10.32%` | `10X Cross` |
| `91` | `0x5b5d...c060` | `SHORT` | 20,107,469.03 USD | `15,964,251.00` | `1.44` | `1.26` | `11.24` | 2,808,599.68 USD | `+13.97%` | `5X Cross` |
| `157` | `0xb83d...6e36` | `SHORT` | 13,297,755.91 USD | `10,555,450.00` | `1.50` | `1.26` | `13.68` | 2,524,813.73 USD | `+18.99%` | `5X Cross` |
| `342` | `0x58f0...0d20` | `LONG` | 6,684,516.17 USD | `5,307,147.00` | `1.24` | `1.26` | `1.22` | 81,672.67 USD | `+1.22%` | `20X Cross` |
| `399` | `0xecb6...2b00` | `SHORT` | 5,608,381.70 USD | `4,452,754.00` | `1.27` | `1.26` | `8.05` | 48,398.69 USD | `+0.86%` | `10X Cross` |
| `423` | `0xca49...53c8` | `SHORT` | 5,212,686.86 USD | `4,138,886.00` | `1.44` | `1.26` | `4.80` | 740,635.87 USD | `+14.21%` | `20X Cross` |
| `439` | `0xdd53...2b13` | `SHORT` | 5,036,400.25 USD | `3,998,914.00` | `1.40` | `1.26` | `16.64` | 560,475.86 USD | `+11.13%` | `3X Cross` |
| `506` | `0x610b...b613` | `LONG` | 4,464,386.74 USD | `3,543,946.00` | `1.44` | `1.26` | `0.8065` | -635,605.87 USD | `-14.24%` | `5X Cross` |
| `534` | `0xfc27...9d9d` | `SHORT` | 4,188,002.33 USD | `3,325,284.00` | `1.29` | `1.26` | `6.56` | 112,706.97 USD | `+2.69%` | `20X Cross` |
| `619` | `0x9946...0852` | `SHORT` | 3,667,861.37 USD | `2,912,418.00` | `1.41` | `1.26` | `1.77` | 440,641.21 USD | `+12.01%` | `20X Cross` |
| `675` | `0xc30c...a4c9` | `SHORT` | 3,367,212.97 USD | `2,672,981.00` | `1.42` | `1.26` | `1.59` | 419,751.13 USD | `+12.47%` | `6X Cross` |
| `700` | `0xf48f...10fe` | `LONG` | 3,232,368.38 USD | `2,565,779.00` | `1.53` | `1.26` | `0.9937` | -692,272.34 USD | `-21.42%` | `4X Cross` |
| `738` | `0x023a...2355` | `SHORT` | 3,104,575.56 USD | `2,464,927.00` | `1.32` | `1.26` | `3.34` | 148,420.68 USD | `+4.78%` | `20X Cross` |
| `746` | `0x45d2...4029` | `SHORT` | 3,089,202.72 USD | `2,453,000.00` | `1.48` | `1.26` | `18.05` | 549,077.70 USD | `+17.77%` | `20X Cross` |
| `1073` | `0xeadc...9d55` | `LONG` | 2,040,194.61 USD | `1,619,805.00` | `1.21` | `1.26` | `0.000000` | 81,351.59 USD | `+3.99%` | `20X Cross` |
| `1149` | `0x94b2...599e` | `SHORT` | 1,940,554.37 USD | `1,540,696.00` | `1.36` | `1.26` | `1.86` | 159,912.08 USD | `+8.24%` | `20X Cross` |
| `1157` | `0xbcd4...0dd2` | `SHORT` | 1,926,814.97 USD | `1,529,461.00` | `1.31` | `1.26` | `1.85` | 77,729.63 USD | `+4.03%` | `20X Cross` |
| `1170` | `0x3fc5...c0c1` | `SHORT` | 1,904,421.27 USD | `1,511,779.00` | `1.52` | `1.26` | `2.34` | 387,193.34 USD | `+20.33%` | `20X Cross` |
| `1202` | `0x31ef...f715` | `LONG` | 1,857,908.99 USD | `1,475,080.00` | `1.49` | `1.26` | `1.04` | -341,356.41 USD | `-18.37%` | `3X Isolated` |
| `1243` | `0x7737...bf66` | `SHORT` | 1,780,260.43 USD | `1,413,466.00` | `1.41` | `1.26` | `13.68` | 218,608.22 USD | `+12.28%` | `10X Cross` |
| `1301` | `0x95da...2328` | `LONG` | 1,668,722.39 USD | `1,324,876.00` | `1.35` | `1.26` | `0.0607` | -124,918.70 USD | `-7.49%` | `5X Cross` |
| `1323` | `0xee2b...d67e` | `LONG` | 1,645,188.93 USD | `1,306,284.00` | `1.55` | `1.26` | `0.3846` | -385,465.97 USD | `-23.43%` | `4X Cross` |
| `1365` | `0x215d...f80a` | `LONG` | 1,579,241.86 USD | `1,251,777.00` | `1.32` | `1.26` | `1.13` | -75,212.36 USD | `-4.76%` | `14X Cross` |
| `1394` | `0x5fa3...35b7` | `SHORT` | 1,563,096.19 USD | `1,240,651.00` | `1.30` | `1.26` | `2.59` | 53,395.94 USD | `+3.42%` | `20X Cross` |
| `1427` | `0x123d...3bff` | `LONG` | 1,530,976.68 USD | `1,215,329.00` | `1.35` | `1.26` | `0.000000` | -106,092.54 USD | `-6.93%` | `10X Cross` |
| `1489` | `0xdf95...7d72` | `SHORT` | 1,461,685.02 USD | `1,160,528.00` | `1.37` | `1.26` | `34.17` | 131,790.12 USD | `+9.02%` | `20X Cross` |
| `1553` | `0xc179...e0c8` | `SHORT` | 1,389,604.38 USD | `1,103,104.00` | `1.29` | `1.26` | `6.83` | 37,845.37 USD | `+2.72%` | `10X Cross` |
| `1563` | `0xef96...9383` | `SHORT` | 1,376,845.91 USD | `1,092,976.00` | `1.34` | `1.26` | `4.54` | 85,901.52 USD | `+6.24%` | `20X Cross` |
| `1613` | `0x7fda...17d1` | `LONG` | 1,312,111.94 USD | `1,041,524.00` | `1.21` | `1.26` | `0.000000` | 48,769.14 USD | `+3.72%` | `20X Cross` |
| `1646` | `0xb1ce...681b` | `LONG` | 1,286,765.65 USD | `1,021,764.00` | `1.49` | `1.26` | `1.16` | -237,290.85 USD | `-18.44%` | `4X Isolated` |
| `1748` | `0x3c36...461a` | `LONG` | 1,183,336.20 USD | `940,051.00` | `1.30` | `1.26` | `1.05` | -35,744.41 USD | `-3.02%` | `10X Cross` |
| `1816` | `0x2577...4897` | `SHORT` | 1,142,996.38 USD | `907,284.00` | `1.24` | `1.26` | `4.89` | -15,802.90 USD | `-1.38%` | `20X Cross` |
| `2005` | `0xbfc7...80b4` | `SHORT` | 1,007,553.60 USD | `800,000.00` | `1.48` | `1.26` | `3.10` | 175,901.05 USD | `+17.46%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.30` | 5,006.53 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.2977 USD [API] | `2026-10-29 02:14:42` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 292.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.29K USD at 1.2952 USD [API] | `2026-10-29 02:16:03` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 117.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.12K USD at 1.2952 USD [API] | `2026-10-29 02:16:03` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 86.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2952 USD [API] | `2026-10-29 02:16:03` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 5,005.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.01K USD at 1.2952 USD [API] | `2026-10-29 02:16:03` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 2,959.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.96K USD at 1.2948 USD [API] | `2026-10-29 02:17:12` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 167.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.17K USD at 1.2948 USD [API] | `2026-10-29 02:17:12` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 15.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2948 USD [API] | `2026-10-29 02:17:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,320.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.32K USD at 1.2948 USD [API] | `2026-10-29 02:17:09` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 195.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2948 USD [API] | `2026-10-29 02:17:09` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,258.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.26K USD at 1.2984 USD [API] | `2026-10-29 02:18:56` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,332.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.33K USD at 1.2984 USD [API] | `2026-10-29 02:18:56` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 11,283.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 11.28K USD at 1.2963 USD [API] | `2026-10-29 02:22:50` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,535.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.54K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,006.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.01K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,901.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.90K USD at 1.2940 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 55.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.06K USD at 1.2940 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 651.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.65K USD at 1.2946 USD [API] | `2026-10-29 02:27:25` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 14.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2946 USD [API] | `2026-10-29 02:27:25` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 41.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.2946 USD [API] | `2026-10-29 02:27:25` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 647.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.65K USD at 1.2946 USD [API] | `2026-10-29 02:27:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 91.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2946 USD [API] | `2026-10-29 02:27:23` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,781.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.78K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 51.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.05K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 380.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.38K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 666.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.67K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,781.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.78K USD at 1.2939 USD [API] | `2026-10-29 02:27:32` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,951.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.95K USD at 1.2931 USD [API] | `2026-10-29 02:28:24` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10,544.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.54K USD at 1.2941 USD [API] | `2026-10-29 02:29:46` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,426.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.43K USD at 1.2941 USD [API] | `2026-10-29 02:29:46` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,398.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 6.40K USD at 1.2935 USD [API] | `2026-10-29 02:28:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 210.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.21K USD at 1.2935 USD [API] | `2026-10-29 02:28:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 15.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2935 USD [API] | `2026-10-29 02:28:18` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 386.76 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.39K USD at 1.2935 USD [API] | `2026-10-29 02:28:18` |
| `ANNOUNCEMENT` | `INFO` | `1.36` | 10,210.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 10.21K USD at 1.3650 USD [API] | `2026-08-30 23:29:31` |
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
| `7D` | `Long Liquidation` | `1.07` | 83,800,000.00 USD | 83,800,000.00 USD | 23,750.00 USD | 0.00 USD | 39,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.07` | 950,500.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 191,170.00 USD | 13,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.09` | 83,740,000.00 USD | 83,740,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 83,690,000.00 USD | 83,690,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 83,600,000.00 USD | 83,600,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.09` | 361,000.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.10` | 83,560,000.00 USD | 83,560,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 83,550,000.00 USD | 83,550,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 83,270,000.00 USD | 83,270,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.10` | 388,580.00 USD | 13,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.11` | 83,260,000.00 USD | 83,260,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 83,260,000.00 USD | 83,260,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 83,260,000.00 USD | 83,260,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 75,000,000.00 USD | 75,000,000.00 USD | 88,950.00 USD | 16,870.00 USD | 125,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 283,400.00 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.12` | 74,770,000.00 USD | 74,770,000.00 USD | 0.00 USD | 14,730.00 USD | 3,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 83,200,000.00 USD | 83,200,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 74,750,000.00 USD | 74,750,000.00 USD | 3,530.00 USD | 1,320.00 USD | 144,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 83,190,000.00 USD | 83,190,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 74,600,000.00 USD | 74,600,000.00 USD | 15,020.00 USD | 68,320.00 USD | 29,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 74,490,000.00 USD | 74,490,000.00 USD | 5,340.00 USD | 40,010.00 USD | 87,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 83,110,000.00 USD | 83,110,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 74,350,000.00 USD | 74,350,000.00 USD | 5,470.00 USD | 2,460.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 83,090,000.00 USD | 83,090,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,230,000.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 74,270,000.00 USD | 74,270,000.00 USD | 92,060.00 USD | 28,150.00 USD | 50,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 74,100,000.00 USD | 74,100,000.00 USD | 69,610.00 USD | 19,950.00 USD | 166,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 82,880,000.00 USD | 82,880,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 73,850,000.00 USD | 73,850,000.00 USD | 0.00 USD | 107,140.00 USD | 82,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 82,680,000.00 USD | 82,680,000.00 USD | 5,450.00 USD | 2,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 73,660,000.00 USD | 73,660,000.00 USD | 0.00 USD | 13,730.00 USD | 168,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 82,680,000.00 USD | 82,680,000.00 USD | 69,750.00 USD | 93,260.00 USD | 8,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 73,480,000.00 USD | 73,480,000.00 USD | 63,980.00 USD | 70,910.00 USD | 41,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 82,500,000.00 USD | 82,500,000.00 USD | 74,920.00 USD | 97,060.00 USD | 224,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 129,840.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.14` | 73,300,000.00 USD | 73,300,000.00 USD | 40,370.00 USD | 125,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 82,110,000.00 USD | 82,110,000.00 USD | 79,780.00 USD | 88,050.00 USD | 71,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 81,870,000.00 USD | 81,870,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 73,130,000.00 USD | 73,130,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 81,840,000.00 USD | 81,840,000.00 USD | 39,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 73,070,000.00 USD | 73,070,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 81,800,000.00 USD | 81,800,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 73,000,000.00 USD | 73,000,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 81,660,000.00 USD | 81,660,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 306,590.00 USD | 10,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 81,650,000.00 USD | 81,650,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 72,860,000.00 USD | 72,860,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 81,590,000.00 USD | 81,590,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 81,220,000.00 USD | 81,220,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 72,850,000.00 USD | 72,850,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 81,060,000.00 USD | 81,060,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 72,780,000.00 USD | 72,780,000.00 USD | 73,200.00 USD | 45,600.00 USD | 263,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 80,900,000.00 USD | 80,900,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 337,540.00 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 72,400,000.00 USD | 72,400,000.00 USD | 20,480.00 USD | 25,050.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 80,020,000.00 USD | 80,020,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 72,270,000.00 USD | 72,270,000.00 USD | 122,170.00 USD | 21,140.00 USD | 392,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 79,780,000.00 USD | 79,780,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 71,730,000.00 USD | 71,730,000.00 USD | 212,900.00 USD | 76,950.00 USD | 158,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 78,920,000.00 USD | 78,920,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 71,290,000.00 USD | 71,290,000.00 USD | 270,110.00 USD | 293,490.00 USD | 148,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 77,840,000.00 USD | 77,840,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 70,570,000.00 USD | 70,570,000.00 USD | 179,260.00 USD | 89,000.00 USD | 719,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 76,540,000.00 USD | 76,540,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,290,000.00 USD | 9,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 69,590,000.00 USD | 69,590,000.00 USD | 87,310.00 USD | 70,600.00 USD | 151,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 74,870,000.00 USD | 74,870,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 69,280,000.00 USD | 69,280,000.00 USD | 113,470.00 USD | 166,170.00 USD | 170,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 73,530,000.00 USD | 73,530,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 68,830,000.00 USD | 68,830,000.00 USD | 162,180.00 USD | 22,610.00 USD | 361,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 72,460,000.00 USD | 72,460,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 68,280,000.00 USD | 68,280,000.00 USD | 371,850.00 USD | 25,710.00 USD | 289,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 70,420,000.00 USD | 70,420,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 67,590,000.00 USD | 67,590,000.00 USD | 124,360.00 USD | 130,370.00 USD | 474,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 69,220,000.00 USD | 69,220,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 394,220.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 66,860,000.00 USD | 66,860,000.00 USD | 304,390.00 USD | 85,620.00 USD | 356,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 67,650,000.00 USD | 67,650,000.00 USD | 181,850.00 USD | 100,190.00 USD | 377,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 66,120,000.00 USD | 66,120,000.00 USD | 71,040.00 USD | 84,480.00 USD | 175,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 66,990,000.00 USD | 66,990,000.00 USD | 85,020.00 USD | 74,230.00 USD | 489,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 65,790,000.00 USD | 65,790,000.00 USD | 113,290.00 USD | 10,150.00 USD | 24,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 66,340,000.00 USD | 66,340,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 65,640,000.00 USD | 65,640,000.00 USD | 222,930.00 USD | 10,160.00 USD | 666,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 65,730,000.00 USD | 65,730,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 64,740,000.00 USD | 64,740,000.00 USD | 196,910.00 USD | 73,630.00 USD | 143,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 65,470,000.00 USD | 65,470,000.00 USD | 299,450.00 USD | 571,980.00 USD | 235,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 520,520.00 USD | 7,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 64,320,000.00 USD | 64,320,000.00 USD | 86,540.00 USD | 511,780.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 64,360,000.00 USD | 64,360,000.00 USD | 76,370.00 USD | 109,420.00 USD | 706,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 63,660,000.00 USD | 63,660,000.00 USD | 365,260.00 USD | 93,260.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 63,470,000.00 USD | 63,470,000.00 USD | 250,710.00 USD | 93,330.00 USD | 585,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 61,630,000.00 USD | 61,630,000.00 USD | 110,600.00 USD | 45,410.00 USD | 319,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 62,540,000.00 USD | 62,540,000.00 USD | 227,280.00 USD | 92,240.00 USD | 795,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 61,160,000.00 USD | 61,160,000.00 USD | 147,820.00 USD | 199,810.00 USD | 469,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 61,420,000.00 USD | 61,420,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 60,340,000.00 USD | 60,340,000.00 USD | 190,850.00 USD | 428,210.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 60,060,000.00 USD | 60,060,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 672,400.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 58,030,000.00 USD | 58,030,000.00 USD | 784,530.00 USD | 121,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 59,230,000.00 USD | 59,230,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 55,910,000.00 USD | 55,910,000.00 USD | 264,550.00 USD | 834,460.00 USD | 657,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 57,640,000.00 USD | 57,640,000.00 USD | 31,150.00 USD | 372,080.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 54,150,000.00 USD | 54,150,000.00 USD | 708,890.00 USD | 419,750.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 54,630,000.00 USD | 54,630,000.00 USD | 736,290.00 USD | 330,310.00 USD | 18,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 50,720,000.00 USD | 50,720,000.00 USD | 137,910.00 USD | 157,180.00 USD | 820,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 53,550,000.00 USD | 53,550,000.00 USD | 264,000.00 USD | 144,630.00 USD | 464,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 49,600,000.00 USD | 49,600,000.00 USD | 526,510.00 USD | 511,570.00 USD | 374,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 52,680,000.00 USD | 52,680,000.00 USD | 47,500.00 USD | 589,990.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 12,330.00 USD | 6,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 48,190,000.00 USD | 48,190,000.00 USD | 328,050.00 USD | 532,540.00 USD | 275,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 52,030,000.00 USD | 52,030,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 47,050,000.00 USD | 47,050,000.00 USD | 1,660,000.00 USD | 193,480.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 52,010,000.00 USD | 52,010,000.00 USD | 456,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 43,530,000.00 USD | 43,530,000.00 USD | 533,310.00 USD | 413,110.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 51,550,000.00 USD | 51,550,000.00 USD | 257,960.00 USD | 492,370.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 41,520,000.00 USD | 41,520,000.00 USD | 1,410,000.00 USD | 572,260.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 47,720,000.00 USD | 47,720,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 38,520,000.00 USD | 38,520,000.00 USD | 0.00 USD | 90,950.00 USD | 898,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 46,490,000.00 USD | 46,490,000.00 USD | 108,640.00 USD | 0.00 USD | 910,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 40,860.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.22` | 37,530,000.00 USD | 37,530,000.00 USD | 226,520.00 USD | 85,640.00 USD | 680,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 45,470,000.00 USD | 45,470,000.00 USD | 142,210.00 USD | 9,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 36,530,000.00 USD | 36,530,000.00 USD | 143,650.00 USD | 4,200.00 USD | 183,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 45,320,000.00 USD | 45,320,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 36,200,000.00 USD | 36,200,000.00 USD | 222,150.00 USD | 97,750.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 44,580,000.00 USD | 44,580,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 35,880,000.00 USD | 35,880,000.00 USD | 113,990.00 USD | 273,720.00 USD | 435,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 43,500,000.00 USD | 43,500,000.00 USD | 0.00 USD | 164,230.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 35,060,000.00 USD | 35,060,000.00 USD | 123,900.00 USD | 0.00 USD | 2,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 43,320,000.00 USD | 43,320,000.00 USD | 51,610.00 USD | 166,160.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.23` | 32,290,000.00 USD | 32,290,000.00 USD | 281,350.00 USD | 575,430.00 USD | 223,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 43,070,000.00 USD | 43,070,000.00 USD | 112,770.00 USD | 535,430.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 31,210,000.00 USD | 31,210,000.00 USD | 452,620.00 USD | 578,850.00 USD | 389,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 42,410,000.00 USD | 42,410,000.00 USD | 59,160.00 USD | 950,550.00 USD | 24,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 29,790,000.00 USD | 29,790,000.00 USD | 170,630.00 USD | 1,010,000.00 USD | 3,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 41,380,000.00 USD | 41,380,000.00 USD | 198,530.00 USD | 888,470.00 USD | 807,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 25,490,000.00 USD | 25,490,000.00 USD | 1,190,000.00 USD | 1,100,000.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 39,480,000.00 USD | 39,480,000.00 USD | 1,020,000.00 USD | 963,040.00 USD | 824,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 20,210,000.00 USD | 20,210,000.00 USD | 340,470.00 USD | 1,190,000.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 36,680,000.00 USD | 36,680,000.00 USD | 1,460,000.00 USD | 1,820,000.00 USD | 3,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 16,990,000.00 USD | 16,990,000.00 USD | 189,670.00 USD | 885,210.00 USD | 558,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 29,530,000.00 USD | 29,530,000.00 USD | 2,040,000.00 USD | 1,800,000.00 USD | 941,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 15,360,000.00 USD | 15,360,000.00 USD | 33,830.00 USD | 224,610.00 USD | 61,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 24,740,000.00 USD | 24,740,000.00 USD | 2,630,000.00 USD | 1,580,000.00 USD | 3,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 15,040,000.00 USD | 15,040,000.00 USD | 618,430.00 USD | 187,820.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 17,040,000.00 USD | 17,040,000.00 USD | 2,070,000.00 USD | 950,140.00 USD | 535,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 12,680,000.00 USD | 12,680,000.00 USD | 319,740.00 USD | 812,380.00 USD | 36,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 13,480,000.00 USD | 13,480,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 11,510,000.00 USD | 11,510,000.00 USD | 1,810,000.00 USD | 5,660.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 12,360,000.00 USD | 12,360,000.00 USD | 1,420,000.00 USD | 15,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 8,520,000.00 USD | 8,520,000.00 USD | 851,070.00 USD | 389,970.00 USD | 414,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 10,920,000.00 USD | 10,920,000.00 USD | 3,370,000.00 USD | 337,070.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 6,860,000.00 USD | 6,860,000.00 USD | 133,680.00 USD | 890,000.00 USD | 544,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 4,920,000.00 USD | 4,920,000.00 USD | 1,630,000.00 USD | 325,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 5,290,000.00 USD | 5,290,000.00 USD | 331,570.00 USD | 171,540.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 9,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 3,780,000.00 USD | 3,780,000.00 USD | 220,120.00 USD | 3,370.00 USD | 196,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 455,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 10,370.00 USD | 669,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 2,510,000.00 USD | 2,510,000.00 USD | 63,660.00 USD | 7,340.00 USD | 878,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.25` | 559.73 USD | 559.73 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.26` | 2,680,000.00 USD | 2,680,000.00 USD | 1,570,000.00 USD | 284,390.00 USD | 369,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 1,560,000.00 USD | 1,560,000.00 USD | 150,010.00 USD | 273,460.00 USD | 783,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.26` | 455,050.00 USD | 455,050.00 USD | 69,930.00 USD | 191,400.00 USD | 193,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 352,210.00 USD | 352,210.00 USD | 0.00 USD | 19,840.00 USD | 239,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 260,790.00 USD | 260,790.00 USD | 208,340.00 USD | 27,670.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 521,580.00 USD | 521,580.00 USD | 208,340.00 USD | 27,670.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.26` | 92,460.00 USD | 92,460.00 USD | 0.00 USD | 10,110.00 USD | 82,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 2,250,000.00 USD | 2,250,000.00 USD | 755,130.00 USD | 100,700.00 USD | 872,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 3,900,000.00 USD | 3,900,000.00 USD | 144,170.00 USD | 26,950.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 6,070,000.00 USD | 6,070,000.00 USD | 772,130.00 USD | 1,180,000.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 9,350,000.00 USD | 9,350,000.00 USD | 834,020.00 USD | 925,190.00 USD | 3,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 116,940.00 USD | 117,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.27` | 10,970,000.00 USD | 10,970,000.00 USD | 1,040,000.00 USD | 1,310,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 25,400,000.00 USD | 25,400,000.00 USD | 4,260,000.00 USD | 3,030,000.00 USD | 8,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 14,430,000.00 USD | 14,430,000.00 USD | 198,110.00 USD | 1,950,000.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 31,150,000.00 USD | 31,150,000.00 USD | 0.00 USD | 1,360,000.00 USD | 4,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 18,630,000.00 USD | 18,630,000.00 USD | 960,010.00 USD | 1,020,000.00 USD | 2,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 34,180,000.00 USD | 34,180,000.00 USD | 138,500.00 USD | 2,540,000.00 USD | 350,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 21,690,000.00 USD | 21,690,000.00 USD | 1,050,000.00 USD | 1,010,000.00 USD | 995,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 41,860,000.00 USD | 41,860,000.00 USD | 1,280,000.00 USD | 4,950,000.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 27,050,000.00 USD | 27,050,000.00 USD | 823,460.00 USD | 1,810,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 54,500,000.00 USD | 54,500,000.00 USD | 2,710,000.00 USD | 2,870,000.00 USD | 7,060,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 15,590.00 USD | 133,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 32,740,000.00 USD | 32,740,000.00 USD | 982,470.00 USD | 2,190,000.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 68,140,000.00 USD | 68,140,000.00 USD | 4,660,000.00 USD | 2,810,000.00 USD | 6,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 43,290,000.00 USD | 43,290,000.00 USD | 4,660,000.00 USD | 1,640,000.00 USD | 4,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 85,250,000.00 USD | 85,250,000.00 USD | 7,780,000.00 USD | 3,210,000.00 USD | 6,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 46,060,000.00 USD | 46,060,000.00 USD | 237,040.00 USD | 1,810,000.00 USD | 721,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 86,770,000.00 USD | 86,770,000.00 USD | 0.00 USD | 1,440,000.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 48,320,000.00 USD | 48,320,000.00 USD | 846,340.00 USD | 100,660.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 87,920,000.00 USD | 87,920,000.00 USD | 1,030,000.00 USD | 30,200.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 50,850,000.00 USD | 50,850,000.00 USD | 985,220.00 USD | 490,930.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 91,300,000.00 USD | 91,300,000.00 USD | 902,470.00 USD | 1,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 48,740.00 USD | 181,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 53,830,000.00 USD | 53,830,000.00 USD | 683,710.00 USD | 939,640.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 94,060,000.00 USD | 94,060,000.00 USD | 796,960.00 USD | 1,290,000.00 USD | 680,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 54,950,000.00 USD | 54,950,000.00 USD | 584,100.00 USD | 427,810.00 USD | 106,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 94,540,000.00 USD | 94,540,000.00 USD | 440,460.00 USD | 2,730.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 55,140,000.00 USD | 55,140,000.00 USD | 95,060.00 USD | 36,830.00 USD | 58,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 95,120,000.00 USD | 95,120,000.00 USD | 70,460.00 USD | 4,320.00 USD | 510,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 57,270,000.00 USD | 57,270,000.00 USD | 378,690.00 USD | 14,980.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 97,210,000.00 USD | 97,210,000.00 USD | 1,040,000.00 USD | 202,640.00 USD | 846,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 61,420,000.00 USD | 61,420,000.00 USD | 1,170,000.00 USD | 375,550.00 USD | 2,600,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 100,860,000.00 USD | 100,860,000.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 66,700,000.00 USD | 66,700,000.00 USD | 1,460,000.00 USD | 1,240,000.00 USD | 2,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 108,150,000.00 USD | 108,150,000.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 67,830,000.00 USD | 67,830,000.00 USD | 464,690.00 USD | 20,370.00 USD | 647,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 110,100,000.00 USD | 110,100,000.00 USD | 25,800.00 USD | 172,080.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 69,130,000.00 USD | 69,130,000.00 USD | 203,220.00 USD | 344,440.00 USD | 752,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 112,100,000.00 USD | 112,100,000.00 USD | 208,510.00 USD | 298,720.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 71,750,000.00 USD | 71,750,000.00 USD | 726,640.00 USD | 871,770.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 113,130,000.00 USD | 113,130,000.00 USD | 85,960.00 USD | 944,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 72,850,000.00 USD | 72,850,000.00 USD | 366,890.00 USD | 250,070.00 USD | 483,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 115,650,000.00 USD | 115,650,000.00 USD | 0.00 USD | 2,040,000.00 USD | 485,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 1,630.00 USD | 183,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 74,210,000.00 USD | 74,210,000.00 USD | 493,480.00 USD | 507,360.00 USD | 358,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 117,600,000.00 USD | 117,600,000.00 USD | 1,770,000.00 USD | 183,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 77,410,000.00 USD | 77,410,000.00 USD | 895,610.00 USD | 341,920.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 122,280,000.00 USD | 122,280,000.00 USD | 1,450,000.00 USD | 821,310.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 80,370,000.00 USD | 80,370,000.00 USD | 1,150,000.00 USD | 326,160.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 124,680,000.00 USD | 124,680,000.00 USD | 1,340,000.00 USD | 408,300.00 USD | 647,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 82,850,000.00 USD | 82,850,000.00 USD | 1,130,000.00 USD | 606,810.00 USD | 745,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 128,660,000.00 USD | 128,660,000.00 USD | 189,510.00 USD | 858,660.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 84,200,000.00 USD | 84,200,000.00 USD | 437,800.00 USD | 146,840.00 USD | 767,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 129,830,000.00 USD | 129,830,000.00 USD | 515,950.00 USD | 151,320.00 USD | 501,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 87,830,000.00 USD | 87,830,000.00 USD | 195,170.00 USD | 875,040.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 134,040,000.00 USD | 134,040,000.00 USD | 68,520.00 USD | 1,750,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 94,440,000.00 USD | 94,440,000.00 USD | 2,070,000.00 USD | 957,920.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 138,880,000.00 USD | 138,880,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 97,390,000.00 USD | 97,390,000.00 USD | 1,570,000.00 USD | 414,530.00 USD | 962,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 140,900,000.00 USD | 140,900,000.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 100,830,000.00 USD | 100,830,000.00 USD | 1,310,000.00 USD | 757,740.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 144,260,000.00 USD | 144,260,000.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 102,700,000.00 USD | 102,700,000.00 USD | 914,960.00 USD | 103,820.00 USD | 851,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 147,040,000.00 USD | 147,040,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 36,960.00 USD | 220,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 103,910,000.00 USD | 103,910,000.00 USD | 552,760.00 USD | 58,200.00 USD | 594,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 148,840,000.00 USD | 148,840,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 105,400,000.00 USD | 105,400,000.00 USD | 578,260.00 USD | 269,680.00 USD | 649,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 149,940,000.00 USD | 149,940,000.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 107,100,000.00 USD | 107,100,000.00 USD | 729,070.00 USD | 105,530.00 USD | 862,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 151,650,000.00 USD | 151,650,000.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 108,920,000.00 USD | 108,920,000.00 USD | 465,720.00 USD | 179,640.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 154,120,000.00 USD | 154,120,000.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 110,780,000.00 USD | 110,780,000.00 USD | 783,210.00 USD | 229,580.00 USD | 838,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 156,150,000.00 USD | 156,150,000.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,950.00 USD | 222,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 111,890,000.00 USD | 111,890,000.00 USD | 286,040.00 USD | 208,270.00 USD | 616,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 157,690,000.00 USD | 157,690,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 112,470,000.00 USD | 112,470,000.00 USD | 289,820.00 USD | 80,370.00 USD | 215,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 160,130,000.00 USD | 160,130,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 113,350,000.00 USD | 113,350,000.00 USD | 353,910.00 USD | 145,200.00 USD | 374,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 162,000,000.00 USD | 162,000,000.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 115,220,000.00 USD | 115,220,000.00 USD | 932,000.00 USD | 374,950.00 USD | 560,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 167,520,000.00 USD | 167,520,000.00 USD | 2,380,000.00 USD | 2,490,000.00 USD | 660,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 117,280,000.00 USD | 117,280,000.00 USD | 820,840.00 USD | 470,890.00 USD | 777,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 174,930,000.00 USD | 174,930,000.00 USD | 2,000,000.00 USD | 2,170,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 17,080.00 USD | 239,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 118,230,000.00 USD | 118,230,000.00 USD | 374,110.00 USD | 172,120.00 USD | 401,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 184,070,000.00 USD | 184,070,000.00 USD | 3,530,000.00 USD | 1,720,000.00 USD | 3,880,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 118,970,000.00 USD | 118,970,000.00 USD | 263,580.00 USD | 78,220.00 USD | 400,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 192,620,000.00 USD | 192,620,000.00 USD | 3,010,000.00 USD | 1,930,000.00 USD | 3,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 119,370,000.00 USD | 119,370,000.00 USD | 200,720.00 USD | 51,130.00 USD | 146,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 200,640,000.00 USD | 200,640,000.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 119,730,000.00 USD | 119,730,000.00 USD | 143,230.00 USD | 29,640.00 USD | 182,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 209,760,000.00 USD | 209,760,000.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 120,170,000.00 USD | 120,170,000.00 USD | 121,440.00 USD | 52,810.00 USD | 271,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 216,510,000.00 USD | 216,510,000.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 2,700.00 USD | 242,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 121,000,000.00 USD | 121,000,000.00 USD | 335,960.00 USD | 65,930.00 USD | 426,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 222,850,000.00 USD | 222,850,000.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 121,500,000.00 USD | 121,500,000.00 USD | 148,530.00 USD | 42,970.00 USD | 310,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 225,400,000.00 USD | 225,400,000.00 USD | 1,060,000.00 USD | 639,580.00 USD | 849,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 122,060,000.00 USD | 122,060,000.00 USD | 269,010.00 USD | 49,330.00 USD | 234,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 228,500,000.00 USD | 228,500,000.00 USD | 1,460,000.00 USD | 414,770.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 122,590,000.00 USD | 122,590,000.00 USD | 143,090.00 USD | 115,680.00 USD | 276,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 232,280,000.00 USD | 232,280,000.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 122,690,000.00 USD | 122,690,000.00 USD | 78,610.00 USD | 14,730.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 235,040,000.00 USD | 235,040,000.00 USD | 1,430,000.00 USD | 616,140.00 USD | 713,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 193,360.00 USD | 435,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 122,960,000.00 USD | 122,960,000.00 USD | 56,040.00 USD | 1,320.00 USD | 206,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 235,860,000.00 USD | 235,860,000.00 USD | 206,650.00 USD | 190,380.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 123,190,000.00 USD | 123,190,000.00 USD | 97,000.00 USD | 109,930.00 USD | 29,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 236,970,000.00 USD | 236,970,000.00 USD | 535,200.00 USD | 181,820.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 123,200,000.00 USD | 123,200,000.00 USD | 0.00 USD | 10,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 238,460,000.00 USD | 238,460,000.00 USD | 415,220.00 USD | 339,760.00 USD | 733,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 123,330,000.00 USD | 123,330,000.00 USD | 5,340.00 USD | 29,850.00 USD | 87,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 240,060,000.00 USD | 240,060,000.00 USD | 553,200.00 USD | 232,110.00 USD | 820,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 123,410,000.00 USD | 123,410,000.00 USD | 5,470.00 USD | 2,460.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 241,980,000.00 USD | 241,980,000.00 USD | 619,020.00 USD | 407,640.00 USD | 893,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 61,720.00 USD | 497,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.38` | 123,580,000.00 USD | 123,580,000.00 USD | 92,060.00 USD | 28,150.00 USD | 50,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 243,210,000.00 USD | 243,210,000.00 USD | 360,280.00 USD | 277,980.00 USD | 586,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 123,830,000.00 USD | 123,830,000.00 USD | 69,610.00 USD | 19,950.00 USD | 166,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 244,670,000.00 USD | 244,670,000.00 USD | 692,200.00 USD | 267,730.00 USD | 499,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 123,950,000.00 USD | 123,950,000.00 USD | 0.00 USD | 41,620.00 USD | 80,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 246,320,000.00 USD | 246,320,000.00 USD | 436,360.00 USD | 142,590.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 124,020,000.00 USD | 124,020,000.00 USD | 0.00 USD | 65,520.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 248,180,000.00 USD | 248,180,000.00 USD | 710,620.00 USD | 348,810.00 USD | 802,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 124,200,000.00 USD | 124,200,000.00 USD | 0.00 USD | 13,730.00 USD | 168,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 248,960,000.00 USD | 248,960,000.00 USD | 403,730.00 USD | 253,120.00 USD | 129,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,280.00 USD | 498,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 124,380,000.00 USD | 124,380,000.00 USD | 63,980.00 USD | 70,910.00 USD | 41,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 249,990,000.00 USD | 249,990,000.00 USD | 377,810.00 USD | 231,880.00 USD | 413,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 124,550,000.00 USD | 124,550,000.00 USD | 40,370.00 USD | 125,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 250,900,000.00 USD | 250,900,000.00 USD | 384,080.00 USD | 308,280.00 USD | 218,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 251,650,000.00 USD | 251,650,000.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 251,980,000.00 USD | 251,980,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 252,040,000.00 USD | 252,040,000.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 2,090.00 USD | 500,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 252,260,000.00 USD | 252,260,000.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 252,270,000.00 USD | 252,270,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 252,330,000.00 USD | 252,330,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 252,410,000.00 USD | 252,410,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 252,700,000.00 USD | 252,700,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 17,770.00 USD | 518,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 252,860,000.00 USD | 252,860,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 253,020,000.00 USD | 253,020,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 253,900,000.00 USD | 253,900,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 254,130,000.00 USD | 254,130,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 254,430,000.00 USD | 254,430,000.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,930.00 USD | 522,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.42` | 254,990,000.00 USD | 254,990,000.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 255,730,000.00 USD | 255,730,000.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 256,780,000.00 USD | 256,780,000.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 258,110,000.00 USD | 258,110,000.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 258,310,000.00 USD | 258,310,000.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 258,630,000.00 USD | 258,630,000.00 USD | 67,230.00 USD | 65,630.00 USD | 183,690.00 USD | `Tier 1 CEX` |
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
| `7D` | `1.07` | 83,800,000.00 USD | 0.00 USD | 83,800,000.00 USD | 23,750.00 USD | 0.00 USD | 39,860.00 USD |
| `7D` | `1.09` | 83,740,000.00 USD | 0.00 USD | 83,740,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `1.09` | 83,690,000.00 USD | 0.00 USD | 83,690,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD |
| `7D` | `1.09` | 83,600,000.00 USD | 0.00 USD | 83,600,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD |
| `7D` | `1.10` | 83,560,000.00 USD | 0.00 USD | 83,560,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD |
| `7D` | `1.10` | 83,550,000.00 USD | 0.00 USD | 83,550,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD |
| `7D` | `1.10` | 83,270,000.00 USD | 0.00 USD | 83,270,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD |
| `7D` | `1.11` | 83,260,000.00 USD | 0.00 USD | 83,260,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD |
| `7D` | `1.11` | 83,260,000.00 USD | 0.00 USD | 83,260,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `7D` | `1.11` | 83,260,000.00 USD | 0.00 USD | 83,260,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD |
| `1D` | `1.11` | 75,000,000.00 USD | 0.00 USD | 75,000,000.00 USD | 88,950.00 USD | 16,870.00 USD | 125,380.00 USD |
| `1D` | `1.12` | 74,770,000.00 USD | 0.00 USD | 74,770,000.00 USD | 0.00 USD | 14,730.00 USD | 3,150.00 USD |
| `7D` | `1.12` | 83,200,000.00 USD | 0.00 USD | 83,200,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `1D` | `1.12` | 74,750,000.00 USD | 0.00 USD | 74,750,000.00 USD | 3,530.00 USD | 1,320.00 USD | 144,950.00 USD |
| `7D` | `1.12` | 83,190,000.00 USD | 0.00 USD | 83,190,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 74,600,000.00 USD | 0.00 USD | 74,600,000.00 USD | 15,020.00 USD | 68,320.00 USD | 29,680.00 USD |
| `1D` | `1.12` | 74,490,000.00 USD | 0.00 USD | 74,490,000.00 USD | 5,340.00 USD | 40,010.00 USD | 87,140.00 USD |
| `7D` | `1.12` | 83,110,000.00 USD | 0.00 USD | 83,110,000.00 USD | 17,190.00 USD | 3,530.00 USD | 0.00 USD |
| `1D` | `1.12` | 74,350,000.00 USD | 0.00 USD | 74,350,000.00 USD | 5,470.00 USD | 2,460.00 USD | 71,880.00 USD |
| `7D` | `1.12` | 83,090,000.00 USD | 0.00 USD | 83,090,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.13` | 74,270,000.00 USD | 0.00 USD | 74,270,000.00 USD | 92,060.00 USD | 28,150.00 USD | 50,130.00 USD |
| `1D` | `1.13` | 74,100,000.00 USD | 0.00 USD | 74,100,000.00 USD | 69,610.00 USD | 19,950.00 USD | 166,510.00 USD |
| `7D` | `1.13` | 82,880,000.00 USD | 0.00 USD | 82,880,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 73,850,000.00 USD | 0.00 USD | 73,850,000.00 USD | 0.00 USD | 107,140.00 USD | 82,360.00 USD |
| `7D` | `1.13` | 82,680,000.00 USD | 0.00 USD | 82,680,000.00 USD | 5,450.00 USD | 2,460.00 USD | 0.00 USD |
| `1D` | `1.13` | 73,660,000.00 USD | 0.00 USD | 73,660,000.00 USD | 0.00 USD | 13,730.00 USD | 168,210.00 USD |
| `7D` | `1.13` | 82,680,000.00 USD | 0.00 USD | 82,680,000.00 USD | 69,750.00 USD | 93,260.00 USD | 8,990.00 USD |
| `1D` | `1.13` | 73,480,000.00 USD | 0.00 USD | 73,480,000.00 USD | 63,980.00 USD | 70,910.00 USD | 41,780.00 USD |
| `7D` | `1.13` | 82,500,000.00 USD | 0.00 USD | 82,500,000.00 USD | 74,920.00 USD | 97,060.00 USD | 224,140.00 USD |
| `1D` | `1.14` | 73,300,000.00 USD | 0.00 USD | 73,300,000.00 USD | 40,370.00 USD | 125,930.00 USD | 0.00 USD |
| `7D` | `1.14` | 82,110,000.00 USD | 0.00 USD | 82,110,000.00 USD | 79,780.00 USD | 88,050.00 USD | 71,350.00 USD |
| `7D` | `1.14` | 81,870,000.00 USD | 0.00 USD | 81,870,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 73,130,000.00 USD | 0.00 USD | 73,130,000.00 USD | 34,800.00 USD | 0.00 USD | 31,230.00 USD |
| `7D` | `1.14` | 81,840,000.00 USD | 0.00 USD | 81,840,000.00 USD | 39,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 73,070,000.00 USD | 0.00 USD | 73,070,000.00 USD | 67,590.00 USD | 749.15 USD | 2,090.00 USD |
| `7D` | `1.14` | 81,800,000.00 USD | 0.00 USD | 81,800,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD |
| `1D` | `1.14` | 73,000,000.00 USD | 0.00 USD | 73,000,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD |
| `7D` | `1.14` | 81,660,000.00 USD | 0.00 USD | 81,660,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.15` | 81,650,000.00 USD | 0.00 USD | 81,650,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `1D` | `1.15` | 72,860,000.00 USD | 0.00 USD | 72,860,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 81,590,000.00 USD | 0.00 USD | 81,590,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD |
| `7D` | `1.15` | 81,220,000.00 USD | 0.00 USD | 81,220,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.15` | 72,850,000.00 USD | 0.00 USD | 72,850,000.00 USD | 1,390.00 USD | 225.14 USD | 64,030.00 USD |
| `7D` | `1.15` | 81,060,000.00 USD | 0.00 USD | 81,060,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 72,780,000.00 USD | 0.00 USD | 72,780,000.00 USD | 73,200.00 USD | 45,600.00 USD | 263,680.00 USD |
| `7D` | `1.15` | 80,900,000.00 USD | 0.00 USD | 80,900,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `1D` | `1.16` | 72,400,000.00 USD | 0.00 USD | 72,400,000.00 USD | 20,480.00 USD | 25,050.00 USD | 82,910.00 USD |
| `7D` | `1.16` | 80,020,000.00 USD | 0.00 USD | 80,020,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 72,270,000.00 USD | 0.00 USD | 72,270,000.00 USD | 122,170.00 USD | 21,140.00 USD | 392,890.00 USD |
| `7D` | `1.16` | 79,780,000.00 USD | 0.00 USD | 79,780,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 71,730,000.00 USD | 0.00 USD | 71,730,000.00 USD | 212,900.00 USD | 76,950.00 USD | 158,690.00 USD |
| `7D` | `1.16` | 78,920,000.00 USD | 0.00 USD | 78,920,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 71,290,000.00 USD | 0.00 USD | 71,290,000.00 USD | 270,110.00 USD | 293,490.00 USD | 148,960.00 USD |
| `7D` | `1.16` | 77,840,000.00 USD | 0.00 USD | 77,840,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD |
| `1D` | `1.16` | 70,570,000.00 USD | 0.00 USD | 70,570,000.00 USD | 179,260.00 USD | 89,000.00 USD | 719,120.00 USD |
| `7D` | `1.16` | 76,540,000.00 USD | 0.00 USD | 76,540,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD |
| `1D` | `1.17` | 69,590,000.00 USD | 0.00 USD | 69,590,000.00 USD | 87,310.00 USD | 70,600.00 USD | 151,280.00 USD |
| `7D` | `1.17` | 74,870,000.00 USD | 0.00 USD | 74,870,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD |
| `1D` | `1.17` | 69,280,000.00 USD | 0.00 USD | 69,280,000.00 USD | 113,470.00 USD | 166,170.00 USD | 170,840.00 USD |
| `7D` | `1.17` | 73,530,000.00 USD | 0.00 USD | 73,530,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 68,830,000.00 USD | 0.00 USD | 68,830,000.00 USD | 162,180.00 USD | 22,610.00 USD | 361,880.00 USD |
| `7D` | `1.17` | 72,460,000.00 USD | 0.00 USD | 72,460,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 68,280,000.00 USD | 0.00 USD | 68,280,000.00 USD | 371,850.00 USD | 25,710.00 USD | 289,390.00 USD |
| `7D` | `1.17` | 70,420,000.00 USD | 0.00 USD | 70,420,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD |
| `1D` | `1.17` | 67,590,000.00 USD | 0.00 USD | 67,590,000.00 USD | 124,360.00 USD | 130,370.00 USD | 474,190.00 USD |
| `7D` | `1.17` | 69,220,000.00 USD | 0.00 USD | 69,220,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD |
| `1D` | `1.18` | 66,860,000.00 USD | 0.00 USD | 66,860,000.00 USD | 304,390.00 USD | 85,620.00 USD | 356,950.00 USD |
| `7D` | `1.18` | 67,650,000.00 USD | 0.00 USD | 67,650,000.00 USD | 181,850.00 USD | 100,190.00 USD | 377,590.00 USD |
| `1D` | `1.18` | 66,120,000.00 USD | 0.00 USD | 66,120,000.00 USD | 71,040.00 USD | 84,480.00 USD | 175,590.00 USD |
| `7D` | `1.18` | 66,990,000.00 USD | 0.00 USD | 66,990,000.00 USD | 85,020.00 USD | 74,230.00 USD | 489,310.00 USD |
| `1D` | `1.18` | 65,790,000.00 USD | 0.00 USD | 65,790,000.00 USD | 113,290.00 USD | 10,150.00 USD | 24,100.00 USD |
| `7D` | `1.18` | 66,340,000.00 USD | 0.00 USD | 66,340,000.00 USD | 270,280.00 USD | 134,360.00 USD | 206,690.00 USD |
| `1D` | `1.18` | 65,640,000.00 USD | 0.00 USD | 65,640,000.00 USD | 222,930.00 USD | 10,160.00 USD | 666,440.00 USD |
| `7D` | `1.18` | 65,730,000.00 USD | 0.00 USD | 65,730,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 64,740,000.00 USD | 0.00 USD | 64,740,000.00 USD | 196,910.00 USD | 73,630.00 USD | 143,880.00 USD |
| `7D` | `1.18` | 65,470,000.00 USD | 0.00 USD | 65,470,000.00 USD | 299,450.00 USD | 571,980.00 USD | 235,490.00 USD |
| `1D` | `1.19` | 64,320,000.00 USD | 0.00 USD | 64,320,000.00 USD | 86,540.00 USD | 511,780.00 USD | 65,030.00 USD |
| `7D` | `1.19` | 64,360,000.00 USD | 0.00 USD | 64,360,000.00 USD | 76,370.00 USD | 109,420.00 USD | 706,450.00 USD |
| `1D` | `1.19` | 63,660,000.00 USD | 0.00 USD | 63,660,000.00 USD | 365,260.00 USD | 93,260.00 USD | 1,570,000.00 USD |
| `7D` | `1.19` | 63,470,000.00 USD | 0.00 USD | 63,470,000.00 USD | 250,710.00 USD | 93,330.00 USD | 585,020.00 USD |
| `1D` | `1.19` | 61,630,000.00 USD | 0.00 USD | 61,630,000.00 USD | 110,600.00 USD | 45,410.00 USD | 319,610.00 USD |
| `7D` | `1.19` | 62,540,000.00 USD | 0.00 USD | 62,540,000.00 USD | 227,280.00 USD | 92,240.00 USD | 795,050.00 USD |
| `1D` | `1.19` | 61,160,000.00 USD | 0.00 USD | 61,160,000.00 USD | 147,820.00 USD | 199,810.00 USD | 469,390.00 USD |
| `7D` | `1.19` | 61,420,000.00 USD | 0.00 USD | 61,420,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD |
| `1D` | `1.19` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 190,850.00 USD | 428,210.00 USD | 1,690,000.00 USD |
| `7D` | `1.19` | 60,060,000.00 USD | 0.00 USD | 60,060,000.00 USD | 220,490.00 USD | 59,450.00 USD | 554,090.00 USD |
| `1D` | `1.20` | 58,030,000.00 USD | 0.00 USD | 58,030,000.00 USD | 784,530.00 USD | 121,000.00 USD | 1,220,000.00 USD |
| `7D` | `1.20` | 59,230,000.00 USD | 0.00 USD | 59,230,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 272,370.00 USD |
| `1D` | `1.20` | 55,910,000.00 USD | 0.00 USD | 55,910,000.00 USD | 264,550.00 USD | 834,460.00 USD | 657,850.00 USD |
| `7D` | `1.20` | 57,640,000.00 USD | 0.00 USD | 57,640,000.00 USD | 31,150.00 USD | 372,080.00 USD | 2,610,000.00 USD |
| `1D` | `1.20` | 54,150,000.00 USD | 0.00 USD | 54,150,000.00 USD | 708,890.00 USD | 419,750.00 USD | 2,300,000.00 USD |
| `7D` | `1.20` | 54,630,000.00 USD | 0.00 USD | 54,630,000.00 USD | 736,290.00 USD | 330,310.00 USD | 18,590.00 USD |
| `1D` | `1.20` | 50,720,000.00 USD | 0.00 USD | 50,720,000.00 USD | 137,910.00 USD | 157,180.00 USD | 820,430.00 USD |
| `7D` | `1.20` | 53,550,000.00 USD | 0.00 USD | 53,550,000.00 USD | 264,000.00 USD | 144,630.00 USD | 464,230.00 USD |
| `1D` | `1.20` | 49,600,000.00 USD | 0.00 USD | 49,600,000.00 USD | 526,510.00 USD | 511,570.00 USD | 374,680.00 USD |
| `7D` | `1.20` | 52,680,000.00 USD | 0.00 USD | 52,680,000.00 USD | 47,500.00 USD | 589,990.00 USD | 5,570.00 USD |
| `1D` | `1.21` | 48,190,000.00 USD | 0.00 USD | 48,190,000.00 USD | 328,050.00 USD | 532,540.00 USD | 275,970.00 USD |
| `7D` | `1.21` | 52,030,000.00 USD | 0.00 USD | 52,030,000.00 USD | 0.00 USD | 22,600.00 USD | 0.00 USD |
| `1D` | `1.21` | 47,050,000.00 USD | 0.00 USD | 47,050,000.00 USD | 1,660,000.00 USD | 193,480.00 USD | 1,670,000.00 USD |
| `7D` | `1.21` | 52,010,000.00 USD | 0.00 USD | 52,010,000.00 USD | 456,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.21` | 43,530,000.00 USD | 0.00 USD | 43,530,000.00 USD | 533,310.00 USD | 413,110.00 USD | 1,070,000.00 USD |
| `7D` | `1.21` | 51,550,000.00 USD | 0.00 USD | 51,550,000.00 USD | 257,960.00 USD | 492,370.00 USD | 3,090,000.00 USD |
| `1D` | `1.21` | 41,520,000.00 USD | 0.00 USD | 41,520,000.00 USD | 1,410,000.00 USD | 572,260.00 USD | 1,020,000.00 USD |
| `7D` | `1.21` | 47,720,000.00 USD | 0.00 USD | 47,720,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.21` | 38,520,000.00 USD | 0.00 USD | 38,520,000.00 USD | 0.00 USD | 90,950.00 USD | 898,860.00 USD |
| `7D` | `1.21` | 46,490,000.00 USD | 0.00 USD | 46,490,000.00 USD | 108,640.00 USD | 0.00 USD | 910,410.00 USD |
| `1D` | `1.22` | 37,530,000.00 USD | 0.00 USD | 37,530,000.00 USD | 226,520.00 USD | 85,640.00 USD | 680,350.00 USD |
| `7D` | `1.22` | 45,470,000.00 USD | 0.00 USD | 45,470,000.00 USD | 142,210.00 USD | 9,150.00 USD | 0.00 USD |
| `1D` | `1.22` | 36,530,000.00 USD | 0.00 USD | 36,530,000.00 USD | 143,650.00 USD | 4,200.00 USD | 183,070.00 USD |
| `7D` | `1.22` | 45,320,000.00 USD | 0.00 USD | 45,320,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD |
| `1D` | `1.22` | 36,200,000.00 USD | 0.00 USD | 36,200,000.00 USD | 222,150.00 USD | 97,750.00 USD | 4,090.00 USD |
| `7D` | `1.22` | 44,580,000.00 USD | 0.00 USD | 44,580,000.00 USD | 138,500.00 USD | 928,300.00 USD | 19,450.00 USD |
| `1D` | `1.22` | 35,880,000.00 USD | 0.00 USD | 35,880,000.00 USD | 113,990.00 USD | 273,720.00 USD | 435,680.00 USD |
| `7D` | `1.22` | 43,500,000.00 USD | 0.00 USD | 43,500,000.00 USD | 0.00 USD | 164,230.00 USD | 11,370.00 USD |
| `1D` | `1.22` | 35,060,000.00 USD | 0.00 USD | 35,060,000.00 USD | 123,900.00 USD | 0.00 USD | 2,640,000.00 USD |
| `7D` | `1.22` | 43,320,000.00 USD | 0.00 USD | 43,320,000.00 USD | 51,610.00 USD | 166,160.00 USD | 33,260.00 USD |
| `1D` | `1.23` | 32,290,000.00 USD | 0.00 USD | 32,290,000.00 USD | 281,350.00 USD | 575,430.00 USD | 223,320.00 USD |
| `7D` | `1.23` | 43,070,000.00 USD | 0.00 USD | 43,070,000.00 USD | 112,770.00 USD | 535,430.00 USD | 9,210.00 USD |
| `1D` | `1.23` | 31,210,000.00 USD | 0.00 USD | 31,210,000.00 USD | 452,620.00 USD | 578,850.00 USD | 389,390.00 USD |
| `7D` | `1.23` | 42,410,000.00 USD | 0.00 USD | 42,410,000.00 USD | 59,160.00 USD | 950,550.00 USD | 24,470.00 USD |
| `1D` | `1.23` | 29,790,000.00 USD | 0.00 USD | 29,790,000.00 USD | 170,630.00 USD | 1,010,000.00 USD | 3,130,000.00 USD |
| `7D` | `1.23` | 41,380,000.00 USD | 0.00 USD | 41,380,000.00 USD | 198,530.00 USD | 888,470.00 USD | 807,050.00 USD |
| `1D` | `1.23` | 25,490,000.00 USD | 0.00 USD | 25,490,000.00 USD | 1,190,000.00 USD | 1,100,000.00 USD | 2,990,000.00 USD |
| `7D` | `1.23` | 39,480,000.00 USD | 0.00 USD | 39,480,000.00 USD | 1,020,000.00 USD | 963,040.00 USD | 824,300.00 USD |
| `1D` | `1.23` | 20,210,000.00 USD | 0.00 USD | 20,210,000.00 USD | 340,470.00 USD | 1,190,000.00 USD | 1,690,000.00 USD |
| `7D` | `1.23` | 36,680,000.00 USD | 0.00 USD | 36,680,000.00 USD | 1,460,000.00 USD | 1,820,000.00 USD | 3,860,000.00 USD |
| `1D` | `1.24` | 16,990,000.00 USD | 0.00 USD | 16,990,000.00 USD | 189,670.00 USD | 885,210.00 USD | 558,770.00 USD |
| `7D` | `1.24` | 29,530,000.00 USD | 0.00 USD | 29,530,000.00 USD | 2,040,000.00 USD | 1,800,000.00 USD | 941,570.00 USD |
| `1D` | `1.24` | 15,360,000.00 USD | 0.00 USD | 15,360,000.00 USD | 33,830.00 USD | 224,610.00 USD | 61,110.00 USD |
| `7D` | `1.24` | 24,740,000.00 USD | 0.00 USD | 24,740,000.00 USD | 2,630,000.00 USD | 1,580,000.00 USD | 3,490,000.00 USD |
| `1D` | `1.24` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 618,430.00 USD | 187,820.00 USD | 1,550,000.00 USD |
| `7D` | `1.24` | 17,040,000.00 USD | 0.00 USD | 17,040,000.00 USD | 2,070,000.00 USD | 950,140.00 USD | 535,960.00 USD |
| `1D` | `1.24` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 319,740.00 USD | 812,380.00 USD | 36,980.00 USD |
| `7D` | `1.24` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.24` | 11,510,000.00 USD | 0.00 USD | 11,510,000.00 USD | 1,810,000.00 USD | 5,660.00 USD | 1,170,000.00 USD |
| `7D` | `1.24` | 12,360,000.00 USD | 0.00 USD | 12,360,000.00 USD | 1,420,000.00 USD | 15,000.00 USD | 0.00 USD |
| `1D` | `1.25` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 851,070.00 USD | 389,970.00 USD | 414,640.00 USD |
| `7D` | `1.25` | 10,920,000.00 USD | 0.00 USD | 10,920,000.00 USD | 3,370,000.00 USD | 337,070.00 USD | 2,290,000.00 USD |
| `1D` | `1.25` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 133,680.00 USD | 890,000.00 USD | 544,830.00 USD |
| `7D` | `1.25` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 1,630,000.00 USD | 325,530.00 USD | 0.00 USD |
| `1D` | `1.25` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 331,570.00 USD | 171,540.00 USD | 1,010,000.00 USD |
| `7D` | `1.25` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 0.00 USD | 9,140.00 USD | 0.00 USD |
| `1D` | `1.25` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 220,120.00 USD | 3,370.00 USD | 196,500.00 USD |
| `7D` | `1.25` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 455,200.00 USD |
| `1D` | `1.25` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 0.00 USD | 10,370.00 USD | 669,770.00 USD |
| `7D` | `1.25` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 63,660.00 USD | 7,340.00 USD | 878,920.00 USD |
| `1D` | `1.26` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 1,570,000.00 USD | 284,390.00 USD | 369,510.00 USD |
| `7D` | `1.26` | 1,560,000.00 USD | 0.00 USD | 1,560,000.00 USD | 150,010.00 USD | 273,460.00 USD | 783,060.00 USD |
| `1D` | `1.26` | 455,050.00 USD | 0.00 USD | 455,050.00 USD | 69,930.00 USD | 191,400.00 USD | 193,710.00 USD |
| `7D` | `1.26` | 352,210.00 USD | 0.00 USD | 352,210.00 USD | 0.00 USD | 19,840.00 USD | 239,910.00 USD |
| `1D` | `1.26` | 260,790.00 USD | 260,790.00 USD | 0.00 USD | 208,340.00 USD | 27,670.00 USD | 24,770.00 USD |
| `1D` | `1.26` | 521,580.00 USD | 521,580.00 USD | 0.00 USD | 208,340.00 USD | 27,670.00 USD | 24,770.00 USD |
| `7D` | `1.26` | 92,460.00 USD | 0.00 USD | 92,460.00 USD | 0.00 USD | 10,110.00 USD | 82,350.00 USD |
| `7D` | `1.26` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 755,130.00 USD | 100,700.00 USD | 872,590.00 USD |
| `7D` | `1.26` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 144,170.00 USD | 26,950.00 USD | 3,730,000.00 USD |
| `1D` | `1.26` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 772,130.00 USD | 1,180,000.00 USD | 1,860,000.00 USD |
| `7D` | `1.26` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 834,020.00 USD | 925,190.00 USD | 3,700,000.00 USD |
| `1D` | `1.27` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 1,040,000.00 USD | 1,310,000.00 USD | 2,550,000.00 USD |
| `7D` | `1.27` | 25,400,000.00 USD | 25,400,000.00 USD | 0.00 USD | 4,260,000.00 USD | 3,030,000.00 USD | 8,760,000.00 USD |
| `1D` | `1.27` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 198,110.00 USD | 1,950,000.00 USD | 1,310,000.00 USD |
| `7D` | `1.27` | 31,150,000.00 USD | 31,150,000.00 USD | 0.00 USD | 0.00 USD | 1,360,000.00 USD | 4,400,000.00 USD |
| `1D` | `1.27` | 18,630,000.00 USD | 18,630,000.00 USD | 0.00 USD | 960,010.00 USD | 1,020,000.00 USD | 2,230,000.00 USD |
| `7D` | `1.27` | 34,180,000.00 USD | 34,180,000.00 USD | 0.00 USD | 138,500.00 USD | 2,540,000.00 USD | 350,390.00 USD |
| `1D` | `1.27` | 21,690,000.00 USD | 21,690,000.00 USD | 0.00 USD | 1,050,000.00 USD | 1,010,000.00 USD | 995,930.00 USD |
| `7D` | `1.27` | 41,860,000.00 USD | 41,860,000.00 USD | 0.00 USD | 1,280,000.00 USD | 4,950,000.00 USD | 1,450,000.00 USD |
| `1D` | `1.27` | 27,050,000.00 USD | 27,050,000.00 USD | 0.00 USD | 823,460.00 USD | 1,810,000.00 USD | 2,730,000.00 USD |
| `7D` | `1.27` | 54,500,000.00 USD | 54,500,000.00 USD | 0.00 USD | 2,710,000.00 USD | 2,870,000.00 USD | 7,060,000.00 USD |
| `1D` | `1.28` | 32,740,000.00 USD | 32,740,000.00 USD | 0.00 USD | 982,470.00 USD | 2,190,000.00 USD | 2,510,000.00 USD |
| `7D` | `1.28` | 68,140,000.00 USD | 68,140,000.00 USD | 0.00 USD | 4,660,000.00 USD | 2,810,000.00 USD | 6,170,000.00 USD |
| `1D` | `1.28` | 43,290,000.00 USD | 43,290,000.00 USD | 0.00 USD | 4,660,000.00 USD | 1,640,000.00 USD | 4,250,000.00 USD |
| `7D` | `1.28` | 85,250,000.00 USD | 85,250,000.00 USD | 0.00 USD | 7,780,000.00 USD | 3,210,000.00 USD | 6,120,000.00 USD |
| `1D` | `1.28` | 46,060,000.00 USD | 46,060,000.00 USD | 0.00 USD | 237,040.00 USD | 1,810,000.00 USD | 721,180.00 USD |
| `7D` | `1.28` | 86,770,000.00 USD | 86,770,000.00 USD | 0.00 USD | 0.00 USD | 1,440,000.00 USD | 84,070.00 USD |
| `1D` | `1.28` | 48,320,000.00 USD | 48,320,000.00 USD | 0.00 USD | 846,340.00 USD | 100,660.00 USD | 1,320,000.00 USD |
| `7D` | `1.28` | 87,920,000.00 USD | 87,920,000.00 USD | 0.00 USD | 1,030,000.00 USD | 30,200.00 USD | 85,990.00 USD |
| `1D` | `1.28` | 50,850,000.00 USD | 50,850,000.00 USD | 0.00 USD | 985,220.00 USD | 490,930.00 USD | 1,050,000.00 USD |
| `7D` | `1.28` | 91,300,000.00 USD | 91,300,000.00 USD | 0.00 USD | 902,470.00 USD | 1,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `1.29` | 53,830,000.00 USD | 53,830,000.00 USD | 0.00 USD | 683,710.00 USD | 939,640.00 USD | 1,350,000.00 USD |
| `7D` | `1.29` | 94,060,000.00 USD | 94,060,000.00 USD | 0.00 USD | 796,960.00 USD | 1,290,000.00 USD | 680,350.00 USD |
| `1D` | `1.29` | 54,950,000.00 USD | 54,950,000.00 USD | 0.00 USD | 584,100.00 USD | 427,810.00 USD | 106,320.00 USD |
| `7D` | `1.29` | 94,540,000.00 USD | 94,540,000.00 USD | 0.00 USD | 440,460.00 USD | 2,730.00 USD | 33,260.00 USD |
| `1D` | `1.29` | 55,140,000.00 USD | 55,140,000.00 USD | 0.00 USD | 95,060.00 USD | 36,830.00 USD | 58,760.00 USD |
| `7D` | `1.29` | 95,120,000.00 USD | 95,120,000.00 USD | 0.00 USD | 70,460.00 USD | 4,320.00 USD | 510,220.00 USD |
| `1D` | `1.29` | 57,270,000.00 USD | 57,270,000.00 USD | 0.00 USD | 378,690.00 USD | 14,980.00 USD | 1,740,000.00 USD |
| `7D` | `1.29` | 97,210,000.00 USD | 97,210,000.00 USD | 0.00 USD | 1,040,000.00 USD | 202,640.00 USD | 846,810.00 USD |
| `1D` | `1.29` | 61,420,000.00 USD | 61,420,000.00 USD | 0.00 USD | 1,170,000.00 USD | 375,550.00 USD | 2,600,000.00 USD |
| `7D` | `1.29` | 100,860,000.00 USD | 100,860,000.00 USD | 0.00 USD | 1,770,000.00 USD | 8,810.00 USD | 1,870,000.00 USD |
| `1D` | `1.30` | 66,700,000.00 USD | 66,700,000.00 USD | 0.00 USD | 1,460,000.00 USD | 1,240,000.00 USD | 2,570,000.00 USD |
| `7D` | `1.30` | 108,150,000.00 USD | 108,150,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 3,730,000.00 USD |
| `1D` | `1.30` | 67,830,000.00 USD | 67,830,000.00 USD | 0.00 USD | 464,690.00 USD | 20,370.00 USD | 647,970.00 USD |
| `7D` | `1.30` | 110,100,000.00 USD | 110,100,000.00 USD | 0.00 USD | 25,800.00 USD | 172,080.00 USD | 1,750,000.00 USD |
| `1D` | `1.30` | 69,130,000.00 USD | 69,130,000.00 USD | 0.00 USD | 203,220.00 USD | 344,440.00 USD | 752,990.00 USD |
| `7D` | `1.30` | 112,100,000.00 USD | 112,100,000.00 USD | 0.00 USD | 208,510.00 USD | 298,720.00 USD | 1,490,000.00 USD |
| `1D` | `1.30` | 71,750,000.00 USD | 71,750,000.00 USD | 0.00 USD | 726,640.00 USD | 871,770.00 USD | 1,020,000.00 USD |
| `7D` | `1.30` | 113,130,000.00 USD | 113,130,000.00 USD | 0.00 USD | 85,960.00 USD | 944,610.00 USD | 0.00 USD |
| `1D` | `1.30` | 72,850,000.00 USD | 72,850,000.00 USD | 0.00 USD | 366,890.00 USD | 250,070.00 USD | 483,560.00 USD |
| `7D` | `1.30` | 115,650,000.00 USD | 115,650,000.00 USD | 0.00 USD | 0.00 USD | 2,040,000.00 USD | 485,710.00 USD |
| `1D` | `1.31` | 74,210,000.00 USD | 74,210,000.00 USD | 0.00 USD | 493,480.00 USD | 507,360.00 USD | 358,310.00 USD |
| `7D` | `1.31` | 117,600,000.00 USD | 117,600,000.00 USD | 0.00 USD | 1,770,000.00 USD | 183,660.00 USD | 0.00 USD |
| `1D` | `1.31` | 77,410,000.00 USD | 77,410,000.00 USD | 0.00 USD | 895,610.00 USD | 341,920.00 USD | 1,960,000.00 USD |
| `7D` | `1.31` | 122,280,000.00 USD | 122,280,000.00 USD | 0.00 USD | 1,450,000.00 USD | 821,310.00 USD | 2,400,000.00 USD |
| `1D` | `1.31` | 80,370,000.00 USD | 80,370,000.00 USD | 0.00 USD | 1,150,000.00 USD | 326,160.00 USD | 1,480,000.00 USD |
| `7D` | `1.31` | 124,680,000.00 USD | 124,680,000.00 USD | 0.00 USD | 1,340,000.00 USD | 408,300.00 USD | 647,870.00 USD |
| `1D` | `1.31` | 82,850,000.00 USD | 82,850,000.00 USD | 0.00 USD | 1,130,000.00 USD | 606,810.00 USD | 745,480.00 USD |
| `7D` | `1.31` | 128,660,000.00 USD | 128,660,000.00 USD | 0.00 USD | 189,510.00 USD | 858,660.00 USD | 2,930,000.00 USD |
| `1D` | `1.31` | 84,200,000.00 USD | 84,200,000.00 USD | 0.00 USD | 437,800.00 USD | 146,840.00 USD | 767,230.00 USD |
| `7D` | `1.31` | 129,830,000.00 USD | 129,830,000.00 USD | 0.00 USD | 515,950.00 USD | 151,320.00 USD | 501,780.00 USD |
| `1D` | `1.32` | 87,830,000.00 USD | 87,830,000.00 USD | 0.00 USD | 195,170.00 USD | 875,040.00 USD | 2,560,000.00 USD |
| `7D` | `1.32` | 134,040,000.00 USD | 134,040,000.00 USD | 0.00 USD | 68,520.00 USD | 1,750,000.00 USD | 2,380,000.00 USD |
| `1D` | `1.32` | 94,440,000.00 USD | 94,440,000.00 USD | 0.00 USD | 2,070,000.00 USD | 957,920.00 USD | 3,590,000.00 USD |
| `7D` | `1.32` | 138,880,000.00 USD | 138,880,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 2,820,000.00 USD |
| `1D` | `1.32` | 97,390,000.00 USD | 97,390,000.00 USD | 0.00 USD | 1,570,000.00 USD | 414,530.00 USD | 962,970.00 USD |
| `7D` | `1.32` | 140,900,000.00 USD | 140,900,000.00 USD | 0.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 100,830,000.00 USD | 100,830,000.00 USD | 0.00 USD | 1,310,000.00 USD | 757,740.00 USD | 1,380,000.00 USD |
| `7D` | `1.32` | 144,260,000.00 USD | 144,260,000.00 USD | 0.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 102,700,000.00 USD | 102,700,000.00 USD | 0.00 USD | 914,960.00 USD | 103,820.00 USD | 851,430.00 USD |
| `7D` | `1.32` | 147,040,000.00 USD | 147,040,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD |
| `1D` | `1.33` | 103,910,000.00 USD | 103,910,000.00 USD | 0.00 USD | 552,760.00 USD | 58,200.00 USD | 594,720.00 USD |
| `7D` | `1.33` | 148,840,000.00 USD | 148,840,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 105,400,000.00 USD | 105,400,000.00 USD | 0.00 USD | 578,260.00 USD | 269,680.00 USD | 649,240.00 USD |
| `7D` | `1.33` | 149,940,000.00 USD | 149,940,000.00 USD | 0.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 107,100,000.00 USD | 107,100,000.00 USD | 0.00 USD | 729,070.00 USD | 105,530.00 USD | 862,480.00 USD |
| `7D` | `1.33` | 151,650,000.00 USD | 151,650,000.00 USD | 0.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 108,920,000.00 USD | 108,920,000.00 USD | 0.00 USD | 465,720.00 USD | 179,640.00 USD | 1,180,000.00 USD |
| `7D` | `1.33` | 154,120,000.00 USD | 154,120,000.00 USD | 0.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD |
| `1D` | `1.33` | 110,780,000.00 USD | 110,780,000.00 USD | 0.00 USD | 783,210.00 USD | 229,580.00 USD | 838,970.00 USD |
| `7D` | `1.33` | 156,150,000.00 USD | 156,150,000.00 USD | 0.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD |
| `1D` | `1.34` | 111,890,000.00 USD | 111,890,000.00 USD | 0.00 USD | 286,040.00 USD | 208,270.00 USD | 616,920.00 USD |
| `7D` | `1.34` | 157,690,000.00 USD | 157,690,000.00 USD | 0.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 112,470,000.00 USD | 112,470,000.00 USD | 0.00 USD | 289,820.00 USD | 80,370.00 USD | 215,870.00 USD |
| `7D` | `1.34` | 160,130,000.00 USD | 160,130,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 113,350,000.00 USD | 113,350,000.00 USD | 0.00 USD | 353,910.00 USD | 145,200.00 USD | 374,680.00 USD |
| `7D` | `1.34` | 162,000,000.00 USD | 162,000,000.00 USD | 0.00 USD | 804,660.00 USD | 472,920.00 USD | 588,220.00 USD |
| `1D` | `1.34` | 115,220,000.00 USD | 115,220,000.00 USD | 0.00 USD | 932,000.00 USD | 374,950.00 USD | 560,930.00 USD |
| `7D` | `1.34` | 167,520,000.00 USD | 167,520,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,490,000.00 USD | 660,660.00 USD |
| `1D` | `1.34` | 117,280,000.00 USD | 117,280,000.00 USD | 0.00 USD | 820,840.00 USD | 470,890.00 USD | 777,090.00 USD |
| `7D` | `1.34` | 174,930,000.00 USD | 174,930,000.00 USD | 0.00 USD | 2,000,000.00 USD | 2,170,000.00 USD | 3,240,000.00 USD |
| `1D` | `1.35` | 118,230,000.00 USD | 118,230,000.00 USD | 0.00 USD | 374,110.00 USD | 172,120.00 USD | 401,650.00 USD |
| `7D` | `1.35` | 184,070,000.00 USD | 184,070,000.00 USD | 0.00 USD | 3,530,000.00 USD | 1,720,000.00 USD | 3,880,000.00 USD |
| `1D` | `1.35` | 118,970,000.00 USD | 118,970,000.00 USD | 0.00 USD | 263,580.00 USD | 78,220.00 USD | 400,600.00 USD |
| `7D` | `1.35` | 192,620,000.00 USD | 192,620,000.00 USD | 0.00 USD | 3,010,000.00 USD | 1,930,000.00 USD | 3,610,000.00 USD |
| `1D` | `1.35` | 119,370,000.00 USD | 119,370,000.00 USD | 0.00 USD | 200,720.00 USD | 51,130.00 USD | 146,530.00 USD |
| `7D` | `1.35` | 200,640,000.00 USD | 200,640,000.00 USD | 0.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD |
| `1D` | `1.35` | 119,730,000.00 USD | 119,730,000.00 USD | 0.00 USD | 143,230.00 USD | 29,640.00 USD | 182,590.00 USD |
| `7D` | `1.35` | 209,760,000.00 USD | 209,760,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 120,170,000.00 USD | 120,170,000.00 USD | 0.00 USD | 121,440.00 USD | 52,810.00 USD | 271,610.00 USD |
| `7D` | `1.35` | 216,510,000.00 USD | 216,510,000.00 USD | 0.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD |
| `1D` | `1.36` | 121,000,000.00 USD | 121,000,000.00 USD | 0.00 USD | 335,960.00 USD | 65,930.00 USD | 426,530.00 USD |
| `7D` | `1.36` | 222,850,000.00 USD | 222,850,000.00 USD | 0.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD |
| `1D` | `1.36` | 121,500,000.00 USD | 121,500,000.00 USD | 0.00 USD | 148,530.00 USD | 42,970.00 USD | 310,320.00 USD |
| `7D` | `1.36` | 225,400,000.00 USD | 225,400,000.00 USD | 0.00 USD | 1,060,000.00 USD | 639,580.00 USD | 849,400.00 USD |
| `1D` | `1.36` | 122,060,000.00 USD | 122,060,000.00 USD | 0.00 USD | 269,010.00 USD | 49,330.00 USD | 234,460.00 USD |
| `7D` | `1.36` | 228,500,000.00 USD | 228,500,000.00 USD | 0.00 USD | 1,460,000.00 USD | 414,770.00 USD | 1,230,000.00 USD |
| `1D` | `1.36` | 122,590,000.00 USD | 122,590,000.00 USD | 0.00 USD | 143,090.00 USD | 115,680.00 USD | 276,810.00 USD |
| `7D` | `1.36` | 232,280,000.00 USD | 232,280,000.00 USD | 0.00 USD | 1,520,000.00 USD | 765,630.00 USD | 1,500,000.00 USD |
| `1D` | `1.36` | 122,690,000.00 USD | 122,690,000.00 USD | 0.00 USD | 78,610.00 USD | 14,730.00 USD | 6,070.00 USD |
| `7D` | `1.36` | 235,040,000.00 USD | 235,040,000.00 USD | 0.00 USD | 1,430,000.00 USD | 616,140.00 USD | 713,350.00 USD |
| `1D` | `1.37` | 122,960,000.00 USD | 122,960,000.00 USD | 0.00 USD | 56,040.00 USD | 1,320.00 USD | 206,760.00 USD |
| `7D` | `1.37` | 235,860,000.00 USD | 235,860,000.00 USD | 0.00 USD | 206,650.00 USD | 190,380.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 123,190,000.00 USD | 123,190,000.00 USD | 0.00 USD | 97,000.00 USD | 109,930.00 USD | 29,680.00 USD |
| `7D` | `1.37` | 236,970,000.00 USD | 236,970,000.00 USD | 0.00 USD | 535,200.00 USD | 181,820.00 USD | 389,280.00 USD |
| `1D` | `1.37` | 123,200,000.00 USD | 123,200,000.00 USD | 0.00 USD | 0.00 USD | 10,160.00 USD | 0.00 USD |
| `7D` | `1.37` | 238,460,000.00 USD | 238,460,000.00 USD | 0.00 USD | 415,220.00 USD | 339,760.00 USD | 733,820.00 USD |
| `1D` | `1.37` | 123,330,000.00 USD | 123,330,000.00 USD | 0.00 USD | 5,340.00 USD | 29,850.00 USD | 87,140.00 USD |
| `7D` | `1.37` | 240,060,000.00 USD | 240,060,000.00 USD | 0.00 USD | 553,200.00 USD | 232,110.00 USD | 820,700.00 USD |
| `1D` | `1.37` | 123,410,000.00 USD | 123,410,000.00 USD | 0.00 USD | 5,470.00 USD | 2,460.00 USD | 71,880.00 USD |
| `7D` | `1.37` | 241,980,000.00 USD | 241,980,000.00 USD | 0.00 USD | 619,020.00 USD | 407,640.00 USD | 893,850.00 USD |
| `1D` | `1.38` | 123,580,000.00 USD | 123,580,000.00 USD | 0.00 USD | 92,060.00 USD | 28,150.00 USD | 50,130.00 USD |
| `7D` | `1.38` | 243,210,000.00 USD | 243,210,000.00 USD | 0.00 USD | 360,280.00 USD | 277,980.00 USD | 586,390.00 USD |
| `1D` | `1.38` | 123,830,000.00 USD | 123,830,000.00 USD | 0.00 USD | 69,610.00 USD | 19,950.00 USD | 166,510.00 USD |
| `7D` | `1.38` | 244,670,000.00 USD | 244,670,000.00 USD | 0.00 USD | 692,200.00 USD | 267,730.00 USD | 499,710.00 USD |
| `1D` | `1.38` | 123,950,000.00 USD | 123,950,000.00 USD | 0.00 USD | 0.00 USD | 41,620.00 USD | 80,220.00 USD |
| `7D` | `1.38` | 246,320,000.00 USD | 246,320,000.00 USD | 0.00 USD | 436,360.00 USD | 142,590.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 124,020,000.00 USD | 124,020,000.00 USD | 0.00 USD | 0.00 USD | 65,520.00 USD | 2,140.00 USD |
| `7D` | `1.38` | 248,180,000.00 USD | 248,180,000.00 USD | 0.00 USD | 710,620.00 USD | 348,810.00 USD | 802,530.00 USD |
| `1D` | `1.38` | 124,200,000.00 USD | 124,200,000.00 USD | 0.00 USD | 0.00 USD | 13,730.00 USD | 168,210.00 USD |
| `7D` | `1.38` | 248,960,000.00 USD | 248,960,000.00 USD | 0.00 USD | 403,730.00 USD | 253,120.00 USD | 129,320.00 USD |
| `1D` | `1.39` | 124,380,000.00 USD | 124,380,000.00 USD | 0.00 USD | 63,980.00 USD | 70,910.00 USD | 41,780.00 USD |
| `7D` | `1.39` | 249,990,000.00 USD | 249,990,000.00 USD | 0.00 USD | 377,810.00 USD | 231,880.00 USD | 413,510.00 USD |
| `1D` | `1.39` | 124,550,000.00 USD | 124,550,000.00 USD | 0.00 USD | 40,370.00 USD | 125,320.00 USD | 0.00 USD |
| `7D` | `1.39` | 250,900,000.00 USD | 250,900,000.00 USD | 0.00 USD | 384,080.00 USD | 308,280.00 USD | 218,620.00 USD |
| `7D` | `1.39` | 251,650,000.00 USD | 251,650,000.00 USD | 0.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD |
| `7D` | `1.39` | 251,980,000.00 USD | 251,980,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `7D` | `1.39` | 252,040,000.00 USD | 252,040,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 0.00 USD |
| `7D` | `1.40` | 252,260,000.00 USD | 252,260,000.00 USD | 0.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD |
| `7D` | `1.40` | 252,270,000.00 USD | 252,270,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 252,330,000.00 USD | 252,330,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 252,410,000.00 USD | 252,410,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `7D` | `1.40` | 252,700,000.00 USD | 252,700,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 252,860,000.00 USD | 252,860,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.41` | 253,020,000.00 USD | 253,020,000.00 USD | 0.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `7D` | `1.41` | 253,900,000.00 USD | 253,900,000.00 USD | 0.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `7D` | `1.41` | 254,130,000.00 USD | 254,130,000.00 USD | 0.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `7D` | `1.41` | 254,430,000.00 USD | 254,430,000.00 USD | 0.00 USD | 83,860.00 USD | 45,350.00 USD | 168,810.00 USD |
| `7D` | `1.42` | 254,990,000.00 USD | 254,990,000.00 USD | 0.00 USD | 174,510.00 USD | 51,350.00 USD | 334,670.00 USD |
| `7D` | `1.42` | 255,730,000.00 USD | 255,730,000.00 USD | 0.00 USD | 225,460.00 USD | 141,020.00 USD | 371,090.00 USD |
| `7D` | `1.42` | 256,780,000.00 USD | 256,780,000.00 USD | 0.00 USD | 320,240.00 USD | 228,170.00 USD | 499,940.00 USD |
| `7D` | `1.42` | 258,110,000.00 USD | 258,110,000.00 USD | 0.00 USD | 510,570.00 USD | 119,370.00 USD | 704,370.00 USD |
| `7D` | `1.42` | 258,310,000.00 USD | 258,310,000.00 USD | 0.00 USD | 66,420.00 USD | 120,690.00 USD | 7,780.00 USD |
| `7D` | `1.43` | 258,630,000.00 USD | 258,630,000.00 USD | 0.00 USD | 67,230.00 USD | 65,630.00 USD | 183,690.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.86B` | Total OI Tokens: `2,274,699,746.7 XRP`
  * 1h OI Change: `+1.54%` | 4h OI Change: `+4.52%` | 24h OI Change: `-4.26%`
  * Exchange Breakdown: Binance=`436.49M` | Bybit=`319.64M` | OKX=`95.61M` | Hyperliquid=`199.38M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-59.00K` | Last 24h: `81.98K` | Last 3d: `547.43K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0072%` | **USDT OKX** | `-0.0122%` |
| **USDT Bybit** | `-0.0275%` | **USDT KuCoin** | `-0.0031%` |
| **USDT MEXC** | `0.0071%` | **USDT BingX** | `0.0069%` |
| **USDT Gate** | `-0.0013%` | **USDT Bitget** | `-0.0039%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `48.06%` | `51.94%` | `0.93` | 242,680,000.00 USD |
| `15M` | `Binance` | `48.78%` | `51.22%` | `0.95` | 80,970,000.00 USD |
| `15M` | `OKX` | `42.27%` | `57.73%` | `0.73` | 43,530,000.00 USD |
| `15M` | `Bybit` | `48.56%` | `51.44%` | `0.94` | 18,950,000.00 USD |
| `15M` | `KuCoin` | `21.55%` | `78.45%` | `0.27` | 1,350,000.00 USD |
| `15M` | `Gate` | `53.39%` | `46.61%` | `1.15` | 46,170,000.00 USD |
| `15M` | `Bitget` | `42.28%` | `57.72%` | `0.73` | 14,290,000.00 USD |
| `15M` | `BingX` | `39.92%` | `60.08%` | `0.66` | 2,880,000.00 USD |
| `15M` | `MEXC` | `46.67%` | `53.33%` | `0.88` | 7,740,000.00 USD |
| `15M` | `Bitunix` | `50.26%` | `49.74%` | `1.01` | 8,120,000.00 USD |
| `15M` | `Hyperliquid` | `30.69%` | `69.31%` | `0.44` | 5,480,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.31%` | `55.69%` | `0.80` | 463,970.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `72.97%` | `27.03%` | `2.70` | 13,800.00 USD |
| `15M` | `HTX` | `70.38%` | `29.62%` | `2.38` | 5,170,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `51.47%` | `48.53%` | `1.06` | 1,460,000.00 USD |
| `15M` | `Bitfinex` | `18.31%` | `81.69%` | `0.22` | 104,660.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `64.12%` | `35.88%` | `1.79` | 1,590,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `54.2%` | `45.8%` | `1.18` | 4,390,000.00 USD |
| `15M` | `Whale Positions` | `48.78%` | `51.22%` | `0.95` | 80,970,000.00 USD |
| `15M` | `Global Accounts` | `48.06%` | `51.94%` | `0.93` | 242,680,000.00 USD |
| `1H` | `XRP` | `51.75%` | `48.25%` | `1.07` | 2,300,000,000.00 USD |
| `1H` | `Binance` | `51.27%` | `48.73%` | `1.05` | 442,160,000.00 USD |
| `1H` | `OKX` | `47.17%` | `52.83%` | `0.89` | 256,330,000.00 USD |
| `1H` | `Bybit` | `51.8%` | `48.2%` | `1.07` | 116,850,000.00 USD |
| `1H` | `KuCoin` | `41.46%` | `58.54%` | `0.71` | 5,840,000.00 USD |
| `1H` | `Gate` | `52.71%` | `47.29%` | `1.11` | 225,230,000.00 USD |
| `1H` | `Bitget` | `51.66%` | `48.34%` | `1.07` | 75,970,000.00 USD |
| `1H` | `BingX` | `58.38%` | `41.62%` | `1.40` | 15,370,000.00 USD |
| `1H` | `MEXC` | `41.13%` | `58.87%` | `0.70` | 40,660,000.00 USD |
| `1H` | `Bitunix` | `50.79%` | `49.21%` | `1.03` | 47,180,000.00 USD |
| `1H` | `Hyperliquid` | `50.76%` | `49.24%` | `1.03` | 40,330,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.16%` | `47.84%` | `1.09` | 7,000,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `52.83%` | `47.17%` | `1.12` | 959,760,000.00 USD |
| `1H` | `HTX` | `77.09%` | `22.91%` | `3.36` | 30,400,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `57.57%` | `42.43%` | `1.36` | 9,330,000.00 USD |
| `1H` | `Bitfinex` | `13.54%` | `86.46%` | `0.16` | 1,210,000.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `39.74%` | `60.26%` | `0.66` | 10,070,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `48.35%` | `51.65%` | `0.94` | 17,060,000.00 USD |
| `1H` | `Whale Positions` | `51.27%` | `48.73%` | `1.05` | 442,160,000.00 USD |
| `1H` | `Global Accounts` | `51.75%` | `48.25%` | `1.07` | 2,300,000,000.00 USD |
| `4H` | `XRP` | `49.82%` | `50.18%` | `0.99` | 9,650,000,000.00 USD |
| `4H` | `Binance` | `51.11%` | `48.89%` | `1.05` | 2,770,000,000.00 USD |
| `4H` | `OKX` | `50.83%` | `49.17%` | `1.03` | 1,640,000,000.00 USD |
| `4H` | `Bybit` | `52.88%` | `47.12%` | `1.12` | 615,570,000.00 USD |
| `4H` | `KuCoin` | `59.6%` | `40.4%` | `1.48` | 78,110,000.00 USD |
| `4H` | `Gate` | `50.15%` | `49.85%` | `1.01` | 1,360,000,000.00 USD |
| `4H` | `Bitget` | `52.31%` | `47.69%` | `1.10` | 421,580,000.00 USD |
| `4H` | `BingX` | `55.77%` | `44.23%` | `1.26` | 80,980,000.00 USD |
| `4H` | `MEXC` | `45.18%` | `54.82%` | `0.82` | 257,010,000.00 USD |
| `4H` | `Bitunix` | `51.25%` | `48.75%` | `1.05` | 313,800,000.00 USD |
| `4H` | `Hyperliquid` | `53.89%` | `46.11%` | `1.17` | 267,630,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `56.64%` | `43.36%` | `1.31` | 42,650,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `38.9%` | `61.1%` | `0.64` | 1,380,000,000.00 USD |
| `4H` | `HTX` | `74.31%` | `25.69%` | `2.89` | 179,260,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `50.22%` | `49.78%` | `1.01` | 50,540,000.00 USD |
| `4H` | `Bitfinex` | `27.49%` | `72.51%` | `0.38` | 4,980,000.00 USD |
| `4H` | `Kraken` | `62.16%` | `37.84%` | `1.64` | 5,360,000.00 USD |
| `4H` | `Aster` | `53.38%` | `46.62%` | `1.15` | 69,030,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.99%` | `51.01%` | `0.96` | 123,220,000.00 USD |
| `4H` | `Whale Positions` | `51.11%` | `48.89%` | `1.05` | 2,770,000,000.00 USD |
| `4H` | `Global Accounts` | `49.82%` | `50.18%` | `0.99` | 9,650,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `1.23` | `1.23` | `1.23` | `1.23` | `1.22` | 7,441,662.05 USD | 4,516,863.46 USD | 2,924,798.59 USD | 1,592,064.87 USD | `+21.39%` | `27B / 7S` |
| `0:00 UTC` | `1.24` | `1.24` | `1.24` | `1.24` | `1.23` | 14,534,365.59 USD | 7,960,789.37 USD | 6,573,576.22 USD | 1,387,213.15 USD | `+9.54%` | `20B / 9S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.24` | 13,408,965.14 USD | 7,227,260.97 USD | 6,181,704.17 USD | 1,045,556.80 USD | `+7.80%` | `8B / 3S` |
| `0:00 UTC` | `1.24` | `1.25` | `1.24` | `1.25` | `1.24` | 11,613,568.18 USD | 6,301,411.52 USD | 5,312,156.67 USD | 989,254.85 USD | `+8.52%` | `26B / 9S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 11,339,015.88 USD | 5,463,329.20 USD | 5,875,686.68 USD | -412,357.48 USD | `-3.64%` | `7B / 6S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 9,975,142.90 USD | 5,917,919.57 USD | 4,057,223.33 USD | 1,860,696.23 USD | `+18.65%` | `9B / 2S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 6,812,599.45 USD | 3,905,481.96 USD | 2,907,117.49 USD | 998,364.47 USD | `+14.65%` | `4B / 3S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 9,935,673.56 USD | 6,437,809.71 USD | 3,497,863.85 USD | 2,939,945.86 USD | `+29.59%` | `23B / 7S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 6,138,672.69 USD | 3,294,606.36 USD | 2,844,066.33 USD | 450,540.03 USD | `+7.34%` | `3B / 1S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 4,077,711.98 USD | 2,216,322.86 USD | 1,861,389.13 USD | 354,933.73 USD | `+8.70%` | `2B / 3S` |

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
| `5m` | 569,950.00 USD | 525,840.00 USD | **`ACCUMULATION`** |
| `15m` | 714,750.00 USD | -337,000.00 USD | **`ACCUMULATION`** |
| `30m` | 1,780,000.00 USD | 3,060,000.00 USD | **`ACCUMULATION`** |
| `1h` | 3,260,000.00 USD | 8,020,000.00 USD | **`ACCUMULATION`** |
| `2h` | 12,210,000.00 USD | 23,250,000.00 USD | **`ACCUMULATION`** |
| `4h` | 19,330,000.00 USD | 31,830,000.00 USD | **`ACCUMULATION`** |
| `6h` | -5,120,000.00 USD | -5,700,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -17,420,000.00 USD | -73,760,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -52,810,000.00 USD | -123,050,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -53,150,000.00 USD | -132,740,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -123,150,000.00 USD | -214,640,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -597,140,000.00 USD | -1,290,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+569.95K` | 15m=`+714.75K` | 1h=`+3.26M` | 24h=`-53.15M`
* Futures Capital Netflows: 5m=`+525.84K` | 15m=`-337.00K` | 1h=`+8.02M` | 24h=`-132.74M`
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
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.21` (Risk Distance: `0.0162` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.28` (Risk Distance: `0.0162` pts)
  * +2.5R Take Profit: `1.22`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
