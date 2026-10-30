# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAUSGD
**Canonical Key**: `XAUSGD` | **Broker Instrument**: `XAUSGD.pi` | **Asset Class**: `Forex Exotic`
**Timestamp**: `2026-10-30 16:27:43 IST` (`2026-10-30 10:57:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `5075.96` | **Live Ask Quote**: `5076.33` | **Mid Price**: `5076.15`
- **Spread Points**: `37.00` | **Spread BPS**: `0.73 bps` (Charter Threshold: `5.00 bps`)
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
  * Golden Pocket Zone (0.618 - 0.650): `5055.84` - `5096.45`
  * Optimal Trade Entry (OTE 0.705): `5086.30`
  * Structural Invalidation Anchor (0.786): `5116.75`

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
| `1217` | `0xead5...69f2` | `LONG` | 1,805,379.25 USD | `453.78` | `4220.88` | `3978.40` | `3539.57` | -109,988.81 USD | `-6.09%` | `5X Isolated` |
| `1298` | `0x46fc...1195` | `LONG` | 1,661,407.69 USD | `417.61` | `4051.00` | `3978.40` | `2268.35` | -30,321.69 USD | `-1.83%` | `20X Cross` |
| `1345` | `0xee02...309d` | `SHORT` | 1,591,320.00 USD | `400.00` | `4438.84` | `3978.40` | `4202.98` | 184,218.60 USD | `+11.58%` | `25X Isolated` |
| `1346` | `0x6d15...d374` | `LONG` | 1,591,200.00 USD | `400.00` | `4068.25` | `3978.40` | `3842.44` | -36,100.00 USD | `-2.27%` | `25X Cross` |
| `1397` | `0x02a7...fe9f` | `SHORT` | 1,551,537.00 USD | `390.00` | `4055.02` | `3978.40` | `4307.31` | 29,922.25 USD | `+1.93%` | `25X Cross` |
| `1435` | `0x7e77...b8d2` | `SHORT` | 1,511,716.00 USD | `380.00` | `4131.92` | `3978.40` | `4294.11` | 58,413.64 USD | `+3.86%` | `20X Cross` |
| `1451` | `0x72c2...9b37` | `LONG` | 1,484,390.94 USD | `373.13` | `4000.98` | `3978.40` | `3778.67` | -8,502.58 USD | `-0.57%` | `13X Isolated` |
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
  * 24H Horizon: Short MP=`4071.25` (Vol: 14,000,000.00 USD, Dist: `+2.13%`) | Long MP=`3950.06` (Vol: 10,500,000.00 USD, Dist: `--0.91%`)
  * 48H Horizon: Short MP=`4076.12` (Vol: 15,300,000.00 USD, Dist: `+2.25%`) | Long MP=`3969.36` (Vol: 9,500,000.00 USD, Dist: `--0.42%`)
  * 3D Horizon: Short MP=`4076.12` (Vol: 15,300,000.00 USD, Dist: `+2.25%`) | Long MP=`3950.52` (Vol: 11,100,000.00 USD, Dist: `--0.90%`)
  * 7D Horizon: Short MP=`4076.12` (Vol: 15,300,000.00 USD, Dist: `+2.25%`) | Long MP=`3963.08` (Vol: 21,000,000.00 USD, Dist: `--0.58%`)
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
| `1D` | `3578.80` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 3,550.00 USD | 0.00 USD | 6,830.00 USD |
| `7D` | `3579.10` | 20,230,000.00 USD | 0.00 USD | 20,230,000.00 USD | 0.00 USD | 0.00 USD | 17,590.00 USD |
| `1D` | `3583.00` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 15,210.00 USD | 0.00 USD | 10,570.00 USD |
| `7D` | `3583.40` | 20,220,000.00 USD | 0.00 USD | 20,220,000.00 USD | 18,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3587.20` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 8,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3587.70` | 20,200,000.00 USD | 0.00 USD | 20,200,000.00 USD | 12,470.00 USD | 0.00 USD | 8,930.00 USD |
| `1D` | `3591.40` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 20,660.00 USD | 0.00 USD | 23,870.00 USD |
| `7D` | `3592.00` | 20,180,000.00 USD | 0.00 USD | 20,180,000.00 USD | 59,500.00 USD | 0.00 USD | 129,530.00 USD |
| `1D` | `3595.60` | 5,660,000.00 USD | 0.00 USD | 5,660,000.00 USD | 31,520.00 USD | 0.00 USD | 58,060.00 USD |
| `7D` | `3596.30` | 19,990,000.00 USD | 0.00 USD | 19,990,000.00 USD | 84,110.00 USD | 0.00 USD | 154,790.00 USD |
| `1D` | `3599.80` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 7,240.00 USD | 0.00 USD | 29,000.00 USD |
| `7D` | `3600.60` | 19,750,000.00 USD | 0.00 USD | 19,750,000.00 USD | 99,620.00 USD | 0.00 USD | 242,270.00 USD |
| `1D` | `3604.00` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 11,200.00 USD | 0.00 USD | 37,960.00 USD |
| `7D` | `3604.90` | 19,410,000.00 USD | 0.00 USD | 19,410,000.00 USD | 31,270.00 USD | 0.00 USD | 69,670.00 USD |
| `1D` | `3608.20` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 18,250.00 USD | 0.00 USD | 58,710.00 USD |
| `7D` | `3609.20` | 19,300,000.00 USD | 0.00 USD | 19,300,000.00 USD | 22,730.00 USD | 0.00 USD | 65,370.00 USD |
| `1D` | `3612.40` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 17,620.00 USD | 0.00 USD | 26,900.00 USD |
| `7D` | `3613.50` | 19,220,000.00 USD | 0.00 USD | 19,220,000.00 USD | 45,060.00 USD | 0.00 USD | 48,820.00 USD |
| `1D` | `3616.60` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 10,800.00 USD | 0.00 USD | 28,100.00 USD |
| `7D` | `3617.80` | 19,120,000.00 USD | 0.00 USD | 19,120,000.00 USD | 20,780.00 USD | 0.00 USD | 71,790.00 USD |
| `1D` | `3620.80` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 16,680.00 USD | 0.00 USD | 40,430.00 USD |
| `7D` | `3622.10` | 19,030,000.00 USD | 0.00 USD | 19,030,000.00 USD | 23,640.00 USD | 0.00 USD | 130,050.00 USD |
| `1D` | `3625.00` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 10,910.00 USD | 0.00 USD | 3,580.00 USD |
| `7D` | `3626.40` | 18,880,000.00 USD | 0.00 USD | 18,880,000.00 USD | 35,220.00 USD | 0.00 USD | 33,300.00 USD |
| `1D` | `3629.20` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 1,760.00 USD |
| `7D` | `3630.70` | 18,810,000.00 USD | 0.00 USD | 18,810,000.00 USD | 34,300.00 USD | 0.00 USD | 56,190.00 USD |
| `1D` | `3633.40` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 2,840.00 USD |
| `7D` | `3635.00` | 18,720,000.00 USD | 0.00 USD | 18,720,000.00 USD | 57,970.00 USD | 0.00 USD | 46,780.00 USD |
| `7D` | `3639.30` | 18,610,000.00 USD | 0.00 USD | 18,610,000.00 USD | 68,420.00 USD | 0.00 USD | 12,090.00 USD |
| `7D` | `3643.60` | 18,530,000.00 USD | 0.00 USD | 18,530,000.00 USD | 20,110.00 USD | 0.00 USD | 7,240.00 USD |
| `7D` | `3647.90` | 18,500,000.00 USD | 0.00 USD | 18,500,000.00 USD | 19,450.00 USD | 0.00 USD | 20,140.00 USD |
| `7D` | `3656.50` | 18,460,000.00 USD | 0.00 USD | 18,460,000.00 USD | 16,960.00 USD | 0.00 USD | 7,980.00 USD |
| `7D` | `3660.80` | 18,440,000.00 USD | 0.00 USD | 18,440,000.00 USD | 2,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3814.00` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 0.00 USD | 0.00 USD | 35,390.00 USD |
| `7D` | `3815.60` | 18,440,000.00 USD | 0.00 USD | 18,440,000.00 USD | 0.00 USD | 0.00 USD | 43,990.00 USD |
| `1D` | `3818.20` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 28,920.00 USD | 0.00 USD | 13,360.00 USD |
| `7D` | `3819.90` | 18,390,000.00 USD | 0.00 USD | 18,390,000.00 USD | 12,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3822.40` | 5,170,000.00 USD | 0.00 USD | 5,170,000.00 USD | 26,640.00 USD | 0.00 USD | 37,960.00 USD |
| `7D` | `3824.20` | 18,380,000.00 USD | 0.00 USD | 18,380,000.00 USD | 44,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3826.60` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 21,450.00 USD | 0.00 USD | 4,790.00 USD |
| `7D` | `3828.50` | 18,340,000.00 USD | 0.00 USD | 18,340,000.00 USD | 129,810.00 USD | 0.00 USD | 133,550.00 USD |
| `1D` | `3830.80` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 56,740.00 USD | 0.00 USD | 76,390.00 USD |
| `7D` | `3832.80` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 210,550.00 USD | 0.00 USD | 393,410.00 USD |
| `1D` | `3835.00` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 111,330.00 USD | 0.00 USD | 114,860.00 USD |
| `7D` | `3837.10` | 17,470,000.00 USD | 0.00 USD | 17,470,000.00 USD | 350,430.00 USD | 0.00 USD | 821,520.00 USD |
| `1D` | `3839.20` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 22,490.00 USD | 0.00 USD | 125,570.00 USD |
| `7D` | `3841.40` | 16,300,000.00 USD | 0.00 USD | 16,300,000.00 USD | 247,320.00 USD | 0.00 USD | 529,780.00 USD |
| `1D` | `3843.40` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 40,860.00 USD | 0.00 USD | 101,690.00 USD |
| `7D` | `3845.70` | 15,520,000.00 USD | 0.00 USD | 15,520,000.00 USD | 72,140.00 USD | 0.00 USD | 192,410.00 USD |
| `1D` | `3847.60` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 72,170.00 USD | 0.00 USD | 190,620.00 USD |
| `7D` | `3850.00` | 15,260,000.00 USD | 0.00 USD | 15,260,000.00 USD | 109,740.00 USD | 0.00 USD | 249,610.00 USD |
| `1D` | `3851.80` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 67,150.00 USD | 0.00 USD | 140,840.00 USD |
| `7D` | `3854.30` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 161,070.00 USD | 0.00 USD | 213,050.00 USD |
| `1D` | `3856.00` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 27,220.00 USD | 0.00 USD | 95,290.00 USD |
| `7D` | `3858.60` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 70,500.00 USD | 0.00 USD | 193,640.00 USD |
| `1D` | `3860.20` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 74,170.00 USD | 0.00 USD | 94,110.00 USD |
| `7D` | `3862.90` | 14,260,000.00 USD | 0.00 USD | 14,260,000.00 USD | 101,780.00 USD | 0.00 USD | 347,920.00 USD |
| `1D` | `3864.40` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 38,370.00 USD | 0.00 USD | 83,690.00 USD |
| `7D` | `3867.20` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 58,720.00 USD | 0.00 USD | 119,800.00 USD |
| `1D` | `3868.60` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 13,630.00 USD | 0.00 USD | 14,120.00 USD |
| `7D` | `3871.50` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 153,110.00 USD | 0.00 USD | 169,500.00 USD |
| `1D` | `3872.80` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 2,390.00 USD | 0.00 USD | 16,700.00 USD |
| `7D` | `3875.80` | 13,310,000.00 USD | 0.00 USD | 13,310,000.00 USD | 215,680.00 USD | 0.00 USD | 169,710.00 USD |
| `7D` | `3880.10` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 226,340.00 USD | 0.00 USD | 18,540.00 USD |
| `7D` | `3884.40` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 108,600.00 USD | 0.00 USD | 116,380.00 USD |
| `7D` | `3888.70` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 37,090.00 USD | 0.00 USD | 53,820.00 USD |
| `7D` | `3893.00` | 12,360,000.00 USD | 0.00 USD | 12,360,000.00 USD | 38,150.00 USD | 0.00 USD | 117,750.00 USD |
| `1D` | `3893.80` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 70,790.00 USD |
| `7D` | `3897.30` | 12,210,000.00 USD | 0.00 USD | 12,210,000.00 USD | 38,400.00 USD | 0.00 USD | 37,970.00 USD |
| `1D` | `3898.00` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 57,830.00 USD | 0.00 USD | 58,390.00 USD |
| `7D` | `3901.60` | 12,130,000.00 USD | 0.00 USD | 12,130,000.00 USD | 157,340.00 USD | 0.00 USD | 37,180.00 USD |
| `1D` | `3902.20` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 53,290.00 USD | 0.00 USD | 44,250.00 USD |
| `7D` | `3905.90` | 11,930,000.00 USD | 0.00 USD | 11,930,000.00 USD | 56,950.00 USD | 0.00 USD | 56,010.00 USD |
| `1D` | `3906.40` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 42,900.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `3910.20` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 373,340.00 USD | 0.00 USD | 609,360.00 USD |
| `1D` | `3910.60` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 113,490.00 USD | 0.00 USD | 152,780.00 USD |
| `7D` | `3914.50` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 455,730.00 USD | 0.00 USD | 1,100,000.00 USD |
| `1D` | `3914.80` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 222,660.00 USD | 0.00 USD | 229,730.00 USD |
| `7D` | `3918.80` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 596,520.00 USD | 0.00 USD | 1,440,000.00 USD |
| `1D` | `3919.00` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 44,970.00 USD | 0.00 USD | 251,130.00 USD |
| `7D` | `3923.10` | 7,250,000.00 USD | 0.00 USD | 7,250,000.00 USD | 431,970.00 USD | 0.00 USD | 661,450.00 USD |
| `1D` | `3923.20` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 81,730.00 USD | 0.00 USD | 194,270.00 USD |
| `1D` | `3927.40` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 132,000.00 USD | 0.00 USD | 390,350.00 USD |
| `7D` | `3927.40` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 158,220.00 USD | 0.00 USD | 469,090.00 USD |
| `1D` | `3931.60` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 144,350.00 USD | 0.00 USD | 259,360.00 USD |
| `7D` | `3931.70` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 352,560.00 USD | 0.00 USD | 429,140.00 USD |
| `1D` | `3935.80` | 944,000.00 USD | 0.00 USD | 944,000.00 USD | 22,890.00 USD | 0.00 USD | 185,740.00 USD |
| `7D` | `3936.00` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 154,220.00 USD | 0.00 USD | 415,030.00 USD |
| `1D` | `3940.00` | 735,370.00 USD | 0.00 USD | 735,370.00 USD | 157,970.00 USD | 0.00 USD | 201,590.00 USD |
| `7D` | `3940.30` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 170,500.00 USD | 0.00 USD | 400,590.00 USD |
| `1D` | `3944.20` | 375,810.00 USD | 0.00 USD | 375,810.00 USD | 81,990.00 USD | 0.00 USD | 173,540.00 USD |
| `7D` | `3944.60` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 156,660.00 USD | 0.00 USD | 702,210.00 USD |
| `1D` | `3948.40` | 120,290.00 USD | 0.00 USD | 120,290.00 USD | 46,230.00 USD | 0.00 USD | 35,870.00 USD |
| `7D` | `3948.90` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 332,570.00 USD | 0.00 USD | 215,000.00 USD |
| `1D` | `3952.60` | 38,180.00 USD | 0.00 USD | 38,180.00 USD | 4,780.00 USD | 0.00 USD | 33,400.00 USD |
| `7D` | `3953.20` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 210,970.00 USD | 0.00 USD | 288,460.00 USD |
| `7D` | `3957.50` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 384,300.00 USD | 0.00 USD | 286,230.00 USD |
| `7D` | `3961.80` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 406,510.00 USD | 0.00 USD | 52,260.00 USD |
| `7D` | `3966.10` | 573,150.00 USD | 0.00 USD | 573,150.00 USD | 190,540.00 USD | 0.00 USD | 232,140.00 USD |
| `7D` | `3970.40` | 150,480.00 USD | 0.00 USD | 150,480.00 USD | 109,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3974.70` | 40,750.00 USD | 0.00 USD | 40,750.00 USD | 40,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3977.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3977.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3979.00` | 75,930.00 USD | 75,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 75,930.00 USD |
| `7D` | `3983.30` | 150,290.00 USD | 150,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 74,360.00 USD |
| `1D` | `4049.20` | 22,880.00 USD | 22,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,880.00 USD |
| `7D` | `4052.10` | 238,260.00 USD | 238,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 87,970.00 USD |
| `1D` | `4053.40` | 70,790.00 USD | 70,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 47,910.00 USD |
| `1D` | `4057.60` | 187,010.00 USD | 187,010.00 USD | 0.00 USD | 57,830.00 USD | 0.00 USD | 58,390.00 USD |
| `7D` | `4060.70` | 328,040.00 USD | 328,040.00 USD | 0.00 USD | 89,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4061.80` | 284,550.00 USD | 284,550.00 USD | 0.00 USD | 53,290.00 USD | 0.00 USD | 44,250.00 USD |
| `7D` | `4065.00` | 352,260.00 USD | 352,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,220.00 USD |
| `1D` | `4066.00` | 337,040.00 USD | 337,040.00 USD | 0.00 USD | 42,900.00 USD | 0.00 USD | 9,580.00 USD |
| `7D` | `4069.30` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 329,870.00 USD | 0.00 USD | 439,790.00 USD |
| `1D` | `4070.20` | 603,300.00 USD | 603,300.00 USD | 0.00 USD | 113,490.00 USD | 0.00 USD | 152,780.00 USD |
| `7D` | `4073.60` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 444,880.00 USD | 0.00 USD | 1,120,000.00 USD |
| `1D` | `4074.40` | 947,480.00 USD | 947,480.00 USD | 0.00 USD | 212,500.00 USD | 0.00 USD | 131,680.00 USD |
| `7D` | `4077.90` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 592,620.00 USD | 0.00 USD | 1,580,000.00 USD |
| `1D` | `4078.60` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 44,700.00 USD | 0.00 USD | 295,980.00 USD |
| `7D` | `4082.20` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 466,070.00 USD | 0.00 USD | 653,780.00 USD |
| `1D` | `4082.80` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 82,490.00 USD | 0.00 USD | 220,480.00 USD |
| `7D` | `4086.50` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 133,300.00 USD | 0.00 USD | 381,650.00 USD |
| `1D` | `4087.00` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 108,840.00 USD | 0.00 USD | 386,200.00 USD |
| `7D` | `4090.80` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 230,150.00 USD | 0.00 USD | 440,740.00 USD |
| `1D` | `4091.20` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 158,790.00 USD | 0.00 USD | 202,520.00 USD |
| `7D` | `4095.10` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 294,010.00 USD | 0.00 USD | 426,100.00 USD |
| `1D` | `4095.40` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 33,980.00 USD | 0.00 USD | 203,820.00 USD |
| `7D` | `4099.40` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 141,000.00 USD | 0.00 USD | 387,270.00 USD |
| `1D` | `4099.60` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 138,890.00 USD | 0.00 USD | 156,280.00 USD |
| `7D` | `4103.70` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 191,320.00 USD | 0.00 USD | 534,970.00 USD |
| `1D` | `4103.80` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 80,670.00 USD | 0.00 USD | 270,820.00 USD |
| `1D` | `4108.00` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 73,930.00 USD | 0.00 USD | 32,930.00 USD |
| `7D` | `4108.00` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 112,940.00 USD | 0.00 USD | 370,850.00 USD |
| `1D` | `4112.20` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 40,060.00 USD |
| `7D` | `4112.30` | 10,260,000.00 USD | 10,260,000.00 USD | 0.00 USD | 305,770.00 USD | 0.00 USD | 326,800.00 USD |
| `1D` | `4116.40` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 4,780.00 USD | 0.00 USD | 14,190.00 USD |
| `7D` | `4116.60` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 283,950.00 USD | 0.00 USD | 381,250.00 USD |
| `7D` | `4120.90` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 424,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4125.20` | 11,780,000.00 USD | 11,780,000.00 USD | 0.00 USD | 277,440.00 USD | 0.00 USD | 157,400.00 USD |
| `1D` | `4129.00` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,740.00 USD |
| `7D` | `4129.50` | 12,050,000.00 USD | 12,050,000.00 USD | 0.00 USD | 145,360.00 USD | 0.00 USD | 127,000.00 USD |
| `1D` | `4133.20` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,660.00 USD |
| `7D` | `4133.80` | 12,350,000.00 USD | 12,350,000.00 USD | 0.00 USD | 97,260.00 USD | 0.00 USD | 196,630.00 USD |
| `1D` | `4137.40` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 28,920.00 USD | 0.00 USD | 29,200.00 USD |
| `7D` | `4138.10` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 79,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4141.60` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 26,640.00 USD | 0.00 USD | 22,130.00 USD |
| `7D` | `4142.40` | 12,650,000.00 USD | 12,650,000.00 USD | 0.00 USD | 151,240.00 USD | 0.00 USD | 75,930.00 USD |
| `1D` | `4145.80` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 21,450.00 USD | 0.00 USD | 4,790.00 USD |
| `7D` | `4146.70` | 12,940,000.00 USD | 12,940,000.00 USD | 0.00 USD | 126,960.00 USD | 0.00 USD | 159,490.00 USD |
| `1D` | `4150.00` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 56,740.00 USD | 0.00 USD | 76,390.00 USD |
| `7D` | `4151.00` | 13,490,000.00 USD | 13,490,000.00 USD | 0.00 USD | 168,430.00 USD | 0.00 USD | 381,500.00 USD |
| `1D` | `4154.20` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 106,250.00 USD | 0.00 USD | 65,840.00 USD |
| `7D` | `4155.30` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 272,950.00 USD | 0.00 USD | 496,980.00 USD |
| `1D` | `4158.40` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 22,350.00 USD | 0.00 USD | 143,490.00 USD |
| `7D` | `4159.60` | 15,230,000.00 USD | 15,230,000.00 USD | 0.00 USD | 271,500.00 USD | 0.00 USD | 694,730.00 USD |
| `1D` | `4162.60` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 41,250.00 USD | 0.00 USD | 114,740.00 USD |
| `7D` | `4163.90` | 15,690,000.00 USD | 15,690,000.00 USD | 0.00 USD | 156,430.00 USD | 0.00 USD | 308,320.00 USD |
| `1D` | `4166.80` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 51,270.00 USD | 0.00 USD | 164,470.00 USD |
| `7D` | `4168.20` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 75,700.00 USD | 0.00 USD | 228,860.00 USD |
| `1D` | `4171.00` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 79,720.00 USD | 0.00 USD | 117,880.00 USD |
| `7D` | `4172.50` | 16,350,000.00 USD | 16,350,000.00 USD | 0.00 USD | 171,170.00 USD | 0.00 USD | 184,620.00 USD |
| `1D` | `4175.20` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 19,810.00 USD | 0.00 USD | 95,720.00 USD |
| `7D` | `4176.80` | 16,640,000.00 USD | 16,640,000.00 USD | 0.00 USD | 77,110.00 USD | 0.00 USD | 207,520.00 USD |
| `1D` | `4179.40` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 39,180.00 USD | 0.00 USD | 96,340.00 USD |
| `7D` | `4181.10` | 16,900,000.00 USD | 16,900,000.00 USD | 0.00 USD | 73,560.00 USD | 0.00 USD | 186,400.00 USD |
| `1D` | `4183.60` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 67,600.00 USD | 0.00 USD | 122,320.00 USD |
| `7D` | `4185.40` | 17,300,000.00 USD | 17,300,000.00 USD | 0.00 USD | 90,020.00 USD | 0.00 USD | 315,450.00 USD |
| `1D` | `4187.80` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 33,260.00 USD | 0.00 USD | 29,560.00 USD |
| `7D` | `4189.70` | 17,490,000.00 USD | 17,490,000.00 USD | 0.00 USD | 84,710.00 USD | 0.00 USD | 105,160.00 USD |
| `1D` | `4192.00` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 6,700.00 USD | 0.00 USD | 13,130.00 USD |
| `7D` | `4194.00` | 17,790,000.00 USD | 17,790,000.00 USD | 0.00 USD | 127,120.00 USD | 0.00 USD | 169,500.00 USD |
| `1D` | `4196.20` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD | 14,000.00 USD |
| `7D` | `4198.30` | 18,110,000.00 USD | 18,110,000.00 USD | 0.00 USD | 151,780.00 USD | 0.00 USD | 169,710.00 USD |
| `7D` | `4202.60` | 18,320,000.00 USD | 18,320,000.00 USD | 0.00 USD | 193,670.00 USD | 0.00 USD | 18,540.00 USD |
| `7D` | `4206.90` | 18,570,000.00 USD | 18,570,000.00 USD | 0.00 USD | 175,690.00 USD | 0.00 USD | 72,260.00 USD |
| `7D` | `4211.20` | 18,690,000.00 USD | 18,690,000.00 USD | 0.00 USD | 66,570.00 USD | 0.00 USD | 51,400.00 USD |
| `7D` | `4215.50` | 18,800,000.00 USD | 18,800,000.00 USD | 0.00 USD | 38,150.00 USD | 0.00 USD | 76,320.00 USD |
| `7D` | `4219.80` | 18,820,000.00 USD | 18,820,000.00 USD | 0.00 USD | 19,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4224.10` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 46,450.00 USD | 0.00 USD | 57,930.00 USD |
| `7D` | `4228.40` | 18,960,000.00 USD | 18,960,000.00 USD | 0.00 USD | 15,250.00 USD | 0.00 USD | 17,220.00 USD |
| `1D` | `4368.40` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 10,290.00 USD |
| `7D` | `4370.30` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,590.00 USD |
| `1D` | `4372.60` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,860.00 USD |
| `1D` | `4376.80` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 18,760.00 USD | 0.00 USD | 9,300.00 USD |
| `7D` | `4378.90` | 18,980,000.00 USD | 18,980,000.00 USD | 0.00 USD | 4,890.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4381.00` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,240.00 USD |
| `7D` | `4383.20` | 19,000,000.00 USD | 19,000,000.00 USD | 0.00 USD | 20,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4385.20` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 8,580.00 USD | 0.00 USD | 6,800.00 USD |
| `7D` | `4387.50` | 19,070,000.00 USD | 19,070,000.00 USD | 0.00 USD | 30,850.00 USD | 0.00 USD | 33,370.00 USD |
| `1D` | `4389.40` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 20,660.00 USD | 0.00 USD | 17,070.00 USD |
| `7D` | `4391.80` | 19,240,000.00 USD | 19,240,000.00 USD | 0.00 USD | 59,080.00 USD | 0.00 USD | 113,670.00 USD |
| `1D` | `4393.60` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 27,200.00 USD | 0.00 USD | 22,420.00 USD |
| `7D` | `4396.10` | 19,530,000.00 USD | 19,530,000.00 USD | 0.00 USD | 80,970.00 USD | 0.00 USD | 213,870.00 USD |
| `1D` | `4397.80` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 4,320.00 USD | 0.00 USD | 50,760.00 USD |
| `1D` | `4399.40` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 5,120.00 USD | 0.00 USD | 12,440.00 USD |
| `7D` | `4400.40` | 19,790,000.00 USD | 19,790,000.00 USD | 0.00 USD | 77,940.00 USD | 0.00 USD | 174,620.00 USD |
| `7D` | `4404.70` | 19,860,000.00 USD | 19,860,000.00 USD | 0.00 USD | 24,710.00 USD | 0.00 USD | 51,380.00 USD |
| `7D` | `4409.00` | 19,940,000.00 USD | 19,940,000.00 USD | 0.00 USD | 8,420.00 USD | 0.00 USD | 68,180.00 USD |
| `7D` | `4413.30` | 20,020,000.00 USD | 20,020,000.00 USD | 0.00 USD | 52,340.00 USD | 0.00 USD | 28,440.00 USD |
| `7D` | `4416.00` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 13,590.00 USD | 0.00 USD | 20,380.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `867.00M` | Total OI Tokens: `218,056.8 XAUT`
  * 1h OI Change: `-0.74%` | 4h OI Change: `+4.55%` | 24h OI Change: `-1.23%`
  * Exchange Breakdown: Binance=`60.56M` | Bybit=`142.27M` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.94K` | Last 24h: `33.89K` | Last 3d: `98.38K` | Last 7d: `284.70K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0042%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0025%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `0.0025%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0098%` | **USDT Bitget** | `0.0050%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XAUT` | `34.04%` | `65.96%` | `0.52` | 2,590,000.00 USD |
| `15M` | `Binance` | `32.74%` | `67.26%` | `0.49` | 753,350.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 379,520.00 USD |
| `15M` | `Bybit` | `28.59%` | `71.41%` | `0.40` | 231,830.00 USD |
| `15M` | `KuCoin` | `27.15%` | `72.85%` | `0.37` | 29,860.00 USD |
| `15M` | `Gate` | `32.37%` | `67.63%` | `0.48` | 38,330.00 USD |
| `15M` | `Bitget` | `33.22%` | `66.78%` | `0.50` | 274,600.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 434,010.00 USD |
| `15M` | `MEXC` | `30.9%` | `69.1%` | `0.45` | 174,230.00 USD |
| `15M` | `Bitunix` | `47.16%` | `52.84%` | `0.89` | 39,000.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 14,760.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55.48%` | `44.52%` | `1.25` | 71,520.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 3.25 USD |
| `15M` | `WhiteBIT` | `75.43%` | `24.57%` | `3.07` | 134,620.00 USD |
| `15M` | `HTX` | `85.95%` | `14.05%` | `6.12` | 154.02 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `90.88%` | `9.12%` | `9.96` | 6,410.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 11.02 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 11,610.00 USD |
| `15M` | `Whale Positions` | `32.74%` | `67.26%` | `0.49` | 753,350.00 USD |
| `15M` | `Global Accounts` | `34.04%` | `65.96%` | `0.52` | 2,590,000.00 USD |
| `1H` | `XAUT` | `36.37%` | `63.63%` | `0.57` | 10,690,000.00 USD |
| `1H` | `Binance` | `50.78%` | `49.22%` | `1.03` | 1,750,000.00 USD |
| `1H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bybit` | `27.17%` | `72.83%` | `0.37` | 1,520,000.00 USD |
| `1H` | `KuCoin` | `39.33%` | `60.67%` | `0.65` | 41,290.00 USD |
| `1H` | `Gate` | `43.71%` | `56.29%` | `0.78` | 366,810.00 USD |
| `1H` | `Bitget` | `41.41%` | `58.59%` | `0.71` | 572,580.00 USD |
| `1H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `MEXC` | `29.55%` | `70.45%` | `0.42` | 4,850,000.00 USD |
| `1H` | `Bitunix` | `47.8%` | `52.2%` | `0.92` | 290,230.00 USD |
| `1H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `41.05%` | `58.95%` | `0.70` | 620,040.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `24.23%` | `75.77%` | `0.32` | 410,910.00 USD |
| `1H` | `HTX` | `20.28%` | `79.72%` | `0.25` | 9,010.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `95.29%` | `4.71%` | `20.23` | 256,160.00 USD |
| `1H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `50.78%` | `49.22%` | `1.03` | 1,750,000.00 USD |
| `1H` | `Global Accounts` | `36.37%` | `63.63%` | `0.57` | 10,690,000.00 USD |
| `4H` | `XAUT` | `51.90%` | `48.10%` | `1.08` | 84,790,000.00 USD |
| `4H` | `Binance` | `50.74%` | `49.26%` | `1.03` | 10,300,000.00 USD |
| `4H` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bybit` | `49.75%` | `50.25%` | `0.99` | 7,660,000.00 USD |
| `4H` | `KuCoin` | `41.58%` | `58.42%` | `0.71` | 398,230.00 USD |
| `4H` | `Gate` | `43.3%` | `56.7%` | `0.76` | 2,790,000.00 USD |
| `4H` | `Bitget` | `50.36%` | `49.64%` | `1.01` | 4,250,000.00 USD |
| `4H` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `MEXC` | `54.28%` | `45.72%` | `1.19` | 50,700,000.00 USD |
| `4H` | `Bitunix` | `52.8%` | `47.2%` | `1.12` | 1,870,000.00 USD |
| `4H` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.27%` | `50.73%` | `0.97` | 4,430,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `12.88%` | `87.12%` | `0.15` | 1,810,000.00 USD |
| `4H` | `HTX` | `57.67%` | `42.33%` | `1.36` | 53,360.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `93.32%` | `6.68%` | `13.97` | 540,200.00 USD |
| `4H` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `50.74%` | `49.26%` | `1.03` | 10,300,000.00 USD |
| `4H` | `Global Accounts` | `51.90%` | `48.10%` | `1.08` | 84,790,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `3997.05` | `3997.44` | `3997.05` | `3999.75` | `3995.25` | 19,570,728.76 USD | 11,961,064.45 USD | 7,609,664.31 USD | 4,351,400.15 USD | `+22.23%` | `5B / 0S` |
| `5:00 UTC` | `4006.95` | `4004.53` | `4006.95` | `4008.45` | `3997.95` | 44,001,963.37 USD | 19,638,518.84 USD | 24,363,444.53 USD | -4,724,925.70 USD | `-10.74%` | `4B / 1S` |
| `0:00 UTC` | `4006.95` | `4003.87` | `4006.95` | `4007.55` | `3999.75` | 22,763,119.63 USD | 8,502,990.90 USD | 14,260,128.73 USD | -5,757,137.84 USD | `-25.29%` | `1B / 8S` |
| `5:00 UTC` | `3999.45` | `4001.01` | `3999.45` | `4004.25` | `3999.15` | 12,529,034.87 USD | 5,499,093.98 USD | 7,029,940.89 USD | -1,530,846.92 USD | `-12.22%` | `0B / 0S` |
| `0:00 UTC` | `4000.35` | `3999.56` | `4000.35` | `4001.55` | `3997.95` | 10,610,433.25 USD | 4,382,210.73 USD | 6,228,222.52 USD | -1,846,011.79 USD | `-17.40%` | `0B / 0S` |
| `5:00 UTC` | `4000.95` | `3999.70` | `4000.95` | `4001.85` | `3996.45` | 14,656,052.45 USD | 7,151,824.61 USD | 7,504,227.84 USD | -352,403.23 USD | `-2.40%` | `0B / 1S` |
| `0:00 UTC` | `3997.95` | `3996.26` | `3997.95` | `4000.95` | `3991.65` | 20,329,795.57 USD | 9,073,400.57 USD | 11,256,395.00 USD | -2,182,994.43 USD | `-10.74%` | `1B / 8S` |
| `5:00 UTC` | `3992.25` | `3992.57` | `3992.25` | `3995.85` | `3989.55` | 14,090,225.56 USD | 5,930,414.16 USD | 8,159,811.40 USD | -2,229,397.23 USD | `-15.82%` | `1B / 5S` |
| `0:00 UTC` | `3991.35` | `3990.85` | `3991.35` | `3992.85` | `3989.25` | 11,588,789.02 USD | 6,837,727.49 USD | 4,751,061.53 USD | 2,086,665.96 USD | `+18.01%` | `1B / 1S` |
| `5:00 UTC` | `3985.95` | `3986.52` | `3985.95` | `3989.55` | `3985.35` | 8,318,936.17 USD | 3,165,198.00 USD | 5,153,738.16 USD | -1,988,540.16 USD | `-23.90%` | `1B / 5S` |

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
| `5m` | -427,710.00 USD | -99,140.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,030,000.00 USD | -192,850.00 USD | **`DISTRIBUTION`** |
| `30m` | 164,500.00 USD | -104,280.00 USD | **`ACCUMULATION`** |
| `1h` | -719,430.00 USD | -297,560.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,830,000.00 USD | -128,990.00 USD | **`DISTRIBUTION`** |
| `4h` | -3,690,000.00 USD | 697,850.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,010,000.00 USD | -495,990.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,550,000.00 USD | -1,420,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -5,690,000.00 USD | -3,510,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -5,730,000.00 USD | -2,310,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -64,030,000.00 USD | -18,450,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -186,810,000.00 USD | -85,100,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-427.71K` | 15m=`-1.03M` | 1h=`-719.43K` | 24h=`-5.73M`
* Futures Capital Netflows: 5m=`-99.14K` | 15m=`-192.85K` | 1h=`-297.56K` | 24h=`-2.31M`
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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `3972.80` (Risk Distance: `9.63` pts)
  * +2.5R Take Profit: `4006.50`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4007.93` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4017.56` (Risk Distance: `9.63` pts)
  * +2.5R Take Profit: `3983.86`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`5116.75`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
