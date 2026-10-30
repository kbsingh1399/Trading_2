# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 16:18:38 IST` (`2026-10-30 10:48:38 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3981.59` | **Live Ask Quote**: `3981.67` | **Mid Price**: `3981.63`
- **Spread Points**: `8.00` | **Spread BPS**: `0.20 bps` (Charter Threshold: `5.00 bps`)
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
| `47` | `0x5b5d...c060` | `SHORT` | 25,845,724.08 USD | `6,489.82` | `4185.46` | `3982.30` | `27363.89` | 1,317,226.93 USD | `+5.10%` | `4X Cross` |
| `49` | `0x4692...164f` | `SHORT` | 25,111,204.05 USD | `6,305.86` | `4127.28` | `3982.30` | `14237.85` | 914,900.73 USD | `+3.64%` | `5X Cross` |
| `63` | `0xb83d...6e36` | `SHORT` | 23,376,874.36 USD | `5,869.90` | `4228.86` | `3982.30` | `22368.49` | 1,446,147.57 USD | `+6.19%` | `5X Cross` |
| `100` | `0xec0b...b078` | `LONG` | 19,230,638.84 USD | `4,828.91` | `4157.43` | `3982.30` | `2261.41` | -845,243.48 USD | `-4.40%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,120,825.12 USD | `3,545.72` | `4127.81` | `3982.30` | `664.87` | -515,257.07 USD | `-3.65%` | `3X Cross` |
| `158` | `0x7a6d...f79c` | `SHORT` | 13,015,659.07 USD | `3,268.21` | `4228.94` | `3982.30` | `4383.12` | 805,420.06 USD | `+6.19%` | `25X Cross` |
| `181` | `0xa742...e390` | `SHORT` | 11,151,088.41 USD | `2,800.02` | `4364.62` | `3982.30` | `4212.84` | 1,069,955.73 USD | `+9.60%` | `20X Cross` |
| `260` | `0x41e5...0825` | `SHORT` | 8,761,500.00 USD | `2,200.00` | `4112.20` | `3982.30` | `4287.19` | 285,354.59 USD | `+3.26%` | `20X Cross` |
| `261` | `0x3678...b209` | `LONG` | 8,761,060.00 USD | `2,200.00` | `4176.09` | `3982.30` | `2634.35` | -426,359.30 USD | `-4.87%` | `25X Cross` |
| `296` | `0xacb6...efbd` | `SHORT` | 7,866,709.90 USD | `1,975.37` | `4048.55` | `3982.30` | `6678.60` | 130,681.81 USD | `+1.66%` | `6X Cross` |
| `362` | `0xc26c...b8f4` | `LONG` | 6,292,158.04 USD | `1,579.95` | `4075.62` | `3982.30` | `0.000000` | -147,138.93 USD | `-2.34%` | `1X Cross` |
| `559` | `0x63da...8add` | `LONG` | 3,982,500.00 USD | `1,000.00` | `4021.46` | `3982.30` | `3564.73` | -38,960.96 USD | `-0.98%` | `25X Cross` |
| `570` | `0xf3dc...1672` | `LONG` | 3,919,661.21 USD | `984.27` | `4018.39` | `3982.30` | `2843.85` | -35,525.49 USD | `-0.91%` | `20X Cross` |
| `586` | `0x9aa5...58af` | `LONG` | 3,819,539.75 USD | `959.11` | `4279.98` | `3982.30` | `0.000000` | -285,411.21 USD | `-7.47%` | `20X Cross` |
| `672` | `0x4a20...3c26` | `LONG` | 3,334,776.83 USD | `837.40` | `4599.73` | `3982.30` | `0.000000` | -517,043.56 USD | `-15.50%` | `20X Cross` |
| `780` | `0x9c06...0560` | `LONG` | 2,895,085.54 USD | `726.95` | `4002.36` | `3982.30` | `0.000000` | -14,443.71 USD | `-0.50%` | `25X Cross` |
| `823` | `0x0fac...7a0a` | `LONG` | 2,733,926.51 USD | `686.49` | `4290.34` | `3982.30` | `1266.50` | -211,332.19 USD | `-7.73%` | `25X Cross` |
| `854` | `0x354b...6425` | `LONG` | 2,637,042.31 USD | `662.21` | `4004.29` | `3982.30` | `0.000000` | -14,634.40 USD | `-0.55%` | `10X Cross` |
| `900` | `0x625e...a354` | `SHORT` | 2,469,150.00 USD | `620.00` | `4122.81` | `3982.30` | `4279.60` | 86,997.03 USD | `+3.52%` | `20X Cross` |
| `928` | `0xeae3...e8ad` | `SHORT` | 2,389,380.00 USD | `600.00` | `4104.77` | `3982.30` | `4268.68` | 73,485.11 USD | `+3.08%` | `20X Cross` |
| `931` | `0xf285...fa82` | `LONG` | 2,381,896.94 USD | `598.11` | `4146.45` | `3982.30` | `3891.87` | -98,122.62 USD | `-4.12%` | `25X Cross` |
| `934` | `0xd8c5...99b0` | `SHORT` | 2,366,899.52 USD | `594.35` | `4175.35` | `3982.30` | `35349.26` | 114,744.51 USD | `+4.85%` | `4X Cross` |
| `940` | `0x12f7...8750` | `LONG` | 2,332,194.61 USD | `585.61` | `4082.77` | `3982.30` | `2758.78` | -58,722.37 USD | `-2.52%` | `10X Cross` |
| `988` | `0x413c...886c` | `LONG` | 2,227,923.03 USD | `559.47` | `4007.05` | `3982.30` | `0.000000` | -13,904.18 USD | `-0.62%` | `2X Cross` |
| `1092` | `0x61ce...a62b` | `SHORT` | 1,981,208.19 USD | `497.50` | `4071.66` | `3982.30` | `4717.11` | 44,460.60 USD | `+2.24%` | `20X Cross` |
| `1173` | `0x2edd...8179` | `LONG` | 1,868,475.57 USD | `468.69` | `4164.68` | `3986.60` | `0.000000` | -83,463.50 USD | `-4.47%` | `10X Cross` |
| `1217` | `0xead5...69f2` | `LONG` | 1,807,149.00 USD | `453.78` | `4220.88` | `3982.30` | `3539.57` | -108,219.06 USD | `-5.99%` | `5X Isolated` |
| `1272` | `0x7a6d...f79c` | `SHORT` | 1,708,418.29 USD | `428.38` | `4136.09` | `3986.60` | `5339.04` | 63,396.72 USD | `+3.71%` | `10X Cross` |
| `1298` | `0x46fc...1195` | `LONG` | 1,662,994.60 USD | `417.61` | `4051.00` | `3982.30` | `2266.73` | -28,734.78 USD | `-1.73%` | `20X Cross` |
| `1342` | `0x6d15...d374` | `LONG` | 1,593,000.00 USD | `400.00` | `4068.25` | `3982.30` | `3842.44` | -34,300.00 USD | `-2.15%` | `25X Cross` |
| `1343` | `0xee02...309d` | `SHORT` | 1,593,000.00 USD | `400.00` | `4438.84` | `3982.30` | `4202.98` | 182,538.60 USD | `+11.46%` | `25X Isolated` |
| `1373` | `0x51f6...2b39` | `LONG` | 1,560,635.02 USD | `391.48` | `4228.25` | `3986.60` | `570.75` | -94,640.67 USD | `-6.06%` | `10X Cross` |
| `1391` | `0x02a7...fe9f` | `SHORT` | 1,553,175.00 USD | `390.00` | `4055.02` | `3982.30` | `4307.31` | 28,284.25 USD | `+1.82%` | `25X Cross` |
| `1432` | `0x7e77...b8d2` | `SHORT` | 1,513,274.00 USD | `380.00` | `4131.92` | `3982.30` | `4294.11` | 56,855.64 USD | `+3.76%` | `20X Cross` |
| `1448` | `0x72c2...9b37` | `LONG` | 1,485,920.78 USD | `373.13` | `4000.98` | `3982.30` | `3778.67` | -6,972.74 USD | `-0.47%` | `13X Isolated` |
| `1465` | `0x781e...96b7` | `SHORT` | 1,458,437.11 USD | `365.84` | `4358.71` | `3986.60` | `12756.62` | 136,170.54 USD | `+9.34%` | `10X Cross` |
| `1494` | `0xaa44...b844` | `LONG` | 1,433,628.00 USD | `360.00` | `4043.10` | `3982.30` | `3225.88` | -21,889.63 USD | `-1.53%` | `7X Cross` |
| `1606` | `0xa41f...d50a` | `LONG` | 1,310,058.67 USD | `328.96` | `4468.89` | `3982.30` | `3802.79` | -160,039.18 USD | `-12.22%` | `15X Cross` |
| `1654` | `0xbf5a...88ba` | `SHORT` | 1,265,028.87 USD | `317.65` | `4091.80` | `3982.30` | `9952.77` | 34,754.16 USD | `+2.75%` | `20X Cross` |
| `1698` | `0xff31...ff6c` | `SHORT` | 1,234,513.00 USD | `310.00` | `4372.43` | `3982.30` | `4789.78` | 120,942.38 USD | `+9.80%` | `10X Isolated` |
| `1724` | `0xada6...6f88` | `LONG` | 1,208,494.64 USD | `303.47` | `4166.46` | `3982.30` | `1803.31` | -55,887.81 USD | `-4.62%` | `5X Cross` |
| `1888` | `0x50e2...d770` | `LONG` | 1,076,684.10 USD | `270.37` | `4243.58` | `3982.30` | `2562.72` | -70,642.36 USD | `-6.56%` | `20X Cross` |
| `1903` | `0x4c92...4f17` | `SHORT` | 1,062,214.39 USD | `266.72` | `4260.98` | `3982.30` | `6484.28` | 74,277.85 USD | `+6.99%` | `20X Cross` |
| `1970` | `0xd346...c4f3` | `LONG` | 1,016,229.66 USD | `255.17` | `4188.66` | `3982.30` | `3311.05` | -52,606.85 USD | `-5.18%` | `5X Isolated` |

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
  * 24H Horizon: Short MP=`4096.30` (Vol: 350,100.00 USD, Dist: `+2.84%`) | Long MP=`3937.38` (Vol: 356,200.00 USD, Dist: `--1.15%`)
  * 48H Horizon: Short MP=`4111.27` (Vol: 328,300.00 USD, Dist: `+3.22%`) | Long MP=`3936.60` (Vol: 378,100.00 USD, Dist: `--1.17%`)
  * 3D Horizon: Short MP=`4111.27` (Vol: 367,600.00 USD, Dist: `+3.22%`) | Long MP=`3949.08` (Vol: 404,600.00 USD, Dist: `--0.85%`)
  * 7D Horizon: Short MP=`4086.31` (Vol: 853,900.00 USD, Dist: `+2.59%`) | Long MP=`3927.24` (Vol: 1,100,000.00 USD, Dist: `--1.40%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3584.50` | 15,110,000.00 USD | 15,110,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3588.80` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3590.30` | 5,620,000.00 USD | 5,620,000.00 USD | 2,640.00 USD | 0.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3593.10` | 15,080,000.00 USD | 15,080,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3594.40` | 5,610,000.00 USD | 5,610,000.00 USD | 32,530.00 USD | 0.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3597.40` | 15,070,000.00 USD | 15,070,000.00 USD | 92,800.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3598.50` | 5,550,000.00 USD | 5,550,000.00 USD | 14,150.00 USD | 0.00 USD | 13,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3601.70` | 14,960,000.00 USD | 14,960,000.00 USD | 175,610.00 USD | 0.00 USD | 67,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3602.60` | 5,530,000.00 USD | 5,530,000.00 USD | 30,030.00 USD | 0.00 USD | 51,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3606.00` | 14,720,000.00 USD | 14,720,000.00 USD | 134,320.00 USD | 0.00 USD | 53,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3606.70` | 5,440,000.00 USD | 5,440,000.00 USD | 55,240.00 USD | 0.00 USD | 15,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3610.30` | 14,530,000.00 USD | 14,530,000.00 USD | 83,580.00 USD | 0.00 USD | 21,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3610.80` | 5,370,000.00 USD | 5,370,000.00 USD | 19,350.00 USD | 0.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3614.60` | 14,430,000.00 USD | 14,430,000.00 USD | 89,070.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3614.90` | 5,350,000.00 USD | 5,350,000.00 USD | 37,500.00 USD | 0.00 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3618.90` | 14,320,000.00 USD | 14,320,000.00 USD | 40,780.00 USD | 0.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3619.00` | 5,300,000.00 USD | 5,300,000.00 USD | 37,960.00 USD | 0.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.10` | 5,260,000.00 USD | 5,260,000.00 USD | 61,150.00 USD | 0.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.20` | 14,270,000.00 USD | 14,270,000.00 USD | 59,230.00 USD | 0.00 USD | 24,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.20` | 5,180,000.00 USD | 5,180,000.00 USD | 23,440.00 USD | 0.00 USD | 4,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3627.50` | 14,190,000.00 USD | 14,190,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.30` | 5,160,000.00 USD | 5,160,000.00 USD | 11,930.00 USD | 0.00 USD | 2,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3631.80` | 14,080,000.00 USD | 14,080,000.00 USD | 60,720.00 USD | 0.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.40` | 5,140,000.00 USD | 5,140,000.00 USD | 9,410.00 USD | 0.00 USD | 204.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.10` | 14,020,000.00 USD | 14,020,000.00 USD | 20,410.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.50` | 5,130,000.00 USD | 5,130,000.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.40` | 13,990,000.00 USD | 13,990,000.00 USD | 55,830.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.70` | 13,930,000.00 USD | 13,930,000.00 USD | 17,720.00 USD | 0.00 USD | 11,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.00` | 13,900,000.00 USD | 13,900,000.00 USD | 24,860.00 USD | 0.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 13,870,000.00 USD | 13,870,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.60` | 13,840,000.00 USD | 13,840,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.90` | 13,800,000.00 USD | 13,800,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3666.20` | 13,780,000.00 USD | 13,780,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3819.90` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3824.00` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3825.30` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3828.10` | 5,110,000.00 USD | 5,110,000.00 USD | 6,610.00 USD | 0.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.60` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3832.20` | 5,090,000.00 USD | 5,090,000.00 USD | 42,920.00 USD | 0.00 USD | 67,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 13,660,000.00 USD | 13,660,000.00 USD | 86,270.00 USD | 0.00 USD | 34,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3836.30` | 4,980,000.00 USD | 4,980,000.00 USD | 76,070.00 USD | 0.00 USD | 69,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.20` | 13,540,000.00 USD | 13,540,000.00 USD | 271,140.00 USD | 0.00 USD | 60,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3840.40` | 4,830,000.00 USD | 4,830,000.00 USD | 87,190.00 USD | 0.00 USD | 82,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.50` | 13,210,000.00 USD | 13,210,000.00 USD | 557,810.00 USD | 0.00 USD | 224,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3844.50` | 4,660,000.00 USD | 4,660,000.00 USD | 180,220.00 USD | 0.00 USD | 136,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.80` | 12,430,000.00 USD | 12,430,000.00 USD | 535,820.00 USD | 0.00 USD | 157,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3848.60` | 4,350,000.00 USD | 4,350,000.00 USD | 38,210.00 USD | 0.00 USD | 20,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3851.10` | 11,730,000.00 USD | 11,730,000.00 USD | 231,930.00 USD | 0.00 USD | 79,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.70` | 4,290,000.00 USD | 4,290,000.00 USD | 85,690.00 USD | 0.00 USD | 39,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3855.40` | 11,420,000.00 USD | 11,420,000.00 USD | 219,990.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.80` | 4,160,000.00 USD | 4,160,000.00 USD | 96,830.00 USD | 0.00 USD | 23,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.70` | 11,150,000.00 USD | 11,150,000.00 USD | 174,170.00 USD | 0.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.90` | 4,040,000.00 USD | 4,040,000.00 USD | 151,640.00 USD | 0.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.00` | 10,950,000.00 USD | 10,950,000.00 USD | 204,130.00 USD | 0.00 USD | 73,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.00` | 3,850,000.00 USD | 3,850,000.00 USD | 203,200.00 USD | 0.00 USD | 23,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3868.30` | 10,680,000.00 USD | 10,680,000.00 USD | 298,110.00 USD | 0.00 USD | 32,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.10` | 3,630,000.00 USD | 3,630,000.00 USD | 103,230.00 USD | 0.00 USD | 13,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3872.60` | 10,350,000.00 USD | 10,350,000.00 USD | 220,790.00 USD | 0.00 USD | 43,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.20` | 3,510,000.00 USD | 3,510,000.00 USD | 42,320.00 USD | 0.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3876.90` | 10,080,000.00 USD | 10,080,000.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3877.30` | 3,460,000.00 USD | 3,460,000.00 USD | 33,210.00 USD | 0.00 USD | 824.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3881.20` | 9,910,000.00 USD | 9,910,000.00 USD | 116,920.00 USD | 0.00 USD | 31,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3881.40` | 3,430,000.00 USD | 3,430,000.00 USD | 5,280.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3885.50` | 9,770,000.00 USD | 9,770,000.00 USD | 124,650.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3889.80` | 9,620,000.00 USD | 9,620,000.00 USD | 85,430.00 USD | 0.00 USD | 25,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3894.10` | 9,500,000.00 USD | 9,500,000.00 USD | 126,480.00 USD | 0.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3898.40` | 9,370,000.00 USD | 9,370,000.00 USD | 132,740.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.90` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 48,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3902.70` | 9,230,000.00 USD | 9,230,000.00 USD | 17,060.00 USD | 0.00 USD | 72,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3906.00` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.00` | 9,140,000.00 USD | 9,140,000.00 USD | 56,630.00 USD | 0.00 USD | 101,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3910.10` | 3,350,000.00 USD | 3,350,000.00 USD | 35,540.00 USD | 0.00 USD | 76,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3911.30` | 8,980,000.00 USD | 8,980,000.00 USD | 51,010.00 USD | 0.00 USD | 81,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3914.20` | 3,230,000.00 USD | 3,230,000.00 USD | 163,060.00 USD | 0.00 USD | 86,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3915.60` | 8,850,000.00 USD | 8,850,000.00 USD | 287,340.00 USD | 0.00 USD | 143,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3918.30` | 2,980,000.00 USD | 2,980,000.00 USD | 119,800.00 USD | 0.00 USD | 139,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3919.90` | 8,420,000.00 USD | 8,420,000.00 USD | 674,750.00 USD | 0.00 USD | 199,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3922.40` | 2,730,000.00 USD | 2,730,000.00 USD | 206,480.00 USD | 0.00 USD | 238,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3924.20` | 7,540,000.00 USD | 7,540,000.00 USD | 1,200,000.00 USD | 0.00 USD | 464,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3926.50` | 2,280,000.00 USD | 2,280,000.00 USD | 311,180.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3928.50` | 5,880,000.00 USD | 5,880,000.00 USD | 913,310.00 USD | 0.00 USD | 195,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3930.60` | 1,780,000.00 USD | 1,780,000.00 USD | 56,230.00 USD | 0.00 USD | 63,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3932.80` | 4,770,000.00 USD | 4,770,000.00 USD | 380,870.00 USD | 0.00 USD | 128,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.70` | 1,660,000.00 USD | 1,660,000.00 USD | 221,570.00 USD | 0.00 USD | 60,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3937.10` | 4,260,000.00 USD | 4,260,000.00 USD | 466,400.00 USD | 0.00 USD | 74,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.80` | 1,370,000.00 USD | 1,370,000.00 USD | 215,190.00 USD | 0.00 USD | 38,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3941.40` | 3,720,000.00 USD | 3,720,000.00 USD | 287,460.00 USD | 0.00 USD | 104,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.90` | 1,120,000.00 USD | 1,120,000.00 USD | 315,460.00 USD | 0.00 USD | 64,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3945.70` | 3,330,000.00 USD | 3,330,000.00 USD | 468,070.00 USD | 0.00 USD | 118,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.00` | 739,960.00 USD | 739,960.00 USD | 331,100.00 USD | 0.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.00` | 2,740,000.00 USD | 2,740,000.00 USD | 529,640.00 USD | 0.00 USD | 78,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.10` | 362,710.00 USD | 362,710.00 USD | 204,640.00 USD | 0.00 USD | 15,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3954.30` | 2,130,000.00 USD | 2,130,000.00 USD | 437,760.00 USD | 0.00 USD | 53,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.20` | 142,100.00 USD | 142,100.00 USD | 53,910.00 USD | 0.00 USD | 14,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3958.60` | 1,640,000.00 USD | 1,640,000.00 USD | 275,800.00 USD | 0.00 USD | 38,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.30` | 73,340.00 USD | 73,340.00 USD | 71,090.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3962.90` | 1,330,000.00 USD | 1,330,000.00 USD | 277,640.00 USD | 0.00 USD | 56,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.40` | 606.18 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3967.20` | 993,660.00 USD | 993,660.00 USD | 148,670.00 USD | 0.00 USD | 57,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3971.50` | 787,110.00 USD | 787,110.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3975.80` | 540,150.00 USD | 540,150.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.10` | 270,930.00 USD | 270,930.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3984.40` | 34,110.00 USD | 34,110.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `3988.70` | 76,450.00 USD | 76,450.00 USD | 76,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4061.80` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 48,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4061.80` | 137,390.00 USD | 137,390.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4065.90` | 73,370.00 USD | 73,370.00 USD | 0.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4070.00` | 185,850.00 USD | 185,850.00 USD | 35,540.00 USD | 0.00 USD | 76,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4070.40` | 339,670.00 USD | 339,670.00 USD | 34,460.00 USD | 0.00 USD | 167,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4074.10` | 435,700.00 USD | 435,700.00 USD | 163,060.00 USD | 0.00 USD | 86,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4074.70` | 621,660.00 USD | 621,660.00 USD | 138,080.00 USD | 0.00 USD | 143,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4078.20` | 686,150.00 USD | 686,150.00 USD | 111,440.00 USD | 0.00 USD | 139,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.00` | 1,560,000.00 USD | 1,560,000.00 USD | 773,860.00 USD | 0.00 USD | 167,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4082.30` | 1,090,000.00 USD | 1,090,000.00 USD | 165,530.00 USD | 0.00 USD | 233,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4083.30` | 3,060,000.00 USD | 3,060,000.00 USD | 1,110,000.00 USD | 0.00 USD | 384,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4086.40` | 1,640,000.00 USD | 1,640,000.00 USD | 360,500.00 USD | 0.00 USD | 199,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4087.60` | 4,170,000.00 USD | 4,170,000.00 USD | 844,290.00 USD | 0.00 USD | 266,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4090.50` | 1,730,000.00 USD | 1,730,000.00 USD | 40,700.00 USD | 0.00 USD | 43,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4091.90` | 4,830,000.00 USD | 4,830,000.00 USD | 514,970.00 USD | 0.00 USD | 144,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.60` | 2,030,000.00 USD | 2,030,000.00 USD | 230,830.00 USD | 0.00 USD | 68,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4096.20` | 5,240,000.00 USD | 5,240,000.00 USD | 310,220.00 USD | 0.00 USD | 100,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.70` | 2,250,000.00 USD | 2,250,000.00 USD | 176,660.00 USD | 0.00 USD | 45,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4100.50` | 5,700,000.00 USD | 5,700,000.00 USD | 415,790.00 USD | 0.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.80` | 2,580,000.00 USD | 2,580,000.00 USD | 265,980.00 USD | 0.00 USD | 63,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4104.80` | 6,200,000.00 USD | 6,200,000.00 USD | 367,480.00 USD | 0.00 USD | 134,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.90` | 3,020,000.00 USD | 3,020,000.00 USD | 393,950.00 USD | 0.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4109.10` | 6,810,000.00 USD | 6,810,000.00 USD | 537,000.00 USD | 0.00 USD | 76,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.00` | 3,240,000.00 USD | 3,240,000.00 USD | 199,430.00 USD | 0.00 USD | 23,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4113.40` | 7,310,000.00 USD | 7,310,000.00 USD | 434,270.00 USD | 0.00 USD | 63,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.10` | 3,340,000.00 USD | 3,340,000.00 USD | 84,640.00 USD | 0.00 USD | 16,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4117.70` | 7,650,000.00 USD | 7,650,000.00 USD | 288,910.00 USD | 0.00 USD | 49,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.20` | 3,410,000.00 USD | 3,410,000.00 USD | 66,420.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.00` | 7,960,000.00 USD | 7,960,000.00 USD | 272,900.00 USD | 0.00 USD | 32,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4123.30` | 3,420,000.00 USD | 3,420,000.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4126.30` | 8,280,000.00 USD | 8,280,000.00 USD | 252,890.00 USD | 0.00 USD | 70,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4130.60` | 8,470,000.00 USD | 8,470,000.00 USD | 143,990.00 USD | 0.00 USD | 48,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4134.90` | 8,750,000.00 USD | 8,750,000.00 USD | 240,010.00 USD | 0.00 USD | 35,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4139.20` | 8,950,000.00 USD | 8,950,000.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.70` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4143.50` | 9,200,000.00 USD | 9,200,000.00 USD | 199,160.00 USD | 0.00 USD | 42,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.80` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4147.80` | 9,350,000.00 USD | 9,350,000.00 USD | 59,830.00 USD | 0.00 USD | 91,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.90` | 3,460,000.00 USD | 3,460,000.00 USD | 6,610.00 USD | 0.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4152.00` | 3,580,000.00 USD | 3,580,000.00 USD | 49,590.00 USD | 0.00 USD | 67,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4152.10` | 9,550,000.00 USD | 9,550,000.00 USD | 133,610.00 USD | 0.00 USD | 71,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4156.10` | 3,720,000.00 USD | 3,720,000.00 USD | 69,390.00 USD | 0.00 USD | 69,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4156.40` | 9,850,000.00 USD | 9,850,000.00 USD | 243,560.00 USD | 0.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4160.20` | 3,860,000.00 USD | 3,860,000.00 USD | 61,360.00 USD | 0.00 USD | 77,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4160.70` | 10,300,000.00 USD | 10,300,000.00 USD | 336,690.00 USD | 0.00 USD | 111,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4164.30` | 4,170,000.00 USD | 4,170,000.00 USD | 184,330.00 USD | 0.00 USD | 123,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.00` | 11,100,000.00 USD | 11,100,000.00 USD | 584,890.00 USD | 0.00 USD | 215,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4168.40` | 4,260,000.00 USD | 4,260,000.00 USD | 59,930.00 USD | 0.00 USD | 33,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.30` | 11,580,000.00 USD | 11,580,000.00 USD | 384,920.00 USD | 0.00 USD | 91,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4172.50` | 4,350,000.00 USD | 4,350,000.00 USD | 56,270.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4173.60` | 11,820,000.00 USD | 11,820,000.00 USD | 181,290.00 USD | 0.00 USD | 60,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.60` | 4,490,000.00 USD | 4,490,000.00 USD | 106,840.00 USD | 0.00 USD | 33,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4177.90` | 12,070,000.00 USD | 12,070,000.00 USD | 209,170.00 USD | 0.00 USD | 37,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.70` | 4,600,000.00 USD | 4,600,000.00 USD | 99,350.00 USD | 0.00 USD | 14,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.20` | 12,270,000.00 USD | 12,270,000.00 USD | 167,760.00 USD | 0.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.80` | 4,770,000.00 USD | 4,770,000.00 USD | 133,000.00 USD | 0.00 USD | 30,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.50` | 12,530,000.00 USD | 12,530,000.00 USD | 188,450.00 USD | 0.00 USD | 68,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.90` | 4,960,000.00 USD | 4,960,000.00 USD | 171,730.00 USD | 0.00 USD | 21,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.80` | 12,840,000.00 USD | 12,840,000.00 USD | 285,320.00 USD | 0.00 USD | 24,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4193.00` | 5,060,000.00 USD | 5,060,000.00 USD | 91,710.00 USD | 0.00 USD | 7,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,080,000.00 USD | 13,080,000.00 USD | 205,140.00 USD | 0.00 USD | 38,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.10` | 5,090,000.00 USD | 5,090,000.00 USD | 26,950.00 USD | 0.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.40` | 13,210,000.00 USD | 13,210,000.00 USD | 101,170.00 USD | 0.00 USD | 24,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.20` | 5,120,000.00 USD | 5,120,000.00 USD | 30,260.00 USD | 0.00 USD | 824.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.70` | 13,390,000.00 USD | 13,390,000.00 USD | 164,070.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4205.30` | 5,130,000.00 USD | 5,130,000.00 USD | 5,280.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.00` | 13,510,000.00 USD | 13,510,000.00 USD | 82,850.00 USD | 0.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4212.30` | 13,620,000.00 USD | 13,620,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.60` | 13,730,000.00 USD | 13,730,000.00 USD | 104,620.00 USD | 0.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.90` | 13,860,000.00 USD | 13,860,000.00 USD | 120,590.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4225.20` | 13,940,000.00 USD | 13,940,000.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4229.50` | 13,990,000.00 USD | 13,990,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4233.80` | 14,040,000.00 USD | 14,040,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4238.10` | 14,050,000.00 USD | 14,050,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4377.50` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4380.00` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4381.60` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4385.70` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4388.60` | 14,080,000.00 USD | 14,080,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4389.80` | 5,160,000.00 USD | 5,160,000.00 USD | 7,110.00 USD | 0.00 USD | 11,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.90` | 14,110,000.00 USD | 14,110,000.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4393.90` | 5,210,000.00 USD | 5,210,000.00 USD | 28,070.00 USD | 0.00 USD | 19,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4397.20` | 14,220,000.00 USD | 14,220,000.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4398.00` | 5,230,000.00 USD | 5,230,000.00 USD | 14,150.00 USD | 0.00 USD | 10,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4401.50` | 14,430,000.00 USD | 14,430,000.00 USD | 143,560.00 USD | 0.00 USD | 62,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4402.10` | 5,290,000.00 USD | 5,290,000.00 USD | 21,490.00 USD | 0.00 USD | 35,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4404.30` | 5,360,000.00 USD | 5,360,000.00 USD | 49,090.00 USD | 0.00 USD | 20,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.80` | 14,590,000.00 USD | 14,590,000.00 USD | 116,280.00 USD | 0.00 USD | 48,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4410.10` | 14,730,000.00 USD | 14,730,000.00 USD | 112,800.00 USD | 0.00 USD | 22,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4414.40` | 14,780,000.00 USD | 14,780,000.00 USD | 36,920.00 USD | 0.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4418.70` | 14,860,000.00 USD | 14,860,000.00 USD | 66,780.00 USD | 0.00 USD | 11,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.00` | 14,900,000.00 USD | 14,900,000.00 USD | 31,340.00 USD | 0.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4427.10` | 14,970,000.00 USD | 14,970,000.00 USD | 59,230.00 USD | 0.00 USD | 17,850.00 USD | `Tier 1 CEX` |

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
| `7D` | `3584.80` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `7D` | `3589.10` | 15,070,000.00 USD | 0.00 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3589.20` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3593.30` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 15,290.00 USD | 0.00 USD | 22,620.00 USD |
| `7D` | `3593.40` | 15,050,000.00 USD | 0.00 USD | 15,050,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `3597.40` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 24,210.00 USD | 0.00 USD | 17,470.00 USD |
| `7D` | `3597.70` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 108,500.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `3601.50` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 28,670.00 USD | 0.00 USD | 35,250.00 USD |
| `7D` | `3602.00` | 14,910,000.00 USD | 0.00 USD | 14,910,000.00 USD | 173,930.00 USD | 0.00 USD | 75,620.00 USD |
| `1D` | `3605.60` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 52,600.00 USD | 0.00 USD | 33,420.00 USD |
| `7D` | `3606.30` | 14,660,000.00 USD | 0.00 USD | 14,660,000.00 USD | 152,940.00 USD | 0.00 USD | 46,290.00 USD |
| `1D` | `3609.70` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 17,150.00 USD | 0.00 USD | 5,060.00 USD |
| `7D` | `3610.60` | 14,460,000.00 USD | 0.00 USD | 14,460,000.00 USD | 72,480.00 USD | 0.00 USD | 20,480.00 USD |
| `1D` | `3613.80` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 34,710.00 USD | 0.00 USD | 9,070.00 USD |
| `7D` | `3614.90` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 76,990.00 USD | 0.00 USD | 16,470.00 USD |
| `1D` | `3617.90` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 37,170.00 USD | 0.00 USD | 5,710.00 USD |
| `7D` | `3619.20` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD |
| `1D` | `3622.00` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 37,530.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `3623.50` | 14,220,000.00 USD | 0.00 USD | 14,220,000.00 USD | 45,130.00 USD | 0.00 USD | 22,740.00 USD |
| `1D` | `3626.10` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 51,070.00 USD | 0.00 USD | 7,660.00 USD |
| `7D` | `3627.80` | 14,150,000.00 USD | 0.00 USD | 14,150,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD |
| `1D` | `3630.20` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 22,340.00 USD | 0.00 USD | 2,670.00 USD |
| `7D` | `3632.10` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 60,720.00 USD | 0.00 USD | 7,710.00 USD |
| `1D` | `3634.30` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 7,270.00 USD | 0.00 USD | 798.46 USD |
| `7D` | `3636.40` | 13,980,000.00 USD | 0.00 USD | 13,980,000.00 USD | 20,410.00 USD | 0.00 USD | 6,070.00 USD |
| `1D` | `3638.40` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 4,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3640.70` | 13,960,000.00 USD | 0.00 USD | 13,960,000.00 USD | 55,830.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3645.00` | 13,890,000.00 USD | 0.00 USD | 13,890,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `7D` | `3649.30` | 13,850,000.00 USD | 0.00 USD | 13,850,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `7D` | `3653.60` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3657.90` | 13,800,000.00 USD | 0.00 USD | 13,800,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3662.20` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3666.50` | 13,740,000.00 USD | 0.00 USD | 13,740,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3822.90` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 24,130.00 USD |
| `7D` | `3825.60` | 13,740,000.00 USD | 0.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD |
| `1D` | `3827.00` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 12,560.00 USD |
| `7D` | `3829.90` | 13,710,000.00 USD | 0.00 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD |
| `1D` | `3831.10` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 21,840.00 USD | 0.00 USD | 50,340.00 USD |
| `7D` | `3834.20` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 86,270.00 USD | 0.00 USD | 34,180.00 USD |
| `1D` | `3835.20` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 86,330.00 USD | 0.00 USD | 69,810.00 USD |
| `7D` | `3838.50` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 334,470.00 USD | 0.00 USD | 99,980.00 USD |
| `1D` | `3839.30` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 69,840.00 USD | 0.00 USD | 69,710.00 USD |
| `7D` | `3842.80` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 569,120.00 USD | 0.00 USD | 199,760.00 USD |
| `1D` | `3843.40` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 142,390.00 USD | 0.00 USD | 141,370.00 USD |
| `7D` | `3847.10` | 12,300,000.00 USD | 0.00 USD | 12,300,000.00 USD | 461,180.00 USD | 0.00 USD | 150,800.00 USD |
| `1D` | `3847.50` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 110,820.00 USD | 0.00 USD | 46,790.00 USD |
| `7D` | `3851.40` | 11,690,000.00 USD | 0.00 USD | 11,690,000.00 USD | 257,490.00 USD | 0.00 USD | 74,890.00 USD |
| `1D` | `3851.60` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 56,270.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `3855.70` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 106,840.00 USD | 0.00 USD | 33,380.00 USD |
| `7D` | `3855.70` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 221,360.00 USD | 0.00 USD | 47,670.00 USD |
| `1D` | `3859.80` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 131,940.00 USD | 0.00 USD | 21,900.00 USD |
| `7D` | `3860.00` | 11,090,000.00 USD | 0.00 USD | 11,090,000.00 USD | 147,250.00 USD | 0.00 USD | 28,510.00 USD |
| `1D` | `3863.90` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 156,710.00 USD | 0.00 USD | 31,120.00 USD |
| `7D` | `3864.30` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 232,560.00 USD | 0.00 USD | 75,710.00 USD |
| `1D` | `3868.00` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 147,350.00 USD | 0.00 USD | 17,660.00 USD |
| `7D` | `3868.60` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 285,320.00 USD | 0.00 USD | 26,240.00 USD |
| `1D` | `3872.10` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 74,090.00 USD | 0.00 USD | 8,910.00 USD |
| `7D` | `3872.90` | 10,290,000.00 USD | 0.00 USD | 10,290,000.00 USD | 221,120.00 USD | 0.00 USD | 41,690.00 USD |
| `1D` | `3876.20` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 24,510.00 USD | 0.00 USD | 2,310.00 USD |
| `7D` | `3877.20` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 153,170.00 USD | 0.00 USD | 23,330.00 USD |
| `1D` | `3880.30` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 17,360.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `3881.50` | 9,850,000.00 USD | 0.00 USD | 9,850,000.00 USD | 96,090.00 USD | 0.00 USD | 27,510.00 USD |
| `7D` | `3885.80` | 9,730,000.00 USD | 0.00 USD | 9,730,000.00 USD | 124,650.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `3890.10` | 9,580,000.00 USD | 0.00 USD | 9,580,000.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD |
| `7D` | `3894.40` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 126,480.00 USD | 0.00 USD | 10,240.00 USD |
| `7D` | `3898.70` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 132,740.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3900.80` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `3903.00` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 17,060.00 USD | 0.00 USD | 74,030.00 USD |
| `1D` | `3904.90` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD |
| `7D` | `3907.30` | 9,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 56,630.00 USD | 0.00 USD | 98,910.00 USD |
| `1D` | `3909.00` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 13,220.00 USD | 0.00 USD | 55,000.00 USD |
| `7D` | `3911.60` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 51,010.00 USD | 0.00 USD | 81,430.00 USD |
| `1D` | `3913.10` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 135,830.00 USD | 0.00 USD | 122,290.00 USD |
| `7D` | `3915.90` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 287,340.00 USD | 0.00 USD | 173,650.00 USD |
| `1D` | `3917.20` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 102,140.00 USD | 0.00 USD | 156,660.00 USD |
| `7D` | `3920.20` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 731,980.00 USD | 0.00 USD | 181,350.00 USD |
| `1D` | `3921.30` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 174,380.00 USD | 0.00 USD | 215,390.00 USD |
| `7D` | `3924.50` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 1,280,000.00 USD | 0.00 USD | 465,510.00 USD |
| `1D` | `3925.40` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 380,980.00 USD | 0.00 USD | 213,850.00 USD |
| `7D` | `3928.80` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 812,760.00 USD | 0.00 USD | 199,680.00 USD |
| `1D` | `3929.50` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 70,210.00 USD | 0.00 USD | 53,310.00 USD |
| `7D` | `3933.10` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 340,890.00 USD | 0.00 USD | 133,810.00 USD |
| `1D` | `3933.60` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 195,060.00 USD | 0.00 USD | 62,500.00 USD |
| `7D` | `3937.40` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 466,400.00 USD | 0.00 USD | 56,370.00 USD |
| `1D` | `3937.70` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 188,180.00 USD | 0.00 USD | 46,890.00 USD |
| `7D` | `3941.70` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 312,800.00 USD | 0.00 USD | 114,460.00 USD |
| `1D` | `3941.80` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 281,660.00 USD | 0.00 USD | 68,080.00 USD |
| `1D` | `3945.90` | 836,040.00 USD | 0.00 USD | 836,040.00 USD | 402,520.00 USD | 0.00 USD | 44,220.00 USD |
| `7D` | `3946.00` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 494,480.00 USD | 0.00 USD | 111,080.00 USD |
| `1D` | `3950.00` | 389,300.00 USD | 0.00 USD | 389,300.00 USD | 199,430.00 USD | 0.00 USD | 23,100.00 USD |
| `7D` | `3950.30` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 498,180.00 USD | 0.00 USD | 72,590.00 USD |
| `1D` | `3954.10` | 166,780.00 USD | 0.00 USD | 166,780.00 USD | 71,970.00 USD | 0.00 USD | 15,560.00 USD |
| `7D` | `3954.60` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 417,480.00 USD | 0.00 USD | 53,640.00 USD |
| `1D` | `3958.20` | 79,250.00 USD | 0.00 USD | 79,250.00 USD | 66,420.00 USD | 0.00 USD | 1,650.00 USD |
| `7D` | `3958.90` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 275,800.00 USD | 0.00 USD | 41,700.00 USD |
| `1D` | `3962.30` | 11,170.00 USD | 0.00 USD | 11,170.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `3963.20` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 303,170.00 USD | 0.00 USD | 57,060.00 USD |
| `7D` | `3967.50` | 930,280.00 USD | 0.00 USD | 930,280.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD |
| `7D` | `3971.80` | 753,000.00 USD | 0.00 USD | 753,000.00 USD | 218,900.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `3976.10` | 488,070.00 USD | 0.00 USD | 488,070.00 USD | 237,870.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `3980.40` | 236,810.00 USD | 0.00 USD | 236,810.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD |
| `7D` | `3983.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3984.70` | 59,830.00 USD | 59,830.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3985.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3989.00` | 110,560.00 USD | 110,560.00 USD | 0.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4060.70` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `4062.10` | 171,510.00 USD | 171,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD |
| `1D` | `4064.80` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD |
| `7D` | `4066.40` | 259,800.00 USD | 259,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 88,290.00 USD |
| `1D` | `4068.90` | 119,410.00 USD | 119,410.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `4070.70` | 373,790.00 USD | 373,790.00 USD | 0.00 USD | 34,460.00 USD | 0.00 USD | 79,530.00 USD |
| `1D` | `4073.00` | 374,600.00 USD | 374,600.00 USD | 0.00 USD | 135,830.00 USD | 0.00 USD | 119,370.00 USD |
| `7D` | `4075.00` | 655,770.00 USD | 655,770.00 USD | 0.00 USD | 138,080.00 USD | 0.00 USD | 143,900.00 USD |
| `1D` | `4077.10` | 637,510.00 USD | 637,510.00 USD | 0.00 USD | 102,140.00 USD | 0.00 USD | 160,770.00 USD |
| `7D` | `4079.30` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 793,160.00 USD | 0.00 USD | 181,320.00 USD |
| `1D` | `4081.20` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 174,380.00 USD | 0.00 USD | 195,070.00 USD |
| `7D` | `4083.60` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 427,200.00 USD |
| `1D` | `4085.30` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 371,270.00 USD | 0.00 USD | 219,480.00 USD |
| `7D` | `4087.90` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 819,620.00 USD | 0.00 USD | 209,710.00 USD |
| `1D` | `4089.40` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 65,600.00 USD | 0.00 USD | 39,630.00 USD |
| `7D` | `4092.20` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 535,480.00 USD | 0.00 USD | 149,790.00 USD |
| `1D` | `4093.50` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 171,390.00 USD | 0.00 USD | 76,210.00 USD |
| `7D` | `4096.50` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 394,180.00 USD | 0.00 USD | 95,350.00 USD |
| `1D` | `4097.60` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 193,650.00 USD | 0.00 USD | 47,210.00 USD |
| `7D` | `4100.80` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 322,520.00 USD | 0.00 USD | 42,790.00 USD |
| `1D` | `4101.70` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 272,900.00 USD | 0.00 USD | 48,030.00 USD |
| `7D` | `4105.10` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 408,250.00 USD | 0.00 USD | 134,430.00 USD |
| `1D` | `4105.80` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 362,410.00 USD | 0.00 USD | 63,100.00 USD |
| `7D` | `4109.40` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 504,830.00 USD | 0.00 USD | 76,750.00 USD |
| `1D` | `4109.90` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 210,960.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4113.70` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 437,970.00 USD | 0.00 USD | 63,950.00 USD |
| `1D` | `4114.00` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 135,090.00 USD | 0.00 USD | 14,420.00 USD |
| `7D` | `4118.00` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 282,440.00 USD | 0.00 USD | 57,050.00 USD |
| `1D` | `4118.10` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 22,910.00 USD | 0.00 USD | 6,130.00 USD |
| `1D` | `4122.20` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 60,830.00 USD | 0.00 USD | 1,630.00 USD |
| `7D` | `4122.30` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 286,850.00 USD | 0.00 USD | 30,750.00 USD |
| `7D` | `4126.60` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 221,890.00 USD | 0.00 USD | 86,130.00 USD |
| `7D` | `4130.90` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD |
| `7D` | `4135.20` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD |
| `1D` | `4138.60` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `4139.50` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4142.70` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD |
| `7D` | `4143.80` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 199,160.00 USD | 0.00 USD | 50,830.00 USD |
| `1D` | `4146.80` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 6,610.00 USD | 0.00 USD | 12,560.00 USD |
| `7D` | `4148.10` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 88,440.00 USD |
| `1D` | `4150.90` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 15,220.00 USD | 0.00 USD | 57,860.00 USD |
| `7D` | `4152.40` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 133,610.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `4155.00` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 98,490.00 USD | 0.00 USD | 69,120.00 USD |
| `7D` | `4156.70` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 268,170.00 USD | 0.00 USD | 57,810.00 USD |
| `1D` | `4159.10` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 57,680.00 USD | 0.00 USD | 51,470.00 USD |
| `7D` | `4161.00` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 420,240.00 USD | 0.00 USD | 134,730.00 USD |
| `1D` | `4163.20` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 101,840.00 USD | 0.00 USD | 142,810.00 USD |
| `7D` | `4165.30` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 485,080.00 USD | 0.00 USD | 204,730.00 USD |
| `1D` | `4167.30` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 151,370.00 USD | 0.00 USD | 53,250.00 USD |
| `7D` | `4169.60` | 11,640,000.00 USD | 11,640,000.00 USD | 0.00 USD | 401,230.00 USD | 0.00 USD | 82,290.00 USD |
| `1D` | `4171.40` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 27,910.00 USD | 0.00 USD | 31,860.00 USD |
| `7D` | `4173.90` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 156,630.00 USD | 0.00 USD | 66,900.00 USD |
| `1D` | `4175.50` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 97,800.00 USD | 0.00 USD | 29,560.00 USD |
| `7D` | `4178.20` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD |
| `1D` | `4179.60` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 93,460.00 USD | 0.00 USD | 19,210.00 USD |
| `7D` | `4182.50` | 12,310,000.00 USD | 12,310,000.00 USD | 0.00 USD | 143,730.00 USD | 0.00 USD | 40,030.00 USD |
| `1D` | `4183.70` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 152,990.00 USD | 0.00 USD | 31,330.00 USD |
| `7D` | `4186.80` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 219,060.00 USD | 0.00 USD | 65,350.00 USD |
| `1D` | `4187.80` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 168,710.00 USD | 0.00 USD | 20,080.00 USD |
| `7D` | `4191.10` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 254,710.00 USD | 0.00 USD | 31,760.00 USD |
| `1D` | `4191.90` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 104,160.00 USD | 0.00 USD | 11,550.00 USD |
| `7D` | `4195.40` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 205,140.00 USD | 0.00 USD | 33,460.00 USD |
| `1D` | `4196.00` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 31,540.00 USD | 0.00 USD | 7,780.00 USD |
| `7D` | `4199.70` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD |
| `1D` | `4200.10` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 33,210.00 USD | 0.00 USD | 824.23 USD |
| `7D` | `4204.00` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 116,920.00 USD | 0.00 USD | 23,560.00 USD |
| `1D` | `4204.20` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 5,280.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `4208.30` | 13,550,000.00 USD | 13,550,000.00 USD | 0.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD |
| `7D` | `4212.60` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `4216.90` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD |
| `7D` | `4221.20` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `4225.50` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD |
| `7D` | `4229.80` | 14,020,000.00 USD | 14,020,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `7D` | `4234.10` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4238.40` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4376.40` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `4380.30` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `4380.50` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD |
| `1D` | `4384.60` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,020.00 USD |
| `1D` | `4388.70` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 5,420.00 USD | 0.00 USD | 10,300.00 USD |
| `7D` | `4388.90` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4392.80` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 29,760.00 USD | 0.00 USD | 12,320.00 USD |
| `7D` | `4393.20` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `4396.90` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 6,970.00 USD | 0.00 USD | 18,290.00 USD |
| `7D` | `4397.50` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `4401.00` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 26,650.00 USD | 0.00 USD | 26,100.00 USD |
| `7D` | `4401.80` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 143,560.00 USD | 0.00 USD | 66,400.00 USD |
| `1D` | `4404.40` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 51,120.00 USD | 0.00 USD | 35,700.00 USD |
| `7D` | `4406.10` | 14,640,000.00 USD | 14,640,000.00 USD | 0.00 USD | 125,560.00 USD | 0.00 USD | 48,210.00 USD |
| `7D` | `4410.40` | 14,760,000.00 USD | 14,760,000.00 USD | 0.00 USD | 103,520.00 USD | 0.00 USD | 18,970.00 USD |
| `7D` | `4414.70` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 36,920.00 USD | 0.00 USD | 17,590.00 USD |
| `7D` | `4419.00` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD | 7,680.00 USD |
| `7D` | `4423.30` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD |
| `7D` | `4424.00` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.30M` | Total OI Tokens: `68,800.0 PAXG`
  * 1h OI Change: `-0.21%` | 4h OI Change: `-0.77%` | 24h OI Change: `-0.26%`
  * Exchange Breakdown: Binance=`104.62M` | Bybit=`24.52M` | OKX=`-` | Hyperliquid=`24.73M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.14K` | Last 24h: `17.74K` | Last 3d: `85.70K` | Last 7d: `216.77K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0015%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `0.0016%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0027%` | **USDT Bitget** | `0.0046%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `40.10%` | `59.90%` | `0.67` | 1,270,000.00 USD |
| `15M` | `Binance` | `51.08%` | `48.92%` | `1.04` | 318,220.00 USD |
| `15M` | `OKX` | `37.36%` | `62.64%` | `0.60` | 141,910.00 USD |
| `15M` | `Bybit` | `47.75%` | `52.25%` | `0.91` | 183,590.00 USD |
| `15M` | `KuCoin` | `71.25%` | `28.75%` | `2.48` | 76,790.00 USD |
| `15M` | `Gate` | `12.58%` | `87.42%` | `0.14` | 34,350.00 USD |
| `15M` | `Bitget` | `69.86%` | `30.14%` | `2.32` | 29,290.00 USD |
| `15M` | `BingX` | `5.9%` | `94.1%` | `0.06` | 278,470.00 USD |
| `15M` | `MEXC` | `79.8%` | `20.2%` | `3.95` | 54,760.00 USD |
| `15M` | `Bitunix` | `56.7%` | `43.3%` | `1.31` | 11,150.00 USD |
| `15M` | `Hyperliquid` | `84.96%` | `15.04%` | `5.65` | 29,270.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.37%` | `49.63%` | `1.01` | 49,130.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `14.59%` | `85.41%` | `0.17` | 58,700.00 USD |
| `15M` | `HTX` | `99.61%` | `0.39%` | `255.41` | 79.86 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 287.96 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `3.99%` | `96.01%` | `0.04` | 251.77 USD |
| `15M` | `Whale Positions` | `51.08%` | `48.92%` | `1.04` | 318,220.00 USD |
| `15M` | `Global Accounts` | `40.10%` | `59.90%` | `0.67` | 1,270,000.00 USD |
| `1H` | `PAXG` | `59.31%` | `40.69%` | `1.46` | 6,960,000.00 USD |
| `1H` | `Binance` | `51.45%` | `48.55%` | `1.06` | 2,290,000.00 USD |
| `1H` | `OKX` | `48.79%` | `51.21%` | `0.95` | 1,070,000.00 USD |
| `1H` | `Bybit` | `58.41%` | `41.59%` | `1.40` | 402,620.00 USD |
| `1H` | `KuCoin` | `66.04%` | `33.96%` | `1.94` | 222,520.00 USD |
| `1H` | `Gate` | `69.32%` | `30.68%` | `2.26` | 235,910.00 USD |
| `1H` | `Bitget` | `49.56%` | `50.44%` | `0.98` | 389,860.00 USD |
| `1H` | `BingX` | `64.91%` | `35.09%` | `1.85` | 347,460.00 USD |
| `1H` | `MEXC` | `75.3%` | `24.7%` | `3.05` | 738,420.00 USD |
| `1H` | `Bitunix` | `58.43%` | `41.57%` | `1.41` | 142,490.00 USD |
| `1H` | `Hyperliquid` | `76.91%` | `23.09%` | `3.33` | 194,200.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.58%` | `50.42%` | `0.98` | 170,860.00 USD |
| `1H` | `Crypto.com` | `54.56%` | `45.44%` | `1.20` | 2,550.00 USD |
| `1H` | `WhiteBIT` | `84.91%` | `15.09%` | `5.63` | 678,720.00 USD |
| `1H` | `HTX` | `92.27%` | `7.73%` | `11.94` | 1,300.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `43.74%` | `56.26%` | `0.78` | 17,330.00 USD |
| `1H` | `Aster` | `88.4%` | `11.6%` | `7.62` | 237.61 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `10.72%` | `89.28%` | `0.12` | 62,440.00 USD |
| `1H` | `Whale Positions` | `51.45%` | `48.55%` | `1.06` | 2,290,000.00 USD |
| `1H` | `Global Accounts` | `59.31%` | `40.69%` | `1.46` | 6,960,000.00 USD |
| `4H` | `PAXG` | `49.66%` | `50.34%` | `0.99` | 42,090,000.00 USD |
| `4H` | `Binance` | `50.44%` | `49.56%` | `1.02` | 15,660,000.00 USD |
| `4H` | `OKX` | `47.02%` | `52.98%` | `0.89` | 6,160,000.00 USD |
| `4H` | `Bybit` | `48.67%` | `51.33%` | `0.95` | 4,620,000.00 USD |
| `4H` | `KuCoin` | `50.01%` | `49.99%` | `1.00` | 725,450.00 USD |
| `4H` | `Gate` | `47.54%` | `52.46%` | `0.91` | 1,360,000.00 USD |
| `4H` | `Bitget` | `48.93%` | `51.07%` | `0.96` | 2,630,000.00 USD |
| `4H` | `BingX` | `31.68%` | `68.32%` | `0.46` | 3,160,000.00 USD |
| `4H` | `MEXC` | `50.17%` | `49.83%` | `1.01` | 2,930,000.00 USD |
| `4H` | `Bitunix` | `50.87%` | `49.13%` | `1.04` | 608,570.00 USD |
| `4H` | `Hyperliquid` | `59.76%` | `40.24%` | `1.49` | 610,960.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.62%` | `50.38%` | `0.98` | 1,510,000.00 USD |
| `4H` | `Crypto.com` | `41.03%` | `58.97%` | `0.70` | 23,970.00 USD |
| `4H` | `WhiteBIT` | `85.55%` | `14.45%` | `5.92` | 1,730,000.00 USD |
| `4H` | `HTX` | `67.23%` | `32.77%` | `2.05` | 13,910.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.14%` | `56.86%` | `0.76` | 99,560.00 USD |
| `4H` | `Aster` | `49.16%` | `50.84%` | `0.97` | 45,040.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.86%` | `47.14%` | `1.12` | 190,360.00 USD |
| `4H` | `Whale Positions` | `50.44%` | `49.56%` | `1.02` | 15,660,000.00 USD |
| `4H` | `Global Accounts` | `49.66%` | `50.34%` | `0.99` | 42,090,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BULLISH (ABOVE PIVOT)`** | GOLD (XAUUSD.pi) Metal Auction: ROTATION | `4045.64` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -11,350.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `15m` | -44,820.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30m` | -78,340.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1h` | -176,680.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `2h` | -592,960.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,730,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `6h` | -83,510.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `8h` | -193,420.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `12h` | 306,230.00 USD | 0.00 USD | **`ACCUMULATION`** |
| `24h` | -1,350,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,690,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,400,000.00 USD | 0.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-11.35K` | 15m=`-44.82K` | 1h=`-176.68K` | 24h=`-1.35M`
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
  * Mathematical Lot Sizing: **`1.05 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4007.50` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4017.02` (Risk Distance: `9.52` pts)
  * +2.5R Take Profit: `3983.71`
  * Mathematical Lot Sizing: **`1.05 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4013.48`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
