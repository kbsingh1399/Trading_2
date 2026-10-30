# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 08:18:38 IST` (`2026-10-30 02:48:38 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4002.97` | **Live Ask Quote**: `4003.05` | **Mid Price**: `4003.01`
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
  * Session VWAP: `4003.01` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `10.01` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4031.03` | Lower -3.00σ Band: `3974.99`
  * Upper +2.51σ Band: `4025.03` | Lower -2.51σ Band: `3980.99`
  * Upper +2.01σ Band: `4019.82` | Lower -2.01σ Band: `3986.20`
  * Upper +2.00σ Band: `4019.02` | Lower -2.00σ Band: `3987.00`
  * Upper +1.28σ Band: `4014.22` | Lower -1.28σ Band: `3991.80`
  * Upper +1.00σ Band: `4011.02` | Lower -1.00σ Band: `3995.00`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4003.01` | EMA-20=`4003.01` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4003.01` (Slope: `+0.0000`) | EMA-100=`4003.01`
  * Institutional Anchors: EMA-144=`4003.01` | EMA-200=`4003.01` (Slope: `+0.0000`) | EMA-233=`4003.01`
- **Range Boundaries**: 24H High=`4043.04` | 24H Low=`3962.98` | Weekly High=`4083.07` | Weekly Low=`3922.95`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4013.39` (Distance: `-0.26%`)
  * Point of Control (POC) = `4006.86` (Distance: `-0.10%`)
  * Value Area Low (VAL) = `4000.33` (Distance: `+0.06%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4049.63` | Weekly POC=`4014.77` | Weekly VAL=`4004.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3996.30`
  * London Session (08:00-16:00 UTC): High=`4019.02` | Low=`3987.00`
  * New York Session (13:00-21:00 UTC): High=`4027.03` | Low=`3978.99`
  * Initial Balance (First Hour): IB High=`4015.02` | IB Low=`3991.00`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3987.00` - `4019.02`
  * Optimal Trade Entry (OTE 0.705): `4011.02`
  * Structural Invalidation Anchor (0.786): `4035.03`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4006.74` | `4007.76` | `4004.07` | `4005.24` | `44` | 174,809.20 USD | 57,144.11 USD | `+32.69%` | -759,572.77 USD | `+0.98` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `4005.23` | `4007.20` | `4004.76` | `4007.07` | `29` | 115,349.45 USD | 10,938.60 USD | `+9.48%` | -748,634.16 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `4007.07` | `4007.07` | `4005.19` | `4005.19` | `15` | 61,659.01 USD | -25,572.28 USD | `-41.47%` | -774,206.44 USD | `-0.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4008.80` | `4013.63` | `4007.24` | `4013.26` | `216` | 865,049.64 USD | -7,541.90 USD | `-0.87%` | -552,958.57 USD | `+0.17` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4013.25` | `4014.92` | `4006.67` | `4006.74` | `129` | 517,573.36 USD | -263,758.31 USD | `-50.96%` | -816,716.88 USD | `-1.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4006.74` | `4007.76` | `4004.07` | `4005.60` | `86` | 345,849.34 USD | 48,478.76 USD | `+14.02%` | -768,238.12 USD | `+0.58` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `4012.56` | `4020.37` | `4006.19` | `4008.11` | `1,140` | 4,574,350.30 USD | -742,392.72 USD | `-16.23%` | -205,918.32 USD | `-1.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4008.10` | `4013.95` | `3999.00` | `4008.79` | `1,150` | 4,606,132.72 USD | -286,613.67 USD | `-6.22%` | -492,531.99 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4008.80` | `4014.92` | `4004.07` | `4005.19` | `433` | 1,734,440.66 USD | -228,789.77 USD | `-13.19%` | -721,321.77 USD | `-0.44` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 614,369.34 USD | `+1.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 632,225.70 USD | `-0.18` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3999.00` | `4005.60` | `2,721` | 10,908,955.36 USD | -1,251,827.84 USD | `-11.48%` | -619,602.14 USD | `-1.53` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4025.10` | `4041.25` | `4019.26` | `4024.40` | `1,995` | 8,039,943.06 USD | -252,376.54 USD | `-3.14%` | -910,560.46 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4024.40` | `4039.41` | `4022.01` | `4026.82` | `3,114` | 12,548,493.70 USD | 432,113.27 USD | `+3.44%` | -478,447.19 USD | `+1.31` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 614,369.34 USD | `+1.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 632,225.70 USD | `-0.18` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3999.00` | `4005.60` | `2,721` | 10,908,955.36 USD | -1,251,827.84 USD | `-11.48%` | -619,602.14 USD | `-1.53` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID` | `4001.50` | `11.6026` | 46,427.80 USD | 1,218,092.02 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4001.60` | `7.3957` | 29,594.63 USD | 1,171,664.21 USD | `4 orders` | `-0.05%` | `-` |
| `BID` | `4001.70` | `50.4005` | 201,687.68 USD | 1,142,069.58 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `4001.80` | `58.2851` | 233,245.31 USD | 940,381.90 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `4001.90` | `5.3064` | 21,235.68 USD | 707,136.59 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4002.00` | `4.1229` | 16,499.85 USD | 685,900.90 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `4002.10` | `13.7389` | 54,984.45 USD | 669,401.06 USD | `5 orders` | `-0.04%` | `-` |
| `BID` | `4002.20` | `21.4947` | 86,026.09 USD | 614,416.61 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `4002.30` | `11.2960` | 45,209.98 USD | 528,390.52 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `4002.40` | `30.3337` | 121,407.60 USD | 483,180.54 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4002.50` | `6.1835` | 24,749.46 USD | 361,772.94 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `4002.60` | `9.1912` | 36,788.70 USD | 337,023.48 USD | `4 orders` | `-0.02%` | `-` |
| `BID` | `4002.70` | `18.5154` | 74,111.59 USD | 300,234.78 USD | `5 orders` | `-0.02%` | `-` |
| `BID` | `4002.80` | `3.8093` | 15,247.87 USD | 226,123.19 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `4002.90` | `0.9368` | 3,749.92 USD | 210,875.32 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `4003.00` | `8.1781` | 32,736.93 USD | 207,125.41 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `4003.10` | `6.2852` | 25,160.28 USD | 174,388.47 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4003.30` | `4.7458` | 18,998.86 USD | 149,228.19 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `4003.40` | `5.2453` | 20,999.03 USD | 130,229.33 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `4003.50` | `27.2837` | 109,230.29 USD | 109,230.29 USD | `11 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `4003.55` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 4,003.55` | `0.00%` | `-` |
| `ASK` | `4003.60` | `1.8962` | 7,591.63 USD | 7,591.63 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `4003.80` | `2.6261` | 10,514.38 USD | 18,106.01 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4003.90` | `7.8661` | 31,495.08 USD | 49,601.08 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `4004.00` | `40.8413` | 163,528.57 USD | 213,129.65 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `4004.10` | `3.7461` | 14,999.76 USD | 228,129.41 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `4004.20` | `2.9959` | 11,996.18 USD | 240,125.59 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `4004.30` | `14.6087` | 58,497.62 USD | 298,623.21 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `4004.40` | `9.2163` | 36,905.75 USD | 335,528.96 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `4004.50` | `9.5415` | 38,208.94 USD | 373,737.90 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `4004.60` | `54.6661` | 218,915.86 USD | 592,653.76 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4004.70` | `5.2435` | 20,998.64 USD | 613,652.40 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4004.80` | `5.3484` | 21,419.27 USD | 635,071.68 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `4004.90` | `63.0669` | 252,576.63 USD | 887,648.30 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `4005.00` | `5.2931` | 21,198.87 USD | 908,847.17 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `4005.10` | `14.5622` | 58,323.07 USD | 967,170.24 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `4005.20` | `82.8752` | 331,931.75 USD | 1,299,101.99 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `4005.30` | `4.0113` | 16,066.46 USD | 1,315,168.45 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `4005.40` | `1.4857` | 5,950.82 USD | 1,321,119.27 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4005.50` | `18.7227` | 74,993.77 USD | 1,396,113.05 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `4005.60` | `8.7186` | 34,923.22 USD | 1,431,036.27 USD | `3 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:13:17 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `48` | `0x5b5d...c060` | `SHORT` | 25,974,222.60 USD | `6,489.82` | `4185.46` | `4002.70` | `30891.68` | 1,188,728.42 USD | `+4.58%` | `4X Cross` |
| `49` | `0x4692...164f` | `SHORT` | 25,250,132.99 USD | `6,307.33` | `4129.91` | `4002.70` | `14008.87` | 798,576.46 USD | `+3.16%` | `5X Cross` |
| `61` | `0xb83d...6e36` | `SHORT` | 23,496,620.31 USD | `5,869.90` | `4228.86` | `4002.70` | `28431.56` | 1,326,401.63 USD | `+5.65%` | `5X Cross` |
| `97` | `0xec0b...b078` | `LONG` | 19,332,528.77 USD | `4,828.91` | `4157.43` | `4002.70` | `2334.42` | -743,353.54 USD | `-3.85%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,141,955.89 USD | `3,532.93` | `4128.54` | `4002.70` | `575.04` | -443,893.29 USD | `-3.14%` | `3X Cross` |
| `156` | `0x7a6d...f79c` | `SHORT` | 13,081,350.15 USD | `3,268.21` | `4228.94` | `4002.70` | `4399.00` | 739,728.98 USD | `+5.65%` | `25X Cross` |
| `179` | `0xa742...e390` | `SHORT` | 11,606,670.40 USD | `2,900.00` | `4364.92` | `4002.70` | `4235.82` | 1,051,605.93 USD | `+9.06%` | `20X Cross` |
| `263` | `0x3678...b209` | `LONG` | 8,807,480.00 USD | `2,200.00` | `4176.09` | `4002.70` | `2698.58` | -379,939.30 USD | `-4.31%` | `25X Cross` |
| `264` | `0x41e5...0825` | `SHORT` | 8,806,380.00 USD | `2,200.00` | `4112.20` | `4002.70` | `4331.30` | 240,474.59 USD | `+2.73%` | `20X Cross` |
| `298` | `0xacb6...efbd` | `SHORT` | 7,907,204.97 USD | `1,975.37` | `4048.55` | `4002.70` | `6587.92` | 90,186.74 USD | `+1.14%` | `6X Cross` |
| `360` | `0xc26c...b8f4` | `LONG` | 6,326,443.00 USD | `1,579.95` | `4075.62` | `4002.70` | `0.000000` | -112,853.97 USD | `-1.78%` | `1X Cross` |
| `486` | `0x354b...6425` | `LONG` | 4,516,233.10 USD | `1,128.24` | `4004.98` | `4002.70` | `0.000000` | -2,352.62 USD | `-0.05%` | `10X Cross` |
| `551` | `0x63da...8add` | `LONG` | 4,002,600.00 USD | `1,000.00` | `4021.46` | `4002.70` | `3564.27` | -18,860.96 USD | `-0.47%` | `25X Cross` |
| `562` | `0xf3dc...1672` | `LONG` | 3,940,035.61 USD | `984.27` | `4018.39` | `4002.70` | `2887.29` | -15,151.08 USD | `-0.38%` | `20X Cross` |
| `574` | `0x9aa5...58af` | `LONG` | 3,889,191.43 USD | `971.64` | `4279.98` | `4002.70` | `0.000000` | -269,417.65 USD | `-6.93%` | `20X Cross` |
| `664` | `0x4a20...3c26` | `LONG` | 3,352,362.22 USD | `837.40` | `4599.73` | `4002.70` | `0.000000` | -499,458.16 USD | `-14.90%` | `20X Cross` |
| `825` | `0x0fac...7a0a` | `LONG` | 2,747,518.92 USD | `686.49` | `4290.34` | `4002.70` | `1292.44` | -197,739.79 USD | `-7.20%` | `25X Cross` |
| `890` | `0xd8c5...99b0` | `SHORT` | 2,523,562.81 USD | `630.35` | `4175.35` | `4002.70` | `33762.45` | 108,394.08 USD | `+4.30%` | `4X Cross` |
| `905` | `0x625e...a354` | `SHORT` | 2,481,798.00 USD | `620.00` | `4122.81` | `4002.70` | `4342.40` | 74,349.03 USD | `+3.00%` | `20X Cross` |
| `929` | `0xeae3...e8ad` | `SHORT` | 2,402,040.00 USD | `600.00` | `4104.77` | `4002.70` | `4325.42` | 60,825.11 USD | `+2.53%` | `20X Cross` |
| `932` | `0xf285...fa82` | `LONG` | 2,393,799.24 USD | `598.11` | `4146.45` | `4002.70` | `3891.40` | -86,220.31 USD | `-3.60%` | `25X Cross` |
| `940` | `0x12f7...8750` | `LONG` | 2,343,965.39 USD | `585.61` | `4082.77` | `4002.70` | `2796.66` | -46,951.59 USD | `-2.00%` | `10X Cross` |
| `1084` | `0x413c...886c` | `LONG` | 2,001,500.00 USD | `500.00` | `4010.43` | `4002.70` | `0.000000` | -3,716.23 USD | `-0.19%` | `2X Cross` |
| `1091` | `0x61ce...a62b` | `SHORT` | 1,991,506.51 USD | `497.50` | `4071.66` | `4002.70` | `4727.30` | 34,162.28 USD | `+1.72%` | `20X Cross` |
| `1163` | `0x2edd...8179` | `LONG` | 1,886,147.84 USD | `470.91` | `4164.68` | `4005.20` | `0.000000` | -75,053.47 USD | `-3.98%` | `10X Cross` |
| `1206` | `0xead5...69f2` | `LONG` | 1,816,451.57 USD | `453.78` | `4220.88` | `4002.70` | `3539.10` | -98,916.49 USD | `-5.45%` | `5X Isolated` |
| `1268` | `0x7a6d...f79c` | `SHORT` | 1,715,786.41 USD | `428.38` | `4136.09` | `4005.20` | `5402.75` | 56,028.60 USD | `+3.27%` | `10X Cross` |
| `1292` | `0x46fc...1195` | `LONG` | 1,670,409.07 USD | `417.29` | `4054.17` | `4002.70` | `2160.61` | -21,356.50 USD | `-1.28%` | `20X Cross` |
| `1345` | `0xee02...309d` | `SHORT` | 1,601,680.00 USD | `400.00` | `4438.84` | `4002.70` | `4227.04` | 173,858.60 USD | `+10.85%` | `25X Isolated` |
| `1347` | `0x6d15...d374` | `LONG` | 1,601,160.00 USD | `400.00` | `4068.25` | `4002.70` | `3841.97` | -26,140.00 USD | `-1.63%` | `25X Cross` |
| `1371` | `0x02a7...fe9f` | `SHORT` | 1,561,521.00 USD | `390.00` | `4055.02` | `4002.70` | `4306.86` | 19,938.25 USD | `+1.28%` | `25X Cross` |
| `1401` | `0x51f6...2b39` | `LONG` | 1,547,271.42 USD | `386.31` | `4231.28` | `4005.20` | `404.07` | -87,299.46 USD | `-5.64%` | `10X Cross` |
| `1424` | `0x7e77...b8d2` | `SHORT` | 1,521,292.00 USD | `380.00` | `4131.92` | `4002.70` | `4293.66` | 48,837.64 USD | `+3.21%` | `20X Cross` |
| `1448` | `0x9c06...0560` | `LONG` | 1,494,424.67 USD | `373.26` | `4018.98` | `4002.70` | `0.000000` | -5,707.14 USD | `-0.38%` | `25X Cross` |
| `1450` | `0x72c2...9b37` | `LONG` | 1,493,644.59 USD | `373.13` | `4000.98` | `4002.70` | `3778.20` | 751.08 USD | `+0.05%` | `13X Isolated` |
| `1485` | `0x781e...96b7` | `SHORT` | 1,445,666.47 USD | `360.91` | `4363.71` | `4005.20` | `13655.36` | 129,236.04 USD | `+8.94%` | `10X Cross` |
| `1488` | `0xaa44...b844` | `LONG` | 1,441,080.00 USD | `360.00` | `4043.10` | `4002.70` | `2821.88` | -14,437.63 USD | `-1.00%` | `4X Cross` |
| `1597` | `0xa41f...d50a` | `LONG` | 1,316,736.60 USD | `328.96` | `4468.89` | `4002.70` | `3802.33` | -153,361.25 USD | `-11.65%` | `15X Cross` |
| `1609` | `0x7fda...17d1` | `SHORT` | 1,304,764.67 USD | `325.91` | `4013.13` | `4002.70` | `30386.91` | 3,138.88 USD | `+0.24%` | `20X Cross` |
| `1642` | `0xbf5a...88ba` | `SHORT` | 1,271,350.21 USD | `317.65` | `4091.80` | `4002.70` | `9737.64` | 28,432.83 USD | `+2.24%` | `20X Cross` |
| `1677` | `0xff31...ff6c` | `SHORT` | 1,241,054.00 USD | `310.00` | `4372.43` | `4002.70` | `4789.33` | 114,401.38 USD | `+9.22%` | `10X Isolated` |
| `1708` | `0xada6...6f88` | `LONG` | 1,214,901.69 USD | `303.50` | `4166.46` | `4002.70` | `1795.53` | -49,611.17 USD | `-4.08%` | `5X Cross` |
| `1862` | `0x50e2...d770` | `LONG` | 1,082,388.85 USD | `270.37` | `4243.58` | `4002.70` | `2562.26` | -64,937.61 USD | `-6.00%` | `20X Cross` |
| `1879` | `0x4c92...4f17` | `SHORT` | 1,067,868.87 USD | `266.72` | `4260.98` | `4002.70` | `6503.98` | 68,623.37 USD | `+6.43%` | `20X Cross` |
| `1936` | `0xd346...c4f3` | `LONG` | 1,021,766.93 USD | `255.17` | `4188.66` | `4002.70` | `3310.58` | -47,069.58 USD | `-4.61%` | `5X Isolated` |
| `1980` | `0xe47f...758c` | `LONG` | 1,000,750.00 USD | `250.00` | `4017.99` | `4002.70` | `3737.11` | -3,749.86 USD | `-0.37%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4110.96` (Vol: 346,900.00 USD, Dist: `+2.25%`) | Long MP=`3936.30` (Vol: 356,200.00 USD, Dist: `--2.09%`)
  * 48H Horizon: Short MP=`4097.83` (Vol: 356,200.00 USD, Dist: `+1.93%`) | Long MP=`3936.80` (Vol: 356,200.00 USD, Dist: `--2.08%`)
  * 3D Horizon: Short MP=`4097.17` (Vol: 387,700.00 USD, Dist: `+1.91%`) | Long MP=`3937.32` (Vol: 387,700.00 USD, Dist: `--2.06%`)
  * 7D Horizon: Short MP=`4111.33` (Vol: 1,000,000.00 USD, Dist: `+2.26%`) | Long MP=`3923.02` (Vol: 879,800.00 USD, Dist: `--2.42%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3611.30` | 16,240,000.00 USD | 16,240,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3615.50` | 16,170,000.00 USD | 16,170,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.40` | 3,900,000.00 USD | 3,900,000.00 USD | 30,440.00 USD | 0.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.70` | 16,030,000.00 USD | 16,030,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3622.50` | 3,870,000.00 USD | 3,870,000.00 USD | 69,970.00 USD | 0.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.90` | 15,960,000.00 USD | 15,960,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3626.60` | 3,790,000.00 USD | 3,790,000.00 USD | 41,750.00 USD | 0.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3628.10` | 15,870,000.00 USD | 15,870,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3630.70` | 3,740,000.00 USD | 3,740,000.00 USD | 35,480.00 USD | 0.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.30` | 15,680,000.00 USD | 15,680,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3634.80` | 3,700,000.00 USD | 3,700,000.00 USD | 30,830.00 USD | 0.00 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.50` | 15,570,000.00 USD | 15,570,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3638.90` | 3,670,000.00 USD | 3,670,000.00 USD | 30,930.00 USD | 0.00 USD | 7,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 15,440,000.00 USD | 15,440,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3643.00` | 3,630,000.00 USD | 3,630,000.00 USD | 8,280.00 USD | 0.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.90` | 15,370,000.00 USD | 15,370,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3647.10` | 3,610,000.00 USD | 3,610,000.00 USD | 12,080.00 USD | 0.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.10` | 15,330,000.00 USD | 15,330,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3651.20` | 3,600,000.00 USD | 3,600,000.00 USD | 12,210.00 USD | 0.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 15,310,000.00 USD | 15,310,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3655.30` | 3,590,000.00 USD | 3,590,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.50` | 15,280,000.00 USD | 15,280,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.70` | 15,250,000.00 USD | 15,250,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3665.90` | 15,220,000.00 USD | 15,220,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.70` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.10` | 15,210,000.00 USD | 15,210,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.30` | 14,850,000.00 USD | 14,850,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.50` | 14,360,000.00 USD | 14,360,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3850.70` | 13,830,000.00 USD | 13,830,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3852.10` | 3,580,000.00 USD | 3,580,000.00 USD | 2,810.00 USD | 0.00 USD | 752.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3854.90` | 13,510,000.00 USD | 13,510,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3856.20` | 3,580,000.00 USD | 3,580,000.00 USD | 76,990.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.10` | 13,200,000.00 USD | 13,200,000.00 USD | 272,330.00 USD | 0.00 USD | 19,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3860.30` | 3,490,000.00 USD | 3,490,000.00 USD | 121,680.00 USD | 0.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3863.30` | 12,910,000.00 USD | 12,910,000.00 USD | 183,740.00 USD | 0.00 USD | 76,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3864.40` | 3,350,000.00 USD | 3,350,000.00 USD | 202,550.00 USD | 0.00 USD | 35,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3867.50` | 12,650,000.00 USD | 12,650,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3868.50` | 3,120,000.00 USD | 3,120,000.00 USD | 151,760.00 USD | 0.00 USD | 23,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3871.70` | 12,110,000.00 USD | 12,110,000.00 USD | 352,520.00 USD | 0.00 USD | 45,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3872.60` | 2,940,000.00 USD | 2,940,000.00 USD | 142,240.00 USD | 0.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3875.90` | 11,710,000.00 USD | 11,710,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3876.70` | 2,780,000.00 USD | 2,780,000.00 USD | 76,690.00 USD | 0.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3880.10` | 11,170,000.00 USD | 11,170,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3880.80` | 2,700,000.00 USD | 2,700,000.00 USD | 128,720.00 USD | 0.00 USD | 19,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3884.30` | 10,830,000.00 USD | 10,830,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3884.90` | 2,550,000.00 USD | 2,550,000.00 USD | 24,980.00 USD | 0.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3888.50` | 10,690,000.00 USD | 10,690,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3889.00` | 2,510,000.00 USD | 2,510,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3892.70` | 10,580,000.00 USD | 10,580,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3893.10` | 2,480,000.00 USD | 2,480,000.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3896.90` | 10,450,000.00 USD | 10,450,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3897.20` | 2,440,000.00 USD | 2,440,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3901.10` | 10,340,000.00 USD | 10,340,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3901.30` | 2,400,000.00 USD | 2,400,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3905.30` | 10,250,000.00 USD | 10,250,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3909.50` | 10,210,000.00 USD | 10,210,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3913.70` | 10,160,000.00 USD | 10,160,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3917.90` | 10,140,000.00 USD | 10,140,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3922.10` | 9,410,000.00 USD | 9,410,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3926.30` | 8,460,000.00 USD | 8,460,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3930.50` | 7,570,000.00 USD | 7,570,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3934.10` | 2,390,000.00 USD | 2,390,000.00 USD | 55,890.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3934.70` | 6,730,000.00 USD | 6,730,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.20` | 2,320,000.00 USD | 2,320,000.00 USD | 153,540.00 USD | 0.00 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3938.90` | 6,270,000.00 USD | 6,270,000.00 USD | 625,340.00 USD | 0.00 USD | 39,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.30` | 2,150,000.00 USD | 2,150,000.00 USD | 299,910.00 USD | 0.00 USD | 59,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3943.10` | 5,600,000.00 USD | 5,600,000.00 USD | 376,840.00 USD | 0.00 USD | 113,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.40` | 1,790,000.00 USD | 1,790,000.00 USD | 385,320.00 USD | 0.00 USD | 53,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3947.30` | 5,110,000.00 USD | 5,110,000.00 USD | 845,980.00 USD | 0.00 USD | 128,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.50` | 1,360,000.00 USD | 1,360,000.00 USD | 359,720.00 USD | 0.00 USD | 40,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3951.50` | 4,140,000.00 USD | 4,140,000.00 USD | 848,650.00 USD | 0.00 USD | 94,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.60` | 955,040.00 USD | 955,040.00 USD | 170,180.00 USD | 0.00 USD | 32,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3955.70` | 3,190,000.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3958.70` | 752,230.00 USD | 752,230.00 USD | 255,750.00 USD | 0.00 USD | 8,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3959.90` | 2,420,000.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3962.80` | 487,860.00 USD | 487,860.00 USD | 139,630.00 USD | 0.00 USD | 49,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3964.10` | 1,580,000.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3966.90` | 298,610.00 USD | 298,610.00 USD | 36,900.00 USD | 0.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3968.30` | 1,110,000.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3971.00` | 243,280.00 USD | 243,280.00 USD | 57,990.00 USD | 0.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3972.50` | 945,550.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3975.10` | 167,990.00 USD | 167,990.00 USD | 102,560.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.70` | 646,890.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3979.20` | 58,070.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.90` | 439,510.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3983.30` | 23,310.00 USD | 23,310.00 USD | 19,950.00 USD | 0.00 USD | 3,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3985.10` | 227,870.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3989.30` | 138,910.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3993.50` | 33,100.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4094.00` | 27,170.00 USD | 27,170.00 USD | 20,110.00 USD | 0.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4098.10` | 183,960.00 USD | 183,960.00 USD | 149,400.00 USD | 0.00 USD | 7,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4102.20` | 504,520.00 USD | 504,520.00 USD | 263,830.00 USD | 0.00 USD | 56,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4102.70` | 4,870,000.00 USD | 4,870,000.00 USD | 330,140.00 USD | 0.00 USD | 115,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.30` | 986,760.00 USD | 986,760.00 USD | 428,010.00 USD | 0.00 USD | 54,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4106.90` | 5,490,000.00 USD | 5,490,000.00 USD | 506,510.00 USD | 0.00 USD | 110,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.40` | 1,290,000.00 USD | 1,290,000.00 USD | 258,370.00 USD | 0.00 USD | 41,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4111.10` | 6,670,000.00 USD | 6,670,000.00 USD | 1,090,000.00 USD | 0.00 USD | 90,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.50` | 1,580,000.00 USD | 1,580,000.00 USD | 264,830.00 USD | 0.00 USD | 32,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4115.30` | 7,320,000.00 USD | 7,320,000.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.60` | 1,760,000.00 USD | 1,760,000.00 USD | 160,660.00 USD | 0.00 USD | 14,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4119.50` | 8,330,000.00 USD | 8,330,000.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.70` | 2,050,000.00 USD | 2,050,000.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4123.70` | 8,840,000.00 USD | 8,840,000.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4126.80` | 2,140,000.00 USD | 2,140,000.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4127.90` | 9,090,000.00 USD | 9,090,000.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4130.90` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 18,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4132.10` | 9,310,000.00 USD | 9,310,000.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4135.00` | 2,280,000.00 USD | 2,280,000.00 USD | 122,580.00 USD | 0.00 USD | 7,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4136.30` | 9,540,000.00 USD | 9,540,000.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.10` | 2,330,000.00 USD | 2,330,000.00 USD | 37,970.00 USD | 0.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4140.50` | 9,760,000.00 USD | 9,760,000.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.20` | 2,370,000.00 USD | 2,370,000.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4144.70` | 9,920,000.00 USD | 9,920,000.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4147.30` | 2,390,000.00 USD | 2,390,000.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.90` | 10,020,000.00 USD | 10,020,000.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4153.10` | 10,110,000.00 USD | 10,110,000.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4157.30` | 10,490,000.00 USD | 10,490,000.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.50` | 10,920,000.00 USD | 10,920,000.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.70` | 11,250,000.00 USD | 11,250,000.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.90` | 11,760,000.00 USD | 11,760,000.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4174.10` | 11,910,000.00 USD | 11,910,000.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4176.00` | 2,430,000.00 USD | 2,430,000.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.30` | 12,360,000.00 USD | 12,360,000.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4180.10` | 2,530,000.00 USD | 2,530,000.00 USD | 89,560.00 USD | 0.00 USD | 5,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,530,000.00 USD | 12,530,000.00 USD | 133,800.00 USD | 0.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4184.20` | 2,700,000.00 USD | 2,700,000.00 USD | 144,610.00 USD | 0.00 USD | 30,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.70` | 12,850,000.00 USD | 12,850,000.00 USD | 249,690.00 USD | 0.00 USD | 66,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4188.30` | 2,900,000.00 USD | 2,900,000.00 USD | 173,790.00 USD | 0.00 USD | 26,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.90` | 13,430,000.00 USD | 13,430,000.00 USD | 556,060.00 USD | 0.00 USD | 30,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4192.40` | 3,100,000.00 USD | 3,100,000.00 USD | 179,860.00 USD | 0.00 USD | 18,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,750,000.00 USD | 13,750,000.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4196.50` | 3,200,000.00 USD | 3,200,000.00 USD | 85,090.00 USD | 0.00 USD | 15,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.30` | 14,190,000.00 USD | 14,190,000.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4200.60` | 3,310,000.00 USD | 3,310,000.00 USD | 105,540.00 USD | 0.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.50` | 14,530,000.00 USD | 14,530,000.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4204.70` | 3,420,000.00 USD | 3,420,000.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4207.70` | 14,670,000.00 USD | 14,670,000.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4208.80` | 3,460,000.00 USD | 3,460,000.00 USD | 22,630.00 USD | 0.00 USD | 10,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4211.90` | 14,780,000.00 USD | 14,780,000.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4212.90` | 3,480,000.00 USD | 3,480,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.10` | 14,890,000.00 USD | 14,890,000.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4217.00` | 3,530,000.00 USD | 3,530,000.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.30` | 15,000,000.00 USD | 15,000,000.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4221.10` | 3,560,000.00 USD | 3,560,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4224.50` | 15,100,000.00 USD | 15,100,000.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4225.20` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4228.70` | 15,150,000.00 USD | 15,150,000.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4229.30` | 3,580,000.00 USD | 3,580,000.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4232.90` | 15,200,000.00 USD | 15,200,000.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4237.10` | 15,220,000.00 USD | 15,220,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.50` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4396.70` | 15,300,000.00 USD | 15,300,000.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4400.90` | 15,420,000.00 USD | 15,420,000.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.10` | 15,560,000.00 USD | 15,560,000.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4409.30` | 15,700,000.00 USD | 15,700,000.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4413.50` | 15,760,000.00 USD | 15,760,000.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4413.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 300.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4417.70` | 15,890,000.00 USD | 15,890,000.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4417.90` | 3,600,000.00 USD | 3,600,000.00 USD | 23,120.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4421.90` | 15,940,000.00 USD | 15,940,000.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4422.00` | 3,630,000.00 USD | 3,630,000.00 USD | 21,930.00 USD | 0.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4426.10` | 3,680,000.00 USD | 3,680,000.00 USD | 38,710.00 USD | 0.00 USD | 8,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4426.10` | 16,000,000.00 USD | 16,000,000.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4430.20` | 3,740,000.00 USD | 3,740,000.00 USD | 53,490.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4430.30` | 16,110,000.00 USD | 16,110,000.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4433.30` | 3,780,000.00 USD | 3,780,000.00 USD | 33,280.00 USD | 0.00 USD | 4,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4434.50` | 16,260,000.00 USD | 16,260,000.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4438.70` | 16,340,000.00 USD | 16,340,000.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4442.90` | 16,500,000.00 USD | 16,500,000.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4446.20` | 16,530,000.00 USD | 16,530,000.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |

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
| `7D` | `3611.30` | 16,240,000.00 USD | 0.00 USD | 16,240,000.00 USD | 54,650.00 USD | 0.00 USD | 17,980.00 USD |
| `7D` | `3615.50` | 16,170,000.00 USD | 0.00 USD | 16,170,000.00 USD | 137,000.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `3618.40` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 30,440.00 USD | 0.00 USD | 3,780.00 USD |
| `7D` | `3619.70` | 16,030,000.00 USD | 0.00 USD | 16,030,000.00 USD | 45,440.00 USD | 0.00 USD | 18,300.00 USD |
| `1D` | `3622.50` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 69,970.00 USD | 0.00 USD | 10,330.00 USD |
| `7D` | `3623.90` | 15,960,000.00 USD | 0.00 USD | 15,960,000.00 USD | 75,670.00 USD | 0.00 USD | 20,150.00 USD |
| `1D` | `3626.60` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 41,750.00 USD | 0.00 USD | 8,860.00 USD |
| `7D` | `3628.10` | 15,870,000.00 USD | 0.00 USD | 15,870,000.00 USD | 174,310.00 USD | 0.00 USD | 11,940.00 USD |
| `1D` | `3630.70` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 35,480.00 USD | 0.00 USD | 5,650.00 USD |
| `7D` | `3632.30` | 15,680,000.00 USD | 0.00 USD | 15,680,000.00 USD | 98,360.00 USD | 0.00 USD | 12,660.00 USD |
| `1D` | `3634.80` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 30,830.00 USD | 0.00 USD | 1,740.00 USD |
| `7D` | `3636.50` | 15,570,000.00 USD | 0.00 USD | 15,570,000.00 USD | 110,910.00 USD | 0.00 USD | 22,430.00 USD |
| `1D` | `3638.90` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 30,930.00 USD | 0.00 USD | 7,190.00 USD |
| `7D` | `3640.70` | 15,440,000.00 USD | 0.00 USD | 15,440,000.00 USD | 55,830.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `3643.00` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 8,280.00 USD | 0.00 USD | 4,410.00 USD |
| `7D` | `3644.90` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `1D` | `3647.10` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 12,080.00 USD | 0.00 USD | 3,460.00 USD |
| `7D` | `3649.10` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3651.20` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 12,210.00 USD | 0.00 USD | 1,010.00 USD |
| `7D` | `3653.30` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3655.30` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 4,780.00 USD | 0.00 USD | 2,460.00 USD |
| `7D` | `3657.50` | 15,280,000.00 USD | 0.00 USD | 15,280,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3661.70` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3665.90` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3829.70` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 950.23 USD |
| `7D` | `3833.90` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 3,650.00 USD |
| `7D` | `3838.10` | 15,210,000.00 USD | 0.00 USD | 15,210,000.00 USD | 348,050.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `3842.30` | 14,850,000.00 USD | 0.00 USD | 14,850,000.00 USD | 437,410.00 USD | 0.00 USD | 48,440.00 USD |
| `7D` | `3846.50` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 458,430.00 USD | 0.00 USD | 74,300.00 USD |
| `7D` | `3850.70` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 256,150.00 USD | 0.00 USD | 69,900.00 USD |
| `1D` | `3852.10` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 2,810.00 USD | 0.00 USD | 752.34 USD |
| `7D` | `3854.90` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 284,750.00 USD | 0.00 USD | 19,860.00 USD |
| `1D` | `3856.20` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 76,990.00 USD | 0.00 USD | 6,160.00 USD |
| `7D` | `3859.10` | 13,200,000.00 USD | 0.00 USD | 13,200,000.00 USD | 272,330.00 USD | 0.00 USD | 19,140.00 USD |
| `1D` | `3860.30` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 121,680.00 USD | 0.00 USD | 17,380.00 USD |
| `7D` | `3863.30` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 183,740.00 USD | 0.00 USD | 76,420.00 USD |
| `1D` | `3864.40` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 202,550.00 USD | 0.00 USD | 35,420.00 USD |
| `7D` | `3867.50` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 495,510.00 USD | 0.00 USD | 44,020.00 USD |
| `1D` | `3868.50` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 151,760.00 USD | 0.00 USD | 23,530.00 USD |
| `7D` | `3871.70` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 352,520.00 USD | 0.00 USD | 45,550.00 USD |
| `1D` | `3872.60` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 142,240.00 USD | 0.00 USD | 18,230.00 USD |
| `7D` | `3875.90` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 468,690.00 USD | 0.00 USD | 72,700.00 USD |
| `1D` | `3876.70` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 76,690.00 USD | 0.00 USD | 5,830.00 USD |
| `7D` | `3880.10` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 310,860.00 USD | 0.00 USD | 32,920.00 USD |
| `1D` | `3880.80` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 128,720.00 USD | 0.00 USD | 19,540.00 USD |
| `7D` | `3884.30` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 94,830.00 USD | 0.00 USD | 41,540.00 USD |
| `1D` | `3884.90` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 24,980.00 USD | 0.00 USD | 13,970.00 USD |
| `7D` | `3888.50` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `1D` | `3889.00` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `3892.70` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 114,000.00 USD | 0.00 USD | 12,340.00 USD |
| `1D` | `3893.10` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `3896.90` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 111,210.00 USD | 0.00 USD | 3,810.00 USD |
| `1D` | `3897.20` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD |
| `7D` | `3901.10` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 73,850.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `3901.30` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 9,970.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `3905.30` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 36,810.00 USD | 0.00 USD | 8,890.00 USD |
| `7D` | `3909.50` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 36,880.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `3913.70` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 16,550.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `3917.90` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 696,100.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `3922.10` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 848,730.00 USD | 0.00 USD | 96,870.00 USD |
| `7D` | `3926.30` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 754,400.00 USD | 0.00 USD | 135,020.00 USD |
| `7D` | `3930.50` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 700,860.00 USD | 0.00 USD | 140,320.00 USD |
| `1D` | `3934.10` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 55,890.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `3934.70` | 6,730,000.00 USD | 0.00 USD | 6,730,000.00 USD | 420,070.00 USD | 0.00 USD | 47,010.00 USD |
| `1D` | `3938.20` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 153,540.00 USD | 0.00 USD | 14,710.00 USD |
| `7D` | `3938.90` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 625,340.00 USD | 0.00 USD | 39,370.00 USD |
| `1D` | `3942.30` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 299,910.00 USD | 0.00 USD | 59,080.00 USD |
| `7D` | `3943.10` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 376,840.00 USD | 0.00 USD | 113,800.00 USD |
| `1D` | `3946.40` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 385,320.00 USD | 0.00 USD | 53,070.00 USD |
| `7D` | `3947.30` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 845,980.00 USD | 0.00 USD | 128,470.00 USD |
| `1D` | `3950.50` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 359,720.00 USD | 0.00 USD | 40,530.00 USD |
| `7D` | `3951.50` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 848,650.00 USD | 0.00 USD | 94,370.00 USD |
| `1D` | `3954.60` | 955,040.00 USD | 0.00 USD | 955,040.00 USD | 170,180.00 USD | 0.00 USD | 32,630.00 USD |
| `7D` | `3955.70` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 700,360.00 USD | 0.00 USD | 77,210.00 USD |
| `1D` | `3958.70` | 752,230.00 USD | 0.00 USD | 752,230.00 USD | 255,750.00 USD | 0.00 USD | 8,620.00 USD |
| `7D` | `3959.90` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 731,220.00 USD | 0.00 USD | 104,920.00 USD |
| `1D` | `3962.80` | 487,860.00 USD | 0.00 USD | 487,860.00 USD | 139,630.00 USD | 0.00 USD | 49,610.00 USD |
| `7D` | `3964.10` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 378,010.00 USD | 0.00 USD | 87,450.00 USD |
| `1D` | `3966.90` | 298,610.00 USD | 0.00 USD | 298,610.00 USD | 36,900.00 USD | 0.00 USD | 18,440.00 USD |
| `7D` | `3968.30` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 125,300.00 USD | 0.00 USD | 43,540.00 USD |
| `1D` | `3971.00` | 243,280.00 USD | 0.00 USD | 243,280.00 USD | 57,990.00 USD | 0.00 USD | 17,300.00 USD |
| `7D` | `3972.50` | 945,550.00 USD | 0.00 USD | 945,550.00 USD | 258,710.00 USD | 0.00 USD | 39,940.00 USD |
| `1D` | `3975.10` | 167,990.00 USD | 0.00 USD | 167,990.00 USD | 102,560.00 USD | 0.00 USD | 7,360.00 USD |
| `7D` | `3976.70` | 646,890.00 USD | 0.00 USD | 646,890.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3979.20` | 58,070.00 USD | 0.00 USD | 58,070.00 USD | 23,910.00 USD | 0.00 USD | 10,850.00 USD |
| `7D` | `3980.90` | 439,510.00 USD | 0.00 USD | 439,510.00 USD | 199,160.00 USD | 0.00 USD | 12,470.00 USD |
| `1D` | `3983.30` | 23,310.00 USD | 0.00 USD | 23,310.00 USD | 19,950.00 USD | 0.00 USD | 3,370.00 USD |
| `7D` | `3985.10` | 227,870.00 USD | 0.00 USD | 227,870.00 USD | 59,830.00 USD | 0.00 USD | 29,130.00 USD |
| `7D` | `3989.30` | 138,910.00 USD | 0.00 USD | 138,910.00 USD | 87,550.00 USD | 0.00 USD | 18,260.00 USD |
| `7D` | `3993.50` | 33,100.00 USD | 0.00 USD | 33,100.00 USD | 33,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4020.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4020.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4073.30` | 7,290.00 USD | 7,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4077.50` | 694,930.00 USD | 694,930.00 USD | 0.00 USD | 657,490.00 USD | 0.00 USD | 30,140.00 USD |
| `7D` | `4081.70` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 819,870.00 USD | 0.00 USD | 73,920.00 USD |
| `7D` | `4085.90` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 670,910.00 USD | 0.00 USD | 148,490.00 USD |
| `7D` | `4090.10` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 722,470.00 USD | 0.00 USD | 147,240.00 USD |
| `1D` | `4094.00` | 27,170.00 USD | 27,170.00 USD | 0.00 USD | 20,110.00 USD | 0.00 USD | 7,060.00 USD |
| `7D` | `4094.30` | 3,750,000.00 USD | 3,750,000.00 USD | 0.00 USD | 424,200.00 USD | 0.00 USD | 47,130.00 USD |
| `1D` | `4098.10` | 183,960.00 USD | 183,960.00 USD | 0.00 USD | 149,400.00 USD | 0.00 USD | 7,400.00 USD |
| `7D` | `4098.50` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 651,150.00 USD | 0.00 USD | 26,970.00 USD |
| `1D` | `4102.20` | 504,520.00 USD | 504,520.00 USD | 0.00 USD | 263,830.00 USD | 0.00 USD | 56,730.00 USD |
| `7D` | `4102.70` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 330,140.00 USD | 0.00 USD | 115,300.00 USD |
| `1D` | `4106.30` | 986,760.00 USD | 986,760.00 USD | 0.00 USD | 428,010.00 USD | 0.00 USD | 54,230.00 USD |
| `7D` | `4106.90` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 506,510.00 USD | 0.00 USD | 110,780.00 USD |
| `1D` | `4110.40` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 258,370.00 USD | 0.00 USD | 41,060.00 USD |
| `7D` | `4111.10` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 90,400.00 USD |
| `1D` | `4114.50` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 264,830.00 USD | 0.00 USD | 32,150.00 USD |
| `7D` | `4115.30` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 573,050.00 USD | 0.00 USD | 70,510.00 USD |
| `1D` | `4118.60` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 160,660.00 USD | 0.00 USD | 14,120.00 USD |
| `7D` | `4119.50` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 894,570.00 USD | 0.00 USD | 118,110.00 USD |
| `1D` | `4122.70` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 250,520.00 USD | 0.00 USD | 40,440.00 USD |
| `7D` | `4123.70` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 417,860.00 USD | 0.00 USD | 88,410.00 USD |
| `1D` | `4126.80` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 61,120.00 USD | 0.00 USD | 25,840.00 USD |
| `7D` | `4127.90` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 202,410.00 USD | 0.00 USD | 52,300.00 USD |
| `1D` | `4130.90` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18,270.00 USD |
| `7D` | `4132.10` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 177,170.00 USD | 0.00 USD | 44,110.00 USD |
| `1D` | `4135.00` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 122,580.00 USD | 0.00 USD | 7,290.00 USD |
| `7D` | `4136.30` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 206,150.00 USD | 0.00 USD | 24,680.00 USD |
| `1D` | `4139.10` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 37,970.00 USD | 0.00 USD | 5,900.00 USD |
| `7D` | `4140.50` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 205,160.00 USD | 0.00 USD | 7,630.00 USD |
| `1D` | `4143.20` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 23,910.00 USD | 0.00 USD | 14,220.00 USD |
| `7D` | `4144.70` | 9,920,000.00 USD | 9,920,000.00 USD | 0.00 USD | 147,710.00 USD | 0.00 USD | 20,360.00 USD |
| `1D` | `4147.30` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 19,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4148.90` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 73,610.00 USD | 0.00 USD | 26,950.00 USD |
| `7D` | `4153.10` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 73,770.00 USD | 0.00 USD | 17,160.00 USD |
| `7D` | `4157.30` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 361,840.00 USD | 0.00 USD | 15,070.00 USD |
| `7D` | `4161.50` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 394,860.00 USD | 0.00 USD | 36,350.00 USD |
| `7D` | `4165.70` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 257,780.00 USD | 0.00 USD | 66,330.00 USD |
| `7D` | `4169.90` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 445,020.00 USD | 0.00 USD | 63,370.00 USD |
| `7D` | `4174.10` | 11,910,000.00 USD | 11,910,000.00 USD | 0.00 USD | 119,870.00 USD | 0.00 USD | 39,110.00 USD |
| `1D` | `4176.00` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 39,370.00 USD | 0.00 USD | 6,430.00 USD |
| `7D` | `4178.30` | 12,360,000.00 USD | 12,360,000.00 USD | 0.00 USD | 426,770.00 USD | 0.00 USD | 15,830.00 USD |
| `1D` | `4180.10` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 89,560.00 USD | 0.00 USD | 5,930.00 USD |
| `7D` | `4182.50` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 133,800.00 USD | 0.00 USD | 40,030.00 USD |
| `1D` | `4184.20` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 144,610.00 USD | 0.00 USD | 30,460.00 USD |
| `7D` | `4186.70` | 12,850,000.00 USD | 12,850,000.00 USD | 0.00 USD | 249,690.00 USD | 0.00 USD | 66,760.00 USD |
| `1D` | `4188.30` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 173,790.00 USD | 0.00 USD | 26,620.00 USD |
| `7D` | `4190.90` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 556,060.00 USD | 0.00 USD | 30,250.00 USD |
| `1D` | `4192.40` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 179,860.00 USD | 0.00 USD | 18,810.00 USD |
| `7D` | `4195.10` | 13,750,000.00 USD | 13,750,000.00 USD | 0.00 USD | 268,520.00 USD | 0.00 USD | 51,950.00 USD |
| `1D` | `4196.50` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 85,090.00 USD | 0.00 USD | 15,950.00 USD |
| `7D` | `4199.30` | 14,190,000.00 USD | 14,190,000.00 USD | 0.00 USD | 376,470.00 USD | 0.00 USD | 64,450.00 USD |
| `1D` | `4200.60` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 105,540.00 USD | 0.00 USD | 3,250.00 USD |
| `7D` | `4203.50` | 14,530,000.00 USD | 14,530,000.00 USD | 0.00 USD | 310,860.00 USD | 0.00 USD | 28,820.00 USD |
| `1D` | `4204.70` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 87,970.00 USD | 0.00 USD | 22,440.00 USD |
| `7D` | `4207.70` | 14,670,000.00 USD | 14,670,000.00 USD | 0.00 USD | 94,830.00 USD | 0.00 USD | 39,930.00 USD |
| `1D` | `4208.80` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 22,630.00 USD | 0.00 USD | 10,900.00 USD |
| `7D` | `4211.90` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 21,800.00 USD |
| `1D` | `4212.90` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 20,530.00 USD | 0.00 USD | 8,920.00 USD |
| `7D` | `4216.10` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `4217.00` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 40,750.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `4220.30` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 94,860.00 USD | 0.00 USD | 8,830.00 USD |
| `1D` | `4221.10` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 30,940.00 USD | 0.00 USD | 2,720.00 USD |
| `7D` | `4224.50` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 99,580.00 USD | 0.00 USD | 6,240.00 USD |
| `1D` | `4225.20` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,110.00 USD |
| `7D` | `4228.70` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 14,570.00 USD |
| `1D` | `4229.30` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 9,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4232.90` | 15,200,000.00 USD | 15,200,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 9,130.00 USD |
| `7D` | `4237.10` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4392.50` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,460.00 USD |
| `7D` | `4396.70` | 15,300,000.00 USD | 15,300,000.00 USD | 0.00 USD | 76,720.00 USD | 0.00 USD | 5,690.00 USD |
| `7D` | `4400.90` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 108,810.00 USD | 0.00 USD | 9,860.00 USD |
| `7D` | `4405.10` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 126,620.00 USD | 0.00 USD | 17,210.00 USD |
| `7D` | `4409.30` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 117,010.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `4413.50` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 46,640.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `4413.80` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 300.94 USD |
| `7D` | `4417.70` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 6,080.00 USD |
| `1D` | `4417.90` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 23,120.00 USD | 0.00 USD | 1,980.00 USD |
| `7D` | `4421.90` | 15,940,000.00 USD | 15,940,000.00 USD | 0.00 USD | 45,950.00 USD | 0.00 USD | 2,020.00 USD |
| `1D` | `4422.00` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 21,930.00 USD | 0.00 USD | 2,500.00 USD |
| `1D` | `4426.10` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 38,710.00 USD | 0.00 USD | 8,260.00 USD |
| `7D` | `4426.10` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 40,010.00 USD | 0.00 USD | 17,700.00 USD |
| `1D` | `4430.20` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 53,490.00 USD | 0.00 USD | 8,690.00 USD |
| `7D` | `4430.30` | 16,110,000.00 USD | 16,110,000.00 USD | 0.00 USD | 88,520.00 USD | 0.00 USD | 21,420.00 USD |
| `1D` | `4433.30` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 33,280.00 USD | 0.00 USD | 4,000.00 USD |
| `7D` | `4434.50` | 16,260,000.00 USD | 16,260,000.00 USD | 0.00 USD | 135,550.00 USD | 0.00 USD | 12,380.00 USD |
| `7D` | `4438.70` | 16,340,000.00 USD | 16,340,000.00 USD | 0.00 USD | 78,610.00 USD | 0.00 USD | 8,390.00 USD |
| `7D` | `4442.90` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 130,670.00 USD | 0.00 USD | 23,570.00 USD |
| `7D` | `4446.20` | 16,530,000.00 USD | 16,530,000.00 USD | 0.00 USD | 22,690.00 USD | 0.00 USD | 6,210.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `275.55M` | Total OI Tokens: `68,809.2 PAXG`
  * 1h OI Change: `+0.06%` | 4h OI Change: `+0.34%` | 24h OI Change: `+0.46%`
  * Exchange Breakdown: Binance=`107.60M` | Bybit=`20.32M` | OKX=`-` | Hyperliquid=`24.63M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.40K` | Last 24h: `27.84K` | Last 3d: `98.08K` | Last 7d: `223.34K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `51.04%` | `48.96%` | `1.04` | 1,100,000.00 USD |
| `15M` | `Binance` | `55.52%` | `44.48%` | `1.25` | 409,980.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `57.62%` | `42.38%` | `1.36` | 157,350.00 USD |
| `15M` | `KuCoin` | `51.43%` | `48.57%` | `1.06` | 101,530.00 USD |
| `15M` | `Gate` | `23.64%` | `76.36%` | `0.31` | 42,030.00 USD |
| `15M` | `Bitget` | `39.28%` | `60.72%` | `0.65` | 198,420.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `38.35%` | `61.65%` | `0.62` | 2,480.00 USD |
| `15M` | `Bitunix` | `48.84%` | `51.16%` | `0.95` | 9,360.00 USD |
| `15M` | `Hyperliquid` | `51.27%` | `48.73%` | `1.05` | 24,830.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `55.08%` | `44.92%` | `1.23` | 144,790.00 USD |
| `15M` | `HTX` | `81.44%` | `18.56%` | `4.39` | 3,800.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 1,000.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `44.51%` | `55.49%` | `0.80` | 5,580.00 USD |
| `15M` | `Whale Positions` | `55.52%` | `44.48%` | `1.25` | 409,980.00 USD |
| `15M` | `Global Accounts` | `51.04%` | `48.96%` | `1.04` | 1,100,000.00 USD |
| `1H` | `PAXG` | `51.41%` | `48.59%` | `1.06` | 4,660,000.00 USD |
| `1H` | `Binance` | `50.64%` | `49.36%` | `1.03` | 2,570,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `61.67%` | `38.33%` | `1.61` | 430,320.00 USD |
| `1H` | `KuCoin` | `50.07%` | `49.93%` | `1.00` | 397,920.00 USD |
| `1H` | `Gate` | `48.35%` | `51.65%` | `0.94` | 144,550.00 USD |
| `1H` | `Bitget` | `45.13%` | `54.87%` | `0.82` | 470,110.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `19.33%` | `80.67%` | `0.24` | 29,190.00 USD |
| `1H` | `Bitunix` | `44.2%` | `55.8%` | `0.79` | 84,980.00 USD |
| `1H` | `Hyperliquid` | `59.49%` | `40.51%` | `1.47` | 113,820.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `58.9%` | `41.1%` | `1.43` | 348,900.00 USD |
| `1H` | `HTX` | `49.38%` | `50.62%` | `0.98` | 28,670.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `33.55%` | `66.45%` | `0.50` | 18,990.00 USD |
| `1H` | `Aster` | `99.23%` | `0.77%` | `128.87` | 1,040.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `44.95%` | `55.05%` | `0.82` | 21,990.00 USD |
| `1H` | `Whale Positions` | `50.64%` | `49.36%` | `1.03` | 2,570,000.00 USD |
| `1H` | `Global Accounts` | `51.41%` | `48.59%` | `1.06` | 4,660,000.00 USD |
| `4H` | `PAXG` | `48.64%` | `51.36%` | `0.95` | 66,580,000.00 USD |
| `4H` | `Binance` | `44.85%` | `55.15%` | `0.81` | 11,710,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `57.36%` | `42.64%` | `1.35` | 8,080,000.00 USD |
| `4H` | `KuCoin` | `49.95%` | `50.05%` | `1.00` | 311,570.00 USD |
| `4H` | `Gate` | `48.36%` | `51.64%` | `0.94` | 2,640,000.00 USD |
| `4H` | `Bitget` | `46.42%` | `53.58%` | `0.87` | 3,360,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `33.18%` | `66.82%` | `0.50` | 31,730,000.00 USD |
| `4H` | `Bitunix` | `40.16%` | `59.84%` | `0.67` | 1,630,000.00 USD |
| `4H` | `Hyperliquid` | `54.4%` | `45.6%` | `1.19` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 5,610,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `76.04%` | `23.96%` | `3.17` | 1,270,000.00 USD |
| `4H` | `HTX` | `69.78%` | `30.22%` | `2.31` | 38,020.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `80.06%` | `19.94%` | `4.02` | 219,940.00 USD |
| `4H` | `Aster` | `56.72%` | `43.28%` | `1.31` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.98%` | `52.02%` | `0.92` | 0.00 USD |
| `4H` | `Whale Positions` | `44.85%` | `55.15%` | `0.81` | 11,710,000.00 USD |
| `4H` | `Global Accounts` | `48.64%` | `51.36%` | `0.95` | 66,580,000.00 USD |


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
| `5m` | -5,190.00 USD | 67,600.00 USD | **`ACCUMULATION`** |
| `15m` | -46,110.00 USD | -34,470.00 USD | **`DISTRIBUTION`** |
| `30m` | -64,510.00 USD | -10,730.00 USD | **`DISTRIBUTION`** |
| `1h` | -130,980.00 USD | -84,070.00 USD | **`DISTRIBUTION`** |
| `2h` | 49,770.00 USD | -355,280.00 USD | **`DISTRIBUTION`** |
| `4h` | 484,080.00 USD | -930,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,020,000.00 USD | -912,840.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,120,000.00 USD | -830,860.00 USD | **`DISTRIBUTION`** |
| `12h` | -776,480.00 USD | -301,210.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,050,000.00 USD | -499,560.00 USD | **`DISTRIBUTION`** |
| `1w` | -9,230,000.00 USD | -7,600,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,410,000.00 USD | -72,720,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-5.19K` | 15m=`-46.11K` | 1h=`-130.98K` | 24h=`-1.05M`
* Futures Capital Netflows: 5m=`+67.60K` | 15m=`-34.47K` | 1h=`-84.07K` | 24h=`-499.56K`
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
  * `2026-10-30 08:00:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:15:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:08:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:09:46 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [morningstar.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `4000.33` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3988.20` (Risk Distance: `12.13` pts)
  * +2.5R Take Profit: `4030.65`
  * Mathematical Lot Sizing: **`0.82 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4013.39` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4025.52` (Risk Distance: `12.13` pts)
  * +2.5R Take Profit: `3983.07`
  * Mathematical Lot Sizing: **`0.82 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4035.03`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
