# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 16:30:44 IST` (`2026-10-30 11:00:44 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3974.64` | **Live Ask Quote**: `3974.72` | **Mid Price**: `3974.68`
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
  * Session VWAP: `3995.80` | VWAP Z-Score: `-1.64` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.56` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `39.85` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4025.33` | Lower -3.00σ Band: `3966.27`
  * Upper +2.51σ Band: `4020.51` | Lower -2.51σ Band: `3971.09`
  * Upper +2.01σ Band: `4015.59` | Lower -2.01σ Band: `3976.01`
  * Upper +2.00σ Band: `4015.49` | Lower -2.00σ Band: `3976.11`
  * Upper +1.28σ Band: `4008.40` | Lower -1.28σ Band: `3983.20`
  * Upper +1.00σ Band: `4005.65` | Lower -1.00σ Band: `3985.96`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3985.30` | EMA-20=`3988.11` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`3996.44` (Slope: `+0.0000`) | EMA-100=`4007.30`
  * Institutional Anchors: EMA-144=`4013.48` | EMA-200=`4018.72` (Slope: `-0.1026`) | EMA-233=`4021.96`
- **Range Boundaries**: 24H High=`4039.31` | 24H Low=`3965.22` | Weekly High=`4082.75` | Weekly Low=`3965.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4007.93` (Distance: `-0.82%`)
  * Point of Control (POC) = `3990.50` (Distance: `-0.39%`)
  * Value Area Low (VAL) = `3982.43` (Distance: `-0.19%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4053.37` | Weekly POC=`4017.32` | Weekly VAL=`4004.00`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3965.22`
  * New York Session (13:00-21:00 UTC): High=`3991.98` | Low=`3974.12`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3988.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3958.78` - `3990.58`
  * Optimal Trade Entry (OTE 0.705): `3982.63`
  * Structural Invalidation Anchor (0.786): `4006.48`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3987.45` | `3988.82` | `3986.00` | `3986.25` | `26` | 105,077.85 USD | -44,441.46 USD | `-42.29%` | 53,297.90 USD | `-0.37` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `3986.25` | `3986.25` | `3982.10` | `3982.65` | `76` | 303,103.14 USD | -80,969.36 USD | `-26.71%` | -27,671.46 USD | `-0.78` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `3982.40` | `3982.50` | `3981.27` | `3981.65` | `32` | 125,779.10 USD | 46,735.70 USD | `+37.16%` | 19,064.24 USD | `+0.69` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `3988.52` | `3991.57` | `3986.48` | `3986.48` | `125` | 499,730.03 USD | -186,942.49 USD | `-37.41%` | -215,062.33 USD | `-0.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `3986.43` | `3989.15` | `3986.00` | `3986.25` | `111` | 441,579.70 USD | 71,280.94 USD | `+16.14%` | -143,781.39 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `3986.25` | `3986.25` | `3981.27` | `3982.00` | `109` | 434,659.65 USD | -29,682.59 USD | `-6.83%` | -173,463.98 USD | `+0.13` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `3981.68` | `4002.39` | `3979.22` | `4001.26` | `1,541` | 6,150,835.88 USD | 541,833.50 USD | `+8.81%` | 137,263.91 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4001.22` | `4002.41` | `3991.51` | `3995.66` | `459` | 1,835,738.77 USD | 110,152.21 USD | `+6.00%` | 247,416.12 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `3995.66` | `3995.82` | `3981.27` | `3982.00` | `640` | 2,554,619.22 USD | -420,880.11 USD | `-16.48%` | -173,463.98 USD | `-0.73` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `3981.65` | `2,639` | 10,535,416.46 USD | 226,554.54 USD | `+2.15%` | -352,411.70 USD | `+0.36` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,524,929.80 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,542,786.16 USD | `-1.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `3981.65` | `2,639` | 10,535,416.46 USD | 226,554.54 USD | `+2.15%` | -352,411.70 USD | `+0.36` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID` | `3975.60` | `52.2438` | 207,700.45 USD | 928,276.40 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3975.70` | `11.9085` | 47,344.62 USD | 720,575.95 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3975.80` | `21.6558` | 86,099.13 USD | 673,231.33 USD | `6 orders` | `-0.05%` | `-` |
| `BID` | `3975.90` | `7.7274` | 30,723.37 USD | 587,132.20 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3976.00` | `7.2778` | 28,936.53 USD | 556,408.83 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `3976.10` | `12.9480` | 51,482.54 USD | 527,472.30 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `3976.20` | `11.4997` | 45,725.11 USD | 475,989.75 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3976.30` | `30.7073` | 122,101.44 USD | 430,264.65 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `3976.40` | `10.6027` | 42,160.58 USD | 308,163.21 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `3976.50` | `4.5062` | 17,918.90 USD | 266,002.63 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `3976.60` | `13.8036` | 54,891.40 USD | 248,083.73 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `3976.70` | `0.5145` | 2,046.01 USD | 193,192.33 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `3976.80` | `7.9773` | 31,724.13 USD | 191,146.32 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3976.90` | `7.6139` | 30,279.72 USD | 159,422.19 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `3977.00` | `0.3771` | 1,499.73 USD | 129,142.48 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `3977.10` | `5.1442` | 20,459.00 USD | 127,642.75 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `3977.20` | `11.5823` | 46,065.12 USD | 107,183.75 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `3977.30` | `3.8329` | 15,244.59 USD | 61,118.63 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `3977.60` | `7.7965` | 31,011.36 USD | 45,874.03 USD | `3 orders` | `-0.00%` | `-` |
| `BID` | `3977.70` | `3.7365` | 14,862.68 USD | 14,862.68 USD | `4 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3977.75` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,977.75` | `0.00%` | `-` |
| `ASK` | `3977.80` | `6.2481` | 24,853.69 USD | 24,853.69 USD | `5 orders` | `+0.00%` | `-` |
| `ASK` | `3977.90` | `35.0830` | 139,556.67 USD | 164,410.36 USD | `3 orders` | `+0.00%` | `-` |
| `ASK` | `3978.00` | `21.4996` | 85,525.41 USD | 249,935.77 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `3978.10` | `4.4909` | 17,865.25 USD | 267,801.02 USD | `4 orders` | `+0.01%` | `-` |
| `ASK` | `3978.20` | `0.2518` | 1,001.71 USD | 268,802.73 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `3978.30` | `13.1623` | 52,363.58 USD | 321,166.30 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `3978.40` | `34.9023` | 138,855.31 USD | 460,021.62 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3978.50` | `64.0543` | 254,840.03 USD | 714,861.65 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `3978.60` | `20.1844` | 80,305.65 USD | 795,167.30 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3978.70` | `11.9681` | 47,617.48 USD | 842,784.78 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `3978.80` | `66.4735` | 264,484.76 USD | 1,107,269.54 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `3978.90` | `0.4712` | 1,874.86 USD | 1,109,144.40 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `3979.00` | `34.6254` | 137,774.47 USD | 1,246,918.87 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `3979.10` | `79.6368` | 316,882.79 USD | 1,563,801.66 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3979.20` | `42.3879` | 168,669.93 USD | 1,732,471.59 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `3979.30` | `12.3455` | 49,126.45 USD | 1,781,598.04 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3979.40` | `8.9807` | 35,737.80 USD | 1,817,335.84 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3979.50` | `29.1208` | 115,886.22 USD | 1,933,222.06 USD | `6 orders` | `+0.04%` | `-` |
| `ASK` | `3979.60` | `4.9591` | 19,735.23 USD | 1,952,957.29 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `3979.70` | `11.3633` | 45,222.53 USD | 1,998,179.82 USD | `4 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `47` | `0x5b5d...c060` | `SHORT` | 25,818,466.82 USD | `6,489.82` | `4185.46` | `3978.40` | `27354.94` | 1,344,484.19 USD | `+5.21%` | `4X Cross` |
| `49` | `0x4692...164f` | `SHORT` | 25,091,294.97 USD | `6,306.88` | `4127.25` | `3978.40` | `14242.62` | 938,818.62 USD | `+3.74%` | `5X Cross` |
| `63` | `0xb83d...6e36` | `SHORT` | 23,353,394.76 USD | `5,869.90` | `4228.86` | `3978.40` | `22356.74` | 1,469,627.17 USD | `+6.29%` | `5X Cross` |
| `100` | `0xec0b...b078` | `LONG` | 19,211,806.10 USD | `4,828.91` | `4157.43` | `3978.40` | `2257.24` | -864,076.21 USD | `-4.50%` | `25X Cross` |
| `144` | `0x645b...87b8` | `LONG` | 14,105,921.17 USD | `3,545.72` | `4127.81` | `3978.40` | `667.35` | -530,148.64 USD | `-3.76%` | `3X Cross` |
| `157` | `0x7a6d...f79c` | `SHORT` | 13,001,932.57 USD | `3,268.21` | `4228.94` | `3978.40` | `4382.85` | 819,146.56 USD | `+6.30%` | `25X Cross` |
| `181` | `0xa742...e390` | `SHORT` | 11,139,328.32 USD | `2,800.02` | `4364.62` | `3978.40` | `4212.84` | 1,081,715.82 USD | `+9.71%` | `20X Cross` |
| `260` | `0x41e5...0825` | `SHORT` | 8,752,700.00 USD | `2,200.00` | `4112.20` | `3978.40` | `4287.19` | 294,154.59 USD | `+3.36%` | `20X Cross` |
| `261` | `0x3678...b209` | `LONG` | 8,752,040.00 USD | `2,200.00` | `4176.09` | `3978.40` | `2640.99` | -435,379.30 USD | `-4.97%` | `25X Cross` |
| `297` | `0xacb6...efbd` | `SHORT` | 7,859,005.96 USD | `1,975.37` | `4048.55` | `3978.40` | `6687.09` | 138,385.75 USD | `+1.76%` | `6X Cross` |
| `364` | `0xc26c...b8f4` | `LONG` | 6,285,522.25 USD | `1,579.95` | `4075.62` | `3978.40` | `0.000000` | -153,774.72 USD | `-2.45%` | `1X Cross` |
| `558` | `0x63da...8add` | `LONG` | 3,978,300.00 USD | `1,000.00` | `4021.46` | `3978.40` | `3564.73` | -43,160.96 USD | `-1.08%` | `25X Cross` |
| `568` | `0xf3dc...1672` | `LONG` | 3,915,920.98 USD | `984.27` | `4018.39` | `3978.40` | `2842.59` | -39,265.71 USD | `-1.00%` | `20X Cross` |
| `592` | `0x9aa5...58af` | `LONG` | 3,802,547.56 USD | `955.80` | `4279.98` | `3978.40` | `0.000000` | -288,250.37 USD | `-7.58%` | `20X Cross` |
| `671` | `0x4a20...3c26` | `LONG` | 3,331,343.49 USD | `837.40` | `4599.73` | `3978.40` | `0.000000` | -520,476.89 USD | `-15.62%` | `20X Cross` |
| `780` | `0x9c06...0560` | `LONG` | 2,892,032.35 USD | `726.95` | `4002.36` | `3978.40` | `0.000000` | -17,496.91 USD | `-0.61%` | `25X Cross` |
| `826` | `0x0fac...7a0a` | `LONG` | 2,731,043.28 USD | `686.49` | `4290.34` | `3978.40` | `1294.26` | -214,215.43 USD | `-7.84%` | `25X Cross` |
| `852` | `0x354b...6425` | `LONG` | 2,634,525.92 USD | `662.21` | `4004.29` | `3978.40` | `0.000000` | -17,150.79 USD | `-0.65%` | `10X Cross` |
| `899` | `0x625e...a354` | `SHORT` | 2,466,670.00 USD | `620.00` | `4122.81` | `3978.40` | `4279.60` | 89,477.03 USD | `+3.63%` | `20X Cross` |
| `929` | `0xeae3...e8ad` | `SHORT` | 2,386,920.00 USD | `600.00` | `4104.77` | `3978.40` | `4268.68` | 75,945.11 USD | `+3.18%` | `20X Cross` |
| `930` | `0xf285...fa82` | `LONG` | 2,379,504.51 USD | `598.11` | `4146.45` | `3978.40` | `3891.87` | -100,515.04 USD | `-4.22%` | `25X Cross` |
| `935` | `0xd8c5...99b0` | `SHORT` | 2,364,462.66 USD | `594.35` | `4175.35` | `3978.40` | `35354.52` | 117,181.37 USD | `+4.96%` | `4X Cross` |
| `948` | `0x12f7...8750` | `LONG` | 2,329,735.05 USD | `585.61` | `4082.77` | `3978.40` | `2758.14` | -61,181.93 USD | `-2.63%` | `10X Cross` |
| `989` | `0x413c...886c` | `LONG` | 2,225,852.99 USD | `559.47` | `4007.05` | `3978.40` | `0.000000` | -15,974.22 USD | `-0.72%` | `2X Cross` |
| `1095` | `0x61ce...a62b` | `SHORT` | 1,979,168.42 USD | `497.50` | `4071.66` | `3978.40` | `4717.40` | 46,500.37 USD | `+2.35%` | `20X Cross` |
| `1171` | `0x2edd...8179` | `LONG` | 1,866,788.29 USD | `468.69` | `4164.68` | `3982.78` | `0.000000` | -85,150.78 USD | `-4.56%` | `10X Cross` |
| `1217` | `0xead5...69f2` | `LONG` | 1,805,379.25 USD | `453.78` | `4220.88` | `3978.40` | `3539.57` | -109,988.81 USD | `-6.09%` | `5X Isolated` |
| `1271` | `0x7a6d...f79c` | `SHORT` | 1,705,890.85 USD | `428.38` | `4136.09` | `3982.78` | `5331.35` | 65,924.15 USD | `+3.86%` | `10X Cross` |
| `1298` | `0x46fc...1195` | `LONG` | 1,661,407.69 USD | `417.61` | `4051.00` | `3978.40` | `2268.35` | -30,321.69 USD | `-1.83%` | `20X Cross` |
| `1345` | `0xee02...309d` | `SHORT` | 1,591,320.00 USD | `400.00` | `4438.84` | `3978.40` | `4202.98` | 184,218.60 USD | `+11.58%` | `25X Isolated` |
| `1346` | `0x6d15...d374` | `LONG` | 1,591,200.00 USD | `400.00` | `4068.25` | `3978.40` | `3842.44` | -36,100.00 USD | `-2.27%` | `25X Cross` |
| `1377` | `0x51f6...2b39` | `LONG` | 1,559,264.84 USD | `391.48` | `4228.25` | `3982.78` | `599.39` | -96,010.85 USD | `-6.16%` | `10X Cross` |
| `1397` | `0x02a7...fe9f` | `SHORT` | 1,551,537.00 USD | `390.00` | `4055.02` | `3978.40` | `4307.31` | 29,922.25 USD | `+1.93%` | `25X Cross` |
| `1435` | `0x7e77...b8d2` | `SHORT` | 1,511,716.00 USD | `380.00` | `4131.92` | `3978.40` | `4294.11` | 58,413.64 USD | `+3.86%` | `20X Cross` |
| `1451` | `0x72c2...9b37` | `LONG` | 1,484,390.94 USD | `373.13` | `4000.98` | `3978.40` | `3778.67` | -8,502.58 USD | `-0.57%` | `13X Isolated` |
| `1466` | `0x781e...96b7` | `SHORT` | 1,457,046.90 USD | `365.84` | `4358.71` | `3982.78` | `12671.96` | 137,560.75 USD | `+9.44%` | `10X Cross` |
| `1500` | `0xaa44...b844` | `LONG` | 1,432,260.00 USD | `360.00` | `4043.10` | `3978.40` | `3225.88` | -23,257.63 USD | `-1.62%` | `7X Cross` |
| `1604` | `0xa41f...d50a` | `LONG` | 1,308,775.71 USD | `328.96` | `4468.89` | `3978.40` | `3802.79` | -161,322.14 USD | `-12.33%` | `15X Cross` |
| `1657` | `0xbf5a...88ba` | `SHORT` | 1,263,758.25 USD | `317.65` | `4091.80` | `3978.40` | `9954.79` | 36,024.78 USD | `+2.85%` | `20X Cross` |
| `1698` | `0xff31...ff6c` | `SHORT` | 1,233,242.00 USD | `310.00` | `4372.43` | `3978.40` | `4789.78` | 122,213.38 USD | `+9.91%` | `10X Isolated` |
| `1727` | `0xada6...6f88` | `LONG` | 1,207,250.43 USD | `303.47` | `4166.46` | `3978.40` | `1805.35` | -57,132.02 USD | `-4.73%` | `5X Cross` |
| `1886` | `0x50e2...d770` | `LONG` | 1,075,575.59 USD | `270.37` | `4243.58` | `3978.40` | `2562.72` | -71,750.87 USD | `-6.67%` | `20X Cross` |
| `1898` | `0x4c92...4f17` | `SHORT` | 1,061,094.17 USD | `266.72` | `4260.98` | `3978.40` | `6480.94` | 75,398.07 USD | `+7.11%` | `20X Cross` |
| `1968` | `0xd346...c4f3` | `LONG` | 1,015,157.93 USD | `255.17` | `4188.66` | `3978.40` | `3311.05` | -53,678.58 USD | `-5.29%` | `5X Isolated` |

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
| `7D` | `Long Liquidation` | `3584.80` | 15,080,000.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3585.20` | 5,710,000.00 USD | 5,710,000.00 USD | 6,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3589.10` | 15,070,000.00 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3589.40` | 5,700,000.00 USD | 5,700,000.00 USD | 2,640.00 USD | 0.00 USD | 9,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3593.40` | 15,050,000.00 USD | 15,050,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3593.60` | 5,690,000.00 USD | 5,690,000.00 USD | 22,620.00 USD | 0.00 USD | 22,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3597.70` | 15,040,000.00 USD | 15,040,000.00 USD | 108,500.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3597.80` | 5,640,000.00 USD | 5,640,000.00 USD | 16,880.00 USD | 0.00 USD | 18,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3602.00` | 5,610,000.00 USD | 5,610,000.00 USD | 31,900.00 USD | 0.00 USD | 36,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3602.00` | 14,910,000.00 USD | 14,910,000.00 USD | 173,930.00 USD | 0.00 USD | 75,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3606.20` | 5,540,000.00 USD | 5,540,000.00 USD | 55,280.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3606.30` | 14,660,000.00 USD | 14,660,000.00 USD | 152,940.00 USD | 0.00 USD | 46,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3610.40` | 5,450,000.00 USD | 5,450,000.00 USD | 21,410.00 USD | 0.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3610.60` | 14,460,000.00 USD | 14,460,000.00 USD | 72,480.00 USD | 0.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3614.60` | 5,430,000.00 USD | 5,430,000.00 USD | 34,930.00 USD | 0.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3614.90` | 14,370,000.00 USD | 14,370,000.00 USD | 76,990.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3618.80` | 5,380,000.00 USD | 5,380,000.00 USD | 40,180.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3619.20` | 14,280,000.00 USD | 14,280,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.00` | 5,330,000.00 USD | 5,330,000.00 USD | 64,700.00 USD | 0.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.50` | 14,220,000.00 USD | 14,220,000.00 USD | 45,130.00 USD | 0.00 USD | 22,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.20` | 5,260,000.00 USD | 5,260,000.00 USD | 23,440.00 USD | 0.00 USD | 3,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3627.80` | 14,150,000.00 USD | 14,150,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3631.40` | 5,230,000.00 USD | 5,230,000.00 USD | 6,520.00 USD | 0.00 USD | 2,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3632.10` | 14,050,000.00 USD | 14,050,000.00 USD | 60,720.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3635.60` | 5,220,000.00 USD | 5,220,000.00 USD | 9,410.00 USD | 0.00 USD | 204.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.40` | 13,980,000.00 USD | 13,980,000.00 USD | 20,410.00 USD | 0.00 USD | 6,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3639.80` | 5,210,000.00 USD | 5,210,000.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.70` | 13,960,000.00 USD | 13,960,000.00 USD | 55,830.00 USD | 0.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3645.00` | 13,890,000.00 USD | 13,890,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.30` | 13,850,000.00 USD | 13,850,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.60` | 13,830,000.00 USD | 13,830,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.90` | 13,800,000.00 USD | 13,800,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3662.20` | 13,770,000.00 USD | 13,770,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3666.50` | 13,740,000.00 USD | 13,740,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3820.40` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3824.60` | 5,200,000.00 USD | 5,200,000.00 USD | 17,190.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3825.60` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3828.80` | 5,170,000.00 USD | 5,170,000.00 USD | 6,610.00 USD | 0.00 USD | 28,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.90` | 13,710,000.00 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3833.00` | 5,130,000.00 USD | 5,130,000.00 USD | 67,910.00 USD | 0.00 USD | 76,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3834.20` | 13,630,000.00 USD | 13,630,000.00 USD | 86,270.00 USD | 0.00 USD | 34,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3837.20` | 4,990,000.00 USD | 4,990,000.00 USD | 51,070.00 USD | 0.00 USD | 78,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.50` | 13,510,000.00 USD | 13,510,000.00 USD | 334,470.00 USD | 0.00 USD | 99,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3841.40` | 4,860,000.00 USD | 4,860,000.00 USD | 96,370.00 USD | 0.00 USD | 107,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.80` | 13,070,000.00 USD | 13,070,000.00 USD | 569,120.00 USD | 0.00 USD | 199,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3845.60` | 4,650,000.00 USD | 4,650,000.00 USD | 181,310.00 USD | 0.00 USD | 112,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3847.10` | 12,300,000.00 USD | 12,300,000.00 USD | 461,180.00 USD | 0.00 USD | 150,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3849.80` | 4,360,000.00 USD | 4,360,000.00 USD | 35,100.00 USD | 0.00 USD | 21,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3851.40` | 11,690,000.00 USD | 11,690,000.00 USD | 257,490.00 USD | 0.00 USD | 74,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3854.00` | 4,300,000.00 USD | 4,300,000.00 USD | 118,550.00 USD | 0.00 USD | 34,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3855.70` | 11,360,000.00 USD | 11,360,000.00 USD | 221,360.00 USD | 0.00 USD | 47,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3858.20` | 4,150,000.00 USD | 4,150,000.00 USD | 97,440.00 USD | 0.00 USD | 25,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3860.00` | 11,090,000.00 USD | 11,090,000.00 USD | 147,250.00 USD | 0.00 USD | 28,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3862.40` | 4,030,000.00 USD | 4,030,000.00 USD | 167,880.00 USD | 0.00 USD | 32,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.30` | 10,910,000.00 USD | 10,910,000.00 USD | 232,560.00 USD | 0.00 USD | 75,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3866.60` | 3,830,000.00 USD | 3,830,000.00 USD | 169,760.00 USD | 0.00 USD | 23,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3868.60` | 10,610,000.00 USD | 10,610,000.00 USD | 285,320.00 USD | 0.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3870.80` | 3,640,000.00 USD | 3,640,000.00 USD | 91,780.00 USD | 0.00 USD | 11,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3872.90` | 10,290,000.00 USD | 10,290,000.00 USD | 221,120.00 USD | 0.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3875.00` | 3,530,000.00 USD | 3,530,000.00 USD | 24,900.00 USD | 0.00 USD | 3,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3877.20` | 10,030,000.00 USD | 10,030,000.00 USD | 153,170.00 USD | 0.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3879.20` | 3,500,000.00 USD | 3,500,000.00 USD | 30,410.00 USD | 0.00 USD | 510.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3881.50` | 9,850,000.00 USD | 9,850,000.00 USD | 96,090.00 USD | 0.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3883.40` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3885.80` | 9,730,000.00 USD | 9,730,000.00 USD | 124,650.00 USD | 0.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3890.10` | 9,580,000.00 USD | 9,580,000.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3894.40` | 9,470,000.00 USD | 9,470,000.00 USD | 126,480.00 USD | 0.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3898.70` | 9,330,000.00 USD | 9,330,000.00 USD | 132,740.00 USD | 0.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3900.20` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3903.00` | 9,190,000.00 USD | 9,190,000.00 USD | 17,060.00 USD | 0.00 USD | 74,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3904.40` | 3,450,000.00 USD | 3,450,000.00 USD | 34,370.00 USD | 0.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.30` | 9,100,000.00 USD | 9,100,000.00 USD | 56,630.00 USD | 0.00 USD | 98,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3908.60` | 3,390,000.00 USD | 3,390,000.00 USD | 13,220.00 USD | 0.00 USD | 57,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3911.60` | 8,950,000.00 USD | 8,950,000.00 USD | 51,010.00 USD | 0.00 USD | 81,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3912.80` | 3,320,000.00 USD | 3,320,000.00 USD | 135,830.00 USD | 0.00 USD | 152,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3915.90` | 8,810,000.00 USD | 8,810,000.00 USD | 287,340.00 USD | 0.00 USD | 173,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3917.00` | 3,030,000.00 USD | 3,030,000.00 USD | 102,140.00 USD | 0.00 USD | 156,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3920.20` | 8,350,000.00 USD | 8,350,000.00 USD | 731,980.00 USD | 0.00 USD | 181,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3921.20` | 2,770,000.00 USD | 2,770,000.00 USD | 174,380.00 USD | 0.00 USD | 199,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3924.50` | 7,440,000.00 USD | 7,440,000.00 USD | 1,280,000.00 USD | 0.00 USD | 465,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3925.40` | 2,400,000.00 USD | 2,400,000.00 USD | 380,980.00 USD | 0.00 USD | 230,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3928.80` | 5,690,000.00 USD | 5,690,000.00 USD | 812,760.00 USD | 0.00 USD | 199,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3929.60` | 1,790,000.00 USD | 1,790,000.00 USD | 70,210.00 USD | 0.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3933.10` | 4,680,000.00 USD | 4,680,000.00 USD | 340,890.00 USD | 0.00 USD | 133,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3933.80` | 1,660,000.00 USD | 1,660,000.00 USD | 195,060.00 USD | 0.00 USD | 66,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3937.40` | 4,210,000.00 USD | 4,210,000.00 USD | 466,400.00 USD | 0.00 USD | 56,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3938.00` | 1,400,000.00 USD | 1,400,000.00 USD | 212,430.00 USD | 0.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3941.70` | 3,680,000.00 USD | 3,680,000.00 USD | 312,800.00 USD | 0.00 USD | 114,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3942.20` | 1,140,000.00 USD | 1,140,000.00 USD | 311,730.00 USD | 0.00 USD | 62,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3946.00` | 3,260,000.00 USD | 3,260,000.00 USD | 494,480.00 USD | 0.00 USD | 111,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3946.40` | 764,920.00 USD | 764,920.00 USD | 348,200.00 USD | 0.00 USD | 44,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.30` | 2,650,000.00 USD | 2,650,000.00 USD | 498,180.00 USD | 0.00 USD | 72,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3950.60` | 372,060.00 USD | 372,060.00 USD | 217,030.00 USD | 0.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3954.60` | 2,080,000.00 USD | 2,080,000.00 USD | 417,480.00 USD | 0.00 USD | 53,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3954.80` | 134,800.00 USD | 134,800.00 USD | 45,900.00 USD | 0.00 USD | 15,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3958.90` | 1,610,000.00 USD | 1,610,000.00 USD | 275,800.00 USD | 0.00 USD | 41,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3959.00` | 73,340.00 USD | 73,340.00 USD | 71,090.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3963.20` | 606.18 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3963.20` | 1,290,000.00 USD | 1,290,000.00 USD | 303,170.00 USD | 0.00 USD | 57,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3967.50` | 930,280.00 USD | 930,280.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3971.80` | 753,000.00 USD | 753,000.00 USD | 218,900.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3976.10` | 488,070.00 USD | 488,070.00 USD | 237,870.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.40` | 236,810.00 USD | 236,810.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `3984.70` | 59,830.00 USD | 59,830.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `3989.00` | 110,560.00 USD | 110,560.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4059.80` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4062.10` | 171,510.00 USD | 171,510.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4064.00` | 82,620.00 USD | 82,620.00 USD | 34,370.00 USD | 0.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4066.40` | 259,800.00 USD | 259,800.00 USD | 0.00 USD | 0.00 USD | 88,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4068.20` | 153,690.00 USD | 153,690.00 USD | 13,220.00 USD | 0.00 USD | 57,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4070.70` | 373,790.00 USD | 373,790.00 USD | 34,460.00 USD | 0.00 USD | 79,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4072.40` | 400,660.00 USD | 400,660.00 USD | 99,190.00 USD | 0.00 USD | 147,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4075.00` | 655,770.00 USD | 655,770.00 USD | 138,080.00 USD | 0.00 USD | 143,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4076.60` | 692,460.00 USD | 692,460.00 USD | 138,780.00 USD | 0.00 USD | 153,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.30` | 1,630,000.00 USD | 1,630,000.00 USD | 793,160.00 USD | 0.00 USD | 181,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4080.80` | 1,050,000.00 USD | 1,050,000.00 USD | 174,380.00 USD | 0.00 USD | 178,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4083.60` | 3,170,000.00 USD | 3,170,000.00 USD | 1,120,000.00 USD | 0.00 USD | 427,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4085.00` | 1,650,000.00 USD | 1,650,000.00 USD | 360,440.00 USD | 0.00 USD | 245,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4087.90` | 4,200,000.00 USD | 4,200,000.00 USD | 819,620.00 USD | 0.00 USD | 209,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4089.20` | 1,770,000.00 USD | 1,770,000.00 USD | 76,430.00 USD | 0.00 USD | 39,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4092.20` | 4,890,000.00 USD | 4,890,000.00 USD | 535,480.00 USD | 0.00 USD | 149,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4093.40` | 2,020,000.00 USD | 2,020,000.00 USD | 171,390.00 USD | 0.00 USD | 76,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4096.50` | 5,380,000.00 USD | 5,380,000.00 USD | 394,180.00 USD | 0.00 USD | 95,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4097.60` | 2,260,000.00 USD | 2,260,000.00 USD | 193,650.00 USD | 0.00 USD | 49,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4100.80` | 5,740,000.00 USD | 5,740,000.00 USD | 322,520.00 USD | 0.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4101.80` | 2,580,000.00 USD | 2,580,000.00 USD | 272,900.00 USD | 0.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4105.10` | 6,290,000.00 USD | 6,290,000.00 USD | 408,250.00 USD | 0.00 USD | 134,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4106.00` | 3,050,000.00 USD | 3,050,000.00 USD | 406,530.00 USD | 0.00 USD | 63,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4109.40` | 6,870,000.00 USD | 6,870,000.00 USD | 504,830.00 USD | 0.00 USD | 76,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4110.20` | 3,270,000.00 USD | 3,270,000.00 USD | 186,300.00 USD | 0.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4113.70` | 7,370,000.00 USD | 7,370,000.00 USD | 437,970.00 USD | 0.00 USD | 63,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4114.40` | 3,380,000.00 USD | 3,380,000.00 USD | 101,250.00 USD | 0.00 USD | 15,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4118.00` | 7,710,000.00 USD | 7,710,000.00 USD | 282,440.00 USD | 0.00 USD | 57,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4118.60` | 3,440,000.00 USD | 3,440,000.00 USD | 55,480.00 USD | 0.00 USD | 4,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.30` | 8,030,000.00 USD | 8,030,000.00 USD | 286,850.00 USD | 0.00 USD | 30,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4122.80` | 3,470,000.00 USD | 3,470,000.00 USD | 28,250.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4126.60` | 8,330,000.00 USD | 8,330,000.00 USD | 221,890.00 USD | 0.00 USD | 86,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4130.90` | 8,550,000.00 USD | 8,550,000.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4135.20` | 8,780,000.00 USD | 8,780,000.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4139.50` | 8,990,000.00 USD | 8,990,000.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4139.60` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4143.80` | 3,510,000.00 USD | 3,510,000.00 USD | 17,190.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4143.80` | 9,240,000.00 USD | 9,240,000.00 USD | 199,160.00 USD | 0.00 USD | 50,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4148.00` | 3,550,000.00 USD | 3,550,000.00 USD | 6,610.00 USD | 0.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4148.10` | 9,390,000.00 USD | 9,390,000.00 USD | 59,830.00 USD | 0.00 USD | 88,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4152.20` | 3,670,000.00 USD | 3,670,000.00 USD | 49,590.00 USD | 0.00 USD | 72,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4152.40` | 9,590,000.00 USD | 9,590,000.00 USD | 133,610.00 USD | 0.00 USD | 66,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4156.40` | 3,820,000.00 USD | 3,820,000.00 USD | 69,390.00 USD | 0.00 USD | 75,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4156.70` | 9,910,000.00 USD | 9,910,000.00 USD | 268,170.00 USD | 0.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4160.60` | 4,000,000.00 USD | 4,000,000.00 USD | 87,190.00 USD | 0.00 USD | 90,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4161.00` | 10,470,000.00 USD | 10,470,000.00 USD | 420,240.00 USD | 0.00 USD | 134,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4164.80` | 4,290,000.00 USD | 4,290,000.00 USD | 171,460.00 USD | 0.00 USD | 122,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.30` | 11,160,000.00 USD | 11,160,000.00 USD | 485,080.00 USD | 0.00 USD | 204,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4169.00` | 4,350,000.00 USD | 4,350,000.00 USD | 46,980.00 USD | 0.00 USD | 18,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.60` | 11,640,000.00 USD | 11,640,000.00 USD | 401,230.00 USD | 0.00 USD | 82,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4173.20` | 4,470,000.00 USD | 4,470,000.00 USD | 74,610.00 USD | 0.00 USD | 36,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4173.90` | 11,860,000.00 USD | 11,860,000.00 USD | 156,630.00 USD | 0.00 USD | 66,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4177.40` | 4,600,000.00 USD | 4,600,000.00 USD | 102,960.00 USD | 0.00 USD | 27,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4178.20` | 12,130,000.00 USD | 12,130,000.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4181.60` | 4,750,000.00 USD | 4,750,000.00 USD | 132,520.00 USD | 0.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.50` | 12,310,000.00 USD | 12,310,000.00 USD | 143,730.00 USD | 0.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4185.80` | 4,920,000.00 USD | 4,920,000.00 USD | 134,870.00 USD | 0.00 USD | 29,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.80` | 12,590,000.00 USD | 12,590,000.00 USD | 219,060.00 USD | 0.00 USD | 65,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4190.00` | 5,070,000.00 USD | 5,070,000.00 USD | 132,820.00 USD | 0.00 USD | 17,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4191.10` | 12,880,000.00 USD | 12,880,000.00 USD | 254,710.00 USD | 0.00 USD | 31,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4194.20` | 5,160,000.00 USD | 5,160,000.00 USD | 88,240.00 USD | 0.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.40` | 13,120,000.00 USD | 13,120,000.00 USD | 205,140.00 USD | 0.00 USD | 33,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4198.40` | 5,180,000.00 USD | 5,180,000.00 USD | 11,450.00 USD | 0.00 USD | 3,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.70` | 13,290,000.00 USD | 13,290,000.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4202.60` | 5,210,000.00 USD | 5,210,000.00 USD | 30,410.00 USD | 0.00 USD | 510.84 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4204.00` | 13,430,000.00 USD | 13,430,000.00 USD | 116,920.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4206.80` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.30` | 13,550,000.00 USD | 13,550,000.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4212.60` | 13,650,000.00 USD | 13,650,000.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.90` | 13,770,000.00 USD | 13,770,000.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4221.20` | 13,890,000.00 USD | 13,890,000.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4225.50` | 13,980,000.00 USD | 13,980,000.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4229.80` | 14,020,000.00 USD | 14,020,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4234.10` | 14,070,000.00 USD | 14,070,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4238.40` | 14,090,000.00 USD | 14,090,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4379.00` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4380.30` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4383.20` | 5,230,000.00 USD | 5,230,000.00 USD | 6,870.00 USD | 0.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4387.40` | 5,240,000.00 USD | 5,240,000.00 USD | 2,640.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4388.90` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4391.60` | 5,270,000.00 USD | 5,270,000.00 USD | 15,290.00 USD | 0.00 USD | 21,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4393.20` | 14,150,000.00 USD | 14,150,000.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4395.80` | 5,320,000.00 USD | 5,320,000.00 USD | 24,210.00 USD | 0.00 USD | 16,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4397.50` | 14,260,000.00 USD | 14,260,000.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4400.00` | 5,360,000.00 USD | 5,360,000.00 USD | 18,280.00 USD | 0.00 USD | 22,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4401.80` | 14,470,000.00 USD | 14,470,000.00 USD | 143,560.00 USD | 0.00 USD | 66,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4404.20` | 5,450,000.00 USD | 5,450,000.00 USD | 59,490.00 USD | 0.00 USD | 37,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4404.80` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4406.10` | 14,640,000.00 USD | 14,640,000.00 USD | 125,560.00 USD | 0.00 USD | 48,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4410.40` | 14,760,000.00 USD | 14,760,000.00 USD | 103,520.00 USD | 0.00 USD | 18,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4414.70` | 14,820,000.00 USD | 14,820,000.00 USD | 36,920.00 USD | 0.00 USD | 17,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4419.00` | 14,890,000.00 USD | 14,890,000.00 USD | 66,780.00 USD | 0.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.30` | 14,950,000.00 USD | 14,950,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4424.00` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 6,020.00 USD | `Tier 1 CEX` |

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
| `1D` | `3585.20` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 6,870.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3589.10` | 15,070,000.00 USD | 0.00 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3589.40` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 2,640.00 USD | 0.00 USD | 9,480.00 USD |
| `7D` | `3593.40` | 15,050,000.00 USD | 0.00 USD | 15,050,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `3593.60` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 22,620.00 USD | 0.00 USD | 22,620.00 USD |
| `7D` | `3597.70` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 108,500.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `3597.80` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 16,880.00 USD | 0.00 USD | 18,980.00 USD |
| `1D` | `3602.00` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 31,900.00 USD | 0.00 USD | 36,250.00 USD |
| `7D` | `3602.00` | 14,910,000.00 USD | 0.00 USD | 14,910,000.00 USD | 173,930.00 USD | 0.00 USD | 75,620.00 USD |
| `1D` | `3606.20` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 55,280.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `3606.30` | 14,660,000.00 USD | 0.00 USD | 14,660,000.00 USD | 152,940.00 USD | 0.00 USD | 46,290.00 USD |
| `1D` | `3610.40` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 21,410.00 USD | 0.00 USD | 5,060.00 USD |
| `7D` | `3610.60` | 14,460,000.00 USD | 0.00 USD | 14,460,000.00 USD | 72,480.00 USD | 0.00 USD | 20,480.00 USD |
| `1D` | `3614.60` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 34,930.00 USD | 0.00 USD | 11,100.00 USD |
| `7D` | `3614.90` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 76,990.00 USD | 0.00 USD | 16,470.00 USD |
| `1D` | `3618.80` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 40,180.00 USD | 0.00 USD | 7,360.00 USD |
| `7D` | `3619.20` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 45,440.00 USD | 0.00 USD | 10,660.00 USD |
| `1D` | `3623.00` | 5,330,000.00 USD | 0.00 USD | 5,330,000.00 USD | 64,700.00 USD | 0.00 USD | 10,200.00 USD |
| `7D` | `3623.50` | 14,220,000.00 USD | 0.00 USD | 14,220,000.00 USD | 45,130.00 USD | 0.00 USD | 22,740.00 USD |
| `1D` | `3627.20` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 23,440.00 USD | 0.00 USD | 3,910.00 USD |
| `7D` | `3627.80` | 14,150,000.00 USD | 0.00 USD | 14,150,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD |
| `1D` | `3631.40` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 6,520.00 USD | 0.00 USD | 2,710.00 USD |
| `7D` | `3632.10` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 60,720.00 USD | 0.00 USD | 7,710.00 USD |
| `1D` | `3635.60` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 9,410.00 USD | 0.00 USD | 204.34 USD |
| `7D` | `3636.40` | 13,980,000.00 USD | 0.00 USD | 13,980,000.00 USD | 20,410.00 USD | 0.00 USD | 6,070.00 USD |
| `1D` | `3639.80` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3640.70` | 13,960,000.00 USD | 0.00 USD | 13,960,000.00 USD | 55,830.00 USD | 0.00 USD | 8,700.00 USD |
| `7D` | `3645.00` | 13,890,000.00 USD | 0.00 USD | 13,890,000.00 USD | 23,870.00 USD | 0.00 USD | 12,380.00 USD |
| `7D` | `3649.30` | 13,850,000.00 USD | 0.00 USD | 13,850,000.00 USD | 18,710.00 USD | 0.00 USD | 2,250.00 USD |
| `7D` | `3653.60` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3657.90` | 13,800,000.00 USD | 0.00 USD | 13,800,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3662.20` | 13,770,000.00 USD | 0.00 USD | 13,770,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3666.50` | 13,740,000.00 USD | 0.00 USD | 13,740,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3820.40` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `1D` | `3824.60` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 17,190.00 USD | 0.00 USD | 14,430.00 USD |
| `7D` | `3825.60` | 13,740,000.00 USD | 0.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD |
| `1D` | `3828.80` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 6,610.00 USD | 0.00 USD | 28,920.00 USD |
| `7D` | `3829.90` | 13,710,000.00 USD | 0.00 USD | 13,710,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD |
| `1D` | `3833.00` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 67,910.00 USD | 0.00 USD | 76,090.00 USD |
| `7D` | `3834.20` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 86,270.00 USD | 0.00 USD | 34,180.00 USD |
| `1D` | `3837.20` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 51,070.00 USD | 0.00 USD | 78,330.00 USD |
| `7D` | `3838.50` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 334,470.00 USD | 0.00 USD | 99,980.00 USD |
| `1D` | `3841.40` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 96,370.00 USD | 0.00 USD | 107,690.00 USD |
| `7D` | `3842.80` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 569,120.00 USD | 0.00 USD | 199,760.00 USD |
| `1D` | `3845.60` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 181,310.00 USD | 0.00 USD | 112,390.00 USD |
| `7D` | `3847.10` | 12,300,000.00 USD | 0.00 USD | 12,300,000.00 USD | 461,180.00 USD | 0.00 USD | 150,800.00 USD |
| `1D` | `3849.80` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 35,100.00 USD | 0.00 USD | 21,580.00 USD |
| `7D` | `3851.40` | 11,690,000.00 USD | 0.00 USD | 11,690,000.00 USD | 257,490.00 USD | 0.00 USD | 74,890.00 USD |
| `1D` | `3854.00` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 118,550.00 USD | 0.00 USD | 34,440.00 USD |
| `7D` | `3855.70` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 221,360.00 USD | 0.00 USD | 47,670.00 USD |
| `1D` | `3858.20` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 97,440.00 USD | 0.00 USD | 25,060.00 USD |
| `7D` | `3860.00` | 11,090,000.00 USD | 0.00 USD | 11,090,000.00 USD | 147,250.00 USD | 0.00 USD | 28,510.00 USD |
| `1D` | `3862.40` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 167,880.00 USD | 0.00 USD | 32,250.00 USD |
| `7D` | `3864.30` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 232,560.00 USD | 0.00 USD | 75,710.00 USD |
| `1D` | `3866.60` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 169,760.00 USD | 0.00 USD | 23,260.00 USD |
| `7D` | `3868.60` | 10,610,000.00 USD | 0.00 USD | 10,610,000.00 USD | 285,320.00 USD | 0.00 USD | 26,240.00 USD |
| `1D` | `3870.80` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 91,780.00 USD | 0.00 USD | 11,380.00 USD |
| `7D` | `3872.90` | 10,290,000.00 USD | 0.00 USD | 10,290,000.00 USD | 221,120.00 USD | 0.00 USD | 41,690.00 USD |
| `1D` | `3875.00` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 24,900.00 USD | 0.00 USD | 3,730.00 USD |
| `7D` | `3877.20` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 153,170.00 USD | 0.00 USD | 23,330.00 USD |
| `1D` | `3879.20` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 30,410.00 USD | 0.00 USD | 510.84 USD |
| `7D` | `3881.50` | 9,850,000.00 USD | 0.00 USD | 9,850,000.00 USD | 96,090.00 USD | 0.00 USD | 27,510.00 USD |
| `1D` | `3883.40` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `3885.80` | 9,730,000.00 USD | 0.00 USD | 9,730,000.00 USD | 124,650.00 USD | 0.00 USD | 30,910.00 USD |
| `7D` | `3890.10` | 9,580,000.00 USD | 0.00 USD | 9,580,000.00 USD | 85,430.00 USD | 0.00 USD | 19,460.00 USD |
| `7D` | `3894.40` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 126,480.00 USD | 0.00 USD | 10,240.00 USD |
| `7D` | `3898.70` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 132,740.00 USD | 0.00 USD | 8,380.00 USD |
| `1D` | `3900.20` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `3903.00` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 17,060.00 USD | 0.00 USD | 74,030.00 USD |
| `1D` | `3904.40` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 34,370.00 USD | 0.00 USD | 28,860.00 USD |
| `7D` | `3907.30` | 9,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 56,630.00 USD | 0.00 USD | 98,910.00 USD |
| `1D` | `3908.60` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 13,220.00 USD | 0.00 USD | 57,840.00 USD |
| `7D` | `3911.60` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 51,010.00 USD | 0.00 USD | 81,430.00 USD |
| `1D` | `3912.80` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 135,830.00 USD | 0.00 USD | 152,180.00 USD |
| `7D` | `3915.90` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 287,340.00 USD | 0.00 USD | 173,650.00 USD |
| `1D` | `3917.00` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 102,140.00 USD | 0.00 USD | 156,660.00 USD |
| `7D` | `3920.20` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 731,980.00 USD | 0.00 USD | 181,350.00 USD |
| `1D` | `3921.20` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 174,380.00 USD | 0.00 USD | 199,180.00 USD |
| `7D` | `3924.50` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 1,280,000.00 USD | 0.00 USD | 465,510.00 USD |
| `1D` | `3925.40` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 380,980.00 USD | 0.00 USD | 230,070.00 USD |
| `7D` | `3928.80` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 812,760.00 USD | 0.00 USD | 199,680.00 USD |
| `1D` | `3929.60` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 70,210.00 USD | 0.00 USD | 53,310.00 USD |
| `7D` | `3933.10` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 340,890.00 USD | 0.00 USD | 133,810.00 USD |
| `1D` | `3933.80` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 195,060.00 USD | 0.00 USD | 66,400.00 USD |
| `7D` | `3937.40` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 466,400.00 USD | 0.00 USD | 56,370.00 USD |
| `1D` | `3938.00` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 212,430.00 USD | 0.00 USD | 51,000.00 USD |
| `7D` | `3941.70` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 312,800.00 USD | 0.00 USD | 114,460.00 USD |
| `1D` | `3942.20` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 311,730.00 USD | 0.00 USD | 62,500.00 USD |
| `7D` | `3946.00` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 494,480.00 USD | 0.00 USD | 111,080.00 USD |
| `1D` | `3946.40` | 764,920.00 USD | 0.00 USD | 764,920.00 USD | 348,200.00 USD | 0.00 USD | 44,660.00 USD |
| `7D` | `3950.30` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 498,180.00 USD | 0.00 USD | 72,590.00 USD |
| `1D` | `3950.60` | 372,060.00 USD | 0.00 USD | 372,060.00 USD | 217,030.00 USD | 0.00 USD | 20,230.00 USD |
| `7D` | `3954.60` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 417,480.00 USD | 0.00 USD | 53,640.00 USD |
| `1D` | `3954.80` | 134,800.00 USD | 0.00 USD | 134,800.00 USD | 45,900.00 USD | 0.00 USD | 15,560.00 USD |
| `7D` | `3958.90` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 275,800.00 USD | 0.00 USD | 41,700.00 USD |
| `1D` | `3959.00` | 73,340.00 USD | 0.00 USD | 73,340.00 USD | 71,090.00 USD | 0.00 USD | 1,650.00 USD |
| `1D` | `3963.20` | 606.18 USD | 0.00 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `3963.20` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 303,170.00 USD | 0.00 USD | 57,060.00 USD |
| `7D` | `3967.50` | 930,280.00 USD | 0.00 USD | 930,280.00 USD | 123,140.00 USD | 0.00 USD | 54,140.00 USD |
| `7D` | `3971.80` | 753,000.00 USD | 0.00 USD | 753,000.00 USD | 218,900.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `3976.10` | 488,070.00 USD | 0.00 USD | 488,070.00 USD | 237,870.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `3980.40` | 236,810.00 USD | 0.00 USD | 236,810.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD |
| `1D` | `3984.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3984.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3984.70` | 59,830.00 USD | 59,830.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3989.00` | 110,560.00 USD | 110,560.00 USD | 0.00 USD | 50,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4059.80` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `4062.10` | 171,510.00 USD | 171,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD |
| `1D` | `4064.00` | 82,620.00 USD | 82,620.00 USD | 0.00 USD | 34,370.00 USD | 0.00 USD | 28,860.00 USD |
| `7D` | `4066.40` | 259,800.00 USD | 259,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 88,290.00 USD |
| `1D` | `4068.20` | 153,690.00 USD | 153,690.00 USD | 0.00 USD | 13,220.00 USD | 0.00 USD | 57,840.00 USD |
| `7D` | `4070.70` | 373,790.00 USD | 373,790.00 USD | 0.00 USD | 34,460.00 USD | 0.00 USD | 79,530.00 USD |
| `1D` | `4072.40` | 400,660.00 USD | 400,660.00 USD | 0.00 USD | 99,190.00 USD | 0.00 USD | 147,780.00 USD |
| `7D` | `4075.00` | 655,770.00 USD | 655,770.00 USD | 0.00 USD | 138,080.00 USD | 0.00 USD | 143,900.00 USD |
| `1D` | `4076.60` | 692,460.00 USD | 692,460.00 USD | 0.00 USD | 138,780.00 USD | 0.00 USD | 153,020.00 USD |
| `7D` | `4079.30` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 793,160.00 USD | 0.00 USD | 181,320.00 USD |
| `1D` | `4080.80` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 174,380.00 USD | 0.00 USD | 178,190.00 USD |
| `7D` | `4083.60` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 427,200.00 USD |
| `1D` | `4085.00` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 360,440.00 USD | 0.00 USD | 245,410.00 USD |
| `7D` | `4087.90` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 819,620.00 USD | 0.00 USD | 209,710.00 USD |
| `1D` | `4089.20` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 76,430.00 USD | 0.00 USD | 39,990.00 USD |
| `7D` | `4092.20` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 535,480.00 USD | 0.00 USD | 149,790.00 USD |
| `1D` | `4093.40` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 171,390.00 USD | 0.00 USD | 76,690.00 USD |
| `7D` | `4096.50` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 394,180.00 USD | 0.00 USD | 95,350.00 USD |
| `1D` | `4097.60` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 193,650.00 USD | 0.00 USD | 49,460.00 USD |
| `7D` | `4100.80` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 322,520.00 USD | 0.00 USD | 42,790.00 USD |
| `1D` | `4101.80` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 272,900.00 USD | 0.00 USD | 48,030.00 USD |
| `7D` | `4105.10` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 408,250.00 USD | 0.00 USD | 134,430.00 USD |
| `1D` | `4106.00` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 406,530.00 USD | 0.00 USD | 63,100.00 USD |
| `7D` | `4109.40` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 504,830.00 USD | 0.00 USD | 76,750.00 USD |
| `1D` | `4110.20` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 186,300.00 USD | 0.00 USD | 31,430.00 USD |
| `7D` | `4113.70` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 437,970.00 USD | 0.00 USD | 63,950.00 USD |
| `1D` | `4114.40` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 101,250.00 USD | 0.00 USD | 15,670.00 USD |
| `7D` | `4118.00` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 282,440.00 USD | 0.00 USD | 57,050.00 USD |
| `1D` | `4118.60` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 55,480.00 USD | 0.00 USD | 4,620.00 USD |
| `7D` | `4122.30` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 286,850.00 USD | 0.00 USD | 30,750.00 USD |
| `1D` | `4122.80` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 28,250.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `4126.60` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 221,890.00 USD | 0.00 USD | 86,130.00 USD |
| `7D` | `4130.90` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 174,770.00 USD | 0.00 USD | 43,610.00 USD |
| `7D` | `4135.20` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 209,230.00 USD | 0.00 USD | 18,350.00 USD |
| `7D` | `4139.50` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4139.60` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `1D` | `4143.80` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 17,190.00 USD | 0.00 USD | 14,430.00 USD |
| `7D` | `4143.80` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 199,160.00 USD | 0.00 USD | 50,830.00 USD |
| `1D` | `4148.00` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 6,610.00 USD | 0.00 USD | 30,420.00 USD |
| `7D` | `4148.10` | 9,390,000.00 USD | 9,390,000.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 88,440.00 USD |
| `1D` | `4152.20` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 49,590.00 USD | 0.00 USD | 72,390.00 USD |
| `7D` | `4152.40` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 133,610.00 USD | 0.00 USD | 66,470.00 USD |
| `1D` | `4156.40` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 69,390.00 USD | 0.00 USD | 75,320.00 USD |
| `7D` | `4156.70` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 268,170.00 USD | 0.00 USD | 57,810.00 USD |
| `1D` | `4160.60` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 87,190.00 USD | 0.00 USD | 90,280.00 USD |
| `7D` | `4161.00` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 420,240.00 USD | 0.00 USD | 134,730.00 USD |
| `1D` | `4164.80` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 171,460.00 USD | 0.00 USD | 122,710.00 USD |
| `7D` | `4165.30` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 485,080.00 USD | 0.00 USD | 204,730.00 USD |
| `1D` | `4169.00` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 46,980.00 USD | 0.00 USD | 18,580.00 USD |
| `7D` | `4169.60` | 11,640,000.00 USD | 11,640,000.00 USD | 0.00 USD | 401,230.00 USD | 0.00 USD | 82,290.00 USD |
| `1D` | `4173.20` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 74,610.00 USD | 0.00 USD | 36,700.00 USD |
| `7D` | `4173.90` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 156,630.00 USD | 0.00 USD | 66,900.00 USD |
| `1D` | `4177.40` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 102,960.00 USD | 0.00 USD | 27,790.00 USD |
| `7D` | `4178.20` | 12,130,000.00 USD | 12,130,000.00 USD | 0.00 USD | 233,200.00 USD | 0.00 USD | 28,180.00 USD |
| `1D` | `4181.60` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 132,520.00 USD | 0.00 USD | 23,210.00 USD |
| `7D` | `4182.50` | 12,310,000.00 USD | 12,310,000.00 USD | 0.00 USD | 143,730.00 USD | 0.00 USD | 40,030.00 USD |
| `1D` | `4185.80` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 134,870.00 USD | 0.00 USD | 29,330.00 USD |
| `7D` | `4186.80` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 219,060.00 USD | 0.00 USD | 65,350.00 USD |
| `1D` | `4190.00` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 132,820.00 USD | 0.00 USD | 17,250.00 USD |
| `7D` | `4191.10` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 254,710.00 USD | 0.00 USD | 31,760.00 USD |
| `1D` | `4194.20` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 88,240.00 USD | 0.00 USD | 8,060.00 USD |
| `7D` | `4195.40` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 205,140.00 USD | 0.00 USD | 33,460.00 USD |
| `1D` | `4198.40` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 11,450.00 USD | 0.00 USD | 3,070.00 USD |
| `7D` | `4199.70` | 13,290,000.00 USD | 13,290,000.00 USD | 0.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD |
| `1D` | `4202.60` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 30,410.00 USD | 0.00 USD | 510.84 USD |
| `7D` | `4204.00` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 116,920.00 USD | 0.00 USD | 23,560.00 USD |
| `1D` | `4206.80` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `4208.30` | 13,550,000.00 USD | 13,550,000.00 USD | 0.00 USD | 92,450.00 USD | 0.00 USD | 32,380.00 USD |
| `7D` | `4212.60` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 77,790.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `4216.90` | 13,770,000.00 USD | 13,770,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 10,670.00 USD |
| `7D` | `4221.20` | 13,890,000.00 USD | 13,890,000.00 USD | 0.00 USD | 120,590.00 USD | 0.00 USD | 5,480.00 USD |
| `7D` | `4225.50` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD |
| `7D` | `4229.80` | 14,020,000.00 USD | 14,020,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `7D` | `4234.10` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4238.40` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4379.00` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `4380.30` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `4383.20` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 6,870.00 USD | 0.00 USD | 7,540.00 USD |
| `1D` | `4387.40` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 2,640.00 USD | 0.00 USD | 7,710.00 USD |
| `7D` | `4388.90` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4391.60` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 15,290.00 USD | 0.00 USD | 21,740.00 USD |
| `7D` | `4393.20` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `4395.80` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 24,210.00 USD | 0.00 USD | 16,740.00 USD |
| `7D` | `4397.50` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `4400.00` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 18,280.00 USD | 0.00 USD | 22,080.00 USD |
| `7D` | `4401.80` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 143,560.00 USD | 0.00 USD | 66,400.00 USD |
| `1D` | `4404.20` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 59,490.00 USD | 0.00 USD | 37,570.00 USD |
| `1D` | `4404.80` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,580.00 USD |
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
  * Total Open Interest: `274.53M` | Total OI Tokens: `68,913.3 PAXG`
  * 1h OI Change: `-0.17%` | 4h OI Change: `-0.92%` | 24h OI Change: `-0.20%`
  * Exchange Breakdown: Binance=`104.56M` | Bybit=`24.59M` | OKX=`-` | Hyperliquid=`24.67M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.06K` | Last 24h: `17.74K` | Last 3d: `85.70K` | Last 7d: `216.77K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0008%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `0.0008%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0026%` | **USDT Bitget** | `0.0034%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `41.27%` | `58.73%` | `0.70` | 1,430,000.00 USD |
| `15M` | `Binance` | `47.18%` | `52.82%` | `0.89` | 619,340.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `61.77%` | `38.23%` | `1.62` | 107,070.00 USD |
| `15M` | `KuCoin` | `23.59%` | `76.41%` | `0.31` | 121,940.00 USD |
| `15M` | `Gate` | `63.25%` | `36.75%` | `1.72` | 34,920.00 USD |
| `15M` | `Bitget` | `44.36%` | `55.64%` | `0.80` | 322,030.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `21.19%` | `78.81%` | `0.27` | 6,880.00 USD |
| `15M` | `Bitunix` | `69.19%` | `30.81%` | `2.25` | 17,850.00 USD |
| `15M` | `Hyperliquid` | `16.62%` | `83.38%` | `0.20` | 34,420.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `9.71%` | `90.29%` | `0.11` | 150,850.00 USD |
| `15M` | `HTX` | `13.1%` | `86.9%` | `0.15` | 1,150.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `14.7%` | `85.3%` | `0.17` | 4,090.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 7.97 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `32.04%` | `67.96%` | `0.47` | 8,020.00 USD |
| `15M` | `Whale Positions` | `47.18%` | `52.82%` | `0.89` | 619,340.00 USD |
| `15M` | `Global Accounts` | `41.27%` | `58.73%` | `0.70` | 1,430,000.00 USD |
| `1H` | `PAXG` | `38.06%` | `61.94%` | `0.61` | 5,270,000.00 USD |
| `1H` | `Binance` | `42.1%` | `57.9%` | `0.73` | 2,730,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `62.42%` | `37.58%` | `1.66` | 326,290.00 USD |
| `1H` | `KuCoin` | `40.52%` | `59.48%` | `0.68` | 309,960.00 USD |
| `1H` | `Gate` | `56.02%` | `43.98%` | `1.27` | 97,530.00 USD |
| `1H` | `Bitget` | `43.79%` | `56.21%` | `0.78` | 829,830.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `26.63%` | `73.37%` | `0.36` | 25,660.00 USD |
| `1H` | `Bitunix` | `47.37%` | `52.63%` | `0.90` | 65,280.00 USD |
| `1H` | `Hyperliquid` | `28.03%` | `71.97%` | `0.39` | 83,480.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `3.1%` | `96.9%` | `0.03` | 722,200.00 USD |
| `1H` | `HTX` | `20.06%` | `79.94%` | `0.25` | 3,480.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `11.36%` | `88.64%` | `0.13` | 23,440.00 USD |
| `1H` | `Aster` | `42.42%` | `57.58%` | `0.74` | 1,820.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `42.29%` | `57.71%` | `0.73` | 44,440.00 USD |
| `1H` | `Whale Positions` | `42.1%` | `57.9%` | `0.73` | 2,730,000.00 USD |
| `1H` | `Global Accounts` | `38.06%` | `61.94%` | `0.61` | 5,270,000.00 USD |
| `4H` | `PAXG` | `46.28%` | `53.72%` | `0.86` | 32,170,000.00 USD |
| `4H` | `Binance` | `47.78%` | `52.22%` | `0.91` | 18,060,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `59.5%` | `40.5%` | `1.47` | 3,120,000.00 USD |
| `4H` | `KuCoin` | `43.34%` | `56.66%` | `0.76` | 1,840,000.00 USD |
| `4H` | `Gate` | `41.83%` | `58.17%` | `0.72` | 1,310,000.00 USD |
| `4H` | `Bitget` | `47.23%` | `52.77%` | `0.90` | 3,780,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `32.34%` | `67.66%` | `0.48` | 173,290.00 USD |
| `4H` | `Bitunix` | `48.35%` | `51.65%` | `0.94` | 566,500.00 USD |
| `4H` | `Hyperliquid` | `57.79%` | `42.21%` | `1.37` | 807,490.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `11.97%` | `88.03%` | `0.14` | 1,980,000.00 USD |
| `4H` | `HTX` | `18.91%` | `81.09%` | `0.23` | 120,150.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `35.85%` | `64.15%` | `0.56` | 106,170.00 USD |
| `4H` | `Aster` | `46.18%` | `53.82%` | `0.86` | 172,330.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `76.01%` | `23.99%` | `3.17` | 119,150.00 USD |
| `4H` | `Whale Positions` | `47.78%` | `52.22%` | `0.91` | 18,060,000.00 USD |
| `4H` | `Global Accounts` | `46.28%` | `53.72%` | `0.86` | 32,170,000.00 USD |


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
| `5m` | -30,190.00 USD | -68,660.00 USD | **`DISTRIBUTION`** |
| `15m` | -73,630.00 USD | -55,360.00 USD | **`DISTRIBUTION`** |
| `30m` | -105,920.00 USD | -114,130.00 USD | **`DISTRIBUTION`** |
| `1h` | -201,270.00 USD | -388,850.00 USD | **`DISTRIBUTION`** |
| `2h` | -667,870.00 USD | -330,640.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,720,000.00 USD | -353,500.00 USD | **`DISTRIBUTION`** |
| `6h` | -112,520.00 USD | 217,280.00 USD | **`ACCUMULATION`** |
| `8h` | -252,590.00 USD | 23,580.00 USD | **`DISTRIBUTION`** |
| `12h` | -102,280.00 USD | -1,080,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,400,000.00 USD | 835,470.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,750,000.00 USD | -8,290,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,450,000.00 USD | -71,200,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-30.19K` | 15m=`-73.63K` | 1h=`-201.27K` | 24h=`-1.40M`
* Futures Capital Netflows: 5m=`-68.66K` | 15m=`-55.36K` | 1h=`-388.85K` | 24h=`+835.47K`
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
  * `2026-10-30 16:26:21 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:29:21 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `3973.24` (Risk Distance: `9.19` pts)
  * +2.5R Take Profit: `4005.42`
  * Mathematical Lot Sizing: **`1.08 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4007.93` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4017.12` (Risk Distance: `9.19` pts)
  * +2.5R Take Profit: `3984.94`
  * Mathematical Lot Sizing: **`1.08 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4006.48`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
