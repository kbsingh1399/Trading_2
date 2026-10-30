# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUAUD
**Canonical Key**: `XAUAUD` | **Broker Instrument**: `XAUAUD.pi` | **Asset Class**: `Forex Cross`
**Timestamp**: `2026-10-30 16:12:33 IST` (`2026-10-30 10:42:33 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3981.59` | **Live Ask Quote**: `3981.67` | **Mid Price**: `3981.63`
- **Spread Points**: `8.00` | **Spread BPS**: `0.20 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `100.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `1.00 USD` | Point Value (0.01 Lot): `0.0100 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `3996.02` | VWAP Z-Score: `-1.60` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.83` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `40.42` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4025.26` | Lower -3.00σ Band: `3966.79`
  * Upper +2.51σ Band: `4020.48` | Lower -2.51σ Band: `3971.56`
  * Upper +2.01σ Band: `4015.61` | Lower -2.01σ Band: `3976.44`
  * Upper +2.00σ Band: `4015.51` | Lower -2.00σ Band: `3976.53`
  * Upper +1.28σ Band: `4008.50` | Lower -1.28σ Band: `3983.55`
  * Upper +1.00σ Band: `4005.77` | Lower -1.00σ Band: `3986.28`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3986.72` | EMA-20=`3989.00` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`3997.13` (Slope: `+0.0000`) | EMA-100=`4007.86`
  * Institutional Anchors: EMA-144=`4013.93` | EMA-200=`4019.04` (Slope: `-0.1030`) | EMA-233=`4022.21`
- **Range Boundaries**: 24H High=`4039.31` | 24H Low=`3965.22` | Weekly High=`4082.75` | Weekly Low=`3965.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4007.50` (Distance: `-0.65%`)
  * Point of Control (POC) = `3990.50` (Distance: `-0.23%`)
  * Value Area Low (VAL) = `3982.43` (Distance: `-0.03%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4053.37` | Weekly POC=`4017.32` | Weekly VAL=`4004.00`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3965.22`
  * New York Session (13:00-21:00 UTC): High=`3991.98` | Low=`3979.80`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3988.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3965.70` - `3997.56`
  * Optimal Trade Entry (OTE 0.705): `3989.59`
  * Structural Invalidation Anchor (0.786): `4013.48`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3986.43` | `3989.15` | `3986.43` | `3988.24` | `50` | 198,167.26 USD | 92,053.57 USD | `+46.45%` | 30,767.41 USD | `+1.17` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `3988.10` | `3988.11` | `3986.49` | `3987.45` | `35` | 138,334.59 USD | 23,668.83 USD | `+17.11%` | 54,436.24 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `3987.45` | `3988.82` | `3987.45` | `3988.07` | `8` | 29,974.06 USD | 3,157.04 USD | `+10.53%` | 57,593.28 USD | `+0.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `3995.66` | `3995.82` | `3988.52` | `3988.53` | `295` | 1,178,649.83 USD | -275,535.97 USD | `-23.38%` | 125,656.32 USD | `-0.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `3988.52` | `3991.57` | `3986.48` | `3986.48` | `125` | 499,730.03 USD | -186,942.49 USD | `-37.41%` | -61,286.16 USD | `-0.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `3986.43` | `3989.15` | `3986.43` | `3988.07` | `92` | 366,475.91 USD | 118,879.45 USD | `+32.44%` | 57,593.28 USD | `+0.71` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `3981.68` | `4002.39` | `3979.22` | `4001.26` | `1,541` | 6,150,835.88 USD | 541,833.50 USD | `+8.81%` | 137,263.91 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4001.22` | `4002.41` | `3991.51` | `3995.66` | `459` | 1,835,738.77 USD | 110,152.21 USD | `+6.00%` | 247,416.12 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `3995.66` | `3995.82` | `3986.43` | `3988.07` | `512` | 2,044,855.78 USD | -343,599.01 USD | `-16.80%` | -96,182.89 USD | `-0.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `3988.07` | `2,513` | 10,031,897.03 USD | 308,215.21 USD | `+3.07%` | -270,751.02 USD | `+0.44` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,524,929.80 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,542,786.16 USD | `-1.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `3988.07` | `2,513` | 10,031,897.03 USD | 308,215.21 USD | `+3.07%` | -270,751.02 USD | `+0.44` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `3981.60` | `1.6930` | 6,740.85 USD | 860,064.54 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `3981.70` | `10.7656` | 42,865.39 USD | 853,323.69 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3981.80` | `4.2369` | 16,870.49 USD | 810,458.31 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3981.90` | `57.0609` | 227,210.80 USD | 793,587.82 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3982.00` | `0.4759` | 1,895.03 USD | 566,377.02 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3982.10` | `14.2930` | 56,916.16 USD | 564,481.99 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3982.20` | `20.3709` | 81,121.00 USD | 507,565.83 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `3982.30` | `2.4125` | 9,607.30 USD | 426,444.83 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3982.40` | `3.8994` | 15,528.97 USD | 416,837.53 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3982.50` | `36.6043` | 145,776.62 USD | 401,308.56 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3982.60` | `14.8455` | 59,123.69 USD | 255,531.94 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3982.80` | `10.9105` | 43,454.34 USD | 196,408.25 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3982.90` | `5.0515` | 20,119.62 USD | 152,953.91 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `3983.00` | `8.4069` | 33,484.68 USD | 132,834.29 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `3983.20` | `0.4224` | 1,682.50 USD | 99,349.61 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3983.30` | `0.1245` | 495.92 USD | 97,667.10 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3983.40` | `7.5304` | 29,996.60 USD | 97,171.18 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `3983.50` | `10.0362` | 39,979.20 USD | 67,174.59 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3983.70` | `0.2510` | 999.91 USD | 27,195.39 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `3983.80` | `6.5755` | 26,195.48 USD | 26,195.48 USD | `5 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3983.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,983.85` | `0.00%` | `-` |
| `ASK` | `3983.90` | `21.9864` | 87,591.62 USD | 87,591.62 USD | `13 orders` | `+0.00%` | `-` |
| `ASK` | `3984.00` | `11.2954` | 45,000.87 USD | 132,592.49 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `3984.10` | `25.3517` | 101,003.71 USD | 233,596.20 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3984.20` | `6.7372` | 26,842.35 USD | 260,438.55 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3984.30` | `12.9042` | 51,414.20 USD | 311,852.76 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `3984.40` | `20.4346` | 81,419.62 USD | 393,272.38 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3984.50` | `4.5308` | 18,052.97 USD | 411,325.35 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3984.60` | `77.9489` | 310,595.19 USD | 721,920.54 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `3984.70` | `32.8102` | 130,738.80 USD | 852,659.34 USD | `7 orders` | `+0.02%` | `-` |
| `ASK` | `3984.80` | `15.7574` | 62,790.09 USD | 915,449.43 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3984.90` | `89.2995` | 355,849.58 USD | 1,271,299.01 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `3985.00` | `11.4927` | 45,798.41 USD | 1,317,097.42 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `3985.10` | `4.2350` | 16,876.90 USD | 1,333,974.31 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `3985.20` | `20.5372` | 81,844.85 USD | 1,415,819.16 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3985.30` | `0.9943` | 3,962.58 USD | 1,419,781.75 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `3985.40` | `13.3875` | 53,354.54 USD | 1,473,136.29 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3985.50` | `80.8310` | 322,151.95 USD | 1,795,288.24 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3985.60` | `20.3737` | 81,201.42 USD | 1,876,489.66 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `3985.70` | `25.8622` | 103,078.97 USD | 1,979,568.63 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `3985.80` | `3.7080` | 14,779.35 USD | 1,994,347.98 USD | `2 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:12:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `47` | `0x5b5d...c060` | `SHORT` | 25,851,564.92 USD | `6,489.82` | `4185.46` | `3984.10` | `27643.26` | 1,311,386.09 USD | `+5.07%` | `4X Cross` |
| `49` | `0x4692...164f` | `SHORT` | 25,129,893.65 USD | `6,306.91` | `4127.28` | `3984.10` | `14220.61` | 900,547.26 USD | `+3.58%` | `5X Cross` |
| `63` | `0xb83d...6e36` | `SHORT` | 23,390,962.12 USD | `5,869.90` | `4228.86` | `3984.10` | `22407.07` | 1,432,059.82 USD | `+6.12%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,234,501.96 USD | `4,828.91` | `4157.43` | `3984.10` | `2274.60` | -841,380.35 USD | `-4.37%` | `25X Cross` |
| `142` | `0x645b...87b8` | `LONG` | 14,124,725.41 USD | `3,545.72` | `4127.81` | `3984.10` | `660.25` | -511,356.77 USD | `-3.62%` | `3X Cross` |
| `157` | `0x7a6d...f79c` | `SHORT` | 13,022,849.14 USD | `3,268.21` | `4228.94` | `3984.10` | `4381.92` | 798,229.99 USD | `+6.13%` | `25X Cross` |
| `180` | `0xa742...e390` | `SHORT` | 11,156,968.46 USD | `2,800.02` | `4364.62` | `3984.10` | `4212.84` | 1,064,075.68 USD | `+9.54%` | `20X Cross` |
| `260` | `0x3678...b209` | `LONG` | 8,765,460.00 USD | `2,200.00` | `4176.09` | `3984.10` | `2632.63` | -421,959.30 USD | `-4.81%` | `25X Cross` |
| `261` | `0x41e5...0825` | `SHORT` | 8,762,600.00 USD | `2,200.00` | `4112.20` | `3984.10` | `4287.19` | 284,254.59 USD | `+3.24%` | `20X Cross` |
| `296` | `0xacb6...efbd` | `SHORT` | 7,868,092.66 USD | `1,975.37` | `4048.55` | `3984.10` | `6680.40` | 129,299.05 USD | `+1.64%` | `6X Cross` |
| `363` | `0xc26c...b8f4` | `LONG` | 6,295,475.94 USD | `1,579.95` | `4075.62` | `3984.10` | `0.000000` | -143,821.03 USD | `-2.28%` | `1X Cross` |
| `558` | `0x63da...8add` | `LONG` | 3,984,700.00 USD | `1,000.00` | `4021.46` | `3984.10` | `3564.73` | -36,760.96 USD | `-0.92%` | `25X Cross` |
| `570` | `0xf3dc...1672` | `LONG` | 3,921,925.03 USD | `984.27` | `4018.39` | `3984.10` | `2824.18` | -33,261.66 USD | `-0.85%` | `20X Cross` |
| `586` | `0x9aa5...58af` | `LONG` | 3,826,781.16 USD | `960.32` | `4279.98` | `3984.10` | `0.000000` | -283,372.12 USD | `-7.40%` | `20X Cross` |
| `671` | `0x4a20...3c26` | `LONG` | 3,336,451.62 USD | `837.40` | `4599.73` | `3984.10` | `0.000000` | -515,368.76 USD | `-15.45%` | `20X Cross` |
| `782` | `0x9c06...0560` | `LONG` | 2,896,612.14 USD | `726.95` | `4002.36` | `3984.10` | `0.000000` | -12,917.11 USD | `-0.45%` | `25X Cross` |
| `823` | `0x0fac...7a0a` | `LONG` | 2,735,436.78 USD | `686.49` | `4290.34` | `3984.10` | `1301.77` | -209,821.92 USD | `-7.67%` | `25X Cross` |
| `850` | `0x354b...6425` | `LONG` | 2,638,830.27 USD | `662.21` | `4004.29` | `3984.10` | `0.000000` | -12,846.44 USD | `-0.49%` | `10X Cross` |
| `897` | `0x625e...a354` | `SHORT` | 2,469,460.00 USD | `620.00` | `4122.81` | `3984.10` | `4279.60` | 86,687.03 USD | `+3.51%` | `20X Cross` |
| `929` | `0xeae3...e8ad` | `SHORT` | 2,390,160.00 USD | `600.00` | `4104.77` | `3984.10` | `4268.68` | 72,705.11 USD | `+3.04%` | `20X Cross` |
| `931` | `0xf285...fa82` | `LONG` | 2,383,272.58 USD | `598.11` | `4146.45` | `3984.10` | `3891.87` | -96,746.97 USD | `-4.06%` | `25X Cross` |
| `936` | `0xd8c5...99b0` | `SHORT` | 2,368,266.53 USD | `594.35` | `4175.35` | `3984.10` | `35353.38` | 113,377.50 USD | `+4.79%` | `4X Cross` |
| `939` | `0x12f7...8750` | `LONG` | 2,333,482.96 USD | `585.61` | `4082.77` | `3984.10` | `2779.82` | -57,434.02 USD | `-2.46%` | `10X Cross` |
| `988` | `0x413c...886c` | `LONG` | 2,229,265.76 USD | `559.47` | `4007.05` | `3984.10` | `0.000000` | -12,561.45 USD | `-0.56%` | `2X Cross` |
| `1091` | `0x61ce...a62b` | `SHORT` | 1,982,352.45 USD | `497.50` | `4071.66` | `3984.10` | `4719.47` | 43,316.35 USD | `+2.19%` | `20X Cross` |
| `1213` | `0xead5...69f2` | `LONG` | 1,807,466.65 USD | `453.78` | `4220.88` | `3984.10` | `3539.57` | -107,901.41 USD | `-5.97%` | `5X Isolated` |
| `1298` | `0x46fc...1195` | `LONG` | 1,664,122.13 USD | `417.61` | `4051.00` | `3984.10` | `2258.84` | -27,607.24 USD | `-1.66%` | `20X Cross` |
| `1345` | `0x6d15...d374` | `LONG` | 1,593,960.00 USD | `400.00` | `4068.25` | `3984.10` | `3842.44` | -33,340.00 USD | `-2.09%` | `25X Cross` |
| `1346` | `0xee02...309d` | `SHORT` | 1,593,840.00 USD | `400.00` | `4438.84` | `3984.10` | `4202.98` | 181,698.60 USD | `+11.40%` | `25X Isolated` |
| `1383` | `0x02a7...fe9f` | `SHORT` | 1,554,033.00 USD | `390.00` | `4055.02` | `3984.10` | `4307.31` | 27,426.25 USD | `+1.76%` | `25X Cross` |
| `1438` | `0x7e77...b8d2` | `SHORT` | 1,513,768.00 USD | `380.00` | `4131.92` | `3984.10` | `4294.11` | 56,361.64 USD | `+3.72%` | `20X Cross` |
| `1453` | `0x72c2...9b37` | `LONG` | 1,486,405.85 USD | `373.13` | `4000.98` | `3984.10` | `3778.67` | -6,487.67 USD | `-0.44%` | `13X Isolated` |
| `1499` | `0xaa44...b844` | `LONG` | 1,434,096.00 USD | `360.00` | `4043.10` | `3984.10` | `3225.88` | -21,421.63 USD | `-1.49%` | `7X Cross` |
| `1606` | `0xa41f...d50a` | `LONG` | 1,310,749.49 USD | `328.96` | `4468.89` | `3984.10` | `3802.79` | -159,348.36 USD | `-12.16%` | `15X Cross` |
| `1656` | `0xbf5a...88ba` | `SHORT` | 1,265,759.48 USD | `317.65` | `4091.80` | `3984.10` | `9945.00` | 34,023.55 USD | `+2.69%` | `20X Cross` |
| `1694` | `0xff31...ff6c` | `SHORT` | 1,235,226.00 USD | `310.00` | `4372.43` | `3984.10` | `4789.78` | 120,229.38 USD | `+9.73%` | `10X Isolated` |
| `1719` | `0xada6...6f88` | `LONG` | 1,209,192.62 USD | `303.47` | `4166.46` | `3984.10` | `1803.94` | -55,189.84 USD | `-4.56%` | `5X Cross` |
| `1878` | `0x50e2...d770` | `LONG` | 1,077,224.83 USD | `270.37` | `4243.58` | `3984.10` | `2562.72` | -70,101.63 USD | `-6.51%` | `20X Cross` |
| `1890` | `0x4c92...4f17` | `SHORT` | 1,062,801.18 USD | `266.72` | `4260.98` | `3984.10` | `6486.15` | 73,691.06 USD | `+6.93%` | `20X Cross` |
| `1964` | `0xd346...c4f3` | `LONG` | 1,016,791.04 USD | `255.17` | `4188.66` | `3984.10` | `3311.05` | -52,045.47 USD | `-5.12%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4002.80` | 24.02 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.02K USD at 4002.8000 USD [API] | `2026-10-23 01:55:44` |
| `ANNOUNCEMENT` | `INFO` | `4002.80` | 19.21 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.02K USD at 4002.8000 USD [API] | `2026-10-23 01:55:38` |
| `ANNOUNCEMENT` | `INFO` | `4002.80` | 198.54 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.20K USD at 4002.8000 USD [API] | `2026-10-23 01:55:38` |
| `ANNOUNCEMENT` | `INFO` | `4089.00` | 1,227.52 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 1.23K USD at 4089.0000 USD [API] | `2026-10-07 12:28:33` |
| `ANNOUNCEMENT` | `INFO` | `4089.00` | 12,789.57 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 12.79K USD at 4089.0000 USD [API | `2026-10-07 12:28:33` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4071.25` (Vol: 14,000,000.00 USD, Dist: `+2.03%`) | Long MP=`3950.06` (Vol: 10,500,000.00 USD, Dist: `--1.01%`)
  * 48H Horizon: Short MP=`4076.12` (Vol: 15,300,000.00 USD, Dist: `+2.15%`) | Long MP=`3969.36` (Vol: 9,500,000.00 USD, Dist: `--0.53%`)
  * 3D Horizon: Short MP=`4076.12` (Vol: 15,300,000.00 USD, Dist: `+2.15%`) | Long MP=`3950.52` (Vol: 11,100,000.00 USD, Dist: `--1.00%`)
  * 7D Horizon: Short MP=`4076.12` (Vol: 15,300,000.00 USD, Dist: `+2.15%`) | Long MP=`3963.08` (Vol: 21,000,000.00 USD, Dist: `--0.69%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3578.80` | 20,310,000.00 USD | 0.00 USD | 20,310,000.00 USD | 0.00 USD | 0.00 USD | 17,590.00 USD |
| `7D` | `3583.10` | 20,290,000.00 USD | 0.00 USD | 20,290,000.00 USD | 18,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3584.30` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3587.40` | 20,270,000.00 USD | 0.00 USD | 20,270,000.00 USD | 12,470.00 USD | 0.00 USD | 8,930.00 USD |
| `1D` | `3588.40` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 8,580.00 USD | 0.00 USD | 11,470.00 USD |
| `7D` | `3591.70` | 20,250,000.00 USD | 0.00 USD | 20,250,000.00 USD | 59,500.00 USD | 0.00 USD | 129,530.00 USD |
| `1D` | `3592.50` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 39,400.00 USD | 0.00 USD | 19,990.00 USD |
| `7D` | `3596.00` | 20,060,000.00 USD | 0.00 USD | 20,060,000.00 USD | 78,750.00 USD | 0.00 USD | 131,570.00 USD |
| `1D` | `3596.60` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 12,780.00 USD | 0.00 USD | 56,550.00 USD |
| `7D` | `3600.30` | 19,850,000.00 USD | 0.00 USD | 19,850,000.00 USD | 104,970.00 USD | 0.00 USD | 265,490.00 USD |
| `1D` | `3600.70` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 9,910.00 USD | 0.00 USD | 36,570.00 USD |
| `7D` | `3604.60` | 19,480,000.00 USD | 0.00 USD | 19,480,000.00 USD | 31,270.00 USD | 0.00 USD | 55,830.00 USD |
| `1D` | `3604.80` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 13,210.00 USD | 0.00 USD | 24,320.00 USD |
| `1D` | `3608.90` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 18,870.00 USD | 0.00 USD | 61,470.00 USD |
| `7D` | `3608.90` | 19,390,000.00 USD | 0.00 USD | 19,390,000.00 USD | 18,230.00 USD | 0.00 USD | 79,200.00 USD |
| `1D` | `3613.00` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 13,760.00 USD | 0.00 USD | 26,910.00 USD |
| `7D` | `3613.20` | 19,300,000.00 USD | 0.00 USD | 19,300,000.00 USD | 49,560.00 USD | 0.00 USD | 48,820.00 USD |
| `1D` | `3617.10` | 5,280,000.00 USD | 0.00 USD | 5,280,000.00 USD | 15,460.00 USD | 0.00 USD | 25,340.00 USD |
| `7D` | `3617.50` | 19,200,000.00 USD | 0.00 USD | 19,200,000.00 USD | 20,780.00 USD | 0.00 USD | 57,940.00 USD |
| `1D` | `3621.20` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 10,550.00 USD | 0.00 USD | 40,430.00 USD |
| `7D` | `3621.80` | 19,120,000.00 USD | 0.00 USD | 19,120,000.00 USD | 23,640.00 USD | 0.00 USD | 118,230.00 USD |
| `1D` | `3625.30` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 12,170.00 USD | 0.00 USD | 3,580.00 USD |
| `7D` | `3626.10` | 18,980,000.00 USD | 0.00 USD | 18,980,000.00 USD | 35,220.00 USD | 0.00 USD | 43,920.00 USD |
| `1D` | `3629.40` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 4,600.00 USD |
| `7D` | `3630.40` | 18,900,000.00 USD | 0.00 USD | 18,900,000.00 USD | 34,300.00 USD | 0.00 USD | 71,240.00 USD |
| `7D` | `3634.70` | 18,790,000.00 USD | 0.00 USD | 18,790,000.00 USD | 57,970.00 USD | 0.00 USD | 46,780.00 USD |
| `7D` | `3639.00` | 18,690,000.00 USD | 0.00 USD | 18,690,000.00 USD | 68,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3643.30` | 18,620,000.00 USD | 0.00 USD | 18,620,000.00 USD | 20,110.00 USD | 0.00 USD | 19,320.00 USD |
| `7D` | `3647.60` | 18,580,000.00 USD | 0.00 USD | 18,580,000.00 USD | 19,450.00 USD | 0.00 USD | 20,140.00 USD |
| `7D` | `3656.20` | 18,540,000.00 USD | 0.00 USD | 18,540,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3660.50` | 18,520,000.00 USD | 0.00 USD | 18,520,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3813.90` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 35,390.00 USD |
| `7D` | `3815.30` | 18,510,000.00 USD | 0.00 USD | 18,510,000.00 USD | 0.00 USD | 0.00 USD | 43,990.00 USD |
| `1D` | `3818.00` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 11,210.00 USD | 0.00 USD | 5,940.00 USD |
| `7D` | `3819.60` | 18,470,000.00 USD | 0.00 USD | 18,470,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3822.10` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 26,640.00 USD | 0.00 USD | 27,360.00 USD |
| `7D` | `3823.90` | 18,460,000.00 USD | 0.00 USD | 18,460,000.00 USD | 44,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3826.20` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 9,770.00 USD | 0.00 USD | 4,790.00 USD |
| `7D` | `3828.20` | 18,410,000.00 USD | 0.00 USD | 18,410,000.00 USD | 96,460.00 USD | 0.00 USD | 97,010.00 USD |
| `1D` | `3830.30` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 61,350.00 USD | 0.00 USD | 64,560.00 USD |
| `7D` | `3832.50` | 18,220,000.00 USD | 0.00 USD | 18,220,000.00 USD | 243,890.00 USD | 0.00 USD | 409,620.00 USD |
| `1D` | `3834.40` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 109,120.00 USD | 0.00 USD | 77,670.00 USD |
| `7D` | `3836.80` | 17,570,000.00 USD | 0.00 USD | 17,570,000.00 USD | 309,200.00 USD | 0.00 USD | 809,660.00 USD |
| `1D` | `3838.50` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 26,560.00 USD | 0.00 USD | 143,490.00 USD |
| `7D` | `3841.10` | 16,450,000.00 USD | 0.00 USD | 16,450,000.00 USD | 267,600.00 USD | 0.00 USD | 536,270.00 USD |
| `1D` | `3842.60` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 41,250.00 USD | 0.00 USD | 114,740.00 USD |
| `7D` | `3845.40` | 15,640,000.00 USD | 0.00 USD | 15,640,000.00 USD | 93,100.00 USD | 0.00 USD | 159,850.00 USD |
| `1D` | `3846.70` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 54,420.00 USD | 0.00 USD | 193,100.00 USD |
| `7D` | `3849.70` | 15,390,000.00 USD | 0.00 USD | 15,390,000.00 USD | 109,740.00 USD | 0.00 USD | 290,370.00 USD |
| `1D` | `3850.80` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 85,710.00 USD | 0.00 USD | 119,800.00 USD |
| `7D` | `3854.00` | 14,990,000.00 USD | 0.00 USD | 14,990,000.00 USD | 161,070.00 USD | 0.00 USD | 191,840.00 USD |
| `1D` | `3854.90` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 10,670.00 USD | 0.00 USD | 108,050.00 USD |
| `7D` | `3858.30` | 14,640,000.00 USD | 0.00 USD | 14,640,000.00 USD | 70,500.00 USD | 0.00 USD | 232,350.00 USD |
| `1D` | `3859.00` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 74,760.00 USD | 0.00 USD | 75,820.00 USD |
| `7D` | `3862.60` | 14,330,000.00 USD | 0.00 USD | 14,330,000.00 USD | 95,660.00 USD | 0.00 USD | 316,690.00 USD |
| `1D` | `3863.10` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 39,090.00 USD | 0.00 USD | 126,130.00 USD |
| `7D` | `3866.90` | 13,920,000.00 USD | 0.00 USD | 13,920,000.00 USD | 64,840.00 USD | 0.00 USD | 151,020.00 USD |
| `1D` | `3867.20` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 37,870.00 USD | 0.00 USD | 13,530.00 USD |
| `7D` | `3871.20` | 13,710,000.00 USD | 0.00 USD | 13,710,000.00 USD | 153,110.00 USD | 0.00 USD | 169,500.00 USD |
| `1D` | `3871.30` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 2,390.00 USD | 0.00 USD | 14,010.00 USD |
| `1D` | `3875.40` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 7,090.00 USD |
| `7D` | `3875.50` | 13,380,000.00 USD | 0.00 USD | 13,380,000.00 USD | 186,290.00 USD | 0.00 USD | 169,710.00 USD |
| `7D` | `3879.80` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 214,810.00 USD | 0.00 USD | 18,540.00 USD |
| `7D` | `3884.10` | 12,790,000.00 USD | 0.00 USD | 12,790,000.00 USD | 139,010.00 USD | 0.00 USD | 116,380.00 USD |
| `7D` | `3888.40` | 12,540,000.00 USD | 0.00 USD | 12,540,000.00 USD | 47,590.00 USD | 0.00 USD | 53,820.00 USD |
| `1D` | `3891.80` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 51,470.00 USD |
| `7D` | `3892.70` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 38,150.00 USD | 0.00 USD | 29,780.00 USD |
| `1D` | `3895.90` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 31,200.00 USD |
| `7D` | `3897.00` | 12,370,000.00 USD | 0.00 USD | 12,370,000.00 USD | 34,360.00 USD | 0.00 USD | 106,850.00 USD |
| `1D` | `3900.00` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 75,710.00 USD | 0.00 USD | 31,670.00 USD |
| `7D` | `3901.30` | 12,230,000.00 USD | 0.00 USD | 12,230,000.00 USD | 92,770.00 USD | 0.00 USD | 56,260.00 USD |
| `1D` | `3904.10` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 32,640.00 USD |
| `7D` | `3905.60` | 12,080,000.00 USD | 0.00 USD | 12,080,000.00 USD | 111,810.00 USD | 0.00 USD | 24,220.00 USD |
| `1D` | `3908.20` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 61,670.00 USD | 0.00 USD | 68,370.00 USD |
| `7D` | `3909.90` | 11,940,000.00 USD | 0.00 USD | 11,940,000.00 USD | 387,080.00 USD | 0.00 USD | 590,540.00 USD |
| `1D` | `3912.30` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 248,080.00 USD | 0.00 USD | 161,740.00 USD |
| `7D` | `3914.20` | 10,970,000.00 USD | 0.00 USD | 10,970,000.00 USD | 444,490.00 USD | 0.00 USD | 1,040,000.00 USD |
| `1D` | `3916.40` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 99,340.00 USD | 0.00 USD | 288,880.00 USD |
| `7D` | `3918.50` | 9,480,000.00 USD | 0.00 USD | 9,480,000.00 USD | 607,770.00 USD | 0.00 USD | 1,540,000.00 USD |
| `1D` | `3920.50` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 54,040.00 USD | 0.00 USD | 121,880.00 USD |
| `7D` | `3922.80` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 422,110.00 USD | 0.00 USD | 661,450.00 USD |
| `1D` | `3924.60` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 51,780.00 USD | 0.00 USD | 279,660.00 USD |
| `7D` | `3927.10` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 168,080.00 USD | 0.00 USD | 426,700.00 USD |
| `1D` | `3928.70` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 135,190.00 USD | 0.00 USD | 374,550.00 USD |
| `7D` | `3931.40` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 352,560.00 USD | 0.00 USD | 471,540.00 USD |
| `1D` | `3932.80` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 140,320.00 USD | 0.00 USD | 204,860.00 USD |
| `7D` | `3935.70` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 136,830.00 USD | 0.00 USD | 415,030.00 USD |
| `1D` | `3936.90` | 931,520.00 USD | 0.00 USD | 931,520.00 USD | 54,630.00 USD | 0.00 USD | 212,760.00 USD |
| `7D` | `3940.00` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 164,510.00 USD | 0.00 USD | 372,810.00 USD |
| `1D` | `3941.00` | 664,130.00 USD | 0.00 USD | 664,130.00 USD | 157,330.00 USD | 0.00 USD | 223,820.00 USD |
| `7D` | `3944.30` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 180,040.00 USD | 0.00 USD | 729,990.00 USD |
| `1D` | `3945.10` | 282,980.00 USD | 0.00 USD | 282,980.00 USD | 65,180.00 USD | 0.00 USD | 125,210.00 USD |
| `7D` | `3948.60` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 242,730.00 USD | 0.00 USD | 111,250.00 USD |
| `1D` | `3949.20` | 92,600.00 USD | 0.00 USD | 92,600.00 USD | 33,570.00 USD | 0.00 USD | 20,850.00 USD |
| `7D` | `3952.90` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 283,610.00 USD | 0.00 USD | 392,210.00 USD |
| `1D` | `3953.30` | 38,180.00 USD | 0.00 USD | 38,180.00 USD | 4,780.00 USD | 0.00 USD | 33,400.00 USD |
| `7D` | `3957.20` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 401,510.00 USD | 0.00 USD | 286,230.00 USD |
| `7D` | `3961.50` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 379,850.00 USD | 0.00 USD | 52,260.00 USD |
| `7D` | `3965.80` | 675,740.00 USD | 0.00 USD | 675,740.00 USD | 217,200.00 USD | 0.00 USD | 217,580.00 USD |
| `7D` | `3970.10` | 240,970.00 USD | 0.00 USD | 240,970.00 USD | 74,180.00 USD | 0.00 USD | 14,560.00 USD |
| `7D` | `3974.40` | 152,230.00 USD | 0.00 USD | 152,230.00 USD | 76,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3978.70` | 75,930.00 USD | 0.00 USD | 75,930.00 USD | 0.00 USD | 0.00 USD | 75,930.00 USD |
| `7D` | `3980.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3981.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3983.00` | 74,360.00 USD | 74,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 74,360.00 USD |
| `1D` | `4051.70` | 70,790.00 USD | 70,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 70,790.00 USD |
| `7D` | `4051.80` | 162,330.00 USD | 162,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 87,970.00 USD |
| `1D` | `4055.80` | 82,670.00 USD | 82,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,880.00 USD |
| `1D` | `4059.90` | 190,050.00 USD | 190,050.00 USD | 0.00 USD | 75,710.00 USD | 0.00 USD | 31,670.00 USD |
| `7D` | `4060.40` | 183,500.00 USD | 183,500.00 USD | 0.00 USD | 21,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4064.00` | 222,690.00 USD | 222,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 32,640.00 USD |
| `7D` | `4064.70` | 276,330.00 USD | 276,330.00 USD | 0.00 USD | 68,610.00 USD | 0.00 USD | 24,220.00 USD |
| `1D` | `4068.10` | 352,730.00 USD | 352,730.00 USD | 0.00 USD | 61,670.00 USD | 0.00 USD | 68,370.00 USD |
| `7D` | `4069.00` | 921,450.00 USD | 921,450.00 USD | 0.00 USD | 279,260.00 USD | 0.00 USD | 365,870.00 USD |
| `1D` | `4072.20` | 778,260.00 USD | 778,260.00 USD | 0.00 USD | 248,080.00 USD | 0.00 USD | 177,460.00 USD |
| `7D` | `4073.30` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 431,680.00 USD | 0.00 USD | 1,020,000.00 USD |
| `1D` | `4076.30` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 99,340.00 USD | 0.00 USD | 279,410.00 USD |
| `7D` | `4077.60` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 623,790.00 USD | 0.00 USD | 1,590,000.00 USD |
| `1D` | `4080.40` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 54,040.00 USD | 0.00 USD | 115,640.00 USD |
| `7D` | `4081.90` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 498,700.00 USD | 0.00 USD | 793,730.00 USD |
| `1D` | `4084.50` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 51,780.00 USD | 0.00 USD | 279,660.00 USD |
| `7D` | `4086.20` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 115,840.00 USD | 0.00 USD | 389,820.00 USD |
| `1D` | `4088.60` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 135,190.00 USD | 0.00 USD | 329,730.00 USD |
| `7D` | `4090.50` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 219,480.00 USD | 0.00 USD | 426,710.00 USD |
| `1D` | `4092.70` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 134,290.00 USD | 0.00 USD | 249,680.00 USD |
| `7D` | `4094.80` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 322,150.00 USD | 0.00 USD | 383,690.00 USD |
| `1D` | `4096.80` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 54,440.00 USD | 0.00 USD | 163,420.00 USD |
| `7D` | `4099.10` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 97,100.00 USD | 0.00 USD | 464,690.00 USD |
| `1D` | `4100.90` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 124,130.00 USD | 0.00 USD | 201,590.00 USD |
| `7D` | `4103.40` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 222,430.00 USD | 0.00 USD | 501,260.00 USD |
| `1D` | `4105.00` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 77,620.00 USD | 0.00 USD | 181,750.00 USD |
| `7D` | `4107.70` | 9,550,000.00 USD | 9,550,000.00 USD | 0.00 USD | 125,730.00 USD | 0.00 USD | 404,560.00 USD |
| `1D` | `4109.10` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 60,550.00 USD | 0.00 USD | 27,060.00 USD |
| `7D` | `4112.00` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 305,770.00 USD | 0.00 USD | 282,160.00 USD |
| `1D` | `4113.20` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 4,780.00 USD | 0.00 USD | 28,030.00 USD |
| `7D` | `4116.30` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 283,950.00 USD | 0.00 USD | 398,270.00 USD |
| `1D` | `4117.30` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,190.00 USD |
| `7D` | `4120.60` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 401,640.00 USD | 0.00 USD | 27,620.00 USD |
| `7D` | `4124.90` | 11,680,000.00 USD | 11,680,000.00 USD | 0.00 USD | 284,910.00 USD | 0.00 USD | 144,020.00 USD |
| `7D` | `4129.20` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 160,410.00 USD | 0.00 USD | 140,380.00 USD |
| `1D` | `4129.60` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,740.00 USD |
| `7D` | `4133.50` | 12,270,000.00 USD | 12,270,000.00 USD | 0.00 USD | 97,260.00 USD | 0.00 USD | 196,630.00 USD |
| `1D` | `4133.70` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,660.00 USD |
| `1D` | `4137.80` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 17,210.00 USD | 0.00 USD | 21,770.00 USD |
| `7D` | `4137.80` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 59,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4141.90` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 20,650.00 USD | 0.00 USD | 13,950.00 USD |
| `7D` | `4142.10` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 170,620.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `4146.00` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 21,450.00 USD | 0.00 USD | 19,370.00 USD |
| `7D` | `4146.40` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 92,210.00 USD | 0.00 USD | 159,490.00 USD |
| `1D` | `4150.10` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 56,740.00 USD | 0.00 USD | 73,480.00 USD |
| `7D` | `4150.70` | 13,410,000.00 USD | 13,410,000.00 USD | 0.00 USD | 196,300.00 USD | 0.00 USD | 381,500.00 USD |
| `1D` | `4154.20` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 106,250.00 USD | 0.00 USD | 51,750.00 USD |
| `7D` | `4155.00` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 259,800.00 USD | 0.00 USD | 480,310.00 USD |
| `1D` | `4158.30` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 22,350.00 USD | 0.00 USD | 143,490.00 USD |
| `7D` | `4159.30` | 15,090,000.00 USD | 15,090,000.00 USD | 0.00 USD | 256,240.00 USD | 0.00 USD | 687,440.00 USD |
| `1D` | `4162.40` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 41,250.00 USD | 0.00 USD | 93,520.00 USD |
| `7D` | `4163.60` | 15,570,000.00 USD | 15,570,000.00 USD | 0.00 USD | 183,210.00 USD | 0.00 USD | 296,640.00 USD |
| `1D` | `4166.50` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 40,500.00 USD | 0.00 USD | 133,830.00 USD |
| `7D` | `4167.90` | 15,880,000.00 USD | 15,880,000.00 USD | 0.00 USD | 79,110.00 USD | 0.00 USD | 234,550.00 USD |
| `1D` | `4170.60` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 82,090.00 USD | 0.00 USD | 164,850.00 USD |
| `7D` | `4172.20` | 16,270,000.00 USD | 16,270,000.00 USD | 0.00 USD | 176,280.00 USD | 0.00 USD | 214,570.00 USD |
| `1D` | `4174.70` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 24,570.00 USD | 0.00 USD | 95,550.00 USD |
| `7D` | `4176.50` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 68,410.00 USD | 0.00 USD | 207,520.00 USD |
| `1D` | `4178.80` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 42,810.00 USD | 0.00 USD | 93,770.00 USD |
| `7D` | `4180.80` | 16,800,000.00 USD | 16,800,000.00 USD | 0.00 USD | 76,280.00 USD | 0.00 USD | 173,940.00 USD |
| `1D` | `4182.90` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 64,790.00 USD | 0.00 USD | 126,090.00 USD |
| `7D` | `4185.10` | 17,210,000.00 USD | 17,210,000.00 USD | 0.00 USD | 96,000.00 USD | 0.00 USD | 313,280.00 USD |
| `1D` | `4187.00` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 30,960.00 USD | 0.00 USD | 37,510.00 USD |
| `7D` | `4189.40` | 17,390,000.00 USD | 17,390,000.00 USD | 0.00 USD | 58,720.00 USD | 0.00 USD | 119,800.00 USD |
| `1D` | `4191.10` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 16,780.00 USD | 0.00 USD | 10,430.00 USD |
| `7D` | `4193.70` | 17,710,000.00 USD | 17,710,000.00 USD | 0.00 USD | 153,110.00 USD | 0.00 USD | 169,500.00 USD |
| `1D` | `4195.20` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD | 16,700.00 USD |
| `7D` | `4198.00` | 18,020,000.00 USD | 18,020,000.00 USD | 0.00 USD | 139,310.00 USD | 0.00 USD | 169,710.00 USD |
| `7D` | `4202.30` | 18,250,000.00 USD | 18,250,000.00 USD | 0.00 USD | 206,140.00 USD | 0.00 USD | 18,540.00 USD |
| `7D` | `4206.60` | 18,460,000.00 USD | 18,460,000.00 USD | 0.00 USD | 144,390.00 USD | 0.00 USD | 72,260.00 USD |
| `7D` | `4210.90` | 18,580,000.00 USD | 18,580,000.00 USD | 0.00 USD | 67,010.00 USD | 0.00 USD | 51,400.00 USD |
| `7D` | `4215.20` | 18,710,000.00 USD | 18,710,000.00 USD | 0.00 USD | 48,630.00 USD | 0.00 USD | 76,320.00 USD |
| `7D` | `4219.50` | 18,740,000.00 USD | 18,740,000.00 USD | 0.00 USD | 33,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4223.80` | 18,830,000.00 USD | 18,830,000.00 USD | 0.00 USD | 53,180.00 USD | 0.00 USD | 37,970.00 USD |
| `7D` | `4228.10` | 18,880,000.00 USD | 18,880,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 37,180.00 USD |
| `1D` | `4367.40` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,290.00 USD |
| `7D` | `4370.00` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,590.00 USD |
| `1D` | `4371.50` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,860.00 USD |
| `1D` | `4375.60` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 4,490.00 USD | 0.00 USD | 6,330.00 USD |
| `7D` | `4378.60` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4379.70` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4382.90` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 20,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4387.20` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 28,590.00 USD | 0.00 USD | 23,550.00 USD |
| `1D` | `4387.90` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 18,340.00 USD | 0.00 USD | 11,470.00 USD |
| `7D` | `4391.50` | 19,160,000.00 USD | 19,160,000.00 USD | 0.00 USD | 61,340.00 USD | 0.00 USD | 123,490.00 USD |
| `1D` | `4392.00` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 32,390.00 USD | 0.00 USD | 31,010.00 USD |
| `7D` | `4395.80` | 19,410,000.00 USD | 19,410,000.00 USD | 0.00 USD | 80,970.00 USD | 0.00 USD | 169,450.00 USD |
| `1D` | `4396.10` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 10,030.00 USD | 0.00 USD | 46,770.00 USD |
| `1D` | `4399.30` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 5,120.00 USD | 0.00 USD | 9,600.00 USD |
| `7D` | `4400.10` | 19,690,000.00 USD | 19,690,000.00 USD | 0.00 USD | 67,080.00 USD | 0.00 USD | 213,790.00 USD |
| `7D` | `4404.40` | 19,780,000.00 USD | 19,780,000.00 USD | 0.00 USD | 29,720.00 USD | 0.00 USD | 56,620.00 USD |
| `7D` | `4408.70` | 19,850,000.00 USD | 19,850,000.00 USD | 0.00 USD | 14,260.00 USD | 0.00 USD | 55,780.00 USD |
| `7D` | `4413.00` | 19,940,000.00 USD | 19,940,000.00 USD | 0.00 USD | 52,340.00 USD | 0.00 USD | 40,830.00 USD |
| `7D` | `4417.30` | 20,000,000.00 USD | 20,000,000.00 USD | 0.00 USD | 13,590.00 USD | 0.00 USD | 46,340.00 USD |
| `7D` | `4419.80` | 20,010,000.00 USD | 20,010,000.00 USD | 0.00 USD | 7,320.00 USD | 0.00 USD | 2,870.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `871.81M` | Total OI Tokens: `218,920.6 XAUT`
  * 1h OI Change: `+0.63%` | 4h OI Change: `+7.67%` | 24h OI Change: `-1.04%`
  * Exchange Breakdown: Binance=`60.55M` | Bybit=`142.38M` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.24K` | Last 24h: `33.89K` | Last 3d: `98.38K` | Last 7d: `284.70K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0027%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0016%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `0.0012%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0069%` | **USDT Bitget** | `0.0050%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XAUT` | `40.36%` | `59.64%` | `0.68` | 1,950,000.00 USD |
| `15M` | `Binance` | `50.68%` | `49.32%` | `1.03` | 659,840.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 358,330.00 USD |
| `15M` | `Bybit` | `22.27%` | `77.73%` | `0.29` | 116,160.00 USD |
| `15M` | `KuCoin` | `33.94%` | `66.06%` | `0.51` | 39,940.00 USD |
| `15M` | `Gate` | `59.56%` | `40.44%` | `1.47` | 108,530.00 USD |
| `15M` | `Bitget` | `49.66%` | `50.34%` | `0.99` | 177,440.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 85,910.00 USD |
| `15M` | `MEXC` | `25.57%` | `74.43%` | `0.34` | 150,190.00 USD |
| `15M` | `Bitunix` | `56.32%` | `43.68%` | `1.29` | 51,050.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 16,410.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `70.2%` | `29.8%` | `2.36` | 31,040.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 923.92 USD |
| `15M` | `WhiteBIT` | `21.63%` | `78.37%` | `0.28` | 116,250.00 USD |
| `15M` | `HTX` | `70.68%` | `29.32%` | `2.41` | 19.96 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `99.24%` | `0.76%` | `130.58` | 9,310.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 38.59 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 30,170.00 USD |
| `15M` | `Whale Positions` | `50.68%` | `49.32%` | `1.03` | 659,840.00 USD |
| `15M` | `Global Accounts` | `40.36%` | `59.64%` | `0.68` | 1,950,000.00 USD |
| `1H` | `XAUT` | `52.70%` | `47.30%` | `1.11` | 3,590,000.00 USD |
| `1H` | `Binance` | `50.8%` | `49.2%` | `1.03` | 1,140,000.00 USD |
| `1H` | `OKX` | `65.61%` | `34.39%` | `1.91` | 462,150.00 USD |
| `1H` | `Bybit` | `61.37%` | `38.63%` | `1.59` | 310,060.00 USD |
| `1H` | `KuCoin` | `51.05%` | `48.95%` | `1.04` | 212,770.00 USD |
| `1H` | `Gate` | `37.04%` | `62.96%` | `0.59` | 66,240.00 USD |
| `1H` | `Bitget` | `49.17%` | `50.83%` | `0.97` | 81,330.00 USD |
| `1H` | `BingX` | `47.48%` | `52.52%` | `0.90` | 153,800.00 USD |
| `1H` | `MEXC` | `53.14%` | `46.86%` | `1.13` | 155,470.00 USD |
| `1H` | `Bitunix` | `60.14%` | `39.86%` | `1.51` | 34,350.00 USD |
| `1H` | `Hyperliquid` | `36.99%` | `63.01%` | `0.59` | 58,700.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.89%` | `45.11%` | `1.22` | 588,740.00 USD |
| `1H` | `Crypto.com` | `7.7%` | `92.3%` | `0.08` | 16.01 USD |
| `1H` | `WhiteBIT` | `36.6%` | `63.4%` | `0.58` | 225,280.00 USD |
| `1H` | `HTX` | `9.5%` | `90.5%` | `0.10` | 151.30 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0.21%` | `99.79%` | `0.00` | 8,850.00 USD |
| `1H` | `Aster` | `9.6%` | `90.4%` | `0.11` | 732.67 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `46.77%` | `53.23%` | `0.88` | 96,780.00 USD |
| `1H` | `Whale Positions` | `50.8%` | `49.2%` | `1.03` | 1,140,000.00 USD |
| `1H` | `Global Accounts` | `52.70%` | `47.30%` | `1.11` | 3,590,000.00 USD |
| `4H` | `XAUT` | `47.91%` | `52.09%` | `0.92` | 41,820,000.00 USD |
| `4H` | `Binance` | `50.14%` | `49.86%` | `1.01` | 15,700,000.00 USD |
| `4H` | `OKX` | `55.13%` | `44.87%` | `1.23` | 6,080,000.00 USD |
| `4H` | `Bybit` | `51.26%` | `48.74%` | `1.05` | 4,670,000.00 USD |
| `4H` | `KuCoin` | `50.66%` | `49.34%` | `1.03` | 717,890.00 USD |
| `4H` | `Gate` | `56.2%` | `43.8%` | `1.28` | 1,350,000.00 USD |
| `4H` | `Bitget` | `47.89%` | `52.11%` | `0.92` | 2,630,000.00 USD |
| `4H` | `BingX` | `23.87%` | `76.13%` | `0.31` | 3,060,000.00 USD |
| `4H` | `MEXC` | `46.77%` | `53.23%` | `0.88` | 2,870,000.00 USD |
| `4H` | `Bitunix` | `37.52%` | `62.48%` | `0.60` | 608,370.00 USD |
| `4H` | `Hyperliquid` | `53.99%` | `46.01%` | `1.17` | 600,740.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.07%` | `49.93%` | `1.00` | 1,510,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 25,620.00 USD |
| `4H` | `WhiteBIT` | `59.57%` | `40.43%` | `1.47` | 1,650,000.00 USD |
| `4H` | `HTX` | `53.88%` | `46.12%` | `1.17` | 13,820.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `59.51%` | `40.49%` | `1.47` | 96,190.00 USD |
| `4H` | `Aster` | `51.37%` | `48.63%` | `1.06` | 45,060.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.24%` | `47.76%` | `1.09` | 184,730.00 USD |
| `4H` | `Whale Positions` | `50.14%` | `49.86%` | `1.01` | 15,700,000.00 USD |
| `4H` | `Global Accounts` | `47.91%` | `52.09%` | `0.92` | 41,820,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `3996.45` | `3997.10` | `3996.45` | `3999.45` | `3992.85` | 36,108,856.13 USD | 13,282,206.51 USD | 22,826,649.62 USD | -9,544,443.10 USD | `-26.43%` | `1B / 5S` |
| `0:00 UTC` | `3997.05` | `3997.44` | `3997.05` | `3999.75` | `3995.25` | 19,570,728.76 USD | 11,961,064.45 USD | 7,609,664.31 USD | 4,351,400.15 USD | `+22.23%` | `5B / 0S` |
| `5:00 UTC` | `4006.95` | `4004.53` | `4006.95` | `4008.45` | `3997.95` | 44,001,963.37 USD | 19,638,518.84 USD | 24,363,444.53 USD | -4,724,925.70 USD | `-10.74%` | `4B / 1S` |
| `0:00 UTC` | `4006.95` | `4003.87` | `4006.95` | `4007.55` | `3999.75` | 22,763,119.63 USD | 8,502,990.90 USD | 14,260,128.73 USD | -5,757,137.84 USD | `-25.29%` | `1B / 8S` |
| `5:00 UTC` | `3999.45` | `4001.01` | `3999.45` | `4004.25` | `3999.15` | 12,529,034.87 USD | 5,499,093.98 USD | 7,029,940.89 USD | -1,530,846.92 USD | `-12.22%` | `0B / 0S` |
| `0:00 UTC` | `4000.35` | `3999.56` | `4000.35` | `4001.55` | `3997.95` | 10,610,433.25 USD | 4,382,210.73 USD | 6,228,222.52 USD | -1,846,011.79 USD | `-17.40%` | `0B / 0S` |
| `5:00 UTC` | `4000.95` | `3999.70` | `4000.95` | `4001.85` | `3996.45` | 14,656,052.45 USD | 7,151,824.61 USD | 7,504,227.84 USD | -352,403.23 USD | `-2.40%` | `0B / 1S` |
| `0:00 UTC` | `3997.95` | `3996.26` | `3997.95` | `4000.95` | `3991.65` | 20,329,795.57 USD | 9,073,400.57 USD | 11,256,395.00 USD | -2,182,994.43 USD | `-10.74%` | `1B / 8S` |
| `5:00 UTC` | `3992.25` | `3992.57` | `3992.25` | `3995.85` | `3989.55` | 14,090,225.56 USD | 5,930,414.16 USD | 8,159,811.40 USD | -2,229,397.23 USD | `-15.82%` | `1B / 5S` |
| `0:00 UTC` | `3991.35` | `3991.01` | `3991.35` | `3992.85` | `3989.55` | 8,522,655.83 USD | 5,037,905.45 USD | 3,484,750.38 USD | 1,553,155.07 USD | `+18.22%` | `3B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:04` | `Volume 5.0K XAU` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `4045.20` | 1,000.00 USD | 0.00 USD |
| `10-28 17:48` | `Volume 5.0K XAU` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `4068.50` | 2,200.00 USD | 0.00 USD |
| `10-28 16:57` | `Volume 5.0K XAU` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4052.80` | 0.00 USD | 0.00 USD |
| `10-28 13:46` | `Volume 5.0K XAU` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4059.60` | 0.00 USD | 0.00 USD |
| `10-28 13:46` | `Volume 5.0K XAU` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `4059.60` | 0.00 USD | 0.00 USD |
| `10-28 10:56` | `Volume 5.0K XAU` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4041.20` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD (XAUUSD.pi) Metal Auction: ROTATION | `4045.64` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_EUR (XAUEUR.pi) Metal Auction: ROTA | `3633.06` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_AUD (XAUAUD.pi) Metal Auction: ROTA | `5747.46` | 0.00 USD | 0.00 USD |
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD_GBP (XAUGBP.pi) Metal Auction: ROTA | `3040.99` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 259,020.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `15m` | 485,070.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `30m` | 45,940.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `1h` | -139,090.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,210,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -4,330,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -3,210,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -3,820,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,880,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `24h` | -4,670,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -63,840,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -184,540,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+259.02K` | 15m=`+485.07K` | 1h=`-139.09K` | 24h=`-4.67M`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * `2026-10-30 15:49:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:45 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3982.43` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3972.91` (Risk Distance: `9.52` pts)
  * +2.5R Take Profit: `4006.22`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4007.50` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4017.02` (Risk Distance: `9.52` pts)
  * +2.5R Take Profit: `3983.71`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4013.48`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
