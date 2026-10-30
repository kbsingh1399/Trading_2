# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 16:21:39 IST` (`2026-10-30 10:51:39 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `96.81` | **Live Ask Quote**: `97.03` | **Mid Price**: `96.92`
- **Spread Points**: `22.00` | **Spread BPS**: `22.70 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `95.74` | VWAP Z-Score: `+0.40` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.5882` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.14` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `100.51` | Lower -3.00σ Band: `90.97`
  * Upper +2.51σ Band: `99.73` | Lower -2.51σ Band: `91.75`
  * Upper +2.01σ Band: `98.94` | Lower -2.01σ Band: `92.54`
  * Upper +2.00σ Band: `98.92` | Lower -2.00σ Band: `92.56`
  * Upper +1.28σ Band: `97.78` | Lower -1.28σ Band: `93.70`
  * Upper +1.00σ Band: `97.33` | Lower -1.00σ Band: `94.15`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`96.65` | EMA-20=`96.80` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`97.02` (Slope: `+0.0000`) | EMA-100=`97.82`
  * Institutional Anchors: EMA-144=`98.38` | EMA-200=`98.93` (Slope: `-0.2810`) | EMA-233=`99.14`
- **Range Boundaries**: 24H High=`102.93` | 24H Low=`91.86` | Weekly High=`103.63` | Weekly Low=`91.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `98.09` (Distance: `-1.16%`)
  * Point of Control (POC) = `96.89` (Distance: `+0.06%`)
  * Value Area Low (VAL) = `95.18` (Distance: `+1.86%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`101.56` | POC=`99.94` | VAL=`98.94`
  * Prior Day Extremes: PDH=`102.93` | PDL=`94.56` | PDC=`95.94`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`102.10` | Weekly POC=`100.92` | Weekly VAL=`99.51`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`97.84` | Low=`91.86`
  * London Session (08:00-16:00 UTC): High=`98.28` | Low=`95.96`
  * New York Session (13:00-21:00 UTC): High=`96.94` | Low=`95.96`
  * Initial Balance (First Hour): IB High=`98.28` | IB Low=`96.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `96.53` - `97.31`
  * Optimal Trade Entry (OTE 0.705): `97.11`
  * Structural Invalidation Anchor (0.786): `97.70`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `96.68` | `97.17` | `96.62` | `97.01` | `136,265` | 13,212,313.96 USD | 692,074.10 USD | `+5.24%` | -219,946,122.53 USD | `+0.69` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `97.01` | `97.15` | `96.94` | `97.15` | `49,772` | 4,830,964.69 USD | 416,064.96 USD | `+8.61%` | -219,530,057.56 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `97.15` | `97.23` | `97.07` | `97.08` | `22,333` | 2,169,697.02 USD | -128,998.84 USD | `-5.95%` | -219,659,056.40 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `96.84` | `96.84` | `96.30` | `96.45` | `188,985` | 18,229,950.06 USD | -194,651.12 USD | `-1.07%` | -222,170,038.43 USD | `+0.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `96.46` | `96.78` | `96.27` | `96.68` | `168,804` | 16,296,059.94 USD | 1,531,841.80 USD | `+9.40%` | -220,638,196.63 USD | `+1.28` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `96.68` | `97.23` | `96.62` | `97.10` | `208,522` | 20,227,741.03 USD | 986,472.00 USD | `+4.88%` | -219,651,724.63 USD | `+0.92` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `97.28` | `97.55` | `96.84` | `97.33` | `564,307` | 54,855,982.25 USD | -1,256,866.37 USD | `-2.29%` | -217,296,468.21 USD | `+0.46` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `97.34` | `97.44` | `96.68` | `96.83` | `564,041` | 54,709,052.00 USD | -2,626,000.84 USD | `-4.80%` | -219,922,469.04 USD | `+0.40` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `96.84` | `97.23` | `96.27` | `97.09` | `566,208` | 54,743,740.13 USD | 2,320,219.40 USD | `+4.24%` | -217,602,249.64 USD | `+0.69` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -192,935,382.59 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `97.28` | `3,030,040` | 295,921,356.18 USD | -16,839,868.63 USD | `-5.69%` | -209,775,251.22 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.28` | `97.55` | `96.27` | `97.08` | `1,694,507` | 164,304,019.93 USD | -1,566,536.31 USD | `-0.95%` | -211,341,787.53 USD | `+0.86` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `102.66` | `103.16` | `99.76` | `99.78` | `3,108,106` | 314,906,395.99 USD | -32,242,782.78 USD | `-10.24%` | -33,800,710.11 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.78` | `99.90` | `94.81` | `95.62` | `13,887,188` | 1,349,343,315.53 USD | -115,873,425.65 USD | `-8.59%` | -149,674,135.76 USD | `-1.37` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `95.62` | `97.23` | `92.25` | `97.19` | `7,753,327` | 731,973,529.17 USD | -43,261,246.83 USD | `-5.91%` | -192,935,382.59 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.20` | `98.54` | `96.72` | `97.28` | `3,030,040` | 295,921,356.18 USD | -16,839,868.63 USD | `-5.69%` | -209,775,251.22 USD | `+0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `97.28` | `97.55` | `96.27` | `97.08` | `1,694,507` | 164,304,019.93 USD | -1,566,536.31 USD | `-0.95%` | -211,341,787.53 USD | `+0.86` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`96.92`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `97.07` | `6.5600` | 636.81 USD | 201,684.87 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.07` | `5.1400` | 498.96 USD | 202,183.82 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.07` | `1.8500` | 179.58 USD | 202,363.41 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.07` | `0.1200` | 11.65 USD | 202,375.05 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.07` | `228.9200` | 22,221.04 USD | 224,596.09 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `97.08` | `175.1000` | 16,999.58 USD | 92,421.42 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `97.08` | `181.6600` | 17,636.28 USD | 110,057.70 USD | `3 orders` | `-0.01%` | `-` |
| `BID` | `97.08` | `298.6100` | 28,989.95 USD | 139,047.65 USD | `5 orders` | `-0.01%` | `-` |
| `BID` | `97.08` | `72.6100` | 7,048.98 USD | 146,096.63 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.08` | `180.1900` | 17,492.67 USD | 163,589.30 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `97.08` | `28.4400` | 2,760.90 USD | 166,350.20 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `97.08` | `72.6100` | 7,048.76 USD | 173,398.96 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.08` | `206.0100` | 19,998.63 USD | 193,397.58 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `97.08` | `78.8100` | 7,650.48 USD | 201,048.06 USD | `1 orders` | `-0.02%` | `-` |
| `ASK` | `97.09` | `10.0000` | 970.94 USD | 970.94 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `97.09` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 97.09` | `0.00%` | `-` |
| `BID` | `97.09` | `38.2400` | 3,712.84 USD | 3,712.84 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `97.09` | `38.2400` | 3,712.80 USD | 7,425.63 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `97.09` | `175.0800` | 16,998.34 USD | 24,423.98 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `97.09` | `175.0800` | 16,998.17 USD | 41,422.14 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `97.09` | `175.1000` | 16,999.93 USD | 58,422.08 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `97.09` | `175.1000` | 16,999.76 USD | 75,421.84 USD | `2 orders` | `-0.01%` | `-` |
| `ASK` | `97.10` | `44.2100` | 4,292.97 USD | 199,228.83 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.10` | `1896.5100` | 184,156.81 USD | 194,935.87 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.10` | `22.2500` | 2,160.52 USD | 10,779.06 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.10` | `78.7600` | 7,647.60 USD | 8,618.54 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.11` | `1132.2600` | 109,959.43 USD | 364,597.91 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `97.11` | `93.2800` | 9,058.79 USD | 254,638.48 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `97.11` | `137.8700` | 13,388.97 USD | 245,579.68 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `97.11` | `83.9700` | 8,154.49 USD | 232,190.72 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `97.11` | `0.6400` | 62.15 USD | 224,036.22 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `97.11` | `176.0600` | 17,097.01 USD | 223,974.07 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `97.11` | `78.7600` | 7,648.23 USD | 206,877.06 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `97.12` | `268.3300` | 26,061.01 USD | 975,604.66 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `97.12` | `83.9700` | 8,155.33 USD | 949,543.65 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `97.12` | `83.9700` | 8,155.25 USD | 941,388.31 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `97.12` | `716.3100` | 69,568.03 USD | 933,233.06 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `97.12` | `4356.1800` | 423,067.85 USD | 863,665.04 USD | `5 orders` | `+0.03%` | `-` |
| `ASK` | `97.12` | `535.8500` | 52,040.68 USD | 440,597.19 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `97.12` | `83.9700` | 8,154.91 USD | 388,556.51 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `97.12` | `162.7300` | 15,803.69 USD | 380,401.60 USD | `2 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:12:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `11` | `0x5b5d...c060` | `SHORT` | 67,580,038.34 USD | `696,120.13` | `94.33` | `97.07` | `308.95` | -1,911,772.12 USD | `-2.83%` | `7X Cross` |
| `19` | `0x9c6a...a4ed` | `LONG` | 53,403,063.03 USD | `550,087.69` | `80.86` | `97.07` | `68.18` | 8,924,076.64 USD | `+16.71%` | `20X Cross` |
| `48` | `0xb83d...6e36` | `SHORT` | 25,208,174.22 USD | `259,338.02` | `91.42` | `97.07` | `503.89` | -1,499,360.18 USD | `-5.95%` | `5X Cross` |
| `77` | `0x3dc9...54b0` | `SHORT` | 21,375,438.46 USD | `220,000.19` | `105.90` | `97.07` | `173.61` | 1,923,668.82 USD | `+9.00%` | `20X Cross` |
| `112` | `0x9c89...600e` | `LONG` | 18,407,442.85 USD | `189,472.50` | `115.21` | `97.07` | `34.98` | -3,421,572.41 USD | `-18.59%` | `20X Cross` |
| `117` | `0x4a20...3c26` | `LONG` | 17,476,200.00 USD | `180,000.00` | `106.43` | `97.07` | `69.71` | -1,682,078.71 USD | `-9.62%` | `20X Cross` |
| `146` | `0xecb6...2b00` | `SHORT` | 13,880,451.65 USD | `142,936.82` | `100.89` | `97.07` | `322.73` | 540,925.70 USD | `+3.90%` | `20X Cross` |
| `226` | `0xb581...6f4f` | `LONG` | 9,715,500.00 USD | `100,000.00` | `112.81` | `97.07` | `0.000000` | -1,565,209.14 USD | `-16.11%` | `3X Cross` |
| `227` | `0xc63a...a3cd` | `LONG` | 9,710,900.00 USD | `100,000.00` | `112.22` | `97.07` | `0.000000` | -1,511,208.97 USD | `-15.56%` | `20X Cross` |
| `290` | `0x645b...87b8` | `SHORT` | 8,048,390.04 USD | `82,879.96` | `103.90` | `97.07` | `355.60` | 563,080.19 USD | `+7.00%` | `20X Cross` |
| `294` | `0xdb3a...cf3b` | `LONG` | 7,956,156.72 USD | `81,851.78` | `106.04` | `97.07` | `46.13` | -723,590.14 USD | `-9.09%` | `4X Cross` |
| `309` | `0xe927...98ef` | `LONG` | 7,578,090.00 USD | `78,000.00` | `96.34` | `97.07` | `38.45` | 63,948.52 USD | `+0.84%` | `3X Cross` |
| `320` | `0xca49...53c8` | `SHORT` | 7,180,574.49 USD | `73,943.45` | `110.70` | `97.07` | `300.63` | 1,005,047.77 USD | `+14.00%` | `20X Cross` |
| `324` | `0x8ae4...3d60` | `LONG` | 7,005,362.57 USD | `72,180.05` | `111.72` | `97.07` | `11.49` | -1,058,797.66 USD | `-15.11%` | `10X Cross` |
| `330` | `0xa0b7...6165` | `SHORT` | 6,895,926.63 USD | `71,044.42` | `107.87` | `97.07` | `190.91` | 767,540.57 USD | `+11.13%` | `2X Cross` |
| `350` | `0xf517...c032` | `SHORT` | 6,580,753.03 USD | `67,778.53` | `84.64` | `97.07` | `222.43` | -843,721.87 USD | `-12.82%` | `20X Cross` |
| `413` | `0x7fda...17d1` | `SHORT` | 5,412,818.76 USD | `55,739.62` | `100.53` | `97.07` | `778.80` | 190,894.25 USD | `+3.53%` | `20X Cross` |
| `467` | `0x7e23...5a5a` | `LONG` | 4,719,163.99 USD | `48,564.56` | `105.17` | `97.07` | `57.00` | -388,405.17 USD | `-8.23%` | `5X Isolated` |
| `565` | `0xf899...88db` | `SHORT` | 3,952,747.20 USD | `40,716.81` | `88.40` | `97.07` | `109.10` | -353,474.33 USD | `-8.94%` | `20X Cross` |
| `574` | `0x2e2b...2fab` | `LONG` | 3,886,920.00 USD | `40,000.00` | `119.55` | `97.07` | `58.00` | -895,115.64 USD | `-23.03%` | `10X Cross` |
| `618` | `0x9c16...4a6f` | `SHORT` | 3,670,344.39 USD | `37,796.13` | `90.79` | `97.07` | `118.42` | -238,993.66 USD | `-6.51%` | `20X Cross` |
| `643` | `0x9946...0852` | `SHORT` | 3,505,233.12 USD | `36,099.58` | `110.82` | `97.07` | `140.30` | 495,353.27 USD | `+14.13%` | `20X Cross` |
| `644` | `0x27b8...12fc` | `LONG` | 3,502,877.90 USD | `36,085.73` | `110.86` | `97.07` | `23.96` | -497,467.36 USD | `-14.20%` | `10X Cross` |
| `668` | `0xa61c...66b9` | `LONG` | 3,365,476.69 USD | `34,662.76` | `102.73` | `97.07` | `0.000000` | -195,594.77 USD | `-5.81%` | `5X Cross` |
| `679` | `0x7a5a...0394` | `SHORT` | 3,291,719.13 USD | `33,900.30` | `99.28` | `97.07` | `124.77` | 73,742.77 USD | `+2.24%` | `10X Cross` |
| `681` | `0x3440...32c5` | `SHORT` | 3,276,511.57 USD | `33,744.03` | `95.02` | `97.07` | `169.41` | -70,111.62 USD | `-2.14%` | `20X Cross` |
| `732` | `0x96a7...79df` | `LONG` | 3,106,080.00 USD | `32,000.00` | `74.39` | `97.07` | `0.000000` | 725,674.15 USD | `+23.36%` | `20X Cross` |
| `772` | `0xbe19...8bd1` | `SHORT` | 2,956,859.10 USD | `30,451.69` | `97.62` | `97.07` | `758.28` | 15,687.53 USD | `+0.53%` | `3X Cross` |
| `773` | `0x482b...cae4` | `SHORT` | 2,942,845.47 USD | `30,310.49` | `88.03` | `97.07` | `154.70` | -274,597.19 USD | `-9.33%` | `20X Cross` |
| `784` | `0x610b...b613` | `LONG` | 2,879,282.68 USD | `29,634.14` | `101.23` | `97.07` | `70.39` | -120,716.67 USD | `-4.19%` | `3X Isolated` |
| `799` | `0x45d2...4029` | `SHORT` | 2,836,969.80 USD | `29,220.00` | `93.28` | `97.07` | `1543.43` | -111,193.82 USD | `-3.92%` | `20X Cross` |
| `844` | `0x458d...ab3b` | `LONG` | 2,658,533.24 USD | `27,385.03` | `117.17` | `97.07` | `81.08` | -550,129.28 USD | `-20.69%` | `3X Isolated` |
| `881` | `0x023a...2355` | `SHORT` | 2,520,134.52 USD | `25,956.15` | `101.16` | `97.07` | `294.32` | 105,495.36 USD | `+4.19%` | `20X Cross` |
| `901` | `0xfc27...9d9d` | `SHORT` | 2,467,552.06 USD | `25,415.10` | `100.27` | `97.07` | `841.61` | 80,760.87 USD | `+3.27%` | `20X Cross` |
| `912` | `0x051c...693c` | `LONG` | 2,440,557.05 USD | `25,139.70` | `89.76` | `97.07` | `45.50` | 183,995.72 USD | `+7.54%` | `20X Cross` |
| `948` | `0x638f...f5f0` | `LONG` | 2,330,160.00 USD | `24,000.00` | `136.71` | `97.07` | `51.28` | -950,808.54 USD | `-40.80%` | `20X Cross` |
| `992` | `0x7277...0b98` | `SHORT` | 2,211,038.85 USD | `22,770.74` | `99.32` | `97.07` | `157.25` | 50,564.90 USD | `+2.29%` | `20X Cross` |
| `999` | `0x7178...0854` | `LONG` | 2,187,902.82 USD | `22,545.24` | `110.94` | `97.07` | `39.60` | -313,241.66 USD | `-14.32%` | `10X Cross` |
| `1023` | `0x739c...cfb2` | `LONG` | 2,087,112.50 USD | `21,500.00` | `91.95` | `97.07` | `77.27` | 110,180.35 USD | `+5.28%` | `20X Cross` |
| `1095` | `0x7737...bf66` | `SHORT` | 1,978,864.16 USD | `20,384.06` | `102.94` | `97.07` | `983.32` | 119,477.73 USD | `+6.04%` | `10X Cross` |
| `1122` | `0xea00...a918` | `LONG` | 1,945,424.58 USD | `20,022.69` | `66.09` | `97.07` | `0.000000` | 622,115.98 USD | `+31.98%` | `20X Cross` |
| `1126` | `0x3fc5...c0c1` | `SHORT` | 1,943,460.00 USD | `20,000.00` | `98.28` | `97.07` | `182.72` | 22,099.84 USD | `+1.14%` | `20X Cross` |
| `1129` | `0x251f...6e5d` | `LONG` | 1,941,840.00 USD | `20,000.00` | `101.15` | `97.07` | `69.87` | -81,257.77 USD | `-4.18%` | `20X Cross` |
| `1131` | `0xbfc7...80b4` | `SHORT` | 1,941,580.00 USD | `20,000.00` | `85.98` | `97.07` | `173.65` | -222,045.50 USD | `-11.44%` | `20X Cross` |
| `1161` | `0x7160...d47c` | `LONG` | 1,886,895.64 USD | `19,434.10` | `105.03` | `97.07` | `75.92` | -154,325.65 USD | `-8.18%` | `20X Cross` |
| `1195` | `0xe097...d0fe` | `LONG` | 1,844,658.29 USD | `18,995.75` | `109.71` | `97.07` | `0.000000` | -239,338.60 USD | `-12.97%` | `20X Cross` |
| `1197` | `0x936c...bb0f` | `SHORT` | 1,843,823.16 USD | `18,988.91` | `105.57` | `97.07` | `523.32` | 160,864.53 USD | `+8.72%` | `20X Cross` |
| `1265` | `0xdf95...7d72` | `SHORT` | 1,728,790.74 USD | `17,802.58` | `104.53` | `97.07` | `2276.70` | 132,166.11 USD | `+7.65%` | `20X Cross` |
| `1269` | `0xe98b...8cd5` | `SHORT` | 1,712,151.88 USD | `17,622.89` | `187.95` | `97.07` | `262.04` | 1,600,068.84 USD | `+93.45%` | `20X Cross` |
| `1308` | `0xee2b...d67e` | `LONG` | 1,646,990.04 USD | `16,963.19` | `119.86` | `97.07` | `34.37` | -386,281.60 USD | `-23.45%` | `4X Cross` |
| `1322` | `0x123d...3bff` | `LONG` | 1,635,734.58 USD | `16,835.30` | `89.54` | `97.07` | `0.000000` | 128,293.33 USD | `+7.84%` | `10X Cross` |
| `1418` | `0x73d7...8be1` | `LONG` | 1,521,596.07 USD | `15,668.95` | `106.60` | `97.07` | `47.77` | -148,744.90 USD | `-9.78%` | `20X Cross` |
| `1434` | `0xc74a...ab93` | `LONG` | 1,508,298.95 USD | `15,536.82` | `64.06` | `97.07` | `54.89` | 513,070.11 USD | `+34.02%` | `5X Isolated` |
| `1468` | `0x5f10...d49d` | `LONG` | 1,456,500.00 USD | `15,000.00` | `96.35` | `97.07` | `70.94` | 11,198.84 USD | `+0.77%` | `20X Cross` |
| `1469` | `0xb322...d51f` | `LONG` | 1,456,362.52 USD | `14,999.82` | `102.98` | `97.07` | `44.84` | -88,364.78 USD | `-6.07%` | `20X Cross` |
| `1520` | `0xffb2...5ed6` | `LONG` | 1,407,647.06 USD | `14,504.05` | `117.89` | `97.07` | `85.26` | -302,257.65 USD | `-21.47%` | `20X Cross` |
| `1552` | `0x0d6a...ca57` | `LONG` | 1,380,502.80 USD | `14,206.65` | `110.41` | `97.07` | `91.60` | -188,087.56 USD | `-13.62%` | `5X Isolated` |
| `1732` | `0x69cc...14fd` | `SHORT` | 1,196,322.79 USD | `12,320.65` | `99.01` | `97.07` | `746.20` | 23,533.58 USD | `+1.97%` | `20X Cross` |
| `1764` | `0x2814...9b08` | `LONG` | 1,171,300.60 USD | `12,061.71` | `96.37` | `97.07` | `93.93` | 8,961.85 USD | `+0.77%` | `20X Isolated` |
| `1846` | `0x7808...6e70` | `SHORT` | 1,115,269.76 USD | `11,488.27` | `97.15` | `97.07` | `151.96` | 792.46 USD | `+0.07%` | `10X Cross` |
| `1858` | `0x2482...0e55` | `LONG` | 1,104,601.58 USD | `11,363.98` | `122.03` | `97.07` | `88.83` | -282,100.34 USD | `-25.54%` | `20X Isolated` |
| `1887` | `0x45db...86eb` | `LONG` | 1,077,909.90 USD | `11,100.00` | `110.69` | `97.07` | `69.28` | -150,772.00 USD | `-13.99%` | `5X Cross` |
| `1897` | `0xe863...8bb8` | `SHORT` | 1,066,476.27 USD | `10,978.19` | `97.06` | `97.07` | `251.18` | -903.08 USD | `-0.08%` | `20X Cross` |
| `1915` | `0x1d04...7c43` | `LONG` | 1,049,616.47 USD | `10,811.76` | `111.55` | `97.07` | `16.53` | -156,445.02 USD | `-14.90%` | `6X Cross` |
| `1929` | `0x2577...4897` | `LONG` | 1,039,296.45 USD | `10,702.37` | `96.58` | `97.07` | `0.000000` | 5,641.91 USD | `+0.54%` | `15X Cross` |
| `1937` | `0x34e6...8d74` | `LONG` | 1,036,264.71 USD | `10,671.15` | `101.19` | `97.07` | `15.56` | -43,509.93 USD | `-4.20%` | `20X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `100.53` | 2.01 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.00K USD at 100.5300 USD [API] | `2026-10-29 11:50:52` |
| `ANNOUNCEMENT` | `INFO` | `100.20` | 25,159.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 25.16K USD at 100.2000 USD [API] | `2026-10-29 12:11:24` |
| `ANNOUNCEMENT` | `INFO` | `100.30` | 44,051.76 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 44.05K USD at 100.3000 USD [API] | `2026-10-29 12:19:01` |
| `ANNOUNCEMENT` | `INFO` | `100.43` | 20,001.64 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 20.00K USD at 100.4300 USD [API] | `2026-10-29 12:29:43` |
| `ANNOUNCEMENT` | `INFO` | `100.68` | 22,375.12 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 22.38K USD at 100.6800 USD [API] | `2026-10-29 13:05:41` |
| `ANNOUNCEMENT` | `INFO` | `100.75` | 37,574.71 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 37.57K USD at 100.7500 USD [API] | `2026-10-29 13:18:58` |
| `ANNOUNCEMENT` | `INFO` | `100.48` | 36,538.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 36.54K USD at 100.4800 USD [API] | `2026-10-29 13:53:35` |
| `ANNOUNCEMENT` | `INFO` | `101.56` | 22,019.22 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 22.02K USD at 101.5600 USD [API] | `2026-10-29 17:38:34` |
| `ANNOUNCEMENT` | `INFO` | `101.01` | 23,419.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 23.42K USD at 101.0100 USD [API] | `2026-10-29 17:57:56` |
| `ANNOUNCEMENT` | `INFO` | `100.53` | 22,222.16 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale BUY: 22.22K USD at 100.5300 USD [API] | `2026-10-29 18:45:28` |
| `ANNOUNCEMENT` | `INFO` | `100.44` | 43.19 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.04K USD at 100.4400 USD [API] | `2026-10-29 18:31:45` |
| `ANNOUNCEMENT` | `INFO` | `101.79` | 242.26 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.24K USD at 101.7900 USD [API] | `2026-10-29 14:36:25` |
| `ANNOUNCEMENT` | `INFO` | `100.28` | 12.03 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.01K USD at 100.2800 USD [API] | `2026-10-29 19:14:24` |
| `ANNOUNCEMENT` | `INFO` | `100.23` | 223.51 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.22K USD at 100.2300 USD [API] | `2026-10-29 19:17:00` |
| `ANNOUNCEMENT` | `INFO` | `100.26` | 31,045.51 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 31.05K USD at 100.2600 USD [API] | `2026-10-29 19:19:43` |
| `ANNOUNCEMENT` | `INFO` | `100.03` | 29,424.82 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 29.42K USD at 100.0300 USD [API] | `2026-10-29 19:54:45` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`101.22` (Vol: 4,800,000.00 USD, Dist: `+4.42%`) | Long MP=`92.18` (Vol: 5,300,000.00 USD, Dist: `--4.91%`)
  * 48H Horizon: Short MP=`101.12` (Vol: 5,400,000.00 USD, Dist: `+4.32%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--4.93%`)
  * 3D Horizon: Short MP=`101.12` (Vol: 5,400,000.00 USD, Dist: `+4.32%`) | Long MP=`92.16` (Vol: 5,300,000.00 USD, Dist: `--4.93%`)
  * 7D Horizon: Short MP=`104.03` (Vol: 7,200,000.00 USD, Dist: `+7.32%`) | Long MP=`92.11` (Vol: 5,300,000.00 USD, Dist: `--4.98%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `19.45` | 18,100.00 USD | 123,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.85` | 18,240.00 USD | 123,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.95` | 15,960.00 USD | 123,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.25` | 1,720.00 USD | 123,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.55` | 4,790.00 USD | 123,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.65` | 748.56 USD | 123,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.05` | 496.78 USD | 123,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.15` | 242.38 USD | 123,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 1,410.00 USD | 123,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 161.73 USD | 123,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.75` | 4,630.00 USD | 123,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.95` | 1,100.00 USD | 123,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.25` | 445.00 USD | 123,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.45` | 133.58 USD | 123,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.55` | 4,850.00 USD | 123,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.95` | 1,260.00 USD | 123,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.05` | 1,130.00 USD | 123,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.15` | 243.31 USD | 123,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.35` | 772.65 USD | 123,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.45` | 2,060.00 USD | 123,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.55` | 249.63 USD | 123,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 1,560.00 USD | 123,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.15` | 18,400.00 USD | 123,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.25` | 1,130.00 USD | 123,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.85` | 896,730.00 USD | 123,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 1,250.00 USD | 122,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.15` | 2,010.00 USD | 122,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 5,470.00 USD | 122,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.45` | 146,460.00 USD | 122,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.65` | 9,870.00 USD | 121,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 3,200.00 USD | 121,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.05` | 5,210.00 USD | 121,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 136.24 USD | 121,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.35` | 217.65 USD | 121,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.55` | 13,590.00 USD | 121,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.65` | 745.67 USD | 121,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.85` | 1,260.00 USD | 121,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 11,460.00 USD | 121,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.15` | 25,480.00 USD | 121,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.35` | 1,050.00 USD | 121,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.75` | 153.18 USD | 121,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.85` | 5,980.00 USD | 121,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 747.10 USD | 121,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.05` | 2,740.00 USD | 121,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.35` | 6,200.00 USD | 121,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 113.80 USD | 121,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.55` | 107.06 USD | 121,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.95` | 665.85 USD | 121,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.05` | 1,770.00 USD | 121,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 87,450.00 USD | 121,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.25` | 10,680.00 USD | 121,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.35` | 843.52 USD | 121,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.45` | 59,610.00 USD | 121,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.55` | 21,130.00 USD | 121,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.65` | 131.94 USD | 121,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.95` | 239.60 USD | 121,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 3,010.00 USD | 121,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 47,340.00 USD | 121,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.45` | 4,240.00 USD | 121,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 11,190.00 USD | 121,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 233.86 USD | 121,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.85` | 35,990.00 USD | 121,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.05` | 820.65 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 870.33 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.35` | 16,400.00 USD | 121,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.45` | 1,020.00 USD | 121,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 2,560.00 USD | 121,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.05` | 164.74 USD | 121,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 496.01 USD | 121,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 39,620.00 USD | 121,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 1,830.00 USD | 121,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 6,290.00 USD | 121,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.05` | 5,410.00 USD | 121,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.55` | 4,570.00 USD | 121,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.85` | 5,750.00 USD | 121,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.95` | 499.40 USD | 121,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.55` | 1,490.00 USD | 121,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 486.14 USD | 121,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.75` | 8,680.00 USD | 121,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.85` | 878.92 USD | 121,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 6,650,000.00 USD | 121,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.15` | 598,290.00 USD | 114,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.65` | 99,830.00 USD | 114,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.75` | 4,990.00 USD | 114,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.95` | 557.94 USD | 114,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.05` | 5,070.00 USD | 114,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 3,500.00 USD | 114,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.25` | 619.51 USD | 114,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 4,410.00 USD | 114,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 2,840.00 USD | 114,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.55` | 58,350.00 USD | 114,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 748.97 USD | 114,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 546.85 USD | 114,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 1,660.00 USD | 114,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 624.29 USD | 114,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 1,310.00 USD | 114,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.25` | 4,280.00 USD | 114,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 19,600.00 USD | 114,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 41,870.00 USD | 114,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 2,430.00 USD | 114,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 5,170.00 USD | 114,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 1,630.00 USD | 114,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.15` | 2,120.00 USD | 114,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 287.63 USD | 114,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 3,000,000.00 USD | 114,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 18,330.00 USD | 111,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 83,250.00 USD | 110,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 2,280.00 USD | 110,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.85` | 4,270.00 USD | 110,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 2,310.00 USD | 110,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 50,470.00 USD | 110,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 195,750.00 USD | 110,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.25` | 1,320.00 USD | 110,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 7,860.00 USD | 110,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 886.44 USD | 110,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 1,560.00 USD | 110,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 159.00 USD | 110,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 1,270.00 USD | 110,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 1,510.00 USD | 110,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 4,490.00 USD | 110,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 632.73 USD | 110,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.35` | 921,810.00 USD | 110,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 62,790.00 USD | 109,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 9,470.00 USD | 109,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 5,150.00 USD | 109,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.75` | 1,070.00 USD | 109,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 3,690.00 USD | 109,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 9,790.00 USD | 109,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 21,580.00 USD | 109,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.15` | 2,950.00 USD | 109,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 723.94 USD | 109,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.35` | 148.45 USD | 109,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.55` | 130.88 USD | 109,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 770.11 USD | 109,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.75` | 836.67 USD | 109,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 3,450.00 USD | 109,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 50,440.00 USD | 109,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 54,040.00 USD | 109,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 8,680.00 USD | 109,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 785.00 USD | 109,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 6,030.00 USD | 109,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.55` | 8,210.00 USD | 109,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 44,250.00 USD | 109,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 460.85 USD | 109,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 2,150.00 USD | 109,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 25,040.00 USD | 109,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 749.95 USD | 109,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.55` | 360.16 USD | 109,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 322.14 USD | 109,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 68,830.00 USD | 109,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 764.31 USD | 109,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 242.16 USD | 109,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.05` | 671,960.00 USD | 109,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 110.82 USD | 108,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 9,160.00 USD | 108,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 4,600.00 USD | 108,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.45` | 10,180.00 USD | 108,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 17,870.00 USD | 108,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 410.78 USD | 108,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 1,790.00 USD | 108,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 477.20 USD | 108,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 6,510.00 USD | 108,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 179.70 USD | 108,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 1,140,000.00 USD | 108,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 37,590.00 USD | 107,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 9,480.00 USD | 107,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 7,940.00 USD | 107,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 12,760.00 USD | 107,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 9,450.00 USD | 107,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 37,220.00 USD | 107,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 400,220.00 USD | 107,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 2,170.00 USD | 106,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.45` | 11,610.00 USD | 106,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 2,050.00 USD | 106,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 542.07 USD | 106,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 537.62 USD | 106,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 140.55 USD | 106,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 3,260.00 USD | 106,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,570.00 USD | 106,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 3,700.00 USD | 106,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 3,880,000.00 USD | 106,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 106.04 USD | 103,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 99,280.00 USD | 103,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 56,650.00 USD | 102,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.85` | 10,290.00 USD | 102,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 14,010.00 USD | 102,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 6,300.00 USD | 102,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 3,980.00 USD | 102,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.35` | 5,630.00 USD | 102,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.45` | 2,930.00 USD | 102,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 97,530.00 USD | 102,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 9,260.00 USD | 102,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 58,330.00 USD | 102,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.85` | 14,260.00 USD | 102,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,250.00 USD | 102,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 5,800.00 USD | 102,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.25` | 21,190.00 USD | 102,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 585.29 USD | 102,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 15,560.00 USD | 102,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 777,020.00 USD | 102,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 9,200.00 USD | 101,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 12,330.00 USD | 101,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 42,210.00 USD | 101,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 22,720.00 USD | 101,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 9,450.00 USD | 101,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.15` | 4,070.00 USD | 101,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 8,170.00 USD | 101,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 7,880.00 USD | 101,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,800.00 USD | 101,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 2,400.00 USD | 101,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 843.83 USD | 101,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 12,800.00 USD | 101,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.85` | 20,000.00 USD | 101,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 12,540.00 USD | 101,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 13,390.00 USD | 101,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.15` | 3,170.00 USD | 101,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.25` | 10,390.00 USD | 101,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.35` | 5,990.00 USD | 101,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.45` | 4,540.00 USD | 101,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.55` | 137,150.00 USD | 101,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.65` | 7,720.00 USD | 101,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.75` | 24,770.00 USD | 101,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.85` | 1,290,000.00 USD | 101,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.95` | 469,860.00 USD | 100,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.15` | 99,630.00 USD | 99,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.25` | 1,550.00 USD | 99,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.35` | 1,030.00 USD | 99,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.45` | 4,780.00 USD | 99,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.55` | 11,110.00 USD | 99,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.65` | 2,630.00 USD | 99,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.75` | 30,770.00 USD | 99,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.85` | 9,370.00 USD | 99,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.95` | 5,320.00 USD | 99,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.05` | 5,120.00 USD | 99,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.15` | 7,910.00 USD | 99,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.25` | 24,120.00 USD | 99,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.35` | 2,930.00 USD | 99,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.45` | 34,210.00 USD | 99,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.55` | 44,230.00 USD | 99,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.65` | 334.24 USD | 99,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.75` | 3,600.00 USD | 99,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.85` | 27,060.00 USD | 99,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.95` | 69,370.00 USD | 99,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.05` | 350.78 USD | 99,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.15` | 19,470.00 USD | 99,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.25` | 5,360.00 USD | 99,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.35` | 30,500.00 USD | 99,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.45` | 753.04 USD | 99,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.55` | 62,540.00 USD | 99,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.65` | 3,290.00 USD | 99,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.75` | 15,140.00 USD | 99,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.85` | 858,930.00 USD | 99,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.95` | 151,380.00 USD | 98,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.05` | 722.26 USD | 98,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.15` | 1,550.00 USD | 98,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.25` | 1,900.00 USD | 98,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.35` | 9,920.00 USD | 98,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.45` | 8,670.00 USD | 98,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.55` | 16,200.00 USD | 98,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.65` | 11,490.00 USD | 98,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.75` | 232,500.00 USD | 98,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.85` | 3,530.00 USD | 97,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.95` | 7,050.00 USD | 97,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.05` | 9,470.00 USD | 97,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.15` | 37,740.00 USD | 97,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.25` | 17,970.00 USD | 97,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.35` | 22,200.00 USD | 97,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.45` | 17,880.00 USD | 97,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.55` | 355,340.00 USD | 97,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.65` | 3,700.00 USD | 97,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.75` | 9,410.00 USD | 97,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.85` | 12,000.00 USD | 97,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.95` | 2,780,000.00 USD | 97,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.05` | 3,620.00 USD | 94,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.15` | 5,740.00 USD | 94,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.25` | 1,270.00 USD | 94,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.35` | 8,840.00 USD | 94,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.45` | 19,200.00 USD | 94,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.55` | 1,390.00 USD | 94,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.65` | 12,790.00 USD | 94,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.75` | 3,130.00 USD | 94,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.85` | 27,330.00 USD | 94,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.95` | 32,460.00 USD | 94,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.05` | 4,710.00 USD | 94,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.15` | 124,360.00 USD | 94,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.25` | 6,670.00 USD | 94,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.35` | 28,010.00 USD | 94,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.45` | 463.51 USD | 94,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.55` | 49,380.00 USD | 94,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.65` | 11,370.00 USD | 94,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.75` | 195.64 USD | 94,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.85` | 6,130.00 USD | 94,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.95` | 62,270.00 USD | 94,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.05` | 3,780.00 USD | 94,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.15` | 15,720.00 USD | 94,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.25` | 46,730.00 USD | 94,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.35` | 28,850.00 USD | 94,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.45` | 4,230.00 USD | 94,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.55` | 14,560.00 USD | 94,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.65` | 18,840.00 USD | 94,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.75` | 22,540.00 USD | 94,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.85` | 28,800.00 USD | 94,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.95` | 38,660.00 USD | 94,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.05` | 19,630.00 USD | 93,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.15` | 2,470,000.00 USD | 93,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.25` | 745.29 USD | 91,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.35` | 3,930.00 USD | 91,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.45` | 38,080.00 USD | 91,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.55` | 8,210.00 USD | 91,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.65` | 711.42 USD | 91,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.75` | 6,520.00 USD | 91,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.85` | 28,890.00 USD | 91,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.95` | 55,160.00 USD | 91,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.05` | 4,230.00 USD | 91,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.15` | 4,870.00 USD | 91,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.25` | 4,630.00 USD | 91,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.35` | 10,170.00 USD | 91,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.45` | 20,920.00 USD | 91,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.55` | 121.87 USD | 91,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.65` | 18,880.00 USD | 91,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.75` | 21,030.00 USD | 91,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.85` | 21,260.00 USD | 91,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.95` | 22,840.00 USD | 91,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.05` | 9,000.00 USD | 91,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.15` | 25,540.00 USD | 91,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.25` | 1,800.00 USD | 91,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.35` | 20,700.00 USD | 91,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.45` | 20,480.00 USD | 91,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.55` | 140,760.00 USD | 91,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.65` | 41,340.00 USD | 91,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.75` | 3,140.00 USD | 90,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.85` | 31,310.00 USD | 90,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.95` | 56,830.00 USD | 90,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.05` | 26,110.00 USD | 90,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.15` | 82,440.00 USD | 90,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.25` | 14,770.00 USD | 90,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.45` | 1,360.00 USD | 90,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.55` | 49,290.00 USD | 90,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.65` | 18,490.00 USD | 90,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.75` | 32,540.00 USD | 90,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.85` | 36,960.00 USD | 90,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.95` | 5,480.00 USD | 90,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.15` | 160.38 USD | 90,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.25` | 5,090.00 USD | 90,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.35` | 875.16 USD | 90,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.45` | 7,090.00 USD | 90,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.55` | 579.66 USD | 90,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.65` | 1,740.00 USD | 90,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.75` | 18,230.00 USD | 90,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.85` | 396.23 USD | 90,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.95` | 209.79 USD | 90,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.05` | 247,180.00 USD | 90,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.15` | 12,510.00 USD | 90,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.25` | 16,400.00 USD | 90,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.35` | 57,020.00 USD | 90,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.45` | 102,230.00 USD | 90,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.55` | 10,470.00 USD | 90,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.65` | 60,250.00 USD | 90,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.75` | 5,370.00 USD | 90,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.85` | 1,300.00 USD | 90,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.95` | 108,010.00 USD | 90,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.05` | 6,280.00 USD | 89,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.25` | 15,490.00 USD | 89,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.35` | 1,810.00 USD | 89,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.45` | 10,990.00 USD | 89,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.55` | 56,020.00 USD | 89,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.65` | 68,880.00 USD | 89,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.75` | 12,210.00 USD | 89,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.85` | 6,010.00 USD | 89,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.95` | 937.30 USD | 89,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.05` | 42,080.00 USD | 89,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.15` | 46,040.00 USD | 89,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.25` | 10,190.00 USD | 89,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.35` | 23,070.00 USD | 89,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.45` | 22,930.00 USD | 89,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.55` | 53,160.00 USD | 89,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.65` | 160,750.00 USD | 89,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.75` | 11,150.00 USD | 89,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.85` | 32,710.00 USD | 89,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.05` | 259,070.00 USD | 89,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.15` | 37,490,000.00 USD | 89,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.25` | 13,820.00 USD | 51,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.35` | 2,860.00 USD | 51,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.45` | 18,450.00 USD | 51,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.55` | 3,260.00 USD | 51,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.65` | 6,610.00 USD | 51,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.75` | 162,300.00 USD | 51,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.85` | 3,260.00 USD | 51,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.95` | 45,480.00 USD | 51,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.05` | 145.70 USD | 51,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.15` | 24,130.00 USD | 51,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.25` | 3,140.00 USD | 51,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.35` | 772,100.00 USD | 51,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.45` | 14,370.00 USD | 50,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.55` | 10,540.00 USD | 50,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.65` | 3,660.00 USD | 50,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.75` | 214,850.00 USD | 50,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.85` | 8,470.00 USD | 50,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.95` | 8,800.00 USD | 50,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.05` | 13,110,000.00 USD | 50,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.15` | 4,120.00 USD | 37,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.25` | 73,790.00 USD | 37,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.35` | 2,170,000.00 USD | 37,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.45` | 116,720.00 USD | 34,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.65` | 45,480.00 USD | 34,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.75` | 9,720.00 USD | 34,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.85` | 29,230.00 USD | 34,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.95` | 4,430.00 USD | 34,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.05` | 47,400.00 USD | 34,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.15` | 69,870.00 USD | 34,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.25` | 6,300.00 USD | 34,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.35` | 15,590.00 USD | 34,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.45` | 38,820.00 USD | 34,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.55` | 43,440.00 USD | 34,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.65` | 4,370.00 USD | 34,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.75` | 28,720.00 USD | 34,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.85` | 2,670.00 USD | 34,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.95` | 12,860.00 USD | 34,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.05` | 1,120,000.00 USD | 34,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.15` | 131,520.00 USD | 33,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.25` | 260,000.00 USD | 33,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.35` | 1,480,000.00 USD | 32,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.45` | 5,600.00 USD | 31,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.55` | 13,960.00 USD | 31,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.65` | 33,720.00 USD | 31,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.75` | 3,690.00 USD | 31,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.85` | 190,300.00 USD | 31,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.95` | 5,600.00 USD | 31,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.05` | 46,010.00 USD | 31,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.15` | 18,520.00 USD | 31,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.25` | 26,730.00 USD | 31,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.35` | 21,920.00 USD | 31,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.45` | 5,350.00 USD | 31,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.55` | 14,850.00 USD | 31,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.65` | 37,850.00 USD | 31,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.75` | 70,280.00 USD | 31,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.85` | 12,370.00 USD | 30,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.95` | 40,040.00 USD | 30,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.05` | 25,190.00 USD | 30,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.15` | 21,430.00 USD | 30,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.25` | 26,460.00 USD | 30,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.35` | 40,040.00 USD | 30,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.45` | 22,440.00 USD | 30,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.55` | 15,670.00 USD | 30,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.65` | 1,030.00 USD | 30,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.75` | 123,840.00 USD | 30,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.85` | 127,450.00 USD | 30,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.95` | 18,090.00 USD | 30,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.05` | 40,670.00 USD | 30,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.25` | 287,360.00 USD | 30,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.35` | 18,360.00 USD | 30,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.45` | 38,660.00 USD | 30,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.55` | 35,050.00 USD | 30,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.65` | 130,250.00 USD | 30,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.75` | 60,640.00 USD | 29,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.85` | 2,880.00 USD | 29,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.95` | 29,830.00 USD | 29,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.15` | 4,370.00 USD | 29,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.25` | 4,340.00 USD | 29,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.35` | 45,780.00 USD | 29,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.45` | 1,720,000.00 USD | 29,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.55` | 37,610.00 USD | 28,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.65` | 55,910.00 USD | 28,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.75` | 5,060.00 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.85` | 135,520.00 USD | 28,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.95` | 33,790.00 USD | 27,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.05` | 80,420.00 USD | 27,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.15` | 1,740,000.00 USD | 27,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.25` | 25,180.00 USD | 26,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.35` | 5,650.00 USD | 25,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.45` | 59,150.00 USD | 25,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.55` | 18,400.00 USD | 25,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.65` | 3,590.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.75` | 9,870.00 USD | 25,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.85` | 83,670.00 USD | 25,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.95` | 15,390.00 USD | 25,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.05` | 21,520.00 USD | 25,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.15` | 63,710.00 USD | 25,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.25` | 70,740.00 USD | 25,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.35` | 55,060.00 USD | 25,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.45` | 26,080.00 USD | 25,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.55` | 5,740.00 USD | 25,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.65` | 32,860.00 USD | 25,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.75` | 52,670.00 USD | 25,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.85` | 62,050.00 USD | 25,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.95` | 1,370.00 USD | 25,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.05` | 6,490.00 USD | 25,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.15` | 128,420.00 USD | 25,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.25` | 47,570.00 USD | 25,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.35` | 17,490.00 USD | 25,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.45` | 7,750.00 USD | 25,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.55` | 6,720.00 USD | 25,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.65` | 45,420.00 USD | 25,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.75` | 194,630.00 USD | 25,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.85` | 30,690.00 USD | 24,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.95` | 34,220.00 USD | 24,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.05` | 40,880.00 USD | 24,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.15` | 34,810.00 USD | 24,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.25` | 79,220.00 USD | 24,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.35` | 107,240.00 USD | 24,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.45` | 11,550.00 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.55` | 16,640.00 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.65` | 103,370.00 USD | 24,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.75` | 52,190.00 USD | 24,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.85` | 439,180.00 USD | 24,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.95` | 25,480.00 USD | 23,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.05` | 2,230,000.00 USD | 23,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.15` | 89,300.00 USD | 21,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.25` | 22,790.00 USD | 21,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.35` | 50,550.00 USD | 21,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.45` | 68,010.00 USD | 21,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.55` | 190,680.00 USD | 21,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.65` | 20,720.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.75` | 18,650.00 USD | 21,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.85` | 35,560.00 USD | 21,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.95` | 153,360.00 USD | 21,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.05` | 123,570.00 USD | 21,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.15` | 804,530.00 USD | 20,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.25` | 43,580.00 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.35` | 158,370.00 USD | 20,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.45` | 218,740.00 USD | 19,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.55` | 18,190.00 USD | 19,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.65` | 184,500.00 USD | 19,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.75` | 7,950.00 USD | 19,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.85` | 58,610.00 USD | 19,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.95` | 23,300.00 USD | 19,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.05` | 107,130.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.15` | 44,400.00 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.25` | 160,260.00 USD | 19,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.35` | 274,420.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.40` | 168,540,000.00 USD | 168,540,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.45` | 54,190.00 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.55` | 20,900.00 USD | 18,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.60` | 168,500,000.00 USD | 168,500,000.00 USD | 0.00 USD | 0.00 USD | 9,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.65` | 130,030.00 USD | 18,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.75` | 81,510.00 USD | 18,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `83.80` | 168,490,000.00 USD | 168,490,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `83.85` | 11,040.00 USD | 18,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.95` | 98,980.00 USD | 18,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.05` | 113,380.00 USD | 18,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.15` | 66,390.00 USD | 18,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.20` | 168,480,000.00 USD | 168,480,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.25` | 49,770.00 USD | 18,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.35` | 397,070.00 USD | 18,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `84.40` | 168,460,000.00 USD | 168,460,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `84.45` | 85,770.00 USD | 17,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.55` | 5,900.00 USD | 17,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.65` | 1,330,000.00 USD | 17,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.75` | 1,040,000.00 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.85` | 95,670.00 USD | 15,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.95` | 162,040.00 USD | 15,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.05` | 15,920.00 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.15` | 7,430.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.20` | 168,430,000.00 USD | 168,430,000.00 USD | 0.00 USD | 218,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.25` | 618,490.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.35` | 20,970.00 USD | 14,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.40` | 168,210,000.00 USD | 168,210,000.00 USD | 0.00 USD | 12,950.00 USD | 192,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.45` | 66,690.00 USD | 14,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.55` | 11,200.00 USD | 14,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.60` | 168,010,000.00 USD | 168,010,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.65` | 43,620.00 USD | 14,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.75` | 9,640.00 USD | 14,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `85.80` | 167,820,000.00 USD | 167,820,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `85.85` | 73,630.00 USD | 14,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.95` | 360,250.00 USD | 14,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.05` | 138,200.00 USD | 13,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.15` | 51,580.00 USD | 13,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.20` | 167,560,000.00 USD | 167,560,000.00 USD | 0.00 USD | 12,130.00 USD | 199,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.25` | 52,570.00 USD | 13,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.35` | 3,860.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.40` | 167,350,000.00 USD | 167,350,000.00 USD | 0.00 USD | 311,220.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.45` | 188,400.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.55` | 30,640.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.65` | 190,730.00 USD | 13,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.70` | 179,340,000.00 USD | 179,340,000.00 USD | 5,980.00 USD | 367,860.00 USD | 71,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.75` | 35,070.00 USD | 13,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `86.80` | 167,030,000.00 USD | 167,030,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.85` | 75,910.00 USD | 13,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `86.90` | 178,900,000.00 USD | 178,900,000.00 USD | 327,130.00 USD | 382,120.00 USD | 268,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `86.95` | 152,510.00 USD | 13,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.00` | 166,880,000.00 USD | 166,880,000.00 USD | 271,000.00 USD | 183,160.00 USD | 310,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.05` | 30,500.00 USD | 12,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.10` | 177,920,000.00 USD | 177,920,000.00 USD | 121,630.00 USD | 119,130.00 USD | 301,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.15` | 20,150.00 USD | 12,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.20` | 166,120,000.00 USD | 166,120,000.00 USD | 8,850.00 USD | 6,510.00 USD | 6,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.25` | 93,120.00 USD | 12,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.30` | 177,380,000.00 USD | 177,380,000.00 USD | 192,810.00 USD | 242,640.00 USD | 278,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.35` | 72,050.00 USD | 12,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.40` | 166,090,000.00 USD | 166,090,000.00 USD | 248,310.00 USD | 225,130.00 USD | 288,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.45` | 151,520.00 USD | 12,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.50` | 176,660,000.00 USD | 176,660,000.00 USD | 156,730.00 USD | 252,960.00 USD | 93,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.55` | 128,170.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.60` | 165,330,000.00 USD | 165,330,000.00 USD | 0.00 USD | 275,130.00 USD | 421,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.65` | 105,970.00 USD | 12,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.70` | 176,160,000.00 USD | 176,160,000.00 USD | 8,600.00 USD | 250,230.00 USD | 264,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.75` | 30,700.00 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `87.80` | 164,640,000.00 USD | 164,640,000.00 USD | 0.00 USD | 413,150.00 USD | 11,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.85` | 66,830.00 USD | 12,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `87.90` | 175,640,000.00 USD | 175,640,000.00 USD | 134,550.00 USD | 427,430.00 USD | 935,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `87.95` | 162,530.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.00` | 164,210,000.00 USD | 164,210,000.00 USD | 0.00 USD | 12,070.00 USD | 251,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.05` | 62,640.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.10` | 174,140,000.00 USD | 174,140,000.00 USD | 59,290.00 USD | 35,690.00 USD | 230,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.15` | 21,240.00 USD | 12,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.20` | 163,950,000.00 USD | 163,950,000.00 USD | 9,900.00 USD | 20,610.00 USD | 28,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.25` | 74,760.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.30` | 173,810,000.00 USD | 173,810,000.00 USD | 116,980.00 USD | 275,350.00 USD | 274,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.35` | 26,970.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.40` | 163,890,000.00 USD | 163,890,000.00 USD | 0.00 USD | 237,870.00 USD | 335,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.45` | 129,160.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.50` | 173,150,000.00 USD | 173,150,000.00 USD | 86,840.00 USD | 99,900.00 USD | 1,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.55` | 251,040.00 USD | 11,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.65` | 96,310.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.70` | 172,960,000.00 USD | 172,960,000.00 USD | 204,330.00 USD | 124,180.00 USD | 413,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.75` | 168,880.00 USD | 11,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `88.80` | 163,320,000.00 USD | 163,320,000.00 USD | 241,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.85` | 1,060,000.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `88.90` | 172,220,000.00 USD | 172,220,000.00 USD | 143,140.00 USD | 62,660.00 USD | 216,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `88.95` | 36,710.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.00` | 163,070,000.00 USD | 163,070,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.05` | 40,570.00 USD | 10,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.10` | 171,790,000.00 USD | 171,790,000.00 USD | 160,900.00 USD | 83,520.00 USD | 30,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.15` | 160,460.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.20` | 162,140,000.00 USD | 162,140,000.00 USD | 8,180.00 USD | 10,750.00 USD | 315,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.25` | 31,740.00 USD | 9,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.30` | 171,520,000.00 USD | 171,520,000.00 USD | 221,290.00 USD | 284,680.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.35` | 42,390.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.40` | 161,810,000.00 USD | 161,810,000.00 USD | 697,470.00 USD | 26,220.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.45` | 511,650.00 USD | 9,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.50` | 171,000,000.00 USD | 171,000,000.00 USD | 4,870.00 USD | 50,620.00 USD | 273,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.55` | 64,040.00 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.60` | 160,920,000.00 USD | 160,920,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.65` | 22,300.00 USD | 9,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.70` | 170,670,000.00 USD | 170,670,000.00 USD | 133,580.00 USD | 30,600.00 USD | 425,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.75` | 134,870.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.80` | 159,240,000.00 USD | 159,240,000.00 USD | 425,950.00 USD | 318,390.00 USD | 314,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.85` | 56,560.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `89.90` | 170,080,000.00 USD | 170,080,000.00 USD | 129,660.00 USD | 91,010.00 USD | 140,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `89.95` | 77,970.00 USD | 9,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.00` | 158,190,000.00 USD | 158,190,000.00 USD | 374,600.00 USD | 647,410.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.05` | 38,720.00 USD | 9,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.10` | 169,720,000.00 USD | 169,720,000.00 USD | 1,080,000.00 USD | 892,740.00 USD | 574,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.15` | 77,700.00 USD | 9,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.20` | 156,070,000.00 USD | 156,070,000.00 USD | 1,250,000.00 USD | 590,390.00 USD | 735,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.25` | 44,640.00 USD | 8,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.30` | 167,170,000.00 USD | 167,170,000.00 USD | 661,900.00 USD | 443,900.00 USD | 346,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.35` | 77,210.00 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.40` | 153,490,000.00 USD | 153,490,000.00 USD | 796,240.00 USD | 68,740.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.45` | 41,960.00 USD | 8,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.50` | 165,720,000.00 USD | 165,720,000.00 USD | 633,950.00 USD | 482,080.00 USD | 876,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.55` | 85,260.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.60` | 151,930,000.00 USD | 151,930,000.00 USD | 1,040,000.00 USD | 1,010,000.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.65` | 116,340.00 USD | 8,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.70` | 163,730,000.00 USD | 163,730,000.00 USD | 628,630.00 USD | 803,190.00 USD | 373,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.75` | 84,390.00 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `90.80` | 148,320,000.00 USD | 148,320,000.00 USD | 1,210,000.00 USD | 1,200,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.85` | 74,130.00 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.90` | 161,920,000.00 USD | 161,920,000.00 USD | 673,680.00 USD | 420,760.00 USD | 105,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.95` | 39,770.00 USD | 8,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.00` | 144,430,000.00 USD | 144,430,000.00 USD | 1,190,000.00 USD | 609,900.00 USD | 810,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.05` | 413,880.00 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.10` | 160,720,000.00 USD | 160,720,000.00 USD | 436,270.00 USD | 732,110.00 USD | 485,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.15` | 282,790.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.20` | 141,820,000.00 USD | 141,820,000.00 USD | 2,280,000.00 USD | 868,420.00 USD | 638,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.25` | 44,170.00 USD | 7,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.30` | 159,070,000.00 USD | 159,070,000.00 USD | 150,320.00 USD | 221,290.00 USD | 445,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.35` | 14,960.00 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.40` | 138,040,000.00 USD | 138,040,000.00 USD | 1,180,000.00 USD | 1,030,000.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.45` | 347,480.00 USD | 7,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.50` | 158,250,000.00 USD | 158,250,000.00 USD | 850,930.00 USD | 781,420.00 USD | 650,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.55` | 1,210,000.00 USD | 7,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.60` | 134,210,000.00 USD | 134,210,000.00 USD | 500,280.00 USD | 1,020,000.00 USD | 872,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.65` | 1,430,000.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.70` | 155,970,000.00 USD | 155,970,000.00 USD | 268,750.00 USD | 463,180.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.75` | 237,560.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `91.80` | 131,820,000.00 USD | 131,820,000.00 USD | 932,400.00 USD | 797,110.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.85` | 71,640.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.90` | 154,070,000.00 USD | 154,070,000.00 USD | 1,280,000.00 USD | 813,050.00 USD | 665,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.95` | 35,980.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.00` | 129,400,000.00 USD | 129,400,000.00 USD | 681,440.00 USD | 656,110.00 USD | 990,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.05` | 168,710.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.10` | 151,310,000.00 USD | 151,310,000.00 USD | 2,310,000.00 USD | 2,670,000.00 USD | 545,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.15` | 328,990.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.20` | 127,070,000.00 USD | 127,070,000.00 USD | 2,870,000.00 USD | 1,110,000.00 USD | 289,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.25` | 168,960.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.30` | 145,780,000.00 USD | 145,780,000.00 USD | 720,590.00 USD | 799,660.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.35` | 369,030.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.40` | 122,810,000.00 USD | 122,810,000.00 USD | 550,500.00 USD | 843,410.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.45` | 117,820.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.50` | 142,830,000.00 USD | 142,830,000.00 USD | 1,300,000.00 USD | 712,060.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.55` | 5,040.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.60` | 119,880,000.00 USD | 119,880,000.00 USD | 98,670.00 USD | 880,990.00 USD | 1,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.65` | 15,170.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.70` | 138,280,000.00 USD | 138,280,000.00 USD | 1,080,000.00 USD | 1,130,000.00 USD | 1,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.75` | 2,060.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `92.80` | 117,210,000.00 USD | 117,210,000.00 USD | 463,730.00 USD | 2,370,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.85` | 23,420.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.90` | 134,400,000.00 USD | 134,400,000.00 USD | 3,420,000.00 USD | 2,100,000.00 USD | 2,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.95` | 5,840.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.00` | 112,730,000.00 USD | 112,730,000.00 USD | 549,700.00 USD | 550,690.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.05` | 31,450.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.10` | 126,020,000.00 USD | 126,020,000.00 USD | 2,660,000.00 USD | 3,410,000.00 USD | 2,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.15` | 4,940.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.20` | 109,600,000.00 USD | 109,600,000.00 USD | 1,090,000.00 USD | 670,930.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.25` | 63,970.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.30` | 117,770,000.00 USD | 117,770,000.00 USD | 3,040,000.00 USD | 3,230,000.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.35` | 11,060.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.40` | 105,710,000.00 USD | 105,710,000.00 USD | 611,840.00 USD | 2,660,000.00 USD | 1,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.45` | 8,060.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.50` | 110,050,000.00 USD | 110,050,000.00 USD | 3,020,000.00 USD | 2,340,000.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.55` | 19,360.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.60` | 101,000,000.00 USD | 101,000,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,640,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.65` | 939,260.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.70` | 102,340,000.00 USD | 102,340,000.00 USD | 640,730.00 USD | 3,170,000.00 USD | 962,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.75` | 10,870.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.80` | 98,060,000.00 USD | 98,060,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.85` | 11,870.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `93.90` | 97,560,000.00 USD | 97,560,000.00 USD | 1,610,000.00 USD | 967,780.00 USD | 1,420,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.95` | 1,140,000.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.00` | 92,810,000.00 USD | 92,810,000.00 USD | 2,660,000.00 USD | 1,780,000.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.05` | 4,190.00 USD | 829,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.10` | 93,560,000.00 USD | 93,560,000.00 USD | 768,990.00 USD | 1,310,000.00 USD | 2,670,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.15` | 29,210.00 USD | 825,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.20` | 86,170,000.00 USD | 86,170,000.00 USD | 24,740.00 USD | 962,410.00 USD | 2,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.25` | 8,860.00 USD | 796,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.30` | 88,810,000.00 USD | 88,810,000.00 USD | 2,300,000.00 USD | 1,250,000.00 USD | 533,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.35` | 7,960.00 USD | 787,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.40` | 82,430,000.00 USD | 82,430,000.00 USD | 0.00 USD | 515,800.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.45` | 155,730.00 USD | 779,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.50` | 84,730,000.00 USD | 84,730,000.00 USD | 1,150,000.00 USD | 1,270,000.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.55` | 80,330.00 USD | 623,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.60` | 81,900,000.00 USD | 81,900,000.00 USD | 560,570.00 USD | 0.00 USD | 432,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.65` | 25,780.00 USD | 543,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.70` | 81,270,000.00 USD | 81,270,000.00 USD | 1,550,000.00 USD | 598,120.00 USD | 461,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.75` | 82,080.00 USD | 517,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.80` | 80,910,000.00 USD | 80,910,000.00 USD | 2,090,000.00 USD | 152,290.00 USD | 3,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.85` | 33,620.00 USD | 435,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `94.90` | 78,660,000.00 USD | 78,660,000.00 USD | 3,530,000.00 USD | 893,010.00 USD | 1,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.95` | 33,760.00 USD | 401,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.00` | 75,240,000.00 USD | 75,240,000.00 USD | 3,420,000.00 USD | 4,770,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.05` | 57,160.00 USD | 367,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.10` | 72,260,000.00 USD | 72,260,000.00 USD | 3,400,000.00 USD | 1,780,000.00 USD | 960,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.15` | 20,130.00 USD | 310,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.20` | 65,470,000.00 USD | 65,470,000.00 USD | 2,420,000.00 USD | 317,900.00 USD | 17,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.25` | 42,330.00 USD | 290,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.30` | 66,120,000.00 USD | 66,120,000.00 USD | 1,840,000.00 USD | 1,790,000.00 USD | 3,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.35` | 7,350.00 USD | 248,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.40` | 62,710,000.00 USD | 62,710,000.00 USD | 2,080,000.00 USD | 2,620,000.00 USD | 4,590,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.45` | 23,550.00 USD | 240,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.50` | 58,710,000.00 USD | 58,710,000.00 USD | 833,050.00 USD | 1,690,000.00 USD | 2,370,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.55` | 44,090.00 USD | 217,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.60` | 53,420,000.00 USD | 53,420,000.00 USD | 3,820,000.00 USD | 7,040,000.00 USD | 5,460,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.65` | 92,490.00 USD | 173,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.70` | 53,810,000.00 USD | 53,810,000.00 USD | 2,410,000.00 USD | 2,670,000.00 USD | 6,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.75` | 49,860.00 USD | 80,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `95.80` | 37,110,000.00 USD | 37,110,000.00 USD | 3,400,000.00 USD | 93,510.00 USD | 2,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.85` | 30,710.00 USD | 30,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.90` | 42,260,000.00 USD | 42,260,000.00 USD | 3,730,000.00 USD | 1,850,000.00 USD | 3,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.95` | 231.24 USD | 231.24 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `96.00` | 31,320,000.00 USD | 31,320,000.00 USD | 5,350,000.00 USD | 1,290,000.00 USD | 5,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.10` | 32,760,000.00 USD | 32,760,000.00 USD | 4,130,000.00 USD | 5,640,000.00 USD | 4,740,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.20` | 19,060,000.00 USD | 19,060,000.00 USD | 6,840,000.00 USD | 2,710,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.30` | 18,250,000.00 USD | 18,250,000.00 USD | 6,740,000.00 USD | 6,040,000.00 USD | 308,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.40` | 4,260,000.00 USD | 4,260,000.00 USD | 1,600,000.00 USD | 2,550,000.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.50` | 5,160,000.00 USD | 5,160,000.00 USD | 1,300,000.00 USD | 1,230,000.00 USD | 305,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.60` | 89,520.00 USD | 89,520.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.70` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 903,030.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `96.75` | 12,160.00 USD | 12,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `96.80` | 64,730.00 USD | 64,730.00 USD | 0.00 USD | 64,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.90` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.10` | 4,460.00 USD | 4,460.00 USD | 0.00 USD | 0.00 USD | 4,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.20` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 3,310,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.30` | 179,280.00 USD | 179,280.00 USD | 174,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.50` | 3,190,000.00 USD | 3,190,000.00 USD | 896,130.00 USD | 1,280,000.00 USD | 836,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.60` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 24,930.00 USD | 4,780,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.70` | 6,180,000.00 USD | 6,180,000.00 USD | 512,980.00 USD | 441,570.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `97.80` | 20,260,000.00 USD | 20,260,000.00 USD | 7,580,000.00 USD | 3,430,000.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `97.90` | 12,780,000.00 USD | 12,780,000.00 USD | 3,970,000.00 USD | 434,450.00 USD | 2,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.00` | 36,960,000.00 USD | 36,960,000.00 USD | 14,120,000.00 USD | 561,730.00 USD | 2,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.10` | 18,910,000.00 USD | 18,910,000.00 USD | 2,790,000.00 USD | 2,530,000.00 USD | 798,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.20` | 47,890,000.00 USD | 47,890,000.00 USD | 9,790,000.00 USD | 1,140,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.30` | 28,450,000.00 USD | 28,450,000.00 USD | 2,390,000.00 USD | 941,940.00 USD | 6,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.40` | 59,460,000.00 USD | 59,460,000.00 USD | 1,780,000.00 USD | 3,320,000.00 USD | 6,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.50` | 39,610,000.00 USD | 39,610,000.00 USD | 832,590.00 USD | 3,490,000.00 USD | 6,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.55` | 5,930.00 USD | 18,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `98.60` | 68,890,000.00 USD | 68,890,000.00 USD | 1,960,000.00 USD | 5,450,000.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `98.70` | 57,420,000.00 USD | 57,420,000.00 USD | 1,790,000.00 USD | 5,690,000.00 USD | 10,330,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `98.80` | 74,710,000.00 USD | 74,710,000.00 USD | 1,100,000.00 USD | 784,380.00 USD | 3,930,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.85` | 3,300.00 USD | 21,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `98.90` | 68,920,000.00 USD | 68,920,000.00 USD | 2,430,000.00 USD | 3,820,000.00 USD | 5,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `98.95` | 1,020.00 USD | 22,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.00` | 83,540,000.00 USD | 83,540,000.00 USD | 2,170,000.00 USD | 2,700,000.00 USD | 3,960,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.05` | 39,790.00 USD | 62,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.10` | 84,620,000.00 USD | 84,620,000.00 USD | 3,630,000.00 USD | 6,360,000.00 USD | 5,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.15` | 1,150,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.20` | 97,510,000.00 USD | 97,510,000.00 USD | 1,220,000.00 USD | 6,520,000.00 USD | 6,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.25` | 20,260.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.30` | 93,680,000.00 USD | 93,680,000.00 USD | 3,190,000.00 USD | 3,420,000.00 USD | 2,440,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.35` | 96,300.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.40` | 98,550,000.00 USD | 98,550,000.00 USD | 0.00 USD | 1,010,000.00 USD | 25,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.45` | 24,220.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.50` | 98,850,000.00 USD | 98,850,000.00 USD | 1,560,000.00 USD | 2,840,000.00 USD | 762,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.55` | 14,200.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.60` | 103,980,000.00 USD | 103,980,000.00 USD | 2,240,000.00 USD | 2,640,000.00 USD | 545,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.65` | 15,630.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.70` | 121,910,000.00 USD | 121,910,000.00 USD | 4,400,000.00 USD | 7,410,000.00 USD | 11,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.75` | 26,990.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `99.80` | 107,310,000.00 USD | 107,310,000.00 USD | 736,270.00 USD | 1,330,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.85` | 410.38 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `99.90` | 130,710,000.00 USD | 130,710,000.00 USD | 857,690.00 USD | 1,960,000.00 USD | 5,980,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `99.95` | 4,010.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.00` | 118,640,000.00 USD | 118,640,000.00 USD | 2,220,000.00 USD | 2,310,000.00 USD | 6,790,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.05` | 36,990.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.10` | 137,940,000.00 USD | 137,940,000.00 USD | 2,220,000.00 USD | 3,440,000.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.15` | 25,710.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.20` | 124,740,000.00 USD | 124,740,000.00 USD | 843,770.00 USD | 2,470,000.00 USD | 2,780,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.25` | 347,460.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.30` | 143,840,000.00 USD | 143,840,000.00 USD | 869,050.00 USD | 2,130,000.00 USD | 2,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.35` | 391,910.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.40` | 129,430,000.00 USD | 129,430,000.00 USD | 993,830.00 USD | 654,600.00 USD | 3,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.45` | 6,010.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.50` | 151,600,000.00 USD | 151,600,000.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 4,190,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.55` | 1,510.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.60` | 135,310,000.00 USD | 135,310,000.00 USD | 2,150,000.00 USD | 1,480,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.65` | 101,930.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.70` | 159,930,000.00 USD | 159,930,000.00 USD | 2,340,000.00 USD | 2,480,000.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.75` | 20,210.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `100.80` | 138,480,000.00 USD | 138,480,000.00 USD | 1,010,000.00 USD | 1,380,000.00 USD | 786,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.85` | 62,360.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.90` | 167,170,000.00 USD | 167,170,000.00 USD | 2,390,000.00 USD | 2,600,000.00 USD | 2,250,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `100.95` | 18,180.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.00` | 157,450,000.00 USD | 157,450,000.00 USD | 4,160,000.00 USD | 7,060,000.00 USD | 7,750,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.05` | 8,240.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.10` | 180,380,000.00 USD | 180,380,000.00 USD | 7,680,000.00 USD | 2,780,000.00 USD | 2,740,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.15` | 14,160.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.20` | 176,860,000.00 USD | 176,860,000.00 USD | 7,240,000.00 USD | 5,320,000.00 USD | 6,850,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.25` | 769.50 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.30` | 190,280,000.00 USD | 190,280,000.00 USD | 3,410,000.00 USD | 3,630,000.00 USD | 2,870,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.35` | 922.29 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.40` | 193,920,000.00 USD | 193,920,000.00 USD | 4,720,000.00 USD | 1,270,000.00 USD | 11,070,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.45` | 118.70 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.50` | 205,630,000.00 USD | 205,630,000.00 USD | 3,140,000.00 USD | 3,520,000.00 USD | 8,700,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.55` | 2,790.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `101.60` | 204,440,000.00 USD | 204,440,000.00 USD | 3,650,000.00 USD | 30,170.00 USD | 6,840,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.65` | 2,640.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.70` | 215,460,000.00 USD | 215,460,000.00 USD | 2,220,000.00 USD | 881,090.00 USD | 6,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.80` | 214,370,000.00 USD | 214,370,000.00 USD | 3,050,000.00 USD | 609,510.00 USD | 6,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.90` | 221,290,000.00 USD | 221,290,000.00 USD | 2,320,000.00 USD | 1,290,000.00 USD | 2,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.95` | 1,560.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.00` | 220,360,000.00 USD | 220,360,000.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | 2,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.05` | 4,280.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.10` | 227,740,000.00 USD | 227,740,000.00 USD | 2,960,000.00 USD | 1,440,000.00 USD | 2,050,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.20` | 227,080,000.00 USD | 227,080,000.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.25` | 1,890.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.30` | 231,730,000.00 USD | 231,730,000.00 USD | 1,670,000.00 USD | 1,260,000.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.40` | 232,390,000.00 USD | 232,390,000.00 USD | 2,340,000.00 USD | 304,350.00 USD | 2,660,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.50` | 236,050,000.00 USD | 236,050,000.00 USD | 1,510,000.00 USD | 785,070.00 USD | 2,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.60` | 234,850,000.00 USD | 234,850,000.00 USD | 1,450,000.00 USD | 979,270.00 USD | 33,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.65` | 1,070.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.70` | 237,940,000.00 USD | 237,940,000.00 USD | 1,110,000.00 USD | 661,840.00 USD | 125,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.75` | 3,340.00 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `102.80` | 242,940,000.00 USD | 242,940,000.00 USD | 7,780,000.00 USD | 23,810.00 USD | 286,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.85` | 654.13 USD | 2,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.90` | 242,470,000.00 USD | 242,470,000.00 USD | 1,510,000.00 USD | 1,530,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.95` | 4,150.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.00` | 259,880,000.00 USD | 259,880,000.00 USD | 12,270,000.00 USD | 394,420.00 USD | 4,270,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.05` | 1,060.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.10` | 247,440,000.00 USD | 247,440,000.00 USD | 2,380,000.00 USD | 1,360,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.15` | 14,800.00 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.20` | 272,550,000.00 USD | 272,550,000.00 USD | 11,620,000.00 USD | 140,550.00 USD | 913,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.25` | 206.50 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.30` | 249,260,000.00 USD | 249,260,000.00 USD | 334,720.00 USD | 717,010.00 USD | 766,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.35` | 385.50 USD | 2,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.40` | 287,120,000.00 USD | 287,120,000.00 USD | 11,050,000.00 USD | 233,330.00 USD | 3,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.45` | 3,300.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.50` | 255,840,000.00 USD | 255,840,000.00 USD | 1,770,000.00 USD | 1,090,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.60` | 305,510,000.00 USD | 305,510,000.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.65` | 4,360.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.70` | 260,550,000.00 USD | 260,550,000.00 USD | 1,370,000.00 USD | 720,260.00 USD | 2,620,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.75` | 261,050.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `103.80` | 317,890,000.00 USD | 317,890,000.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.85` | 14,630.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.90` | 264,370,000.00 USD | 264,370,000.00 USD | 1,370,000.00 USD | 1,640,000.00 USD | 804,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.95` | 827.44 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.00` | 344,600,000.00 USD | 344,600,000.00 USD | 10,830,000.00 USD | 7,160,000.00 USD | 8,710,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.05` | 1,110.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.10` | 269,290,000.00 USD | 269,290,000.00 USD | 2,020,000.00 USD | 724,740.00 USD | 2,180,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.15` | 1,180.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.20` | 366,630,000.00 USD | 366,630,000.00 USD | 8,520,000.00 USD | 7,230,000.00 USD | 6,280,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.25` | 40,840.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.30` | 271,960,000.00 USD | 271,960,000.00 USD | 1,000,000.00 USD | 971,040.00 USD | 696,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.35` | 14,580.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.40` | 383,810,000.00 USD | 383,810,000.00 USD | 5,100,000.00 USD | 3,710,000.00 USD | 8,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.45` | 9,560.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.50` | 275,530,000.00 USD | 275,530,000.00 USD | 1,310,000.00 USD | 1,030,000.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.55` | 575.03 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.60` | 401,560,000.00 USD | 401,560,000.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 7,020,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.65` | 401.86 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.70` | 281,290,000.00 USD | 281,290,000.00 USD | 1,690,000.00 USD | 982,920.00 USD | 3,090,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.75` | 3,620.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `104.80` | 418,950,000.00 USD | 418,950,000.00 USD | 5,170,000.00 USD | 4,410,000.00 USD | 7,820,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.85` | 31,470.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.90` | 282,760,000.00 USD | 282,760,000.00 USD | 486,940.00 USD | 283,560.00 USD | 703,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.95` | 125,660.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.00` | 435,120,000.00 USD | 435,120,000.00 USD | 5,730,000.00 USD | 4,110,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.05` | 578.83 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.10` | 284,600,000.00 USD | 284,600,000.00 USD | 299,230.00 USD | 436,680.00 USD | 1,110,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.15` | 13,330.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.20` | 445,780,000.00 USD | 445,780,000.00 USD | 5,340,000.00 USD | 2,800,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.25` | 2,110.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.30` | 284,800,000.00 USD | 284,800,000.00 USD | 94,380.00 USD | 96,460.00 USD | 2,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.35` | 6,840.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.40` | 454,000,000.00 USD | 454,000,000.00 USD | 1,570,000.00 USD | 3,170,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.45` | 531,450.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.50` | 285,410,000.00 USD | 285,410,000.00 USD | 245,610.00 USD | 180,000.00 USD | 187,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.55` | 4,180.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.60` | 462,420,000.00 USD | 462,420,000.00 USD | 3,700,000.00 USD | 2,270,000.00 USD | 2,450,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.65` | 1,950.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.70` | 285,630,000.00 USD | 285,630,000.00 USD | 65,040.00 USD | 150,210.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.75` | 4,160.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `105.80` | 471,230,000.00 USD | 471,230,000.00 USD | 2,690,000.00 USD | 2,620,000.00 USD | 3,510,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.85` | 91,370.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.90` | 286,680,000.00 USD | 286,680,000.00 USD | 177,140.00 USD | 685,100.00 USD | 187,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.95` | 592.26 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.00` | 476,380,000.00 USD | 476,380,000.00 USD | 1,970,000.00 USD | 1,050,000.00 USD | 2,130,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.05` | 33,380.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.10` | 288,150,000.00 USD | 288,150,000.00 USD | 706,860.00 USD | 459,510.00 USD | 305,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.20` | 485,280,000.00 USD | 485,280,000.00 USD | 3,820,000.00 USD | 2,560,000.00 USD | 2,520,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.25` | 1,970.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.30` | 289,350,000.00 USD | 289,350,000.00 USD | 316,990.00 USD | 488,800.00 USD | 393,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.35` | 256,690.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.40` | 491,360,000.00 USD | 491,360,000.00 USD | 2,430,000.00 USD | 2,180,000.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.45` | 216,090.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.50` | 290,270,000.00 USD | 290,270,000.00 USD | 326,070.00 USD | 292,550.00 USD | 306,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.55` | 219.49 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `106.60` | 496,200,000.00 USD | 496,200,000.00 USD | 1,330,000.00 USD | 1,250,000.00 USD | 2,260,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.65` | 6,680.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.70` | 292,690,000.00 USD | 292,690,000.00 USD | 697,200.00 USD | 284,770.00 USD | 1,440,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.80` | 500,850,000.00 USD | 500,850,000.00 USD | 999,190.00 USD | 927,000.00 USD | 2,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.85` | 479,350.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.90` | 293,520,000.00 USD | 293,520,000.00 USD | 156,730.00 USD | 336,790.00 USD | 330,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.95` | 131.55 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.00` | 505,000,000.00 USD | 505,000,000.00 USD | 527,980.00 USD | 1,180,000.00 USD | 2,430,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.05` | 14,600.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.10` | 294,580,000.00 USD | 294,580,000.00 USD | 97,170.00 USD | 368,740.00 USD | 596,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.15` | 3,060.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.20` | 506,090,000.00 USD | 506,090,000.00 USD | 230,020.00 USD | 507,570.00 USD | 352,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.25` | 34,950.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.30` | 294,910,000.00 USD | 294,910,000.00 USD | 60,260.00 USD | 159,710.00 USD | 110,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.35` | 766.48 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.40` | 295,360,000.00 USD | 295,360,000.00 USD | 0.00 USD | 41,740.00 USD | 408,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.40` | 507,370,000.00 USD | 507,370,000.00 USD | 0.00 USD | 576,040.00 USD | 709,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.45` | 32,580.00 USD | 4,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.55` | 221.55 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `107.60` | 508,000,000.00 USD | 508,000,000.00 USD | 213,520.00 USD | 12,070.00 USD | 406,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.80` | 508,840,000.00 USD | 508,840,000.00 USD | 499,550.00 USD | 31,020.00 USD | 305,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.85` | 143,340.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.95` | 8,330.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.00` | 509,420,000.00 USD | 509,420,000.00 USD | 5,950.00 USD | 237,870.00 USD | 335,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.05` | 1,080.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.15` | 1,150.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.20` | 509,700,000.00 USD | 509,700,000.00 USD | 0.00 USD | 205,080.00 USD | 74,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.25` | 162,440.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.35` | 3,470.00 USD | 5,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.40` | 510,190,000.00 USD | 510,190,000.00 USD | 487,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.45` | 108,080.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.55` | 381.01 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.60` | 510,370,000.00 USD | 510,370,000.00 USD | 17,470.00 USD | 167,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.65` | 5,050.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.80` | 511,300,000.00 USD | 511,300,000.00 USD | 350,210.00 USD | 286,220.00 USD | 287,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.85` | 3,980.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.95` | 3,170.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `109.00` | 511,580,000.00 USD | 511,580,000.00 USD | 0.00 USD | 0.00 USD | 286,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.05` | 356.59 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.25` | 4,450,000.00 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.35` | 20,440.00 USD | 9,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.45` | 426.86 USD | 9,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.55` | 356.04 USD | 9,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.65` | 38,750.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.75` | 408,730.00 USD | 10,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.85` | 459.17 USD | 10,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `109.95` | 301.26 USD | 10,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.05` | 14,790.00 USD | 10,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.15` | 33,240.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.25` | 226.01 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.35` | 143,450.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 376.63 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 203.41 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.85` | 28,970.00 USD | 10,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 4,450.00 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.15` | 1,710.00 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.35` | 390.84 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.45` | 841.45 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.55` | 892.40 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.65` | 199.85 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.75` | 169.86 USD | 10,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.85` | 15,880.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `111.95` | 223.90 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.05` | 1,640.00 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.15` | 291.59 USD | 10,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.35` | 262,980.00 USD | 10,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.45` | 5,670.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.55` | 1,070.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.65` | 707.44 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.75` | 118,640.00 USD | 10,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `112.85` | 108,760.00 USD | 10,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.05` | 406.98 USD | 10,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.15` | 37,800.00 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.25` | 698.75 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.35` | 4,970.00 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.45` | 3,360.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.55` | 17,470.00 USD | 10,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.65` | 4,360.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.75` | 107,800.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.85` | 2,470.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.95` | 21,840.00 USD | 11,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.05` | 31,740.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.15` | 253.41 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.25` | 2,370.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.45` | 3,830.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.65` | 3,430.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.05` | 569,550.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.15` | 1,100.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.25` | 1,260.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.45` | 879,040.00 USD | 12,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.55` | 167,330.00 USD | 12,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.65` | 5,970.00 USD | 12,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.75` | 14,920.00 USD | 12,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.85` | 289.62 USD | 12,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.05` | 5,930.00 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.25` | 6,270.00 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.35` | 4,960.00 USD | 12,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.55` | 2,040.00 USD | 12,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.65` | 113.15 USD | 12,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.85` | 10,520.00 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.05` | 156.85 USD | 12,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.15` | 89,950.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.35` | 11,610.00 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.55` | 635.95 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.75` | 10,360.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.95` | 1,890.00 USD | 12,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.25` | 9,280.00 USD | 12,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.45` | 30,080.00 USD | 12,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.55` | 7,700.00 USD | 12,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.65` | 4,480,000.00 USD | 17,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.75` | 309.94 USD | 17,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.85` | 5,750.00 USD | 17,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.25` | 240.88 USD | 17,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.35` | 58,320.00 USD | 17,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.55` | 8,970.00 USD | 17,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.75` | 261.06 USD | 17,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.85` | 485.39 USD | 17,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.15` | 31,040.00 USD | 17,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.25` | 97,590.00 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.35` | 145.62 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.45` | 968.42 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.55` | 1,190.00 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.65` | 1,110.00 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.85` | 123.27 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.95` | 13,290.00 USD | 17,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.05` | 60,700.00 USD | 17,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.15` | 316.20 USD | 17,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.45` | 42,460.00 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.55` | 5,940.00 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.75` | 105.92 USD | 17,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.05` | 56,150.00 USD | 17,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.15` | 169.79 USD | 17,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.25` | 4,210.00 USD | 17,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.45` | 899,680.00 USD | 18,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.65` | 116.52 USD | 18,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.25` | 471,560.00 USD | 19,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.35` | 2,330.00 USD | 19,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.45` | 1,960.00 USD | 19,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.75` | 124,610.00 USD | 19,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.95` | 36,200.00 USD | 19,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.05` | 586.76 USD | 19,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.15` | 121.67 USD | 19,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.25` | 23,360.00 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.35` | 775.94 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.55` | 4,760,000.00 USD | 24,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.65` | 675.60 USD | 24,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.75` | 5,330.00 USD | 24,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.95` | 49,090.00 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.05` | 208.83 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.15` | 6,260.00 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.35` | 5,320.00 USD | 24,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.45` | 590.87 USD | 24,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.55` | 4,610.00 USD | 24,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.65` | 1,560.00 USD | 24,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.75` | 1,930.00 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.95` | 110.84 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.05` | 810.50 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.15` | 470.54 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.35` | 4,350.00 USD | 24,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.45` | 4,880.00 USD | 24,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.55` | 403.69 USD | 24,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.65` | 30,830.00 USD | 24,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.85` | 3,870.00 USD | 24,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.05` | 2,030.00 USD | 24,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.15` | 389.08 USD | 24,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.35` | 29,060.00 USD | 24,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.45` | 138.92 USD | 24,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.55` | 4,460.00 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.65` | 4,840.00 USD | 24,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.75` | 20,800.00 USD | 24,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.85` | 388.66 USD | 24,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.95` | 12,330.00 USD | 24,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.05` | 116,190.00 USD | 24,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.15` | 1,000.00 USD | 24,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.35` | 195.09 USD | 24,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.65` | 788.62 USD | 24,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.75` | 18,730.00 USD | 24,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.85` | 32,440.00 USD | 24,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.15` | 55,570.00 USD | 24,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.25` | 32,310.00 USD | 24,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.35` | 35,060.00 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.45` | 730.10 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.55` | 910.74 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.65` | 700,970.00 USD | 25,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.75` | 2,210.00 USD | 25,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.85` | 490.83 USD | 25,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.25` | 145.88 USD | 25,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.45` | 343,340.00 USD | 25,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.85` | 3,180.00 USD | 25,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.95` | 2,070.00 USD | 25,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.05` | 188.71 USD | 25,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.25` | 1,560.00 USD | 25,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.35` | 14,210.00 USD | 25,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.45` | 219.52 USD | 25,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.65` | 17,640.00 USD | 25,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.85` | 3,210.00 USD | 25,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.05` | 1,710.00 USD | 25,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.15` | 33,680.00 USD | 25,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.45` | 8,530.00 USD | 25,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.55` | 196.17 USD | 25,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.65` | 240.10 USD | 25,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.75` | 136.73 USD | 25,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.85` | 49,280.00 USD | 25,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.05` | 1,700.00 USD | 25,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.15` | 8,440.00 USD | 25,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.25` | 1,330.00 USD | 25,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.65` | 156.37 USD | 25,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.75` | 151,200.00 USD | 25,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.95` | 503.65 USD | 25,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.05` | 12,620.00 USD | 25,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.15` | 2,510.00 USD | 25,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.25` | 11,590.00 USD | 25,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.95` | 395.40 USD | 25,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.45` | 14,560.00 USD | 25,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.65` | 415.09 USD | 25,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.85` | 9,680.00 USD | 26,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.95` | 504.37 USD | 26,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.25` | 49,000.00 USD | 26,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.45` | 1,500.00 USD | 26,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.55` | 8,700.00 USD | 26,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.65` | 1,110.00 USD | 26,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.95` | 34,240.00 USD | 26,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.05` | 836.00 USD | 26,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.15` | 809.19 USD | 26,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.85` | 68,930.00 USD | 26,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.05` | 1,270.00 USD | 26,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.15` | 41,450.00 USD | 26,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.25` | 45,220.00 USD | 26,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.35` | 15,400.00 USD | 26,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.45` | 9,370.00 USD | 26,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.65` | 4,160.00 USD | 26,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.75` | 2,360.00 USD | 26,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.85` | 9,290.00 USD | 26,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.15` | 552.43 USD | 26,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.35` | 253.62 USD | 26,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.55` | 494.01 USD | 26,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.75` | 4,870.00 USD | 26,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.95` | 394.66 USD | 26,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.05` | 1,800.00 USD | 26,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.35` | 127.72 USD | 26,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.45` | 4,870.00 USD | 26,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.55` | 8,030.00 USD | 26,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.65` | 4,210.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.95` | 1,940.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.05` | 3,710.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.15` | 67,420.00 USD | 26,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.35` | 5,100,000.00 USD | 31,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.45` | 247,540.00 USD | 31,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.55` | 2,770.00 USD | 31,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.65` | 1,220.00 USD | 31,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.75` | 2,250.00 USD | 31,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.85` | 1,950,000.00 USD | 33,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.95` | 211.51 USD | 33,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.25` | 3,470.00 USD | 33,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.35` | 71,180.00 USD | 33,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.45` | 23,250.00 USD | 33,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.55` | 42,080.00 USD | 33,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.65` | 87,970.00 USD | 33,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.75` | 368.30 USD | 33,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.15` | 1,460.00 USD | 33,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.35` | 22,260.00 USD | 33,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.45` | 790.41 USD | 33,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.55` | 103.36 USD | 33,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.65` | 2,840.00 USD | 33,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.75` | 1,710.00 USD | 33,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.85` | 1,480.00 USD | 33,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.95` | 285.02 USD | 33,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.05` | 3,750.00 USD | 33,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.25` | 34,630.00 USD | 34,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.55` | 599,880.00 USD | 34,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.65` | 1,240.00 USD | 34,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.15` | 1,760.00 USD | 34,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.25` | 1,090.00 USD | 34,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.45` | 28,990.00 USD | 34,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.55` | 1,270.00 USD | 34,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.75` | 1,340.00 USD | 34,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.85` | 5,990.00 USD | 34,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.95` | 106,560.00 USD | 34,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.15` | 88,760.00 USD | 34,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.25` | 22,210.00 USD | 34,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.35` | 7,330.00 USD | 34,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.45` | 1,400.00 USD | 34,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.55` | 74,780.00 USD | 34,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.65` | 587,730.00 USD | 35,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.75` | 493.08 USD | 35,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.85` | 442,670.00 USD | 35,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.95` | 3,340.00 USD | 35,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.05` | 166.17 USD | 35,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.15` | 30,890.00 USD | 36,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.35` | 169.45 USD | 36,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.45` | 204.96 USD | 36,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.55` | 1,690.00 USD | 36,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.65` | 237.72 USD | 36,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.85` | 510.08 USD | 36,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.15` | 102.22 USD | 36,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.45` | 163.29 USD | 36,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.55` | 344,780.00 USD | 36,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.65` | 78,850.00 USD | 36,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.75` | 99,350.00 USD | 36,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.85` | 520,980.00 USD | 37,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.55` | 116.65 USD | 37,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.65` | 1,410,000.00 USD | 38,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.85` | 123,060.00 USD | 38,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.95` | 234,200.00 USD | 38,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.05` | 2,930.00 USD | 38,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.15` | 642.64 USD | 38,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.35` | 105,250.00 USD | 38,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.55` | 4,560,000.00 USD | 43,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.15` | 3,530.00 USD | 43,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.25` | 2,370.00 USD | 43,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.45` | 8,830.00 USD | 43,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.95` | 1,920.00 USD | 43,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.25` | 1,860,000.00 USD | 45,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.35` | 2,040,000.00 USD | 47,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.45` | 47,900.00 USD | 47,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.65` | 615.18 USD | 47,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.75` | 1,570.00 USD | 47,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.85` | 13,500.00 USD | 47,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.05` | 1,060.00 USD | 47,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.25` | 239.07 USD | 47,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.35` | 2,300.00 USD | 47,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.45` | 47,510.00 USD | 47,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.65` | 8,340.00 USD | 47,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.85` | 995.41 USD | 47,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.15` | 292.89 USD | 47,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.25` | 2,340.00 USD | 47,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.45` | 4,240.00 USD | 47,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.75` | 363.66 USD | 47,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.05` | 1,500.00 USD | 47,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.25` | 3,020.00 USD | 47,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.55` | 267.55 USD | 47,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.75` | 118.37 USD | 47,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.15` | 326.35 USD | 47,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.25` | 7,810.00 USD | 47,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.35` | 197.00 USD | 47,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.45` | 4,900.00 USD | 47,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.65` | 1,170.00 USD | 47,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.15` | 49,270.00 USD | 47,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.65` | 654.25 USD | 47,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.75` | 92,600.00 USD | 47,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.25` | 299.09 USD | 47,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.65` | 237,980.00 USD | 47,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.05` | 44,690.00 USD | 47,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.45` | 2,410.00 USD | 47,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.65` | 1,760.00 USD | 47,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.75` | 656.57 USD | 47,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.85` | 3,640,000.00 USD | 51,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.15` | 683,000.00 USD | 52,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.25` | 498.38 USD | 52,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.35` | 7,070.00 USD | 52,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.55` | 449.54 USD | 52,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.75` | 434,020.00 USD | 52,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.95` | 28,210.00 USD | 52,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.05` | 255,020.00 USD | 53,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.15` | 102,630.00 USD | 53,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.25` | 4,120.00 USD | 53,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.35` | 21,430.00 USD | 53,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.55` | 410.34 USD | 53,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.75` | 142,240.00 USD | 53,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.95` | 144,610.00 USD | 53,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.05` | 405,950.00 USD | 53,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.15` | 5,970.00 USD | 53,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.45` | 86,540.00 USD | 53,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.95` | 19,080.00 USD | 53,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.85` | 786.48 USD | 53,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.95` | 207,900.00 USD | 54,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.15` | 198.18 USD | 54,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.65` | 3,420.00 USD | 54,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.05` | 149.45 USD | 54,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.15` | 996.90 USD | 54,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.25` | 14,070.00 USD | 54,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.45` | 1,380.00 USD | 54,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.75` | 685.34 USD | 54,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.95` | 3,230.00 USD | 54,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.65` | 115.68 USD | 54,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.75` | 1,890.00 USD | 54,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.05` | 122.68 USD | 54,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.15` | 111,420.00 USD | 54,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.25` | 629.25 USD | 54,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.35` | 19,740.00 USD | 54,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.65` | 325,850.00 USD | 54,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.45` | 5,720,000.00 USD | 60,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.55` | 847.75 USD | 60,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.05` | 6,000.00 USD | 60,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.75` | 447.37 USD | 60,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.45` | 111.44 USD | 60,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.75` | 182,360.00 USD | 60,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.05` | 20,480.00 USD | 60,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.45` | 51,730.00 USD | 60,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.85` | 1,190.00 USD | 60,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.25` | 36,050.00 USD | 60,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.35` | 284.29 USD | 60,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.45` | 16,540.00 USD | 60,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.85` | 695.40 USD | 60,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.95` | 25,850.00 USD | 60,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.05` | 28,180.00 USD | 60,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.15` | 104,490.00 USD | 60,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.25` | 245,010.00 USD | 61,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.35` | 205,490.00 USD | 61,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.55` | 18,550.00 USD | 61,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.75` | 146.79 USD | 61,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.35` | 119.24 USD | 61,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.75` | 263.62 USD | 61,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.05` | 2,960.00 USD | 61,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.15` | 350.54 USD | 61,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.25` | 625.69 USD | 61,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.35` | 19,940.00 USD | 61,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.55` | 38,840,000.00 USD | 100,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.95` | 106,170.00 USD | 100,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.05` | 470,750.00 USD | 100,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.45` | 12,000.00 USD | 100,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.65` | 3,550,000.00 USD | 104,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.95` | 78,300.00 USD | 104,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.05` | 25,750.00 USD | 104,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.35` | 33,140.00 USD | 104,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.45` | 2,440.00 USD | 104,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.95` | 2,830.00 USD | 104,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.25` | 1,040,000.00 USD | 105,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.85` | 4,500.00 USD | 105,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.95` | 2,030.00 USD | 105,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.05` | 45,030.00 USD | 105,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.25` | 3,730.00 USD | 105,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.35` | 1,340,000.00 USD | 106,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.55` | 148,410.00 USD | 107,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.75` | 72,300.00 USD | 107,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.15` | 5,020.00 USD | 107,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.25` | 18,120.00 USD | 107,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.55` | 254.17 USD | 107,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.75` | 727.00 USD | 107,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.05` | 91,030.00 USD | 107,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.15` | 3,990.00 USD | 107,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.75` | 1,370.00 USD | 107,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.25` | 1,680.00 USD | 107,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.35` | 993.65 USD | 107,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.45` | 9,540.00 USD | 107,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.95` | 165,230.00 USD | 107,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.25` | 13,750.00 USD | 107,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.45` | 2,770.00 USD | 107,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.65` | 7,830.00 USD | 107,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.85` | 2,190.00 USD | 107,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.15` | 2,450.00 USD | 107,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.65` | 232.69 USD | 107,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.85` | 1,560.00 USD | 107,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.05` | 3,820,000.00 USD | 111,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.55` | 231.92 USD | 111,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.65` | 29,110.00 USD | 111,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.75` | 813.51 USD | 111,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.95` | 1,450.00 USD | 111,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.15` | 257.24 USD | 111,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.25` | 456.09 USD | 111,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.55` | 284.33 USD | 111,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.65` | 117.58 USD | 111,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.75` | 1,010.00 USD | 111,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.85` | 189.85 USD | 111,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.95` | 284,930.00 USD | 111,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.15` | 148.32 USD | 111,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.45` | 118.08 USD | 111,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.65` | 278.35 USD | 111,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.95` | 13,570,000.00 USD | 125,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.15` | 191.15 USD | 125,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.25` | 118.58 USD | 125,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.55` | 62,850.00 USD | 125,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.95` | 322.48 USD | 125,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.65` | 9,300.00 USD | 125,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `19.45` | 123,140,000.00 USD | 0.00 USD | 18,100.00 USD | `-79.82%` | `930.46` |
| `Live` | `Long` | `19.85` | 123,120,000.00 USD | 0.00 USD | 18,240.00 USD | `-79.41%` | `919.00` |
| `Live` | `Long` | `19.95` | 123,110,000.00 USD | 0.00 USD | 15,960.00 USD | `-79.30%` | `800.00` |
| `Live` | `Long` | `20.25` | 123,090,000.00 USD | 0.00 USD | 1,720.00 USD | `-78.99%` | `85.17` |
| `Live` | `Long` | `20.55` | 123,090,000.00 USD | 0.00 USD | 4,790.00 USD | `-78.68%` | `233.31` |
| `Live` | `Long` | `20.65` | 123,080,000.00 USD | 0.00 USD | 748.56 USD | `-78.58%` | `36.25` |
| `Live` | `Long` | `21.05` | 123,080,000.00 USD | 0.00 USD | 496.78 USD | `-78.16%` | `23.60` |
| `Live` | `Long` | `21.15` | 123,080,000.00 USD | 0.00 USD | 242.38 USD | `-78.06%` | `11.46` |
| `Live` | `Long` | `21.35` | 123,080,000.00 USD | 0.00 USD | 1,410.00 USD | `-77.85%` | `65.89` |
| `Live` | `Long` | `21.45` | 123,080,000.00 USD | 0.00 USD | 161.73 USD | `-77.75%` | `7.54` |
| `Live` | `Long` | `21.75` | 123,080,000.00 USD | 0.00 USD | 4,630.00 USD | `-77.44%` | `212.70` |
| `Live` | `Long` | `21.95` | 123,080,000.00 USD | 0.00 USD | 1,100.00 USD | `-77.23%` | `50.00` |
| `Live` | `Long` | `22.25` | 123,080,000.00 USD | 0.00 USD | 445.00 USD | `-76.92%` | `20.00` |
| `Live` | `Long` | `22.45` | 123,070,000.00 USD | 0.00 USD | 133.58 USD | `-76.71%` | `5.95` |
| `Live` | `Long` | `22.55` | 123,070,000.00 USD | 0.00 USD | 4,850.00 USD | `-76.61%` | `215.00` |
| `Live` | `Long` | `22.95` | 123,070,000.00 USD | 0.00 USD | 1,260.00 USD | `-76.19%` | `54.95` |
| `Live` | `Long` | `23.05` | 123,070,000.00 USD | 0.00 USD | 1,130.00 USD | `-76.09%` | `49.01` |
| `Live` | `Long` | `23.15` | 123,070,000.00 USD | 0.00 USD | 243.31 USD | `-75.98%` | `10.51` |
| `Live` | `Long` | `23.35` | 123,070,000.00 USD | 0.00 USD | 772.65 USD | `-75.78%` | `33.09` |
| `Live` | `Long` | `23.45` | 123,070,000.00 USD | 0.00 USD | 2,060.00 USD | `-75.67%` | `88.01` |
| `Live` | `Long` | `23.55` | 123,060,000.00 USD | 0.00 USD | 249.63 USD | `-75.57%` | `10.60` |
| `Live` | `Long` | `23.75` | 123,060,000.00 USD | 0.00 USD | 1,560.00 USD | `-75.36%` | `65.63` |
| `Live` | `Long` | `24.15` | 123,060,000.00 USD | 0.00 USD | 18,400.00 USD | `-74.95%` | `762.03` |
| `Live` | `Long` | `24.25` | 123,040,000.00 USD | 0.00 USD | 1,130.00 USD | `-74.84%` | `46.58` |
| `Live` | `Long` | `24.85` | 123,040,000.00 USD | 0.00 USD | 896,730.00 USD | `-74.22%` | `36,085.73` |
| `Live` | `Long` | `25.05` | 122,150,000.00 USD | 0.00 USD | 1,250.00 USD | `-74.01%` | `50.00` |
| `Live` | `Long` | `25.15` | 122,140,000.00 USD | 0.00 USD | 2,010.00 USD | `-73.91%` | `80.00` |
| `Live` | `Long` | `25.25` | 122,140,000.00 USD | 0.00 USD | 5,470.00 USD | `-73.81%` | `216.71` |
| `Live` | `Long` | `25.45` | 122,140,000.00 USD | 0.00 USD | 146,460.00 USD | `-73.60%` | `5,754.63` |
| `Live` | `Long` | `25.65` | 121,990,000.00 USD | 0.00 USD | 9,870.00 USD | `-73.39%` | `384.80` |
| `Live` | `Long` | `25.95` | 121,980,000.00 USD | 0.00 USD | 3,200.00 USD | `-73.08%` | `123.26` |
| `Live` | `Long` | `26.05` | 121,980,000.00 USD | 0.00 USD | 5,210.00 USD | `-72.98%` | `200.00` |
| `Live` | `Long` | `26.25` | 121,970,000.00 USD | 0.00 USD | 136.24 USD | `-72.77%` | `5.19` |
| `Live` | `Long` | `26.35` | 121,970,000.00 USD | 0.00 USD | 217.65 USD | `-72.66%` | `8.26` |
| `Live` | `Long` | `26.55` | 121,970,000.00 USD | 0.00 USD | 13,590.00 USD | `-72.46%` | `512.00` |
| `Live` | `Long` | `26.65` | 121,960,000.00 USD | 0.00 USD | 745.67 USD | `-72.35%` | `27.98` |
| `Live` | `Long` | `26.85` | 121,960,000.00 USD | 0.00 USD | 1,260.00 USD | `-72.15%` | `47.02` |
| `Live` | `Long` | `26.95` | 121,960,000.00 USD | 0.00 USD | 11,460.00 USD | `-72.04%` | `425.19` |
| `Live` | `Long` | `27.15` | 121,950,000.00 USD | 0.00 USD | 25,480.00 USD | `-71.83%` | `938.38` |
| `Live` | `Long` | `27.35` | 121,920,000.00 USD | 0.00 USD | 1,050.00 USD | `-71.63%` | `38.33` |
| `Live` | `Long` | `27.75` | 121,920,000.00 USD | 0.00 USD | 153.18 USD | `-71.21%` | `5.52` |
| `Live` | `Long` | `27.85` | 121,920,000.00 USD | 0.00 USD | 5,980.00 USD | `-71.11%` | `214.80` |
| `Live` | `Long` | `27.95` | 121,910,000.00 USD | 0.00 USD | 747.10 USD | `-71.00%` | `26.73` |
| `Live` | `Long` | `28.05` | 121,910,000.00 USD | 0.00 USD | 2,740.00 USD | `-70.90%` | `97.63` |
| `Live` | `Long` | `28.35` | 121,910,000.00 USD | 0.00 USD | 6,200.00 USD | `-70.59%` | `218.55` |
| `Live` | `Long` | `28.45` | 121,900,000.00 USD | 0.00 USD | 113.80 USD | `-70.49%` | `4.00` |
| `Live` | `Long` | `28.55` | 121,900,000.00 USD | 0.00 USD | 107.06 USD | `-70.38%` | `3.75` |
| `Live` | `Long` | `28.95` | 121,900,000.00 USD | 0.00 USD | 665.85 USD | `-69.97%` | `23.00` |
| `Live` | `Long` | `29.05` | 121,900,000.00 USD | 0.00 USD | 1,770.00 USD | `-69.86%` | `60.81` |
| `Live` | `Long` | `29.15` | 121,900,000.00 USD | 0.00 USD | 87,450.00 USD | `-69.76%` | `3,000.00` |
| `Live` | `Long` | `29.25` | 121,810,000.00 USD | 0.00 USD | 10,680.00 USD | `-69.66%` | `365.00` |
| `Live` | `Long` | `29.35` | 121,800,000.00 USD | 0.00 USD | 843.52 USD | `-69.55%` | `28.74` |
| `Live` | `Long` | `29.45` | 121,800,000.00 USD | 0.00 USD | 59,610.00 USD | `-69.45%` | `2,023.99` |
| `Live` | `Long` | `29.55` | 121,740,000.00 USD | 0.00 USD | 21,130.00 USD | `-69.34%` | `715.00` |
| `Live` | `Long` | `29.65` | 121,720,000.00 USD | 0.00 USD | 131.94 USD | `-69.24%` | `4.45` |
| `Live` | `Long` | `29.95` | 121,720,000.00 USD | 0.00 USD | 239.60 USD | `-68.93%` | `8.00` |
| `Live` | `Long` | `30.05` | 121,720,000.00 USD | 0.00 USD | 3,010.00 USD | `-68.83%` | `100.04` |
| `Live` | `Long` | `30.15` | 121,720,000.00 USD | 0.00 USD | 47,340.00 USD | `-68.72%` | `1,570.00` |
| `Live` | `Long` | `30.45` | 121,670,000.00 USD | 0.00 USD | 4,240.00 USD | `-68.41%` | `139.36` |
| `Live` | `Long` | `30.55` | 121,670,000.00 USD | 0.00 USD | 11,190.00 USD | `-68.31%` | `366.29` |
| `Live` | `Long` | `30.65` | 121,650,000.00 USD | 0.00 USD | 233.86 USD | `-68.20%` | `7.63` |
| `Live` | `Long` | `30.85` | 121,650,000.00 USD | 0.00 USD | 35,990.00 USD | `-68.00%` | `1,166.55` |
| `Live` | `Long` | `31.05` | 121,620,000.00 USD | 0.00 USD | 820.65 USD | `-67.79%` | `26.43` |
| `Live` | `Long` | `31.15` | 121,620,000.00 USD | 0.00 USD | 870.33 USD | `-67.69%` | `27.94` |
| `Live` | `Long` | `31.35` | 121,620,000.00 USD | 0.00 USD | 16,400.00 USD | `-67.48%` | `523.23` |
| `Live` | `Long` | `31.45` | 121,600,000.00 USD | 0.00 USD | 1,020.00 USD | `-67.37%` | `32.37` |
| `Live` | `Long` | `31.95` | 121,600,000.00 USD | 0.00 USD | 2,560.00 USD | `-66.86%` | `80.00` |
| `Live` | `Long` | `32.05` | 121,600,000.00 USD | 0.00 USD | 164.74 USD | `-66.75%` | `5.14` |
| `Live` | `Long` | `32.25` | 121,600,000.00 USD | 0.00 USD | 496.01 USD | `-66.54%` | `15.38` |
| `Live` | `Long` | `32.35` | 121,600,000.00 USD | 0.00 USD | 39,620.00 USD | `-66.44%` | `1,224.78` |
| `Live` | `Long` | `32.45` | 121,560,000.00 USD | 0.00 USD | 1,830.00 USD | `-66.34%` | `56.43` |
| `Live` | `Long` | `32.85` | 121,550,000.00 USD | 0.00 USD | 6,290.00 USD | `-65.92%` | `191.33` |
| `Live` | `Long` | `33.05` | 121,550,000.00 USD | 0.00 USD | 5,410.00 USD | `-65.71%` | `163.78` |
| `Live` | `Long` | `33.55` | 121,540,000.00 USD | 0.00 USD | 4,570.00 USD | `-65.20%` | `136.10` |
| `Live` | `Long` | `33.85` | 121,540,000.00 USD | 0.00 USD | 5,750.00 USD | `-64.88%` | `169.92` |
| `Live` | `Long` | `33.95` | 121,530,000.00 USD | 0.00 USD | 499.40 USD | `-64.78%` | `14.71` |
| `Live` | `Long` | `34.55` | 121,530,000.00 USD | 0.00 USD | 1,490.00 USD | `-64.16%` | `43.14` |
| `Live` | `Long` | `34.65` | 121,530,000.00 USD | 0.00 USD | 486.14 USD | `-64.05%` | `14.03` |
| `Live` | `Long` | `34.75` | 121,530,000.00 USD | 0.00 USD | 8,680.00 USD | `-63.95%` | `249.89` |
| `Live` | `Long` | `34.85` | 121,520,000.00 USD | 0.00 USD | 878.92 USD | `-63.85%` | `25.22` |
| `Live` | `Long` | `35.05` | 121,520,000.00 USD | 0.00 USD | 6,650,000.00 USD | `-63.64%` | `189,675.12` |
| `Live` | `Long` | `35.15` | 114,870,000.00 USD | 0.00 USD | 598,290.00 USD | `-63.54%` | `17,021.03` |
| `Live` | `Long` | `35.65` | 114,270,000.00 USD | 0.00 USD | 99,830.00 USD | `-63.02%` | `2,800.26` |
| `Live` | `Long` | `35.75` | 114,170,000.00 USD | 0.00 USD | 4,990.00 USD | `-62.91%` | `139.48` |
| `Live` | `Long` | `35.95` | 114,170,000.00 USD | 0.00 USD | 557.94 USD | `-62.71%` | `15.52` |
| `Live` | `Long` | `36.05` | 114,170,000.00 USD | 0.00 USD | 5,070.00 USD | `-62.60%` | `140.61` |
| `Live` | `Long` | `36.15` | 114,160,000.00 USD | 0.00 USD | 3,500.00 USD | `-62.50%` | `96.83` |
| `Live` | `Long` | `36.25` | 114,160,000.00 USD | 0.00 USD | 619.51 USD | `-62.39%` | `17.09` |
| `Live` | `Long` | `36.35` | 114,160,000.00 USD | 0.00 USD | 4,410.00 USD | `-62.29%` | `121.32` |
| `Live` | `Long` | `36.45` | 114,150,000.00 USD | 0.00 USD | 2,840.00 USD | `-62.19%` | `77.86` |
| `Live` | `Long` | `36.55` | 114,150,000.00 USD | 0.00 USD | 58,350.00 USD | `-62.08%` | `1,596.58` |
| `Live` | `Long` | `36.75` | 114,090,000.00 USD | 0.00 USD | 748.97 USD | `-61.88%` | `20.38` |
| `Live` | `Long` | `36.85` | 114,090,000.00 USD | 0.00 USD | 546.85 USD | `-61.77%` | `14.84` |
| `Live` | `Long` | `36.95` | 114,090,000.00 USD | 0.00 USD | 1,660.00 USD | `-61.67%` | `45.00` |
| `Live` | `Long` | `37.05` | 114,090,000.00 USD | 0.00 USD | 624.29 USD | `-61.56%` | `16.85` |
| `Live` | `Long` | `37.15` | 114,090,000.00 USD | 0.00 USD | 1,310.00 USD | `-61.46%` | `35.38` |
| `Live` | `Long` | `37.25` | 114,090,000.00 USD | 0.00 USD | 4,280.00 USD | `-61.36%` | `114.97` |
| `Live` | `Long` | `37.35` | 114,080,000.00 USD | 0.00 USD | 19,600.00 USD | `-61.25%` | `524.75` |
| `Live` | `Long` | `37.55` | 114,060,000.00 USD | 0.00 USD | 41,870.00 USD | `-61.05%` | `1,115.13` |
| `Live` | `Long` | `37.65` | 114,020,000.00 USD | 0.00 USD | 2,430.00 USD | `-60.94%` | `64.52` |
| `Live` | `Long` | `37.95` | 114,020,000.00 USD | 0.00 USD | 5,170.00 USD | `-60.63%` | `136.35` |
| `Live` | `Long` | `38.05` | 114,020,000.00 USD | 0.00 USD | 1,630.00 USD | `-60.53%` | `42.73` |
| `Live` | `Long` | `38.15` | 114,010,000.00 USD | 0.00 USD | 2,120.00 USD | `-60.42%` | `55.47` |
| `Live` | `Long` | `38.35` | 114,010,000.00 USD | 0.00 USD | 287.63 USD | `-60.22%` | `7.50` |
| `Live` | `Long` | `38.45` | 114,010,000.00 USD | 0.00 USD | 3,000,000.00 USD | `-60.11%` | `78,000.00` |
| `Live` | `Long` | `38.55` | 111,010,000.00 USD | 0.00 USD | 18,330.00 USD | `-60.01%` | `475.39` |
| `Live` | `Long` | `38.65` | 110,990,000.00 USD | 0.00 USD | 83,250.00 USD | `-59.90%` | `2,154.01` |
| `Live` | `Long` | `38.75` | 110,910,000.00 USD | 0.00 USD | 2,280.00 USD | `-59.80%` | `58.86` |
| `Live` | `Long` | `38.85` | 110,910,000.00 USD | 0.00 USD | 4,270.00 USD | `-59.70%` | `109.96` |
| `Live` | `Long` | `38.95` | 110,900,000.00 USD | 0.00 USD | 2,310.00 USD | `-59.59%` | `59.27` |
| `Live` | `Long` | `39.05` | 110,900,000.00 USD | 0.00 USD | 50,470.00 USD | `-59.49%` | `1,292.50` |
| `Live` | `Long` | `39.15` | 110,850,000.00 USD | 0.00 USD | 195,750.00 USD | `-59.39%` | `5,000.00` |
| `Live` | `Long` | `39.25` | 110,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-59.28%` | `33.68` |
| `Live` | `Long` | `39.35` | 110,650,000.00 USD | 0.00 USD | 7,860.00 USD | `-59.18%` | `199.79` |
| `Live` | `Long` | `39.45` | 110,650,000.00 USD | 0.00 USD | 886.44 USD | `-59.07%` | `22.47` |
| `Live` | `Long` | `39.65` | 110,650,000.00 USD | 0.00 USD | 1,560.00 USD | `-58.87%` | `39.31` |
| `Live` | `Long` | `39.75` | 110,640,000.00 USD | 0.00 USD | 159.00 USD | `-58.76%` | `4.00` |
| `Live` | `Long` | `39.85` | 110,640,000.00 USD | 0.00 USD | 1,270.00 USD | `-58.66%` | `31.86` |
| `Live` | `Long` | `40.05` | 110,640,000.00 USD | 0.00 USD | 1,510.00 USD | `-58.45%` | `37.77` |
| `Live` | `Long` | `40.15` | 110,640,000.00 USD | 0.00 USD | 4,490.00 USD | `-58.35%` | `111.93` |
| `Live` | `Long` | `40.25` | 110,640,000.00 USD | 0.00 USD | 632.73 USD | `-58.24%` | `15.72` |
| `Live` | `Long` | `40.35` | 110,640,000.00 USD | 0.00 USD | 921,810.00 USD | `-58.14%` | `22,845.24` |
| `Live` | `Long` | `40.45` | 109,710,000.00 USD | 0.00 USD | 62,790.00 USD | `-58.04%` | `1,552.17` |
| `Live` | `Long` | `40.55` | 109,650,000.00 USD | 0.00 USD | 9,470.00 USD | `-57.93%` | `233.52` |
| `Live` | `Long` | `40.65` | 109,640,000.00 USD | 0.00 USD | 5,150.00 USD | `-57.83%` | `126.80` |
| `Live` | `Long` | `40.75` | 109,640,000.00 USD | 0.00 USD | 1,070.00 USD | `-57.73%` | `26.36` |
| `Live` | `Long` | `40.85` | 109,640,000.00 USD | 0.00 USD | 3,690.00 USD | `-57.62%` | `90.27` |
| `Live` | `Long` | `40.95` | 109,630,000.00 USD | 0.00 USD | 9,790.00 USD | `-57.52%` | `239.18` |
| `Live` | `Long` | `41.05` | 109,620,000.00 USD | 0.00 USD | 21,580.00 USD | `-57.41%` | `525.58` |
| `Live` | `Long` | `41.15` | 109,600,000.00 USD | 0.00 USD | 2,950.00 USD | `-57.31%` | `71.74` |
| `Live` | `Long` | `41.25` | 109,600,000.00 USD | 0.00 USD | 723.94 USD | `-57.21%` | `17.55` |
| `Live` | `Long` | `41.35` | 109,600,000.00 USD | 0.00 USD | 148.45 USD | `-57.10%` | `3.59` |
| `Live` | `Long` | `41.55` | 109,600,000.00 USD | 0.00 USD | 130.88 USD | `-56.90%` | `3.15` |
| `Live` | `Long` | `41.65` | 109,600,000.00 USD | 0.00 USD | 770.11 USD | `-56.79%` | `18.49` |
| `Live` | `Long` | `41.75` | 109,600,000.00 USD | 0.00 USD | 836.67 USD | `-56.69%` | `20.04` |
| `Live` | `Long` | `41.85` | 109,600,000.00 USD | 0.00 USD | 3,450.00 USD | `-56.58%` | `82.36` |
| `Live` | `Long` | `41.95` | 109,590,000.00 USD | 0.00 USD | 50,440.00 USD | `-56.48%` | `1,202.48` |
| `Live` | `Long` | `42.05` | 109,540,000.00 USD | 0.00 USD | 54,040.00 USD | `-56.38%` | `1,285.08` |
| `Live` | `Long` | `42.15` | 109,490,000.00 USD | 0.00 USD | 8,680.00 USD | `-56.27%` | `205.83` |
| `Live` | `Long` | `42.25` | 109,480,000.00 USD | 0.00 USD | 785.00 USD | `-56.17%` | `18.58` |
| `Live` | `Long` | `42.35` | 109,480,000.00 USD | 0.00 USD | 6,030.00 USD | `-56.07%` | `142.31` |
| `Live` | `Long` | `42.55` | 109,470,000.00 USD | 0.00 USD | 8,210.00 USD | `-55.86%` | `193.00` |
| `Live` | `Long` | `42.85` | 109,460,000.00 USD | 0.00 USD | 44,250.00 USD | `-55.55%` | `1,032.68` |
| `Live` | `Long` | `42.95` | 109,420,000.00 USD | 0.00 USD | 460.85 USD | `-55.44%` | `10.73` |
| `Live` | `Long` | `43.25` | 109,420,000.00 USD | 0.00 USD | 2,150.00 USD | `-55.13%` | `49.79` |
| `Live` | `Long` | `43.35` | 109,420,000.00 USD | 0.00 USD | 25,040.00 USD | `-55.03%` | `577.54` |
| `Live` | `Long` | `43.45` | 109,390,000.00 USD | 0.00 USD | 749.95 USD | `-54.93%` | `17.26` |
| `Live` | `Long` | `43.55` | 109,390,000.00 USD | 0.00 USD | 360.16 USD | `-54.82%` | `8.27` |
| `Live` | `Long` | `43.65` | 109,390,000.00 USD | 0.00 USD | 322.14 USD | `-54.72%` | `7.38` |
| `Live` | `Long` | `43.75` | 109,390,000.00 USD | 0.00 USD | 68,830.00 USD | `-54.61%` | `1,573.15` |
| `Live` | `Long` | `43.85` | 109,320,000.00 USD | 0.00 USD | 764.31 USD | `-54.51%` | `17.43` |
| `Live` | `Long` | `43.95` | 109,320,000.00 USD | 0.00 USD | 242.16 USD | `-54.41%` | `5.51` |
| `Live` | `Long` | `44.05` | 109,320,000.00 USD | 0.00 USD | 671,960.00 USD | `-54.30%` | `15,254.51` |
| `Live` | `Long` | `44.15` | 108,650,000.00 USD | 0.00 USD | 110.82 USD | `-54.20%` | `2.51` |
| `Live` | `Long` | `44.25` | 108,650,000.00 USD | 0.00 USD | 9,160.00 USD | `-54.10%` | `206.90` |
| `Live` | `Long` | `44.35` | 108,640,000.00 USD | 0.00 USD | 4,600.00 USD | `-53.99%` | `103.68` |
| `Live` | `Long` | `44.45` | 108,630,000.00 USD | 0.00 USD | 10,180.00 USD | `-53.89%` | `229.02` |
| `Live` | `Long` | `44.55` | 108,620,000.00 USD | 0.00 USD | 17,870.00 USD | `-53.78%` | `401.03` |
| `Live` | `Long` | `44.65` | 108,610,000.00 USD | 0.00 USD | 410.78 USD | `-53.68%` | `9.20` |
| `Live` | `Long` | `44.75` | 108,610,000.00 USD | 0.00 USD | 1,790.00 USD | `-53.58%` | `39.98` |
| `Live` | `Long` | `44.85` | 108,600,000.00 USD | 0.00 USD | 477.20 USD | `-53.47%` | `10.64` |
| `Live` | `Long` | `44.95` | 108,600,000.00 USD | 0.00 USD | 6,510.00 USD | `-53.37%` | `144.85` |
| `Live` | `Long` | `45.15` | 108,600,000.00 USD | 0.00 USD | 179.70 USD | `-53.16%` | `3.98` |
| `Live` | `Long` | `45.25` | 108,600,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-53.06%` | `25,139.70` |
| `Live` | `Long` | `45.35` | 107,460,000.00 USD | 0.00 USD | 37,590.00 USD | `-52.95%` | `828.95` |
| `Live` | `Long` | `45.45` | 107,420,000.00 USD | 0.00 USD | 9,480.00 USD | `-52.85%` | `208.64` |
| `Live` | `Long` | `45.55` | 107,410,000.00 USD | 0.00 USD | 7,940.00 USD | `-52.75%` | `174.26` |
| `Live` | `Long` | `45.65` | 107,400,000.00 USD | 0.00 USD | 12,760.00 USD | `-52.64%` | `279.53` |
| `Live` | `Long` | `45.75` | 107,390,000.00 USD | 0.00 USD | 9,450.00 USD | `-52.54%` | `206.46` |
| `Live` | `Long` | `45.85` | 107,380,000.00 USD | 0.00 USD | 37,220.00 USD | `-52.44%` | `811.71` |
| `Live` | `Long` | `45.95` | 107,350,000.00 USD | 0.00 USD | 400,220.00 USD | `-52.33%` | `8,709.90` |
| `Live` | `Long` | `46.05` | 106,940,000.00 USD | 0.00 USD | 2,170.00 USD | `-52.23%` | `47.16` |
| `Live` | `Long` | `46.45` | 106,940,000.00 USD | 0.00 USD | 11,610.00 USD | `-51.81%` | `250.00` |
| `Live` | `Long` | `46.55` | 106,930,000.00 USD | 0.00 USD | 2,050.00 USD | `-51.71%` | `43.98` |
| `Live` | `Long` | `46.65` | 106,930,000.00 USD | 0.00 USD | 542.07 USD | `-51.61%` | `11.62` |
| `Live` | `Long` | `46.75` | 106,930,000.00 USD | 0.00 USD | 537.62 USD | `-51.50%` | `11.50` |
| `Live` | `Long` | `46.85` | 106,930,000.00 USD | 0.00 USD | 140.55 USD | `-51.40%` | `3.00` |
| `Live` | `Long` | `46.95` | 106,930,000.00 USD | 0.00 USD | 3,260.00 USD | `-51.29%` | `69.48` |
| `Live` | `Long` | `47.15` | 106,920,000.00 USD | 0.00 USD | 1,570.00 USD | `-51.09%` | `33.22` |
| `Live` | `Long` | `47.25` | 106,920,000.00 USD | 0.00 USD | 3,700.00 USD | `-50.98%` | `78.21` |
| `Live` | `Long` | `47.35` | 106,920,000.00 USD | 0.00 USD | 3,880,000.00 USD | `-50.88%` | `81,851.78` |
| `Live` | `Long` | `47.55` | 103,040,000.00 USD | 0.00 USD | 106.04 USD | `-50.67%` | `2.23` |
| `Live` | `Long` | `47.65` | 103,040,000.00 USD | 0.00 USD | 99,280.00 USD | `-50.57%` | `2,083.61` |
| `Live` | `Long` | `47.75` | 102,940,000.00 USD | 0.00 USD | 56,650.00 USD | `-50.46%` | `1,186.40` |
| `Live` | `Long` | `47.85` | 102,890,000.00 USD | 0.00 USD | 10,290.00 USD | `-50.36%` | `215.05` |
| `Live` | `Long` | `48.05` | 102,880,000.00 USD | 0.00 USD | 14,010.00 USD | `-50.15%` | `291.51` |
| `Live` | `Long` | `48.15` | 102,860,000.00 USD | 0.00 USD | 6,300.00 USD | `-50.05%` | `130.93` |
| `Live` | `Long` | `48.25` | 102,860,000.00 USD | 0.00 USD | 3,980.00 USD | `-49.95%` | `82.45` |
| `Live` | `Long` | `48.35` | 102,850,000.00 USD | 0.00 USD | 5,630.00 USD | `-49.84%` | `116.44` |
| `Live` | `Long` | `48.45` | 102,850,000.00 USD | 0.00 USD | 2,930.00 USD | `-49.74%` | `60.44` |
| `Live` | `Long` | `48.55` | 102,840,000.00 USD | 0.00 USD | 97,530.00 USD | `-49.63%` | `2,008.83` |
| `Live` | `Long` | `48.65` | 102,750,000.00 USD | 0.00 USD | 9,260.00 USD | `-49.53%` | `190.42` |
| `Live` | `Long` | `48.75` | 102,740,000.00 USD | 0.00 USD | 58,330.00 USD | `-49.43%` | `1,196.55` |
| `Live` | `Long` | `48.85` | 102,680,000.00 USD | 0.00 USD | 14,260.00 USD | `-49.32%` | `291.88` |
| `Live` | `Long` | `48.95` | 102,670,000.00 USD | 0.00 USD | 1,250.00 USD | `-49.22%` | `25.51` |
| `Live` | `Long` | `49.05` | 102,660,000.00 USD | 0.00 USD | 5,800.00 USD | `-49.12%` | `118.27` |
| `Live` | `Long` | `49.25` | 102,660,000.00 USD | 0.00 USD | 21,190.00 USD | `-48.91%` | `430.30` |
| `Live` | `Long` | `49.35` | 102,640,000.00 USD | 0.00 USD | 585.29 USD | `-48.80%` | `11.86` |
| `Live` | `Long` | `49.45` | 102,640,000.00 USD | 0.00 USD | 15,560.00 USD | `-48.70%` | `314.65` |
| `Live` | `Long` | `49.55` | 102,620,000.00 USD | 0.00 USD | 777,020.00 USD | `-48.60%` | `15,681.62` |
| `Live` | `Long` | `49.65` | 101,840,000.00 USD | 0.00 USD | 9,200.00 USD | `-48.49%` | `185.21` |
| `Live` | `Long` | `49.75` | 101,830,000.00 USD | 0.00 USD | 12,330.00 USD | `-48.39%` | `247.90` |
| `Live` | `Long` | `49.85` | 101,820,000.00 USD | 0.00 USD | 42,210.00 USD | `-48.29%` | `846.70` |
| `Live` | `Long` | `49.95` | 101,780,000.00 USD | 0.00 USD | 22,720.00 USD | `-48.18%` | `454.83` |
| `Live` | `Long` | `50.05` | 101,760,000.00 USD | 0.00 USD | 9,450.00 USD | `-48.08%` | `188.80` |
| `Live` | `Long` | `50.15` | 101,750,000.00 USD | 0.00 USD | 4,070.00 USD | `-47.97%` | `81.09` |
| `Live` | `Long` | `50.25` | 101,740,000.00 USD | 0.00 USD | 8,170.00 USD | `-47.87%` | `162.55` |
| `Live` | `Long` | `50.35` | 101,740,000.00 USD | 0.00 USD | 7,880.00 USD | `-47.77%` | `156.51` |
| `Live` | `Long` | `50.45` | 101,730,000.00 USD | 0.00 USD | 4,800.00 USD | `-47.66%` | `95.10` |
| `Live` | `Long` | `50.55` | 101,720,000.00 USD | 0.00 USD | 2,400.00 USD | `-47.56%` | `47.47` |
| `Live` | `Long` | `50.65` | 101,720,000.00 USD | 0.00 USD | 843.83 USD | `-47.46%` | `16.66` |
| `Live` | `Long` | `50.75` | 101,720,000.00 USD | 0.00 USD | 12,800.00 USD | `-47.35%` | `252.21` |
| `Live` | `Long` | `50.85` | 101,710,000.00 USD | 0.00 USD | 20,000.00 USD | `-47.25%` | `393.39` |
| `Live` | `Long` | `50.95` | 101,690,000.00 USD | 0.00 USD | 12,540.00 USD | `-47.14%` | `246.18` |
| `Live` | `Long` | `51.05` | 101,670,000.00 USD | 0.00 USD | 13,390.00 USD | `-47.04%` | `262.21` |
| `Live` | `Long` | `51.15` | 101,660,000.00 USD | 0.00 USD | 3,170.00 USD | `-46.94%` | `61.92` |
| `Live` | `Long` | `51.25` | 101,660,000.00 USD | 0.00 USD | 10,390.00 USD | `-46.83%` | `202.74` |
| `Live` | `Long` | `51.35` | 101,650,000.00 USD | 0.00 USD | 5,990.00 USD | `-46.73%` | `116.62` |
| `Live` | `Long` | `51.45` | 101,640,000.00 USD | 0.00 USD | 4,540.00 USD | `-46.63%` | `88.31` |
| `Live` | `Long` | `51.55` | 101,640,000.00 USD | 0.00 USD | 137,150.00 USD | `-46.52%` | `2,660.60` |
| `Live` | `Long` | `51.65` | 101,500,000.00 USD | 0.00 USD | 7,720.00 USD | `-46.42%` | `149.52` |
| `Live` | `Long` | `51.75` | 101,490,000.00 USD | 0.00 USD | 24,770.00 USD | `-46.31%` | `478.71` |
| `Live` | `Long` | `51.85` | 101,470,000.00 USD | 0.00 USD | 1,290,000.00 USD | `-46.21%` | `24,889.34` |
| `Live` | `Long` | `51.95` | 100,180,000.00 USD | 0.00 USD | 469,860.00 USD | `-46.11%` | `9,044.37` |
| `Live` | `Long` | `52.15` | 99,710,000.00 USD | 0.00 USD | 99,630.00 USD | `-45.90%` | `1,910.43` |
| `Live` | `Long` | `52.25` | 99,610,000.00 USD | 0.00 USD | 1,550.00 USD | `-45.80%` | `29.66` |
| `Live` | `Long` | `52.35` | 99,610,000.00 USD | 0.00 USD | 1,030.00 USD | `-45.69%` | `19.66` |
| `Live` | `Long` | `52.45` | 99,600,000.00 USD | 0.00 USD | 4,780.00 USD | `-45.59%` | `91.07` |
| `Live` | `Long` | `52.55` | 99,600,000.00 USD | 0.00 USD | 11,110.00 USD | `-45.48%` | `211.45` |
| `Live` | `Long` | `52.65` | 99,590,000.00 USD | 0.00 USD | 2,630.00 USD | `-45.38%` | `50.00` |
| `Live` | `Long` | `52.75` | 99,590,000.00 USD | 0.00 USD | 30,770.00 USD | `-45.28%` | `583.33` |
| `Live` | `Long` | `52.85` | 99,560,000.00 USD | 0.00 USD | 9,370.00 USD | `-45.17%` | `177.38` |
| `Live` | `Long` | `52.95` | 99,550,000.00 USD | 0.00 USD | 5,320.00 USD | `-45.07%` | `100.41` |
| `Live` | `Long` | `53.05` | 99,540,000.00 USD | 0.00 USD | 5,120.00 USD | `-44.97%` | `96.59` |
| `Live` | `Long` | `53.15` | 99,540,000.00 USD | 0.00 USD | 7,910.00 USD | `-44.86%` | `148.83` |
| `Live` | `Long` | `53.25` | 99,530,000.00 USD | 0.00 USD | 24,120.00 USD | `-44.76%` | `452.99` |
| `Live` | `Long` | `53.35` | 99,500,000.00 USD | 0.00 USD | 2,930.00 USD | `-44.65%` | `54.90` |
| `Live` | `Long` | `53.45` | 99,500,000.00 USD | 0.00 USD | 34,210.00 USD | `-44.55%` | `639.97` |
| `Live` | `Long` | `53.55` | 99,470,000.00 USD | 0.00 USD | 44,230.00 USD | `-44.45%` | `826.05` |
| `Live` | `Long` | `53.65` | 99,420,000.00 USD | 0.00 USD | 334.24 USD | `-44.34%` | `6.23` |
| `Live` | `Long` | `53.75` | 99,420,000.00 USD | 0.00 USD | 3,600.00 USD | `-44.24%` | `67.00` |
| `Live` | `Long` | `53.85` | 99,420,000.00 USD | 0.00 USD | 27,060.00 USD | `-44.14%` | `502.46` |
| `Live` | `Long` | `53.95` | 99,390,000.00 USD | 0.00 USD | 69,370.00 USD | `-44.03%` | `1,285.73` |
| `Live` | `Long` | `54.05` | 99,320,000.00 USD | 0.00 USD | 350.78 USD | `-43.93%` | `6.49` |
| `Live` | `Long` | `54.15` | 99,320,000.00 USD | 0.00 USD | 19,470.00 USD | `-43.82%` | `359.63` |
| `Live` | `Long` | `54.25` | 99,300,000.00 USD | 0.00 USD | 5,360.00 USD | `-43.72%` | `98.83` |
| `Live` | `Long` | `54.35` | 99,300,000.00 USD | 0.00 USD | 30,500.00 USD | `-43.62%` | `561.12` |
| `Live` | `Long` | `54.45` | 99,270,000.00 USD | 0.00 USD | 753.04 USD | `-43.51%` | `13.83` |
| `Live` | `Long` | `54.55` | 99,270,000.00 USD | 0.00 USD | 62,540.00 USD | `-43.41%` | `1,146.45` |
| `Live` | `Long` | `54.65` | 99,200,000.00 USD | 0.00 USD | 3,290.00 USD | `-43.31%` | `60.21` |
| `Live` | `Long` | `54.75` | 99,200,000.00 USD | 0.00 USD | 15,140.00 USD | `-43.20%` | `276.50` |
| `Live` | `Long` | `54.85` | 99,180,000.00 USD | 0.00 USD | 858,930.00 USD | `-43.10%` | `15,659.66` |
| `Live` | `Long` | `54.95` | 98,330,000.00 USD | 0.00 USD | 151,380.00 USD | `-42.99%` | `2,754.84` |
| `Live` | `Long` | `55.05` | 98,170,000.00 USD | 0.00 USD | 722.26 USD | `-42.89%` | `13.12` |
| `Live` | `Long` | `55.15` | 98,170,000.00 USD | 0.00 USD | 1,550.00 USD | `-42.79%` | `28.06` |
| `Live` | `Long` | `55.25` | 98,170,000.00 USD | 0.00 USD | 1,900.00 USD | `-42.68%` | `34.45` |
| `Live` | `Long` | `55.35` | 98,170,000.00 USD | 0.00 USD | 9,920.00 USD | `-42.58%` | `179.16` |
| `Live` | `Long` | `55.45` | 98,160,000.00 USD | 0.00 USD | 8,670.00 USD | `-42.48%` | `156.35` |
| `Live` | `Long` | `55.55` | 98,150,000.00 USD | 0.00 USD | 16,200.00 USD | `-42.37%` | `291.69` |
| `Live` | `Long` | `55.65` | 98,130,000.00 USD | 0.00 USD | 11,490.00 USD | `-42.27%` | `206.41` |
| `Live` | `Long` | `55.75` | 98,120,000.00 USD | 0.00 USD | 232,500.00 USD | `-42.17%` | `4,170.46` |
| `Live` | `Long` | `55.85` | 97,890,000.00 USD | 0.00 USD | 3,530.00 USD | `-42.06%` | `63.22` |
| `Live` | `Long` | `55.95` | 97,890,000.00 USD | 0.00 USD | 7,050.00 USD | `-41.96%` | `125.95` |
| `Live` | `Long` | `56.05` | 97,880,000.00 USD | 0.00 USD | 9,470.00 USD | `-41.85%` | `169.01` |
| `Live` | `Long` | `56.15` | 97,870,000.00 USD | 0.00 USD | 37,740.00 USD | `-41.75%` | `672.10` |
| `Live` | `Long` | `56.25` | 97,830,000.00 USD | 0.00 USD | 17,970.00 USD | `-41.65%` | `319.43` |
| `Live` | `Long` | `56.35` | 97,820,000.00 USD | 0.00 USD | 22,200.00 USD | `-41.54%` | `393.91` |
| `Live` | `Long` | `56.45` | 97,790,000.00 USD | 0.00 USD | 17,880.00 USD | `-41.44%` | `316.72` |
| `Live` | `Long` | `56.55` | 97,780,000.00 USD | 0.00 USD | 355,340.00 USD | `-41.34%` | `6,283.63` |
| `Live` | `Long` | `56.65` | 97,420,000.00 USD | 0.00 USD | 3,700.00 USD | `-41.23%` | `65.40` |
| `Live` | `Long` | `56.75` | 97,420,000.00 USD | 0.00 USD | 9,410.00 USD | `-41.13%` | `165.87` |
| `Live` | `Long` | `56.85` | 97,410,000.00 USD | 0.00 USD | 12,000.00 USD | `-41.02%` | `211.05` |
| `Live` | `Long` | `56.95` | 97,390,000.00 USD | 0.00 USD | 2,780,000.00 USD | `-40.92%` | `48,815.94` |
| `Live` | `Long` | `57.05` | 94,610,000.00 USD | 0.00 USD | 3,620.00 USD | `-40.82%` | `63.42` |
| `Live` | `Long` | `57.15` | 94,610,000.00 USD | 0.00 USD | 5,740.00 USD | `-40.71%` | `100.36` |
| `Live` | `Long` | `57.25` | 94,610,000.00 USD | 0.00 USD | 1,270.00 USD | `-40.61%` | `22.11` |
| `Live` | `Long` | `57.35` | 94,600,000.00 USD | 0.00 USD | 8,840.00 USD | `-40.51%` | `154.09` |
| `Live` | `Long` | `57.45` | 94,600,000.00 USD | 0.00 USD | 19,200.00 USD | `-40.40%` | `334.25` |
| `Live` | `Long` | `57.55` | 94,580,000.00 USD | 0.00 USD | 1,390.00 USD | `-40.30%` | `24.22` |
| `Live` | `Long` | `57.65` | 94,570,000.00 USD | 0.00 USD | 12,790.00 USD | `-40.19%` | `221.85` |
| `Live` | `Long` | `57.75` | 94,560,000.00 USD | 0.00 USD | 3,130.00 USD | `-40.09%` | `54.14` |
| `Live` | `Long` | `57.85` | 94,560,000.00 USD | 0.00 USD | 27,330.00 USD | `-39.99%` | `472.35` |
| `Live` | `Long` | `57.95` | 94,530,000.00 USD | 0.00 USD | 32,460.00 USD | `-39.88%` | `560.10` |
| `Live` | `Long` | `58.05` | 94,500,000.00 USD | 0.00 USD | 4,710.00 USD | `-39.78%` | `81.10` |
| `Live` | `Long` | `58.15` | 94,490,000.00 USD | 0.00 USD | 124,360.00 USD | `-39.68%` | `2,138.54` |
| `Live` | `Long` | `58.25` | 94,370,000.00 USD | 0.00 USD | 6,670.00 USD | `-39.57%` | `114.44` |
| `Live` | `Long` | `58.35` | 94,360,000.00 USD | 0.00 USD | 28,010.00 USD | `-39.47%` | `480.09` |
| `Live` | `Long` | `58.45` | 94,340,000.00 USD | 0.00 USD | 463.51 USD | `-39.36%` | `7.93` |
| `Live` | `Long` | `58.55` | 94,330,000.00 USD | 0.00 USD | 49,380.00 USD | `-39.26%` | `843.30` |
| `Live` | `Long` | `58.65` | 94,290,000.00 USD | 0.00 USD | 11,370.00 USD | `-39.16%` | `193.94` |
| `Live` | `Long` | `58.75` | 94,270,000.00 USD | 0.00 USD | 195.64 USD | `-39.05%` | `3.33` |
| `Live` | `Long` | `58.85` | 94,270,000.00 USD | 0.00 USD | 6,130.00 USD | `-38.95%` | `104.08` |
| `Live` | `Long` | `58.95` | 94,270,000.00 USD | 0.00 USD | 62,270.00 USD | `-38.85%` | `1,056.32` |
| `Live` | `Long` | `59.05` | 94,210,000.00 USD | 0.00 USD | 3,780.00 USD | `-38.74%` | `63.97` |
| `Live` | `Long` | `59.15` | 94,200,000.00 USD | 0.00 USD | 15,720.00 USD | `-38.64%` | `265.70` |
| `Live` | `Long` | `59.25` | 94,190,000.00 USD | 0.00 USD | 46,730.00 USD | `-38.53%` | `788.65` |
| `Live` | `Long` | `59.35` | 94,140,000.00 USD | 0.00 USD | 28,850.00 USD | `-38.43%` | `486.15` |
| `Live` | `Long` | `59.45` | 94,110,000.00 USD | 0.00 USD | 4,230.00 USD | `-38.33%` | `71.12` |
| `Live` | `Long` | `59.55` | 94,110,000.00 USD | 0.00 USD | 14,560.00 USD | `-38.22%` | `244.57` |
| `Live` | `Long` | `59.65` | 94,090,000.00 USD | 0.00 USD | 18,840.00 USD | `-38.12%` | `315.85` |
| `Live` | `Long` | `59.75` | 94,070,000.00 USD | 0.00 USD | 22,540.00 USD | `-38.02%` | `377.28` |
| `Live` | `Long` | `59.85` | 94,050,000.00 USD | 0.00 USD | 28,800.00 USD | `-37.91%` | `481.25` |
| `Live` | `Long` | `59.95` | 94,020,000.00 USD | 0.00 USD | 38,660.00 USD | `-37.81%` | `644.88` |
| `Live` | `Long` | `60.05` | 93,980,000.00 USD | 0.00 USD | 19,630.00 USD | `-37.70%` | `326.86` |
| `Live` | `Long` | `60.15` | 93,960,000.00 USD | 0.00 USD | 2,470,000.00 USD | `-37.60%` | `41,032.55` |
| `Live` | `Long` | `60.25` | 91,490,000.00 USD | 0.00 USD | 745.29 USD | `-37.50%` | `12.37` |
| `Live` | `Long` | `60.35` | 91,490,000.00 USD | 0.00 USD | 3,930.00 USD | `-37.39%` | `65.10` |
| `Live` | `Long` | `60.45` | 91,490,000.00 USD | 0.00 USD | 38,080.00 USD | `-37.29%` | `630.00` |
| `Live` | `Long` | `60.55` | 91,450,000.00 USD | 0.00 USD | 8,210.00 USD | `-37.19%` | `135.51` |
| `Live` | `Long` | `60.65` | 91,440,000.00 USD | 0.00 USD | 711.42 USD | `-37.08%` | `11.73` |
| `Live` | `Long` | `60.75` | 91,440,000.00 USD | 0.00 USD | 6,520.00 USD | `-36.98%` | `107.26` |
| `Live` | `Long` | `60.85` | 91,440,000.00 USD | 0.00 USD | 28,890.00 USD | `-36.87%` | `474.84` |
| `Live` | `Long` | `60.95` | 91,410,000.00 USD | 0.00 USD | 55,160.00 USD | `-36.77%` | `905.08` |
| `Live` | `Long` | `61.05` | 91,350,000.00 USD | 0.00 USD | 4,230.00 USD | `-36.67%` | `69.34` |
| `Live` | `Long` | `61.15` | 91,350,000.00 USD | 0.00 USD | 4,870.00 USD | `-36.56%` | `79.64` |
| `Live` | `Long` | `61.25` | 91,340,000.00 USD | 0.00 USD | 4,630.00 USD | `-36.46%` | `75.67` |
| `Live` | `Long` | `61.35` | 91,340,000.00 USD | 0.00 USD | 10,170.00 USD | `-36.36%` | `165.83` |
| `Live` | `Long` | `61.45` | 91,330,000.00 USD | 0.00 USD | 20,920.00 USD | `-36.25%` | `340.48` |
| `Live` | `Long` | `61.55` | 91,310,000.00 USD | 0.00 USD | 121.87 USD | `-36.15%` | `1.98` |
| `Live` | `Long` | `61.65` | 91,310,000.00 USD | 0.00 USD | 18,880.00 USD | `-36.04%` | `306.22` |
| `Live` | `Long` | `61.75` | 91,290,000.00 USD | 0.00 USD | 21,030.00 USD | `-35.94%` | `340.52` |
| `Live` | `Long` | `61.85` | 91,270,000.00 USD | 0.00 USD | 21,260.00 USD | `-35.84%` | `343.81` |
| `Live` | `Long` | `61.95` | 91,250,000.00 USD | 0.00 USD | 22,840.00 USD | `-35.73%` | `368.75` |
| `Live` | `Long` | `62.05` | 91,220,000.00 USD | 0.00 USD | 9,000.00 USD | `-35.63%` | `145.05` |
| `Live` | `Long` | `62.15` | 91,210,000.00 USD | 0.00 USD | 25,540.00 USD | `-35.53%` | `410.91` |
| `Live` | `Long` | `62.25` | 91,190,000.00 USD | 0.00 USD | 1,800.00 USD | `-35.42%` | `28.90` |
| `Live` | `Long` | `62.35` | 91,190,000.00 USD | 0.00 USD | 20,700.00 USD | `-35.32%` | `331.95` |
| `Live` | `Long` | `62.45` | 91,170,000.00 USD | 0.00 USD | 20,480.00 USD | `-35.21%` | `327.96` |
| `Live` | `Long` | `62.55` | 91,150,000.00 USD | 0.00 USD | 140,760.00 USD | `-35.11%` | `2,250.35` |
| `Live` | `Long` | `62.65` | 91,010,000.00 USD | 0.00 USD | 41,340.00 USD | `-35.01%` | `659.81` |
| `Live` | `Long` | `62.75` | 90,960,000.00 USD | 0.00 USD | 3,140.00 USD | `-34.90%` | `49.97` |
| `Live` | `Long` | `62.85` | 90,960,000.00 USD | 0.00 USD | 31,310.00 USD | `-34.80%` | `498.17` |
| `Live` | `Long` | `62.95` | 90,930,000.00 USD | 0.00 USD | 56,830.00 USD | `-34.70%` | `902.71` |
| `Live` | `Long` | `63.05` | 90,870,000.00 USD | 0.00 USD | 26,110.00 USD | `-34.59%` | `414.11` |
| `Live` | `Long` | `63.15` | 90,850,000.00 USD | 0.00 USD | 82,440.00 USD | `-34.49%` | `1,305.44` |
| `Live` | `Long` | `63.25` | 90,760,000.00 USD | 0.00 USD | 14,770.00 USD | `-34.38%` | `233.52` |
| `Live` | `Long` | `63.45` | 90,750,000.00 USD | 0.00 USD | 1,360.00 USD | `-34.18%` | `21.42` |
| `Live` | `Long` | `63.55` | 90,750,000.00 USD | 0.00 USD | 49,290.00 USD | `-34.07%` | `775.56` |
| `Live` | `Long` | `63.65` | 90,700,000.00 USD | 0.00 USD | 18,490.00 USD | `-33.97%` | `290.57` |
| `Live` | `Long` | `63.75` | 90,680,000.00 USD | 0.00 USD | 32,540.00 USD | `-33.87%` | `510.36` |
| `Live` | `Long` | `63.85` | 90,650,000.00 USD | 0.00 USD | 36,960.00 USD | `-33.76%` | `578.89` |
| `Live` | `Long` | `63.95` | 90,610,000.00 USD | 0.00 USD | 5,480.00 USD | `-33.66%` | `85.70` |
| `Live` | `Long` | `64.15` | 90,610,000.00 USD | 0.00 USD | 160.38 USD | `-33.45%` | `2.50` |
| `Live` | `Long` | `64.25` | 90,610,000.00 USD | 0.00 USD | 5,090.00 USD | `-33.35%` | `79.27` |
| `Live` | `Long` | `64.35` | 90,600,000.00 USD | 0.00 USD | 875.16 USD | `-33.24%` | `13.60` |
| `Live` | `Long` | `64.45` | 90,600,000.00 USD | 0.00 USD | 7,090.00 USD | `-33.14%` | `110.04` |
| `Live` | `Long` | `64.55` | 90,590,000.00 USD | 0.00 USD | 579.66 USD | `-33.04%` | `8.98` |
| `Live` | `Long` | `64.65` | 90,590,000.00 USD | 0.00 USD | 1,740.00 USD | `-32.93%` | `26.99` |
| `Live` | `Long` | `64.75` | 90,590,000.00 USD | 0.00 USD | 18,230.00 USD | `-32.83%` | `281.58` |
| `Live` | `Long` | `64.85` | 90,570,000.00 USD | 0.00 USD | 396.23 USD | `-32.72%` | `6.11` |
| `Live` | `Long` | `64.95` | 90,570,000.00 USD | 0.00 USD | 209.79 USD | `-32.62%` | `3.23` |
| `Live` | `Long` | `65.05` | 90,570,000.00 USD | 0.00 USD | 247,180.00 USD | `-32.52%` | `3,799.85` |
| `Live` | `Long` | `65.15` | 90,320,000.00 USD | 0.00 USD | 12,510.00 USD | `-32.41%` | `192.07` |
| `Live` | `Long` | `65.25` | 90,310,000.00 USD | 0.00 USD | 16,400.00 USD | `-32.31%` | `251.41` |
| `Live` | `Long` | `65.35` | 90,290,000.00 USD | 0.00 USD | 57,020.00 USD | `-32.21%` | `872.59` |
| `Live` | `Long` | `65.45` | 90,240,000.00 USD | 0.00 USD | 102,230.00 USD | `-32.10%` | `1,561.89` |
| `Live` | `Long` | `65.55` | 90,140,000.00 USD | 0.00 USD | 10,470.00 USD | `-32.00%` | `159.76` |
| `Live` | `Long` | `65.65` | 90,130,000.00 USD | 0.00 USD | 60,250.00 USD | `-31.89%` | `917.71` |
| `Live` | `Long` | `65.75` | 90,060,000.00 USD | 0.00 USD | 5,370.00 USD | `-31.79%` | `81.62` |
| `Live` | `Long` | `65.85` | 90,060,000.00 USD | 0.00 USD | 1,300.00 USD | `-31.69%` | `19.81` |
| `Live` | `Long` | `65.95` | 90,060,000.00 USD | 0.00 USD | 108,010.00 USD | `-31.58%` | `1,637.71` |
| `Live` | `Long` | `66.05` | 89,950,000.00 USD | 0.00 USD | 6,280.00 USD | `-31.48%` | `95.15` |
| `Live` | `Long` | `66.25` | 89,940,000.00 USD | 0.00 USD | 15,490.00 USD | `-31.27%` | `233.79` |
| `Live` | `Long` | `66.35` | 89,930,000.00 USD | 0.00 USD | 1,810.00 USD | `-31.17%` | `27.33` |
| `Live` | `Long` | `66.45` | 89,930,000.00 USD | 0.00 USD | 10,990.00 USD | `-31.06%` | `165.37` |
| `Live` | `Long` | `66.55` | 89,920,000.00 USD | 0.00 USD | 56,020.00 USD | `-30.96%` | `841.75` |
| `Live` | `Long` | `66.65` | 89,860,000.00 USD | 0.00 USD | 68,880.00 USD | `-30.86%` | `1,033.44` |
| `Live` | `Long` | `66.75` | 89,790,000.00 USD | 0.00 USD | 12,210.00 USD | `-30.75%` | `182.96` |
| `Live` | `Long` | `66.85` | 89,780,000.00 USD | 0.00 USD | 6,010.00 USD | `-30.65%` | `89.90` |
| `Live` | `Long` | `66.95` | 89,770,000.00 USD | 0.00 USD | 937.30 USD | `-30.55%` | `14.00` |
| `Live` | `Long` | `67.05` | 89,770,000.00 USD | 0.00 USD | 42,080.00 USD | `-30.44%` | `627.62` |
| `Live` | `Long` | `67.15` | 89,730,000.00 USD | 0.00 USD | 46,040.00 USD | `-30.34%` | `685.65` |
| `Live` | `Long` | `67.25` | 89,680,000.00 USD | 0.00 USD | 10,190.00 USD | `-30.23%` | `151.47` |
| `Live` | `Long` | `67.35` | 89,670,000.00 USD | 0.00 USD | 23,070.00 USD | `-30.13%` | `342.55` |
| `Live` | `Long` | `67.45` | 89,650,000.00 USD | 0.00 USD | 22,930.00 USD | `-30.03%` | `339.94` |
| `Live` | `Long` | `67.55` | 89,630,000.00 USD | 0.00 USD | 53,160.00 USD | `-29.92%` | `786.93` |
| `Live` | `Long` | `67.65` | 89,570,000.00 USD | 0.00 USD | 160,750.00 USD | `-29.82%` | `2,376.17` |
| `Live` | `Long` | `67.75` | 89,410,000.00 USD | 0.00 USD | 11,150.00 USD | `-29.72%` | `164.59` |
| `Live` | `Long` | `67.85` | 89,400,000.00 USD | 0.00 USD | 32,710.00 USD | `-29.61%` | `482.02` |
| `Live` | `Long` | `68.05` | 89,370,000.00 USD | 0.00 USD | 259,070.00 USD | `-29.41%` | `3,807.08` |
| `Live` | `Long` | `68.15` | 89,110,000.00 USD | 0.00 USD | 37,490,000.00 USD | `-29.30%` | `550,112.64` |
| `Live` | `Long` | `68.25` | 51,620,000.00 USD | 0.00 USD | 13,820.00 USD | `-29.20%` | `202.43` |
| `Live` | `Long` | `68.35` | 51,610,000.00 USD | 0.00 USD | 2,860.00 USD | `-29.09%` | `41.82` |
| `Live` | `Long` | `68.45` | 51,600,000.00 USD | 0.00 USD | 18,450.00 USD | `-28.99%` | `269.55` |
| `Live` | `Long` | `68.55` | 51,590,000.00 USD | 0.00 USD | 3,260.00 USD | `-28.89%` | `47.60` |
| `Live` | `Long` | `68.65` | 51,580,000.00 USD | 0.00 USD | 6,610.00 USD | `-28.78%` | `96.35` |
| `Live` | `Long` | `68.75` | 51,580,000.00 USD | 0.00 USD | 162,300.00 USD | `-28.68%` | `2,360.72` |
| `Live` | `Long` | `68.85` | 51,410,000.00 USD | 0.00 USD | 3,260.00 USD | `-28.58%` | `47.36` |
| `Live` | `Long` | `68.95` | 51,410,000.00 USD | 0.00 USD | 45,480.00 USD | `-28.47%` | `659.55` |
| `Live` | `Long` | `69.05` | 51,360,000.00 USD | 0.00 USD | 145.70 USD | `-28.37%` | `2.11` |
| `Live` | `Long` | `69.15` | 51,360,000.00 USD | 0.00 USD | 24,130.00 USD | `-28.26%` | `348.94` |
| `Live` | `Long` | `69.25` | 51,340,000.00 USD | 0.00 USD | 3,140.00 USD | `-28.16%` | `45.34` |
| `Live` | `Long` | `69.35` | 51,340,000.00 USD | 0.00 USD | 772,100.00 USD | `-28.06%` | `11,133.44` |
| `Live` | `Long` | `69.45` | 50,560,000.00 USD | 0.00 USD | 14,370.00 USD | `-27.95%` | `206.85` |
| `Live` | `Long` | `69.55` | 50,550,000.00 USD | 0.00 USD | 10,540.00 USD | `-27.85%` | `151.60` |
| `Live` | `Long` | `69.65` | 50,540,000.00 USD | 0.00 USD | 3,660.00 USD | `-27.75%` | `52.48` |
| `Live` | `Long` | `69.75` | 50,540,000.00 USD | 0.00 USD | 214,850.00 USD | `-27.64%` | `3,080.30` |
| `Live` | `Long` | `69.85` | 50,320,000.00 USD | 0.00 USD | 8,470.00 USD | `-27.54%` | `121.19` |
| `Live` | `Long` | `69.95` | 50,310,000.00 USD | 0.00 USD | 8,800.00 USD | `-27.43%` | `125.81` |
| `Live` | `Long` | `70.05` | 50,300,000.00 USD | 0.00 USD | 13,110,000.00 USD | `-27.33%` | `187,140.55` |
| `Live` | `Long` | `70.15` | 37,190,000.00 USD | 0.00 USD | 4,120.00 USD | `-27.23%` | `58.77` |
| `Live` | `Long` | `70.25` | 37,190,000.00 USD | 0.00 USD | 73,790.00 USD | `-27.12%` | `1,050.46` |
| `Live` | `Long` | `70.35` | 37,120,000.00 USD | 0.00 USD | 2,170,000.00 USD | `-27.02%` | `30,814.81` |
| `Live` | `Long` | `70.45` | 34,950,000.00 USD | 0.00 USD | 116,720.00 USD | `-26.92%` | `1,656.76` |
| `Live` | `Long` | `70.65` | 34,830,000.00 USD | 0.00 USD | 45,480.00 USD | `-26.71%` | `643.67` |
| `Live` | `Long` | `70.75` | 34,790,000.00 USD | 0.00 USD | 9,720.00 USD | `-26.60%` | `137.39` |
| `Live` | `Long` | `70.85` | 34,780,000.00 USD | 0.00 USD | 29,230.00 USD | `-26.50%` | `412.53` |
| `Live` | `Long` | `70.95` | 34,750,000.00 USD | 0.00 USD | 4,430.00 USD | `-26.40%` | `62.38` |
| `Live` | `Long` | `71.05` | 34,740,000.00 USD | 0.00 USD | 47,400.00 USD | `-26.29%` | `667.14` |
| `Live` | `Long` | `71.15` | 34,700,000.00 USD | 0.00 USD | 69,870.00 USD | `-26.19%` | `982.07` |
| `Live` | `Long` | `71.25` | 34,630,000.00 USD | 0.00 USD | 6,300.00 USD | `-26.09%` | `88.37` |
| `Live` | `Long` | `71.35` | 34,620,000.00 USD | 0.00 USD | 15,590.00 USD | `-25.98%` | `218.51` |
| `Live` | `Long` | `71.45` | 34,600,000.00 USD | 0.00 USD | 38,820.00 USD | `-25.88%` | `543.37` |
| `Live` | `Long` | `71.55` | 34,570,000.00 USD | 0.00 USD | 43,440.00 USD | `-25.77%` | `607.14` |
| `Live` | `Long` | `71.65` | 34,520,000.00 USD | 0.00 USD | 4,370.00 USD | `-25.67%` | `61.05` |
| `Live` | `Long` | `71.75` | 34,520,000.00 USD | 0.00 USD | 28,720.00 USD | `-25.57%` | `400.33` |
| `Live` | `Long` | `71.85` | 34,490,000.00 USD | 0.00 USD | 2,670.00 USD | `-25.46%` | `37.11` |
| `Live` | `Long` | `71.95` | 34,490,000.00 USD | 0.00 USD | 12,860.00 USD | `-25.36%` | `178.70` |
| `Live` | `Long` | `72.05` | 34,470,000.00 USD | 0.00 USD | 1,120,000.00 USD | `-25.26%` | `15,562.06` |
| `Live` | `Long` | `72.15` | 33,350,000.00 USD | 0.00 USD | 131,520.00 USD | `-25.15%` | `1,822.91` |
| `Live` | `Long` | `72.25` | 33,220,000.00 USD | 0.00 USD | 260,000.00 USD | `-25.05%` | `3,598.60` |
| `Live` | `Long` | `72.35` | 32,960,000.00 USD | 0.00 USD | 1,480,000.00 USD | `-24.94%` | `20,402.20` |
| `Live` | `Long` | `72.45` | 31,480,000.00 USD | 0.00 USD | 5,600.00 USD | `-24.84%` | `77.33` |
| `Live` | `Long` | `72.55` | 31,480,000.00 USD | 0.00 USD | 13,960.00 USD | `-24.74%` | `192.38` |
| `Live` | `Long` | `72.65` | 31,470,000.00 USD | 0.00 USD | 33,720.00 USD | `-24.63%` | `464.15` |
| `Live` | `Long` | `72.75` | 31,430,000.00 USD | 0.00 USD | 3,690.00 USD | `-24.53%` | `50.79` |
| `Live` | `Long` | `72.85` | 31,430,000.00 USD | 0.00 USD | 190,300.00 USD | `-24.43%` | `2,612.27` |
| `Live` | `Long` | `72.95` | 31,240,000.00 USD | 0.00 USD | 5,600.00 USD | `-24.32%` | `76.71` |
| `Live` | `Long` | `73.05` | 31,230,000.00 USD | 0.00 USD | 46,010.00 USD | `-24.22%` | `629.88` |
| `Live` | `Long` | `73.15` | 31,190,000.00 USD | 0.00 USD | 18,520.00 USD | `-24.11%` | `253.14` |
| `Live` | `Long` | `73.25` | 31,170,000.00 USD | 0.00 USD | 26,730.00 USD | `-24.01%` | `364.96` |
| `Live` | `Long` | `73.35` | 31,140,000.00 USD | 0.00 USD | 21,920.00 USD | `-23.91%` | `298.83` |
| `Live` | `Long` | `73.45` | 31,120,000.00 USD | 0.00 USD | 5,350.00 USD | `-23.80%` | `72.82` |
| `Live` | `Long` | `73.55` | 31,110,000.00 USD | 0.00 USD | 14,850.00 USD | `-23.70%` | `201.89` |
| `Live` | `Long` | `73.65` | 31,100,000.00 USD | 0.00 USD | 37,850.00 USD | `-23.60%` | `513.85` |
| `Live` | `Long` | `73.75` | 31,060,000.00 USD | 0.00 USD | 70,280.00 USD | `-23.49%` | `952.95` |
| `Live` | `Long` | `73.85` | 30,990,000.00 USD | 0.00 USD | 12,370.00 USD | `-23.39%` | `167.54` |
| `Live` | `Long` | `73.95` | 30,980,000.00 USD | 0.00 USD | 40,040.00 USD | `-23.28%` | `541.40` |
| `Live` | `Long` | `74.05` | 30,940,000.00 USD | 0.00 USD | 25,190.00 USD | `-23.18%` | `340.24` |
| `Live` | `Long` | `74.15` | 30,910,000.00 USD | 0.00 USD | 21,430.00 USD | `-23.08%` | `289.03` |
| `Live` | `Long` | `74.25` | 30,890,000.00 USD | 0.00 USD | 26,460.00 USD | `-22.97%` | `356.31` |
| `Live` | `Long` | `74.35` | 30,860,000.00 USD | 0.00 USD | 40,040.00 USD | `-22.87%` | `538.50` |
| `Live` | `Long` | `74.45` | 30,820,000.00 USD | 0.00 USD | 22,440.00 USD | `-22.77%` | `301.36` |
| `Live` | `Long` | `74.55` | 30,800,000.00 USD | 0.00 USD | 15,670.00 USD | `-22.66%` | `210.23` |
| `Live` | `Long` | `74.65` | 30,790,000.00 USD | 0.00 USD | 1,030.00 USD | `-22.56%` | `13.82` |
| `Live` | `Long` | `74.75` | 30,790,000.00 USD | 0.00 USD | 123,840.00 USD | `-22.45%` | `1,656.66` |
| `Live` | `Long` | `74.85` | 30,660,000.00 USD | 0.00 USD | 127,450.00 USD | `-22.35%` | `1,702.70` |
| `Live` | `Long` | `74.95` | 30,530,000.00 USD | 0.00 USD | 18,090.00 USD | `-22.25%` | `241.37` |
| `Live` | `Long` | `75.05` | 30,520,000.00 USD | 0.00 USD | 40,670.00 USD | `-22.14%` | `541.85` |
| `Live` | `Long` | `75.25` | 30,480,000.00 USD | 0.00 USD | 287,360.00 USD | `-21.94%` | `3,818.68` |
| `Live` | `Long` | `75.35` | 30,190,000.00 USD | 0.00 USD | 18,360.00 USD | `-21.83%` | `243.67` |
| `Live` | `Long` | `75.45` | 30,170,000.00 USD | 0.00 USD | 38,660.00 USD | `-21.73%` | `512.34` |
| `Live` | `Long` | `75.55` | 30,130,000.00 USD | 0.00 USD | 35,050.00 USD | `-21.62%` | `463.97` |
| `Live` | `Long` | `75.65` | 30,100,000.00 USD | 0.00 USD | 130,250.00 USD | `-21.52%` | `1,721.70` |
| `Live` | `Long` | `75.75` | 29,970,000.00 USD | 0.00 USD | 60,640.00 USD | `-21.42%` | `800.51` |
| `Live` | `Long` | `75.85` | 29,910,000.00 USD | 0.00 USD | 2,880.00 USD | `-21.31%` | `37.95` |
| `Live` | `Long` | `75.95` | 29,900,000.00 USD | 0.00 USD | 29,830.00 USD | `-21.21%` | `392.72` |
| `Live` | `Long` | `76.15` | 29,870,000.00 USD | 0.00 USD | 4,370.00 USD | `-21.00%` | `57.43` |
| `Live` | `Long` | `76.25` | 29,870,000.00 USD | 0.00 USD | 4,340.00 USD | `-20.90%` | `56.96` |
| `Live` | `Long` | `76.35` | 29,860,000.00 USD | 0.00 USD | 45,780.00 USD | `-20.79%` | `599.62` |
| `Live` | `Long` | `76.45` | 29,820,000.00 USD | 0.00 USD | 1,720,000.00 USD | `-20.69%` | `22,507.44` |
| `Live` | `Long` | `76.55` | 28,100,000.00 USD | 0.00 USD | 37,610.00 USD | `-20.59%` | `491.36` |
| `Live` | `Long` | `76.65` | 28,060,000.00 USD | 0.00 USD | 55,910.00 USD | `-20.48%` | `729.36` |
| `Live` | `Long` | `76.75` | 28,000,000.00 USD | 0.00 USD | 5,060.00 USD | `-20.38%` | `65.89` |
| `Live` | `Long` | `76.85` | 28,000,000.00 USD | 0.00 USD | 135,520.00 USD | `-20.28%` | `1,763.49` |
| `Live` | `Long` | `76.95` | 27,860,000.00 USD | 0.00 USD | 33,790.00 USD | `-20.17%` | `439.09` |
| `Live` | `Long` | `77.05` | 27,830,000.00 USD | 0.00 USD | 80,420.00 USD | `-20.07%` | `1,043.70` |
| `Live` | `Long` | `77.15` | 27,750,000.00 USD | 0.00 USD | 1,740,000.00 USD | `-19.96%` | `22,565.63` |
| `Live` | `Long` | `77.25` | 26,010,000.00 USD | 0.00 USD | 25,180.00 USD | `-19.86%` | `325.91` |
| `Live` | `Long` | `77.35` | 25,980,000.00 USD | 0.00 USD | 5,650.00 USD | `-19.76%` | `73.07` |
| `Live` | `Long` | `77.45` | 25,980,000.00 USD | 0.00 USD | 59,150.00 USD | `-19.65%` | `763.68` |
| `Live` | `Long` | `77.55` | 25,920,000.00 USD | 0.00 USD | 18,400.00 USD | `-19.55%` | `237.26` |
| `Live` | `Long` | `77.65` | 25,900,000.00 USD | 0.00 USD | 3,590.00 USD | `-19.45%` | `46.26` |
| `Live` | `Long` | `77.75` | 25,900,000.00 USD | 0.00 USD | 9,870.00 USD | `-19.34%` | `126.99` |
| `Live` | `Long` | `77.85` | 25,890,000.00 USD | 0.00 USD | 83,670.00 USD | `-19.24%` | `1,074.71` |
| `Live` | `Long` | `77.95` | 25,800,000.00 USD | 0.00 USD | 15,390.00 USD | `-19.13%` | `197.48` |
| `Live` | `Long` | `78.05` | 25,790,000.00 USD | 0.00 USD | 21,520.00 USD | `-19.03%` | `275.71` |
| `Live` | `Long` | `78.15` | 25,770,000.00 USD | 0.00 USD | 63,710.00 USD | `-18.93%` | `815.26` |
| `Live` | `Long` | `78.25` | 25,700,000.00 USD | 0.00 USD | 70,740.00 USD | `-18.82%` | `904.08` |
| `Live` | `Long` | `78.35` | 25,630,000.00 USD | 0.00 USD | 55,060.00 USD | `-18.72%` | `702.76` |
| `Live` | `Long` | `78.45` | 25,580,000.00 USD | 0.00 USD | 26,080.00 USD | `-18.62%` | `332.40` |
| `Live` | `Long` | `78.55` | 25,550,000.00 USD | 0.00 USD | 5,740.00 USD | `-18.51%` | `73.09` |
| `Live` | `Long` | `78.65` | 25,540,000.00 USD | 0.00 USD | 32,860.00 USD | `-18.41%` | `417.75` |
| `Live` | `Long` | `78.75` | 25,510,000.00 USD | 0.00 USD | 52,670.00 USD | `-18.30%` | `668.88` |
| `Live` | `Long` | `78.85` | 25,460,000.00 USD | 0.00 USD | 62,050.00 USD | `-18.20%` | `786.91` |
| `Live` | `Long` | `78.95` | 25,400,000.00 USD | 0.00 USD | 1,370.00 USD | `-18.10%` | `17.33` |
| `Live` | `Long` | `79.05` | 25,400,000.00 USD | 0.00 USD | 6,490.00 USD | `-17.99%` | `82.14` |
| `Live` | `Long` | `79.15` | 25,390,000.00 USD | 0.00 USD | 128,420.00 USD | `-17.89%` | `1,622.43` |
| `Live` | `Long` | `79.25` | 25,260,000.00 USD | 0.00 USD | 47,570.00 USD | `-17.79%` | `600.23` |
| `Live` | `Long` | `79.35` | 25,210,000.00 USD | 0.00 USD | 17,490.00 USD | `-17.68%` | `220.45` |
| `Live` | `Long` | `79.45` | 25,200,000.00 USD | 0.00 USD | 7,750.00 USD | `-17.58%` | `97.50` |
| `Live` | `Long` | `79.55` | 25,190,000.00 USD | 0.00 USD | 6,720.00 USD | `-17.47%` | `84.52` |
| `Live` | `Long` | `79.65` | 25,180,000.00 USD | 0.00 USD | 45,420.00 USD | `-17.37%` | `570.30` |
| `Live` | `Long` | `79.75` | 25,140,000.00 USD | 0.00 USD | 194,630.00 USD | `-17.27%` | `2,440.53` |
| `Live` | `Long` | `79.85` | 24,940,000.00 USD | 0.00 USD | 30,690.00 USD | `-17.16%` | `384.36` |
| `Live` | `Long` | `79.95` | 24,910,000.00 USD | 0.00 USD | 34,220.00 USD | `-17.06%` | `428.08` |
| `Live` | `Long` | `80.05` | 24,880,000.00 USD | 0.00 USD | 40,880.00 USD | `-16.96%` | `510.63` |
| `Live` | `Long` | `80.15` | 24,840,000.00 USD | 0.00 USD | 34,810.00 USD | `-16.85%` | `434.26` |
| `Live` | `Long` | `80.25` | 24,800,000.00 USD | 0.00 USD | 79,220.00 USD | `-16.75%` | `987.16` |
| `Live` | `Long` | `80.35` | 24,720,000.00 USD | 0.00 USD | 107,240.00 USD | `-16.65%` | `1,334.64` |
| `Live` | `Long` | `80.45` | 24,610,000.00 USD | 0.00 USD | 11,550.00 USD | `-16.54%` | `143.59` |
| `Live` | `Long` | `80.55` | 24,600,000.00 USD | 0.00 USD | 16,640.00 USD | `-16.44%` | `206.58` |
| `Live` | `Long` | `80.65` | 24,590,000.00 USD | 0.00 USD | 103,370.00 USD | `-16.33%` | `1,281.68` |
| `Live` | `Long` | `80.75` | 24,480,000.00 USD | 0.00 USD | 52,190.00 USD | `-16.23%` | `646.30` |
| `Live` | `Long` | `80.85` | 24,430,000.00 USD | 0.00 USD | 439,180.00 USD | `-16.13%` | `5,432.01` |
| `Live` | `Long` | `80.95` | 23,990,000.00 USD | 0.00 USD | 25,480.00 USD | `-16.02%` | `314.80` |
| `Live` | `Long` | `81.05` | 23,970,000.00 USD | 0.00 USD | 2,230,000.00 USD | `-15.92%` | `27,457.97` |
| `Live` | `Long` | `81.15` | 21,740,000.00 USD | 0.00 USD | 89,300.00 USD | `-15.82%` | `1,100.39` |
| `Live` | `Long` | `81.25` | 21,650,000.00 USD | 0.00 USD | 22,790.00 USD | `-15.71%` | `280.49` |
| `Live` | `Long` | `81.35` | 21,630,000.00 USD | 0.00 USD | 50,550.00 USD | `-15.61%` | `621.37` |
| `Live` | `Long` | `81.45` | 21,580,000.00 USD | 0.00 USD | 68,010.00 USD | `-15.50%` | `834.94` |
| `Live` | `Long` | `81.55` | 21,510,000.00 USD | 0.00 USD | 190,680.00 USD | `-15.40%` | `2,338.18` |
| `Live` | `Long` | `81.65` | 21,320,000.00 USD | 0.00 USD | 20,720.00 USD | `-15.30%` | `253.76` |
| `Live` | `Long` | `81.75` | 21,300,000.00 USD | 0.00 USD | 18,650.00 USD | `-15.19%` | `228.11` |
| `Live` | `Long` | `81.85` | 21,280,000.00 USD | 0.00 USD | 35,560.00 USD | `-15.09%` | `434.40` |
| `Live` | `Long` | `81.95` | 21,240,000.00 USD | 0.00 USD | 153,360.00 USD | `-14.99%` | `1,871.43` |
| `Live` | `Long` | `82.05` | 21,090,000.00 USD | 0.00 USD | 123,570.00 USD | `-14.88%` | `1,506.01` |
| `Live` | `Long` | `82.15` | 20,970,000.00 USD | 0.00 USD | 804,530.00 USD | `-14.78%` | `9,793.43` |
| `Live` | `Long` | `82.25` | 20,160,000.00 USD | 0.00 USD | 43,580.00 USD | `-14.67%` | `529.88` |
| `Live` | `Long` | `82.35` | 20,120,000.00 USD | 0.00 USD | 158,370.00 USD | `-14.57%` | `1,923.09` |
| `Live` | `Long` | `82.45` | 19,960,000.00 USD | 0.00 USD | 218,740.00 USD | `-14.47%` | `2,652.97` |
| `Live` | `Long` | `82.55` | 19,740,000.00 USD | 0.00 USD | 18,190.00 USD | `-14.36%` | `220.40` |
| `Live` | `Long` | `82.65` | 19,720,000.00 USD | 0.00 USD | 184,500.00 USD | `-14.26%` | `2,232.25` |
| `Live` | `Long` | `82.75` | 19,540,000.00 USD | 0.00 USD | 7,950.00 USD | `-14.16%` | `96.13` |
| `Live` | `Long` | `82.85` | 19,530,000.00 USD | 0.00 USD | 58,610.00 USD | `-14.05%` | `707.39` |
| `Live` | `Long` | `82.95` | 19,470,000.00 USD | 0.00 USD | 23,300.00 USD | `-13.95%` | `280.94` |
| `Live` | `Long` | `83.05` | 19,450,000.00 USD | 0.00 USD | 107,130.00 USD | `-13.84%` | `1,289.96` |
| `Live` | `Long` | `83.15` | 19,340,000.00 USD | 0.00 USD | 44,400.00 USD | `-13.74%` | `534.02` |
| `Live` | `Long` | `83.25` | 19,300,000.00 USD | 0.00 USD | 160,260.00 USD | `-13.64%` | `1,925.04` |
| `Live` | `Long` | `83.35` | 19,140,000.00 USD | 0.00 USD | 274,420.00 USD | `-13.53%` | `3,292.33` |
| `Live` | `Long` | `83.45` | 18,860,000.00 USD | 0.00 USD | 54,190.00 USD | `-13.43%` | `649.42` |
| `Live` | `Long` | `83.55` | 18,810,000.00 USD | 0.00 USD | 20,900.00 USD | `-13.33%` | `250.12` |
| `Live` | `Long` | `83.65` | 18,790,000.00 USD | 0.00 USD | 130,030.00 USD | `-13.22%` | `1,554.46` |
| `Live` | `Long` | `83.75` | 18,660,000.00 USD | 0.00 USD | 81,510.00 USD | `-13.12%` | `973.24` |
| `Live` | `Long` | `83.85` | 18,580,000.00 USD | 0.00 USD | 11,040.00 USD | `-13.01%` | `131.62` |
| `Live` | `Long` | `83.95` | 18,570,000.00 USD | 0.00 USD | 98,980.00 USD | `-12.91%` | `1,178.98` |
| `Live` | `Long` | `84.05` | 18,470,000.00 USD | 0.00 USD | 113,380.00 USD | `-12.81%` | `1,348.96` |
| `Live` | `Long` | `84.15` | 18,350,000.00 USD | 0.00 USD | 66,390.00 USD | `-12.70%` | `788.98` |
| `Live` | `Long` | `84.25` | 18,290,000.00 USD | 0.00 USD | 49,770.00 USD | `-12.60%` | `590.78` |
| `Live` | `Long` | `84.35` | 18,240,000.00 USD | 0.00 USD | 397,070.00 USD | `-12.50%` | `4,707.45` |
| `Live` | `Long` | `84.45` | 17,840,000.00 USD | 0.00 USD | 85,770.00 USD | `-12.39%` | `1,015.66` |
| `Live` | `Long` | `84.55` | 17,750,000.00 USD | 0.00 USD | 5,900.00 USD | `-12.29%` | `69.79` |
| `Live` | `Long` | `84.65` | 17,750,000.00 USD | 0.00 USD | 1,330,000.00 USD | `-12.18%` | `15,710.69` |
| `Live` | `Long` | `84.75` | 16,420,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-12.08%` | `12,268.62` |
| `Live` | `Long` | `84.85` | 15,380,000.00 USD | 0.00 USD | 95,670.00 USD | `-11.98%` | `1,127.48` |
| `Live` | `Long` | `84.95` | 15,280,000.00 USD | 0.00 USD | 162,040.00 USD | `-11.87%` | `1,907.46` |
| `Live` | `Long` | `85.05` | 15,120,000.00 USD | 0.00 USD | 15,920.00 USD | `-11.77%` | `187.17` |
| `Live` | `Long` | `85.15` | 15,100,000.00 USD | 0.00 USD | 7,430.00 USD | `-11.67%` | `87.29` |
| `Live` | `Long` | `85.25` | 15,100,000.00 USD | 0.00 USD | 618,490.00 USD | `-11.56%` | `7,255.05` |
| `Live` | `Long` | `85.35` | 14,480,000.00 USD | 0.00 USD | 20,970.00 USD | `-11.46%` | `245.72` |
| `Live` | `Long` | `85.45` | 14,460,000.00 USD | 0.00 USD | 66,690.00 USD | `-11.35%` | `780.41` |
| `Live` | `Long` | `85.55` | 14,390,000.00 USD | 0.00 USD | 11,200.00 USD | `-11.25%` | `130.93` |
| `Live` | `Long` | `85.65` | 14,380,000.00 USD | 0.00 USD | 43,620.00 USD | `-11.15%` | `509.33` |
| `Live` | `Long` | `85.75` | 14,340,000.00 USD | 0.00 USD | 9,640.00 USD | `-11.04%` | `112.40` |
| `Live` | `Long` | `85.85` | 14,330,000.00 USD | 0.00 USD | 73,630.00 USD | `-10.94%` | `857.62` |
| `Live` | `Long` | `85.95` | 14,250,000.00 USD | 0.00 USD | 360,250.00 USD | `-10.84%` | `4,191.38` |
| `Live` | `Long` | `86.05` | 13,890,000.00 USD | 0.00 USD | 138,200.00 USD | `-10.73%` | `1,606.03` |
| `Live` | `Long` | `86.15` | 13,750,000.00 USD | 0.00 USD | 51,580.00 USD | `-10.63%` | `598.73` |
| `Live` | `Long` | `86.25` | 13,700,000.00 USD | 0.00 USD | 52,570.00 USD | `-10.52%` | `609.53` |
| `Live` | `Long` | `86.35` | 13,650,000.00 USD | 0.00 USD | 3,860.00 USD | `-10.42%` | `44.73` |
| `Live` | `Long` | `86.45` | 13,650,000.00 USD | 0.00 USD | 188,400.00 USD | `-10.32%` | `2,179.28` |
| `Live` | `Long` | `86.55` | 13,460,000.00 USD | 0.00 USD | 30,640.00 USD | `-10.21%` | `353.96` |
| `Live` | `Long` | `86.65` | 13,430,000.00 USD | 0.00 USD | 190,730.00 USD | `-10.11%` | `2,201.12` |
| `Live` | `Long` | `86.75` | 13,240,000.00 USD | 0.00 USD | 35,070.00 USD | `-10.01%` | `404.31` |
| `Live` | `Long` | `86.85` | 13,200,000.00 USD | 0.00 USD | 75,910.00 USD | `-9.90%` | `874.00` |
| `Live` | `Long` | `86.95` | 13,130,000.00 USD | 0.00 USD | 152,510.00 USD | `-9.80%` | `1,754.01` |
| `Live` | `Long` | `87.05` | 12,970,000.00 USD | 0.00 USD | 30,500.00 USD | `-9.69%` | `350.43` |
| `Live` | `Long` | `87.15` | 12,940,000.00 USD | 0.00 USD | 20,150.00 USD | `-9.59%` | `231.21` |
| `Live` | `Long` | `87.25` | 12,920,000.00 USD | 0.00 USD | 93,120.00 USD | `-9.49%` | `1,067.25` |
| `Live` | `Long` | `87.35` | 12,830,000.00 USD | 0.00 USD | 72,050.00 USD | `-9.38%` | `824.89` |
| `Live` | `Long` | `87.45` | 12,760,000.00 USD | 0.00 USD | 151,520.00 USD | `-9.28%` | `1,732.68` |
| `Live` | `Long` | `87.55` | 12,610,000.00 USD | 0.00 USD | 128,170.00 USD | `-9.18%` | `1,463.96` |
| `Live` | `Long` | `87.65` | 12,480,000.00 USD | 0.00 USD | 105,970.00 USD | `-9.07%` | `1,208.96` |
| `Live` | `Long` | `87.75` | 12,370,000.00 USD | 0.00 USD | 30,700.00 USD | `-8.97%` | `349.86` |
| `Live` | `Long` | `87.85` | 12,340,000.00 USD | 0.00 USD | 66,830.00 USD | `-8.86%` | `760.69` |
| `Live` | `Long` | `87.95` | 12,270,000.00 USD | 0.00 USD | 162,530.00 USD | `-8.76%` | `1,847.96` |
| `Live` | `Long` | `88.05` | 12,110,000.00 USD | 0.00 USD | 62,640.00 USD | `-8.66%` | `711.44` |
| `Live` | `Long` | `88.15` | 12,050,000.00 USD | 0.00 USD | 21,240.00 USD | `-8.55%` | `240.98` |
| `Live` | `Long` | `88.25` | 12,030,000.00 USD | 0.00 USD | 74,760.00 USD | `-8.45%` | `847.09` |
| `Live` | `Long` | `88.35` | 11,950,000.00 USD | 0.00 USD | 26,970.00 USD | `-8.35%` | `305.29` |
| `Live` | `Long` | `88.45` | 11,930,000.00 USD | 0.00 USD | 129,160.00 USD | `-8.24%` | `1,460.28` |
| `Live` | `Long` | `88.55` | 11,800,000.00 USD | 0.00 USD | 251,040.00 USD | `-8.14%` | `2,834.96` |
| `Live` | `Long` | `88.65` | 11,550,000.00 USD | 0.00 USD | 96,310.00 USD | `-8.03%` | `1,086.46` |
| `Live` | `Long` | `88.75` | 11,450,000.00 USD | 0.00 USD | 168,880.00 USD | `-7.93%` | `1,902.89` |
| `Live` | `Long` | `88.85` | 11,280,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-7.83%` | `11,930.59` |
| `Live` | `Long` | `88.95` | 10,220,000.00 USD | 0.00 USD | 36,710.00 USD | `-7.72%` | `412.71` |
| `Live` | `Long` | `89.05` | 10,180,000.00 USD | 0.00 USD | 40,570.00 USD | `-7.62%` | `455.59` |
| `Live` | `Long` | `89.15` | 10,140,000.00 USD | 0.00 USD | 160,460.00 USD | `-7.52%` | `1,799.88` |
| `Live` | `Long` | `89.25` | 9,980,000.00 USD | 0.00 USD | 31,740.00 USD | `-7.41%` | `355.61` |
| `Live` | `Long` | `89.35` | 9,950,000.00 USD | 0.00 USD | 42,390.00 USD | `-7.31%` | `474.42` |
| `Live` | `Long` | `89.45` | 9,910,000.00 USD | 0.00 USD | 511,650.00 USD | `-7.20%` | `5,719.99` |
| `Live` | `Long` | `89.55` | 9,400,000.00 USD | 0.00 USD | 64,040.00 USD | `-7.10%` | `715.09` |
| `Live` | `Long` | `89.65` | 9,330,000.00 USD | 0.00 USD | 22,300.00 USD | `-7.00%` | `248.69` |
| `Live` | `Long` | `89.75` | 9,310,000.00 USD | 0.00 USD | 134,870.00 USD | `-6.89%` | `1,502.76` |
| `Live` | `Long` | `89.85` | 9,180,000.00 USD | 0.00 USD | 56,560.00 USD | `-6.79%` | `629.54` |
| `Live` | `Long` | `89.95` | 9,120,000.00 USD | 0.00 USD | 77,970.00 USD | `-6.69%` | `866.84` |
| `Live` | `Long` | `90.05` | 9,040,000.00 USD | 0.00 USD | 38,720.00 USD | `-6.58%` | `430.03` |
| `Live` | `Long` | `90.15` | 9,000,000.00 USD | 0.00 USD | 77,700.00 USD | `-6.48%` | `861.87` |
| `Live` | `Long` | `90.25` | 8,920,000.00 USD | 0.00 USD | 44,640.00 USD | `-6.37%` | `494.61` |
| `Live` | `Long` | `90.35` | 8,880,000.00 USD | 0.00 USD | 77,210.00 USD | `-6.27%` | `854.62` |
| `Live` | `Long` | `90.45` | 8,800,000.00 USD | 0.00 USD | 41,960.00 USD | `-6.17%` | `463.95` |
| `Live` | `Long` | `90.55` | 8,760,000.00 USD | 0.00 USD | 85,260.00 USD | `-6.06%` | `941.55` |
| `Live` | `Long` | `90.65` | 8,680,000.00 USD | 0.00 USD | 116,340.00 USD | `-5.96%` | `1,283.37` |
| `Live` | `Long` | `90.75` | 8,560,000.00 USD | 0.00 USD | 84,390.00 USD | `-5.86%` | `929.89` |
| `Live` | `Long` | `90.85` | 8,480,000.00 USD | 0.00 USD | 74,130.00 USD | `-5.75%` | `815.96` |
| `Live` | `Long` | `90.95` | 8,400,000.00 USD | 0.00 USD | 39,770.00 USD | `-5.65%` | `437.23` |
| `Live` | `Long` | `91.05` | 8,360,000.00 USD | 0.00 USD | 413,880.00 USD | `-5.54%` | `4,545.58` |
| `Live` | `Long` | `91.15` | 7,950,000.00 USD | 0.00 USD | 282,790.00 USD | `-5.44%` | `3,102.48` |
| `Live` | `Long` | `91.25` | 7,660,000.00 USD | 0.00 USD | 44,170.00 USD | `-5.34%` | `484.10` |
| `Live` | `Long` | `91.35` | 7,620,000.00 USD | 0.00 USD | 14,960.00 USD | `-5.23%` | `163.74` |
| `Live` | `Long` | `91.45` | 7,610,000.00 USD | 0.00 USD | 347,480.00 USD | `-5.13%` | `3,799.62` |
| `Live` | `Long` | `91.55` | 7,260,000.00 USD | 0.00 USD | 1,210,000.00 USD | `-5.03%` | `13,204.29` |
| `Live` | `Long` | `91.65` | 6,050,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-4.92%` | `15,594.68` |
| `Live` | `Long` | `91.75` | 4,620,000.00 USD | 0.00 USD | 237,560.00 USD | `-4.82%` | `2,589.24` |
| `Live` | `Long` | `91.85` | 4,380,000.00 USD | 0.00 USD | 71,640.00 USD | `-4.71%` | `779.93` |
| `Live` | `Long` | `91.95` | 4,310,000.00 USD | 0.00 USD | 35,980.00 USD | `-4.61%` | `391.35` |
| `Live` | `Long` | `92.05` | 4,270,000.00 USD | 0.00 USD | 168,710.00 USD | `-4.51%` | `1,832.79` |
| `Live` | `Long` | `92.15` | 4,110,000.00 USD | 0.00 USD | 328,990.00 USD | `-4.40%` | `3,570.11` |
| `Live` | `Long` | `92.25` | 3,780,000.00 USD | 0.00 USD | 168,960.00 USD | `-4.30%` | `1,831.52` |
| `Live` | `Long` | `92.35` | 3,610,000.00 USD | 0.00 USD | 369,030.00 USD | `-4.20%` | `3,995.96` |
| `Live` | `Long` | `92.45` | 3,240,000.00 USD | 0.00 USD | 117,820.00 USD | `-4.09%` | `1,274.42` |
| `Live` | `Long` | `92.55` | 3,120,000.00 USD | 0.00 USD | 5,040.00 USD | `-3.99%` | `54.41` |
| `Live` | `Long` | `92.65` | 3,120,000.00 USD | 0.00 USD | 15,170.00 USD | `-3.89%` | `163.78` |
| `Live` | `Long` | `92.75` | 3,100,000.00 USD | 0.00 USD | 2,060.00 USD | `-3.78%` | `22.19` |
| `Live` | `Long` | `92.85` | 3,100,000.00 USD | 0.00 USD | 23,420.00 USD | `-3.68%` | `252.19` |
| `Live` | `Long` | `92.95` | 3,080,000.00 USD | 0.00 USD | 5,840.00 USD | `-3.57%` | `62.86` |
| `Live` | `Long` | `93.05` | 3,070,000.00 USD | 0.00 USD | 31,450.00 USD | `-3.47%` | `338.04` |
| `Live` | `Long` | `93.15` | 3,040,000.00 USD | 0.00 USD | 4,940.00 USD | `-3.37%` | `53.02` |
| `Live` | `Long` | `93.25` | 3,030,000.00 USD | 0.00 USD | 63,970.00 USD | `-3.26%` | `686.00` |
| `Live` | `Long` | `93.35` | 2,970,000.00 USD | 0.00 USD | 11,060.00 USD | `-3.16%` | `118.46` |
| `Live` | `Long` | `93.45` | 2,960,000.00 USD | 0.00 USD | 8,060.00 USD | `-3.06%` | `86.26` |
| `Live` | `Long` | `93.55` | 2,950,000.00 USD | 0.00 USD | 19,360.00 USD | `-2.95%` | `206.98` |
| `Live` | `Long` | `93.65` | 2,930,000.00 USD | 0.00 USD | 939,260.00 USD | `-2.85%` | `10,029.52` |
| `Live` | `Long` | `93.75` | 1,990,000.00 USD | 0.00 USD | 10,870.00 USD | `-2.74%` | `115.91` |
| `Live` | `Long` | `93.85` | 1,980,000.00 USD | 0.00 USD | 11,870.00 USD | `-2.64%` | `126.50` |
| `Live` | `Long` | `93.95` | 1,970,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-2.54%` | `12,126.47` |
| `Live` | `Long` | `94.05` | 829,440.00 USD | 0.00 USD | 4,190.00 USD | `-2.43%` | `44.53` |
| `Live` | `Long` | `94.15` | 825,260.00 USD | 0.00 USD | 29,210.00 USD | `-2.33%` | `310.26` |
| `Live` | `Long` | `94.25` | 796,050.00 USD | 0.00 USD | 8,860.00 USD | `-2.23%` | `93.98` |
| `Live` | `Long` | `94.35` | 787,190.00 USD | 0.00 USD | 7,960.00 USD | `-2.12%` | `84.41` |
| `Live` | `Long` | `94.45` | 779,220.00 USD | 0.00 USD | 155,730.00 USD | `-2.02%` | `1,648.85` |
| `Live` | `Long` | `94.55` | 623,490.00 USD | 0.00 USD | 80,330.00 USD | `-1.91%` | `849.62` |
| `Live` | `Long` | `94.65` | 543,160.00 USD | 0.00 USD | 25,780.00 USD | `-1.81%` | `272.42` |
| `Live` | `Long` | `94.75` | 517,370.00 USD | 0.00 USD | 82,080.00 USD | `-1.71%` | `866.31` |
| `Live` | `Long` | `94.85` | 435,290.00 USD | 0.00 USD | 33,620.00 USD | `-1.60%` | `354.43` |
| `Live` | `Long` | `94.95` | 401,670.00 USD | 0.00 USD | 33,760.00 USD | `-1.50%` | `355.56` |
| `Live` | `Long` | `95.05` | 367,910.00 USD | 0.00 USD | 57,160.00 USD | `-1.40%` | `601.41` |
| `Live` | `Long` | `95.15` | 310,750.00 USD | 0.00 USD | 20,130.00 USD | `-1.29%` | `211.59` |
| `Live` | `Long` | `95.25` | 290,620.00 USD | 0.00 USD | 42,330.00 USD | `-1.19%` | `444.46` |
| `Live` | `Long` | `95.35` | 248,280.00 USD | 0.00 USD | 7,350.00 USD | `-1.08%` | `77.08` |
| `Live` | `Long` | `95.45` | 240,930.00 USD | 0.00 USD | 23,550.00 USD | `-0.98%` | `246.70` |
| `Live` | `Long` | `95.55` | 217,380.00 USD | 0.00 USD | 44,090.00 USD | `-0.88%` | `461.42` |
| `Live` | `Long` | `95.65` | 173,300.00 USD | 0.00 USD | 92,490.00 USD | `-0.77%` | `966.99` |
| `Live` | `Long` | `95.75` | 80,800.00 USD | 0.00 USD | 49,860.00 USD | `-0.67%` | `520.70` |
| `Live` | `Long` | `95.85` | 30,950.00 USD | 0.00 USD | 30,710.00 USD | `-0.57%` | `320.44` |
| `Live` | `Long` | `95.95` | 231.24 USD | 0.00 USD | 231.24 USD | `-0.46%` | `2.41` |
| `Live` | `Short` | `96.75` | 12,160.00 USD | 12,160.00 USD | 0.00 USD | `+0.37%` | `125.72` |
| `Live` | `Short` | `98.55` | 18,090.00 USD | 5,930.00 USD | 0.00 USD | `+2.24%` | `60.17` |
| `Live` | `Short` | `98.85` | 21,390.00 USD | 3,300.00 USD | 0.00 USD | `+2.55%` | `33.40` |
| `Live` | `Short` | `98.95` | 22,410.00 USD | 1,020.00 USD | 0.00 USD | `+2.65%` | `10.28` |
| `Live` | `Short` | `99.05` | 62,210.00 USD | 39,790.00 USD | 0.00 USD | `+2.75%` | `401.76` |
| `Live` | `Short` | `99.15` | 1,210,000.00 USD | 1,150,000.00 USD | 0.00 USD | `+2.86%` | `11,548.97` |
| `Live` | `Short` | `99.25` | 1,230,000.00 USD | 20,260.00 USD | 0.00 USD | `+2.96%` | `204.12` |
| `Live` | `Short` | `99.35` | 1,320,000.00 USD | 96,300.00 USD | 0.00 USD | `+3.07%` | `969.32` |
| `Live` | `Short` | `99.45` | 1,350,000.00 USD | 24,220.00 USD | 0.00 USD | `+3.17%` | `243.54` |
| `Live` | `Short` | `99.55` | 1,360,000.00 USD | 14,200.00 USD | 0.00 USD | `+3.27%` | `142.63` |
| `Live` | `Short` | `99.65` | 1,380,000.00 USD | 15,630.00 USD | 0.00 USD | `+3.38%` | `156.84` |
| `Live` | `Short` | `99.75` | 1,400,000.00 USD | 26,990.00 USD | 0.00 USD | `+3.48%` | `270.61` |
| `Live` | `Short` | `99.85` | 1,410,000.00 USD | 410.38 USD | 0.00 USD | `+3.58%` | `4.11` |
| `Live` | `Short` | `99.95` | 1,410,000.00 USD | 4,010.00 USD | 0.00 USD | `+3.69%` | `40.15` |
| `Live` | `Short` | `100.05` | 1,450,000.00 USD | 36,990.00 USD | 0.00 USD | `+3.79%` | `369.67` |
| `Live` | `Short` | `100.15` | 1,470,000.00 USD | 25,710.00 USD | 0.00 USD | `+3.90%` | `256.74` |
| `Live` | `Short` | `100.25` | 1,820,000.00 USD | 347,460.00 USD | 0.00 USD | `+4.00%` | `3,465.93` |
| `Live` | `Short` | `100.35` | 2,210,000.00 USD | 391,910.00 USD | 0.00 USD | `+4.10%` | `3,905.45` |
| `Live` | `Short` | `100.45` | 2,220,000.00 USD | 6,010.00 USD | 0.00 USD | `+4.21%` | `59.81` |
| `Live` | `Short` | `100.55` | 2,220,000.00 USD | 1,510.00 USD | 0.00 USD | `+4.31%` | `15.00` |
| `Live` | `Short` | `100.65` | 2,320,000.00 USD | 101,930.00 USD | 0.00 USD | `+4.41%` | `1,012.76` |
| `Live` | `Short` | `100.75` | 2,340,000.00 USD | 20,210.00 USD | 0.00 USD | `+4.52%` | `200.63` |
| `Live` | `Short` | `100.85` | 2,400,000.00 USD | 62,360.00 USD | 0.00 USD | `+4.62%` | `618.31` |
| `Live` | `Short` | `100.95` | 2,420,000.00 USD | 18,180.00 USD | 0.00 USD | `+4.73%` | `180.12` |
| `Live` | `Short` | `101.05` | 2,430,000.00 USD | 8,240.00 USD | 0.00 USD | `+4.83%` | `81.52` |
| `Live` | `Short` | `101.15` | 2,440,000.00 USD | 14,160.00 USD | 0.00 USD | `+4.93%` | `140.03` |
| `Live` | `Short` | `101.25` | 2,440,000.00 USD | 769.50 USD | 0.00 USD | `+5.04%` | `7.60` |
| `Live` | `Short` | `101.35` | 2,450,000.00 USD | 922.29 USD | 0.00 USD | `+5.14%` | `9.10` |
| `Live` | `Short` | `101.45` | 2,450,000.00 USD | 118.70 USD | 0.00 USD | `+5.24%` | `1.17` |
| `Live` | `Short` | `101.55` | 2,450,000.00 USD | 2,790.00 USD | 0.00 USD | `+5.35%` | `27.47` |
| `Live` | `Short` | `101.65` | 2,450,000.00 USD | 2,640.00 USD | 0.00 USD | `+5.45%` | `26.02` |
| `Live` | `Short` | `101.95` | 2,450,000.00 USD | 1,560.00 USD | 0.00 USD | `+5.76%` | `15.31` |
| `Live` | `Short` | `102.05` | 2,460,000.00 USD | 4,280.00 USD | 0.00 USD | `+5.87%` | `41.98` |
| `Live` | `Short` | `102.25` | 2,460,000.00 USD | 1,890.00 USD | 0.00 USD | `+6.07%` | `18.48` |
| `Live` | `Short` | `102.65` | 2,460,000.00 USD | 1,070.00 USD | 0.00 USD | `+6.49%` | `10.45` |
| `Live` | `Short` | `102.75` | 2,460,000.00 USD | 3,340.00 USD | 0.00 USD | `+6.59%` | `32.53` |
| `Live` | `Short` | `102.85` | 2,460,000.00 USD | 654.13 USD | 0.00 USD | `+6.70%` | `6.36` |
| `Live` | `Short` | `102.95` | 2,470,000.00 USD | 4,150.00 USD | 0.00 USD | `+6.80%` | `40.32` |
| `Live` | `Short` | `103.05` | 2,470,000.00 USD | 1,060.00 USD | 0.00 USD | `+6.90%` | `10.24` |
| `Live` | `Short` | `103.15` | 2,480,000.00 USD | 14,800.00 USD | 0.00 USD | `+7.01%` | `143.46` |
| `Live` | `Short` | `103.25` | 2,480,000.00 USD | 206.50 USD | 0.00 USD | `+7.11%` | `2.00` |
| `Live` | `Short` | `103.35` | 2,480,000.00 USD | 385.50 USD | 0.00 USD | `+7.22%` | `3.73` |
| `Live` | `Short` | `103.45` | 2,490,000.00 USD | 3,300.00 USD | 0.00 USD | `+7.32%` | `31.94` |
| `Live` | `Short` | `103.65` | 2,490,000.00 USD | 4,360.00 USD | 0.00 USD | `+7.53%` | `42.09` |
| `Live` | `Short` | `103.75` | 2,750,000.00 USD | 261,050.00 USD | 0.00 USD | `+7.63%` | `2,516.13` |
| `Live` | `Short` | `103.85` | 2,770,000.00 USD | 14,630.00 USD | 0.00 USD | `+7.73%` | `140.89` |
| `Live` | `Short` | `103.95` | 2,770,000.00 USD | 827.44 USD | 0.00 USD | `+7.84%` | `7.96` |
| `Live` | `Short` | `104.05` | 2,770,000.00 USD | 1,110.00 USD | 0.00 USD | `+7.94%` | `10.66` |
| `Live` | `Short` | `104.15` | 2,770,000.00 USD | 1,180.00 USD | 0.00 USD | `+8.05%` | `11.34` |
| `Live` | `Short` | `104.25` | 2,810,000.00 USD | 40,840.00 USD | 0.00 USD | `+8.15%` | `391.71` |
| `Live` | `Short` | `104.35` | 2,830,000.00 USD | 14,580.00 USD | 0.00 USD | `+8.25%` | `139.68` |
| `Live` | `Short` | `104.45` | 2,840,000.00 USD | 9,560.00 USD | 0.00 USD | `+8.36%` | `91.52` |
| `Live` | `Short` | `104.55` | 2,840,000.00 USD | 575.03 USD | 0.00 USD | `+8.46%` | `5.50` |
| `Live` | `Short` | `104.65` | 2,840,000.00 USD | 401.86 USD | 0.00 USD | `+8.56%` | `3.84` |
| `Live` | `Short` | `104.75` | 2,840,000.00 USD | 3,620.00 USD | 0.00 USD | `+8.67%` | `34.59` |
| `Live` | `Short` | `104.85` | 2,870,000.00 USD | 31,470.00 USD | 0.00 USD | `+8.77%` | `300.15` |
| `Live` | `Short` | `104.95` | 3,000,000.00 USD | 125,660.00 USD | 0.00 USD | `+8.87%` | `1,197.29` |
| `Live` | `Short` | `105.05` | 3,000,000.00 USD | 578.83 USD | 0.00 USD | `+8.98%` | `5.51` |
| `Live` | `Short` | `105.15` | 3,010,000.00 USD | 13,330.00 USD | 0.00 USD | `+9.08%` | `126.78` |
| `Live` | `Short` | `105.25` | 3,010,000.00 USD | 2,110.00 USD | 0.00 USD | `+9.19%` | `20.07` |
| `Live` | `Short` | `105.35` | 3,020,000.00 USD | 6,840.00 USD | 0.00 USD | `+9.29%` | `64.89` |
| `Live` | `Short` | `105.45` | 3,550,000.00 USD | 531,450.00 USD | 0.00 USD | `+9.39%` | `5,039.81` |
| `Live` | `Short` | `105.55` | 3,560,000.00 USD | 4,180.00 USD | 0.00 USD | `+9.50%` | `39.61` |
| `Live` | `Short` | `105.65` | 3,560,000.00 USD | 1,950.00 USD | 0.00 USD | `+9.60%` | `18.49` |
| `Live` | `Short` | `105.75` | 3,560,000.00 USD | 4,160.00 USD | 0.00 USD | `+9.70%` | `39.37` |
| `Live` | `Short` | `105.85` | 3,650,000.00 USD | 91,370.00 USD | 0.00 USD | `+9.81%` | `863.23` |
| `Live` | `Short` | `105.95` | 3,650,000.00 USD | 592.26 USD | 0.00 USD | `+9.91%` | `5.59` |
| `Live` | `Short` | `106.05` | 3,690,000.00 USD | 33,380.00 USD | 0.00 USD | `+10.02%` | `314.77` |
| `Live` | `Short` | `106.25` | 3,690,000.00 USD | 1,970.00 USD | 0.00 USD | `+10.22%` | `18.57` |
| `Live` | `Short` | `106.35` | 3,950,000.00 USD | 256,690.00 USD | 0.00 USD | `+10.33%` | `2,413.61` |
| `Live` | `Short` | `106.45` | 4,160,000.00 USD | 216,090.00 USD | 0.00 USD | `+10.43%` | `2,029.98` |
| `Live` | `Short` | `106.55` | 4,160,000.00 USD | 219.49 USD | 0.00 USD | `+10.53%` | `2.06` |
| `Live` | `Short` | `106.65` | 4,170,000.00 USD | 6,680.00 USD | 0.00 USD | `+10.64%` | `62.64` |
| `Live` | `Short` | `106.85` | 4,650,000.00 USD | 479,350.00 USD | 0.00 USD | `+10.85%` | `4,486.21` |
| `Live` | `Short` | `106.95` | 4,650,000.00 USD | 131.55 USD | 0.00 USD | `+10.95%` | `1.23` |
| `Live` | `Short` | `107.05` | 4,660,000.00 USD | 14,600.00 USD | 0.00 USD | `+11.05%` | `136.36` |
| `Live` | `Short` | `107.15` | 4,670,000.00 USD | 3,060.00 USD | 0.00 USD | `+11.16%` | `28.58` |
| `Live` | `Short` | `107.25` | 4,700,000.00 USD | 34,950.00 USD | 0.00 USD | `+11.26%` | `325.92` |
| `Live` | `Short` | `107.35` | 4,700,000.00 USD | 766.48 USD | 0.00 USD | `+11.36%` | `7.14` |
| `Live` | `Short` | `107.45` | 4,730,000.00 USD | 32,580.00 USD | 0.00 USD | `+11.47%` | `303.18` |
| `Live` | `Short` | `107.55` | 4,740,000.00 USD | 221.55 USD | 0.00 USD | `+11.57%` | `2.06` |
| `Live` | `Short` | `107.85` | 4,880,000.00 USD | 143,340.00 USD | 0.00 USD | `+11.88%` | `1,329.08` |
| `Live` | `Short` | `107.95` | 4,890,000.00 USD | 8,330.00 USD | 0.00 USD | `+11.99%` | `77.19` |
| `Live` | `Short` | `108.05` | 4,890,000.00 USD | 1,080.00 USD | 0.00 USD | `+12.09%` | `10.04` |
| `Live` | `Short` | `108.15` | 4,890,000.00 USD | 1,150.00 USD | 0.00 USD | `+12.19%` | `10.66` |
| `Live` | `Short` | `108.25` | 5,050,000.00 USD | 162,440.00 USD | 0.00 USD | `+12.30%` | `1,500.57` |
| `Live` | `Short` | `108.35` | 5,050,000.00 USD | 3,470.00 USD | 0.00 USD | `+12.40%` | `32.00` |
| `Live` | `Short` | `108.45` | 5,160,000.00 USD | 108,080.00 USD | 0.00 USD | `+12.51%` | `996.61` |
| `Live` | `Short` | `108.55` | 5,160,000.00 USD | 381.01 USD | 0.00 USD | `+12.61%` | `3.51` |
| `Live` | `Short` | `108.65` | 5,170,000.00 USD | 5,050.00 USD | 0.00 USD | `+12.71%` | `46.45` |
| `Live` | `Short` | `108.85` | 5,170,000.00 USD | 3,980.00 USD | 0.00 USD | `+12.92%` | `36.58` |
| `Live` | `Short` | `108.95` | 5,180,000.00 USD | 3,170.00 USD | 0.00 USD | `+13.02%` | `29.10` |
| `Live` | `Short` | `109.05` | 5,180,000.00 USD | 356.59 USD | 0.00 USD | `+13.13%` | `3.27` |
| `Live` | `Short` | `109.25` | 9,620,000.00 USD | 4,450,000.00 USD | 0.00 USD | `+13.34%` | `40,716.81` |
| `Live` | `Short` | `109.35` | 9,640,000.00 USD | 20,440.00 USD | 0.00 USD | `+13.44%` | `186.91` |
| `Live` | `Short` | `109.45` | 9,650,000.00 USD | 426.86 USD | 0.00 USD | `+13.54%` | `3.90` |
| `Live` | `Short` | `109.55` | 9,650,000.00 USD | 356.04 USD | 0.00 USD | `+13.65%` | `3.25` |
| `Live` | `Short` | `109.65` | 9,680,000.00 USD | 38,750.00 USD | 0.00 USD | `+13.75%` | `353.42` |
| `Live` | `Short` | `109.75` | 10,090,000.00 USD | 408,730.00 USD | 0.00 USD | `+13.85%` | `3,724.17` |
| `Live` | `Short` | `109.85` | 10,090,000.00 USD | 459.17 USD | 0.00 USD | `+13.96%` | `4.18` |
| `Live` | `Short` | `109.95` | 10,090,000.00 USD | 301.26 USD | 0.00 USD | `+14.06%` | `2.74` |
| `Live` | `Short` | `110.05` | 10,110,000.00 USD | 14,790.00 USD | 0.00 USD | `+14.17%` | `134.36` |
| `Live` | `Short` | `110.15` | 10,140,000.00 USD | 33,240.00 USD | 0.00 USD | `+14.27%` | `301.77` |
| `Live` | `Short` | `110.25` | 10,140,000.00 USD | 226.01 USD | 0.00 USD | `+14.37%` | `2.05` |
| `Live` | `Short` | `110.35` | 10,290,000.00 USD | 143,450.00 USD | 0.00 USD | `+14.48%` | `1,299.99` |
| `Live` | `Short` | `110.45` | 10,290,000.00 USD | 376.63 USD | 0.00 USD | `+14.58%` | `3.41` |
| `Live` | `Short` | `110.55` | 10,290,000.00 USD | 203.41 USD | 0.00 USD | `+14.68%` | `1.84` |
| `Live` | `Short` | `110.85` | 10,310,000.00 USD | 28,970.00 USD | 0.00 USD | `+15.00%` | `261.31` |
| `Live` | `Short` | `110.95` | 10,320,000.00 USD | 4,450.00 USD | 0.00 USD | `+15.10%` | `40.12` |
| `Live` | `Short` | `111.15` | 10,320,000.00 USD | 1,710.00 USD | 0.00 USD | `+15.31%` | `15.37` |
| `Live` | `Short` | `111.35` | 10,320,000.00 USD | 390.84 USD | 0.00 USD | `+15.51%` | `3.51` |
| `Live` | `Short` | `111.45` | 10,320,000.00 USD | 841.45 USD | 0.00 USD | `+15.62%` | `7.55` |
| `Live` | `Short` | `111.55` | 10,320,000.00 USD | 892.40 USD | 0.00 USD | `+15.72%` | `8.00` |
| `Live` | `Short` | `111.65` | 10,320,000.00 USD | 199.85 USD | 0.00 USD | `+15.83%` | `1.79` |
| `Live` | `Short` | `111.75` | 10,320,000.00 USD | 169.86 USD | 0.00 USD | `+15.93%` | `1.52` |
| `Live` | `Short` | `111.85` | 10,340,000.00 USD | 15,880.00 USD | 0.00 USD | `+16.03%` | `141.95` |
| `Live` | `Short` | `111.95` | 10,340,000.00 USD | 223.90 USD | 0.00 USD | `+16.14%` | `2.00` |
| `Live` | `Short` | `112.05` | 10,340,000.00 USD | 1,640.00 USD | 0.00 USD | `+16.24%` | `14.66` |
| `Live` | `Short` | `112.15` | 10,340,000.00 USD | 291.59 USD | 0.00 USD | `+16.34%` | `2.60` |
| `Live` | `Short` | `112.35` | 10,600,000.00 USD | 262,980.00 USD | 0.00 USD | `+16.55%` | `2,340.72` |
| `Live` | `Short` | `112.45` | 10,610,000.00 USD | 5,670.00 USD | 0.00 USD | `+16.66%` | `50.42` |
| `Live` | `Short` | `112.55` | 10,610,000.00 USD | 1,070.00 USD | 0.00 USD | `+16.76%` | `9.55` |
| `Live` | `Short` | `112.65` | 10,610,000.00 USD | 707.44 USD | 0.00 USD | `+16.86%` | `6.28` |
| `Live` | `Short` | `112.75` | 10,730,000.00 USD | 118,640.00 USD | 0.00 USD | `+16.97%` | `1,052.24` |
| `Live` | `Short` | `112.85` | 10,840,000.00 USD | 108,760.00 USD | 0.00 USD | `+17.07%` | `963.76` |
| `Live` | `Short` | `113.05` | 10,840,000.00 USD | 406.98 USD | 0.00 USD | `+17.28%` | `3.60` |
| `Live` | `Short` | `113.15` | 10,880,000.00 USD | 37,800.00 USD | 0.00 USD | `+17.38%` | `334.03` |
| `Live` | `Short` | `113.25` | 10,880,000.00 USD | 698.75 USD | 0.00 USD | `+17.49%` | `6.17` |
| `Live` | `Short` | `113.35` | 10,880,000.00 USD | 4,970.00 USD | 0.00 USD | `+17.59%` | `43.83` |
| `Live` | `Short` | `113.45` | 10,890,000.00 USD | 3,360.00 USD | 0.00 USD | `+17.69%` | `29.62` |
| `Live` | `Short` | `113.55` | 10,900,000.00 USD | 17,470.00 USD | 0.00 USD | `+17.80%` | `153.86` |
| `Live` | `Short` | `113.65` | 10,910,000.00 USD | 4,360.00 USD | 0.00 USD | `+17.90%` | `38.38` |
| `Live` | `Short` | `113.75` | 11,020,000.00 USD | 107,800.00 USD | 0.00 USD | `+18.00%` | `947.67` |
| `Live` | `Short` | `113.85` | 11,020,000.00 USD | 2,470.00 USD | 0.00 USD | `+18.11%` | `21.72` |
| `Live` | `Short` | `113.95` | 11,040,000.00 USD | 21,840.00 USD | 0.00 USD | `+18.21%` | `191.69` |
| `Live` | `Short` | `114.05` | 11,070,000.00 USD | 31,740.00 USD | 0.00 USD | `+18.32%` | `278.26` |
| `Live` | `Short` | `114.15` | 11,070,000.00 USD | 253.41 USD | 0.00 USD | `+18.42%` | `2.22` |
| `Live` | `Short` | `114.25` | 11,070,000.00 USD | 2,370.00 USD | 0.00 USD | `+18.52%` | `20.72` |
| `Live` | `Short` | `114.45` | 11,080,000.00 USD | 3,830.00 USD | 0.00 USD | `+18.73%` | `33.46` |
| `Live` | `Short` | `114.65` | 11,080,000.00 USD | 3,430.00 USD | 0.00 USD | `+18.94%` | `29.93` |
| `Live` | `Short` | `115.05` | 11,650,000.00 USD | 569,550.00 USD | 0.00 USD | `+19.35%` | `4,950.49` |
| `Live` | `Short` | `115.15` | 11,650,000.00 USD | 1,100.00 USD | 0.00 USD | `+19.46%` | `9.52` |
| `Live` | `Short` | `115.25` | 11,650,000.00 USD | 1,260.00 USD | 0.00 USD | `+19.56%` | `10.94` |
| `Live` | `Short` | `115.45` | 12,530,000.00 USD | 879,040.00 USD | 0.00 USD | `+19.77%` | `7,614.00` |
| `Live` | `Short` | `115.55` | 12,700,000.00 USD | 167,330.00 USD | 0.00 USD | `+19.87%` | `1,448.12` |
| `Live` | `Short` | `115.65` | 12,710,000.00 USD | 5,970.00 USD | 0.00 USD | `+19.98%` | `51.58` |
| `Live` | `Short` | `115.75` | 12,720,000.00 USD | 14,920.00 USD | 0.00 USD | `+20.08%` | `128.93` |
| `Live` | `Short` | `115.85` | 12,720,000.00 USD | 289.62 USD | 0.00 USD | `+20.18%` | `2.50` |
| `Live` | `Short` | `116.05` | 12,730,000.00 USD | 5,930.00 USD | 0.00 USD | `+20.39%` | `51.14` |
| `Live` | `Short` | `116.25` | 12,730,000.00 USD | 6,270.00 USD | 0.00 USD | `+20.60%` | `53.91` |
| `Live` | `Short` | `116.35` | 12,740,000.00 USD | 4,960.00 USD | 0.00 USD | `+20.70%` | `42.60` |
| `Live` | `Short` | `116.55` | 12,740,000.00 USD | 2,040.00 USD | 0.00 USD | `+20.91%` | `17.52` |
| `Live` | `Short` | `116.65` | 12,740,000.00 USD | 113.15 USD | 0.00 USD | `+21.01%` | `0.97` |
| `Live` | `Short` | `116.85` | 12,750,000.00 USD | 10,520.00 USD | 0.00 USD | `+21.22%` | `90.00` |
| `Live` | `Short` | `117.05` | 12,750,000.00 USD | 156.85 USD | 0.00 USD | `+21.43%` | `1.34` |
| `Live` | `Short` | `117.15` | 12,840,000.00 USD | 89,950.00 USD | 0.00 USD | `+21.53%` | `767.80` |
| `Live` | `Short` | `117.35` | 12,850,000.00 USD | 11,610.00 USD | 0.00 USD | `+21.74%` | `98.95` |
| `Live` | `Short` | `117.55` | 12,850,000.00 USD | 635.95 USD | 0.00 USD | `+21.95%` | `5.41` |
| `Live` | `Short` | `117.75` | 12,860,000.00 USD | 10,360.00 USD | 0.00 USD | `+22.15%` | `87.98` |
| `Live` | `Short` | `117.95` | 12,870,000.00 USD | 1,890.00 USD | 0.00 USD | `+22.36%` | `16.05` |
| `Live` | `Short` | `118.25` | 12,880,000.00 USD | 9,280.00 USD | 0.00 USD | `+22.67%` | `78.51` |
| `Live` | `Short` | `118.45` | 12,910,000.00 USD | 30,080.00 USD | 0.00 USD | `+22.88%` | `253.91` |
| `Live` | `Short` | `118.55` | 12,910,000.00 USD | 7,700.00 USD | 0.00 USD | `+22.98%` | `64.98` |
| `Live` | `Short` | `118.65` | 17,400,000.00 USD | 4,480,000.00 USD | 0.00 USD | `+23.09%` | `37,796.13` |
| `Live` | `Short` | `118.75` | 17,400,000.00 USD | 309.94 USD | 0.00 USD | `+23.19%` | `2.61` |
| `Live` | `Short` | `118.85` | 17,400,000.00 USD | 5,750.00 USD | 0.00 USD | `+23.29%` | `48.34` |
| `Live` | `Short` | `119.25` | 17,400,000.00 USD | 240.88 USD | 0.00 USD | `+23.71%` | `2.02` |
| `Live` | `Short` | `119.35` | 17,460,000.00 USD | 58,320.00 USD | 0.00 USD | `+23.81%` | `488.65` |
| `Live` | `Short` | `119.55` | 17,470,000.00 USD | 8,970.00 USD | 0.00 USD | `+24.02%` | `75.00` |
| `Live` | `Short` | `119.75` | 17,470,000.00 USD | 261.06 USD | 0.00 USD | `+24.23%` | `2.18` |
| `Live` | `Short` | `119.85` | 17,470,000.00 USD | 485.39 USD | 0.00 USD | `+24.33%` | `4.05` |
| `Live` | `Short` | `120.15` | 17,500,000.00 USD | 31,040.00 USD | 0.00 USD | `+24.64%` | `258.38` |
| `Live` | `Short` | `120.25` | 17,600,000.00 USD | 97,590.00 USD | 0.00 USD | `+24.75%` | `811.55` |
| `Live` | `Short` | `120.35` | 17,600,000.00 USD | 145.62 USD | 0.00 USD | `+24.85%` | `1.21` |
| `Live` | `Short` | `120.45` | 17,600,000.00 USD | 968.42 USD | 0.00 USD | `+24.95%` | `8.04` |
| `Live` | `Short` | `120.55` | 17,600,000.00 USD | 1,190.00 USD | 0.00 USD | `+25.06%` | `9.86` |
| `Live` | `Short` | `120.65` | 17,600,000.00 USD | 1,110.00 USD | 0.00 USD | `+25.16%` | `9.19` |
| `Live` | `Short` | `120.85` | 17,600,000.00 USD | 123.27 USD | 0.00 USD | `+25.37%` | `1.02` |
| `Live` | `Short` | `120.95` | 17,620,000.00 USD | 13,290.00 USD | 0.00 USD | `+25.47%` | `109.91` |
| `Live` | `Short` | `121.05` | 17,680,000.00 USD | 60,700.00 USD | 0.00 USD | `+25.58%` | `501.43` |
| `Live` | `Short` | `121.15` | 17,680,000.00 USD | 316.20 USD | 0.00 USD | `+25.68%` | `2.61` |
| `Live` | `Short` | `121.45` | 17,720,000.00 USD | 42,460.00 USD | 0.00 USD | `+25.99%` | `349.58` |
| `Live` | `Short` | `121.55` | 17,730,000.00 USD | 5,940.00 USD | 0.00 USD | `+26.10%` | `48.87` |
| `Live` | `Short` | `121.75` | 17,730,000.00 USD | 105.92 USD | 0.00 USD | `+26.30%` | `0.87` |
| `Live` | `Short` | `122.05` | 17,780,000.00 USD | 56,150.00 USD | 0.00 USD | `+26.61%` | `460.06` |
| `Live` | `Short` | `122.15` | 17,780,000.00 USD | 169.79 USD | 0.00 USD | `+26.72%` | `1.39` |
| `Live` | `Short` | `122.25` | 17,790,000.00 USD | 4,210.00 USD | 0.00 USD | `+26.82%` | `34.46` |
| `Live` | `Short` | `122.45` | 18,690,000.00 USD | 899,680.00 USD | 0.00 USD | `+27.03%` | `7,347.30` |
| `Live` | `Short` | `122.65` | 18,690,000.00 USD | 116.52 USD | 0.00 USD | `+27.24%` | `0.95` |
| `Live` | `Short` | `123.25` | 19,160,000.00 USD | 471,560.00 USD | 0.00 USD | `+27.86%` | `3,826.05` |
| `Live` | `Short` | `123.35` | 19,160,000.00 USD | 2,330.00 USD | 0.00 USD | `+27.96%` | `18.92` |
| `Live` | `Short` | `123.45` | 19,160,000.00 USD | 1,960.00 USD | 0.00 USD | `+28.07%` | `15.87` |
| `Live` | `Short` | `123.75` | 19,290,000.00 USD | 124,610.00 USD | 0.00 USD | `+28.38%` | `1,006.96` |
| `Live` | `Short` | `123.95` | 19,320,000.00 USD | 36,200.00 USD | 0.00 USD | `+28.59%` | `292.09` |
| `Live` | `Short` | `124.05` | 19,320,000.00 USD | 586.76 USD | 0.00 USD | `+28.69%` | `4.73` |
| `Live` | `Short` | `124.15` | 19,320,000.00 USD | 121.67 USD | 0.00 USD | `+28.79%` | `0.98` |
| `Live` | `Short` | `124.25` | 19,350,000.00 USD | 23,360.00 USD | 0.00 USD | `+28.90%` | `188.01` |
| `Live` | `Short` | `124.35` | 19,350,000.00 USD | 775.94 USD | 0.00 USD | `+29.00%` | `6.24` |
| `Live` | `Short` | `124.55` | 24,110,000.00 USD | 4,760,000.00 USD | 0.00 USD | `+29.21%` | `38,235.81` |
| `Live` | `Short` | `124.65` | 24,110,000.00 USD | 675.60 USD | 0.00 USD | `+29.31%` | `5.42` |
| `Live` | `Short` | `124.75` | 24,120,000.00 USD | 5,330.00 USD | 0.00 USD | `+29.42%` | `42.73` |
| `Live` | `Short` | `124.95` | 24,170,000.00 USD | 49,090.00 USD | 0.00 USD | `+29.62%` | `392.91` |
| `Live` | `Short` | `125.05` | 24,170,000.00 USD | 208.83 USD | 0.00 USD | `+29.73%` | `1.67` |
| `Live` | `Short` | `125.15` | 24,170,000.00 USD | 6,260.00 USD | 0.00 USD | `+29.83%` | `50.00` |
| `Live` | `Short` | `125.35` | 24,180,000.00 USD | 5,320.00 USD | 0.00 USD | `+30.04%` | `42.44` |
| `Live` | `Short` | `125.45` | 24,180,000.00 USD | 590.87 USD | 0.00 USD | `+30.14%` | `4.71` |
| `Live` | `Short` | `125.55` | 24,180,000.00 USD | 4,610.00 USD | 0.00 USD | `+30.25%` | `36.71` |
| `Live` | `Short` | `125.65` | 24,180,000.00 USD | 1,560.00 USD | 0.00 USD | `+30.35%` | `12.41` |
| `Live` | `Short` | `125.75` | 24,190,000.00 USD | 1,930.00 USD | 0.00 USD | `+30.45%` | `15.31` |
| `Live` | `Short` | `125.95` | 24,190,000.00 USD | 110.84 USD | 0.00 USD | `+30.66%` | `0.88` |
| `Live` | `Short` | `126.05` | 24,190,000.00 USD | 810.50 USD | 0.00 USD | `+30.76%` | `6.43` |
| `Live` | `Short` | `126.15` | 24,190,000.00 USD | 470.54 USD | 0.00 USD | `+30.87%` | `3.73` |
| `Live` | `Short` | `126.35` | 24,190,000.00 USD | 4,350.00 USD | 0.00 USD | `+31.08%` | `34.43` |
| `Live` | `Short` | `126.45` | 24,200,000.00 USD | 4,880.00 USD | 0.00 USD | `+31.18%` | `38.63` |
| `Live` | `Short` | `126.55` | 24,200,000.00 USD | 403.69 USD | 0.00 USD | `+31.28%` | `3.19` |
| `Live` | `Short` | `126.65` | 24,230,000.00 USD | 30,830.00 USD | 0.00 USD | `+31.39%` | `243.46` |
| `Live` | `Short` | `126.85` | 24,230,000.00 USD | 3,870.00 USD | 0.00 USD | `+31.59%` | `30.49` |
| `Live` | `Short` | `127.05` | 24,230,000.00 USD | 2,030.00 USD | 0.00 USD | `+31.80%` | `16.01` |
| `Live` | `Short` | `127.15` | 24,230,000.00 USD | 389.08 USD | 0.00 USD | `+31.91%` | `3.06` |
| `Live` | `Short` | `127.35` | 24,260,000.00 USD | 29,060.00 USD | 0.00 USD | `+32.11%` | `228.18` |
| `Live` | `Short` | `127.45` | 24,260,000.00 USD | 138.92 USD | 0.00 USD | `+32.22%` | `1.09` |
| `Live` | `Short` | `127.55` | 24,270,000.00 USD | 4,460.00 USD | 0.00 USD | `+32.32%` | `35.00` |
| `Live` | `Short` | `127.65` | 24,270,000.00 USD | 4,840.00 USD | 0.00 USD | `+32.42%` | `37.89` |
| `Live` | `Short` | `127.75` | 24,290,000.00 USD | 20,800.00 USD | 0.00 USD | `+32.53%` | `162.83` |
| `Live` | `Short` | `127.85` | 24,290,000.00 USD | 388.66 USD | 0.00 USD | `+32.63%` | `3.04` |
| `Live` | `Short` | `127.95` | 24,310,000.00 USD | 12,330.00 USD | 0.00 USD | `+32.74%` | `96.34` |
| `Live` | `Short` | `128.05` | 24,420,000.00 USD | 116,190.00 USD | 0.00 USD | `+32.84%` | `907.38` |
| `Live` | `Short` | `128.15` | 24,420,000.00 USD | 1,000.00 USD | 0.00 USD | `+32.94%` | `7.83` |
| `Live` | `Short` | `128.35` | 24,420,000.00 USD | 195.09 USD | 0.00 USD | `+33.15%` | `1.52` |
| `Live` | `Short` | `128.65` | 24,430,000.00 USD | 788.62 USD | 0.00 USD | `+33.46%` | `6.13` |
| `Live` | `Short` | `128.75` | 24,440,000.00 USD | 18,730.00 USD | 0.00 USD | `+33.57%` | `145.45` |
| `Live` | `Short` | `128.85` | 24,480,000.00 USD | 32,440.00 USD | 0.00 USD | `+33.67%` | `251.77` |
| `Live` | `Short` | `129.15` | 24,530,000.00 USD | 55,570.00 USD | 0.00 USD | `+33.98%` | `430.25` |
| `Live` | `Short` | `129.25` | 24,560,000.00 USD | 32,310.00 USD | 0.00 USD | `+34.08%` | `250.00` |
| `Live` | `Short` | `129.35` | 24,600,000.00 USD | 35,060.00 USD | 0.00 USD | `+34.19%` | `271.06` |
| `Live` | `Short` | `129.45` | 24,600,000.00 USD | 730.10 USD | 0.00 USD | `+34.29%` | `5.64` |
| `Live` | `Short` | `129.55` | 24,600,000.00 USD | 910.74 USD | 0.00 USD | `+34.39%` | `7.03` |
| `Live` | `Short` | `129.65` | 25,300,000.00 USD | 700,970.00 USD | 0.00 USD | `+34.50%` | `5,406.67` |
| `Live` | `Short` | `129.75` | 25,300,000.00 USD | 2,210.00 USD | 0.00 USD | `+34.60%` | `17.05` |
| `Live` | `Short` | `129.85` | 25,300,000.00 USD | 490.83 USD | 0.00 USD | `+34.71%` | `3.78` |
| `Live` | `Short` | `130.25` | 25,300,000.00 USD | 145.88 USD | 0.00 USD | `+35.12%` | `1.12` |
| `Live` | `Short` | `130.45` | 25,650,000.00 USD | 343,340.00 USD | 0.00 USD | `+35.33%` | `2,631.99` |
| `Live` | `Short` | `130.85` | 25,650,000.00 USD | 3,180.00 USD | 0.00 USD | `+35.74%` | `24.34` |
| `Live` | `Short` | `130.95` | 25,650,000.00 USD | 2,070.00 USD | 0.00 USD | `+35.85%` | `15.84` |
| `Live` | `Short` | `131.05` | 25,650,000.00 USD | 188.71 USD | 0.00 USD | `+35.95%` | `1.44` |
| `Live` | `Short` | `131.25` | 25,650,000.00 USD | 1,560.00 USD | 0.00 USD | `+36.16%` | `11.87` |
| `Live` | `Short` | `131.35` | 25,670,000.00 USD | 14,210.00 USD | 0.00 USD | `+36.26%` | `108.18` |
| `Live` | `Short` | `131.45` | 25,670,000.00 USD | 219.52 USD | 0.00 USD | `+36.37%` | `1.67` |
| `Live` | `Short` | `131.65` | 25,690,000.00 USD | 17,640.00 USD | 0.00 USD | `+36.57%` | `134.01` |
| `Live` | `Short` | `131.85` | 25,690,000.00 USD | 3,210.00 USD | 0.00 USD | `+36.78%` | `24.35` |
| `Live` | `Short` | `132.05` | 25,690,000.00 USD | 1,710.00 USD | 0.00 USD | `+36.99%` | `12.93` |
| `Live` | `Short` | `132.15` | 25,730,000.00 USD | 33,680.00 USD | 0.00 USD | `+37.09%` | `254.83` |
| `Live` | `Short` | `132.45` | 25,730,000.00 USD | 8,530.00 USD | 0.00 USD | `+37.40%` | `64.37` |
| `Live` | `Short` | `132.55` | 25,730,000.00 USD | 196.17 USD | 0.00 USD | `+37.51%` | `1.48` |
| `Live` | `Short` | `132.65` | 25,730,000.00 USD | 240.10 USD | 0.00 USD | `+37.61%` | `1.81` |
| `Live` | `Short` | `132.75` | 25,730,000.00 USD | 136.73 USD | 0.00 USD | `+37.71%` | `1.03` |
| `Live` | `Short` | `132.85` | 25,780,000.00 USD | 49,280.00 USD | 0.00 USD | `+37.82%` | `370.98` |
| `Live` | `Short` | `133.05` | 25,790,000.00 USD | 1,700.00 USD | 0.00 USD | `+38.03%` | `12.75` |
| `Live` | `Short` | `133.15` | 25,790,000.00 USD | 8,440.00 USD | 0.00 USD | `+38.13%` | `63.42` |
| `Live` | `Short` | `133.25` | 25,800,000.00 USD | 1,330.00 USD | 0.00 USD | `+38.23%` | `9.95` |
| `Live` | `Short` | `133.65` | 25,800,000.00 USD | 156.37 USD | 0.00 USD | `+38.65%` | `1.17` |
| `Live` | `Short` | `133.75` | 25,950,000.00 USD | 151,200.00 USD | 0.00 USD | `+38.75%` | `1,130.50` |
| `Live` | `Short` | `133.95` | 25,950,000.00 USD | 503.65 USD | 0.00 USD | `+38.96%` | `3.76` |
| `Live` | `Short` | `134.05` | 25,960,000.00 USD | 12,620.00 USD | 0.00 USD | `+39.06%` | `94.18` |
| `Live` | `Short` | `134.15` | 25,960,000.00 USD | 2,510.00 USD | 0.00 USD | `+39.17%` | `18.74` |
| `Live` | `Short` | `134.25` | 25,970,000.00 USD | 11,590.00 USD | 0.00 USD | `+39.27%` | `86.32` |
| `Live` | `Short` | `134.95` | 25,970,000.00 USD | 395.40 USD | 0.00 USD | `+40.00%` | `2.93` |
| `Live` | `Short` | `135.45` | 25,990,000.00 USD | 14,560.00 USD | 0.00 USD | `+40.52%` | `107.50` |
| `Live` | `Short` | `135.65` | 25,990,000.00 USD | 415.09 USD | 0.00 USD | `+40.72%` | `3.06` |
| `Live` | `Short` | `135.85` | 26,000,000.00 USD | 9,680.00 USD | 0.00 USD | `+40.93%` | `71.24` |
| `Live` | `Short` | `135.95` | 26,000,000.00 USD | 504.37 USD | 0.00 USD | `+41.03%` | `3.71` |
| `Live` | `Short` | `136.25` | 26,050,000.00 USD | 49,000.00 USD | 0.00 USD | `+41.35%` | `359.64` |
| `Live` | `Short` | `136.45` | 26,050,000.00 USD | 1,500.00 USD | 0.00 USD | `+41.55%` | `11.00` |
| `Live` | `Short` | `136.55` | 26,060,000.00 USD | 8,700.00 USD | 0.00 USD | `+41.66%` | `63.70` |
| `Live` | `Short` | `136.65` | 26,060,000.00 USD | 1,110.00 USD | 0.00 USD | `+41.76%` | `8.14` |
| `Live` | `Short` | `136.95` | 26,090,000.00 USD | 34,240.00 USD | 0.00 USD | `+42.07%` | `250.00` |
| `Live` | `Short` | `137.05` | 26,100,000.00 USD | 836.00 USD | 0.00 USD | `+42.18%` | `6.10` |
| `Live` | `Short` | `137.15` | 26,100,000.00 USD | 809.19 USD | 0.00 USD | `+42.28%` | `5.90` |
| `Live` | `Short` | `137.85` | 26,160,000.00 USD | 68,930.00 USD | 0.00 USD | `+43.01%` | `500.00` |
| `Live` | `Short` | `138.05` | 26,170,000.00 USD | 1,270.00 USD | 0.00 USD | `+43.21%` | `9.20` |
| `Live` | `Short` | `138.15` | 26,210,000.00 USD | 41,450.00 USD | 0.00 USD | `+43.32%` | `300.00` |
| `Live` | `Short` | `138.25` | 26,250,000.00 USD | 45,220.00 USD | 0.00 USD | `+43.42%` | `327.11` |
| `Live` | `Short` | `138.35` | 26,270,000.00 USD | 15,400.00 USD | 0.00 USD | `+43.52%` | `111.33` |
| `Live` | `Short` | `138.45` | 26,280,000.00 USD | 9,370.00 USD | 0.00 USD | `+43.63%` | `67.70` |
| `Live` | `Short` | `138.65` | 26,280,000.00 USD | 4,160.00 USD | 0.00 USD | `+43.84%` | `30.00` |
| `Live` | `Short` | `138.75` | 26,280,000.00 USD | 2,360.00 USD | 0.00 USD | `+43.94%` | `17.04` |
| `Live` | `Short` | `138.85` | 26,290,000.00 USD | 9,290.00 USD | 0.00 USD | `+44.04%` | `66.89` |
| `Live` | `Short` | `139.15` | 26,290,000.00 USD | 552.43 USD | 0.00 USD | `+44.35%` | `3.97` |
| `Live` | `Short` | `139.35` | 26,290,000.00 USD | 253.62 USD | 0.00 USD | `+44.56%` | `1.82` |
| `Live` | `Short` | `139.55` | 26,290,000.00 USD | 494.01 USD | 0.00 USD | `+44.77%` | `3.54` |
| `Live` | `Short` | `139.75` | 26,300,000.00 USD | 4,870.00 USD | 0.00 USD | `+44.98%` | `34.82` |
| `Live` | `Short` | `139.95` | 26,300,000.00 USD | 394.66 USD | 0.00 USD | `+45.18%` | `2.82` |
| `Live` | `Short` | `140.05` | 26,300,000.00 USD | 1,800.00 USD | 0.00 USD | `+45.29%` | `12.85` |
| `Live` | `Short` | `140.35` | 26,300,000.00 USD | 127.72 USD | 0.00 USD | `+45.60%` | `0.91` |
| `Live` | `Short` | `140.45` | 26,310,000.00 USD | 4,870.00 USD | 0.00 USD | `+45.70%` | `34.66` |
| `Live` | `Short` | `140.55` | 26,310,000.00 USD | 8,030.00 USD | 0.00 USD | `+45.81%` | `57.16` |
| `Live` | `Short` | `140.65` | 26,320,000.00 USD | 4,210.00 USD | 0.00 USD | `+45.91%` | `29.93` |
| `Live` | `Short` | `140.95` | 26,320,000.00 USD | 1,940.00 USD | 0.00 USD | `+46.22%` | `13.73` |
| `Live` | `Short` | `141.05` | 26,320,000.00 USD | 3,710.00 USD | 0.00 USD | `+46.33%` | `26.29` |
| `Live` | `Short` | `141.15` | 26,390,000.00 USD | 67,420.00 USD | 0.00 USD | `+46.43%` | `477.67` |
| `Live` | `Short` | `141.35` | 31,490,000.00 USD | 5,100,000.00 USD | 0.00 USD | `+46.64%` | `36,101.07` |
| `Live` | `Short` | `141.45` | 31,740,000.00 USD | 247,540.00 USD | 0.00 USD | `+46.74%` | `1,750.00` |
| `Live` | `Short` | `141.55` | 31,750,000.00 USD | 2,770.00 USD | 0.00 USD | `+46.84%` | `19.56` |
| `Live` | `Short` | `141.65` | 31,750,000.00 USD | 1,220.00 USD | 0.00 USD | `+46.95%` | `8.59` |
| `Live` | `Short` | `141.75` | 31,750,000.00 USD | 2,250.00 USD | 0.00 USD | `+47.05%` | `15.84` |
| `Live` | `Short` | `141.85` | 33,700,000.00 USD | 1,950,000.00 USD | 0.00 USD | `+47.15%` | `13,744.62` |
| `Live` | `Short` | `141.95` | 33,700,000.00 USD | 211.51 USD | 0.00 USD | `+47.26%` | `1.49` |
| `Live` | `Short` | `142.25` | 33,700,000.00 USD | 3,470.00 USD | 0.00 USD | `+47.57%` | `24.41` |
| `Live` | `Short` | `142.35` | 33,770,000.00 USD | 71,180.00 USD | 0.00 USD | `+47.67%` | `500.00` |
| `Live` | `Short` | `142.45` | 33,800,000.00 USD | 23,250.00 USD | 0.00 USD | `+47.78%` | `163.25` |
| `Live` | `Short` | `142.55` | 33,840,000.00 USD | 42,080.00 USD | 0.00 USD | `+47.88%` | `295.19` |
| `Live` | `Short` | `142.65` | 33,930,000.00 USD | 87,970.00 USD | 0.00 USD | `+47.98%` | `616.67` |
| `Live` | `Short` | `142.75` | 33,930,000.00 USD | 368.30 USD | 0.00 USD | `+48.09%` | `2.58` |
| `Live` | `Short` | `143.15` | 33,930,000.00 USD | 1,460.00 USD | 0.00 USD | `+48.50%` | `10.22` |
| `Live` | `Short` | `143.35` | 33,950,000.00 USD | 22,260.00 USD | 0.00 USD | `+48.71%` | `155.27` |
| `Live` | `Short` | `143.45` | 33,950,000.00 USD | 790.41 USD | 0.00 USD | `+48.81%` | `5.51` |
| `Live` | `Short` | `143.55` | 33,950,000.00 USD | 103.36 USD | 0.00 USD | `+48.92%` | `0.72` |
| `Live` | `Short` | `143.65` | 33,950,000.00 USD | 2,840.00 USD | 0.00 USD | `+49.02%` | `19.75` |
| `Live` | `Short` | `143.75` | 33,960,000.00 USD | 1,710.00 USD | 0.00 USD | `+49.13%` | `11.91` |
| `Live` | `Short` | `143.85` | 33,960,000.00 USD | 1,480.00 USD | 0.00 USD | `+49.23%` | `10.26` |
| `Live` | `Short` | `143.95` | 33,960,000.00 USD | 285.02 USD | 0.00 USD | `+49.33%` | `1.98` |
| `Live` | `Short` | `144.05` | 33,960,000.00 USD | 3,750.00 USD | 0.00 USD | `+49.44%` | `26.00` |
| `Live` | `Short` | `144.25` | 34,000,000.00 USD | 34,630.00 USD | 0.00 USD | `+49.64%` | `240.07` |
| `Live` | `Short` | `144.55` | 34,600,000.00 USD | 599,880.00 USD | 0.00 USD | `+49.96%` | `4,150.00` |
| `Live` | `Short` | `144.65` | 34,600,000.00 USD | 1,240.00 USD | 0.00 USD | `+50.06%` | `8.60` |
| `Live` | `Short` | `145.15` | 34,600,000.00 USD | 1,760.00 USD | 0.00 USD | `+50.58%` | `12.12` |
| `Live` | `Short` | `145.25` | 34,600,000.00 USD | 1,090.00 USD | 0.00 USD | `+50.68%` | `7.50` |
| `Live` | `Short` | `145.45` | 34,630,000.00 USD | 28,990.00 USD | 0.00 USD | `+50.89%` | `199.30` |
| `Live` | `Short` | `145.55` | 34,630,000.00 USD | 1,270.00 USD | 0.00 USD | `+50.99%` | `8.75` |
| `Live` | `Short` | `145.75` | 34,630,000.00 USD | 1,340.00 USD | 0.00 USD | `+51.20%` | `9.22` |
| `Live` | `Short` | `145.85` | 34,640,000.00 USD | 5,990.00 USD | 0.00 USD | `+51.30%` | `41.09` |
| `Live` | `Short` | `145.95` | 34,740,000.00 USD | 106,560.00 USD | 0.00 USD | `+51.41%` | `730.14` |
| `Live` | `Short` | `146.15` | 34,830,000.00 USD | 88,760.00 USD | 0.00 USD | `+51.62%` | `607.33` |
| `Live` | `Short` | `146.25` | 34,860,000.00 USD | 22,210.00 USD | 0.00 USD | `+51.72%` | `151.85` |
| `Live` | `Short` | `146.35` | 34,860,000.00 USD | 7,330.00 USD | 0.00 USD | `+51.82%` | `50.10` |
| `Live` | `Short` | `146.45` | 34,860,000.00 USD | 1,400.00 USD | 0.00 USD | `+51.93%` | `9.57` |
| `Live` | `Short` | `146.55` | 34,940,000.00 USD | 74,780.00 USD | 0.00 USD | `+52.03%` | `510.30` |
| `Live` | `Short` | `146.65` | 35,530,000.00 USD | 587,730.00 USD | 0.00 USD | `+52.13%` | `4,007.68` |
| `Live` | `Short` | `146.75` | 35,530,000.00 USD | 493.08 USD | 0.00 USD | `+52.24%` | `3.36` |
| `Live` | `Short` | `146.85` | 35,970,000.00 USD | 442,670.00 USD | 0.00 USD | `+52.34%` | `3,014.41` |
| `Live` | `Short` | `146.95` | 35,970,000.00 USD | 3,340.00 USD | 0.00 USD | `+52.45%` | `22.76` |
| `Live` | `Short` | `147.05` | 35,970,000.00 USD | 166.17 USD | 0.00 USD | `+52.55%` | `1.13` |
| `Live` | `Short` | `147.15` | 36,000,000.00 USD | 30,890.00 USD | 0.00 USD | `+52.65%` | `209.92` |
| `Live` | `Short` | `147.35` | 36,000,000.00 USD | 169.45 USD | 0.00 USD | `+52.86%` | `1.15` |
| `Live` | `Short` | `147.45` | 36,000,000.00 USD | 204.96 USD | 0.00 USD | `+52.96%` | `1.39` |
| `Live` | `Short` | `147.55` | 36,010,000.00 USD | 1,690.00 USD | 0.00 USD | `+53.07%` | `11.48` |
| `Live` | `Short` | `147.65` | 36,010,000.00 USD | 237.72 USD | 0.00 USD | `+53.17%` | `1.61` |
| `Live` | `Short` | `147.85` | 36,010,000.00 USD | 510.08 USD | 0.00 USD | `+53.38%` | `3.45` |
| `Live` | `Short` | `148.15` | 36,010,000.00 USD | 102.22 USD | 0.00 USD | `+53.69%` | `0.69` |
| `Live` | `Short` | `148.45` | 36,010,000.00 USD | 163.29 USD | 0.00 USD | `+54.00%` | `1.10` |
| `Live` | `Short` | `148.55` | 36,350,000.00 USD | 344,780.00 USD | 0.00 USD | `+54.11%` | `2,321.00` |
| `Live` | `Short` | `148.65` | 36,430,000.00 USD | 78,850.00 USD | 0.00 USD | `+54.21%` | `530.42` |
| `Live` | `Short` | `148.75` | 36,530,000.00 USD | 99,350.00 USD | 0.00 USD | `+54.31%` | `667.91` |
| `Live` | `Short` | `148.85` | 37,050,000.00 USD | 520,980.00 USD | 0.00 USD | `+54.42%` | `3,500.00` |
| `Live` | `Short` | `149.55` | 37,050,000.00 USD | 116.65 USD | 0.00 USD | `+55.14%` | `0.78` |
| `Live` | `Short` | `149.65` | 38,460,000.00 USD | 1,410,000.00 USD | 0.00 USD | `+55.25%` | `9,389.48` |
| `Live` | `Short` | `149.85` | 38,580,000.00 USD | 123,060.00 USD | 0.00 USD | `+55.45%` | `821.21` |
| `Live` | `Short` | `149.95` | 38,810,000.00 USD | 234,200.00 USD | 0.00 USD | `+55.56%` | `1,561.87` |
| `Live` | `Short` | `150.05` | 38,820,000.00 USD | 2,930.00 USD | 0.00 USD | `+55.66%` | `19.54` |
| `Live` | `Short` | `150.15` | 38,820,000.00 USD | 642.64 USD | 0.00 USD | `+55.77%` | `4.28` |
| `Live` | `Short` | `150.35` | 38,920,000.00 USD | 105,250.00 USD | 0.00 USD | `+55.97%` | `700.00` |
| `Live` | `Short` | `150.55` | 43,490,000.00 USD | 4,560,000.00 USD | 0.00 USD | `+56.18%` | `30,310.49` |
| `Live` | `Short` | `151.15` | 43,490,000.00 USD | 3,530.00 USD | 0.00 USD | `+56.80%` | `23.35` |
| `Live` | `Short` | `151.25` | 43,490,000.00 USD | 2,370.00 USD | 0.00 USD | `+56.91%` | `15.69` |
| `Live` | `Short` | `151.45` | 43,500,000.00 USD | 8,830.00 USD | 0.00 USD | `+57.11%` | `58.32` |
| `Live` | `Short` | `151.95` | 43,500,000.00 USD | 1,920.00 USD | 0.00 USD | `+57.63%` | `12.64` |
| `Live` | `Short` | `152.25` | 45,370,000.00 USD | 1,860,000.00 USD | 0.00 USD | `+57.94%` | `12,240.90` |
| `Live` | `Short` | `152.35` | 47,400,000.00 USD | 2,040,000.00 USD | 0.00 USD | `+58.05%` | `13,369.14` |
| `Live` | `Short` | `152.45` | 47,450,000.00 USD | 47,900.00 USD | 0.00 USD | `+58.15%` | `314.22` |
| `Live` | `Short` | `152.65` | 47,450,000.00 USD | 615.18 USD | 0.00 USD | `+58.36%` | `4.03` |
| `Live` | `Short` | `152.75` | 47,450,000.00 USD | 1,570.00 USD | 0.00 USD | `+58.46%` | `10.30` |
| `Live` | `Short` | `152.85` | 47,470,000.00 USD | 13,500.00 USD | 0.00 USD | `+58.57%` | `88.35` |
| `Live` | `Short` | `153.05` | 47,470,000.00 USD | 1,060.00 USD | 0.00 USD | `+58.77%` | `6.95` |
| `Live` | `Short` | `153.25` | 47,470,000.00 USD | 239.07 USD | 0.00 USD | `+58.98%` | `1.56` |
| `Live` | `Short` | `153.35` | 47,470,000.00 USD | 2,300.00 USD | 0.00 USD | `+59.09%` | `15.00` |
| `Live` | `Short` | `153.45` | 47,520,000.00 USD | 47,510.00 USD | 0.00 USD | `+59.19%` | `309.63` |
| `Live` | `Short` | `153.65` | 47,530,000.00 USD | 8,340.00 USD | 0.00 USD | `+59.40%` | `54.29` |
| `Live` | `Short` | `153.85` | 47,530,000.00 USD | 995.41 USD | 0.00 USD | `+59.60%` | `6.47` |
| `Live` | `Short` | `154.15` | 47,530,000.00 USD | 292.89 USD | 0.00 USD | `+59.91%` | `1.90` |
| `Live` | `Short` | `154.25` | 47,530,000.00 USD | 2,340.00 USD | 0.00 USD | `+60.02%` | `15.20` |
| `Live` | `Short` | `154.45` | 47,530,000.00 USD | 4,240.00 USD | 0.00 USD | `+60.23%` | `27.45` |
| `Live` | `Short` | `154.75` | 47,530,000.00 USD | 363.66 USD | 0.00 USD | `+60.54%` | `2.35` |
| `Live` | `Short` | `155.05` | 47,540,000.00 USD | 1,500.00 USD | 0.00 USD | `+60.85%` | `9.68` |
| `Live` | `Short` | `155.25` | 47,540,000.00 USD | 3,020.00 USD | 0.00 USD | `+61.06%` | `19.46` |
| `Live` | `Short` | `155.55` | 47,540,000.00 USD | 267.55 USD | 0.00 USD | `+61.37%` | `1.72` |
| `Live` | `Short` | `155.75` | 47,540,000.00 USD | 118.37 USD | 0.00 USD | `+61.57%` | `0.76` |
| `Live` | `Short` | `156.15` | 47,540,000.00 USD | 326.35 USD | 0.00 USD | `+61.99%` | `2.09` |
| `Live` | `Short` | `156.25` | 47,550,000.00 USD | 7,810.00 USD | 0.00 USD | `+62.09%` | `50.00` |
| `Live` | `Short` | `156.35` | 47,550,000.00 USD | 197.00 USD | 0.00 USD | `+62.20%` | `1.26` |
| `Live` | `Short` | `156.45` | 47,550,000.00 USD | 4,900.00 USD | 0.00 USD | `+62.30%` | `31.29` |
| `Live` | `Short` | `156.65` | 47,550,000.00 USD | 1,170.00 USD | 0.00 USD | `+62.51%` | `7.50` |
| `Live` | `Short` | `157.15` | 47,600,000.00 USD | 49,270.00 USD | 0.00 USD | `+63.03%` | `313.50` |
| `Live` | `Short` | `157.65` | 47,600,000.00 USD | 654.25 USD | 0.00 USD | `+63.55%` | `4.15` |
| `Live` | `Short` | `157.75` | 47,700,000.00 USD | 92,600.00 USD | 0.00 USD | `+63.65%` | `587.00` |
| `Live` | `Short` | `158.25` | 47,700,000.00 USD | 299.09 USD | 0.00 USD | `+64.17%` | `1.89` |
| `Live` | `Short` | `158.65` | 47,930,000.00 USD | 237,980.00 USD | 0.00 USD | `+64.58%` | `1,500.00` |
| `Live` | `Short` | `159.05` | 47,980,000.00 USD | 44,690.00 USD | 0.00 USD | `+65.00%` | `281.00` |
| `Live` | `Short` | `159.45` | 47,980,000.00 USD | 2,410.00 USD | 0.00 USD | `+65.41%` | `15.09` |
| `Live` | `Short` | `159.65` | 47,980,000.00 USD | 1,760.00 USD | 0.00 USD | `+65.62%` | `11.01` |
| `Live` | `Short` | `159.75` | 47,980,000.00 USD | 656.57 USD | 0.00 USD | `+65.72%` | `4.11` |
| `Live` | `Short` | `159.85` | 51,620,000.00 USD | 3,640,000.00 USD | 0.00 USD | `+65.83%` | `22,770.74` |
| `Live` | `Short` | `160.15` | 52,310,000.00 USD | 683,000.00 USD | 0.00 USD | `+66.14%` | `4,264.75` |
| `Live` | `Short` | `160.25` | 52,310,000.00 USD | 498.38 USD | 0.00 USD | `+66.24%` | `3.11` |
| `Live` | `Short` | `160.35` | 52,310,000.00 USD | 7,070.00 USD | 0.00 USD | `+66.35%` | `44.12` |
| `Live` | `Short` | `160.55` | 52,310,000.00 USD | 449.54 USD | 0.00 USD | `+66.55%` | `2.80` |
| `Live` | `Short` | `160.75` | 52,750,000.00 USD | 434,020.00 USD | 0.00 USD | `+66.76%` | `2,700.00` |
| `Live` | `Short` | `160.95` | 52,780,000.00 USD | 28,210.00 USD | 0.00 USD | `+66.97%` | `175.30` |
| `Live` | `Short` | `161.05` | 53,030,000.00 USD | 255,020.00 USD | 0.00 USD | `+67.07%` | `1,583.47` |
| `Live` | `Short` | `161.15` | 53,130,000.00 USD | 102,630.00 USD | 0.00 USD | `+67.18%` | `636.89` |
| `Live` | `Short` | `161.25` | 53,140,000.00 USD | 4,120.00 USD | 0.00 USD | `+67.28%` | `25.54` |
| `Live` | `Short` | `161.35` | 53,160,000.00 USD | 21,430.00 USD | 0.00 USD | `+67.38%` | `132.81` |
| `Live` | `Short` | `161.55` | 53,160,000.00 USD | 410.34 USD | 0.00 USD | `+67.59%` | `2.54` |
| `Live` | `Short` | `161.75` | 53,300,000.00 USD | 142,240.00 USD | 0.00 USD | `+67.80%` | `879.39` |
| `Live` | `Short` | `161.95` | 53,450,000.00 USD | 144,610.00 USD | 0.00 USD | `+68.01%` | `892.95` |
| `Live` | `Short` | `162.05` | 53,850,000.00 USD | 405,950.00 USD | 0.00 USD | `+68.11%` | `2,505.07` |
| `Live` | `Short` | `162.15` | 53,860,000.00 USD | 5,970.00 USD | 0.00 USD | `+68.21%` | `36.83` |
| `Live` | `Short` | `162.45` | 53,950,000.00 USD | 86,540.00 USD | 0.00 USD | `+68.53%` | `532.74` |
| `Live` | `Short` | `162.95` | 53,960,000.00 USD | 19,080.00 USD | 0.00 USD | `+69.04%` | `117.09` |
| `Live` | `Short` | `163.85` | 53,970,000.00 USD | 786.48 USD | 0.00 USD | `+69.98%` | `4.80` |
| `Live` | `Short` | `163.95` | 54,170,000.00 USD | 207,900.00 USD | 0.00 USD | `+70.08%` | `1,268.05` |
| `Live` | `Short` | `165.15` | 54,170,000.00 USD | 198.18 USD | 0.00 USD | `+71.33%` | `1.20` |
| `Live` | `Short` | `165.65` | 54,180,000.00 USD | 3,420.00 USD | 0.00 USD | `+71.85%` | `20.63` |
| `Live` | `Short` | `166.05` | 54,180,000.00 USD | 149.45 USD | 0.00 USD | `+72.26%` | `0.90` |
| `Live` | `Short` | `166.15` | 54,180,000.00 USD | 996.90 USD | 0.00 USD | `+72.36%` | `6.00` |
| `Live` | `Short` | `166.25` | 54,190,000.00 USD | 14,070.00 USD | 0.00 USD | `+72.47%` | `84.61` |
| `Live` | `Short` | `166.45` | 54,190,000.00 USD | 1,380.00 USD | 0.00 USD | `+72.67%` | `8.29` |
| `Live` | `Short` | `166.75` | 54,190,000.00 USD | 685.34 USD | 0.00 USD | `+72.99%` | `4.11` |
| `Live` | `Short` | `166.95` | 54,200,000.00 USD | 3,230.00 USD | 0.00 USD | `+73.19%` | `19.33` |
| `Live` | `Short` | `167.65` | 54,200,000.00 USD | 115.68 USD | 0.00 USD | `+73.92%` | `0.69` |
| `Live` | `Short` | `167.75` | 54,200,000.00 USD | 1,890.00 USD | 0.00 USD | `+74.02%` | `11.27` |
| `Live` | `Short` | `168.05` | 54,200,000.00 USD | 122.68 USD | 0.00 USD | `+74.33%` | `0.73` |
| `Live` | `Short` | `168.15` | 54,310,000.00 USD | 111,420.00 USD | 0.00 USD | `+74.44%` | `662.62` |
| `Live` | `Short` | `168.25` | 54,310,000.00 USD | 629.25 USD | 0.00 USD | `+74.54%` | `3.74` |
| `Live` | `Short` | `168.35` | 54,330,000.00 USD | 19,740.00 USD | 0.00 USD | `+74.65%` | `117.24` |
| `Live` | `Short` | `168.65` | 54,660,000.00 USD | 325,850.00 USD | 0.00 USD | `+74.96%` | `1,932.10` |
| `Live` | `Short` | `169.45` | 60,380,000.00 USD | 5,720,000.00 USD | 0.00 USD | `+75.79%` | `33,744.03` |
| `Live` | `Short` | `169.55` | 60,380,000.00 USD | 847.75 USD | 0.00 USD | `+75.89%` | `5.00` |
| `Live` | `Short` | `170.05` | 60,380,000.00 USD | 6,000.00 USD | 0.00 USD | `+76.41%` | `35.27` |
| `Live` | `Short` | `170.75` | 60,380,000.00 USD | 447.37 USD | 0.00 USD | `+77.14%` | `2.62` |
| `Live` | `Short` | `171.45` | 60,380,000.00 USD | 111.44 USD | 0.00 USD | `+77.86%` | `0.65` |
| `Live` | `Short` | `171.75` | 60,570,000.00 USD | 182,360.00 USD | 0.00 USD | `+78.17%` | `1,061.79` |
| `Live` | `Short` | `172.05` | 60,590,000.00 USD | 20,480.00 USD | 0.00 USD | `+78.48%` | `119.02` |
| `Live` | `Short` | `172.45` | 60,640,000.00 USD | 51,730.00 USD | 0.00 USD | `+78.90%` | `300.00` |
| `Live` | `Short` | `172.85` | 60,640,000.00 USD | 1,190.00 USD | 0.00 USD | `+79.31%` | `6.88` |
| `Live` | `Short` | `173.25` | 60,670,000.00 USD | 36,050.00 USD | 0.00 USD | `+79.73%` | `208.07` |
| `Live` | `Short` | `173.35` | 60,670,000.00 USD | 284.29 USD | 0.00 USD | `+79.83%` | `1.64` |
| `Live` | `Short` | `173.45` | 60,690,000.00 USD | 16,540.00 USD | 0.00 USD | `+79.94%` | `95.36` |
| `Live` | `Short` | `173.85` | 60,690,000.00 USD | 695.40 USD | 0.00 USD | `+80.35%` | `4.00` |
| `Live` | `Short` | `173.95` | 60,720,000.00 USD | 25,850.00 USD | 0.00 USD | `+80.46%` | `148.59` |
| `Live` | `Short` | `174.05` | 60,750,000.00 USD | 28,180.00 USD | 0.00 USD | `+80.56%` | `161.92` |
| `Live` | `Short` | `174.15` | 60,850,000.00 USD | 104,490.00 USD | 0.00 USD | `+80.66%` | `600.00` |
| `Live` | `Short` | `174.25` | 61,100,000.00 USD | 245,010.00 USD | 0.00 USD | `+80.77%` | `1,406.07` |
| `Live` | `Short` | `174.35` | 61,300,000.00 USD | 205,490.00 USD | 0.00 USD | `+80.87%` | `1,178.60` |
| `Live` | `Short` | `174.55` | 61,320,000.00 USD | 18,550.00 USD | 0.00 USD | `+81.08%` | `106.26` |
| `Live` | `Short` | `174.75` | 61,320,000.00 USD | 146.79 USD | 0.00 USD | `+81.29%` | `0.84` |
| `Live` | `Short` | `175.35` | 61,320,000.00 USD | 119.24 USD | 0.00 USD | `+81.91%` | `0.68` |
| `Live` | `Short` | `175.75` | 61,320,000.00 USD | 263.62 USD | 0.00 USD | `+82.32%` | `1.50` |
| `Live` | `Short` | `176.05` | 61,320,000.00 USD | 2,960.00 USD | 0.00 USD | `+82.63%` | `16.82` |
| `Live` | `Short` | `176.15` | 61,320,000.00 USD | 350.54 USD | 0.00 USD | `+82.74%` | `1.99` |
| `Live` | `Short` | `176.25` | 61,320,000.00 USD | 625.69 USD | 0.00 USD | `+82.84%` | `3.55` |
| `Live` | `Short` | `176.35` | 61,340,000.00 USD | 19,940.00 USD | 0.00 USD | `+82.95%` | `113.07` |
| `Live` | `Short` | `176.55` | 100,190,000.00 USD | 38,840,000.00 USD | 0.00 USD | `+83.15%` | `220,000.19` |
| `Live` | `Short` | `176.95` | 100,290,000.00 USD | 106,170.00 USD | 0.00 USD | `+83.57%` | `600.00` |
| `Live` | `Short` | `177.05` | 100,760,000.00 USD | 470,750.00 USD | 0.00 USD | `+83.67%` | `2,658.88` |
| `Live` | `Short` | `177.45` | 100,770,000.00 USD | 12,000.00 USD | 0.00 USD | `+84.09%` | `67.60` |
| `Live` | `Short` | `177.65` | 104,330,000.00 USD | 3,550,000.00 USD | 0.00 USD | `+84.29%` | `20,003.59` |
| `Live` | `Short` | `177.95` | 104,410,000.00 USD | 78,300.00 USD | 0.00 USD | `+84.61%` | `440.00` |
| `Live` | `Short` | `178.05` | 104,430,000.00 USD | 25,750.00 USD | 0.00 USD | `+84.71%` | `144.60` |
| `Live` | `Short` | `178.35` | 104,460,000.00 USD | 33,140.00 USD | 0.00 USD | `+85.02%` | `185.84` |
| `Live` | `Short` | `178.45` | 104,470,000.00 USD | 2,440.00 USD | 0.00 USD | `+85.12%` | `13.65` |
| `Live` | `Short` | `178.95` | 104,470,000.00 USD | 2,830.00 USD | 0.00 USD | `+85.64%` | `15.84` |
| `Live` | `Short` | `179.25` | 105,510,000.00 USD | 1,040,000.00 USD | 0.00 USD | `+85.95%` | `5,807.37` |
| `Live` | `Short` | `179.85` | 105,520,000.00 USD | 4,500.00 USD | 0.00 USD | `+86.58%` | `25.00` |
| `Live` | `Short` | `179.95` | 105,520,000.00 USD | 2,030.00 USD | 0.00 USD | `+86.68%` | `11.27` |
| `Live` | `Short` | `180.05` | 105,560,000.00 USD | 45,030.00 USD | 0.00 USD | `+86.78%` | `250.10` |
| `Live` | `Short` | `180.25` | 105,570,000.00 USD | 3,730.00 USD | 0.00 USD | `+86.99%` | `20.70` |
| `Live` | `Short` | `180.35` | 106,910,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+87.09%` | `7,439.01` |
| `Live` | `Short` | `180.55` | 107,060,000.00 USD | 148,410.00 USD | 0.00 USD | `+87.30%` | `822.01` |
| `Live` | `Short` | `180.75` | 107,130,000.00 USD | 72,300.00 USD | 0.00 USD | `+87.51%` | `400.00` |
| `Live` | `Short` | `181.15` | 107,130,000.00 USD | 5,020.00 USD | 0.00 USD | `+87.92%` | `27.73` |
| `Live` | `Short` | `181.25` | 107,150,000.00 USD | 18,120.00 USD | 0.00 USD | `+88.03%` | `100.00` |
| `Live` | `Short` | `181.55` | 107,150,000.00 USD | 254.17 USD | 0.00 USD | `+88.34%` | `1.40` |
| `Live` | `Short` | `181.75` | 107,150,000.00 USD | 727.00 USD | 0.00 USD | `+88.55%` | `4.00` |
| `Live` | `Short` | `182.05` | 107,240,000.00 USD | 91,030.00 USD | 0.00 USD | `+88.86%` | `500.00` |
| `Live` | `Short` | `182.15` | 107,250,000.00 USD | 3,990.00 USD | 0.00 USD | `+88.96%` | `21.93` |
| `Live` | `Short` | `182.75` | 107,250,000.00 USD | 1,370.00 USD | 0.00 USD | `+89.58%` | `7.52` |
| `Live` | `Short` | `184.25` | 107,250,000.00 USD | 1,680.00 USD | 0.00 USD | `+91.14%` | `9.12` |
| `Live` | `Short` | `184.35` | 107,250,000.00 USD | 993.65 USD | 0.00 USD | `+91.24%` | `5.39` |
| `Live` | `Short` | `184.45` | 107,260,000.00 USD | 9,540.00 USD | 0.00 USD | `+91.35%` | `51.72` |
| `Live` | `Short` | `184.95` | 107,430,000.00 USD | 165,230.00 USD | 0.00 USD | `+91.87%` | `893.35` |
| `Live` | `Short` | `185.25` | 107,440,000.00 USD | 13,750.00 USD | 0.00 USD | `+92.18%` | `74.22` |
| `Live` | `Short` | `185.45` | 107,440,000.00 USD | 2,770.00 USD | 0.00 USD | `+92.39%` | `14.94` |
| `Live` | `Short` | `185.65` | 107,450,000.00 USD | 7,830.00 USD | 0.00 USD | `+92.59%` | `42.17` |
| `Live` | `Short` | `186.85` | 107,450,000.00 USD | 2,190.00 USD | 0.00 USD | `+93.84%` | `11.72` |
| `Live` | `Short` | `187.15` | 107,460,000.00 USD | 2,450.00 USD | 0.00 USD | `+94.15%` | `13.11` |
| `Live` | `Short` | `187.65` | 107,460,000.00 USD | 232.69 USD | 0.00 USD | `+94.67%` | `1.24` |
| `Live` | `Short` | `187.85` | 107,460,000.00 USD | 1,560.00 USD | 0.00 USD | `+94.88%` | `8.32` |
| `Live` | `Short` | `188.05` | 111,270,000.00 USD | 3,820,000.00 USD | 0.00 USD | `+95.08%` | `20,287.30` |
| `Live` | `Short` | `188.55` | 111,270,000.00 USD | 231.92 USD | 0.00 USD | `+95.60%` | `1.23` |
| `Live` | `Short` | `188.65` | 111,300,000.00 USD | 29,110.00 USD | 0.00 USD | `+95.71%` | `154.32` |
| `Live` | `Short` | `188.75` | 111,300,000.00 USD | 813.51 USD | 0.00 USD | `+95.81%` | `4.31` |
| `Live` | `Short` | `188.95` | 111,300,000.00 USD | 1,450.00 USD | 0.00 USD | `+96.02%` | `7.69` |
| `Live` | `Short` | `189.15` | 111,300,000.00 USD | 257.24 USD | 0.00 USD | `+96.22%` | `1.36` |
| `Live` | `Short` | `189.25` | 111,300,000.00 USD | 456.09 USD | 0.00 USD | `+96.33%` | `2.41` |
| `Live` | `Short` | `189.55` | 111,310,000.00 USD | 284.33 USD | 0.00 USD | `+96.64%` | `1.50` |
| `Live` | `Short` | `189.65` | 111,310,000.00 USD | 117.58 USD | 0.00 USD | `+96.74%` | `0.62` |
| `Live` | `Short` | `189.75` | 111,310,000.00 USD | 1,010.00 USD | 0.00 USD | `+96.85%` | `5.30` |
| `Live` | `Short` | `189.85` | 111,310,000.00 USD | 189.85 USD | 0.00 USD | `+96.95%` | `1.00` |
| `Live` | `Short` | `189.95` | 111,590,000.00 USD | 284,930.00 USD | 0.00 USD | `+97.05%` | `1,500.00` |
| `Live` | `Short` | `190.15` | 111,590,000.00 USD | 148.32 USD | 0.00 USD | `+97.26%` | `0.78` |
| `Live` | `Short` | `190.45` | 111,590,000.00 USD | 118.08 USD | 0.00 USD | `+97.57%` | `0.62` |
| `Live` | `Short` | `190.65` | 111,590,000.00 USD | 278.35 USD | 0.00 USD | `+97.78%` | `1.46` |
| `Live` | `Short` | `190.95` | 125,160,000.00 USD | 13,570,000.00 USD | 0.00 USD | `+98.09%` | `71,044.42` |
| `Live` | `Short` | `191.15` | 125,160,000.00 USD | 191.15 USD | 0.00 USD | `+98.30%` | `1.00` |
| `Live` | `Short` | `191.25` | 125,160,000.00 USD | 118.58 USD | 0.00 USD | `+98.40%` | `0.62` |
| `Live` | `Short` | `191.55` | 125,220,000.00 USD | 62,850.00 USD | 0.00 USD | `+98.71%` | `328.11` |
| `Live` | `Short` | `191.95` | 125,220,000.00 USD | 322.48 USD | 0.00 USD | `+99.13%` | `1.68` |
| `Live` | `Short` | `192.65` | 125,230,000.00 USD | 9,300.00 USD | 0.00 USD | `+99.85%` | `48.28` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.05` | 10,460,000.00 USD | 0.00 USD | 14,190.00 USD | `-76.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.35` | 10,440,000.00 USD | 0.00 USD | 499.56 USD | `-68.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `32.05` | 10,440,000.00 USD | 0.00 USD | 1,230.00 USD | `-66.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.05` | 10,440,000.00 USD | 0.00 USD | 818.32 USD | `-65.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.85` | 10,440,000.00 USD | 0.00 USD | 1,340.00 USD | `-63.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 10,440,000.00 USD | 0.00 USD | 2,160.00 USD | `-62.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.45` | 10,440,000.00 USD | 0.00 USD | 434.85 USD | `-62.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.05` | 10,440,000.00 USD | 0.00 USD | 267.87 USD | `-60.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.55` | 10,440,000.00 USD | 0.00 USD | 3,460.00 USD | `-58.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.75` | 10,430,000.00 USD | 0.00 USD | 157.01 USD | `-58.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 10,430,000.00 USD | 0.00 USD | 1,050.00 USD | `-58.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.75` | 10,430,000.00 USD | 0.00 USD | 120.66 USD | `-56.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.15` | 10,430,000.00 USD | 0.00 USD | 121.81 USD | `-56.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.55` | 10,430,000.00 USD | 0.00 USD | 170,530.00 USD | `-55.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.75` | 10,260,000.00 USD | 0.00 USD | 105.00 USD | `-54.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 10,260,000.00 USD | 0.00 USD | 64,240.00 USD | `-53.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.75` | 10,200,000.00 USD | 0.00 USD | 251.05 USD | `-51.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.75` | 10,200,000.00 USD | 0.00 USD | 143.25 USD | `-50.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.85` | 10,200,000.00 USD | 0.00 USD | 191.40 USD | `-50.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 10,200,000.00 USD | 0.00 USD | 50,240.00 USD | `-50.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.55` | 10,150,000.00 USD | 0.00 USD | 664.65 USD | `-49.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.75` | 10,150,000.00 USD | 0.00 USD | 103.35 USD | `-49.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 10,150,000.00 USD | 0.00 USD | 4,660.00 USD | `-48.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.25` | 10,140,000.00 USD | 0.00 USD | 107.03 USD | `-47.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 10,140,000.00 USD | 0.00 USD | 102.62 USD | `-47.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.25` | 10,140,000.00 USD | 0.00 USD | 134.28 USD | `-46.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 10,140,000.00 USD | 0.00 USD | 3,950.00 USD | `-46.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.15` | 10,140,000.00 USD | 0.00 USD | 102.74 USD | `-45.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 10,140,000.00 USD | 0.00 USD | 126.12 USD | `-45.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 10,140,000.00 USD | 0.00 USD | 200.15 USD | `-45.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 10,140,000.00 USD | 0.00 USD | 24,450.00 USD | `-44.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 10,110,000.00 USD | 0.00 USD | 1,660.00 USD | `-44.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 10,110,000.00 USD | 0.00 USD | 641.57 USD | `-43.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 10,110,000.00 USD | 0.00 USD | 139.87 USD | `-43.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 10,110,000.00 USD | 0.00 USD | 209.19 USD | `-42.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 10,110,000.00 USD | 0.00 USD | 4,350.00 USD | `-41.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 10,110,000.00 USD | 0.00 USD | 894.56 USD | `-41.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 10,100,000.00 USD | 0.00 USD | 4,930.00 USD | `-41.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 10,100,000.00 USD | 0.00 USD | 6,790.00 USD | `-40.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.35` | 10,090,000.00 USD | 0.00 USD | 265.53 USD | `-40.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.95` | 10,090,000.00 USD | 0.00 USD | 268.31 USD | `-39.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 10,090,000.00 USD | 0.00 USD | 158.48 USD | `-39.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.15` | 10,090,000.00 USD | 0.00 USD | 3,820.00 USD | `-39.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 10,090,000.00 USD | 0.00 USD | 428.72 USD | `-39.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.05` | 10,090,000.00 USD | 0.00 USD | 295.25 USD | `-38.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.35` | 10,090,000.00 USD | 0.00 USD | 200.01 USD | `-38.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.55` | 10,090,000.00 USD | 0.00 USD | 1,460.00 USD | `-38.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.95` | 10,090,000.00 USD | 0.00 USD | 9,040.00 USD | `-37.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.05` | 10,080,000.00 USD | 0.00 USD | 35,050.00 USD | `-37.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.15` | 10,040,000.00 USD | 0.00 USD | 2,820.00 USD | `-37.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.25` | 10,040,000.00 USD | 0.00 USD | 488.63 USD | `-37.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.35` | 10,040,000.00 USD | 0.00 USD | 258.90 USD | `-37.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.45` | 10,040,000.00 USD | 0.00 USD | 206.13 USD | `-37.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.55` | 10,040,000.00 USD | 0.00 USD | 724.78 USD | `-37.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.05` | 10,040,000.00 USD | 0.00 USD | 14,350.00 USD | `-36.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.35` | 10,020,000.00 USD | 0.00 USD | 142.33 USD | `-36.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.45` | 10,020,000.00 USD | 0.00 USD | 100.78 USD | `-36.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.55` | 10,020,000.00 USD | 0.00 USD | 243.74 USD | `-36.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.05` | 10,020,000.00 USD | 0.00 USD | 6,720.00 USD | `-35.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.55` | 10,020,000.00 USD | 0.00 USD | 136.98 USD | `-35.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.05` | 10,020,000.00 USD | 0.00 USD | 9,990.00 USD | `-34.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.55` | 10,010,000.00 USD | 0.00 USD | 2,980.00 USD | `-34.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.95` | 10,000,000.00 USD | 0.00 USD | 222.55 USD | `-33.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.25` | 10,000,000.00 USD | 0.00 USD | 163.19 USD | `-33.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.85` | 10,000,000.00 USD | 0.00 USD | 129.70 USD | `-32.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.05` | 10,000,000.00 USD | 0.00 USD | 2,450.00 USD | `-32.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.15` | 10,000,000.00 USD | 0.00 USD | 2,190.00 USD | `-32.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.55` | 10,000,000.00 USD | 0.00 USD | 2,200.00 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.05` | 9,990,000.00 USD | 0.00 USD | 7,100.00 USD | `-31.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.55` | 9,990,000.00 USD | 0.00 USD | 541.72 USD | `-30.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.05` | 9,990,000.00 USD | 0.00 USD | 335.25 USD | `-30.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.15` | 9,990,000.00 USD | 0.00 USD | 268.60 USD | `-30.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.05` | 9,990,000.00 USD | 0.00 USD | 13,310.00 USD | `-29.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.45` | 9,970,000.00 USD | 0.00 USD | 7,600.00 USD | `-28.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.55` | 9,970,000.00 USD | 0.00 USD | 5,610.00 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.65` | 9,960,000.00 USD | 0.00 USD | 552.63 USD | `-28.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.75` | 9,960,000.00 USD | 0.00 USD | 1,200.00 USD | `-28.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.05` | 9,960,000.00 USD | 0.00 USD | 11,360.00 USD | `-28.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.15` | 9,950,000.00 USD | 0.00 USD | 172.18 USD | `-28.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.25` | 9,950,000.00 USD | 0.00 USD | 668.96 USD | `-28.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.65` | 9,950,000.00 USD | 0.00 USD | 107.96 USD | `-27.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.75` | 9,950,000.00 USD | 0.00 USD | 42,360.00 USD | `-27.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.85` | 9,900,000.00 USD | 0.00 USD | 365.32 USD | `-27.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.95` | 9,900,000.00 USD | 0.00 USD | 1,510.00 USD | `-27.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.05` | 9,900,000.00 USD | 0.00 USD | 43,920.00 USD | `-27.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.25` | 9,860,000.00 USD | 0.00 USD | 5,270.00 USD | `-27.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.35` | 9,850,000.00 USD | 0.00 USD | 562.80 USD | `-27.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.55` | 9,850,000.00 USD | 0.00 USD | 681.51 USD | `-26.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.65` | 9,850,000.00 USD | 0.00 USD | 4,920.00 USD | `-26.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.75` | 9,850,000.00 USD | 0.00 USD | 2,790.00 USD | `-26.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.05` | 9,840,000.00 USD | 0.00 USD | 265.02 USD | `-26.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.35` | 9,840,000.00 USD | 0.00 USD | 32,450.00 USD | `-25.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.45` | 9,810,000.00 USD | 0.00 USD | 289.37 USD | `-25.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.65` | 9,810,000.00 USD | 0.00 USD | 1,930.00 USD | `-25.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.75` | 9,810,000.00 USD | 0.00 USD | 235.34 USD | `-25.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.05` | 9,810,000.00 USD | 0.00 USD | 20,410.00 USD | `-25.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.55` | 9,790,000.00 USD | 0.00 USD | 19,560.00 USD | `-24.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.65` | 9,770,000.00 USD | 0.00 USD | 14,530.00 USD | `-24.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.95` | 9,750,000.00 USD | 0.00 USD | 66,160.00 USD | `-24.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.05` | 9,690,000.00 USD | 0.00 USD | 7,970.00 USD | `-24.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.35` | 9,680,000.00 USD | 0.00 USD | 733.50 USD | `-23.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.45` | 9,680,000.00 USD | 0.00 USD | 139.56 USD | `-23.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.05` | 9,680,000.00 USD | 0.00 USD | 510.95 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.25` | 9,680,000.00 USD | 0.00 USD | 621.47 USD | `-22.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.35` | 9,680,000.00 USD | 0.00 USD | 1,660.00 USD | `-22.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.45` | 9,680,000.00 USD | 0.00 USD | 10,730.00 USD | `-22.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.55` | 9,670,000.00 USD | 0.00 USD | 331.00 USD | `-22.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.75` | 9,670,000.00 USD | 0.00 USD | 28,050.00 USD | `-22.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.05` | 9,640,000.00 USD | 0.00 USD | 27,010.00 USD | `-22.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.35` | 9,610,000.00 USD | 0.00 USD | 153.71 USD | `-21.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.45` | 9,610,000.00 USD | 0.00 USD | 163.73 USD | `-21.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.75` | 9,610,000.00 USD | 0.00 USD | 2,220.00 USD | `-21.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.95` | 9,610,000.00 USD | 0.00 USD | 277.98 USD | `-21.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.05` | 9,610,000.00 USD | 0.00 USD | 8,680.00 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.15` | 9,600,000.00 USD | 0.00 USD | 254.34 USD | `-21.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.25` | 9,600,000.00 USD | 0.00 USD | 486.47 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.35` | 9,600,000.00 USD | 0.00 USD | 358.84 USD | `-20.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.55` | 9,600,000.00 USD | 0.00 USD | 4,340.00 USD | `-20.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.65` | 9,590,000.00 USD | 0.00 USD | 536.55 USD | `-20.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.75` | 9,590,000.00 USD | 0.00 USD | 251.74 USD | `-20.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.05` | 9,590,000.00 USD | 0.00 USD | 5,000.00 USD | `-20.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.35` | 9,590,000.00 USD | 0.00 USD | 5,690.00 USD | `-19.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.45` | 9,580,000.00 USD | 0.00 USD | 1,020.00 USD | `-19.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.55` | 9,580,000.00 USD | 0.00 USD | 242.73 USD | `-19.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.95` | 9,580,000.00 USD | 0.00 USD | 155.12 USD | `-19.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.05` | 9,580,000.00 USD | 0.00 USD | 60,010.00 USD | `-19.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.15` | 9,520,000.00 USD | 0.00 USD | 532.98 USD | `-18.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.55` | 9,520,000.00 USD | 0.00 USD | 18,590.00 USD | `-18.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.65` | 9,500,000.00 USD | 0.00 USD | 116.40 USD | `-18.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.05` | 9,500,000.00 USD | 0.00 USD | 5,300.00 USD | `-17.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.15` | 9,500,000.00 USD | 0.00 USD | 201.04 USD | `-17.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.25` | 9,500,000.00 USD | 0.00 USD | 2,140.00 USD | `-17.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.45` | 9,490,000.00 USD | 0.00 USD | 5,850.00 USD | `-17.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.65` | 9,490,000.00 USD | 0.00 USD | 238.95 USD | `-17.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.75` | 9,490,000.00 USD | 0.00 USD | 1,330.00 USD | `-17.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.85` | 9,490,000.00 USD | 0.00 USD | 289.06 USD | `-17.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.95` | 9,490,000.00 USD | 0.00 USD | 808.29 USD | `-17.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.05` | 9,480,000.00 USD | 0.00 USD | 40,970.00 USD | `-16.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.15` | 9,440,000.00 USD | 0.00 USD | 8,360.00 USD | `-16.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.35` | 9,440,000.00 USD | 0.00 USD | 359.97 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.45` | 9,440,000.00 USD | 0.00 USD | 8,770.00 USD | `-16.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.55` | 9,430,000.00 USD | 0.00 USD | 1,280.00 USD | `-16.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.65` | 9,430,000.00 USD | 0.00 USD | 1,280.00 USD | `-16.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.75` | 9,420,000.00 USD | 0.00 USD | 22,780.00 USD | `-16.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.85` | 9,400,000.00 USD | 0.00 USD | 341.19 USD | `-16.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.05` | 9,400,000.00 USD | 0.00 USD | 1,620.00 USD | `-15.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.25` | 9,400,000.00 USD | 0.00 USD | 266.50 USD | `-15.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.45` | 9,400,000.00 USD | 0.00 USD | 6,260.00 USD | `-15.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.55` | 9,390,000.00 USD | 0.00 USD | 572.48 USD | `-15.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.65` | 9,390,000.00 USD | 0.00 USD | 952.86 USD | `-15.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.75` | 9,390,000.00 USD | 0.00 USD | 1,390.00 USD | `-15.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.85` | 9,390,000.00 USD | 0.00 USD | 818.50 USD | `-15.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.95` | 9,390,000.00 USD | 0.00 USD | 70,900.00 USD | `-14.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.05` | 9,320,000.00 USD | 0.00 USD | 6,750.00 USD | `-14.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.15` | 9,310,000.00 USD | 0.00 USD | 684.31 USD | `-14.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.25` | 9,310,000.00 USD | 0.00 USD | 486.92 USD | `-14.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.35` | 9,310,000.00 USD | 0.00 USD | 386.22 USD | `-14.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.45` | 9,310,000.00 USD | 0.00 USD | 1,870.00 USD | `-14.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.55` | 9,310,000.00 USD | 0.00 USD | 1,310.00 USD | `-14.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.65` | 9,310,000.00 USD | 0.00 USD | 267,390.00 USD | `-14.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.75` | 9,040,000.00 USD | 0.00 USD | 1,660.00 USD | `-14.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.85` | 9,040,000.00 USD | 0.00 USD | 3,270.00 USD | `-14.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.95` | 9,030,000.00 USD | 0.00 USD | 945.63 USD | `-13.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.05` | 9,030,000.00 USD | 0.00 USD | 6,040.00 USD | `-13.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.15` | 9,030,000.00 USD | 0.00 USD | 239.47 USD | `-13.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.25` | 9,030,000.00 USD | 0.00 USD | 18,330.00 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.45` | 9,010,000.00 USD | 0.00 USD | 168.57 USD | `-13.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.55` | 9,010,000.00 USD | 0.00 USD | 421.09 USD | `-13.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.65` | 9,010,000.00 USD | 0.00 USD | 1,100.00 USD | `-13.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.75` | 9,010,000.00 USD | 0.00 USD | 1,320.00 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.95` | 9,010,000.00 USD | 0.00 USD | 4,550.00 USD | `-12.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.05` | 9,000,000.00 USD | 0.00 USD | 40,720.00 USD | `-12.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.15` | 8,960,000.00 USD | 0.00 USD | 25,220.00 USD | `-12.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.25` | 8,940,000.00 USD | 0.00 USD | 2,690.00 USD | `-12.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.45` | 8,930,000.00 USD | 0.00 USD | 965.26 USD | `-12.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.55` | 8,930,000.00 USD | 0.00 USD | 169.95 USD | `-12.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.65` | 8,930,000.00 USD | 0.00 USD | 858.35 USD | `-12.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.75` | 8,930,000.00 USD | 0.00 USD | 306.80 USD | `-12.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.95` | 8,930,000.00 USD | 0.00 USD | 137.62 USD | `-11.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.05` | 8,930,000.00 USD | 0.00 USD | 239,080.00 USD | `-11.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.15` | 8,690,000.00 USD | 0.00 USD | 437.67 USD | `-11.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.25` | 8,690,000.00 USD | 0.00 USD | 1,320.00 USD | `-11.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.35` | 8,690,000.00 USD | 0.00 USD | 39,110.00 USD | `-11.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.45` | 8,650,000.00 USD | 0.00 USD | 120.48 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.55` | 8,650,000.00 USD | 0.00 USD | 105.23 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.65` | 8,650,000.00 USD | 0.00 USD | 493,240.00 USD | `-11.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.75` | 8,160,000.00 USD | 0.00 USD | 1,410.00 USD | `-11.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.85` | 8,160,000.00 USD | 0.00 USD | 360.57 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.95` | 8,150,000.00 USD | 0.00 USD | 2,050.00 USD | `-10.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.05` | 8,150,000.00 USD | 0.00 USD | 10,910.00 USD | `-10.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.15` | 8,140,000.00 USD | 0.00 USD | 2,210.00 USD | `-10.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.25` | 8,140,000.00 USD | 0.00 USD | 163.88 USD | `-10.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.35` | 8,140,000.00 USD | 0.00 USD | 5,710.00 USD | `-10.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.45` | 8,130,000.00 USD | 0.00 USD | 2,790.00 USD | `-10.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.55` | 8,130,000.00 USD | 0.00 USD | 417.17 USD | `-10.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.65` | 8,130,000.00 USD | 0.00 USD | 220,550.00 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.75` | 7,910,000.00 USD | 0.00 USD | 3,060.00 USD | `-10.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.85` | 7,910,000.00 USD | 0.00 USD | 788.60 USD | `-9.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.95` | 7,910,000.00 USD | 0.00 USD | 132.16 USD | `-9.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.05` | 7,910,000.00 USD | 0.00 USD | 283,280.00 USD | `-9.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.15` | 7,620,000.00 USD | 0.00 USD | 23,550.00 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.25` | 7,600,000.00 USD | 0.00 USD | 8,200.00 USD | `-9.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.35` | 7,590,000.00 USD | 0.00 USD | 102.20 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.45` | 7,590,000.00 USD | 0.00 USD | 730.21 USD | `-9.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.55` | 7,590,000.00 USD | 0.00 USD | 1,160.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.65` | 7,590,000.00 USD | 0.00 USD | 2,300.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.85` | 7,590,000.00 USD | 0.00 USD | 131.78 USD | `-8.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.95` | 7,590,000.00 USD | 0.00 USD | 1,410.00 USD | `-8.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.05` | 7,590,000.00 USD | 0.00 USD | 132,850.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.15` | 7,450,000.00 USD | 0.00 USD | 833.02 USD | `-8.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.25` | 7,450,000.00 USD | 0.00 USD | 1,870.00 USD | `-8.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.35` | 7,450,000.00 USD | 0.00 USD | 38,020.00 USD | `-8.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.45` | 7,410,000.00 USD | 0.00 USD | 867.69 USD | `-8.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.55` | 7,410,000.00 USD | 0.00 USD | 32,280.00 USD | `-8.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.65` | 7,380,000.00 USD | 0.00 USD | 27,220.00 USD | `-8.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.75` | 7,350,000.00 USD | 0.00 USD | 53,390.00 USD | `-7.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.85` | 7,300,000.00 USD | 0.00 USD | 91,430.00 USD | `-7.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.95` | 7,210,000.00 USD | 0.00 USD | 141.43 USD | `-7.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.05` | 7,210,000.00 USD | 0.00 USD | 12,930.00 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.15` | 7,190,000.00 USD | 0.00 USD | 6,470.00 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.25` | 7,190,000.00 USD | 0.00 USD | 1,340.00 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.35` | 7,190,000.00 USD | 0.00 USD | 4,220.00 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.45` | 7,180,000.00 USD | 0.00 USD | 5,280.00 USD | `-7.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.55` | 7,180,000.00 USD | 0.00 USD | 348.35 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.65` | 7,180,000.00 USD | 0.00 USD | 192.75 USD | `-7.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.75` | 7,180,000.00 USD | 0.00 USD | 105.01 USD | `-6.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.85` | 7,180,000.00 USD | 0.00 USD | 17,800.00 USD | `-6.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.95` | 7,160,000.00 USD | 0.00 USD | 87,020.00 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.05` | 7,070,000.00 USD | 0.00 USD | 2,350,000.00 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.15` | 4,720,000.00 USD | 0.00 USD | 1,130.00 USD | `-6.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.25` | 4,720,000.00 USD | 0.00 USD | 12,170.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.35` | 4,710,000.00 USD | 0.00 USD | 338.81 USD | `-6.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.45` | 4,710,000.00 USD | 0.00 USD | 5,010.00 USD | `-6.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.55` | 4,700,000.00 USD | 0.00 USD | 12,520.00 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.65` | 4,690,000.00 USD | 0.00 USD | 75,820.00 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.75` | 4,610,000.00 USD | 0.00 USD | 4,980.00 USD | `-5.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.85` | 4,610,000.00 USD | 0.00 USD | 6,580.00 USD | `-5.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.95` | 4,600,000.00 USD | 0.00 USD | 7,300.00 USD | `-5.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.05` | 4,590,000.00 USD | 0.00 USD | 626,620.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.15` | 3,970,000.00 USD | 0.00 USD | 1,120.00 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.25` | 3,970,000.00 USD | 0.00 USD | 1,660.00 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.35` | 3,970,000.00 USD | 0.00 USD | 16,980.00 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.45` | 3,950,000.00 USD | 0.00 USD | 920.90 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.55` | 3,950,000.00 USD | 0.00 USD | 20,520.00 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.65` | 3,930,000.00 USD | 0.00 USD | 37,810.00 USD | `-4.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.75` | 3,890,000.00 USD | 0.00 USD | 21,870.00 USD | `-4.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.85` | 3,870,000.00 USD | 0.00 USD | 41,980.00 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.95` | 3,830,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.05` | 2,780,000.00 USD | 0.00 USD | 268,660.00 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.15` | 2,510,000.00 USD | 0.00 USD | 49,850.00 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.25` | 2,460,000.00 USD | 0.00 USD | 6,810.00 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.35` | 2,460,000.00 USD | 0.00 USD | 20,880.00 USD | `-4.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.45` | 2,440,000.00 USD | 0.00 USD | 132.20 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.55` | 2,440,000.00 USD | 0.00 USD | 937,650.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.65` | 1,500,000.00 USD | 0.00 USD | 59,380.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.75` | 1,440,000.00 USD | 0.00 USD | 7,590.00 USD | `-3.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.85` | 1,430,000.00 USD | 0.00 USD | 32,380.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.95` | 1,400,000.00 USD | 0.00 USD | 14,800.00 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.05` | 1,380,000.00 USD | 0.00 USD | 70,600.00 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.15` | 1,310,000.00 USD | 0.00 USD | 135,720.00 USD | `-3.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.25` | 1,180,000.00 USD | 0.00 USD | 9,220.00 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.35` | 1,170,000.00 USD | 0.00 USD | 23,560.00 USD | `-3.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.45` | 1,150,000.00 USD | 0.00 USD | 7,970.00 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.55` | 1,140,000.00 USD | 0.00 USD | 12,940.00 USD | `-2.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.65` | 1,120,000.00 USD | 0.00 USD | 3,290.00 USD | `-2.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.75` | 1,120,000.00 USD | 0.00 USD | 4,050.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.85` | 1,120,000.00 USD | 0.00 USD | 674.78 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.95` | 1,120,000.00 USD | 0.00 USD | 454.72 USD | `-2.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.05` | 1,120,000.00 USD | 0.00 USD | 111,780.00 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.15` | 1,000,000.00 USD | 0.00 USD | 528.18 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.25` | 1,000,000.00 USD | 0.00 USD | 1,050.00 USD | `-2.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.35` | 1,000,000.00 USD | 0.00 USD | 6,530.00 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.45` | 996,120.00 USD | 0.00 USD | 69,890.00 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.55` | 926,240.00 USD | 0.00 USD | 94,340.00 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.65` | 831,890.00 USD | 0.00 USD | 25,000.00 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.75` | 806,890.00 USD | 0.00 USD | 32,630.00 USD | `-1.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.85` | 774,260.00 USD | 0.00 USD | 15,630.00 USD | `-1.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.95` | 758,630.00 USD | 0.00 USD | 8,370.00 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.05` | 750,260.00 USD | 0.00 USD | 184,930.00 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.15` | 565,340.00 USD | 0.00 USD | 65,810.00 USD | `-1.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.25` | 499,520.00 USD | 0.00 USD | 2,730.00 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.35` | 496,800.00 USD | 0.00 USD | 11,350.00 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.45` | 485,440.00 USD | 0.00 USD | 80,520.00 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.55` | 404,930.00 USD | 0.00 USD | 159,990.00 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.65` | 244,940.00 USD | 0.00 USD | 4,850.00 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.75` | 240,090.00 USD | 0.00 USD | 36,220.00 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.85` | 203,870.00 USD | 0.00 USD | 26,550.00 USD | `-0.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.95` | 177,320.00 USD | 0.00 USD | 32,220.00 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.05` | 145,110.00 USD | 0.00 USD | 31,080.00 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.15` | 114,020.00 USD | 0.00 USD | 34,750.00 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.25` | 79,280.00 USD | 0.00 USD | 14,620.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.35` | 64,660.00 USD | 0.00 USD | 64,660.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.45` | 979,030.00 USD | 979,030.00 USD | 0.00 USD | `+0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.55` | 1,030,000.00 USD | 54,510.00 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.65` | 1,060,000.00 USD | 26,630.00 USD | 0.00 USD | `+0.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.75` | 1,410,000.00 USD | 353,080.00 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.85` | 1,420,000.00 USD | 8,290.00 USD | 0.00 USD | `+0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.95` | 1,420,000.00 USD | 731.97 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.05` | 1,420,000.00 USD | 379.47 USD | 0.00 USD | `+0.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.15` | 1,460,000.00 USD | 38,340.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.25` | 1,490,000.00 USD | 27,460.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.35` | 1,500,000.00 USD | 8,150.00 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.45` | 1,500,000.00 USD | 6,380.00 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.55` | 1,520,000.00 USD | 18,390.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.65` | 1,530,000.00 USD | 6,780.00 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.75` | 1,530,000.00 USD | 4,770.00 USD | 0.00 USD | `+1.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.85` | 1,580,000.00 USD | 48,470.00 USD | 0.00 USD | `+1.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `97.95` | 1,580,000.00 USD | 1,770.00 USD | 0.00 USD | `+1.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,610,000.00 USD | 23,860.00 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.15` | 1,610,000.00 USD | 215.93 USD | 0.00 USD | `+1.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.25` | 1,610,000.00 USD | 1,680.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.35` | 1,620,000.00 USD | 11,510.00 USD | 0.00 USD | `+2.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.45` | 1,640,000.00 USD | 24,200.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.55` | 1,780,000.00 USD | 139,510.00 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.65` | 1,820,000.00 USD | 37,650.00 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.75` | 1,880,000.00 USD | 59,410.00 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.85` | 1,890,000.00 USD | 6,460.00 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.95` | 1,910,000.00 USD | 24,050.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,940,000.00 USD | 27,700.00 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.15` | 1,960,000.00 USD | 16,550.00 USD | 0.00 USD | `+2.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.25` | 1,960,000.00 USD | 6,940.00 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.35` | 2,000,000.00 USD | 39,840.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.45` | 2,000,000.00 USD | 1,770.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.55` | 2,040,000.00 USD | 34,050.00 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.65` | 2,060,000.00 USD | 17,050.00 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.75` | 2,070,000.00 USD | 9,780.00 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.85` | 2,070,000.00 USD | 3,680.00 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.95` | 2,110,000.00 USD | 42,410.00 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 2,710,000.00 USD | 595,650.00 USD | 0.00 USD | `+3.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.15` | 2,720,000.00 USD | 12,360.00 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.25` | 2,720,000.00 USD | 5,030.00 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.35` | 2,730,000.00 USD | 1,250.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.45` | 2,740,000.00 USD | 12,940.00 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.55` | 2,740,000.00 USD | 2,700.00 USD | 0.00 USD | `+4.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.65` | 2,760,000.00 USD | 22,990.00 USD | 0.00 USD | `+4.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.75` | 2,770,000.00 USD | 1,110.00 USD | 0.00 USD | `+4.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.85` | 2,770,000.00 USD | 2,570.00 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.95` | 2,770,000.00 USD | 2,490.00 USD | 0.00 USD | `+4.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.05` | 2,990,000.00 USD | 223,000.00 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.15` | 4,210,000.00 USD | 1,220,000.00 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.25` | 4,220,000.00 USD | 8,940.00 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.35` | 4,230,000.00 USD | 3,850.00 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.45` | 4,230,000.00 USD | 1,450.00 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.55` | 4,240,000.00 USD | 10,050.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.65` | 4,240,000.00 USD | 477.76 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.75` | 4,240,000.00 USD | 648.15 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.85` | 4,240,000.00 USD | 4,720.00 USD | 0.00 USD | `+5.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.95` | 4,240,000.00 USD | 1,080.00 USD | 0.00 USD | `+5.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 4,330,000.00 USD | 83,280.00 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.15` | 4,330,000.00 USD | 231.88 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.25` | 4,330,000.00 USD | 3,080.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.35` | 4,340,000.00 USD | 4,280.00 USD | 0.00 USD | `+6.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.45` | 4,340,000.00 USD | 7,280.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.55` | 4,510,000.00 USD | 168,820.00 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.65` | 4,780,000.00 USD | 268,070.00 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.75` | 4,780,000.00 USD | 1,280.00 USD | 0.00 USD | `+6.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.85` | 4,780,000.00 USD | 1,780.00 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.95` | 4,790,000.00 USD | 4,280.00 USD | 0.00 USD | `+6.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 4,830,000.00 USD | 42,010.00 USD | 0.00 USD | `+6.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 4,830,000.00 USD | 3,180.00 USD | 0.00 USD | `+7.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.25` | 4,900,000.00 USD | 64,080.00 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.35` | 4,900,000.00 USD | 4,260.00 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.45` | 4,900,000.00 USD | 3,860.00 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.55` | 4,930,000.00 USD | 20,580.00 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.65` | 4,940,000.00 USD | 17,250.00 USD | 0.00 USD | `+7.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.75` | 4,940,000.00 USD | 980.44 USD | 0.00 USD | `+7.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.85` | 5,170,000.00 USD | 227,080.00 USD | 0.00 USD | `+7.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.95` | 5,230,000.00 USD | 62,400.00 USD | 0.00 USD | `+7.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.05` | 5,250,000.00 USD | 13,180.00 USD | 0.00 USD | `+7.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.15` | 5,250,000.00 USD | 1,180.00 USD | 0.00 USD | `+8.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.25` | 5,250,000.00 USD | 519.17 USD | 0.00 USD | `+8.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.35` | 5,250,000.00 USD | 323.49 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.45` | 5,340,000.00 USD | 95,950.00 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.55` | 5,370,000.00 USD | 28,290.00 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.65` | 5,370,000.00 USD | 680.23 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.75` | 5,380,000.00 USD | 2,150.00 USD | 0.00 USD | `+8.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.85` | 5,380,000.00 USD | 5,900.00 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.95` | 5,410,000.00 USD | 25,930.00 USD | 0.00 USD | `+8.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.05` | 5,530,000.00 USD | 126,860.00 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.15` | 5,560,000.00 USD | 28,780.00 USD | 0.00 USD | `+9.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.25` | 5,560,000.00 USD | 1,010.00 USD | 0.00 USD | `+9.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.35` | 5,560,000.00 USD | 1,090.00 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.45` | 5,570,000.00 USD | 266.79 USD | 0.00 USD | `+9.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.55` | 5,570,000.00 USD | 3,620.00 USD | 0.00 USD | `+9.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.65` | 5,570,000.00 USD | 1,970.00 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.75` | 5,570,000.00 USD | 549.90 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.85` | 5,580,000.00 USD | 10,600.00 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.95` | 5,590,000.00 USD | 3,620.00 USD | 0.00 USD | `+9.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.05` | 5,610,000.00 USD | 19,780.00 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.15` | 5,610,000.00 USD | 7,080.00 USD | 0.00 USD | `+10.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.25` | 5,610,000.00 USD | 758.62 USD | 0.00 USD | `+10.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.35` | 5,620,000.00 USD | 7,980.00 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.45` | 5,650,000.00 USD | 26,170.00 USD | 0.00 USD | `+10.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.55` | 5,650,000.00 USD | 7,640.00 USD | 0.00 USD | `+10.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.65` | 5,660,000.00 USD | 355.14 USD | 0.00 USD | `+10.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.75` | 5,770,000.00 USD | 110,390.00 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.85` | 5,770,000.00 USD | 1,730.00 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.95` | 5,770,000.00 USD | 2,990.00 USD | 0.00 USD | `+10.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.05` | 5,910,000.00 USD | 142,930.00 USD | 0.00 USD | `+11.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.15` | 5,910,000.00 USD | 109.29 USD | 0.00 USD | `+11.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.25` | 5,930,000.00 USD | 20,190.00 USD | 0.00 USD | `+11.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.35` | 5,930,000.00 USD | 698.85 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.45` | 5,940,000.00 USD | 8,930.00 USD | 0.00 USD | `+11.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.55` | 6,000,000.00 USD | 52,130.00 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.65` | 6,060,000.00 USD | 65,380.00 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.75` | 6,060,000.00 USD | 536.60 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.85` | 6,070,000.00 USD | 11,350.00 USD | 0.00 USD | `+11.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.95` | 6,080,000.00 USD | 9,120.00 USD | 0.00 USD | `+11.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 6,170,000.00 USD | 87,120.00 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.15` | 6,240,000.00 USD | 68,190.00 USD | 0.00 USD | `+12.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.35` | 6,240,000.00 USD | 7,280.00 USD | 0.00 USD | `+12.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.45` | 6,250,000.00 USD | 2,580.00 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.55` | 6,250,000.00 USD | 5,430.00 USD | 0.00 USD | `+12.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.65` | 6,250,000.00 USD | 666.02 USD | 0.00 USD | `+12.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.75` | 6,250,000.00 USD | 1,010.00 USD | 0.00 USD | `+12.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.85` | 6,260,000.00 USD | 1,430.00 USD | 0.00 USD | `+12.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.95` | 6,300,000.00 USD | 40,920.00 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 6,370,000.00 USD | 73,460.00 USD | 0.00 USD | `+13.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.15` | 6,380,000.00 USD | 7,660.00 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.25` | 10,320,000.00 USD | 3,950,000.00 USD | 0.00 USD | `+13.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.35` | 10,350,000.00 USD | 31,070.00 USD | 0.00 USD | `+13.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.45` | 10,360,000.00 USD | 5,880.00 USD | 0.00 USD | `+13.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.55` | 10,360,000.00 USD | 1,070.00 USD | 0.00 USD | `+13.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.65` | 10,370,000.00 USD | 5,040.00 USD | 0.00 USD | `+13.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.75` | 10,370,000.00 USD | 1,370.00 USD | 0.00 USD | `+13.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.85` | 10,370,000.00 USD | 1,420.00 USD | 0.00 USD | `+13.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.95` | 10,370,000.00 USD | 357.34 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.05` | 10,890,000.00 USD | 522,250.00 USD | 0.00 USD | `+14.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.15` | 10,900,000.00 USD | 4,150.00 USD | 0.00 USD | `+14.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.25` | 10,900,000.00 USD | 102.53 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.35` | 10,900,000.00 USD | 1,610.00 USD | 0.00 USD | `+14.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.45` | 10,900,000.00 USD | 1,580.00 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.55` | 10,910,000.00 USD | 10,280.00 USD | 0.00 USD | `+14.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.65` | 10,910,000.00 USD | 3,030.00 USD | 0.00 USD | `+14.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.85` | 10,930,000.00 USD | 17,520.00 USD | 0.00 USD | `+15.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.95` | 11,000,000.00 USD | 74,620.00 USD | 0.00 USD | `+15.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 11,070,000.00 USD | 64,770.00 USD | 0.00 USD | `+15.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.15` | 11,070,000.00 USD | 1,300.00 USD | 0.00 USD | `+15.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.25` | 11,080,000.00 USD | 5,910.00 USD | 0.00 USD | `+15.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.45` | 11,080,000.00 USD | 585.11 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.55` | 11,080,000.00 USD | 852.24 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.65` | 11,100,000.00 USD | 22,910.00 USD | 0.00 USD | `+15.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.75` | 11,100,000.00 USD | 2,420.00 USD | 0.00 USD | `+15.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.85` | 11,110,000.00 USD | 2,100.00 USD | 0.00 USD | `+16.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.05` | 11,120,000.00 USD | 14,400.00 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.15` | 11,170,000.00 USD | 49,680.00 USD | 0.00 USD | `+16.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.25` | 11,180,000.00 USD | 5,260.00 USD | 0.00 USD | `+16.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 11,180,000.00 USD | 4,920.00 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.45` | 11,180,000.00 USD | 953.58 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.55` | 11,220,000.00 USD | 36,280.00 USD | 0.00 USD | `+16.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.65` | 11,220,000.00 USD | 6,710.00 USD | 0.00 USD | `+16.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.85` | 11,220,000.00 USD | 586.82 USD | 0.00 USD | `+17.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.05` | 11,310,000.00 USD | 81,560.00 USD | 0.00 USD | `+17.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.25` | 11,310,000.00 USD | 710.08 USD | 0.00 USD | `+17.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.35` | 11,340,000.00 USD | 35,250.00 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.45` | 11,340,000.00 USD | 655.74 USD | 0.00 USD | `+17.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.55` | 11,350,000.00 USD | 4,470.00 USD | 0.00 USD | `+17.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.65` | 11,350,000.00 USD | 230.71 USD | 0.00 USD | `+17.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.75` | 11,350,000.00 USD | 257.07 USD | 0.00 USD | `+18.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.85` | 11,350,000.00 USD | 4,540.00 USD | 0.00 USD | `+18.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.05` | 11,350,000.00 USD | 1,970.00 USD | 0.00 USD | `+18.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.15` | 11,350,000.00 USD | 122.14 USD | 0.00 USD | `+18.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.25` | 11,360,000.00 USD | 907.14 USD | 0.00 USD | `+18.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.35` | 11,360,000.00 USD | 740.99 USD | 0.00 USD | `+18.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.45` | 11,360,000.00 USD | 343.35 USD | 0.00 USD | `+18.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.55` | 11,360,000.00 USD | 1,640.00 USD | 0.00 USD | `+18.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.65` | 11,360,000.00 USD | 105.48 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.75` | 11,360,000.00 USD | 1,010.00 USD | 0.00 USD | `+19.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.95` | 11,360,000.00 USD | 2,520.00 USD | 0.00 USD | `+19.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.05` | 11,440,000.00 USD | 81,890.00 USD | 0.00 USD | `+19.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.35` | 11,440,000.00 USD | 309.14 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.45` | 11,440,000.00 USD | 346.35 USD | 0.00 USD | `+19.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.55` | 11,450,000.00 USD | 4,900.00 USD | 0.00 USD | `+19.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.75` | 11,450,000.00 USD | 121.54 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.85` | 11,450,000.00 USD | 579.25 USD | 0.00 USD | `+20.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.05` | 11,460,000.00 USD | 6,400.00 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.15` | 11,460,000.00 USD | 1,740.00 USD | 0.00 USD | `+20.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.25` | 11,460,000.00 USD | 1,920.00 USD | 0.00 USD | `+20.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.45` | 11,460,000.00 USD | 2,870.00 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.55` | 11,480,000.00 USD | 14,010.00 USD | 0.00 USD | `+20.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.65` | 11,480,000.00 USD | 6,000.00 USD | 0.00 USD | `+21.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.75` | 11,490,000.00 USD | 3,580.00 USD | 0.00 USD | `+21.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.85` | 11,490,000.00 USD | 234.87 USD | 0.00 USD | `+21.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.95` | 11,500,000.00 USD | 12,860.00 USD | 0.00 USD | `+21.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.05` | 11,500,000.00 USD | 4,200.00 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.15` | 11,500,000.00 USD | 584.58 USD | 0.00 USD | `+21.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.25` | 11,510,000.00 USD | 1,740.00 USD | 0.00 USD | `+21.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.35` | 11,510,000.00 USD | 2,330.00 USD | 0.00 USD | `+21.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.45` | 11,630,000.00 USD | 118,690.00 USD | 0.00 USD | `+21.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.65` | 11,730,000.00 USD | 106,330.00 USD | 0.00 USD | `+22.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.75` | 11,740,000.00 USD | 5,920.00 USD | 0.00 USD | `+22.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.85` | 11,790,000.00 USD | 55,580.00 USD | 0.00 USD | `+22.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.05` | 11,860,000.00 USD | 69,220.00 USD | 0.00 USD | `+22.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.15` | 11,870,000.00 USD | 3,980.00 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.25` | 11,870,000.00 USD | 4,460.00 USD | 0.00 USD | `+22.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.35` | 11,870,000.00 USD | 127.82 USD | 0.00 USD | `+22.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.45` | 11,870,000.00 USD | 707.15 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.55` | 11,870,000.00 USD | 1,260.00 USD | 0.00 USD | `+22.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.65` | 11,880,000.00 USD | 2,970.00 USD | 0.00 USD | `+23.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.75` | 11,880,000.00 USD | 403.75 USD | 0.00 USD | `+23.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.85` | 11,890,000.00 USD | 15,940.00 USD | 0.00 USD | `+23.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.95` | 11,940,000.00 USD | 42,290.00 USD | 0.00 USD | `+23.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.05` | 11,990,000.00 USD | 52,430.00 USD | 0.00 USD | `+23.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.15` | 12,000,000.00 USD | 15,130.00 USD | 0.00 USD | `+23.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.25` | 12,010,000.00 USD | 1,850.00 USD | 0.00 USD | `+23.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.35` | 12,010,000.00 USD | 4,150.00 USD | 0.00 USD | `+23.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.45` | 12,010,000.00 USD | 310.57 USD | 0.00 USD | `+23.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.65` | 12,010,000.00 USD | 615.00 USD | 0.00 USD | `+24.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.75` | 12,140,000.00 USD | 125,500.00 USD | 0.00 USD | `+24.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.85` | 12,170,000.00 USD | 37,630.00 USD | 0.00 USD | `+24.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.95` | 12,170,000.00 USD | 458.21 USD | 0.00 USD | `+24.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.05` | 12,360,000.00 USD | 184,950.00 USD | 0.00 USD | `+24.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.15` | 12,360,000.00 USD | 414.52 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.25` | 12,360,000.00 USD | 3,210.00 USD | 0.00 USD | `+24.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.35` | 12,370,000.00 USD | 7,850.00 USD | 0.00 USD | `+24.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.45` | 12,380,000.00 USD | 13,560.00 USD | 0.00 USD | `+24.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.55` | 12,390,000.00 USD | 904.13 USD | 0.00 USD | `+25.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.65` | 12,390,000.00 USD | 191.83 USD | 0.00 USD | `+25.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.85` | 12,390,000.00 USD | 663.47 USD | 0.00 USD | `+25.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.05` | 12,410,000.00 USD | 20,960.00 USD | 0.00 USD | `+25.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.15` | 12,410,000.00 USD | 122.36 USD | 0.00 USD | `+25.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.25` | 12,420,000.00 USD | 11,200.00 USD | 0.00 USD | `+25.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.45` | 12,430,000.00 USD | 11,570.00 USD | 0.00 USD | `+25.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.55` | 12,440,000.00 USD | 7,860.00 USD | 0.00 USD | `+26.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.65` | 12,440,000.00 USD | 4,430.00 USD | 0.00 USD | `+26.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.75` | 12,440,000.00 USD | 2,450.00 USD | 0.00 USD | `+26.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.85` | 12,450,000.00 USD | 1,480.00 USD | 0.00 USD | `+26.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.95` | 12,530,000.00 USD | 80,260.00 USD | 0.00 USD | `+26.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.05` | 12,720,000.00 USD | 192,930.00 USD | 0.00 USD | `+26.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.15` | 12,720,000.00 USD | 1,000.00 USD | 0.00 USD | `+26.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.25` | 12,950,000.00 USD | 234,430.00 USD | 0.00 USD | `+26.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.35` | 13,010,000.00 USD | 52,330.00 USD | 0.00 USD | `+26.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.45` | 13,010,000.00 USD | 3,060.00 USD | 0.00 USD | `+27.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.55` | 13,020,000.00 USD | 7,020.00 USD | 0.00 USD | `+27.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.65` | 13,030,000.00 USD | 11,000.00 USD | 0.00 USD | `+27.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.75` | 13,030,000.00 USD | 368.25 USD | 0.00 USD | `+27.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.85` | 13,030,000.00 USD | 3,850.00 USD | 0.00 USD | `+27.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.95` | 13,050,000.00 USD | 16,430.00 USD | 0.00 USD | `+27.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.05` | 14,060,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+27.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.15` | 14,060,000.00 USD | 252.46 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.25` | 14,070,000.00 USD | 7,710.00 USD | 0.00 USD | `+27.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.35` | 14,070,000.00 USD | 6,790.00 USD | 0.00 USD | `+27.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.45` | 14,080,000.00 USD | 2,670.00 USD | 0.00 USD | `+28.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.55` | 14,080,000.00 USD | 632.58 USD | 0.00 USD | `+28.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.65` | 14,090,000.00 USD | 11,550.00 USD | 0.00 USD | `+28.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.85` | 14,090,000.00 USD | 5,530.00 USD | 0.00 USD | `+28.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.95` | 14,110,000.00 USD | 18,470.00 USD | 0.00 USD | `+28.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.05` | 14,130,000.00 USD | 16,360.00 USD | 0.00 USD | `+28.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.15` | 14,130,000.00 USD | 1,320.00 USD | 0.00 USD | `+28.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.25` | 14,130,000.00 USD | 151.59 USD | 0.00 USD | `+28.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.35` | 14,130,000.00 USD | 4,240.00 USD | 0.00 USD | `+29.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.45` | 14,140,000.00 USD | 1,370.00 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.55` | 14,140,000.00 USD | 7,330.00 USD | 0.00 USD | `+29.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.65` | 14,150,000.00 USD | 6,610.00 USD | 0.00 USD | `+29.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.85` | 14,150,000.00 USD | 596.78 USD | 0.00 USD | `+29.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.95` | 14,160,000.00 USD | 10,310.00 USD | 0.00 USD | `+29.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.05` | 14,710,000.00 USD | 554,250.00 USD | 0.00 USD | `+29.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.15` | 14,720,000.00 USD | 603.22 USD | 0.00 USD | `+29.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.25` | 14,720,000.00 USD | 311.87 USD | 0.00 USD | `+29.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.35` | 14,720,000.00 USD | 6,780.00 USD | 0.00 USD | `+30.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.45` | 14,720,000.00 USD | 993.56 USD | 0.00 USD | `+30.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.55` | 14,740,000.00 USD | 16,280.00 USD | 0.00 USD | `+30.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.85` | 14,740,000.00 USD | 471.94 USD | 0.00 USD | `+30.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.95` | 14,740,000.00 USD | 209.08 USD | 0.00 USD | `+30.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.05` | 14,890,000.00 USD | 151,060.00 USD | 0.00 USD | `+30.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.15` | 14,890,000.00 USD | 189.23 USD | 0.00 USD | `+30.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.45` | 14,890,000.00 USD | 187.15 USD | 0.00 USD | `+31.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.65` | 14,900,000.00 USD | 3,550.00 USD | 0.00 USD | `+31.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.75` | 14,900,000.00 USD | 7,460.00 USD | 0.00 USD | `+31.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.05` | 15,090,000.00 USD | 190,580.00 USD | 0.00 USD | `+31.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.35` | 15,090,000.00 USD | 534.87 USD | 0.00 USD | `+32.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.45` | 15,100,000.00 USD | 4,620.00 USD | 0.00 USD | `+32.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.65` | 15,100,000.00 USD | 5,000.00 USD | 0.00 USD | `+32.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.75` | 15,100,000.00 USD | 362.81 USD | 0.00 USD | `+32.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.85` | 15,160,000.00 USD | 60,770.00 USD | 0.00 USD | `+32.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.95` | 15,170,000.00 USD | 482.37 USD | 0.00 USD | `+32.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.05` | 15,170,000.00 USD | 3,700.00 USD | 0.00 USD | `+32.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.15` | 15,170,000.00 USD | 3,010.00 USD | 0.00 USD | `+32.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.25` | 15,170,000.00 USD | 191.09 USD | 0.00 USD | `+33.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.65` | 15,210,000.00 USD | 41,130.00 USD | 0.00 USD | `+33.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.95` | 15,230,000.00 USD | 12,600.00 USD | 0.00 USD | `+33.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.05` | 15,280,000.00 USD | 50,720.00 USD | 0.00 USD | `+33.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.15` | 15,280,000.00 USD | 229.89 USD | 0.00 USD | `+33.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.25` | 15,290,000.00 USD | 15,330.00 USD | 0.00 USD | `+34.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.45` | 15,290,000.00 USD | 401.29 USD | 0.00 USD | `+34.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.55` | 15,290,000.00 USD | 1,320.00 USD | 0.00 USD | `+34.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.65` | 15,290,000.00 USD | 152.99 USD | 0.00 USD | `+34.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.75` | 15,290,000.00 USD | 153.10 USD | 0.00 USD | `+34.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.85` | 15,290,000.00 USD | 116.87 USD | 0.00 USD | `+34.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.05` | 15,350,000.00 USD | 51,520.00 USD | 0.00 USD | `+34.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.35` | 15,350,000.00 USD | 1,760.00 USD | 0.00 USD | `+35.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.45` | 15,350,000.00 USD | 4,090.00 USD | 0.00 USD | `+35.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.65` | 15,350,000.00 USD | 192.06 USD | 0.00 USD | `+35.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.75` | 15,360,000.00 USD | 3,150.00 USD | 0.00 USD | `+35.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.85` | 15,360,000.00 USD | 2,620.00 USD | 0.00 USD | `+35.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.95` | 15,370,000.00 USD | 10,140.00 USD | 0.00 USD | `+35.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.05` | 15,370,000.00 USD | 6,000.00 USD | 0.00 USD | `+35.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.15` | 15,380,000.00 USD | 5,950.00 USD | 0.00 USD | `+36.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.25` | 15,390,000.00 USD | 8,820.00 USD | 0.00 USD | `+36.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.45` | 15,390,000.00 USD | 135.39 USD | 0.00 USD | `+36.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.65` | 15,550,000.00 USD | 160,920.00 USD | 0.00 USD | `+36.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.75` | 15,550,000.00 USD | 144.93 USD | 0.00 USD | `+36.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.05` | 15,560,000.00 USD | 12,390.00 USD | 0.00 USD | `+36.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.65` | 15,560,000.00 USD | 397.95 USD | 0.00 USD | `+37.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.85` | 15,570,000.00 USD | 9,310.00 USD | 0.00 USD | `+37.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.95` | 15,580,000.00 USD | 3,910.00 USD | 0.00 USD | `+37.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.05` | 15,580,000.00 USD | 267.43 USD | 0.00 USD | `+38.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.15` | 15,580,000.00 USD | 509.96 USD | 0.00 USD | `+38.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.25` | 15,580,000.00 USD | 191.88 USD | 0.00 USD | `+38.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.35` | 15,580,000.00 USD | 237.36 USD | 0.00 USD | `+38.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.55` | 15,580,000.00 USD | 1,210.00 USD | 0.00 USD | `+38.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.65` | 15,580,000.00 USD | 192.46 USD | 0.00 USD | `+38.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.75` | 15,580,000.00 USD | 112.35 USD | 0.00 USD | `+38.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.95` | 15,580,000.00 USD | 4,620.00 USD | 0.00 USD | `+38.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.05` | 15,640,000.00 USD | 54,080.00 USD | 0.00 USD | `+39.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.25` | 15,640,000.00 USD | 331.60 USD | 0.00 USD | `+39.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.55` | 15,910,000.00 USD | 270,270.00 USD | 0.00 USD | `+39.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.85` | 15,910,000.00 USD | 647.28 USD | 0.00 USD | `+39.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.05` | 16,020,000.00 USD | 116,220.00 USD | 0.00 USD | `+40.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.55` | 16,030,000.00 USD | 7,560.00 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.05` | 16,030,000.00 USD | 1,890.00 USD | 0.00 USD | `+41.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.35` | 16,030,000.00 USD | 192.25 USD | 0.00 USD | `+41.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.45` | 16,030,000.00 USD | 465.29 USD | 0.00 USD | `+41.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.55` | 16,040,000.00 USD | 389.17 USD | 0.00 USD | `+41.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.85` | 16,040,000.00 USD | 826.57 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.05` | 16,040,000.00 USD | 231.61 USD | 0.00 USD | `+42.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.25` | 16,040,000.00 USD | 2,910.00 USD | 0.00 USD | `+42.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.35` | 16,040,000.00 USD | 3,920.00 USD | 0.00 USD | `+42.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.65` | 16,070,000.00 USD | 26,260.00 USD | 0.00 USD | `+42.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.75` | 16,070,000.00 USD | 133.62 USD | 0.00 USD | `+42.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.05` | 16,080,000.00 USD | 14,550.00 USD | 0.00 USD | `+43.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.45` | 16,080,000.00 USD | 692.25 USD | 0.00 USD | `+43.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.65` | 16,090,000.00 USD | 447.84 USD | 0.00 USD | `+43.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.85` | 22,830,000.00 USD | 6,740,000.00 USD | 0.00 USD | `+44.04%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `138.95` | 22,830,000.00 USD | 826.75 USD | 0.00 USD | `+44.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.05` | 25,020,000.00 USD | 2,190,000.00 USD | 0.00 USD | `+44.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `139.55` | 25,030,000.00 USD | 5,920.00 USD | 0.00 USD | `+44.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.05` | 25,140,000.00 USD | 110,660.00 USD | 0.00 USD | `+45.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.45` | 25,150,000.00 USD | 12,120.00 USD | 0.00 USD | `+45.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.55` | 25,250,000.00 USD | 98,400.00 USD | 0.00 USD | `+45.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.75` | 25,250,000.00 USD | 990.88 USD | 0.00 USD | `+46.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.05` | 25,260,000.00 USD | 12,080.00 USD | 0.00 USD | `+46.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.25` | 25,270,000.00 USD | 6,190.00 USD | 0.00 USD | `+46.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.65` | 25,270,000.00 USD | 796.07 USD | 0.00 USD | `+46.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.05` | 25,270,000.00 USD | 826.73 USD | 0.00 USD | `+47.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.85` | 25,270,000.00 USD | 278.56 USD | 0.00 USD | `+48.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.95` | 25,600,000.00 USD | 329,100.00 USD | 0.00 USD | `+48.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.05` | 25,670,000.00 USD | 72,610.00 USD | 0.00 USD | `+48.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.15` | 25,690,000.00 USD | 16,980.00 USD | 0.00 USD | `+48.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.35` | 25,690,000.00 USD | 528.96 USD | 0.00 USD | `+48.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.05` | 25,690,000.00 USD | 6,330.00 USD | 0.00 USD | `+49.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.25` | 25,700,000.00 USD | 415.44 USD | 0.00 USD | `+49.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.35` | 25,980,000.00 USD | 282,520.00 USD | 0.00 USD | `+49.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.55` | 25,980,000.00 USD | 7,260.00 USD | 0.00 USD | `+49.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.75` | 25,990,000.00 USD | 791.78 USD | 0.00 USD | `+50.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.05` | 26,020,000.00 USD | 36,040.00 USD | 0.00 USD | `+50.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.25` | 26,020,000.00 USD | 209.16 USD | 0.00 USD | `+50.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.55` | 26,020,000.00 USD | 698.64 USD | 0.00 USD | `+50.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.05` | 26,210,000.00 USD | 190,100.00 USD | 0.00 USD | `+51.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.15` | 26,220,000.00 USD | 3,300.00 USD | 0.00 USD | `+51.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.25` | 26,220,000.00 USD | 1,020.00 USD | 0.00 USD | `+51.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.95` | 26,220,000.00 USD | 1,500.00 USD | 0.00 USD | `+52.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.05` | 26,260,000.00 USD | 37,700.00 USD | 0.00 USD | `+52.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.45` | 26,260,000.00 USD | 844.89 USD | 0.00 USD | `+52.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.85` | 26,260,000.00 USD | 4,610.00 USD | 0.00 USD | `+53.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.95` | 26,260,000.00 USD | 3,100.00 USD | 0.00 USD | `+53.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.05` | 27,600,000.00 USD | 1,340,000.00 USD | 0.00 USD | `+53.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.45` | 27,600,000.00 USD | 1,370.00 USD | 0.00 USD | `+54.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.55` | 27,610,000.00 USD | 4,760.00 USD | 0.00 USD | `+54.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.05` | 27,610,000.00 USD | 549.99 USD | 0.00 USD | `+54.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.15` | 28,120,000.00 USD | 510,120.00 USD | 0.00 USD | `+54.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.05` | 28,370,000.00 USD | 249,190.00 USD | 0.00 USD | `+55.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.25` | 28,370,000.00 USD | 1,200.00 USD | 0.00 USD | `+55.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.35` | 28,370,000.00 USD | 178.92 USD | 0.00 USD | `+55.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.55` | 28,370,000.00 USD | 1,360.00 USD | 0.00 USD | `+56.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.05` | 28,390,000.00 USD | 14,430.00 USD | 0.00 USD | `+56.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.25` | 28,390,000.00 USD | 2,000.00 USD | 0.00 USD | `+56.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.45` | 28,390,000.00 USD | 411.94 USD | 0.00 USD | `+57.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.15` | 28,400,000.00 USD | 10,620.00 USD | 0.00 USD | `+58.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.65` | 28,400,000.00 USD | 1,020.00 USD | 0.00 USD | `+59.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.55` | 28,410,000.00 USD | 12,000.00 USD | 0.00 USD | `+60.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.85` | 28,410,000.00 USD | 113.04 USD | 0.00 USD | `+60.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.05` | 28,410,000.00 USD | 1,830.00 USD | 0.00 USD | `+60.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.35` | 28,440,000.00 USD | 22,680.00 USD | 0.00 USD | `+61.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.85` | 28,450,000.00 USD | 16,970.00 USD | 0.00 USD | `+61.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.05` | 28,460,000.00 USD | 2,230.00 USD | 0.00 USD | `+61.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.05` | 28,460,000.00 USD | 6,640.00 USD | 0.00 USD | `+63.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.75` | 28,480,000.00 USD | 15,880.00 USD | 0.00 USD | `+64.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.15` | 28,480,000.00 USD | 692.30 USD | 0.00 USD | `+65.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.95` | 28,490,000.00 USD | 5,620.00 USD | 0.00 USD | `+65.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.05` | 28,570,000.00 USD | 89,040.00 USD | 0.00 USD | `+66.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.05` | 28,570,000.00 USD | 281.84 USD | 0.00 USD | `+67.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.05` | 28,580,000.00 USD | 4,080.00 USD | 0.00 USD | `+69.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.05` | 28,670,000.00 USD | 89,230.00 USD | 0.00 USD | `+71.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.45` | 28,670,000.00 USD | 823.94 USD | 0.00 USD | `+71.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.45` | 28,670,000.00 USD | 211.39 USD | 0.00 USD | `+72.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.95` | 28,670,000.00 USD | 307.19 USD | 0.00 USD | `+73.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.05` | 28,670,000.00 USD | 593.03 USD | 0.00 USD | `+73.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.75` | 28,670,000.00 USD | 1,440.00 USD | 0.00 USD | `+74.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.05` | 28,680,000.00 USD | 5,720.00 USD | 0.00 USD | `+74.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.55` | 28,680,000.00 USD | 495.09 USD | 0.00 USD | `+75.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.95` | 28,680,000.00 USD | 912.63 USD | 0.00 USD | `+76.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.05` | 28,720,000.00 USD | 43,480.00 USD | 0.00 USD | `+76.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.55` | 28,720,000.00 USD | 686.20 USD | 0.00 USD | `+77.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.05` | 28,760,000.00 USD | 35,280.00 USD | 0.00 USD | `+78.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.45` | 28,760,000.00 USD | 703.60 USD | 0.00 USD | `+78.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.05` | 28,760,000.00 USD | 3,160.00 USD | 0.00 USD | `+79.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `174.85` | 28,760,000.00 USD | 1,430.00 USD | 0.00 USD | `+81.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.05` | 28,820,000.00 USD | 52,520.00 USD | 0.00 USD | `+81.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.25` | 28,840,000.00 USD | 21,960.00 USD | 0.00 USD | `+81.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.85` | 28,840,000.00 USD | 1,450.00 USD | 0.00 USD | `+83.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.05` | 28,840,000.00 USD | 885.25 USD | 0.00 USD | `+83.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.55` | 28,840,000.00 USD | 2,990.00 USD | 0.00 USD | `+85.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.15` | 28,840,000.00 USD | 261.56 USD | 0.00 USD | `+85.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.05` | 28,920,000.00 USD | 80,290.00 USD | 0.00 USD | `+86.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.05` | 28,930,000.00 USD | 2,440.00 USD | 0.00 USD | `+87.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.95` | 28,930,000.00 USD | 349.34 USD | 0.00 USD | `+88.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.45` | 28,950,000.00 USD | 19,620.00 USD | 0.00 USD | `+89.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.45` | 29,500,000.00 USD | 550,350.00 USD | 0.00 USD | `+90.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.05` | 29,530,000.00 USD | 29,610.00 USD | 0.00 USD | `+91.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.05` | 29,690,000.00 USD | 165,580.00 USD | 0.00 USD | `+94.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.05` | 29,830,000.00 USD | 141,190.00 USD | 0.00 USD | `+95.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `189.05` | 29,850,000.00 USD | 15,340.00 USD | 0.00 USD | `+96.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.05` | 29,880,000.00 USD | 35,880.00 USD | 0.00 USD | `+97.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.35` | 29,880,000.00 USD | 744.27 USD | 0.00 USD | `+97.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.65` | 29,890,000.00 USD | 7,750.00 USD | 0.00 USD | `+97.78%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `83.40` | 168,540,000.00 USD | 0.00 USD | 168,540,000.00 USD | 0.00 USD | 41,020.00 USD | 0.00 USD |
| `7D` | `83.60` | 168,500,000.00 USD | 0.00 USD | 168,500,000.00 USD | 0.00 USD | 0.00 USD | 9,920.00 USD |
| `7D` | `83.80` | 168,490,000.00 USD | 0.00 USD | 168,490,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `84.20` | 168,480,000.00 USD | 0.00 USD | 168,480,000.00 USD | 0.00 USD | 14,010.00 USD | 8,980.00 USD |
| `7D` | `84.40` | 168,460,000.00 USD | 0.00 USD | 168,460,000.00 USD | 0.00 USD | 26,170.00 USD | 0.00 USD |
| `7D` | `85.20` | 168,430,000.00 USD | 0.00 USD | 168,430,000.00 USD | 0.00 USD | 218,580.00 USD | 0.00 USD |
| `7D` | `85.40` | 168,210,000.00 USD | 0.00 USD | 168,210,000.00 USD | 0.00 USD | 12,950.00 USD | 192,310.00 USD |
| `7D` | `85.60` | 168,010,000.00 USD | 0.00 USD | 168,010,000.00 USD | 0.00 USD | 0.00 USD | 189,820.00 USD |
| `7D` | `85.80` | 167,820,000.00 USD | 0.00 USD | 167,820,000.00 USD | 0.00 USD | 260,960.00 USD | 0.00 USD |
| `7D` | `86.20` | 167,560,000.00 USD | 0.00 USD | 167,560,000.00 USD | 0.00 USD | 12,130.00 USD | 199,350.00 USD |
| `7D` | `86.40` | 167,350,000.00 USD | 0.00 USD | 167,350,000.00 USD | 0.00 USD | 311,220.00 USD | 4,340.00 USD |
| `1D` | `86.70` | 179,340,000.00 USD | 0.00 USD | 179,340,000.00 USD | 5,980.00 USD | 367,860.00 USD | 71,410.00 USD |
| `7D` | `86.80` | 167,030,000.00 USD | 0.00 USD | 167,030,000.00 USD | 0.00 USD | 149,840.00 USD | 0.00 USD |
| `1D` | `86.90` | 178,900,000.00 USD | 0.00 USD | 178,900,000.00 USD | 327,130.00 USD | 382,120.00 USD | 268,460.00 USD |
| `7D` | `87.00` | 166,880,000.00 USD | 0.00 USD | 166,880,000.00 USD | 271,000.00 USD | 183,160.00 USD | 310,380.00 USD |
| `1D` | `87.10` | 177,920,000.00 USD | 0.00 USD | 177,920,000.00 USD | 121,630.00 USD | 119,130.00 USD | 301,120.00 USD |
| `7D` | `87.20` | 166,120,000.00 USD | 0.00 USD | 166,120,000.00 USD | 8,850.00 USD | 6,510.00 USD | 6,820.00 USD |
| `1D` | `87.30` | 177,380,000.00 USD | 0.00 USD | 177,380,000.00 USD | 192,810.00 USD | 242,640.00 USD | 278,220.00 USD |
| `7D` | `87.40` | 166,090,000.00 USD | 0.00 USD | 166,090,000.00 USD | 248,310.00 USD | 225,130.00 USD | 288,100.00 USD |
| `1D` | `87.50` | 176,660,000.00 USD | 0.00 USD | 176,660,000.00 USD | 156,730.00 USD | 252,960.00 USD | 93,990.00 USD |
| `7D` | `87.60` | 165,330,000.00 USD | 0.00 USD | 165,330,000.00 USD | 0.00 USD | 275,130.00 USD | 421,310.00 USD |
| `1D` | `87.70` | 176,160,000.00 USD | 0.00 USD | 176,160,000.00 USD | 8,600.00 USD | 250,230.00 USD | 264,100.00 USD |
| `7D` | `87.80` | 164,640,000.00 USD | 0.00 USD | 164,640,000.00 USD | 0.00 USD | 413,150.00 USD | 11,130.00 USD |
| `1D` | `87.90` | 175,640,000.00 USD | 0.00 USD | 175,640,000.00 USD | 134,550.00 USD | 427,430.00 USD | 935,440.00 USD |
| `7D` | `88.00` | 164,210,000.00 USD | 0.00 USD | 164,210,000.00 USD | 0.00 USD | 12,070.00 USD | 251,100.00 USD |
| `1D` | `88.10` | 174,140,000.00 USD | 0.00 USD | 174,140,000.00 USD | 59,290.00 USD | 35,690.00 USD | 230,810.00 USD |
| `7D` | `88.20` | 163,950,000.00 USD | 0.00 USD | 163,950,000.00 USD | 9,900.00 USD | 20,610.00 USD | 28,240.00 USD |
| `1D` | `88.30` | 173,810,000.00 USD | 0.00 USD | 173,810,000.00 USD | 116,980.00 USD | 275,350.00 USD | 274,090.00 USD |
| `7D` | `88.40` | 163,890,000.00 USD | 0.00 USD | 163,890,000.00 USD | 0.00 USD | 237,870.00 USD | 335,390.00 USD |
| `1D` | `88.50` | 173,150,000.00 USD | 0.00 USD | 173,150,000.00 USD | 86,840.00 USD | 99,900.00 USD | 1,520.00 USD |
| `1D` | `88.70` | 172,960,000.00 USD | 0.00 USD | 172,960,000.00 USD | 204,330.00 USD | 124,180.00 USD | 413,910.00 USD |
| `7D` | `88.80` | 163,320,000.00 USD | 0.00 USD | 163,320,000.00 USD | 241,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `88.90` | 172,220,000.00 USD | 0.00 USD | 172,220,000.00 USD | 143,140.00 USD | 62,660.00 USD | 216,130.00 USD |
| `7D` | `89.00` | 163,070,000.00 USD | 0.00 USD | 163,070,000.00 USD | 350,210.00 USD | 289,350.00 USD | 293,700.00 USD |
| `1D` | `89.10` | 171,790,000.00 USD | 0.00 USD | 171,790,000.00 USD | 160,900.00 USD | 83,520.00 USD | 30,530.00 USD |
| `7D` | `89.20` | 162,140,000.00 USD | 0.00 USD | 162,140,000.00 USD | 8,180.00 USD | 10,750.00 USD | 315,450.00 USD |
| `1D` | `89.30` | 171,520,000.00 USD | 0.00 USD | 171,520,000.00 USD | 221,290.00 USD | 284,680.00 USD | 10,290.00 USD |
| `7D` | `89.40` | 161,810,000.00 USD | 0.00 USD | 161,810,000.00 USD | 697,470.00 USD | 26,220.00 USD | 160,460.00 USD |
| `1D` | `89.50` | 171,000,000.00 USD | 0.00 USD | 171,000,000.00 USD | 4,870.00 USD | 50,620.00 USD | 273,030.00 USD |
| `7D` | `89.60` | 160,920,000.00 USD | 0.00 USD | 160,920,000.00 USD | 684,220.00 USD | 270,260.00 USD | 723,370.00 USD |
| `1D` | `89.70` | 170,670,000.00 USD | 0.00 USD | 170,670,000.00 USD | 133,580.00 USD | 30,600.00 USD | 425,450.00 USD |
| `7D` | `89.80` | 159,240,000.00 USD | 0.00 USD | 159,240,000.00 USD | 425,950.00 USD | 318,390.00 USD | 314,310.00 USD |
| `1D` | `89.90` | 170,080,000.00 USD | 0.00 USD | 170,080,000.00 USD | 129,660.00 USD | 91,010.00 USD | 140,750.00 USD |
| `7D` | `90.00` | 158,190,000.00 USD | 0.00 USD | 158,190,000.00 USD | 374,600.00 USD | 647,410.00 USD | 1,090,000.00 USD |
| `1D` | `90.10` | 169,720,000.00 USD | 0.00 USD | 169,720,000.00 USD | 1,080,000.00 USD | 892,740.00 USD | 574,620.00 USD |
| `7D` | `90.20` | 156,070,000.00 USD | 0.00 USD | 156,070,000.00 USD | 1,250,000.00 USD | 590,390.00 USD | 735,310.00 USD |
| `1D` | `90.30` | 167,170,000.00 USD | 0.00 USD | 167,170,000.00 USD | 661,900.00 USD | 443,900.00 USD | 346,750.00 USD |
| `7D` | `90.40` | 153,490,000.00 USD | 0.00 USD | 153,490,000.00 USD | 796,240.00 USD | 68,740.00 USD | 694,770.00 USD |
| `1D` | `90.50` | 165,720,000.00 USD | 0.00 USD | 165,720,000.00 USD | 633,950.00 USD | 482,080.00 USD | 876,680.00 USD |
| `7D` | `90.60` | 151,930,000.00 USD | 0.00 USD | 151,930,000.00 USD | 1,040,000.00 USD | 1,010,000.00 USD | 1,560,000.00 USD |
| `1D` | `90.70` | 163,730,000.00 USD | 0.00 USD | 163,730,000.00 USD | 628,630.00 USD | 803,190.00 USD | 373,750.00 USD |
| `7D` | `90.80` | 148,320,000.00 USD | 0.00 USD | 148,320,000.00 USD | 1,210,000.00 USD | 1,200,000.00 USD | 1,480,000.00 USD |
| `1D` | `90.90` | 161,920,000.00 USD | 0.00 USD | 161,920,000.00 USD | 673,680.00 USD | 420,760.00 USD | 105,030.00 USD |
| `7D` | `91.00` | 144,430,000.00 USD | 0.00 USD | 144,430,000.00 USD | 1,190,000.00 USD | 609,900.00 USD | 810,620.00 USD |
| `1D` | `91.10` | 160,720,000.00 USD | 0.00 USD | 160,720,000.00 USD | 436,270.00 USD | 732,110.00 USD | 485,040.00 USD |
| `7D` | `91.20` | 141,820,000.00 USD | 0.00 USD | 141,820,000.00 USD | 2,280,000.00 USD | 868,420.00 USD | 638,860.00 USD |
| `1D` | `91.30` | 159,070,000.00 USD | 0.00 USD | 159,070,000.00 USD | 150,320.00 USD | 221,290.00 USD | 445,800.00 USD |
| `7D` | `91.40` | 138,040,000.00 USD | 0.00 USD | 138,040,000.00 USD | 1,180,000.00 USD | 1,030,000.00 USD | 1,620,000.00 USD |
| `1D` | `91.50` | 158,250,000.00 USD | 0.00 USD | 158,250,000.00 USD | 850,930.00 USD | 781,420.00 USD | 650,990.00 USD |
| `7D` | `91.60` | 134,210,000.00 USD | 0.00 USD | 134,210,000.00 USD | 500,280.00 USD | 1,020,000.00 USD | 872,760.00 USD |
| `1D` | `91.70` | 155,970,000.00 USD | 0.00 USD | 155,970,000.00 USD | 268,750.00 USD | 463,180.00 USD | 1,170,000.00 USD |
| `7D` | `91.80` | 131,820,000.00 USD | 0.00 USD | 131,820,000.00 USD | 932,400.00 USD | 797,110.00 USD | 688,730.00 USD |
| `1D` | `91.90` | 154,070,000.00 USD | 0.00 USD | 154,070,000.00 USD | 1,280,000.00 USD | 813,050.00 USD | 665,200.00 USD |
| `7D` | `92.00` | 129,400,000.00 USD | 0.00 USD | 129,400,000.00 USD | 681,440.00 USD | 656,110.00 USD | 990,500.00 USD |
| `1D` | `92.10` | 151,310,000.00 USD | 0.00 USD | 151,310,000.00 USD | 2,310,000.00 USD | 2,670,000.00 USD | 545,990.00 USD |
| `7D` | `92.20` | 127,070,000.00 USD | 0.00 USD | 127,070,000.00 USD | 2,870,000.00 USD | 1,110,000.00 USD | 289,060.00 USD |
| `1D` | `92.30` | 145,780,000.00 USD | 0.00 USD | 145,780,000.00 USD | 720,590.00 USD | 799,660.00 USD | 1,430,000.00 USD |
| `7D` | `92.40` | 122,810,000.00 USD | 0.00 USD | 122,810,000.00 USD | 550,500.00 USD | 843,410.00 USD | 1,540,000.00 USD |
| `1D` | `92.50` | 142,830,000.00 USD | 0.00 USD | 142,830,000.00 USD | 1,300,000.00 USD | 712,060.00 USD | 2,550,000.00 USD |
| `7D` | `92.60` | 119,880,000.00 USD | 0.00 USD | 119,880,000.00 USD | 98,670.00 USD | 880,990.00 USD | 1,690,000.00 USD |
| `1D` | `92.70` | 138,280,000.00 USD | 0.00 USD | 138,280,000.00 USD | 1,080,000.00 USD | 1,130,000.00 USD | 1,670,000.00 USD |
| `7D` | `92.80` | 117,210,000.00 USD | 0.00 USD | 117,210,000.00 USD | 463,730.00 USD | 2,370,000.00 USD | 1,640,000.00 USD |
| `1D` | `92.90` | 134,400,000.00 USD | 0.00 USD | 134,400,000.00 USD | 3,420,000.00 USD | 2,100,000.00 USD | 2,850,000.00 USD |
| `7D` | `93.00` | 112,730,000.00 USD | 0.00 USD | 112,730,000.00 USD | 549,700.00 USD | 550,690.00 USD | 2,030,000.00 USD |
| `1D` | `93.10` | 126,020,000.00 USD | 0.00 USD | 126,020,000.00 USD | 2,660,000.00 USD | 3,410,000.00 USD | 2,190,000.00 USD |
| `7D` | `93.20` | 109,600,000.00 USD | 0.00 USD | 109,600,000.00 USD | 1,090,000.00 USD | 670,930.00 USD | 2,130,000.00 USD |
| `1D` | `93.30` | 117,770,000.00 USD | 0.00 USD | 117,770,000.00 USD | 3,040,000.00 USD | 3,230,000.00 USD | 1,460,000.00 USD |
| `7D` | `93.40` | 105,710,000.00 USD | 0.00 USD | 105,710,000.00 USD | 611,840.00 USD | 2,660,000.00 USD | 1,430,000.00 USD |
| `1D` | `93.50` | 110,050,000.00 USD | 0.00 USD | 110,050,000.00 USD | 3,020,000.00 USD | 2,340,000.00 USD | 2,350,000.00 USD |
| `7D` | `93.60` | 101,000,000.00 USD | 0.00 USD | 101,000,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,640,000.00 USD |
| `1D` | `93.70` | 102,340,000.00 USD | 0.00 USD | 102,340,000.00 USD | 640,730.00 USD | 3,170,000.00 USD | 962,410.00 USD |
| `7D` | `93.80` | 98,060,000.00 USD | 0.00 USD | 98,060,000.00 USD | 0.00 USD | 2,080,000.00 USD | 3,170,000.00 USD |
| `1D` | `93.90` | 97,560,000.00 USD | 0.00 USD | 97,560,000.00 USD | 1,610,000.00 USD | 967,780.00 USD | 1,420,000.00 USD |
| `7D` | `94.00` | 92,810,000.00 USD | 0.00 USD | 92,810,000.00 USD | 2,660,000.00 USD | 1,780,000.00 USD | 2,210,000.00 USD |
| `1D` | `94.10` | 93,560,000.00 USD | 0.00 USD | 93,560,000.00 USD | 768,990.00 USD | 1,310,000.00 USD | 2,670,000.00 USD |
| `7D` | `94.20` | 86,170,000.00 USD | 0.00 USD | 86,170,000.00 USD | 24,740.00 USD | 962,410.00 USD | 2,750,000.00 USD |
| `1D` | `94.30` | 88,810,000.00 USD | 0.00 USD | 88,810,000.00 USD | 2,300,000.00 USD | 1,250,000.00 USD | 533,990.00 USD |
| `7D` | `94.40` | 82,430,000.00 USD | 0.00 USD | 82,430,000.00 USD | 0.00 USD | 515,800.00 USD | 9,790.00 USD |
| `1D` | `94.50` | 84,730,000.00 USD | 0.00 USD | 84,730,000.00 USD | 1,150,000.00 USD | 1,270,000.00 USD | 1,040,000.00 USD |
| `7D` | `94.60` | 81,900,000.00 USD | 0.00 USD | 81,900,000.00 USD | 560,570.00 USD | 0.00 USD | 432,770.00 USD |
| `1D` | `94.70` | 81,270,000.00 USD | 0.00 USD | 81,270,000.00 USD | 1,550,000.00 USD | 598,120.00 USD | 461,390.00 USD |
| `7D` | `94.80` | 80,910,000.00 USD | 0.00 USD | 80,910,000.00 USD | 2,090,000.00 USD | 152,290.00 USD | 3,430,000.00 USD |
| `1D` | `94.90` | 78,660,000.00 USD | 0.00 USD | 78,660,000.00 USD | 3,530,000.00 USD | 893,010.00 USD | 1,980,000.00 USD |
| `7D` | `95.00` | 75,240,000.00 USD | 0.00 USD | 75,240,000.00 USD | 3,420,000.00 USD | 4,770,000.00 USD | 1,570,000.00 USD |
| `1D` | `95.10` | 72,260,000.00 USD | 0.00 USD | 72,260,000.00 USD | 3,400,000.00 USD | 1,780,000.00 USD | 960,890.00 USD |
| `7D` | `95.20` | 65,470,000.00 USD | 0.00 USD | 65,470,000.00 USD | 2,420,000.00 USD | 317,900.00 USD | 17,980.00 USD |
| `1D` | `95.30` | 66,120,000.00 USD | 0.00 USD | 66,120,000.00 USD | 1,840,000.00 USD | 1,790,000.00 USD | 3,780,000.00 USD |
| `7D` | `95.40` | 62,710,000.00 USD | 0.00 USD | 62,710,000.00 USD | 2,080,000.00 USD | 2,620,000.00 USD | 4,590,000.00 USD |
| `1D` | `95.50` | 58,710,000.00 USD | 0.00 USD | 58,710,000.00 USD | 833,050.00 USD | 1,690,000.00 USD | 2,370,000.00 USD |
| `7D` | `95.60` | 53,420,000.00 USD | 0.00 USD | 53,420,000.00 USD | 3,820,000.00 USD | 7,040,000.00 USD | 5,460,000.00 USD |
| `1D` | `95.70` | 53,810,000.00 USD | 0.00 USD | 53,810,000.00 USD | 2,410,000.00 USD | 2,670,000.00 USD | 6,480,000.00 USD |
| `7D` | `95.80` | 37,110,000.00 USD | 0.00 USD | 37,110,000.00 USD | 3,400,000.00 USD | 93,510.00 USD | 2,300,000.00 USD |
| `1D` | `95.90` | 42,260,000.00 USD | 0.00 USD | 42,260,000.00 USD | 3,730,000.00 USD | 1,850,000.00 USD | 3,930,000.00 USD |
| `7D` | `96.00` | 31,320,000.00 USD | 0.00 USD | 31,320,000.00 USD | 5,350,000.00 USD | 1,290,000.00 USD | 5,620,000.00 USD |
| `1D` | `96.10` | 32,760,000.00 USD | 0.00 USD | 32,760,000.00 USD | 4,130,000.00 USD | 5,640,000.00 USD | 4,740,000.00 USD |
| `7D` | `96.20` | 19,060,000.00 USD | 0.00 USD | 19,060,000.00 USD | 6,840,000.00 USD | 2,710,000.00 USD | 5,250,000.00 USD |
| `1D` | `96.30` | 18,250,000.00 USD | 0.00 USD | 18,250,000.00 USD | 6,740,000.00 USD | 6,040,000.00 USD | 308,290.00 USD |
| `7D` | `96.40` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 1,600,000.00 USD | 2,550,000.00 USD | 20,910.00 USD |
| `1D` | `96.50` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 1,300,000.00 USD | 1,230,000.00 USD | 305,730.00 USD |
| `7D` | `96.60` | 89,520.00 USD | 0.00 USD | 89,520.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD |
| `1D` | `96.70` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 0.00 USD | 903,030.00 USD | 13,950.00 USD |
| `7D` | `96.80` | 64,730.00 USD | 0.00 USD | 64,730.00 USD | 0.00 USD | 64,730.00 USD | 0.00 USD |
| `1D` | `96.90` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD |
| `7D` | `96.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `97.10` | 4,460.00 USD | 4,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,460.00 USD |
| `7D` | `97.20` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,310,000.00 USD |
| `1D` | `97.30` | 179,280.00 USD | 179,280.00 USD | 0.00 USD | 174,820.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `97.40` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 0.00 USD | 101,560.00 USD | 0.00 USD |
| `1D` | `97.50` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 896,130.00 USD | 1,280,000.00 USD | 836,420.00 USD |
| `7D` | `97.60` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 0.00 USD | 24,930.00 USD | 4,780,000.00 USD |
| `1D` | `97.70` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 512,980.00 USD | 441,570.00 USD | 2,030,000.00 USD |
| `7D` | `97.80` | 20,260,000.00 USD | 20,260,000.00 USD | 0.00 USD | 7,580,000.00 USD | 3,430,000.00 USD | 1,020,000.00 USD |
| `1D` | `97.90` | 12,780,000.00 USD | 12,780,000.00 USD | 0.00 USD | 3,970,000.00 USD | 434,450.00 USD | 2,210,000.00 USD |
| `7D` | `98.00` | 36,960,000.00 USD | 36,960,000.00 USD | 0.00 USD | 14,120,000.00 USD | 561,730.00 USD | 2,030,000.00 USD |
| `1D` | `98.10` | 18,910,000.00 USD | 18,910,000.00 USD | 0.00 USD | 2,790,000.00 USD | 2,530,000.00 USD | 798,550.00 USD |
| `7D` | `98.20` | 47,890,000.00 USD | 47,890,000.00 USD | 0.00 USD | 9,790,000.00 USD | 1,140,000.00 USD | 0.00 USD |
| `1D` | `98.30` | 28,450,000.00 USD | 28,450,000.00 USD | 0.00 USD | 2,390,000.00 USD | 941,940.00 USD | 6,210,000.00 USD |
| `7D` | `98.40` | 59,460,000.00 USD | 59,460,000.00 USD | 0.00 USD | 1,780,000.00 USD | 3,320,000.00 USD | 6,460,000.00 USD |
| `1D` | `98.50` | 39,610,000.00 USD | 39,610,000.00 USD | 0.00 USD | 832,590.00 USD | 3,490,000.00 USD | 6,840,000.00 USD |
| `7D` | `98.60` | 68,890,000.00 USD | 68,890,000.00 USD | 0.00 USD | 1,960,000.00 USD | 5,450,000.00 USD | 2,020,000.00 USD |
| `1D` | `98.70` | 57,420,000.00 USD | 57,420,000.00 USD | 0.00 USD | 1,790,000.00 USD | 5,690,000.00 USD | 10,330,000.00 USD |
| `7D` | `98.80` | 74,710,000.00 USD | 74,710,000.00 USD | 0.00 USD | 1,100,000.00 USD | 784,380.00 USD | 3,930,000.00 USD |
| `1D` | `98.90` | 68,920,000.00 USD | 68,920,000.00 USD | 0.00 USD | 2,430,000.00 USD | 3,820,000.00 USD | 5,250,000.00 USD |
| `7D` | `99.00` | 83,540,000.00 USD | 83,540,000.00 USD | 0.00 USD | 2,170,000.00 USD | 2,700,000.00 USD | 3,960,000.00 USD |
| `1D` | `99.10` | 84,620,000.00 USD | 84,620,000.00 USD | 0.00 USD | 3,630,000.00 USD | 6,360,000.00 USD | 5,710,000.00 USD |
| `7D` | `99.20` | 97,510,000.00 USD | 97,510,000.00 USD | 0.00 USD | 1,220,000.00 USD | 6,520,000.00 USD | 6,240,000.00 USD |
| `1D` | `99.30` | 93,680,000.00 USD | 93,680,000.00 USD | 0.00 USD | 3,190,000.00 USD | 3,420,000.00 USD | 2,440,000.00 USD |
| `7D` | `99.40` | 98,550,000.00 USD | 98,550,000.00 USD | 0.00 USD | 0.00 USD | 1,010,000.00 USD | 25,850.00 USD |
| `1D` | `99.50` | 98,850,000.00 USD | 98,850,000.00 USD | 0.00 USD | 1,560,000.00 USD | 2,840,000.00 USD | 762,970.00 USD |
| `7D` | `99.60` | 103,980,000.00 USD | 103,980,000.00 USD | 0.00 USD | 2,240,000.00 USD | 2,640,000.00 USD | 545,090.00 USD |
| `1D` | `99.70` | 121,910,000.00 USD | 121,910,000.00 USD | 0.00 USD | 4,400,000.00 USD | 7,410,000.00 USD | 11,260,000.00 USD |
| `7D` | `99.80` | 107,310,000.00 USD | 107,310,000.00 USD | 0.00 USD | 736,270.00 USD | 1,330,000.00 USD | 1,270,000.00 USD |
| `1D` | `99.90` | 130,710,000.00 USD | 130,710,000.00 USD | 0.00 USD | 857,690.00 USD | 1,960,000.00 USD | 5,980,000.00 USD |
| `7D` | `100.00` | 118,640,000.00 USD | 118,640,000.00 USD | 0.00 USD | 2,220,000.00 USD | 2,310,000.00 USD | 6,790,000.00 USD |
| `1D` | `100.10` | 137,940,000.00 USD | 137,940,000.00 USD | 0.00 USD | 2,220,000.00 USD | 3,440,000.00 USD | 1,570,000.00 USD |
| `7D` | `100.20` | 124,740,000.00 USD | 124,740,000.00 USD | 0.00 USD | 843,770.00 USD | 2,470,000.00 USD | 2,780,000.00 USD |
| `1D` | `100.30` | 143,840,000.00 USD | 143,840,000.00 USD | 0.00 USD | 869,050.00 USD | 2,130,000.00 USD | 2,900,000.00 USD |
| `7D` | `100.40` | 129,430,000.00 USD | 129,430,000.00 USD | 0.00 USD | 993,830.00 USD | 654,600.00 USD | 3,050,000.00 USD |
| `1D` | `100.50` | 151,600,000.00 USD | 151,600,000.00 USD | 0.00 USD | 2,290,000.00 USD | 1,270,000.00 USD | 4,190,000.00 USD |
| `7D` | `100.60` | 135,310,000.00 USD | 135,310,000.00 USD | 0.00 USD | 2,150,000.00 USD | 1,480,000.00 USD | 2,250,000.00 USD |
| `1D` | `100.70` | 159,930,000.00 USD | 159,930,000.00 USD | 0.00 USD | 2,340,000.00 USD | 2,480,000.00 USD | 3,520,000.00 USD |
| `7D` | `100.80` | 138,480,000.00 USD | 138,480,000.00 USD | 0.00 USD | 1,010,000.00 USD | 1,380,000.00 USD | 786,390.00 USD |
| `1D` | `100.90` | 167,170,000.00 USD | 167,170,000.00 USD | 0.00 USD | 2,390,000.00 USD | 2,600,000.00 USD | 2,250,000.00 USD |
| `7D` | `101.00` | 157,450,000.00 USD | 157,450,000.00 USD | 0.00 USD | 4,160,000.00 USD | 7,060,000.00 USD | 7,750,000.00 USD |
| `1D` | `101.10` | 180,380,000.00 USD | 180,380,000.00 USD | 0.00 USD | 7,680,000.00 USD | 2,780,000.00 USD | 2,740,000.00 USD |
| `7D` | `101.20` | 176,860,000.00 USD | 176,860,000.00 USD | 0.00 USD | 7,240,000.00 USD | 5,320,000.00 USD | 6,850,000.00 USD |
| `1D` | `101.30` | 190,280,000.00 USD | 190,280,000.00 USD | 0.00 USD | 3,410,000.00 USD | 3,630,000.00 USD | 2,870,000.00 USD |
| `7D` | `101.40` | 193,920,000.00 USD | 193,920,000.00 USD | 0.00 USD | 4,720,000.00 USD | 1,270,000.00 USD | 11,070,000.00 USD |
| `1D` | `101.50` | 205,630,000.00 USD | 205,630,000.00 USD | 0.00 USD | 3,140,000.00 USD | 3,520,000.00 USD | 8,700,000.00 USD |
| `7D` | `101.60` | 204,440,000.00 USD | 204,440,000.00 USD | 0.00 USD | 3,650,000.00 USD | 30,170.00 USD | 6,840,000.00 USD |
| `1D` | `101.70` | 215,460,000.00 USD | 215,460,000.00 USD | 0.00 USD | 2,220,000.00 USD | 881,090.00 USD | 6,730,000.00 USD |
| `7D` | `101.80` | 214,370,000.00 USD | 214,370,000.00 USD | 0.00 USD | 3,050,000.00 USD | 609,510.00 USD | 6,270,000.00 USD |
| `1D` | `101.90` | 221,290,000.00 USD | 221,290,000.00 USD | 0.00 USD | 2,320,000.00 USD | 1,290,000.00 USD | 2,220,000.00 USD |
| `7D` | `102.00` | 220,360,000.00 USD | 220,360,000.00 USD | 0.00 USD | 1,830,000.00 USD | 1,470,000.00 USD | 2,690,000.00 USD |
| `1D` | `102.10` | 227,740,000.00 USD | 227,740,000.00 USD | 0.00 USD | 2,960,000.00 USD | 1,440,000.00 USD | 2,050,000.00 USD |
| `7D` | `102.20` | 227,080,000.00 USD | 227,080,000.00 USD | 0.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,540,000.00 USD |
| `1D` | `102.30` | 231,730,000.00 USD | 231,730,000.00 USD | 0.00 USD | 1,670,000.00 USD | 1,260,000.00 USD | 1,060,000.00 USD |
| `7D` | `102.40` | 232,390,000.00 USD | 232,390,000.00 USD | 0.00 USD | 2,340,000.00 USD | 304,350.00 USD | 2,660,000.00 USD |
| `1D` | `102.50` | 236,050,000.00 USD | 236,050,000.00 USD | 0.00 USD | 1,510,000.00 USD | 785,070.00 USD | 2,020,000.00 USD |
| `7D` | `102.60` | 234,850,000.00 USD | 234,850,000.00 USD | 0.00 USD | 1,450,000.00 USD | 979,270.00 USD | 33,240.00 USD |
| `1D` | `102.70` | 237,940,000.00 USD | 237,940,000.00 USD | 0.00 USD | 1,110,000.00 USD | 661,840.00 USD | 125,790.00 USD |
| `7D` | `102.80` | 242,940,000.00 USD | 242,940,000.00 USD | 0.00 USD | 7,780,000.00 USD | 23,810.00 USD | 286,910.00 USD |
| `1D` | `102.90` | 242,470,000.00 USD | 242,470,000.00 USD | 0.00 USD | 1,510,000.00 USD | 1,530,000.00 USD | 1,480,000.00 USD |
| `7D` | `103.00` | 259,880,000.00 USD | 259,880,000.00 USD | 0.00 USD | 12,270,000.00 USD | 394,420.00 USD | 4,270,000.00 USD |
| `1D` | `103.10` | 247,440,000.00 USD | 247,440,000.00 USD | 0.00 USD | 2,380,000.00 USD | 1,360,000.00 USD | 1,230,000.00 USD |
| `7D` | `103.20` | 272,550,000.00 USD | 272,550,000.00 USD | 0.00 USD | 11,620,000.00 USD | 140,550.00 USD | 913,680.00 USD |
| `1D` | `103.30` | 249,260,000.00 USD | 249,260,000.00 USD | 0.00 USD | 334,720.00 USD | 717,010.00 USD | 766,990.00 USD |
| `7D` | `103.40` | 287,120,000.00 USD | 287,120,000.00 USD | 0.00 USD | 11,050,000.00 USD | 233,330.00 USD | 3,280,000.00 USD |
| `1D` | `103.50` | 255,840,000.00 USD | 255,840,000.00 USD | 0.00 USD | 1,770,000.00 USD | 1,090,000.00 USD | 3,730,000.00 USD |
| `7D` | `103.60` | 305,510,000.00 USD | 305,510,000.00 USD | 0.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD |
| `1D` | `103.70` | 260,550,000.00 USD | 260,550,000.00 USD | 0.00 USD | 1,370,000.00 USD | 720,260.00 USD | 2,620,000.00 USD |
| `7D` | `103.80` | 317,890,000.00 USD | 317,890,000.00 USD | 0.00 USD | 7,960,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD |
| `1D` | `103.90` | 264,370,000.00 USD | 264,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,640,000.00 USD | 804,480.00 USD |
| `7D` | `104.00` | 344,600,000.00 USD | 344,600,000.00 USD | 0.00 USD | 10,830,000.00 USD | 7,160,000.00 USD | 8,710,000.00 USD |
| `1D` | `104.10` | 269,290,000.00 USD | 269,290,000.00 USD | 0.00 USD | 2,020,000.00 USD | 724,740.00 USD | 2,180,000.00 USD |
| `7D` | `104.20` | 366,630,000.00 USD | 366,630,000.00 USD | 0.00 USD | 8,520,000.00 USD | 7,230,000.00 USD | 6,280,000.00 USD |
| `1D` | `104.30` | 271,960,000.00 USD | 271,960,000.00 USD | 0.00 USD | 1,000,000.00 USD | 971,040.00 USD | 696,260.00 USD |
| `7D` | `104.40` | 383,810,000.00 USD | 383,810,000.00 USD | 0.00 USD | 5,100,000.00 USD | 3,710,000.00 USD | 8,360,000.00 USD |
| `1D` | `104.50` | 275,530,000.00 USD | 275,530,000.00 USD | 0.00 USD | 1,310,000.00 USD | 1,030,000.00 USD | 1,230,000.00 USD |
| `7D` | `104.60` | 401,560,000.00 USD | 401,560,000.00 USD | 0.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 7,020,000.00 USD |
| `1D` | `104.70` | 281,290,000.00 USD | 281,290,000.00 USD | 0.00 USD | 1,690,000.00 USD | 982,920.00 USD | 3,090,000.00 USD |
| `7D` | `104.80` | 418,950,000.00 USD | 418,950,000.00 USD | 0.00 USD | 5,170,000.00 USD | 4,410,000.00 USD | 7,820,000.00 USD |
| `1D` | `104.90` | 282,760,000.00 USD | 282,760,000.00 USD | 0.00 USD | 486,940.00 USD | 283,560.00 USD | 703,660.00 USD |
| `7D` | `105.00` | 435,120,000.00 USD | 435,120,000.00 USD | 0.00 USD | 5,730,000.00 USD | 4,110,000.00 USD | 6,330,000.00 USD |
| `1D` | `105.10` | 284,600,000.00 USD | 284,600,000.00 USD | 0.00 USD | 299,230.00 USD | 436,680.00 USD | 1,110,000.00 USD |
| `7D` | `105.20` | 445,780,000.00 USD | 445,780,000.00 USD | 0.00 USD | 5,340,000.00 USD | 2,800,000.00 USD | 2,530,000.00 USD |
| `1D` | `105.30` | 284,800,000.00 USD | 284,800,000.00 USD | 0.00 USD | 94,380.00 USD | 96,460.00 USD | 2,000.00 USD |
| `7D` | `105.40` | 454,000,000.00 USD | 454,000,000.00 USD | 0.00 USD | 1,570,000.00 USD | 3,170,000.00 USD | 3,470,000.00 USD |
| `1D` | `105.50` | 285,410,000.00 USD | 285,410,000.00 USD | 0.00 USD | 245,610.00 USD | 180,000.00 USD | 187,100.00 USD |
| `7D` | `105.60` | 462,420,000.00 USD | 462,420,000.00 USD | 0.00 USD | 3,700,000.00 USD | 2,270,000.00 USD | 2,450,000.00 USD |
| `1D` | `105.70` | 285,630,000.00 USD | 285,630,000.00 USD | 0.00 USD | 65,040.00 USD | 150,210.00 USD | 4,030.00 USD |
| `7D` | `105.80` | 471,230,000.00 USD | 471,230,000.00 USD | 0.00 USD | 2,690,000.00 USD | 2,620,000.00 USD | 3,510,000.00 USD |
| `1D` | `105.90` | 286,680,000.00 USD | 286,680,000.00 USD | 0.00 USD | 177,140.00 USD | 685,100.00 USD | 187,160.00 USD |
| `7D` | `106.00` | 476,380,000.00 USD | 476,380,000.00 USD | 0.00 USD | 1,970,000.00 USD | 1,050,000.00 USD | 2,130,000.00 USD |
| `1D` | `106.10` | 288,150,000.00 USD | 288,150,000.00 USD | 0.00 USD | 706,860.00 USD | 459,510.00 USD | 305,220.00 USD |
| `7D` | `106.20` | 485,280,000.00 USD | 485,280,000.00 USD | 0.00 USD | 3,820,000.00 USD | 2,560,000.00 USD | 2,520,000.00 USD |
| `1D` | `106.30` | 289,350,000.00 USD | 289,350,000.00 USD | 0.00 USD | 316,990.00 USD | 488,800.00 USD | 393,080.00 USD |
| `7D` | `106.40` | 491,360,000.00 USD | 491,360,000.00 USD | 0.00 USD | 2,430,000.00 USD | 2,180,000.00 USD | 1,480,000.00 USD |
| `1D` | `106.50` | 290,270,000.00 USD | 290,270,000.00 USD | 0.00 USD | 326,070.00 USD | 292,550.00 USD | 306,400.00 USD |
| `7D` | `106.60` | 496,200,000.00 USD | 496,200,000.00 USD | 0.00 USD | 1,330,000.00 USD | 1,250,000.00 USD | 2,260,000.00 USD |
| `1D` | `106.70` | 292,690,000.00 USD | 292,690,000.00 USD | 0.00 USD | 697,200.00 USD | 284,770.00 USD | 1,440,000.00 USD |
| `7D` | `106.80` | 500,850,000.00 USD | 500,850,000.00 USD | 0.00 USD | 999,190.00 USD | 927,000.00 USD | 2,730,000.00 USD |
| `1D` | `106.90` | 293,520,000.00 USD | 293,520,000.00 USD | 0.00 USD | 156,730.00 USD | 336,790.00 USD | 330,150.00 USD |
| `7D` | `107.00` | 505,000,000.00 USD | 505,000,000.00 USD | 0.00 USD | 527,980.00 USD | 1,180,000.00 USD | 2,430,000.00 USD |
| `1D` | `107.10` | 294,580,000.00 USD | 294,580,000.00 USD | 0.00 USD | 97,170.00 USD | 368,740.00 USD | 596,890.00 USD |
| `7D` | `107.20` | 506,090,000.00 USD | 506,090,000.00 USD | 0.00 USD | 230,020.00 USD | 507,570.00 USD | 352,500.00 USD |
| `1D` | `107.30` | 294,910,000.00 USD | 294,910,000.00 USD | 0.00 USD | 60,260.00 USD | 159,710.00 USD | 110,290.00 USD |
| `1D` | `107.40` | 295,360,000.00 USD | 295,360,000.00 USD | 0.00 USD | 0.00 USD | 41,740.00 USD | 408,060.00 USD |
| `7D` | `107.40` | 507,370,000.00 USD | 507,370,000.00 USD | 0.00 USD | 0.00 USD | 576,040.00 USD | 709,670.00 USD |
| `7D` | `107.60` | 508,000,000.00 USD | 508,000,000.00 USD | 0.00 USD | 213,520.00 USD | 12,070.00 USD | 406,020.00 USD |
| `7D` | `107.80` | 508,840,000.00 USD | 508,840,000.00 USD | 0.00 USD | 499,550.00 USD | 31,020.00 USD | 305,630.00 USD |
| `7D` | `108.00` | 509,420,000.00 USD | 509,420,000.00 USD | 0.00 USD | 5,950.00 USD | 237,870.00 USD | 335,390.00 USD |
| `7D` | `108.20` | 509,700,000.00 USD | 509,700,000.00 USD | 0.00 USD | 0.00 USD | 205,080.00 USD | 74,400.00 USD |
| `7D` | `108.40` | 510,190,000.00 USD | 510,190,000.00 USD | 0.00 USD | 487,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `108.60` | 510,370,000.00 USD | 510,370,000.00 USD | 0.00 USD | 17,470.00 USD | 167,730.00 USD | 0.00 USD |
| `7D` | `108.80` | 511,300,000.00 USD | 511,300,000.00 USD | 0.00 USD | 350,210.00 USD | 286,220.00 USD | 287,660.00 USD |
| `7D` | `109.00` | 511,580,000.00 USD | 511,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 286,720.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `5.61B` | Total OI Tokens: `57,793,537.2 SOL`
  * 1h OI Change: `-0.05%` | 4h OI Change: `-1.60%` | 24h OI Change: `-13.57%`
  * Exchange Breakdown: Binance=`970.71M` | Bybit=`612.13M` | OKX=`378.51M` | Hyperliquid=`518.00M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `72.30K` | Last 24h: `177.62K` | Last 3d: `997.77K` | Last 7d: `2.11M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0074%` |
| **USDT Bybit** | `0.0031%` | **USDT KuCoin** | `-0.0042%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0015%` | **USDT Bitget** | `-0.0095%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0011%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `61.30%` | `38.70%` | `1.58` | 877,520,000.00 USD |
| `15M` | `Binance` | `59.74%` | `40.26%` | `1.48` | 278,600,000.00 USD |
| `15M` | `OKX` | `58.35%` | `41.65%` | `1.40` | 190,240,000.00 USD |
| `15M` | `Bybit` | `65.35%` | `34.65%` | `1.89` | 53,130,000.00 USD |
| `15M` | `KuCoin` | `78.97%` | `21.03%` | `3.76` | 9,000,000.00 USD |
| `15M` | `Gate` | `55.07%` | `44.93%` | `1.23` | 130,830,000.00 USD |
| `15M` | `Bitget` | `64.41%` | `35.59%` | `1.81` | 37,730,000.00 USD |
| `15M` | `BingX` | `69.04%` | `30.96%` | `2.23` | 16,530,000.00 USD |
| `15M` | `MEXC` | `56.26%` | `43.74%` | `1.29` | 38,730,000.00 USD |
| `15M` | `Bitunix` | `58.15%` | `41.85%` | `1.39` | 31,140,000.00 USD |
| `15M` | `Hyperliquid` | `89.01%` | `10.99%` | `8.10` | 50,520,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.72%` | `43.28%` | `1.31` | 2,010,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `80.5%` | `19.5%` | `4.13` | 5,880,000.00 USD |
| `15M` | `HTX` | `52.35%` | `47.65%` | `1.10` | 7,000,000.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `58.99%` | `41.01%` | `1.44` | 4,660,000.00 USD |
| `15M` | `Bitfinex` | `78.99%` | `21.01%` | `3.76` | 280,880.00 USD |
| `15M` | `Kraken` | `75.01%` | `24.99%` | `3.00` | 3,410,000.00 USD |
| `15M` | `Aster` | `64.04%` | `35.96%` | `1.78` | 10,460,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `57.64%` | `42.36%` | `1.36` | 7,350,000.00 USD |
| `15M` | `Whale Positions` | `59.74%` | `40.26%` | `1.48` | 278,600,000.00 USD |
| `15M` | `Global Accounts` | `61.30%` | `38.70%` | `1.58` | 877,520,000.00 USD |
| `1H` | `SOL` | `56.49%` | `43.51%` | `1.30` | 1,640,000,000.00 USD |
| `1H` | `Binance` | `55.9%` | `44.1%` | `1.27` | 517,490,000.00 USD |
| `1H` | `OKX` | `55.96%` | `44.04%` | `1.27` | 340,310,000.00 USD |
| `1H` | `Bybit` | `59.11%` | `40.89%` | `1.45` | 103,140,000.00 USD |
| `1H` | `KuCoin` | `65.3%` | `34.7%` | `1.88` | 12,790,000.00 USD |
| `1H` | `Gate` | `54.2%` | `45.8%` | `1.18` | 247,530,000.00 USD |
| `1H` | `Bitget` | `55.9%` | `44.1%` | `1.27` | 57,920,000.00 USD |
| `1H` | `BingX` | `52.49%` | `47.51%` | `1.10` | 31,820,000.00 USD |
| `1H` | `MEXC` | `54.95%` | `45.05%` | `1.22` | 66,930,000.00 USD |
| `1H` | `Bitunix` | `53.06%` | `46.94%` | `1.13` | 59,110,000.00 USD |
| `1H` | `Hyperliquid` | `73.9%` | `26.1%` | `2.83` | 107,410,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.74%` | `45.26%` | `1.21` | 3,890,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `50.23%` | `49.77%` | `1.01` | 12,210,000.00 USD |
| `1H` | `HTX` | `31.62%` | `68.38%` | `0.46` | 24,760,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `52%` | `48%` | `1.08` | 12,810,000.00 USD |
| `1H` | `Bitfinex` | `63.74%` | `36.26%` | `1.76` | 499,650.00 USD |
| `1H` | `Kraken` | `54%` | `46%` | `1.17` | 8,110,000.00 USD |
| `1H` | `Aster` | `58.24%` | `41.76%` | `1.39` | 16,720,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `57.34%` | `42.66%` | `1.34` | 17,250,000.00 USD |
| `1H` | `Whale Positions` | `55.9%` | `44.1%` | `1.27` | 517,490,000.00 USD |
| `1H` | `Global Accounts` | `56.49%` | `43.51%` | `1.30` | 1,640,000,000.00 USD |
| `4H` | `SOL` | `44.42%` | `55.58%` | `0.80` | 461,810,000.00 USD |
| `4H` | `Binance` | `47.07%` | `52.93%` | `0.89` | 152,290,000.00 USD |
| `4H` | `OKX` | `43.45%` | `56.55%` | `0.77` | 49,700,000.00 USD |
| `4H` | `Bybit` | `41.73%` | `58.27%` | `0.72` | 73,450,000.00 USD |
| `4H` | `KuCoin` | `49.22%` | `50.78%` | `0.97` | 4,960,000.00 USD |
| `4H` | `Gate` | `54.91%` | `45.09%` | `1.22` | 23,050,000.00 USD |
| `4H` | `Bitget` | `49.18%` | `50.82%` | `0.97` | 34,690,000.00 USD |
| `4H` | `BingX` | `32.35%` | `67.65%` | `0.48` | 9,160,000.00 USD |
| `4H` | `MEXC` | `47.98%` | `52.02%` | `0.92` | 57,690,000.00 USD |
| `4H` | `Bitunix` | `46.19%` | `53.81%` | `0.86` | 16,540,000.00 USD |
| `4H` | `Hyperliquid` | `57.78%` | `42.22%` | `1.37` | 11,180,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.5%` | `49.5%` | `1.02` | 1,610,000.00 USD |
| `4H` | `Crypto.com` | `53.1%` | `46.9%` | `1.13` | 866,820.00 USD |
| `4H` | `WhiteBIT` | `1.56%` | `98.44%` | `0.02` | 19,710,000.00 USD |
| `4H` | `HTX` | `44.93%` | `55.07%` | `0.82` | 231,580.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `38.71%` | `61.29%` | `0.63` | 2,670,000.00 USD |
| `4H` | `Aster` | `34.35%` | `65.65%` | `0.52` | 3,180,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `57.36%` | `42.64%` | `1.35` | 814,910.00 USD |
| `4H` | `Whale Positions` | `47.07%` | `52.93%` | `0.89` | 152,290,000.00 USD |
| `4H` | `Global Accounts` | `44.42%` | `55.58%` | `0.80` | 461,810,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `97.15` | `97.19` | `97.15` | `97.37` | `97.05` | 9,961,152.58 USD | 4,407,159.48 USD | 5,553,993.10 USD | -1,146,833.62 USD | `-11.51%` | `1B / 5S` |
| `5:00 UTC` | `97.03` | `97.24` | `97.03` | `97.56` | `97.00` | 11,034,358.76 USD | 5,603,314.27 USD | 5,431,044.48 USD | 172,269.79 USD | `+1.56%` | `15B / 4S` |
| `0:00 UTC` | `97.13` | `97.19` | `97.13` | `97.44` | `97.03` | 17,561,649.50 USD | 7,274,477.25 USD | 10,287,172.25 USD | -3,012,695.00 USD | `-17.15%` | `4B / 13S` |
| `5:00 UTC` | `96.81` | `96.94` | `96.81` | `97.16` | `96.81` | 12,337,515.78 USD | 5,226,804.15 USD | 7,110,711.63 USD | -1,883,907.48 USD | `-15.27%` | `2B / 2S` |
| `0:00 UTC` | `96.81` | `96.92` | `96.81` | `97.16` | `96.69` | 14,931,632.13 USD | 8,028,191.38 USD | 6,903,440.75 USD | 1,124,750.63 USD | `+7.53%` | `9B / 6S` |
| `5:00 UTC` | `96.80` | `96.85` | `96.80` | `97.02` | `96.73` | 9,878,254.59 USD | 5,512,052.81 USD | 4,366,201.79 USD | 1,145,851.02 USD | `+11.60%` | `5B / 5S` |
| `0:00 UTC` | `96.43` | `96.47` | `96.43` | `96.84` | `96.31` | 18,229,950.06 USD | 9,017,649.47 USD | 9,212,300.59 USD | -194,651.12 USD | `-1.07%` | `1B / 6S` |
| `5:00 UTC` | `96.75` | `96.54` | `96.75` | `96.78` | `96.28` | 16,296,059.94 USD | 8,913,950.87 USD | 7,382,109.07 USD | 1,531,841.80 USD | `+9.40%` | `13B / 2S` |
| `0:00 UTC` | `97.12` | `97.02` | `97.12` | `97.23` | `96.62` | 22,145,911.65 USD | 11,618,840.75 USD | 10,527,070.90 USD | 1,091,769.84 USD | `+4.93%` | `11B / 4S` |
| `5:00 UTC` | `96.98` | `96.95` | `96.98` | `97.12` | `96.84` | 3,215,993.24 USD | 1,215,723.48 USD | 2,000,269.76 USD | -784,546.28 USD | `-24.40%` | `4B / 8S` |

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
| `5m` | 282,870.00 USD | 589,490.00 USD | **`ACCUMULATION`** |
| `15m` | 463,590.00 USD | 7,480,000.00 USD | **`ACCUMULATION`** |
| `30m` | -533,930.00 USD | 5,980,000.00 USD | **`ACCUMULATION`** |
| `1h` | -2,060,000.00 USD | -1,480,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -4,330,000.00 USD | -22,980,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -4,820,000.00 USD | -43,790,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,640,000.00 USD | -44,640,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 912,140.00 USD | -4,880,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -10,560,000.00 USD | -119,510,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -50,970,000.00 USD | -445,140,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 31,600,000.00 USD | -697,890,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -12,230,000.00 USD | -2,210,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+282.87K` | 15m=`+463.59K` | 1h=`-2.06M` | 24h=`-50.97M`
* Futures Capital Netflows: 5m=`+589.49K` | 15m=`+7.48M` | 1h=`-1.48M` | 24h=`-445.14M`
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
  * Execution Entry: `95.18` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `94.14` (Risk Distance: `1.04` pts)
  * +2.5R Take Profit: `97.77`
  * Mathematical Lot Sizing: **`9.65 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `98.09` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `99.13` (Risk Distance: `1.04` pts)
  * +2.5R Take Profit: `95.50`
  * Mathematical Lot Sizing: **`9.65 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`97.70`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
