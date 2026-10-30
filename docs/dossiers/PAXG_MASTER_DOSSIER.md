# 🏛️ SOVEREIGN CANDIDATE DOSSIER: PAXG
**Canonical Key**: `PAXG` | **Broker Instrument**: `XAUUSD.pi` | **Asset Class**: `Tokenized Metal`
**Timestamp**: `2026-10-30 16:00:27 IST` (`2026-10-30 10:30:27 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3985.82` | **Live Ask Quote**: `3985.90` | **Mid Price**: `3985.86`
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
  * Session VWAP: `3996.25` | VWAP Z-Score: `-1.41` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `7.93` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `42.02` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4025.25` | Lower -3.00σ Band: `3967.24`
  * Upper +2.51σ Band: `4020.51` | Lower -2.51σ Band: `3971.98`
  * Upper +2.01σ Band: `4015.68` | Lower -2.01σ Band: `3976.81`
  * Upper +2.00σ Band: `4015.58` | Lower -2.00σ Band: `3976.91`
  * Upper +1.28σ Band: `4008.62` | Lower -1.28σ Band: `3983.87`
  * Upper +1.00σ Band: `4005.91` | Lower -1.00σ Band: `3986.58`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`3988.30` | EMA-20=`3989.91` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`3997.81` (Slope: `+0.0000`) | EMA-100=`4008.41`
  * Institutional Anchors: EMA-144=`4014.38` | EMA-200=`4019.37` (Slope: `-0.1028`) | EMA-233=`4022.47`
- **Range Boundaries**: 24H High=`4039.31` | 24H Low=`3965.22` | Weekly High=`4082.75` | Weekly Low=`3965.22`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4007.50` (Distance: `-0.55%`)
  * Point of Control (POC) = `3990.50` (Distance: `-0.13%`)
  * Value Area Low (VAL) = `3982.85` (Distance: `+0.06%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4039.67` | POC=`4027.32` | VAL=`4016.67`
  * Prior Day Extremes: PDH=`4069.28` | PDL=`4005.38` | PDC=`4021.40`
  * Monday Range Blueprint: High=`4030.02` | Mid=`4004.09` | Low=`3978.16`
  * Developing Weekly Value Area: Weekly VAH=`4053.37` | Weekly POC=`4017.32` | Weekly VAL=`4004.00`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4028.96` | Low=`3987.44`
  * London Session (08:00-16:00 UTC): High=`4011.55` | Low=`3965.22`
  * New York Session (13:00-21:00 UTC): High=`3991.98` | Low=`3981.70`
  * Initial Balance (First Hour): IB High=`4011.55` | IB Low=`3988.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3969.92` - `4001.80`
  * Optimal Trade Entry (OTE 0.705): `3993.83`
  * Structural Invalidation Anchor (0.786): `4017.75`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `3992.34` | `3992.34` | `3988.52` | `3988.53` | `127` | 506,397.77 USD | -289,291.56 USD | `-57.13%` | -143,261.62 USD | `-2.36` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `3988.52` | `3991.57` | `3987.55` | `3991.33` | `57` | 228,182.85 USD | -38,714.02 USD | `-16.97%` | -181,975.64 USD | `-0.39` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `3991.33` | `3991.33` | `3990.46` | `3990.47` | `5` | 18,665.82 USD | -16,622.70 USD | `-89.05%` | -198,598.34 USD | `-0.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `3993.76` | `3996.37` | `3991.51` | `3995.66` | `73` | 293,015.61 USD | -29,423.98 USD | `-10.04%` | 166,362.30 USD | `-0.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `3995.66` | `3995.82` | `3988.52` | `3988.53` | `295` | 1,178,649.83 USD | -275,535.97 USD | `-23.38%` | -109,173.67 USD | `-0.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `3988.52` | `3991.57` | `3987.55` | `3990.47` | `62` | 246,848.67 USD | -55,336.72 USD | `-22.42%` | -164,510.39 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `3981.68` | `4002.39` | `3979.22` | `4001.26` | `1,541` | 6,150,835.88 USD | 541,833.50 USD | `+8.81%` | 137,263.91 USD | `+1.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4001.22` | `4002.41` | `3991.51` | `3995.66` | `459` | 1,835,738.77 USD | 110,152.21 USD | `+6.00%` | 247,416.12 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `3995.66` | `3995.82` | `3987.55` | `3990.47` | `357` | 1,425,498.51 USD | -330,872.69 USD | `-23.21%` | -83,456.57 USD | `-0.57` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `3990.47` | `2,357` | 9,412,073.15 USD | 321,113.02 USD | `+3.41%` | -257,853.21 USD | `+0.45` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4026.82` | `4029.00` | `4011.01` | `4025.60` | `2,531` | 10,172,773.87 USD | 1,092,816.53 USD | `+10.74%` | 1,524,929.80 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4025.61` | `4033.50` | `4012.31` | `4012.55` | `2,621` | 10,543,019.56 USD | 17,856.35 USD | `+0.17%` | 1,542,786.16 USD | `-1.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4012.56` | `4020.37` | `3997.60` | `4000.51` | `4,138` | 16,575,387.63 USD | -1,342,501.16 USD | `-8.10%` | 200,285.00 USD | `-1.56` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4000.52` | `4017.75` | `3973.63` | `3981.69` | `5,893` | 23,547,344.15 USD | -779,251.23 USD | `-3.31%` | -578,966.23 USD | `-0.77` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `3981.68` | `4002.41` | `3979.22` | `3990.47` | `2,357` | 9,412,073.15 USD | 321,113.02 USD | `+3.41%` | -257,853.21 USD | `+0.45` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| `BID` | `3985.20` | `13.5007` | 53,802.99 USD | 1,119,923.38 USD | `4 orders` | `-0.07%` | `-` |
| `BID` | `3985.30` | `75.3235` | 300,186.74 USD | 1,066,120.39 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `3985.40` | `13.0471` | 51,997.91 USD | 765,933.65 USD | `5 orders` | `-0.07%` | `-` |
| `BID` | `3985.50` | `15.7135` | 62,626.15 USD | 713,935.74 USD | `4 orders` | `-0.07%` | `-` |
| `BID` | `3985.60` | `1.6910` | 6,739.65 USD | 651,309.58 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `3985.70` | `4.4019` | 17,544.65 USD | 644,569.93 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `3985.80` | `13.4629` | 53,660.43 USD | 627,025.28 USD | `4 orders` | `-0.06%` | `-` |
| `BID` | `3985.90` | `50.1757` | 199,995.32 USD | 573,364.85 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `3986.00` | `4.4681` | 17,809.85 USD | 373,369.53 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3986.10` | `17.7036` | 70,568.32 USD | 355,559.68 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `3986.20` | `12.6990` | 50,620.75 USD | 284,991.36 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `3986.30` | `4.4362` | 17,684.02 USD | 234,370.61 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `3986.40` | `2.5315` | 10,091.57 USD | 216,686.59 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3986.50` | `27.6787` | 110,341.14 USD | 206,595.01 USD | `4 orders` | `-0.04%` | `-` |
| `BID` | `3986.60` | `7.5222` | 29,988.00 USD | 96,253.88 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `3986.70` | `11.5322` | 45,975.42 USD | 66,265.87 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `3986.80` | `0.0720` | 287.05 USD | 20,290.45 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `3986.90` | `2.4107` | 9,611.22 USD | 20,003.40 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `3987.00` | `0.3705` | 1,477.18 USD | 10,392.18 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `3988.10` | `2.2354` | 8,915.00 USD | 8,915.00 USD | `2 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `3988.15` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 3,988.15` | `0.00%` | `-` |
| `ASK` | `3988.20` | `140.1088` | 558,781.92 USD | 558,781.92 USD | `29 orders` | `+0.00%` | `-` |
| `ASK` | `3988.30` | `16.4547` | 65,626.28 USD | 624,408.20 USD | `5 orders` | `+0.00%` | `-` |
| `ASK` | `3988.40` | `25.2591` | 100,743.39 USD | 725,151.59 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `3988.50` | `3.0223` | 12,054.44 USD | 737,206.03 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `3988.60` | `0.4380` | 1,747.01 USD | 738,953.04 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `3988.70` | `27.6983` | 110,480.21 USD | 849,433.25 USD | `5 orders` | `+0.01%` | `-` |
| `ASK` | `3988.80` | `7.2401` | 28,879.31 USD | 878,312.56 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `3988.90` | `71.0983` | 283,604.01 USD | 1,161,916.57 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `3989.00` | `36.9877` | 147,543.94 USD | 1,309,460.51 USD | `6 orders` | `+0.02%` | `-` |
| `ASK` | `3989.10` | `3.4984` | 13,955.47 USD | 1,323,415.97 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `3989.20` | `12.4092` | 49,502.78 USD | 1,372,918.75 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `3989.30` | `12.6424` | 50,434.33 USD | 1,423,353.08 USD | `7 orders` | `+0.03%` | `-` |
| `ASK` | `3989.40` | `7.9011` | 31,520.65 USD | 1,454,873.73 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `3989.50` | `89.2244` | 355,960.74 USD | 1,810,834.47 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `3989.60` | `7.9801` | 31,837.41 USD | 1,842,671.88 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `3989.70` | `7.6626` | 30,571.48 USD | 1,873,243.35 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3989.80` | `18.5587` | 74,045.50 USD | 1,947,288.86 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `3989.90` | `33.6468` | 134,247.37 USD | 2,081,536.22 USD | `3 orders` | `+0.04%` | `-` |
| `ASK` | `3990.00` | `8.7729` | 35,003.87 USD | 2,116,540.09 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `3990.10` | `17.6549` | 70,444.82 USD | 2,186,984.91 USD | `7 orders` | `+0.05%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:50:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `47` | `0x5b5d...c060` | `SHORT` | 25,863,895.59 USD | `6,489.82` | `4185.46` | `3984.40` | `28210.60` | 1,299,055.43 USD | `+5.02%` | `4X Cross` |
| `48` | `0x4692...164f` | `SHORT` | 25,141,166.22 USD | `6,308.63` | `4127.30` | `3984.40` | `14221.29` | 896,481.68 USD | `+3.57%` | `5X Cross` |
| `61` | `0xb83d...6e36` | `SHORT` | 23,391,549.11 USD | `5,869.90` | `4228.86` | `3984.40` | `22903.16` | 1,431,472.83 USD | `+6.12%` | `5X Cross` |
| `99` | `0xec0b...b078` | `LONG` | 19,244,159.78 USD | `4,828.91` | `4157.43` | `3984.40` | `2298.56` | -831,722.54 USD | `-4.32%` | `25X Cross` |
| `143` | `0x645b...87b8` | `LONG` | 14,130,410.52 USD | `3,545.72` | `4127.81` | `3984.40` | `661.11` | -505,684.05 USD | `-3.58%` | `3X Cross` |
| `156` | `0x7a6d...f79c` | `SHORT` | 13,024,483.24 USD | `3,268.21` | `4228.94` | `3984.40` | `4381.50` | 796,595.89 USD | `+6.12%` | `25X Cross` |
| `182` | `0xa742...e390` | `SHORT` | 11,158,648.47 USD | `2,800.02` | `4364.62` | `3984.40` | `4212.84` | 1,062,395.67 USD | `+9.52%` | `20X Cross` |
| `260` | `0x3678...b209` | `LONG` | 8,770,300.00 USD | `2,200.00` | `4176.09` | `3984.40` | `2682.44` | -417,119.30 USD | `-4.76%` | `25X Cross` |
| `261` | `0x41e5...0825` | `SHORT` | 8,767,440.00 USD | `2,200.00` | `4112.20` | `3984.40` | `4287.19` | 279,414.59 USD | `+3.19%` | `20X Cross` |
| `297` | `0xacb6...efbd` | `SHORT` | 7,872,240.94 USD | `1,975.37` | `4048.55` | `3984.40` | `6681.01` | 125,150.78 USD | `+1.59%` | `6X Cross` |
| `364` | `0xc26c...b8f4` | `LONG` | 6,296,897.90 USD | `1,579.95` | `4075.62` | `3984.40` | `0.000000` | -142,399.07 USD | `-2.26%` | `1X Cross` |
| `554` | `0x63da...8add` | `LONG` | 3,985,200.00 USD | `1,000.00` | `4021.46` | `3984.40` | `3564.73` | -36,260.96 USD | `-0.91%` | `25X Cross` |
| `566` | `0xf3dc...1672` | `LONG` | 3,922,515.59 USD | `984.27` | `4018.39` | `3984.40` | `2790.57` | -32,671.10 USD | `-0.83%` | `20X Cross` |
| `582` | `0x9aa5...58af` | `LONG` | 3,841,579.37 USD | `963.96` | `4279.98` | `3984.40` | `0.000000` | -284,157.32 USD | `-7.40%` | `20X Cross` |
| `665` | `0x4a20...3c26` | `LONG` | 3,338,293.90 USD | `837.40` | `4599.73` | `3984.40` | `0.000000` | -513,526.48 USD | `-15.38%` | `20X Cross` |
| `782` | `0x9c06...0560` | `LONG` | 2,897,121.01 USD | `726.95` | `4002.36` | `3984.40` | `0.000000` | -12,408.24 USD | `-0.43%` | `25X Cross` |
| `822` | `0x0fac...7a0a` | `LONG` | 2,735,848.67 USD | `686.49` | `4290.34` | `3984.40` | `1422.80` | -209,410.03 USD | `-7.65%` | `25X Cross` |
| `849` | `0x354b...6425` | `LONG` | 2,639,028.93 USD | `662.21` | `4004.29` | `3984.40` | `0.000000` | -12,647.78 USD | `-0.48%` | `10X Cross` |
| `891` | `0x625e...a354` | `SHORT` | 2,470,700.00 USD | `620.00` | `4122.81` | `3984.40` | `4279.60` | 85,447.03 USD | `+3.46%` | `20X Cross` |
| `921` | `0xeae3...e8ad` | `SHORT` | 2,391,120.00 USD | `600.00` | `4104.77` | `3984.40` | `4268.68` | 71,745.11 USD | `+3.00%` | `20X Cross` |
| `929` | `0xf285...fa82` | `LONG` | 2,383,631.44 USD | `598.11` | `4146.45` | `3984.40` | `3891.87` | -96,388.11 USD | `-4.04%` | `25X Cross` |
| `932` | `0xd8c5...99b0` | `SHORT` | 2,368,623.15 USD | `594.35` | `4175.35` | `3984.40` | `35406.63` | 113,020.88 USD | `+4.77%` | `4X Cross` |
| `937` | `0x12f7...8750` | `LONG` | 2,333,775.76 USD | `585.61` | `4082.77` | `3984.40` | `2818.93` | -57,141.22 USD | `-2.45%` | `10X Cross` |
| `981` | `0x413c...886c` | `LONG` | 2,229,601.44 USD | `559.47` | `4007.05` | `3984.40` | `0.000000` | -12,225.77 USD | `-0.55%` | `2X Cross` |
| `1085` | `0x61ce...a62b` | `SHORT` | 1,982,650.95 USD | `497.50` | `4071.66` | `3984.40` | `4724.81` | 43,017.84 USD | `+2.17%` | `20X Cross` |
| `1164` | `0x2edd...8179` | `LONG` | 1,871,447.83 USD | `469.26` | `4164.68` | `3987.60` | `0.000000` | -82,860.94 USD | `-4.43%` | `10X Cross` |
| `1213` | `0xead5...69f2` | `LONG` | 1,808,419.60 USD | `453.78` | `4220.88` | `3984.40` | `3539.57` | -106,948.46 USD | `-5.91%` | `5X Isolated` |
| `1273` | `0x7a6d...f79c` | `SHORT` | 1,708,718.16 USD | `428.38` | `4136.09` | `3987.60` | `5425.68` | 63,096.85 USD | `+3.69%` | `10X Cross` |
| `1305` | `0x46fc...1195` | `LONG` | 1,650,299.22 USD | `414.11` | `4051.57` | `3984.40` | `2232.78` | -27,486.16 USD | `-1.67%` | `20X Cross` |
| `1344` | `0xee02...309d` | `SHORT` | 1,594,120.00 USD | `400.00` | `4438.84` | `3984.40` | `4202.98` | 181,418.60 USD | `+11.38%` | `25X Isolated` |
| `1345` | `0x6d15...d374` | `LONG` | 1,594,080.00 USD | `400.00` | `4068.25` | `3984.40` | `3842.44` | -33,220.00 USD | `-2.08%` | `25X Cross` |
| `1373` | `0x51f6...2b39` | `LONG` | 1,561,457.13 USD | `391.48` | `4228.25` | `3987.60` | `521.36` | -93,818.56 USD | `-6.01%` | `10X Cross` |
| `1382` | `0x02a7...fe9f` | `SHORT` | 1,554,657.00 USD | `390.00` | `4055.02` | `3984.40` | `4307.31` | 26,802.25 USD | `+1.72%` | `25X Cross` |
| `1429` | `0x7e77...b8d2` | `SHORT` | 1,514,376.00 USD | `380.00` | `4131.92` | `3984.40` | `4294.11` | 55,753.64 USD | `+3.68%` | `20X Cross` |
| `1451` | `0x72c2...9b37` | `LONG` | 1,487,002.86 USD | `373.13` | `4000.98` | `3984.40` | `3778.67` | -5,890.66 USD | `-0.40%` | `13X Isolated` |
| `1468` | `0x781e...96b7` | `SHORT` | 1,459,168.79 USD | `365.84` | `4358.71` | `3987.60` | `12906.79` | 135,438.85 USD | `+9.28%` | `10X Cross` |
| `1490` | `0xaa44...b844` | `LONG` | 1,434,672.00 USD | `360.00` | `4043.10` | `3984.40` | `3225.88` | -20,845.63 USD | `-1.45%` | `7X Cross` |
| `1606` | `0xa41f...d50a` | `LONG` | 1,310,979.76 USD | `328.96` | `4468.89` | `3984.40` | `3802.79` | -159,118.09 USD | `-12.14%` | `15X Cross` |
| `1651` | `0xbf5a...88ba` | `SHORT` | 1,265,918.31 USD | `317.65` | `4091.80` | `3984.40` | `9918.99` | 33,864.73 USD | `+2.68%` | `20X Cross` |
| `1689` | `0xff31...ff6c` | `SHORT` | 1,235,412.00 USD | `310.00` | `4372.43` | `3984.40` | `4789.78` | 120,043.38 USD | `+9.72%` | `10X Isolated` |
| `1716` | `0xada6...6f88` | `LONG` | 1,209,374.70 USD | `303.47` | `4166.46` | `3984.40` | `1803.93` | -55,007.76 USD | `-4.55%` | `5X Cross` |
| `1879` | `0x50e2...d770` | `LONG` | 1,077,468.16 USD | `270.37` | `4243.58` | `3984.40` | `2562.72` | -69,858.30 USD | `-6.48%` | `20X Cross` |
| `1888` | `0x4c92...4f17` | `SHORT` | 1,062,934.54 USD | `266.72` | `4260.98` | `3984.40` | `6483.15` | 73,557.70 USD | `+6.92%` | `20X Cross` |
| `1954` | `0xd346...c4f3` | `LONG` | 1,016,944.15 USD | `255.17` | `4188.66` | `3984.40` | `3311.05` | -51,892.36 USD | `-5.10%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4002.80` | 24.02 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.02K USD at 4002.8000 USD [API] | `2026-10-23 01:55:44` |
| `ANNOUNCEMENT` | `INFO` | `4002.80` | 19.21 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.02K USD at 4002.8000 USD [API] | `2026-10-23 01:55:38` |
| `ANNOUNCEMENT` | `INFO` | `4002.80` | 198.54 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:GOLD Liquidated Short: 0.20K USD at 4002.8000 USD [API] | `2026-10-23 01:55:38` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4096.30` (Vol: 350,100.00 USD, Dist: `+2.69%`) | Long MP=`3937.38` (Vol: 356,200.00 USD, Dist: `--1.29%`)
  * 48H Horizon: Short MP=`4111.27` (Vol: 328,300.00 USD, Dist: `+3.07%`) | Long MP=`3936.60` (Vol: 378,100.00 USD, Dist: `--1.31%`)
  * 3D Horizon: Short MP=`4111.27` (Vol: 367,600.00 USD, Dist: `+3.07%`) | Long MP=`3949.08` (Vol: 404,600.00 USD, Dist: `--1.00%`)
  * 7D Horizon: Short MP=`4086.31` (Vol: 853,900.00 USD, Dist: `+2.44%`) | Long MP=`3927.24` (Vol: 1,100,000.00 USD, Dist: `--1.55%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `Long Liquidation` | `3584.50` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3588.80` | 15,180,000.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3591.00` | 5,590,000.00 USD | 5,590,000.00 USD | 4,460.00 USD | 0.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3593.10` | 15,160,000.00 USD | 15,160,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3595.10` | 5,570,000.00 USD | 5,570,000.00 USD | 28,070.00 USD | 0.00 USD | 20,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3597.40` | 15,150,000.00 USD | 15,150,000.00 USD | 92,800.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3599.20` | 5,520,000.00 USD | 5,520,000.00 USD | 21,680.00 USD | 0.00 USD | 18,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3601.70` | 15,040,000.00 USD | 15,040,000.00 USD | 175,610.00 USD | 0.00 USD | 67,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3603.30` | 5,480,000.00 USD | 5,480,000.00 USD | 63,060.00 USD | 0.00 USD | 48,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3606.00` | 14,790,000.00 USD | 14,790,000.00 USD | 134,320.00 USD | 0.00 USD | 53,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3607.40` | 5,370,000.00 USD | 5,370,000.00 USD | 14,680.00 USD | 0.00 USD | 10,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3610.30` | 14,610,000.00 USD | 14,610,000.00 USD | 83,580.00 USD | 0.00 USD | 21,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3611.50` | 5,350,000.00 USD | 5,350,000.00 USD | 25,560.00 USD | 0.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3614.60` | 14,500,000.00 USD | 14,500,000.00 USD | 89,070.00 USD | 0.00 USD | 16,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3615.60` | 5,310,000.00 USD | 5,310,000.00 USD | 31,290.00 USD | 0.00 USD | 7,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3618.90` | 14,400,000.00 USD | 14,400,000.00 USD | 40,780.00 USD | 0.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3619.70` | 5,270,000.00 USD | 5,270,000.00 USD | 42,080.00 USD | 0.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3623.20` | 14,350,000.00 USD | 14,350,000.00 USD | 59,230.00 USD | 0.00 USD | 24,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3623.80` | 5,220,000.00 USD | 5,220,000.00 USD | 61,240.00 USD | 0.00 USD | 7,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3627.50` | 14,260,000.00 USD | 14,260,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3627.90` | 5,150,000.00 USD | 5,150,000.00 USD | 26,230.00 USD | 0.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3631.80` | 14,160,000.00 USD | 14,160,000.00 USD | 60,720.00 USD | 0.00 USD | 6,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3632.00` | 5,120,000.00 USD | 5,120,000.00 USD | 4,940.00 USD | 0.00 USD | 2,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3636.10` | 5,120,000.00 USD | 5,120,000.00 USD | 11,520.00 USD | 0.00 USD | 204.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3636.10` | 14,090,000.00 USD | 14,090,000.00 USD | 20,410.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3640.40` | 14,070,000.00 USD | 14,070,000.00 USD | 55,830.00 USD | 0.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3644.70` | 14,000,000.00 USD | 14,000,000.00 USD | 17,720.00 USD | 0.00 USD | 11,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3649.00` | 13,970,000.00 USD | 13,970,000.00 USD | 24,860.00 USD | 0.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3653.30` | 13,940,000.00 USD | 13,940,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3657.60` | 13,910,000.00 USD | 13,910,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3661.90` | 13,880,000.00 USD | 13,880,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3666.20` | 13,860,000.00 USD | 13,860,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3820.60` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3824.70` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3825.30` | 13,850,000.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3828.80` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 12,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3829.60` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3832.90` | 5,070,000.00 USD | 5,070,000.00 USD | 49,590.00 USD | 0.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3833.90` | 13,740,000.00 USD | 13,740,000.00 USD | 86,270.00 USD | 0.00 USD | 34,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3837.00` | 4,950,000.00 USD | 4,950,000.00 USD | 69,390.00 USD | 0.00 USD | 78,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3838.20` | 13,620,000.00 USD | 13,620,000.00 USD | 271,140.00 USD | 0.00 USD | 60,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3841.10` | 4,800,000.00 USD | 4,800,000.00 USD | 87,190.00 USD | 0.00 USD | 94,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3842.50` | 13,280,000.00 USD | 13,280,000.00 USD | 557,810.00 USD | 0.00 USD | 224,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3845.20` | 4,620,000.00 USD | 4,620,000.00 USD | 190,490.00 USD | 0.00 USD | 114,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3846.80` | 12,500,000.00 USD | 12,500,000.00 USD | 535,820.00 USD | 0.00 USD | 157,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3849.30` | 4,320,000.00 USD | 4,320,000.00 USD | 35,100.00 USD | 0.00 USD | 31,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3851.10` | 11,810,000.00 USD | 11,810,000.00 USD | 231,930.00 USD | 0.00 USD | 79,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3853.40` | 4,250,000.00 USD | 4,250,000.00 USD | 97,530.00 USD | 0.00 USD | 33,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3855.40` | 11,500,000.00 USD | 11,500,000.00 USD | 219,990.00 USD | 0.00 USD | 50,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3857.50` | 4,120,000.00 USD | 4,120,000.00 USD | 94,090.00 USD | 0.00 USD | 21,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3859.70` | 11,230,000.00 USD | 11,230,000.00 USD | 174,170.00 USD | 0.00 USD | 22,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3861.60` | 4,000,000.00 USD | 4,000,000.00 USD | 156,450.00 USD | 0.00 USD | 34,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3864.00` | 11,030,000.00 USD | 11,030,000.00 USD | 204,130.00 USD | 0.00 USD | 73,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3865.70` | 3,810,000.00 USD | 3,810,000.00 USD | 185,640.00 USD | 0.00 USD | 22,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3868.30` | 10,750,000.00 USD | 10,750,000.00 USD | 298,110.00 USD | 0.00 USD | 32,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3869.80` | 3,600,000.00 USD | 3,600,000.00 USD | 114,850.00 USD | 0.00 USD | 10,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3872.60` | 10,420,000.00 USD | 10,420,000.00 USD | 220,790.00 USD | 0.00 USD | 43,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3873.90` | 3,480,000.00 USD | 3,480,000.00 USD | 27,180.00 USD | 0.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3876.90` | 10,160,000.00 USD | 10,160,000.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3878.00` | 3,440,000.00 USD | 3,440,000.00 USD | 33,210.00 USD | 0.00 USD | 824.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3881.20` | 9,990,000.00 USD | 9,990,000.00 USD | 116,920.00 USD | 0.00 USD | 31,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3882.10` | 3,410,000.00 USD | 3,410,000.00 USD | 5,280.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3885.50` | 9,840,000.00 USD | 9,840,000.00 USD | 124,650.00 USD | 0.00 USD | 24,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3889.80` | 9,690,000.00 USD | 9,690,000.00 USD | 85,430.00 USD | 0.00 USD | 25,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3894.10` | 9,580,000.00 USD | 9,580,000.00 USD | 126,480.00 USD | 0.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3898.40` | 9,450,000.00 USD | 9,450,000.00 USD | 132,740.00 USD | 0.00 USD | 9,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3902.60` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 48,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3902.70` | 9,300,000.00 USD | 9,300,000.00 USD | 17,060.00 USD | 0.00 USD | 72,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3906.70` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3907.00` | 9,210,000.00 USD | 9,210,000.00 USD | 56,630.00 USD | 0.00 USD | 101,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3910.80` | 3,330,000.00 USD | 3,330,000.00 USD | 30,450.00 USD | 0.00 USD | 82,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3911.30` | 9,060,000.00 USD | 9,060,000.00 USD | 51,010.00 USD | 0.00 USD | 81,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3914.90` | 3,220,000.00 USD | 3,220,000.00 USD | 166,670.00 USD | 0.00 USD | 118,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3915.60` | 8,920,000.00 USD | 8,920,000.00 USD | 287,340.00 USD | 0.00 USD | 143,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3919.00` | 2,930,000.00 USD | 2,930,000.00 USD | 122,800.00 USD | 0.00 USD | 138,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3919.90` | 8,490,000.00 USD | 8,490,000.00 USD | 674,750.00 USD | 0.00 USD | 199,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3923.10` | 2,670,000.00 USD | 2,670,000.00 USD | 262,450.00 USD | 0.00 USD | 299,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3924.20` | 7,620,000.00 USD | 7,620,000.00 USD | 1,200,000.00 USD | 0.00 USD | 464,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3927.20` | 2,110,000.00 USD | 2,110,000.00 USD | 266,840.00 USD | 0.00 USD | 96,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3928.50` | 5,960,000.00 USD | 5,960,000.00 USD | 913,310.00 USD | 0.00 USD | 195,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3931.30` | 1,750,000.00 USD | 1,750,000.00 USD | 92,000.00 USD | 0.00 USD | 60,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3932.80` | 4,850,000.00 USD | 4,850,000.00 USD | 380,870.00 USD | 0.00 USD | 128,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3935.40` | 1,590,000.00 USD | 1,590,000.00 USD | 207,080.00 USD | 0.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3937.10` | 4,340,000.00 USD | 4,340,000.00 USD | 466,400.00 USD | 0.00 USD | 74,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3939.50` | 1,310,000.00 USD | 1,310,000.00 USD | 225,840.00 USD | 0.00 USD | 28,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3941.40` | 3,800,000.00 USD | 3,800,000.00 USD | 287,460.00 USD | 0.00 USD | 104,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3943.60` | 1,050,000.00 USD | 1,050,000.00 USD | 272,530.00 USD | 0.00 USD | 65,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3945.70` | 3,400,000.00 USD | 3,400,000.00 USD | 468,070.00 USD | 0.00 USD | 118,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3947.70` | 716,760.00 USD | 716,760.00 USD | 343,950.00 USD | 0.00 USD | 43,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3950.00` | 2,820,000.00 USD | 2,820,000.00 USD | 529,640.00 USD | 0.00 USD | 78,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3951.80` | 329,200.00 USD | 329,200.00 USD | 185,240.00 USD | 0.00 USD | 19,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3954.30` | 2,210,000.00 USD | 2,210,000.00 USD | 437,760.00 USD | 0.00 USD | 53,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3955.90` | 124,590.00 USD | 124,590.00 USD | 55,340.00 USD | 0.00 USD | 6,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3958.60` | 1,720,000.00 USD | 1,720,000.00 USD | 275,800.00 USD | 0.00 USD | 38,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3960.00` | 62,450.00 USD | 62,450.00 USD | 60,830.00 USD | 0.00 USD | 1,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3962.90` | 1,400,000.00 USD | 1,400,000.00 USD | 277,640.00 USD | 0.00 USD | 56,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3964.10` | 606.18 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3967.20` | 1,070,000.00 USD | 1,070,000.00 USD | 148,670.00 USD | 0.00 USD | 57,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3971.50` | 863,560.00 USD | 863,560.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3975.80` | 616,600.00 USD | 616,600.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3980.10` | 347,370.00 USD | 347,370.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3984.40` | 110,560.00 USD | 110,560.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3988.70` | 76,450.00 USD | 76,450.00 USD | 76,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4058.40` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4061.80` | 60,950.00 USD | 60,950.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4062.50` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4066.60` | 73,370.00 USD | 73,370.00 USD | 0.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4070.40` | 263,230.00 USD | 263,230.00 USD | 34,460.00 USD | 0.00 USD | 167,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4070.70` | 186,300.00 USD | 186,300.00 USD | 30,450.00 USD | 0.00 USD | 82,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4074.70` | 545,210.00 USD | 545,210.00 USD | 138,080.00 USD | 0.00 USD | 143,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4074.80` | 471,040.00 USD | 471,040.00 USD | 166,670.00 USD | 0.00 USD | 118,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4078.90` | 725,520.00 USD | 725,520.00 USD | 122,800.00 USD | 0.00 USD | 131,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4079.00` | 1,490,000.00 USD | 1,490,000.00 USD | 773,860.00 USD | 0.00 USD | 167,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4083.00` | 1,200,000.00 USD | 1,200,000.00 USD | 191,740.00 USD | 0.00 USD | 286,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4083.30` | 2,980,000.00 USD | 2,980,000.00 USD | 1,110,000.00 USD | 0.00 USD | 384,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4087.10` | 1,650,000.00 USD | 1,650,000.00 USD | 337,560.00 USD | 0.00 USD | 111,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4087.60` | 4,090,000.00 USD | 4,090,000.00 USD | 844,290.00 USD | 0.00 USD | 266,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4091.20` | 1,770,000.00 USD | 1,770,000.00 USD | 55,810.00 USD | 0.00 USD | 63,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4091.90` | 4,750,000.00 USD | 4,750,000.00 USD | 514,970.00 USD | 0.00 USD | 144,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4095.30` | 2,030,000.00 USD | 2,030,000.00 USD | 195,600.00 USD | 0.00 USD | 60,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4096.20` | 5,160,000.00 USD | 5,160,000.00 USD | 310,220.00 USD | 0.00 USD | 100,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4099.40` | 2,260,000.00 USD | 2,260,000.00 USD | 194,880.00 USD | 0.00 USD | 38,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4100.50` | 5,620,000.00 USD | 5,620,000.00 USD | 415,790.00 USD | 0.00 USD | 42,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4103.50` | 2,640,000.00 USD | 2,640,000.00 USD | 313,700.00 USD | 0.00 USD | 63,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4104.80` | 6,120,000.00 USD | 6,120,000.00 USD | 367,480.00 USD | 0.00 USD | 134,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4107.60` | 3,000,000.00 USD | 3,000,000.00 USD | 321,740.00 USD | 0.00 USD | 43,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4109.10` | 6,740,000.00 USD | 6,740,000.00 USD | 537,000.00 USD | 0.00 USD | 76,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4111.70` | 3,250,000.00 USD | 3,250,000.00 USD | 229,700.00 USD | 0.00 USD | 19,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4113.40` | 7,240,000.00 USD | 7,240,000.00 USD | 434,270.00 USD | 0.00 USD | 63,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4115.80` | 3,320,000.00 USD | 3,320,000.00 USD | 54,370.00 USD | 0.00 USD | 15,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4117.70` | 7,570,000.00 USD | 7,570,000.00 USD | 288,910.00 USD | 0.00 USD | 49,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4119.90` | 3,390,000.00 USD | 3,390,000.00 USD | 66,420.00 USD | 0.00 USD | 1,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4122.00` | 7,880,000.00 USD | 7,880,000.00 USD | 272,900.00 USD | 0.00 USD | 32,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4124.00` | 3,400,000.00 USD | 3,400,000.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4126.30` | 8,200,000.00 USD | 8,200,000.00 USD | 252,890.00 USD | 0.00 USD | 70,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4130.60` | 8,400,000.00 USD | 8,400,000.00 USD | 143,990.00 USD | 0.00 USD | 48,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4134.90` | 8,670,000.00 USD | 8,670,000.00 USD | 240,010.00 USD | 0.00 USD | 35,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4139.20` | 8,880,000.00 USD | 8,880,000.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4140.40` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4143.50` | 9,120,000.00 USD | 9,120,000.00 USD | 199,160.00 USD | 0.00 USD | 42,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4144.50` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4147.80` | 9,270,000.00 USD | 9,270,000.00 USD | 59,830.00 USD | 0.00 USD | 91,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4148.60` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4152.10` | 9,480,000.00 USD | 9,480,000.00 USD | 133,610.00 USD | 0.00 USD | 71,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4152.70` | 3,570,000.00 USD | 3,570,000.00 USD | 67,910.00 USD | 0.00 USD | 55,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4156.40` | 9,780,000.00 USD | 9,780,000.00 USD | 243,560.00 USD | 0.00 USD | 57,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4156.80` | 3,700,000.00 USD | 3,700,000.00 USD | 51,070.00 USD | 0.00 USD | 78,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4160.70` | 10,230,000.00 USD | 10,230,000.00 USD | 336,690.00 USD | 0.00 USD | 111,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4160.90` | 3,880,000.00 USD | 3,880,000.00 USD | 87,190.00 USD | 0.00 USD | 85,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4165.00` | 4,180,000.00 USD | 4,180,000.00 USD | 180,220.00 USD | 0.00 USD | 122,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4165.00` | 11,030,000.00 USD | 11,030,000.00 USD | 584,890.00 USD | 0.00 USD | 215,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4169.10` | 4,240,000.00 USD | 4,240,000.00 USD | 38,210.00 USD | 0.00 USD | 18,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4169.30` | 11,500,000.00 USD | 11,500,000.00 USD | 384,920.00 USD | 0.00 USD | 91,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4173.20` | 4,350,000.00 USD | 4,350,000.00 USD | 74,610.00 USD | 0.00 USD | 36,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4173.60` | 11,740,000.00 USD | 11,740,000.00 USD | 181,290.00 USD | 0.00 USD | 60,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4177.30` | 4,480,000.00 USD | 4,480,000.00 USD | 102,960.00 USD | 0.00 USD | 27,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4177.90` | 11,990,000.00 USD | 11,990,000.00 USD | 209,170.00 USD | 0.00 USD | 37,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4181.40` | 4,620,000.00 USD | 4,620,000.00 USD | 117,490.00 USD | 0.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4182.20` | 12,190,000.00 USD | 12,190,000.00 USD | 167,760.00 USD | 0.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4185.50` | 4,770,000.00 USD | 4,770,000.00 USD | 130,020.00 USD | 0.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4186.50` | 12,450,000.00 USD | 12,450,000.00 USD | 188,450.00 USD | 0.00 USD | 68,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4189.60` | 4,940,000.00 USD | 4,940,000.00 USD | 149,320.00 USD | 0.00 USD | 20,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4190.80` | 12,760,000.00 USD | 12,760,000.00 USD | 285,320.00 USD | 0.00 USD | 24,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4193.70` | 5,040,000.00 USD | 5,040,000.00 USD | 88,920.00 USD | 0.00 USD | 8,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4195.10` | 13,000,000.00 USD | 13,000,000.00 USD | 205,140.00 USD | 0.00 USD | 38,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4197.80` | 5,070,000.00 USD | 5,070,000.00 USD | 22,540.00 USD | 0.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4199.40` | 13,130,000.00 USD | 13,130,000.00 USD | 101,170.00 USD | 0.00 USD | 24,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4201.90` | 5,100,000.00 USD | 5,100,000.00 USD | 35,540.00 USD | 0.00 USD | 824.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4203.70` | 13,320,000.00 USD | 13,320,000.00 USD | 164,070.00 USD | 0.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4206.00` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 303.09 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4208.00` | 13,430,000.00 USD | 13,430,000.00 USD | 82,850.00 USD | 0.00 USD | 32,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4212.30` | 13,540,000.00 USD | 13,540,000.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4216.60` | 13,650,000.00 USD | 13,650,000.00 USD | 104,620.00 USD | 0.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4220.90` | 13,780,000.00 USD | 13,780,000.00 USD | 120,590.00 USD | 0.00 USD | 8,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4225.20` | 13,870,000.00 USD | 13,870,000.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4229.50` | 13,910,000.00 USD | 13,910,000.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4233.80` | 13,960,000.00 USD | 13,960,000.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4238.10` | 13,980,000.00 USD | 13,980,000.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4378.20` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4380.00` | 13,990,000.00 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4382.30` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4386.40` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4388.60` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4390.50` | 5,140,000.00 USD | 5,140,000.00 USD | 4,460.00 USD | 0.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4392.90` | 14,040,000.00 USD | 14,040,000.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4394.60` | 5,180,000.00 USD | 5,180,000.00 USD | 28,070.00 USD | 0.00 USD | 14,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4397.20` | 14,150,000.00 USD | 14,150,000.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4398.70` | 5,210,000.00 USD | 5,210,000.00 USD | 14,150.00 USD | 0.00 USD | 14,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4401.50` | 14,350,000.00 USD | 14,350,000.00 USD | 143,560.00 USD | 0.00 USD | 62,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4402.80` | 5,270,000.00 USD | 5,270,000.00 USD | 30,030.00 USD | 0.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4404.20` | 5,330,000.00 USD | 5,330,000.00 USD | 40,550.00 USD | 0.00 USD | 17,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4405.80` | 14,520,000.00 USD | 14,520,000.00 USD | 116,280.00 USD | 0.00 USD | 48,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4410.10` | 14,650,000.00 USD | 14,650,000.00 USD | 112,800.00 USD | 0.00 USD | 22,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4414.40` | 14,700,000.00 USD | 14,700,000.00 USD | 36,920.00 USD | 0.00 USD | 14,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4418.70` | 14,780,000.00 USD | 14,780,000.00 USD | 66,780.00 USD | 0.00 USD | 11,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4423.00` | 14,820,000.00 USD | 14,820,000.00 USD | 31,340.00 USD | 0.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4427.10` | 14,900,000.00 USD | 14,900,000.00 USD | 59,230.00 USD | 0.00 USD | 17,850.00 USD | `Tier 1 CEX` |

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
| `7D` | `3584.50` | 15,190,000.00 USD | 0.00 USD | 15,190,000.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `7D` | `3588.80` | 15,180,000.00 USD | 0.00 USD | 15,180,000.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `3591.00` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 4,460.00 USD | 0.00 USD | 9,350.00 USD |
| `7D` | `3593.10` | 15,160,000.00 USD | 0.00 USD | 15,160,000.00 USD | 11,530.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `3595.10` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 28,070.00 USD | 0.00 USD | 20,370.00 USD |
| `7D` | `3597.40` | 15,150,000.00 USD | 0.00 USD | 15,150,000.00 USD | 92,800.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `3599.20` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 21,680.00 USD | 0.00 USD | 18,120.00 USD |
| `7D` | `3601.70` | 15,040,000.00 USD | 0.00 USD | 15,040,000.00 USD | 175,610.00 USD | 0.00 USD | 67,670.00 USD |
| `1D` | `3603.30` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 63,060.00 USD | 0.00 USD | 48,430.00 USD |
| `7D` | `3606.00` | 14,790,000.00 USD | 0.00 USD | 14,790,000.00 USD | 134,320.00 USD | 0.00 USD | 53,650.00 USD |
| `1D` | `3607.40` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 14,680.00 USD | 0.00 USD | 10,640.00 USD |
| `7D` | `3610.30` | 14,610,000.00 USD | 0.00 USD | 14,610,000.00 USD | 83,580.00 USD | 0.00 USD | 21,070.00 USD |
| `1D` | `3611.50` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 25,560.00 USD | 0.00 USD | 8,870.00 USD |
| `7D` | `3614.60` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 89,070.00 USD | 0.00 USD | 16,470.00 USD |
| `1D` | `3615.60` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 31,290.00 USD | 0.00 USD | 7,470.00 USD |
| `7D` | `3618.90` | 14,400,000.00 USD | 0.00 USD | 14,400,000.00 USD | 40,780.00 USD | 0.00 USD | 8,780.00 USD |
| `1D` | `3619.70` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 42,080.00 USD | 0.00 USD | 10,780.00 USD |
| `7D` | `3623.20` | 14,350,000.00 USD | 0.00 USD | 14,350,000.00 USD | 59,230.00 USD | 0.00 USD | 24,620.00 USD |
| `1D` | `3623.80` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 61,240.00 USD | 0.00 USD | 7,400.00 USD |
| `7D` | `3627.50` | 14,260,000.00 USD | 0.00 USD | 14,260,000.00 USD | 88,510.00 USD | 0.00 USD | 13,590.00 USD |
| `1D` | `3627.90` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 26,230.00 USD | 0.00 USD | 3,350.00 USD |
| `7D` | `3631.80` | 14,160,000.00 USD | 0.00 USD | 14,160,000.00 USD | 60,720.00 USD | 0.00 USD | 6,570.00 USD |
| `1D` | `3632.00` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 4,940.00 USD | 0.00 USD | 2,710.00 USD |
| `1D` | `3636.10` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 11,520.00 USD | 0.00 USD | 204.34 USD |
| `7D` | `3636.10` | 14,090,000.00 USD | 0.00 USD | 14,090,000.00 USD | 20,410.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `3640.40` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 55,830.00 USD | 0.00 USD | 7,210.00 USD |
| `7D` | `3644.70` | 14,000,000.00 USD | 0.00 USD | 14,000,000.00 USD | 17,720.00 USD | 0.00 USD | 11,980.00 USD |
| `7D` | `3649.00` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 24,860.00 USD | 0.00 USD | 4,150.00 USD |
| `7D` | `3653.30` | 13,940,000.00 USD | 0.00 USD | 13,940,000.00 USD | 29,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3657.60` | 13,910,000.00 USD | 0.00 USD | 13,910,000.00 USD | 29,540.00 USD | 0.00 USD | 5,330.00 USD |
| `7D` | `3661.90` | 13,880,000.00 USD | 0.00 USD | 13,880,000.00 USD | 19,350.00 USD | 0.00 USD | 5,170.00 USD |
| `7D` | `3666.20` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3820.60` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `1D` | `3824.70` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD |
| `7D` | `3825.30` | 13,850,000.00 USD | 0.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 30,470.00 USD |
| `1D` | `3828.80` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 12,560.00 USD |
| `7D` | `3829.60` | 13,820,000.00 USD | 0.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 81,210.00 USD |
| `1D` | `3832.90` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 49,590.00 USD | 0.00 USD | 67,000.00 USD |
| `7D` | `3833.90` | 13,740,000.00 USD | 0.00 USD | 13,740,000.00 USD | 86,270.00 USD | 0.00 USD | 34,180.00 USD |
| `1D` | `3837.00` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 69,390.00 USD | 0.00 USD | 78,330.00 USD |
| `7D` | `3838.20` | 13,620,000.00 USD | 0.00 USD | 13,620,000.00 USD | 271,140.00 USD | 0.00 USD | 60,650.00 USD |
| `1D` | `3841.10` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 87,190.00 USD | 0.00 USD | 94,840.00 USD |
| `7D` | `3842.50` | 13,280,000.00 USD | 0.00 USD | 13,280,000.00 USD | 557,810.00 USD | 0.00 USD | 224,650.00 USD |
| `1D` | `3845.20` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 190,490.00 USD | 0.00 USD | 114,490.00 USD |
| `7D` | `3846.80` | 12,500,000.00 USD | 0.00 USD | 12,500,000.00 USD | 535,820.00 USD | 0.00 USD | 157,990.00 USD |
| `1D` | `3849.30` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 35,100.00 USD | 0.00 USD | 31,950.00 USD |
| `7D` | `3851.10` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 231,930.00 USD | 0.00 USD | 79,320.00 USD |
| `1D` | `3853.40` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 97,530.00 USD | 0.00 USD | 33,200.00 USD |
| `7D` | `3855.40` | 11,500,000.00 USD | 0.00 USD | 11,500,000.00 USD | 219,990.00 USD | 0.00 USD | 50,490.00 USD |
| `1D` | `3857.50` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 94,090.00 USD | 0.00 USD | 21,490.00 USD |
| `7D` | `3859.70` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 174,170.00 USD | 0.00 USD | 22,980.00 USD |
| `1D` | `3861.60` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 156,450.00 USD | 0.00 USD | 34,850.00 USD |
| `7D` | `3864.00` | 11,030,000.00 USD | 0.00 USD | 11,030,000.00 USD | 204,130.00 USD | 0.00 USD | 73,250.00 USD |
| `1D` | `3865.70` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 185,640.00 USD | 0.00 USD | 22,730.00 USD |
| `7D` | `3868.30` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 298,110.00 USD | 0.00 USD | 32,300.00 USD |
| `1D` | `3869.80` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 114,850.00 USD | 0.00 USD | 10,740.00 USD |
| `7D` | `3872.60` | 10,420,000.00 USD | 0.00 USD | 10,420,000.00 USD | 220,790.00 USD | 0.00 USD | 43,620.00 USD |
| `1D` | `3873.90` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 27,180.00 USD | 0.00 USD | 7,780.00 USD |
| `7D` | `3876.90` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 148,310.00 USD | 0.00 USD | 19,440.00 USD |
| `1D` | `3878.00` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 33,210.00 USD | 0.00 USD | 824.23 USD |
| `7D` | `3881.20` | 9,990,000.00 USD | 0.00 USD | 9,990,000.00 USD | 116,920.00 USD | 0.00 USD | 31,390.00 USD |
| `1D` | `3882.10` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 5,280.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `3885.50` | 9,840,000.00 USD | 0.00 USD | 9,840,000.00 USD | 124,650.00 USD | 0.00 USD | 24,550.00 USD |
| `7D` | `3889.80` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 85,430.00 USD | 0.00 USD | 25,820.00 USD |
| `7D` | `3894.10` | 9,580,000.00 USD | 0.00 USD | 9,580,000.00 USD | 126,480.00 USD | 0.00 USD | 8,570.00 USD |
| `7D` | `3898.40` | 9,450,000.00 USD | 0.00 USD | 9,450,000.00 USD | 132,740.00 USD | 0.00 USD | 9,060.00 USD |
| `1D` | `3902.60` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 0.00 USD | 0.00 USD | 48,250.00 USD |
| `7D` | `3902.70` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 17,060.00 USD | 0.00 USD | 72,710.00 USD |
| `1D` | `3906.70` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 25,120.00 USD |
| `7D` | `3907.00` | 9,210,000.00 USD | 0.00 USD | 9,210,000.00 USD | 56,630.00 USD | 0.00 USD | 101,220.00 USD |
| `1D` | `3910.80` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 30,450.00 USD | 0.00 USD | 82,480.00 USD |
| `7D` | `3911.30` | 9,060,000.00 USD | 0.00 USD | 9,060,000.00 USD | 51,010.00 USD | 0.00 USD | 81,430.00 USD |
| `1D` | `3914.90` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 166,670.00 USD | 0.00 USD | 118,070.00 USD |
| `7D` | `3915.60` | 8,920,000.00 USD | 0.00 USD | 8,920,000.00 USD | 287,340.00 USD | 0.00 USD | 143,900.00 USD |
| `1D` | `3919.00` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 122,800.00 USD | 0.00 USD | 138,160.00 USD |
| `7D` | `3919.90` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 674,750.00 USD | 0.00 USD | 199,110.00 USD |
| `1D` | `3923.10` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 262,450.00 USD | 0.00 USD | 299,010.00 USD |
| `7D` | `3924.20` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 1,200,000.00 USD | 0.00 USD | 464,810.00 USD |
| `1D` | `3927.20` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 266,840.00 USD | 0.00 USD | 96,060.00 USD |
| `7D` | `3928.50` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 913,310.00 USD | 0.00 USD | 195,870.00 USD |
| `1D` | `3931.30` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 92,000.00 USD | 0.00 USD | 60,750.00 USD |
| `7D` | `3932.80` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 380,870.00 USD | 0.00 USD | 128,930.00 USD |
| `1D` | `3935.40` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 207,080.00 USD | 0.00 USD | 76,870.00 USD |
| `7D` | `3937.10` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 466,400.00 USD | 0.00 USD | 74,650.00 USD |
| `1D` | `3939.50` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 225,840.00 USD | 0.00 USD | 28,980.00 USD |
| `7D` | `3941.40` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 287,460.00 USD | 0.00 USD | 104,590.00 USD |
| `1D` | `3943.60` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 272,530.00 USD | 0.00 USD | 65,260.00 USD |
| `7D` | `3945.70` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 468,070.00 USD | 0.00 USD | 118,120.00 USD |
| `1D` | `3947.70` | 716,760.00 USD | 0.00 USD | 716,760.00 USD | 343,950.00 USD | 0.00 USD | 43,620.00 USD |
| `7D` | `3950.00` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 529,640.00 USD | 0.00 USD | 78,520.00 USD |
| `1D` | `3951.80` | 329,200.00 USD | 0.00 USD | 329,200.00 USD | 185,240.00 USD | 0.00 USD | 19,370.00 USD |
| `7D` | `3954.30` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 437,760.00 USD | 0.00 USD | 53,640.00 USD |
| `1D` | `3955.90` | 124,590.00 USD | 0.00 USD | 124,590.00 USD | 55,340.00 USD | 0.00 USD | 6,800.00 USD |
| `7D` | `3958.60` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 275,800.00 USD | 0.00 USD | 38,590.00 USD |
| `1D` | `3960.00` | 62,450.00 USD | 0.00 USD | 62,450.00 USD | 60,830.00 USD | 0.00 USD | 1,020.00 USD |
| `7D` | `3962.90` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 277,640.00 USD | 0.00 USD | 56,430.00 USD |
| `1D` | `3964.10` | 606.18 USD | 0.00 USD | 606.18 USD | 0.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `3967.20` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 148,670.00 USD | 0.00 USD | 57,880.00 USD |
| `7D` | `3971.50` | 863,560.00 USD | 0.00 USD | 863,560.00 USD | 200,930.00 USD | 0.00 USD | 46,030.00 USD |
| `7D` | `3975.80` | 616,600.00 USD | 0.00 USD | 616,600.00 USD | 255,840.00 USD | 0.00 USD | 13,380.00 USD |
| `7D` | `3980.10` | 347,370.00 USD | 0.00 USD | 347,370.00 USD | 232,530.00 USD | 0.00 USD | 4,280.00 USD |
| `7D` | `3984.40` | 110,560.00 USD | 0.00 USD | 110,560.00 USD | 34,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3988.30` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3988.70` | 76,450.00 USD | 0.00 USD | 76,450.00 USD | 76,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3989.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4058.40` | 19,400.00 USD | 19,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,400.00 USD |
| `7D` | `4061.80` | 60,950.00 USD | 60,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 60,950.00 USD |
| `1D` | `4062.50` | 48,250.00 USD | 48,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,860.00 USD |
| `1D` | `4066.60` | 73,370.00 USD | 73,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,120.00 USD |
| `7D` | `4070.40` | 263,230.00 USD | 263,230.00 USD | 0.00 USD | 34,460.00 USD | 0.00 USD | 167,820.00 USD |
| `1D` | `4070.70` | 186,300.00 USD | 186,300.00 USD | 0.00 USD | 30,450.00 USD | 0.00 USD | 82,480.00 USD |
| `7D` | `4074.70` | 545,210.00 USD | 545,210.00 USD | 0.00 USD | 138,080.00 USD | 0.00 USD | 143,900.00 USD |
| `1D` | `4074.80` | 471,040.00 USD | 471,040.00 USD | 0.00 USD | 166,670.00 USD | 0.00 USD | 118,070.00 USD |
| `1D` | `4078.90` | 725,520.00 USD | 725,520.00 USD | 0.00 USD | 122,800.00 USD | 0.00 USD | 131,680.00 USD |
| `7D` | `4079.00` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 773,860.00 USD | 0.00 USD | 167,100.00 USD |
| `1D` | `4083.00` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 191,740.00 USD | 0.00 USD | 286,670.00 USD |
| `7D` | `4083.30` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 384,910.00 USD |
| `1D` | `4087.10` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 337,560.00 USD | 0.00 USD | 111,920.00 USD |
| `7D` | `4087.60` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 844,290.00 USD | 0.00 USD | 266,230.00 USD |
| `1D` | `4091.20` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 55,810.00 USD | 0.00 USD | 63,710.00 USD |
| `7D` | `4091.90` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 514,970.00 USD | 0.00 USD | 144,150.00 USD |
| `1D` | `4095.30` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 195,600.00 USD | 0.00 USD | 60,140.00 USD |
| `7D` | `4096.20` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 310,220.00 USD | 0.00 USD | 100,990.00 USD |
| `1D` | `4099.40` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 194,880.00 USD | 0.00 USD | 38,300.00 USD |
| `7D` | `4100.50` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 415,790.00 USD | 0.00 USD | 42,790.00 USD |
| `1D` | `4103.50` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 313,700.00 USD | 0.00 USD | 63,240.00 USD |
| `7D` | `4104.80` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 367,480.00 USD | 0.00 USD | 134,430.00 USD |
| `1D` | `4107.60` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 321,740.00 USD | 0.00 USD | 43,180.00 USD |
| `7D` | `4109.10` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 537,000.00 USD | 0.00 USD | 76,750.00 USD |
| `1D` | `4111.70` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 229,700.00 USD | 0.00 USD | 19,850.00 USD |
| `7D` | `4113.40` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 434,270.00 USD | 0.00 USD | 63,950.00 USD |
| `1D` | `4115.80` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 54,370.00 USD | 0.00 USD | 15,560.00 USD |
| `7D` | `4117.70` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 288,910.00 USD | 0.00 USD | 49,430.00 USD |
| `1D` | `4119.90` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 66,420.00 USD | 0.00 USD | 1,650.00 USD |
| `7D` | `4122.00` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 272,900.00 USD | 0.00 USD | 32,280.00 USD |
| `1D` | `4124.00` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 10,570.00 USD | 0.00 USD | 606.18 USD |
| `7D` | `4126.30` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 252,890.00 USD | 0.00 USD | 70,690.00 USD |
| `7D` | `4130.60` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 143,990.00 USD | 0.00 USD | 48,360.00 USD |
| `7D` | `4134.90` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 240,010.00 USD | 0.00 USD | 35,130.00 USD |
| `7D` | `4139.20` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 189,720.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4140.40` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,700.00 USD |
| `7D` | `4143.50` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 199,160.00 USD | 0.00 USD | 42,950.00 USD |
| `1D` | `4144.50` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,430.00 USD |
| `7D` | `4147.80` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 59,830.00 USD | 0.00 USD | 91,570.00 USD |
| `1D` | `4148.60` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,520.00 USD |
| `7D` | `4152.10` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 133,610.00 USD | 0.00 USD | 71,220.00 USD |
| `1D` | `4152.70` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 67,910.00 USD | 0.00 USD | 55,030.00 USD |
| `7D` | `4156.40` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 243,560.00 USD | 0.00 USD | 57,810.00 USD |
| `1D` | `4156.80` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 51,070.00 USD | 0.00 USD | 78,330.00 USD |
| `7D` | `4160.70` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 336,690.00 USD | 0.00 USD | 111,100.00 USD |
| `1D` | `4160.90` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 87,190.00 USD | 0.00 USD | 85,070.00 USD |
| `1D` | `4165.00` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 180,220.00 USD | 0.00 USD | 122,710.00 USD |
| `7D` | `4165.00` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 584,890.00 USD | 0.00 USD | 215,140.00 USD |
| `1D` | `4169.10` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 38,210.00 USD | 0.00 USD | 18,580.00 USD |
| `7D` | `4169.30` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 384,920.00 USD | 0.00 USD | 91,530.00 USD |
| `1D` | `4173.20` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 74,610.00 USD | 0.00 USD | 36,700.00 USD |
| `7D` | `4173.60` | 11,740,000.00 USD | 11,740,000.00 USD | 0.00 USD | 181,290.00 USD | 0.00 USD | 60,200.00 USD |
| `1D` | `4177.30` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 102,960.00 USD | 0.00 USD | 27,790.00 USD |
| `7D` | `4177.90` | 11,990,000.00 USD | 11,990,000.00 USD | 0.00 USD | 209,170.00 USD | 0.00 USD | 37,330.00 USD |
| `1D` | `4181.40` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 117,490.00 USD | 0.00 USD | 21,420.00 USD |
| `7D` | `4182.20` | 12,190,000.00 USD | 12,190,000.00 USD | 0.00 USD | 167,760.00 USD | 0.00 USD | 35,380.00 USD |
| `1D` | `4185.50` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 130,020.00 USD | 0.00 USD | 27,230.00 USD |
| `7D` | `4186.50` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 188,450.00 USD | 0.00 USD | 68,840.00 USD |
| `1D` | `4189.60` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 149,320.00 USD | 0.00 USD | 20,750.00 USD |
| `7D` | `4190.80` | 12,760,000.00 USD | 12,760,000.00 USD | 0.00 USD | 285,320.00 USD | 0.00 USD | 24,310.00 USD |
| `1D` | `4193.70` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 88,920.00 USD | 0.00 USD | 8,740.00 USD |
| `7D` | `4195.10` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 205,140.00 USD | 0.00 USD | 38,220.00 USD |
| `1D` | `4197.80` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 22,540.00 USD | 0.00 USD | 3,080.00 USD |
| `7D` | `4199.40` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 101,170.00 USD | 0.00 USD | 24,830.00 USD |
| `1D` | `4201.90` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 35,540.00 USD | 0.00 USD | 824.23 USD |
| `7D` | `4203.70` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 164,070.00 USD | 0.00 USD | 23,560.00 USD |
| `1D` | `4206.00` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 303.09 USD |
| `7D` | `4208.00` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 82,850.00 USD | 0.00 USD | 32,380.00 USD |
| `7D` | `4212.30` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 87,390.00 USD | 0.00 USD | 22,060.00 USD |
| `7D` | `4216.60` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 104,620.00 USD | 0.00 USD | 7,320.00 USD |
| `7D` | `4220.90` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 120,590.00 USD | 0.00 USD | 8,830.00 USD |
| `7D` | `4225.20` | 13,870,000.00 USD | 13,870,000.00 USD | 0.00 USD | 73,850.00 USD | 0.00 USD | 10,180.00 USD |
| `7D` | `4229.50` | 13,910,000.00 USD | 13,910,000.00 USD | 0.00 USD | 29,910.00 USD | 0.00 USD | 13,000.00 USD |
| `7D` | `4233.80` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 6,750.00 USD |
| `7D` | `4238.10` | 13,980,000.00 USD | 13,980,000.00 USD | 0.00 USD | 16,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4378.20` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,880.00 USD |
| `7D` | `4380.00` | 13,990,000.00 USD | 13,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12,190.00 USD |
| `1D` | `4382.30` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD |
| `1D` | `4386.40` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,020.00 USD |
| `7D` | `4388.60` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,660.00 USD |
| `1D` | `4390.50` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 4,460.00 USD | 0.00 USD | 17,600.00 USD |
| `7D` | `4392.90` | 14,040,000.00 USD | 14,040,000.00 USD | 0.00 USD | 27,620.00 USD | 0.00 USD | 1,460.00 USD |
| `1D` | `4394.60` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 28,070.00 USD | 0.00 USD | 14,860.00 USD |
| `7D` | `4397.20` | 14,150,000.00 USD | 14,150,000.00 USD | 0.00 USD | 92,410.00 USD | 0.00 USD | 17,970.00 USD |
| `1D` | `4398.70` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 14,150.00 USD | 0.00 USD | 14,090.00 USD |
| `7D` | `4401.50` | 14,350,000.00 USD | 14,350,000.00 USD | 0.00 USD | 143,560.00 USD | 0.00 USD | 62,400.00 USD |
| `1D` | `4402.80` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 30,030.00 USD | 0.00 USD | 32,720.00 USD |
| `1D` | `4404.20` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 40,550.00 USD | 0.00 USD | 17,000.00 USD |
| `7D` | `4405.80` | 14,520,000.00 USD | 14,520,000.00 USD | 0.00 USD | 116,280.00 USD | 0.00 USD | 48,470.00 USD |
| `7D` | `4410.10` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 112,800.00 USD | 0.00 USD | 22,020.00 USD |
| `7D` | `4414.40` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 36,920.00 USD | 0.00 USD | 14,010.00 USD |
| `7D` | `4418.70` | 14,780,000.00 USD | 14,780,000.00 USD | 0.00 USD | 66,780.00 USD | 0.00 USD | 11,960.00 USD |
| `7D` | `4423.00` | 14,820,000.00 USD | 14,820,000.00 USD | 0.00 USD | 31,340.00 USD | 0.00 USD | 8,780.00 USD |
| `7D` | `4427.10` | 14,900,000.00 USD | 14,900,000.00 USD | 0.00 USD | 59,230.00 USD | 0.00 USD | 17,850.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `274.38M` | Total OI Tokens: `68,787.8 PAXG`
  * 1h OI Change: `-0.23%` | 4h OI Change: `-0.32%` | 24h OI Change: `-0.37%`
  * Exchange Breakdown: Binance=`104.70M` | Bybit=`24.46M` | OKX=`-` | Hyperliquid=`24.74M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.92K` | Last 24h: `17.74K` | Last 3d: `85.70K` | Last 7d: `216.77K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0026%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0050%` |
| **USDT MEXC** | `0.0026%` | **USDT BingX** | `-` |
| **USDT Gate** | `0.0022%` | **USDT Bitget** | `0.0050%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `PAXG` | `35.80%` | `64.20%` | `0.56` | 2,850,000.00 USD |
| `15M` | `Binance` | `49.85%` | `50.15%` | `0.99` | 536,450.00 USD |
| `15M` | `OKX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bybit` | `33.01%` | `66.99%` | `0.49` | 504,720.00 USD |
| `15M` | `KuCoin` | `27.72%` | `72.28%` | `0.38` | 27,870.00 USD |
| `15M` | `Gate` | `44.18%` | `55.82%` | `0.79` | 74,540.00 USD |
| `15M` | `Bitget` | `39.04%` | `60.96%` | `0.64` | 141,540.00 USD |
| `15M` | `BingX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `MEXC` | `23.97%` | `76.03%` | `0.32` | 944,980.00 USD |
| `15M` | `Bitunix` | `51.01%` | `48.99%` | `1.04` | 127,630.00 USD |
| `15M` | `Hyperliquid` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `35.2%` | `64.8%` | `0.54` | 267,120.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `6.93%` | `93.07%` | `0.07` | 114,030.00 USD |
| `15M` | `HTX` | `3.6%` | `96.4%` | `0.04` | 6,090.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `94.27%` | `5.73%` | `16.45` | 100,740.00 USD |
| `15M` | `Aster` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `49.85%` | `50.15%` | `0.99` | 536,450.00 USD |
| `15M` | `Global Accounts` | `35.80%` | `64.20%` | `0.56` | 2,850,000.00 USD |
| `1H` | `PAXG` | `54.70%` | `45.30%` | `1.21` | 7,170,000.00 USD |
| `1H` | `Binance` | `46.19%` | `53.81%` | `0.86` | 2,530,000.00 USD |
| `1H` | `OKX` | `47.38%` | `52.62%` | `0.90` | 1,070,000.00 USD |
| `1H` | `Bybit` | `55%` | `45%` | `1.22` | 418,770.00 USD |
| `1H` | `KuCoin` | `65.62%` | `34.38%` | `1.91` | 220,390.00 USD |
| `1H` | `Gate` | `52.36%` | `47.64%` | `1.10` | 200,100.00 USD |
| `1H` | `Bitget` | `57.7%` | `42.3%` | `1.36` | 302,830.00 USD |
| `1H` | `BingX` | `44.19%` | `55.81%` | `0.79` | 310,930.00 USD |
| `1H` | `MEXC` | `67.63%` | `32.37%` | `2.09` | 726,660.00 USD |
| `1H` | `Bitunix` | `43.9%` | `56.1%` | `0.78` | 127,680.00 USD |
| `1H` | `Hyperliquid` | `71.36%` | `28.64%` | `2.49` | 224,610.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.73%` | `50.27%` | `0.99` | 298,940.00 USD |
| `1H` | `Crypto.com` | `43.53%` | `56.47%` | `0.77` | 5,310.00 USD |
| `1H` | `WhiteBIT` | `84.85%` | `15.15%` | `5.60` | 685,270.00 USD |
| `1H` | `HTX` | `81.36%` | `18.64%` | `4.36` | 1,590.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `68.82%` | `31.18%` | `2.21` | 13,880.00 USD |
| `1H` | `Aster` | `92.54%` | `7.46%` | `12.40` | 221.71 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `15.63%` | `84.37%` | `0.19` | 40,200.00 USD |
| `1H` | `Whale Positions` | `46.19%` | `53.81%` | `0.86` | 2,530,000.00 USD |
| `1H` | `Global Accounts` | `54.70%` | `45.30%` | `1.21` | 7,170,000.00 USD |
| `4H` | `PAXG` | `48.62%` | `51.38%` | `0.95` | 41,480,000.00 USD |
| `4H` | `Binance` | `49.55%` | `50.45%` | `0.98` | 15,550,000.00 USD |
| `4H` | `OKX` | `46.69%` | `53.31%` | `0.88` | 6,080,000.00 USD |
| `4H` | `Bybit` | `47.88%` | `52.12%` | `0.92` | 4,770,000.00 USD |
| `4H` | `KuCoin` | `49.34%` | `50.66%` | `0.97` | 709,920.00 USD |
| `4H` | `Gate` | `45.02%` | `54.98%` | `0.82` | 1,280,000.00 USD |
| `4H` | `Bitget` | `48.34%` | `51.66%` | `0.94` | 2,710,000.00 USD |
| `4H` | `BingX` | `29.14%` | `70.86%` | `0.41` | 3,020,000.00 USD |
| `4H` | `MEXC` | `47.87%` | `52.13%` | `0.92` | 2,730,000.00 USD |
| `4H` | `Bitunix` | `48.84%` | `51.16%` | `0.95` | 602,870.00 USD |
| `4H` | `Hyperliquid` | `59.81%` | `40.19%` | `1.49` | 594,030.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.67%` | `50.33%` | `0.99` | 1,520,000.00 USD |
| `4H` | `Crypto.com` | `41.66%` | `58.34%` | `0.71` | 25,870.00 USD |
| `4H` | `WhiteBIT` | `83.97%` | `16.03%` | `5.24` | 1,570,000.00 USD |
| `4H` | `HTX` | `83.89%` | `16.11%` | `5.21` | 29,750.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.96%` | `57.04%` | `0.75` | 87,140.00 USD |
| `4H` | `Aster` | `49.06%` | `50.94%` | `0.96` | 45,120.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `63.34%` | `36.66%` | `1.73` | 156,970.00 USD |
| `4H` | `Whale Positions` | `49.55%` | `50.45%` | `0.98` | 15,550,000.00 USD |
| `4H` | `Global Accounts` | `48.62%` | `51.38%` | `0.95` | 41,480,000.00 USD |


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
| `5m` | -15,360.00 USD | -3,160.00 USD | **`DISTRIBUTION`** |
| `15m` | -84,550.00 USD | -403,720.00 USD | **`DISTRIBUTION`** |
| `30m` | -104,060.00 USD | -274,720.00 USD | **`DISTRIBUTION`** |
| `1h` | -301,320.00 USD | -187,040.00 USD | **`DISTRIBUTION`** |
| `2h` | -748,930.00 USD | 493,340.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,700,000.00 USD | -887,170.00 USD | **`DISTRIBUTION`** |
| `6h` | -23,130.00 USD | 171,080.00 USD | **`ACCUMULATION`** |
| `8h` | -181,080.00 USD | -81,500.00 USD | **`DISTRIBUTION`** |
| `12h` | 300,650.00 USD | -844,870.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,330,000.00 USD | 638,790.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,110,000.00 USD | -8,180,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -20,350,000.00 USD | -71,080,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-15.36K` | 15m=`-84.55K` | 1h=`-301.32K` | 24h=`-1.33M`
* Futures Capital Netflows: 5m=`-3.16K` | 15m=`-403.72K` | 1h=`-187.04K` | 24h=`+638.79K`
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
  * `2026-10-30 15:49:55 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:55 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:31:55 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:55 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:55 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3982.85` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3973.22` (Risk Distance: `9.63` pts)
  * +2.5R Take Profit: `4006.93`
  * Mathematical Lot Sizing: **`1.03 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4007.50` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4017.13` (Risk Distance: `9.63` pts)
  * +2.5R Take Profit: `3983.42`
  * Mathematical Lot Sizing: **`1.03 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4017.75`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
