# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XRP
**Canonical Key**: `XRP` | **Broker Instrument**: `XRPUSD.pi` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 08:54:58 IST` (`2026-10-30 03:24:58 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1.22` | **Live Ask Quote**: `1.23` | **Mid Price**: `1.23`
- **Spread Points**: `5.00` | **Spread BPS**: `40.80 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `1.21` | VWAP Z-Score: `+1.01` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0115` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `41.99` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1.24` | Lower -3.00σ Band: `1.19`
  * Upper +2.51σ Band: `1.23` | Lower -2.51σ Band: `1.20`
  * Upper +2.01σ Band: `1.23` | Lower -2.01σ Band: `1.20`
  * Upper +2.00σ Band: `1.23` | Lower -2.00σ Band: `1.20`
  * Upper +1.28σ Band: `1.22` | Lower -1.28σ Band: `1.20`
  * Upper +1.00σ Band: `1.22` | Lower -1.00σ Band: `1.21`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1.22` | EMA-20=`1.23` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1.25` (Slope: `+0.0000`) | EMA-100=`1.27`
  * Institutional Anchors: EMA-144=`1.28` | EMA-200=`1.28` (Slope: `-0.7015`) | EMA-233=`1.29`
- **Range Boundaries**: 24H High=`1.31` | 24H Low=`1.19` | Weekly High=`1.34` | Weekly Low=`1.19`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1.26` (Distance: `-2.76%`)
  * Point of Control (POC) = `1.25` (Distance: `-1.59%`)
  * Value Area Low (VAL) = `1.22` (Distance: `+0.64%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1.31` | POC=`1.29` | VAL=`1.28`
  * Prior Day Extremes: PDH=`1.33` | PDL=`1.22` | PDC=`1.24`
  * Monday Range Blueprint: High=`1.30` | Mid=`1.29` | Low=`1.27`
  * Developing Weekly Value Area: Weekly VAH=`1.32` | Weekly POC=`1.29` | Weekly VAL=`1.28`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1.26` | Low=`1.19`
  * London Session (08:00-16:00 UTC): High=`1.23` | Low=`1.22`
  * New York Session (13:00-21:00 UTC): High=`1.23` | Low=`1.22`
  * Initial Balance (First Hour): IB High=`1.23` | IB Low=`1.22`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1.22` - `1.23`
  * Optimal Trade Entry (OTE 0.705): `1.23`
  * Structural Invalidation Anchor (0.786): `1.24`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `1.22` | `1.22` | `1.22` | `1.22` | `2,521,092` | 3,073,673.58 USD | 983,756.96 USD | `+32.01%` | -53,596,800.46 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `1.22` | `1.23` | `1.22` | `1.22` | `3,642,808` | 4,462,142.85 USD | 101,853.48 USD | `+2.28%` | -53,494,946.98 USD | `+0.24` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `1.22` | `1.23` | `1.22` | `1.23` | `2,441,755` | 2,994,423.96 USD | 870,686.04 USD | `+29.08%` | -52,624,260.94 USD | `+0.81` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `1.22` | `1.23` | `1.22` | `1.22` | `9,143,244` | 11,190,777.85 USD | -274,594.69 USD | `-2.45%` | -52,701,145.61 USD | `-0.13` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `1.22` | `1.22` | `1.22` | `1.22` | `7,984,378` | 9,740,915.81 USD | -287,366.00 USD | `-2.95%` | -52,988,511.62 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `1.22` | `1.23` | `1.22` | `1.23` | `6,084,564` | 7,456,566.80 USD | 972,539.53 USD | `+13.04%` | -52,015,972.09 USD | `+0.34` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `1.22` | `1.23` | `1.20` | `1.21` | `65,407,468` | 79,255,485.65 USD | -5,075,130.35 USD | `-6.40%` | -54,164,861.34 USD | `-0.28` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `1.21` | `1.23` | `1.21` | `1.22` | `41,352,402` | 50,352,977.66 USD | 2,483,683.00 USD | `+4.93%` | -51,681,178.34 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `1.22` | `1.23` | `1.22` | `1.23` | `6,090,805` | 7,464,234.49 USD | 980,196.90 USD | `+13.13%` | -50,700,981.44 USD | `+0.39` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -16,707,900.94 USD | `-1.69` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -44,798,035.15 USD | `-1.70` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.24` | `1.20` | `1.23` | `253,075,745` | 308,028,812.06 USD | -5,910,616.94 USD | `-1.92%` | -50,708,652.09 USD | `+0.25` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `1.29` | `1.30` | `1.29` | `1.29` | `51,543,790` | 66,567,053.49 USD | -1,316,863.99 USD | `-1.98%` | -3,158,099.65 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `1.29` | `1.31` | `1.29` | `1.31` | `105,451,962` | 136,952,441.12 USD | 1,861,993.66 USD | `+1.36%` | -1,296,105.99 USD | `+1.40` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `1.31` | `1.32` | `1.28` | `1.28` | `114,056,020` | 147,369,675.26 USD | -15,411,794.95 USD | `-10.46%` | -16,707,900.94 USD | `-1.69` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.28` | `1.28` | `1.22` | `1.24` | `424,836,006` | 530,340,937.40 USD | -28,090,134.21 USD | `-5.30%` | -44,798,035.15 USD | `-1.70` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `1.24` | `1.24` | `1.20` | `1.23` | `253,075,745` | 308,028,812.06 USD | -5,910,616.94 USD | `-1.92%` | -50,708,652.09 USD | `+0.25` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`1.23`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:53:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `27` | `0x31b1...1434` | `LONG` | 42,966,048.90 USD | `35,031,430.00` | `1.13` | `1.23` | `0.9612` | 3,387,165.63 USD | `+7.88%` | `10X Cross` |
| `92` | `0x5b5d...c060` | `SHORT` | 19,575,364.58 USD | `15,964,251.00` | `1.44` | `1.23` | `11.93` | 3,340,704.13 USD | `+17.07%` | `5X Cross` |
| `157` | `0xb83d...6e36` | `SHORT` | 12,947,314.97 USD | `10,555,450.00` | `1.50` | `1.23` | `14.56` | 2,875,254.67 USD | `+22.21%` | `5X Cross` |
| `423` | `0xca49...53c8` | `SHORT` | 5,076,757.57 USD | `4,138,886.00` | `1.44` | `1.23` | `5.00` | 876,565.16 USD | `+17.27%` | `20X Cross` |
| `427` | `0xfc27...9d9d` | `SHORT` | 5,036,808.77 USD | `4,102,471.00` | `1.29` | `1.23` | `5.95` | 269,244.59 USD | `+5.35%` | `20X Cross` |
| `439` | `0xecb6...2b00` | `SHORT` | 4,902,583.45 USD | `3,993,958.00` | `1.27` | `1.23` | `8.45` | 183,728.60 USD | `+3.75%` | `10X Cross` |
| `444` | `0xdd53...2b13` | `SHORT` | 4,822,862.54 USD | `3,930,293.00` | `1.40` | `1.23` | `17.94` | 688,517.15 USD | `+14.28%` | `3X Cross` |
| `504` | `0x610b...b613` | `LONG` | 4,344,169.01 USD | `3,543,946.00` | `1.44` | `1.23` | `0.8563` | -755,823.60 USD | `-17.40%` | `5X Cross` |
| `674` | `0x9946...0852` | `SHORT` | 3,278,296.26 USD | `2,671,145.00` | `1.43` | `1.23` | `1.88` | 530,205.76 USD | `+16.17%` | `20X Cross` |
| `675` | `0xc30c...a4c9` | `SHORT` | 3,276,005.51 USD | `2,672,981.00` | `1.42` | `1.23` | `1.61` | 510,958.59 USD | `+15.60%` | `6X Cross` |
| `706` | `0xf48f...10fe` | `LONG` | 3,147,184.52 USD | `2,565,779.00` | `1.53` | `1.23` | `1.02` | -777,456.21 USD | `-24.70%` | `4X Cross` |
| `750` | `0x58f0...0d20` | `LONG` | 3,024,240.82 USD | `2,466,352.00` | `1.25` | `1.23` | `1.18` | -53,058.02 USD | `-1.75%` | `20X Cross` |
| `752` | `0x023a...2355` | `SHORT` | 3,016,757.86 USD | `2,458,445.00` | `1.32` | `1.23` | `3.38` | 228,434.83 USD | `+7.57%` | `20X Cross` |
| `753` | `0x45d2...4029` | `SHORT` | 3,011,670.75 USD | `2,453,000.00` | `1.48` | `1.23` | `19.35` | 626,609.67 USD | `+20.81%` | `20X Cross` |
| `1091` | `0xeadc...9d55` | `LONG` | 1,986,204.89 USD | `1,619,805.00` | `1.21` | `1.23` | `0.000000` | 27,361.87 USD | `+1.38%` | `20X Cross` |
| `1158` | `0x94b2...599e` | `SHORT` | 1,889,201.44 USD | `1,540,696.00` | `1.36` | `1.23` | `1.89` | 211,265.02 USD | `+11.18%` | `20X Cross` |
| `1167` | `0xbcd4...0dd2` | `SHORT` | 1,876,036.86 USD | `1,529,461.00` | `1.31` | `1.23` | `1.92` | 128,507.73 USD | `+6.85%` | `20X Cross` |
| `1176` | `0x3fc5...c0c1` | `SHORT` | 1,853,441.05 USD | `1,511,779.00` | `1.52` | `1.23` | `2.49` | 438,173.55 USD | `+23.64%` | `20X Cross` |
| `1209` | `0x31ef...f715` | `LONG` | 1,807,858.05 USD | `1,475,080.00` | `1.49` | `1.23` | `1.04` | -391,407.35 USD | `-21.65%` | `3X Isolated` |
| `1255` | `0x7737...bf66` | `SHORT` | 1,733,616.05 USD | `1,413,466.00` | `1.41` | `1.23` | `13.19` | 265,252.60 USD | `+15.30%` | `10X Cross` |
| `1319` | `0x95da...2328` | `LONG` | 1,624,562.95 USD | `1,324,876.00` | `1.35` | `1.23` | `0.1668` | -169,078.15 USD | `-10.41%` | `5X Cross` |
| `1337` | `0xee2b...d67e` | `LONG` | 1,603,071.72 USD | `1,306,284.00` | `1.55` | `1.23` | `0.4680` | -427,583.18 USD | `-26.67%` | `4X Cross` |
| `1403` | `0x215d...f80a` | `LONG` | 1,536,305.91 USD | `1,251,777.00` | `1.32` | `1.23` | `1.13` | -118,148.31 USD | `-7.69%` | `14X Cross` |
| `1413` | `0x5fa3...35b7` | `SHORT` | 1,522,402.84 USD | `1,240,651.00` | `1.30` | `1.23` | `2.79` | 94,106.82 USD | `+6.18%` | `20X Cross` |
| `1446` | `0x123d...3bff` | `LONG` | 1,491,330.22 USD | `1,215,329.00` | `1.35` | `1.23` | `0.000000` | -145,739.01 USD | `-9.77%` | `10X Cross` |
| `1466` | `0x7fda...17d1` | `LONG` | 1,465,074.03 USD | `1,193,543.00` | `1.21` | `1.23` | `0.000000` | 18,317.14 USD | `+1.25%` | `20X Cross` |
| `1506` | `0xdf95...7d72` | `SHORT` | 1,424,548.12 USD | `1,160,528.00` | `1.37` | `1.23` | `35.68` | 168,927.02 USD | `+11.86%` | `20X Cross` |
| `1575` | `0xef96...9383` | `SHORT` | 1,341,628.04 USD | `1,092,976.00` | `1.34` | `1.23` | `4.65` | 121,119.40 USD | `+9.03%` | `20X Cross` |
| `1628` | `0xc179...e0c8` | `SHORT` | 1,281,858.57 USD | `1,044,965.00` | `1.30` | `1.23` | `7.26` | 73,691.62 USD | `+5.75%` | `10X Cross` |
| `1658` | `0xb1ce...681b` | `LONG` | 1,254,419.66 USD | `1,021,764.00` | `1.49` | `1.23` | `1.16` | -269,636.83 USD | `-21.49%` | `4X Isolated` |
| `1769` | `0x3c36...461a` | `LONG` | 1,153,066.56 USD | `940,051.00` | `1.30` | `1.23` | `1.05` | -66,014.06 USD | `-5.73%` | `10X Cross` |
| `1795` | `0x9aa5...58af` | `SHORT` | 1,136,596.48 USD | `926,397.00` | `1.46` | `1.23` | `11.40` | 214,434.58 USD | `+18.87%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,004.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.3302 USD [API] | `2026-10-28 20:54:28` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,779.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.78K USD at 1.3302 USD [API] | `2026-10-28 20:54:28` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 11,929.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 11.93K USD at 1.3302 USD [API] | `2026-10-28 20:54:28` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,439.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.44K USD at 1.3307 USD [API] | `2026-10-28 20:54:22` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,960.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.96K USD at 1.3306 USD [API] | `2026-10-28 20:54:22` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 27,579.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 27.58K USD at 1.3299 USD [API] | `2026-10-28 20:57:48` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 13,328.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 13.33K USD at 1.3299 USD [API] | `2026-10-28 20:57:48` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,354.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 9.35K USD at 1.3299 USD [API] | `2026-10-28 20:57:48` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,950.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.95K USD at 1.3300 USD [API] | `2026-10-28 20:57:48` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 25,270.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 25.27K USD at 1.3300 USD [API] | `2026-10-28 20:57:48` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 39,332.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 39.33K USD at 1.3300 USD [API] | `2026-10-28 20:57:48` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,531.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.53K USD at 1.3309 USD [API] | `2026-10-28 21:09:22` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 39,406.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 39.41K USD at 1.3309 USD [API] | `2026-10-28 21:09:22` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,615.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 9.62K USD at 1.3309 USD [API] | `2026-10-28 21:09:22` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,511.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.51K USD at 1.3325 USD [API] | `2026-10-28 21:19:52` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,271.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.27K USD at 1.3333 USD [API] | `2026-10-28 21:21:50` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 13,431.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 13.43K USD at 1.3270 USD [API] | `2026-10-28 21:30:21` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,004.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.00K USD at 1.3270 USD [API] | `2026-10-28 21:30:21` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,375.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.38K USD at 1.3270 USD [API] | `2026-10-28 21:30:21` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 13,482.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 13.48K USD at 1.3270 USD [API] | `2026-10-28 21:30:21` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,706.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.71K USD at 1.3270 USD [API] | `2026-10-28 21:30:21` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 13,502.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 13.50K USD at 1.3289 USD [API] | `2026-10-28 21:40:44` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,216.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.22K USD at 1.3317 USD [API] | `2026-10-28 21:46:35` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,847.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.85K USD at 1.3329 USD [API] | `2026-10-28 21:53:39` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 9,187.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 9.19K USD at 1.3306 USD [API] | `2026-10-28 22:14:33` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,707.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.71K USD at 1.3274 USD [API] | `2026-10-28 22:21:20` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,373.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.37K USD at 1.3276 USD [API] | `2026-10-28 22:30:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,792.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.79K USD at 1.3276 USD [API] | `2026-10-28 22:30:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,005.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3276 USD [API] | `2026-10-28 22:30:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,030.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.03K USD at 1.3276 USD [API] | `2026-10-28 22:30:58` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,004.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.00K USD at 1.3279 USD [API] | `2026-10-28 22:36:48` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,214.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.21K USD at 1.2887 USD [API] | `2026-10-23 22:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 559.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.56K USD at 1.2887 USD [API] | `2026-10-23 22:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,998.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.2887 USD [API] | `2026-10-23 22:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,750.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.75K USD at 1.2887 USD [API] | `2026-10-23 22:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 15.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.02K USD at 1.2887 USD [API] | `2026-10-23 22:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.2887 USD [API] | `2026-10-23 22:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 74.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.07K USD at 1.2887 USD [API] | `2026-10-23 22:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,399.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.40K USD at 1.2888 USD [API] | `2026-10-23 22:50:55` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,137.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 2.14K USD at 1.3354 USD [API] | `2026-10-20 14:14:55` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,589.57 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.59K USD at 1.3353 USD [API] | `2026-10-20 14:14:55` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 6,262.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 6.26K USD at 1.3353 USD [API] | `2026-10-20 14:14:55` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 132.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.13K USD at 1.3353 USD [API] | `2026-10-20 14:14:55` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 17,061.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 17.06K USD at 1.3352 USD [API] | `2026-10-20 14:14:55` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,590.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 5.59K USD at 1.3351 USD [API] | `2026-10-20 14:14:55` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 17,058.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 17.06K USD at 1.3350 USD [API] | `2026-10-20 14:14:55` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 954.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 0.95K USD at 1.3350 USD [API] | `2026-10-20 14:14:55` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 17,047.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 17.05K USD at 1.3737 USD [API] | `2026-10-08 15:19:06` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 1,127.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.13K USD at 1.3737 USD [API] | `2026-10-08 15:19:06` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 9,684.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.68K USD at 1.4625 USD [API] | `2026-10-02 18:39:33` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 2,358.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.36K USD at 1.4827 USD [API] | `2026-09-29 16:49:26` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 3,998.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4827 USD [API] | `2026-09-29 16:49:26` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 5,000.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.4828 USD [API] | `2026-09-29 16:49:26` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 3,999.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4828 USD [API] | `2026-09-29 16:49:26` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 13.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.4828 USD [API] | `2026-09-29 16:49:26` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 99.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.10K USD at 1.4828 USD [API] | `2026-09-29 16:49:26` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 10,015.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.02K USD at 1.4891 USD [API] | `2026-09-28 03:31:22` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,578.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.58K USD at 1.4891 USD [API] | `2026-09-28 03:31:22` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 3,486.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.49K USD at 1.5075 USD [API] | `2026-09-26 20:42:41` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 3,999.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.5075 USD [API] | `2026-09-26 20:42:41` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 399.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.5075 USD [API] | `2026-09-26 20:42:41` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 208.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.21K USD at 1.5076 USD [API] | `2026-09-26 20:42:41` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 4,082.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.08K USD at 1.5076 USD [API] | `2026-09-26 20:42:41` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 3,999.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.5076 USD [API] | `2026-09-26 20:42:41` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 8,807.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.81K USD at 1.5076 USD [API] | `2026-09-26 20:42:41` |
| `ANNOUNCEMENT` | `INFO` | `1.55` | 18,106.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 18.11K USD at 1.5465 USD [API] | `2026-09-23 14:11:53` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 7,868.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.87K USD at 1.3266 USD [API] | `2026-10-28 22:40:59` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,630.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.63K USD at 1.3272 USD [API] | `2026-10-28 22:43:29` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,005.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3270 USD [API] | `2026-10-28 22:55:14` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,372.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.37K USD at 1.3271 USD [API] | `2026-10-28 22:55:14` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 19,875.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 19.88K USD at 1.3250 USD [API] | `2026-10-28 23:02:01` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 893.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.89K USD at 1.3420 USD [API] | `2026-10-28 20:01:48` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,567.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.57K USD at 1.3420 USD [API] | `2026-10-28 20:01:48` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,527.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.53K USD at 1.3420 USD [API] | `2026-10-28 20:01:48` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 101.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.10K USD at 1.3420 USD [API] | `2026-10-28 20:01:48` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,589.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.59K USD at 1.3263 USD [API] | `2026-10-28 23:07:45` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 5,185.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.19K USD at 1.3266 USD [API] | `2026-10-28 23:13:04` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 10,026.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.03K USD at 1.3266 USD [API] | `2026-10-28 23:13:04` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 8,527.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.53K USD at 1.3266 USD [API] | `2026-10-28 23:13:04` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 4,883.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.88K USD at 1.2590 USD [API] | `2026-10-24 15:16:27` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 44.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.04K USD at 1.2590 USD [API] | `2026-10-24 15:16:27` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 2,221.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.22K USD at 1.2591 USD [API] | `2026-10-24 15:16:27` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 2,221.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.22K USD at 1.2591 USD [API] | `2026-10-24 15:16:27` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 2,725.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.73K USD at 1.2591 USD [API] | `2026-10-24 15:16:27` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 138.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.14K USD at 1.2591 USD [API] | `2026-10-24 15:16:27` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 49.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.2591 USD [API] | `2026-10-24 15:16:27` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 7,028.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.03K USD at 1.2592 USD [API] | `2026-10-24 15:16:27` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 5,801.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.80K USD at 1.2592 USD [API] | `2026-10-24 15:16:27` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 5,415.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.42K USD at 1.2592 USD [API] | `2026-10-24 15:16:27` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,700.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.70K USD at 1.2861 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 7,243.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.24K USD at 1.2861 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 167.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.17K USD at 1.2861 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 9,459.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.46K USD at 1.2861 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,790.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.79K USD at 1.2861 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 10.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.2861 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 19,888.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 19.89K USD at 1.2862 USD [API] | `2026-10-23 22:53:45` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,037.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.04K USD at 1.3133 USD [API] | `2026-10-22 16:48:52` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,922.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.92K USD at 1.3133 USD [API] | `2026-10-22 16:48:52` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,999.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3133 USD [API] | `2026-10-22 16:48:52` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 2,663.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.66K USD at 1.3134 USD [API] | `2026-10-22 16:48:52` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,999.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3134 USD [API] | `2026-10-22 16:48:52` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 394.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.39K USD at 1.3135 USD [API] | `2026-10-22 16:48:52` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,999.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3135 USD [API] | `2026-10-22 16:48:52` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,506.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.51K USD at 1.3136 USD [API] | `2026-10-22 16:48:52` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 218.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.22K USD at 1.3136 USD [API] | `2026-10-22 16:48:52` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 53.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3136 USD [API] | `2026-10-22 16:48:52` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 3,923.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.92K USD at 1.3503 USD [API] | `2026-10-22 01:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 38,742.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 38.74K USD at 1.3504 USD [API] | `2026-10-22 01:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 2,719.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.72K USD at 1.3504 USD [API] | `2026-10-22 01:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 2,039.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.04K USD at 1.3504 USD [API] | `2026-10-22 01:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 1,359.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.36K USD at 1.3504 USD [API] | `2026-10-22 01:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 679.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.68K USD at 1.3504 USD [API] | `2026-10-22 01:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 679.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.68K USD at 1.3504 USD [API] | `2026-10-22 01:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.35` | 426.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.43K USD at 1.3504 USD [API] | `2026-10-22 01:41:01` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 9,920.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.92K USD at 1.2733 USD [API] | `2026-10-17 21:34:43` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 9,549.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.55K USD at 1.2733 USD [API] | `2026-10-17 21:34:43` |
| `ANNOUNCEMENT` | `INFO` | `1.27` | 5,836.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.84K USD at 1.2733 USD [API] | `2026-10-17 21:34:43` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 21,150.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 21.15K USD at 1.3069 USD [API] | `2026-10-16 15:53:08` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,005.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.01K USD at 1.3069 USD [API] | `2026-10-16 15:53:08` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,381.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.38K USD at 1.3069 USD [API] | `2026-10-16 15:53:08` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,999.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3069 USD [API] | `2026-10-16 15:53:08` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,024.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.02K USD at 1.3069 USD [API] | `2026-10-16 15:53:08` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 4,026.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.03K USD at 1.3070 USD [API] | `2026-10-16 15:53:08` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 3,999.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3070 USD [API] | `2026-10-16 15:53:08` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 809.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.81K USD at 1.3070 USD [API] | `2026-10-16 15:53:08` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 14.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3070 USD [API] | `2026-10-16 15:53:08` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 4,036.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.04K USD at 1.3071 USD [API] | `2026-10-16 15:53:08` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,004.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3071 USD [API] | `2026-10-16 15:53:08` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 4,187.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.19K USD at 1.3071 USD [API] | `2026-10-16 15:53:08` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 11,571.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 11.57K USD at 1.3018 USD [API] | `2026-10-15 02:22:28` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 4,612.28 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.61K USD at 1.3018 USD [API] | `2026-10-15 02:22:28` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 100.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.10K USD at 1.3018 USD [API] | `2026-10-15 02:22:28` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 98.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.10K USD at 1.3020 USD [API] | `2026-10-15 02:22:28` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 1,469.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.47K USD at 1.3020 USD [API] | `2026-10-15 02:22:28` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,939.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.94K USD at 1.3020 USD [API] | `2026-10-15 02:22:28` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 18,155.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 18.16K USD at 1.3020 USD [API] | `2026-10-15 02:22:28` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 3,481.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.48K USD at 1.3020 USD [API] | `2026-10-15 02:22:28` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 648.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.65K USD at 1.3403 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 92.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.09K USD at 1.3403 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,438.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.44K USD at 1.3404 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,173.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.17K USD at 1.3404 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,999.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3404 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 501.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.3404 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,171.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.17K USD at 1.3404 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 501.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.3404 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 414.21 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.41K USD at 1.3405 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,939.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.94K USD at 1.3405 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 50.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3405 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 50.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3405 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,998.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3405 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,416.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.42K USD at 1.3405 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,597.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.60K USD at 1.3405 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 6,114.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.11K USD at 1.3405 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 120.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.12K USD at 1.3405 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 222.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.22K USD at 1.3406 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 289.57 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.29K USD at 1.3406 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 585.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.59K USD at 1.3406 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,174.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.17K USD at 1.3406 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,689.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.69K USD at 1.3406 USD [API] | `2026-10-14 14:11:06` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 21,329.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 21.33K USD at 1.3391 USD [API] | `2026-10-12 23:34:26` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 7,667.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.67K USD at 1.3391 USD [API] | `2026-10-12 23:34:26` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,233.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.23K USD at 1.3392 USD [API] | `2026-10-12 23:34:26` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,830.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.83K USD at 1.3392 USD [API] | `2026-10-12 23:34:26` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 8,878.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.88K USD at 1.3392 USD [API] | `2026-10-12 23:34:26` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,031.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.03K USD at 1.3392 USD [API] | `2026-10-12 23:34:26` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 7,668.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.67K USD at 1.3392 USD [API] | `2026-10-12 23:34:26` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,520.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.52K USD at 1.3393 USD [API] | `2026-10-12 23:34:26` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 15,230.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 15.23K USD at 1.3750 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 11.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3750 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 184.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.18K USD at 1.3750 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 173.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.17K USD at 1.3750 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,999.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3750 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,689.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.69K USD at 1.3750 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 171.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.17K USD at 1.3750 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,005.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.01K USD at 1.3750 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 68.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.07K USD at 1.3750 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 8,111.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.11K USD at 1.3751 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 50.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3751 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 125.13 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.13K USD at 1.3751 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,998.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3751 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 4,247.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.25K USD at 1.3752 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 412.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.41K USD at 1.3752 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 13,046.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 13.05K USD at 1.3752 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 99.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.10K USD at 1.3752 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,999.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3752 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,724.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.72K USD at 1.3753 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,999.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3753 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 5,665.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.67K USD at 1.3755 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 8,479.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.48K USD at 1.3755 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 8,479.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.48K USD at 1.3755 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 5,666.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.67K USD at 1.3756 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 6,243.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.24K USD at 1.3756 USD [API] | `2026-10-12 14:39:46` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 3,520.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.52K USD at 1.3756 USD [API] | `2026-10-12 14:39:40` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 5,556.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.56K USD at 1.3756 USD [API] | `2026-10-12 14:39:40` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 5,090.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.09K USD at 1.3757 USD [API] | `2026-10-12 14:39:40` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 9,672.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.67K USD at 1.3757 USD [API] | `2026-10-12 14:39:40` |
| `ANNOUNCEMENT` | `INFO` | `1.38` | 1,888.84 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.89K USD at 1.3757 USD [API] | `2026-10-12 14:39:40` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 2,737.53 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.74K USD at 1.4951 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 7,938.98 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.94K USD at 1.4951 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 562.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.56K USD at 1.4951 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 554.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.55K USD at 1.4951 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 3,999.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4951 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 10,726.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.73K USD at 1.4952 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 165.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.17K USD at 1.4952 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 2,248.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.25K USD at 1.4952 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 3,999.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4952 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 681.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.68K USD at 1.4952 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 1,999.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.00K USD at 1.4952 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 4,049.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.05K USD at 1.4953 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 5,973.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.97K USD at 1.4953 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 3,999.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4953 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 3,998.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4954 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 2,965.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.97K USD at 1.4954 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 7,937.58 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.94K USD at 1.4954 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 285.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.29K USD at 1.4955 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 3,998.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4955 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 5,000.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.4955 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 2,235.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.24K USD at 1.4956 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 3,999.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4956 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 49.35 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.4956 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 3,849.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.85K USD at 1.4956 USD [API] | `2026-10-02 17:15:54` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 1,730.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.73K USD at 1.4954 USD [API] | `2026-10-02 17:15:51` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 3,998.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4954 USD [API] | `2026-10-02 17:15:51` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 73.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.07K USD at 1.4954 USD [API] | `2026-10-02 17:15:51` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 1,021.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.02K USD at 1.4954 USD [API] | `2026-10-02 17:15:51` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 4,049.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.05K USD at 1.4955 USD [API] | `2026-10-02 17:15:51` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 3,998.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4955 USD [API] | `2026-10-02 17:15:51` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 6,120.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.12K USD at 1.4956 USD [API] | `2026-10-02 17:15:51` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 91,838.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 91.84K USD at 1.4779 USD [API] | `2026-10-01 08:35:13` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 3,999.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4779 USD [API] | `2026-10-01 08:35:13` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 4,943.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.94K USD at 1.4780 USD [API] | `2026-10-01 08:35:13` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 2,243.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.24K USD at 1.4780 USD [API] | `2026-10-01 08:35:13` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 521.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.52K USD at 1.4780 USD [API] | `2026-10-01 08:35:13` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 3,999.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4780 USD [API] | `2026-10-01 08:35:13` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 48.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.4780 USD [API] | `2026-10-01 08:35:13` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 2,639.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.64K USD at 1.4780 USD [API] | `2026-10-01 08:35:13` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 663.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.66K USD at 1.4780 USD [API] | `2026-10-01 08:35:13` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 208.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.21K USD at 1.4780 USD [API] | `2026-10-01 08:35:13` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 328.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.33K USD at 1.4777 USD [API] | `2026-10-01 08:35:11` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 53.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.4777 USD [API] | `2026-10-01 08:35:11` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 2,929.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.93K USD at 1.4778 USD [API] | `2026-10-01 08:35:11` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 23,644.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 23.64K USD at 1.4778 USD [API] | `2026-10-01 08:35:11` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 818.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.82K USD at 1.4778 USD [API] | `2026-10-01 08:35:11` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 11.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.4740 USD [API] | `2026-09-29 01:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 10,091.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.09K USD at 1.4740 USD [API] | `2026-09-29 01:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 3,998.96 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4740 USD [API] | `2026-09-29 01:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 40,316.85 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 40.32K USD at 1.4740 USD [API] | `2026-09-29 01:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 33,313.87 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 33.31K USD at 1.4740 USD [API] | `2026-09-29 01:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 1,474.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.47K USD at 1.4740 USD [API] | `2026-09-29 01:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 3,999.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4741 USD [API] | `2026-09-29 01:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 5,137.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.14K USD at 1.4741 USD [API] | `2026-09-29 01:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 5,471.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.47K USD at 1.4741 USD [API] | `2026-09-29 01:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 8,153.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.15K USD at 1.4742 USD [API] | `2026-09-29 01:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 2,715.48 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.72K USD at 1.4742 USD [API] | `2026-09-29 01:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 3,999.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4742 USD [API] | `2026-09-29 01:19:43` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 22,020.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 22.02K USD at 1.4745 USD [API] | `2026-09-29 01:19:34` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 1,626.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.63K USD at 1.4745 USD [API] | `2026-09-29 01:19:34` |
| `ANNOUNCEMENT` | `INFO` | `1.47` | 6,032.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.03K USD at 1.4745 USD [API] | `2026-09-29 01:19:34` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 11,352.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 11.35K USD at 1.4855 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,998.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4855 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 20,770.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 20.77K USD at 1.4856 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,999.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4856 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,999.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4857 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 9,999.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.00K USD at 1.4858 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,999.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4858 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 2,887.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.89K USD at 1.4859 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,998.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4859 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 2,619.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.62K USD at 1.4860 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,998.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4860 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 104.03 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.10K USD at 1.4861 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 5,813.62 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.81K USD at 1.4861 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 4,971.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.97K USD at 1.4861 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 4,024.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.02K USD at 1.4861 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,999.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4861 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 445.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.45K USD at 1.4862 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,999.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4862 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,281.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.28K USD at 1.4863 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,999.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4863 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 4,972.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.97K USD at 1.4864 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 4,025.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.03K USD at 1.4864 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 445.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.45K USD at 1.4864 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,999.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4864 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 138.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.14K USD at 1.4864 USD [API] | `2026-09-28 03:31:59` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 11,517.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 11.52K USD at 1.4856 USD [API] | `2026-09-28 03:31:55` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,999.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4856 USD [API] | `2026-09-28 03:31:55` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 2,267.18 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.27K USD at 1.4857 USD [API] | `2026-09-28 03:31:55` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 4,250.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.25K USD at 1.4857 USD [API] | `2026-09-28 03:31:55` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,999.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.4857 USD [API] | `2026-09-28 03:31:55` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 2,921.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.92K USD at 1.4858 USD [API] | `2026-09-28 03:31:55` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 1,435.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.44K USD at 1.5122 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 4,095.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.10K USD at 1.5122 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 14,176.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 14.18K USD at 1.5122 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 13,327.90 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 13.33K USD at 1.5123 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 3,998.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.5123 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 1,649.92 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.65K USD at 1.5123 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 8,805.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.81K USD at 1.5124 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 3,998.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.5124 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 33,324.22 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 33.32K USD at 1.5124 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 48,283.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 48.28K USD at 1.5124 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 2,614.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.61K USD at 1.5124 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 12,590.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 12.59K USD at 1.5124 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 12.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.5125 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 3,109.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.11K USD at 1.5125 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 1,650.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.65K USD at 1.5126 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 202.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.20K USD at 1.5126 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 4,999.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.5127 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 6,478.89 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.48K USD at 1.5127 USD [API] | `2026-09-26 20:40:06` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 12,067.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 12.07K USD at 1.5136 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 399.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.5136 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 7,568.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.57K USD at 1.5136 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 2,281.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.28K USD at 1.5136 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 3,998.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.5136 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 1,651.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.65K USD at 1.5136 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 4,999.75 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.5137 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.51` | 8,255.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 8.26K USD at 1.5137 USD [API] | `2026-09-26 20:40:02` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 6,381.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.38K USD at 1.3270 USD [API] | `2026-10-28 23:22:54` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 237.53 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.24K USD at 1.3420 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 193.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.19K USD at 1.3421 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,752.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.75K USD at 1.3421 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,552.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.55K USD at 1.3421 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 505.97 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.51K USD at 1.3421 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,996.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.00K USD at 1.3423 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 36,396.49 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 36.40K USD at 1.3424 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 400.04 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3424 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 53.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3424 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 166.47 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.17K USD at 1.3425 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,037.71 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.04K USD at 1.3425 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,753.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.75K USD at 1.3425 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,152.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.15K USD at 1.3426 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,754.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.75K USD at 1.3426 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 13,568.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 13.57K USD at 1.3428 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 1,499.91 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.50K USD at 1.3428 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,154.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.15K USD at 1.3429 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,130.77 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.13K USD at 1.3431 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 9,162.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.16K USD at 1.3431 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 6,871.30 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.87K USD at 1.3431 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,003.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3432 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 5,002.82 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.3434 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 2,009.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.01K USD at 1.3435 USD [API] | `2026-10-08 15:23:27` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 17,373.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 17.37K USD at 1.3250 USD [API] | `2026-10-28 23:50:00` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 19,875.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 19.88K USD at 1.3250 USD [API] | `2026-10-28 23:51:12` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,800.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.80K USD at 1.3240 USD [API] | `2026-10-29 00:10:19` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,944.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.94K USD at 1.3240 USD [API] | `2026-10-29 00:10:19` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,012.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.01K USD at 1.3240 USD [API] | `2026-10-29 00:10:19` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 32,462.17 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 32.46K USD at 1.3245 USD [API] | `2026-10-29 00:10:43` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,833.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.83K USD at 1.3245 USD [API] | `2026-10-29 00:10:43` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3245 USD [API] | `2026-10-29 00:10:43` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,673.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.67K USD at 1.3244 USD [API] | `2026-10-29 00:16:28` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,591.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.59K USD at 1.3230 USD [API] | `2026-10-29 00:21:23` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 30,298.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 30.30K USD at 1.3230 USD [API] | `2026-10-29 00:22:31` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 31,405.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 31.41K USD at 1.3230 USD [API] | `2026-10-29 00:22:31` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 25,590.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 25.59K USD at 1.3230 USD [API] | `2026-10-29 00:22:31` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,410.31 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 8.41K USD at 1.3230 USD [API] | `2026-10-29 00:22:31` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,194.74 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.19K USD at 1.3235 USD [API] | `2026-10-29 00:30:53` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3234 USD [API] | `2026-10-29 00:43:09` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 29,859.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 29.86K USD at 1.3222 USD [API] | `2026-10-29 00:50:57` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,000.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 10.00K USD at 1.3220 USD [API] | `2026-10-29 00:53:55` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,975.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 6.98K USD at 1.3181 USD [API] | `2026-10-29 01:15:46` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 6,269.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 6.27K USD at 1.3186 USD [API] | `2026-10-29 01:18:22` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3187 USD [API] | `2026-10-29 01:18:22` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 5,005.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3187 USD [API] | `2026-10-29 01:18:22` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 33,334.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 33.33K USD at 1.3187 USD [API] | `2026-10-29 01:18:22` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 8,344.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.34K USD at 1.3176 USD [API] | `2026-10-29 01:21:01` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 10,493.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 10.49K USD at 1.3176 USD [API] | `2026-10-29 01:21:01` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 24,542.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 24.54K USD at 1.3175 USD [API] | `2026-10-29 01:21:01` |
| `ANNOUNCEMENT` | `INFO` | `1.32` | 7,114.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 7.11K USD at 1.3175 USD [API] | `2026-10-29 01:21:01` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 40,493.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 40.49K USD at 1.3101 USD [API] | `2026-10-29 01:39:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,006.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.01K USD at 1.3102 USD [API] | `2026-10-29 01:39:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 7,861.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 7.86K USD at 1.3102 USD [API] | `2026-10-29 01:39:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,125.50 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale SELL: 5.13K USD at 1.3102 USD [API] | `2026-10-29 01:39:23` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,491.94 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.49K USD at 1.3101 USD [API] | `2026-10-29 01:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 39,284.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 39.28K USD at 1.3101 USD [API] | `2026-10-29 01:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 8,058.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 8.06K USD at 1.3101 USD [API] | `2026-10-29 01:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 13,338.42 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 13.34K USD at 1.3100 USD [API] | `2026-10-29 01:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,710.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.71K USD at 1.3078 USD [API] | `2026-10-29 01:42:24` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 1,813.44 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Short: 1.81K USD at 1.3084 USD [API] | `2026-10-29 01:42:21` |
| `ANNOUNCEMENT` | `INFO` | `1.31` | 5,005.67 USD | `-` | `NEWS_INTEL` | `-` | #XRP Whale BUY: 5.01K USD at 1.3097 USD [API] | `2026-10-29 01:44:12` |
| `ANNOUNCEMENT` | `INFO` | `1.28` | 1,108.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.11K USD at 1.2850 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 5,005.46 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.01K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 3,999.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 6,087.52 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.09K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 1,535.69 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.54K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 105.38 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.11K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 889.29 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.89K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,446.45 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.45K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.29` | 4,856.39 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.86K USD at 1.2851 USD [API] | `2026-10-23 22:55:16` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,427.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.43K USD at 1.3357 USD [API] | `2026-10-22 08:02:50` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,509.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.51K USD at 1.3358 USD [API] | `2026-10-22 08:02:50` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,255.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.26K USD at 1.3358 USD [API] | `2026-10-22 08:02:50` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 4,255.86 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.26K USD at 1.3358 USD [API] | `2026-10-22 08:02:50` |
| `ANNOUNCEMENT` | `INFO` | `1.34` | 3,975.34 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.98K USD at 1.3358 USD [API] | `2026-10-22 08:02:50` |
| `ANNOUNCEMENT` | `INFO` | `1.26` | 10,779.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.78K USD at 1.2611 USD [API] | `2026-10-18 19:39:16` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,842.88 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.84K USD at 1.2999 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 399.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 11.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,500.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.50K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 130.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.13K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 1,872.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.87K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 13.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.01K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 499.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.50K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 35.10 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.04K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 72.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.07K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 6,260.80 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.26K USD at 1.3000 USD [API] | `2026-10-16 17:13:59` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 1,471.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.47K USD at 1.3020 USD [API] | `2026-10-15 02:22:32` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,971.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.97K USD at 1.3026 USD [API] | `2026-10-15 02:22:32` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 379.06 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.38K USD at 1.3026 USD [API] | `2026-10-15 02:22:32` |
| `ANNOUNCEMENT` | `INFO` | `1.30` | 2,506.59 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.51K USD at 1.3028 USD [API] | `2026-10-15 02:22:32` |
| `ANNOUNCEMENT` | `INFO` | `1.33` | 16,681.79 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 16.68K USD at 1.3269 USD [API] | `2026-10-13 00:08:28` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 1,232.40 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.23K USD at 1.3663 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,292.78 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.29K USD at 1.3663 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 3,999.16 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3663 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 49.19 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3663 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 50.56 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.05K USD at 1.3664 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 4,939.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.94K USD at 1.3664 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 6,587.41 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.59K USD at 1.3664 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 5,005.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.01K USD at 1.3664 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 6,586.05 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 6.59K USD at 1.3664 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.37` | 2,902.23 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.90K USD at 1.3664 USD [API] | `2026-10-12 16:50:27` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 506.15 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.51K USD at 1.4178 USD [API] | `2026-10-07 17:27:02` |
| `ANNOUNCEMENT` | `INFO` | `1.42` | 3,842.24 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.84K USD at 1.4178 USD [API] | `2026-10-07 17:27:02` |
| `ANNOUNCEMENT` | `INFO` | `1.43` | 12,403.72 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 12.40K USD at 1.4323 USD [API] | `2026-10-07 02:01:21` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 15,911.25 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 15.91K USD at 1.4627 USD [API] | `2026-10-02 18:39:33` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 2,571.43 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 2.57K USD at 1.4627 USD [API] | `2026-10-02 18:39:33` |
| `ANNOUNCEMENT` | `INFO` | `1.46` | 10,642.61 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.64K USD at 1.4627 USD [API] | `2026-10-02 18:39:33` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 158.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.16K USD at 1.4800 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 198.32 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.20K USD at 1.4800 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 10,777.36 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 10.78K USD at 1.4800 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 595.00 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.60K USD at 1.4801 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 399.63 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.4801 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 5,001.26 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 5.00K USD at 1.4801 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.48` | 7,943.70 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.94K USD at 1.4801 USD [API] | `2026-09-28 05:23:56` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 39,758.27 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 39.76K USD at 1.4531 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 1,363.01 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.36K USD at 1.4531 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 284.81 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.28K USD at 1.4531 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 1,499.60 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.50K USD at 1.4531 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 85.73 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.09K USD at 1.4531 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 4,860.95 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.86K USD at 1.4532 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.45` | 4,698.20 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.70K USD at 1.4532 USD [API] | `2026-09-24 10:13:45` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 7,710.64 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 7.71K USD at 1.4946 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 272.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.27K USD at 1.4946 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 4,216.55 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.22K USD at 1.4947 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 11,231.93 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 11.23K USD at 1.4948 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 9,771.51 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 9.77K USD at 1.4948 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 1,459.02 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.46K USD at 1.4949 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 3,518.99 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.52K USD at 1.4949 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.49` | 4,217.11 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.22K USD at 1.4949 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 1,154.14 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.15K USD at 1.4950 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 400.66 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.4950 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.50` | 879.12 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.88K USD at 1.4951 USD [API] | `2026-09-23 16:01:24` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 1,294.09 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.29K USD at 1.3960 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 3,999.54 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3960 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 1,717.08 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 1.72K USD at 1.3960 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 418.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.42K USD at 1.3961 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 3,448.37 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 3.45K USD at 1.3961 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 400.68 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 0.40K USD at 1.3961 USD [API] | `2026-09-20 01:37:09` |
| `ANNOUNCEMENT` | `INFO` | `1.40` | 3,999.83 USD | `-` | `NEWS_INTEL` | `-` | #XRP Liquidated Long: 4.00K USD at 1.3961 USD [API] | `2026-09-20 01:37:09` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.30` (Vol: 2,600,000.00 USD, Dist: `+5.65%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--2.21%`)
  * 48H Horizon: Short MP=`1.32` (Vol: 2,300,000.00 USD, Dist: `+7.92%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--2.22%`)
  * 3D Horizon: Short MP=`1.35` (Vol: 2,700,000.00 USD, Dist: `+10.14%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--2.22%`)
  * 7D Horizon: Short MP=`1.35` (Vol: 3,000,000.00 USD, Dist: `+9.79%`) | Long MP=`1.20` (Vol: 921,200.00 USD, Dist: `--2.22%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.2550` | 760.66 USD | 61,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2650` | 358.81 USD | 61,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2750` | 161,250.00 USD | 61,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2850` | 577.70 USD | 61,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2950` | 3,550.00 USD | 61,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3050` | 6,890.00 USD | 61,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3150` | 7,320.00 USD | 61,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3350` | 434.83 USD | 61,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3450` | 1,120.00 USD | 61,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3550` | 6,980.00 USD | 61,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3650` | 2,430.00 USD | 61,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3950` | 1,490.00 USD | 61,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4050` | 8,900.00 USD | 61,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4250` | 24,660.00 USD | 61,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4350` | 8,340.00 USD | 61,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4450` | 1,870.00 USD | 61,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4550` | 3,290.00 USD | 61,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4650` | 39,940.00 USD | 61,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4750` | 581.88 USD | 61,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4850` | 635,960.00 USD | 61,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4950` | 629.64 USD | 60,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5050` | 206.04 USD | 60,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5150` | 14,700.00 USD | 60,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5250` | 184,010.00 USD | 60,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5350` | 7,930.00 USD | 60,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5450` | 3,300.00 USD | 60,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5650` | 793.26 USD | 60,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5750` | 8,590.00 USD | 60,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5850` | 11,920.00 USD | 60,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5950` | 174,470.00 USD | 60,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6050` | 16,680.00 USD | 60,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6150` | 29,870.00 USD | 60,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6250` | 11,060.00 USD | 60,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6350` | 19,810.00 USD | 60,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6450` | 19,570.00 USD | 60,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6550` | 1,260.00 USD | 60,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6650` | 19,390.00 USD | 60,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6750` | 30,010.00 USD | 60,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6850` | 4,220.00 USD | 60,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.6950` | 144,920.00 USD | 60,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7050` | 19,510.00 USD | 60,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7150` | 104,770.00 USD | 60,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7250` | 233,610.00 USD | 59,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7350` | 25,330.00 USD | 59,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7450` | 92,830.00 USD | 59,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7550` | 86,370.00 USD | 59,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7650` | 16,120.00 USD | 59,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7750` | 35,390.00 USD | 59,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7850` | 12,270.00 USD | 59,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.7950` | 12,350.00 USD | 59,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8050` | 31,990.00 USD | 59,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 59,810.00 USD | 59,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8250` | 527,170.00 USD | 59,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 40,140.00 USD | 58,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 128,270.00 USD | 58,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 51,910.00 USD | 58,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 3,090,000.00 USD | 58,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 93,340.00 USD | 55,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 344,420.00 USD | 55,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 321,600.00 USD | 55,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 120,130.00 USD | 54,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 95,680.00 USD | 54,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 108,950.00 USD | 54,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 93,770.00 USD | 54,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 137,230.00 USD | 54,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 81,710.00 USD | 54,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 33,890,000.00 USD | 54,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 255,680.00 USD | 20,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 468,920.00 USD | 19,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 73,970.00 USD | 19,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 442,510.00 USD | 19,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 325,740.00 USD | 18,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 2,700,000.00 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 2,130,000.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 177,970.00 USD | 13,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 1,620,000.00 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 720,150.00 USD | 11,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 492,670.00 USD | 11,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 749,110.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 396,730.00 USD | 10,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 94,380.00 USD | 9,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.11` | 31,160,000.00 USD | 31,160,000.00 USD | 17,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 52,480,000.00 USD | 52,480,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 31,140,000.00 USD | 31,140,000.00 USD | 18,710.00 USD | 0.00 USD | 121,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.11` | 31,000,000.00 USD | 31,000,000.00 USD | 0.00 USD | 2,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.11` | 52,460,000.00 USD | 52,460,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.11` | 308,050.00 USD | 9,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.12` | 31,000,000.00 USD | 31,000,000.00 USD | 0.00 USD | 0.00 USD | 62,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 52,450,000.00 USD | 52,450,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 30,940,000.00 USD | 30,940,000.00 USD | 0.00 USD | 47,340.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 30,880,000.00 USD | 30,880,000.00 USD | 10,140.00 USD | 2,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 52,370,000.00 USD | 52,370,000.00 USD | 17,190.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 30,870,000.00 USD | 30,870,000.00 USD | 0.00 USD | 1,530.00 USD | 57,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 52,350,000.00 USD | 52,350,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.12` | 30,810,000.00 USD | 30,810,000.00 USD | 66,330.00 USD | 29,190.00 USD | 56,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.12` | 52,350,000.00 USD | 52,350,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.12` | 2,130,000.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.13` | 30,660,000.00 USD | 30,660,000.00 USD | 0.00 USD | 783.15 USD | 104,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 30,550,000.00 USD | 30,550,000.00 USD | 0.00 USD | 42,490.00 USD | 78,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 52,140,000.00 USD | 52,140,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 30,430,000.00 USD | 30,430,000.00 USD | 0.00 USD | 66,770.00 USD | 166,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 51,950,000.00 USD | 51,950,000.00 USD | 5,450.00 USD | 3,410.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.13` | 30,200,000.00 USD | 30,200,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.13` | 51,930,000.00 USD | 51,930,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 30,140,000.00 USD | 30,140,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 51,460,000.00 USD | 51,460,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.14` | 454,740.00 USD | 7,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.14` | 30,090,000.00 USD | 30,090,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 51,210,000.00 USD | 51,210,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 30,000,000.00 USD | 30,000,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 51,110,000.00 USD | 51,110,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 29,980,000.00 USD | 29,980,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 51,100,000.00 USD | 51,100,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.14` | 29,910,000.00 USD | 29,910,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.14` | 51,040,000.00 USD | 51,040,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 29,770,000.00 USD | 29,770,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 50,920,000.00 USD | 50,920,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.15` | 323,110.00 USD | 6,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `1.15` | 50,910,000.00 USD | 50,910,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 29,730,000.00 USD | 29,730,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 50,770,000.00 USD | 50,770,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 50,410,000.00 USD | 50,410,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.15` | 29,720,000.00 USD | 29,720,000.00 USD | 4,040.00 USD | 11,230.00 USD | 185,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.15` | 50,250,000.00 USD | 50,250,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 29,520,000.00 USD | 29,520,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 49,870,000.00 USD | 49,870,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.16` | 119,260.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.16` | 29,180,000.00 USD | 29,180,000.00 USD | 29,120.00 USD | 9,570.00 USD | 31,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 49,220,000.00 USD | 49,220,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 29,110,000.00 USD | 29,110,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 48,420,000.00 USD | 48,420,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 28,790,000.00 USD | 28,790,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 47,900,000.00 USD | 47,900,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.16` | 28,170,000.00 USD | 28,170,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.16` | 46,870,000.00 USD | 46,870,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 27,550,000.00 USD | 27,550,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 45,500,000.00 USD | 45,500,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,680,000.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.17` | 27,340,000.00 USD | 27,340,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 44,870,000.00 USD | 44,870,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 27,030,000.00 USD | 27,030,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 43,490,000.00 USD | 43,490,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 26,860,000.00 USD | 26,860,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 41,990,000.00 USD | 41,990,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.17` | 26,690,000.00 USD | 26,690,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.17` | 40,600,000.00 USD | 40,600,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 26,440,000.00 USD | 26,440,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 39,800,000.00 USD | 39,800,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.18` | 486,240.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.18` | 26,100,000.00 USD | 26,100,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 38,920,000.00 USD | 38,920,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 25,970,000.00 USD | 25,970,000.00 USD | 93,410.00 USD | 41,360.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 38,460,000.00 USD | 38,460,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 25,790,000.00 USD | 25,790,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 37,750,000.00 USD | 37,750,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.18` | 25,750,000.00 USD | 25,750,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.18` | 37,370,000.00 USD | 37,370,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 25,640,000.00 USD | 25,640,000.00 USD | 92,110.00 USD | 7,460.00 USD | 27,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 37,240,000.00 USD | 37,240,000.00 USD | 123,240.00 USD | 97,270.00 USD | 289,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.19` | 3,330,000.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.19` | 25,520,000.00 USD | 25,520,000.00 USD | 16,710.00 USD | 139,070.00 USD | 324,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 36,730,000.00 USD | 36,730,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 25,040,000.00 USD | 25,040,000.00 USD | 239,430.00 USD | 8,930.00 USD | 410,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 35,960,000.00 USD | 35,960,000.00 USD | 182,110.00 USD | 132,500.00 USD | 276,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 24,380,000.00 USD | 24,380,000.00 USD | 48,220.00 USD | 10,480.00 USD | 205,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 35,370,000.00 USD | 35,370,000.00 USD | 152,830.00 USD | 265,920.00 USD | 471,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.19` | 24,110,000.00 USD | 24,110,000.00 USD | 25,890.00 USD | 217,630.00 USD | 79,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.19` | 34,480,000.00 USD | 34,480,000.00 USD | 218,910.00 USD | 106,640.00 USD | 335,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 23,790,000.00 USD | 23,790,000.00 USD | 15,240.00 USD | 40,110.00 USD | 48,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 33,820,000.00 USD | 33,820,000.00 USD | 381,050.00 USD | 81,170.00 USD | 291,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.20` | 697,120.00 USD | 700,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.20` | 23,690,000.00 USD | 23,690,000.00 USD | 21,190.00 USD | 3,620.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 33,060,000.00 USD | 33,060,000.00 USD | 5,350.00 USD | 102,680.00 USD | 187,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 23,660,000.00 USD | 23,660,000.00 USD | 66,960.00 USD | 22,280.00 USD | 291,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 32,770,000.00 USD | 32,770,000.00 USD | 67,200.00 USD | 158,480.00 USD | 738,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 23,280,000.00 USD | 23,280,000.00 USD | 169,810.00 USD | 250,260.00 USD | 180,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 31,800,000.00 USD | 31,800,000.00 USD | 243,240.00 USD | 225,970.00 USD | 15,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.20` | 22,680,000.00 USD | 22,680,000.00 USD | 102,120.00 USD | 4,970.00 USD | 260,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.20` | 31,320,000.00 USD | 31,320,000.00 USD | 202,570.00 USD | 146,780.00 USD | 534,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 22,310,000.00 USD | 22,310,000.00 USD | 4,360.00 USD | 297,650.00 USD | 195,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 30,440,000.00 USD | 30,440,000.00 USD | 0.00 USD | 17,680.00 USD | 79,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `1.21` | 3,260.00 USD | 3,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.21` | 21,810,000.00 USD | 21,810,000.00 USD | 81,900.00 USD | 32,170.00 USD | 415,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 30,340,000.00 USD | 30,340,000.00 USD | 80,450.00 USD | 7,260.00 USD | 9,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 21,280,000.00 USD | 21,280,000.00 USD | 220,830.00 USD | 67,350.00 USD | 14,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 30,240,000.00 USD | 30,240,000.00 USD | 659,990.00 USD | 518,690.00 USD | 368,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 20,980,000.00 USD | 20,980,000.00 USD | 99,310.00 USD | 425,250.00 USD | 731,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 28,690,000.00 USD | 28,690,000.00 USD | 180,260.00 USD | 264,440.00 USD | 802,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.21` | 19,720,000.00 USD | 19,720,000.00 USD | 419,060.00 USD | 162,630.00 USD | 699,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.21` | 27,450,000.00 USD | 27,450,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 18,440,000.00 USD | 18,440,000.00 USD | 166,960.00 USD | 8,790.00 USD | 102,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 27,040,000.00 USD | 27,040,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 18,160,000.00 USD | 18,160,000.00 USD | 118,950.00 USD | 5,680.00 USD | 470,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 26,870,000.00 USD | 26,870,000.00 USD | 157,620.00 USD | 396,140.00 USD | 396,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 17,570,000.00 USD | 17,570,000.00 USD | 285,170.00 USD | 423,840.00 USD | 178,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 25,920,000.00 USD | 25,920,000.00 USD | 256,390.00 USD | 8,330.00 USD | 40,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 16,680,000.00 USD | 16,680,000.00 USD | 54,610.00 USD | 42,060.00 USD | 228,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 25,610,000.00 USD | 25,610,000.00 USD | 245,120.00 USD | 10,480.00 USD | 328,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.22` | 16,360,000.00 USD | 16,360,000.00 USD | 141,030.00 USD | 525,900.00 USD | 394,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.22` | 25,030,000.00 USD | 25,030,000.00 USD | 0.00 USD | 205,130.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 15,290,000.00 USD | 15,290,000.00 USD | 828,850.00 USD | 352,590.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 23,780,000.00 USD | 23,780,000.00 USD | 1,040,000.00 USD | 788,680.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 11,360,000.00 USD | 11,360,000.00 USD | 344,500.00 USD | 161,310.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 20,890,000.00 USD | 20,890,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 9,820,000.00 USD | 9,820,000.00 USD | 105,710.00 USD | 213,020.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 20,430,000.00 USD | 20,430,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 8,420,000.00 USD | 8,420,000.00 USD | 319,240.00 USD | 1,170,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 17,540,000.00 USD | 17,540,000.00 USD | 782,590.00 USD | 485,710.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.23` | 6,930,000.00 USD | 6,930,000.00 USD | 281,800.00 USD | 336,650.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.23` | 16,260,000.00 USD | 16,260,000.00 USD | 1,040,000.00 USD | 597,200.00 USD | 112,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 5,290,000.00 USD | 5,290,000.00 USD | 433,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 14,510,000.00 USD | 14,510,000.00 USD | 996,240.00 USD | 998,790.00 USD | 66,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.24` | 52,360.00 USD | 52,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `1.24` | 4,850,000.00 USD | 4,850,000.00 USD | 267,830.00 USD | 542,950.00 USD | 739,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 12,450,000.00 USD | 12,450,000.00 USD | 1,640,000.00 USD | 1,500,000.00 USD | 2,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 3,300,000.00 USD | 3,300,000.00 USD | 663,280.00 USD | 998,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 6,500,000.00 USD | 6,500,000.00 USD | 2,610,000.00 USD | 799,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 3,100,000.00 USD | 3,100,000.00 USD | 1,820,000.00 USD | 374,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `1.24` | 1,640,000.00 USD | 1,640,000.00 USD | 305,740.00 USD | 774,420.00 USD | 560,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `1.24` | 896,470.00 USD | 896,470.00 USD | 896,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 3,330,000.00 USD | 3,330,000.00 USD | 1,270,000.00 USD | 0.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 6,650,000.00 USD | 6,650,000.00 USD | 1,270,000.00 USD | 0.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 4,250,000.00 USD | 4,250,000.00 USD | 3,330,000.00 USD | 923,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 8,510,000.00 USD | 8,510,000.00 USD | 3,330,000.00 USD | 923,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.25` | 39,960.00 USD | 92,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.25` | 7,760,000.00 USD | 7,760,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 10,740,000.00 USD | 10,740,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 10,880,000.00 USD | 10,880,000.00 USD | 140,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 8,350,000.00 USD | 8,350,000.00 USD | 202,510.00 USD | 0.00 USD | 392,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 11,060,000.00 USD | 11,060,000.00 USD | 180,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 532,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 12,000,000.00 USD | 12,000,000.00 USD | 74,170.00 USD | 0.00 USD | 860,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.25` | 9,680,000.00 USD | 9,680,000.00 USD | 794,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.25` | 12,190,000.00 USD | 12,190,000.00 USD | 172,030.00 USD | 0.00 USD | 18,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.25` | 49,650.00 USD | 141,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.26` | 10,820,000.00 USD | 10,820,000.00 USD | 803,540.00 USD | 140,210.00 USD | 193,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 10,910,000.00 USD | 10,910,000.00 USD | 86,570.00 USD | 3,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 12,290,000.00 USD | 12,290,000.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 12,990,000.00 USD | 12,990,000.00 USD | 331,210.00 USD | 66,520.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 381,520.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 16,360,000.00 USD | 16,360,000.00 USD | 1,050,000.00 USD | 696,320.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 18,800,000.00 USD | 18,800,000.00 USD | 834,020.00 USD | 799,870.00 USD | 1,910,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.26` | 20,010,000.00 USD | 20,010,000.00 USD | 367,910.00 USD | 759,740.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.26` | 25,740,000.00 USD | 25,740,000.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.26` | 180,810.00 USD | 322,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.27` | 22,260,000.00 USD | 22,260,000.00 USD | 39,860.00 USD | 1,080,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 39,370,000.00 USD | 39,370,000.00 USD | 2,620,000.00 USD | 2,370,000.00 USD | 8,640,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 24,360,000.00 USD | 24,360,000.00 USD | 23,990.00 USD | 2,070,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 44,140,000.00 USD | 44,140,000.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 27,350,000.00 USD | 27,350,000.00 USD | 369,350.00 USD | 841,430.00 USD | 1,780,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 47,780,000.00 USD | 47,780,000.00 USD | 1,030,000.00 USD | 2,480,000.00 USD | 123,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 30,230,000.00 USD | 30,230,000.00 USD | 1,860,000.00 USD | 348,710.00 USD | 676,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 52,550,000.00 USD | 52,550,000.00 USD | 186,960.00 USD | 3,990,000.00 USD | 591,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.27` | 36,770,000.00 USD | 36,770,000.00 USD | 778,390.00 USD | 2,410,000.00 USD | 3,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.27` | 68,980,000.00 USD | 68,980,000.00 USD | 4,840,000.00 USD | 2,340,000.00 USD | 9,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.27` | 43,670.00 USD | 366,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.28` | 47,340,000.00 USD | 47,340,000.00 USD | 3,100,000.00 USD | 2,940,000.00 USD | 4,520,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 87,260,000.00 USD | 87,260,000.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 55,070,000.00 USD | 55,070,000.00 USD | 3,180,000.00 USD | 2,210,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 93,550,000.00 USD | 93,550,000.00 USD | 3,260,000.00 USD | 1,940,000.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 56,400,000.00 USD | 56,400,000.00 USD | 209,970.00 USD | 608,220.00 USD | 507,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 94,510,000.00 USD | 94,510,000.00 USD | 0.00 USD | 879,610.00 USD | 79,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 59,260,000.00 USD | 59,260,000.00 USD | 1,120,000.00 USD | 199,040.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 96,510,000.00 USD | 96,510,000.00 USD | 1,460,000.00 USD | 478,060.00 USD | 67,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.28` | 61,290,000.00 USD | 61,290,000.00 USD | 421,680.00 USD | 611,360.00 USD | 993,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.28` | 100,110,000.00 USD | 100,110,000.00 USD | 639,910.00 USD | 1,380,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.28` | 2,390.00 USD | 368,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.29` | 63,200,000.00 USD | 63,200,000.00 USD | 726,790.00 USD | 768,570.00 USD | 419,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 101,270,000.00 USD | 101,270,000.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 63,520,000.00 USD | 63,520,000.00 USD | 210,950.00 USD | 8,830.00 USD | 99,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 101,390,000.00 USD | 101,390,000.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 63,830,000.00 USD | 63,830,000.00 USD | 151,350.00 USD | 0.00 USD | 157,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 103,670,000.00 USD | 103,670,000.00 USD | 1,060,000.00 USD | 198,070.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 66,720,000.00 USD | 66,720,000.00 USD | 546,160.00 USD | 195,000.00 USD | 2,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 104,100,000.00 USD | 104,100,000.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.29` | 72,670,000.00 USD | 72,670,000.00 USD | 1,810,000.00 USD | 645,070.00 USD | 3,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.29` | 113,780,000.00 USD | 113,780,000.00 USD | 3,400,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.29` | 692.82 USD | 369,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.30` | 74,920,000.00 USD | 74,920,000.00 USD | 518,910.00 USD | 633,000.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 115,010,000.00 USD | 115,010,000.00 USD | 209,360.00 USD | 398,190.00 USD | 628,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 75,640,000.00 USD | 75,640,000.00 USD | 321,680.00 USD | 109,620.00 USD | 291,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 117,070,000.00 USD | 117,070,000.00 USD | 0.00 USD | 100,810.00 USD | 1,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 77,770,000.00 USD | 77,770,000.00 USD | 443,890.00 USD | 332,000.00 USD | 1,350,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 118,740,000.00 USD | 118,740,000.00 USD | 208,510.00 USD | 486,620.00 USD | 970,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 79,490,000.00 USD | 79,490,000.00 USD | 587,440.00 USD | 869,380.00 USD | 260,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 121,830,000.00 USD | 121,830,000.00 USD | 0.00 USD | 2,610,000.00 USD | 485,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.30` | 80,760,000.00 USD | 80,760,000.00 USD | 304,340.00 USD | 649,450.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.30` | 121,830,000.00 USD | 121,830,000.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.30` | 19,210.00 USD | 388,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.31` | 83,050,000.00 USD | 83,050,000.00 USD | 689,960.00 USD | 147,250.00 USD | 1,450,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 124,840,000.00 USD | 124,840,000.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 86,290,000.00 USD | 86,290,000.00 USD | 1,130,000.00 USD | 330,750.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 129,300,000.00 USD | 129,300,000.00 USD | 1,670,000.00 USD | 1,060,000.00 USD | 1,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 88,610,000.00 USD | 88,610,000.00 USD | 876,130.00 USD | 869,070.00 USD | 573,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 132,560,000.00 USD | 132,560,000.00 USD | 839,350.00 USD | 430,210.00 USD | 1,990,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 91,540,000.00 USD | 91,540,000.00 USD | 1,320,000.00 USD | 664,910.00 USD | 944,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 135,400,000.00 USD | 135,400,000.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.31` | 94,470,000.00 USD | 94,470,000.00 USD | 372,630.00 USD | 454,810.00 USD | 2,110,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.31` | 137,860,000.00 USD | 137,860,000.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 100,980,000.00 USD | 100,980,000.00 USD | 1,320,000.00 USD | 1,640,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 142,480,000.00 USD | 142,480,000.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 106,060,000.00 USD | 106,060,000.00 USD | 1,740,000.00 USD | 836,160.00 USD | 2,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 145,560,000.00 USD | 145,560,000.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 109,560,000.00 USD | 109,560,000.00 USD | 1,650,000.00 USD | 652,780.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 147,390,000.00 USD | 147,390,000.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 114,150,000.00 USD | 114,150,000.00 USD | 1,990,000.00 USD | 583,250.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 151,850,000.00 USD | 151,850,000.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.32` | 116,150,000.00 USD | 116,150,000.00 USD | 1,080,000.00 USD | 287,760.00 USD | 625,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.32` | 154,220,000.00 USD | 154,220,000.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.32` | 59,090.00 USD | 447,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.33` | 118,680,000.00 USD | 118,680,000.00 USD | 664,210.00 USD | 621,550.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 154,760,000.00 USD | 154,760,000.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 120,920,000.00 USD | 120,920,000.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 155,910,000.00 USD | 155,910,000.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 123,770,000.00 USD | 123,770,000.00 USD | 848,670.00 USD | 298,810.00 USD | 1,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 157,630,000.00 USD | 157,630,000.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 126,160,000.00 USD | 126,160,000.00 USD | 1,040,000.00 USD | 190,550.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 161,680,000.00 USD | 161,680,000.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.33` | 128,240,000.00 USD | 128,240,000.00 USD | 859,040.00 USD | 354,550.00 USD | 872,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.33` | 162,230,000.00 USD | 162,230,000.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.33` | 1,730.00 USD | 449,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.34` | 130,220,000.00 USD | 130,220,000.00 USD | 829,900.00 USD | 219,260.00 USD | 927,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 164,180,000.00 USD | 164,180,000.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 132,490,000.00 USD | 132,490,000.00 USD | 1,010,000.00 USD | 331,250.00 USD | 927,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 166,520,000.00 USD | 166,520,000.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 134,360,000.00 USD | 134,360,000.00 USD | 892,570.00 USD | 387,310.00 USD | 592,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 171,230,000.00 USD | 171,230,000.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 137,610,000.00 USD | 137,610,000.00 USD | 1,410,000.00 USD | 693,530.00 USD | 1,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 176,870,000.00 USD | 176,870,000.00 USD | 1,700,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.34` | 139,380,000.00 USD | 139,380,000.00 USD | 584,400.00 USD | 416,300.00 USD | 762,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.34` | 187,840,000.00 USD | 187,840,000.00 USD | 3,600,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.34` | 4,330.00 USD | 453,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.35` | 140,420,000.00 USD | 140,420,000.00 USD | 355,660.00 USD | 234,160.00 USD | 458,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 194,780,000.00 USD | 194,780,000.00 USD | 2,310,000.00 USD | 2,170,000.00 USD | 2,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 141,910,000.00 USD | 141,910,000.00 USD | 749,450.00 USD | 149,380.00 USD | 591,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 205,030,000.00 USD | 205,030,000.00 USD | 4,290,000.00 USD | 1,640,000.00 USD | 4,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 142,940,000.00 USD | 142,940,000.00 USD | 471,590.00 USD | 126,450.00 USD | 425,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 212,740,000.00 USD | 212,740,000.00 USD | 2,580,000.00 USD | 1,380,000.00 USD | 3,750,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 144,360,000.00 USD | 144,360,000.00 USD | 597,310.00 USD | 312,930.00 USD | 511,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 221,000,000.00 USD | 221,000,000.00 USD | 2,620,000.00 USD | 1,160,000.00 USD | 4,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.35` | 145,150,000.00 USD | 145,150,000.00 USD | 142,180.00 USD | 79,810.00 USD | 571,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.35` | 229,230,000.00 USD | 229,230,000.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.35` | 2,700.00 USD | 456,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.36` | 146,090,000.00 USD | 146,090,000.00 USD | 391,410.00 USD | 17,220.00 USD | 531,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 233,320,000.00 USD | 233,320,000.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 146,430,000.00 USD | 146,430,000.00 USD | 213,710.00 USD | 42,480.00 USD | 84,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 237,110,000.00 USD | 237,110,000.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 147,180,000.00 USD | 147,180,000.00 USD | 277,960.00 USD | 149,990.00 USD | 316,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 239,240,000.00 USD | 239,240,000.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 147,520,000.00 USD | 147,520,000.00 USD | 171,250.00 USD | 2,700.00 USD | 166,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 243,340,000.00 USD | 243,340,000.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.36` | 147,630,000.00 USD | 147,630,000.00 USD | 0.00 USD | 26,460.00 USD | 88,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.36` | 245,060,000.00 USD | 245,060,000.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.36` | 193,360.00 USD | 649,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.37` | 147,960,000.00 USD | 147,960,000.00 USD | 53,740.00 USD | 104,420.00 USD | 171,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 245,550,000.00 USD | 245,550,000.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 148,160,000.00 USD | 148,160,000.00 USD | 126,110.00 USD | 2,890.00 USD | 68,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 246,960,000.00 USD | 246,960,000.00 USD | 528,490.00 USD | 135,750.00 USD | 753,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 148,360,000.00 USD | 148,360,000.00 USD | 7,080.00 USD | 67,780.00 USD | 119,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 248,150,000.00 USD | 248,150,000.00 USD | 351,750.00 USD | 372,470.00 USD | 461,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.37` | 148,560,000.00 USD | 148,560,000.00 USD | 75,340.00 USD | 1,780.00 USD | 126,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.37` | 250,620,000.00 USD | 250,620,000.00 USD | 821,620.00 USD | 376,730.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 148,840,000.00 USD | 148,840,000.00 USD | 120,880.00 USD | 30,080.00 USD | 125,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 252,420,000.00 USD | 252,420,000.00 USD | 536,130.00 USD | 295,850.00 USD | 966,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.38` | 14,100.00 USD | 664,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.38` | 149,230,000.00 USD | 149,230,000.00 USD | 93,260.00 USD | 50,590.00 USD | 254,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 253,910,000.00 USD | 253,910,000.00 USD | 617,230.00 USD | 329,740.00 USD | 552,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 149,710,000.00 USD | 149,710,000.00 USD | 195,140.00 USD | 100,700.00 USD | 182,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 256,010,000.00 USD | 256,010,000.00 USD | 579,450.00 USD | 256,720.00 USD | 1,260,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 149,790,000.00 USD | 149,790,000.00 USD | 12,100.00 USD | 65,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 258,560,000.00 USD | 258,560,000.00 USD | 1,210,000.00 USD | 331,990.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.38` | 149,960,000.00 USD | 149,960,000.00 USD | 0.00 USD | 1,250.00 USD | 166,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.38` | 259,650,000.00 USD | 259,650,000.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 150,010,000.00 USD | 150,010,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 260,930,000.00 USD | 260,930,000.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.39` | 63,450.00 USD | 727,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `1.39` | 150,070,000.00 USD | 150,070,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 261,480,000.00 USD | 261,480,000.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 150,160,000.00 USD | 150,160,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 262,580,000.00 USD | 262,580,000.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 262,740,000.00 USD | 262,740,000.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `1.39` | 150,180,000.00 USD | 150,180,000.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.39` | 263,070,000.00 USD | 263,070,000.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 263,240,000.00 USD | 263,240,000.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.40` | 2,090.00 USD | 729,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.40` | 263,360,000.00 USD | 263,360,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 263,370,000.00 USD | 263,370,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 263,500,000.00 USD | 263,500,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.40` | 263,620,000.00 USD | 263,620,000.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 263,860,000.00 USD | 263,860,000.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.41` | 635.06 USD | 730,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.41` | 264,030,000.00 USD | 264,030,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 264,410,000.00 USD | 264,410,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 265,050,000.00 USD | 265,050,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.41` | 265,230,000.00 USD | 265,230,000.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 265,850,000.00 USD | 265,850,000.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.42` | 3,930.00 USD | 734,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.42` | 266,380,000.00 USD | 266,380,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 267,400,000.00 USD | 267,400,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 268,780,000.00 USD | 268,780,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.42` | 269,400,000.00 USD | 269,400,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 269,760,000.00 USD | 269,760,000.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.43` | 93,280.00 USD | 827,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.43` | 270,780,000.00 USD | 270,780,000.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 272,290,000.00 USD | 272,290,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 273,680,000.00 USD | 273,680,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.43` | 274,480,000.00 USD | 274,480,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 275,010,000.00 USD | 275,010,000.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.44` | 258.30 USD | 827,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.44` | 275,360,000.00 USD | 275,360,000.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 275,810,000.00 USD | 275,810,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 276,530,000.00 USD | 276,530,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.44` | 276,900,000.00 USD | 276,900,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 277,030,000.00 USD | 277,030,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.45` | 284.66 USD | 827,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `1.45` | 277,160,000.00 USD | 277,160,000.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 277,490,000.00 USD | 277,490,000.00 USD | 62,180.00 USD | 96,050.00 USD | 173,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 278,100,000.00 USD | 278,100,000.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.45` | 278,660,000.00 USD | 278,660,000.00 USD | 182,110.00 USD | 128,180.00 USD | 249,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 279,120,000.00 USD | 279,120,000.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 279,280,000.00 USD | 279,280,000.00 USD | 85,350.00 USD | 50,790.00 USD | 20,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 279,750,000.00 USD | 279,750,000.00 USD | 119,110.00 USD | 55,850.00 USD | 296,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `1.46` | 279,960,000.00 USD | 279,960,000.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `1.47` | 128,690.00 USD | 956,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.49` | 576,690.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,150.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.50` | 12,310.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.51` | 11,570.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.53` | 988.54 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.54` | 2,590.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.55` | 1,360.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.56` | 679.21 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.57` | 2,900.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.58` | 123.63 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.59` | 1,180.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.60` | 2,650.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.61` | 4,320,000.00 USD | 5,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.62` | 271.38 USD | 5,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.64` | 136,310.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.65` | 2,350.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.66` | 147.30 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.67` | 586.08 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.68` | 177.55 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.69` | 4,060.00 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.70` | 974.62 USD | 6,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.71` | 1,980.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.73` | 1,110.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.74` | 2,970.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 2,870.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.75` | 591.43 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.76` | 1,110.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.78` | 299,390.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.79` | 99,360.00 USD | 6,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.80` | 4,500.00 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.81` | 21,420.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.82` | 5,420,000.00 USD | 11,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.83` | 266.07 USD | 11,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.84` | 21,500.00 USD | 11,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.85` | 1,340.00 USD | 11,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.86` | 6,370.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.89` | 2,900,000.00 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.90` | 7,980.00 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.91` | 373.38 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.92` | 309,150.00 USD | 15,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.93` | 257,200.00 USD | 15,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.94` | 2,960,000.00 USD | 18,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.96` | 1,910.00 USD | 18,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.97` | 254,610.00 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.98` | 1,470.00 USD | 18,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.00` | 40,100.00 USD | 18,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.02` | 513.83 USD | 18,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.04` | 914.12 USD | 18,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.06` | 460.50 USD | 18,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 331.01 USD | 18,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.10` | 294.70 USD | 18,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 427,880.00 USD | 19,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.12` | 1,250.00 USD | 19,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.13` | 177.20 USD | 19,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 251,750.00 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.15` | 196.11 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.17` | 2,730.00 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.19` | 201.94 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 78,560.00 USD | 19,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.21` | 203.78 USD | 19,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 1,090.00 USD | 19,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.23` | 2,570.00 USD | 19,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.25` | 11,280.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.27` | 2,390.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.29` | 52,230.00 USD | 19,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.31` | 212.06 USD | 19,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.33` | 1,140.00 USD | 19,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.35` | 1,670.00 USD | 19,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.37` | 99,360.00 USD | 19,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 111.62 USD | 19,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.38` | 20,830.00 USD | 19,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 129,620.00 USD | 19,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.42` | 199,360.00 USD | 19,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `2.44` | 2,650.00 USD | 19,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.2550` | 61,660,000.00 USD | 0.00 USD | 760.66 USD | `-79.10%` | `2,983.00` |
| `Live` | `Long` | `0.2650` | 61,660,000.00 USD | 0.00 USD | 358.81 USD | `-78.28%` | `1,354.00` |
| `Live` | `Long` | `0.2750` | 61,660,000.00 USD | 0.00 USD | 161,250.00 USD | `-77.46%` | `586,361.00` |
| `Live` | `Long` | `0.2850` | 61,500,000.00 USD | 0.00 USD | 577.70 USD | `-76.64%` | `2,027.00` |
| `Live` | `Long` | `0.2950` | 61,490,000.00 USD | 0.00 USD | 3,550.00 USD | `-75.82%` | `12,021.00` |
| `Live` | `Long` | `0.3050` | 61,490,000.00 USD | 0.00 USD | 6,890.00 USD | `-75.00%` | `22,593.00` |
| `Live` | `Long` | `0.3150` | 61,480,000.00 USD | 0.00 USD | 7,320.00 USD | `-74.18%` | `23,226.00` |
| `Live` | `Long` | `0.3350` | 61,480,000.00 USD | 0.00 USD | 434.83 USD | `-72.54%` | `1,298.00` |
| `Live` | `Long` | `0.3450` | 61,480,000.00 USD | 0.00 USD | 1,120.00 USD | `-71.72%` | `3,236.00` |
| `Live` | `Long` | `0.3550` | 61,480,000.00 USD | 0.00 USD | 6,980.00 USD | `-70.90%` | `19,653.00` |
| `Live` | `Long` | `0.3650` | 61,470,000.00 USD | 0.00 USD | 2,430.00 USD | `-70.08%` | `6,662.00` |
| `Live` | `Long` | `0.3950` | 61,470,000.00 USD | 0.00 USD | 1,490.00 USD | `-67.62%` | `3,777.00` |
| `Live` | `Long` | `0.4050` | 61,460,000.00 USD | 0.00 USD | 8,900.00 USD | `-66.80%` | `21,978.00` |
| `Live` | `Long` | `0.4250` | 61,460,000.00 USD | 0.00 USD | 24,660.00 USD | `-65.16%` | `58,022.00` |
| `Live` | `Long` | `0.4350` | 61,430,000.00 USD | 0.00 USD | 8,340.00 USD | `-64.34%` | `19,179.00` |
| `Live` | `Long` | `0.4450` | 61,420,000.00 USD | 0.00 USD | 1,870.00 USD | `-63.52%` | `4,205.00` |
| `Live` | `Long` | `0.4550` | 61,420,000.00 USD | 0.00 USD | 3,290.00 USD | `-62.70%` | `7,229.00` |
| `Live` | `Long` | `0.4650` | 61,420,000.00 USD | 0.00 USD | 39,940.00 USD | `-61.88%` | `85,892.00` |
| `Live` | `Long` | `0.4750` | 61,380,000.00 USD | 0.00 USD | 581.88 USD | `-61.06%` | `1,225.00` |
| `Live` | `Long` | `0.4850` | 61,380,000.00 USD | 0.00 USD | 635,960.00 USD | `-60.24%` | `1,311,263.00` |
| `Live` | `Long` | `0.4950` | 60,740,000.00 USD | 0.00 USD | 629.64 USD | `-59.42%` | `1,272.00` |
| `Live` | `Long` | `0.5050` | 60,740,000.00 USD | 0.00 USD | 206.04 USD | `-58.60%` | `408.00` |
| `Live` | `Long` | `0.5150` | 60,740,000.00 USD | 0.00 USD | 14,700.00 USD | `-57.78%` | `28,541.00` |
| `Live` | `Long` | `0.5250` | 60,730,000.00 USD | 0.00 USD | 184,010.00 USD | `-56.96%` | `350,500.00` |
| `Live` | `Long` | `0.5350` | 60,540,000.00 USD | 0.00 USD | 7,930.00 USD | `-56.14%` | `14,830.00` |
| `Live` | `Long` | `0.5450` | 60,530,000.00 USD | 0.00 USD | 3,300.00 USD | `-55.32%` | `6,063.00` |
| `Live` | `Long` | `0.5650` | 60,530,000.00 USD | 0.00 USD | 793.26 USD | `-53.68%` | `1,404.00` |
| `Live` | `Long` | `0.5750` | 60,530,000.00 USD | 0.00 USD | 8,590.00 USD | `-52.86%` | `14,935.00` |
| `Live` | `Long` | `0.5850` | 60,520,000.00 USD | 0.00 USD | 11,920.00 USD | `-52.05%` | `20,374.00` |
| `Live` | `Long` | `0.5950` | 60,510,000.00 USD | 0.00 USD | 174,470.00 USD | `-51.23%` | `293,228.00` |
| `Live` | `Long` | `0.6050` | 60,330,000.00 USD | 0.00 USD | 16,680.00 USD | `-50.41%` | `27,571.00` |
| `Live` | `Long` | `0.6150` | 60,320,000.00 USD | 0.00 USD | 29,870.00 USD | `-49.59%` | `48,564.00` |
| `Live` | `Long` | `0.6250` | 60,290,000.00 USD | 0.00 USD | 11,060.00 USD | `-48.77%` | `17,694.00` |
| `Live` | `Long` | `0.6350` | 60,280,000.00 USD | 0.00 USD | 19,810.00 USD | `-47.95%` | `31,200.00` |
| `Live` | `Long` | `0.6450` | 60,260,000.00 USD | 0.00 USD | 19,570.00 USD | `-47.13%` | `30,341.00` |
| `Live` | `Long` | `0.6550` | 60,240,000.00 USD | 0.00 USD | 1,260.00 USD | `-46.31%` | `1,927.00` |
| `Live` | `Long` | `0.6650` | 60,240,000.00 USD | 0.00 USD | 19,390.00 USD | `-45.49%` | `29,159.00` |
| `Live` | `Long` | `0.6750` | 60,220,000.00 USD | 0.00 USD | 30,010.00 USD | `-44.67%` | `44,455.00` |
| `Live` | `Long` | `0.6850` | 60,190,000.00 USD | 0.00 USD | 4,220.00 USD | `-43.85%` | `6,166.00` |
| `Live` | `Long` | `0.6950` | 60,180,000.00 USD | 0.00 USD | 144,920.00 USD | `-43.03%` | `208,513.00` |
| `Live` | `Long` | `0.7050` | 60,040,000.00 USD | 0.00 USD | 19,510.00 USD | `-42.21%` | `27,677.00` |
| `Live` | `Long` | `0.7150` | 60,020,000.00 USD | 0.00 USD | 104,770.00 USD | `-41.39%` | `146,530.00` |
| `Live` | `Long` | `0.7250` | 59,910,000.00 USD | 0.00 USD | 233,610.00 USD | `-40.57%` | `322,224.00` |
| `Live` | `Long` | `0.7350` | 59,680,000.00 USD | 0.00 USD | 25,330.00 USD | `-39.75%` | `34,458.00` |
| `Live` | `Long` | `0.7450` | 59,650,000.00 USD | 0.00 USD | 92,830.00 USD | `-38.93%` | `124,601.00` |
| `Live` | `Long` | `0.7550` | 59,560,000.00 USD | 0.00 USD | 86,370.00 USD | `-38.11%` | `114,392.00` |
| `Live` | `Long` | `0.7650` | 59,480,000.00 USD | 0.00 USD | 16,120.00 USD | `-37.29%` | `21,074.00` |
| `Live` | `Long` | `0.7750` | 59,460,000.00 USD | 0.00 USD | 35,390.00 USD | `-36.47%` | `45,666.00` |
| `Live` | `Long` | `0.7850` | 59,420,000.00 USD | 0.00 USD | 12,270.00 USD | `-35.65%` | `15,635.00` |
| `Live` | `Long` | `0.7950` | 59,410,000.00 USD | 0.00 USD | 12,350.00 USD | `-34.83%` | `15,539.00` |
| `Live` | `Long` | `0.8050` | 59,400,000.00 USD | 0.00 USD | 31,990.00 USD | `-34.01%` | `39,735.00` |
| `Live` | `Long` | `0.8150` | 59,370,000.00 USD | 0.00 USD | 59,810.00 USD | `-33.19%` | `73,382.00` |
| `Live` | `Long` | `0.8250` | 59,310,000.00 USD | 0.00 USD | 527,170.00 USD | `-32.37%` | `638,989.00` |
| `Live` | `Long` | `0.8350` | 58,780,000.00 USD | 0.00 USD | 40,140.00 USD | `-31.55%` | `48,067.00` |
| `Live` | `Long` | `0.8450` | 58,740,000.00 USD | 0.00 USD | 128,270.00 USD | `-30.73%` | `151,797.00` |
| `Live` | `Long` | `0.8550` | 58,610,000.00 USD | 0.00 USD | 51,910.00 USD | `-29.91%` | `60,708.00` |
| `Live` | `Long` | `0.8650` | 58,560,000.00 USD | 0.00 USD | 3,090,000.00 USD | `-29.09%` | `3,575,824.00` |
| `Live` | `Long` | `0.8750` | 55,470,000.00 USD | 0.00 USD | 93,340.00 USD | `-28.27%` | `106,673.00` |
| `Live` | `Long` | `0.8850` | 55,370,000.00 USD | 0.00 USD | 344,420.00 USD | `-27.45%` | `389,175.00` |
| `Live` | `Long` | `0.8950` | 55,030,000.00 USD | 0.00 USD | 321,600.00 USD | `-26.63%` | `359,334.00` |
| `Live` | `Long` | `0.9050` | 54,710,000.00 USD | 0.00 USD | 120,130.00 USD | `-25.81%` | `132,739.00` |
| `Live` | `Long` | `0.9150` | 54,590,000.00 USD | 0.00 USD | 95,680.00 USD | `-24.99%` | `104,567.00` |
| `Live` | `Long` | `0.9250` | 54,490,000.00 USD | 0.00 USD | 108,950.00 USD | `-24.17%` | `117,781.00` |
| `Live` | `Long` | `0.9350` | 54,380,000.00 USD | 0.00 USD | 93,770.00 USD | `-23.35%` | `100,285.00` |
| `Live` | `Long` | `0.9450` | 54,290,000.00 USD | 0.00 USD | 137,230.00 USD | `-22.53%` | `145,222.00` |
| `Live` | `Long` | `0.9550` | 54,150,000.00 USD | 0.00 USD | 81,710.00 USD | `-21.71%` | `85,561.00` |
| `Live` | `Long` | `0.9650` | 54,070,000.00 USD | 0.00 USD | 33,890,000.00 USD | `-20.90%` | `35,116,086.00` |
| `Live` | `Long` | `0.9750` | 20,180,000.00 USD | 0.00 USD | 255,680.00 USD | `-20.08%` | `262,241.00` |
| `Live` | `Long` | `0.9850` | 19,930,000.00 USD | 0.00 USD | 468,920.00 USD | `-19.26%` | `476,059.00` |
| `Live` | `Long` | `0.9950` | 19,460,000.00 USD | 0.00 USD | 73,970.00 USD | `-18.44%` | `74,345.00` |
| `Live` | `Long` | `1.00` | 19,380,000.00 USD | 0.00 USD | 442,510.00 USD | `-17.62%` | `440,310.00` |
| `Live` | `Long` | `1.01` | 18,940,000.00 USD | 0.00 USD | 325,740.00 USD | `-16.80%` | `320,925.00` |
| `Live` | `Long` | `1.02` | 18,620,000.00 USD | 0.00 USD | 2,700,000.00 USD | `-15.98%` | `2,635,603.00` |
| `Live` | `Long` | `1.03` | 15,910,000.00 USD | 0.00 USD | 2,130,000.00 USD | `-15.16%` | `2,053,899.00` |
| `Live` | `Long` | `1.04` | 13,790,000.00 USD | 0.00 USD | 177,970.00 USD | `-14.34%` | `170,306.00` |
| `Live` | `Long` | `1.05` | 13,610,000.00 USD | 0.00 USD | 1,620,000.00 USD | `-13.52%` | `1,533,108.00` |
| `Live` | `Long` | `1.06` | 11,990,000.00 USD | 0.00 USD | 720,150.00 USD | `-12.70%` | `676,195.00` |
| `Live` | `Long` | `1.07` | 11,270,000.00 USD | 0.00 USD | 492,670.00 USD | `-11.88%` | `458,301.00` |
| `Live` | `Long` | `1.08` | 10,780,000.00 USD | 0.00 USD | 749,110.00 USD | `-11.06%` | `690,420.00` |
| `Live` | `Long` | `1.09` | 10,030,000.00 USD | 0.00 USD | 396,730.00 USD | `-10.24%` | `362,308.00` |
| `Live` | `Long` | `1.10` | 9,630,000.00 USD | 0.00 USD | 94,380.00 USD | `-9.42%` | `85,414.00` |
| `Live` | `Long` | `1.11` | 9,540,000.00 USD | 0.00 USD | 308,050.00 USD | `-8.60%` | `276,275.00` |
| `Live` | `Long` | `1.12` | 9,230,000.00 USD | 0.00 USD | 2,130,000.00 USD | `-7.78%` | `1,897,458.00` |
| `Live` | `Long` | `1.14` | 7,100,000.00 USD | 0.00 USD | 454,740.00 USD | `-6.96%` | `400,652.00` |
| `Live` | `Long` | `1.15` | 6,640,000.00 USD | 0.00 USD | 323,110.00 USD | `-6.14%` | `282,189.00` |
| `Live` | `Long` | `1.16` | 6,320,000.00 USD | 0.00 USD | 119,260.00 USD | `-5.32%` | `103,256.00` |
| `Live` | `Long` | `1.17` | 6,200,000.00 USD | 0.00 USD | 1,680,000.00 USD | `-4.50%` | `1,445,225.00` |
| `Live` | `Long` | `1.18` | 4,520,000.00 USD | 0.00 USD | 486,240.00 USD | `-3.68%` | `413,819.00` |
| `Live` | `Long` | `1.19` | 4,030,000.00 USD | 0.00 USD | 3,330,000.00 USD | `-2.86%` | `2,810,477.00` |
| `Live` | `Long` | `1.20` | 700,380.00 USD | 0.00 USD | 697,120.00 USD | `-2.04%` | `583,368.00` |
| `Live` | `Long` | `1.21` | 3,260.00 USD | 0.00 USD | 3,260.00 USD | `-1.22%` | `2,703.00` |
| `Live` | `Short` | `1.24` | 52,360.00 USD | 52,360.00 USD | 0.00 USD | `+1.24%` | `42,394.00` |
| `Live` | `Short` | `1.25` | 92,320.00 USD | 39,960.00 USD | 0.00 USD | `+2.06%` | `32,099.00` |
| `Live` | `Short` | `1.25` | 141,970.00 USD | 49,650.00 USD | 0.00 USD | `+2.88%` | `39,564.00` |
| `Live` | `Short` | `1.26` | 322,780.00 USD | 180,810.00 USD | 0.00 USD | `+3.70%` | `142,933.00` |
| `Live` | `Short` | `1.27` | 366,450.00 USD | 43,670.00 USD | 0.00 USD | `+4.52%` | `34,249.00` |
| `Live` | `Short` | `1.28` | 368,840.00 USD | 2,390.00 USD | 0.00 USD | `+5.34%` | `1,862.00` |
| `Live` | `Short` | `1.29` | 369,540.00 USD | 692.82 USD | 0.00 USD | `+6.16%` | `535.00` |
| `Live` | `Short` | `1.30` | 388,750.00 USD | 19,210.00 USD | 0.00 USD | `+6.98%` | `14,721.00` |
| `Live` | `Short` | `1.32` | 447,840.00 USD | 59,090.00 USD | 0.00 USD | `+8.62%` | `44,597.00` |
| `Live` | `Short` | `1.33` | 449,570.00 USD | 1,730.00 USD | 0.00 USD | `+9.44%` | `1,298.00` |
| `Live` | `Short` | `1.34` | 453,900.00 USD | 4,330.00 USD | 0.00 USD | `+10.25%` | `3,220.00` |
| `Live` | `Short` | `1.35` | 456,600.00 USD | 2,700.00 USD | 0.00 USD | `+11.07%` | `1,989.00` |
| `Live` | `Short` | `1.36` | 649,960.00 USD | 193,360.00 USD | 0.00 USD | `+11.89%` | `141,656.00` |
| `Live` | `Short` | `1.38` | 664,060.00 USD | 14,100.00 USD | 0.00 USD | `+12.71%` | `10,258.00` |
| `Live` | `Short` | `1.39` | 727,510.00 USD | 63,450.00 USD | 0.00 USD | `+13.53%` | `45,809.00` |
| `Live` | `Short` | `1.40` | 729,600.00 USD | 2,090.00 USD | 0.00 USD | `+14.35%` | `1,500.00` |
| `Live` | `Short` | `1.41` | 730,230.00 USD | 635.06 USD | 0.00 USD | `+15.17%` | `452.00` |
| `Live` | `Short` | `1.42` | 734,160.00 USD | 3,930.00 USD | 0.00 USD | `+15.99%` | `2,776.00` |
| `Live` | `Short` | `1.43` | 827,440.00 USD | 93,280.00 USD | 0.00 USD | `+16.81%` | `65,460.00` |
| `Live` | `Short` | `1.44` | 827,700.00 USD | 258.30 USD | 0.00 USD | `+17.63%` | `180.00` |
| `Live` | `Short` | `1.45` | 827,990.00 USD | 284.66 USD | 0.00 USD | `+18.45%` | `197.00` |
| `Live` | `Short` | `1.47` | 956,670.00 USD | 128,690.00 USD | 0.00 USD | `+20.09%` | `87,842.00` |
| `Live` | `Short` | `1.49` | 1,530,000.00 USD | 576,690.00 USD | 0.00 USD | `+21.73%` | `388,344.00` |
| `Live` | `Short` | `1.50` | 1,550,000.00 USD | 12,150.00 USD | 0.00 USD | `+22.55%` | `8,126.00` |
| `Live` | `Short` | `1.50` | 1,560,000.00 USD | 12,310.00 USD | 0.00 USD | `+23.37%` | `8,180.00` |
| `Live` | `Short` | `1.51` | 1,570,000.00 USD | 11,570.00 USD | 0.00 USD | `+24.19%` | `7,640.00` |
| `Live` | `Short` | `1.53` | 1,570,000.00 USD | 988.54 USD | 0.00 USD | `+25.83%` | `644.00` |
| `Live` | `Short` | `1.54` | 1,570,000.00 USD | 2,590.00 USD | 0.00 USD | `+26.65%` | `1,678.00` |
| `Live` | `Short` | `1.55` | 1,570,000.00 USD | 1,360.00 USD | 0.00 USD | `+27.47%` | `873.00` |
| `Live` | `Short` | `1.56` | 1,580,000.00 USD | 679.21 USD | 0.00 USD | `+28.29%` | `434.00` |
| `Live` | `Short` | `1.57` | 1,580,000.00 USD | 2,900.00 USD | 0.00 USD | `+29.11%` | `1,843.00` |
| `Live` | `Short` | `1.58` | 1,580,000.00 USD | 123.63 USD | 0.00 USD | `+29.93%` | `78.00` |
| `Live` | `Short` | `1.59` | 1,580,000.00 USD | 1,180.00 USD | 0.00 USD | `+30.75%` | `739.00` |
| `Live` | `Short` | `1.60` | 1,580,000.00 USD | 2,650.00 USD | 0.00 USD | `+31.57%` | `1,649.00` |
| `Live` | `Short` | `1.61` | 5,900,000.00 USD | 4,320,000.00 USD | 0.00 USD | `+32.39%` | `2,673,128.00` |
| `Live` | `Short` | `1.62` | 5,900,000.00 USD | 271.38 USD | 0.00 USD | `+33.21%` | `167.00` |
| `Live` | `Short` | `1.64` | 6,040,000.00 USD | 136,310.00 USD | 0.00 USD | `+34.03%` | `83,370.00` |
| `Live` | `Short` | `1.65` | 6,040,000.00 USD | 2,350.00 USD | 0.00 USD | `+34.85%` | `1,429.00` |
| `Live` | `Short` | `1.66` | 6,040,000.00 USD | 147.30 USD | 0.00 USD | `+35.67%` | `89.00` |
| `Live` | `Short` | `1.67` | 6,040,000.00 USD | 586.08 USD | 0.00 USD | `+36.49%` | `352.00` |
| `Live` | `Short` | `1.68` | 6,040,000.00 USD | 177.55 USD | 0.00 USD | `+37.31%` | `106.00` |
| `Live` | `Short` | `1.69` | 6,040,000.00 USD | 4,060.00 USD | 0.00 USD | `+38.13%` | `2,409.00` |
| `Live` | `Short` | `1.70` | 6,040,000.00 USD | 974.62 USD | 0.00 USD | `+38.95%` | `575.00` |
| `Live` | `Short` | `1.71` | 6,050,000.00 USD | 1,980.00 USD | 0.00 USD | `+39.77%` | `1,163.00` |
| `Live` | `Short` | `1.73` | 6,050,000.00 USD | 1,110.00 USD | 0.00 USD | `+41.41%` | `642.00` |
| `Live` | `Short` | `1.74` | 6,050,000.00 USD | 2,970.00 USD | 0.00 USD | `+42.22%` | `1,713.00` |
| `Live` | `Short` | `1.75` | 6,050,000.00 USD | 2,870.00 USD | 0.00 USD | `+43.04%` | `1,642.00` |
| `Live` | `Short` | `1.75` | 6,050,000.00 USD | 591.43 USD | 0.00 USD | `+43.86%` | `337.00` |
| `Live` | `Short` | `1.76` | 6,050,000.00 USD | 1,110.00 USD | 0.00 USD | `+44.68%` | `627.00` |
| `Live` | `Short` | `1.78` | 6,350,000.00 USD | 299,390.00 USD | 0.00 USD | `+46.32%` | `167,725.00` |
| `Live` | `Short` | `1.79` | 6,450,000.00 USD | 99,360.00 USD | 0.00 USD | `+47.14%` | `55,351.00` |
| `Live` | `Short` | `1.80` | 6,460,000.00 USD | 4,500.00 USD | 0.00 USD | `+47.96%` | `2,493.00` |
| `Live` | `Short` | `1.81` | 6,480,000.00 USD | 21,420.00 USD | 0.00 USD | `+48.78%` | `11,801.00` |
| `Live` | `Short` | `1.82` | 11,900,000.00 USD | 5,420,000.00 USD | 0.00 USD | `+49.60%` | `2,969,079.00` |
| `Live` | `Short` | `1.83` | 11,900,000.00 USD | 266.07 USD | 0.00 USD | `+50.42%` | `145.00` |
| `Live` | `Short` | `1.84` | 11,920,000.00 USD | 21,500.00 USD | 0.00 USD | `+51.24%` | `11,653.00` |
| `Live` | `Short` | `1.85` | 11,920,000.00 USD | 1,340.00 USD | 0.00 USD | `+52.06%` | `725.00` |
| `Live` | `Short` | `1.86` | 11,930,000.00 USD | 6,370.00 USD | 0.00 USD | `+52.88%` | `3,417.00` |
| `Live` | `Short` | `1.89` | 14,830,000.00 USD | 2,900,000.00 USD | 0.00 USD | `+54.52%` | `1,540,696.00` |
| `Live` | `Short` | `1.90` | 14,840,000.00 USD | 7,980.00 USD | 0.00 USD | `+55.34%` | `4,211.00` |
| `Live` | `Short` | `1.91` | 14,840,000.00 USD | 373.38 USD | 0.00 USD | `+56.16%` | `196.00` |
| `Live` | `Short` | `1.92` | 15,150,000.00 USD | 309,150.00 USD | 0.00 USD | `+56.98%` | `161,437.00` |
| `Live` | `Short` | `1.93` | 15,410,000.00 USD | 257,200.00 USD | 0.00 USD | `+57.80%` | `133,610.00` |
| `Live` | `Short` | `1.94` | 18,370,000.00 USD | 2,960,000.00 USD | 0.00 USD | `+58.62%` | `1,530,104.00` |
| `Live` | `Short` | `1.96` | 18,370,000.00 USD | 1,910.00 USD | 0.00 USD | `+60.26%` | `979.00` |
| `Live` | `Short` | `1.97` | 18,620,000.00 USD | 254,610.00 USD | 0.00 USD | `+61.08%` | `129,574.00` |
| `Live` | `Short` | `1.98` | 18,620,000.00 USD | 1,470.00 USD | 0.00 USD | `+61.90%` | `745.00` |
| `Live` | `Short` | `2.00` | 18,660,000.00 USD | 40,100.00 USD | 0.00 USD | `+64.36%` | `20,000.00` |
| `Live` | `Short` | `2.02` | 18,670,000.00 USD | 513.83 USD | 0.00 USD | `+65.18%` | `255.00` |
| `Live` | `Short` | `2.04` | 18,670,000.00 USD | 914.12 USD | 0.00 USD | `+67.64%` | `447.00` |
| `Live` | `Short` | `2.06` | 18,670,000.00 USD | 460.50 USD | 0.00 USD | `+69.28%` | `223.00` |
| `Live` | `Short` | `2.10` | 18,670,000.00 USD | 331.01 USD | 0.00 USD | `+71.74%` | `158.00` |
| `Live` | `Short` | `2.10` | 18,670,000.00 USD | 294.70 USD | 0.00 USD | `+72.56%` | `140.00` |
| `Live` | `Short` | `2.12` | 19,100,000.00 USD | 427,880.00 USD | 0.00 USD | `+73.37%` | `202,309.00` |
| `Live` | `Short` | `2.12` | 19,100,000.00 USD | 1,250.00 USD | 0.00 USD | `+74.19%` | `589.00` |
| `Live` | `Short` | `2.13` | 19,100,000.00 USD | 177.20 USD | 0.00 USD | `+75.01%` | `83.00` |
| `Live` | `Short` | `2.15` | 19,350,000.00 USD | 251,750.00 USD | 0.00 USD | `+75.83%` | `117,368.00` |
| `Live` | `Short` | `2.15` | 19,350,000.00 USD | 196.11 USD | 0.00 USD | `+76.65%` | `91.00` |
| `Live` | `Short` | `2.17` | 19,350,000.00 USD | 2,730.00 USD | 0.00 USD | `+78.29%` | `1,253.00` |
| `Live` | `Short` | `2.19` | 19,350,000.00 USD | 201.94 USD | 0.00 USD | `+79.93%` | `92.00` |
| `Live` | `Short` | `2.21` | 19,430,000.00 USD | 78,560.00 USD | 0.00 USD | `+80.75%` | `35,628.00` |
| `Live` | `Short` | `2.21` | 19,430,000.00 USD | 203.78 USD | 0.00 USD | `+81.57%` | `92.00` |
| `Live` | `Short` | `2.23` | 19,430,000.00 USD | 1,090.00 USD | 0.00 USD | `+82.39%` | `491.00` |
| `Live` | `Short` | `2.23` | 19,430,000.00 USD | 2,570.00 USD | 0.00 USD | `+83.21%` | `1,148.00` |
| `Live` | `Short` | `2.25` | 19,450,000.00 USD | 11,280.00 USD | 0.00 USD | `+84.85%` | `5,000.00` |
| `Live` | `Short` | `2.27` | 19,450,000.00 USD | 2,390.00 USD | 0.00 USD | `+85.67%` | `1,057.00` |
| `Live` | `Short` | `2.29` | 19,500,000.00 USD | 52,230.00 USD | 0.00 USD | `+88.13%` | `22,758.00` |
| `Live` | `Short` | `2.31` | 19,500,000.00 USD | 212.06 USD | 0.00 USD | `+88.95%` | `92.00` |
| `Live` | `Short` | `2.33` | 19,500,000.00 USD | 1,140.00 USD | 0.00 USD | `+90.59%` | `490.00` |
| `Live` | `Short` | `2.35` | 19,500,000.00 USD | 1,670.00 USD | 0.00 USD | `+93.05%` | `711.00` |
| `Live` | `Short` | `2.37` | 19,600,000.00 USD | 99,360.00 USD | 0.00 USD | `+93.87%` | `42,014.00` |
| `Live` | `Short` | `2.38` | 19,600,000.00 USD | 111.62 USD | 0.00 USD | `+94.69%` | `47.00` |
| `Live` | `Short` | `2.38` | 19,620,000.00 USD | 20,830.00 USD | 0.00 USD | `+95.51%` | `8,734.00` |
| `Live` | `Short` | `2.42` | 19,750,000.00 USD | 129,620.00 USD | 0.00 USD | `+97.97%` | `53,673.00` |
| `Live` | `Short` | `2.42` | 19,950,000.00 USD | 199,360.00 USD | 0.00 USD | `+98.79%` | `82,212.00` |
| `Live` | `Short` | `2.44` | 19,950,000.00 USD | 2,650.00 USD | 0.00 USD | `+99.61%` | `1,090.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.2550` | 1,980,000.00 USD | 0.00 USD | 116.53 USD | `-79.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3650` | 1,980,000.00 USD | 0.00 USD | 351.50 USD | `-70.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3750` | 1,980,000.00 USD | 0.00 USD | 139.12 USD | `-69.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3950` | 1,980,000.00 USD | 0.00 USD | 2,880.00 USD | `-67.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4050` | 1,980,000.00 USD | 0.00 USD | 2,950.00 USD | `-66.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4450` | 1,970,000.00 USD | 0.00 USD | 408.51 USD | `-63.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4550` | 1,970,000.00 USD | 0.00 USD | 273.00 USD | `-62.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4650` | 1,970,000.00 USD | 0.00 USD | 151.12 USD | `-61.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4750` | 1,970,000.00 USD | 0.00 USD | 142.50 USD | `-61.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4850` | 1,970,000.00 USD | 0.00 USD | 145.50 USD | `-60.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5050` | 1,970,000.00 USD | 0.00 USD | 1,030.00 USD | `-58.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5150` | 1,970,000.00 USD | 0.00 USD | 285.82 USD | `-57.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5250` | 1,970,000.00 USD | 0.00 USD | 306.60 USD | `-56.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5550` | 1,970,000.00 USD | 0.00 USD | 121.55 USD | `-54.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5650` | 1,970,000.00 USD | 0.00 USD | 656.53 USD | `-53.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5850` | 1,970,000.00 USD | 0.00 USD | 100.62 USD | `-52.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6250` | 1,970,000.00 USD | 0.00 USD | 203.75 USD | `-48.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6350` | 1,970,000.00 USD | 0.00 USD | 791.85 USD | `-47.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6450` | 1,970,000.00 USD | 0.00 USD | 573.40 USD | `-47.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6550` | 1,970,000.00 USD | 0.00 USD | 244.31 USD | `-46.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6650` | 1,970,000.00 USD | 0.00 USD | 29,530.00 USD | `-45.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6750` | 1,940,000.00 USD | 0.00 USD | 503.55 USD | `-44.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6850` | 1,940,000.00 USD | 0.00 USD | 480.19 USD | `-43.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6950` | 1,940,000.00 USD | 0.00 USD | 11,870.00 USD | `-43.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7050` | 1,930,000.00 USD | 0.00 USD | 2,260.00 USD | `-42.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7150` | 1,920,000.00 USD | 0.00 USD | 228.80 USD | `-41.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7250` | 1,920,000.00 USD | 0.00 USD | 536.50 USD | `-40.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7550` | 1,920,000.00 USD | 0.00 USD | 1,300.00 USD | `-38.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7650` | 1,920,000.00 USD | 0.00 USD | 2,880.00 USD | `-37.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.7950` | 1,920,000.00 USD | 0.00 USD | 878.48 USD | `-34.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 1,920,000.00 USD | 0.00 USD | 6,020.00 USD | `-32.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8550` | 1,910,000.00 USD | 0.00 USD | 1,360.00 USD | `-29.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8750` | 1,910,000.00 USD | 0.00 USD | 690.38 USD | `-28.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8850` | 1,910,000.00 USD | 0.00 USD | 1,210.00 USD | `-27.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8950` | 1,910,000.00 USD | 0.00 USD | 3,230.00 USD | `-26.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9050` | 1,900,000.00 USD | 0.00 USD | 838.94 USD | `-25.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9150` | 1,900,000.00 USD | 0.00 USD | 338.55 USD | `-24.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9250` | 1,900,000.00 USD | 0.00 USD | 1,060.00 USD | `-24.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9350` | 1,900,000.00 USD | 0.00 USD | 1,090.00 USD | `-23.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9450` | 1,900,000.00 USD | 0.00 USD | 112.46 USD | `-22.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9550` | 1,900,000.00 USD | 0.00 USD | 1,730.00 USD | `-21.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9650` | 1,900,000.00 USD | 0.00 USD | 4,010.00 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9750` | 1,900,000.00 USD | 0.00 USD | 6,200.00 USD | `-20.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9850` | 1,890,000.00 USD | 0.00 USD | 4,890.00 USD | `-19.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.9950` | 1,880,000.00 USD | 0.00 USD | 902.47 USD | `-18.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 1,880,000.00 USD | 0.00 USD | 15,420.00 USD | `-17.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 1,870,000.00 USD | 0.00 USD | 59,740.00 USD | `-16.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.02` | 1,810,000.00 USD | 0.00 USD | 2,420.00 USD | `-15.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.03` | 1,810,000.00 USD | 0.00 USD | 42,670.00 USD | `-15.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.04` | 1,760,000.00 USD | 0.00 USD | 1,780.00 USD | `-14.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.05` | 1,760,000.00 USD | 0.00 USD | 25,010.00 USD | `-13.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.06` | 1,740,000.00 USD | 0.00 USD | 3,960.00 USD | `-12.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.07` | 1,730,000.00 USD | 0.00 USD | 48,460.00 USD | `-11.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.08` | 1,680,000.00 USD | 0.00 USD | 3,690.00 USD | `-11.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.09` | 1,680,000.00 USD | 0.00 USD | 279,970.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.10` | 1,400,000.00 USD | 0.00 USD | 21,590.00 USD | `-9.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.11` | 1,380,000.00 USD | 0.00 USD | 9,410.00 USD | `-8.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.12` | 1,370,000.00 USD | 0.00 USD | 121,430.00 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.14` | 1,250,000.00 USD | 0.00 USD | 13,730.00 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.15` | 1,230,000.00 USD | 0.00 USD | 120,050.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.16` | 1,110,000.00 USD | 0.00 USD | 40,860.00 USD | `-5.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.17` | 1,070,000.00 USD | 0.00 USD | 50,120.00 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.18` | 1,020,000.00 USD | 0.00 USD | 101,020.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.19` | 921,940.00 USD | 0.00 USD | 230,940.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 691,000.00 USD | 0.00 USD | 254,700.00 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.21` | 436,300.00 USD | 0.00 USD | 412,440.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.22` | 23,870.00 USD | 0.00 USD | 23,870.00 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 697.03 USD | 697.03 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.24` | 271,660.00 USD | 270,970.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 365,830.00 USD | 94,170.00 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.25` | 377,130.00 USD | 11,300.00 USD | 0.00 USD | `+2.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.26` | 676,030.00 USD | 298,890.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.27` | 693,900.00 USD | 17,870.00 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.28` | 944,680.00 USD | 250,780.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.29` | 999,530.00 USD | 54,850.00 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.30` | 1,040,000.00 USD | 35,690.00 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.31` | 1,690,000.00 USD | 650,180.00 USD | 0.00 USD | `+7.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.32` | 1,890,000.00 USD | 205,800.00 USD | 0.00 USD | `+8.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.33` | 1,940,000.00 USD | 44,130.00 USD | 0.00 USD | `+9.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.34` | 2,010,000.00 USD | 77,550.00 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.35` | 2,030,000.00 USD | 14,640.00 USD | 0.00 USD | `+11.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.36` | 2,280,000.00 USD | 249,240.00 USD | 0.00 USD | `+11.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.38` | 2,360,000.00 USD | 81,760.00 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.39` | 2,410,000.00 USD | 53,860.00 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.40` | 2,420,000.00 USD | 3,960.00 USD | 0.00 USD | `+14.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.41` | 6,680,000.00 USD | 4,260,000.00 USD | 0.00 USD | `+15.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.42` | 6,680,000.00 USD | 3,710.00 USD | 0.00 USD | `+15.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.43` | 6,690,000.00 USD | 5,680.00 USD | 0.00 USD | `+16.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.44` | 6,770,000.00 USD | 78,630.00 USD | 0.00 USD | `+17.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.45` | 7,010,000.00 USD | 242,580.00 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.46` | 7,020,000.00 USD | 7,510.00 USD | 0.00 USD | `+19.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.47` | 7,040,000.00 USD | 23,260.00 USD | 0.00 USD | `+20.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.48` | 7,150,000.00 USD | 108,020.00 USD | 0.00 USD | `+20.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.49` | 7,160,000.00 USD | 14,970.00 USD | 0.00 USD | `+21.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 7,180,000.00 USD | 14,120.00 USD | 0.00 USD | `+22.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.50` | 7,240,000.00 USD | 65,400.00 USD | 0.00 USD | `+23.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.51` | 7,250,000.00 USD | 11,760.00 USD | 0.00 USD | `+24.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.52` | 7,270,000.00 USD | 19,430.00 USD | 0.00 USD | `+25.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.53` | 7,320,000.00 USD | 45,620.00 USD | 0.00 USD | `+25.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.54` | 7,330,000.00 USD | 10,870.00 USD | 0.00 USD | `+26.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.55` | 7,330,000.00 USD | 2,380.00 USD | 0.00 USD | `+27.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.56` | 7,340,000.00 USD | 6,450.00 USD | 0.00 USD | `+28.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.57` | 7,340,000.00 USD | 5,570.00 USD | 0.00 USD | `+29.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.58` | 7,360,000.00 USD | 12,640.00 USD | 0.00 USD | `+29.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.59` | 7,500,000.00 USD | 139,320.00 USD | 0.00 USD | `+30.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.60` | 7,500,000.00 USD | 1,840.00 USD | 0.00 USD | `+31.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.61` | 7,580,000.00 USD | 80,330.00 USD | 0.00 USD | `+32.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.62` | 7,580,000.00 USD | 464.75 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.64` | 7,760,000.00 USD | 179,860.00 USD | 0.00 USD | `+34.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.65` | 7,760,000.00 USD | 2,670.00 USD | 0.00 USD | `+34.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.66` | 7,850,000.00 USD | 85,010.00 USD | 0.00 USD | `+35.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.67` | 7,850,000.00 USD | 6,080.00 USD | 0.00 USD | `+36.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.68` | 7,870,000.00 USD | 18,400.00 USD | 0.00 USD | `+37.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.69` | 7,940,000.00 USD | 70,850.00 USD | 0.00 USD | `+38.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.70` | 7,960,000.00 USD | 18,000.00 USD | 0.00 USD | `+38.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.71` | 8,190,000.00 USD | 230,160.00 USD | 0.00 USD | `+39.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.72` | 8,200,000.00 USD | 14,250.00 USD | 0.00 USD | `+40.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.73` | 8,210,000.00 USD | 3,120.00 USD | 0.00 USD | `+41.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.74` | 8,250,000.00 USD | 43,240.00 USD | 0.00 USD | `+42.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 8,250,000.00 USD | 3,330.00 USD | 0.00 USD | `+43.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.75` | 8,260,000.00 USD | 5,510.00 USD | 0.00 USD | `+43.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.76` | 8,280,000.00 USD | 21,720.00 USD | 0.00 USD | `+44.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.77` | 8,410,000.00 USD | 128,330.00 USD | 0.00 USD | `+45.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.78` | 8,510,000.00 USD | 96,600.00 USD | 0.00 USD | `+46.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.79` | 8,510,000.00 USD | 3,980.00 USD | 0.00 USD | `+47.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.80` | 8,510,000.00 USD | 254.51 USD | 0.00 USD | `+47.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.81` | 8,520,000.00 USD | 12,860.00 USD | 0.00 USD | `+48.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.82` | 8,530,000.00 USD | 3,970.00 USD | 0.00 USD | `+49.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.83` | 8,530,000.00 USD | 8,170.00 USD | 0.00 USD | `+50.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.84` | 8,540,000.00 USD | 843.17 USD | 0.00 USD | `+51.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.85` | 8,540,000.00 USD | 8,390.00 USD | 0.00 USD | `+52.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.88` | 8,550,000.00 USD | 4,420.00 USD | 0.00 USD | `+53.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.89` | 8,550,000.00 USD | 591.89 USD | 0.00 USD | `+54.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.90` | 8,600,000.00 USD | 46,370.00 USD | 0.00 USD | `+55.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.91` | 8,600,000.00 USD | 9,270.00 USD | 0.00 USD | `+56.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.94` | 8,600,000.00 USD | 265.10 USD | 0.00 USD | `+58.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.95` | 8,610,000.00 USD | 2,040.00 USD | 0.00 USD | `+59.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.96` | 8,610,000.00 USD | 1,070.00 USD | 0.00 USD | `+60.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.97` | 8,620,000.00 USD | 14,120.00 USD | 0.00 USD | `+61.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.98` | 8,630,000.00 USD | 4,010.00 USD | 0.00 USD | `+61.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.99` | 8,630,000.00 USD | 325.54 USD | 0.00 USD | `+62.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,630,000.00 USD | 7,020.00 USD | 0.00 USD | `+63.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.00` | 8,760,000.00 USD | 123,020.00 USD | 0.00 USD | `+64.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.02` | 8,760,000.00 USD | 3,350.00 USD | 0.00 USD | `+66.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,760,000.00 USD | 181.12 USD | 0.00 USD | `+66.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.04` | 8,760,000.00 USD | 382.41 USD | 0.00 USD | `+67.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.06` | 8,760,000.00 USD | 3,420.00 USD | 0.00 USD | `+69.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.08` | 8,760,000.00 USD | 661.93 USD | 0.00 USD | `+70.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 8,890,000.00 USD | 124,400.00 USD | 0.00 USD | `+71.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.10` | 9,040,000.00 USD | 149,690.00 USD | 0.00 USD | `+72.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.12` | 9,050,000.00 USD | 13,900.00 USD | 0.00 USD | `+74.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 9,080,000.00 USD | 24,840.00 USD | 0.00 USD | `+75.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.15` | 9,130,000.00 USD | 50,580.00 USD | 0.00 USD | `+76.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.17` | 9,130,000.00 USD | 2,690.00 USD | 0.00 USD | `+77.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.19` | 9,130,000.00 USD | 2,180.00 USD | 0.00 USD | `+79.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.21` | 9,280,000.00 USD | 151,380.00 USD | 0.00 USD | `+81.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.27` | 9,290,000.00 USD | 3,120.00 USD | 0.00 USD | `+86.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 9,290,000.00 USD | 1,140.00 USD | 0.00 USD | `+87.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.29` | 9,300,000.00 USD | 11,670.00 USD | 0.00 USD | `+88.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.31` | 9,300,000.00 USD | 370.40 USD | 0.00 USD | `+89.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.33` | 9,300,000.00 USD | 733.19 USD | 0.00 USD | `+91.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.37` | 9,300,000.00 USD | 2,410.00 USD | 0.00 USD | `+93.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 9,300,000.00 USD | 475.00 USD | 0.00 USD | `+94.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.38` | 9,300,000.00 USD | 1,190.00 USD | 0.00 USD | `+95.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 9,310,000.00 USD | 2,540.00 USD | 0.00 USD | `+96.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.40` | 9,310,000.00 USD | 1,590.00 USD | 0.00 USD | `+97.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 9,310,000.00 USD | 1,370.00 USD | 0.00 USD | `+97.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.42` | 9,330,000.00 USD | 19,590.00 USD | 0.00 USD | `+98.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `2.44` | 9,330,000.00 USD | 564.92 USD | 0.00 USD | `+99.61%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `1.11` | 31,160,000.00 USD | 0.00 USD | 31,160,000.00 USD | 17,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.11` | 52,480,000.00 USD | 0.00 USD | 52,480,000.00 USD | 21,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.11` | 31,140,000.00 USD | 0.00 USD | 31,140,000.00 USD | 18,710.00 USD | 0.00 USD | 121,720.00 USD |
| `1D` | `1.11` | 31,000,000.00 USD | 0.00 USD | 31,000,000.00 USD | 0.00 USD | 2,700.00 USD | 0.00 USD |
| `7D` | `1.11` | 52,460,000.00 USD | 0.00 USD | 52,460,000.00 USD | 0.00 USD | 1,730.00 USD | 11,030.00 USD |
| `1D` | `1.12` | 31,000,000.00 USD | 0.00 USD | 31,000,000.00 USD | 0.00 USD | 0.00 USD | 62,820.00 USD |
| `7D` | `1.12` | 52,450,000.00 USD | 0.00 USD | 52,450,000.00 USD | 0.00 USD | 79,230.00 USD | 0.00 USD |
| `1D` | `1.12` | 30,940,000.00 USD | 0.00 USD | 30,940,000.00 USD | 0.00 USD | 47,340.00 USD | 5,360.00 USD |
| `1D` | `1.12` | 30,880,000.00 USD | 0.00 USD | 30,880,000.00 USD | 10,140.00 USD | 2,890.00 USD | 0.00 USD |
| `7D` | `1.12` | 52,370,000.00 USD | 0.00 USD | 52,370,000.00 USD | 17,190.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `1.12` | 30,870,000.00 USD | 0.00 USD | 30,870,000.00 USD | 0.00 USD | 1,530.00 USD | 57,100.00 USD |
| `7D` | `1.12` | 52,350,000.00 USD | 0.00 USD | 52,350,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD |
| `1D` | `1.12` | 30,810,000.00 USD | 0.00 USD | 30,810,000.00 USD | 66,330.00 USD | 29,190.00 USD | 56,030.00 USD |
| `7D` | `1.12` | 52,350,000.00 USD | 0.00 USD | 52,350,000.00 USD | 0.00 USD | 1,350.00 USD | 209,650.00 USD |
| `1D` | `1.13` | 30,660,000.00 USD | 0.00 USD | 30,660,000.00 USD | 0.00 USD | 783.15 USD | 104,240.00 USD |
| `1D` | `1.13` | 30,550,000.00 USD | 0.00 USD | 30,550,000.00 USD | 0.00 USD | 42,490.00 USD | 78,200.00 USD |
| `7D` | `1.13` | 52,140,000.00 USD | 0.00 USD | 52,140,000.00 USD | 0.00 USD | 0.00 USD | 194,280.00 USD |
| `1D` | `1.13` | 30,430,000.00 USD | 0.00 USD | 30,430,000.00 USD | 0.00 USD | 66,770.00 USD | 166,310.00 USD |
| `7D` | `1.13` | 51,950,000.00 USD | 0.00 USD | 51,950,000.00 USD | 5,450.00 USD | 3,410.00 USD | 3,970.00 USD |
| `1D` | `1.13` | 30,200,000.00 USD | 0.00 USD | 30,200,000.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD |
| `7D` | `1.13` | 51,930,000.00 USD | 0.00 USD | 51,930,000.00 USD | 144,660.00 USD | 189,370.00 USD | 142,970.00 USD |
| `1D` | `1.14` | 30,140,000.00 USD | 0.00 USD | 30,140,000.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD |
| `7D` | `1.14` | 51,460,000.00 USD | 0.00 USD | 51,460,000.00 USD | 0.00 USD | 88,050.00 USD | 157,540.00 USD |
| `1D` | `1.14` | 30,090,000.00 USD | 0.00 USD | 30,090,000.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD |
| `7D` | `1.14` | 51,210,000.00 USD | 0.00 USD | 51,210,000.00 USD | 79,780.00 USD | 0.00 USD | 20,240.00 USD |
| `1D` | `1.14` | 30,000,000.00 USD | 0.00 USD | 30,000,000.00 USD | 26,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.14` | 51,110,000.00 USD | 0.00 USD | 51,110,000.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 29,980,000.00 USD | 0.00 USD | 29,980,000.00 USD | 29,510.00 USD | 749.15 USD | 33,330.00 USD |
| `7D` | `1.14` | 51,100,000.00 USD | 0.00 USD | 51,100,000.00 USD | 63,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.14` | 29,910,000.00 USD | 0.00 USD | 29,910,000.00 USD | 89,980.00 USD | 495.40 USD | 49,840.00 USD |
| `7D` | `1.14` | 51,040,000.00 USD | 0.00 USD | 51,040,000.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `1D` | `1.15` | 29,770,000.00 USD | 0.00 USD | 29,770,000.00 USD | 5,140.00 USD | 570.50 USD | 33,610.00 USD |
| `7D` | `1.15` | 50,920,000.00 USD | 0.00 USD | 50,920,000.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.15` | 50,910,000.00 USD | 0.00 USD | 50,910,000.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `1D` | `1.15` | 29,730,000.00 USD | 0.00 USD | 29,730,000.00 USD | 16,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.15` | 50,770,000.00 USD | 0.00 USD | 50,770,000.00 USD | 272,740.00 USD | 46,940.00 USD | 40,030.00 USD |
| `7D` | `1.15` | 50,410,000.00 USD | 0.00 USD | 50,410,000.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `1D` | `1.15` | 29,720,000.00 USD | 0.00 USD | 29,720,000.00 USD | 4,040.00 USD | 11,230.00 USD | 185,060.00 USD |
| `7D` | `1.15` | 50,250,000.00 USD | 0.00 USD | 50,250,000.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `1D` | `1.16` | 29,520,000.00 USD | 0.00 USD | 29,520,000.00 USD | 91,040.00 USD | 52,530.00 USD | 196,750.00 USD |
| `7D` | `1.16` | 49,870,000.00 USD | 0.00 USD | 49,870,000.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `1D` | `1.16` | 29,180,000.00 USD | 0.00 USD | 29,180,000.00 USD | 29,120.00 USD | 9,570.00 USD | 31,170.00 USD |
| `7D` | `1.16` | 49,220,000.00 USD | 0.00 USD | 49,220,000.00 USD | 178,230.00 USD | 99,350.00 USD | 520,790.00 USD |
| `1D` | `1.16` | 29,110,000.00 USD | 0.00 USD | 29,110,000.00 USD | 137,370.00 USD | 26,520.00 USD | 149,720.00 USD |
| `7D` | `1.16` | 48,420,000.00 USD | 0.00 USD | 48,420,000.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `1D` | `1.16` | 28,790,000.00 USD | 0.00 USD | 28,790,000.00 USD | 288,770.00 USD | 177,310.00 USD | 151,900.00 USD |
| `7D` | `1.16` | 47,900,000.00 USD | 0.00 USD | 47,900,000.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `1D` | `1.16` | 28,170,000.00 USD | 0.00 USD | 28,170,000.00 USD | 292,830.00 USD | 135,810.00 USD | 193,830.00 USD |
| `7D` | `1.16` | 46,870,000.00 USD | 0.00 USD | 46,870,000.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `1D` | `1.17` | 27,550,000.00 USD | 0.00 USD | 27,550,000.00 USD | 63,800.00 USD | 60,200.00 USD | 91,270.00 USD |
| `7D` | `1.17` | 45,500,000.00 USD | 0.00 USD | 45,500,000.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `1D` | `1.17` | 27,340,000.00 USD | 0.00 USD | 27,340,000.00 USD | 182,810.00 USD | 38,870.00 USD | 90,040.00 USD |
| `7D` | `1.17` | 44,870,000.00 USD | 0.00 USD | 44,870,000.00 USD | 454,610.00 USD | 132,100.00 USD | 791,480.00 USD |
| `1D` | `1.17` | 27,030,000.00 USD | 0.00 USD | 27,030,000.00 USD | 86,630.00 USD | 31,280.00 USD | 43,000.00 USD |
| `7D` | `1.17` | 43,490,000.00 USD | 0.00 USD | 43,490,000.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `1D` | `1.17` | 26,860,000.00 USD | 0.00 USD | 26,860,000.00 USD | 27,580.00 USD | 49,790.00 USD | 94,780.00 USD |
| `7D` | `1.17` | 41,990,000.00 USD | 0.00 USD | 41,990,000.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `1D` | `1.17` | 26,690,000.00 USD | 0.00 USD | 26,690,000.00 USD | 32,280.00 USD | 26,620.00 USD | 195,860.00 USD |
| `7D` | `1.17` | 40,600,000.00 USD | 0.00 USD | 40,600,000.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `1D` | `1.18` | 26,440,000.00 USD | 0.00 USD | 26,440,000.00 USD | 141,540.00 USD | 16,760.00 USD | 182,860.00 USD |
| `7D` | `1.18` | 39,800,000.00 USD | 0.00 USD | 39,800,000.00 USD | 290,470.00 USD | 90,550.00 USD | 499,970.00 USD |
| `1D` | `1.18` | 26,100,000.00 USD | 0.00 USD | 26,100,000.00 USD | 80,830.00 USD | 13,900.00 USD | 30,960.00 USD |
| `7D` | `1.18` | 38,920,000.00 USD | 0.00 USD | 38,920,000.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `1D` | `1.18` | 25,970,000.00 USD | 0.00 USD | 25,970,000.00 USD | 93,410.00 USD | 41,360.00 USD | 49,320.00 USD |
| `7D` | `1.18` | 38,460,000.00 USD | 0.00 USD | 38,460,000.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `1D` | `1.18` | 25,790,000.00 USD | 0.00 USD | 25,790,000.00 USD | 19,950.00 USD | 10,580.00 USD | 2,210.00 USD |
| `7D` | `1.18` | 37,750,000.00 USD | 0.00 USD | 37,750,000.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `1D` | `1.18` | 25,750,000.00 USD | 0.00 USD | 25,750,000.00 USD | 21,010.00 USD | 22,830.00 USD | 66,040.00 USD |
| `7D` | `1.18` | 37,370,000.00 USD | 0.00 USD | 37,370,000.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `1D` | `1.19` | 25,640,000.00 USD | 0.00 USD | 25,640,000.00 USD | 92,110.00 USD | 7,460.00 USD | 27,490.00 USD |
| `7D` | `1.19` | 37,240,000.00 USD | 0.00 USD | 37,240,000.00 USD | 123,240.00 USD | 97,270.00 USD | 289,750.00 USD |
| `1D` | `1.19` | 25,520,000.00 USD | 0.00 USD | 25,520,000.00 USD | 16,710.00 USD | 139,070.00 USD | 324,370.00 USD |
| `7D` | `1.19` | 36,730,000.00 USD | 0.00 USD | 36,730,000.00 USD | 190,550.00 USD | 38,510.00 USD | 544,050.00 USD |
| `1D` | `1.19` | 25,040,000.00 USD | 0.00 USD | 25,040,000.00 USD | 239,430.00 USD | 8,930.00 USD | 410,930.00 USD |
| `7D` | `1.19` | 35,960,000.00 USD | 0.00 USD | 35,960,000.00 USD | 182,110.00 USD | 132,500.00 USD | 276,980.00 USD |
| `1D` | `1.19` | 24,380,000.00 USD | 0.00 USD | 24,380,000.00 USD | 48,220.00 USD | 10,480.00 USD | 205,240.00 USD |
| `7D` | `1.19` | 35,370,000.00 USD | 0.00 USD | 35,370,000.00 USD | 152,830.00 USD | 265,920.00 USD | 471,430.00 USD |
| `1D` | `1.19` | 24,110,000.00 USD | 0.00 USD | 24,110,000.00 USD | 25,890.00 USD | 217,630.00 USD | 79,010.00 USD |
| `7D` | `1.19` | 34,480,000.00 USD | 0.00 USD | 34,480,000.00 USD | 218,910.00 USD | 106,640.00 USD | 335,240.00 USD |
| `1D` | `1.20` | 23,790,000.00 USD | 0.00 USD | 23,790,000.00 USD | 15,240.00 USD | 40,110.00 USD | 48,430.00 USD |
| `7D` | `1.20` | 33,820,000.00 USD | 0.00 USD | 33,820,000.00 USD | 381,050.00 USD | 81,170.00 USD | 291,070.00 USD |
| `1D` | `1.20` | 23,690,000.00 USD | 0.00 USD | 23,690,000.00 USD | 21,190.00 USD | 3,620.00 USD | 3,770.00 USD |
| `7D` | `1.20` | 33,060,000.00 USD | 0.00 USD | 33,060,000.00 USD | 5,350.00 USD | 102,680.00 USD | 187,830.00 USD |
| `1D` | `1.20` | 23,660,000.00 USD | 0.00 USD | 23,660,000.00 USD | 66,960.00 USD | 22,280.00 USD | 291,610.00 USD |
| `7D` | `1.20` | 32,770,000.00 USD | 0.00 USD | 32,770,000.00 USD | 67,200.00 USD | 158,480.00 USD | 738,030.00 USD |
| `1D` | `1.20` | 23,280,000.00 USD | 0.00 USD | 23,280,000.00 USD | 169,810.00 USD | 250,260.00 USD | 180,340.00 USD |
| `7D` | `1.20` | 31,800,000.00 USD | 0.00 USD | 31,800,000.00 USD | 243,240.00 USD | 225,970.00 USD | 15,030.00 USD |
| `1D` | `1.20` | 22,680,000.00 USD | 0.00 USD | 22,680,000.00 USD | 102,120.00 USD | 4,970.00 USD | 260,610.00 USD |
| `7D` | `1.20` | 31,320,000.00 USD | 0.00 USD | 31,320,000.00 USD | 202,570.00 USD | 146,780.00 USD | 534,000.00 USD |
| `1D` | `1.21` | 22,310,000.00 USD | 0.00 USD | 22,310,000.00 USD | 4,360.00 USD | 297,650.00 USD | 195,510.00 USD |
| `7D` | `1.21` | 30,440,000.00 USD | 0.00 USD | 30,440,000.00 USD | 0.00 USD | 17,680.00 USD | 79,720.00 USD |
| `1D` | `1.21` | 21,810,000.00 USD | 0.00 USD | 21,810,000.00 USD | 81,900.00 USD | 32,170.00 USD | 415,780.00 USD |
| `7D` | `1.21` | 30,340,000.00 USD | 0.00 USD | 30,340,000.00 USD | 80,450.00 USD | 7,260.00 USD | 9,940.00 USD |
| `1D` | `1.21` | 21,280,000.00 USD | 0.00 USD | 21,280,000.00 USD | 220,830.00 USD | 67,350.00 USD | 14,960.00 USD |
| `7D` | `1.21` | 30,240,000.00 USD | 0.00 USD | 30,240,000.00 USD | 659,990.00 USD | 518,690.00 USD | 368,310.00 USD |
| `1D` | `1.21` | 20,980,000.00 USD | 0.00 USD | 20,980,000.00 USD | 99,310.00 USD | 425,250.00 USD | 731,080.00 USD |
| `7D` | `1.21` | 28,690,000.00 USD | 0.00 USD | 28,690,000.00 USD | 180,260.00 USD | 264,440.00 USD | 802,150.00 USD |
| `1D` | `1.21` | 19,720,000.00 USD | 0.00 USD | 19,720,000.00 USD | 419,060.00 USD | 162,630.00 USD | 699,260.00 USD |
| `7D` | `1.21` | 27,450,000.00 USD | 0.00 USD | 27,450,000.00 USD | 302,400.00 USD | 51,780.00 USD | 50,590.00 USD |
| `1D` | `1.22` | 18,440,000.00 USD | 0.00 USD | 18,440,000.00 USD | 166,960.00 USD | 8,790.00 USD | 102,180.00 USD |
| `7D` | `1.22` | 27,040,000.00 USD | 0.00 USD | 27,040,000.00 USD | 49,970.00 USD | 48,510.00 USD | 75,690.00 USD |
| `1D` | `1.22` | 18,160,000.00 USD | 0.00 USD | 18,160,000.00 USD | 118,950.00 USD | 5,680.00 USD | 470,840.00 USD |
| `7D` | `1.22` | 26,870,000.00 USD | 0.00 USD | 26,870,000.00 USD | 157,620.00 USD | 396,140.00 USD | 396,840.00 USD |
| `1D` | `1.22` | 17,570,000.00 USD | 0.00 USD | 17,570,000.00 USD | 285,170.00 USD | 423,840.00 USD | 178,880.00 USD |
| `7D` | `1.22` | 25,920,000.00 USD | 0.00 USD | 25,920,000.00 USD | 256,390.00 USD | 8,330.00 USD | 40,620.00 USD |
| `1D` | `1.22` | 16,680,000.00 USD | 0.00 USD | 16,680,000.00 USD | 54,610.00 USD | 42,060.00 USD | 228,420.00 USD |
| `7D` | `1.22` | 25,610,000.00 USD | 0.00 USD | 25,610,000.00 USD | 245,120.00 USD | 10,480.00 USD | 328,940.00 USD |
| `1D` | `1.22` | 16,360,000.00 USD | 0.00 USD | 16,360,000.00 USD | 141,030.00 USD | 525,900.00 USD | 394,250.00 USD |
| `7D` | `1.22` | 25,030,000.00 USD | 0.00 USD | 25,030,000.00 USD | 0.00 USD | 205,130.00 USD | 1,040,000.00 USD |
| `1D` | `1.23` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 828,850.00 USD | 352,590.00 USD | 2,750,000.00 USD |
| `7D` | `1.23` | 23,780,000.00 USD | 0.00 USD | 23,780,000.00 USD | 1,040,000.00 USD | 788,680.00 USD | 1,050,000.00 USD |
| `1D` | `1.23` | 11,360,000.00 USD | 0.00 USD | 11,360,000.00 USD | 344,500.00 USD | 161,310.00 USD | 1,030,000.00 USD |
| `7D` | `1.23` | 20,890,000.00 USD | 0.00 USD | 20,890,000.00 USD | 313,350.00 USD | 128,580.00 USD | 16,600.00 USD |
| `1D` | `1.23` | 9,820,000.00 USD | 0.00 USD | 9,820,000.00 USD | 105,710.00 USD | 213,020.00 USD | 1,080,000.00 USD |
| `7D` | `1.23` | 20,430,000.00 USD | 0.00 USD | 20,430,000.00 USD | 0.00 USD | 1,110,000.00 USD | 1,790,000.00 USD |
| `1D` | `1.23` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 319,240.00 USD | 1,170,000.00 USD | 0.00 USD |
| `7D` | `1.23` | 17,540,000.00 USD | 0.00 USD | 17,540,000.00 USD | 782,590.00 USD | 485,710.00 USD | 8,010.00 USD |
| `1D` | `1.23` | 6,930,000.00 USD | 0.00 USD | 6,930,000.00 USD | 281,800.00 USD | 336,650.00 USD | 1,030,000.00 USD |
| `7D` | `1.23` | 16,260,000.00 USD | 0.00 USD | 16,260,000.00 USD | 1,040,000.00 USD | 597,200.00 USD | 112,990.00 USD |
| `1D` | `1.24` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 433,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.24` | 14,510,000.00 USD | 0.00 USD | 14,510,000.00 USD | 996,240.00 USD | 998,790.00 USD | 66,130.00 USD |
| `1D` | `1.24` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 267,830.00 USD | 542,950.00 USD | 739,970.00 USD |
| `7D` | `1.24` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 1,640,000.00 USD | 1,500,000.00 USD | 2,820,000.00 USD |
| `1D` | `1.24` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 663,280.00 USD | 998,910.00 USD | 0.00 USD |
| `7D` | `1.24` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 2,610,000.00 USD | 799,870.00 USD | 0.00 USD |
| `7D` | `1.24` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 1,820,000.00 USD | 374,420.00 USD | 0.00 USD |
| `1D` | `1.24` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 305,740.00 USD | 774,420.00 USD | 560,940.00 USD |
| `7D` | `1.24` | 896,470.00 USD | 0.00 USD | 896,470.00 USD | 896,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 2,050,000.00 USD |
| `1D` | `1.25` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 2,050,000.00 USD |
| `7D` | `1.25` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 3,330,000.00 USD | 923,130.00 USD | 0.00 USD |
| `7D` | `1.25` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 3,330,000.00 USD | 923,130.00 USD | 0.00 USD |
| `1D` | `1.25` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 10,880,000.00 USD | 10,880,000.00 USD | 0.00 USD | 140,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 202,510.00 USD | 0.00 USD | 392,980.00 USD |
| `7D` | `1.25` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 180,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.25` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 532,200.00 USD |
| `7D` | `1.25` | 12,000,000.00 USD | 12,000,000.00 USD | 0.00 USD | 74,170.00 USD | 0.00 USD | 860,180.00 USD |
| `1D` | `1.25` | 9,680,000.00 USD | 9,680,000.00 USD | 0.00 USD | 794,390.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.25` | 12,190,000.00 USD | 12,190,000.00 USD | 0.00 USD | 172,030.00 USD | 0.00 USD | 18,740.00 USD |
| `1D` | `1.26` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 803,540.00 USD | 140,210.00 USD | 193,710.00 USD |
| `1D` | `1.26` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 86,570.00 USD | 3,600.00 USD | 0.00 USD |
| `7D` | `1.26` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 107,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `1.26` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 331,210.00 USD | 66,520.00 USD | 1,690,000.00 USD |
| `7D` | `1.26` | 15,260,000.00 USD | 15,260,000.00 USD | 0.00 USD | 0.00 USD | 381,520.00 USD | 2,580,000.00 USD |
| `1D` | `1.26` | 16,360,000.00 USD | 16,360,000.00 USD | 0.00 USD | 1,050,000.00 USD | 696,320.00 USD | 1,620,000.00 USD |
| `7D` | `1.26` | 18,800,000.00 USD | 18,800,000.00 USD | 0.00 USD | 834,020.00 USD | 799,870.00 USD | 1,910,000.00 USD |
| `1D` | `1.26` | 20,010,000.00 USD | 20,010,000.00 USD | 0.00 USD | 367,910.00 USD | 759,740.00 USD | 2,520,000.00 USD |
| `7D` | `1.26` | 25,740,000.00 USD | 25,740,000.00 USD | 0.00 USD | 1,640,000.00 USD | 891,350.00 USD | 4,400,000.00 USD |
| `1D` | `1.27` | 22,260,000.00 USD | 22,260,000.00 USD | 0.00 USD | 39,860.00 USD | 1,080,000.00 USD | 1,130,000.00 USD |
| `7D` | `1.27` | 39,370,000.00 USD | 39,370,000.00 USD | 0.00 USD | 2,620,000.00 USD | 2,370,000.00 USD | 8,640,000.00 USD |
| `1D` | `1.27` | 24,360,000.00 USD | 24,360,000.00 USD | 0.00 USD | 23,990.00 USD | 2,070,000.00 USD | 0.00 USD |
| `7D` | `1.27` | 44,140,000.00 USD | 44,140,000.00 USD | 0.00 USD | 0.00 USD | 2,630,000.00 USD | 2,140,000.00 USD |
| `1D` | `1.27` | 27,350,000.00 USD | 27,350,000.00 USD | 0.00 USD | 369,350.00 USD | 841,430.00 USD | 1,780,000.00 USD |
| `7D` | `1.27` | 47,780,000.00 USD | 47,780,000.00 USD | 0.00 USD | 1,030,000.00 USD | 2,480,000.00 USD | 123,930.00 USD |
| `1D` | `1.27` | 30,230,000.00 USD | 30,230,000.00 USD | 0.00 USD | 1,860,000.00 USD | 348,710.00 USD | 676,760.00 USD |
| `7D` | `1.27` | 52,550,000.00 USD | 52,550,000.00 USD | 0.00 USD | 186,960.00 USD | 3,990,000.00 USD | 591,560.00 USD |
| `1D` | `1.27` | 36,770,000.00 USD | 36,770,000.00 USD | 0.00 USD | 778,390.00 USD | 2,410,000.00 USD | 3,350,000.00 USD |
| `7D` | `1.27` | 68,980,000.00 USD | 68,980,000.00 USD | 0.00 USD | 4,840,000.00 USD | 2,340,000.00 USD | 9,260,000.00 USD |
| `1D` | `1.28` | 47,340,000.00 USD | 47,340,000.00 USD | 0.00 USD | 3,100,000.00 USD | 2,940,000.00 USD | 4,520,000.00 USD |
| `7D` | `1.28` | 87,260,000.00 USD | 87,260,000.00 USD | 0.00 USD | 6,760,000.00 USD | 3,160,000.00 USD | 8,350,000.00 USD |
| `1D` | `1.28` | 55,070,000.00 USD | 55,070,000.00 USD | 0.00 USD | 3,180,000.00 USD | 2,210,000.00 USD | 2,350,000.00 USD |
| `7D` | `1.28` | 93,550,000.00 USD | 93,550,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,940,000.00 USD | 1,090,000.00 USD |
| `1D` | `1.28` | 56,400,000.00 USD | 56,400,000.00 USD | 0.00 USD | 209,970.00 USD | 608,220.00 USD | 507,970.00 USD |
| `7D` | `1.28` | 94,510,000.00 USD | 94,510,000.00 USD | 0.00 USD | 0.00 USD | 879,610.00 USD | 79,220.00 USD |
| `1D` | `1.28` | 59,260,000.00 USD | 59,260,000.00 USD | 0.00 USD | 1,120,000.00 USD | 199,040.00 USD | 1,540,000.00 USD |
| `7D` | `1.28` | 96,510,000.00 USD | 96,510,000.00 USD | 0.00 USD | 1,460,000.00 USD | 478,060.00 USD | 67,480.00 USD |
| `1D` | `1.28` | 61,290,000.00 USD | 61,290,000.00 USD | 0.00 USD | 421,680.00 USD | 611,360.00 USD | 993,120.00 USD |
| `7D` | `1.28` | 100,110,000.00 USD | 100,110,000.00 USD | 0.00 USD | 639,910.00 USD | 1,380,000.00 USD | 1,570,000.00 USD |
| `1D` | `1.29` | 63,200,000.00 USD | 63,200,000.00 USD | 0.00 USD | 726,790.00 USD | 768,570.00 USD | 419,810.00 USD |
| `7D` | `1.29` | 101,270,000.00 USD | 101,270,000.00 USD | 0.00 USD | 944,150.00 USD | 223,080.00 USD | 0.00 USD |
| `1D` | `1.29` | 63,520,000.00 USD | 63,520,000.00 USD | 0.00 USD | 210,950.00 USD | 8,830.00 USD | 99,970.00 USD |
| `7D` | `1.29` | 101,390,000.00 USD | 101,390,000.00 USD | 0.00 USD | 48,320.00 USD | 7,050.00 USD | 60,830.00 USD |
| `1D` | `1.29` | 63,830,000.00 USD | 63,830,000.00 USD | 0.00 USD | 151,350.00 USD | 0.00 USD | 157,060.00 USD |
| `7D` | `1.29` | 103,670,000.00 USD | 103,670,000.00 USD | 0.00 USD | 1,060,000.00 USD | 198,070.00 USD | 1,030,000.00 USD |
| `1D` | `1.29` | 66,720,000.00 USD | 66,720,000.00 USD | 0.00 USD | 546,160.00 USD | 195,000.00 USD | 2,140,000.00 USD |
| `7D` | `1.29` | 104,100,000.00 USD | 104,100,000.00 USD | 0.00 USD | 119,390.00 USD | 0.00 USD | 301,640.00 USD |
| `1D` | `1.29` | 72,670,000.00 USD | 72,670,000.00 USD | 0.00 USD | 1,810,000.00 USD | 645,070.00 USD | 3,500,000.00 USD |
| `7D` | `1.29` | 113,780,000.00 USD | 113,780,000.00 USD | 0.00 USD | 3,400,000.00 USD | 1,190,000.00 USD | 5,100,000.00 USD |
| `1D` | `1.30` | 74,920,000.00 USD | 74,920,000.00 USD | 0.00 USD | 518,910.00 USD | 633,000.00 USD | 1,100,000.00 USD |
| `7D` | `1.30` | 115,010,000.00 USD | 115,010,000.00 USD | 0.00 USD | 209,360.00 USD | 398,190.00 USD | 628,450.00 USD |
| `1D` | `1.30` | 75,640,000.00 USD | 75,640,000.00 USD | 0.00 USD | 321,680.00 USD | 109,620.00 USD | 291,610.00 USD |
| `7D` | `1.30` | 117,070,000.00 USD | 117,070,000.00 USD | 0.00 USD | 0.00 USD | 100,810.00 USD | 1,960,000.00 USD |
| `1D` | `1.30` | 77,770,000.00 USD | 77,770,000.00 USD | 0.00 USD | 443,890.00 USD | 332,000.00 USD | 1,350,000.00 USD |
| `7D` | `1.30` | 118,740,000.00 USD | 118,740,000.00 USD | 0.00 USD | 208,510.00 USD | 486,620.00 USD | 970,290.00 USD |
| `1D` | `1.30` | 79,490,000.00 USD | 79,490,000.00 USD | 0.00 USD | 587,440.00 USD | 869,380.00 USD | 260,610.00 USD |
| `7D` | `1.30` | 121,830,000.00 USD | 121,830,000.00 USD | 0.00 USD | 0.00 USD | 2,610,000.00 USD | 485,710.00 USD |
| `1D` | `1.30` | 80,760,000.00 USD | 80,760,000.00 USD | 0.00 USD | 304,340.00 USD | 649,450.00 USD | 322,840.00 USD |
| `7D` | `1.30` | 121,830,000.00 USD | 121,830,000.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD | 0.00 USD |
| `1D` | `1.31` | 83,050,000.00 USD | 83,050,000.00 USD | 0.00 USD | 689,960.00 USD | 147,250.00 USD | 1,450,000.00 USD |
| `7D` | `1.31` | 124,840,000.00 USD | 124,840,000.00 USD | 0.00 USD | 2,140,000.00 USD | 180,530.00 USD | 684,370.00 USD |
| `1D` | `1.31` | 86,290,000.00 USD | 86,290,000.00 USD | 0.00 USD | 1,130,000.00 USD | 330,750.00 USD | 1,770,000.00 USD |
| `7D` | `1.31` | 129,300,000.00 USD | 129,300,000.00 USD | 0.00 USD | 1,670,000.00 USD | 1,060,000.00 USD | 1,720,000.00 USD |
| `1D` | `1.31` | 88,610,000.00 USD | 88,610,000.00 USD | 0.00 USD | 876,130.00 USD | 869,070.00 USD | 573,540.00 USD |
| `7D` | `1.31` | 132,560,000.00 USD | 132,560,000.00 USD | 0.00 USD | 839,350.00 USD | 430,210.00 USD | 1,990,000.00 USD |
| `1D` | `1.31` | 91,540,000.00 USD | 91,540,000.00 USD | 0.00 USD | 1,320,000.00 USD | 664,910.00 USD | 944,450.00 USD |
| `7D` | `1.31` | 135,400,000.00 USD | 135,400,000.00 USD | 0.00 USD | 557,940.00 USD | 430,030.00 USD | 1,860,000.00 USD |
| `1D` | `1.31` | 94,470,000.00 USD | 94,470,000.00 USD | 0.00 USD | 372,630.00 USD | 454,810.00 USD | 2,110,000.00 USD |
| `7D` | `1.31` | 137,860,000.00 USD | 137,860,000.00 USD | 0.00 USD | 81,320.00 USD | 1,080,000.00 USD | 1,300,000.00 USD |
| `1D` | `1.32` | 100,980,000.00 USD | 100,980,000.00 USD | 0.00 USD | 1,320,000.00 USD | 1,640,000.00 USD | 3,550,000.00 USD |
| `7D` | `1.32` | 142,480,000.00 USD | 142,480,000.00 USD | 0.00 USD | 1,120,000.00 USD | 1,210,000.00 USD | 2,300,000.00 USD |
| `1D` | `1.32` | 106,060,000.00 USD | 106,060,000.00 USD | 0.00 USD | 1,740,000.00 USD | 836,160.00 USD | 2,510,000.00 USD |
| `7D` | `1.32` | 145,560,000.00 USD | 145,560,000.00 USD | 0.00 USD | 815,030.00 USD | 495,580.00 USD | 1,770,000.00 USD |
| `1D` | `1.32` | 109,560,000.00 USD | 109,560,000.00 USD | 0.00 USD | 1,650,000.00 USD | 652,780.00 USD | 1,200,000.00 USD |
| `7D` | `1.32` | 147,390,000.00 USD | 147,390,000.00 USD | 0.00 USD | 1,220,000.00 USD | 238,530.00 USD | 367,890.00 USD |
| `1D` | `1.32` | 114,150,000.00 USD | 114,150,000.00 USD | 0.00 USD | 1,990,000.00 USD | 583,250.00 USD | 2,020,000.00 USD |
| `7D` | `1.32` | 151,850,000.00 USD | 151,850,000.00 USD | 0.00 USD | 2,090,000.00 USD | 761,100.00 USD | 1,600,000.00 USD |
| `1D` | `1.32` | 116,150,000.00 USD | 116,150,000.00 USD | 0.00 USD | 1,080,000.00 USD | 287,760.00 USD | 625,660.00 USD |
| `7D` | `1.32` | 154,220,000.00 USD | 154,220,000.00 USD | 0.00 USD | 1,620,000.00 USD | 198,920.00 USD | 553,750.00 USD |
| `1D` | `1.33` | 118,680,000.00 USD | 118,680,000.00 USD | 0.00 USD | 664,210.00 USD | 621,550.00 USD | 1,240,000.00 USD |
| `7D` | `1.33` | 154,760,000.00 USD | 154,760,000.00 USD | 0.00 USD | 462,320.00 USD | 5,470.00 USD | 69,380.00 USD |
| `1D` | `1.33` | 120,920,000.00 USD | 120,920,000.00 USD | 0.00 USD | 683,490.00 USD | 159,620.00 USD | 1,400,000.00 USD |
| `7D` | `1.33` | 155,910,000.00 USD | 155,910,000.00 USD | 0.00 USD | 53,290.00 USD | 10,370.00 USD | 1,090,000.00 USD |
| `1D` | `1.33` | 123,770,000.00 USD | 123,770,000.00 USD | 0.00 USD | 848,670.00 USD | 298,810.00 USD | 1,700,000.00 USD |
| `7D` | `1.33` | 157,630,000.00 USD | 157,630,000.00 USD | 0.00 USD | 581,420.00 USD | 268,860.00 USD | 869,220.00 USD |
| `1D` | `1.33` | 126,160,000.00 USD | 126,160,000.00 USD | 0.00 USD | 1,040,000.00 USD | 190,550.00 USD | 1,160,000.00 USD |
| `7D` | `1.33` | 161,680,000.00 USD | 161,680,000.00 USD | 0.00 USD | 1,450,000.00 USD | 404,190.00 USD | 2,200,000.00 USD |
| `1D` | `1.33` | 128,240,000.00 USD | 128,240,000.00 USD | 0.00 USD | 859,040.00 USD | 354,550.00 USD | 872,500.00 USD |
| `7D` | `1.33` | 162,230,000.00 USD | 162,230,000.00 USD | 0.00 USD | 157,960.00 USD | 194,680.00 USD | 189,650.00 USD |
| `1D` | `1.34` | 130,220,000.00 USD | 130,220,000.00 USD | 0.00 USD | 829,900.00 USD | 219,260.00 USD | 927,340.00 USD |
| `7D` | `1.34` | 164,180,000.00 USD | 164,180,000.00 USD | 0.00 USD | 679,750.00 USD | 645,230.00 USD | 622,960.00 USD |
| `1D` | `1.34` | 132,490,000.00 USD | 132,490,000.00 USD | 0.00 USD | 1,010,000.00 USD | 331,250.00 USD | 927,070.00 USD |
| `7D` | `1.34` | 166,520,000.00 USD | 166,520,000.00 USD | 0.00 USD | 1,240,000.00 USD | 362,920.00 USD | 737,530.00 USD |
| `1D` | `1.34` | 134,360,000.00 USD | 134,360,000.00 USD | 0.00 USD | 892,570.00 USD | 387,310.00 USD | 592,540.00 USD |
| `7D` | `1.34` | 171,230,000.00 USD | 171,230,000.00 USD | 0.00 USD | 2,650,000.00 USD | 1,630,000.00 USD | 423,310.00 USD |
| `1D` | `1.34` | 137,610,000.00 USD | 137,610,000.00 USD | 0.00 USD | 1,410,000.00 USD | 693,530.00 USD | 1,150,000.00 USD |
| `7D` | `1.34` | 176,870,000.00 USD | 176,870,000.00 USD | 0.00 USD | 1,700,000.00 USD | 2,810,000.00 USD | 1,130,000.00 USD |
| `1D` | `1.34` | 139,380,000.00 USD | 139,380,000.00 USD | 0.00 USD | 584,400.00 USD | 416,300.00 USD | 762,530.00 USD |
| `7D` | `1.34` | 187,840,000.00 USD | 187,840,000.00 USD | 0.00 USD | 3,600,000.00 USD | 1,930,000.00 USD | 5,440,000.00 USD |
| `1D` | `1.35` | 140,420,000.00 USD | 140,420,000.00 USD | 0.00 USD | 355,660.00 USD | 234,160.00 USD | 458,570.00 USD |
| `7D` | `1.35` | 194,780,000.00 USD | 194,780,000.00 USD | 0.00 USD | 2,310,000.00 USD | 2,170,000.00 USD | 2,460,000.00 USD |
| `1D` | `1.35` | 141,910,000.00 USD | 141,910,000.00 USD | 0.00 USD | 749,450.00 USD | 149,380.00 USD | 591,590.00 USD |
| `7D` | `1.35` | 205,030,000.00 USD | 205,030,000.00 USD | 0.00 USD | 4,290,000.00 USD | 1,640,000.00 USD | 4,310,000.00 USD |
| `1D` | `1.35` | 142,940,000.00 USD | 142,940,000.00 USD | 0.00 USD | 471,590.00 USD | 126,450.00 USD | 425,480.00 USD |
| `7D` | `1.35` | 212,740,000.00 USD | 212,740,000.00 USD | 0.00 USD | 2,580,000.00 USD | 1,380,000.00 USD | 3,750,000.00 USD |
| `1D` | `1.35` | 144,360,000.00 USD | 144,360,000.00 USD | 0.00 USD | 597,310.00 USD | 312,930.00 USD | 511,530.00 USD |
| `7D` | `1.35` | 221,000,000.00 USD | 221,000,000.00 USD | 0.00 USD | 2,620,000.00 USD | 1,160,000.00 USD | 4,480,000.00 USD |
| `1D` | `1.35` | 145,150,000.00 USD | 145,150,000.00 USD | 0.00 USD | 142,180.00 USD | 79,810.00 USD | 571,660.00 USD |
| `7D` | `1.35` | 229,230,000.00 USD | 229,230,000.00 USD | 0.00 USD | 3,780,000.00 USD | 873,380.00 USD | 3,580,000.00 USD |
| `1D` | `1.36` | 146,090,000.00 USD | 146,090,000.00 USD | 0.00 USD | 391,410.00 USD | 17,220.00 USD | 531,190.00 USD |
| `7D` | `1.36` | 233,320,000.00 USD | 233,320,000.00 USD | 0.00 USD | 1,340,000.00 USD | 879,500.00 USD | 1,870,000.00 USD |
| `1D` | `1.36` | 146,430,000.00 USD | 146,430,000.00 USD | 0.00 USD | 213,710.00 USD | 42,480.00 USD | 84,480.00 USD |
| `7D` | `1.36` | 237,110,000.00 USD | 237,110,000.00 USD | 0.00 USD | 1,490,000.00 USD | 632,530.00 USD | 1,670,000.00 USD |
| `1D` | `1.36` | 147,180,000.00 USD | 147,180,000.00 USD | 0.00 USD | 277,960.00 USD | 149,990.00 USD | 316,940.00 USD |
| `7D` | `1.36` | 239,240,000.00 USD | 239,240,000.00 USD | 0.00 USD | 667,940.00 USD | 542,980.00 USD | 925,670.00 USD |
| `1D` | `1.36` | 147,520,000.00 USD | 147,520,000.00 USD | 0.00 USD | 171,250.00 USD | 2,700.00 USD | 166,760.00 USD |
| `7D` | `1.36` | 243,340,000.00 USD | 243,340,000.00 USD | 0.00 USD | 2,100,000.00 USD | 753,930.00 USD | 1,250,000.00 USD |
| `1D` | `1.36` | 147,630,000.00 USD | 147,630,000.00 USD | 0.00 USD | 0.00 USD | 26,460.00 USD | 88,450.00 USD |
| `7D` | `1.36` | 245,060,000.00 USD | 245,060,000.00 USD | 0.00 USD | 660,170.00 USD | 350,000.00 USD | 707,350.00 USD |
| `1D` | `1.37` | 147,960,000.00 USD | 147,960,000.00 USD | 0.00 USD | 53,740.00 USD | 104,420.00 USD | 171,320.00 USD |
| `7D` | `1.37` | 245,550,000.00 USD | 245,550,000.00 USD | 0.00 USD | 239,150.00 USD | 216,290.00 USD | 31,780.00 USD |
| `1D` | `1.37` | 148,160,000.00 USD | 148,160,000.00 USD | 0.00 USD | 126,110.00 USD | 2,890.00 USD | 68,720.00 USD |
| `7D` | `1.37` | 246,960,000.00 USD | 246,960,000.00 USD | 0.00 USD | 528,490.00 USD | 135,750.00 USD | 753,550.00 USD |
| `1D` | `1.37` | 148,360,000.00 USD | 148,360,000.00 USD | 0.00 USD | 7,080.00 USD | 67,780.00 USD | 119,540.00 USD |
| `7D` | `1.37` | 248,150,000.00 USD | 248,150,000.00 USD | 0.00 USD | 351,750.00 USD | 372,470.00 USD | 461,160.00 USD |
| `1D` | `1.37` | 148,560,000.00 USD | 148,560,000.00 USD | 0.00 USD | 75,340.00 USD | 1,780.00 USD | 126,860.00 USD |
| `7D` | `1.37` | 250,620,000.00 USD | 250,620,000.00 USD | 0.00 USD | 821,620.00 USD | 376,730.00 USD | 1,270,000.00 USD |
| `1D` | `1.38` | 148,840,000.00 USD | 148,840,000.00 USD | 0.00 USD | 120,880.00 USD | 30,080.00 USD | 125,000.00 USD |
| `7D` | `1.38` | 252,420,000.00 USD | 252,420,000.00 USD | 0.00 USD | 536,130.00 USD | 295,850.00 USD | 966,400.00 USD |
| `1D` | `1.38` | 149,230,000.00 USD | 149,230,000.00 USD | 0.00 USD | 93,260.00 USD | 50,590.00 USD | 254,190.00 USD |
| `7D` | `1.38` | 253,910,000.00 USD | 253,910,000.00 USD | 0.00 USD | 617,230.00 USD | 329,740.00 USD | 552,000.00 USD |
| `1D` | `1.38` | 149,710,000.00 USD | 149,710,000.00 USD | 0.00 USD | 195,140.00 USD | 100,700.00 USD | 182,120.00 USD |
| `7D` | `1.38` | 256,010,000.00 USD | 256,010,000.00 USD | 0.00 USD | 579,450.00 USD | 256,720.00 USD | 1,260,000.00 USD |
| `1D` | `1.38` | 149,790,000.00 USD | 149,790,000.00 USD | 0.00 USD | 12,100.00 USD | 65,520.00 USD | 0.00 USD |
| `7D` | `1.38` | 258,560,000.00 USD | 258,560,000.00 USD | 0.00 USD | 1,210,000.00 USD | 331,990.00 USD | 1,000,000.00 USD |
| `1D` | `1.38` | 149,960,000.00 USD | 149,960,000.00 USD | 0.00 USD | 0.00 USD | 1,250.00 USD | 166,310.00 USD |
| `7D` | `1.38` | 259,650,000.00 USD | 259,650,000.00 USD | 0.00 USD | 297,210.00 USD | 312,330.00 USD | 477,040.00 USD |
| `1D` | `1.39` | 150,010,000.00 USD | 150,010,000.00 USD | 0.00 USD | 53,700.00 USD | 0.00 USD | 3,090.00 USD |
| `7D` | `1.39` | 260,930,000.00 USD | 260,930,000.00 USD | 0.00 USD | 505,510.00 USD | 379,820.00 USD | 401,920.00 USD |
| `1D` | `1.39` | 150,070,000.00 USD | 150,070,000.00 USD | 0.00 USD | 0.00 USD | 46,750.00 USD | 5,020.00 USD |
| `7D` | `1.39` | 261,480,000.00 USD | 261,480,000.00 USD | 0.00 USD | 86,820.00 USD | 248,490.00 USD | 207,780.00 USD |
| `1D` | `1.39` | 150,160,000.00 USD | 150,160,000.00 USD | 0.00 USD | 40,370.00 USD | 49,560.00 USD | 0.00 USD |
| `7D` | `1.39` | 262,580,000.00 USD | 262,580,000.00 USD | 0.00 USD | 690,420.00 USD | 162,590.00 USD | 245,460.00 USD |
| `7D` | `1.39` | 262,740,000.00 USD | 262,740,000.00 USD | 0.00 USD | 128,420.00 USD | 39,430.00 USD | 0.00 USD |
| `1D` | `1.39` | 150,180,000.00 USD | 150,180,000.00 USD | 0.00 USD | 22,490.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `1.39` | 263,070,000.00 USD | 263,070,000.00 USD | 0.00 USD | 82,350.00 USD | 36,390.00 USD | 208,520.00 USD |
| `7D` | `1.40` | 263,240,000.00 USD | 263,240,000.00 USD | 0.00 USD | 145,140.00 USD | 22,660.00 USD | 0.00 USD |
| `7D` | `1.40` | 263,360,000.00 USD | 263,360,000.00 USD | 0.00 USD | 102,560.00 USD | 1,340.00 USD | 16,250.00 USD |
| `7D` | `1.40` | 263,370,000.00 USD | 263,370,000.00 USD | 0.00 USD | 0.00 USD | 996.88 USD | 5,880.00 USD |
| `7D` | `1.40` | 263,500,000.00 USD | 263,500,000.00 USD | 0.00 USD | 0.00 USD | 75,720.00 USD | 60,830.00 USD |
| `7D` | `1.40` | 263,620,000.00 USD | 263,620,000.00 USD | 0.00 USD | 94,530.00 USD | 21,520.00 USD | 1,960.00 USD |
| `7D` | `1.41` | 263,860,000.00 USD | 263,860,000.00 USD | 0.00 USD | 178,210.00 USD | 25,430.00 USD | 38,070.00 USD |
| `7D` | `1.41` | 264,030,000.00 USD | 264,030,000.00 USD | 0.00 USD | 71,870.00 USD | 20,210.00 USD | 74,090.00 USD |
| `7D` | `1.41` | 264,410,000.00 USD | 264,410,000.00 USD | 0.00 USD | 86,900.00 USD | 37,300.00 USD | 257,010.00 USD |
| `7D` | `1.41` | 265,050,000.00 USD | 265,050,000.00 USD | 0.00 USD | 198,150.00 USD | 157,090.00 USD | 290,590.00 USD |
| `7D` | `1.41` | 265,230,000.00 USD | 265,230,000.00 USD | 0.00 USD | 16,340.00 USD | 26,480.00 USD | 132,120.00 USD |
| `7D` | `1.42` | 265,850,000.00 USD | 265,850,000.00 USD | 0.00 USD | 161,890.00 USD | 72,870.00 USD | 388,670.00 USD |
| `7D` | `1.42` | 266,380,000.00 USD | 266,380,000.00 USD | 0.00 USD | 171,750.00 USD | 52,740.00 USD | 301,800.00 USD |
| `7D` | `1.42` | 267,400,000.00 USD | 267,400,000.00 USD | 0.00 USD | 352,520.00 USD | 254,030.00 USD | 414,730.00 USD |
| `7D` | `1.42` | 268,780,000.00 USD | 268,780,000.00 USD | 0.00 USD | 485,880.00 USD | 161,060.00 USD | 729,640.00 USD |
| `7D` | `1.42` | 269,400,000.00 USD | 269,400,000.00 USD | 0.00 USD | 209,000.00 USD | 165,260.00 USD | 251,820.00 USD |
| `7D` | `1.43` | 269,760,000.00 USD | 269,760,000.00 USD | 0.00 USD | 87,470.00 USD | 69,800.00 USD | 203,060.00 USD |
| `7D` | `1.43` | 270,780,000.00 USD | 270,780,000.00 USD | 0.00 USD | 367,140.00 USD | 62,300.00 USD | 588,430.00 USD |
| `7D` | `1.43` | 272,290,000.00 USD | 272,290,000.00 USD | 0.00 USD | 256,550.00 USD | 293,730.00 USD | 958,180.00 USD |
| `7D` | `1.43` | 273,680,000.00 USD | 273,680,000.00 USD | 0.00 USD | 502,470.00 USD | 173,270.00 USD | 712,600.00 USD |
| `7D` | `1.43` | 274,480,000.00 USD | 274,480,000.00 USD | 0.00 USD | 290,530.00 USD | 57,330.00 USD | 450,640.00 USD |
| `7D` | `1.44` | 275,010,000.00 USD | 275,010,000.00 USD | 0.00 USD | 215,800.00 USD | 23,880.00 USD | 290,120.00 USD |
| `7D` | `1.44` | 275,360,000.00 USD | 275,360,000.00 USD | 0.00 USD | 74,670.00 USD | 66,670.00 USD | 209,840.00 USD |
| `7D` | `1.44` | 275,810,000.00 USD | 275,810,000.00 USD | 0.00 USD | 154,760.00 USD | 55,000.00 USD | 245,840.00 USD |
| `7D` | `1.44` | 276,530,000.00 USD | 276,530,000.00 USD | 0.00 USD | 299,590.00 USD | 107,790.00 USD | 309,090.00 USD |
| `7D` | `1.44` | 276,900,000.00 USD | 276,900,000.00 USD | 0.00 USD | 69,670.00 USD | 106,400.00 USD | 197,340.00 USD |
| `7D` | `1.45` | 277,030,000.00 USD | 277,030,000.00 USD | 0.00 USD | 67,200.00 USD | 53,830.00 USD | 8,750.00 USD |
| `7D` | `1.45` | 277,160,000.00 USD | 277,160,000.00 USD | 0.00 USD | 7,480.00 USD | 1,230.00 USD | 116,410.00 USD |
| `7D` | `1.45` | 277,490,000.00 USD | 277,490,000.00 USD | 0.00 USD | 62,180.00 USD | 96,050.00 USD | 173,340.00 USD |
| `7D` | `1.45` | 278,100,000.00 USD | 278,100,000.00 USD | 0.00 USD | 190,550.00 USD | 38,510.00 USD | 381,070.00 USD |
| `7D` | `1.45` | 278,660,000.00 USD | 278,660,000.00 USD | 0.00 USD | 182,110.00 USD | 128,180.00 USD | 249,400.00 USD |
| `7D` | `1.46` | 279,120,000.00 USD | 279,120,000.00 USD | 0.00 USD | 130,690.00 USD | 67,850.00 USD | 262,740.00 USD |
| `7D` | `1.46` | 279,280,000.00 USD | 279,280,000.00 USD | 0.00 USD | 85,350.00 USD | 50,790.00 USD | 20,990.00 USD |
| `7D` | `1.46` | 279,750,000.00 USD | 279,750,000.00 USD | 0.00 USD | 119,110.00 USD | 55,850.00 USD | 296,470.00 USD |
| `7D` | `1.46` | 279,960,000.00 USD | 279,960,000.00 USD | 0.00 USD | 64,640.00 USD | 15,350.00 USD | 128,450.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `2.78B` | Total OI Tokens: `2,263,456,650.9 XRP`
  * 1h OI Change: `+1.72%` | 4h OI Change: `-2.79%` | 24h OI Change: `-3.97%`
  * Exchange Breakdown: Binance=`436.21M` | Bybit=`314.14M` | OKX=`91.88M` | Hyperliquid=`194.41M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-61.73K` | Last 24h: `81.98K` | Last 3d: `547.43K` | Last 7d: `1.15M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0078%` | **USDT OKX** | `-0.0072%` |
| **USDT Bybit** | `-0.0326%` | **USDT KuCoin** | `-0.0030%` |
| **USDT MEXC** | `0.0079%` | **USDT BingX** | `0.0081%` |
| **USDT Gate** | `-0.0008%` | **USDT Bitget** | `-0.0021%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `XRP` | `50.76%` | `49.24%` | `1.03` | 331,590,000.00 USD |
| `15M` | `Binance` | `46.91%` | `53.09%` | `0.88` | 121,050,000.00 USD |
| `15M` | `OKX` | `61.66%` | `38.34%` | `1.61` | 53,650,000.00 USD |
| `15M` | `Bybit` | `54.81%` | `45.19%` | `1.21` | 45,920,000.00 USD |
| `15M` | `KuCoin` | `52.83%` | `47.17%` | `1.12` | 1,080,000.00 USD |
| `15M` | `Gate` | `54.86%` | `45.14%` | `1.22` | 39,360,000.00 USD |
| `15M` | `Bitget` | `47.07%` | `52.93%` | `0.89` | 15,470,000.00 USD |
| `15M` | `BingX` | `59.05%` | `40.95%` | `1.44` | 2,860,000.00 USD |
| `15M` | `MEXC` | `49.11%` | `50.89%` | `0.97` | 6,930,000.00 USD |
| `15M` | `Bitunix` | `50.88%` | `49.12%` | `1.04` | 11,380,000.00 USD |
| `15M` | `Hyperliquid` | `32.94%` | `67.06%` | `0.49` | 9,400,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.62%` | `43.38%` | `1.31` | 485,470.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0.61%` | `99.39%` | `0.01` | 8,350,000.00 USD |
| `15M` | `HTX` | `72.38%` | `27.62%` | `2.62` | 8,010,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `48.97%` | `51.03%` | `0.96` | 1,280,000.00 USD |
| `15M` | `Bitfinex` | `28.57%` | `71.43%` | `0.40` | 228,470.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `54.34%` | `45.66%` | `1.19` | 4,160,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `39.53%` | `60.47%` | `0.65` | 1,970,000.00 USD |
| `15M` | `Whale Positions` | `46.91%` | `53.09%` | `0.88` | 121,050,000.00 USD |
| `15M` | `Global Accounts` | `50.76%` | `49.24%` | `1.03` | 331,590,000.00 USD |
| `1H` | `XRP` | `55.46%` | `44.54%` | `1.25` | 169,210,000.00 USD |
| `1H` | `Binance` | `53.27%` | `46.73%` | `1.14` | 53,070,000.00 USD |
| `1H` | `OKX` | `48.03%` | `51.97%` | `0.92` | 27,630,000.00 USD |
| `1H` | `Bybit` | `56.02%` | `43.98%` | `1.27` | 36,490,000.00 USD |
| `1H` | `KuCoin` | `61.23%` | `38.77%` | `1.58` | 1,630,000.00 USD |
| `1H` | `Gate` | `53.23%` | `46.77%` | `1.14` | 4,040,000.00 USD |
| `1H` | `Bitget` | `58.89%` | `41.11%` | `1.43` | 11,220,000.00 USD |
| `1H` | `BingX` | `54.4%` | `45.6%` | `1.19` | 2,690,000.00 USD |
| `1H` | `MEXC` | `63.79%` | `36.21%` | `1.76` | 16,100,000.00 USD |
| `1H` | `Bitunix` | `58.61%` | `41.39%` | `1.42` | 5,330,000.00 USD |
| `1H` | `Hyperliquid` | `58.51%` | `41.49%` | `1.41` | 5,790,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `58.78%` | `41.22%` | `1.43` | 1,010,000.00 USD |
| `1H` | `Crypto.com` | `45.32%` | `54.68%` | `0.83` | 216,290.00 USD |
| `1H` | `WhiteBIT` | `89.7%` | `10.3%` | `8.71` | 2,300,000.00 USD |
| `1H` | `HTX` | `47.13%` | `52.87%` | `0.89` | 131,140.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `31.76%` | `68.24%` | `0.47` | 14,440.00 USD |
| `1H` | `Aster` | `53.1%` | `46.9%` | `1.13` | 573,370.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `75.81%` | `24.19%` | `3.13` | 977,410.00 USD |
| `1H` | `Whale Positions` | `53.27%` | `46.73%` | `1.14` | 53,070,000.00 USD |
| `1H` | `Global Accounts` | `55.46%` | `44.54%` | `1.25` | 169,210,000.00 USD |
| `4H` | `XRP` | `49.08%` | `50.92%` | `0.96` | 18,970,000,000.00 USD |
| `4H` | `Binance` | `46.33%` | `53.67%` | `0.86` | 5,630,000,000.00 USD |
| `4H` | `OKX` | `46.77%` | `53.23%` | `0.88` | 3,330,000,000.00 USD |
| `4H` | `Bybit` | `48.99%` | `51.01%` | `0.96` | 1,270,000,000.00 USD |
| `4H` | `KuCoin` | `57.87%` | `42.13%` | `1.37` | 218,380,000.00 USD |
| `4H` | `Gate` | `47.8%` | `52.2%` | `0.92` | 1,830,000,000.00 USD |
| `4H` | `Bitget` | `49.49%` | `50.51%` | `0.98` | 715,500,000.00 USD |
| `4H` | `BingX` | `48.74%` | `51.26%` | `0.95` | 157,130,000.00 USD |
| `4H` | `MEXC` | `47.92%` | `52.08%` | `0.92` | 568,740,000.00 USD |
| `4H` | `Bitunix` | `49.67%` | `50.33%` | `0.99` | 630,530,000.00 USD |
| `4H` | `Hyperliquid` | `49.34%` | `50.66%` | `0.97` | 797,670,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.58%` | `44.42%` | `1.25` | 61,190,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `57.23%` | `42.77%` | `1.34` | 3,060,000,000.00 USD |
| `4H` | `HTX` | `51.06%` | `48.94%` | `1.04` | 149,930,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `51.08%` | `48.92%` | `1.04` | 123,150,000.00 USD |
| `4H` | `Bitfinex` | `25.71%` | `74.29%` | `0.35` | 12,550,000.00 USD |
| `4H` | `Kraken` | `39.3%` | `60.7%` | `0.65` | 60,220,000.00 USD |
| `4H` | `Aster` | `46.55%` | `53.45%` | `0.87` | 171,770,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `43.73%` | `56.27%` | `0.78` | 189,070,000.00 USD |
| `4H` | `Whale Positions` | `46.33%` | `53.67%` | `0.86` | 5,630,000,000.00 USD |
| `4H` | `Global Accounts` | `49.08%` | `50.92%` | `0.96` | 18,970,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `1.22` | `1.22` | `1.22` | `1.23` | `1.22` | 21,277,514.97 USD | 12,252,987.06 USD | 9,024,527.92 USD | 3,228,459.14 USD | `+15.17%` | `19B / 7S` |
| `5:00 UTC` | `1.21` | `1.21` | `1.21` | `1.22` | `1.21` | 13,086,923.36 USD | 5,315,021.50 USD | 7,771,901.86 USD | -2,456,880.36 USD | `-18.77%` | `9B / 24S` |
| `0:00 UTC` | `1.20` | `1.21` | `1.20` | `1.22` | `1.20` | 29,441,576.87 USD | 12,289,098.45 USD | 17,152,478.42 USD | -4,863,379.97 USD | `-16.52%` | `4B / 29S` |
| `5:00 UTC` | `1.21` | `1.21` | `1.21` | `1.21` | `1.20` | 15,449,446.82 USD | 7,233,070.64 USD | 8,216,376.18 USD | -983,305.53 USD | `-6.36%` | `6B / 10S` |
| `0:00 UTC` | `1.21` | `1.21` | `1.21` | `1.22` | `1.21` | 14,612,277.95 USD | 7,327,776.10 USD | 7,284,501.85 USD | 43,274.26 USD | `+0.30%` | `14B / 9S` |
| `5:00 UTC` | `1.22` | `1.22` | `1.22` | `1.22` | `1.21` | 14,809,006.05 USD | 8,905,687.74 USD | 5,903,318.31 USD | 3,002,369.44 USD | `+20.27%` | `27B / 5S` |
| `0:00 UTC` | `1.22` | `1.22` | `1.22` | `1.23` | `1.22` | 11,190,777.85 USD | 5,458,091.58 USD | 5,732,686.27 USD | -274,594.69 USD | `-2.45%` | `2B / 5S` |
| `5:00 UTC` | `1.22` | `1.22` | `1.22` | `1.22` | `1.22` | 9,740,915.81 USD | 4,726,774.90 USD | 5,014,140.91 USD | -287,366.00 USD | `-2.95%` | `9B / 19S` |
| `0:00 UTC` | `1.23` | `1.23` | `1.23` | `1.23` | `1.22` | 10,276,393.47 USD | 5,352,457.47 USD | 4,923,936.00 USD | 428,521.46 USD | `+4.17%` | `12B / 9S` |
| `5:00 UTC` | `1.23` | `1.23` | `1.23` | `1.23` | `1.22` | 1,976,366.08 USD | 1,085,956.92 USD | 890,409.16 USD | 195,547.76 USD | `+9.89%` | `8B / 6S` |

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
| `5m` | 283,480.00 USD | 168,260.00 USD | **`ACCUMULATION`** |
| `15m` | 1,190,000.00 USD | 1,940,000.00 USD | **`ACCUMULATION`** |
| `30m` | 1,530,000.00 USD | 7,800,000.00 USD | **`ACCUMULATION`** |
| `1h` | 4,050,000.00 USD | 5,010,000.00 USD | **`ACCUMULATION`** |
| `2h` | 991,280.00 USD | -9,560,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -19,880,000.00 USD | -32,940,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -28,220,000.00 USD | -36,380,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -57,780,000.00 USD | -144,920,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -68,500,000.00 USD | -161,140,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -67,430,000.00 USD | -159,320,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -137,290,000.00 USD | -245,510,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -609,260,000.00 USD | -1,320,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+283.48K` | 15m=`+1.19M` | 1h=`+4.05M` | 24h=`-67.43M`
* Futures Capital Netflows: 5m=`+168.26K` | 15m=`+1.94M` | 1h=`+5.01M` | 24h=`-159.32M`
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
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:00:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:48:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:49:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:49:58 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1.22` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1.20` (Risk Distance: `0.0213` pts)
  * +2.5R Take Profit: `1.27`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1.26` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.28` (Risk Distance: `0.0213` pts)
  * +2.5R Take Profit: `1.21`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1.24`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
