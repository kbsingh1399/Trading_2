# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 17:22:13 IST` (`2026-10-30 11:52:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.24` | **Live Ask Quote**: `1.25` | **Mid Price**: `1.25`
- **Spread Points**: `3.00` | **Spread BPS**: `24.09 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1.24` | VWAP Z-Score: `+0.24` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0073` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.45` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.30` | Lower -3.00σ Band: `1.18`
  * Upper +2.51σ Band: `1.29` | Lower -2.51σ Band: `1.19`
  * Upper +2.01σ Band: `1.28` | Lower -2.01σ Band: `1.20`
  * Upper +2.00σ Band: `1.28` | Lower -2.00σ Band: `1.20`
  * Upper +1.28σ Band: `1.26` | Lower -1.28σ Band: `1.21`
  * Upper +1.00σ Band: `1.26` | Lower -1.00σ Band: `1.22`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.25` | EMA-20=`1.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.25` (Slope: `+0.0000`) | EMA-100=`1.26`
  * Institutional Anchors: EMA-144=`1.27` | EMA-200=`1.28` (Slope: `-0.2680`) | EMA-233=`1.28`
- **Range Boundaries**: 24H High=`1.31` | 24H Low=`1.19` | Weekly High=`1.34` | Weekly Low=`1.19`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-1.20%`)
  * Point of Control (POC) = `1.25` (Distance: `-0.36%`)
  * Value Area Low (VAL) = `1.23` (Distance: `+0.95%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.33` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.19`
  * London Session (08:00-16:00 UTC): High=`1.27` | Low=`1.24`
  * New York Session (13:00-21:00 UTC): High=`1.26` | Low=`1.24`
  * Initial Balance (First Hour): IB High=`1.26` | IB Low=`1.25`
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
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `1,722,042` | 2,148,434.82 USD | -662,840.06 USD | `-30.85%` | -40,598,297.92 USD | `-1.47` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `2,306,813` | 2,876,017.16 USD | -399,943.41 USD | `-13.91%` | -40,998,241.33 USD | `-0.81` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `1.25` | `1.25` | `1.25` | `1.25` | `68,891` | 85,926.63 USD | -38,272.00 USD | `-44.54%` | -41,036,513.34 USD | `-0.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.25` | `1.25` | `1.25` | `1.25` | `5,024,516` | 6,278,668.13 USD | 434,327.57 USD | `+6.92%` | -39,450,281.39 USD | `+0.62` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `1.25` | `1.25` | `1.25` | `1.25` | `3,866,160` | 4,831,183.07 USD | -902,667.79 USD | `-18.68%` | -40,352,949.19 USD | `-0.63` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `1.25` | `1.25` | `1.25` | `1.25` | `2,437,023` | 3,038,433.94 USD | -361,741.23 USD | `-11.91%` | -40,714,690.42 USD | `-0.01` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `1.26` | `1.26` | `1.25` | `1.25` | `24,012,060` | 30,200,518.12 USD | -808,085.55 USD | `-2.68%` | -39,421,461.68 USD | `+0.13` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `1.25` | `1.26` | `1.24` | `1.26` | `26,461,360` | 33,135,236.56 USD | -1,222,941.16 USD | `-3.69%` | -40,644,402.83 USD | `+0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `1.26` | `1.26` | `1.25` | `1.25` | `16,176,802` | 20,235,642.61 USD | -71,962.68 USD | `-0.36%` | -40,716,365.51 USD | `+0.23` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -44,069,722.41 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.27` | `1.24` | `1.25` | `116,541,770` | 146,517,167.36 USD | 4,788,193.48 USD | `+3.27%` | -39,281,528.93 USD | `+1.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.25` | `86,808,282` | 108,833,643.78 USD | -1,509,635.67 USD | `-1.39%` | -40,791,164.60 USD | `+0.46` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -13,549,801.29 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -41,639,935.50 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.25` | `1.20` | `1.25` | `283,933,134` | 346,233,644.78 USD | -2,429,786.91 USD | `-0.70%` | -44,069,722.41 USD | `+0.73` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.25` | `1.27` | `1.24` | `1.25` | `116,541,770` | 146,517,167.36 USD | 4,788,193.48 USD | `+3.27%` | -39,281,528.93 USD | `+1.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.25` | `1.26` | `1.24` | `1.25` | `86,808,282` | 108,833,643.78 USD | -1,509,635.67 USD | `-1.39%` | -40,791,164.60 USD | `+0.46` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `ASK` | `1.25` | `53948.0000` | 67,402.63 USD | 2,870,151.18 USD | `3 orders` | `+0.16%` | `-` |
| `ASK` | `1.25` | `78112.0000` | 97,585.32 USD | 2,802,748.55 USD | `5 orders` | `+0.15%` | `-` |
| `ASK` | `1.25` | `7906.0000` | 9,876.18 USD | 2,705,163.23 USD | `5 orders` | `+0.14%` | `-` |
| `ASK` | `1.25` | `210857.0000` | 263,381.48 USD | 2,695,287.05 USD | `4 orders` | `+0.13%` | `-` |
| `ASK` | `1.25` | `96068.0000` | 119,988.93 USD | 2,431,905.57 USD | `5 orders` | `+0.12%` | `-` |
| `ASK` | `1.25` | `569004.0000` | 710,629.10 USD | 2,311,916.64 USD | `5 orders` | `+0.12%` | `-` |
| `ASK` | `1.25` | `17664.0000` | 22,058.80 USD | 1,601,287.55 USD | `4 orders` | `+0.11%` | `-` |
| `ASK` | `1.25` | `269340.0000` | 336,324.86 USD | 1,579,228.74 USD | `8 orders` | `+0.10%` | `-` |
| `ASK` | `1.25` | `71002.0000` | 88,653.10 USD | 1,242,903.89 USD | `9 orders` | `+0.09%` | `-` |
| `ASK` | `1.25` | `31604.0000` | 39,457.59 USD | 1,154,250.79 USD | `7 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `12065.0000` | 15,061.95 USD | 1,114,793.19 USD | `4 orders` | `+0.08%` | `-` |
| `ASK` | `1.25` | `311826.0000` | 389,252.40 USD | 1,099,731.25 USD | `16 orders` | `+0.07%` | `-` |
| `ASK` | `1.25` | `173435.0000` | 216,481.57 USD | 710,478.85 USD | `11 orders` | `+0.06%` | `-` |
| `ASK` | `1.25` | `92287.0000` | 115,183.40 USD | 493,997.29 USD | `9 orders` | `+0.05%` | `-` |
| `ASK` | `1.25` | `68497.0000` | 85,484.26 USD | 378,813.88 USD | `13 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `32600.0000` | 40,681.54 USD | 293,329.62 USD | `10 orders` | `+0.04%` | `-` |
| `ASK` | `1.25` | `115903.0000` | 144,623.76 USD | 252,648.08 USD | `13 orders` | `+0.03%` | `-` |
| `ASK` | `1.25` | `25110.0000` | 31,329.75 USD | 108,024.32 USD | `11 orders` | `+0.02%` | `-` |
| `ASK` | `1.25` | `7693.0000` | 9,597.79 USD | 76,694.57 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `1.25` | `53785.0000` | 67,096.79 USD | 67,096.79 USD | `8 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `1.25` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 1.25` | `0.00%` | `-` |
| `BID` | `1.25` | `4014.0000` | 5,007.06 USD | 5,007.06 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `1.25` | `7959.0000` | 9,927.26 USD | 14,934.32 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `1.25` | `10008.0000` | 12,481.98 USD | 27,416.30 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `1.25` | `6393.0000` | 7,972.71 USD | 35,389.01 USD | `6 orders` | `-0.03%` | `-` |
| `BID` | `1.25` | `41365.0000` | 51,582.16 USD | 86,971.17 USD | `8 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `58312.0000` | 72,709.23 USD | 159,680.40 USD | `8 orders` | `-0.04%` | `-` |
| `BID` | `1.25` | `20568.0000` | 25,644.18 USD | 185,324.58 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `1.25` | `4484.0000` | 5,590.20 USD | 190,914.79 USD | `3 orders` | `-0.06%` | `-` |
| `BID` | `1.25` | `28541.0000` | 35,579.21 USD | 226,494.00 USD | `7 orders` | `-0.07%` | `-` |
| `BID` | `1.25` | `119857.0000` | 149,401.75 USD | 375,895.75 USD | `10 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `34797.0000` | 43,370.98 USD | 419,266.73 USD | `6 orders` | `-0.08%` | `-` |
| `BID` | `1.25` | `85652.0000` | 106,748.09 USD | 526,014.81 USD | `6 orders` | `-0.09%` | `-` |
| `BID` | `1.25` | `14069.0000` | 17,532.79 USD | 543,547.60 USD | `7 orders` | `-0.10%` | `-` |
| `BID` | `1.25` | `53399.0000` | 66,540.49 USD | 610,088.10 USD | `5 orders` | `-0.11%` | `-` |
| `BID` | `1.25` | `289964.0000` | 361,295.14 USD | 971,383.24 USD | `6 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `117162.0000` | 145,972.14 USD | 1,117,355.38 USD | `9 orders` | `-0.12%` | `-` |
| `BID` | `1.25` | `18133.0000` | 22,590.09 USD | 1,139,945.47 USD | `5 orders` | `-0.13%` | `-` |
| `BID` | `1.25` | `98307.0000` | 122,461.03 USD | 1,262,406.50 USD | `8 orders` | `-0.14%` | `-` |
| `BID` | `1.25` | `79798.0000` | 99,396.39 USD | 1,361,802.89 USD | `6 orders` | `-0.15%` | `-` |
| `BID` | `1.25` | `10955.0000` | 13,644.45 USD | 1,375,447.34 USD | `3 orders` | `-0.16%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 17:20:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `27` | `0x31b1...1434` | `LONG` | 43,708,715.21 USD | `35,031,430.00` | `1.13` | `1.25` | `0.9612` | 4,129,831.94 USD | `+9.45%` | `10X Cross` |
| `98` | `0x5b5d...c060` | `SHORT` | 19,375,334.82 USD | `15,519,251.00` | `1.44` | `1.25` | `10.82` | 2,901,953.50 USD | `+14.98%` | `5X Cross` |
| `165` | `0xb83d...6e36` | `SHORT` | 12,359,682.84 USD | `9,905,616.00` | `1.50` | `1.25` | `11.96` | 2,488,788.71 USD | `+20.14%` | `5X Cross` |
| `349` | `0x58f0...0d20` | `LONG` | 6,621,727.31 USD | `5,307,147.00` | `1.24` | `1.25` | `1.22` | 18,883.81 USD | `+0.29%` | `20X Cross` |
| `384` | `0xecb6...2b00` | `SHORT` | 5,949,983.18 USD | `4,767,206.00` | `1.27` | `1.25` | `8.39` | 98,170.72 USD | `+1.65%` | `10X Cross` |
| `430` | `0xca49...53c8` | `SHORT` | 5,164,915.84 USD | `4,138,886.00` | `1.44` | `1.25` | `4.90` | 788,406.89 USD | `+15.26%` | `20X Cross` |
| `442` | `0xdd53...2b13` | `SHORT` | 4,991,044.56 USD | `3,998,914.00` | `1.40` | `1.25` | `16.64` | 605,831.55 USD | `+12.14%` | `3X Cross` |
| `510` | `0x610b...b613` | `LONG` | 4,424,616.58 USD | `3,543,946.00` | `1.44` | `1.25` | `0.8373` | -675,376.03 USD | `-15.26%` | `5X Cross` |
| `590` | `0x9946...0852` | `SHORT` | 3,832,576.88 USD | `3,070,483.00` | `1.40` | `1.25` | `1.77` | 475,925.34 USD | `+12.42%` | `20X Cross` |
| `651` | `0xc30c...a4c9` | `SHORT` | 3,483,104.47 USD | `2,791,515.00` | `1.41` | `1.25` | `1.59` | 453,408.27 USD | `+13.02%` | `8X Cross` |
| `654` | `0xc179...e0c8` | `SHORT` | 3,455,739.94 USD | `2,768,785.00` | `1.27` | `1.25` | `3.35` | 52,676.95 USD | `+1.52%` | `10X Cross` |
| `661` | `0xfc27...9d9d` | `SHORT` | 3,427,024.22 USD | `2,746,013.00` | `1.29` | `1.25` | `8.14` | 124,159.69 USD | `+3.62%` | `20X Cross` |
| `700` | `0xf48f...10fe` | `LONG` | 3,203,375.08 USD | `2,565,779.00` | `1.53` | `1.25` | `1.01` | -721,265.65 USD | `-22.52%` | `4X Cross` |
| `744` | `0x023a...2355` | `SHORT` | 3,074,536.86 USD | `2,463,360.00` | `1.32` | `1.25` | `3.35` | 176,391.39 USD | `+5.74%` | `20X Cross` |
| `751` | `0x45d2...4029` | `SHORT` | 3,061,344.00 USD | `2,453,000.00` | `1.48` | `1.25` | `18.41` | 576,936.42 USD | `+18.85%` | `20X Cross` |
| `1073` | `0xeadc...9d55` | `LONG` | 2,021,030.70 USD | `1,619,805.00` | `1.21` | `1.25` | `0.000000` | 62,187.68 USD | `+3.08%` | `20X Cross` |
| `1148` | `0x94b2...599e` | `SHORT` | 1,922,326.40 USD | `1,540,696.00` | `1.36` | `1.25` | `1.87` | 178,140.05 USD | `+9.27%` | `20X Cross` |
| `1163` | `0x3fc5...c0c1` | `SHORT` | 1,886,700.19 USD | `1,511,779.00` | `1.52` | `1.25` | `2.40` | 404,914.41 USD | `+21.46%` | `20X Cross` |
| `1199` | `0x31ef...f715` | `LONG` | 1,840,752.33 USD | `1,475,080.00` | `1.49` | `1.25` | `1.04` | -358,513.07 USD | `-19.48%` | `3X Isolated` |
| `1248` | `0x7737...bf66` | `SHORT` | 1,763,581.53 USD | `1,413,466.00` | `1.41` | `1.25` | `13.97` | 235,287.12 USD | `+13.34%` | `10X Cross` |
| `1308` | `0x95da...2328` | `LONG` | 1,653,047.79 USD | `1,324,876.00` | `1.35` | `1.25` | `0.0710` | -140,593.31 USD | `-8.51%` | `5X Cross` |
| `1329` | `0xee2b...d67e` | `LONG` | 1,630,382.20 USD | `1,306,284.00` | `1.55` | `1.25` | `0.4446` | -400,272.70 USD | `-24.55%` | `4X Cross` |
| `1380` | `0x215d...f80a` | `LONG` | 1,561,842.16 USD | `1,251,777.00` | `1.32` | `1.25` | `1.13` | -92,612.06 USD | `-5.93%` | `14X Cross` |
| `1402` | `0x5fa3...35b7` | `SHORT` | 1,547,960.25 USD | `1,240,651.00` | `1.30` | `1.25` | `2.63` | 68,531.88 USD | `+4.43%` | `20X Cross` |
| `1436` | `0x123d...3bff` | `LONG` | 1,513,043.42 USD | `1,211,889.00` | `1.35` | `1.25` | `0.000000` | -119,392.06 USD | `-7.89%` | `10X Cross` |
| `1450` | `0xbcd4...0dd2` | `SHORT` | 1,492,764.00 USD | `1,196,125.00` | `1.31` | `1.25` | `2.00` | 74,903.24 USD | `+5.02%` | `20X Cross` |
| `1571` | `0xdf95...7d72` | `SHORT` | 1,372,458.05 USD | `1,099,726.00` | `1.37` | `1.25` | `36.54` | 137,140.75 USD | `+9.99%` | `20X Cross` |
| `1611` | `0x7fda...17d1` | `LONG` | 1,318,844.71 USD | `1,056,676.00` | `1.22` | `1.25` | `0.000000` | 31,249.77 USD | `+2.37%` | `20X Cross` |
| `1642` | `0xef96...9383` | `SHORT` | 1,293,620.42 USD | `1,036,765.00` | `1.34` | `1.25` | `4.62` | 93,898.93 USD | `+7.26%` | `20X Cross` |
| `1658` | `0xb1ce...681b` | `LONG` | 1,275,161.47 USD | `1,021,764.00` | `1.49` | `1.25` | `1.16` | -248,895.02 USD | `-19.52%` | `4X Isolated` |
| `1768` | `0x3c36...461a` | `LONG` | 1,172,995.64 USD | `940,051.00` | `1.30` | `1.25` | `1.05` | -46,084.98 USD | `-3.93%` | `10X Cross` |
| `1901` | `0x2577...4897` | `SHORT` | 1,063,050.18 USD | `851,730.00` | `1.24` | `1.25` | `5.22` | -3,027.03 USD | `-0.28%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.29` | 12,657.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 12.66K USD at 1.2924 USD [API] | `2026-10-29 18:11:20` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,407.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.41K USD at 1.2835 USD [API] | `2026-10-29 18:34:54` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,320.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.32K USD at 1.2835 USD [API] | `2026-10-29 18:34:54` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,004.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.2835 USD [API] | `2026-10-29 18:34:54` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 7,794.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.79K USD at 1.2813 USD [API] | `2026-10-29 18:36:59` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 165.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.17K USD at 1.2854 USD [API] | `2026-10-29 18:31:36` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 614.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.61K USD at 1.2854 USD [API] | `2026-10-29 18:31:36` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 7,892.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.89K USD at 1.3047 USD [API] | `2026-10-29 16:29:53` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 8,234.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.23K USD at 1.2803 USD [API] | `2026-10-29 18:40:55` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,876.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.88K USD at 1.3428 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,003.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3428 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,218.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.22K USD at 1.3428 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,911.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.91K USD at 1.3428 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 400.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3429 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,873.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.87K USD at 1.3429 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,573.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.57K USD at 1.3429 USD [API] | `2026-10-08 15:59:10` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 1,011.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.01K USD at 1.4803 USD [API] | `2026-09-28 05:23:54` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 905.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.91K USD at 1.4803 USD [API] | `2026-09-28 05:23:54` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 17.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.4600 USD [API] | `2026-09-24 09:31:06` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 91.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.4600 USD [API] | `2026-09-24 09:31:06` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 7,933.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 7.93K USD at 1.4600 USD [API] | `2026-09-24 09:31:06` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 3,171.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.17K USD at 1.4600 USD [API] | `2026-09-24 09:31:06` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 14,525.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 14.53K USD at 1.2824 USD [API] | `2026-10-29 18:45:20` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 30,950.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 30.95K USD at 1.2863 USD [API] | `2026-10-29 18:51:28` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,048.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.05K USD at 1.2863 USD [API] | `2026-10-29 18:51:28` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,512.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.51K USD at 1.2840 USD [API] | `2026-10-29 19:12:52` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,807.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.81K USD at 1.2824 USD [API] | `2026-10-29 19:14:08` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,005.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.2842 USD [API] | `2026-10-29 19:23:02` |
| `ANNOUNCEMENT` | `INFO` | `2.26` | 4,521.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.52K USD at 2.2605 USD [API] | `2025-02-03 00:43:28` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,004.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.2839 USD [API] | `2026-10-29 19:48:16` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 7,813.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.81K USD at 1.2769 USD [API] | `2026-10-29 20:02:41` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 6,213.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.21K USD at 1.2771 USD [API] | `2026-10-29 20:02:41` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 69.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.2681 USD [API] | `2026-10-29 20:05:46` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,458.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.46K USD at 1.2684 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 6,420.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 6.42K USD at 1.2684 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,332.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.33K USD at 1.2788 USD [API] | `2026-10-29 18:41:37` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,275.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.28K USD at 1.3049 USD [API] | `2026-10-29 16:29:53` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,270.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.27K USD at 1.3048 USD [API] | `2026-10-29 16:29:53` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,291.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.29K USD at 1.3047 USD [API] | `2026-10-29 16:29:53` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 85.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2781 USD [API] | `2026-10-29 20:01:48` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 332.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.33K USD at 1.2781 USD [API] | `2026-10-29 20:01:48` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 933.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.93K USD at 1.2781 USD [API] | `2026-10-29 20:01:48` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 12,423.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 12.42K USD at 1.2617 USD [API] | `2026-10-29 20:33:59` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 6,288.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.29K USD at 1.2618 USD [API] | `2026-10-29 20:33:59` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 15,158.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 15.16K USD at 1.2627 USD [API] | `2026-10-29 20:33:59` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 6,393.45 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 6.39K USD at 1.2588 USD [API] | `2026-10-29 20:34:20` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 581.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.58K USD at 1.2624 USD [API] | `2026-10-29 20:33:49` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 416.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.42K USD at 1.2624 USD [API] | `2026-10-29 20:33:49` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 626.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.63K USD at 1.2585 USD [API] | `2026-10-29 20:34:17` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 70.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 66.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 445.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.45K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 25.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 11.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 33,057.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 33.06K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 18.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 96.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 2,016.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.02K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 652.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.65K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 12,593.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 12.59K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 584.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.58K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 178.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.18K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 99.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.2593 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 477.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.48K USD at 1.2605 USD [API] | `2026-10-29 20:34:04` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 408.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.41K USD at 1.2605 USD [API] | `2026-10-29 20:34:04` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 1,489.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.49K USD at 1.2605 USD [API] | `2026-10-29 20:34:04` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 205.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.21K USD at 1.2605 USD [API] | `2026-10-29 20:34:04` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 576.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.58K USD at 1.2605 USD [API] | `2026-10-29 20:34:04` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 4,851.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.85K USD at 1.2605 USD [API] | `2026-10-29 20:34:04` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 98.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.2605 USD [API] | `2026-10-29 20:34:04` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 1,948.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.95K USD at 1.2605 USD [API] | `2026-10-29 20:34:04` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 366.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.37K USD at 1.2605 USD [API] | `2026-10-29 20:34:04` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 2,634.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.63K USD at 1.2605 USD [API] | `2026-10-29 20:34:04` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 11.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2633 USD [API] | `2026-10-29 20:33:37` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 11.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2633 USD [API] | `2026-10-29 20:33:34` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 17,686.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 17.69K USD at 1.2633 USD [API] | `2026-10-29 20:33:34` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 11.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2633 USD [API] | `2026-10-29 20:33:34` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 1,128.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.13K USD at 1.2633 USD [API] | `2026-10-29 20:33:34` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 151.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.15K USD at 1.2633 USD [API] | `2026-10-29 20:33:34` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 561.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.56K USD at 1.2645 USD [API] | `2026-10-29 20:33:09` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 85.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2645 USD [API] | `2026-10-29 20:33:09` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 36.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.2645 USD [API] | `2026-10-29 20:33:09` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 29,833.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 29.83K USD at 1.2645 USD [API] | `2026-10-29 20:33:09` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 16.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2645 USD [API] | `2026-10-29 20:33:09` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 270.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.27K USD at 1.2645 USD [API] | `2026-10-29 20:33:09` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 632.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.63K USD at 1.2645 USD [API] | `2026-10-29 20:33:09` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 1,583.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.58K USD at 1.2645 USD [API] | `2026-10-29 20:33:06` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 323.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.32K USD at 1.2645 USD [API] | `2026-10-29 20:33:06` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 26,874.07 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 26.87K USD at 1.2649 USD [API] | `2026-10-29 20:33:06` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 442.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.44K USD at 1.2649 USD [API] | `2026-10-29 20:33:06` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,692.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.69K USD at 1.2662 USD [API] | `2026-10-29 20:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 2,585.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.59K USD at 1.2666 USD [API] | `2026-10-29 20:06:46` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 82.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.08K USD at 1.2666 USD [API] | `2026-10-29 20:06:46` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 226.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.23K USD at 1.2666 USD [API] | `2026-10-29 20:06:46` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 4,229.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.23K USD at 1.2666 USD [API] | `2026-10-29 20:06:46` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 195.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2666 USD [API] | `2026-10-29 20:06:46` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,359.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.36K USD at 1.2666 USD [API] | `2026-10-29 20:06:46` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 70.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.2666 USD [API] | `2026-10-29 20:06:46` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 228.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.23K USD at 1.2670 USD [API] | `2026-10-29 20:06:44` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 63.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.06K USD at 1.2670 USD [API] | `2026-10-29 20:06:07` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 13,036.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 13.04K USD at 1.2670 USD [API] | `2026-10-29 20:06:07` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2674 USD [API] | `2026-10-29 20:05:48` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 92.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2674 USD [API] | `2026-10-29 20:05:48` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 15,102.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 15.10K USD at 1.2674 USD [API] | `2026-10-29 20:05:48` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 346.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.35K USD at 1.2674 USD [API] | `2026-10-29 20:05:48` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 88.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2674 USD [API] | `2026-10-29 20:05:48` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 309.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.31K USD at 1.2674 USD [API] | `2026-10-29 20:05:48` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 139.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.14K USD at 1.2682 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 4,526.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.53K USD at 1.2682 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 48.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.05K USD at 1.2682 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2682 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 10,508.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 10.51K USD at 1.2682 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 507.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.51K USD at 1.2682 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,053.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.05K USD at 1.2682 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 240.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.24K USD at 1.2682 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 15.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2682 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 9,949.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 9.95K USD at 1.2682 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,980.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.98K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 455.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.46K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 3,383.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.38K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 4,141.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.14K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 204.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 11.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 13.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 19.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 12.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 5,188.57 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.19K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 216.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.22K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 162.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.16K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,527.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.53K USD at 1.2686 USD [API] | `2026-10-29 20:05:39` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 36.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.2710 USD [API] | `2026-10-29 20:05:12` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 4,589.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 4.59K USD at 1.2710 USD [API] | `2026-10-29 20:05:12` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 55.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.06K USD at 1.2714 USD [API] | `2026-10-29 20:05:00` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 2,003.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.00K USD at 1.2714 USD [API] | `2026-10-29 20:05:00` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,779.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.78K USD at 1.2714 USD [API] | `2026-10-29 20:05:00` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 38.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.2714 USD [API] | `2026-10-29 20:05:00` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 40.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.2714 USD [API] | `2026-10-29 20:05:00` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 375.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.38K USD at 1.2714 USD [API] | `2026-10-29 20:05:00` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 1,927.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.93K USD at 1.2714 USD [API] | `2026-10-29 20:04:57` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 444.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.44K USD at 1.2714 USD [API] | `2026-10-29 20:04:57` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 2,147.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.15K USD at 1.2714 USD [API] | `2026-10-29 20:04:57` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 87.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.09K USD at 1.2714 USD [API] | `2026-10-29 20:04:57` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 587.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.59K USD at 1.2714 USD [API] | `2026-10-29 20:04:57` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 22.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2722 USD [API] | `2026-10-29 20:04:54` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 230.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.23K USD at 1.2734 USD [API] | `2026-10-29 20:04:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 329.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.33K USD at 1.2734 USD [API] | `2026-10-29 20:04:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 15,437.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 15.44K USD at 1.2734 USD [API] | `2026-10-29 20:04:08` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 35.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.2738 USD [API] | `2026-10-29 20:04:02` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 2,141.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.14K USD at 1.2742 USD [API] | `2026-10-29 20:03:47` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 3,423.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.42K USD at 1.2742 USD [API] | `2026-10-29 20:03:47` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 25,811.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 25.81K USD at 1.2742 USD [API] | `2026-10-29 20:03:47` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 2,105.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.11K USD at 1.2746 USD [API] | `2026-10-29 20:03:40` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 95.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.2746 USD [API] | `2026-10-29 20:03:40` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 891.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.89K USD at 1.2751 USD [API] | `2026-10-29 20:03:38` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 70.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.07K USD at 1.2751 USD [API] | `2026-10-29 20:03:38` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 321.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.32K USD at 1.2751 USD [API] | `2026-10-29 20:03:38` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 22.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2755 USD [API] | `2026-10-29 20:03:35` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 5,441.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.44K USD at 1.2759 USD [API] | `2026-10-29 20:03:03` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 75.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.08K USD at 1.2759 USD [API] | `2026-10-29 20:03:03` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 1,646.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.65K USD at 1.2767 USD [API] | `2026-10-29 20:02:12` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 373.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.37K USD at 1.2779 USD [API] | `2026-10-29 20:01:54` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 19.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2779 USD [API] | `2026-10-29 20:01:54` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 477.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.48K USD at 1.2779 USD [API] | `2026-10-29 20:01:54` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 591.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.59K USD at 1.2779 USD [API] | `2026-10-29 20:01:51` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 47.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.05K USD at 1.2779 USD [API] | `2026-10-29 20:01:51` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 451.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.45K USD at 1.2779 USD [API] | `2026-10-29 20:01:51` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 13,744.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 13.74K USD at 1.2787 USD [API] | `2026-10-29 18:41:37` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 84.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.08K USD at 1.2791 USD [API] | `2026-10-29 18:41:37` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 11.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2791 USD [API] | `2026-10-29 18:41:34` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 1,093.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.09K USD at 1.2791 USD [API] | `2026-10-29 18:40:31` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 35.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.2791 USD [API] | `2026-10-29 18:40:31` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 76.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.08K USD at 1.2791 USD [API] | `2026-10-29 18:40:31` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 21,664.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 21.66K USD at 1.2795 USD [API] | `2026-10-29 18:40:25` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 564.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.56K USD at 1.2795 USD [API] | `2026-10-29 18:40:25` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 2,409.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.41K USD at 1.2795 USD [API] | `2026-10-29 18:40:25` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 95.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.10K USD at 1.2795 USD [API] | `2026-10-29 18:40:25` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 972.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.97K USD at 1.2795 USD [API] | `2026-10-29 18:40:25` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 768.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.77K USD at 1.2807 USD [API] | `2026-10-29 18:40:22` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 563.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.56K USD at 1.2807 USD [API] | `2026-10-29 18:40:22` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 115.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.12K USD at 1.2811 USD [API] | `2026-10-29 18:36:02` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 33.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2811 USD [API] | `2026-10-29 18:36:02` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 199.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.20K USD at 1.2815 USD [API] | `2026-10-29 18:33:59` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 24.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.02K USD at 1.2819 USD [API] | `2026-10-29 18:31:51` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 1,949.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.95K USD at 1.2819 USD [API] | `2026-10-29 18:31:51` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 11.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2819 USD [API] | `2026-10-29 18:31:51` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 39.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.04K USD at 1.2823 USD [API] | `2026-10-29 18:31:42` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 34.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.03K USD at 1.2823 USD [API] | `2026-10-29 18:31:42` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 14.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2823 USD [API] | `2026-10-29 18:31:42` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 247.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.25K USD at 1.2823 USD [API] | `2026-10-29 18:31:42` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 11.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2823 USD [API] | `2026-10-29 18:31:42` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 3,519.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 3.52K USD at 1.2823 USD [API] | `2026-10-29 18:31:42` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 11.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.2823 USD [API] | `2026-10-29 18:31:42` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 109.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.11K USD at 1.2823 USD [API] | `2026-10-29 18:31:42` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 18,130.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 18.13K USD at 1.2852 USD [API] | `2026-10-29 18:31:32` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 20,410.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 20.41K USD at 1.2607 USD [API] | `2026-10-29 20:36:19` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 29,833.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 29.83K USD at 1.2645 USD [API] | `2026-10-29 20:33:09` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 2,265.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.27K USD at 1.2721 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 5,126.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.13K USD at 1.2722 USD [API] | `2026-10-24 14:16:11` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,039.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.04K USD at 1.2992 USD [API] | `2026-09-15 18:48:23` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 3,998.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.2992 USD [API] | `2026-09-15 18:48:23` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,097.07 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.10K USD at 1.2993 USD [API] | `2026-09-15 18:48:23` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 3,999.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.2993 USD [API] | `2026-09-15 18:48:23` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 3,422.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.42K USD at 1.2994 USD [API] | `2026-09-15 18:48:23` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 13,609.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 13.61K USD at 1.3534 USD [API] | `2026-09-10 12:47:06` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 2,067.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.07K USD at 1.5022 USD [API] | `2026-08-22 01:45:33` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 234.33 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.23K USD at 1.5021 USD [API] | `2026-08-22 01:45:33` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 980.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.98K USD at 1.5021 USD [API] | `2026-08-22 01:45:33` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 12.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.01K USD at 1.5021 USD [API] | `2026-08-22 01:45:33` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+3.26%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.42%`)
  * 48H Horizon: Short MP=`1.32` (Vol: 2,300,000.00 USD, Dist: `+5.49%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.43%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,800,000.00 USD, Dist: `+7.65%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.43%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 2,900,000.00 USD, Dist: `+7.54%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--4.43%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 10,850.00 USD | 64,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 6,060.00 USD | 64,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 1,090.00 USD | 64,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 1,410.00 USD | 64,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 1,050.00 USD | 64,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 10,710.00 USD | 64,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3250` | 53,390.00 USD | 64,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 4,960.00 USD | 64,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 139.38 USD | 64,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 2,770.00 USD | 64,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 4,670.00 USD | 64,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3750` | 1,170.00 USD | 64,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3850` | 269.50 USD | 64,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 2,640.00 USD | 64,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 3,210.00 USD | 64,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4150` | 2,170.00 USD | 64,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 1,020.00 USD | 64,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 585,350.00 USD | 64,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 155,750.00 USD | 63,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 244.34 USD | 63,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 1,700.00 USD | 63,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 13,510.00 USD | 63,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 121.25 USD | 63,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 444.91 USD | 63,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 2,890.00 USD | 63,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 10,750.00 USD | 63,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 154,280.00 USD | 63,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 14,210.00 USD | 63,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5550` | 6,690.00 USD | 63,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 5,160.00 USD | 63,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 7,130.00 USD | 63,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 3,920.00 USD | 63,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 6,520.00 USD | 63,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 39,370.00 USD | 63,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 36,560.00 USD | 63,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 9,040.00 USD | 63,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 12,180.00 USD | 63,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 19,930.00 USD | 63,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 11,640.00 USD | 63,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 17,310.00 USD | 63,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 28,750.00 USD | 63,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 3,380.00 USD | 63,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 142,460.00 USD | 63,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 31,130.00 USD | 63,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 67,660.00 USD | 62,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 217,180.00 USD | 62,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 106,710.00 USD | 62,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 70,830.00 USD | 62,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 91,900.00 USD | 62,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 2,320.00 USD | 62,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 6,230.00 USD | 62,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 509,740.00 USD | 62,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 23,170.00 USD | 61,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 17,590.00 USD | 61,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 48,100.00 USD | 61,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 5,580.00 USD | 61,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 3,000,000.00 USD | 61,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 67,320.00 USD | 58,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 63,720.00 USD | 58,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 35,380.00 USD | 58,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 112,870.00 USD | 58,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 393,690.00 USD | 58,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 140,940.00 USD | 58,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 132,420.00 USD | 58,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 86,550.00 USD | 57,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 71,480.00 USD | 57,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 86,260.00 USD | 57,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 63,620.00 USD | 57,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 154,550.00 USD | 57,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,900,000.00 USD | 57,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 157,210.00 USD | 23,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 447,720.00 USD | 23,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 2,690,000.00 USD | 22,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 466,450.00 USD | 20,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 294,250.00 USD | 19,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 80,710.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,190,000.00 USD | 19,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 698,670.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,140,000.00 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 379,080.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.07` | 103,090,000.00 USD | 103,090,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.07` | 1,140,000.00 USD | 14,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 216,770.00 USD | 13,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.09` | 103,080,000.00 USD | 103,080,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 103,040,000.00 USD | 103,040,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.09` | 102,940,000.00 USD | 102,940,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.09` | 695,430.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.10` | 102,900,000.00 USD | 102,900,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 102,900,000.00 USD | 102,900,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.10` | 102,610,000.00 USD | 102,610,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.10` | 98,950.00 USD | 12,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.11` | 102,610,000.00 USD | 102,610,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 102,610,000.00 USD | 102,610,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 102,610,000.00 USD | 102,610,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 280,050.00 USD | 12,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.12` | 102,550,000.00 USD | 102,550,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 102,540,000.00 USD | 102,540,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 101,690,000.00 USD | 101,690,000.00 USD | 19,780.00 USD | 70,020.00 USD | 236,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 101,370,000.00 USD | 101,370,000.00 USD | 7,800.00 USD | 40,660.00 USD | 176,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 102,460,000.00 USD | 102,460,000.00 USD | 17,190.00 USD | 3,530.00 USD | 108,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 101,140,000.00 USD | 101,140,000.00 USD | 31,610.00 USD | 8,290.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 102,330,000.00 USD | 102,330,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,190,000.00 USD | 12,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 101,030,000.00 USD | 101,030,000.00 USD | 126,800.00 USD | 79,730.00 USD | 249,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 102,120,000.00 USD | 102,120,000.00 USD | 0.00 USD | 53,430.00 USD | 94,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 100,570,000.00 USD | 100,570,000.00 USD | 77,710.00 USD | 59,850.00 USD | 210,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 101,970,000.00 USD | 101,970,000.00 USD | 0.00 USD | 0.00 USD | 295,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 100,230,000.00 USD | 100,230,000.00 USD | 29,530.00 USD | 126,490.00 USD | 405,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 101,680,000.00 USD | 101,680,000.00 USD | 5,450.00 USD | 55,710.00 USD | 98,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 99,670,000.00 USD | 99,670,000.00 USD | 5,520.00 USD | 78,550.00 USD | 312,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 101,520,000.00 USD | 101,520,000.00 USD | 69,750.00 USD | 93,260.00 USD | 205,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 99,270,000.00 USD | 99,270,000.00 USD | 91,470.00 USD | 89,100.00 USD | 115,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 101,150,000.00 USD | 101,150,000.00 USD | 74,920.00 USD | 187,750.00 USD | 224,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 114,760.00 USD | 10,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.14` | 98,970,000.00 USD | 98,970,000.00 USD | 42,870.00 USD | 153,340.00 USD | 163,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 100,660,000.00 USD | 100,660,000.00 USD | 79,780.00 USD | 88,050.00 USD | 370,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 98,610,000.00 USD | 98,610,000.00 USD | 38,180.00 USD | 18,330.00 USD | 49,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 100,120,000.00 USD | 100,120,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 98,510,000.00 USD | 98,510,000.00 USD | 34,800.00 USD | 44,230.00 USD | 258,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 100,090,000.00 USD | 100,090,000.00 USD | 39,170.00 USD | 54,580.00 USD | 250,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 98,170,000.00 USD | 98,170,000.00 USD | 67,590.00 USD | 0.00 USD | 2,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 99,750,000.00 USD | 99,750,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 98,100,000.00 USD | 98,100,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 99,610,000.00 USD | 99,610,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 495,010.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 99,600,000.00 USD | 99,600,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 97,970,000.00 USD | 97,970,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 99,540,000.00 USD | 99,540,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 97,950,000.00 USD | 97,950,000.00 USD | 0.00 USD | 75.47 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 99,160,000.00 USD | 99,160,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 97,950,000.00 USD | 97,950,000.00 USD | 1,390.00 USD | 149.67 USD | 64,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 99,010,000.00 USD | 99,010,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 97,880,000.00 USD | 97,880,000.00 USD | 73,200.00 USD | 45,610.00 USD | 263,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 98,850,000.00 USD | 98,850,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 118,760.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 97,500,000.00 USD | 97,500,000.00 USD | 20,480.00 USD | 23,120.00 USD | 82,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 97,970,000.00 USD | 97,970,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 97,380,000.00 USD | 97,380,000.00 USD | 108,420.00 USD | 20,680.00 USD | 371,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 97,730,000.00 USD | 97,730,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 96,880,000.00 USD | 96,880,000.00 USD | 149,150.00 USD | 46,560.00 USD | 127,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 96,870,000.00 USD | 96,870,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 96,550,000.00 USD | 96,550,000.00 USD | 134,780.00 USD | 232,220.00 USD | 78,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 95,790,000.00 USD | 95,790,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 96,110,000.00 USD | 96,110,000.00 USD | 85,830.00 USD | 48,800.00 USD | 626,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 94,490,000.00 USD | 94,490,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,280,000.00 USD | 9,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 95,350,000.00 USD | 95,350,000.00 USD | 45,160.00 USD | 3,210.00 USD | 106,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 92,820,000.00 USD | 92,820,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 95,190,000.00 USD | 95,190,000.00 USD | 104,050.00 USD | 170,360.00 USD | 170,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 91,480,000.00 USD | 91,480,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 94,750,000.00 USD | 94,750,000.00 USD | 152,210.00 USD | 24,880.00 USD | 358,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 90,410,000.00 USD | 90,410,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 94,210,000.00 USD | 94,210,000.00 USD | 371,850.00 USD | 783.46 USD | 266,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 88,370,000.00 USD | 88,370,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 93,570,000.00 USD | 93,570,000.00 USD | 124,360.00 USD | 133,540.00 USD | 474,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 87,170,000.00 USD | 87,170,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 290,280.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 92,840,000.00 USD | 92,840,000.00 USD | 304,390.00 USD | 85,620.00 USD | 356,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 85,600,000.00 USD | 85,600,000.00 USD | 181,850.00 USD | 71,240.00 USD | 311,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 92,090,000.00 USD | 92,090,000.00 USD | 71,040.00 USD | 84,510.00 USD | 175,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 85,040,000.00 USD | 85,040,000.00 USD | 85,020.00 USD | 26,480.00 USD | 380,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 91,760,000.00 USD | 91,760,000.00 USD | 113,290.00 USD | 4,120.00 USD | 24,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 84,540,000.00 USD | 84,540,000.00 USD | 267,580.00 USD | 78,500.00 USD | 194,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 91,620,000.00 USD | 91,620,000.00 USD | 222,930.00 USD | 9,740.00 USD | 666,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 84,000,000.00 USD | 84,000,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 90,720,000.00 USD | 90,720,000.00 USD | 196,910.00 USD | 88,190.00 USD | 143,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 83,740,000.00 USD | 83,740,000.00 USD | 297,510.00 USD | 570,360.00 USD | 235,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 498,200.00 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 90,290,000.00 USD | 90,290,000.00 USD | 86,540.00 USD | 501,490.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 82,630,000.00 USD | 82,630,000.00 USD | 76,370.00 USD | 69,240.00 USD | 706,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 89,640,000.00 USD | 89,640,000.00 USD | 365,260.00 USD | 94,780.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 81,780,000.00 USD | 81,780,000.00 USD | 216,820.00 USD | 93,330.00 USD | 477,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 87,610,000.00 USD | 87,610,000.00 USD | 110,600.00 USD | 41,860.00 USD | 319,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 80,990,000.00 USD | 80,990,000.00 USD | 179,980.00 USD | 69,020.00 USD | 728,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 87,140,000.00 USD | 87,140,000.00 USD | 147,820.00 USD | 204,560.00 USD | 470,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 80,020,000.00 USD | 80,020,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 86,320,000.00 USD | 86,320,000.00 USD | 195,220.00 USD | 436,550.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 78,650,000.00 USD | 78,650,000.00 USD | 229,630.00 USD | 59,450.00 USD | 558,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 587,240.00 USD | 7,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 83,780,000.00 USD | 83,780,000.00 USD | 787,460.00 USD | 119,400.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 77,810,000.00 USD | 77,810,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 707,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 81,440,000.00 USD | 81,440,000.00 USD | 344,480.00 USD | 837,030.00 USD | 761,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 75,790,000.00 USD | 75,790,000.00 USD | 31,150.00 USD | 373,690.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 79,500,000.00 USD | 79,500,000.00 USD | 944,770.00 USD | 537,300.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 72,780,000.00 USD | 72,780,000.00 USD | 800,760.00 USD | 466,100.00 USD | 255,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 75,410,000.00 USD | 75,410,000.00 USD | 221,270.00 USD | 284,650.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 71,250,000.00 USD | 71,250,000.00 USD | 337,020.00 USD | 144,630.00 USD | 622,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 73,710,000.00 USD | 73,710,000.00 USD | 641,370.00 USD | 589,780.00 USD | 557,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 70,150,000.00 USD | 70,150,000.00 USD | 47,500.00 USD | 723,100.00 USD | 407,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 8,380.00 USD | 6,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 71,920,000.00 USD | 71,920,000.00 USD | 466,520.00 USD | 581,610.00 USD | 999,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 68,970,000.00 USD | 68,970,000.00 USD | 0.00 USD | 124,960.00 USD | 245,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 69,870,000.00 USD | 69,870,000.00 USD | 1,740,000.00 USD | 376,210.00 USD | 2,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 68,600,000.00 USD | 68,600,000.00 USD | 564,460.00 USD | 0.00 USD | 635,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 65,670,000.00 USD | 65,670,000.00 USD | 686,600.00 USD | 485,620.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 67,400,000.00 USD | 67,400,000.00 USD | 257,960.00 USD | 719,110.00 USD | 3,230,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 63,190,000.00 USD | 63,190,000.00 USD | 1,520,000.00 USD | 658,010.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 63,200,000.00 USD | 63,200,000.00 USD | 1,350,000.00 USD | 0.00 USD | 899,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 59,450,000.00 USD | 59,450,000.00 USD | 30,610.00 USD | 180,030.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 60,940,000.00 USD | 60,940,000.00 USD | 108,640.00 USD | 136,460.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.22` | 104,870.00 USD | 6,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.22` | 58,150,000.00 USD | 58,150,000.00 USD | 226,520.00 USD | 196,610.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 59,410,000.00 USD | 59,410,000.00 USD | 142,210.00 USD | 9,150.00 USD | 253,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 56,560,000.00 USD | 56,560,000.00 USD | 152,400.00 USD | 6,620.00 USD | 246,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 59,010,000.00 USD | 59,010,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 56,150,000.00 USD | 56,150,000.00 USD | 228,030.00 USD | 95,330.00 USD | 422,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 58,270,000.00 USD | 58,270,000.00 USD | 156,790.00 USD | 928,300.00 USD | 569,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 55,400,000.00 USD | 55,400,000.00 USD | 122,290.00 USD | 275,000.00 USD | 881,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 56,620,000.00 USD | 56,620,000.00 USD | 0.00 USD | 167,460.00 USD | 340,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 54,130,000.00 USD | 54,130,000.00 USD | 504,680.00 USD | 82,730.00 USD | 2,890,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 56,110,000.00 USD | 56,110,000.00 USD | 180,560.00 USD | 170,590.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.23` | 6,810,000.00 USD | 6,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.23` | 50,650,000.00 USD | 50,650,000.00 USD | 609,560.00 USD | 833,330.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 55,730,000.00 USD | 55,730,000.00 USD | 258,810.00 USD | 802,580.00 USD | 790,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 47,990,000.00 USD | 47,990,000.00 USD | 599,790.00 USD | 813,980.00 USD | 800,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 53,870,000.00 USD | 53,870,000.00 USD | 59,160.00 USD | 950,550.00 USD | 538,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 45,770,000.00 USD | 45,770,000.00 USD | 485,440.00 USD | 1,130,000.00 USD | 3,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 52,330,000.00 USD | 52,330,000.00 USD | 198,530.00 USD | 1,150,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 40,300,000.00 USD | 40,300,000.00 USD | 1,370,000.00 USD | 1,380,000.00 USD | 5,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 49,370,000.00 USD | 49,370,000.00 USD | 1,040,000.00 USD | 1,170,000.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 32,100,000.00 USD | 32,100,000.00 USD | 640,340.00 USD | 1,350,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 45,570,000.00 USD | 45,570,000.00 USD | 1,660,000.00 USD | 1,990,000.00 USD | 6,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.24` | 18,990.00 USD | 18,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 27,310,000.00 USD | 27,310,000.00 USD | 577,460.00 USD | 1,140,000.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 35,810,000.00 USD | 35,810,000.00 USD | 2,040,000.00 USD | 2,080,000.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 23,660,000.00 USD | 23,660,000.00 USD | 1,350,000.00 USD | 915,810.00 USD | 2,610,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 28,660,000.00 USD | 28,660,000.00 USD | 3,420,000.00 USD | 2,120,000.00 USD | 5,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 18,780,000.00 USD | 18,780,000.00 USD | 847,110.00 USD | 824,940.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 18,080,000.00 USD | 18,080,000.00 USD | 2,070,000.00 USD | 1,220,000.00 USD | 2,290,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 14,370,000.00 USD | 14,370,000.00 USD | 851,040.00 USD | 1,300,000.00 USD | 2,420,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 12,490,000.00 USD | 12,490,000.00 USD | 1,130,000.00 USD | 510,590.00 USD | 2,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 9,800,000.00 USD | 9,800,000.00 USD | 1,950,000.00 USD | 526,050.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 8,780,000.00 USD | 8,780,000.00 USD | 1,420,000.00 USD | 424,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 4,020,000.00 USD | 4,020,000.00 USD | 1,410,000.00 USD | 706,700.00 USD | 525,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 6,940,000.00 USD | 6,940,000.00 USD | 3,770,000.00 USD | 688,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.25` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.25` | 2,480,000.00 USD | 2,480,000.00 USD | 1,630,000.00 USD | 857,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 158,820.00 USD | 158,820.00 USD | 150,010.00 USD | 8,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 856,480.00 USD | 856,480.00 USD | 0.00 USD | 0.00 USD | 856,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 19,840.00 USD | 1,740,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 1,490,000.00 USD | 1,490,000.00 USD | 253,360.00 USD | 0.00 USD | 379,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 10,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 2,140,000.00 USD | 2,140,000.00 USD | 228,810.00 USD | 253,090.00 USD | 167,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 2,330,000.00 USD | 2,330,000.00 USD | 402,060.00 USD | 3,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 5,280,000.00 USD | 5,280,000.00 USD | 664,010.00 USD | 508,070.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 4,810,000.00 USD | 4,810,000.00 USD | 292,090.00 USD | 542,940.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 7,740,000.00 USD | 7,740,000.00 USD | 1,210,000.00 USD | 457,890.00 USD | 784,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 10,110,000.00 USD | 10,110,000.00 USD | 4,260,000.00 USD | 9,150.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 11,480,000.00 USD | 11,480,000.00 USD | 790,310.00 USD | 1,540,000.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 16,060,000.00 USD | 16,060,000.00 USD | 0.00 USD | 1,870,000.00 USD | 4,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 19,940,000.00 USD | 19,940,000.00 USD | 1,240,000.00 USD | 1,390,000.00 USD | 5,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 21,620,000.00 USD | 21,620,000.00 USD | 156,790.00 USD | 2,950,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 24,780,000.00 USD | 24,780,000.00 USD | 1,620,000.00 USD | 1,300,000.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 31,350,000.00 USD | 31,350,000.00 USD | 1,680,000.00 USD | 5,310,000.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 33,150,000.00 USD | 33,150,000.00 USD | 1,380,000.00 USD | 2,380,000.00 USD | 4,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 48,830,000.00 USD | 48,830,000.00 USD | 2,840,000.00 USD | 3,400,000.00 USD | 11,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 13,790.00 USD | 13,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 40,740,000.00 USD | 40,740,000.00 USD | 1,690,000.00 USD | 1,960,000.00 USD | 3,940,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 64,150,000.00 USD | 64,150,000.00 USD | 5,290,000.00 USD | 3,080,000.00 USD | 6,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 49,330,000.00 USD | 49,330,000.00 USD | 3,260,000.00 USD | 1,370,000.00 USD | 3,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 83,820,000.00 USD | 83,820,000.00 USD | 7,780,000.00 USD | 3,760,000.00 USD | 8,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 55,120,000.00 USD | 55,120,000.00 USD | 551,850.00 USD | 1,860,000.00 USD | 3,370,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 87,410,000.00 USD | 87,410,000.00 USD | 0.00 USD | 1,700,000.00 USD | 1,890,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 59,710,000.00 USD | 59,710,000.00 USD | 1,030,000.00 USD | 367,140.00 USD | 3,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 89,550,000.00 USD | 89,550,000.00 USD | 1,040,000.00 USD | 234,920.00 USD | 861,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 62,930,000.00 USD | 62,930,000.00 USD | 1,290,000.00 USD | 629,480.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 93,800,000.00 USD | 93,800,000.00 USD | 1,100,000.00 USD | 1,300,000.00 USD | 1,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 48,800.00 USD | 62,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 67,240,000.00 USD | 67,240,000.00 USD | 818,130.00 USD | 1,150,000.00 USD | 2,340,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 98,930,000.00 USD | 98,930,000.00 USD | 796,960.00 USD | 1,560,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 69,080,000.00 USD | 69,080,000.00 USD | 787,490.00 USD | 457,810.00 USD | 591,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 99,650,000.00 USD | 99,650,000.00 USD | 685,300.00 USD | 2,730.00 USD | 33,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 69,900,000.00 USD | 69,900,000.00 USD | 156,280.00 USD | 213,200.00 USD | 456,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 101,250,000.00 USD | 101,250,000.00 USD | 70,460.00 USD | 277,240.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 73,240,000.00 USD | 73,240,000.00 USD | 378,690.00 USD | 236,330.00 USD | 2,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 103,850,000.00 USD | 103,850,000.00 USD | 1,040,000.00 USD | 202,640.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 77,710,000.00 USD | 77,710,000.00 USD | 1,170,000.00 USD | 374,490.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 107,510,000.00 USD | 107,510,000.00 USD | 1,780,000.00 USD | 8,810.00 USD | 1,880,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 64,820.00 USD | 127,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 83,210,000.00 USD | 83,210,000.00 USD | 1,470,000.00 USD | 1,240,000.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 115,230,000.00 USD | 115,230,000.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 4,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 84,530,000.00 USD | 84,530,000.00 USD | 544,620.00 USD | 21,940.00 USD | 751,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 117,180,000.00 USD | 117,180,000.00 USD | 25,800.00 USD | 173,700.00 USD | 1,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 86,490,000.00 USD | 86,490,000.00 USD | 439,090.00 USD | 461,990.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 119,620,000.00 USD | 119,620,000.00 USD | 272,980.00 USD | 434,510.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 89,340,000.00 USD | 89,340,000.00 USD | 810,010.00 USD | 640,150.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 120,880,000.00 USD | 120,880,000.00 USD | 158,990.00 USD | 944,610.00 USD | 158,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 90,820,000.00 USD | 90,820,000.00 USD | 481,740.00 USD | 328,660.00 USD | 666,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 123,940,000.00 USD | 123,940,000.00 USD | 0.00 USD | 2,170,000.00 USD | 887,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 281,910.00 USD | 409,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 93,090,000.00 USD | 93,090,000.00 USD | 631,950.00 USD | 559,170.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 126,240,000.00 USD | 126,240,000.00 USD | 1,770,000.00 USD | 286,020.00 USD | 245,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 96,950,000.00 USD | 96,950,000.00 USD | 977,640.00 USD | 522,010.00 USD | 2,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 131,670,000.00 USD | 131,670,000.00 USD | 1,560,000.00 USD | 821,310.00 USD | 3,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 100,350,000.00 USD | 100,350,000.00 USD | 1,310,000.00 USD | 359,190.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 134,440,000.00 USD | 134,440,000.00 USD | 1,340,000.00 USD | 635,040.00 USD | 789,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 103,050,000.00 USD | 103,050,000.00 USD | 919,330.00 USD | 635,660.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 139,310,000.00 USD | 139,310,000.00 USD | 189,510.00 USD | 858,660.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 104,610,000.00 USD | 104,610,000.00 USD | 503,300.00 USD | 157,920.00 USD | 891,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 140,600,000.00 USD | 140,600,000.00 USD | 638,380.00 USD | 151,320.00 USD | 501,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.31` | 55,110.00 USD | 464,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.32` | 107,430,000.00 USD | 107,430,000.00 USD | 174,570.00 USD | 546,170.00 USD | 2,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 145,320,000.00 USD | 145,320,000.00 USD | 68,520.00 USD | 1,890,000.00 USD | 2,760,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 113,040,000.00 USD | 113,040,000.00 USD | 1,730,000.00 USD | 623,240.00 USD | 3,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 150,420,000.00 USD | 150,420,000.00 USD | 1,560,000.00 USD | 457,220.00 USD | 3,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 115,210,000.00 USD | 115,210,000.00 USD | 1,200,000.00 USD | 197,040.00 USD | 769,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 152,440,000.00 USD | 152,440,000.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 117,960,000.00 USD | 117,960,000.00 USD | 1,030,000.00 USD | 608,700.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 155,800,000.00 USD | 155,800,000.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 119,740,000.00 USD | 119,740,000.00 USD | 867,870.00 USD | 61,350.00 USD | 851,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 158,570,000.00 USD | 158,570,000.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 7,390.00 USD | 471,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 120,780,000.00 USD | 120,780,000.00 USD | 405,790.00 USD | 54,470.00 USD | 578,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 160,380,000.00 USD | 160,380,000.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 122,000,000.00 USD | 122,000,000.00 USD | 545,530.00 USD | 175,480.00 USD | 494,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 161,480,000.00 USD | 161,480,000.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 123,690,000.00 USD | 123,690,000.00 USD | 729,070.00 USD | 104,910.00 USD | 862,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 163,190,000.00 USD | 163,190,000.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 125,520,000.00 USD | 125,520,000.00 USD | 465,720.00 USD | 180,450.00 USD | 1,180,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 165,660,000.00 USD | 165,660,000.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 127,370,000.00 USD | 127,370,000.00 USD | 783,210.00 USD | 227,790.00 USD | 838,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 167,690,000.00 USD | 167,690,000.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 43,550.00 USD | 515,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 128,480,000.00 USD | 128,480,000.00 USD | 286,040.00 USD | 207,050.00 USD | 616,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 169,230,000.00 USD | 169,230,000.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 128,940,000.00 USD | 128,940,000.00 USD | 240,600.00 USD | 80,780.00 USD | 141,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 171,670,000.00 USD | 171,670,000.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 129,730,000.00 USD | 129,730,000.00 USD | 331,150.00 USD | 119,540.00 USD | 335,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 173,530,000.00 USD | 173,530,000.00 USD | 804,660.00 USD | 463,950.00 USD | 588,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 130,850,000.00 USD | 130,850,000.00 USD | 616,160.00 USD | 165,460.00 USD | 342,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 178,990,000.00 USD | 178,990,000.00 USD | 2,380,000.00 USD | 2,430,000.00 USD | 660,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 131,830,000.00 USD | 131,830,000.00 USD | 365,760.00 USD | 246,750.00 USD | 369,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 186,110,000.00 USD | 186,110,000.00 USD | 2,000,000.00 USD | 1,890,000.00 USD | 3,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 6,380.00 USD | 521,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 132,360,000.00 USD | 132,360,000.00 USD | 189,800.00 USD | 64,310.00 USD | 274,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 194,370,000.00 USD | 194,370,000.00 USD | 3,270,000.00 USD | 1,640,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 132,760,000.00 USD | 132,760,000.00 USD | 123,430.00 USD | 3,590.00 USD | 270,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 202,120,000.00 USD | 202,120,000.00 USD | 2,780,000.00 USD | 1,820,000.00 USD | 3,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 133,110,000.00 USD | 133,110,000.00 USD | 177,170.00 USD | 30,570.00 USD | 146,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 210,140,000.00 USD | 210,140,000.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 133,390,000.00 USD | 133,390,000.00 USD | 69,740.00 USD | 26,920.00 USD | 174,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 219,260,000.00 USD | 219,260,000.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 133,690,000.00 USD | 133,690,000.00 USD | 105,080.00 USD | 4,310.00 USD | 194,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 226,010,000.00 USD | 226,010,000.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 2,700.00 USD | 524,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 134,520,000.00 USD | 134,520,000.00 USD | 335,960.00 USD | 66,020.00 USD | 426,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 232,350,000.00 USD | 232,350,000.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 135,020,000.00 USD | 135,020,000.00 USD | 148,530.00 USD | 44,160.00 USD | 310,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 234,890,000.00 USD | 234,890,000.00 USD | 1,060,000.00 USD | 639,580.00 USD | 837,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 135,570,000.00 USD | 135,570,000.00 USD | 269,010.00 USD | 48,080.00 USD | 234,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 237,530,000.00 USD | 237,530,000.00 USD | 1,300,000.00 USD | 280,910.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 136,110,000.00 USD | 136,110,000.00 USD | 143,090.00 USD | 117,400.00 USD | 276,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 240,790,000.00 USD | 240,790,000.00 USD | 1,480,000.00 USD | 652,340.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 136,210,000.00 USD | 136,210,000.00 USD | 78,610.00 USD | 13,410.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 243,450,000.00 USD | 243,450,000.00 USD | 1,420,000.00 USD | 531,090.00 USD | 698,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 1,510.00 USD | 525,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 136,470,000.00 USD | 136,470,000.00 USD | 56,040.00 USD | 477.43 USD | 206,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 244,260,000.00 USD | 244,260,000.00 USD | 206,650.00 USD | 189,790.00 USD | 421,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 136,770,000.00 USD | 136,770,000.00 USD | 98,240.00 USD | 110,720.00 USD | 87,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 245,320,000.00 USD | 245,320,000.00 USD | 486,840.00 USD | 176,380.00 USD | 389,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 136,780,000.00 USD | 136,780,000.00 USD | 1,170.00 USD | 10,080.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 246,740,000.00 USD | 246,740,000.00 USD | 367,350.00 USD | 211,750.00 USD | 841,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 136,990,000.00 USD | 136,990,000.00 USD | 6,620.00 USD | 30,590.00 USD | 175,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 247,970,000.00 USD | 247,970,000.00 USD | 393,010.00 USD | 171,680.00 USD | 667,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 137,100,000.00 USD | 137,100,000.00 USD | 31,610.00 USD | 8,290.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 249,640,000.00 USD | 249,640,000.00 USD | 563,840.00 USD | 386,690.00 USD | 717,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 647,210.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.38` | 137,560,000.00 USD | 137,560,000.00 USD | 126,800.00 USD | 79,730.00 USD | 249,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 250,670,000.00 USD | 250,670,000.00 USD | 242,030.00 USD | 273,360.00 USD | 514,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 137,910,000.00 USD | 137,910,000.00 USD | 77,710.00 USD | 59,850.00 USD | 210,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 252,230,000.00 USD | 252,230,000.00 USD | 692,200.00 USD | 267,730.00 USD | 600,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 138,120,000.00 USD | 138,120,000.00 USD | 22,650.00 USD | 53,100.00 USD | 132,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 253,930,000.00 USD | 253,930,000.00 USD | 436,360.00 USD | 195,830.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 138,470,000.00 USD | 138,470,000.00 USD | 6,880.00 USD | 73,390.00 USD | 273,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 255,890,000.00 USD | 255,890,000.00 USD | 710,620.00 USD | 348,810.00 USD | 900,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 138,870,000.00 USD | 138,870,000.00 USD | 5,520.00 USD | 78,550.00 USD | 312,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 256,870,000.00 USD | 256,870,000.00 USD | 403,730.00 USD | 253,120.00 USD | 325,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 1,510.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 139,160,000.00 USD | 139,160,000.00 USD | 91,470.00 USD | 89,100.00 USD | 110,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 257,980,000.00 USD | 257,980,000.00 USD | 377,810.00 USD | 322,570.00 USD | 413,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 139,510,000.00 USD | 139,510,000.00 USD | 40,370.00 USD | 153,030.00 USD | 160,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 259,200,000.00 USD | 259,200,000.00 USD | 384,080.00 USD | 308,280.00 USD | 518,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 259,950,000.00 USD | 259,950,000.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 260,480,000.00 USD | 260,480,000.00 USD | 82,350.00 USD | 90,970.00 USD | 358,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 260,640,000.00 USD | 260,640,000.00 USD | 39,170.00 USD | 22,660.00 USD | 101,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 2,310.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 260,860,000.00 USD | 260,860,000.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 260,870,000.00 USD | 260,870,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 260,930,000.00 USD | 260,930,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 261,010,000.00 USD | 261,010,000.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 261,310,000.00 USD | 261,310,000.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 2,670.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 261,460,000.00 USD | 261,460,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 261,600,000.00 USD | 261,600,000.00 USD | 4,390.00 USD | 15,880.00 USD | 120,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 261,880,000.00 USD | 261,880,000.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 46,840.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,510.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.44` | 1,220.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.45` | 284.66 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.47` | 129,170.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.48` | 551.65 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,150.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 12,140.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 174.99 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 1,370.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 555.57 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,900.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 4,430,000.00 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 239.15 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 3,760.00 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 8,920.00 USD | 5,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 6,750.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 135,800.00 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 120.60 USD | 6,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 15,830.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 110.17 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 2,110.00 USD | 6,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.72` | 140,830.00 USD | 6,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 1,110.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 7,300.00 USD | 6,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 113,360.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 5,390,000.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 1,250.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 130,520.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 4,530.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 1,780.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 12,710.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 120.45 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 29,790.00 USD | 11,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 29,320.00 USD | 11,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 428.50 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 2,880,000.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.88` | 946.88 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 4,300.00 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 373.38 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 180.01 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 310,420.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 1,240.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 3,230.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 227,560.00 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 651.75 USD | 15,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 2,390,000.00 USD | 17,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 401,870.00 USD | 18,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 799.96 USD | 18,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 178.20 USD | 18,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 198.36 USD | 18,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 170.56 USD | 18,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 460.50 USD | 18,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 708.11 USD | 18,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 81,120.00 USD | 18,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 251,210.00 USD | 18,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 18,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 49,710.00 USD | 18,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 82,770.00 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 2,110.00 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 438.80 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 11,670.00 USD | 18,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 43,950.00 USD | 18,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 2,060.00 USD | 18,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 105.57 USD | 18,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 248.94 USD | 18,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 106.49 USD | 18,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 1,310.00 USD | 18,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 1,550.00 USD | 18,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 14,540.00 USD | 18,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 4,140.00 USD | 18,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 3,590,000.00 USD | 22,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 477.00 USD | 22,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 1,470,000.00 USD | 23,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.40` | 610.87 USD | 23,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 81,630.00 USD | 23,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 364,240.00 USD | 24,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 24,510.00 USD | 24,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 3,580.00 USD | 24,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.46` | 19,100.00 USD | 24,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 306.90 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.48` | 144.13 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.50` | 95,910.00 USD | 24,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.52` | 5,630.00 USD | 24,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 64,410,000.00 USD | 0.00 USD | 10,850.00 USD | `-79.73%` | `42,557.00` |
| `Live` | `Long` | `0.2650` | 64,390,000.00 USD | 0.00 USD | 6,060.00 USD | `-78.94%` | `22,862.00` |
| `Live` | `Long` | `0.2750` | 64,390,000.00 USD | 0.00 USD | 1,090.00 USD | `-78.14%` | `3,950.00` |
| `Live` | `Long` | `0.2850` | 64,390,000.00 USD | 0.00 USD | 1,410.00 USD | `-77.35%` | `4,963.00` |
| `Live` | `Long` | `0.3050` | 64,390,000.00 USD | 0.00 USD | 1,050.00 USD | `-75.76%` | `3,432.00` |
| `Live` | `Long` | `0.3150` | 64,390,000.00 USD | 0.00 USD | 10,710.00 USD | `-74.96%` | `34,015.00` |
| `Live` | `Long` | `0.3250` | 64,370,000.00 USD | 0.00 USD | 53,390.00 USD | `-74.17%` | `164,267.00` |
| `Live` | `Long` | `0.3350` | 64,320,000.00 USD | 0.00 USD | 4,960.00 USD | `-73.37%` | `14,809.00` |
| `Live` | `Long` | `0.3450` | 64,320,000.00 USD | 0.00 USD | 139.38 USD | `-72.58%` | `404.00` |
| `Live` | `Long` | `0.3550` | 64,320,000.00 USD | 0.00 USD | 2,770.00 USD | `-71.78%` | `7,804.00` |
| `Live` | `Long` | `0.3650` | 64,310,000.00 USD | 0.00 USD | 4,670.00 USD | `-70.99%` | `12,790.00` |
| `Live` | `Long` | `0.3750` | 64,310,000.00 USD | 0.00 USD | 1,170.00 USD | `-70.19%` | `3,129.00` |
| `Live` | `Long` | `0.3850` | 64,310,000.00 USD | 0.00 USD | 269.50 USD | `-69.40%` | `700.00` |
| `Live` | `Long` | `0.3950` | 64,310,000.00 USD | 0.00 USD | 2,640.00 USD | `-68.60%` | `6,671.00` |
| `Live` | `Long` | `0.4050` | 64,300,000.00 USD | 0.00 USD | 3,210.00 USD | `-67.81%` | `7,930.00` |
| `Live` | `Long` | `0.4150` | 64,300,000.00 USD | 0.00 USD | 2,170.00 USD | `-67.01%` | `5,220.00` |
| `Live` | `Long` | `0.4250` | 64,300,000.00 USD | 0.00 USD | 1,020.00 USD | `-66.22%` | `2,400.00` |
| `Live` | `Long` | `0.4350` | 64,300,000.00 USD | 0.00 USD | 585,350.00 USD | `-65.42%` | `1,345,635.00` |
| `Live` | `Long` | `0.4450` | 63,710,000.00 USD | 0.00 USD | 155,750.00 USD | `-64.63%` | `350,000.00` |
| `Live` | `Long` | `0.4550` | 63,560,000.00 USD | 0.00 USD | 244.34 USD | `-63.83%` | `537.00` |
| `Live` | `Long` | `0.4650` | 63,560,000.00 USD | 0.00 USD | 1,700.00 USD | `-63.04%` | `3,656.00` |
| `Live` | `Long` | `0.4750` | 63,560,000.00 USD | 0.00 USD | 13,510.00 USD | `-62.24%` | `28,432.00` |
| `Live` | `Long` | `0.4850` | 63,540,000.00 USD | 0.00 USD | 121.25 USD | `-61.45%` | `250.00` |
| `Live` | `Long` | `0.5050` | 63,540,000.00 USD | 0.00 USD | 444.91 USD | `-59.86%` | `881.00` |
| `Live` | `Long` | `0.5150` | 63,540,000.00 USD | 0.00 USD | 2,890.00 USD | `-59.07%` | `5,603.00` |
| `Live` | `Long` | `0.5250` | 63,540,000.00 USD | 0.00 USD | 10,750.00 USD | `-58.27%` | `20,472.00` |
| `Live` | `Long` | `0.5350` | 63,530,000.00 USD | 0.00 USD | 154,280.00 USD | `-57.48%` | `288,375.00` |
| `Live` | `Long` | `0.5450` | 63,370,000.00 USD | 0.00 USD | 14,210.00 USD | `-56.68%` | `26,082.00` |
| `Live` | `Long` | `0.5550` | 63,360,000.00 USD | 0.00 USD | 6,690.00 USD | `-55.89%` | `12,057.00` |
| `Live` | `Long` | `0.5650` | 63,350,000.00 USD | 0.00 USD | 5,160.00 USD | `-55.09%` | `9,137.00` |
| `Live` | `Long` | `0.5750` | 63,350,000.00 USD | 0.00 USD | 7,130.00 USD | `-54.30%` | `12,402.00` |
| `Live` | `Long` | `0.5850` | 63,340,000.00 USD | 0.00 USD | 3,920.00 USD | `-53.50%` | `6,698.00` |
| `Live` | `Long` | `0.5950` | 63,340,000.00 USD | 0.00 USD | 6,520.00 USD | `-52.71%` | `10,951.00` |
| `Live` | `Long` | `0.6050` | 63,330,000.00 USD | 0.00 USD | 39,370.00 USD | `-51.91%` | `65,077.00` |
| `Live` | `Long` | `0.6150` | 63,290,000.00 USD | 0.00 USD | 36,560.00 USD | `-51.12%` | `59,444.00` |
| `Live` | `Long` | `0.6250` | 63,250,000.00 USD | 0.00 USD | 9,040.00 USD | `-50.32%` | `14,460.00` |
| `Live` | `Long` | `0.6350` | 63,240,000.00 USD | 0.00 USD | 12,180.00 USD | `-49.53%` | `19,187.00` |
| `Live` | `Long` | `0.6450` | 63,230,000.00 USD | 0.00 USD | 19,930.00 USD | `-48.73%` | `30,901.00` |
| `Live` | `Long` | `0.6550` | 63,210,000.00 USD | 0.00 USD | 11,640.00 USD | `-47.94%` | `17,769.00` |
| `Live` | `Long` | `0.6650` | 63,200,000.00 USD | 0.00 USD | 17,310.00 USD | `-47.14%` | `26,027.00` |
| `Live` | `Long` | `0.6750` | 63,180,000.00 USD | 0.00 USD | 28,750.00 USD | `-46.35%` | `42,587.00` |
| `Live` | `Long` | `0.6850` | 63,150,000.00 USD | 0.00 USD | 3,380.00 USD | `-45.55%` | `4,930.00` |
| `Live` | `Long` | `0.6950` | 63,150,000.00 USD | 0.00 USD | 142,460.00 USD | `-44.76%` | `204,973.00` |
| `Live` | `Long` | `0.7050` | 63,010,000.00 USD | 0.00 USD | 31,130.00 USD | `-43.96%` | `44,154.00` |
| `Live` | `Long` | `0.7150` | 62,980,000.00 USD | 0.00 USD | 67,660.00 USD | `-43.17%` | `94,630.00` |
| `Live` | `Long` | `0.7250` | 62,910,000.00 USD | 0.00 USD | 217,180.00 USD | `-42.37%` | `299,562.00` |
| `Live` | `Long` | `0.7350` | 62,690,000.00 USD | 0.00 USD | 106,710.00 USD | `-41.58%` | `145,188.00` |
| `Live` | `Long` | `0.7450` | 62,590,000.00 USD | 0.00 USD | 70,830.00 USD | `-40.78%` | `95,075.00` |
| `Live` | `Long` | `0.7550` | 62,520,000.00 USD | 0.00 USD | 91,900.00 USD | `-39.99%` | `121,727.00` |
| `Live` | `Long` | `0.7650` | 62,420,000.00 USD | 0.00 USD | 2,320.00 USD | `-39.19%` | `3,032.00` |
| `Live` | `Long` | `0.7750` | 62,420,000.00 USD | 0.00 USD | 6,230.00 USD | `-38.40%` | `8,045.00` |
| `Live` | `Long` | `0.7850` | 62,410,000.00 USD | 0.00 USD | 509,740.00 USD | `-37.60%` | `649,353.00` |
| `Live` | `Long` | `0.7950` | 61,910,000.00 USD | 0.00 USD | 23,170.00 USD | `-36.81%` | `29,147.00` |
| `Live` | `Long` | `0.8050` | 61,880,000.00 USD | 0.00 USD | 17,590.00 USD | `-36.01%` | `21,852.00` |
| `Live` | `Long` | `0.8150` | 61,860,000.00 USD | 0.00 USD | 48,100.00 USD | `-35.22%` | `59,014.00` |
| `Live` | `Long` | `0.8250` | 61,820,000.00 USD | 0.00 USD | 5,580.00 USD | `-34.42%` | `6,762.00` |
| `Live` | `Long` | `0.8350` | 61,810,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-33.63%` | `3,593,083.00` |
| `Live` | `Long` | `0.8450` | 58,810,000.00 USD | 0.00 USD | 67,320.00 USD | `-32.84%` | `79,671.00` |
| `Live` | `Long` | `0.8550` | 58,740,000.00 USD | 0.00 USD | 63,720.00 USD | `-32.04%` | `74,525.00` |
| `Live` | `Long` | `0.8650` | 58,680,000.00 USD | 0.00 USD | 35,380.00 USD | `-31.25%` | `40,898.00` |
| `Live` | `Long` | `0.8750` | 58,640,000.00 USD | 0.00 USD | 112,870.00 USD | `-30.45%` | `128,998.00` |
| `Live` | `Long` | `0.8850` | 58,530,000.00 USD | 0.00 USD | 393,690.00 USD | `-29.66%` | `444,847.00` |
| `Live` | `Long` | `0.8950` | 58,140,000.00 USD | 0.00 USD | 140,940.00 USD | `-28.86%` | `157,475.00` |
| `Live` | `Long` | `0.9050` | 58,000,000.00 USD | 0.00 USD | 132,420.00 USD | `-28.07%` | `146,315.00` |
| `Live` | `Long` | `0.9150` | 57,860,000.00 USD | 0.00 USD | 86,550.00 USD | `-27.27%` | `94,585.00` |
| `Live` | `Long` | `0.9250` | 57,780,000.00 USD | 0.00 USD | 71,480.00 USD | `-26.48%` | `77,272.00` |
| `Live` | `Long` | `0.9350` | 57,710,000.00 USD | 0.00 USD | 86,260.00 USD | `-25.68%` | `92,260.00` |
| `Live` | `Long` | `0.9450` | 57,620,000.00 USD | 0.00 USD | 63,620.00 USD | `-24.89%` | `67,324.00` |
| `Live` | `Long` | `0.9550` | 57,560,000.00 USD | 0.00 USD | 154,550.00 USD | `-24.09%` | `161,837.00` |
| `Live` | `Long` | `0.9650` | 57,400,000.00 USD | 0.00 USD | 33,900,000.00 USD | `-23.30%` | `35,131,978.00` |
| `Live` | `Long` | `0.9750` | 23,500,000.00 USD | 0.00 USD | 157,210.00 USD | `-22.50%` | `161,244.00` |
| `Live` | `Long` | `0.9850` | 23,340,000.00 USD | 0.00 USD | 447,720.00 USD | `-21.71%` | `454,534.00` |
| `Live` | `Long` | `0.9950` | 22,890,000.00 USD | 0.00 USD | 2,690,000.00 USD | `-20.91%` | `2,702,087.00` |
| `Live` | `Long` | `1.00` | 20,210,000.00 USD | 0.00 USD | 466,450.00 USD | `-20.12%` | `464,128.00` |
| `Live` | `Long` | `1.01` | 19,740,000.00 USD | 0.00 USD | 294,250.00 USD | `-19.32%` | `289,899.00` |
| `Live` | `Long` | `1.02` | 19,450,000.00 USD | 0.00 USD | 80,710.00 USD | `-18.53%` | `78,739.00` |
| `Live` | `Long` | `1.03` | 19,360,000.00 USD | 0.00 USD | 2,190,000.00 USD | `-17.73%` | `2,119,953.00` |
| `Live` | `Long` | `1.04` | 17,170,000.00 USD | 0.00 USD | 698,670.00 USD | `-16.94%` | `668,583.00` |
| `Live` | `Long` | `1.05` | 16,470,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-16.14%` | `1,077,898.00` |
| `Live` | `Long` | `1.06` | 15,330,000.00 USD | 0.00 USD | 379,080.00 USD | `-15.35%` | `355,941.00` |
| `Live` | `Long` | `1.07` | 14,960,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-14.55%` | `1,063,801.00` |
| `Live` | `Long` | `1.08` | 13,810,000.00 USD | 0.00 USD | 216,770.00 USD | `-13.76%` | `199,786.00` |
| `Live` | `Long` | `1.09` | 13,590,000.00 USD | 0.00 USD | 695,430.00 USD | `-12.96%` | `635,094.00` |
| `Live` | `Long` | `1.10` | 12,900,000.00 USD | 0.00 USD | 98,950.00 USD | `-12.17%` | `89,545.00` |
| `Live` | `Long` | `1.11` | 12,800,000.00 USD | 0.00 USD | 280,050.00 USD | `-11.37%` | `251,162.00` |
| `Live` | `Long` | `1.12` | 12,520,000.00 USD | 0.00 USD | 2,190,000.00 USD | `-10.58%` | `1,944,542.00` |
| `Live` | `Long` | `1.14` | 10,330,000.00 USD | 0.00 USD | 114,760.00 USD | `-9.78%` | `101,114.00` |
| `Live` | `Long` | `1.15` | 10,220,000.00 USD | 0.00 USD | 495,010.00 USD | `-8.99%` | `432,325.00` |
| `Live` | `Long` | `1.16` | 9,720,000.00 USD | 0.00 USD | 118,760.00 USD | `-8.19%` | `102,821.00` |
| `Live` | `Long` | `1.17` | 9,600,000.00 USD | 0.00 USD | 1,280,000.00 USD | `-7.40%` | `1,102,157.00` |
| `Live` | `Long` | `1.18` | 8,320,000.00 USD | 0.00 USD | 290,280.00 USD | `-6.61%` | `247,047.00` |
| `Live` | `Long` | `1.19` | 8,030,000.00 USD | 0.00 USD | 498,200.00 USD | `-5.81%` | `420,422.00` |
| `Live` | `Long` | `1.20` | 7,530,000.00 USD | 0.00 USD | 587,240.00 USD | `-5.02%` | `491,417.00` |
| `Live` | `Long` | `1.21` | 6,940,000.00 USD | 0.00 USD | 8,380.00 USD | `-4.22%` | `6,955.00` |
| `Live` | `Long` | `1.22` | 6,940,000.00 USD | 0.00 USD | 104,870.00 USD | `-3.43%` | `86,314.00` |
| `Live` | `Long` | `1.23` | 6,830,000.00 USD | 0.00 USD | 6,810,000.00 USD | `-2.63%` | `5,561,122.00` |
| `Live` | `Long` | `1.24` | 18,990.00 USD | 0.00 USD | 18,990.00 USD | `-1.84%` | `15,375.00` |
| `Live` | `Short` | `1.27` | 13,790.00 USD | 13,790.00 USD | 0.00 USD | `+1.34%` | `10,813.00` |
| `Live` | `Short` | `1.28` | 62,590.00 USD | 48,800.00 USD | 0.00 USD | `+2.14%` | `37,978.00` |
| `Live` | `Short` | `1.29` | 127,410.00 USD | 64,820.00 USD | 0.00 USD | `+2.93%` | `50,053.00` |
| `Live` | `Short` | `1.30` | 409,320.00 USD | 281,910.00 USD | 0.00 USD | `+3.73%` | `216,022.00` |
| `Live` | `Short` | `1.31` | 464,430.00 USD | 55,110.00 USD | 0.00 USD | `+4.52%` | `41,912.00` |
| `Live` | `Short` | `1.32` | 471,820.00 USD | 7,390.00 USD | 0.00 USD | `+5.32%` | `5,576.00` |
| `Live` | `Short` | `1.33` | 515,370.00 USD | 43,550.00 USD | 0.00 USD | `+6.11%` | `32,622.00` |
| `Live` | `Short` | `1.34` | 521,750.00 USD | 6,380.00 USD | 0.00 USD | `+6.91%` | `4,742.00` |
| `Live` | `Short` | `1.35` | 524,440.00 USD | 2,700.00 USD | 0.00 USD | `+7.70%` | `1,989.00` |
| `Live` | `Short` | `1.36` | 525,950.00 USD | 1,510.00 USD | 0.00 USD | `+8.50%` | `1,105.00` |
| `Live` | `Short` | `1.38` | 1,170,000.00 USD | 647,210.00 USD | 0.00 USD | `+9.29%` | `470,696.00` |
| `Live` | `Short` | `1.39` | 1,170,000.00 USD | 1,510.00 USD | 0.00 USD | `+10.09%` | `1,093.00` |
| `Live` | `Short` | `1.40` | 1,180,000.00 USD | 2,310.00 USD | 0.00 USD | `+10.88%` | `1,659.00` |
| `Live` | `Short` | `1.41` | 1,180,000.00 USD | 2,670.00 USD | 0.00 USD | `+11.68%` | `1,900.00` |
| `Live` | `Short` | `1.42` | 1,230,000.00 USD | 46,840.00 USD | 0.00 USD | `+12.47%` | `33,102.00` |
| `Live` | `Short` | `1.43` | 1,320,000.00 USD | 93,510.00 USD | 0.00 USD | `+13.27%` | `65,619.00` |
| `Live` | `Short` | `1.44` | 1,320,000.00 USD | 1,220.00 USD | 0.00 USD | `+14.06%` | `848.00` |
| `Live` | `Short` | `1.45` | 1,320,000.00 USD | 284.66 USD | 0.00 USD | `+14.86%` | `197.00` |
| `Live` | `Short` | `1.47` | 1,450,000.00 USD | 129,170.00 USD | 0.00 USD | `+16.45%` | `88,171.00` |
| `Live` | `Short` | `1.48` | 1,450,000.00 USD | 551.65 USD | 0.00 USD | `+17.24%` | `374.00` |
| `Live` | `Short` | `1.50` | 1,460,000.00 USD | 12,150.00 USD | 0.00 USD | `+18.83%` | `8,126.00` |
| `Live` | `Short` | `1.51` | 1,480,000.00 USD | 12,140.00 USD | 0.00 USD | `+20.42%` | `8,011.00` |
| `Live` | `Short` | `1.53` | 1,480,000.00 USD | 174.99 USD | 0.00 USD | `+22.01%` | `114.00` |
| `Live` | `Short` | `1.54` | 1,480,000.00 USD | 1,370.00 USD | 0.00 USD | `+22.80%` | `889.00` |
| `Live` | `Short` | `1.55` | 1,480,000.00 USD | 1,360.00 USD | 0.00 USD | `+23.60%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,480,000.00 USD | 555.57 USD | 0.00 USD | `+24.39%` | `355.00` |
| `Live` | `Short` | `1.57` | 1,480,000.00 USD | 2,900.00 USD | 0.00 USD | `+25.19%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 5,910,000.00 USD | 4,430,000.00 USD | 0.00 USD | `+25.98%` | `2,793,593.00` |
| `Live` | `Short` | `1.60` | 5,910,000.00 USD | 239.15 USD | 0.00 USD | `+27.57%` | `149.00` |
| `Live` | `Short` | `1.61` | 5,910,000.00 USD | 3,760.00 USD | 0.00 USD | `+28.37%` | `2,329.00` |
| `Live` | `Short` | `1.62` | 5,920,000.00 USD | 8,920.00 USD | 0.00 USD | `+29.16%` | `5,489.00` |
| `Live` | `Short` | `1.64` | 5,930,000.00 USD | 6,750.00 USD | 0.00 USD | `+29.96%` | `4,131.00` |
| `Live` | `Short` | `1.66` | 5,930,000.00 USD | 147.30 USD | 0.00 USD | `+31.55%` | `89.00` |
| `Live` | `Short` | `1.67` | 6,070,000.00 USD | 135,800.00 USD | 0.00 USD | `+32.34%` | `81,562.00` |
| `Live` | `Short` | `1.68` | 6,070,000.00 USD | 120.60 USD | 0.00 USD | `+33.14%` | `72.00` |
| `Live` | `Short` | `1.69` | 6,080,000.00 USD | 15,830.00 USD | 0.00 USD | `+33.93%` | `9,396.00` |
| `Live` | `Short` | `1.70` | 6,080,000.00 USD | 110.17 USD | 0.00 USD | `+34.73%` | `65.00` |
| `Live` | `Short` | `1.71` | 6,080,000.00 USD | 2,110.00 USD | 0.00 USD | `+35.52%` | `1,240.00` |
| `Live` | `Short` | `1.72` | 6,220,000.00 USD | 140,830.00 USD | 0.00 USD | `+36.32%` | `82,115.00` |
| `Live` | `Short` | `1.73` | 6,230,000.00 USD | 1,110.00 USD | 0.00 USD | `+37.11%` | `642.00` |
| `Live` | `Short` | `1.74` | 6,230,000.00 USD | 7,300.00 USD | 0.00 USD | `+37.91%` | `4,208.00` |
| `Live` | `Short` | `1.75` | 6,350,000.00 USD | 113,360.00 USD | 0.00 USD | `+38.70%` | `64,965.00` |
| `Live` | `Short` | `1.75` | 11,730,000.00 USD | 5,390,000.00 USD | 0.00 USD | `+39.50%` | `3,070,568.00` |
| `Live` | `Short` | `1.76` | 11,740,000.00 USD | 1,250.00 USD | 0.00 USD | `+40.29%` | `710.00` |
| `Live` | `Short` | `1.78` | 11,870,000.00 USD | 130,520.00 USD | 0.00 USD | `+41.88%` | `73,118.00` |
| `Live` | `Short` | `1.79` | 11,870,000.00 USD | 4,530.00 USD | 0.00 USD | `+42.68%` | `2,525.00` |
| `Live` | `Short` | `1.80` | 11,870,000.00 USD | 1,780.00 USD | 0.00 USD | `+43.47%` | `987.00` |
| `Live` | `Short` | `1.81` | 11,890,000.00 USD | 12,710.00 USD | 0.00 USD | `+44.27%` | `7,004.00` |
| `Live` | `Short` | `1.82` | 11,890,000.00 USD | 120.45 USD | 0.00 USD | `+45.06%` | `66.00` |
| `Live` | `Short` | `1.83` | 11,920,000.00 USD | 29,790.00 USD | 0.00 USD | `+45.85%` | `16,235.00` |
| `Live` | `Short` | `1.84` | 11,940,000.00 USD | 29,320.00 USD | 0.00 USD | `+46.65%` | `15,893.00` |
| `Live` | `Short` | `1.85` | 11,950,000.00 USD | 428.50 USD | 0.00 USD | `+47.44%` | `231.00` |
| `Live` | `Short` | `1.86` | 14,820,000.00 USD | 2,880,000.00 USD | 0.00 USD | `+48.24%` | `1,541,775.00` |
| `Live` | `Short` | `1.88` | 14,820,000.00 USD | 946.88 USD | 0.00 USD | `+49.03%` | `505.00` |
| `Live` | `Short` | `1.90` | 14,830,000.00 USD | 4,300.00 USD | 0.00 USD | `+50.62%` | `2,268.00` |
| `Live` | `Short` | `1.91` | 14,830,000.00 USD | 373.38 USD | 0.00 USD | `+51.42%` | `196.00` |
| `Live` | `Short` | `1.92` | 14,830,000.00 USD | 180.01 USD | 0.00 USD | `+52.21%` | `94.00` |
| `Live` | `Short` | `1.93` | 15,140,000.00 USD | 310,420.00 USD | 0.00 USD | `+53.01%` | `161,259.00` |
| `Live` | `Short` | `1.94` | 15,140,000.00 USD | 1,240.00 USD | 0.00 USD | `+53.80%` | `643.00` |
| `Live` | `Short` | `1.96` | 15,140,000.00 USD | 3,230.00 USD | 0.00 USD | `+55.39%` | `1,650.00` |
| `Live` | `Short` | `1.97` | 15,370,000.00 USD | 227,560.00 USD | 0.00 USD | `+56.19%` | `115,806.00` |
| `Live` | `Short` | `1.98` | 15,370,000.00 USD | 651.75 USD | 0.00 USD | `+56.98%` | `330.00` |
| `Live` | `Short` | `2.00` | 17,760,000.00 USD | 2,390,000.00 USD | 0.00 USD | `+58.57%` | `1,196,475.00` |
| `Live` | `Short` | `2.00` | 18,160,000.00 USD | 401,870.00 USD | 0.00 USD | `+59.37%` | `200,434.00` |
| `Live` | `Short` | `2.02` | 18,160,000.00 USD | 799.96 USD | 0.00 USD | `+60.16%` | `397.00` |
| `Live` | `Short` | `2.02` | 18,160,000.00 USD | 178.20 USD | 0.00 USD | `+60.96%` | `88.00` |
| `Live` | `Short` | `2.04` | 18,160,000.00 USD | 198.36 USD | 0.00 USD | `+62.55%` | `97.00` |
| `Live` | `Short` | `2.06` | 18,160,000.00 USD | 170.56 USD | 0.00 USD | `+63.34%` | `83.00` |
| `Live` | `Short` | `2.06` | 18,160,000.00 USD | 460.50 USD | 0.00 USD | `+64.14%` | `223.00` |
| `Live` | `Short` | `2.10` | 18,160,000.00 USD | 708.11 USD | 0.00 USD | `+66.52%` | `338.00` |
| `Live` | `Short` | `2.10` | 18,240,000.00 USD | 81,120.00 USD | 0.00 USD | `+67.32%` | `38,537.00` |
| `Live` | `Short` | `2.12` | 18,490,000.00 USD | 251,210.00 USD | 0.00 USD | `+68.11%` | `118,776.00` |
| `Live` | `Short` | `2.15` | 18,490,000.00 USD | 196.11 USD | 0.00 USD | `+71.29%` | `91.00` |
| `Live` | `Short` | `2.17` | 18,540,000.00 USD | 49,710.00 USD | 0.00 USD | `+72.08%` | `22,960.00` |
| `Live` | `Short` | `2.17` | 18,630,000.00 USD | 82,770.00 USD | 0.00 USD | `+72.88%` | `38,056.00` |
| `Live` | `Short` | `2.19` | 18,630,000.00 USD | 2,110.00 USD | 0.00 USD | `+73.67%` | `965.00` |
| `Live` | `Short` | `2.21` | 18,630,000.00 USD | 438.80 USD | 0.00 USD | `+75.26%` | `199.00` |
| `Live` | `Short` | `2.23` | 18,640,000.00 USD | 11,670.00 USD | 0.00 USD | `+76.85%` | `5,244.00` |
| `Live` | `Short` | `2.27` | 18,680,000.00 USD | 43,950.00 USD | 0.00 USD | `+80.83%` | `19,317.00` |
| `Live` | `Short` | `2.29` | 18,690,000.00 USD | 2,060.00 USD | 0.00 USD | `+81.62%` | `900.00` |
| `Live` | `Short` | `2.29` | 18,690,000.00 USD | 105.57 USD | 0.00 USD | `+82.42%` | `46.00` |
| `Live` | `Short` | `2.31` | 18,690,000.00 USD | 248.94 USD | 0.00 USD | `+83.21%` | `108.00` |
| `Live` | `Short` | `2.31` | 18,690,000.00 USD | 106.49 USD | 0.00 USD | `+84.01%` | `46.00` |
| `Live` | `Short` | `2.33` | 18,690,000.00 USD | 1,310.00 USD | 0.00 USD | `+84.80%` | `562.00` |
| `Live` | `Short` | `2.33` | 18,690,000.00 USD | 1,550.00 USD | 0.00 USD | `+85.60%` | `665.00` |
| `Live` | `Short` | `2.35` | 18,700,000.00 USD | 14,540.00 USD | 0.00 USD | `+86.39%` | `6,201.00` |
| `Live` | `Short` | `2.35` | 18,710,000.00 USD | 4,140.00 USD | 0.00 USD | `+87.19%` | `1,760.00` |
| `Live` | `Short` | `2.38` | 22,300,000.00 USD | 3,590,000.00 USD | 0.00 USD | `+88.78%` | `1,512,779.00` |
| `Live` | `Short` | `2.38` | 22,300,000.00 USD | 477.00 USD | 0.00 USD | `+89.57%` | `200.00` |
| `Live` | `Short` | `2.40` | 23,770,000.00 USD | 1,470,000.00 USD | 0.00 USD | `+90.37%` | `613,646.00` |
| `Live` | `Short` | `2.40` | 23,770,000.00 USD | 610.87 USD | 0.00 USD | `+91.16%` | `254.00` |
| `Live` | `Short` | `2.42` | 23,850,000.00 USD | 81,630.00 USD | 0.00 USD | `+91.96%` | `33,802.00` |
| `Live` | `Short` | `2.42` | 24,220,000.00 USD | 364,240.00 USD | 0.00 USD | `+92.75%` | `150,200.00` |
| `Live` | `Short` | `2.44` | 24,240,000.00 USD | 24,510.00 USD | 0.00 USD | `+93.55%` | `10,065.00` |
| `Live` | `Short` | `2.44` | 24,250,000.00 USD | 3,580.00 USD | 0.00 USD | `+94.34%` | `1,463.00` |
| `Live` | `Short` | `2.46` | 24,260,000.00 USD | 19,100.00 USD | 0.00 USD | `+95.14%` | `7,780.00` |
| `Live` | `Short` | `2.48` | 24,270,000.00 USD | 306.90 USD | 0.00 USD | `+96.73%` | `124.00` |
| `Live` | `Short` | `2.48` | 24,270,000.00 USD | 144.13 USD | 0.00 USD | `+97.52%` | `58.00` |
| `Live` | `Short` | `2.50` | 24,360,000.00 USD | 95,910.00 USD | 0.00 USD | `+98.31%` | `38,440.00` |
| `Live` | `Short` | `2.52` | 24,370,000.00 USD | 5,630.00 USD | 0.00 USD | `+99.90%` | `2,240.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 3,720,000.00 USD | 0.00 USD | 102.00 USD | `-79.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3650` | 3,720,000.00 USD | 0.00 USD | 351.50 USD | `-70.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 3,720,000.00 USD | 0.00 USD | 139.12 USD | `-70.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3950` | 3,720,000.00 USD | 0.00 USD | 2,880.00 USD | `-68.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4050` | 3,720,000.00 USD | 0.00 USD | 2,950.00 USD | `-67.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 3,720,000.00 USD | 0.00 USD | 408.51 USD | `-64.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 3,720,000.00 USD | 0.00 USD | 273.00 USD | `-63.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 3,720,000.00 USD | 0.00 USD | 151.12 USD | `-63.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 3,720,000.00 USD | 0.00 USD | 142.50 USD | `-62.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 3,720,000.00 USD | 0.00 USD | 145.50 USD | `-61.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4950` | 3,720,000.00 USD | 0.00 USD | 562.81 USD | `-60.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 3,710,000.00 USD | 0.00 USD | 1,030.00 USD | `-59.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 3,710,000.00 USD | 0.00 USD | 285.82 USD | `-59.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 3,710,000.00 USD | 0.00 USD | 306.60 USD | `-58.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 3,710,000.00 USD | 0.00 USD | 121.55 USD | `-55.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 3,710,000.00 USD | 0.00 USD | 656.53 USD | `-55.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 3,710,000.00 USD | 0.00 USD | 100.62 USD | `-53.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 3,710,000.00 USD | 0.00 USD | 203.75 USD | `-50.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 3,710,000.00 USD | 0.00 USD | 791.85 USD | `-49.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 3,710,000.00 USD | 0.00 USD | 573.40 USD | `-48.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 3,710,000.00 USD | 0.00 USD | 244.31 USD | `-47.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 3,710,000.00 USD | 0.00 USD | 29,530.00 USD | `-47.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 3,680,000.00 USD | 0.00 USD | 503.55 USD | `-46.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 3,680,000.00 USD | 0.00 USD | 480.19 USD | `-45.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 3,680,000.00 USD | 0.00 USD | 11,870.00 USD | `-44.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 3,670,000.00 USD | 0.00 USD | 2,260.00 USD | `-43.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 3,670,000.00 USD | 0.00 USD | 228.80 USD | `-43.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 3,670,000.00 USD | 0.00 USD | 536.50 USD | `-42.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 3,670,000.00 USD | 0.00 USD | 1,300.00 USD | `-39.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 3,660,000.00 USD | 0.00 USD | 2,880.00 USD | `-39.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 3,660,000.00 USD | 0.00 USD | 25,490.00 USD | `-36.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 3,640,000.00 USD | 0.00 USD | 2,310,000.00 USD | `-34.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 1,330,000.00 USD | 0.00 USD | 1,260.00 USD | `-32.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 1,330,000.00 USD | 0.00 USD | 690.38 USD | `-30.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 1,320,000.00 USD | 0.00 USD | 1,400.00 USD | `-29.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 1,320,000.00 USD | 0.00 USD | 3,230.00 USD | `-28.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 1,320,000.00 USD | 0.00 USD | 838.94 USD | `-28.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 1,320,000.00 USD | 0.00 USD | 338.55 USD | `-27.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 1,320,000.00 USD | 0.00 USD | 1,060.00 USD | `-26.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 1,320,000.00 USD | 0.00 USD | 1,090.00 USD | `-25.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 1,320,000.00 USD | 0.00 USD | 112.46 USD | `-24.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 1,320,000.00 USD | 0.00 USD | 1,730.00 USD | `-24.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 1,310,000.00 USD | 0.00 USD | 4,010.00 USD | `-23.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 1,310,000.00 USD | 0.00 USD | 6,300.00 USD | `-22.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 1,300,000.00 USD | 0.00 USD | 8,260.00 USD | `-21.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 1,300,000.00 USD | 0.00 USD | 902.47 USD | `-20.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 1,300,000.00 USD | 0.00 USD | 45,660.00 USD | `-20.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 1,250,000.00 USD | 0.00 USD | 5,660.00 USD | `-19.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 1,240,000.00 USD | 0.00 USD | 1,840.00 USD | `-18.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 1,240,000.00 USD | 0.00 USD | 48,180.00 USD | `-17.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 1,190,000.00 USD | 0.00 USD | 1,780.00 USD | `-16.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 1,190,000.00 USD | 0.00 USD | 27,270.00 USD | `-16.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,160,000.00 USD | 0.00 USD | 3,960.00 USD | `-15.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,160,000.00 USD | 0.00 USD | 48,460.00 USD | `-14.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,110,000.00 USD | 0.00 USD | 3,360.00 USD | `-13.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,110,000.00 USD | 0.00 USD | 16,460.00 USD | `-12.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 1,090,000.00 USD | 0.00 USD | 12,830.00 USD | `-12.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 1,080,000.00 USD | 0.00 USD | 9,410.00 USD | `-11.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 1,070,000.00 USD | 0.00 USD | 77,260.00 USD | `-10.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 993,040.00 USD | 0.00 USD | 13,250.00 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 979,790.00 USD | 0.00 USD | 118,970.00 USD | `-8.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 860,810.00 USD | 0.00 USD | 58,820.00 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 802,000.00 USD | 0.00 USD | 17,890.00 USD | `-7.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 784,100.00 USD | 0.00 USD | 92,150.00 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 691,950.00 USD | 0.00 USD | 251,600.00 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 440,350.00 USD | 0.00 USD | 203,140.00 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 237,220.00 USD | 0.00 USD | 90,800.00 USD | `-4.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 146,420.00 USD | 0.00 USD | 23,230.00 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.23` | 123,190.00 USD | 0.00 USD | 36,670.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.24` | 86,520.00 USD | 0.00 USD | 51,090.00 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 35,430.00 USD | 0.00 USD | 27,910.00 USD | `-1.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.25` | 7,520.00 USD | 0.00 USD | 7,520.00 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 193,670.00 USD | 193,670.00 USD | 0.00 USD | `+0.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 284,380.00 USD | 90,710.00 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 585,840.00 USD | 301,460.00 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 666,880.00 USD | 81,040.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 686,700.00 USD | 19,820.00 USD | 0.00 USD | `+3.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 1,300,000.00 USD | 611,060.00 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,610,000.00 USD | 313,300.00 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,660,000.00 USD | 48,460.00 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 1,730,000.00 USD | 70,930.00 USD | 0.00 USD | `+6.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 1,750,000.00 USD | 14,640.00 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 1,790,000.00 USD | 47,040.00 USD | 0.00 USD | `+8.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 1,870,000.00 USD | 82,000.00 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 1,930,000.00 USD | 55,750.00 USD | 0.00 USD | `+10.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 1,940,000.00 USD | 5,430.00 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 6,340,000.00 USD | 4,400,000.00 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 6,340,000.00 USD | 2,390.00 USD | 0.00 USD | `+12.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 6,350,000.00 USD | 6,460.00 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,350,000.00 USD | 1,450.00 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 6,590,000.00 USD | 242,580.00 USD | 0.00 USD | `+14.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 6,600,000.00 USD | 7,510.00 USD | 0.00 USD | `+15.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 6,620,000.00 USD | 21,280.00 USD | 0.00 USD | `+16.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 6,730,000.00 USD | 108,020.00 USD | 0.00 USD | `+17.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 6,740,000.00 USD | 14,870.00 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,760,000.00 USD | 17,790.00 USD | 0.00 USD | `+18.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 6,830,000.00 USD | 70,600.00 USD | 0.00 USD | `+19.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 6,840,000.00 USD | 11,760.00 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 6,860,000.00 USD | 19,430.00 USD | 0.00 USD | `+21.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 6,910,000.00 USD | 45,620.00 USD | 0.00 USD | `+22.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 6,920,000.00 USD | 12,200.00 USD | 0.00 USD | `+22.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 6,920,000.00 USD | 2,380.00 USD | 0.00 USD | `+23.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 6,930,000.00 USD | 7,160.00 USD | 0.00 USD | `+24.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 6,940,000.00 USD | 5,570.00 USD | 0.00 USD | `+25.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 6,950,000.00 USD | 10,570.00 USD | 0.00 USD | `+25.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 7,090,000.00 USD | 139,120.00 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 7,090,000.00 USD | 1,840.00 USD | 0.00 USD | `+27.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 7,170,000.00 USD | 80,330.00 USD | 0.00 USD | `+28.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 7,170,000.00 USD | 464.75 USD | 0.00 USD | `+29.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,350,000.00 USD | 183,460.00 USD | 0.00 USD | `+29.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,350,000.00 USD | 2,670.00 USD | 0.00 USD | `+30.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,370,000.00 USD | 18,210.00 USD | 0.00 USD | `+31.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,380,000.00 USD | 6,080.00 USD | 0.00 USD | `+32.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,400,000.00 USD | 25,340.00 USD | 0.00 USD | `+33.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,480,000.00 USD | 70,850.00 USD | 0.00 USD | `+33.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,490,000.00 USD | 18,000.00 USD | 0.00 USD | `+34.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 7,740,000.00 USD | 251,050.00 USD | 0.00 USD | `+35.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 7,760,000.00 USD | 14,250.00 USD | 0.00 USD | `+36.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 7,760,000.00 USD | 534.75 USD | 0.00 USD | `+37.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 7,800,000.00 USD | 43,240.00 USD | 0.00 USD | `+37.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,810,000.00 USD | 3,330.00 USD | 0.00 USD | `+38.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 7,810,000.00 USD | 9,200.00 USD | 0.00 USD | `+39.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 7,840,000.00 USD | 21,720.00 USD | 0.00 USD | `+40.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 7,960,000.00 USD | 126,830.00 USD | 0.00 USD | `+41.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 8,060,000.00 USD | 96,600.00 USD | 0.00 USD | `+41.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 8,060,000.00 USD | 3,980.00 USD | 0.00 USD | `+42.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 8,060,000.00 USD | 254.51 USD | 0.00 USD | `+43.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 8,080,000.00 USD | 11,080.00 USD | 0.00 USD | `+44.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 8,080,000.00 USD | 3,970.00 USD | 0.00 USD | `+45.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 8,090,000.00 USD | 8,170.00 USD | 0.00 USD | `+45.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 8,090,000.00 USD | 843.17 USD | 0.00 USD | `+46.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 8,100,000.00 USD | 8,390.00 USD | 0.00 USD | `+47.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 8,100,000.00 USD | 4,420.00 USD | 0.00 USD | `+49.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 8,100,000.00 USD | 591.89 USD | 0.00 USD | `+49.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 8,150,000.00 USD | 46,370.00 USD | 0.00 USD | `+50.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 8,160,000.00 USD | 9,270.00 USD | 0.00 USD | `+51.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 8,160,000.00 USD | 265.10 USD | 0.00 USD | `+53.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 8,160,000.00 USD | 2,040.00 USD | 0.00 USD | `+54.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 8,160,000.00 USD | 807.42 USD | 0.00 USD | `+55.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,170,000.00 USD | 14,120.00 USD | 0.00 USD | `+56.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,180,000.00 USD | 4,010.00 USD | 0.00 USD | `+56.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,180,000.00 USD | 325.54 USD | 0.00 USD | `+57.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,190,000.00 USD | 7,020.00 USD | 0.00 USD | `+58.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,310,000.00 USD | 127,100.00 USD | 0.00 USD | `+59.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,320,000.00 USD | 3,350.00 USD | 0.00 USD | `+60.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,320,000.00 USD | 181.12 USD | 0.00 USD | `+61.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,320,000.00 USD | 382.41 USD | 0.00 USD | `+62.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,320,000.00 USD | 3,420.00 USD | 0.00 USD | `+64.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,320,000.00 USD | 661.93 USD | 0.00 USD | `+64.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,450,000.00 USD | 124,400.00 USD | 0.00 USD | `+66.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,450,000.00 USD | 1,580.00 USD | 0.00 USD | `+67.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 8,460,000.00 USD | 13,900.00 USD | 0.00 USD | `+68.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,490,000.00 USD | 24,840.00 USD | 0.00 USD | `+70.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 8,540,000.00 USD | 50,580.00 USD | 0.00 USD | `+71.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 8,540,000.00 USD | 2,690.00 USD | 0.00 USD | `+72.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 8,540,000.00 USD | 2,180.00 USD | 0.00 USD | `+74.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 8,690,000.00 USD | 151,380.00 USD | 0.00 USD | `+76.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 8,690,000.00 USD | 2,230.00 USD | 0.00 USD | `+80.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,700,000.00 USD | 1,140.00 USD | 0.00 USD | `+81.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 8,710,000.00 USD | 11,670.00 USD | 0.00 USD | `+82.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 8,710,000.00 USD | 370.40 USD | 0.00 USD | `+84.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 8,710,000.00 USD | 733.19 USD | 0.00 USD | `+85.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 8,710,000.00 USD | 2,410.00 USD | 0.00 USD | `+87.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,710,000.00 USD | 475.00 USD | 0.00 USD | `+88.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 8,710,000.00 USD | 1,190.00 USD | 0.00 USD | `+89.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,720,000.00 USD | 2,540.00 USD | 0.00 USD | `+90.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 8,720,000.00 USD | 1,590.00 USD | 0.00 USD | `+91.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,720,000.00 USD | 1,370.00 USD | 0.00 USD | `+91.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 8,740,000.00 USD | 19,590.00 USD | 0.00 USD | `+92.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 8,740,000.00 USD | 564.92 USD | 0.00 USD | `+93.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.48` | 8,740,000.00 USD | 3,420.00 USD | 0.00 USD | `+97.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,740,000.00 USD | 124.75 USD | 0.00 USD | `+98.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.50` | 8,770,000.00 USD | 29,920.00 USD | 0.00 USD | `+99.11%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `1.07` | 103,090,000.00 USD | 0.00 USD | 103,090,000.00 USD | 0.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `1.09` | 103,080,000.00 USD | 0.00 USD | 103,080,000.00 USD | 37,460.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `1.09` | 103,040,000.00 USD | 0.00 USD | 103,040,000.00 USD | 0.00 USD | 96,360.00 USD | 0.00 USD |
| `7D` | `1.09` | 102,940,000.00 USD | 0.00 USD | 102,940,000.00 USD | 0.00 USD | 6,470.00 USD | 32,940.00 USD |
| `7D` | `1.10` | 102,900,000.00 USD | 0.00 USD | 102,900,000.00 USD | 0.00 USD | 3,000.00 USD | 0.00 USD |
| `7D` | `1.10` | 102,900,000.00 USD | 0.00 USD | 102,900,000.00 USD | 0.00 USD | 0.00 USD | 287,290.00 USD |
| `7D` | `1.10` | 102,610,000.00 USD | 0.00 USD | 102,610,000.00 USD | 0.00 USD | 1,830.00 USD | 0.00 USD |
| `7D` | `1.11` | 102,610,000.00 USD | 0.00 USD | 102,610,000.00 USD | 0.00 USD | 4,520.00 USD | 0.00 USD |
| `7D` | `1.11` | 102,610,000.00 USD | 0.00 USD | 102,610,000.00 USD | 0.00 USD | 1,740.00 USD | 0.00 USD |
| `7D` | `1.11` | 102,610,000.00 USD | 0.00 USD | 102,610,000.00 USD | 50,260.00 USD | 4,710.00 USD | 0.00 USD |
| `7D` | `1.12` | 102,550,000.00 USD | 0.00 USD | 102,550,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `7D` | `1.12` | 102,540,000.00 USD | 0.00 USD | 102,540,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 101,690,000.00 USD | 0.00 USD | 101,690,000.00 USD | 19,780.00 USD | 70,020.00 USD | 236,090.00 USD |
| `1D` | `1.12` | 101,370,000.00 USD | 0.00 USD | 101,370,000.00 USD | 7,800.00 USD | 40,660.00 USD | 176,660.00 USD |
| `7D` | `1.12` | 102,460,000.00 USD | 0.00 USD | 102,460,000.00 USD | 17,190.00 USD | 3,530.00 USD | 108,090.00 USD |
| `1D` | `1.12` | 101,140,000.00 USD | 0.00 USD | 101,140,000.00 USD | 31,610.00 USD | 8,290.00 USD | 71,880.00 USD |
| `7D` | `1.12` | 102,330,000.00 USD | 0.00 USD | 102,330,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.13` | 101,030,000.00 USD | 0.00 USD | 101,030,000.00 USD | 126,800.00 USD | 79,730.00 USD | 249,770.00 USD |
| `7D` | `1.13` | 102,120,000.00 USD | 0.00 USD | 102,120,000.00 USD | 0.00 USD | 53,430.00 USD | 94,670.00 USD |
| `1D` | `1.13` | 100,570,000.00 USD | 0.00 USD | 100,570,000.00 USD | 77,710.00 USD | 59,850.00 USD | 210,640.00 USD |
| `7D` | `1.13` | 101,970,000.00 USD | 0.00 USD | 101,970,000.00 USD | 0.00 USD | 0.00 USD | 295,180.00 USD |
| `1D` | `1.13` | 100,230,000.00 USD | 0.00 USD | 100,230,000.00 USD | 29,530.00 USD | 126,490.00 USD | 405,270.00 USD |
| `7D` | `1.13` | 101,680,000.00 USD | 0.00 USD | 101,680,000.00 USD | 5,450.00 USD | 55,710.00 USD | 98,170.00 USD |
| `1D` | `1.13` | 99,670,000.00 USD | 0.00 USD | 99,670,000.00 USD | 5,520.00 USD | 78,550.00 USD | 312,810.00 USD |
| `7D` | `1.13` | 101,520,000.00 USD | 0.00 USD | 101,520,000.00 USD | 69,750.00 USD | 93,260.00 USD | 205,230.00 USD |
| `1D` | `1.13` | 99,270,000.00 USD | 0.00 USD | 99,270,000.00 USD | 91,470.00 USD | 89,100.00 USD | 115,470.00 USD |
| `7D` | `1.13` | 101,150,000.00 USD | 0.00 USD | 101,150,000.00 USD | 74,920.00 USD | 187,750.00 USD | 224,140.00 USD |
| `1D` | `1.14` | 98,970,000.00 USD | 0.00 USD | 98,970,000.00 USD | 42,870.00 USD | 153,340.00 USD | 163,320.00 USD |
| `7D` | `1.14` | 100,660,000.00 USD | 0.00 USD | 100,660,000.00 USD | 79,780.00 USD | 88,050.00 USD | 370,800.00 USD |
| `1D` | `1.14` | 98,610,000.00 USD | 0.00 USD | 98,610,000.00 USD | 38,180.00 USD | 18,330.00 USD | 49,660.00 USD |
| `7D` | `1.14` | 100,120,000.00 USD | 0.00 USD | 100,120,000.00 USD | 9,660.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 98,510,000.00 USD | 0.00 USD | 98,510,000.00 USD | 34,800.00 USD | 44,230.00 USD | 258,540.00 USD |
| `7D` | `1.14` | 100,090,000.00 USD | 0.00 USD | 100,090,000.00 USD | 39,170.00 USD | 54,580.00 USD | 250,970.00 USD |
| `1D` | `1.14` | 98,170,000.00 USD | 0.00 USD | 98,170,000.00 USD | 67,590.00 USD | 0.00 USD | 2,090.00 USD |
| `7D` | `1.14` | 99,750,000.00 USD | 0.00 USD | 99,750,000.00 USD | 126,430.00 USD | 1,340.00 USD | 11,130.00 USD |
| `1D` | `1.14` | 98,100,000.00 USD | 0.00 USD | 98,100,000.00 USD | 48,530.00 USD | 1,070.00 USD | 83,450.00 USD |
| `7D` | `1.14` | 99,610,000.00 USD | 0.00 USD | 99,610,000.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.15` | 99,600,000.00 USD | 0.00 USD | 99,600,000.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `1D` | `1.15` | 97,970,000.00 USD | 0.00 USD | 97,970,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 99,540,000.00 USD | 0.00 USD | 99,540,000.00 USD | 237,280.00 USD | 97,230.00 USD | 39,360.00 USD |
| `1D` | `1.15` | 97,950,000.00 USD | 0.00 USD | 97,950,000.00 USD | 0.00 USD | 75.47 USD | 0.00 USD |
| `7D` | `1.15` | 99,160,000.00 USD | 0.00 USD | 99,160,000.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `1D` | `1.15` | 97,950,000.00 USD | 0.00 USD | 97,950,000.00 USD | 1,390.00 USD | 149.67 USD | 64,030.00 USD |
| `7D` | `1.15` | 99,010,000.00 USD | 0.00 USD | 99,010,000.00 USD | 13,200.00 USD | 23,040.00 USD | 129,410.00 USD |
| `1D` | `1.15` | 97,880,000.00 USD | 0.00 USD | 97,880,000.00 USD | 73,200.00 USD | 45,610.00 USD | 263,680.00 USD |
| `7D` | `1.15` | 98,850,000.00 USD | 0.00 USD | 98,850,000.00 USD | 242,410.00 USD | 155,320.00 USD | 482,250.00 USD |
| `1D` | `1.16` | 97,500,000.00 USD | 0.00 USD | 97,500,000.00 USD | 20,480.00 USD | 23,120.00 USD | 82,910.00 USD |
| `7D` | `1.16` | 97,970,000.00 USD | 0.00 USD | 97,970,000.00 USD | 50,170.00 USD | 44,310.00 USD | 139,190.00 USD |
| `1D` | `1.16` | 97,380,000.00 USD | 0.00 USD | 97,380,000.00 USD | 108,420.00 USD | 20,680.00 USD | 371,290.00 USD |
| `7D` | `1.16` | 97,730,000.00 USD | 0.00 USD | 97,730,000.00 USD | 258,370.00 USD | 104,050.00 USD | 503,480.00 USD |
| `1D` | `1.16` | 96,880,000.00 USD | 0.00 USD | 96,880,000.00 USD | 149,150.00 USD | 46,560.00 USD | 127,480.00 USD |
| `7D` | `1.16` | 96,870,000.00 USD | 0.00 USD | 96,870,000.00 USD | 319,120.00 USD | 391,890.00 USD | 371,090.00 USD |
| `1D` | `1.16` | 96,550,000.00 USD | 0.00 USD | 96,550,000.00 USD | 134,780.00 USD | 232,220.00 USD | 78,330.00 USD |
| `7D` | `1.16` | 95,790,000.00 USD | 0.00 USD | 95,790,000.00 USD | 320,240.00 USD | 239,290.00 USD | 739,850.00 USD |
| `1D` | `1.16` | 96,110,000.00 USD | 0.00 USD | 96,110,000.00 USD | 85,830.00 USD | 48,800.00 USD | 626,390.00 USD |
| `7D` | `1.16` | 94,490,000.00 USD | 0.00 USD | 94,490,000.00 USD | 510,570.00 USD | 127,800.00 USD | 1,030,000.00 USD |
| `1D` | `1.17` | 95,350,000.00 USD | 0.00 USD | 95,350,000.00 USD | 45,160.00 USD | 3,210.00 USD | 106,000.00 USD |
| `7D` | `1.17` | 92,820,000.00 USD | 0.00 USD | 92,820,000.00 USD | 218,150.00 USD | 329,380.00 USD | 797,710.00 USD |
| `1D` | `1.17` | 95,190,000.00 USD | 0.00 USD | 95,190,000.00 USD | 104,050.00 USD | 170,360.00 USD | 170,840.00 USD |
| `7D` | `1.17` | 91,480,000.00 USD | 0.00 USD | 91,480,000.00 USD | 346,160.00 USD | 154,130.00 USD | 569,320.00 USD |
| `1D` | `1.17` | 94,750,000.00 USD | 0.00 USD | 94,750,000.00 USD | 152,210.00 USD | 24,880.00 USD | 358,690.00 USD |
| `7D` | `1.17` | 90,410,000.00 USD | 0.00 USD | 90,410,000.00 USD | 511,610.00 USD | 301,290.00 USD | 1,220,000.00 USD |
| `1D` | `1.17` | 94,210,000.00 USD | 0.00 USD | 94,210,000.00 USD | 371,850.00 USD | 783.46 USD | 266,890.00 USD |
| `7D` | `1.17` | 88,370,000.00 USD | 0.00 USD | 88,370,000.00 USD | 335,720.00 USD | 94,140.00 USD | 772,040.00 USD |
| `1D` | `1.17` | 93,570,000.00 USD | 0.00 USD | 93,570,000.00 USD | 124,360.00 USD | 133,540.00 USD | 474,190.00 USD |
| `7D` | `1.17` | 87,170,000.00 USD | 0.00 USD | 87,170,000.00 USD | 605,040.00 USD | 127,910.00 USD | 835,540.00 USD |
| `1D` | `1.18` | 92,840,000.00 USD | 0.00 USD | 92,840,000.00 USD | 304,390.00 USD | 85,620.00 USD | 356,950.00 USD |
| `7D` | `1.18` | 85,600,000.00 USD | 0.00 USD | 85,600,000.00 USD | 181,850.00 USD | 71,240.00 USD | 311,840.00 USD |
| `1D` | `1.18` | 92,090,000.00 USD | 0.00 USD | 92,090,000.00 USD | 71,040.00 USD | 84,510.00 USD | 175,590.00 USD |
| `7D` | `1.18` | 85,040,000.00 USD | 0.00 USD | 85,040,000.00 USD | 85,020.00 USD | 26,480.00 USD | 380,570.00 USD |
| `1D` | `1.18` | 91,760,000.00 USD | 0.00 USD | 91,760,000.00 USD | 113,290.00 USD | 4,120.00 USD | 24,100.00 USD |
| `7D` | `1.18` | 84,540,000.00 USD | 0.00 USD | 84,540,000.00 USD | 267,580.00 USD | 78,500.00 USD | 194,450.00 USD |
| `1D` | `1.18` | 91,620,000.00 USD | 0.00 USD | 91,620,000.00 USD | 222,930.00 USD | 9,740.00 USD | 666,440.00 USD |
| `7D` | `1.18` | 84,000,000.00 USD | 0.00 USD | 84,000,000.00 USD | 78,320.00 USD | 72,360.00 USD | 116,120.00 USD |
| `1D` | `1.18` | 90,720,000.00 USD | 0.00 USD | 90,720,000.00 USD | 196,910.00 USD | 88,190.00 USD | 143,880.00 USD |
| `7D` | `1.18` | 83,740,000.00 USD | 0.00 USD | 83,740,000.00 USD | 297,510.00 USD | 570,360.00 USD | 235,490.00 USD |
| `1D` | `1.19` | 90,290,000.00 USD | 0.00 USD | 90,290,000.00 USD | 86,540.00 USD | 501,490.00 USD | 65,030.00 USD |
| `7D` | `1.19` | 82,630,000.00 USD | 0.00 USD | 82,630,000.00 USD | 76,370.00 USD | 69,240.00 USD | 706,450.00 USD |
| `1D` | `1.19` | 89,640,000.00 USD | 0.00 USD | 89,640,000.00 USD | 365,260.00 USD | 94,780.00 USD | 1,570,000.00 USD |
| `7D` | `1.19` | 81,780,000.00 USD | 0.00 USD | 81,780,000.00 USD | 216,820.00 USD | 93,330.00 USD | 477,730.00 USD |
| `1D` | `1.19` | 87,610,000.00 USD | 0.00 USD | 87,610,000.00 USD | 110,600.00 USD | 41,860.00 USD | 319,610.00 USD |
| `7D` | `1.19` | 80,990,000.00 USD | 0.00 USD | 80,990,000.00 USD | 179,980.00 USD | 69,020.00 USD | 728,280.00 USD |
| `1D` | `1.19` | 87,140,000.00 USD | 0.00 USD | 87,140,000.00 USD | 147,820.00 USD | 204,560.00 USD | 470,630.00 USD |
| `7D` | `1.19` | 80,020,000.00 USD | 0.00 USD | 80,020,000.00 USD | 72,430.00 USD | 531,420.00 USD | 757,460.00 USD |
| `1D` | `1.19` | 86,320,000.00 USD | 0.00 USD | 86,320,000.00 USD | 195,220.00 USD | 436,550.00 USD | 1,900,000.00 USD |
| `7D` | `1.19` | 78,650,000.00 USD | 0.00 USD | 78,650,000.00 USD | 229,630.00 USD | 59,450.00 USD | 558,970.00 USD |
| `1D` | `1.20` | 83,780,000.00 USD | 0.00 USD | 83,780,000.00 USD | 787,460.00 USD | 119,400.00 USD | 1,430,000.00 USD |
| `7D` | `1.20` | 77,810,000.00 USD | 0.00 USD | 77,810,000.00 USD | 261,330.00 USD | 1,050,000.00 USD | 707,370.00 USD |
| `1D` | `1.20` | 81,440,000.00 USD | 0.00 USD | 81,440,000.00 USD | 344,480.00 USD | 837,030.00 USD | 761,200.00 USD |
| `7D` | `1.20` | 75,790,000.00 USD | 0.00 USD | 75,790,000.00 USD | 31,150.00 USD | 373,690.00 USD | 2,610,000.00 USD |
| `1D` | `1.20` | 79,500,000.00 USD | 0.00 USD | 79,500,000.00 USD | 944,770.00 USD | 537,300.00 USD | 2,610,000.00 USD |
| `7D` | `1.20` | 72,780,000.00 USD | 0.00 USD | 72,780,000.00 USD | 800,760.00 USD | 466,100.00 USD | 255,270.00 USD |
| `1D` | `1.20` | 75,410,000.00 USD | 0.00 USD | 75,410,000.00 USD | 221,270.00 USD | 284,650.00 USD | 1,200,000.00 USD |
| `7D` | `1.20` | 71,250,000.00 USD | 0.00 USD | 71,250,000.00 USD | 337,020.00 USD | 144,630.00 USD | 622,930.00 USD |
| `1D` | `1.20` | 73,710,000.00 USD | 0.00 USD | 73,710,000.00 USD | 641,370.00 USD | 589,780.00 USD | 557,480.00 USD |
| `7D` | `1.20` | 70,150,000.00 USD | 0.00 USD | 70,150,000.00 USD | 47,500.00 USD | 723,100.00 USD | 407,740.00 USD |
| `1D` | `1.21` | 71,920,000.00 USD | 0.00 USD | 71,920,000.00 USD | 466,520.00 USD | 581,610.00 USD | 999,510.00 USD |
| `7D` | `1.21` | 68,970,000.00 USD | 0.00 USD | 68,970,000.00 USD | 0.00 USD | 124,960.00 USD | 245,420.00 USD |
| `1D` | `1.21` | 69,870,000.00 USD | 0.00 USD | 69,870,000.00 USD | 1,740,000.00 USD | 376,210.00 USD | 2,080,000.00 USD |
| `7D` | `1.21` | 68,600,000.00 USD | 0.00 USD | 68,600,000.00 USD | 564,460.00 USD | 0.00 USD | 635,770.00 USD |
| `1D` | `1.21` | 65,670,000.00 USD | 0.00 USD | 65,670,000.00 USD | 686,600.00 USD | 485,620.00 USD | 1,320,000.00 USD |
| `7D` | `1.21` | 67,400,000.00 USD | 0.00 USD | 67,400,000.00 USD | 257,960.00 USD | 719,110.00 USD | 3,230,000.00 USD |
| `1D` | `1.21` | 63,190,000.00 USD | 0.00 USD | 63,190,000.00 USD | 1,520,000.00 USD | 658,010.00 USD | 1,560,000.00 USD |
| `7D` | `1.21` | 63,200,000.00 USD | 0.00 USD | 63,200,000.00 USD | 1,350,000.00 USD | 0.00 USD | 899,930.00 USD |
| `1D` | `1.21` | 59,450,000.00 USD | 0.00 USD | 59,450,000.00 USD | 30,610.00 USD | 180,030.00 USD | 1,100,000.00 USD |
| `7D` | `1.21` | 60,940,000.00 USD | 0.00 USD | 60,940,000.00 USD | 108,640.00 USD | 136,460.00 USD | 1,280,000.00 USD |
| `1D` | `1.22` | 58,150,000.00 USD | 0.00 USD | 58,150,000.00 USD | 226,520.00 USD | 196,610.00 USD | 1,170,000.00 USD |
| `7D` | `1.22` | 59,410,000.00 USD | 0.00 USD | 59,410,000.00 USD | 142,210.00 USD | 9,150.00 USD | 253,540.00 USD |
| `1D` | `1.22` | 56,560,000.00 USD | 0.00 USD | 56,560,000.00 USD | 152,400.00 USD | 6,620.00 USD | 246,050.00 USD |
| `7D` | `1.22` | 59,010,000.00 USD | 0.00 USD | 59,010,000.00 USD | 316,090.00 USD | 0.00 USD | 419,340.00 USD |
| `1D` | `1.22` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 228,030.00 USD | 95,330.00 USD | 422,060.00 USD |
| `7D` | `1.22` | 58,270,000.00 USD | 0.00 USD | 58,270,000.00 USD | 156,790.00 USD | 928,300.00 USD | 569,650.00 USD |
| `1D` | `1.22` | 55,400,000.00 USD | 0.00 USD | 55,400,000.00 USD | 122,290.00 USD | 275,000.00 USD | 881,110.00 USD |
| `7D` | `1.22` | 56,620,000.00 USD | 0.00 USD | 56,620,000.00 USD | 0.00 USD | 167,460.00 USD | 340,920.00 USD |
| `1D` | `1.22` | 54,130,000.00 USD | 0.00 USD | 54,130,000.00 USD | 504,680.00 USD | 82,730.00 USD | 2,890,000.00 USD |
| `7D` | `1.22` | 56,110,000.00 USD | 0.00 USD | 56,110,000.00 USD | 180,560.00 USD | 170,590.00 USD | 33,260.00 USD |
| `1D` | `1.23` | 50,650,000.00 USD | 0.00 USD | 50,650,000.00 USD | 609,560.00 USD | 833,330.00 USD | 1,220,000.00 USD |
| `7D` | `1.23` | 55,730,000.00 USD | 0.00 USD | 55,730,000.00 USD | 258,810.00 USD | 802,580.00 USD | 790,120.00 USD |
| `1D` | `1.23` | 47,990,000.00 USD | 0.00 USD | 47,990,000.00 USD | 599,790.00 USD | 813,980.00 USD | 800,610.00 USD |
| `7D` | `1.23` | 53,870,000.00 USD | 0.00 USD | 53,870,000.00 USD | 59,160.00 USD | 950,550.00 USD | 538,800.00 USD |
| `1D` | `1.23` | 45,770,000.00 USD | 0.00 USD | 45,770,000.00 USD | 485,440.00 USD | 1,130,000.00 USD | 3,850,000.00 USD |
| `7D` | `1.23` | 52,330,000.00 USD | 0.00 USD | 52,330,000.00 USD | 198,530.00 USD | 1,150,000.00 USD | 1,600,000.00 USD |
| `1D` | `1.23` | 40,300,000.00 USD | 0.00 USD | 40,300,000.00 USD | 1,370,000.00 USD | 1,380,000.00 USD | 5,450,000.00 USD |
| `7D` | `1.23` | 49,370,000.00 USD | 0.00 USD | 49,370,000.00 USD | 1,040,000.00 USD | 1,170,000.00 USD | 1,600,000.00 USD |
| `1D` | `1.23` | 32,100,000.00 USD | 0.00 USD | 32,100,000.00 USD | 640,340.00 USD | 1,350,000.00 USD | 2,800,000.00 USD |
| `7D` | `1.23` | 45,570,000.00 USD | 0.00 USD | 45,570,000.00 USD | 1,660,000.00 USD | 1,990,000.00 USD | 6,100,000.00 USD |
| `1D` | `1.24` | 27,310,000.00 USD | 0.00 USD | 27,310,000.00 USD | 577,460.00 USD | 1,140,000.00 USD | 1,920,000.00 USD |
| `7D` | `1.24` | 35,810,000.00 USD | 0.00 USD | 35,810,000.00 USD | 2,040,000.00 USD | 2,080,000.00 USD | 3,030,000.00 USD |
| `1D` | `1.24` | 23,660,000.00 USD | 0.00 USD | 23,660,000.00 USD | 1,350,000.00 USD | 915,810.00 USD | 2,610,000.00 USD |
| `7D` | `1.24` | 28,660,000.00 USD | 0.00 USD | 28,660,000.00 USD | 3,420,000.00 USD | 2,120,000.00 USD | 5,050,000.00 USD |
| `1D` | `1.24` | 18,780,000.00 USD | 0.00 USD | 18,780,000.00 USD | 847,110.00 USD | 824,940.00 USD | 2,740,000.00 USD |
| `7D` | `1.24` | 18,080,000.00 USD | 0.00 USD | 18,080,000.00 USD | 2,070,000.00 USD | 1,220,000.00 USD | 2,290,000.00 USD |
| `1D` | `1.24` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 851,040.00 USD | 1,300,000.00 USD | 2,420,000.00 USD |
| `7D` | `1.24` | 12,490,000.00 USD | 0.00 USD | 12,490,000.00 USD | 1,130,000.00 USD | 510,590.00 USD | 2,060,000.00 USD |
| `1D` | `1.24` | 9,800,000.00 USD | 0.00 USD | 9,800,000.00 USD | 1,950,000.00 USD | 526,050.00 USD | 3,310,000.00 USD |
| `7D` | `1.24` | 8,780,000.00 USD | 0.00 USD | 8,780,000.00 USD | 1,420,000.00 USD | 424,430.00 USD | 0.00 USD |
| `1D` | `1.25` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 1,410,000.00 USD | 706,700.00 USD | 525,240.00 USD |
| `7D` | `1.25` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 3,770,000.00 USD | 688,040.00 USD | 0.00 USD |
| `1D` | `1.25` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD |
| `7D` | `1.25` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 1,630,000.00 USD | 857,970.00 USD | 0.00 USD |
| `1D` | `1.25` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.26` | 158,820.00 USD | 158,820.00 USD | 0.00 USD | 150,010.00 USD | 8,810.00 USD | 0.00 USD |
| `1D` | `1.26` | 856,480.00 USD | 856,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 856,480.00 USD |
| `7D` | `1.26` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 19,840.00 USD | 1,740,000.00 USD |
| `1D` | `1.26` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 253,360.00 USD | 0.00 USD | 379,020.00 USD |
| `7D` | `1.26` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 10,110.00 USD | 0.00 USD |
| `1D` | `1.26` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 228,810.00 USD | 253,090.00 USD | 167,810.00 USD |
| `7D` | `1.26` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 402,060.00 USD | 3,390.00 USD | 0.00 USD |
| `1D` | `1.26` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 664,010.00 USD | 508,070.00 USD | 1,970,000.00 USD |
| `7D` | `1.26` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 292,090.00 USD | 542,940.00 USD | 1,640,000.00 USD |
| `1D` | `1.27` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 1,210,000.00 USD | 457,890.00 USD | 784,820.00 USD |
| `7D` | `1.27` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 4,260,000.00 USD | 9,150.00 USD | 1,030,000.00 USD |
| `1D` | `1.27` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 790,310.00 USD | 1,540,000.00 USD | 1,410,000.00 USD |
| `7D` | `1.27` | 16,060,000.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 1,870,000.00 USD | 4,090,000.00 USD |
| `1D` | `1.27` | 19,940,000.00 USD | 19,940,000.00 USD | 0.00 USD | 1,240,000.00 USD | 1,390,000.00 USD | 5,830,000.00 USD |
| `7D` | `1.27` | 21,620,000.00 USD | 21,620,000.00 USD | 0.00 USD | 156,790.00 USD | 2,950,000.00 USD | 2,450,000.00 USD |
| `1D` | `1.27` | 24,780,000.00 USD | 24,780,000.00 USD | 0.00 USD | 1,620,000.00 USD | 1,300,000.00 USD | 1,920,000.00 USD |
| `7D` | `1.27` | 31,350,000.00 USD | 31,350,000.00 USD | 0.00 USD | 1,680,000.00 USD | 5,310,000.00 USD | 2,750,000.00 USD |
| `1D` | `1.27` | 33,150,000.00 USD | 33,150,000.00 USD | 0.00 USD | 1,380,000.00 USD | 2,380,000.00 USD | 4,620,000.00 USD |
| `7D` | `1.27` | 48,830,000.00 USD | 48,830,000.00 USD | 0.00 USD | 2,840,000.00 USD | 3,400,000.00 USD | 11,230,000.00 USD |
| `1D` | `1.28` | 40,740,000.00 USD | 40,740,000.00 USD | 0.00 USD | 1,690,000.00 USD | 1,960,000.00 USD | 3,940,000.00 USD |
| `7D` | `1.28` | 64,150,000.00 USD | 64,150,000.00 USD | 0.00 USD | 5,290,000.00 USD | 3,080,000.00 USD | 6,950,000.00 USD |
| `1D` | `1.28` | 49,330,000.00 USD | 49,330,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,370,000.00 USD | 3,970,000.00 USD |
| `7D` | `1.28` | 83,820,000.00 USD | 83,820,000.00 USD | 0.00 USD | 7,780,000.00 USD | 3,760,000.00 USD | 8,130,000.00 USD |
| `1D` | `1.28` | 55,120,000.00 USD | 55,120,000.00 USD | 0.00 USD | 551,850.00 USD | 1,860,000.00 USD | 3,370,000.00 USD |
| `7D` | `1.28` | 87,410,000.00 USD | 87,410,000.00 USD | 0.00 USD | 0.00 USD | 1,700,000.00 USD | 1,890,000.00 USD |
| `1D` | `1.28` | 59,710,000.00 USD | 59,710,000.00 USD | 0.00 USD | 1,030,000.00 USD | 367,140.00 USD | 3,190,000.00 USD |
| `7D` | `1.28` | 89,550,000.00 USD | 89,550,000.00 USD | 0.00 USD | 1,040,000.00 USD | 234,920.00 USD | 861,600.00 USD |
| `1D` | `1.28` | 62,930,000.00 USD | 62,930,000.00 USD | 0.00 USD | 1,290,000.00 USD | 629,480.00 USD | 1,310,000.00 USD |
| `7D` | `1.28` | 93,800,000.00 USD | 93,800,000.00 USD | 0.00 USD | 1,100,000.00 USD | 1,300,000.00 USD | 1,850,000.00 USD |
| `1D` | `1.29` | 67,240,000.00 USD | 67,240,000.00 USD | 0.00 USD | 818,130.00 USD | 1,150,000.00 USD | 2,340,000.00 USD |
| `7D` | `1.29` | 98,930,000.00 USD | 98,930,000.00 USD | 0.00 USD | 796,960.00 USD | 1,560,000.00 USD | 2,760,000.00 USD |
| `1D` | `1.29` | 69,080,000.00 USD | 69,080,000.00 USD | 0.00 USD | 787,490.00 USD | 457,810.00 USD | 591,760.00 USD |
| `7D` | `1.29` | 99,650,000.00 USD | 99,650,000.00 USD | 0.00 USD | 685,300.00 USD | 2,730.00 USD | 33,260.00 USD |
| `1D` | `1.29` | 69,900,000.00 USD | 69,900,000.00 USD | 0.00 USD | 156,280.00 USD | 213,200.00 USD | 456,570.00 USD |
| `7D` | `1.29` | 101,250,000.00 USD | 101,250,000.00 USD | 0.00 USD | 70,460.00 USD | 277,240.00 USD | 1,260,000.00 USD |
| `1D` | `1.29` | 73,240,000.00 USD | 73,240,000.00 USD | 0.00 USD | 378,690.00 USD | 236,330.00 USD | 2,720,000.00 USD |
| `7D` | `1.29` | 103,850,000.00 USD | 103,850,000.00 USD | 0.00 USD | 1,040,000.00 USD | 202,640.00 USD | 1,350,000.00 USD |
| `1D` | `1.29` | 77,710,000.00 USD | 77,710,000.00 USD | 0.00 USD | 1,170,000.00 USD | 374,490.00 USD | 2,930,000.00 USD |
| `7D` | `1.29` | 107,510,000.00 USD | 107,510,000.00 USD | 0.00 USD | 1,780,000.00 USD | 8,810.00 USD | 1,880,000.00 USD |
| `1D` | `1.30` | 83,210,000.00 USD | 83,210,000.00 USD | 0.00 USD | 1,470,000.00 USD | 1,240,000.00 USD | 2,790,000.00 USD |
| `7D` | `1.30` | 115,230,000.00 USD | 115,230,000.00 USD | 0.00 USD | 1,980,000.00 USD | 1,570,000.00 USD | 4,170,000.00 USD |
| `1D` | `1.30` | 84,530,000.00 USD | 84,530,000.00 USD | 0.00 USD | 544,620.00 USD | 21,940.00 USD | 751,320.00 USD |
| `7D` | `1.30` | 117,180,000.00 USD | 117,180,000.00 USD | 0.00 USD | 25,800.00 USD | 173,700.00 USD | 1,750,000.00 USD |
| `1D` | `1.30` | 86,490,000.00 USD | 86,490,000.00 USD | 0.00 USD | 439,090.00 USD | 461,990.00 USD | 1,060,000.00 USD |
| `7D` | `1.30` | 119,620,000.00 USD | 119,620,000.00 USD | 0.00 USD | 272,980.00 USD | 434,510.00 USD | 1,730,000.00 USD |
| `1D` | `1.30` | 89,340,000.00 USD | 89,340,000.00 USD | 0.00 USD | 810,010.00 USD | 640,150.00 USD | 1,400,000.00 USD |
| `7D` | `1.30` | 120,880,000.00 USD | 120,880,000.00 USD | 0.00 USD | 158,990.00 USD | 944,610.00 USD | 158,700.00 USD |
| `1D` | `1.30` | 90,820,000.00 USD | 90,820,000.00 USD | 0.00 USD | 481,740.00 USD | 328,660.00 USD | 666,360.00 USD |
| `7D` | `1.30` | 123,940,000.00 USD | 123,940,000.00 USD | 0.00 USD | 0.00 USD | 2,170,000.00 USD | 887,870.00 USD |
| `1D` | `1.31` | 93,090,000.00 USD | 93,090,000.00 USD | 0.00 USD | 631,950.00 USD | 559,170.00 USD | 1,080,000.00 USD |
| `7D` | `1.31` | 126,240,000.00 USD | 126,240,000.00 USD | 0.00 USD | 1,770,000.00 USD | 286,020.00 USD | 245,420.00 USD |
| `1D` | `1.31` | 96,950,000.00 USD | 96,950,000.00 USD | 0.00 USD | 977,640.00 USD | 522,010.00 USD | 2,360,000.00 USD |
| `7D` | `1.31` | 131,670,000.00 USD | 131,670,000.00 USD | 0.00 USD | 1,560,000.00 USD | 821,310.00 USD | 3,040,000.00 USD |
| `1D` | `1.31` | 100,350,000.00 USD | 100,350,000.00 USD | 0.00 USD | 1,310,000.00 USD | 359,190.00 USD | 1,730,000.00 USD |
| `7D` | `1.31` | 134,440,000.00 USD | 134,440,000.00 USD | 0.00 USD | 1,340,000.00 USD | 635,040.00 USD | 789,810.00 USD |
| `1D` | `1.31` | 103,050,000.00 USD | 103,050,000.00 USD | 0.00 USD | 919,330.00 USD | 635,660.00 USD | 1,150,000.00 USD |
| `7D` | `1.31` | 139,310,000.00 USD | 139,310,000.00 USD | 0.00 USD | 189,510.00 USD | 858,660.00 USD | 3,830,000.00 USD |
| `1D` | `1.31` | 104,610,000.00 USD | 104,610,000.00 USD | 0.00 USD | 503,300.00 USD | 157,920.00 USD | 891,380.00 USD |
| `7D` | `1.31` | 140,600,000.00 USD | 140,600,000.00 USD | 0.00 USD | 638,380.00 USD | 151,320.00 USD | 501,780.00 USD |
| `1D` | `1.32` | 107,430,000.00 USD | 107,430,000.00 USD | 0.00 USD | 174,570.00 USD | 546,170.00 USD | 2,100,000.00 USD |
| `7D` | `1.32` | 145,320,000.00 USD | 145,320,000.00 USD | 0.00 USD | 68,520.00 USD | 1,890,000.00 USD | 2,760,000.00 USD |
| `1D` | `1.32` | 113,040,000.00 USD | 113,040,000.00 USD | 0.00 USD | 1,730,000.00 USD | 623,240.00 USD | 3,260,000.00 USD |
| `7D` | `1.32` | 150,420,000.00 USD | 150,420,000.00 USD | 0.00 USD | 1,560,000.00 USD | 457,220.00 USD | 3,080,000.00 USD |
| `1D` | `1.32` | 115,210,000.00 USD | 115,210,000.00 USD | 0.00 USD | 1,200,000.00 USD | 197,040.00 USD | 769,650.00 USD |
| `7D` | `1.32` | 152,440,000.00 USD | 152,440,000.00 USD | 0.00 USD | 1,140,000.00 USD | 433,750.00 USD | 450,000.00 USD |
| `1D` | `1.32` | 117,960,000.00 USD | 117,960,000.00 USD | 0.00 USD | 1,030,000.00 USD | 608,700.00 USD | 1,120,000.00 USD |
| `7D` | `1.32` | 155,800,000.00 USD | 155,800,000.00 USD | 0.00 USD | 1,200,000.00 USD | 855,190.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 119,740,000.00 USD | 119,740,000.00 USD | 0.00 USD | 867,870.00 USD | 61,350.00 USD | 851,430.00 USD |
| `7D` | `1.32` | 158,570,000.00 USD | 158,570,000.00 USD | 0.00 USD | 2,030,000.00 USD | 197,050.00 USD | 551,150.00 USD |
| `1D` | `1.33` | 120,780,000.00 USD | 120,780,000.00 USD | 0.00 USD | 405,790.00 USD | 54,470.00 USD | 578,770.00 USD |
| `7D` | `1.33` | 160,380,000.00 USD | 160,380,000.00 USD | 0.00 USD | 1,290,000.00 USD | 129,500.00 USD | 390,200.00 USD |
| `1D` | `1.33` | 122,000,000.00 USD | 122,000,000.00 USD | 0.00 USD | 545,530.00 USD | 175,480.00 USD | 494,230.00 USD |
| `7D` | `1.33` | 161,480,000.00 USD | 161,480,000.00 USD | 0.00 USD | 172,880.00 USD | 22,770.00 USD | 903,000.00 USD |
| `1D` | `1.33` | 123,690,000.00 USD | 123,690,000.00 USD | 0.00 USD | 729,070.00 USD | 104,910.00 USD | 862,480.00 USD |
| `7D` | `1.33` | 163,190,000.00 USD | 163,190,000.00 USD | 0.00 USD | 548,610.00 USD | 234,930.00 USD | 930,350.00 USD |
| `1D` | `1.33` | 125,520,000.00 USD | 125,520,000.00 USD | 0.00 USD | 465,720.00 USD | 180,450.00 USD | 1,180,000.00 USD |
| `7D` | `1.33` | 165,660,000.00 USD | 165,660,000.00 USD | 0.00 USD | 829,540.00 USD | 243,350.00 USD | 1,390,000.00 USD |
| `1D` | `1.33` | 127,370,000.00 USD | 127,370,000.00 USD | 0.00 USD | 783,210.00 USD | 227,790.00 USD | 838,970.00 USD |
| `7D` | `1.33` | 167,690,000.00 USD | 167,690,000.00 USD | 0.00 USD | 688,720.00 USD | 297,580.00 USD | 1,040,000.00 USD |
| `1D` | `1.34` | 128,480,000.00 USD | 128,480,000.00 USD | 0.00 USD | 286,040.00 USD | 207,050.00 USD | 616,400.00 USD |
| `7D` | `1.34` | 169,230,000.00 USD | 169,230,000.00 USD | 0.00 USD | 652,270.00 USD | 347,210.00 USD | 543,190.00 USD |
| `1D` | `1.34` | 128,940,000.00 USD | 128,940,000.00 USD | 0.00 USD | 240,600.00 USD | 80,780.00 USD | 141,600.00 USD |
| `7D` | `1.34` | 171,670,000.00 USD | 171,670,000.00 USD | 0.00 USD | 1,190,000.00 USD | 742,990.00 USD | 503,900.00 USD |
| `1D` | `1.34` | 129,730,000.00 USD | 129,730,000.00 USD | 0.00 USD | 331,150.00 USD | 119,540.00 USD | 335,780.00 USD |
| `7D` | `1.34` | 173,530,000.00 USD | 173,530,000.00 USD | 0.00 USD | 804,660.00 USD | 463,950.00 USD | 588,220.00 USD |
| `1D` | `1.34` | 130,850,000.00 USD | 130,850,000.00 USD | 0.00 USD | 616,160.00 USD | 165,460.00 USD | 342,620.00 USD |
| `7D` | `1.34` | 178,990,000.00 USD | 178,990,000.00 USD | 0.00 USD | 2,380,000.00 USD | 2,430,000.00 USD | 660,660.00 USD |
| `1D` | `1.34` | 131,830,000.00 USD | 131,830,000.00 USD | 0.00 USD | 365,760.00 USD | 246,750.00 USD | 369,190.00 USD |
| `7D` | `1.34` | 186,110,000.00 USD | 186,110,000.00 USD | 0.00 USD | 2,000,000.00 USD | 1,890,000.00 USD | 3,240,000.00 USD |
| `1D` | `1.35` | 132,360,000.00 USD | 132,360,000.00 USD | 0.00 USD | 189,800.00 USD | 64,310.00 USD | 274,740.00 USD |
| `7D` | `1.35` | 194,370,000.00 USD | 194,370,000.00 USD | 0.00 USD | 3,270,000.00 USD | 1,640,000.00 USD | 3,350,000.00 USD |
| `1D` | `1.35` | 132,760,000.00 USD | 132,760,000.00 USD | 0.00 USD | 123,430.00 USD | 3,590.00 USD | 270,210.00 USD |
| `7D` | `1.35` | 202,120,000.00 USD | 202,120,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,820,000.00 USD | 3,160,000.00 USD |
| `1D` | `1.35` | 133,110,000.00 USD | 133,110,000.00 USD | 0.00 USD | 177,170.00 USD | 30,570.00 USD | 146,530.00 USD |
| `7D` | `1.35` | 210,140,000.00 USD | 210,140,000.00 USD | 0.00 USD | 3,770,000.00 USD | 1,590,000.00 USD | 2,660,000.00 USD |
| `1D` | `1.35` | 133,390,000.00 USD | 133,390,000.00 USD | 0.00 USD | 69,740.00 USD | 26,920.00 USD | 174,610.00 USD |
| `7D` | `1.35` | 219,260,000.00 USD | 219,260,000.00 USD | 0.00 USD | 3,040,000.00 USD | 1,260,000.00 USD | 4,820,000.00 USD |
| `1D` | `1.35` | 133,690,000.00 USD | 133,690,000.00 USD | 0.00 USD | 105,080.00 USD | 4,310.00 USD | 194,110.00 USD |
| `7D` | `1.35` | 226,010,000.00 USD | 226,010,000.00 USD | 0.00 USD | 2,180,000.00 USD | 776,450.00 USD | 3,790,000.00 USD |
| `1D` | `1.36` | 134,520,000.00 USD | 134,520,000.00 USD | 0.00 USD | 335,960.00 USD | 66,020.00 USD | 426,530.00 USD |
| `7D` | `1.36` | 232,350,000.00 USD | 232,350,000.00 USD | 0.00 USD | 2,550,000.00 USD | 867,260.00 USD | 2,920,000.00 USD |
| `1D` | `1.36` | 135,020,000.00 USD | 135,020,000.00 USD | 0.00 USD | 148,530.00 USD | 44,160.00 USD | 310,320.00 USD |
| `7D` | `1.36` | 234,890,000.00 USD | 234,890,000.00 USD | 0.00 USD | 1,060,000.00 USD | 639,580.00 USD | 837,310.00 USD |
| `1D` | `1.36` | 135,570,000.00 USD | 135,570,000.00 USD | 0.00 USD | 269,010.00 USD | 48,080.00 USD | 234,460.00 USD |
| `7D` | `1.36` | 237,530,000.00 USD | 237,530,000.00 USD | 0.00 USD | 1,300,000.00 USD | 280,910.00 USD | 1,060,000.00 USD |
| `1D` | `1.36` | 136,110,000.00 USD | 136,110,000.00 USD | 0.00 USD | 143,090.00 USD | 117,400.00 USD | 276,810.00 USD |
| `7D` | `1.36` | 240,790,000.00 USD | 240,790,000.00 USD | 0.00 USD | 1,480,000.00 USD | 652,340.00 USD | 1,140,000.00 USD |
| `1D` | `1.36` | 136,210,000.00 USD | 136,210,000.00 USD | 0.00 USD | 78,610.00 USD | 13,410.00 USD | 6,070.00 USD |
| `7D` | `1.36` | 243,450,000.00 USD | 243,450,000.00 USD | 0.00 USD | 1,420,000.00 USD | 531,090.00 USD | 698,940.00 USD |
| `1D` | `1.37` | 136,470,000.00 USD | 136,470,000.00 USD | 0.00 USD | 56,040.00 USD | 477.43 USD | 206,760.00 USD |
| `7D` | `1.37` | 244,260,000.00 USD | 244,260,000.00 USD | 0.00 USD | 206,650.00 USD | 189,790.00 USD | 421,640.00 USD |
| `1D` | `1.37` | 136,770,000.00 USD | 136,770,000.00 USD | 0.00 USD | 98,240.00 USD | 110,720.00 USD | 87,980.00 USD |
| `7D` | `1.37` | 245,320,000.00 USD | 245,320,000.00 USD | 0.00 USD | 486,840.00 USD | 176,380.00 USD | 389,280.00 USD |
| `1D` | `1.37` | 136,780,000.00 USD | 136,780,000.00 USD | 0.00 USD | 1,170.00 USD | 10,080.00 USD | 1,340.00 USD |
| `7D` | `1.37` | 246,740,000.00 USD | 246,740,000.00 USD | 0.00 USD | 367,350.00 USD | 211,750.00 USD | 841,910.00 USD |
| `1D` | `1.37` | 136,990,000.00 USD | 136,990,000.00 USD | 0.00 USD | 6,620.00 USD | 30,590.00 USD | 175,320.00 USD |
| `7D` | `1.37` | 247,970,000.00 USD | 247,970,000.00 USD | 0.00 USD | 393,010.00 USD | 171,680.00 USD | 667,760.00 USD |
| `1D` | `1.37` | 137,100,000.00 USD | 137,100,000.00 USD | 0.00 USD | 31,610.00 USD | 8,290.00 USD | 71,880.00 USD |
| `7D` | `1.37` | 249,640,000.00 USD | 249,640,000.00 USD | 0.00 USD | 563,840.00 USD | 386,690.00 USD | 717,890.00 USD |
| `1D` | `1.38` | 137,560,000.00 USD | 137,560,000.00 USD | 0.00 USD | 126,800.00 USD | 79,730.00 USD | 249,770.00 USD |
| `7D` | `1.38` | 250,670,000.00 USD | 250,670,000.00 USD | 0.00 USD | 242,030.00 USD | 273,360.00 USD | 514,140.00 USD |
| `1D` | `1.38` | 137,910,000.00 USD | 137,910,000.00 USD | 0.00 USD | 77,710.00 USD | 59,850.00 USD | 210,640.00 USD |
| `7D` | `1.38` | 252,230,000.00 USD | 252,230,000.00 USD | 0.00 USD | 692,200.00 USD | 267,730.00 USD | 600,610.00 USD |
| `1D` | `1.38` | 138,120,000.00 USD | 138,120,000.00 USD | 0.00 USD | 22,650.00 USD | 53,100.00 USD | 132,170.00 USD |
| `7D` | `1.38` | 253,930,000.00 USD | 253,930,000.00 USD | 0.00 USD | 436,360.00 USD | 195,830.00 USD | 1,070,000.00 USD |
| `1D` | `1.38` | 138,470,000.00 USD | 138,470,000.00 USD | 0.00 USD | 6,880.00 USD | 73,390.00 USD | 273,100.00 USD |
| `7D` | `1.38` | 255,890,000.00 USD | 255,890,000.00 USD | 0.00 USD | 710,620.00 USD | 348,810.00 USD | 900,700.00 USD |
| `1D` | `1.38` | 138,870,000.00 USD | 138,870,000.00 USD | 0.00 USD | 5,520.00 USD | 78,550.00 USD | 312,810.00 USD |
| `7D` | `1.38` | 256,870,000.00 USD | 256,870,000.00 USD | 0.00 USD | 403,730.00 USD | 253,120.00 USD | 325,550.00 USD |
| `1D` | `1.39` | 139,160,000.00 USD | 139,160,000.00 USD | 0.00 USD | 91,470.00 USD | 89,100.00 USD | 110,450.00 USD |
| `7D` | `1.39` | 257,980,000.00 USD | 257,980,000.00 USD | 0.00 USD | 377,810.00 USD | 322,570.00 USD | 413,510.00 USD |
| `1D` | `1.39` | 139,510,000.00 USD | 139,510,000.00 USD | 0.00 USD | 40,370.00 USD | 153,030.00 USD | 160,820.00 USD |
| `7D` | `1.39` | 259,200,000.00 USD | 259,200,000.00 USD | 0.00 USD | 384,080.00 USD | 308,280.00 USD | 518,070.00 USD |
| `7D` | `1.39` | 259,950,000.00 USD | 259,950,000.00 USD | 0.00 USD | 507,160.00 USD | 118,700.00 USD | 124,730.00 USD |
| `7D` | `1.39` | 260,480,000.00 USD | 260,480,000.00 USD | 0.00 USD | 82,350.00 USD | 90,970.00 USD | 358,080.00 USD |
| `7D` | `1.39` | 260,640,000.00 USD | 260,640,000.00 USD | 0.00 USD | 39,170.00 USD | 22,660.00 USD | 101,420.00 USD |
| `7D` | `1.40` | 260,860,000.00 USD | 260,860,000.00 USD | 0.00 USD | 208,530.00 USD | 1,340.00 USD | 11,130.00 USD |
| `7D` | `1.40` | 260,870,000.00 USD | 260,870,000.00 USD | 0.00 USD | 0.00 USD | 749.75 USD | 7,780.00 USD |
| `7D` | `1.40` | 260,930,000.00 USD | 260,930,000.00 USD | 0.00 USD | 0.00 USD | 247.13 USD | 62,390.00 USD |
| `7D` | `1.40` | 261,010,000.00 USD | 261,010,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 1,670.00 USD |
| `7D` | `1.40` | 261,310,000.00 USD | 261,310,000.00 USD | 0.00 USD | 237,280.00 USD | 21,520.00 USD | 37,690.00 USD |
| `7D` | `1.41` | 261,460,000.00 USD | 261,460,000.00 USD | 0.00 USD | 102,940.00 USD | 43,840.00 USD | 5,300.00 USD |
| `7D` | `1.41` | 261,600,000.00 USD | 261,600,000.00 USD | 0.00 USD | 4,390.00 USD | 15,880.00 USD | 120,660.00 USD |
| `7D` | `1.41` | 261,880,000.00 USD | 261,880,000.00 USD | 0.00 USD | 66,820.00 USD | 15,820.00 USD | 197,430.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.81B` | Total OI Tokens: `2,255,306,254.9 XRP`
  * 1h OI Change: `-0.10%` | 4h OI Change: `-1.42%` | 24h OI Change: `-6.48%`
  * Exchange Breakdown: Binance=`421.96M` | Bybit=`326.11M` | OKX=`96.07M` | Hyperliquid=`197.50M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-18.05K` | Last 24h: `21.94K` | Last 3d: `414.05K` | Last 7d: `1.06M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0092%` |
| **USDT Bybit** | `-0.0161%` | **USDT KuCoin** | `-0.0063%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0003%` | **USDT Bitget** | `-0.0023%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-0.0072%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `43.69%` | `56.31%` | `0.78` | 369,900,000.00 USD |
| `15M` | `Binance` | `39.66%` | `60.34%` | `0.66` | 117,690,000.00 USD |
| `15M` | `OKX` | `45.16%` | `54.84%` | `0.82` | 48,650,000.00 USD |
| `15M` | `Bybit` | `47.94%` | `52.06%` | `0.92` | 43,720,000.00 USD |
| `15M` | `KuCoin` | `27.83%` | `72.17%` | `0.39` | 3,230,000.00 USD |
| `15M` | `Gate` | `44.54%` | `55.46%` | `0.80` | 37,920,000.00 USD |
| `15M` | `Bitget` | `44.67%` | `55.33%` | `0.81` | 16,680,000.00 USD |
| `15M` | `BingX` | `39.66%` | `60.34%` | `0.66` | 6,250,000.00 USD |
| `15M` | `MEXC` | `44.9%` | `55.1%` | `0.81` | 19,050,000.00 USD |
| `15M` | `Bitunix` | `43.94%` | `56.06%` | `0.78` | 15,450,000.00 USD |
| `15M` | `Hyperliquid` | `67.77%` | `32.23%` | `2.10` | 11,020,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.77%` | `49.23%` | `1.03` | 5,200,000.00 USD |
| `15M` | `Crypto.com` | `60.6%` | `39.4%` | `1.54` | 1,910,000.00 USD |
| `15M` | `WhiteBIT` | `0.08%` | `99.92%` | `0.00` | 4,220,000.00 USD |
| `15M` | `HTX` | `42.72%` | `57.28%` | `0.75` | 1,780,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `49.39%` | `50.61%` | `0.98` | 21,020,000.00 USD |
| `15M` | `Bitfinex` | `48.18%` | `51.82%` | `0.93` | 611,040.00 USD |
| `15M` | `Kraken` | `39.13%` | `60.87%` | `0.64` | 3,810,000.00 USD |
| `15M` | `Aster` | `33.84%` | `66.16%` | `0.51` | 7,620,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `53.41%` | `46.59%` | `1.15` | 4,080,000.00 USD |
| `15M` | `Whale Positions` | `39.66%` | `60.34%` | `0.66` | 117,690,000.00 USD |
| `15M` | `Global Accounts` | `43.69%` | `56.31%` | `0.78` | 369,900,000.00 USD |
| `1H` | `XRP` | `54.23%` | `45.77%` | `1.18` | 1,840,000,000.00 USD |
| `1H` | `Binance` | `53.06%` | `46.94%` | `1.13` | 578,840,000.00 USD |
| `1H` | `OKX` | `51.54%` | `48.46%` | `1.06` | 398,660,000.00 USD |
| `1H` | `Bybit` | `55.88%` | `44.12%` | `1.27` | 119,050,000.00 USD |
| `1H` | `KuCoin` | `68.51%` | `31.49%` | `2.18` | 12,010,000.00 USD |
| `1H` | `Gate` | `50.71%` | `49.29%` | `1.03` | 288,920,000.00 USD |
| `1H` | `Bitget` | `53.84%` | `46.16%` | `1.17` | 72,030,000.00 USD |
| `1H` | `BingX` | `59.2%` | `40.8%` | `1.45` | 33,480,000.00 USD |
| `1H` | `MEXC` | `54.52%` | `45.48%` | `1.20` | 83,080,000.00 USD |
| `1H` | `Bitunix` | `51.08%` | `48.92%` | `1.04` | 69,540,000.00 USD |
| `1H` | `Hyperliquid` | `81.65%` | `18.35%` | `4.45` | 81,210,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.24%` | `45.76%` | `1.19` | 4,240,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `76.82%` | `23.18%` | `3.31` | 13,250,000.00 USD |
| `1H` | `HTX` | `57.9%` | `42.1%` | `1.38` | 18,530,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `54.85%` | `45.15%` | `1.21` | 10,450,000.00 USD |
| `1H` | `Bitfinex` | `67.63%` | `32.37%` | `2.09` | 480,390.00 USD |
| `1H` | `Kraken` | `48.52%` | `51.48%` | `0.94` | 8,660,000.00 USD |
| `1H` | `Aster` | `52.36%` | `47.64%` | `1.10` | 28,570,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.08%` | `47.92%` | `1.09` | 22,680,000.00 USD |
| `1H` | `Whale Positions` | `53.06%` | `46.94%` | `1.13` | 578,840,000.00 USD |
| `1H` | `Global Accounts` | `54.23%` | `45.77%` | `1.18` | 1,840,000,000.00 USD |
| `4H` | `XRP` | `46.48%` | `53.52%` | `0.87` | 10,770,000,000.00 USD |
| `4H` | `Binance` | `44.28%` | `55.72%` | `0.79` | 3,140,000,000.00 USD |
| `4H` | `OKX` | `49.27%` | `50.73%` | `0.97` | 1,510,000,000.00 USD |
| `4H` | `Bybit` | `45.96%` | `54.04%` | `0.85` | 961,110,000.00 USD |
| `4H` | `KuCoin` | `51.59%` | `48.41%` | `1.07` | 29,620,000.00 USD |
| `4H` | `Gate` | `50.56%` | `49.44%` | `1.02` | 1,080,000,000.00 USD |
| `4H` | `Bitget` | `44.16%` | `55.84%` | `0.79` | 487,570,000.00 USD |
| `4H` | `BingX` | `49.63%` | `50.37%` | `0.99` | 203,010,000.00 USD |
| `4H` | `MEXC` | `46.77%` | `53.23%` | `0.88` | 515,790,000.00 USD |
| `4H` | `Bitunix` | `48.49%` | `51.51%` | `0.94` | 436,620,000.00 USD |
| `4H` | `Hyperliquid` | `43.64%` | `56.36%` | `0.77` | 619,770,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.38%` | `49.62%` | `1.02` | 693,970,000.00 USD |
| `4H` | `Crypto.com` | `47.15%` | `52.85%` | `0.89` | 37,350,000.00 USD |
| `4H` | `WhiteBIT` | `16.18%` | `83.82%` | `0.19` | 193,410,000.00 USD |
| `4H` | `HTX` | `44.94%` | `55.06%` | `0.82` | 36,960,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.43%` | `48.57%` | `1.06` | 515,160,000.00 USD |
| `4H` | `Bitfinex` | `50.22%` | `49.78%` | `1.01` | 8,360,000.00 USD |
| `4H` | `Kraken` | `47.61%` | `52.39%` | `0.91` | 71,120,000.00 USD |
| `4H` | `Aster` | `45.14%` | `54.86%` | `0.82` | 116,140,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.46%` | `48.54%` | `1.06` | 99,410,000.00 USD |
| `4H` | `Whale Positions` | `44.28%` | `55.72%` | `0.79` | 3,140,000,000.00 USD |
| `4H` | `Global Accounts` | `46.48%` | `53.52%` | `0.87` | 10,770,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 12,807,415.42 USD | 6,692,980.18 USD | 6,114,435.24 USD | 578,544.93 USD | `+4.52%` | `12B / 4S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.26` | 7,616,675.33 USD | 3,341,703.26 USD | 4,274,972.07 USD | -933,268.81 USD | `-12.25%` | `11B / 16S` |
| `0:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 4,530,946.41 USD | 2,213,429.43 USD | 2,317,516.98 USD | -104,087.54 USD | `-2.30%` | `0B / 9S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 5,245,480.96 USD | 2,448,103.42 USD | 2,797,377.55 USD | -349,274.13 USD | `-6.66%` | `3B / 8S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 6,871,051.82 USD | 2,753,850.97 USD | 4,117,200.85 USD | -1,363,349.88 USD | `-19.84%` | `6B / 18S` |
| `5:00 UTC` | `1.24` | `1.25` | `1.24` | `1.25` | `1.24` | 7,510,859.07 USD | 3,308,536.37 USD | 4,202,322.70 USD | -893,786.33 USD | `-11.90%` | `5B / 11S` |
| `0:00 UTC` | `1.25` | `1.25` | `1.25` | `1.26` | `1.25` | 11,036,044.54 USD | 6,175,268.47 USD | 4,860,776.07 USD | 1,314,492.40 USD | `+11.91%` | `19B / 7S` |
| `5:00 UTC` | `1.26` | `1.26` | `1.26` | `1.26` | `1.25` | 7,717,281.13 USD | 3,718,491.89 USD | 3,998,789.24 USD | -280,297.35 USD | `-3.63%` | `12B / 9S` |
| `0:00 UTC` | `1.25` | `1.26` | `1.25` | `1.26` | `1.25` | 6,089,032.56 USD | 3,424,413.21 USD | 2,664,619.34 USD | 759,793.87 USD | `+12.48%` | `17B / 11S` |
| `5:00 UTC` | `1.25` | `1.25` | `1.25` | `1.25` | `1.25` | 2,780,960.51 USD | 1,113,016.87 USD | 1,667,943.63 USD | -554,926.76 USD | `-19.95%` | `0B / 14S` |

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
| `5m` | 95,950.00 USD | -1,470,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -872,740.00 USD | -1,420,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -463,020.00 USD | -1,680,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 1,370,000.00 USD | -935,700.00 USD | **`ACCUMULATION`** |
| `2h` | -866,920.00 USD | -16,320,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 728,040.00 USD | -24,480,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 6,070,000.00 USD | -18,810,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 19,160,000.00 USD | 15,240,000.00 USD | **`ACCUMULATION`** |
| `12h` | -746,790.00 USD | -23,330,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -47,800,000.00 USD | -145,900,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -111,970,000.00 USD | -232,120,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -592,450,000.00 USD | -1,310,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+95.95K` | 15m=`-872.74K` | 1h=`+1.37M` | 24h=`-47.80M`
* Futures Capital Netflows: 5m=`-1.47M` | 15m=`-1.42M` | 1h=`-935.70K` | 24h=`-145.90M`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1.22` (Risk Distance: `0.0133` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.27` (Risk Distance: `0.0133` pts)
  * +2.5R Take Profit: `1.23`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.26`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
