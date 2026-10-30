# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 14:26:38 IST` (`2026-10-30 08:56:38 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `96.87` | **Live Ask Quote**: `97.09` | **Mid Price**: `96.98`
- **Spread Points**: `22.00` | **Spread BPS**: `22.69 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.01 USD` | Point Value (0.01 Lot): `0.0001 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `95.60` | VWAP Z-Score: `+0.74` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.6297` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `48.25` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `100.59` | Lower -3.00σ Band: `90.61`
  * Upper +2.51σ Band: `99.78` | Lower -2.51σ Band: `91.43`
  * Upper +2.01σ Band: `98.95` | Lower -2.01σ Band: `92.26`
  * Upper +2.00σ Band: `98.93` | Lower -2.00σ Band: `92.27`
  * Upper +1.28σ Band: `97.73` | Lower -1.28σ Band: `93.47`
  * Upper +1.00σ Band: `97.27` | Lower -1.00σ Band: `93.94`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`97.14` | EMA-20=`97.04` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`97.15` (Slope: `+0.0000`) | EMA-100=`98.01`
  * Institutional Anchors: EMA-144=`98.56` | EMA-200=`99.06` (Slope: `-0.2133`) | EMA-233=`99.29`
- **Range Boundaries**: 24H High=`102.93` | 24H Low=`91.86` | Weekly High=`103.63` | Weekly Low=`91.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `98.09` (Distance: `-1.15%`)
  * Point of Control (POC) = `96.89` (Distance: `+0.07%`)
  * Value Area Low (VAL) = `94.96` (Distance: `+2.10%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`101.56` | POC=`99.94` | VAL=`98.94`
  * Prior Day Extremes: PDH=`102.93` | PDL=`94.56` | PDC=`95.94`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`102.02` | Weekly POC=`100.92` | Weekly VAL=`99.51`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`97.84` | Low=`91.86`
  * London Session (08:00-16:00 UTC): High=`98.28` | Low=`96.52`
  * New York Session (13:00-21:00 UTC): High=`97.56` | Low=`96.40`
  * Initial Balance (First Hour): IB High=`98.28` | IB Low=`96.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `96.59` - `97.37`
  * Optimal Trade Entry (OTE 0.705): `97.17`
  * Structural Invalidation Anchor (0.786): `97.76`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `97.21` | `97.36` | `97.13` | `97.24` | `40,755` | 3,962,164.69 USD | -397,035.45 USD | `-10.02%` | -217,361,761.78 USD | `+0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `97.24` | `97.30` | `97.09` | `97.22` | `32,353` | 3,144,195.21 USD | -223,308.77 USD | `-7.10%` | -217,585,070.55 USD | `+0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `97.22` | `97.24` | `97.07` | `97.07` | `3,731` | 362,448.63 USD | -174,380.40 USD | `-48.11%` | -217,759,450.95 USD | `+0.31` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `97.28` | `97.31` | `96.84` | `97.20` | `198,976` | 19,320,776.86 USD | -1,231,743.19 USD | `-6.38%` | -217,914,166.98 USD | `-0.28` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `97.20` | `97.55` | `97.17` | `97.20` | `149,345` | 14,539,694.05 USD | 949,440.65 USD | `+6.53%` | -216,964,726.33 USD | `+0.72` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `97.21` | `97.36` | `97.07` | `97.07` | `76,865` | 7,471,374.11 USD | -796,954.30 USD | `-10.67%` | -217,761,680.63 USD | `-0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `97.94` | `98.52` | `97.74` | `98.25` | `547,707` | 53,720,475.41 USD | 736,909.02 USD | `+1.37%` | -207,883,012.55 USD | `+0.59` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `98.26` | `98.28` | `96.93` | `97.28` | `823,584` | 80,361,988.15 USD | -10,205,381.09 USD | `-12.70%` | -218,088,393.64 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `97.28` | `97.55` | `96.84` | `97.07` | `424,844` | 41,298,652.69 USD | -1,050,270.01 USD | `-2.54%` | -219,138,663.66 USD | `+0.47` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -192,935,382.59 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `97.28` | `3,030,040` | 295,921,356.18 USD | -16,839,868.63 USD | `-5.69%` | -209,775,251.22 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.28` | `97.55` | `96.84` | `97.07` | `425,160` | 41,329,279.45 USD | -1,077,027.16 USD | `-2.61%` | -210,852,278.38 USD | `+0.87` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -33,800,710.11 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.62` | `13,887,188` | 1,349,343,315.53 USD | -115,873,425.65 USD | `-8.59%` | -149,674,135.76 USD | `-1.37` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -192,935,382.59 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `97.28` | `3,030,040` | 295,921,356.18 USD | -16,839,868.63 USD | `-5.69%` | -209,775,251.22 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.28` | `97.55` | `96.84` | `97.07` | `425,160` | 41,329,279.45 USD | -1,077,027.16 USD | `-2.61%` | -210,852,278.38 USD | `+0.87` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`96.98`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `97.08` | `145.7800` | 14,152.91 USD | 137,306.95 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `97.08` | `154.6800` | 15,016.80 USD | 152,323.75 USD | `3 orders` | `-0.03%` | `-` |
| `BID` | `97.08` | `41.2000` | 3,999.78 USD | 156,323.53 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.08` | `502.7700` | 48,809.41 USD | 205,132.94 USD | `5 orders` | `-0.03%` | `-` |
| `BID` | `97.09` | `159.4100` | 15,477.91 USD | 73,814.65 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.09` | `57.8300` | 5,614.89 USD | 79,429.53 USD | `3 orders` | `-0.02%` | `-` |
| `BID` | `97.09` | `0.9600` | 93.21 USD | 79,522.74 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.09` | `92.2000` | 8,951.70 USD | 88,474.44 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `97.09` | `1.0000` | 97.09 USD | 88,571.53 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.09` | `232.0900` | 22,533.15 USD | 111,104.68 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `97.09` | `20.9100` | 2,030.09 USD | 113,134.77 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.09` | `103.2000` | 10,019.28 USD | 123,154.05 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.10` | `48.7500` | 4,733.82 USD | 28,123.92 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.10` | `1.9700` | 191.29 USD | 28,315.21 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `97.10` | `103.2200` | 10,022.46 USD | 38,337.66 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.10` | `205.9700` | 19,999.07 USD | 58,336.73 USD | `1 orders` | `-0.02%` | `-` |
| `ASK` | `97.11` | `398.2700` | 38,677.99 USD | 38,677.99 USD | `7 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `97.11` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 97.11` | `0.00%` | `-` |
| `BID` | `97.11` | `0.6200` | 60.21 USD | 60.21 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `97.11` | `61.7400` | 5,995.51 USD | 6,055.72 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.11` | `168.5100` | 16,363.33 USD | 22,419.05 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `97.11` | `10.0000` | 971.05 USD | 23,390.10 USD | `1 orders` | `-0.01%` | `-` |
| `ASK` | `97.12` | `124.1800` | 12,060.73 USD | 68,120.11 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `97.12` | `2.0500` | 199.10 USD | 56,059.38 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.12` | `176.4100` | 17,132.76 USD | 55,860.28 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `97.12` | `0.5100` | 49.53 USD | 38,727.52 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `97.13` | `289.0000` | 28,071.44 USD | 137,107.23 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `97.13` | `82.4600` | 8,009.50 USD | 109,035.79 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `97.13` | `92.4600` | 8,980.73 USD | 101,026.29 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `97.13` | `83.4700` | 8,107.44 USD | 92,045.56 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `97.13` | `59.6500` | 5,793.63 USD | 83,938.11 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.13` | `103.2100` | 10,024.37 USD | 78,144.49 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.14` | `792.8600` | 77,021.59 USD | 545,399.78 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `97.14` | `1978.9500` | 192,241.14 USD | 468,378.19 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `97.14` | `92.0900` | 8,945.81 USD | 276,137.05 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `97.14` | `103.3500` | 10,039.52 USD | 267,191.24 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `97.14` | `117.4200` | 11,406.18 USD | 257,151.72 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `97.14` | `82.4400` | 8,008.14 USD | 245,745.54 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `97.14` | `294.3600` | 28,593.54 USD | 237,737.40 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `97.14` | `657.0500` | 63,823.87 USD | 209,143.86 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `97.14` | `84.5500` | 8,212.76 USD | 145,319.99 USD | `2 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `10` | `0x5b5d...c060` | `SHORT` | 67,721,350.73 USD | `696,120.13` | `94.33` | `97.42` | `323.95` | -2,053,084.51 USD | `-3.03%` | `7X Cross` |
| `18` | `0x9c6a...a4ed` | `LONG` | 53,493,277.41 USD | `550,087.69` | `80.86` | `97.42` | `68.18` | 9,014,291.03 USD | `+16.85%` | `20X Cross` |
| `49` | `0xb83d...6e36` | `SHORT` | 25,222,178.47 USD | `259,338.02` | `91.42` | `97.42` | `597.83` | -1,513,364.43 USD | `-6.00%` | `5X Cross` |
| `79` | `0x3dc9...54b0` | `SHORT` | 21,386,812.47 USD | `220,000.19` | `105.90` | `97.42` | `175.44` | 1,912,294.81 USD | `+8.94%` | `20X Cross` |
| `109` | `0x9c89...600e` | `LONG` | 18,395,316.61 USD | `189,472.50` | `115.21` | `97.42` | `35.01` | -3,433,698.65 USD | `-18.67%` | `20X Cross` |
| `117` | `0x4a20...3c26` | `LONG` | 17,493,660.00 USD | `180,000.00` | `106.43` | `97.42` | `69.72` | -1,664,618.71 USD | `-9.52%` | `20X Cross` |
| `160` | `0xecb6...2b00` | `SHORT` | 12,853,123.17 USD | `132,119.60` | `101.25` | `97.42` | `333.55` | 523,917.42 USD | `+4.08%` | `20X Cross` |
| `226` | `0xc63a...a3cd` | `LONG` | 9,717,500.00 USD | `100,000.00` | `112.22` | `97.42` | `0.000000` | -1,504,608.97 USD | `-15.48%` | `20X Cross` |
| `227` | `0xb581...6f4f` | `LONG` | 9,710,700.00 USD | `100,000.00` | `112.81` | `97.42` | `0.000000` | -1,570,009.14 USD | `-16.17%` | `3X Cross` |
| `294` | `0x645b...87b8` | `SHORT` | 8,060,573.39 USD | `82,879.96` | `103.90` | `97.42` | `360.77` | 550,896.83 USD | `+6.83%` | `20X Cross` |
| `300` | `0xdb3a...cf3b` | `LONG` | 7,946,580.06 USD | `81,851.78` | `106.04` | `97.42` | `47.22` | -733,166.80 USD | `-9.23%` | `4X Cross` |
| `318` | `0xe927...98ef` | `LONG` | 7,582,590.60 USD | `78,000.00` | `96.34` | `97.42` | `38.45` | 68,449.12 USD | `+0.90%` | `3X Cross` |
| `325` | `0xca49...53c8` | `SHORT` | 7,186,194.19 USD | `73,943.45` | `110.70` | `97.42` | `302.46` | 999,428.07 USD | `+13.91%` | `20X Cross` |
| `330` | `0x8ae4...3d60` | `LONG` | 7,021,963.98 USD | `72,180.05` | `111.72` | `97.42` | `11.89` | -1,042,196.25 USD | `-14.84%` | `10X Cross` |
| `334` | `0xa0b7...6165` | `SHORT` | 6,907,648.96 USD | `71,044.42` | `107.87` | `97.42` | `190.91` | 755,818.24 USD | `+10.94%` | `2X Cross` |
| `352` | `0xf517...c032` | `SHORT` | 6,587,734.22 USD | `67,778.53` | `84.64` | `97.42` | `220.45` | -850,703.06 USD | `-12.91%` | `20X Cross` |
| `411` | `0x7fda...17d1` | `SHORT` | 5,433,432.03 USD | `55,851.24` | `100.53` | `97.42` | `790.62` | 181,502.55 USD | `+3.34%` | `20X Cross` |
| `468` | `0x7e23...5a5a` | `LONG` | 4,720,280.97 USD | `48,564.56` | `105.17` | `97.42` | `57.00` | -387,288.19 USD | `-8.20%` | `5X Isolated` |
| `540` | `0x7a5a...0394` | `SHORT` | 4,183,404.01 USD | `43,041.35` | `99.29` | `97.42` | `124.03` | 90,002.54 USD | `+2.15%` | `10X Cross` |
| `572` | `0xf899...88db` | `SHORT` | 3,959,954.07 USD | `40,716.81` | `88.40` | `97.42` | `109.13` | -360,681.20 USD | `-9.11%` | `20X Cross` |
| `592` | `0x2e2b...2fab` | `LONG` | 3,887,840.00 USD | `40,000.00` | `119.55` | `97.42` | `59.79` | -894,195.64 USD | `-23.00%` | `10X Cross` |
| `625` | `0x9c16...4a6f` | `SHORT` | 3,672,838.93 USD | `37,796.13` | `90.79` | `97.42` | `118.49` | -241,488.21 USD | `-6.57%` | `20X Cross` |
| `648` | `0x9946...0852` | `SHORT` | 3,508,698.68 USD | `36,099.58` | `110.82` | `97.42` | `141.24` | 491,887.71 USD | `+14.02%` | `20X Cross` |
| `650` | `0x27b8...12fc` | `LONG` | 3,504,158.94 USD | `36,085.73` | `110.86` | `97.42` | `24.43` | -496,186.31 USD | `-14.16%` | `10X Cross` |
| `675` | `0xa61c...66b9` | `LONG` | 3,347,275.28 USD | `34,438.76` | `102.78` | `97.42` | `0.000000` | -192,186.03 USD | `-5.74%` | `5X Cross` |
| `692` | `0x3440...32c5` | `SHORT` | 3,276,680.29 USD | `33,744.03` | `95.02` | `97.42` | `168.30` | -70,280.34 USD | `-2.14%` | `20X Cross` |
| `741` | `0x96a7...79df` | `LONG` | 3,110,806.40 USD | `32,000.00` | `74.39` | `97.42` | `0.000000` | 730,400.55 USD | `+23.48%` | `20X Cross` |
| `783` | `0xbe19...8bd1` | `SHORT` | 2,959,752.01 USD | `30,451.69` | `97.62` | `97.42` | `763.53` | 12,794.62 USD | `+0.43%` | `3X Cross` |
| `786` | `0x482b...cae4` | `SHORT` | 2,945,785.59 USD | `30,310.49` | `88.03` | `97.42` | `151.26` | -277,537.30 USD | `-9.42%` | `20X Cross` |
| `798` | `0x610b...b613` | `LONG` | 2,880,814.76 USD | `29,634.14` | `101.23` | `97.42` | `70.39` | -119,184.59 USD | `-4.14%` | `3X Isolated` |
| `806` | `0x023a...2355` | `SHORT` | 2,864,156.39 USD | `29,462.78` | `101.18` | `97.42` | `273.04` | 116,765.44 USD | `+4.08%` | `20X Cross` |
| `814` | `0x45d2...4029` | `SHORT` | 2,838,021.72 USD | `29,220.00` | `93.28` | `97.42` | `1580.15` | -112,245.74 USD | `-3.96%` | `20X Cross` |
| `863` | `0x458d...ab3b` | `LONG` | 2,662,172.71 USD | `27,385.03` | `117.17` | `97.42` | `81.08` | -546,489.81 USD | `-20.53%` | `3X Isolated` |
| `924` | `0x051c...693c` | `LONG` | 2,443,898.11 USD | `25,139.70` | `89.76` | `97.42` | `44.96` | 187,336.79 USD | `+7.67%` | `20X Cross` |
| `941` | `0xfc27...9d9d` | `SHORT` | 2,386,190.71 USD | `24,528.09` | `100.40` | `97.42` | `855.24` | 76,322.43 USD | `+3.20%` | `20X Cross` |
| `965` | `0x638f...f5f0` | `LONG` | 2,331,480.00 USD | `24,000.00` | `136.71` | `97.42` | `51.19` | -949,488.54 USD | `-40.72%` | `20X Cross` |
| `1010` | `0x7277...0b98` | `SHORT` | 2,213,202.07 USD | `22,770.74` | `99.32` | `97.42` | `159.67` | 48,401.68 USD | `+2.19%` | `20X Cross` |
| `1022` | `0x7178...0854` | `LONG` | 2,189,300.62 USD | `22,545.24` | `110.94` | `97.42` | `40.17` | -311,843.85 USD | `-14.24%` | `10X Cross` |
| `1049` | `0x69cc...14fd` | `SHORT` | 2,109,284.10 USD | `21,701.57` | `99.01` | `97.42` | `472.17` | 39,368.65 USD | `+1.87%` | `20X Cross` |
| `1053` | `0x739c...cfb2` | `LONG` | 2,090,073.05 USD | `21,500.00` | `91.95` | `97.42` | `75.52` | 113,140.90 USD | `+5.41%` | `20X Cross` |
| `1116` | `0x7737...bf66` | `SHORT` | 1,982,247.91 USD | `20,384.06` | `102.94` | `97.42` | `983.11` | 116,093.98 USD | `+5.86%` | `10X Cross` |
| `1144` | `0xbfc7...80b4` | `SHORT` | 1,945,120.00 USD | `20,000.00` | `85.98` | `97.42` | `175.45` | -225,585.50 USD | `-11.60%` | `20X Cross` |
| `1145` | `0x3fc5...c0c1` | `SHORT` | 1,944,254.00 USD | `20,000.00` | `98.28` | `97.42` | `186.47` | 21,305.84 USD | `+1.10%` | `20X Cross` |
| `1146` | `0xea00...a918` | `LONG` | 1,943,942.90 USD | `20,022.69` | `66.09` | `97.42` | `0.000000` | 620,634.31 USD | `+31.93%` | `20X Cross` |
| `1147` | `0x251f...6e5d` | `LONG` | 1,943,900.00 USD | `20,000.00` | `101.15` | `97.42` | `70.82` | -79,197.77 USD | `-4.07%` | `20X Cross` |
| `1181` | `0x7160...d47c` | `LONG` | 1,888,897.35 USD | `19,434.10` | `105.03` | `97.42` | `76.25` | -152,323.94 USD | `-8.06%` | `20X Cross` |
| `1198` | `0x936c...bb0f` | `SHORT` | 1,847,317.12 USD | `18,988.91` | `105.57` | `97.42` | `530.45` | 157,370.57 USD | `+8.52%` | `20X Cross` |
| `1200` | `0xe097...d0fe` | `LONG` | 1,845,912.01 USD | `18,995.75` | `109.71` | `97.42` | `0.000000` | -238,084.88 USD | `-12.90%` | `20X Cross` |
| `1280` | `0xdf95...7d72` | `SHORT` | 1,731,407.72 USD | `17,802.58` | `104.53` | `97.42` | `2295.04` | 129,549.13 USD | `+7.48%` | `20X Cross` |
| `1293` | `0xe98b...8cd5` | `SHORT` | 1,713,473.59 USD | `17,622.89` | `187.95` | `97.42` | `262.47` | 1,598,747.13 USD | `+93.30%` | `20X Cross` |
| `1326` | `0xee2b...d67e` | `LONG` | 1,648,737.25 USD | `16,963.19` | `119.86` | `97.42` | `34.04` | -384,534.39 USD | `-23.32%` | `4X Cross` |
| `1335` | `0x123d...3bff` | `LONG` | 1,636,604.97 USD | `16,835.30` | `89.54` | `97.42` | `0.000000` | 129,163.71 USD | `+7.89%` | `10X Cross` |
| `1436` | `0x73d7...8be1` | `LONG` | 1,522,786.91 USD | `15,668.95` | `106.60` | `97.42` | `49.71` | -147,554.06 USD | `-9.69%` | `20X Cross` |
| `1453` | `0xc74a...ab93` | `LONG` | 1,510,878.06 USD | `15,536.82` | `64.06` | `97.42` | `54.88` | 515,649.23 USD | `+34.13%` | `5X Isolated` |
| `1485` | `0x5f10...d49d` | `LONG` | 1,457,925.00 USD | `15,000.00` | `96.35` | `97.42` | `72.02` | 12,623.84 USD | `+0.87%` | `20X Cross` |
| `1486` | `0xb322...d51f` | `LONG` | 1,457,907.50 USD | `14,999.82` | `102.98` | `97.42` | `43.71` | -86,819.80 USD | `-5.96%` | `20X Cross` |
| `1536` | `0xffb2...5ed6` | `LONG` | 1,408,154.70 USD | `14,504.05` | `117.89` | `97.42` | `84.52` | -301,750.01 USD | `-21.43%` | `20X Cross` |
| `1560` | `0x0d6a...ca57` | `LONG` | 1,380,829.55 USD | `14,206.65` | `110.41` | `97.42` | `91.60` | -187,760.80 USD | `-13.60%` | `5X Isolated` |
| `1778` | `0x2814...9b08` | `LONG` | 1,172,108.73 USD | `12,061.71` | `96.37` | `97.42` | `93.93` | 9,769.99 USD | `+0.83%` | `20X Isolated` |
| `1850` | `0x7808...6e70` | `SHORT` | 1,115,361.67 USD | `11,488.27` | `97.15` | `97.42` | `152.10` | 700.55 USD | `+0.06%` | `10X Cross` |
| `1867` | `0x2482...0e55` | `LONG` | 1,104,533.40 USD | `11,363.98` | `122.03` | `97.42` | `88.83` | -282,168.52 USD | `-25.55%` | `20X Isolated` |
| `1898` | `0x45db...86eb` | `LONG` | 1,078,542.60 USD | `11,100.00` | `110.69` | `97.42` | `69.15` | -150,139.30 USD | `-13.92%` | `5X Cross` |
| `1926` | `0x1d04...7c43` | `LONG` | 1,051,227.42 USD | `10,811.76` | `111.55` | `97.42` | `17.23` | -154,834.07 USD | `-14.73%` | `6X Cross` |
| `1944` | `0x34e6...8d74` | `LONG` | 1,037,075.71 USD | `10,671.15` | `101.19` | `97.42` | `15.56` | -42,698.93 USD | `-4.12%` | `20X Cross` |
| `2004` | `0x2577...4897` | `LONG` | 1,004,367.57 USD | `10,327.05` | `96.54` | `97.42` | `0.000000` | 7,371.13 USD | `+0.73%` | `15X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `100.72` | 3,101.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.10K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.72` | 1,874.40 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.87K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.72` | 179.28 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.18K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.72` | 1,380.87 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.38K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.72` | 12.09 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.72` | 1,380.87 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.38K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.72` | 2,143.32 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.14K USD at 100.7200 USD [API] | `2026-10-18 19:41:08` |
| `ANNOUNCEMENT` | `INFO` | `100.13` | 59,164.81 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 59.16K USD at 100.1300 USD [API] | `2026-10-29 09:30:31` |
| `ANNOUNCEMENT` | `INFO` | `100.31` | 34,002.08 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 34.00K USD at 100.3100 USD [API] | `2026-10-29 09:58:06` |
| `ANNOUNCEMENT` | `INFO` | `100.55` | 25,634.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 25.63K USD at 100.5500 USD [API] | `2026-10-29 10:48:31` |
| `ANNOUNCEMENT` | `INFO` | `100.53` | 2.01 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.00K USD at 100.5300 USD [API] | `2026-10-29 11:50:52` |
| `ANNOUNCEMENT` | `INFO` | `100.20` | 25,159.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 25.16K USD at 100.2000 USD [API] | `2026-10-29 12:11:24` |
| `ANNOUNCEMENT` | `INFO` | `100.30` | 44,051.76 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 44.05K USD at 100.3000 USD [API] | `2026-10-29 12:19:01` |
| `ANNOUNCEMENT` | `INFO` | `100.43` | 20,001.64 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 20.00K USD at 100.4300 USD [API] | `2026-10-29 12:29:43` |
| `ANNOUNCEMENT` | `INFO` | `100.68` | 22,375.12 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 22.38K USD at 100.6800 USD [API] | `2026-10-29 13:05:41` |
| `ANNOUNCEMENT` | `INFO` | `100.75` | 37,574.71 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 37.57K USD at 100.7500 USD [API] | `2026-10-29 13:18:58` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 36,538.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 36.54K USD at 100.4800 USD [API] | `2026-10-29 13:53:35` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`101.22` (Vol: 4,800,000.00 USD, Dist: `+4.28%`) | Long MP=`92.18` (Vol: 5,300,000.00 USD, Dist: `--5.04%`)
  * 48H Horizon: Short MP=`101.12` (Vol: 5,400,000.00 USD, Dist: `+4.18%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--5.05%`)
  * 3D Horizon: Short MP=`101.12` (Vol: 5,400,000.00 USD, Dist: `+4.18%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--5.05%`)
  * 7D Horizon: Short MP=`104.03` (Vol: 7,200,000.00 USD, Dist: `+7.17%`) | Long MP=`92.11` (Vol: 5,300,000.00 USD, Dist: `--5.11%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `19.45` | 3,100.00 USD | 122,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.55` | 449.65 USD | 122,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.65` | 514.44 USD | 122,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.05` | 897.84 USD | 122,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.15` | 730.44 USD | 122,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 12,190.00 USD | 122,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.85` | 689.93 USD | 122,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.95` | 1,030.00 USD | 122,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 1,410.00 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 407.55 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.75` | 4,630.00 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.95` | 1,100.00 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.05` | 4,740.00 USD | 122,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.35` | 2,040.00 USD | 122,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.65` | 112.12 USD | 122,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 1,150.00 USD | 122,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.15` | 11,820.00 USD | 122,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.25` | 838,990.00 USD | 122,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.35` | 46,700.00 USD | 121,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 1,380.00 USD | 121,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.65` | 9,830.00 USD | 121,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 1,570.00 USD | 121,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 9,590.00 USD | 121,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.25` | 248.81 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 882.72 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.75` | 976.88 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.85` | 5,360.00 USD | 121,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.95` | 25,960.00 USD | 121,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 1,250.00 USD | 121,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 3,270.00 USD | 121,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 106.64 USD | 121,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.65` | 147,500.00 USD | 121,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.75` | 309.00 USD | 121,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 3,320.00 USD | 121,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.05` | 5,730.00 USD | 121,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 136.24 USD | 121,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.35` | 366.79 USD | 121,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.45` | 1,710.00 USD | 121,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 265.17 USD | 121,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 10,110.00 USD | 121,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 332.30 USD | 121,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.75` | 1,190.00 USD | 121,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 14,980.00 USD | 121,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 154.28 USD | 121,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.05` | 2,740.00 USD | 121,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.15` | 271.37 USD | 121,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.25` | 755.12 USD | 121,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.35` | 6,200.00 USD | 121,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 113.80 USD | 121,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.05` | 11,030.00 USD | 121,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 15,270.00 USD | 121,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.25` | 88,480.00 USD | 121,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.35` | 9,900.00 USD | 121,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.45` | 151.96 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 33,370.00 USD | 121,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.95` | 18,960.00 USD | 121,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 5,410.00 USD | 121,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 50,050.00 USD | 121,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.25` | 47,800.00 USD | 121,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.35` | 4,230.00 USD | 120,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 889.01 USD | 120,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 5,250.00 USD | 120,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.85` | 157.64 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.05` | 621.00 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 178.49 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.35` | 6,120.00 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 278.33 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 162.17 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.75` | 11,130.00 USD | 120,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 796.68 USD | 120,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 173.50 USD | 120,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 861.87 USD | 120,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 1,150.00 USD | 120,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 562,480.00 USD | 120,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.95` | 1,160.00 USD | 120,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.05` | 5,420.00 USD | 120,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.25` | 39,900.00 USD | 120,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 1,830.00 USD | 120,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.75` | 72,700.00 USD | 120,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 3,650.00 USD | 120,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 19,990.00 USD | 120,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.25` | 799.05 USD | 120,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.35` | 982.41 USD | 120,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.55` | 17,270.00 USD | 120,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 486.14 USD | 120,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.75` | 143.86 USD | 120,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.85` | 3,660.00 USD | 120,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 6,620,000.00 USD | 120,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 441.84 USD | 113,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.25` | 1,360.00 USD | 113,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.65` | 3,040.00 USD | 113,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 4,840.00 USD | 113,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.85` | 9,050.00 USD | 113,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 557.94 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.05` | 5,070.00 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 531.41 USD | 113,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.25` | 2,630.00 USD | 113,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 5,630.00 USD | 113,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 42,810.00 USD | 113,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.55` | 50,420.00 USD | 113,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 748.97 USD | 113,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 1,470.00 USD | 113,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 1,660.00 USD | 113,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 146.37 USD | 113,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 373.62 USD | 113,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 38,140.00 USD | 113,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 144,730.00 USD | 113,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 4,610.00 USD | 113,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 636.09 USD | 113,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 819.83 USD | 113,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 5,000.00 USD | 113,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 1,490.00 USD | 113,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 480.42 USD | 113,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 287.63 USD | 113,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 3,000,000.00 USD | 113,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 17,850.00 USD | 110,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 6,130.00 USD | 110,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 194,490.00 USD | 110,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 4,270.00 USD | 110,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 607.62 USD | 110,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 933,530.00 USD | 110,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 194.18 USD | 109,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 4,930.00 USD | 109,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 258.40 USD | 109,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 11,970.00 USD | 109,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 159.00 USD | 109,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 1,270.00 USD | 109,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 13,530.00 USD | 109,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 2,510.00 USD | 109,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 632.73 USD | 109,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.35` | 51,650.00 USD | 109,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,970.00 USD | 109,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 3,160.00 USD | 109,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 12,650.00 USD | 109,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 581.49 USD | 109,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 5,220.00 USD | 109,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 1,070.00 USD | 109,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 368.36 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 148.45 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 130.88 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 770.11 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 588.26 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 1,020.00 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 389,980.00 USD | 109,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 20,830.00 USD | 108,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 2,790.00 USD | 108,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 3,050.00 USD | 108,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 6,460.00 USD | 108,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.45` | 106.12 USD | 108,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 8,230.00 USD | 108,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 44,750.00 USD | 108,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 1,620.00 USD | 108,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 1,400.00 USD | 108,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 2,040.00 USD | 108,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 1,080.00 USD | 108,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 4,710.00 USD | 108,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 440.15 USD | 108,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.55` | 2,180.00 USD | 108,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 6,530.00 USD | 108,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 1,170,000.00 USD | 108,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 219,360.00 USD | 107,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 10,340.00 USD | 107,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 12,870.00 USD | 107,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 662,360.00 USD | 107,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 6,550.00 USD | 106,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 2,380.00 USD | 106,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 10,180.00 USD | 106,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 20,540.00 USD | 106,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 4,880.00 USD | 106,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 1,790.00 USD | 106,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 477.20 USD | 106,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 3,690,000.00 USD | 106,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 179.70 USD | 102,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 67,560.00 USD | 102,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 9,480.00 USD | 102,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 7,940.00 USD | 102,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 866.89 USD | 102,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 9,780.00 USD | 102,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 458.50 USD | 102,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 26,070.00 USD | 102,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 9,760.00 USD | 102,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.15` | 714.40 USD | 102,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 824.95 USD | 102,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 685.68 USD | 102,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 542.07 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 374.00 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 543.93 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 2,090.00 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,160.00 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 13,380.00 USD | 102,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 502.50 USD | 102,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 106.04 USD | 102,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 98,780.00 USD | 102,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 56,650.00 USD | 102,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.85` | 473.72 USD | 102,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 3,360.00 USD | 102,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 13,580.00 USD | 102,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 16,260.00 USD | 102,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 2,430.00 USD | 102,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 9,290.00 USD | 102,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 764,270.00 USD | 102,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 97,400.00 USD | 101,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 10,720.00 USD | 101,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 2,330.00 USD | 101,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.85` | 17,060.00 USD | 101,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,490.00 USD | 101,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,120.00 USD | 101,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 21,190.00 USD | 101,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 585.29 USD | 101,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 17,090.00 USD | 101,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 627.80 USD | 101,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 8,890.00 USD | 101,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 2,650.00 USD | 101,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 41,540.00 USD | 101,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 29,590.00 USD | 101,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 9,750.00 USD | 101,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 5,850.00 USD | 101,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 1,210,000.00 USD | 101,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 8,240.00 USD | 100,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,800.00 USD | 100,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 12,940.00 USD | 100,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 1,270.00 USD | 100,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 13,300.00 USD | 100,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.85` | 20,760.00 USD | 100,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 5,110.00 USD | 100,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 3,470.00 USD | 100,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 2,620.00 USD | 100,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.25` | 10,940.00 USD | 100,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 4,340.00 USD | 100,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.45` | 3,920.00 USD | 100,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.55` | 135,270.00 USD | 100,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.65` | 4,290.00 USD | 99,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.75` | 24,770.00 USD | 99,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.85` | 46,110.00 USD | 99,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.95` | 469,860.00 USD | 99,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.05` | 31,030.00 USD | 99,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.15` | 112,570.00 USD | 99,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.25` | 12,600.00 USD | 99,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.35` | 2,160.00 USD | 99,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.45` | 43,640.00 USD | 99,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.55` | 11,110.00 USD | 99,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.65` | 9,300.00 USD | 99,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.75` | 3,180.00 USD | 99,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.85` | 9,370.00 USD | 99,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.95` | 6,120.00 USD | 99,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.05` | 5,120.00 USD | 99,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.15` | 3,340.00 USD | 99,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.25` | 24,120.00 USD | 99,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.35` | 2,130.00 USD | 99,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.45` | 52,360.00 USD | 99,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.55` | 44,480.00 USD | 99,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.65` | 230.70 USD | 98,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.75` | 3,600.00 USD | 98,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.85` | 19,810.00 USD | 98,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.95` | 58,760.00 USD | 98,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.05` | 350.78 USD | 98,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.15` | 14,640.00 USD | 98,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.25` | 6,660.00 USD | 98,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.35` | 11,720.00 USD | 98,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.45` | 1,410.00 USD | 98,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.55` | 61,670.00 USD | 98,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.65` | 10,920.00 USD | 98,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.75` | 15,140.00 USD | 98,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.85` | 861,080.00 USD | 98,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.95` | 142,480.00 USD | 97,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.05` | 552.70 USD | 97,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.15` | 665.66 USD | 97,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.25` | 2,010.00 USD | 97,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.35` | 9,920.00 USD | 97,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.45` | 5,620.00 USD | 97,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.55` | 145,530.00 USD | 97,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.65` | 11,490.00 USD | 97,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.75` | 91,720.00 USD | 97,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.85` | 18,770.00 USD | 97,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.95` | 7,050.00 USD | 97,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.05` | 5,640.00 USD | 97,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.15` | 38,930.00 USD | 97,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.25` | 13,300.00 USD | 97,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.35` | 12,890.00 USD | 97,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.45` | 13,320.00 USD | 97,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.55` | 4,730.00 USD | 97,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.65` | 3,190.00 USD | 97,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.75` | 9,410.00 USD | 97,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.85` | 28,550.00 USD | 97,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.95` | 14,320.00 USD | 97,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.05` | 2,770,000.00 USD | 97,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.15` | 5,380.00 USD | 94,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.25` | 2,470.00 USD | 94,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.35` | 7,120.00 USD | 94,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.45` | 19,200.00 USD | 94,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.55` | 8,510.00 USD | 94,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.65` | 13,030.00 USD | 94,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.75` | 8,290.00 USD | 94,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.85` | 22,150.00 USD | 94,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.95` | 10,870.00 USD | 94,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.05` | 39,250.00 USD | 94,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.15` | 125,030.00 USD | 94,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.25` | 9,870.00 USD | 94,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.35` | 30,840.00 USD | 94,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.45` | 697.31 USD | 94,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.55` | 4,680.00 USD | 94,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.65` | 4,690.00 USD | 94,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.75` | 14,500.00 USD | 94,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.85` | 13,970.00 USD | 94,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.95` | 31,930.00 USD | 94,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.05` | 65,660.00 USD | 94,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.15` | 2,370,000.00 USD | 94,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.25` | 1,990.00 USD | 91,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.35` | 28,500.00 USD | 91,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.45` | 4,830.00 USD | 91,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.55` | 26,470.00 USD | 91,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.65` | 3,640.00 USD | 91,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.75` | 13,290.00 USD | 91,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.85` | 28,800.00 USD | 91,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.95` | 38,940.00 USD | 91,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.05` | 55,060.00 USD | 91,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.15` | 35,380.00 USD | 91,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.25` | 20,380.00 USD | 91,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.35` | 4,540.00 USD | 91,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.55` | 10,140.00 USD | 91,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.65` | 711.42 USD | 91,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.75` | 5,300.00 USD | 91,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.85` | 33,430.00 USD | 91,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.95` | 57,890.00 USD | 91,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.05` | 4,520.00 USD | 91,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.15` | 5,900.00 USD | 91,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.25` | 4,630.00 USD | 91,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.35` | 11,660.00 USD | 91,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.45` | 20,920.00 USD | 91,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.55` | 651.20 USD | 91,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.65` | 19,270.00 USD | 91,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.75` | 109,820.00 USD | 91,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.85` | 24,050.00 USD | 91,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.95` | 4,680.00 USD | 91,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.05` | 53,350.00 USD | 91,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.15` | 25,350.00 USD | 91,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.25` | 47,880.00 USD | 91,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.35` | 20,220.00 USD | 91,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.45` | 67,320.00 USD | 91,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.55` | 135,200.00 USD | 90,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.65` | 2,630.00 USD | 90,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.75` | 3,140.00 USD | 90,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.85` | 31,310.00 USD | 90,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.95` | 9,610.00 USD | 90,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.05` | 16,070.00 USD | 90,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.15` | 82,790.00 USD | 90,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.25` | 32,790.00 USD | 90,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.35` | 1,200.00 USD | 90,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.45` | 291.24 USD | 90,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.55` | 49,290.00 USD | 90,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.65` | 416.27 USD | 90,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.75` | 32,540.00 USD | 90,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.85` | 37,610.00 USD | 90,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.95` | 19,530.00 USD | 90,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.05` | 796.78 USD | 90,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.15` | 35,280.00 USD | 90,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.25` | 5,090.00 USD | 90,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.35` | 875.16 USD | 90,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.45` | 4,310.00 USD | 90,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.55` | 579.66 USD | 90,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.65` | 2,220.00 USD | 90,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.75` | 16,300.00 USD | 90,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.85` | 396.23 USD | 90,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.95` | 209.79 USD | 90,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.05` | 265,650.00 USD | 90,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.15` | 108,780.00 USD | 90,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.25` | 13,060.00 USD | 90,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.35` | 39,610.00 USD | 90,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.45` | 3,450.00 USD | 90,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.55` | 10,470.00 USD | 89,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.65` | 58,270.00 USD | 89,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.75` | 5,050.00 USD | 89,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.85` | 1,300.00 USD | 89,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.95` | 5,780.00 USD | 89,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.05` | 6,490.00 USD | 89,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.15` | 20,170.00 USD | 89,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.25` | 14,930.00 USD | 89,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.35` | 1,600.00 USD | 89,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.45` | 75,010.00 USD | 89,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.55` | 52,610.00 USD | 89,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.65` | 40,710.00 USD | 89,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.75` | 43,110.00 USD | 89,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.85` | 20,000.00 USD | 89,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.95` | 937.30 USD | 89,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.05` | 46,770.00 USD | 89,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.15` | 3,620.00 USD | 89,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.25` | 248.83 USD | 89,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.35` | 1,880.00 USD | 89,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.45` | 22,250.00 USD | 89,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.55` | 53,380.00 USD | 89,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.65` | 129,430.00 USD | 89,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.75` | 30,820.00 USD | 89,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.85` | 28,740.00 USD | 89,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.05` | 11,140.00 USD | 89,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.15` | 37,490,000.00 USD | 89,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.25` | 17,190.00 USD | 51,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.35` | 2,860.00 USD | 51,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.45` | 18,610.00 USD | 51,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.55` | 1,380,000.00 USD | 51,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.65` | 7,740.00 USD | 50,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.75` | 151,610.00 USD | 50,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.85` | 417,630.00 USD | 50,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.95` | 46,330.00 USD | 49,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.05` | 786,930.00 USD | 49,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.15` | 29,000.00 USD | 48,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.25` | 20,140.00 USD | 48,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.35` | 12,490,000.00 USD | 48,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.45` | 264,310.00 USD | 36,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.55` | 10,170.00 USD | 36,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.65` | 5,280.00 USD | 36,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.75` | 212,170.00 USD | 36,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.85` | 8,590.00 USD | 35,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.95` | 8,800.00 USD | 35,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.05` | 496,560.00 USD | 35,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.15` | 4,120.00 USD | 35,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.25` | 72,890.00 USD | 35,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.35` | 2,140,000.00 USD | 35,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.45` | 113,800.00 USD | 33,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.55` | 458.58 USD | 33,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.65` | 49,010.00 USD | 33,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.75` | 10,240.00 USD | 33,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.85` | 15,430.00 USD | 33,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.95` | 7,010.00 USD | 33,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.05` | 31,630.00 USD | 33,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.15` | 69,160.00 USD | 33,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.25` | 1,080,000.00 USD | 32,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.35` | 15,910.00 USD | 31,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.45` | 31,640.00 USD | 31,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.55` | 41,780.00 USD | 31,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.65` | 894.91 USD | 31,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.75` | 30,200.00 USD | 31,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.85` | 2,130.00 USD | 31,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.95` | 12,860.00 USD | 31,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.05` | 42,610.00 USD | 31,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.15` | 130,700.00 USD | 31,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.25` | 259,270.00 USD | 31,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.35` | 29,390.00 USD | 31,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.45` | 2,240.00 USD | 31,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.55` | 16,450.00 USD | 31,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.65` | 33,720.00 USD | 31,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.75` | 3,100.00 USD | 31,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.85` | 186,830.00 USD | 31,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.95` | 18,610.00 USD | 31,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.05` | 7,310.00 USD | 30,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.15` | 17,140.00 USD | 30,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.25` | 28,470.00 USD | 30,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.35` | 8,280.00 USD | 30,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.45` | 5,350.00 USD | 30,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.55` | 17,060.00 USD | 30,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.65` | 38,360.00 USD | 30,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.75` | 77,660.00 USD | 30,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.85` | 11,710.00 USD | 30,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.95` | 40,040.00 USD | 30,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.05` | 38,460.00 USD | 30,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.15` | 21,430.00 USD | 30,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.25` | 41,310.00 USD | 30,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.35` | 24,920.00 USD | 30,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.45` | 22,920.00 USD | 30,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.55` | 11,550.00 USD | 30,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.65` | 1,030.00 USD | 30,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.75` | 46,150.00 USD | 30,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.85` | 127,450.00 USD | 30,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.95` | 19,860.00 USD | 30,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.05` | 48,410.00 USD | 30,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.15` | 2,430.00 USD | 30,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.25` | 1,910,000.00 USD | 30,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.35` | 18,360.00 USD | 28,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.45` | 33,560.00 USD | 28,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.55` | 29,130.00 USD | 28,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.65` | 130,250.00 USD | 28,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.75` | 1,550,000.00 USD | 28,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.85` | 4,110.00 USD | 26,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.95` | 27,920.00 USD | 26,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.05` | 8,540.00 USD | 26,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.15` | 17,050.00 USD | 26,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.25` | 9,710.00 USD | 26,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.35` | 35,800.00 USD | 26,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.45` | 1,990.00 USD | 26,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.55` | 68,230.00 USD | 26,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.65` | 57,460.00 USD | 26,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.75` | 5,060.00 USD | 26,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.85` | 134,060.00 USD | 26,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.95` | 29,250.00 USD | 26,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.05` | 80,420.00 USD | 26,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.15` | 257,230.00 USD | 26,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.25` | 32,190.00 USD | 25,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.35` | 8,780.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.45` | 52,110.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.55` | 12,900.00 USD | 25,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.75` | 9,870.00 USD | 25,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.85` | 59,570.00 USD | 25,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.95` | 14,550.00 USD | 25,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.05` | 21,880.00 USD | 25,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.15` | 63,910.00 USD | 25,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.25` | 39,070.00 USD | 25,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.35` | 55,060.00 USD | 25,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.45` | 26,080.00 USD | 25,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.55` | 5,910.00 USD | 25,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.65` | 32,860.00 USD | 25,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.75` | 60,550.00 USD | 25,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.85` | 62,050.00 USD | 25,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.95` | 1,370.00 USD | 25,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.05` | 6,870.00 USD | 25,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.15` | 128,420.00 USD | 25,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.25` | 59,390.00 USD | 25,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.35` | 25,940.00 USD | 25,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.45` | 11,960.00 USD | 25,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.55` | 1,900.00 USD | 25,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.65` | 19,720.00 USD | 25,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.75` | 85,820.00 USD | 25,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.85` | 171,770.00 USD | 25,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.95` | 29,580.00 USD | 24,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.05` | 8,660.00 USD | 24,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.15` | 59,220.00 USD | 24,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.25` | 76,330.00 USD | 24,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.35` | 113,360.00 USD | 24,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.45` | 12,930.00 USD | 24,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.55` | 8,000.00 USD | 24,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.65` | 94,280.00 USD | 24,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.75` | 26,360.00 USD | 24,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.85` | 440,510.00 USD | 24,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.95` | 10,620.00 USD | 24,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.05` | 2,230,000.00 USD | 23,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.15` | 136,780.00 USD | 21,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.25` | 31,500.00 USD | 21,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.35` | 56,470.00 USD | 21,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.45` | 59,690.00 USD | 21,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.55` | 68,180.00 USD | 21,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.65` | 36,930.00 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.75` | 18,650.00 USD | 21,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.85` | 37,600.00 USD | 21,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.95` | 22,190.00 USD | 21,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.05` | 117,060.00 USD | 21,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.15` | 804,530.00 USD | 21,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.25` | 41,530.00 USD | 20,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.35` | 162,250.00 USD | 20,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.45` | 213,390.00 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.55` | 390,360.00 USD | 19,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.60` | 162,820,000.00 USD | 162,820,000.00 USD | 53,130.00 USD | 56,870.00 USD | 141,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.65` | 106,090.00 USD | 19,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.75` | 41,050.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `82.80` | 162,570,000.00 USD | 162,570,000.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `82.85` | 20,820.00 USD | 19,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.95` | 24,190.00 USD | 19,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.00` | 162,570,000.00 USD | 162,570,000.00 USD | 1,690.00 USD | 2,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.05` | 99,450.00 USD | 19,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.15` | 758,900.00 USD | 19,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.20` | 162,570,000.00 USD | 162,570,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.25` | 158,960.00 USD | 18,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.35` | 263,640.00 USD | 18,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.40` | 162,530,000.00 USD | 162,530,000.00 USD | 0.00 USD | 0.00 USD | 579.46 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.45` | 54,780.00 USD | 18,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.55` | 65,570.00 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.60` | 162,530,000.00 USD | 162,530,000.00 USD | 0.00 USD | 0.00 USD | 86,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.65` | 79,520.00 USD | 17,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.75` | 89,170.00 USD | 17,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.80` | 162,440,000.00 USD | 162,440,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.85` | 13,820.00 USD | 17,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.95` | 103,880.00 USD | 17,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 124,350.00 USD | 17,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.15` | 65,530.00 USD | 17,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.20` | 162,430,000.00 USD | 162,430,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.25` | 204,990.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.35` | 25,180.00 USD | 17,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.40` | 162,410,000.00 USD | 162,410,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.45` | 86,250.00 USD | 17,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 2,300.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 101,540.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 289,310.00 USD | 17,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 94,350.00 USD | 16,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 1,800.00 USD | 16,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 15,480.00 USD | 16,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.15` | 1,240,000.00 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.20` | 162,380,000.00 USD | 162,380,000.00 USD | 0.00 USD | 218,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.25` | 609,970.00 USD | 15,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.35` | 21,130.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.40` | 162,160,000.00 USD | 162,160,000.00 USD | 0.00 USD | 12,950.00 USD | 192,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.45` | 57,870.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.55` | 63,600.00 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.60` | 161,960,000.00 USD | 161,960,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.65` | 43,310.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.75` | 9,950.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.80` | 161,770,000.00 USD | 161,770,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.85` | 70,970.00 USD | 14,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.95` | 361,960.00 USD | 14,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.05` | 276,690.00 USD | 14,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.15` | 51,580.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.20` | 161,510,000.00 USD | 161,510,000.00 USD | 0.00 USD | 12,130.00 USD | 199,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.25` | 29,040.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.35` | 5,680.00 USD | 13,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.40` | 161,290,000.00 USD | 161,290,000.00 USD | 0.00 USD | 311,220.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.45` | 108,330.00 USD | 13,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.55` | 60,140.00 USD | 13,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.65` | 190,730.00 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.75` | 34,820.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.80` | 160,980,000.00 USD | 160,980,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.85` | 92,320.00 USD | 13,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.95` | 152,510.00 USD | 13,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.00` | 160,830,000.00 USD | 160,830,000.00 USD | 263,340.00 USD | 176,600.00 USD | 297,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.05` | 31,140.00 USD | 13,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.15` | 4,410.00 USD | 13,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.20` | 172,630,000.00 USD | 172,630,000.00 USD | 129,420.00 USD | 138,340.00 USD | 350,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.20` | 160,090,000.00 USD | 160,090,000.00 USD | 8,850.00 USD | 0.00 USD | 6,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.25` | 92,780.00 USD | 13,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.35` | 100,830.00 USD | 13,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.40` | 172,010,000.00 USD | 172,010,000.00 USD | 30,080.00 USD | 196,500.00 USD | 109,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.40` | 160,080,000.00 USD | 160,080,000.00 USD | 248,310.00 USD | 217,060.00 USD | 288,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.45` | 156,920.00 USD | 12,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.55` | 243,070.00 USD | 12,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.60` | 171,680,000.00 USD | 171,680,000.00 USD | 105,350.00 USD | 295,330.00 USD | 57,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.60` | 159,320,000.00 USD | 159,320,000.00 USD | 0.00 USD | 275,130.00 USD | 421,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.65` | 108,400.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.75` | 28,570.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.80` | 171,220,000.00 USD | 171,220,000.00 USD | 90,150.00 USD | 276,230.00 USD | 716,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `87.80` | 158,630,000.00 USD | 158,630,000.00 USD | 0.00 USD | 413,150.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.85` | 72,180.00 USD | 12,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.95` | 6,600.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.00` | 170,130,000.00 USD | 170,130,000.00 USD | 47,860.00 USD | 202,660.00 USD | 485,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.00` | 158,200,000.00 USD | 158,200,000.00 USD | 0.00 USD | 12,070.00 USD | 251,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.05` | 154,390.00 USD | 12,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.15` | 37,310.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.20` | 169,400,000.00 USD | 169,400,000.00 USD | 140,490.00 USD | 168,390.00 USD | 365,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.20` | 157,940,000.00 USD | 157,940,000.00 USD | 9,900.00 USD | 20,610.00 USD | 28,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.25` | 68,850.00 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.35` | 91,590.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.40` | 168,720,000.00 USD | 168,720,000.00 USD | 84,680.00 USD | 178,840.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.40` | 157,880,000.00 USD | 157,880,000.00 USD | 0.00 USD | 237,870.00 USD | 335,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.45` | 69,390.00 USD | 11,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.55` | 242,620.00 USD | 11,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.60` | 168,390,000.00 USD | 168,390,000.00 USD | 68,370.00 USD | 64,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.65` | 95,980.00 USD | 11,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.75` | 167,190.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.80` | 168,260,000.00 USD | 168,260,000.00 USD | 304,990.00 USD | 175,710.00 USD | 415,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `88.80` | 157,310,000.00 USD | 157,310,000.00 USD | 241,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.85` | 1,090,000.00 USD | 11,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.95` | 48,800.00 USD | 10,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.00` | 167,370,000.00 USD | 167,370,000.00 USD | 8,600.00 USD | 11,540.00 USD | 227,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.00` | 157,060,000.00 USD | 157,060,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.05` | 24,630.00 USD | 10,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.15` | 119,730.00 USD | 10,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.20` | 167,120,000.00 USD | 167,120,000.00 USD | 377,030.00 USD | 119,090.00 USD | 11,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.20` | 156,130,000.00 USD | 156,130,000.00 USD | 8,180.00 USD | 10,750.00 USD | 315,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.25` | 31,740.00 USD | 10,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.35` | 47,410.00 USD | 10,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.40` | 166,610,000.00 USD | 166,610,000.00 USD | 5,150.00 USD | 292,120.00 USD | 274,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.40` | 155,800,000.00 USD | 155,800,000.00 USD | 697,470.00 USD | 26,220.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.45` | 488,780.00 USD | 10,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.55` | 36,300.00 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.60` | 166,040,000.00 USD | 166,040,000.00 USD | 138,450.00 USD | 5,250.00 USD | 135,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.60` | 154,910,000.00 USD | 154,910,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.65` | 15,430.00 USD | 9,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.75` | 122,670.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.80` | 165,760,000.00 USD | 165,760,000.00 USD | 72,520.00 USD | 91,280.00 USD | 440,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `89.80` | 153,240,000.00 USD | 153,240,000.00 USD | 425,950.00 USD | 318,390.00 USD | 314,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.85` | 71,950.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.95` | 81,650.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.00` | 165,150,000.00 USD | 165,150,000.00 USD | 705,820.00 USD | 302,220.00 USD | 417,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.00` | 152,180,000.00 USD | 152,180,000.00 USD | 374,600.00 USD | 647,410.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.05` | 30,300.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.15` | 60,240.00 USD | 9,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.20` | 163,730,000.00 USD | 163,730,000.00 USD | 822,890.00 USD | 930,230.00 USD | 363,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.20` | 150,060,000.00 USD | 150,060,000.00 USD | 1,250,000.00 USD | 590,390.00 USD | 735,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.25` | 35,780.00 USD | 9,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.35` | 79,990.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.40` | 161,610,000.00 USD | 161,610,000.00 USD | 779,410.00 USD | 544,380.00 USD | 671,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.40` | 147,480,000.00 USD | 147,480,000.00 USD | 796,240.00 USD | 68,740.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.45` | 64,160.00 USD | 9,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.55` | 54,910.00 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.60` | 159,620,000.00 USD | 159,620,000.00 USD | 676,760.00 USD | 671,710.00 USD | 840,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.60` | 145,920,000.00 USD | 145,920,000.00 USD | 1,040,000.00 USD | 1,010,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.65` | 114,260.00 USD | 8,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.75` | 84,750.00 USD | 8,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.80` | 157,430,000.00 USD | 157,430,000.00 USD | 404,570.00 USD | 518,670.00 USD | 250,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.80` | 142,310,000.00 USD | 142,310,000.00 USD | 1,210,000.00 USD | 1,200,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.85` | 94,780.00 USD | 8,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.95` | 31,540.00 USD | 8,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.00` | 156,250,000.00 USD | 156,250,000.00 USD | 1,020,000.00 USD | 597,650.00 USD | 483,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.00` | 138,420,000.00 USD | 138,420,000.00 USD | 1,190,000.00 USD | 609,900.00 USD | 810,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.05` | 389,480.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.15` | 293,530.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.20` | 154,150,000.00 USD | 154,150,000.00 USD | 16,980.00 USD | 493,060.00 USD | 403,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.20` | 135,810,000.00 USD | 135,810,000.00 USD | 2,280,000.00 USD | 868,420.00 USD | 638,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.25` | 30,390.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.35` | 14,960.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.40` | 153,230,000.00 USD | 153,230,000.00 USD | 664,720.00 USD | 758,110.00 USD | 111,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.40` | 132,030,000.00 USD | 132,030,000.00 USD | 1,180,000.00 USD | 1,030,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.45` | 309,360.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.55` | 1,210,000.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.60` | 151,700,000.00 USD | 151,700,000.00 USD | 488,750.00 USD | 281,460.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.60` | 128,200,000.00 USD | 128,200,000.00 USD | 500,280.00 USD | 1,020,000.00 USD | 872,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.65` | 1,430,000.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.75` | 237,960.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.80` | 149,830,000.00 USD | 149,830,000.00 USD | 526,140.00 USD | 449,000.00 USD | 713,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.80` | 125,810,000.00 USD | 125,810,000.00 USD | 932,400.00 USD | 797,110.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.85` | 46,220.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.95` | 64,120.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.00` | 148,140,000.00 USD | 148,140,000.00 USD | 2,810,000.00 USD | 2,220,000.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.00` | 123,390,000.00 USD | 123,390,000.00 USD | 681,440.00 USD | 656,110.00 USD | 990,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.05` | 192,580.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.15` | 328,220.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.20` | 142,000,000.00 USD | 142,000,000.00 USD | 887,260.00 USD | 1,630,000.00 USD | 465,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.20` | 121,070,000.00 USD | 121,070,000.00 USD | 2,870,000.00 USD | 1,110,000.00 USD | 289,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.25` | 225,070.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.35` | 308,200.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.40` | 139,020,000.00 USD | 139,020,000.00 USD | 731,980.00 USD | 331,330.00 USD | 2,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.40` | 116,800,000.00 USD | 116,800,000.00 USD | 550,500.00 USD | 833,900.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.45` | 117,820.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.55` | 4,870.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.60` | 135,790,000.00 USD | 135,790,000.00 USD | 1,330,000.00 USD | 1,530,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.60` | 113,880,000.00 USD | 113,880,000.00 USD | 98,670.00 USD | 880,990.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.65` | 14,980.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.75` | 5,120.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.80` | 130,510,000.00 USD | 130,510,000.00 USD | 1,940,000.00 USD | 824,500.00 USD | 775,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.80` | 111,420,000.00 USD | 111,420,000.00 USD | 422,920.00 USD | 2,340,000.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.85` | 337,230.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.95` | 3,780.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.00` | 126,970,000.00 USD | 126,970,000.00 USD | 2,640,000.00 USD | 3,760,000.00 USD | 3,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.00` | 107,050,000.00 USD | 107,050,000.00 USD | 35,740.00 USD | 393,980.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.05` | 29,770.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.15` | 2,810.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.20` | 117,540,000.00 USD | 117,540,000.00 USD | 2,300,000.00 USD | 1,470,000.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.20` | 105,350,000.00 USD | 105,350,000.00 USD | 921,350.00 USD | 511,980.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.25` | 38,840.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.35` | 12,570.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.40` | 111,860,000.00 USD | 111,860,000.00 USD | 3,070,000.00 USD | 3,100,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.40` | 101,790,000.00 USD | 101,790,000.00 USD | 611,840.00 USD | 2,520,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.45` | 7,320.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.55` | 19,840.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.60` | 103,390,000.00 USD | 103,390,000.00 USD | 1,950,000.00 USD | 3,880,000.00 USD | 1,070,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.60` | 97,220,000.00 USD | 97,220,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.65` | 3,240.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.75` | 942,560.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.80` | 96,480,000.00 USD | 96,480,000.00 USD | 1,010,000.00 USD | 1,030,000.00 USD | 483,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.80` | 94,280,000.00 USD | 94,280,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.85` | 7,310.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.95` | 1,140,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.00` | 93,970,000.00 USD | 93,970,000.00 USD | 759,420.00 USD | 1,060,000.00 USD | 1,830,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.00` | 89,030,000.00 USD | 89,030,000.00 USD | 2,660,000.00 USD | 1,780,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.15` | 33,550.00 USD | 821,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.20` | 90,320,000.00 USD | 90,320,000.00 USD | 1,980,000.00 USD | 1,940,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.20` | 82,380,000.00 USD | 82,380,000.00 USD | 134,580.00 USD | 962,410.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.25` | 8,860.00 USD | 788,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.35` | 5,200.00 USD | 779,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.40` | 84,240,000.00 USD | 84,240,000.00 USD | 1,650,000.00 USD | 568,640.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.40` | 78,540,000.00 USD | 78,540,000.00 USD | 0.00 USD | 496,790.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.45` | 146,220.00 USD | 774,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.55` | 97,340.00 USD | 627,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.60` | 81,020,000.00 USD | 81,020,000.00 USD | 142,910.00 USD | 1,380,000.00 USD | 396,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.60` | 78,030,000.00 USD | 78,030,000.00 USD | 560,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.65` | 2,690.00 USD | 530,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.75` | 33,140.00 USD | 527,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.80` | 79,100,000.00 USD | 79,100,000.00 USD | 2,800,000.00 USD | 553,660.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.80` | 77,470,000.00 USD | 77,470,000.00 USD | 2,010,000.00 USD | 99,300.00 USD | 3,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.85` | 52,310.00 USD | 494,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.95` | 13,860.00 USD | 442,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.00` | 74,520,000.00 USD | 74,520,000.00 USD | 3,210,000.00 USD | 673,040.00 USD | 17,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.00` | 72,000,000.00 USD | 72,000,000.00 USD | 2,400,000.00 USD | 4,460,000.00 USD | 47,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.05` | 77,030.00 USD | 428,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.15` | 25,120.00 USD | 351,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.20` | 70,630,000.00 USD | 70,630,000.00 USD | 875,540.00 USD | 1,490,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.20` | 65,100,000.00 USD | 65,100,000.00 USD | 2,080,000.00 USD | 0.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.25` | 32,200.00 USD | 326,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.35` | 8,070.00 USD | 294,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.40` | 65,300,000.00 USD | 65,300,000.00 USD | 1,120,000.00 USD | 1,820,000.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.40` | 62,990,000.00 USD | 62,990,000.00 USD | 2,080,000.00 USD | 2,340,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.45` | 23,290.00 USD | 286,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.55` | 48,980.00 USD | 262,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.60` | 61,190,000.00 USD | 61,190,000.00 USD | 1,850,000.00 USD | 2,410,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.60` | 53,980,000.00 USD | 53,980,000.00 USD | 3,820,000.00 USD | 7,040,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.65` | 93,140.00 USD | 213,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.75` | 84,480.00 USD | 120,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.80` | 55,790,000.00 USD | 55,790,000.00 USD | 571,180.00 USD | 1,020,000.00 USD | 5,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.80` | 38,540,000.00 USD | 38,540,000.00 USD | 3,400,000.00 USD | 93,510.00 USD | 1,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.85` | 32,540.00 USD | 36,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.95` | 231.24 USD | 3,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.00` | 48,290,000.00 USD | 48,290,000.00 USD | 3,110,000.00 USD | 2,380,000.00 USD | 4,580,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.00` | 33,770,000.00 USD | 33,770,000.00 USD | 2,670,000.00 USD | 728,410.00 USD | 3,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.05` | 2,210.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.15` | 345.18 USD | 1,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.20` | 38,220,000.00 USD | 38,220,000.00 USD | 4,910,000.00 USD | 6,490,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.20` | 26,780,000.00 USD | 26,780,000.00 USD | 6,840,000.00 USD | 1,580,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.35` | 964.46 USD | 964.46 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.40` | 25,520,000.00 USD | 25,520,000.00 USD | 4,170,000.00 USD | 2,150,000.00 USD | 4,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.40` | 13,110,000.00 USD | 13,110,000.00 USD | 1,600,000.00 USD | 2,590,000.00 USD | 6,470,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.60` | 14,580,000.00 USD | 14,580,000.00 USD | 1,410,000.00 USD | 2,010,000.00 USD | 299,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.60` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.80` | 10,860,000.00 USD | 10,860,000.00 USD | 1,350,000.00 USD | 2,230,000.00 USD | 2,320,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.80` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 79,170.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.00` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 1,410,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.00` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 2,870,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.00` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 2,870,000.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.20` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.20` | 16,470,000.00 USD | 16,470,000.00 USD | 0.00 USD | 3,100,000.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.40` | 3,330,000.00 USD | 3,330,000.00 USD | 534,370.00 USD | 1,280,000.00 USD | 292,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.40` | 16,580,000.00 USD | 16,580,000.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `97.45` | 331.33 USD | 331.33 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `97.60` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.60` | 20,510,000.00 USD | 20,510,000.00 USD | 0.00 USD | 24,930.00 USD | 3,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.80` | 6,190,000.00 USD | 6,190,000.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.80` | 31,530,000.00 USD | 31,530,000.00 USD | 7,580,000.00 USD | 3,430,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.00` | 7,480,000.00 USD | 7,480,000.00 USD | 773,040.00 USD | 196,190.00 USD | 320,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.00` | 42,960,000.00 USD | 42,960,000.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.20` | 12,120,000.00 USD | 12,120,000.00 USD | 1,900,000.00 USD | 1,430,000.00 USD | 1,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.20` | 52,750,000.00 USD | 52,750,000.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.40` | 22,920,000.00 USD | 22,920,000.00 USD | 772,180.00 USD | 311,650.00 USD | 9,720,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.40` | 63,880,000.00 USD | 63,880,000.00 USD | 1,780,000.00 USD | 3,320,000.00 USD | 6,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.55` | 5,930.00 USD | 6,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.60` | 36,140,000.00 USD | 36,140,000.00 USD | 488,190.00 USD | 5,730,000.00 USD | 7,000,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.60` | 73,110,000.00 USD | 73,110,000.00 USD | 1,880,000.00 USD | 5,400,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.65` | 9,740.00 USD | 16,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.80` | 47,690,000.00 USD | 47,690,000.00 USD | 1,400,000.00 USD | 4,160,000.00 USD | 5,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.80` | 76,060,000.00 USD | 76,060,000.00 USD | 71,480.00 USD | 470,960.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.95` | 1,020.00 USD | 17,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.00` | 61,350,000.00 USD | 61,350,000.00 USD | 2,660,000.00 USD | 5,590,000.00 USD | 5,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.00` | 84,240,000.00 USD | 84,240,000.00 USD | 1,830,000.00 USD | 2,380,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.05` | 5,640.00 USD | 22,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.15` | 1,110,000.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.20` | 72,350,000.00 USD | 72,350,000.00 USD | 2,840,000.00 USD | 4,520,000.00 USD | 3,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.20` | 97,930,000.00 USD | 97,930,000.00 USD | 1,220,000.00 USD | 6,240,000.00 USD | 6,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.25` | 7,330.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.35` | 64,750.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.40` | 79,260,000.00 USD | 79,260,000.00 USD | 3,580,000.00 USD | 1,650,000.00 USD | 1,680,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.40` | 98,970,000.00 USD | 98,970,000.00 USD | 0.00 USD | 1,010,000.00 USD | 25,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.45` | 335.15 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.55` | 11,890.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.60` | 96,010,000.00 USD | 96,010,000.00 USD | 2,920,000.00 USD | 6,720,000.00 USD | 7,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.60` | 104,400,000.00 USD | 104,400,000.00 USD | 2,240,000.00 USD | 2,640,000.00 USD | 545,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.65` | 1,130.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.75` | 25,520.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.80` | 110,970,000.00 USD | 110,970,000.00 USD | 2,520,000.00 USD | 4,590,000.00 USD | 7,850,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `99.80` | 107,730,000.00 USD | 107,730,000.00 USD | 736,270.00 USD | 1,330,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.85` | 238.64 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `99.95` | 3,070.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.00` | 121,420,000.00 USD | 121,420,000.00 USD | 2,850,000.00 USD | 3,360,000.00 USD | 4,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.00` | 119,060,000.00 USD | 119,060,000.00 USD | 2,220,000.00 USD | 2,310,000.00 USD | 6,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.05` | 32,030.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.15` | 33,940.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.20` | 124,590,000.00 USD | 124,590,000.00 USD | 651,800.00 USD | 2,130,000.00 USD | 388,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.20` | 125,140,000.00 USD | 125,140,000.00 USD | 843,770.00 USD | 2,460,000.00 USD | 2,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.25` | 345,350.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.35` | 410,700.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.40` | 130,340,000.00 USD | 130,340,000.00 USD | 976,110.00 USD | 1,790,000.00 USD | 2,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.40` | 129,620,000.00 USD | 129,620,000.00 USD | 993,830.00 USD | 654,600.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.45` | 26,900.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.55` | 41,910.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.60` | 140,980,000.00 USD | 140,980,000.00 USD | 2,220,000.00 USD | 1,710,000.00 USD | 6,710,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.60` | 135,400,000.00 USD | 135,400,000.00 USD | 2,110,000.00 USD | 1,450,000.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.65` | 102,960.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.75` | 19,590.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.80` | 146,430,000.00 USD | 146,430,000.00 USD | 1,990,000.00 USD | 1,820,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.80` | 137,140,000.00 USD | 137,140,000.00 USD | 491,210.00 USD | 1,220,000.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.95` | 498.69 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.00` | 156,520,000.00 USD | 156,520,000.00 USD | 5,830,000.00 USD | 3,070,000.00 USD | 1,190,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.00` | 155,780,000.00 USD | 155,780,000.00 USD | 4,000,000.00 USD | 6,900,000.00 USD | 7,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.05` | 168.75 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.15` | 12,350.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.20` | 169,240,000.00 USD | 169,240,000.00 USD | 5,410,000.00 USD | 4,390,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.20` | 175,050,000.00 USD | 175,050,000.00 USD | 7,240,000.00 USD | 5,180,000.00 USD | 6,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.25` | 769.50 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.40` | 179,910,000.00 USD | 179,910,000.00 USD | 3,860,000.00 USD | 2,700,000.00 USD | 4,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.40` | 192,110,000.00 USD | 192,110,000.00 USD | 4,720,000.00 USD | 1,270,000.00 USD | 11,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.45` | 1,340.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.55` | 2,790.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.60` | 195,720,000.00 USD | 195,720,000.00 USD | 3,100,000.00 USD | 2,930,000.00 USD | 9,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.60` | 202,630,000.00 USD | 202,630,000.00 USD | 3,650,000.00 USD | 30,170.00 USD | 6,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.65` | 2,640.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.80` | 201,940,000.00 USD | 201,940,000.00 USD | 646,170.00 USD | 836,200.00 USD | 4,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.80` | 212,560,000.00 USD | 212,560,000.00 USD | 3,050,000.00 USD | 609,510.00 USD | 6,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.85` | 8,240.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `101.95` | 1,760.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.00` | 208,220,000.00 USD | 208,220,000.00 USD | 2,520,000.00 USD | 1,780,000.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.00` | 218,550,000.00 USD | 218,550,000.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.05` | 5,220.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.20` | 214,570,000.00 USD | 214,570,000.00 USD | 3,180,000.00 USD | 1,360,000.00 USD | 1,800,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.20` | 225,270,000.00 USD | 225,270,000.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.25` | 1,170.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.35` | 720.54 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.40` | 219,070,000.00 USD | 219,070,000.00 USD | 1,560,000.00 USD | 716,320.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.40` | 230,580,000.00 USD | 230,580,000.00 USD | 2,340,000.00 USD | 304,350.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.45` | 175.19 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.55` | 6,330.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.60` | 221,700,000.00 USD | 221,700,000.00 USD | 985,660.00 USD | 606,030.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.60` | 233,040,000.00 USD | 233,040,000.00 USD | 1,450,000.00 USD | 979,270.00 USD | 33,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.65` | 1,070.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.75` | 3,340.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.80` | 225,750,000.00 USD | 225,750,000.00 USD | 1,260,000.00 USD | 1,570,000.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.80` | 241,130,000.00 USD | 241,130,000.00 USD | 7,780,000.00 USD | 23,810.00 USD | 286,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.95` | 4,150.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.00` | 230,800,000.00 USD | 230,800,000.00 USD | 3,120,000.00 USD | 1,440,000.00 USD | 498,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.00` | 258,070,000.00 USD | 258,070,000.00 USD | 12,270,000.00 USD | 394,420.00 USD | 4,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.05` | 692.50 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.15` | 11,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.20` | 233,180,000.00 USD | 233,180,000.00 USD | 301,000.00 USD | 853,780.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.20` | 270,740,000.00 USD | 270,740,000.00 USD | 11,620,000.00 USD | 140,550.00 USD | 913,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.25` | 859.04 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.35` | 385.50 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.40` | 236,100,000.00 USD | 236,100,000.00 USD | 867,130.00 USD | 1,180,000.00 USD | 877,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.40` | 285,310,000.00 USD | 285,310,000.00 USD | 11,050,000.00 USD | 233,330.00 USD | 3,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.45` | 14,540.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.60` | 243,730,000.00 USD | 243,730,000.00 USD | 2,430,000.00 USD | 183,360.00 USD | 5,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.60` | 303,700,000.00 USD | 303,700,000.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.65` | 4,360.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.75` | 261,050.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.80` | 246,930,000.00 USD | 246,930,000.00 USD | 527,740.00 USD | 1,320,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.80` | 316,080,000.00 USD | 316,080,000.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.85` | 14,220.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.95` | 827.44 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.00` | 253,200,000.00 USD | 253,200,000.00 USD | 2,450,000.00 USD | 1,560,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.00` | 342,790,000.00 USD | 342,790,000.00 USD | 10,830,000.00 USD | 7,160,000.00 USD | 8,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.05` | 775.17 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.15` | 1,180.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.20` | 256,620,000.00 USD | 256,620,000.00 USD | 1,440,000.00 USD | 931,620.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.20` | 364,820,000.00 USD | 364,820,000.00 USD | 8,520,000.00 USD | 7,230,000.00 USD | 6,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.25` | 722.45 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.35` | 11,820.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.40` | 261,480,000.00 USD | 261,480,000.00 USD | 1,860,000.00 USD | 1,510,000.00 USD | 1,490,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.40` | 382,000,000.00 USD | 382,000,000.00 USD | 5,100,000.00 USD | 3,710,000.00 USD | 8,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.45` | 12,640.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.55` | 360.70 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.60` | 265,720,000.00 USD | 265,720,000.00 USD | 1,060,000.00 USD | 868,480.00 USD | 2,310,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.60` | 399,750,000.00 USD | 399,750,000.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.65` | 401.86 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.75` | 199.02 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.80` | 269,730,000.00 USD | 269,730,000.00 USD | 1,250,000.00 USD | 820,470.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.80` | 417,140,000.00 USD | 417,140,000.00 USD | 5,170,000.00 USD | 4,410,000.00 USD | 7,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.85` | 3,430.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.95` | 126,060.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.00` | 270,960,000.00 USD | 270,960,000.00 USD | 463,890.00 USD | 350,040.00 USD | 413,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.00` | 433,310,000.00 USD | 433,310,000.00 USD | 5,730,000.00 USD | 4,110,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.05` | 2,800.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.15` | 21,880.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.20` | 272,030,000.00 USD | 272,030,000.00 USD | 111,930.00 USD | 94,030.00 USD | 864,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.20` | 443,970,000.00 USD | 443,970,000.00 USD | 5,340,000.00 USD | 2,800,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.25` | 2,860.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.35` | 6,840.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.40` | 272,510,000.00 USD | 272,510,000.00 USD | 262,490.00 USD | 138,720.00 USD | 78,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.40` | 452,190,000.00 USD | 452,190,000.00 USD | 1,570,000.00 USD | 3,170,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.45` | 531,450.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.55` | 5,240.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.60` | 272,940,000.00 USD | 272,940,000.00 USD | 130,280.00 USD | 187,950.00 USD | 110,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.60` | 464,240,000.00 USD | 464,240,000.00 USD | 4,800,000.00 USD | 2,700,000.00 USD | 4,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.65` | 1,740.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.80` | 273,630,000.00 USD | 273,630,000.00 USD | 87,540.00 USD | 526,970.00 USD | 76,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.80` | 473,050,000.00 USD | 473,050,000.00 USD | 2,690,000.00 USD | 2,620,000.00 USD | 3,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.85` | 92,920.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `105.95` | 592.26 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.00` | 274,780,000.00 USD | 274,780,000.00 USD | 372,000.00 USD | 554,120.00 USD | 226,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.00` | 478,200,000.00 USD | 478,200,000.00 USD | 1,970,000.00 USD | 1,050,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.05` | 33,380.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.15` | 248.39 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.20` | 276,200,000.00 USD | 276,200,000.00 USD | 623,340.00 USD | 349,490.00 USD | 440,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.20` | 487,100,000.00 USD | 487,100,000.00 USD | 3,820,000.00 USD | 2,560,000.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.35` | 256,250.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.40` | 276,930,000.00 USD | 276,930,000.00 USD | 181,780.00 USD | 354,890.00 USD | 197,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.40` | 493,160,000.00 USD | 493,160,000.00 USD | 2,420,000.00 USD | 2,170,000.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.45` | 34,730.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.55` | 105.48 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.60` | 278,610,000.00 USD | 278,610,000.00 USD | 388,660.00 USD | 278,100.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.60` | 499,810,000.00 USD | 499,810,000.00 USD | 1,870,000.00 USD | 1,460,000.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.65` | 6,360.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.80` | 279,950,000.00 USD | 279,950,000.00 USD | 340,680.00 USD | 280,340.00 USD | 718,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.80` | 504,460,000.00 USD | 504,460,000.00 USD | 999,190.00 USD | 918,930.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.85` | 479,130.00 USD | 4,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.95` | 37,730.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.00` | 280,700,000.00 USD | 280,700,000.00 USD | 193,920.00 USD | 413,830.00 USD | 147,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.00` | 508,600,000.00 USD | 508,600,000.00 USD | 527,980.00 USD | 1,180,000.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.05` | 14,600.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.15` | 3,060.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.20` | 281,190,000.00 USD | 281,190,000.00 USD | 0.00 USD | 50,140.00 USD | 436,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.20` | 509,690,000.00 USD | 509,690,000.00 USD | 230,020.00 USD | 507,570.00 USD | 352,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.25` | 35,230.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.35` | 766.48 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.40` | 282,030,000.00 USD | 282,030,000.00 USD | 90,150.00 USD | 226,090.00 USD | 523,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.40` | 510,980,000.00 USD | 510,980,000.00 USD | 0.00 USD | 576,040.00 USD | 709,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.45` | 32,580.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.55` | 11,910.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.60` | 282,770,000.00 USD | 282,770,000.00 USD | 47,860.00 USD | 202,660.00 USD | 485,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.60` | 511,610,000.00 USD | 511,610,000.00 USD | 213,520.00 USD | 12,070.00 USD | 406,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.80` | 283,440,000.00 USD | 283,440,000.00 USD | 140,490.00 USD | 168,390.00 USD | 365,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.80` | 512,440,000.00 USD | 512,440,000.00 USD | 499,550.00 USD | 31,020.00 USD | 305,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.85` | 143,340.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.95` | 17,360.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.00` | 283,770,000.00 USD | 283,770,000.00 USD | 84,680.00 USD | 178,840.00 USD | 65,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.00` | 513,020,000.00 USD | 513,020,000.00 USD | 5,950.00 USD | 237,870.00 USD | 335,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.15` | 1,150.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `108.20` | 283,900,000.00 USD | 283,900,000.00 USD | 68,370.00 USD | 62,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.20` | 513,300,000.00 USD | 513,300,000.00 USD | 0.00 USD | 205,080.00 USD | 74,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.25` | 38,000.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.35` | 3,470.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.40` | 513,790,000.00 USD | 513,790,000.00 USD | 487,890.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.45` | 108,080.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.55` | 117.23 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.60` | 513,980,000.00 USD | 513,980,000.00 USD | 17,470.00 USD | 167,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.65` | 5,050.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.75` | 2,120.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.80` | 515,820,000.00 USD | 515,820,000.00 USD | 624,820.00 USD | 397,420.00 USD | 819,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.85` | 3,230.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.95` | 3,170.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.00` | 516,110,000.00 USD | 516,110,000.00 USD | 8,180.00 USD | 0.00 USD | 286,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.05` | 163.58 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.25` | 131,370.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.35` | 247.13 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.45` | 202.48 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.55` | 408,340.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.65` | 38,640.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.85` | 3,190.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.95` | 301.26 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.05` | 14,560.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.15` | 194.97 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.25` | 195.14 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.35` | 158.90 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 143,580.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 203.41 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 38,290.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.85` | 1,090.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 4,450.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.15` | 1,710.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.35` | 390.84 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.45` | 841.45 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.55` | 892.40 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.65` | 3,220.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.75` | 169.86 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.85` | 15,880.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.95` | 223.90 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.15` | 528.23 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.35` | 61,610.00 USD | 5,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.45` | 5,670.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.55` | 844.13 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.65` | 707.44 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.75` | 118,640.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.85` | 108,760.00 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.05` | 406.98 USD | 5,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.15` | 9,560.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.25` | 698.75 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.35` | 4,120.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.45` | 3,360.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.55` | 263,860.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.65` | 105,510.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.75` | 5,200.00 USD | 6,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.85` | 104.74 USD | 6,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.95` | 21,840.00 USD | 6,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.05` | 31,740.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.25` | 2,150.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.45` | 3,830.00 USD | 6,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.55` | 7,090.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.65` | 3,430.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.05` | 569,550.00 USD | 6,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.15` | 1,100.00 USD | 6,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.25` | 161.35 USD | 6,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.45` | 893,760.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.55` | 167,330.00 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.75` | 160.89 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.85` | 289.62 USD | 7,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.05` | 4,450.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.25` | 180.19 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.35` | 4,960.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.55` | 2,040.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.65` | 113.15 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.85` | 1,520.00 USD | 7,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.05` | 156.85 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.15` | 90,390.00 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.25` | 225.12 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.35` | 4,790,000.00 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.55` | 188.08 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.65` | 47,200.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.75` | 20,960.00 USD | 12,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.95` | 353.85 USD | 12,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.25` | 4,470,000.00 USD | 17,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.45` | 30,080.00 USD | 17,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.55` | 7,700.00 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.75` | 309.94 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.25` | 240.88 USD | 17,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.35` | 57,850.00 USD | 17,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.45` | 27,900.00 USD | 17,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.55` | 8,970.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.65` | 1,760.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.75` | 731.67 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.85` | 485.39 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.95` | 4,200.00 USD | 17,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.05` | 96,110.00 USD | 17,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.15` | 2,980.00 USD | 17,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.45` | 145.74 USD | 17,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.55` | 1,190.00 USD | 17,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.65` | 60,330.00 USD | 17,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.95` | 13,290.00 USD | 17,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.15` | 316.20 USD | 17,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.25` | 1,550.00 USD | 17,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.55` | 6,460.00 USD | 17,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.75` | 105.92 USD | 17,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.05` | 56,150.00 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.15` | 169.79 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.25` | 883,070.00 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.45` | 17,500.00 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.65` | 116.52 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.25` | 472,220.00 USD | 19,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.35` | 2,330.00 USD | 19,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.45` | 126,270.00 USD | 19,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.65` | 6,680.00 USD | 19,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.05` | 586.76 USD | 19,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.15` | 121.67 USD | 19,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.25` | 23,360.00 USD | 19,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.35` | 29,710.00 USD | 19,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.45` | 46,110.00 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.55` | 3,080.00 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.65` | 675.60 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.75` | 6,020.00 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.95` | 3,500.00 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.05` | 208.83 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.15` | 462,650.00 USD | 19,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.35` | 5,320.00 USD | 19,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.45` | 590.87 USD | 19,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.55` | 4,610.00 USD | 19,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.65` | 1,560.00 USD | 19,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.75` | 1,930.00 USD | 19,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.85` | 57,880.00 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.95` | 110.84 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.05` | 810.50 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.15` | 470.54 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.35` | 4,090.00 USD | 19,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.45` | 5,000.00 USD | 19,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.65` | 30,830.00 USD | 19,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.75` | 10,650.00 USD | 19,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.85` | 3,870.00 USD | 19,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.05` | 262,490.00 USD | 20,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.15` | 389.08 USD | 20,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.35` | 6,610,000.00 USD | 26,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.55` | 139,870.00 USD | 26,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.65` | 4,840.00 USD | 26,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.75` | 20,800.00 USD | 26,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.85` | 388.66 USD | 26,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.95` | 10,510.00 USD | 27,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.05` | 116,190.00 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.35` | 195.09 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.45` | 783.54 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.65` | 788.62 USD | 27,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.75` | 18,730.00 USD | 27,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.85` | 32,440.00 USD | 27,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.15` | 55,570.00 USD | 27,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.25` | 32,310.00 USD | 27,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.35` | 699,390.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.55` | 2,590.00 USD | 27,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.75` | 71,060.00 USD | 28,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.85` | 490.83 USD | 28,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.25` | 13,200.00 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.35` | 145.99 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.65` | 866.21 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.75` | 132.06 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.85` | 3,180.00 USD | 28,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.95` | 2,070.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.05` | 188.71 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.25` | 1,560.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.45` | 219.52 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.85` | 3,100.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.95` | 3,710.00 USD | 28,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.05` | 11,940.00 USD | 28,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.15` | 325.09 USD | 28,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.55` | 8,730.00 USD | 28,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.65` | 240.10 USD | 28,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.85` | 49,280.00 USD | 28,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.05` | 30,050.00 USD | 28,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.15` | 10,040.00 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.25` | 1,330.00 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.35` | 390.72 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.65` | 156.37 USD | 28,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.75` | 151,200.00 USD | 28,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.95` | 503.65 USD | 28,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.05` | 12,620.00 USD | 28,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.25` | 11,590.00 USD | 28,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.65` | 67,330.00 USD | 28,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.35` | 414.17 USD | 28,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.75` | 6,420.00 USD | 28,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.85` | 3,250.00 USD | 28,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.95` | 49,400.00 USD | 28,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.15` | 14,640.00 USD | 28,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.35` | 8,690.00 USD | 28,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.55` | 136.55 USD | 28,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.65` | 1,110.00 USD | 28,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.75` | 4,090.00 USD | 28,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.95` | 34,240.00 USD | 28,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.05` | 836.00 USD | 28,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.15` | 2,220.00 USD | 28,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.35` | 18,410.00 USD | 28,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.55` | 697.38 USD | 28,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.95` | 2,050.00 USD | 28,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.05` | 4,090.00 USD | 28,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.15` | 41,450.00 USD | 28,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.25` | 45,220.00 USD | 28,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.45` | 7,310.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.75` | 2,360.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.15` | 552.43 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.35` | 4,180.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.45` | 253.80 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.55` | 494.01 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.65` | 1,680.00 USD | 28,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.75` | 4,870.00 USD | 28,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.95` | 394.66 USD | 28,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.05` | 116.24 USD | 28,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.35` | 158.60 USD | 28,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.45` | 4,870.00 USD | 28,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.55` | 1,330.00 USD | 28,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.65` | 7,340.00 USD | 28,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.85` | 5,160,000.00 USD | 33,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.95` | 1,940.00 USD | 33,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.05` | 3,080.00 USD | 33,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.35` | 210.61 USD | 33,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.45` | 247,540.00 USD | 34,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.55` | 1,950,000.00 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.65` | 211.06 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.75` | 4,780.00 USD | 36,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.95` | 23,020.00 USD | 36,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.05` | 782.70 USD | 36,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.25` | 3,470.00 USD | 36,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.45` | 151.00 USD | 36,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.75` | 368.30 USD | 36,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.15` | 90,580.00 USD | 36,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.25` | 2,830.00 USD | 36,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.35` | 64,570.00 USD | 36,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.55` | 103.36 USD | 36,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.95` | 597,390.00 USD | 36,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.05` | 3,750.00 USD | 36,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.15` | 23,300.00 USD | 36,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.55` | 602.77 USD | 36,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.65` | 3,260.00 USD | 36,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.75` | 72,380.00 USD | 36,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.15` | 1,760.00 USD | 36,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.35` | 106,270.00 USD | 37,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.45` | 28,990.00 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.65` | 145.65 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.85` | 5,850.00 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.95` | 490.39 USD | 37,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.15` | 88,760.00 USD | 37,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.25` | 4,050.00 USD | 37,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.35` | 7,330.00 USD | 37,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.55` | 17,380.00 USD | 37,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.65` | 587,730.00 USD | 37,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.75` | 2,110.00 USD | 37,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.95` | 78,060.00 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.05` | 166.17 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.15` | 1,730.00 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.35` | 169.45 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.45` | 204.96 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.55` | 1,000.00 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.65` | 237.72 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.85` | 578.09 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.15` | 122,350.00 USD | 37,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.25` | 78,630.00 USD | 38,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.35` | 445,050.00 USD | 38,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.45` | 519,740.00 USD | 39,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.55` | 373,600.00 USD | 39,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.65` | 5,650.00 USD | 39,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.75` | 93,700.00 USD | 39,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.05` | 1,120.00 USD | 39,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.35` | 1,390,000.00 USD | 40,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.55` | 116.65 USD | 40,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.65` | 16,030.00 USD | 40,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.95` | 234,200.00 USD | 41,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.05` | 5,200.00 USD | 41,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.15` | 123,300.00 USD | 41,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.85` | 346.96 USD | 41,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.95` | 2,370.00 USD | 41,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.15` | 3,180.00 USD | 41,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.45` | 8,830.00 USD | 41,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.55` | 1,740,000.00 USD | 43,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.95` | 1,110,000.00 USD | 44,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.05` | 4,610,000.00 USD | 48,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.15` | 44,670.00 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.25` | 400.42 USD | 48,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.35` | 287,690.00 USD | 49,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.45` | 5,950.00 USD | 49,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.55` | 757,860.00 USD | 49,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.75` | 1,570.00 USD | 49,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.95` | 925.35 USD | 49,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.05` | 1,060.00 USD | 49,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.15` | 44,610.00 USD | 49,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.25` | 239.07 USD | 49,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.35` | 2,300.00 USD | 49,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.45` | 1,230.00 USD | 49,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.65` | 8,340.00 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.85` | 1,490.00 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.15` | 292.89 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.25` | 2,340.00 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.45` | 4,240.00 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.75` | 363.66 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.05` | 117.84 USD | 49,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.25` | 1,110.00 USD | 49,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.35` | 2,810.00 USD | 49,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.55` | 267.55 USD | 49,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.05` | 326.14 USD | 49,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.15` | 7,810.00 USD | 49,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.35` | 197.00 USD | 49,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.45` | 4,900.00 USD | 49,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.05` | 80,150.00 USD | 50,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.15` | 49,270.00 USD | 50,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.65` | 654.25 USD | 50,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.75` | 92,600.00 USD | 50,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.85` | 237,070.00 USD | 50,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.35` | 23,570.00 USD | 50,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.65` | 428,360.00 USD | 50,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.75` | 3,610,000.00 USD | 54,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.05` | 145,990.00 USD | 54,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.25` | 654.52 USD | 54,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.65` | 1,760.00 USD | 54,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.95` | 497.44 USD | 54,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.15` | 683,000.00 USD | 55,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.25` | 80,940.00 USD | 55,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.35` | 655.83 USD | 55,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.55` | 28,140.00 USD | 55,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.05` | 2,240.00 USD | 55,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.35` | 1,530.00 USD | 55,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.45` | 322,900.00 USD | 55,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.55` | 410.34 USD | 55,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.65` | 86,120.00 USD | 55,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.75` | 18,940.00 USD | 55,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.95` | 5,840,000.00 USD | 61,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.35` | 6,500.00 USD | 61,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.45` | 142,860.00 USD | 61,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.55` | 24,150.00 USD | 61,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.55` | 23,440.00 USD | 61,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.85` | 786.48 USD | 61,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.95` | 208,190.00 USD | 62,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.75` | 677.12 USD | 62,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.15` | 198.18 USD | 62,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.15` | 1,620.00 USD | 62,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.25` | 14,070.00 USD | 62,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.65` | 67,790.00 USD | 62,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.95` | 3,440.00 USD | 62,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.15` | 17,120.00 USD | 62,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.55` | 150.80 USD | 62,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.65` | 115.68 USD | 62,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.75` | 1,890.00 USD | 62,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.95` | 4,090.00 USD | 62,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.05` | 122.68 USD | 62,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.35` | 19,740.00 USD | 62,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.65` | 437,600.00 USD | 62,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.05` | 34,790.00 USD | 62,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.35` | 443.70 USD | 62,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.55` | 335.71 USD | 62,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.75` | 3,180.00 USD | 62,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.95` | 181,510.00 USD | 62,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.45` | 111.44 USD | 62,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.55` | 1,180.00 USD | 62,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.75` | 20,440.00 USD | 62,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.45` | 51,730.00 USD | 62,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.65` | 27,960.00 USD | 62,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.35` | 204.55 USD | 62,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.45` | 16,540.00 USD | 62,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.75` | 284.95 USD | 62,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.85` | 695.40 USD | 62,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.95` | 346.16 USD | 62,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.15` | 104,490.00 USD | 63,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.25` | 245,010.00 USD | 63,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.35` | 205,490.00 USD | 63,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.75` | 146.79 USD | 63,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.85` | 38,470,000.00 USD | 102,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.15` | 238.20 USD | 102,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.45` | 119.31 USD | 102,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.75` | 263.62 USD | 102,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.85` | 105,510.00 USD | 102,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.95` | 19,890.00 USD | 102,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.05` | 123.23 USD | 102,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.25` | 625.69 USD | 102,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.35` | 3,530,000.00 USD | 105,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.65` | 25,540.00 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.75` | 1,300.00 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.85` | 4,420.00 USD | 105,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.55` | 267,040.00 USD | 105,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.65` | 4,320.00 USD | 105,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.75` | 208,810.00 USD | 106,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.85` | 277.45 USD | 106,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.95` | 78,300.00 USD | 106,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.05` | 142,440.00 USD | 106,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.05` | 4,970.00 USD | 106,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.65` | 44,930.00 USD | 106,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.85` | 1,040,000.00 USD | 107,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.15` | 1,340,000.00 USD | 108,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.55` | 38,150.00 USD | 108,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.25` | 19,490.00 USD | 108,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.55` | 254.17 USD | 108,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.05` | 91,030.00 USD | 108,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.15` | 3,990.00 USD | 108,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.35` | 72,940.00 USD | 109,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.45` | 9,440.00 USD | 109,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.05` | 3,660,000.00 USD | 112,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.15` | 793.69 USD | 112,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.25` | 1,680.00 USD | 112,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.95` | 165,230.00 USD | 112,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.15` | 7,670.00 USD | 112,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.25` | 737.29 USD | 112,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.45` | 56,050.00 USD | 112,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.55` | 1,220.00 USD | 112,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.65` | 11,090.00 USD | 112,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.85` | 2,190.00 USD | 112,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.55` | 232.56 USD | 112,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.75` | 2,460.00 USD | 112,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.85` | 14,260.00 USD | 112,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.15` | 997.20 USD | 112,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.55` | 231.92 USD | 112,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.65` | 29,110.00 USD | 113,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.75` | 4,070.00 USD | 113,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.95` | 1,450.00 USD | 113,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.25` | 456.09 USD | 113,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.85` | 189.85 USD | 113,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.95` | 284,930.00 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.15` | 148.32 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.45` | 118.08 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.55` | 118.14 USD | 113,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.95` | 13,570,000.00 USD | 126,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.35` | 68,210.00 USD | 126,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.85` | 383,700.00 USD | 127,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.95` | 514.43 USD | 127,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.15` | 872,340.00 USD | 128,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.25` | 280.69 USD | 128,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.15` | 2,170.00 USD | 128,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.55` | 114,580.00 USD | 128,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.05` | 19,910.00 USD | 128,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.15` | 1,380.00 USD | 128,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.25` | 9,380.00 USD | 128,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `19.45` | 122,460,000.00 USD | 0.00 USD | 3,100.00 USD | `-80.00%` | `159.30` |
| `Live` | `Long` | `19.55` | 122,460,000.00 USD | 0.00 USD | 449.65 USD | `-79.90%` | `23.00` |
| `Live` | `Long` | `19.65` | 122,460,000.00 USD | 0.00 USD | 514.44 USD | `-79.80%` | `26.18` |
| `Live` | `Long` | `20.05` | 122,460,000.00 USD | 0.00 USD | 897.84 USD | `-79.38%` | `44.78` |
| `Live` | `Long` | `20.15` | 122,460,000.00 USD | 0.00 USD | 730.44 USD | `-79.28%` | `36.25` |
| `Live` | `Long` | `20.55` | 122,460,000.00 USD | 0.00 USD | 12,190.00 USD | `-78.87%` | `593.31` |
| `Live` | `Long` | `20.85` | 122,450,000.00 USD | 0.00 USD | 689.93 USD | `-78.56%` | `33.09` |
| `Live` | `Long` | `20.95` | 122,450,000.00 USD | 0.00 USD | 1,030.00 USD | `-78.46%` | `49.01` |
| `Live` | `Long` | `21.35` | 122,440,000.00 USD | 0.00 USD | 1,410.00 USD | `-78.05%` | `65.89` |
| `Live` | `Long` | `21.45` | 122,440,000.00 USD | 0.00 USD | 407.55 USD | `-77.94%` | `19.00` |
| `Live` | `Long` | `21.75` | 122,440,000.00 USD | 0.00 USD | 4,630.00 USD | `-77.64%` | `212.70` |
| `Live` | `Long` | `21.95` | 122,440,000.00 USD | 0.00 USD | 1,100.00 USD | `-77.43%` | `50.00` |
| `Live` | `Long` | `22.05` | 122,440,000.00 USD | 0.00 USD | 4,740.00 USD | `-77.33%` | `215.00` |
| `Live` | `Long` | `22.35` | 122,430,000.00 USD | 0.00 USD | 2,040.00 USD | `-77.02%` | `91.12` |
| `Live` | `Long` | `22.65` | 122,430,000.00 USD | 0.00 USD | 112.12 USD | `-76.71%` | `4.95` |
| `Live` | `Long` | `22.95` | 122,430,000.00 USD | 0.00 USD | 1,150.00 USD | `-76.40%` | `50.00` |
| `Live` | `Long` | `23.15` | 122,430,000.00 USD | 0.00 USD | 11,820.00 USD | `-76.20%` | `510.51` |
| `Live` | `Long` | `23.25` | 122,420,000.00 USD | 0.00 USD | 838,990.00 USD | `-76.09%` | `36,085.73` |
| `Live` | `Long` | `23.35` | 121,580,000.00 USD | 0.00 USD | 46,700.00 USD | `-75.99%` | `2,000.00` |
| `Live` | `Long` | `23.45` | 121,530,000.00 USD | 0.00 USD | 1,380.00 USD | `-75.89%` | `58.86` |
| `Live` | `Long` | `23.65` | 121,530,000.00 USD | 0.00 USD | 9,830.00 USD | `-75.68%` | `415.58` |
| `Live` | `Long` | `23.75` | 121,520,000.00 USD | 0.00 USD | 1,570.00 USD | `-75.58%` | `65.92` |
| `Live` | `Long` | `23.85` | 121,520,000.00 USD | 0.00 USD | 9,590.00 USD | `-75.48%` | `402.03` |
| `Live` | `Long` | `24.25` | 121,510,000.00 USD | 0.00 USD | 248.81 USD | `-75.07%` | `10.26` |
| `Live` | `Long` | `24.65` | 121,510,000.00 USD | 0.00 USD | 882.72 USD | `-74.65%` | `35.81` |
| `Live` | `Long` | `24.75` | 121,510,000.00 USD | 0.00 USD | 976.88 USD | `-74.55%` | `39.47` |
| `Live` | `Long` | `24.85` | 121,510,000.00 USD | 0.00 USD | 5,360.00 USD | `-74.45%` | `215.80` |
| `Live` | `Long` | `24.95` | 121,500,000.00 USD | 0.00 USD | 25,960.00 USD | `-74.35%` | `1,040.52` |
| `Live` | `Long` | `25.05` | 121,480,000.00 USD | 0.00 USD | 1,250.00 USD | `-74.24%` | `50.00` |
| `Live` | `Long` | `25.15` | 121,470,000.00 USD | 0.00 USD | 3,270.00 USD | `-74.14%` | `130.00` |
| `Live` | `Long` | `25.45` | 121,470,000.00 USD | 0.00 USD | 106.64 USD | `-73.83%` | `4.19` |
| `Live` | `Long` | `25.65` | 121,470,000.00 USD | 0.00 USD | 147,500.00 USD | `-73.63%` | `5,750.44` |
| `Live` | `Long` | `25.75` | 121,320,000.00 USD | 0.00 USD | 309.00 USD | `-73.52%` | `12.00` |
| `Live` | `Long` | `25.95` | 121,320,000.00 USD | 0.00 USD | 3,320.00 USD | `-73.32%` | `127.84` |
| `Live` | `Long` | `26.05` | 121,320,000.00 USD | 0.00 USD | 5,730.00 USD | `-73.21%` | `220.00` |
| `Live` | `Long` | `26.25` | 121,310,000.00 USD | 0.00 USD | 136.24 USD | `-73.01%` | `5.19` |
| `Live` | `Long` | `26.35` | 121,310,000.00 USD | 0.00 USD | 366.79 USD | `-72.91%` | `13.92` |
| `Live` | `Long` | `26.45` | 121,310,000.00 USD | 0.00 USD | 1,710.00 USD | `-72.80%` | `64.72` |
| `Live` | `Long` | `26.65` | 121,310,000.00 USD | 0.00 USD | 265.17 USD | `-72.60%` | `9.95` |
| `Live` | `Long` | `26.95` | 121,310,000.00 USD | 0.00 USD | 10,110.00 USD | `-72.29%` | `375.19` |
| `Live` | `Long` | `27.35` | 121,300,000.00 USD | 0.00 USD | 332.30 USD | `-71.88%` | `12.15` |
| `Live` | `Long` | `27.75` | 121,300,000.00 USD | 0.00 USD | 1,190.00 USD | `-71.47%` | `43.06` |
| `Live` | `Long` | `27.85` | 121,300,000.00 USD | 0.00 USD | 14,980.00 USD | `-71.36%` | `538.03` |
| `Live` | `Long` | `27.95` | 121,280,000.00 USD | 0.00 USD | 154.28 USD | `-71.26%` | `5.52` |
| `Live` | `Long` | `28.05` | 121,280,000.00 USD | 0.00 USD | 2,740.00 USD | `-71.16%` | `97.63` |
| `Live` | `Long` | `28.15` | 121,280,000.00 USD | 0.00 USD | 271.37 USD | `-71.06%` | `9.64` |
| `Live` | `Long` | `28.25` | 121,280,000.00 USD | 0.00 USD | 755.12 USD | `-70.95%` | `26.73` |
| `Live` | `Long` | `28.35` | 121,280,000.00 USD | 0.00 USD | 6,200.00 USD | `-70.85%` | `218.55` |
| `Live` | `Long` | `28.45` | 121,270,000.00 USD | 0.00 USD | 113.80 USD | `-70.75%` | `4.00` |
| `Live` | `Long` | `29.05` | 121,270,000.00 USD | 0.00 USD | 11,030.00 USD | `-70.13%` | `379.80` |
| `Live` | `Long` | `29.15` | 121,260,000.00 USD | 0.00 USD | 15,270.00 USD | `-70.03%` | `523.99` |
| `Live` | `Long` | `29.25` | 121,250,000.00 USD | 0.00 USD | 88,480.00 USD | `-69.92%` | `3,025.00` |
| `Live` | `Long` | `29.35` | 121,160,000.00 USD | 0.00 USD | 9,900.00 USD | `-69.82%` | `337.19` |
| `Live` | `Long` | `29.45` | 121,150,000.00 USD | 0.00 USD | 151.96 USD | `-69.72%` | `5.16` |
| `Live` | `Long` | `29.75` | 121,150,000.00 USD | 0.00 USD | 33,370.00 USD | `-69.41%` | `1,121.64` |
| `Live` | `Long` | `29.95` | 121,120,000.00 USD | 0.00 USD | 18,960.00 USD | `-69.20%` | `633.00` |
| `Live` | `Long` | `30.05` | 121,100,000.00 USD | 0.00 USD | 5,410.00 USD | `-69.10%` | `179.99` |
| `Live` | `Long` | `30.15` | 121,090,000.00 USD | 0.00 USD | 50,050.00 USD | `-69.00%` | `1,660.00` |
| `Live` | `Long` | `30.25` | 121,040,000.00 USD | 0.00 USD | 47,800.00 USD | `-68.90%` | `1,580.00` |
| `Live` | `Long` | `30.35` | 120,990,000.00 USD | 0.00 USD | 4,230.00 USD | `-68.79%` | `139.36` |
| `Live` | `Long` | `30.55` | 120,990,000.00 USD | 0.00 USD | 889.01 USD | `-68.59%` | `29.10` |
| `Live` | `Long` | `30.65` | 120,990,000.00 USD | 0.00 USD | 5,250.00 USD | `-68.48%` | `171.41` |
| `Live` | `Long` | `30.85` | 120,980,000.00 USD | 0.00 USD | 157.64 USD | `-68.28%` | `5.11` |
| `Live` | `Long` | `31.05` | 120,980,000.00 USD | 0.00 USD | 621.00 USD | `-68.07%` | `20.00` |
| `Live` | `Long` | `31.15` | 120,980,000.00 USD | 0.00 USD | 178.49 USD | `-67.97%` | `5.73` |
| `Live` | `Long` | `31.35` | 120,980,000.00 USD | 0.00 USD | 6,120.00 USD | `-67.77%` | `195.31` |
| `Live` | `Long` | `31.45` | 120,980,000.00 USD | 0.00 USD | 278.33 USD | `-67.66%` | `8.85` |
| `Live` | `Long` | `31.55` | 120,980,000.00 USD | 0.00 USD | 162.17 USD | `-67.56%` | `5.14` |
| `Live` | `Long` | `31.75` | 120,980,000.00 USD | 0.00 USD | 11,130.00 USD | `-67.35%` | `350.67` |
| `Live` | `Long` | `32.15` | 120,970,000.00 USD | 0.00 USD | 796.68 USD | `-66.94%` | `24.78` |
| `Live` | `Long` | `32.25` | 120,960,000.00 USD | 0.00 USD | 173.50 USD | `-66.84%` | `5.38` |
| `Live` | `Long` | `32.45` | 120,960,000.00 USD | 0.00 USD | 861.87 USD | `-66.63%` | `26.56` |
| `Live` | `Long` | `32.65` | 120,960,000.00 USD | 0.00 USD | 1,150.00 USD | `-66.43%` | `35.37` |
| `Live` | `Long` | `32.85` | 120,960,000.00 USD | 0.00 USD | 562,480.00 USD | `-66.22%` | `17,122.80` |
| `Live` | `Long` | `32.95` | 120,400,000.00 USD | 0.00 USD | 1,160.00 USD | `-66.12%` | `35.22` |
| `Live` | `Long` | `33.05` | 120,400,000.00 USD | 0.00 USD | 5,420.00 USD | `-66.02%` | `164.04` |
| `Live` | `Long` | `33.25` | 120,390,000.00 USD | 0.00 USD | 39,900.00 USD | `-65.81%` | `1,200.00` |
| `Live` | `Long` | `33.65` | 120,350,000.00 USD | 0.00 USD | 1,830.00 USD | `-65.40%` | `54.25` |
| `Live` | `Long` | `33.75` | 120,350,000.00 USD | 0.00 USD | 72,700.00 USD | `-65.30%` | `2,154.01` |
| `Live` | `Long` | `34.05` | 120,280,000.00 USD | 0.00 USD | 3,650.00 USD | `-64.99%` | `107.30` |
| `Live` | `Long` | `34.15` | 120,270,000.00 USD | 0.00 USD | 19,990.00 USD | `-64.89%` | `585.29` |
| `Live` | `Long` | `34.25` | 120,250,000.00 USD | 0.00 USD | 799.05 USD | `-64.78%` | `23.33` |
| `Live` | `Long` | `34.35` | 120,250,000.00 USD | 0.00 USD | 982.41 USD | `-64.68%` | `28.60` |
| `Live` | `Long` | `34.55` | 120,250,000.00 USD | 0.00 USD | 17,270.00 USD | `-64.47%` | `500.00` |
| `Live` | `Long` | `34.65` | 120,240,000.00 USD | 0.00 USD | 486.14 USD | `-64.37%` | `14.03` |
| `Live` | `Long` | `34.75` | 120,240,000.00 USD | 0.00 USD | 143.86 USD | `-64.27%` | `4.14` |
| `Live` | `Long` | `34.85` | 120,240,000.00 USD | 0.00 USD | 3,660.00 USD | `-64.17%` | `104.94` |
| `Live` | `Long` | `34.95` | 120,230,000.00 USD | 0.00 USD | 6,620,000.00 USD | `-64.06%` | `189,472.50` |
| `Live` | `Long` | `35.15` | 113,610,000.00 USD | 0.00 USD | 441.84 USD | `-63.86%` | `12.57` |
| `Live` | `Long` | `35.25` | 113,610,000.00 USD | 0.00 USD | 1,360.00 USD | `-63.76%` | `38.48` |
| `Live` | `Long` | `35.65` | 113,610,000.00 USD | 0.00 USD | 3,040.00 USD | `-63.34%` | `85.14` |
| `Live` | `Long` | `35.75` | 113,600,000.00 USD | 0.00 USD | 4,840.00 USD | `-63.24%` | `135.34` |
| `Live` | `Long` | `35.85` | 113,600,000.00 USD | 0.00 USD | 9,050.00 USD | `-63.14%` | `252.39` |
| `Live` | `Long` | `35.95` | 113,590,000.00 USD | 0.00 USD | 557.94 USD | `-63.04%` | `15.52` |
| `Live` | `Long` | `36.05` | 113,590,000.00 USD | 0.00 USD | 5,070.00 USD | `-62.93%` | `140.61` |
| `Live` | `Long` | `36.15` | 113,590,000.00 USD | 0.00 USD | 531.41 USD | `-62.83%` | `14.70` |
| `Live` | `Long` | `36.25` | 113,580,000.00 USD | 0.00 USD | 2,630.00 USD | `-62.73%` | `72.56` |
| `Live` | `Long` | `36.35` | 113,580,000.00 USD | 0.00 USD | 5,630.00 USD | `-62.62%` | `155.00` |
| `Live` | `Long` | `36.45` | 113,580,000.00 USD | 0.00 USD | 42,810.00 USD | `-62.52%` | `1,174.37` |
| `Live` | `Long` | `36.55` | 113,530,000.00 USD | 0.00 USD | 50,420.00 USD | `-62.42%` | `1,379.57` |
| `Live` | `Long` | `36.75` | 113,480,000.00 USD | 0.00 USD | 748.97 USD | `-62.21%` | `20.38` |
| `Live` | `Long` | `36.85` | 113,480,000.00 USD | 0.00 USD | 1,470.00 USD | `-62.11%` | `39.85` |
| `Live` | `Long` | `36.95` | 113,480,000.00 USD | 0.00 USD | 1,660.00 USD | `-62.01%` | `45.00` |
| `Live` | `Long` | `37.15` | 113,480,000.00 USD | 0.00 USD | 146.37 USD | `-61.80%` | `3.94` |
| `Live` | `Long` | `37.25` | 113,480,000.00 USD | 0.00 USD | 373.62 USD | `-61.70%` | `10.03` |
| `Live` | `Long` | `37.35` | 113,480,000.00 USD | 0.00 USD | 38,140.00 USD | `-61.60%` | `1,021.13` |
| `Live` | `Long` | `37.55` | 113,440,000.00 USD | 0.00 USD | 144,730.00 USD | `-61.39%` | `3,854.39` |
| `Live` | `Long` | `37.65` | 113,300,000.00 USD | 0.00 USD | 4,610.00 USD | `-61.29%` | `122.49` |
| `Live` | `Long` | `37.75` | 113,290,000.00 USD | 0.00 USD | 636.09 USD | `-61.18%` | `16.85` |
| `Live` | `Long` | `37.85` | 113,290,000.00 USD | 0.00 USD | 819.83 USD | `-61.08%` | `21.66` |
| `Live` | `Long` | `37.95` | 113,290,000.00 USD | 0.00 USD | 5,000.00 USD | `-60.98%` | `131.84` |
| `Live` | `Long` | `38.05` | 113,280,000.00 USD | 0.00 USD | 1,490.00 USD | `-60.88%` | `39.05` |
| `Live` | `Long` | `38.25` | 113,280,000.00 USD | 0.00 USD | 480.42 USD | `-60.67%` | `12.56` |
| `Live` | `Long` | `38.35` | 113,280,000.00 USD | 0.00 USD | 287.63 USD | `-60.57%` | `7.50` |
| `Live` | `Long` | `38.45` | 113,280,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-60.46%` | `78,003.34` |
| `Live` | `Long` | `38.55` | 110,280,000.00 USD | 0.00 USD | 17,850.00 USD | `-60.36%` | `462.98` |
| `Live` | `Long` | `38.65` | 110,270,000.00 USD | 0.00 USD | 6,130.00 USD | `-60.26%` | `158.58` |
| `Live` | `Long` | `38.75` | 110,260,000.00 USD | 0.00 USD | 194,490.00 USD | `-60.16%` | `5,019.01` |
| `Live` | `Long` | `38.85` | 110,060,000.00 USD | 0.00 USD | 4,270.00 USD | `-60.05%` | `109.96` |
| `Live` | `Long` | `38.95` | 110,060,000.00 USD | 0.00 USD | 607.62 USD | `-59.95%` | `15.60` |
| `Live` | `Long` | `39.05` | 110,060,000.00 USD | 0.00 USD | 933,530.00 USD | `-59.85%` | `23,905.94` |
| `Live` | `Long` | `39.15` | 109,130,000.00 USD | 0.00 USD | 194.18 USD | `-59.75%` | `4.96` |
| `Live` | `Long` | `39.35` | 109,130,000.00 USD | 0.00 USD | 4,930.00 USD | `-59.54%` | `125.24` |
| `Live` | `Long` | `39.45` | 109,120,000.00 USD | 0.00 USD | 258.40 USD | `-59.44%` | `6.55` |
| `Live` | `Long` | `39.65` | 109,120,000.00 USD | 0.00 USD | 11,970.00 USD | `-59.23%` | `301.95` |
| `Live` | `Long` | `39.75` | 109,110,000.00 USD | 0.00 USD | 159.00 USD | `-59.13%` | `4.00` |
| `Live` | `Long` | `39.85` | 109,110,000.00 USD | 0.00 USD | 1,270.00 USD | `-59.03%` | `31.86` |
| `Live` | `Long` | `40.05` | 109,110,000.00 USD | 0.00 USD | 13,530.00 USD | `-58.82%` | `337.77` |
| `Live` | `Long` | `40.15` | 109,090,000.00 USD | 0.00 USD | 2,510.00 USD | `-58.72%` | `62.48` |
| `Live` | `Long` | `40.25` | 109,090,000.00 USD | 0.00 USD | 632.73 USD | `-58.61%` | `15.72` |
| `Live` | `Long` | `40.35` | 109,090,000.00 USD | 0.00 USD | 51,650.00 USD | `-58.51%` | `1,280.00` |
| `Live` | `Long` | `40.45` | 109,040,000.00 USD | 0.00 USD | 1,970.00 USD | `-58.41%` | `48.64` |
| `Live` | `Long` | `40.55` | 109,040,000.00 USD | 0.00 USD | 3,160.00 USD | `-58.31%` | `77.90` |
| `Live` | `Long` | `40.85` | 109,030,000.00 USD | 0.00 USD | 12,650.00 USD | `-58.00%` | `309.58` |
| `Live` | `Long` | `40.95` | 109,020,000.00 USD | 0.00 USD | 581.49 USD | `-57.89%` | `14.20` |
| `Live` | `Long` | `41.05` | 109,020,000.00 USD | 0.00 USD | 5,220.00 USD | `-57.79%` | `127.05` |
| `Live` | `Long` | `41.15` | 109,020,000.00 USD | 0.00 USD | 1,070.00 USD | `-57.69%` | `26.08` |
| `Live` | `Long` | `41.25` | 109,010,000.00 USD | 0.00 USD | 368.36 USD | `-57.59%` | `8.93` |
| `Live` | `Long` | `41.35` | 109,010,000.00 USD | 0.00 USD | 148.45 USD | `-57.48%` | `3.59` |
| `Live` | `Long` | `41.55` | 109,010,000.00 USD | 0.00 USD | 130.88 USD | `-57.28%` | `3.15` |
| `Live` | `Long` | `41.65` | 109,010,000.00 USD | 0.00 USD | 770.11 USD | `-57.17%` | `18.49` |
| `Live` | `Long` | `41.75` | 109,010,000.00 USD | 0.00 USD | 588.26 USD | `-57.07%` | `14.09` |
| `Live` | `Long` | `41.85` | 109,010,000.00 USD | 0.00 USD | 1,020.00 USD | `-56.97%` | `24.39` |
| `Live` | `Long` | `41.95` | 109,010,000.00 USD | 0.00 USD | 389,980.00 USD | `-56.87%` | `9,296.40` |
| `Live` | `Long` | `42.05` | 108,620,000.00 USD | 0.00 USD | 20,830.00 USD | `-56.76%` | `495.42` |
| `Live` | `Long` | `42.15` | 108,600,000.00 USD | 0.00 USD | 2,790.00 USD | `-56.66%` | `66.27` |
| `Live` | `Long` | `42.25` | 108,600,000.00 USD | 0.00 USD | 3,050.00 USD | `-56.56%` | `72.27` |
| `Live` | `Long` | `42.35` | 108,600,000.00 USD | 0.00 USD | 6,460.00 USD | `-56.45%` | `152.52` |
| `Live` | `Long` | `42.45` | 108,590,000.00 USD | 0.00 USD | 106.12 USD | `-56.35%` | `2.50` |
| `Live` | `Long` | `42.65` | 108,590,000.00 USD | 0.00 USD | 8,230.00 USD | `-56.15%` | `193.00` |
| `Live` | `Long` | `42.85` | 108,580,000.00 USD | 0.00 USD | 44,750.00 USD | `-55.94%` | `1,044.29` |
| `Live` | `Long` | `42.95` | 108,540,000.00 USD | 0.00 USD | 1,620.00 USD | `-55.84%` | `37.62` |
| `Live` | `Long` | `43.05` | 108,530,000.00 USD | 0.00 USD | 1,400.00 USD | `-55.73%` | `32.45` |
| `Live` | `Long` | `43.15` | 108,530,000.00 USD | 0.00 USD | 2,040.00 USD | `-55.63%` | `47.26` |
| `Live` | `Long` | `43.25` | 108,530,000.00 USD | 0.00 USD | 1,080.00 USD | `-55.53%` | `25.00` |
| `Live` | `Long` | `43.35` | 108,530,000.00 USD | 0.00 USD | 4,710.00 USD | `-55.43%` | `108.68` |
| `Live` | `Long` | `43.45` | 108,520,000.00 USD | 0.00 USD | 440.15 USD | `-55.32%` | `10.13` |
| `Live` | `Long` | `43.55` | 108,520,000.00 USD | 0.00 USD | 2,180.00 USD | `-55.22%` | `50.00` |
| `Live` | `Long` | `43.65` | 108,520,000.00 USD | 0.00 USD | 6,530.00 USD | `-55.12%` | `149.60` |
| `Live` | `Long` | `43.75` | 108,520,000.00 USD | 0.00 USD | 1,170,000.00 USD | `-55.02%` | `26,712.85` |
| `Live` | `Long` | `43.85` | 107,350,000.00 USD | 0.00 USD | 219,360.00 USD | `-54.91%` | `5,002.43` |
| `Live` | `Long` | `43.95` | 107,130,000.00 USD | 0.00 USD | 10,340.00 USD | `-54.81%` | `235.30` |
| `Live` | `Long` | `44.05` | 107,120,000.00 USD | 0.00 USD | 12,870.00 USD | `-54.71%` | `292.12` |
| `Live` | `Long` | `44.15` | 107,100,000.00 USD | 0.00 USD | 662,360.00 USD | `-54.60%` | `15,002.44` |
| `Live` | `Long` | `44.25` | 106,440,000.00 USD | 0.00 USD | 6,550.00 USD | `-54.50%` | `148.09` |
| `Live` | `Long` | `44.35` | 106,440,000.00 USD | 0.00 USD | 2,380.00 USD | `-54.40%` | `53.68` |
| `Live` | `Long` | `44.45` | 106,430,000.00 USD | 0.00 USD | 10,180.00 USD | `-54.30%` | `229.02` |
| `Live` | `Long` | `44.55` | 106,420,000.00 USD | 0.00 USD | 20,540.00 USD | `-54.19%` | `461.03` |
| `Live` | `Long` | `44.65` | 106,400,000.00 USD | 0.00 USD | 4,880.00 USD | `-54.09%` | `109.20` |
| `Live` | `Long` | `44.75` | 106,400,000.00 USD | 0.00 USD | 1,790.00 USD | `-53.99%` | `39.98` |
| `Live` | `Long` | `44.85` | 106,400,000.00 USD | 0.00 USD | 477.20 USD | `-53.88%` | `10.64` |
| `Live` | `Long` | `44.95` | 106,400,000.00 USD | 0.00 USD | 3,690,000.00 USD | `-53.78%` | `81,996.63` |
| `Live` | `Long` | `45.15` | 102,710,000.00 USD | 0.00 USD | 179.70 USD | `-53.58%` | `3.98` |
| `Live` | `Long` | `45.35` | 102,710,000.00 USD | 0.00 USD | 67,560.00 USD | `-53.37%` | `1,489.78` |
| `Live` | `Long` | `45.45` | 102,640,000.00 USD | 0.00 USD | 9,480.00 USD | `-53.27%` | `208.64` |
| `Live` | `Long` | `45.55` | 102,630,000.00 USD | 0.00 USD | 7,940.00 USD | `-53.16%` | `174.26` |
| `Live` | `Long` | `45.65` | 102,620,000.00 USD | 0.00 USD | 866.89 USD | `-53.06%` | `18.99` |
| `Live` | `Long` | `45.75` | 102,620,000.00 USD | 0.00 USD | 9,780.00 USD | `-52.96%` | `213.69` |
| `Live` | `Long` | `45.85` | 102,610,000.00 USD | 0.00 USD | 458.50 USD | `-52.86%` | `10.00` |
| `Live` | `Long` | `45.95` | 102,610,000.00 USD | 0.00 USD | 26,070.00 USD | `-52.75%` | `567.34` |
| `Live` | `Long` | `46.05` | 102,590,000.00 USD | 0.00 USD | 9,760.00 USD | `-52.65%` | `211.98` |
| `Live` | `Long` | `46.15` | 102,580,000.00 USD | 0.00 USD | 714.40 USD | `-52.55%` | `15.48` |
| `Live` | `Long` | `46.45` | 102,580,000.00 USD | 0.00 USD | 824.95 USD | `-52.24%` | `17.76` |
| `Live` | `Long` | `46.55` | 102,580,000.00 USD | 0.00 USD | 685.68 USD | `-52.14%` | `14.73` |
| `Live` | `Long` | `46.65` | 102,570,000.00 USD | 0.00 USD | 542.07 USD | `-52.03%` | `11.62` |
| `Live` | `Long` | `46.75` | 102,570,000.00 USD | 0.00 USD | 374.00 USD | `-51.93%` | `8.00` |
| `Live` | `Long` | `46.85` | 102,570,000.00 USD | 0.00 USD | 543.93 USD | `-51.83%` | `11.61` |
| `Live` | `Long` | `46.95` | 102,570,000.00 USD | 0.00 USD | 2,090.00 USD | `-51.72%` | `44.48` |
| `Live` | `Long` | `47.15` | 102,570,000.00 USD | 0.00 USD | 1,160.00 USD | `-51.52%` | `24.61` |
| `Live` | `Long` | `47.25` | 102,570,000.00 USD | 0.00 USD | 13,380.00 USD | `-51.42%` | `283.26` |
| `Live` | `Long` | `47.45` | 102,560,000.00 USD | 0.00 USD | 502.50 USD | `-51.21%` | `10.59` |
| `Live` | `Long` | `47.55` | 102,560,000.00 USD | 0.00 USD | 106.04 USD | `-51.11%` | `2.23` |
| `Live` | `Long` | `47.65` | 102,560,000.00 USD | 0.00 USD | 98,780.00 USD | `-51.01%` | `2,073.02` |
| `Live` | `Long` | `47.75` | 102,460,000.00 USD | 0.00 USD | 56,650.00 USD | `-50.90%` | `1,186.40` |
| `Live` | `Long` | `47.85` | 102,400,000.00 USD | 0.00 USD | 473.72 USD | `-50.80%` | `9.90` |
| `Live` | `Long` | `47.95` | 102,400,000.00 USD | 0.00 USD | 3,360.00 USD | `-50.70%` | `70.01` |
| `Live` | `Long` | `48.05` | 102,400,000.00 USD | 0.00 USD | 13,580.00 USD | `-50.59%` | `282.59` |
| `Live` | `Long` | `48.15` | 102,380,000.00 USD | 0.00 USD | 16,260.00 USD | `-50.49%` | `337.72` |
| `Live` | `Long` | `48.25` | 102,370,000.00 USD | 0.00 USD | 2,430.00 USD | `-50.39%` | `50.45` |
| `Live` | `Long` | `48.35` | 102,360,000.00 USD | 0.00 USD | 9,290.00 USD | `-50.29%` | `192.07` |
| `Live` | `Long` | `48.45` | 102,360,000.00 USD | 0.00 USD | 764,270.00 USD | `-50.18%` | `15,774.45` |
| `Live` | `Long` | `48.55` | 101,590,000.00 USD | 0.00 USD | 97,400.00 USD | `-50.08%` | `2,006.13` |
| `Live` | `Long` | `48.65` | 101,490,000.00 USD | 0.00 USD | 10,720.00 USD | `-49.98%` | `220.28` |
| `Live` | `Long` | `48.75` | 101,480,000.00 USD | 0.00 USD | 2,330.00 USD | `-49.87%` | `47.81` |
| `Live` | `Long` | `48.85` | 101,480,000.00 USD | 0.00 USD | 17,060.00 USD | `-49.77%` | `349.28` |
| `Live` | `Long` | `48.95` | 101,460,000.00 USD | 0.00 USD | 1,490.00 USD | `-49.67%` | `30.41` |
| `Live` | `Long` | `49.05` | 101,460,000.00 USD | 0.00 USD | 1,120.00 USD | `-49.57%` | `22.86` |
| `Live` | `Long` | `49.25` | 101,460,000.00 USD | 0.00 USD | 21,190.00 USD | `-49.36%` | `430.30` |
| `Live` | `Long` | `49.35` | 101,440,000.00 USD | 0.00 USD | 585.29 USD | `-49.26%` | `11.86` |
| `Live` | `Long` | `49.45` | 101,440,000.00 USD | 0.00 USD | 17,090.00 USD | `-49.15%` | `345.66` |
| `Live` | `Long` | `49.55` | 101,420,000.00 USD | 0.00 USD | 627.80 USD | `-49.05%` | `12.67` |
| `Live` | `Long` | `49.65` | 101,420,000.00 USD | 0.00 USD | 8,890.00 USD | `-48.95%` | `179.12` |
| `Live` | `Long` | `49.75` | 101,410,000.00 USD | 0.00 USD | 2,650.00 USD | `-48.85%` | `53.29` |
| `Live` | `Long` | `49.85` | 101,410,000.00 USD | 0.00 USD | 41,540.00 USD | `-48.74%` | `833.28` |
| `Live` | `Long` | `49.95` | 101,370,000.00 USD | 0.00 USD | 29,590.00 USD | `-48.64%` | `592.33` |
| `Live` | `Long` | `50.05` | 101,340,000.00 USD | 0.00 USD | 9,750.00 USD | `-48.54%` | `194.89` |
| `Live` | `Long` | `50.15` | 101,330,000.00 USD | 0.00 USD | 5,850.00 USD | `-48.43%` | `116.57` |
| `Live` | `Long` | `50.25` | 101,320,000.00 USD | 0.00 USD | 1,210,000.00 USD | `-48.33%` | `24,156.35` |
| `Live` | `Long` | `50.35` | 100,110,000.00 USD | 0.00 USD | 8,240.00 USD | `-48.23%` | `163.68` |
| `Live` | `Long` | `50.45` | 100,100,000.00 USD | 0.00 USD | 4,800.00 USD | `-48.13%` | `95.10` |
| `Live` | `Long` | `50.55` | 100,100,000.00 USD | 0.00 USD | 12,940.00 USD | `-48.02%` | `256.04` |
| `Live` | `Long` | `50.65` | 100,080,000.00 USD | 0.00 USD | 1,270.00 USD | `-47.92%` | `25.11` |
| `Live` | `Long` | `50.75` | 100,080,000.00 USD | 0.00 USD | 13,300.00 USD | `-47.82%` | `262.06` |
| `Live` | `Long` | `50.85` | 100,070,000.00 USD | 0.00 USD | 20,760.00 USD | `-47.71%` | `408.18` |
| `Live` | `Long` | `50.95` | 100,050,000.00 USD | 0.00 USD | 5,110.00 USD | `-47.61%` | `100.23` |
| `Live` | `Long` | `51.05` | 100,040,000.00 USD | 0.00 USD | 3,470.00 USD | `-47.51%` | `67.96` |
| `Live` | `Long` | `51.15` | 100,040,000.00 USD | 0.00 USD | 2,620.00 USD | `-47.41%` | `51.22` |
| `Live` | `Long` | `51.25` | 100,040,000.00 USD | 0.00 USD | 10,940.00 USD | `-47.30%` | `213.44` |
| `Live` | `Long` | `51.35` | 100,030,000.00 USD | 0.00 USD | 4,340.00 USD | `-47.20%` | `84.48` |
| `Live` | `Long` | `51.45` | 100,020,000.00 USD | 0.00 USD | 3,920.00 USD | `-47.10%` | `76.22` |
| `Live` | `Long` | `51.55` | 100,020,000.00 USD | 0.00 USD | 135,270.00 USD | `-47.00%` | `2,623.99` |
| `Live` | `Long` | `51.65` | 99,880,000.00 USD | 0.00 USD | 4,290.00 USD | `-46.89%` | `83.14` |
| `Live` | `Long` | `51.75` | 99,880,000.00 USD | 0.00 USD | 24,770.00 USD | `-46.79%` | `478.71` |
| `Live` | `Long` | `51.85` | 99,850,000.00 USD | 0.00 USD | 46,110.00 USD | `-46.69%` | `889.34` |
| `Live` | `Long` | `51.95` | 99,810,000.00 USD | 0.00 USD | 469,860.00 USD | `-46.58%` | `9,044.37` |
| `Live` | `Long` | `52.05` | 99,340,000.00 USD | 0.00 USD | 31,030.00 USD | `-46.48%` | `596.12` |
| `Live` | `Long` | `52.15` | 99,310,000.00 USD | 0.00 USD | 112,570.00 USD | `-46.38%` | `2,158.54` |
| `Live` | `Long` | `52.25` | 99,190,000.00 USD | 0.00 USD | 12,600.00 USD | `-46.28%` | `241.08` |
| `Live` | `Long` | `52.35` | 99,180,000.00 USD | 0.00 USD | 2,160.00 USD | `-46.17%` | `41.28` |
| `Live` | `Long` | `52.45` | 99,180,000.00 USD | 0.00 USD | 43,640.00 USD | `-46.07%` | `832.10` |
| `Live` | `Long` | `52.55` | 99,140,000.00 USD | 0.00 USD | 11,110.00 USD | `-45.97%` | `211.45` |
| `Live` | `Long` | `52.65` | 99,120,000.00 USD | 0.00 USD | 9,300.00 USD | `-45.86%` | `176.71` |
| `Live` | `Long` | `52.75` | 99,120,000.00 USD | 0.00 USD | 3,180.00 USD | `-45.76%` | `60.32` |
| `Live` | `Long` | `52.85` | 99,110,000.00 USD | 0.00 USD | 9,370.00 USD | `-45.66%` | `177.38` |
| `Live` | `Long` | `52.95` | 99,100,000.00 USD | 0.00 USD | 6,120.00 USD | `-45.56%` | `115.56` |
| `Live` | `Long` | `53.05` | 99,100,000.00 USD | 0.00 USD | 5,120.00 USD | `-45.45%` | `96.59` |
| `Live` | `Long` | `53.15` | 99,090,000.00 USD | 0.00 USD | 3,340.00 USD | `-45.35%` | `62.76` |
| `Live` | `Long` | `53.25` | 99,090,000.00 USD | 0.00 USD | 24,120.00 USD | `-45.25%` | `452.99` |
| `Live` | `Long` | `53.35` | 99,060,000.00 USD | 0.00 USD | 2,130.00 USD | `-45.14%` | `39.99` |
| `Live` | `Long` | `53.45` | 99,060,000.00 USD | 0.00 USD | 52,360.00 USD | `-45.04%` | `979.55` |
| `Live` | `Long` | `53.55` | 99,010,000.00 USD | 0.00 USD | 44,480.00 USD | `-44.94%` | `830.55` |
| `Live` | `Long` | `53.65` | 98,960,000.00 USD | 0.00 USD | 230.70 USD | `-44.84%` | `4.30` |
| `Live` | `Long` | `53.75` | 98,960,000.00 USD | 0.00 USD | 3,600.00 USD | `-44.73%` | `67.00` |
| `Live` | `Long` | `53.85` | 98,960,000.00 USD | 0.00 USD | 19,810.00 USD | `-44.63%` | `367.96` |
| `Live` | `Long` | `53.95` | 98,940,000.00 USD | 0.00 USD | 58,760.00 USD | `-44.53%` | `1,089.22` |
| `Live` | `Long` | `54.05` | 98,880,000.00 USD | 0.00 USD | 350.78 USD | `-44.42%` | `6.49` |
| `Live` | `Long` | `54.15` | 98,880,000.00 USD | 0.00 USD | 14,640.00 USD | `-44.32%` | `270.39` |
| `Live` | `Long` | `54.25` | 98,870,000.00 USD | 0.00 USD | 6,660.00 USD | `-44.22%` | `122.83` |
| `Live` | `Long` | `54.35` | 98,860,000.00 USD | 0.00 USD | 11,720.00 USD | `-44.12%` | `215.69` |
| `Live` | `Long` | `54.45` | 98,850,000.00 USD | 0.00 USD | 1,410.00 USD | `-44.01%` | `25.83` |
| `Live` | `Long` | `54.55` | 98,850,000.00 USD | 0.00 USD | 61,670.00 USD | `-43.91%` | `1,130.45` |
| `Live` | `Long` | `54.65` | 98,790,000.00 USD | 0.00 USD | 10,920.00 USD | `-43.81%` | `199.82` |
| `Live` | `Long` | `54.75` | 98,780,000.00 USD | 0.00 USD | 15,140.00 USD | `-43.70%` | `276.50` |
| `Live` | `Long` | `54.85` | 98,760,000.00 USD | 0.00 USD | 861,080.00 USD | `-43.60%` | `15,698.74` |
| `Live` | `Long` | `54.95` | 97,900,000.00 USD | 0.00 USD | 142,480.00 USD | `-43.50%` | `2,592.93` |
| `Live` | `Long` | `55.05` | 97,760,000.00 USD | 0.00 USD | 552.70 USD | `-43.40%` | `10.04` |
| `Live` | `Long` | `55.15` | 97,760,000.00 USD | 0.00 USD | 665.66 USD | `-43.29%` | `12.07` |
| `Live` | `Long` | `55.25` | 97,760,000.00 USD | 0.00 USD | 2,010.00 USD | `-43.19%` | `36.31` |
| `Live` | `Long` | `55.35` | 97,750,000.00 USD | 0.00 USD | 9,920.00 USD | `-43.09%` | `179.16` |
| `Live` | `Long` | `55.45` | 97,740,000.00 USD | 0.00 USD | 5,620.00 USD | `-42.98%` | `101.35` |
| `Live` | `Long` | `55.55` | 97,740,000.00 USD | 0.00 USD | 145,530.00 USD | `-42.88%` | `2,619.78` |
| `Live` | `Long` | `55.65` | 97,590,000.00 USD | 0.00 USD | 11,490.00 USD | `-42.78%` | `206.41` |
| `Live` | `Long` | `55.75` | 97,580,000.00 USD | 0.00 USD | 91,720.00 USD | `-42.68%` | `1,645.25` |
| `Live` | `Long` | `55.85` | 97,490,000.00 USD | 0.00 USD | 18,770.00 USD | `-42.57%` | `336.16` |
| `Live` | `Long` | `55.95` | 97,470,000.00 USD | 0.00 USD | 7,050.00 USD | `-42.47%` | `125.95` |
| `Live` | `Long` | `56.05` | 97,460,000.00 USD | 0.00 USD | 5,640.00 USD | `-42.37%` | `100.70` |
| `Live` | `Long` | `56.15` | 97,460,000.00 USD | 0.00 USD | 38,930.00 USD | `-42.27%` | `693.27` |
| `Live` | `Long` | `56.25` | 97,420,000.00 USD | 0.00 USD | 13,300.00 USD | `-42.16%` | `236.52` |
| `Live` | `Long` | `56.35` | 97,410,000.00 USD | 0.00 USD | 12,890.00 USD | `-42.06%` | `228.82` |
| `Live` | `Long` | `56.45` | 97,390,000.00 USD | 0.00 USD | 13,320.00 USD | `-41.96%` | `235.94` |
| `Live` | `Long` | `56.55` | 97,380,000.00 USD | 0.00 USD | 4,730.00 USD | `-41.85%` | `83.63` |
| `Live` | `Long` | `56.65` | 97,370,000.00 USD | 0.00 USD | 3,190.00 USD | `-41.75%` | `56.32` |
| `Live` | `Long` | `56.75` | 97,370,000.00 USD | 0.00 USD | 9,410.00 USD | `-41.65%` | `165.87` |
| `Live` | `Long` | `56.85` | 97,360,000.00 USD | 0.00 USD | 28,550.00 USD | `-41.55%` | `502.16` |
| `Live` | `Long` | `56.95` | 97,330,000.00 USD | 0.00 USD | 14,320.00 USD | `-41.44%` | `251.38` |
| `Live` | `Long` | `57.05` | 97,320,000.00 USD | 0.00 USD | 2,770,000.00 USD | `-41.34%` | `48,630.05` |
| `Live` | `Long` | `57.15` | 94,540,000.00 USD | 0.00 USD | 5,380.00 USD | `-41.24%` | `94.22` |
| `Live` | `Long` | `57.25` | 94,540,000.00 USD | 0.00 USD | 2,470.00 USD | `-41.13%` | `43.18` |
| `Live` | `Long` | `57.35` | 94,540,000.00 USD | 0.00 USD | 7,120.00 USD | `-41.03%` | `124.09` |
| `Live` | `Long` | `57.45` | 94,530,000.00 USD | 0.00 USD | 19,200.00 USD | `-40.93%` | `334.25` |
| `Live` | `Long` | `57.55` | 94,510,000.00 USD | 0.00 USD | 8,510.00 USD | `-40.83%` | `147.80` |
| `Live` | `Long` | `57.65` | 94,500,000.00 USD | 0.00 USD | 13,030.00 USD | `-40.72%` | `226.05` |
| `Live` | `Long` | `57.75` | 94,490,000.00 USD | 0.00 USD | 8,290.00 USD | `-40.62%` | `143.57` |
| `Live` | `Long` | `57.85` | 94,480,000.00 USD | 0.00 USD | 22,150.00 USD | `-40.52%` | `382.92` |
| `Live` | `Long` | `57.95` | 94,460,000.00 USD | 0.00 USD | 10,870.00 USD | `-40.41%` | `187.54` |
| `Live` | `Long` | `58.05` | 94,450,000.00 USD | 0.00 USD | 39,250.00 USD | `-40.31%` | `676.10` |
| `Live` | `Long` | `58.15` | 94,410,000.00 USD | 0.00 USD | 125,030.00 USD | `-40.21%` | `2,150.08` |
| `Live` | `Long` | `58.25` | 94,280,000.00 USD | 0.00 USD | 9,870.00 USD | `-40.11%` | `169.44` |
| `Live` | `Long` | `58.35` | 94,270,000.00 USD | 0.00 USD | 30,840.00 USD | `-40.00%` | `528.48` |
| `Live` | `Long` | `58.45` | 94,240,000.00 USD | 0.00 USD | 697.31 USD | `-39.90%` | `11.93` |
| `Live` | `Long` | `58.55` | 94,240,000.00 USD | 0.00 USD | 4,680.00 USD | `-39.80%` | `79.85` |
| `Live` | `Long` | `58.65` | 94,240,000.00 USD | 0.00 USD | 4,690.00 USD | `-39.69%` | `79.96` |
| `Live` | `Long` | `58.75` | 94,230,000.00 USD | 0.00 USD | 14,500.00 USD | `-39.59%` | `246.76` |
| `Live` | `Long` | `58.85` | 94,220,000.00 USD | 0.00 USD | 13,970.00 USD | `-39.49%` | `237.34` |
| `Live` | `Long` | `58.95` | 94,200,000.00 USD | 0.00 USD | 31,930.00 USD | `-39.39%` | `541.62` |
| `Live` | `Long` | `59.05` | 94,170,000.00 USD | 0.00 USD | 65,660.00 USD | `-39.28%` | `1,112.00` |
| `Live` | `Long` | `59.15` | 94,110,000.00 USD | 0.00 USD | 2,370,000.00 USD | `-39.18%` | `40,080.44` |
| `Live` | `Long` | `59.25` | 91,740,000.00 USD | 0.00 USD | 1,990.00 USD | `-39.08%` | `33.57` |
| `Live` | `Long` | `59.35` | 91,730,000.00 USD | 0.00 USD | 28,500.00 USD | `-38.97%` | `480.18` |
| `Live` | `Long` | `59.45` | 91,710,000.00 USD | 0.00 USD | 4,830.00 USD | `-38.87%` | `81.29` |
| `Live` | `Long` | `59.55` | 91,700,000.00 USD | 0.00 USD | 26,470.00 USD | `-38.77%` | `444.57` |
| `Live` | `Long` | `59.65` | 91,670,000.00 USD | 0.00 USD | 3,640.00 USD | `-38.67%` | `61.07` |
| `Live` | `Long` | `59.75` | 91,670,000.00 USD | 0.00 USD | 13,290.00 USD | `-38.56%` | `222.40` |
| `Live` | `Long` | `59.85` | 91,660,000.00 USD | 0.00 USD | 28,800.00 USD | `-38.46%` | `481.25` |
| `Live` | `Long` | `59.95` | 91,630,000.00 USD | 0.00 USD | 38,940.00 USD | `-38.36%` | `649.55` |
| `Live` | `Long` | `60.05` | 91,590,000.00 USD | 0.00 USD | 55,060.00 USD | `-38.26%` | `916.86` |
| `Live` | `Long` | `60.15` | 91,530,000.00 USD | 0.00 USD | 35,380.00 USD | `-38.15%` | `588.24` |
| `Live` | `Long` | `60.25` | 91,500,000.00 USD | 0.00 USD | 20,380.00 USD | `-38.05%` | `338.29` |
| `Live` | `Long` | `60.35` | 91,480,000.00 USD | 0.00 USD | 4,540.00 USD | `-37.95%` | `75.26` |
| `Live` | `Long` | `60.55` | 91,470,000.00 USD | 0.00 USD | 10,140.00 USD | `-37.74%` | `167.46` |
| `Live` | `Long` | `60.65` | 91,460,000.00 USD | 0.00 USD | 711.42 USD | `-37.64%` | `11.73` |
| `Live` | `Long` | `60.75` | 91,460,000.00 USD | 0.00 USD | 5,300.00 USD | `-37.54%` | `87.26` |
| `Live` | `Long` | `60.85` | 91,460,000.00 USD | 0.00 USD | 33,430.00 USD | `-37.43%` | `549.34` |
| `Live` | `Long` | `60.95` | 91,420,000.00 USD | 0.00 USD | 57,890.00 USD | `-37.33%` | `949.84` |
| `Live` | `Long` | `61.05` | 91,370,000.00 USD | 0.00 USD | 4,520.00 USD | `-37.23%` | `74.10` |
| `Live` | `Long` | `61.15` | 91,360,000.00 USD | 0.00 USD | 5,900.00 USD | `-37.12%` | `96.47` |
| `Live` | `Long` | `61.25` | 91,360,000.00 USD | 0.00 USD | 4,630.00 USD | `-37.02%` | `75.67` |
| `Live` | `Long` | `61.35` | 91,350,000.00 USD | 0.00 USD | 11,660.00 USD | `-36.92%` | `189.99` |
| `Live` | `Long` | `61.45` | 91,340,000.00 USD | 0.00 USD | 20,920.00 USD | `-36.82%` | `340.48` |
| `Live` | `Long` | `61.55` | 91,320,000.00 USD | 0.00 USD | 651.20 USD | `-36.71%` | `10.58` |
| `Live` | `Long` | `61.65` | 91,320,000.00 USD | 0.00 USD | 19,270.00 USD | `-36.61%` | `312.58` |
| `Live` | `Long` | `61.75` | 91,300,000.00 USD | 0.00 USD | 109,820.00 USD | `-36.51%` | `1,778.54` |
| `Live` | `Long` | `61.85` | 91,190,000.00 USD | 0.00 USD | 24,050.00 USD | `-36.40%` | `388.89` |
| `Live` | `Long` | `61.95` | 91,160,000.00 USD | 0.00 USD | 4,680.00 USD | `-36.30%` | `75.54` |
| `Live` | `Long` | `62.05` | 91,160,000.00 USD | 0.00 USD | 53,350.00 USD | `-36.20%` | `859.82` |
| `Live` | `Long` | `62.15` | 91,110,000.00 USD | 0.00 USD | 25,350.00 USD | `-36.10%` | `407.88` |
| `Live` | `Long` | `62.25` | 91,080,000.00 USD | 0.00 USD | 47,880.00 USD | `-35.99%` | `769.12` |
| `Live` | `Long` | `62.35` | 91,030,000.00 USD | 0.00 USD | 20,220.00 USD | `-35.89%` | `324.29` |
| `Live` | `Long` | `62.45` | 91,010,000.00 USD | 0.00 USD | 67,320.00 USD | `-35.79%` | `1,077.96` |
| `Live` | `Long` | `62.55` | 90,950,000.00 USD | 0.00 USD | 135,200.00 USD | `-35.68%` | `2,161.40` |
| `Live` | `Long` | `62.65` | 90,810,000.00 USD | 0.00 USD | 2,630.00 USD | `-35.58%` | `41.99` |
| `Live` | `Long` | `62.75` | 90,810,000.00 USD | 0.00 USD | 3,140.00 USD | `-35.48%` | `49.97` |
| `Live` | `Long` | `62.85` | 90,810,000.00 USD | 0.00 USD | 31,310.00 USD | `-35.38%` | `498.17` |
| `Live` | `Long` | `62.95` | 90,770,000.00 USD | 0.00 USD | 9,610.00 USD | `-35.27%` | `152.71` |
| `Live` | `Long` | `63.05` | 90,760,000.00 USD | 0.00 USD | 16,070.00 USD | `-35.17%` | `254.91` |
| `Live` | `Long` | `63.15` | 90,750,000.00 USD | 0.00 USD | 82,790.00 USD | `-35.07%` | `1,311.05` |
| `Live` | `Long` | `63.25` | 90,670,000.00 USD | 0.00 USD | 32,790.00 USD | `-34.96%` | `518.43` |
| `Live` | `Long` | `63.35` | 90,630,000.00 USD | 0.00 USD | 1,200.00 USD | `-34.86%` | `18.99` |
| `Live` | `Long` | `63.45` | 90,630,000.00 USD | 0.00 USD | 291.24 USD | `-34.76%` | `4.59` |
| `Live` | `Long` | `63.55` | 90,630,000.00 USD | 0.00 USD | 49,290.00 USD | `-34.66%` | `775.56` |
| `Live` | `Long` | `63.65` | 90,580,000.00 USD | 0.00 USD | 416.27 USD | `-34.55%` | `6.54` |
| `Live` | `Long` | `63.75` | 90,580,000.00 USD | 0.00 USD | 32,540.00 USD | `-34.45%` | `510.36` |
| `Live` | `Long` | `63.85` | 90,550,000.00 USD | 0.00 USD | 37,610.00 USD | `-34.35%` | `589.03` |
| `Live` | `Long` | `63.95` | 90,510,000.00 USD | 0.00 USD | 19,530.00 USD | `-34.25%` | `305.33` |
| `Live` | `Long` | `64.05` | 90,490,000.00 USD | 0.00 USD | 796.78 USD | `-34.14%` | `12.44` |
| `Live` | `Long` | `64.15` | 90,490,000.00 USD | 0.00 USD | 35,280.00 USD | `-34.04%` | `550.00` |
| `Live` | `Long` | `64.25` | 90,460,000.00 USD | 0.00 USD | 5,090.00 USD | `-33.94%` | `79.27` |
| `Live` | `Long` | `64.35` | 90,450,000.00 USD | 0.00 USD | 875.16 USD | `-33.83%` | `13.60` |
| `Live` | `Long` | `64.45` | 90,450,000.00 USD | 0.00 USD | 4,310.00 USD | `-33.73%` | `66.88` |
| `Live` | `Long` | `64.55` | 90,450,000.00 USD | 0.00 USD | 579.66 USD | `-33.63%` | `8.98` |
| `Live` | `Long` | `64.65` | 90,440,000.00 USD | 0.00 USD | 2,220.00 USD | `-33.53%` | `34.28` |
| `Live` | `Long` | `64.75` | 90,440,000.00 USD | 0.00 USD | 16,300.00 USD | `-33.42%` | `251.76` |
| `Live` | `Long` | `64.85` | 90,430,000.00 USD | 0.00 USD | 396.23 USD | `-33.32%` | `6.11` |
| `Live` | `Long` | `64.95` | 90,430,000.00 USD | 0.00 USD | 209.79 USD | `-33.22%` | `3.23` |
| `Live` | `Long` | `65.05` | 90,430,000.00 USD | 0.00 USD | 265,650.00 USD | `-33.11%` | `4,083.76` |
| `Live` | `Long` | `65.15` | 90,160,000.00 USD | 0.00 USD | 108,780.00 USD | `-33.01%` | `1,669.64` |
| `Live` | `Long` | `65.25` | 90,050,000.00 USD | 0.00 USD | 13,060.00 USD | `-32.91%` | `200.16` |
| `Live` | `Long` | `65.35` | 90,040,000.00 USD | 0.00 USD | 39,610.00 USD | `-32.81%` | `606.07` |
| `Live` | `Long` | `65.45` | 90,000,000.00 USD | 0.00 USD | 3,450.00 USD | `-32.70%` | `52.67` |
| `Live` | `Long` | `65.55` | 89,990,000.00 USD | 0.00 USD | 10,470.00 USD | `-32.60%` | `159.76` |
| `Live` | `Long` | `65.65` | 89,980,000.00 USD | 0.00 USD | 58,270.00 USD | `-32.50%` | `887.62` |
| `Live` | `Long` | `65.75` | 89,930,000.00 USD | 0.00 USD | 5,050.00 USD | `-32.39%` | `76.84` |
| `Live` | `Long` | `65.85` | 89,920,000.00 USD | 0.00 USD | 1,300.00 USD | `-32.29%` | `19.81` |
| `Live` | `Long` | `65.95` | 89,920,000.00 USD | 0.00 USD | 5,780.00 USD | `-32.19%` | `87.71` |
| `Live` | `Long` | `66.05` | 89,910,000.00 USD | 0.00 USD | 6,490.00 USD | `-32.09%` | `98.25` |
| `Live` | `Long` | `66.15` | 89,910,000.00 USD | 0.00 USD | 20,170.00 USD | `-31.98%` | `304.96` |
| `Live` | `Long` | `66.25` | 89,890,000.00 USD | 0.00 USD | 14,930.00 USD | `-31.88%` | `225.38` |
| `Live` | `Long` | `66.35` | 89,870,000.00 USD | 0.00 USD | 1,600.00 USD | `-31.78%` | `24.08` |
| `Live` | `Long` | `66.45` | 89,870,000.00 USD | 0.00 USD | 75,010.00 USD | `-31.67%` | `1,128.89` |
| `Live` | `Long` | `66.55` | 89,800,000.00 USD | 0.00 USD | 52,610.00 USD | `-31.57%` | `790.60` |
| `Live` | `Long` | `66.65` | 89,740,000.00 USD | 0.00 USD | 40,710.00 USD | `-31.47%` | `610.73` |
| `Live` | `Long` | `66.75` | 89,700,000.00 USD | 0.00 USD | 43,110.00 USD | `-31.37%` | `645.77` |
| `Live` | `Long` | `66.85` | 89,660,000.00 USD | 0.00 USD | 20,000.00 USD | `-31.26%` | `299.15` |
| `Live` | `Long` | `66.95` | 89,640,000.00 USD | 0.00 USD | 937.30 USD | `-31.16%` | `14.00` |
| `Live` | `Long` | `67.05` | 89,640,000.00 USD | 0.00 USD | 46,770.00 USD | `-31.06%` | `697.58` |
| `Live` | `Long` | `67.15` | 89,590,000.00 USD | 0.00 USD | 3,620.00 USD | `-30.95%` | `53.94` |
| `Live` | `Long` | `67.25` | 89,590,000.00 USD | 0.00 USD | 248.83 USD | `-30.85%` | `3.70` |
| `Live` | `Long` | `67.35` | 89,590,000.00 USD | 0.00 USD | 1,880.00 USD | `-30.75%` | `27.84` |
| `Live` | `Long` | `67.45` | 89,590,000.00 USD | 0.00 USD | 22,250.00 USD | `-30.65%` | `329.80` |
| `Live` | `Long` | `67.55` | 89,560,000.00 USD | 0.00 USD | 53,380.00 USD | `-30.54%` | `790.17` |
| `Live` | `Long` | `67.65` | 89,510,000.00 USD | 0.00 USD | 129,430.00 USD | `-30.44%` | `1,913.17` |
| `Live` | `Long` | `67.75` | 89,380,000.00 USD | 0.00 USD | 30,820.00 USD | `-30.34%` | `454.97` |
| `Live` | `Long` | `67.85` | 89,350,000.00 USD | 0.00 USD | 28,740.00 USD | `-30.23%` | `423.64` |
| `Live` | `Long` | `68.05` | 89,320,000.00 USD | 0.00 USD | 11,140.00 USD | `-30.03%` | `163.65` |
| `Live` | `Long` | `68.15` | 89,310,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-29.93%` | `550,166.69` |
| `Live` | `Long` | `68.25` | 51,820,000.00 USD | 0.00 USD | 17,190.00 USD | `-29.82%` | `251.82` |
| `Live` | `Long` | `68.35` | 51,800,000.00 USD | 0.00 USD | 2,860.00 USD | `-29.72%` | `41.82` |
| `Live` | `Long` | `68.45` | 51,800,000.00 USD | 0.00 USD | 18,610.00 USD | `-29.62%` | `271.81` |
| `Live` | `Long` | `68.55` | 51,780,000.00 USD | 0.00 USD | 1,380,000.00 USD | `-29.52%` | `20,078.78` |
| `Live` | `Long` | `68.65` | 50,400,000.00 USD | 0.00 USD | 7,740.00 USD | `-29.41%` | `112.73` |
| `Live` | `Long` | `68.75` | 50,390,000.00 USD | 0.00 USD | 151,610.00 USD | `-29.31%` | `2,205.18` |
| `Live` | `Long` | `68.85` | 50,240,000.00 USD | 0.00 USD | 417,630.00 USD | `-29.21%` | `6,065.83` |
| `Live` | `Long` | `68.95` | 49,820,000.00 USD | 0.00 USD | 46,330.00 USD | `-29.10%` | `671.97` |
| `Live` | `Long` | `69.05` | 49,780,000.00 USD | 0.00 USD | 786,930.00 USD | `-29.00%` | `11,396.58` |
| `Live` | `Long` | `69.15` | 48,990,000.00 USD | 0.00 USD | 29,000.00 USD | `-28.90%` | `419.40` |
| `Live` | `Long` | `69.25` | 48,960,000.00 USD | 0.00 USD | 20,140.00 USD | `-28.80%` | `290.80` |
| `Live` | `Long` | `69.35` | 48,940,000.00 USD | 0.00 USD | 12,490,000.00 USD | `-28.69%` | `180,144.14` |
| `Live` | `Long` | `69.45` | 36,450,000.00 USD | 0.00 USD | 264,310.00 USD | `-28.59%` | `3,805.73` |
| `Live` | `Long` | `69.55` | 36,180,000.00 USD | 0.00 USD | 10,170.00 USD | `-28.49%` | `146.29` |
| `Live` | `Long` | `69.65` | 36,170,000.00 USD | 0.00 USD | 5,280.00 USD | `-28.38%` | `75.77` |
| `Live` | `Long` | `69.75` | 36,170,000.00 USD | 0.00 USD | 212,170.00 USD | `-28.28%` | `3,041.83` |
| `Live` | `Long` | `69.85` | 35,960,000.00 USD | 0.00 USD | 8,590.00 USD | `-28.18%` | `122.91` |
| `Live` | `Long` | `69.95` | 35,950,000.00 USD | 0.00 USD | 8,800.00 USD | `-28.08%` | `125.81` |
| `Live` | `Long` | `70.05` | 35,940,000.00 USD | 0.00 USD | 496,560.00 USD | `-27.97%` | `7,088.66` |
| `Live` | `Long` | `70.15` | 35,440,000.00 USD | 0.00 USD | 4,120.00 USD | `-27.87%` | `58.77` |
| `Live` | `Long` | `70.25` | 35,440,000.00 USD | 0.00 USD | 72,890.00 USD | `-27.77%` | `1,037.54` |
| `Live` | `Long` | `70.35` | 35,370,000.00 USD | 0.00 USD | 2,140,000.00 USD | `-27.66%` | `30,414.81` |
| `Live` | `Long` | `70.45` | 33,230,000.00 USD | 0.00 USD | 113,800.00 USD | `-27.56%` | `1,615.34` |
| `Live` | `Long` | `70.55` | 33,110,000.00 USD | 0.00 USD | 458.58 USD | `-27.46%` | `6.50` |
| `Live` | `Long` | `70.65` | 33,110,000.00 USD | 0.00 USD | 49,010.00 USD | `-27.36%` | `693.67` |
| `Live` | `Long` | `70.75` | 33,060,000.00 USD | 0.00 USD | 10,240.00 USD | `-27.25%` | `144.80` |
| `Live` | `Long` | `70.85` | 33,050,000.00 USD | 0.00 USD | 15,430.00 USD | `-27.15%` | `217.72` |
| `Live` | `Long` | `70.95` | 33,040,000.00 USD | 0.00 USD | 7,010.00 USD | `-27.05%` | `98.87` |
| `Live` | `Long` | `71.05` | 33,030,000.00 USD | 0.00 USD | 31,630.00 USD | `-26.94%` | `445.17` |
| `Live` | `Long` | `71.15` | 33,000,000.00 USD | 0.00 USD | 69,160.00 USD | `-26.84%` | `972.07` |
| `Live` | `Long` | `71.25` | 32,930,000.00 USD | 0.00 USD | 1,080,000.00 USD | `-26.74%` | `15,123.14` |
| `Live` | `Long` | `71.35` | 31,850,000.00 USD | 0.00 USD | 15,910.00 USD | `-26.64%` | `223.05` |
| `Live` | `Long` | `71.45` | 31,840,000.00 USD | 0.00 USD | 31,640.00 USD | `-26.53%` | `442.82` |
| `Live` | `Long` | `71.55` | 31,800,000.00 USD | 0.00 USD | 41,780.00 USD | `-26.43%` | `583.97` |
| `Live` | `Long` | `71.65` | 31,760,000.00 USD | 0.00 USD | 894.91 USD | `-26.33%` | `12.49` |
| `Live` | `Long` | `71.75` | 31,760,000.00 USD | 0.00 USD | 30,200.00 USD | `-26.22%` | `420.90` |
| `Live` | `Long` | `71.85` | 31,730,000.00 USD | 0.00 USD | 2,130.00 USD | `-26.12%` | `29.71` |
| `Live` | `Long` | `71.95` | 31,730,000.00 USD | 0.00 USD | 12,860.00 USD | `-26.02%` | `178.70` |
| `Live` | `Long` | `72.05` | 31,720,000.00 USD | 0.00 USD | 42,610.00 USD | `-25.92%` | `591.41` |
| `Live` | `Long` | `72.15` | 31,670,000.00 USD | 0.00 USD | 130,700.00 USD | `-25.81%` | `1,811.56` |
| `Live` | `Long` | `72.25` | 31,540,000.00 USD | 0.00 USD | 259,270.00 USD | `-25.71%` | `3,588.45` |
| `Live` | `Long` | `72.35` | 31,280,000.00 USD | 0.00 USD | 29,390.00 USD | `-25.61%` | `406.17` |
| `Live` | `Long` | `72.45` | 31,250,000.00 USD | 0.00 USD | 2,240.00 USD | `-25.51%` | `30.92` |
| `Live` | `Long` | `72.55` | 31,250,000.00 USD | 0.00 USD | 16,450.00 USD | `-25.40%` | `226.78` |
| `Live` | `Long` | `72.65` | 31,240,000.00 USD | 0.00 USD | 33,720.00 USD | `-25.30%` | `464.15` |
| `Live` | `Long` | `72.75` | 31,200,000.00 USD | 0.00 USD | 3,100.00 USD | `-25.20%` | `42.56` |
| `Live` | `Long` | `72.85` | 31,200,000.00 USD | 0.00 USD | 186,830.00 USD | `-25.09%` | `2,564.61` |
| `Live` | `Long` | `72.95` | 31,010,000.00 USD | 0.00 USD | 18,610.00 USD | `-24.99%` | `255.12` |
| `Live` | `Long` | `73.05` | 30,990,000.00 USD | 0.00 USD | 7,310.00 USD | `-24.89%` | `100.09` |
| `Live` | `Long` | `73.15` | 30,990,000.00 USD | 0.00 USD | 17,140.00 USD | `-24.79%` | `234.31` |
| `Live` | `Long` | `73.25` | 30,970,000.00 USD | 0.00 USD | 28,470.00 USD | `-24.68%` | `388.71` |
| `Live` | `Long` | `73.35` | 30,940,000.00 USD | 0.00 USD | 8,280.00 USD | `-24.58%` | `112.91` |
| `Live` | `Long` | `73.45` | 30,930,000.00 USD | 0.00 USD | 5,350.00 USD | `-24.48%` | `72.82` |
| `Live` | `Long` | `73.55` | 30,930,000.00 USD | 0.00 USD | 17,060.00 USD | `-24.37%` | `232.00` |
| `Live` | `Long` | `73.65` | 30,910,000.00 USD | 0.00 USD | 38,360.00 USD | `-24.27%` | `520.79` |
| `Live` | `Long` | `73.75` | 30,870,000.00 USD | 0.00 USD | 77,660.00 USD | `-24.17%` | `1,052.95` |
| `Live` | `Long` | `73.85` | 30,790,000.00 USD | 0.00 USD | 11,710.00 USD | `-24.07%` | `158.63` |
| `Live` | `Long` | `73.95` | 30,780,000.00 USD | 0.00 USD | 40,040.00 USD | `-23.96%` | `541.40` |
| `Live` | `Long` | `74.05` | 30,740,000.00 USD | 0.00 USD | 38,460.00 USD | `-23.86%` | `519.35` |
| `Live` | `Long` | `74.15` | 30,700,000.00 USD | 0.00 USD | 21,430.00 USD | `-23.76%` | `289.03` |
| `Live` | `Long` | `74.25` | 30,680,000.00 USD | 0.00 USD | 41,310.00 USD | `-23.65%` | `556.34` |
| `Live` | `Long` | `74.35` | 30,640,000.00 USD | 0.00 USD | 24,920.00 USD | `-23.55%` | `335.13` |
| `Live` | `Long` | `74.45` | 30,620,000.00 USD | 0.00 USD | 22,920.00 USD | `-23.45%` | `307.90` |
| `Live` | `Long` | `74.55` | 30,590,000.00 USD | 0.00 USD | 11,550.00 USD | `-23.35%` | `154.96` |
| `Live` | `Long` | `74.65` | 30,580,000.00 USD | 0.00 USD | 1,030.00 USD | `-23.24%` | `13.82` |
| `Live` | `Long` | `74.75` | 30,580,000.00 USD | 0.00 USD | 46,150.00 USD | `-23.14%` | `617.43` |
| `Live` | `Long` | `74.85` | 30,530,000.00 USD | 0.00 USD | 127,450.00 USD | `-23.04%` | `1,702.70` |
| `Live` | `Long` | `74.95` | 30,410,000.00 USD | 0.00 USD | 19,860.00 USD | `-22.93%` | `264.93` |
| `Live` | `Long` | `75.05` | 30,390,000.00 USD | 0.00 USD | 48,410.00 USD | `-22.83%` | `645.02` |
| `Live` | `Long` | `75.15` | 30,340,000.00 USD | 0.00 USD | 2,430.00 USD | `-22.73%` | `32.32` |
| `Live` | `Long` | `75.25` | 30,340,000.00 USD | 0.00 USD | 1,910,000.00 USD | `-22.63%` | `25,318.68` |
| `Live` | `Long` | `75.35` | 28,430,000.00 USD | 0.00 USD | 18,360.00 USD | `-22.52%` | `243.67` |
| `Live` | `Long` | `75.45` | 28,410,000.00 USD | 0.00 USD | 33,560.00 USD | `-22.42%` | `444.85` |
| `Live` | `Long` | `75.55` | 28,380,000.00 USD | 0.00 USD | 29,130.00 USD | `-22.32%` | `385.56` |
| `Live` | `Long` | `75.65` | 28,350,000.00 USD | 0.00 USD | 130,250.00 USD | `-22.21%` | `1,721.70` |
| `Live` | `Long` | `75.75` | 28,220,000.00 USD | 0.00 USD | 1,550,000.00 USD | `-22.11%` | `20,412.03` |
| `Live` | `Long` | `75.85` | 26,670,000.00 USD | 0.00 USD | 4,110.00 USD | `-22.01%` | `54.17` |
| `Live` | `Long` | `75.95` | 26,670,000.00 USD | 0.00 USD | 27,920.00 USD | `-21.91%` | `367.58` |
| `Live` | `Long` | `76.05` | 26,640,000.00 USD | 0.00 USD | 8,540.00 USD | `-21.80%` | `112.25` |
| `Live` | `Long` | `76.15` | 26,630,000.00 USD | 0.00 USD | 17,050.00 USD | `-21.70%` | `223.90` |
| `Live` | `Long` | `76.25` | 26,620,000.00 USD | 0.00 USD | 9,710.00 USD | `-21.60%` | `127.31` |
| `Live` | `Long` | `76.35` | 26,610,000.00 USD | 0.00 USD | 35,800.00 USD | `-21.50%` | `468.95` |
| `Live` | `Long` | `76.45` | 26,570,000.00 USD | 0.00 USD | 1,990.00 USD | `-21.39%` | `25.99` |
| `Live` | `Long` | `76.55` | 26,570,000.00 USD | 0.00 USD | 68,230.00 USD | `-21.29%` | `891.36` |
| `Live` | `Long` | `76.65` | 26,500,000.00 USD | 0.00 USD | 57,460.00 USD | `-21.19%` | `749.66` |
| `Live` | `Long` | `76.75` | 26,440,000.00 USD | 0.00 USD | 5,060.00 USD | `-21.08%` | `65.89` |
| `Live` | `Long` | `76.85` | 26,440,000.00 USD | 0.00 USD | 134,060.00 USD | `-20.98%` | `1,744.46` |
| `Live` | `Long` | `76.95` | 26,300,000.00 USD | 0.00 USD | 29,250.00 USD | `-20.88%` | `380.17` |
| `Live` | `Long` | `77.05` | 26,270,000.00 USD | 0.00 USD | 80,420.00 USD | `-20.78%` | `1,043.70` |
| `Live` | `Long` | `77.15` | 26,190,000.00 USD | 0.00 USD | 257,230.00 USD | `-20.67%` | `3,334.13` |
| `Live` | `Long` | `77.25` | 25,940,000.00 USD | 0.00 USD | 32,190.00 USD | `-20.57%` | `416.73` |
| `Live` | `Long` | `77.35` | 25,900,000.00 USD | 0.00 USD | 8,780.00 USD | `-20.47%` | `113.48` |
| `Live` | `Long` | `77.45` | 25,900,000.00 USD | 0.00 USD | 52,110.00 USD | `-20.36%` | `672.81` |
| `Live` | `Long` | `77.55` | 25,840,000.00 USD | 0.00 USD | 12,900.00 USD | `-20.26%` | `166.30` |
| `Live` | `Long` | `77.75` | 25,830,000.00 USD | 0.00 USD | 9,870.00 USD | `-20.06%` | `126.99` |
| `Live` | `Long` | `77.85` | 25,820,000.00 USD | 0.00 USD | 59,570.00 USD | `-19.95%` | `765.23` |
| `Live` | `Long` | `77.95` | 25,760,000.00 USD | 0.00 USD | 14,550.00 USD | `-19.85%` | `186.64` |
| `Live` | `Long` | `78.05` | 25,750,000.00 USD | 0.00 USD | 21,880.00 USD | `-19.75%` | `280.28` |
| `Live` | `Long` | `78.15` | 25,730,000.00 USD | 0.00 USD | 63,910.00 USD | `-19.64%` | `817.81` |
| `Live` | `Long` | `78.25` | 25,660,000.00 USD | 0.00 USD | 39,070.00 USD | `-19.54%` | `499.28` |
| `Live` | `Long` | `78.35` | 25,620,000.00 USD | 0.00 USD | 55,060.00 USD | `-19.44%` | `702.76` |
| `Live` | `Long` | `78.45` | 25,570,000.00 USD | 0.00 USD | 26,080.00 USD | `-19.34%` | `332.40` |
| `Live` | `Long` | `78.55` | 25,540,000.00 USD | 0.00 USD | 5,910.00 USD | `-19.23%` | `75.27` |
| `Live` | `Long` | `78.65` | 25,540,000.00 USD | 0.00 USD | 32,860.00 USD | `-19.13%` | `417.75` |
| `Live` | `Long` | `78.75` | 25,500,000.00 USD | 0.00 USD | 60,550.00 USD | `-19.03%` | `768.88` |
| `Live` | `Long` | `78.85` | 25,440,000.00 USD | 0.00 USD | 62,050.00 USD | `-18.92%` | `786.91` |
| `Live` | `Long` | `78.95` | 25,380,000.00 USD | 0.00 USD | 1,370.00 USD | `-18.82%` | `17.33` |
| `Live` | `Long` | `79.05` | 25,380,000.00 USD | 0.00 USD | 6,870.00 USD | `-18.72%` | `86.94` |
| `Live` | `Long` | `79.15` | 25,370,000.00 USD | 0.00 USD | 128,420.00 USD | `-18.62%` | `1,622.43` |
| `Live` | `Long` | `79.25` | 25,240,000.00 USD | 0.00 USD | 59,390.00 USD | `-18.51%` | `749.42` |
| `Live` | `Long` | `79.35` | 25,180,000.00 USD | 0.00 USD | 25,940.00 USD | `-18.41%` | `326.87` |
| `Live` | `Long` | `79.45` | 25,160,000.00 USD | 0.00 USD | 11,960.00 USD | `-18.31%` | `150.55` |
| `Live` | `Long` | `79.55` | 25,150,000.00 USD | 0.00 USD | 1,900.00 USD | `-18.20%` | `23.91` |
| `Live` | `Long` | `79.65` | 25,140,000.00 USD | 0.00 USD | 19,720.00 USD | `-18.10%` | `247.58` |
| `Live` | `Long` | `79.75` | 25,120,000.00 USD | 0.00 USD | 85,820.00 USD | `-18.00%` | `1,076.13` |
| `Live` | `Long` | `79.85` | 25,040,000.00 USD | 0.00 USD | 171,770.00 USD | `-17.90%` | `2,151.11` |
| `Live` | `Long` | `79.95` | 24,870,000.00 USD | 0.00 USD | 29,580.00 USD | `-17.79%` | `370.00` |
| `Live` | `Long` | `80.05` | 24,840,000.00 USD | 0.00 USD | 8,660.00 USD | `-17.69%` | `108.13` |
| `Live` | `Long` | `80.15` | 24,830,000.00 USD | 0.00 USD | 59,220.00 USD | `-17.59%` | `738.90` |
| `Live` | `Long` | `80.25` | 24,770,000.00 USD | 0.00 USD | 76,330.00 USD | `-17.48%` | `951.14` |
| `Live` | `Long` | `80.35` | 24,690,000.00 USD | 0.00 USD | 113,360.00 USD | `-17.38%` | `1,410.88` |
| `Live` | `Long` | `80.45` | 24,580,000.00 USD | 0.00 USD | 12,930.00 USD | `-17.28%` | `160.76` |
| `Live` | `Long` | `80.55` | 24,570,000.00 USD | 0.00 USD | 8,000.00 USD | `-17.18%` | `99.36` |
| `Live` | `Long` | `80.65` | 24,560,000.00 USD | 0.00 USD | 94,280.00 USD | `-17.07%` | `1,168.99` |
| `Live` | `Long` | `80.75` | 24,460,000.00 USD | 0.00 USD | 26,360.00 USD | `-16.97%` | `326.45` |
| `Live` | `Long` | `80.85` | 24,440,000.00 USD | 0.00 USD | 440,510.00 USD | `-16.87%` | `5,448.49` |
| `Live` | `Long` | `80.95` | 24,000,000.00 USD | 0.00 USD | 10,620.00 USD | `-16.77%` | `131.18` |
| `Live` | `Long` | `81.05` | 23,990,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-16.66%` | `27,552.04` |
| `Live` | `Long` | `81.15` | 21,750,000.00 USD | 0.00 USD | 136,780.00 USD | `-16.56%` | `1,685.52` |
| `Live` | `Long` | `81.25` | 21,620,000.00 USD | 0.00 USD | 31,500.00 USD | `-16.46%` | `387.71` |
| `Live` | `Long` | `81.35` | 21,590,000.00 USD | 0.00 USD | 56,470.00 USD | `-16.35%` | `694.17` |
| `Live` | `Long` | `81.45` | 21,530,000.00 USD | 0.00 USD | 59,690.00 USD | `-16.25%` | `732.84` |
| `Live` | `Long` | `81.55` | 21,470,000.00 USD | 0.00 USD | 68,180.00 USD | `-16.15%` | `836.02` |
| `Live` | `Long` | `81.65` | 21,400,000.00 USD | 0.00 USD | 36,930.00 USD | `-16.05%` | `452.28` |
| `Live` | `Long` | `81.75` | 21,360,000.00 USD | 0.00 USD | 18,650.00 USD | `-15.94%` | `228.11` |
| `Live` | `Long` | `81.85` | 21,350,000.00 USD | 0.00 USD | 37,600.00 USD | `-15.84%` | `459.40` |
| `Live` | `Long` | `81.95` | 21,310,000.00 USD | 0.00 USD | 22,190.00 USD | `-15.74%` | `270.82` |
| `Live` | `Long` | `82.05` | 21,290,000.00 USD | 0.00 USD | 117,060.00 USD | `-15.63%` | `1,426.69` |
| `Live` | `Long` | `82.15` | 21,170,000.00 USD | 0.00 USD | 804,530.00 USD | `-15.53%` | `9,793.43` |
| `Live` | `Long` | `82.25` | 20,360,000.00 USD | 0.00 USD | 41,530.00 USD | `-15.43%` | `504.88` |
| `Live` | `Long` | `82.35` | 20,320,000.00 USD | 0.00 USD | 162,250.00 USD | `-15.33%` | `1,970.24` |
| `Live` | `Long` | `82.45` | 20,160,000.00 USD | 0.00 USD | 213,390.00 USD | `-15.22%` | `2,588.09` |
| `Live` | `Long` | `82.55` | 19,950,000.00 USD | 0.00 USD | 390,360.00 USD | `-15.12%` | `4,728.74` |
| `Live` | `Long` | `82.65` | 19,560,000.00 USD | 0.00 USD | 106,090.00 USD | `-15.02%` | `1,283.61` |
| `Live` | `Long` | `82.75` | 19,450,000.00 USD | 0.00 USD | 41,050.00 USD | `-14.91%` | `496.13` |
| `Live` | `Long` | `82.85` | 19,410,000.00 USD | 0.00 USD | 20,820.00 USD | `-14.81%` | `251.35` |
| `Live` | `Long` | `82.95` | 19,390,000.00 USD | 0.00 USD | 24,190.00 USD | `-14.71%` | `291.66` |
| `Live` | `Long` | `83.05` | 19,360,000.00 USD | 0.00 USD | 99,450.00 USD | `-14.61%` | `1,197.53` |
| `Live` | `Long` | `83.15` | 19,260,000.00 USD | 0.00 USD | 758,900.00 USD | `-14.50%` | `9,126.86` |
| `Live` | `Long` | `83.25` | 18,510,000.00 USD | 0.00 USD | 158,960.00 USD | `-14.40%` | `1,909.42` |
| `Live` | `Long` | `83.35` | 18,350,000.00 USD | 0.00 USD | 263,640.00 USD | `-14.30%` | `3,163.01` |
| `Live` | `Long` | `83.45` | 18,080,000.00 USD | 0.00 USD | 54,780.00 USD | `-14.19%` | `656.45` |
| `Live` | `Long` | `83.55` | 18,030,000.00 USD | 0.00 USD | 65,570.00 USD | `-14.09%` | `784.75` |
| `Live` | `Long` | `83.65` | 17,960,000.00 USD | 0.00 USD | 79,520.00 USD | `-13.99%` | `950.65` |
| `Live` | `Long` | `83.75` | 17,880,000.00 USD | 0.00 USD | 89,170.00 USD | `-13.89%` | `1,064.74` |
| `Live` | `Long` | `83.85` | 17,790,000.00 USD | 0.00 USD | 13,820.00 USD | `-13.78%` | `164.79` |
| `Live` | `Long` | `83.95` | 17,780,000.00 USD | 0.00 USD | 103,880.00 USD | `-13.68%` | `1,237.43` |
| `Live` | `Long` | `84.05` | 17,680,000.00 USD | 0.00 USD | 124,350.00 USD | `-13.58%` | `1,479.48` |
| `Live` | `Long` | `84.15` | 17,550,000.00 USD | 0.00 USD | 65,530.00 USD | `-13.47%` | `778.68` |
| `Live` | `Long` | `84.25` | 17,490,000.00 USD | 0.00 USD | 204,990.00 USD | `-13.37%` | `2,433.17` |
| `Live` | `Long` | `84.35` | 17,280,000.00 USD | 0.00 USD | 25,180.00 USD | `-13.27%` | `298.47` |
| `Live` | `Long` | `84.45` | 17,260,000.00 USD | 0.00 USD | 86,250.00 USD | `-13.17%` | `1,021.32` |
| `Live` | `Long` | `84.55` | 17,170,000.00 USD | 0.00 USD | 2,300.00 USD | `-13.06%` | `27.26` |
| `Live` | `Long` | `84.65` | 17,170,000.00 USD | 0.00 USD | 101,540.00 USD | `-12.96%` | `1,199.56` |
| `Live` | `Long` | `84.75` | 17,070,000.00 USD | 0.00 USD | 289,310.00 USD | `-12.86%` | `3,413.65` |
| `Live` | `Long` | `84.85` | 16,780,000.00 USD | 0.00 USD | 94,350.00 USD | `-12.76%` | `1,112.02` |
| `Live` | `Long` | `84.95` | 16,680,000.00 USD | 0.00 USD | 1,800.00 USD | `-12.65%` | `21.17` |
| `Live` | `Long` | `85.05` | 16,680,000.00 USD | 0.00 USD | 15,480.00 USD | `-12.55%` | `181.97` |
| `Live` | `Long` | `85.15` | 16,670,000.00 USD | 0.00 USD | 1,240,000.00 USD | `-12.45%` | `14,563.53` |
| `Live` | `Long` | `85.25` | 15,430,000.00 USD | 0.00 USD | 609,970.00 USD | `-12.34%` | `7,155.05` |
| `Live` | `Long` | `85.35` | 14,820,000.00 USD | 0.00 USD | 21,130.00 USD | `-12.24%` | `247.60` |
| `Live` | `Long` | `85.45` | 14,790,000.00 USD | 0.00 USD | 57,870.00 USD | `-12.14%` | `677.20` |
| `Live` | `Long` | `85.55` | 14,740,000.00 USD | 0.00 USD | 63,600.00 USD | `-12.04%` | `743.39` |
| `Live` | `Long` | `85.65` | 14,670,000.00 USD | 0.00 USD | 43,310.00 USD | `-11.93%` | `505.67` |
| `Live` | `Long` | `85.75` | 14,630,000.00 USD | 0.00 USD | 9,950.00 USD | `-11.83%` | `116.05` |
| `Live` | `Long` | `85.85` | 14,620,000.00 USD | 0.00 USD | 70,970.00 USD | `-11.73%` | `826.65` |
| `Live` | `Long` | `85.95` | 14,550,000.00 USD | 0.00 USD | 361,960.00 USD | `-11.62%` | `4,211.33` |
| `Live` | `Long` | `86.05` | 14,190,000.00 USD | 0.00 USD | 276,690.00 USD | `-11.52%` | `3,215.43` |
| `Live` | `Long` | `86.15` | 13,910,000.00 USD | 0.00 USD | 51,580.00 USD | `-11.42%` | `598.73` |
| `Live` | `Long` | `86.25` | 13,860,000.00 USD | 0.00 USD | 29,040.00 USD | `-11.32%` | `336.74` |
| `Live` | `Long` | `86.35` | 13,830,000.00 USD | 0.00 USD | 5,680.00 USD | `-11.21%` | `65.77` |
| `Live` | `Long` | `86.45` | 13,820,000.00 USD | 0.00 USD | 108,330.00 USD | `-11.11%` | `1,253.13` |
| `Live` | `Long` | `86.55` | 13,720,000.00 USD | 0.00 USD | 60,140.00 USD | `-11.01%` | `694.88` |
| `Live` | `Long` | `86.65` | 13,660,000.00 USD | 0.00 USD | 190,730.00 USD | `-10.90%` | `2,201.12` |
| `Live` | `Long` | `86.75` | 13,460,000.00 USD | 0.00 USD | 34,820.00 USD | `-10.80%` | `401.33` |
| `Live` | `Long` | `86.85` | 13,430,000.00 USD | 0.00 USD | 92,320.00 USD | `-10.70%` | `1,063.03` |
| `Live` | `Long` | `86.95` | 13,340,000.00 USD | 0.00 USD | 152,510.00 USD | `-10.60%` | `1,754.01` |
| `Live` | `Long` | `87.05` | 13,180,000.00 USD | 0.00 USD | 31,140.00 USD | `-10.49%` | `357.77` |
| `Live` | `Long` | `87.15` | 13,150,000.00 USD | 0.00 USD | 4,410.00 USD | `-10.39%` | `50.58` |
| `Live` | `Long` | `87.25` | 13,150,000.00 USD | 0.00 USD | 92,780.00 USD | `-10.29%` | `1,063.42` |
| `Live` | `Long` | `87.35` | 13,060,000.00 USD | 0.00 USD | 100,830.00 USD | `-10.18%` | `1,154.31` |
| `Live` | `Long` | `87.45` | 12,960,000.00 USD | 0.00 USD | 156,920.00 USD | `-10.08%` | `1,794.35` |
| `Live` | `Long` | `87.55` | 12,800,000.00 USD | 0.00 USD | 243,070.00 USD | `-9.98%` | `2,776.30` |
| `Live` | `Long` | `87.65` | 12,560,000.00 USD | 0.00 USD | 108,400.00 USD | `-9.88%` | `1,236.74` |
| `Live` | `Long` | `87.75` | 12,450,000.00 USD | 0.00 USD | 28,570.00 USD | `-9.77%` | `325.62` |
| `Live` | `Long` | `87.85` | 12,420,000.00 USD | 0.00 USD | 72,180.00 USD | `-9.67%` | `821.66` |
| `Live` | `Long` | `87.95` | 12,350,000.00 USD | 0.00 USD | 6,600.00 USD | `-9.57%` | `75.02` |
| `Live` | `Long` | `88.05` | 12,340,000.00 USD | 0.00 USD | 154,390.00 USD | `-9.46%` | `1,753.45` |
| `Live` | `Long` | `88.15` | 12,190,000.00 USD | 0.00 USD | 37,310.00 USD | `-9.36%` | `423.22` |
| `Live` | `Long` | `88.25` | 12,150,000.00 USD | 0.00 USD | 68,850.00 USD | `-9.26%` | `780.18` |
| `Live` | `Long` | `88.35` | 12,080,000.00 USD | 0.00 USD | 91,590.00 USD | `-9.16%` | `1,036.71` |
| `Live` | `Long` | `88.45` | 11,990,000.00 USD | 0.00 USD | 69,390.00 USD | `-9.05%` | `784.46` |
| `Live` | `Long` | `88.55` | 11,920,000.00 USD | 0.00 USD | 242,620.00 USD | `-8.95%` | `2,739.96` |
| `Live` | `Long` | `88.65` | 11,680,000.00 USD | 0.00 USD | 95,980.00 USD | `-8.85%` | `1,082.67` |
| `Live` | `Long` | `88.75` | 11,580,000.00 USD | 0.00 USD | 167,190.00 USD | `-8.75%` | `1,883.78` |
| `Live` | `Long` | `88.85` | 11,410,000.00 USD | 0.00 USD | 1,090,000.00 USD | `-8.64%` | `12,214.12` |
| `Live` | `Long` | `88.95` | 10,330,000.00 USD | 0.00 USD | 48,800.00 USD | `-8.54%` | `548.66` |
| `Live` | `Long` | `89.05` | 10,280,000.00 USD | 0.00 USD | 24,630.00 USD | `-8.44%` | `276.62` |
| `Live` | `Long` | `89.15` | 10,250,000.00 USD | 0.00 USD | 119,730.00 USD | `-8.33%` | `1,342.99` |
| `Live` | `Long` | `89.25` | 10,130,000.00 USD | 0.00 USD | 31,740.00 USD | `-8.23%` | `355.61` |
| `Live` | `Long` | `89.35` | 10,100,000.00 USD | 0.00 USD | 47,410.00 USD | `-8.13%` | `530.60` |
| `Live` | `Long` | `89.45` | 10,050,000.00 USD | 0.00 USD | 488,780.00 USD | `-8.03%` | `5,464.27` |
| `Live` | `Long` | `89.55` | 9,570,000.00 USD | 0.00 USD | 36,300.00 USD | `-7.92%` | `405.39` |
| `Live` | `Long` | `89.65` | 9,530,000.00 USD | 0.00 USD | 15,430.00 USD | `-7.82%` | `172.07` |
| `Live` | `Long` | `89.75` | 9,510,000.00 USD | 0.00 USD | 122,670.00 USD | `-7.72%` | `1,366.81` |
| `Live` | `Long` | `89.85` | 9,390,000.00 USD | 0.00 USD | 71,950.00 USD | `-7.61%` | `800.73` |
| `Live` | `Long` | `89.95` | 9,320,000.00 USD | 0.00 USD | 81,650.00 USD | `-7.51%` | `907.74` |
| `Live` | `Long` | `90.05` | 9,240,000.00 USD | 0.00 USD | 30,300.00 USD | `-7.41%` | `336.50` |
| `Live` | `Long` | `90.15` | 9,210,000.00 USD | 0.00 USD | 60,240.00 USD | `-7.31%` | `668.24` |
| `Live` | `Long` | `90.25` | 9,150,000.00 USD | 0.00 USD | 35,780.00 USD | `-7.20%` | `396.47` |
| `Live` | `Long` | `90.35` | 9,110,000.00 USD | 0.00 USD | 79,990.00 USD | `-7.10%` | `885.35` |
| `Live` | `Long` | `90.45` | 9,030,000.00 USD | 0.00 USD | 64,160.00 USD | `-7.00%` | `709.33` |
| `Live` | `Long` | `90.55` | 8,970,000.00 USD | 0.00 USD | 54,910.00 USD | `-6.89%` | `606.42` |
| `Live` | `Long` | `90.65` | 8,910,000.00 USD | 0.00 USD | 114,260.00 USD | `-6.79%` | `1,260.49` |
| `Live` | `Long` | `90.75` | 8,800,000.00 USD | 0.00 USD | 84,750.00 USD | `-6.69%` | `933.93` |
| `Live` | `Long` | `90.85` | 8,710,000.00 USD | 0.00 USD | 94,780.00 USD | `-6.59%` | `1,043.26` |
| `Live` | `Long` | `90.95` | 8,620,000.00 USD | 0.00 USD | 31,540.00 USD | `-6.48%` | `346.78` |
| `Live` | `Long` | `91.05` | 8,590,000.00 USD | 0.00 USD | 389,480.00 USD | `-6.38%` | `4,277.65` |
| `Live` | `Long` | `91.15` | 8,200,000.00 USD | 0.00 USD | 293,530.00 USD | `-6.28%` | `3,220.27` |
| `Live` | `Long` | `91.25` | 7,900,000.00 USD | 0.00 USD | 30,390.00 USD | `-6.17%` | `333.03` |
| `Live` | `Long` | `91.35` | 7,870,000.00 USD | 0.00 USD | 14,960.00 USD | `-6.07%` | `163.74` |
| `Live` | `Long` | `91.45` | 7,860,000.00 USD | 0.00 USD | 309,360.00 USD | `-5.97%` | `3,382.87` |
| `Live` | `Long` | `91.55` | 7,550,000.00 USD | 0.00 USD | 1,210,000.00 USD | `-5.87%` | `13,204.29` |
| `Live` | `Long` | `91.65` | 6,340,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-5.76%` | `15,594.68` |
| `Live` | `Long` | `91.75` | 4,910,000.00 USD | 0.00 USD | 237,960.00 USD | `-5.66%` | `2,593.57` |
| `Live` | `Long` | `91.85` | 4,670,000.00 USD | 0.00 USD | 46,220.00 USD | `-5.56%` | `503.25` |
| `Live` | `Long` | `91.95` | 4,630,000.00 USD | 0.00 USD | 64,120.00 USD | `-5.45%` | `697.35` |
| `Live` | `Long` | `92.05` | 4,560,000.00 USD | 0.00 USD | 192,580.00 USD | `-5.35%` | `2,092.14` |
| `Live` | `Long` | `92.15` | 4,370,000.00 USD | 0.00 USD | 328,220.00 USD | `-5.25%` | `3,561.81` |
| `Live` | `Long` | `92.25` | 4,040,000.00 USD | 0.00 USD | 225,070.00 USD | `-5.15%` | `2,439.82` |
| `Live` | `Long` | `92.35` | 3,820,000.00 USD | 0.00 USD | 308,200.00 USD | `-5.04%` | `3,337.27` |
| `Live` | `Long` | `92.45` | 3,510,000.00 USD | 0.00 USD | 117,820.00 USD | `-4.94%` | `1,274.42` |
| `Live` | `Long` | `92.55` | 3,390,000.00 USD | 0.00 USD | 4,870.00 USD | `-4.84%` | `52.65` |
| `Live` | `Long` | `92.65` | 3,390,000.00 USD | 0.00 USD | 14,980.00 USD | `-4.73%` | `161.63` |
| `Live` | `Long` | `92.75` | 3,370,000.00 USD | 0.00 USD | 5,120.00 USD | `-4.63%` | `55.19` |
| `Live` | `Long` | `92.85` | 3,370,000.00 USD | 0.00 USD | 337,230.00 USD | `-4.53%` | `3,631.97` |
| `Live` | `Long` | `92.95` | 3,030,000.00 USD | 0.00 USD | 3,780.00 USD | `-4.43%` | `40.66` |
| `Live` | `Long` | `93.05` | 3,030,000.00 USD | 0.00 USD | 29,770.00 USD | `-4.32%` | `319.90` |
| `Live` | `Long` | `93.15` | 3,000,000.00 USD | 0.00 USD | 2,810.00 USD | `-4.22%` | `30.17` |
| `Live` | `Long` | `93.25` | 2,990,000.00 USD | 0.00 USD | 38,840.00 USD | `-4.12%` | `416.49` |
| `Live` | `Long` | `93.35` | 2,950,000.00 USD | 0.00 USD | 12,570.00 USD | `-4.02%` | `134.70` |
| `Live` | `Long` | `93.45` | 2,940,000.00 USD | 0.00 USD | 7,320.00 USD | `-3.91%` | `78.38` |
| `Live` | `Long` | `93.55` | 2,930,000.00 USD | 0.00 USD | 19,840.00 USD | `-3.81%` | `212.09` |
| `Live` | `Long` | `93.65` | 2,910,000.00 USD | 0.00 USD | 3,240.00 USD | `-3.71%` | `34.59` |
| `Live` | `Long` | `93.75` | 2,910,000.00 USD | 0.00 USD | 942,560.00 USD | `-3.60%` | `10,053.98` |
| `Live` | `Long` | `93.85` | 1,970,000.00 USD | 0.00 USD | 7,310.00 USD | `-3.50%` | `77.92` |
| `Live` | `Long` | `93.95` | 1,960,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-3.40%` | `12,128.34` |
| `Live` | `Long` | `94.15` | 821,780.00 USD | 0.00 USD | 33,550.00 USD | `-3.19%` | `356.38` |
| `Live` | `Long` | `94.25` | 788,220.00 USD | 0.00 USD | 8,860.00 USD | `-3.09%` | `93.98` |
| `Live` | `Long` | `94.35` | 779,370.00 USD | 0.00 USD | 5,200.00 USD | `-2.99%` | `55.11` |
| `Live` | `Long` | `94.45` | 774,170.00 USD | 0.00 USD | 146,220.00 USD | `-2.88%` | `1,548.16` |
| `Live` | `Long` | `94.55` | 627,940.00 USD | 0.00 USD | 97,340.00 USD | `-2.78%` | `1,029.56` |
| `Live` | `Long` | `94.65` | 530,600.00 USD | 0.00 USD | 2,690.00 USD | `-2.68%` | `28.44` |
| `Live` | `Long` | `94.75` | 527,910.00 USD | 0.00 USD | 33,140.00 USD | `-2.58%` | `349.72` |
| `Live` | `Long` | `94.85` | 494,770.00 USD | 0.00 USD | 52,310.00 USD | `-2.47%` | `551.46` |
| `Live` | `Long` | `94.95` | 442,460.00 USD | 0.00 USD | 13,860.00 USD | `-2.37%` | `145.98` |
| `Live` | `Long` | `95.05` | 428,600.00 USD | 0.00 USD | 77,030.00 USD | `-2.27%` | `810.40` |
| `Live` | `Long` | `95.15` | 351,580.00 USD | 0.00 USD | 25,120.00 USD | `-2.16%` | `263.99` |
| `Live` | `Long` | `95.25` | 326,460.00 USD | 0.00 USD | 32,200.00 USD | `-2.06%` | `338.05` |
| `Live` | `Long` | `95.35` | 294,260.00 USD | 0.00 USD | 8,070.00 USD | `-1.96%` | `84.66` |
| `Live` | `Long` | `95.45` | 286,180.00 USD | 0.00 USD | 23,290.00 USD | `-1.86%` | `244.01` |
| `Live` | `Long` | `95.55` | 262,890.00 USD | 0.00 USD | 48,980.00 USD | `-1.75%` | `512.58` |
| `Live` | `Long` | `95.65` | 213,920.00 USD | 0.00 USD | 93,140.00 USD | `-1.65%` | `973.81` |
| `Live` | `Long` | `95.75` | 120,770.00 USD | 0.00 USD | 84,480.00 USD | `-1.55%` | `882.34` |
| `Live` | `Long` | `95.85` | 36,290.00 USD | 0.00 USD | 32,540.00 USD | `-1.44%` | `339.50` |
| `Live` | `Long` | `95.95` | 3,750.00 USD | 0.00 USD | 231.24 USD | `-1.34%` | `2.41` |
| `Live` | `Long` | `96.05` | 3,520.00 USD | 0.00 USD | 2,210.00 USD | `-1.24%` | `22.97` |
| `Live` | `Long` | `96.15` | 1,310.00 USD | 0.00 USD | 345.18 USD | `-1.14%` | `3.59` |
| `Live` | `Long` | `96.35` | 964.46 USD | 0.00 USD | 964.46 USD | `-0.93%` | `10.01` |
| `Live` | `Short` | `97.45` | 331.33 USD | 331.33 USD | 0.00 USD | `+0.20%` | `3.40` |
| `Live` | `Short` | `98.55` | 6,260.00 USD | 5,930.00 USD | 0.00 USD | `+1.33%` | `60.17` |
| `Live` | `Short` | `98.65` | 16,000.00 USD | 9,740.00 USD | 0.00 USD | `+1.43%` | `98.70` |
| `Live` | `Short` | `98.95` | 17,020.00 USD | 1,020.00 USD | 0.00 USD | `+1.74%` | `10.28` |
| `Live` | `Short` | `99.05` | 22,660.00 USD | 5,640.00 USD | 0.00 USD | `+1.85%` | `56.99` |
| `Live` | `Short` | `99.15` | 1,140,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+1.95%` | `11,235.53` |
| `Live` | `Short` | `99.25` | 1,140,000.00 USD | 7,330.00 USD | 0.00 USD | `+2.05%` | `73.86` |
| `Live` | `Short` | `99.35` | 1,210,000.00 USD | 64,750.00 USD | 0.00 USD | `+2.15%` | `651.77` |
| `Live` | `Short` | `99.45` | 1,210,000.00 USD | 335.15 USD | 0.00 USD | `+2.26%` | `3.37` |
| `Live` | `Short` | `99.55` | 1,220,000.00 USD | 11,890.00 USD | 0.00 USD | `+2.36%` | `119.45` |
| `Live` | `Short` | `99.65` | 1,220,000.00 USD | 1,130.00 USD | 0.00 USD | `+2.46%` | `11.30` |
| `Live` | `Short` | `99.75` | 1,250,000.00 USD | 25,520.00 USD | 0.00 USD | `+2.57%` | `255.85` |
| `Live` | `Short` | `99.85` | 1,250,000.00 USD | 238.64 USD | 0.00 USD | `+2.67%` | `2.39` |
| `Live` | `Short` | `99.95` | 1,250,000.00 USD | 3,070.00 USD | 0.00 USD | `+2.77%` | `30.69` |
| `Live` | `Short` | `100.05` | 1,280,000.00 USD | 32,030.00 USD | 0.00 USD | `+2.87%` | `320.09` |
| `Live` | `Short` | `100.15` | 1,320,000.00 USD | 33,940.00 USD | 0.00 USD | `+2.98%` | `338.87` |
| `Live` | `Short` | `100.25` | 1,660,000.00 USD | 345,350.00 USD | 0.00 USD | `+3.08%` | `3,444.84` |
| `Live` | `Short` | `100.35` | 2,070,000.00 USD | 410,700.00 USD | 0.00 USD | `+3.18%` | `4,092.63` |
| `Live` | `Short` | `100.45` | 2,100,000.00 USD | 26,900.00 USD | 0.00 USD | `+3.29%` | `267.76` |
| `Live` | `Short` | `100.55` | 2,140,000.00 USD | 41,910.00 USD | 0.00 USD | `+3.39%` | `416.76` |
| `Live` | `Short` | `100.65` | 2,240,000.00 USD | 102,960.00 USD | 0.00 USD | `+3.49%` | `1,022.93` |
| `Live` | `Short` | `100.75` | 2,260,000.00 USD | 19,590.00 USD | 0.00 USD | `+3.59%` | `194.44` |
| `Live` | `Short` | `100.95` | 2,260,000.00 USD | 498.69 USD | 0.00 USD | `+3.80%` | `4.94` |
| `Live` | `Short` | `101.05` | 2,260,000.00 USD | 168.75 USD | 0.00 USD | `+3.90%` | `1.67` |
| `Live` | `Short` | `101.15` | 2,280,000.00 USD | 12,350.00 USD | 0.00 USD | `+4.00%` | `122.06` |
| `Live` | `Short` | `101.25` | 2,280,000.00 USD | 769.50 USD | 0.00 USD | `+4.11%` | `7.60` |
| `Live` | `Short` | `101.45` | 2,280,000.00 USD | 1,340.00 USD | 0.00 USD | `+4.31%` | `13.25` |
| `Live` | `Short` | `101.55` | 2,280,000.00 USD | 2,790.00 USD | 0.00 USD | `+4.42%` | `27.47` |
| `Live` | `Short` | `101.65` | 2,280,000.00 USD | 2,640.00 USD | 0.00 USD | `+4.52%` | `26.02` |
| `Live` | `Short` | `101.85` | 2,290,000.00 USD | 8,240.00 USD | 0.00 USD | `+4.72%` | `80.91` |
| `Live` | `Short` | `101.95` | 2,290,000.00 USD | 1,760.00 USD | 0.00 USD | `+4.83%` | `17.31` |
| `Live` | `Short` | `102.05` | 2,300,000.00 USD | 5,220.00 USD | 0.00 USD | `+4.93%` | `51.17` |
| `Live` | `Short` | `102.25` | 2,300,000.00 USD | 1,170.00 USD | 0.00 USD | `+5.14%` | `11.44` |
| `Live` | `Short` | `102.35` | 2,300,000.00 USD | 720.54 USD | 0.00 USD | `+5.24%` | `7.04` |
| `Live` | `Short` | `102.45` | 2,300,000.00 USD | 175.19 USD | 0.00 USD | `+5.34%` | `1.71` |
| `Live` | `Short` | `102.55` | 2,310,000.00 USD | 6,330.00 USD | 0.00 USD | `+5.44%` | `61.77` |
| `Live` | `Short` | `102.65` | 2,310,000.00 USD | 1,070.00 USD | 0.00 USD | `+5.55%` | `10.45` |
| `Live` | `Short` | `102.75` | 2,310,000.00 USD | 3,340.00 USD | 0.00 USD | `+5.65%` | `32.53` |
| `Live` | `Short` | `102.95` | 2,320,000.00 USD | 4,150.00 USD | 0.00 USD | `+5.86%` | `40.32` |
| `Live` | `Short` | `103.05` | 2,320,000.00 USD | 692.50 USD | 0.00 USD | `+5.96%` | `6.72` |
| `Live` | `Short` | `103.15` | 2,330,000.00 USD | 11,000.00 USD | 0.00 USD | `+6.06%` | `106.62` |
| `Live` | `Short` | `103.25` | 2,330,000.00 USD | 859.04 USD | 0.00 USD | `+6.16%` | `8.32` |
| `Live` | `Short` | `103.35` | 2,330,000.00 USD | 385.50 USD | 0.00 USD | `+6.27%` | `3.73` |
| `Live` | `Short` | `103.45` | 2,340,000.00 USD | 14,540.00 USD | 0.00 USD | `+6.37%` | `140.56` |
| `Live` | `Short` | `103.65` | 2,350,000.00 USD | 4,360.00 USD | 0.00 USD | `+6.58%` | `42.09` |
| `Live` | `Short` | `103.75` | 2,610,000.00 USD | 261,050.00 USD | 0.00 USD | `+6.68%` | `2,516.13` |
| `Live` | `Short` | `103.85` | 2,620,000.00 USD | 14,220.00 USD | 0.00 USD | `+6.78%` | `136.92` |
| `Live` | `Short` | `103.95` | 2,620,000.00 USD | 827.44 USD | 0.00 USD | `+6.88%` | `7.96` |
| `Live` | `Short` | `104.05` | 2,630,000.00 USD | 775.17 USD | 0.00 USD | `+6.99%` | `7.45` |
| `Live` | `Short` | `104.15` | 2,630,000.00 USD | 1,180.00 USD | 0.00 USD | `+7.09%` | `11.34` |
| `Live` | `Short` | `104.25` | 2,630,000.00 USD | 722.45 USD | 0.00 USD | `+7.19%` | `6.93` |
| `Live` | `Short` | `104.35` | 2,640,000.00 USD | 11,820.00 USD | 0.00 USD | `+7.30%` | `113.24` |
| `Live` | `Short` | `104.45` | 2,650,000.00 USD | 12,640.00 USD | 0.00 USD | `+7.40%` | `120.99` |
| `Live` | `Short` | `104.55` | 2,650,000.00 USD | 360.70 USD | 0.00 USD | `+7.50%` | `3.45` |
| `Live` | `Short` | `104.65` | 2,650,000.00 USD | 401.86 USD | 0.00 USD | `+7.60%` | `3.84` |
| `Live` | `Short` | `104.75` | 2,650,000.00 USD | 199.02 USD | 0.00 USD | `+7.71%` | `1.90` |
| `Live` | `Short` | `104.85` | 2,660,000.00 USD | 3,430.00 USD | 0.00 USD | `+7.81%` | `32.69` |
| `Live` | `Short` | `104.95` | 2,780,000.00 USD | 126,060.00 USD | 0.00 USD | `+7.91%` | `1,201.13` |
| `Live` | `Short` | `105.05` | 2,790,000.00 USD | 2,800.00 USD | 0.00 USD | `+8.02%` | `26.70` |
| `Live` | `Short` | `105.15` | 2,810,000.00 USD | 21,880.00 USD | 0.00 USD | `+8.12%` | `208.08` |
| `Live` | `Short` | `105.25` | 2,810,000.00 USD | 2,860.00 USD | 0.00 USD | `+8.22%` | `27.17` |
| `Live` | `Short` | `105.35` | 2,820,000.00 USD | 6,840.00 USD | 0.00 USD | `+8.32%` | `64.89` |
| `Live` | `Short` | `105.45` | 3,350,000.00 USD | 531,450.00 USD | 0.00 USD | `+8.43%` | `5,039.81` |
| `Live` | `Short` | `105.55` | 3,350,000.00 USD | 5,240.00 USD | 0.00 USD | `+8.53%` | `49.61` |
| `Live` | `Short` | `105.65` | 3,360,000.00 USD | 1,740.00 USD | 0.00 USD | `+8.63%` | `16.44` |
| `Live` | `Short` | `105.85` | 3,450,000.00 USD | 92,920.00 USD | 0.00 USD | `+8.84%` | `877.89` |
| `Live` | `Short` | `105.95` | 3,450,000.00 USD | 592.26 USD | 0.00 USD | `+8.94%` | `5.59` |
| `Live` | `Short` | `106.05` | 3,480,000.00 USD | 33,380.00 USD | 0.00 USD | `+9.04%` | `314.77` |
| `Live` | `Short` | `106.15` | 3,480,000.00 USD | 248.39 USD | 0.00 USD | `+9.15%` | `2.34` |
| `Live` | `Short` | `106.35` | 3,740,000.00 USD | 256,250.00 USD | 0.00 USD | `+9.35%` | `2,409.50` |
| `Live` | `Short` | `106.45` | 3,770,000.00 USD | 34,730.00 USD | 0.00 USD | `+9.45%` | `326.30` |
| `Live` | `Short` | `106.55` | 3,770,000.00 USD | 105.48 USD | 0.00 USD | `+9.56%` | `0.99` |
| `Live` | `Short` | `106.65` | 3,780,000.00 USD | 6,360.00 USD | 0.00 USD | `+9.66%` | `59.59` |
| `Live` | `Short` | `106.85` | 4,260,000.00 USD | 479,130.00 USD | 0.00 USD | `+9.87%` | `4,484.15` |
| `Live` | `Short` | `106.95` | 4,300,000.00 USD | 37,730.00 USD | 0.00 USD | `+9.97%` | `352.76` |
| `Live` | `Short` | `107.05` | 4,310,000.00 USD | 14,600.00 USD | 0.00 USD | `+10.07%` | `136.36` |
| `Live` | `Short` | `107.15` | 4,310,000.00 USD | 3,060.00 USD | 0.00 USD | `+10.17%` | `28.58` |
| `Live` | `Short` | `107.25` | 4,350,000.00 USD | 35,230.00 USD | 0.00 USD | `+10.28%` | `328.47` |
| `Live` | `Short` | `107.35` | 4,350,000.00 USD | 766.48 USD | 0.00 USD | `+10.38%` | `7.14` |
| `Live` | `Short` | `107.45` | 4,380,000.00 USD | 32,580.00 USD | 0.00 USD | `+10.48%` | `303.18` |
| `Live` | `Short` | `107.55` | 4,390,000.00 USD | 11,910.00 USD | 0.00 USD | `+10.59%` | `110.74` |
| `Live` | `Short` | `107.85` | 4,540,000.00 USD | 143,340.00 USD | 0.00 USD | `+10.89%` | `1,329.08` |
| `Live` | `Short` | `107.95` | 4,560,000.00 USD | 17,360.00 USD | 0.00 USD | `+11.00%` | `160.77` |
| `Live` | `Short` | `108.05` | 4,560,000.00 USD | 1,080.00 USD | 0.00 USD | `+11.10%` | `10.04` |
| `Live` | `Short` | `108.15` | 4,560,000.00 USD | 1,150.00 USD | 0.00 USD | `+11.20%` | `10.66` |
| `Live` | `Short` | `108.25` | 4,600,000.00 USD | 38,000.00 USD | 0.00 USD | `+11.31%` | `351.08` |
| `Live` | `Short` | `108.35` | 4,600,000.00 USD | 3,470.00 USD | 0.00 USD | `+11.41%` | `32.00` |
| `Live` | `Short` | `108.45` | 4,710,000.00 USD | 108,080.00 USD | 0.00 USD | `+11.51%` | `996.61` |
| `Live` | `Short` | `108.55` | 4,710,000.00 USD | 117.23 USD | 0.00 USD | `+11.61%` | `1.08` |
| `Live` | `Short` | `108.65` | 4,710,000.00 USD | 5,050.00 USD | 0.00 USD | `+11.72%` | `46.45` |
| `Live` | `Short` | `108.75` | 4,710,000.00 USD | 2,120.00 USD | 0.00 USD | `+11.82%` | `19.46` |
| `Live` | `Short` | `108.85` | 4,720,000.00 USD | 3,230.00 USD | 0.00 USD | `+11.92%` | `29.68` |
| `Live` | `Short` | `108.95` | 4,720,000.00 USD | 3,170.00 USD | 0.00 USD | `+12.03%` | `29.10` |
| `Live` | `Short` | `109.05` | 4,720,000.00 USD | 163.58 USD | 0.00 USD | `+12.13%` | `1.50` |
| `Live` | `Short` | `109.25` | 4,850,000.00 USD | 131,370.00 USD | 0.00 USD | `+12.33%` | `1,202.44` |
| `Live` | `Short` | `109.35` | 4,850,000.00 USD | 247.13 USD | 0.00 USD | `+12.44%` | `2.26` |
| `Live` | `Short` | `109.45` | 4,850,000.00 USD | 202.48 USD | 0.00 USD | `+12.54%` | `1.85` |
| `Live` | `Short` | `109.55` | 5,260,000.00 USD | 408,340.00 USD | 0.00 USD | `+12.64%` | `3,727.42` |
| `Live` | `Short` | `109.65` | 5,300,000.00 USD | 38,640.00 USD | 0.00 USD | `+12.74%` | `352.40` |
| `Live` | `Short` | `109.85` | 5,300,000.00 USD | 3,190.00 USD | 0.00 USD | `+12.95%` | `29.08` |
| `Live` | `Short` | `109.95` | 5,300,000.00 USD | 301.26 USD | 0.00 USD | `+13.05%` | `2.74` |
| `Live` | `Short` | `110.05` | 5,320,000.00 USD | 14,560.00 USD | 0.00 USD | `+13.16%` | `132.30` |
| `Live` | `Short` | `110.15` | 5,320,000.00 USD | 194.97 USD | 0.00 USD | `+13.26%` | `1.77` |
| `Live` | `Short` | `110.25` | 5,320,000.00 USD | 195.14 USD | 0.00 USD | `+13.36%` | `1.77` |
| `Live` | `Short` | `110.35` | 5,320,000.00 USD | 158.90 USD | 0.00 USD | `+13.46%` | `1.44` |
| `Live` | `Short` | `110.45` | 5,460,000.00 USD | 143,580.00 USD | 0.00 USD | `+13.57%` | `1,299.91` |
| `Live` | `Short` | `110.55` | 5,460,000.00 USD | 203.41 USD | 0.00 USD | `+13.67%` | `1.84` |
| `Live` | `Short` | `110.65` | 5,500,000.00 USD | 38,290.00 USD | 0.00 USD | `+13.77%` | `346.03` |
| `Live` | `Short` | `110.85` | 5,500,000.00 USD | 1,090.00 USD | 0.00 USD | `+13.98%` | `9.87` |
| `Live` | `Short` | `110.95` | 5,510,000.00 USD | 4,450.00 USD | 0.00 USD | `+14.08%` | `40.12` |
| `Live` | `Short` | `111.15` | 5,510,000.00 USD | 1,710.00 USD | 0.00 USD | `+14.29%` | `15.37` |
| `Live` | `Short` | `111.35` | 5,510,000.00 USD | 390.84 USD | 0.00 USD | `+14.49%` | `3.51` |
| `Live` | `Short` | `111.45` | 5,510,000.00 USD | 841.45 USD | 0.00 USD | `+14.60%` | `7.55` |
| `Live` | `Short` | `111.55` | 5,510,000.00 USD | 892.40 USD | 0.00 USD | `+14.70%` | `8.00` |
| `Live` | `Short` | `111.65` | 5,510,000.00 USD | 3,220.00 USD | 0.00 USD | `+14.80%` | `28.82` |
| `Live` | `Short` | `111.75` | 5,510,000.00 USD | 169.86 USD | 0.00 USD | `+14.90%` | `1.52` |
| `Live` | `Short` | `111.85` | 5,530,000.00 USD | 15,880.00 USD | 0.00 USD | `+15.01%` | `141.95` |
| `Live` | `Short` | `111.95` | 5,530,000.00 USD | 223.90 USD | 0.00 USD | `+15.11%` | `2.00` |
| `Live` | `Short` | `112.15` | 5,530,000.00 USD | 528.23 USD | 0.00 USD | `+15.32%` | `4.71` |
| `Live` | `Short` | `112.35` | 5,590,000.00 USD | 61,610.00 USD | 0.00 USD | `+15.52%` | `548.37` |
| `Live` | `Short` | `112.45` | 5,600,000.00 USD | 5,670.00 USD | 0.00 USD | `+15.62%` | `50.42` |
| `Live` | `Short` | `112.55` | 5,600,000.00 USD | 844.13 USD | 0.00 USD | `+15.73%` | `7.50` |
| `Live` | `Short` | `112.65` | 5,600,000.00 USD | 707.44 USD | 0.00 USD | `+15.83%` | `6.28` |
| `Live` | `Short` | `112.75` | 5,720,000.00 USD | 118,640.00 USD | 0.00 USD | `+15.93%` | `1,052.24` |
| `Live` | `Short` | `112.85` | 5,830,000.00 USD | 108,760.00 USD | 0.00 USD | `+16.04%` | `963.76` |
| `Live` | `Short` | `113.05` | 5,830,000.00 USD | 406.98 USD | 0.00 USD | `+16.24%` | `3.60` |
| `Live` | `Short` | `113.15` | 5,840,000.00 USD | 9,560.00 USD | 0.00 USD | `+16.34%` | `84.51` |
| `Live` | `Short` | `113.25` | 5,840,000.00 USD | 698.75 USD | 0.00 USD | `+16.45%` | `6.17` |
| `Live` | `Short` | `113.35` | 5,840,000.00 USD | 4,120.00 USD | 0.00 USD | `+16.55%` | `36.36` |
| `Live` | `Short` | `113.45` | 5,840,000.00 USD | 3,360.00 USD | 0.00 USD | `+16.65%` | `29.62` |
| `Live` | `Short` | `113.55` | 6,110,000.00 USD | 263,860.00 USD | 0.00 USD | `+16.75%` | `2,323.72` |
| `Live` | `Short` | `113.65` | 6,210,000.00 USD | 105,510.00 USD | 0.00 USD | `+16.86%` | `928.37` |
| `Live` | `Short` | `113.75` | 6,220,000.00 USD | 5,200.00 USD | 0.00 USD | `+16.96%` | `45.74` |
| `Live` | `Short` | `113.85` | 6,220,000.00 USD | 104.74 USD | 0.00 USD | `+17.06%` | `0.92` |
| `Live` | `Short` | `113.95` | 6,240,000.00 USD | 21,840.00 USD | 0.00 USD | `+17.17%` | `191.69` |
| `Live` | `Short` | `114.05` | 6,270,000.00 USD | 31,740.00 USD | 0.00 USD | `+17.27%` | `278.26` |
| `Live` | `Short` | `114.25` | 6,270,000.00 USD | 2,150.00 USD | 0.00 USD | `+17.47%` | `18.80` |
| `Live` | `Short` | `114.45` | 6,280,000.00 USD | 3,830.00 USD | 0.00 USD | `+17.68%` | `33.46` |
| `Live` | `Short` | `114.55` | 6,290,000.00 USD | 7,090.00 USD | 0.00 USD | `+17.78%` | `61.90` |
| `Live` | `Short` | `114.65` | 6,290,000.00 USD | 3,430.00 USD | 0.00 USD | `+17.89%` | `29.93` |
| `Live` | `Short` | `115.05` | 6,860,000.00 USD | 569,550.00 USD | 0.00 USD | `+18.30%` | `4,950.49` |
| `Live` | `Short` | `115.15` | 6,860,000.00 USD | 1,100.00 USD | 0.00 USD | `+18.40%` | `9.52` |
| `Live` | `Short` | `115.25` | 6,860,000.00 USD | 161.35 USD | 0.00 USD | `+18.50%` | `1.40` |
| `Live` | `Short` | `115.45` | 7,750,000.00 USD | 893,760.00 USD | 0.00 USD | `+18.71%` | `7,741.54` |
| `Live` | `Short` | `115.55` | 7,920,000.00 USD | 167,330.00 USD | 0.00 USD | `+18.81%` | `1,448.12` |
| `Live` | `Short` | `115.75` | 7,920,000.00 USD | 160.89 USD | 0.00 USD | `+19.02%` | `1.39` |
| `Live` | `Short` | `115.85` | 7,920,000.00 USD | 289.62 USD | 0.00 USD | `+19.12%` | `2.50` |
| `Live` | `Short` | `116.05` | 7,930,000.00 USD | 4,450.00 USD | 0.00 USD | `+19.33%` | `38.34` |
| `Live` | `Short` | `116.25` | 7,930,000.00 USD | 180.19 USD | 0.00 USD | `+19.53%` | `1.55` |
| `Live` | `Short` | `116.35` | 7,930,000.00 USD | 4,960.00 USD | 0.00 USD | `+19.63%` | `42.60` |
| `Live` | `Short` | `116.55` | 7,930,000.00 USD | 2,040.00 USD | 0.00 USD | `+19.84%` | `17.52` |
| `Live` | `Short` | `116.65` | 7,930,000.00 USD | 113.15 USD | 0.00 USD | `+19.94%` | `0.97` |
| `Live` | `Short` | `116.85` | 7,930,000.00 USD | 1,520.00 USD | 0.00 USD | `+20.15%` | `13.05` |
| `Live` | `Short` | `117.05` | 7,940,000.00 USD | 156.85 USD | 0.00 USD | `+20.35%` | `1.34` |
| `Live` | `Short` | `117.15` | 8,030,000.00 USD | 90,390.00 USD | 0.00 USD | `+20.46%` | `771.61` |
| `Live` | `Short` | `117.25` | 8,030,000.00 USD | 225.12 USD | 0.00 USD | `+20.56%` | `1.92` |
| `Live` | `Short` | `117.35` | 12,820,000.00 USD | 4,790,000.00 USD | 0.00 USD | `+20.66%` | `40,815.76` |
| `Live` | `Short` | `117.55` | 12,820,000.00 USD | 188.08 USD | 0.00 USD | `+20.87%` | `1.60` |
| `Live` | `Short` | `117.65` | 12,860,000.00 USD | 47,200.00 USD | 0.00 USD | `+20.97%` | `401.16` |
| `Live` | `Short` | `117.75` | 12,880,000.00 USD | 20,960.00 USD | 0.00 USD | `+21.07%` | `177.98` |
| `Live` | `Short` | `117.95` | 12,880,000.00 USD | 353.85 USD | 0.00 USD | `+21.28%` | `3.00` |
| `Live` | `Short` | `118.25` | 17,350,000.00 USD | 4,470,000.00 USD | 0.00 USD | `+21.59%` | `37,796.13` |
| `Live` | `Short` | `118.45` | 17,380,000.00 USD | 30,080.00 USD | 0.00 USD | `+21.79%` | `253.91` |
| `Live` | `Short` | `118.55` | 17,390,000.00 USD | 7,700.00 USD | 0.00 USD | `+21.90%` | `64.98` |
| `Live` | `Short` | `118.75` | 17,390,000.00 USD | 309.94 USD | 0.00 USD | `+22.10%` | `2.61` |
| `Live` | `Short` | `119.25` | 17,390,000.00 USD | 240.88 USD | 0.00 USD | `+22.62%` | `2.02` |
| `Live` | `Short` | `119.35` | 17,450,000.00 USD | 57,850.00 USD | 0.00 USD | `+22.72%` | `484.72` |
| `Live` | `Short` | `119.45` | 17,480,000.00 USD | 27,900.00 USD | 0.00 USD | `+22.82%` | `233.55` |
| `Live` | `Short` | `119.55` | 17,490,000.00 USD | 8,970.00 USD | 0.00 USD | `+22.92%` | `75.00` |
| `Live` | `Short` | `119.65` | 17,490,000.00 USD | 1,760.00 USD | 0.00 USD | `+23.03%` | `14.72` |
| `Live` | `Short` | `119.75` | 17,490,000.00 USD | 731.67 USD | 0.00 USD | `+23.13%` | `6.11` |
| `Live` | `Short` | `119.85` | 17,490,000.00 USD | 485.39 USD | 0.00 USD | `+23.23%` | `4.05` |
| `Live` | `Short` | `119.95` | 17,490,000.00 USD | 4,200.00 USD | 0.00 USD | `+23.34%` | `35.00` |
| `Live` | `Short` | `120.05` | 17,590,000.00 USD | 96,110.00 USD | 0.00 USD | `+23.44%` | `800.60` |
| `Live` | `Short` | `120.15` | 17,590,000.00 USD | 2,980.00 USD | 0.00 USD | `+23.54%` | `24.83` |
| `Live` | `Short` | `120.45` | 17,590,000.00 USD | 145.74 USD | 0.00 USD | `+23.85%` | `1.21` |
| `Live` | `Short` | `120.55` | 17,590,000.00 USD | 1,190.00 USD | 0.00 USD | `+23.95%` | `9.86` |
| `Live` | `Short` | `120.65` | 17,650,000.00 USD | 60,330.00 USD | 0.00 USD | `+24.06%` | `500.00` |
| `Live` | `Short` | `120.95` | 17,670,000.00 USD | 13,290.00 USD | 0.00 USD | `+24.36%` | `109.91` |
| `Live` | `Short` | `121.15` | 17,670,000.00 USD | 316.20 USD | 0.00 USD | `+24.57%` | `2.61` |
| `Live` | `Short` | `121.25` | 17,670,000.00 USD | 1,550.00 USD | 0.00 USD | `+24.67%` | `12.80` |
| `Live` | `Short` | `121.55` | 17,680,000.00 USD | 6,460.00 USD | 0.00 USD | `+24.98%` | `53.14` |
| `Live` | `Short` | `121.75` | 17,680,000.00 USD | 105.92 USD | 0.00 USD | `+25.19%` | `0.87` |
| `Live` | `Short` | `122.05` | 17,730,000.00 USD | 56,150.00 USD | 0.00 USD | `+25.49%` | `460.06` |
| `Live` | `Short` | `122.15` | 17,730,000.00 USD | 169.79 USD | 0.00 USD | `+25.60%` | `1.39` |
| `Live` | `Short` | `122.25` | 18,620,000.00 USD | 883,070.00 USD | 0.00 USD | `+25.70%` | `7,223.45` |
| `Live` | `Short` | `122.45` | 18,630,000.00 USD | 17,500.00 USD | 0.00 USD | `+25.91%` | `142.95` |
| `Live` | `Short` | `122.65` | 18,630,000.00 USD | 116.52 USD | 0.00 USD | `+26.11%` | `0.95` |
| `Live` | `Short` | `123.25` | 19,110,000.00 USD | 472,220.00 USD | 0.00 USD | `+26.73%` | `3,831.37` |
| `Live` | `Short` | `123.35` | 19,110,000.00 USD | 2,330.00 USD | 0.00 USD | `+26.83%` | `18.92` |
| `Live` | `Short` | `123.45` | 19,230,000.00 USD | 126,270.00 USD | 0.00 USD | `+26.93%` | `1,022.83` |
| `Live` | `Short` | `123.65` | 19,240,000.00 USD | 6,680.00 USD | 0.00 USD | `+27.14%` | `54.05` |
| `Live` | `Short` | `124.05` | 19,240,000.00 USD | 586.76 USD | 0.00 USD | `+27.55%` | `4.73` |
| `Live` | `Short` | `124.15` | 19,240,000.00 USD | 121.67 USD | 0.00 USD | `+27.65%` | `0.98` |
| `Live` | `Short` | `124.25` | 19,260,000.00 USD | 23,360.00 USD | 0.00 USD | `+27.76%` | `188.01` |
| `Live` | `Short` | `124.35` | 19,290,000.00 USD | 29,710.00 USD | 0.00 USD | `+27.86%` | `238.96` |
| `Live` | `Short` | `124.45` | 19,340,000.00 USD | 46,110.00 USD | 0.00 USD | `+27.96%` | `370.50` |
| `Live` | `Short` | `124.55` | 19,340,000.00 USD | 3,080.00 USD | 0.00 USD | `+28.07%` | `24.76` |
| `Live` | `Short` | `124.65` | 19,340,000.00 USD | 675.60 USD | 0.00 USD | `+28.17%` | `5.42` |
| `Live` | `Short` | `124.75` | 19,350,000.00 USD | 6,020.00 USD | 0.00 USD | `+28.27%` | `48.24` |
| `Live` | `Short` | `124.95` | 19,350,000.00 USD | 3,500.00 USD | 0.00 USD | `+28.48%` | `28.05` |
| `Live` | `Short` | `125.05` | 19,350,000.00 USD | 208.83 USD | 0.00 USD | `+28.58%` | `1.67` |
| `Live` | `Short` | `125.15` | 19,820,000.00 USD | 462,650.00 USD | 0.00 USD | `+28.68%` | `3,696.78` |
| `Live` | `Short` | `125.35` | 19,820,000.00 USD | 5,320.00 USD | 0.00 USD | `+28.89%` | `42.44` |
| `Live` | `Short` | `125.45` | 19,820,000.00 USD | 590.87 USD | 0.00 USD | `+28.99%` | `4.71` |
| `Live` | `Short` | `125.55` | 19,830,000.00 USD | 4,610.00 USD | 0.00 USD | `+29.09%` | `36.71` |
| `Live` | `Short` | `125.65` | 19,830,000.00 USD | 1,560.00 USD | 0.00 USD | `+29.20%` | `12.41` |
| `Live` | `Short` | `125.75` | 19,830,000.00 USD | 1,930.00 USD | 0.00 USD | `+29.30%` | `15.31` |
| `Live` | `Short` | `125.85` | 19,890,000.00 USD | 57,880.00 USD | 0.00 USD | `+29.40%` | `459.90` |
| `Live` | `Short` | `125.95` | 19,890,000.00 USD | 110.84 USD | 0.00 USD | `+29.50%` | `0.88` |
| `Live` | `Short` | `126.05` | 19,890,000.00 USD | 810.50 USD | 0.00 USD | `+29.61%` | `6.43` |
| `Live` | `Short` | `126.15` | 19,890,000.00 USD | 470.54 USD | 0.00 USD | `+29.71%` | `3.73` |
| `Live` | `Short` | `126.35` | 19,890,000.00 USD | 4,090.00 USD | 0.00 USD | `+29.92%` | `32.36` |
| `Live` | `Short` | `126.45` | 19,900,000.00 USD | 5,000.00 USD | 0.00 USD | `+30.02%` | `39.56` |
| `Live` | `Short` | `126.65` | 19,930,000.00 USD | 30,830.00 USD | 0.00 USD | `+30.22%` | `243.46` |
| `Live` | `Short` | `126.75` | 19,940,000.00 USD | 10,650.00 USD | 0.00 USD | `+30.33%` | `84.00` |
| `Live` | `Short` | `126.85` | 19,940,000.00 USD | 3,870.00 USD | 0.00 USD | `+30.43%` | `30.49` |
| `Live` | `Short` | `127.05` | 20,210,000.00 USD | 262,490.00 USD | 0.00 USD | `+30.64%` | `2,066.01` |
| `Live` | `Short` | `127.15` | 20,210,000.00 USD | 389.08 USD | 0.00 USD | `+30.74%` | `3.06` |
| `Live` | `Short` | `127.35` | 26,820,000.00 USD | 6,610,000.00 USD | 0.00 USD | `+30.94%` | `51,921.31` |
| `Live` | `Short` | `127.55` | 26,960,000.00 USD | 139,870.00 USD | 0.00 USD | `+31.15%` | `1,096.61` |
| `Live` | `Short` | `127.65` | 26,960,000.00 USD | 4,840.00 USD | 0.00 USD | `+31.25%` | `37.89` |
| `Live` | `Short` | `127.75` | 26,990,000.00 USD | 20,800.00 USD | 0.00 USD | `+31.36%` | `162.83` |
| `Live` | `Short` | `127.85` | 26,990,000.00 USD | 388.66 USD | 0.00 USD | `+31.46%` | `3.04` |
| `Live` | `Short` | `127.95` | 27,000,000.00 USD | 10,510.00 USD | 0.00 USD | `+31.56%` | `82.13` |
| `Live` | `Short` | `128.05` | 27,110,000.00 USD | 116,190.00 USD | 0.00 USD | `+31.66%` | `907.38` |
| `Live` | `Short` | `128.35` | 27,110,000.00 USD | 195.09 USD | 0.00 USD | `+31.97%` | `1.52` |
| `Live` | `Short` | `128.45` | 27,110,000.00 USD | 783.54 USD | 0.00 USD | `+32.08%` | `6.10` |
| `Live` | `Short` | `128.65` | 27,110,000.00 USD | 788.62 USD | 0.00 USD | `+32.28%` | `6.13` |
| `Live` | `Short` | `128.75` | 27,130,000.00 USD | 18,730.00 USD | 0.00 USD | `+32.38%` | `145.45` |
| `Live` | `Short` | `128.85` | 27,170,000.00 USD | 32,440.00 USD | 0.00 USD | `+32.49%` | `251.77` |
| `Live` | `Short` | `129.15` | 27,220,000.00 USD | 55,570.00 USD | 0.00 USD | `+32.80%` | `430.25` |
| `Live` | `Short` | `129.25` | 27,250,000.00 USD | 32,310.00 USD | 0.00 USD | `+32.90%` | `250.00` |
| `Live` | `Short` | `129.35` | 27,950,000.00 USD | 699,390.00 USD | 0.00 USD | `+33.00%` | `5,406.93` |
| `Live` | `Short` | `129.55` | 27,950,000.00 USD | 2,590.00 USD | 0.00 USD | `+33.21%` | `19.96` |
| `Live` | `Short` | `129.75` | 28,030,000.00 USD | 71,060.00 USD | 0.00 USD | `+33.41%` | `547.66` |
| `Live` | `Short` | `129.85` | 28,030,000.00 USD | 490.83 USD | 0.00 USD | `+33.51%` | `3.78` |
| `Live` | `Short` | `130.25` | 28,040,000.00 USD | 13,200.00 USD | 0.00 USD | `+33.93%` | `101.38` |
| `Live` | `Short` | `130.35` | 28,040,000.00 USD | 145.99 USD | 0.00 USD | `+34.03%` | `1.12` |
| `Live` | `Short` | `130.65` | 28,040,000.00 USD | 866.21 USD | 0.00 USD | `+34.34%` | `6.63` |
| `Live` | `Short` | `130.75` | 28,040,000.00 USD | 132.06 USD | 0.00 USD | `+34.44%` | `1.01` |
| `Live` | `Short` | `130.85` | 28,040,000.00 USD | 3,180.00 USD | 0.00 USD | `+34.54%` | `24.34` |
| `Live` | `Short` | `130.95` | 28,050,000.00 USD | 2,070.00 USD | 0.00 USD | `+34.65%` | `15.84` |
| `Live` | `Short` | `131.05` | 28,050,000.00 USD | 188.71 USD | 0.00 USD | `+34.75%` | `1.44` |
| `Live` | `Short` | `131.25` | 28,050,000.00 USD | 1,560.00 USD | 0.00 USD | `+34.95%` | `11.87` |
| `Live` | `Short` | `131.45` | 28,050,000.00 USD | 219.52 USD | 0.00 USD | `+35.16%` | `1.67` |
| `Live` | `Short` | `131.85` | 28,050,000.00 USD | 3,100.00 USD | 0.00 USD | `+35.57%` | `23.54` |
| `Live` | `Short` | `131.95` | 28,050,000.00 USD | 3,710.00 USD | 0.00 USD | `+35.67%` | `28.10` |
| `Live` | `Short` | `132.05` | 28,070,000.00 USD | 11,940.00 USD | 0.00 USD | `+35.78%` | `90.43` |
| `Live` | `Short` | `132.15` | 28,070,000.00 USD | 325.09 USD | 0.00 USD | `+35.88%` | `2.46` |
| `Live` | `Short` | `132.55` | 28,080,000.00 USD | 8,730.00 USD | 0.00 USD | `+36.29%` | `65.85` |
| `Live` | `Short` | `132.65` | 28,080,000.00 USD | 240.10 USD | 0.00 USD | `+36.39%` | `1.81` |
| `Live` | `Short` | `132.85` | 28,130,000.00 USD | 49,280.00 USD | 0.00 USD | `+36.60%` | `370.98` |
| `Live` | `Short` | `133.05` | 28,160,000.00 USD | 30,050.00 USD | 0.00 USD | `+36.81%` | `225.86` |
| `Live` | `Short` | `133.15` | 28,170,000.00 USD | 10,040.00 USD | 0.00 USD | `+36.91%` | `75.39` |
| `Live` | `Short` | `133.25` | 28,170,000.00 USD | 1,330.00 USD | 0.00 USD | `+37.01%` | `9.95` |
| `Live` | `Short` | `133.35` | 28,170,000.00 USD | 390.72 USD | 0.00 USD | `+37.11%` | `2.93` |
| `Live` | `Short` | `133.65` | 28,170,000.00 USD | 156.37 USD | 0.00 USD | `+37.42%` | `1.17` |
| `Live` | `Short` | `133.75` | 28,320,000.00 USD | 151,200.00 USD | 0.00 USD | `+37.53%` | `1,130.50` |
| `Live` | `Short` | `133.95` | 28,320,000.00 USD | 503.65 USD | 0.00 USD | `+37.73%` | `3.76` |
| `Live` | `Short` | `134.05` | 28,330,000.00 USD | 12,620.00 USD | 0.00 USD | `+37.83%` | `94.18` |
| `Live` | `Short` | `134.25` | 28,340,000.00 USD | 11,590.00 USD | 0.00 USD | `+38.04%` | `86.32` |
| `Live` | `Short` | `134.65` | 28,410,000.00 USD | 67,330.00 USD | 0.00 USD | `+38.45%` | `500.00` |
| `Live` | `Short` | `135.35` | 28,410,000.00 USD | 414.17 USD | 0.00 USD | `+39.17%` | `3.06` |
| `Live` | `Short` | `135.75` | 28,420,000.00 USD | 6,420.00 USD | 0.00 USD | `+39.58%` | `47.30` |
| `Live` | `Short` | `135.85` | 28,420,000.00 USD | 3,250.00 USD | 0.00 USD | `+39.68%` | `23.94` |
| `Live` | `Short` | `135.95` | 28,470,000.00 USD | 49,400.00 USD | 0.00 USD | `+39.79%` | `363.35` |
| `Live` | `Short` | `136.15` | 28,480,000.00 USD | 14,640.00 USD | 0.00 USD | `+39.99%` | `107.50` |
| `Live` | `Short` | `136.35` | 28,490,000.00 USD | 8,690.00 USD | 0.00 USD | `+40.20%` | `63.73` |
| `Live` | `Short` | `136.55` | 28,490,000.00 USD | 136.55 USD | 0.00 USD | `+40.40%` | `1.00` |
| `Live` | `Short` | `136.65` | 28,490,000.00 USD | 1,110.00 USD | 0.00 USD | `+40.51%` | `8.14` |
| `Live` | `Short` | `136.75` | 28,500,000.00 USD | 4,090.00 USD | 0.00 USD | `+40.61%` | `29.93` |
| `Live` | `Short` | `136.95` | 28,530,000.00 USD | 34,240.00 USD | 0.00 USD | `+40.82%` | `250.00` |
| `Live` | `Short` | `137.05` | 28,530,000.00 USD | 836.00 USD | 0.00 USD | `+40.92%` | `6.10` |
| `Live` | `Short` | `137.15` | 28,540,000.00 USD | 2,220.00 USD | 0.00 USD | `+41.02%` | `16.16` |
| `Live` | `Short` | `137.35` | 28,550,000.00 USD | 18,410.00 USD | 0.00 USD | `+41.23%` | `134.01` |
| `Live` | `Short` | `137.55` | 28,560,000.00 USD | 697.38 USD | 0.00 USD | `+41.43%` | `5.07` |
| `Live` | `Short` | `137.95` | 28,560,000.00 USD | 2,050.00 USD | 0.00 USD | `+41.84%` | `14.87` |
| `Live` | `Short` | `138.05` | 28,560,000.00 USD | 4,090.00 USD | 0.00 USD | `+41.95%` | `29.62` |
| `Live` | `Short` | `138.15` | 28,600,000.00 USD | 41,450.00 USD | 0.00 USD | `+42.05%` | `300.00` |
| `Live` | `Short` | `138.25` | 28,650,000.00 USD | 45,220.00 USD | 0.00 USD | `+42.15%` | `327.11` |
| `Live` | `Short` | `138.45` | 28,660,000.00 USD | 7,310.00 USD | 0.00 USD | `+42.36%` | `52.83` |
| `Live` | `Short` | `138.75` | 28,660,000.00 USD | 2,360.00 USD | 0.00 USD | `+42.67%` | `17.04` |
| `Live` | `Short` | `139.15` | 28,660,000.00 USD | 552.43 USD | 0.00 USD | `+43.08%` | `3.97` |
| `Live` | `Short` | `139.35` | 28,660,000.00 USD | 4,180.00 USD | 0.00 USD | `+43.28%` | `30.00` |
| `Live` | `Short` | `139.45` | 28,660,000.00 USD | 253.80 USD | 0.00 USD | `+43.39%` | `1.82` |
| `Live` | `Short` | `139.55` | 28,660,000.00 USD | 494.01 USD | 0.00 USD | `+43.49%` | `3.54` |
| `Live` | `Short` | `139.65` | 28,660,000.00 USD | 1,680.00 USD | 0.00 USD | `+43.59%` | `12.02` |
| `Live` | `Short` | `139.75` | 28,670,000.00 USD | 4,870.00 USD | 0.00 USD | `+43.69%` | `34.82` |
| `Live` | `Short` | `139.95` | 28,670,000.00 USD | 394.66 USD | 0.00 USD | `+43.90%` | `2.82` |
| `Live` | `Short` | `140.05` | 28,670,000.00 USD | 116.24 USD | 0.00 USD | `+44.00%` | `0.83` |
| `Live` | `Short` | `140.35` | 28,670,000.00 USD | 158.60 USD | 0.00 USD | `+44.31%` | `1.13` |
| `Live` | `Short` | `140.45` | 28,680,000.00 USD | 4,870.00 USD | 0.00 USD | `+44.41%` | `34.66` |
| `Live` | `Short` | `140.55` | 28,680,000.00 USD | 1,330.00 USD | 0.00 USD | `+44.52%` | `9.46` |
| `Live` | `Short` | `140.65` | 28,680,000.00 USD | 7,340.00 USD | 0.00 USD | `+44.62%` | `52.16` |
| `Live` | `Short` | `140.85` | 33,850,000.00 USD | 5,160,000.00 USD | 0.00 USD | `+44.83%` | `36,668.16` |
| `Live` | `Short` | `140.95` | 33,850,000.00 USD | 1,940.00 USD | 0.00 USD | `+44.93%` | `13.73` |
| `Live` | `Short` | `141.05` | 33,850,000.00 USD | 3,080.00 USD | 0.00 USD | `+45.03%` | `21.83` |
| `Live` | `Short` | `141.35` | 33,850,000.00 USD | 210.61 USD | 0.00 USD | `+45.34%` | `1.49` |
| `Live` | `Short` | `141.45` | 34,100,000.00 USD | 247,540.00 USD | 0.00 USD | `+45.44%` | `1,750.00` |
| `Live` | `Short` | `141.55` | 36,050,000.00 USD | 1,950,000.00 USD | 0.00 USD | `+45.55%` | `13,746.29` |
| `Live` | `Short` | `141.65` | 36,050,000.00 USD | 211.06 USD | 0.00 USD | `+45.65%` | `1.49` |
| `Live` | `Short` | `141.75` | 36,050,000.00 USD | 4,780.00 USD | 0.00 USD | `+45.75%` | `33.73` |
| `Live` | `Short` | `141.95` | 36,080,000.00 USD | 23,020.00 USD | 0.00 USD | `+45.96%` | `162.19` |
| `Live` | `Short` | `142.05` | 36,080,000.00 USD | 782.70 USD | 0.00 USD | `+46.06%` | `5.51` |
| `Live` | `Short` | `142.25` | 36,080,000.00 USD | 3,470.00 USD | 0.00 USD | `+46.26%` | `24.41` |
| `Live` | `Short` | `142.45` | 36,080,000.00 USD | 151.00 USD | 0.00 USD | `+46.47%` | `1.06` |
| `Live` | `Short` | `142.75` | 36,080,000.00 USD | 368.30 USD | 0.00 USD | `+46.78%` | `2.58` |
| `Live` | `Short` | `143.15` | 36,170,000.00 USD | 90,580.00 USD | 0.00 USD | `+47.19%` | `632.77` |
| `Live` | `Short` | `143.25` | 36,170,000.00 USD | 2,830.00 USD | 0.00 USD | `+47.29%` | `19.75` |
| `Live` | `Short` | `143.35` | 36,240,000.00 USD | 64,570.00 USD | 0.00 USD | `+47.40%` | `450.46` |
| `Live` | `Short` | `143.55` | 36,240,000.00 USD | 103.36 USD | 0.00 USD | `+47.60%` | `0.72` |
| `Live` | `Short` | `143.95` | 36,840,000.00 USD | 597,390.00 USD | 0.00 USD | `+48.01%` | `4,150.00` |
| `Live` | `Short` | `144.05` | 36,840,000.00 USD | 3,750.00 USD | 0.00 USD | `+48.12%` | `26.00` |
| `Live` | `Short` | `144.15` | 36,860,000.00 USD | 23,300.00 USD | 0.00 USD | `+48.22%` | `161.66` |
| `Live` | `Short` | `144.55` | 36,860,000.00 USD | 602.77 USD | 0.00 USD | `+48.63%` | `4.17` |
| `Live` | `Short` | `144.65` | 36,870,000.00 USD | 3,260.00 USD | 0.00 USD | `+48.73%` | `22.52` |
| `Live` | `Short` | `144.75` | 36,940,000.00 USD | 72,380.00 USD | 0.00 USD | `+48.84%` | `500.00` |
| `Live` | `Short` | `145.15` | 36,940,000.00 USD | 1,760.00 USD | 0.00 USD | `+49.25%` | `12.12` |
| `Live` | `Short` | `145.35` | 37,050,000.00 USD | 106,270.00 USD | 0.00 USD | `+49.45%` | `731.14` |
| `Live` | `Short` | `145.45` | 37,080,000.00 USD | 28,990.00 USD | 0.00 USD | `+49.56%` | `199.30` |
| `Live` | `Short` | `145.65` | 37,080,000.00 USD | 145.65 USD | 0.00 USD | `+49.76%` | `1.00` |
| `Live` | `Short` | `145.85` | 37,080,000.00 USD | 5,850.00 USD | 0.00 USD | `+49.97%` | `40.09` |
| `Live` | `Short` | `145.95` | 37,080,000.00 USD | 490.39 USD | 0.00 USD | `+50.07%` | `3.36` |
| `Live` | `Short` | `146.15` | 37,170,000.00 USD | 88,760.00 USD | 0.00 USD | `+50.28%` | `607.33` |
| `Live` | `Short` | `146.25` | 37,170,000.00 USD | 4,050.00 USD | 0.00 USD | `+50.38%` | `27.70` |
| `Live` | `Short` | `146.35` | 37,180,000.00 USD | 7,330.00 USD | 0.00 USD | `+50.48%` | `50.10` |
| `Live` | `Short` | `146.55` | 37,200,000.00 USD | 17,380.00 USD | 0.00 USD | `+50.69%` | `118.57` |
| `Live` | `Short` | `146.65` | 37,790,000.00 USD | 587,730.00 USD | 0.00 USD | `+50.79%` | `4,007.68` |
| `Live` | `Short` | `146.75` | 37,790,000.00 USD | 2,110.00 USD | 0.00 USD | `+50.89%` | `14.41` |
| `Live` | `Short` | `146.95` | 37,870,000.00 USD | 78,060.00 USD | 0.00 USD | `+51.10%` | `531.18` |
| `Live` | `Short` | `147.05` | 37,870,000.00 USD | 166.17 USD | 0.00 USD | `+51.20%` | `1.13` |
| `Live` | `Short` | `147.15` | 37,870,000.00 USD | 1,730.00 USD | 0.00 USD | `+51.30%` | `11.75` |
| `Live` | `Short` | `147.35` | 37,870,000.00 USD | 169.45 USD | 0.00 USD | `+51.51%` | `1.15` |
| `Live` | `Short` | `147.45` | 37,870,000.00 USD | 204.96 USD | 0.00 USD | `+51.61%` | `1.39` |
| `Live` | `Short` | `147.55` | 37,870,000.00 USD | 1,000.00 USD | 0.00 USD | `+51.71%` | `6.78` |
| `Live` | `Short` | `147.65` | 37,870,000.00 USD | 237.72 USD | 0.00 USD | `+51.82%` | `1.61` |
| `Live` | `Short` | `147.85` | 37,870,000.00 USD | 578.09 USD | 0.00 USD | `+52.02%` | `3.91` |
| `Live` | `Short` | `148.15` | 37,990,000.00 USD | 122,350.00 USD | 0.00 USD | `+52.33%` | `825.82` |
| `Live` | `Short` | `148.25` | 38,070,000.00 USD | 78,630.00 USD | 0.00 USD | `+52.43%` | `530.42` |
| `Live` | `Short` | `148.35` | 38,520,000.00 USD | 445,050.00 USD | 0.00 USD | `+52.54%` | `3,000.00` |
| `Live` | `Short` | `148.45` | 39,040,000.00 USD | 519,740.00 USD | 0.00 USD | `+52.64%` | `3,501.10` |
| `Live` | `Short` | `148.55` | 39,410,000.00 USD | 373,600.00 USD | 0.00 USD | `+52.74%` | `2,515.00` |
| `Live` | `Short` | `148.65` | 39,420,000.00 USD | 5,650.00 USD | 0.00 USD | `+52.85%` | `38.00` |
| `Live` | `Short` | `148.75` | 39,510,000.00 USD | 93,700.00 USD | 0.00 USD | `+52.95%` | `629.91` |
| `Live` | `Short` | `149.05` | 39,510,000.00 USD | 1,120.00 USD | 0.00 USD | `+53.26%` | `7.50` |
| `Live` | `Short` | `149.35` | 40,900,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+53.57%` | `9,285.70` |
| `Live` | `Short` | `149.55` | 40,900,000.00 USD | 116.65 USD | 0.00 USD | `+53.77%` | `0.78` |
| `Live` | `Short` | `149.65` | 40,910,000.00 USD | 16,030.00 USD | 0.00 USD | `+53.87%` | `107.15` |
| `Live` | `Short` | `149.95` | 41,150,000.00 USD | 234,200.00 USD | 0.00 USD | `+54.18%` | `1,561.87` |
| `Live` | `Short` | `150.05` | 41,150,000.00 USD | 5,200.00 USD | 0.00 USD | `+54.29%` | `34.63` |
| `Live` | `Short` | `150.15` | 41,280,000.00 USD | 123,300.00 USD | 0.00 USD | `+54.39%` | `821.21` |
| `Live` | `Short` | `150.85` | 41,280,000.00 USD | 346.96 USD | 0.00 USD | `+55.11%` | `2.30` |
| `Live` | `Short` | `150.95` | 41,280,000.00 USD | 2,370.00 USD | 0.00 USD | `+55.21%` | `15.69` |
| `Live` | `Short` | `151.15` | 41,280,000.00 USD | 3,180.00 USD | 0.00 USD | `+55.42%` | `21.05` |
| `Live` | `Short` | `151.45` | 41,290,000.00 USD | 8,830.00 USD | 0.00 USD | `+55.72%` | `58.32` |
| `Live` | `Short` | `151.55` | 43,030,000.00 USD | 1,740,000.00 USD | 0.00 USD | `+55.83%` | `11,488.27` |
| `Live` | `Short` | `151.95` | 44,140,000.00 USD | 1,110,000.00 USD | 0.00 USD | `+56.24%` | `7,284.27` |
| `Live` | `Short` | `152.05` | 48,750,000.00 USD | 4,610,000.00 USD | 0.00 USD | `+56.34%` | `30,310.49` |
| `Live` | `Short` | `152.15` | 48,790,000.00 USD | 44,670.00 USD | 0.00 USD | `+56.44%` | `293.57` |
| `Live` | `Short` | `152.25` | 48,790,000.00 USD | 400.42 USD | 0.00 USD | `+56.55%` | `2.63` |
| `Live` | `Short` | `152.35` | 49,080,000.00 USD | 287,690.00 USD | 0.00 USD | `+56.65%` | `1,888.37` |
| `Live` | `Short` | `152.45` | 49,090,000.00 USD | 5,950.00 USD | 0.00 USD | `+56.75%` | `39.02` |
| `Live` | `Short` | `152.55` | 49,850,000.00 USD | 757,860.00 USD | 0.00 USD | `+56.86%` | `4,967.95` |
| `Live` | `Short` | `152.75` | 49,850,000.00 USD | 1,570.00 USD | 0.00 USD | `+57.06%` | `10.30` |
| `Live` | `Short` | `152.95` | 49,850,000.00 USD | 925.35 USD | 0.00 USD | `+57.27%` | `6.05` |
| `Live` | `Short` | `153.05` | 49,850,000.00 USD | 1,060.00 USD | 0.00 USD | `+57.37%` | `6.95` |
| `Live` | `Short` | `153.15` | 49,890,000.00 USD | 44,610.00 USD | 0.00 USD | `+57.47%` | `291.26` |
| `Live` | `Short` | `153.25` | 49,890,000.00 USD | 239.07 USD | 0.00 USD | `+57.58%` | `1.56` |
| `Live` | `Short` | `153.35` | 49,900,000.00 USD | 2,300.00 USD | 0.00 USD | `+57.68%` | `15.00` |
| `Live` | `Short` | `153.45` | 49,900,000.00 USD | 1,230.00 USD | 0.00 USD | `+57.78%` | `8.00` |
| `Live` | `Short` | `153.65` | 49,910,000.00 USD | 8,340.00 USD | 0.00 USD | `+57.99%` | `54.29` |
| `Live` | `Short` | `153.85` | 49,910,000.00 USD | 1,490.00 USD | 0.00 USD | `+58.19%` | `9.68` |
| `Live` | `Short` | `154.15` | 49,910,000.00 USD | 292.89 USD | 0.00 USD | `+58.50%` | `1.90` |
| `Live` | `Short` | `154.25` | 49,910,000.00 USD | 2,340.00 USD | 0.00 USD | `+58.60%` | `15.20` |
| `Live` | `Short` | `154.45` | 49,910,000.00 USD | 4,240.00 USD | 0.00 USD | `+58.81%` | `27.45` |
| `Live` | `Short` | `154.75` | 49,910,000.00 USD | 363.66 USD | 0.00 USD | `+59.12%` | `2.35` |
| `Live` | `Short` | `155.05` | 49,910,000.00 USD | 117.84 USD | 0.00 USD | `+59.43%` | `0.76` |
| `Live` | `Short` | `155.25` | 49,920,000.00 USD | 1,110.00 USD | 0.00 USD | `+59.63%` | `7.16` |
| `Live` | `Short` | `155.35` | 49,920,000.00 USD | 2,810.00 USD | 0.00 USD | `+59.73%` | `18.06` |
| `Live` | `Short` | `155.55` | 49,920,000.00 USD | 267.55 USD | 0.00 USD | `+59.94%` | `1.72` |
| `Live` | `Short` | `156.05` | 49,920,000.00 USD | 326.14 USD | 0.00 USD | `+60.45%` | `2.09` |
| `Live` | `Short` | `156.15` | 49,930,000.00 USD | 7,810.00 USD | 0.00 USD | `+60.56%` | `50.00` |
| `Live` | `Short` | `156.35` | 49,930,000.00 USD | 197.00 USD | 0.00 USD | `+60.76%` | `1.26` |
| `Live` | `Short` | `156.45` | 49,930,000.00 USD | 4,900.00 USD | 0.00 USD | `+60.87%` | `31.29` |
| `Live` | `Short` | `157.05` | 50,010,000.00 USD | 80,150.00 USD | 0.00 USD | `+61.48%` | `510.34` |
| `Live` | `Short` | `157.15` | 50,060,000.00 USD | 49,270.00 USD | 0.00 USD | `+61.59%` | `313.50` |
| `Live` | `Short` | `157.65` | 50,060,000.00 USD | 654.25 USD | 0.00 USD | `+62.10%` | `4.15` |
| `Live` | `Short` | `157.75` | 50,150,000.00 USD | 92,600.00 USD | 0.00 USD | `+62.20%` | `587.00` |
| `Live` | `Short` | `157.85` | 50,390,000.00 USD | 237,070.00 USD | 0.00 USD | `+62.31%` | `1,501.89` |
| `Live` | `Short` | `158.35` | 50,410,000.00 USD | 23,570.00 USD | 0.00 USD | `+62.82%` | `148.84` |
| `Live` | `Short` | `158.65` | 50,840,000.00 USD | 428,360.00 USD | 0.00 USD | `+63.13%` | `2,700.00` |
| `Live` | `Short` | `158.75` | 54,460,000.00 USD | 3,610,000.00 USD | 0.00 USD | `+63.23%` | `22,770.74` |
| `Live` | `Short` | `159.05` | 54,600,000.00 USD | 145,990.00 USD | 0.00 USD | `+63.54%` | `917.89` |
| `Live` | `Short` | `159.25` | 54,600,000.00 USD | 654.52 USD | 0.00 USD | `+63.74%` | `4.11` |
| `Live` | `Short` | `159.65` | 54,610,000.00 USD | 1,760.00 USD | 0.00 USD | `+64.16%` | `11.01` |
| `Live` | `Short` | `159.95` | 54,610,000.00 USD | 497.44 USD | 0.00 USD | `+64.46%` | `3.11` |
| `Live` | `Short` | `160.15` | 55,290,000.00 USD | 683,000.00 USD | 0.00 USD | `+64.67%` | `4,264.75` |
| `Live` | `Short` | `160.25` | 55,370,000.00 USD | 80,940.00 USD | 0.00 USD | `+64.77%` | `505.07` |
| `Live` | `Short` | `160.35` | 55,370,000.00 USD | 655.83 USD | 0.00 USD | `+64.88%` | `4.09` |
| `Live` | `Short` | `160.55` | 55,400,000.00 USD | 28,140.00 USD | 0.00 USD | `+65.08%` | `175.30` |
| `Live` | `Short` | `161.05` | 55,400,000.00 USD | 2,240.00 USD | 0.00 USD | `+65.60%` | `13.93` |
| `Live` | `Short` | `161.35` | 55,400,000.00 USD | 1,530.00 USD | 0.00 USD | `+65.90%` | `9.51` |
| `Live` | `Short` | `161.45` | 55,730,000.00 USD | 322,900.00 USD | 0.00 USD | `+66.01%` | `2,000.00` |
| `Live` | `Short` | `161.55` | 55,730,000.00 USD | 410.34 USD | 0.00 USD | `+66.11%` | `2.54` |
| `Live` | `Short` | `161.65` | 55,810,000.00 USD | 86,120.00 USD | 0.00 USD | `+66.21%` | `532.74` |
| `Live` | `Short` | `161.75` | 55,830,000.00 USD | 18,940.00 USD | 0.00 USD | `+66.32%` | `117.09` |
| `Live` | `Short` | `161.95` | 61,670,000.00 USD | 5,840,000.00 USD | 0.00 USD | `+66.52%` | `36,063.22` |
| `Live` | `Short` | `162.35` | 61,680,000.00 USD | 6,500.00 USD | 0.00 USD | `+66.93%` | `40.03` |
| `Live` | `Short` | `162.45` | 61,820,000.00 USD | 142,860.00 USD | 0.00 USD | `+67.04%` | `879.39` |
| `Live` | `Short` | `162.55` | 61,850,000.00 USD | 24,150.00 USD | 0.00 USD | `+67.14%` | `148.59` |
| `Live` | `Short` | `163.55` | 61,870,000.00 USD | 23,440.00 USD | 0.00 USD | `+68.17%` | `143.32` |
| `Live` | `Short` | `163.85` | 61,870,000.00 USD | 786.48 USD | 0.00 USD | `+68.47%` | `4.80` |
| `Live` | `Short` | `163.95` | 62,080,000.00 USD | 208,190.00 USD | 0.00 USD | `+68.58%` | `1,269.85` |
| `Live` | `Short` | `164.75` | 62,080,000.00 USD | 677.12 USD | 0.00 USD | `+69.40%` | `4.11` |
| `Live` | `Short` | `165.15` | 62,080,000.00 USD | 198.18 USD | 0.00 USD | `+69.81%` | `1.20` |
| `Live` | `Short` | `166.15` | 62,080,000.00 USD | 1,620.00 USD | 0.00 USD | `+70.84%` | `9.74` |
| `Live` | `Short` | `166.25` | 62,090,000.00 USD | 14,070.00 USD | 0.00 USD | `+70.94%` | `84.61` |
| `Live` | `Short` | `166.65` | 62,160,000.00 USD | 67,790.00 USD | 0.00 USD | `+71.35%` | `406.80` |
| `Live` | `Short` | `166.95` | 62,170,000.00 USD | 3,440.00 USD | 0.00 USD | `+71.66%` | `20.63` |
| `Live` | `Short` | `167.15` | 62,180,000.00 USD | 17,120.00 USD | 0.00 USD | `+71.87%` | `102.40` |
| `Live` | `Short` | `167.55` | 62,180,000.00 USD | 150.80 USD | 0.00 USD | `+72.28%` | `0.90` |
| `Live` | `Short` | `167.65` | 62,180,000.00 USD | 115.68 USD | 0.00 USD | `+72.38%` | `0.69` |
| `Live` | `Short` | `167.75` | 62,190,000.00 USD | 1,890.00 USD | 0.00 USD | `+72.48%` | `11.27` |
| `Live` | `Short` | `167.95` | 62,190,000.00 USD | 4,090.00 USD | 0.00 USD | `+72.69%` | `24.33` |
| `Live` | `Short` | `168.05` | 62,190,000.00 USD | 122.68 USD | 0.00 USD | `+72.79%` | `0.73` |
| `Live` | `Short` | `168.35` | 62,210,000.00 USD | 19,740.00 USD | 0.00 USD | `+73.10%` | `117.24` |
| `Live` | `Short` | `168.65` | 62,650,000.00 USD | 437,600.00 USD | 0.00 USD | `+73.41%` | `2,594.72` |
| `Live` | `Short` | `169.05` | 62,680,000.00 USD | 34,790.00 USD | 0.00 USD | `+73.82%` | `205.77` |
| `Live` | `Short` | `169.35` | 62,680,000.00 USD | 443.70 USD | 0.00 USD | `+74.13%` | `2.62` |
| `Live` | `Short` | `169.55` | 62,680,000.00 USD | 335.71 USD | 0.00 USD | `+74.34%` | `1.98` |
| `Live` | `Short` | `169.75` | 62,690,000.00 USD | 3,180.00 USD | 0.00 USD | `+74.54%` | `18.73` |
| `Live` | `Short` | `170.95` | 62,870,000.00 USD | 181,510.00 USD | 0.00 USD | `+75.78%` | `1,061.79` |
| `Live` | `Short` | `171.45` | 62,870,000.00 USD | 111.44 USD | 0.00 USD | `+76.29%` | `0.65` |
| `Live` | `Short` | `171.55` | 62,870,000.00 USD | 1,180.00 USD | 0.00 USD | `+76.39%` | `6.88` |
| `Live` | `Short` | `171.75` | 62,890,000.00 USD | 20,440.00 USD | 0.00 USD | `+76.60%` | `119.02` |
| `Live` | `Short` | `172.45` | 62,940,000.00 USD | 51,730.00 USD | 0.00 USD | `+77.32%` | `300.00` |
| `Live` | `Short` | `172.65` | 62,970,000.00 USD | 27,960.00 USD | 0.00 USD | `+77.52%` | `161.92` |
| `Live` | `Short` | `173.35` | 62,970,000.00 USD | 204.55 USD | 0.00 USD | `+78.24%` | `1.18` |
| `Live` | `Short` | `173.45` | 62,990,000.00 USD | 16,540.00 USD | 0.00 USD | `+78.35%` | `95.36` |
| `Live` | `Short` | `173.75` | 62,990,000.00 USD | 284.95 USD | 0.00 USD | `+78.65%` | `1.64` |
| `Live` | `Short` | `173.85` | 62,990,000.00 USD | 695.40 USD | 0.00 USD | `+78.76%` | `4.00` |
| `Live` | `Short` | `173.95` | 62,990,000.00 USD | 346.16 USD | 0.00 USD | `+78.86%` | `1.99` |
| `Live` | `Short` | `174.15` | 63,090,000.00 USD | 104,490.00 USD | 0.00 USD | `+79.07%` | `600.00` |
| `Live` | `Short` | `174.25` | 63,340,000.00 USD | 245,010.00 USD | 0.00 USD | `+79.17%` | `1,406.07` |
| `Live` | `Short` | `174.35` | 63,540,000.00 USD | 205,490.00 USD | 0.00 USD | `+79.27%` | `1,178.60` |
| `Live` | `Short` | `174.75` | 63,540,000.00 USD | 146.79 USD | 0.00 USD | `+79.68%` | `0.84` |
| `Live` | `Short` | `174.85` | 102,010,000.00 USD | 38,470,000.00 USD | 0.00 USD | `+79.79%` | `220,000.19` |
| `Live` | `Short` | `175.15` | 102,010,000.00 USD | 238.20 USD | 0.00 USD | `+80.09%` | `1.36` |
| `Live` | `Short` | `175.45` | 102,010,000.00 USD | 119.31 USD | 0.00 USD | `+80.40%` | `0.68` |
| `Live` | `Short` | `175.75` | 102,010,000.00 USD | 263.62 USD | 0.00 USD | `+80.71%` | `1.50` |
| `Live` | `Short` | `175.85` | 102,110,000.00 USD | 105,510.00 USD | 0.00 USD | `+80.81%` | `600.00` |
| `Live` | `Short` | `175.95` | 102,130,000.00 USD | 19,890.00 USD | 0.00 USD | `+80.92%` | `113.07` |
| `Live` | `Short` | `176.05` | 102,130,000.00 USD | 123.23 USD | 0.00 USD | `+81.02%` | `0.70` |
| `Live` | `Short` | `176.25` | 102,140,000.00 USD | 625.69 USD | 0.00 USD | `+81.22%` | `3.55` |
| `Live` | `Short` | `176.35` | 105,660,000.00 USD | 3,530,000.00 USD | 0.00 USD | `+81.33%` | `20,000.00` |
| `Live` | `Short` | `176.65` | 105,690,000.00 USD | 25,540.00 USD | 0.00 USD | `+81.64%` | `144.60` |
| `Live` | `Short` | `176.75` | 105,690,000.00 USD | 1,300.00 USD | 0.00 USD | `+81.74%` | `7.37` |
| `Live` | `Short` | `176.85` | 105,690,000.00 USD | 4,420.00 USD | 0.00 USD | `+81.84%` | `25.00` |
| `Live` | `Short` | `177.55` | 105,960,000.00 USD | 267,040.00 USD | 0.00 USD | `+82.56%` | `1,504.00` |
| `Live` | `Short` | `177.65` | 105,970,000.00 USD | 4,320.00 USD | 0.00 USD | `+82.66%` | `24.29` |
| `Live` | `Short` | `177.75` | 106,170,000.00 USD | 208,810.00 USD | 0.00 USD | `+82.77%` | `1,174.72` |
| `Live` | `Short` | `177.85` | 106,170,000.00 USD | 277.45 USD | 0.00 USD | `+82.87%` | `1.56` |
| `Live` | `Short` | `177.95` | 106,250,000.00 USD | 78,300.00 USD | 0.00 USD | `+82.97%` | `440.00` |
| `Live` | `Short` | `178.05` | 106,390,000.00 USD | 142,440.00 USD | 0.00 USD | `+83.08%` | `800.00` |
| `Live` | `Short` | `179.05` | 106,400,000.00 USD | 4,970.00 USD | 0.00 USD | `+84.10%` | `27.73` |
| `Live` | `Short` | `179.65` | 106,440,000.00 USD | 44,930.00 USD | 0.00 USD | `+84.72%` | `250.10` |
| `Live` | `Short` | `179.85` | 107,490,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+84.93%` | `5,800.00` |
| `Live` | `Short` | `180.15` | 108,830,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+85.23%` | `7,450.28` |
| `Live` | `Short` | `180.55` | 108,870,000.00 USD | 38,150.00 USD | 0.00 USD | `+85.65%` | `211.32` |
| `Live` | `Short` | `181.25` | 108,890,000.00 USD | 19,490.00 USD | 0.00 USD | `+86.37%` | `107.52` |
| `Live` | `Short` | `181.55` | 108,890,000.00 USD | 254.17 USD | 0.00 USD | `+86.67%` | `1.40` |
| `Live` | `Short` | `182.05` | 108,980,000.00 USD | 91,030.00 USD | 0.00 USD | `+87.19%` | `500.00` |
| `Live` | `Short` | `182.15` | 108,980,000.00 USD | 3,990.00 USD | 0.00 USD | `+87.29%` | `21.93` |
| `Live` | `Short` | `182.35` | 109,060,000.00 USD | 72,940.00 USD | 0.00 USD | `+87.50%` | `400.00` |
| `Live` | `Short` | `182.45` | 109,070,000.00 USD | 9,440.00 USD | 0.00 USD | `+87.60%` | `51.72` |
| `Live` | `Short` | `183.05` | 112,730,000.00 USD | 3,660,000.00 USD | 0.00 USD | `+88.22%` | `20,000.00` |
| `Live` | `Short` | `184.15` | 112,730,000.00 USD | 793.69 USD | 0.00 USD | `+89.35%` | `4.31` |
| `Live` | `Short` | `184.25` | 112,730,000.00 USD | 1,680.00 USD | 0.00 USD | `+89.45%` | `9.12` |
| `Live` | `Short` | `184.95` | 112,890,000.00 USD | 165,230.00 USD | 0.00 USD | `+90.17%` | `893.35` |
| `Live` | `Short` | `185.15` | 112,900,000.00 USD | 7,670.00 USD | 0.00 USD | `+90.38%` | `41.43` |
| `Live` | `Short` | `185.25` | 112,900,000.00 USD | 737.29 USD | 0.00 USD | `+90.48%` | `3.98` |
| `Live` | `Short` | `185.45` | 112,960,000.00 USD | 56,050.00 USD | 0.00 USD | `+90.68%` | `302.24` |
| `Live` | `Short` | `185.55` | 112,960,000.00 USD | 1,220.00 USD | 0.00 USD | `+90.79%` | `6.56` |
| `Live` | `Short` | `185.65` | 112,970,000.00 USD | 11,090.00 USD | 0.00 USD | `+90.89%` | `59.74` |
| `Live` | `Short` | `186.85` | 112,970,000.00 USD | 2,190.00 USD | 0.00 USD | `+92.12%` | `11.72` |
| `Live` | `Short` | `187.55` | 112,970,000.00 USD | 232.56 USD | 0.00 USD | `+92.84%` | `1.24` |
| `Live` | `Short` | `187.75` | 112,980,000.00 USD | 2,460.00 USD | 0.00 USD | `+93.05%` | `13.11` |
| `Live` | `Short` | `187.85` | 112,990,000.00 USD | 14,260.00 USD | 0.00 USD | `+93.15%` | `75.92` |
| `Live` | `Short` | `188.15` | 112,990,000.00 USD | 997.20 USD | 0.00 USD | `+93.46%` | `5.30` |
| `Live` | `Short` | `188.55` | 112,990,000.00 USD | 231.92 USD | 0.00 USD | `+93.87%` | `1.23` |
| `Live` | `Short` | `188.65` | 113,020,000.00 USD | 29,110.00 USD | 0.00 USD | `+93.97%` | `154.32` |
| `Live` | `Short` | `188.75` | 113,020,000.00 USD | 4,070.00 USD | 0.00 USD | `+94.08%` | `21.57` |
| `Live` | `Short` | `188.95` | 113,030,000.00 USD | 1,450.00 USD | 0.00 USD | `+94.28%` | `7.69` |
| `Live` | `Short` | `189.25` | 113,030,000.00 USD | 456.09 USD | 0.00 USD | `+94.59%` | `2.41` |
| `Live` | `Short` | `189.85` | 113,030,000.00 USD | 189.85 USD | 0.00 USD | `+95.21%` | `1.00` |
| `Live` | `Short` | `189.95` | 113,310,000.00 USD | 284,930.00 USD | 0.00 USD | `+95.31%` | `1,500.00` |
| `Live` | `Short` | `190.15` | 113,310,000.00 USD | 148.32 USD | 0.00 USD | `+95.52%` | `0.78` |
| `Live` | `Short` | `190.45` | 113,310,000.00 USD | 118.08 USD | 0.00 USD | `+95.83%` | `0.62` |
| `Live` | `Short` | `190.55` | 113,310,000.00 USD | 118.14 USD | 0.00 USD | `+95.93%` | `0.62` |
| `Live` | `Short` | `190.95` | 126,880,000.00 USD | 13,570,000.00 USD | 0.00 USD | `+96.34%` | `71,044.42` |
| `Live` | `Short` | `191.35` | 126,950,000.00 USD | 68,210.00 USD | 0.00 USD | `+96.75%` | `356.45` |
| `Live` | `Short` | `191.85` | 127,330,000.00 USD | 383,700.00 USD | 0.00 USD | `+97.26%` | `2,000.00` |
| `Live` | `Short` | `191.95` | 127,330,000.00 USD | 514.43 USD | 0.00 USD | `+97.37%` | `2.68` |
| `Live` | `Short` | `192.15` | 128,200,000.00 USD | 872,340.00 USD | 0.00 USD | `+97.57%` | `4,539.90` |
| `Live` | `Short` | `192.25` | 128,200,000.00 USD | 280.69 USD | 0.00 USD | `+97.68%` | `1.46` |
| `Live` | `Short` | `193.15` | 128,210,000.00 USD | 2,170.00 USD | 0.00 USD | `+98.60%` | `11.24` |
| `Live` | `Short` | `193.55` | 128,320,000.00 USD | 114,580.00 USD | 0.00 USD | `+99.01%` | `592.00` |
| `Live` | `Short` | `194.05` | 128,340,000.00 USD | 19,910.00 USD | 0.00 USD | `+99.53%` | `102.58` |
| `Live` | `Short` | `194.15` | 128,340,000.00 USD | 1,380.00 USD | 0.00 USD | `+99.63%` | `7.13` |
| `Live` | `Short` | `194.25` | 128,350,000.00 USD | 9,380.00 USD | 0.00 USD | `+99.73%` | `48.28` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 9,380,000.00 USD | 0.00 USD | 14,230.00 USD | `-76.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 9,360,000.00 USD | 0.00 USD | 499.56 USD | `-68.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `32.05` | 9,360,000.00 USD | 0.00 USD | 1,230.00 USD | `-67.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 9,360,000.00 USD | 0.00 USD | 818.32 USD | `-66.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 9,360,000.00 USD | 0.00 USD | 1,340.00 USD | `-64.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 9,360,000.00 USD | 0.00 USD | 2,160.00 USD | `-62.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.45` | 9,360,000.00 USD | 0.00 USD | 434.85 USD | `-62.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.05` | 9,360,000.00 USD | 0.00 USD | 267.87 USD | `-60.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 9,360,000.00 USD | 0.00 USD | 3,460.00 USD | `-59.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 9,350,000.00 USD | 0.00 USD | 157.01 USD | `-59.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 9,350,000.00 USD | 0.00 USD | 1,050.00 USD | `-58.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.75` | 9,350,000.00 USD | 0.00 USD | 120.66 USD | `-57.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.15` | 9,350,000.00 USD | 0.00 USD | 121.81 USD | `-56.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 9,350,000.00 USD | 0.00 USD | 170,530.00 USD | `-56.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 9,180,000.00 USD | 0.00 USD | 105.00 USD | `-55.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 9,180,000.00 USD | 0.00 USD | 64,240.00 USD | `-53.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 9,120,000.00 USD | 0.00 USD | 251.05 USD | `-51.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 9,120,000.00 USD | 0.00 USD | 143.25 USD | `-50.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 9,120,000.00 USD | 0.00 USD | 191.40 USD | `-50.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 9,120,000.00 USD | 0.00 USD | 50,240.00 USD | `-50.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.55` | 9,070,000.00 USD | 0.00 USD | 664.65 USD | `-50.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 9,070,000.00 USD | 0.00 USD | 103.35 USD | `-49.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 9,070,000.00 USD | 0.00 USD | 4,660.00 USD | `-48.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 9,060,000.00 USD | 0.00 USD | 107.03 USD | `-48.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 9,060,000.00 USD | 0.00 USD | 102.62 USD | `-48.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 9,060,000.00 USD | 0.00 USD | 134.28 USD | `-47.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 9,060,000.00 USD | 0.00 USD | 3,950.00 USD | `-46.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 9,060,000.00 USD | 0.00 USD | 102.74 USD | `-46.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 9,060,000.00 USD | 0.00 USD | 126.12 USD | `-45.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 9,060,000.00 USD | 0.00 USD | 200.15 USD | `-45.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 9,060,000.00 USD | 0.00 USD | 24,450.00 USD | `-45.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 9,030,000.00 USD | 0.00 USD | 1,660.00 USD | `-45.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 9,030,000.00 USD | 0.00 USD | 641.57 USD | `-44.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 9,030,000.00 USD | 0.00 USD | 139.87 USD | `-43.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 9,030,000.00 USD | 0.00 USD | 209.19 USD | `-43.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 9,030,000.00 USD | 0.00 USD | 4,350.00 USD | `-42.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 9,030,000.00 USD | 0.00 USD | 894.56 USD | `-42.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 9,020,000.00 USD | 0.00 USD | 4,930.00 USD | `-42.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 9,020,000.00 USD | 0.00 USD | 6,790.00 USD | `-41.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.35` | 9,010,000.00 USD | 0.00 USD | 265.53 USD | `-41.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.95` | 9,010,000.00 USD | 0.00 USD | 268.31 USD | `-40.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 9,010,000.00 USD | 0.00 USD | 158.48 USD | `-40.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.15` | 9,010,000.00 USD | 0.00 USD | 3,820.00 USD | `-40.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 9,010,000.00 USD | 0.00 USD | 428.72 USD | `-40.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 9,010,000.00 USD | 0.00 USD | 295.25 USD | `-39.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 9,010,000.00 USD | 0.00 USD | 200.01 USD | `-38.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 9,010,000.00 USD | 0.00 USD | 1,460.00 USD | `-38.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 9,010,000.00 USD | 0.00 USD | 9,040.00 USD | `-38.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 9,000,000.00 USD | 0.00 USD | 35,050.00 USD | `-38.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.15` | 8,960,000.00 USD | 0.00 USD | 2,820.00 USD | `-38.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 8,960,000.00 USD | 0.00 USD | 488.63 USD | `-38.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 8,960,000.00 USD | 0.00 USD | 258.90 USD | `-37.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 8,960,000.00 USD | 0.00 USD | 206.13 USD | `-37.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 8,960,000.00 USD | 0.00 USD | 724.78 USD | `-37.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 8,960,000.00 USD | 0.00 USD | 14,350.00 USD | `-37.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 8,940,000.00 USD | 0.00 USD | 142.33 USD | `-36.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 8,940,000.00 USD | 0.00 USD | 100.78 USD | `-36.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 8,940,000.00 USD | 0.00 USD | 243.74 USD | `-36.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 8,940,000.00 USD | 0.00 USD | 6,720.00 USD | `-36.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 8,940,000.00 USD | 0.00 USD | 136.98 USD | `-35.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 8,940,000.00 USD | 0.00 USD | 9,990.00 USD | `-35.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 8,930,000.00 USD | 0.00 USD | 2,980.00 USD | `-34.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 8,920,000.00 USD | 0.00 USD | 222.55 USD | `-34.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 8,920,000.00 USD | 0.00 USD | 163.19 USD | `-33.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 8,920,000.00 USD | 0.00 USD | 129.70 USD | `-33.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 8,920,000.00 USD | 0.00 USD | 2,440.00 USD | `-33.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 8,920,000.00 USD | 0.00 USD | 2,190.00 USD | `-33.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 8,920,000.00 USD | 0.00 USD | 2,200.00 USD | `-32.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 8,920,000.00 USD | 0.00 USD | 7,100.00 USD | `-32.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 8,910,000.00 USD | 0.00 USD | 541.72 USD | `-31.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 8,910,000.00 USD | 0.00 USD | 335.25 USD | `-31.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 8,910,000.00 USD | 0.00 USD | 268.60 USD | `-30.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 8,910,000.00 USD | 0.00 USD | 195.30 USD | `-30.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.45` | 8,910,000.00 USD | 0.00 USD | 7,600.00 USD | `-29.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 8,900,000.00 USD | 0.00 USD | 5,610.00 USD | `-29.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 8,890,000.00 USD | 0.00 USD | 552.63 USD | `-29.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 8,890,000.00 USD | 0.00 USD | 1,200.00 USD | `-29.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 8,890,000.00 USD | 0.00 USD | 11,360.00 USD | `-29.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 8,880,000.00 USD | 0.00 USD | 172.18 USD | `-28.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 8,880,000.00 USD | 0.00 USD | 668.96 USD | `-28.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 8,880,000.00 USD | 0.00 USD | 107.96 USD | `-28.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 8,880,000.00 USD | 0.00 USD | 42,360.00 USD | `-28.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 8,840,000.00 USD | 0.00 USD | 365.32 USD | `-28.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.95` | 8,840,000.00 USD | 0.00 USD | 1,510.00 USD | `-28.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 8,840,000.00 USD | 0.00 USD | 43,920.00 USD | `-27.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 8,790,000.00 USD | 0.00 USD | 5,270.00 USD | `-27.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 8,790,000.00 USD | 0.00 USD | 562.80 USD | `-27.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 8,790,000.00 USD | 0.00 USD | 681.51 USD | `-27.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 8,780,000.00 USD | 0.00 USD | 4,920.00 USD | `-27.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 8,780,000.00 USD | 0.00 USD | 2,790.00 USD | `-27.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 8,780,000.00 USD | 0.00 USD | 265.02 USD | `-26.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.35` | 8,780,000.00 USD | 0.00 USD | 32,450.00 USD | `-26.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 8,740,000.00 USD | 0.00 USD | 289.37 USD | `-26.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 8,740,000.00 USD | 0.00 USD | 1,930.00 USD | `-26.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.75` | 8,740,000.00 USD | 0.00 USD | 235.34 USD | `-26.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 8,740,000.00 USD | 0.00 USD | 20,410.00 USD | `-25.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 8,720,000.00 USD | 0.00 USD | 19,560.00 USD | `-25.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.65` | 8,700,000.00 USD | 0.00 USD | 14,530.00 USD | `-25.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 8,690,000.00 USD | 0.00 USD | 66,160.00 USD | `-24.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.05` | 8,620,000.00 USD | 0.00 USD | 7,970.00 USD | `-24.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.35` | 8,610,000.00 USD | 0.00 USD | 733.50 USD | `-24.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 8,610,000.00 USD | 0.00 USD | 139.56 USD | `-24.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 8,610,000.00 USD | 0.00 USD | 510.95 USD | `-23.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.25` | 8,610,000.00 USD | 0.00 USD | 621.47 USD | `-23.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 8,610,000.00 USD | 0.00 USD | 1,660.00 USD | `-23.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 8,610,000.00 USD | 0.00 USD | 10,730.00 USD | `-23.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 8,600,000.00 USD | 0.00 USD | 331.00 USD | `-23.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 8,600,000.00 USD | 0.00 USD | 28,050.00 USD | `-23.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 8,570,000.00 USD | 0.00 USD | 30,040.00 USD | `-22.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.35` | 8,540,000.00 USD | 0.00 USD | 153.71 USD | `-22.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.45` | 8,540,000.00 USD | 0.00 USD | 163.73 USD | `-22.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 8,540,000.00 USD | 0.00 USD | 2,220.00 USD | `-22.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 8,540,000.00 USD | 0.00 USD | 277.98 USD | `-21.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 8,540,000.00 USD | 0.00 USD | 8,680.00 USD | `-21.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 8,530,000.00 USD | 0.00 USD | 254.34 USD | `-21.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 8,530,000.00 USD | 0.00 USD | 486.47 USD | `-21.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.35` | 8,530,000.00 USD | 0.00 USD | 358.84 USD | `-21.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 8,530,000.00 USD | 0.00 USD | 4,340.00 USD | `-21.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 8,520,000.00 USD | 0.00 USD | 536.55 USD | `-21.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 8,520,000.00 USD | 0.00 USD | 251.74 USD | `-21.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 8,520,000.00 USD | 0.00 USD | 17,010.00 USD | `-20.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 8,510,000.00 USD | 0.00 USD | 5,690.00 USD | `-20.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.45` | 8,500,000.00 USD | 0.00 USD | 1,020.00 USD | `-20.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 8,500,000.00 USD | 0.00 USD | 155.12 USD | `-19.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 8,500,000.00 USD | 0.00 USD | 56,850.00 USD | `-19.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 8,440,000.00 USD | 0.00 USD | 738.52 USD | `-19.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 8,440,000.00 USD | 0.00 USD | 18,590.00 USD | `-19.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.65` | 8,420,000.00 USD | 0.00 USD | 116.40 USD | `-19.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.75` | 8,420,000.00 USD | 0.00 USD | 379.58 USD | `-19.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 8,420,000.00 USD | 0.00 USD | 5,300.00 USD | `-18.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 8,420,000.00 USD | 0.00 USD | 201.04 USD | `-18.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 8,420,000.00 USD | 0.00 USD | 2,140.00 USD | `-18.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 8,410,000.00 USD | 0.00 USD | 5,850.00 USD | `-18.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 8,410,000.00 USD | 0.00 USD | 238.95 USD | `-18.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.75` | 8,410,000.00 USD | 0.00 USD | 1,330.00 USD | `-18.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.85` | 8,410,000.00 USD | 0.00 USD | 289.06 USD | `-17.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 8,410,000.00 USD | 0.00 USD | 808.29 USD | `-17.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 8,410,000.00 USD | 0.00 USD | 41,050.00 USD | `-17.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.15` | 8,360,000.00 USD | 0.00 USD | 8,360.00 USD | `-17.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.35` | 8,360,000.00 USD | 0.00 USD | 359.97 USD | `-17.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.45` | 8,360,000.00 USD | 0.00 USD | 8,770.00 USD | `-17.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.55` | 8,350,000.00 USD | 0.00 USD | 1,280.00 USD | `-17.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.65` | 8,350,000.00 USD | 0.00 USD | 1,280.00 USD | `-17.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.75` | 8,340,000.00 USD | 0.00 USD | 22,780.00 USD | `-16.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.85` | 8,320,000.00 USD | 0.00 USD | 341.19 USD | `-16.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 8,320,000.00 USD | 0.00 USD | 1,620.00 USD | `-16.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.25` | 8,320,000.00 USD | 0.00 USD | 266.50 USD | `-16.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 8,320,000.00 USD | 0.00 USD | 5,830.00 USD | `-16.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.55` | 8,310,000.00 USD | 0.00 USD | 572.48 USD | `-16.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 8,310,000.00 USD | 0.00 USD | 952.86 USD | `-16.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.75` | 8,310,000.00 USD | 0.00 USD | 1,390.00 USD | `-15.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.85` | 8,310,000.00 USD | 0.00 USD | 818.50 USD | `-15.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 8,310,000.00 USD | 0.00 USD | 70,900.00 USD | `-15.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 8,240,000.00 USD | 0.00 USD | 3,220.00 USD | `-15.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 8,240,000.00 USD | 0.00 USD | 684.31 USD | `-15.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.25` | 8,240,000.00 USD | 0.00 USD | 486.92 USD | `-15.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 8,230,000.00 USD | 0.00 USD | 386.22 USD | `-15.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 8,230,000.00 USD | 0.00 USD | 1,870.00 USD | `-15.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.55` | 8,230,000.00 USD | 0.00 USD | 1,310.00 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.65` | 8,230,000.00 USD | 0.00 USD | 267,390.00 USD | `-15.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 7,960,000.00 USD | 0.00 USD | 1,660.00 USD | `-14.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.85` | 7,960,000.00 USD | 0.00 USD | 3,270.00 USD | `-14.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.95` | 7,960,000.00 USD | 0.00 USD | 945.63 USD | `-14.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 7,960,000.00 USD | 0.00 USD | 6,420.00 USD | `-14.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 7,950,000.00 USD | 0.00 USD | 239.47 USD | `-14.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 7,950,000.00 USD | 0.00 USD | 18,330.00 USD | `-14.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 7,930,000.00 USD | 0.00 USD | 168.57 USD | `-14.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 7,930,000.00 USD | 0.00 USD | 421.09 USD | `-14.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 7,930,000.00 USD | 0.00 USD | 1,100.00 USD | `-13.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 7,930,000.00 USD | 0.00 USD | 1,320.00 USD | `-13.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 7,930,000.00 USD | 0.00 USD | 4,550.00 USD | `-13.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 7,930,000.00 USD | 0.00 USD | 40,720.00 USD | `-13.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.15` | 7,880,000.00 USD | 0.00 USD | 25,220.00 USD | `-13.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 7,860,000.00 USD | 0.00 USD | 2,690.00 USD | `-13.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.45` | 7,860,000.00 USD | 0.00 USD | 965.26 USD | `-13.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.55` | 7,860,000.00 USD | 0.00 USD | 169.95 USD | `-13.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 7,860,000.00 USD | 0.00 USD | 858.35 USD | `-12.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 7,850,000.00 USD | 0.00 USD | 306.80 USD | `-12.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 7,850,000.00 USD | 0.00 USD | 137.62 USD | `-12.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 7,850,000.00 USD | 0.00 USD | 238,730.00 USD | `-12.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 7,620,000.00 USD | 0.00 USD | 437.67 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 7,620,000.00 USD | 0.00 USD | 1,320.00 USD | `-12.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 7,610,000.00 USD | 0.00 USD | 39,110.00 USD | `-12.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 7,570,000.00 USD | 0.00 USD | 120.48 USD | `-12.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 7,570,000.00 USD | 0.00 USD | 105.23 USD | `-12.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 7,570,000.00 USD | 0.00 USD | 310.05 USD | `-11.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 7,570,000.00 USD | 0.00 USD | 1,410.00 USD | `-11.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 7,570,000.00 USD | 0.00 USD | 360.57 USD | `-11.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 7,570,000.00 USD | 0.00 USD | 2,050.00 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 7,570,000.00 USD | 0.00 USD | 10,910.00 USD | `-11.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 7,560,000.00 USD | 0.00 USD | 2,210.00 USD | `-11.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 7,560,000.00 USD | 0.00 USD | 163.88 USD | `-11.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 7,560,000.00 USD | 0.00 USD | 4,080.00 USD | `-11.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 7,550,000.00 USD | 0.00 USD | 2,790.00 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 7,550,000.00 USD | 0.00 USD | 417.17 USD | `-11.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 7,550,000.00 USD | 0.00 USD | 220,550.00 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 7,330,000.00 USD | 0.00 USD | 3,060.00 USD | `-10.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 7,330,000.00 USD | 0.00 USD | 788.60 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 7,330,000.00 USD | 0.00 USD | 132.16 USD | `-10.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 7,330,000.00 USD | 0.00 USD | 280,590.00 USD | `-10.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 7,040,000.00 USD | 0.00 USD | 23,550.00 USD | `-10.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 7,020,000.00 USD | 0.00 USD | 8,200.00 USD | `-10.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 7,010,000.00 USD | 0.00 USD | 102.20 USD | `-10.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 7,010,000.00 USD | 0.00 USD | 730.21 USD | `-10.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 7,010,000.00 USD | 0.00 USD | 7,840.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 7,000,000.00 USD | 0.00 USD | 2,300.00 USD | `-9.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.85` | 7,000,000.00 USD | 0.00 USD | 131.78 USD | `-9.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.95` | 7,000,000.00 USD | 0.00 USD | 1,410.00 USD | `-9.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 7,000,000.00 USD | 0.00 USD | 132,850.00 USD | `-9.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 6,870,000.00 USD | 0.00 USD | 833.02 USD | `-9.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 6,870,000.00 USD | 0.00 USD | 1,870.00 USD | `-9.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 6,870,000.00 USD | 0.00 USD | 38,020.00 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 6,830,000.00 USD | 0.00 USD | 867.69 USD | `-9.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 6,830,000.00 USD | 0.00 USD | 32,610.00 USD | `-8.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 6,790,000.00 USD | 0.00 USD | 27,220.00 USD | `-8.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 6,770,000.00 USD | 0.00 USD | 53,390.00 USD | `-8.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 6,710,000.00 USD | 0.00 USD | 91,430.00 USD | `-8.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 6,620,000.00 USD | 0.00 USD | 141.43 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 6,620,000.00 USD | 0.00 USD | 15,380.00 USD | `-8.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 6,610,000.00 USD | 0.00 USD | 6,470.00 USD | `-8.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 6,600,000.00 USD | 0.00 USD | 1,340.00 USD | `-8.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 6,600,000.00 USD | 0.00 USD | 4,220.00 USD | `-8.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 6,590,000.00 USD | 0.00 USD | 5,280.00 USD | `-8.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 6,590,000.00 USD | 0.00 USD | 348.35 USD | `-7.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 6,590,000.00 USD | 0.00 USD | 297.64 USD | `-7.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 6,590,000.00 USD | 0.00 USD | 105.01 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 6,590,000.00 USD | 0.00 USD | 17,170.00 USD | `-7.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 6,570,000.00 USD | 0.00 USD | 87,020.00 USD | `-7.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 6,480,000.00 USD | 0.00 USD | 3,270,000.00 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 3,220,000.00 USD | 0.00 USD | 301.10 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 3,220,000.00 USD | 0.00 USD | 12,170.00 USD | `-7.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.35` | 3,200,000.00 USD | 0.00 USD | 106,890.00 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 3,100,000.00 USD | 0.00 USD | 5,010.00 USD | `-7.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 3,090,000.00 USD | 0.00 USD | 13,500.00 USD | `-6.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 3,080,000.00 USD | 0.00 USD | 75,820.00 USD | `-6.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 3,000,000.00 USD | 0.00 USD | 4,980.00 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.85` | 3,000,000.00 USD | 0.00 USD | 6,580.00 USD | `-6.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 2,990,000.00 USD | 0.00 USD | 7,300.00 USD | `-6.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 2,980,000.00 USD | 0.00 USD | 642,140.00 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 2,340,000.00 USD | 0.00 USD | 1,120.00 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.25` | 2,340,000.00 USD | 0.00 USD | 743.69 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 2,340,000.00 USD | 0.00 USD | 16,770.00 USD | `-6.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 2,320,000.00 USD | 0.00 USD | 920.90 USD | `-5.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 2,320,000.00 USD | 0.00 USD | 20,520.00 USD | `-5.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 2,300,000.00 USD | 0.00 USD | 38,100.00 USD | `-5.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 2,260,000.00 USD | 0.00 USD | 21,870.00 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 2,240,000.00 USD | 0.00 USD | 41,980.00 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 2,200,000.00 USD | 0.00 USD | 33,290.00 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 2,170,000.00 USD | 0.00 USD | 267,700.00 USD | `-5.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 1,900,000.00 USD | 0.00 USD | 49,850.00 USD | `-5.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 1,850,000.00 USD | 0.00 USD | 5,610.00 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 1,840,000.00 USD | 0.00 USD | 18,900.00 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 1,830,000.00 USD | 0.00 USD | 11,060.00 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 1,810,000.00 USD | 0.00 USD | 17,280.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 1,800,000.00 USD | 0.00 USD | 55,540.00 USD | `-4.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 1,740,000.00 USD | 0.00 USD | 6,990.00 USD | `-4.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 1,730,000.00 USD | 0.00 USD | 32,630.00 USD | `-4.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 1,700,000.00 USD | 0.00 USD | 14,800.00 USD | `-4.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 1,690,000.00 USD | 0.00 USD | 44,480.00 USD | `-4.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 1,640,000.00 USD | 0.00 USD | 135,650.00 USD | `-4.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 1,510,000.00 USD | 0.00 USD | 7,920.00 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 1,500,000.00 USD | 0.00 USD | 385.54 USD | `-4.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 1,500,000.00 USD | 0.00 USD | 1,380.00 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 1,500,000.00 USD | 0.00 USD | 1,120.00 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 1,500,000.00 USD | 0.00 USD | 3,290.00 USD | `-3.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 1,490,000.00 USD | 0.00 USD | 3,660.00 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 1,490,000.00 USD | 0.00 USD | 1,200.00 USD | `-3.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 1,490,000.00 USD | 0.00 USD | 106.16 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 1,490,000.00 USD | 0.00 USD | 111,370.00 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 1,380,000.00 USD | 0.00 USD | 318.23 USD | `-3.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 1,380,000.00 USD | 0.00 USD | 1,050.00 USD | `-3.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 1,370,000.00 USD | 0.00 USD | 12,280.00 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 1,360,000.00 USD | 0.00 USD | 63,650.00 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 1,300,000.00 USD | 0.00 USD | 91,930.00 USD | `-2.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 1,210,000.00 USD | 0.00 USD | 24,170.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 1,180,000.00 USD | 0.00 USD | 27,810.00 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 1,150,000.00 USD | 0.00 USD | 22,510.00 USD | `-2.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 1,130,000.00 USD | 0.00 USD | 4,000.00 USD | `-2.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 1,130,000.00 USD | 0.00 USD | 68,710.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 1,060,000.00 USD | 0.00 USD | 61,360.00 USD | `-2.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 998,360.00 USD | 0.00 USD | 7,310.00 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 991,060.00 USD | 0.00 USD | 11,640.00 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 979,410.00 USD | 0.00 USD | 77,760.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 901,650.00 USD | 0.00 USD | 162,880.00 USD | `-1.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 738,770.00 USD | 0.00 USD | 4,590.00 USD | `-1.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 734,180.00 USD | 0.00 USD | 60,370.00 USD | `-1.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 673,820.00 USD | 0.00 USD | 32,460.00 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 641,360.00 USD | 0.00 USD | 24,880.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 616,470.00 USD | 0.00 USD | 24,810.00 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.15` | 591,660.00 USD | 0.00 USD | 27,080.00 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.25` | 564,580.00 USD | 0.00 USD | 7,290.00 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.35` | 557,300.00 USD | 0.00 USD | 63,210.00 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.45` | 494,090.00 USD | 0.00 USD | 152.39 USD | `-0.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.55` | 493,940.00 USD | 0.00 USD | 8,770.00 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.65` | 485,170.00 USD | 0.00 USD | 25,020.00 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.75` | 460,150.00 USD | 0.00 USD | 353,830.00 USD | `-0.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.85` | 106,320.00 USD | 0.00 USD | 15,490.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.95` | 90,830.00 USD | 0.00 USD | 35,570.00 USD | `-0.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.05` | 55,260.00 USD | 0.00 USD | 16,800.00 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.15` | 38,460.00 USD | 0.00 USD | 6,080.00 USD | `-0.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.25` | 32,370.00 USD | 0.00 USD | 32,370.00 USD | `-0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.35` | 8,150.00 USD | 8,150.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.45` | 20,590.00 USD | 12,440.00 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.55` | 24,890.00 USD | 4,300.00 USD | 0.00 USD | `+0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.65` | 39,110.00 USD | 14,220.00 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.75` | 45,210.00 USD | 6,090.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.85` | 47,160.00 USD | 1,950.00 USD | 0.00 USD | `+0.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.95` | 49,080.00 USD | 1,920.00 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 63,260.00 USD | 14,180.00 USD | 0.00 USD | `+0.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.15` | 64,520.00 USD | 1,260.00 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.25` | 119,240.00 USD | 54,730.00 USD | 0.00 USD | `+1.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.35` | 120,640.00 USD | 1,400.00 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.45` | 124,760.00 USD | 4,120.00 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.55` | 238,600.00 USD | 113,850.00 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.65` | 276,990.00 USD | 38,380.00 USD | 0.00 USD | `+1.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.75` | 359,740.00 USD | 82,750.00 USD | 0.00 USD | `+1.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.85` | 366,320.00 USD | 6,580.00 USD | 0.00 USD | `+1.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.95` | 371,300.00 USD | 4,980.00 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 440,150.00 USD | 68,850.00 USD | 0.00 USD | `+1.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.15` | 457,640.00 USD | 17,490.00 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.25` | 462,370.00 USD | 4,730.00 USD | 0.00 USD | `+2.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.35` | 501,750.00 USD | 39,390.00 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.45` | 639,650.00 USD | 137,900.00 USD | 0.00 USD | `+2.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.55` | 774,320.00 USD | 134,670.00 USD | 0.00 USD | `+2.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.65` | 788,190.00 USD | 13,860.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.75` | 797,960.00 USD | 9,780.00 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.85` | 802,640.00 USD | 4,680.00 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 845,060.00 USD | 42,410.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 2,640,000.00 USD | 1,790,000.00 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 2,650,000.00 USD | 12,820.00 USD | 0.00 USD | `+2.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 2,650,000.00 USD | 5,240.00 USD | 0.00 USD | `+3.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 2,650,000.00 USD | 254.89 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 2,660,000.00 USD | 6,690.00 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 2,660,000.00 USD | 2,490.00 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 2,720,000.00 USD | 52,210.00 USD | 0.00 USD | `+3.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 2,720,000.00 USD | 1,220.00 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 2,750,000.00 USD | 27,710.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 2,750,000.00 USD | 2,760.00 USD | 0.00 USD | `+3.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 2,980,000.00 USD | 227,930.00 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 2,980,000.00 USD | 1,730.00 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 2,990,000.00 USD | 7,600.00 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 2,990,000.00 USD | 3,850.00 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 2,990,000.00 USD | 5,550.00 USD | 0.00 USD | `+4.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 3,000,000.00 USD | 4,880.00 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 3,000,000.00 USD | 477.76 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 3,000,000.00 USD | 417.17 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 3,000,000.00 USD | 2,110.00 USD | 0.00 USD | `+4.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 3,000,000.00 USD | 1,080.00 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 3,090,000.00 USD | 82,730.00 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 3,100,000.00 USD | 17,480.00 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 3,110,000.00 USD | 2,120.00 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 3,110,000.00 USD | 4,580.00 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 3,120,000.00 USD | 7,280.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 3,130,000.00 USD | 13,740.00 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 3,400,000.00 USD | 266,350.00 USD | 0.00 USD | `+5.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 3,400,000.00 USD | 1,280.00 USD | 0.00 USD | `+5.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 3,400,000.00 USD | 2,480.00 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 3,410,000.00 USD | 4,280.00 USD | 0.00 USD | `+5.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 3,450,000.00 USD | 45,690.00 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 3,450,000.00 USD | 3,180.00 USD | 0.00 USD | `+6.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 3,520,000.00 USD | 64,080.00 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 3,520,000.00 USD | 4,260.00 USD | 0.00 USD | `+6.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 3,530,000.00 USD | 3,860.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 3,550,000.00 USD | 20,580.00 USD | 0.00 USD | `+6.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 3,560,000.00 USD | 17,250.00 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 3,570,000.00 USD | 980.44 USD | 0.00 USD | `+6.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 3,790,000.00 USD | 226,740.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 3,850,000.00 USD | 62,400.00 USD | 0.00 USD | `+6.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 3,870,000.00 USD | 13,180.00 USD | 0.00 USD | `+6.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 3,870,000.00 USD | 1,180.00 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 3,870,000.00 USD | 519.17 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 3,870,000.00 USD | 146.09 USD | 0.00 USD | `+7.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 3,970,000.00 USD | 95,950.00 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 3,990,000.00 USD | 28,290.00 USD | 0.00 USD | `+7.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 3,990,000.00 USD | 230.23 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 4,000,000.00 USD | 2,150.00 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 4,000,000.00 USD | 5,900.00 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 4,030,000.00 USD | 25,930.00 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 4,160,000.00 USD | 132,100.00 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 4,190,000.00 USD | 28,780.00 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 4,190,000.00 USD | 1,010.00 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 4,190,000.00 USD | 1,090.00 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 4,190,000.00 USD | 266.79 USD | 0.00 USD | `+8.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 4,200,000.00 USD | 3,620.00 USD | 0.00 USD | `+8.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 4,200,000.00 USD | 1,970.00 USD | 0.00 USD | `+8.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 4,200,000.00 USD | 549.90 USD | 0.00 USD | `+8.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 4,210,000.00 USD | 10,600.00 USD | 0.00 USD | `+8.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 4,210,000.00 USD | 206.60 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 4,230,000.00 USD | 19,890.00 USD | 0.00 USD | `+9.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 4,240,000.00 USD | 7,900.00 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 4,240,000.00 USD | 758.62 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 4,250,000.00 USD | 7,980.00 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 4,270,000.00 USD | 26,170.00 USD | 0.00 USD | `+9.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 4,280,000.00 USD | 7,640.00 USD | 0.00 USD | `+9.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 4,280,000.00 USD | 355.14 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 4,390,000.00 USD | 110,390.00 USD | 0.00 USD | `+9.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 4,390,000.00 USD | 1,400.00 USD | 0.00 USD | `+9.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 4,390,000.00 USD | 2,990.00 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 4,540,000.00 USD | 142,930.00 USD | 0.00 USD | `+10.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 4,540,000.00 USD | 109.29 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 4,560,000.00 USD | 20,190.00 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 4,560,000.00 USD | 698.85 USD | 0.00 USD | `+10.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 4,570,000.00 USD | 8,930.00 USD | 0.00 USD | `+10.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 4,620,000.00 USD | 52,130.00 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 4,680,000.00 USD | 65,380.00 USD | 0.00 USD | `+10.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 4,680,000.00 USD | 536.60 USD | 0.00 USD | `+10.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 4,700,000.00 USD | 11,350.00 USD | 0.00 USD | `+10.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 4,710,000.00 USD | 9,120.00 USD | 0.00 USD | `+11.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 4,790,000.00 USD | 89,330.00 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 4,860,000.00 USD | 68,190.00 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 4,870,000.00 USD | 7,140.00 USD | 0.00 USD | `+11.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 4,870,000.00 USD | 2,580.00 USD | 0.00 USD | `+11.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 4,880,000.00 USD | 5,430.00 USD | 0.00 USD | `+11.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 4,880,000.00 USD | 666.02 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 4,880,000.00 USD | 1,030.00 USD | 0.00 USD | `+11.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 4,880,000.00 USD | 1,430.00 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 4,920,000.00 USD | 40,920.00 USD | 0.00 USD | `+12.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 5,000,000.00 USD | 73,460.00 USD | 0.00 USD | `+12.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 5,000,000.00 USD | 7,660.00 USD | 0.00 USD | `+12.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 8,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | `+12.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 8,980,000.00 USD | 31,070.00 USD | 0.00 USD | `+12.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 8,990,000.00 USD | 5,880.00 USD | 0.00 USD | `+12.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 8,990,000.00 USD | 1,070.00 USD | 0.00 USD | `+12.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 8,990,000.00 USD | 5,040.00 USD | 0.00 USD | `+12.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 8,990,000.00 USD | 1,370.00 USD | 0.00 USD | `+12.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 9,000,000.00 USD | 1,430.00 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 9,000,000.00 USD | 357.34 USD | 0.00 USD | `+13.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 9,520,000.00 USD | 522,250.00 USD | 0.00 USD | `+13.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 9,520,000.00 USD | 4,150.00 USD | 0.00 USD | `+13.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 9,520,000.00 USD | 102.53 USD | 0.00 USD | `+13.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 9,520,000.00 USD | 1,610.00 USD | 0.00 USD | `+13.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 9,530,000.00 USD | 1,580.00 USD | 0.00 USD | `+13.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 9,540,000.00 USD | 10,280.00 USD | 0.00 USD | `+13.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 9,540,000.00 USD | 3,030.00 USD | 0.00 USD | `+13.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 9,560,000.00 USD | 17,740.00 USD | 0.00 USD | `+13.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 9,630,000.00 USD | 74,410.00 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 9,700,000.00 USD | 64,770.00 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 9,700,000.00 USD | 1,300.00 USD | 0.00 USD | `+14.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 9,700,000.00 USD | 5,910.00 USD | 0.00 USD | `+14.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 9,700,000.00 USD | 585.11 USD | 0.00 USD | `+14.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 9,700,000.00 USD | 852.24 USD | 0.00 USD | `+14.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 9,730,000.00 USD | 22,910.00 USD | 0.00 USD | `+14.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 9,730,000.00 USD | 2,420.00 USD | 0.00 USD | `+14.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 9,730,000.00 USD | 2,330.00 USD | 0.00 USD | `+15.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 9,750,000.00 USD | 14,190.00 USD | 0.00 USD | `+15.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 9,800,000.00 USD | 49,680.00 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 9,800,000.00 USD | 5,260.00 USD | 0.00 USD | `+15.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 9,810,000.00 USD | 6,270.00 USD | 0.00 USD | `+15.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 9,810,000.00 USD | 843.38 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 9,840,000.00 USD | 36,280.00 USD | 0.00 USD | `+15.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 9,850,000.00 USD | 6,150.00 USD | 0.00 USD | `+15.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 9,850,000.00 USD | 586.82 USD | 0.00 USD | `+16.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 9,930,000.00 USD | 78,560.00 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 9,930,000.00 USD | 473.38 USD | 0.00 USD | `+16.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 9,970,000.00 USD | 35,250.00 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 9,970,000.00 USD | 655.74 USD | 0.00 USD | `+16.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 9,970,000.00 USD | 4,470.00 USD | 0.00 USD | `+16.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 9,970,000.00 USD | 230.71 USD | 0.00 USD | `+16.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 9,970,000.00 USD | 257.07 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 9,980,000.00 USD | 4,540.00 USD | 0.00 USD | `+17.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 9,980,000.00 USD | 1,970.00 USD | 0.00 USD | `+17.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 9,980,000.00 USD | 122.14 USD | 0.00 USD | `+17.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 9,980,000.00 USD | 907.14 USD | 0.00 USD | `+17.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 9,980,000.00 USD | 740.99 USD | 0.00 USD | `+17.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 9,980,000.00 USD | 343.35 USD | 0.00 USD | `+17.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 9,980,000.00 USD | 1,640.00 USD | 0.00 USD | `+17.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 9,980,000.00 USD | 105.48 USD | 0.00 USD | `+17.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 9,980,000.00 USD | 1,010.00 USD | 0.00 USD | `+17.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 9,980,000.00 USD | 2,520.00 USD | 0.00 USD | `+18.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 10,070,000.00 USD | 81,890.00 USD | 0.00 USD | `+18.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 10,070,000.00 USD | 309.14 USD | 0.00 USD | `+18.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 10,070,000.00 USD | 346.35 USD | 0.00 USD | `+18.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 10,070,000.00 USD | 2,440.00 USD | 0.00 USD | `+18.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.75` | 10,070,000.00 USD | 121.54 USD | 0.00 USD | `+19.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 10,070,000.00 USD | 579.25 USD | 0.00 USD | `+19.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 10,080,000.00 USD | 6,400.00 USD | 0.00 USD | `+19.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 10,080,000.00 USD | 1,740.00 USD | 0.00 USD | `+19.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 10,080,000.00 USD | 1,920.00 USD | 0.00 USD | `+19.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 10,080,000.00 USD | 2,870.00 USD | 0.00 USD | `+19.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 10,100,000.00 USD | 14,010.00 USD | 0.00 USD | `+19.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 10,100,000.00 USD | 6,000.00 USD | 0.00 USD | `+19.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 10,110,000.00 USD | 3,580.00 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 10,110,000.00 USD | 234.87 USD | 0.00 USD | `+20.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 10,120,000.00 USD | 12,860.00 USD | 0.00 USD | `+20.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 10,120,000.00 USD | 4,200.00 USD | 0.00 USD | `+20.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 10,120,000.00 USD | 584.58 USD | 0.00 USD | `+20.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 10,130,000.00 USD | 1,740.00 USD | 0.00 USD | `+20.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 10,130,000.00 USD | 2,330.00 USD | 0.00 USD | `+20.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 10,250,000.00 USD | 118,690.00 USD | 0.00 USD | `+20.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 10,350,000.00 USD | 106,330.00 USD | 0.00 USD | `+20.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 10,360,000.00 USD | 5,920.00 USD | 0.00 USD | `+21.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 10,420,000.00 USD | 55,580.00 USD | 0.00 USD | `+21.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 10,480,000.00 USD | 69,220.00 USD | 0.00 USD | `+21.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 10,490,000.00 USD | 3,980.00 USD | 0.00 USD | `+21.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 10,490,000.00 USD | 4,460.00 USD | 0.00 USD | `+21.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 10,490,000.00 USD | 127.82 USD | 0.00 USD | `+21.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 10,490,000.00 USD | 707.15 USD | 0.00 USD | `+21.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 10,500,000.00 USD | 1,260.00 USD | 0.00 USD | `+21.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 10,500,000.00 USD | 2,970.00 USD | 0.00 USD | `+22.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 10,500,000.00 USD | 403.75 USD | 0.00 USD | `+22.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 10,510,000.00 USD | 15,940.00 USD | 0.00 USD | `+22.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 10,560,000.00 USD | 42,290.00 USD | 0.00 USD | `+22.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 10,610,000.00 USD | 52,430.00 USD | 0.00 USD | `+22.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 10,620,000.00 USD | 15,130.00 USD | 0.00 USD | `+22.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 10,630,000.00 USD | 1,850.00 USD | 0.00 USD | `+22.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 10,630,000.00 USD | 4,150.00 USD | 0.00 USD | `+22.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 10,630,000.00 USD | 310.57 USD | 0.00 USD | `+22.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 10,630,000.00 USD | 615.00 USD | 0.00 USD | `+23.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 10,760,000.00 USD | 125,500.00 USD | 0.00 USD | `+23.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 10,790,000.00 USD | 37,630.00 USD | 0.00 USD | `+23.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 10,790,000.00 USD | 458.21 USD | 0.00 USD | `+23.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 10,980,000.00 USD | 181,410.00 USD | 0.00 USD | `+23.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 10,980,000.00 USD | 414.52 USD | 0.00 USD | `+23.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 10,980,000.00 USD | 3,210.00 USD | 0.00 USD | `+23.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 10,990,000.00 USD | 7,850.00 USD | 0.00 USD | `+23.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 11,000,000.00 USD | 13,560.00 USD | 0.00 USD | `+23.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 11,000,000.00 USD | 904.13 USD | 0.00 USD | `+23.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 11,000,000.00 USD | 191.83 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.75` | 11,000,000.00 USD | 2,150.00 USD | 0.00 USD | `+24.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 11,010,000.00 USD | 663.47 USD | 0.00 USD | `+24.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 11,030,000.00 USD | 20,960.00 USD | 0.00 USD | `+24.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 11,030,000.00 USD | 122.36 USD | 0.00 USD | `+24.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 11,040,000.00 USD | 11,200.00 USD | 0.00 USD | `+24.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 11,050,000.00 USD | 11,570.00 USD | 0.00 USD | `+24.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 11,060,000.00 USD | 7,860.00 USD | 0.00 USD | `+24.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 11,060,000.00 USD | 2,070.00 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 11,060,000.00 USD | 2,450.00 USD | 0.00 USD | `+25.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 11,060,000.00 USD | 1,480.00 USD | 0.00 USD | `+25.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 11,140,000.00 USD | 80,260.00 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 11,340,000.00 USD | 192,930.00 USD | 0.00 USD | `+25.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 11,340,000.00 USD | 1,000.00 USD | 0.00 USD | `+25.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 11,570,000.00 USD | 234,430.00 USD | 0.00 USD | `+25.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 11,620,000.00 USD | 52,330.00 USD | 0.00 USD | `+25.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 11,630,000.00 USD | 3,060.00 USD | 0.00 USD | `+25.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 11,640,000.00 USD | 14,830.00 USD | 0.00 USD | `+26.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 11,650,000.00 USD | 11,000.00 USD | 0.00 USD | `+26.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 11,650,000.00 USD | 104.34 USD | 0.00 USD | `+26.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 11,660,000.00 USD | 3,850.00 USD | 0.00 USD | `+26.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 11,670,000.00 USD | 16,430.00 USD | 0.00 USD | `+26.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 12,680,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+26.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 12,680,000.00 USD | 252.46 USD | 0.00 USD | `+26.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 12,690,000.00 USD | 7,710.00 USD | 0.00 USD | `+26.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 12,700,000.00 USD | 6,790.00 USD | 0.00 USD | `+26.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 12,700,000.00 USD | 2,670.00 USD | 0.00 USD | `+26.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 12,700,000.00 USD | 632.58 USD | 0.00 USD | `+27.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 12,710,000.00 USD | 11,550.00 USD | 0.00 USD | `+27.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 12,720,000.00 USD | 5,530.00 USD | 0.00 USD | `+27.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 12,740,000.00 USD | 18,470.00 USD | 0.00 USD | `+27.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 12,750,000.00 USD | 16,360.00 USD | 0.00 USD | `+27.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 12,750,000.00 USD | 1,320.00 USD | 0.00 USD | `+27.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 12,750,000.00 USD | 151.59 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 12,760,000.00 USD | 4,240.00 USD | 0.00 USD | `+27.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 12,760,000.00 USD | 1,370.00 USD | 0.00 USD | `+27.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 12,770,000.00 USD | 7,330.00 USD | 0.00 USD | `+28.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 12,770,000.00 USD | 6,610.00 USD | 0.00 USD | `+28.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 12,770,000.00 USD | 596.78 USD | 0.00 USD | `+28.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 12,790,000.00 USD | 10,310.00 USD | 0.00 USD | `+28.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 13,340,000.00 USD | 554,250.00 USD | 0.00 USD | `+28.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 13,340,000.00 USD | 603.22 USD | 0.00 USD | `+28.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 13,340,000.00 USD | 311.87 USD | 0.00 USD | `+28.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 13,350,000.00 USD | 6,780.00 USD | 0.00 USD | `+28.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 13,350,000.00 USD | 993.56 USD | 0.00 USD | `+28.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 13,360,000.00 USD | 16,280.00 USD | 0.00 USD | `+29.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 13,360,000.00 USD | 471.94 USD | 0.00 USD | `+29.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 13,370,000.00 USD | 209.08 USD | 0.00 USD | `+29.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 13,520,000.00 USD | 151,060.00 USD | 0.00 USD | `+29.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 13,520,000.00 USD | 189.23 USD | 0.00 USD | `+29.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 13,520,000.00 USD | 187.15 USD | 0.00 USD | `+30.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 13,520,000.00 USD | 3,550.00 USD | 0.00 USD | `+30.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 13,530,000.00 USD | 7,460.00 USD | 0.00 USD | `+30.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 13,720,000.00 USD | 190,580.00 USD | 0.00 USD | `+30.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 13,720,000.00 USD | 534.87 USD | 0.00 USD | `+30.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 13,720,000.00 USD | 4,620.00 USD | 0.00 USD | `+31.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 13,730,000.00 USD | 5,000.00 USD | 0.00 USD | `+31.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 13,730,000.00 USD | 362.81 USD | 0.00 USD | `+31.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 13,790,000.00 USD | 60,770.00 USD | 0.00 USD | `+31.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 13,790,000.00 USD | 482.37 USD | 0.00 USD | `+31.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 13,790,000.00 USD | 3,700.00 USD | 0.00 USD | `+31.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 13,800,000.00 USD | 3,010.00 USD | 0.00 USD | `+31.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 13,800,000.00 USD | 191.09 USD | 0.00 USD | `+31.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.65` | 13,840,000.00 USD | 41,130.00 USD | 0.00 USD | `+32.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 13,850,000.00 USD | 12,600.00 USD | 0.00 USD | `+32.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 13,900,000.00 USD | 50,720.00 USD | 0.00 USD | `+32.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.15` | 13,900,000.00 USD | 229.89 USD | 0.00 USD | `+32.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 13,920,000.00 USD | 15,330.00 USD | 0.00 USD | `+32.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 13,920,000.00 USD | 401.29 USD | 0.00 USD | `+33.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 13,920,000.00 USD | 1,320.00 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.65` | 13,920,000.00 USD | 152.99 USD | 0.00 USD | `+33.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 13,920,000.00 USD | 153.10 USD | 0.00 USD | `+33.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 13,920,000.00 USD | 116.87 USD | 0.00 USD | `+33.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 13,970,000.00 USD | 51,520.00 USD | 0.00 USD | `+33.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 13,970,000.00 USD | 1,760.00 USD | 0.00 USD | `+34.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 13,980,000.00 USD | 4,090.00 USD | 0.00 USD | `+34.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 13,980,000.00 USD | 192.06 USD | 0.00 USD | `+34.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 13,980,000.00 USD | 3,150.00 USD | 0.00 USD | `+34.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 13,980,000.00 USD | 2,620.00 USD | 0.00 USD | `+34.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 13,990,000.00 USD | 10,140.00 USD | 0.00 USD | `+34.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 14,000,000.00 USD | 6,000.00 USD | 0.00 USD | `+34.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 14,000,000.00 USD | 5,950.00 USD | 0.00 USD | `+34.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 14,010,000.00 USD | 8,820.00 USD | 0.00 USD | `+34.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.45` | 14,010,000.00 USD | 135.39 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 14,170,000.00 USD | 160,920.00 USD | 0.00 USD | `+35.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 14,170,000.00 USD | 144.93 USD | 0.00 USD | `+35.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 14,190,000.00 USD | 12,390.00 USD | 0.00 USD | `+35.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 14,190,000.00 USD | 397.95 USD | 0.00 USD | `+36.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 14,200,000.00 USD | 9,310.00 USD | 0.00 USD | `+36.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 14,200,000.00 USD | 3,910.00 USD | 0.00 USD | `+36.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 14,200,000.00 USD | 267.43 USD | 0.00 USD | `+36.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 14,200,000.00 USD | 509.96 USD | 0.00 USD | `+36.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 14,200,000.00 USD | 191.88 USD | 0.00 USD | `+37.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 14,200,000.00 USD | 237.36 USD | 0.00 USD | `+37.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 14,200,000.00 USD | 1,210.00 USD | 0.00 USD | `+37.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.65` | 14,200,000.00 USD | 192.46 USD | 0.00 USD | `+37.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 14,200,000.00 USD | 112.35 USD | 0.00 USD | `+37.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 14,210,000.00 USD | 4,620.00 USD | 0.00 USD | `+37.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 14,260,000.00 USD | 54,080.00 USD | 0.00 USD | `+37.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 14,260,000.00 USD | 331.60 USD | 0.00 USD | `+38.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 14,530,000.00 USD | 270,270.00 USD | 0.00 USD | `+38.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 14,530,000.00 USD | 647.28 USD | 0.00 USD | `+38.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 14,650,000.00 USD | 116,220.00 USD | 0.00 USD | `+38.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 14,660,000.00 USD | 7,560.00 USD | 0.00 USD | `+39.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 14,660,000.00 USD | 1,890.00 USD | 0.00 USD | `+39.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 14,660,000.00 USD | 192.25 USD | 0.00 USD | `+40.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 14,660,000.00 USD | 465.29 USD | 0.00 USD | `+40.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 14,660,000.00 USD | 389.17 USD | 0.00 USD | `+40.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 14,660,000.00 USD | 826.57 USD | 0.00 USD | `+40.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 14,660,000.00 USD | 231.61 USD | 0.00 USD | `+40.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 14,660,000.00 USD | 2,910.00 USD | 0.00 USD | `+41.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 14,670,000.00 USD | 3,920.00 USD | 0.00 USD | `+41.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 14,690,000.00 USD | 26,260.00 USD | 0.00 USD | `+41.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.75` | 14,690,000.00 USD | 133.62 USD | 0.00 USD | `+41.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 14,710,000.00 USD | 14,550.00 USD | 0.00 USD | `+41.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 14,710,000.00 USD | 692.25 USD | 0.00 USD | `+42.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 14,710,000.00 USD | 406.24 USD | 0.00 USD | `+42.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 21,450,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+42.77%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 21,450,000.00 USD | 826.75 USD | 0.00 USD | `+42.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 23,650,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+42.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 23,650,000.00 USD | 5,920.00 USD | 0.00 USD | `+43.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 23,760,000.00 USD | 110,660.00 USD | 0.00 USD | `+44.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.45` | 23,770,000.00 USD | 12,120.00 USD | 0.00 USD | `+44.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 23,870,000.00 USD | 98,400.00 USD | 0.00 USD | `+44.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 23,870,000.00 USD | 990.88 USD | 0.00 USD | `+44.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 23,890,000.00 USD | 11,640.00 USD | 0.00 USD | `+45.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 23,890,000.00 USD | 6,190.00 USD | 0.00 USD | `+45.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 23,890,000.00 USD | 796.07 USD | 0.00 USD | `+45.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 23,890,000.00 USD | 826.73 USD | 0.00 USD | `+46.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 23,890,000.00 USD | 278.56 USD | 0.00 USD | `+46.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 24,220,000.00 USD | 329,100.00 USD | 0.00 USD | `+46.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.05` | 24,290,000.00 USD | 72,610.00 USD | 0.00 USD | `+47.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.15` | 24,310,000.00 USD | 16,980.00 USD | 0.00 USD | `+47.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 24,310,000.00 USD | 528.96 USD | 0.00 USD | `+47.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 24,320,000.00 USD | 6,330.00 USD | 0.00 USD | `+48.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 24,320,000.00 USD | 415.44 USD | 0.00 USD | `+48.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 24,600,000.00 USD | 282,520.00 USD | 0.00 USD | `+48.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 24,610,000.00 USD | 7,260.00 USD | 0.00 USD | `+48.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 24,610,000.00 USD | 791.78 USD | 0.00 USD | `+48.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 24,650,000.00 USD | 36,040.00 USD | 0.00 USD | `+49.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 24,650,000.00 USD | 209.16 USD | 0.00 USD | `+49.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 24,650,000.00 USD | 698.64 USD | 0.00 USD | `+49.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 24,840,000.00 USD | 190,100.00 USD | 0.00 USD | `+50.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 24,840,000.00 USD | 3,300.00 USD | 0.00 USD | `+50.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 24,840,000.00 USD | 1,020.00 USD | 0.00 USD | `+50.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 24,840,000.00 USD | 1,500.00 USD | 0.00 USD | `+51.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 24,880,000.00 USD | 37,700.00 USD | 0.00 USD | `+51.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 24,880,000.00 USD | 844.89 USD | 0.00 USD | `+51.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 24,890,000.00 USD | 4,610.00 USD | 0.00 USD | `+52.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 24,890,000.00 USD | 3,100.00 USD | 0.00 USD | `+52.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 26,230,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+52.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 26,230,000.00 USD | 1,370.00 USD | 0.00 USD | `+52.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 26,230,000.00 USD | 4,760.00 USD | 0.00 USD | `+52.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 26,230,000.00 USD | 549.99 USD | 0.00 USD | `+53.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 26,740,000.00 USD | 510,120.00 USD | 0.00 USD | `+53.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 26,990,000.00 USD | 249,190.00 USD | 0.00 USD | `+54.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 26,990,000.00 USD | 1,200.00 USD | 0.00 USD | `+54.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 26,990,000.00 USD | 178.92 USD | 0.00 USD | `+54.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 27,000,000.00 USD | 1,360.00 USD | 0.00 USD | `+54.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 27,010,000.00 USD | 14,430.00 USD | 0.00 USD | `+55.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 27,010,000.00 USD | 2,000.00 USD | 0.00 USD | `+55.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 27,010,000.00 USD | 411.94 USD | 0.00 USD | `+55.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 27,020,000.00 USD | 10,620.00 USD | 0.00 USD | `+57.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 27,020,000.00 USD | 1,020.00 USD | 0.00 USD | `+57.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 27,040,000.00 USD | 12,000.00 USD | 0.00 USD | `+58.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 27,040,000.00 USD | 113.04 USD | 0.00 USD | `+59.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 27,040,000.00 USD | 1,830.00 USD | 0.00 USD | `+59.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.35` | 27,060,000.00 USD | 22,680.00 USD | 0.00 USD | `+59.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 27,080,000.00 USD | 16,970.00 USD | 0.00 USD | `+60.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 27,080,000.00 USD | 2,230.00 USD | 0.00 USD | `+60.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 27,090,000.00 USD | 6,640.00 USD | 0.00 USD | `+62.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 27,100,000.00 USD | 15,880.00 USD | 0.00 USD | `+63.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 27,100,000.00 USD | 692.30 USD | 0.00 USD | `+63.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.95` | 27,110,000.00 USD | 5,620.00 USD | 0.00 USD | `+64.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 27,200,000.00 USD | 89,040.00 USD | 0.00 USD | `+64.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.05` | 27,200,000.00 USD | 281.84 USD | 0.00 USD | `+65.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 27,200,000.00 USD | 4,080.00 USD | 0.00 USD | `+67.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 27,290,000.00 USD | 89,230.00 USD | 0.00 USD | `+69.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 27,290,000.00 USD | 823.94 USD | 0.00 USD | `+70.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 27,290,000.00 USD | 211.39 USD | 0.00 USD | `+71.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 27,290,000.00 USD | 307.19 USD | 0.00 USD | `+71.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 27,290,000.00 USD | 593.03 USD | 0.00 USD | `+71.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 27,300,000.00 USD | 1,440.00 USD | 0.00 USD | `+72.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 27,300,000.00 USD | 5,720.00 USD | 0.00 USD | `+72.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 27,300,000.00 USD | 495.09 USD | 0.00 USD | `+74.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 27,300,000.00 USD | 912.63 USD | 0.00 USD | `+74.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 27,350,000.00 USD | 43,480.00 USD | 0.00 USD | `+74.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 27,350,000.00 USD | 686.20 USD | 0.00 USD | `+76.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 27,380,000.00 USD | 35,280.00 USD | 0.00 USD | `+76.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 27,380,000.00 USD | 703.60 USD | 0.00 USD | `+77.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 27,390,000.00 USD | 3,160.00 USD | 0.00 USD | `+77.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `174.85` | 27,390,000.00 USD | 1,430.00 USD | 0.00 USD | `+79.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 27,440,000.00 USD | 52,520.00 USD | 0.00 USD | `+79.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 27,460,000.00 USD | 21,960.00 USD | 0.00 USD | `+80.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 27,460,000.00 USD | 1,450.00 USD | 0.00 USD | `+81.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 27,460,000.00 USD | 885.25 USD | 0.00 USD | `+82.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 27,470,000.00 USD | 2,990.00 USD | 0.00 USD | `+83.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 27,470,000.00 USD | 261.56 USD | 0.00 USD | `+84.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 27,550,000.00 USD | 80,290.00 USD | 0.00 USD | `+85.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 27,550,000.00 USD | 2,440.00 USD | 0.00 USD | `+86.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 27,550,000.00 USD | 349.34 USD | 0.00 USD | `+87.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 27,570,000.00 USD | 19,620.00 USD | 0.00 USD | `+87.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 28,120,000.00 USD | 550,350.00 USD | 0.00 USD | `+88.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 28,150,000.00 USD | 29,610.00 USD | 0.00 USD | `+90.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 28,320,000.00 USD | 165,580.00 USD | 0.00 USD | `+92.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 28,460,000.00 USD | 141,190.00 USD | 0.00 USD | `+93.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 28,490,000.00 USD | 35,880.00 USD | 0.00 USD | `+95.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 28,490,000.00 USD | 744.27 USD | 0.00 USD | `+95.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.65` | 28,500,000.00 USD | 7,750.00 USD | 0.00 USD | `+96.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.05` | 28,510,000.00 USD | 4,270.00 USD | 0.00 USD | `+99.53%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `82.60` | 162,820,000.00 USD | 0.00 USD | 162,820,000.00 USD | 53,130.00 USD | 56,870.00 USD | 141,300.00 USD |
| `7D` | `82.80` | 162,570,000.00 USD | 0.00 USD | 162,570,000.00 USD | 1,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `83.00` | 162,570,000.00 USD | 0.00 USD | 162,570,000.00 USD | 1,690.00 USD | 2,080.00 USD | 0.00 USD |
| `7D` | `83.20` | 162,570,000.00 USD | 0.00 USD | 162,570,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD |
| `7D` | `83.40` | 162,530,000.00 USD | 0.00 USD | 162,530,000.00 USD | 0.00 USD | 0.00 USD | 579.46 USD |
| `7D` | `83.60` | 162,530,000.00 USD | 0.00 USD | 162,530,000.00 USD | 0.00 USD | 0.00 USD | 86,160.00 USD |
| `7D` | `83.80` | 162,440,000.00 USD | 0.00 USD | 162,440,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `84.20` | 162,430,000.00 USD | 0.00 USD | 162,430,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD |
| `7D` | `84.40` | 162,410,000.00 USD | 0.00 USD | 162,410,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD |
| `7D` | `85.20` | 162,380,000.00 USD | 0.00 USD | 162,380,000.00 USD | 0.00 USD | 218,580.00 USD | 0.00 USD |
| `7D` | `85.40` | 162,160,000.00 USD | 0.00 USD | 162,160,000.00 USD | 0.00 USD | 12,950.00 USD | 192,310.00 USD |
| `7D` | `85.60` | 161,960,000.00 USD | 0.00 USD | 161,960,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD |
| `7D` | `85.80` | 161,770,000.00 USD | 0.00 USD | 161,770,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD |
| `7D` | `86.20` | 161,510,000.00 USD | 0.00 USD | 161,510,000.00 USD | 0.00 USD | 12,130.00 USD | 199,350.00 USD |
| `7D` | `86.40` | 161,290,000.00 USD | 0.00 USD | 161,290,000.00 USD | 0.00 USD | 311,220.00 USD | 4,340.00 USD |
| `7D` | `86.80` | 160,980,000.00 USD | 0.00 USD | 160,980,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD |
| `7D` | `87.00` | 160,830,000.00 USD | 0.00 USD | 160,830,000.00 USD | 263,340.00 USD | 176,600.00 USD | 297,340.00 USD |
| `1D` | `87.20` | 174,240,000.00 USD | 0.00 USD | 174,240,000.00 USD | 129,420.00 USD | 138,340.00 USD | 351,900.00 USD |
| `7D` | `87.20` | 160,090,000.00 USD | 0.00 USD | 160,090,000.00 USD | 8,850.00 USD | 0.00 USD | 6,820.00 USD |
| `1D` | `87.40` | 173,620,000.00 USD | 0.00 USD | 173,620,000.00 USD | 30,080.00 USD | 232,930.00 USD | 109,500.00 USD |
| `7D` | `87.40` | 160,080,000.00 USD | 0.00 USD | 160,080,000.00 USD | 248,310.00 USD | 217,060.00 USD | 288,100.00 USD |
| `1D` | `87.60` | 173,250,000.00 USD | 0.00 USD | 173,250,000.00 USD | 105,350.00 USD | 295,330.00 USD | 57,210.00 USD |
| `7D` | `87.60` | 159,320,000.00 USD | 0.00 USD | 159,320,000.00 USD | 0.00 USD | 275,130.00 USD | 421,310.00 USD |
| `1D` | `87.80` | 172,790,000.00 USD | 0.00 USD | 172,790,000.00 USD | 90,150.00 USD | 276,230.00 USD | 716,950.00 USD |
| `7D` | `87.80` | 158,630,000.00 USD | 0.00 USD | 158,630,000.00 USD | 0.00 USD | 413,150.00 USD | 11,130.00 USD |
| `1D` | `88.00` | 171,710,000.00 USD | 0.00 USD | 171,710,000.00 USD | 47,860.00 USD | 202,660.00 USD | 485,910.00 USD |
| `7D` | `88.00` | 158,200,000.00 USD | 0.00 USD | 158,200,000.00 USD | 0.00 USD | 12,070.00 USD | 251,100.00 USD |
| `1D` | `88.20` | 170,970,000.00 USD | 0.00 USD | 170,970,000.00 USD | 140,490.00 USD | 168,390.00 USD | 365,710.00 USD |
| `7D` | `88.20` | 157,940,000.00 USD | 0.00 USD | 157,940,000.00 USD | 9,900.00 USD | 20,610.00 USD | 28,240.00 USD |
| `1D` | `88.40` | 170,300,000.00 USD | 0.00 USD | 170,300,000.00 USD | 84,680.00 USD | 178,840.00 USD | 65,030.00 USD |
| `7D` | `88.40` | 157,880,000.00 USD | 0.00 USD | 157,880,000.00 USD | 0.00 USD | 237,870.00 USD | 335,390.00 USD |
| `1D` | `88.60` | 169,970,000.00 USD | 0.00 USD | 169,970,000.00 USD | 68,370.00 USD | 64,340.00 USD | 0.00 USD |
| `1D` | `88.80` | 169,840,000.00 USD | 0.00 USD | 169,840,000.00 USD | 304,990.00 USD | 175,710.00 USD | 415,440.00 USD |
| `7D` | `88.80` | 157,310,000.00 USD | 0.00 USD | 157,310,000.00 USD | 241,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `89.00` | 168,940,000.00 USD | 0.00 USD | 168,940,000.00 USD | 8,600.00 USD | 11,540.00 USD | 227,790.00 USD |
| `7D` | `89.00` | 157,060,000.00 USD | 0.00 USD | 157,060,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD |
| `1D` | `89.20` | 168,690,000.00 USD | 0.00 USD | 168,690,000.00 USD | 377,030.00 USD | 119,090.00 USD | 11,970.00 USD |
| `7D` | `89.20` | 156,130,000.00 USD | 0.00 USD | 156,130,000.00 USD | 8,180.00 USD | 10,750.00 USD | 315,450.00 USD |
| `1D` | `89.40` | 168,180,000.00 USD | 0.00 USD | 168,180,000.00 USD | 5,150.00 USD | 292,120.00 USD | 274,990.00 USD |
| `7D` | `89.40` | 155,800,000.00 USD | 0.00 USD | 155,800,000.00 USD | 697,470.00 USD | 26,220.00 USD | 160,460.00 USD |
| `1D` | `89.60` | 167,610,000.00 USD | 0.00 USD | 167,610,000.00 USD | 138,450.00 USD | 5,250.00 USD | 135,260.00 USD |
| `7D` | `89.60` | 154,910,000.00 USD | 0.00 USD | 154,910,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD |
| `1D` | `89.80` | 167,330,000.00 USD | 0.00 USD | 167,330,000.00 USD | 54,220.00 USD | 91,280.00 USD | 440,250.00 USD |
| `7D` | `89.80` | 153,240,000.00 USD | 0.00 USD | 153,240,000.00 USD | 425,950.00 USD | 318,390.00 USD | 314,310.00 USD |
| `1D` | `90.00` | 166,750,000.00 USD | 0.00 USD | 166,750,000.00 USD | 686,700.00 USD | 302,220.00 USD | 278,530.00 USD |
| `7D` | `90.00` | 152,180,000.00 USD | 0.00 USD | 152,180,000.00 USD | 374,600.00 USD | 647,410.00 USD | 1,090,000.00 USD |
| `1D` | `90.20` | 165,480,000.00 USD | 0.00 USD | 165,480,000.00 USD | 822,890.00 USD | 930,230.00 USD | 363,600.00 USD |
| `7D` | `90.20` | 150,060,000.00 USD | 0.00 USD | 150,060,000.00 USD | 1,250,000.00 USD | 590,390.00 USD | 735,310.00 USD |
| `1D` | `90.40` | 163,360,000.00 USD | 0.00 USD | 163,360,000.00 USD | 779,410.00 USD | 544,380.00 USD | 671,130.00 USD |
| `7D` | `90.40` | 147,480,000.00 USD | 0.00 USD | 147,480,000.00 USD | 796,240.00 USD | 68,740.00 USD | 694,770.00 USD |
| `1D` | `90.60` | 161,370,000.00 USD | 0.00 USD | 161,370,000.00 USD | 676,760.00 USD | 671,710.00 USD | 840,150.00 USD |
| `7D` | `90.60` | 145,920,000.00 USD | 0.00 USD | 145,920,000.00 USD | 1,040,000.00 USD | 1,010,000.00 USD | 1,560,000.00 USD |
| `1D` | `90.80` | 159,180,000.00 USD | 0.00 USD | 159,180,000.00 USD | 404,570.00 USD | 518,670.00 USD | 250,200.00 USD |
| `7D` | `90.80` | 142,310,000.00 USD | 0.00 USD | 142,310,000.00 USD | 1,210,000.00 USD | 1,200,000.00 USD | 1,480,000.00 USD |
| `1D` | `91.00` | 158,010,000.00 USD | 0.00 USD | 158,010,000.00 USD | 1,020,000.00 USD | 597,650.00 USD | 483,730.00 USD |
| `7D` | `91.00` | 138,420,000.00 USD | 0.00 USD | 138,420,000.00 USD | 1,190,000.00 USD | 609,900.00 USD | 810,620.00 USD |
| `1D` | `91.20` | 155,900,000.00 USD | 0.00 USD | 155,900,000.00 USD | 16,980.00 USD | 493,060.00 USD | 403,810.00 USD |
| `7D` | `91.20` | 135,810,000.00 USD | 0.00 USD | 135,810,000.00 USD | 2,280,000.00 USD | 868,420.00 USD | 638,860.00 USD |
| `1D` | `91.40` | 154,990,000.00 USD | 0.00 USD | 154,990,000.00 USD | 664,720.00 USD | 758,110.00 USD | 111,340.00 USD |
| `7D` | `91.40` | 132,030,000.00 USD | 0.00 USD | 132,030,000.00 USD | 1,180,000.00 USD | 1,030,000.00 USD | 1,620,000.00 USD |
| `1D` | `91.60` | 153,450,000.00 USD | 0.00 USD | 153,450,000.00 USD | 488,750.00 USD | 281,460.00 USD | 1,100,000.00 USD |
| `7D` | `91.60` | 128,200,000.00 USD | 0.00 USD | 128,200,000.00 USD | 500,280.00 USD | 1,020,000.00 USD | 872,760.00 USD |
| `1D` | `91.80` | 151,580,000.00 USD | 0.00 USD | 151,580,000.00 USD | 526,140.00 USD | 449,000.00 USD | 713,610.00 USD |
| `7D` | `91.80` | 125,810,000.00 USD | 0.00 USD | 125,810,000.00 USD | 932,400.00 USD | 797,110.00 USD | 688,730.00 USD |
| `1D` | `92.00` | 149,890,000.00 USD | 0.00 USD | 149,890,000.00 USD | 2,810,000.00 USD | 2,220,000.00 USD | 1,110,000.00 USD |
| `7D` | `92.00` | 123,390,000.00 USD | 0.00 USD | 123,390,000.00 USD | 681,440.00 USD | 656,110.00 USD | 990,500.00 USD |
| `1D` | `92.20` | 143,750,000.00 USD | 0.00 USD | 143,750,000.00 USD | 887,260.00 USD | 1,630,000.00 USD | 465,660.00 USD |
| `7D` | `92.20` | 121,070,000.00 USD | 0.00 USD | 121,070,000.00 USD | 2,870,000.00 USD | 1,110,000.00 USD | 289,060.00 USD |
| `1D` | `92.40` | 140,770,000.00 USD | 0.00 USD | 140,770,000.00 USD | 731,980.00 USD | 331,330.00 USD | 2,170,000.00 USD |
| `7D` | `92.40` | 116,800,000.00 USD | 0.00 USD | 116,800,000.00 USD | 550,500.00 USD | 833,900.00 USD | 1,540,000.00 USD |
| `1D` | `92.60` | 137,540,000.00 USD | 0.00 USD | 137,540,000.00 USD | 1,330,000.00 USD | 1,530,000.00 USD | 2,410,000.00 USD |
| `7D` | `92.60` | 113,880,000.00 USD | 0.00 USD | 113,880,000.00 USD | 98,670.00 USD | 880,990.00 USD | 1,480,000.00 USD |
| `1D` | `92.80` | 132,260,000.00 USD | 0.00 USD | 132,260,000.00 USD | 1,940,000.00 USD | 824,500.00 USD | 775,910.00 USD |
| `7D` | `92.80` | 111,420,000.00 USD | 0.00 USD | 111,420,000.00 USD | 422,920.00 USD | 2,340,000.00 USD | 1,610,000.00 USD |
| `1D` | `93.00` | 128,720,000.00 USD | 0.00 USD | 128,720,000.00 USD | 2,640,000.00 USD | 3,760,000.00 USD | 3,040,000.00 USD |
| `7D` | `93.00` | 107,050,000.00 USD | 0.00 USD | 107,050,000.00 USD | 35,740.00 USD | 393,980.00 USD | 1,270,000.00 USD |
| `1D` | `93.20` | 119,280,000.00 USD | 0.00 USD | 119,280,000.00 USD | 2,380,000.00 USD | 1,620,000.00 USD | 1,940,000.00 USD |
| `7D` | `93.20` | 105,350,000.00 USD | 0.00 USD | 105,350,000.00 USD | 921,350.00 USD | 511,980.00 USD | 2,130,000.00 USD |
| `1D` | `93.40` | 113,350,000.00 USD | 0.00 USD | 113,350,000.00 USD | 3,070,000.00 USD | 3,100,000.00 USD | 2,300,000.00 USD |
| `7D` | `93.40` | 101,790,000.00 USD | 0.00 USD | 101,790,000.00 USD | 611,840.00 USD | 2,520,000.00 USD | 1,430,000.00 USD |
| `1D` | `93.60` | 104,880,000.00 USD | 0.00 USD | 104,880,000.00 USD | 1,950,000.00 USD | 3,880,000.00 USD | 1,070,000.00 USD |
| `7D` | `93.60` | 97,220,000.00 USD | 0.00 USD | 97,220,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,640,000.00 USD |
| `1D` | `93.80` | 97,980,000.00 USD | 0.00 USD | 97,980,000.00 USD | 1,010,000.00 USD | 1,030,000.00 USD | 483,140.00 USD |
| `7D` | `93.80` | 94,280,000.00 USD | 0.00 USD | 94,280,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,170,000.00 USD |
| `1D` | `94.00` | 95,460,000.00 USD | 0.00 USD | 95,460,000.00 USD | 759,420.00 USD | 1,060,000.00 USD | 1,830,000.00 USD |
| `7D` | `94.00` | 89,030,000.00 USD | 0.00 USD | 89,030,000.00 USD | 2,660,000.00 USD | 1,780,000.00 USD | 2,210,000.00 USD |
| `1D` | `94.20` | 91,820,000.00 USD | 0.00 USD | 91,820,000.00 USD | 1,980,000.00 USD | 1,940,000.00 USD | 2,160,000.00 USD |
| `7D` | `94.20` | 82,380,000.00 USD | 0.00 USD | 82,380,000.00 USD | 134,580.00 USD | 962,410.00 USD | 2,750,000.00 USD |
| `1D` | `94.40` | 85,730,000.00 USD | 0.00 USD | 85,730,000.00 USD | 1,650,000.00 USD | 568,640.00 USD | 1,010,000.00 USD |
| `7D` | `94.40` | 78,540,000.00 USD | 0.00 USD | 78,540,000.00 USD | 0.00 USD | 496,790.00 USD | 9,790.00 USD |
| `1D` | `94.60` | 82,510,000.00 USD | 0.00 USD | 82,510,000.00 USD | 142,910.00 USD | 1,380,000.00 USD | 396,580.00 USD |
| `7D` | `94.60` | 78,030,000.00 USD | 0.00 USD | 78,030,000.00 USD | 560,570.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `94.80` | 80,590,000.00 USD | 0.00 USD | 80,590,000.00 USD | 2,800,000.00 USD | 553,660.00 USD | 1,220,000.00 USD |
| `7D` | `94.80` | 77,470,000.00 USD | 0.00 USD | 77,470,000.00 USD | 2,010,000.00 USD | 99,300.00 USD | 3,360,000.00 USD |
| `1D` | `95.00` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 3,210,000.00 USD | 673,040.00 USD | 25,490.00 USD |
| `7D` | `95.00` | 72,000,000.00 USD | 0.00 USD | 72,000,000.00 USD | 2,400,000.00 USD | 4,460,000.00 USD | 47,940.00 USD |
| `1D` | `95.20` | 72,110,000.00 USD | 0.00 USD | 72,110,000.00 USD | 1,030,000.00 USD | 1,780,000.00 USD | 3,040,000.00 USD |
| `7D` | `95.20` | 65,100,000.00 USD | 0.00 USD | 65,100,000.00 USD | 2,080,000.00 USD | 0.00 USD | 17,980.00 USD |
| `1D` | `95.40` | 66,270,000.00 USD | 0.00 USD | 66,270,000.00 USD | 1,120,000.00 USD | 1,820,000.00 USD | 1,170,000.00 USD |
| `7D` | `95.40` | 62,990,000.00 USD | 0.00 USD | 62,990,000.00 USD | 2,080,000.00 USD | 2,340,000.00 USD | 4,590,000.00 USD |
| `1D` | `95.60` | 62,160,000.00 USD | 0.00 USD | 62,160,000.00 USD | 1,850,000.00 USD | 2,410,000.00 USD | 1,130,000.00 USD |
| `7D` | `95.60` | 53,980,000.00 USD | 0.00 USD | 53,980,000.00 USD | 3,820,000.00 USD | 7,040,000.00 USD | 4,590,000.00 USD |
| `1D` | `95.80` | 56,770,000.00 USD | 0.00 USD | 56,770,000.00 USD | 571,180.00 USD | 1,020,000.00 USD | 5,910,000.00 USD |
| `7D` | `95.80` | 38,540,000.00 USD | 0.00 USD | 38,540,000.00 USD | 3,400,000.00 USD | 93,510.00 USD | 1,280,000.00 USD |
| `1D` | `96.00` | 49,260,000.00 USD | 0.00 USD | 49,260,000.00 USD | 3,070,000.00 USD | 2,590,000.00 USD | 4,580,000.00 USD |
| `7D` | `96.00` | 33,770,000.00 USD | 0.00 USD | 33,770,000.00 USD | 2,670,000.00 USD | 728,410.00 USD | 3,590,000.00 USD |
| `1D` | `96.20` | 39,020,000.00 USD | 0.00 USD | 39,020,000.00 USD | 5,210,000.00 USD | 6,860,000.00 USD | 1,440,000.00 USD |
| `7D` | `96.20` | 26,780,000.00 USD | 0.00 USD | 26,780,000.00 USD | 6,840,000.00 USD | 1,580,000.00 USD | 5,250,000.00 USD |
| `1D` | `96.40` | 25,520,000.00 USD | 0.00 USD | 25,520,000.00 USD | 4,170,000.00 USD | 2,150,000.00 USD | 4,620,000.00 USD |
| `7D` | `96.40` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 1,600,000.00 USD | 2,590,000.00 USD | 6,470,000.00 USD |
| `1D` | `96.60` | 14,580,000.00 USD | 0.00 USD | 14,580,000.00 USD | 1,410,000.00 USD | 2,010,000.00 USD | 299,180.00 USD |
| `7D` | `96.60` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD |
| `1D` | `96.80` | 10,860,000.00 USD | 0.00 USD | 10,860,000.00 USD | 1,350,000.00 USD | 2,230,000.00 USD | 2,320,000.00 USD |
| `7D` | `96.80` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 0.00 USD | 79,170.00 USD | 2,350,000.00 USD |
| `1D` | `97.00` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 0.00 USD | 1,410,000.00 USD | 3,550,000.00 USD |
| `7D` | `97.00` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 2,870,000.00 USD | 2,160,000.00 USD |
| `7D` | `97.00` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 0.00 USD | 2,870,000.00 USD | 2,160,000.00 USD |
| `7D` | `97.20` | 16,470,000.00 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 3,100,000.00 USD | 3,310,000.00 USD |
| `1D` | `97.40` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 534,370.00 USD | 1,280,000.00 USD | 292,940.00 USD |
| `1D` | `97.40` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 534,370.00 USD | 1,280,000.00 USD | 292,940.00 USD |
| `7D` | `97.40` | 16,580,000.00 USD | 16,580,000.00 USD | 0.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD |
| `1D` | `97.60` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD |
| `7D` | `97.60` | 20,510,000.00 USD | 20,510,000.00 USD | 0.00 USD | 0.00 USD | 24,930.00 USD | 3,910,000.00 USD |
| `1D` | `97.80` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.80` | 31,530,000.00 USD | 31,530,000.00 USD | 0.00 USD | 7,580,000.00 USD | 3,430,000.00 USD | 0.00 USD |
| `1D` | `98.00` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 773,040.00 USD | 407,460.00 USD | 320,840.00 USD |
| `7D` | `98.00` | 42,960,000.00 USD | 42,960,000.00 USD | 0.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `98.20` | 13,930,000.00 USD | 13,930,000.00 USD | 0.00 USD | 2,200,000.00 USD | 1,790,000.00 USD | 1,450,000.00 USD |
| `7D` | `98.20` | 52,750,000.00 USD | 52,750,000.00 USD | 0.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `98.40` | 24,730,000.00 USD | 24,730,000.00 USD | 0.00 USD | 772,180.00 USD | 311,650.00 USD | 9,720,000.00 USD |
| `7D` | `98.40` | 63,880,000.00 USD | 63,880,000.00 USD | 0.00 USD | 1,780,000.00 USD | 3,320,000.00 USD | 6,030,000.00 USD |
| `1D` | `98.60` | 37,960,000.00 USD | 37,960,000.00 USD | 0.00 USD | 488,190.00 USD | 5,730,000.00 USD | 7,000,000.00 USD |
| `7D` | `98.60` | 73,110,000.00 USD | 73,110,000.00 USD | 0.00 USD | 1,880,000.00 USD | 5,400,000.00 USD | 1,950,000.00 USD |
| `1D` | `98.80` | 49,510,000.00 USD | 49,510,000.00 USD | 0.00 USD | 1,400,000.00 USD | 4,160,000.00 USD | 6,000,000.00 USD |
| `7D` | `98.80` | 76,060,000.00 USD | 76,060,000.00 USD | 0.00 USD | 71,480.00 USD | 470,960.00 USD | 2,410,000.00 USD |
| `1D` | `99.00` | 63,670,000.00 USD | 63,670,000.00 USD | 0.00 USD | 2,810,000.00 USD | 5,870,000.00 USD | 5,480,000.00 USD |
| `7D` | `99.00` | 84,240,000.00 USD | 84,240,000.00 USD | 0.00 USD | 1,830,000.00 USD | 2,380,000.00 USD | 3,960,000.00 USD |
| `1D` | `99.20` | 74,680,000.00 USD | 74,680,000.00 USD | 0.00 USD | 2,840,000.00 USD | 4,520,000.00 USD | 3,640,000.00 USD |
| `7D` | `99.20` | 97,930,000.00 USD | 97,930,000.00 USD | 0.00 USD | 1,220,000.00 USD | 6,240,000.00 USD | 6,240,000.00 USD |
| `1D` | `99.40` | 81,590,000.00 USD | 81,590,000.00 USD | 0.00 USD | 3,580,000.00 USD | 1,650,000.00 USD | 1,680,000.00 USD |
| `7D` | `99.40` | 98,970,000.00 USD | 98,970,000.00 USD | 0.00 USD | 0.00 USD | 1,010,000.00 USD | 25,850.00 USD |
| `1D` | `99.60` | 98,340,000.00 USD | 98,340,000.00 USD | 0.00 USD | 2,920,000.00 USD | 6,720,000.00 USD | 7,120,000.00 USD |
| `7D` | `99.60` | 104,400,000.00 USD | 104,400,000.00 USD | 0.00 USD | 2,240,000.00 USD | 2,640,000.00 USD | 545,090.00 USD |
| `1D` | `99.80` | 113,290,000.00 USD | 113,290,000.00 USD | 0.00 USD | 2,520,000.00 USD | 4,590,000.00 USD | 7,850,000.00 USD |
| `7D` | `99.80` | 107,730,000.00 USD | 107,730,000.00 USD | 0.00 USD | 736,270.00 USD | 1,330,000.00 USD | 1,270,000.00 USD |
| `1D` | `100.00` | 123,750,000.00 USD | 123,750,000.00 USD | 0.00 USD | 2,850,000.00 USD | 3,360,000.00 USD | 4,250,000.00 USD |
| `7D` | `100.00` | 119,060,000.00 USD | 119,060,000.00 USD | 0.00 USD | 2,220,000.00 USD | 2,310,000.00 USD | 6,790,000.00 USD |
| `1D` | `100.20` | 126,920,000.00 USD | 126,920,000.00 USD | 0.00 USD | 651,800.00 USD | 2,130,000.00 USD | 388,240.00 USD |
| `7D` | `100.20` | 125,140,000.00 USD | 125,140,000.00 USD | 0.00 USD | 843,770.00 USD | 2,460,000.00 USD | 2,780,000.00 USD |
| `1D` | `100.40` | 132,670,000.00 USD | 132,670,000.00 USD | 0.00 USD | 976,110.00 USD | 1,790,000.00 USD | 2,990,000.00 USD |
| `7D` | `100.40` | 129,620,000.00 USD | 129,620,000.00 USD | 0.00 USD | 993,830.00 USD | 654,600.00 USD | 2,830,000.00 USD |
| `1D` | `100.60` | 143,310,000.00 USD | 143,310,000.00 USD | 0.00 USD | 2,220,000.00 USD | 1,710,000.00 USD | 6,710,000.00 USD |
| `7D` | `100.60` | 135,400,000.00 USD | 135,400,000.00 USD | 0.00 USD | 2,110,000.00 USD | 1,450,000.00 USD | 2,220,000.00 USD |
| `1D` | `100.80` | 148,760,000.00 USD | 148,760,000.00 USD | 0.00 USD | 1,990,000.00 USD | 1,820,000.00 USD | 1,650,000.00 USD |
| `7D` | `100.80` | 137,140,000.00 USD | 137,140,000.00 USD | 0.00 USD | 491,210.00 USD | 1,220,000.00 USD | 23,970.00 USD |
| `1D` | `101.00` | 158,930,000.00 USD | 158,930,000.00 USD | 0.00 USD | 5,730,000.00 USD | 3,220,000.00 USD | 1,220,000.00 USD |
| `7D` | `101.00` | 155,780,000.00 USD | 155,780,000.00 USD | 0.00 USD | 4,000,000.00 USD | 6,900,000.00 USD | 7,750,000.00 USD |
| `1D` | `101.20` | 171,650,000.00 USD | 171,650,000.00 USD | 0.00 USD | 5,410,000.00 USD | 4,390,000.00 USD | 2,920,000.00 USD |
| `7D` | `101.20` | 175,050,000.00 USD | 175,050,000.00 USD | 0.00 USD | 7,240,000.00 USD | 5,180,000.00 USD | 6,850,000.00 USD |
| `1D` | `101.40` | 182,320,000.00 USD | 182,320,000.00 USD | 0.00 USD | 3,860,000.00 USD | 2,700,000.00 USD | 4,110,000.00 USD |
| `7D` | `101.40` | 192,110,000.00 USD | 192,110,000.00 USD | 0.00 USD | 4,720,000.00 USD | 1,270,000.00 USD | 11,070,000.00 USD |
| `1D` | `101.60` | 198,130,000.00 USD | 198,130,000.00 USD | 0.00 USD | 3,100,000.00 USD | 2,930,000.00 USD | 9,780,000.00 USD |
| `7D` | `101.60` | 202,630,000.00 USD | 202,630,000.00 USD | 0.00 USD | 3,650,000.00 USD | 30,170.00 USD | 6,840,000.00 USD |
| `1D` | `101.80` | 204,350,000.00 USD | 204,350,000.00 USD | 0.00 USD | 646,170.00 USD | 836,200.00 USD | 4,730,000.00 USD |
| `7D` | `101.80` | 212,560,000.00 USD | 212,560,000.00 USD | 0.00 USD | 3,050,000.00 USD | 609,510.00 USD | 6,270,000.00 USD |
| `1D` | `102.00` | 210,630,000.00 USD | 210,630,000.00 USD | 0.00 USD | 2,520,000.00 USD | 1,780,000.00 USD | 1,990,000.00 USD |
| `7D` | `102.00` | 218,550,000.00 USD | 218,550,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | 2,690,000.00 USD |
| `1D` | `102.20` | 216,980,000.00 USD | 216,980,000.00 USD | 0.00 USD | 3,180,000.00 USD | 1,360,000.00 USD | 1,800,000.00 USD |
| `7D` | `102.20` | 225,270,000.00 USD | 225,270,000.00 USD | 0.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,540,000.00 USD |
| `1D` | `102.40` | 221,480,000.00 USD | 221,480,000.00 USD | 0.00 USD | 1,560,000.00 USD | 716,320.00 USD | 2,220,000.00 USD |
| `7D` | `102.40` | 230,580,000.00 USD | 230,580,000.00 USD | 0.00 USD | 2,340,000.00 USD | 304,350.00 USD | 2,660,000.00 USD |
| `1D` | `102.60` | 224,110,000.00 USD | 224,110,000.00 USD | 0.00 USD | 985,660.00 USD | 606,030.00 USD | 1,040,000.00 USD |
| `7D` | `102.60` | 233,040,000.00 USD | 233,040,000.00 USD | 0.00 USD | 1,450,000.00 USD | 979,270.00 USD | 33,240.00 USD |
| `1D` | `102.80` | 228,160,000.00 USD | 228,160,000.00 USD | 0.00 USD | 1,260,000.00 USD | 1,570,000.00 USD | 1,220,000.00 USD |
| `7D` | `102.80` | 241,130,000.00 USD | 241,130,000.00 USD | 0.00 USD | 7,780,000.00 USD | 23,810.00 USD | 286,910.00 USD |
| `1D` | `103.00` | 233,220,000.00 USD | 233,220,000.00 USD | 0.00 USD | 3,120,000.00 USD | 1,440,000.00 USD | 498,100.00 USD |
| `7D` | `103.00` | 258,070,000.00 USD | 258,070,000.00 USD | 0.00 USD | 12,270,000.00 USD | 394,420.00 USD | 4,270,000.00 USD |
| `1D` | `103.20` | 235,590,000.00 USD | 235,590,000.00 USD | 0.00 USD | 301,000.00 USD | 853,780.00 USD | 1,220,000.00 USD |
| `7D` | `103.20` | 270,740,000.00 USD | 270,740,000.00 USD | 0.00 USD | 11,620,000.00 USD | 140,550.00 USD | 913,680.00 USD |
| `1D` | `103.40` | 238,510,000.00 USD | 238,510,000.00 USD | 0.00 USD | 867,130.00 USD | 1,180,000.00 USD | 877,320.00 USD |
| `7D` | `103.40` | 285,310,000.00 USD | 285,310,000.00 USD | 0.00 USD | 11,050,000.00 USD | 233,330.00 USD | 3,280,000.00 USD |
| `1D` | `103.60` | 246,140,000.00 USD | 246,140,000.00 USD | 0.00 USD | 2,430,000.00 USD | 183,360.00 USD | 5,010,000.00 USD |
| `7D` | `103.60` | 303,700,000.00 USD | 303,700,000.00 USD | 0.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD |
| `1D` | `103.80` | 249,300,000.00 USD | 249,300,000.00 USD | 0.00 USD | 481,980.00 USD | 1,320,000.00 USD | 1,350,000.00 USD |
| `7D` | `103.80` | 316,080,000.00 USD | 316,080,000.00 USD | 0.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD |
| `1D` | `104.00` | 255,150,000.00 USD | 255,150,000.00 USD | 0.00 USD | 2,410,000.00 USD | 1,540,000.00 USD | 1,910,000.00 USD |
| `7D` | `104.00` | 342,790,000.00 USD | 342,790,000.00 USD | 0.00 USD | 10,830,000.00 USD | 7,160,000.00 USD | 8,710,000.00 USD |
| `1D` | `104.20` | 258,570,000.00 USD | 258,570,000.00 USD | 0.00 USD | 1,440,000.00 USD | 931,620.00 USD | 1,050,000.00 USD |
| `7D` | `104.20` | 364,820,000.00 USD | 364,820,000.00 USD | 0.00 USD | 8,520,000.00 USD | 7,230,000.00 USD | 6,280,000.00 USD |
| `1D` | `104.40` | 263,420,000.00 USD | 263,420,000.00 USD | 0.00 USD | 1,860,000.00 USD | 1,510,000.00 USD | 1,490,000.00 USD |
| `7D` | `104.40` | 382,000,000.00 USD | 382,000,000.00 USD | 0.00 USD | 5,100,000.00 USD | 3,710,000.00 USD | 8,360,000.00 USD |
| `1D` | `104.60` | 267,660,000.00 USD | 267,660,000.00 USD | 0.00 USD | 1,060,000.00 USD | 868,480.00 USD | 2,310,000.00 USD |
| `7D` | `104.60` | 399,750,000.00 USD | 399,750,000.00 USD | 0.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 7,020,000.00 USD |
| `1D` | `104.80` | 271,680,000.00 USD | 271,680,000.00 USD | 0.00 USD | 1,250,000.00 USD | 820,470.00 USD | 1,950,000.00 USD |
| `7D` | `104.80` | 417,140,000.00 USD | 417,140,000.00 USD | 0.00 USD | 5,170,000.00 USD | 4,410,000.00 USD | 7,820,000.00 USD |
| `1D` | `105.00` | 272,900,000.00 USD | 272,900,000.00 USD | 0.00 USD | 463,890.00 USD | 350,040.00 USD | 413,950.00 USD |
| `7D` | `105.00` | 433,310,000.00 USD | 433,310,000.00 USD | 0.00 USD | 5,730,000.00 USD | 4,110,000.00 USD | 6,330,000.00 USD |
| `1D` | `105.20` | 273,970,000.00 USD | 273,970,000.00 USD | 0.00 USD | 111,930.00 USD | 94,030.00 USD | 864,650.00 USD |
| `7D` | `105.20` | 443,970,000.00 USD | 443,970,000.00 USD | 0.00 USD | 5,340,000.00 USD | 2,800,000.00 USD | 2,530,000.00 USD |
| `1D` | `105.40` | 274,450,000.00 USD | 274,450,000.00 USD | 0.00 USD | 262,490.00 USD | 138,720.00 USD | 78,430.00 USD |
| `7D` | `105.40` | 452,190,000.00 USD | 452,190,000.00 USD | 0.00 USD | 1,570,000.00 USD | 3,170,000.00 USD | 3,470,000.00 USD |
| `1D` | `105.60` | 274,880,000.00 USD | 274,880,000.00 USD | 0.00 USD | 130,280.00 USD | 187,950.00 USD | 110,700.00 USD |
| `7D` | `105.60` | 464,240,000.00 USD | 464,240,000.00 USD | 0.00 USD | 4,800,000.00 USD | 2,700,000.00 USD | 4,550,000.00 USD |
| `1D` | `105.80` | 275,570,000.00 USD | 275,570,000.00 USD | 0.00 USD | 87,540.00 USD | 526,970.00 USD | 76,760.00 USD |
| `7D` | `105.80` | 473,050,000.00 USD | 473,050,000.00 USD | 0.00 USD | 2,690,000.00 USD | 2,620,000.00 USD | 3,510,000.00 USD |
| `1D` | `106.00` | 276,730,000.00 USD | 276,730,000.00 USD | 0.00 USD | 372,000.00 USD | 554,120.00 USD | 226,820.00 USD |
| `7D` | `106.00` | 478,200,000.00 USD | 478,200,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,050,000.00 USD | 2,130,000.00 USD |
| `1D` | `106.20` | 278,140,000.00 USD | 278,140,000.00 USD | 0.00 USD | 623,340.00 USD | 349,490.00 USD | 440,280.00 USD |
| `7D` | `106.20` | 487,100,000.00 USD | 487,100,000.00 USD | 0.00 USD | 3,820,000.00 USD | 2,560,000.00 USD | 2,520,000.00 USD |
| `1D` | `106.40` | 278,870,000.00 USD | 278,870,000.00 USD | 0.00 USD | 181,780.00 USD | 354,890.00 USD | 197,110.00 USD |
| `7D` | `106.40` | 493,160,000.00 USD | 493,160,000.00 USD | 0.00 USD | 2,420,000.00 USD | 2,170,000.00 USD | 1,470,000.00 USD |
| `1D` | `106.60` | 280,550,000.00 USD | 280,550,000.00 USD | 0.00 USD | 388,660.00 USD | 278,100.00 USD | 1,010,000.00 USD |
| `7D` | `106.60` | 499,810,000.00 USD | 499,810,000.00 USD | 0.00 USD | 1,870,000.00 USD | 1,460,000.00 USD | 3,310,000.00 USD |
| `1D` | `106.80` | 281,930,000.00 USD | 281,930,000.00 USD | 0.00 USD | 340,680.00 USD | 316,760.00 USD | 718,820.00 USD |
| `7D` | `106.80` | 504,460,000.00 USD | 504,460,000.00 USD | 0.00 USD | 999,190.00 USD | 918,930.00 USD | 2,730,000.00 USD |
| `1D` | `107.00` | 282,690,000.00 USD | 282,690,000.00 USD | 0.00 USD | 193,920.00 USD | 413,830.00 USD | 147,220.00 USD |
| `7D` | `107.00` | 508,600,000.00 USD | 508,600,000.00 USD | 0.00 USD | 527,980.00 USD | 1,180,000.00 USD | 2,430,000.00 USD |
| `1D` | `107.20` | 283,170,000.00 USD | 283,170,000.00 USD | 0.00 USD | 0.00 USD | 50,140.00 USD | 436,040.00 USD |
| `7D` | `107.20` | 509,690,000.00 USD | 509,690,000.00 USD | 0.00 USD | 230,020.00 USD | 507,570.00 USD | 352,500.00 USD |
| `1D` | `107.40` | 284,010,000.00 USD | 284,010,000.00 USD | 0.00 USD | 90,150.00 USD | 226,090.00 USD | 523,690.00 USD |
| `7D` | `107.40` | 510,980,000.00 USD | 510,980,000.00 USD | 0.00 USD | 0.00 USD | 576,040.00 USD | 709,670.00 USD |
| `1D` | `107.60` | 284,750,000.00 USD | 284,750,000.00 USD | 0.00 USD | 47,860.00 USD | 202,660.00 USD | 485,910.00 USD |
| `7D` | `107.60` | 511,610,000.00 USD | 511,610,000.00 USD | 0.00 USD | 213,520.00 USD | 12,070.00 USD | 406,020.00 USD |
| `1D` | `107.80` | 285,420,000.00 USD | 285,420,000.00 USD | 0.00 USD | 140,490.00 USD | 168,390.00 USD | 365,710.00 USD |
| `7D` | `107.80` | 512,440,000.00 USD | 512,440,000.00 USD | 0.00 USD | 499,550.00 USD | 31,020.00 USD | 305,630.00 USD |
| `1D` | `108.00` | 285,750,000.00 USD | 285,750,000.00 USD | 0.00 USD | 84,680.00 USD | 178,840.00 USD | 65,030.00 USD |
| `7D` | `108.00` | 513,020,000.00 USD | 513,020,000.00 USD | 0.00 USD | 5,950.00 USD | 237,870.00 USD | 335,390.00 USD |
| `1D` | `108.20` | 285,880,000.00 USD | 285,880,000.00 USD | 0.00 USD | 68,370.00 USD | 62,390.00 USD | 0.00 USD |
| `7D` | `108.20` | 513,300,000.00 USD | 513,300,000.00 USD | 0.00 USD | 0.00 USD | 205,080.00 USD | 74,400.00 USD |
| `7D` | `108.40` | 513,790,000.00 USD | 513,790,000.00 USD | 0.00 USD | 487,890.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `108.60` | 513,980,000.00 USD | 513,980,000.00 USD | 0.00 USD | 17,470.00 USD | 167,730.00 USD | 0.00 USD |
| `7D` | `108.80` | 515,820,000.00 USD | 515,820,000.00 USD | 0.00 USD | 624,820.00 USD | 397,420.00 USD | 819,150.00 USD |
| `7D` | `109.00` | 516,110,000.00 USD | 516,110,000.00 USD | 0.00 USD | 8,180.00 USD | 0.00 USD | 286,720.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `5.61B` | Total OI Tokens: `57,630,108.2 SOL`
  * 1h OI Change: `+0.45%` | 4h OI Change: `-1.98%` | 24h OI Change: `-12.82%`
  * Exchange Breakdown: Binance=`971.23M` | Bybit=`611.51M` | OKX=`390.88M` | Hyperliquid=`521.91M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-134.78K` | Last 24h: `177.62K` | Last 3d: `997.77K` | Last 7d: `2.11M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0019%` | **USDT OKX** | `-0.0239%` |
| **USDT Bybit** | `-0.0127%` | **USDT KuCoin** | `-0.0110%` |
| **USDT MEXC** | `0.0018%` | **USDT BingX** | `0.0017%` |
| **USDT Gate** | `-0.0129%` | **USDT Bitget** | `-0.0113%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0053%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `42.64%` | `57.36%` | `0.74` | 51,350,000.00 USD |
| `15M` | `Binance` | `39.39%` | `60.61%` | `0.65` | 12,520,000.00 USD |
| `15M` | `OKX` | `32.2%` | `67.8%` | `0.47` | 9,820,000.00 USD |
| `15M` | `Bybit` | `50.81%` | `49.19%` | `1.03` | 2,570,000.00 USD |
| `15M` | `KuCoin` | `48.32%` | `51.68%` | `0.93` | 147,880.00 USD |
| `15M` | `Gate` | `46.35%` | `53.65%` | `0.86` | 3,510,000.00 USD |
| `15M` | `Bitget` | `41.46%` | `58.54%` | `0.71` | 3,180,000.00 USD |
| `15M` | `BingX` | `43.43%` | `56.57%` | `0.77` | 2,390,000.00 USD |
| `15M` | `MEXC` | `48.34%` | `51.66%` | `0.94` | 9,500,000.00 USD |
| `15M` | `Bitunix` | `54.22%` | `45.78%` | `1.18` | 2,250,000.00 USD |
| `15M` | `Hyperliquid` | `36.2%` | `63.8%` | `0.57` | 1,770,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.63%` | `48.37%` | `1.07` | 2,190,000.00 USD |
| `15M` | `Crypto.com` | `34.3%` | `65.7%` | `0.52` | 129,270.00 USD |
| `15M` | `WhiteBIT` | `69.6%` | `30.4%` | `2.29` | 519,280.00 USD |
| `15M` | `HTX` | `46.9%` | `53.1%` | `0.88` | 67,290.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `46.75%` | `53.25%` | `0.88` | 281,790.00 USD |
| `15M` | `Aster` | `58.91%` | `41.09%` | `1.43` | 209,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `57.17%` | `42.83%` | `1.33` | 276,330.00 USD |
| `15M` | `Whale Positions` | `39.39%` | `60.61%` | `0.65` | 12,520,000.00 USD |
| `15M` | `Global Accounts` | `42.64%` | `57.36%` | `0.74` | 51,350,000.00 USD |
| `1H` | `SOL` | `49.93%` | `50.07%` | `1.00` | 100,510,000.00 USD |
| `1H` | `Binance` | `51.29%` | `48.71%` | `1.05` | 32,150,000.00 USD |
| `1H` | `OKX` | `48.55%` | `51.45%` | `0.94` | 8,550,000.00 USD |
| `1H` | `Bybit` | `60.46%` | `39.54%` | `1.53` | 16,080,000.00 USD |
| `1H` | `KuCoin` | `57.84%` | `42.16%` | `1.37` | 974,580.00 USD |
| `1H` | `Gate` | `56.2%` | `43.8%` | `1.28` | 6,890,000.00 USD |
| `1H` | `Bitget` | `51.34%` | `48.66%` | `1.06` | 8,110,000.00 USD |
| `1H` | `BingX` | `28.78%` | `71.22%` | `0.40` | 2,160,000.00 USD |
| `1H` | `MEXC` | `46.45%` | `53.55%` | `0.87` | 11,390,000.00 USD |
| `1H` | `Bitunix` | `47.64%` | `52.36%` | `0.91` | 3,470,000.00 USD |
| `1H` | `Hyperliquid` | `72.03%` | `27.97%` | `2.58` | 3,780,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `56.66%` | `43.34%` | `1.31` | 486,860.00 USD |
| `1H` | `Crypto.com` | `56.48%` | `43.52%` | `1.30` | 240,120.00 USD |
| `1H` | `WhiteBIT` | `1.44%` | `98.56%` | `0.01` | 4,540,000.00 USD |
| `1H` | `HTX` | `46.76%` | `53.24%` | `0.88` | 34,580.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `19.89%` | `80.11%` | `0.25` | 721,110.00 USD |
| `1H` | `Aster` | `26.41%` | `73.59%` | `0.36` | 780,700.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.39%` | `39.61%` | `1.52` | 161,670.00 USD |
| `1H` | `Whale Positions` | `51.29%` | `48.71%` | `1.05` | 32,150,000.00 USD |
| `1H` | `Global Accounts` | `49.93%` | `50.07%` | `1.00` | 100,510,000.00 USD |
| `4H` | `SOL` | `48.47%` | `51.53%` | `0.94` | 1,090,000,000.00 USD |
| `4H` | `Binance` | `47.08%` | `52.92%` | `0.89` | 326,570,000.00 USD |
| `4H` | `OKX` | `48.02%` | `51.98%` | `0.92` | 221,340,000.00 USD |
| `4H` | `Bybit` | `50.24%` | `49.76%` | `1.01` | 121,240,000.00 USD |
| `4H` | `KuCoin` | `49.94%` | `50.06%` | `1.00` | 4,810,000.00 USD |
| `4H` | `Gate` | `52.47%` | `47.53%` | `1.10` | 78,770,000.00 USD |
| `4H` | `Bitget` | `44.1%` | `55.9%` | `0.79` | 50,890,000.00 USD |
| `4H` | `BingX` | `46.22%` | `53.78%` | `0.86` | 45,120,000.00 USD |
| `4H` | `MEXC` | `45.42%` | `54.58%` | `0.83` | 94,220,000.00 USD |
| `4H` | `Bitunix` | `48.24%` | `51.76%` | `0.93` | 58,240,000.00 USD |
| `4H` | `Hyperliquid` | `52.26%` | `47.74%` | `1.09` | 41,960,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.31%` | `48.69%` | `1.05` | 12,920,000.00 USD |
| `4H` | `Crypto.com` | `50.14%` | `49.86%` | `1.01` | 2,290,000.00 USD |
| `4H` | `WhiteBIT` | `87.08%` | `12.92%` | `6.74` | 14,090,000.00 USD |
| `4H` | `HTX` | `55.74%` | `44.26%` | `1.26` | 1,710,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `30.45%` | `69.55%` | `0.44` | 1,070,000.00 USD |
| `4H` | `Aster` | `46.19%` | `53.81%` | `0.86` | 6,930,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `42.5%` | `57.5%` | `0.74` | 12,660,000.00 USD |
| `4H` | `Whale Positions` | `47.08%` | `52.92%` | `0.89` | 326,570,000.00 USD |
| `4H` | `Global Accounts` | `48.47%` | `51.53%` | `0.94` | 1,090,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `98.16` | `98.20` | `98.16` | `98.53` | `98.00` | 14,041,198.88 USD | 6,875,129.47 USD | 7,166,069.42 USD | -290,939.95 USD | `-2.07%` | `8B / 3S` |
| `5:00 UTC` | `98.00` | `98.10` | `98.00` | `98.38` | `97.82` | 11,697,482.78 USD | 5,190,334.49 USD | 6,507,148.30 USD | -1,316,813.81 USD | `-11.26%` | `5B / 11S` |
| `0:00 UTC` | `98.09` | `98.10` | `98.09` | `98.28` | `97.90` | 11,316,185.46 USD | 4,994,801.42 USD | 6,321,384.04 USD | -1,326,582.61 USD | `-11.72%` | `0B / 11S` |
| `5:00 UTC` | `97.95` | `97.99` | `97.95` | `98.12` | `97.90` | 8,075,212.15 USD | 2,930,391.45 USD | 5,144,820.70 USD | -2,214,429.25 USD | `-27.42%` | `1B / 4S` |
| `0:00 UTC` | `97.70` | `97.69` | `97.70` | `98.20` | `97.19` | 26,621,435.83 USD | 11,084,087.20 USD | 15,537,348.64 USD | -4,453,261.44 USD | `-16.73%` | `5B / 32S` |
| `5:00 UTC` | `97.31` | `97.23` | `97.31` | `97.59` | `96.94` | 34,349,154.70 USD | 16,069,023.45 USD | 18,280,131.25 USD | -2,211,107.80 USD | `-6.44%` | `8B / 12S` |
| `0:00 UTC` | `97.07` | `97.11` | `97.07` | `97.31` | `96.84` | 19,320,776.86 USD | 9,044,516.83 USD | 10,276,260.03 USD | -1,231,743.19 USD | `-6.38%` | `6B / 9S` |
| `5:00 UTC` | `97.31` | `97.36` | `97.31` | `97.56` | `97.18` | 14,539,694.05 USD | 7,744,567.35 USD | 6,795,126.70 USD | 949,440.65 USD | `+6.53%` | `8B / 2S` |
| `0:00 UTC` | `97.15` | `97.19` | `97.15` | `97.37` | `97.05` | 9,961,152.58 USD | 4,407,159.48 USD | 5,553,993.10 USD | -1,146,833.62 USD | `-11.51%` | `1B / 5S` |
| `5:00 UTC` | `97.03` | `97.06` | `97.03` | `97.13` | `97.03` | 1,897,044.68 USD | 583,786.63 USD | 1,313,258.05 USD | -729,471.42 USD | `-38.45%` | `1B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 18:37` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `101.13` | 0.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 500K SOL` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `101.76` | 0.00 USD | 0.00 USD |
| `10-28 15:32` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.87` | 99,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Volume 500K SOL` | `Divergence` | **`BULLISH`** | Drop without taker selling | `102.88` | 0.00 USD | 0.00 USD |
| `10-28 13:30` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `102.22` | 103,000.00 USD | 0.00 USD |
| `10-28 10:59` | `Volume 500K SOL` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `101.76` | 110,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -210,460.00 USD | -4,170,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -479,490.00 USD | -6,580,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -253,680.00 USD | -7,510,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 2,120,000.00 USD | -7,610,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -881,700.00 USD | -30,780,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 3,130,000.00 USD | -30,500,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 5,440,000.00 USD | 10,210,000.00 USD | **`ACCUMULATION`** |
| `8h` | 13,430,000.00 USD | -83,110,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -30,010,000.00 USD | -227,260,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -43,140,000.00 USD | -424,520,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 31,990,000.00 USD | -687,610,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -1,820,000.00 USD | -2,190,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-210.46K` | 15m=`-479.49K` | 1h=`+2.12M` | 24h=`-43.14M`
* Futures Capital Netflows: 5m=`-4.17M` | 15m=`-6.58M` | 1h=`-7.61M` | 24h=`-424.52M`
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
  * `2026-10-30 14:10:12 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:12 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `94.96` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `93.87` (Risk Distance: `1.09` pts)
  * +2.5R Take Profit: `97.67`
  * Mathematical Lot Sizing: **`9.21 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `98.09` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `99.18` (Risk Distance: `1.09` pts)
  * +2.5R Take Profit: `95.38`
  * Mathematical Lot Sizing: **`9.21 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`97.76`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
