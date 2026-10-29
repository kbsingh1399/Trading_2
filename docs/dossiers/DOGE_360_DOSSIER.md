# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 03:04:03 IST` (`2026-10-29 21:34:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0754` | **Live Ask Quote**: `0.0775` | **Mid Price**: `0.0764`
- **Spread Points**: `21.00` | **Spread BPS**: `274.69 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0764` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0770` | Lower -3.00σ Band: `0.0759`
  * Upper +2.51σ Band: `0.0769` | Lower -2.51σ Band: `0.0760`
  * Upper +2.01σ Band: `0.0768` | Lower -2.01σ Band: `0.0761`
  * Upper +2.00σ Band: `0.0768` | Lower -2.00σ Band: `0.0761`
  * Upper +1.28σ Band: `0.0767` | Lower -1.28σ Band: `0.0762`
  * Upper +1.00σ Band: `0.0766` | Lower -1.00σ Band: `0.0763`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0764` | EMA-20=`0.0764` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0764` (Slope: `+0.0000`) | EMA-100=`0.0764`
  * Institutional Anchors: EMA-144=`0.0764` | EMA-200=`0.0764` (Slope: `+0.0000`) | EMA-233=`0.0764`
- **Range Boundaries**: 24H High=`0.0772` | 24H Low=`0.0757` | Weekly High=`0.0780` | Weekly Low=`0.0749`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0757` (Distance: `+1.13%`)
  * Point of Control (POC) = `0.0748` (Distance: `+2.35%`)
  * Value Area Low (VAL) = `0.0744` (Distance: `+2.83%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0788` | POC=`0.0767` | VAL=`0.0765`
  * Prior Day Extremes: PDH=`0.0803` | PDL=`0.0733` | PDC=`0.0741`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0782` | Weekly POC=`0.0761` | Weekly VAL=`0.0755`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0757` | Low=`0.0738`
  * London Session (08:00-16:00 UTC): High=`0.0768` | Low=`0.0761`
  * New York Session (13:00-21:00 UTC): High=`0.0769` | Low=`0.0760`
  * Initial Balance (First Hour): IB High=`0.0767` | IB Low=`0.0762`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0761` - `0.0768`
  * Optimal Trade Entry (OTE 0.705): `0.0766`
  * Structural Invalidation Anchor (0.786): `0.0771`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0750` | `0.0760` | `0.0749` | `0.0760` | `118,783,730` | 8,967,347.00 USD | 379,834.53 USD | `+4.24%` | -31,550,836.29 USD | `+0.63` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `0.0760` | `0.0761` | `0.0758` | `0.0759` | `80,218,228` | 6,092,103.09 USD | 1,162,067.86 USD | `+19.07%` | -30,388,768.43 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.0759` | `0.0760` | `0.0759` | `0.0760` | `3,943,513` | 299,428.14 USD | 79,525.64 USD | `+26.56%` | -30,309,242.80 USD | `+0.45` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0756` | `0.0761` | `0.0742` | `0.0753` | `803,424,264` | 60,549,155.39 USD | -6,174,284.35 USD | `-10.20%` | -31,976,315.57 USD | `-1.96` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.0753` | `0.0761` | `0.0749` | `0.0759` | `386,883,236` | 29,212,143.58 USD | 1,797,469.02 USD | `+6.15%` | -30,178,846.55 USD | `+1.08` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.0759` | `0.0760` | `0.0759` | `0.0760` | `4,434,060` | 336,695.25 USD | 74,799.72 USD | `+22.22%` | -30,104,046.83 USD | `+0.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.0793` | `0.0795` | `0.0790` | `0.0793` | `99,331,512` | 7,872,201.47 USD | -219,088.96 USD | `-2.78%` | -13,221,722.80 USD | `+0.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0792` | `0.0793` | `0.0742` | `0.0753` | `1,891,844,576` | 144,606,422.97 USD | -19,167,046.23 USD | `-13.25%` | -32,388,769.03 USD | `-4.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0753` | `0.0761` | `0.0749` | `0.0760` | `391,317,296` | 29,548,838.83 USD | 1,872,268.74 USD | `+6.34%` | -30,516,500.29 USD | `+0.71` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -9,817,756.70 USD | `+1.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -12,825,425.50 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0760` | `2,282,671,325` | 174,117,994.70 USD | -17,290,051.57 USD | `-9.93%` | -30,115,477.08 USD | `-1.88` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0778` | `0.0790` | `0.0775` | `0.0777` | `649,981,168` | 50,850,515.04 USD | -4,359,439.36 USD | `-8.57%` | -11,383,503.61 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -14,406,508.13 USD | `+1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -9,817,756.70 USD | `+1.63` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0793` | `1,033,932,614` | 82,725,509.47 USD | -3,007,668.80 USD | `-3.64%` | -12,825,425.50 USD | `-0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0792` | `0.0793` | `0.0742` | `0.0760` | `2,282,671,325` | 174,117,994.70 USD | -17,290,051.57 USD | `-9.93%` | -30,115,477.08 USD | `-1.88` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.0764`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `0.0765` | `14128.0000` | 1,081.48 USD | 100,453.22 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.0765` | `449843.0000` | 34,434.58 USD | 134,887.80 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `0.0765` | `81763.0000` | 6,258.71 USD | 141,146.52 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.0765` | `3673.0000` | 281.15 USD | 141,427.67 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `0.0765` | `85193.0000` | 6,521.01 USD | 147,948.68 USD | `3 orders` | `-0.08%` | `-` |
| `BID` | `0.0765` | `280109.0000` | 21,440.10 USD | 169,388.79 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `0.0765` | `3888.0000` | 297.58 USD | 169,686.37 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `0.0765` | `64029.0000` | 4,900.59 USD | 174,586.95 USD | `2 orders` | `-0.09%` | `-` |
| `ASK` | `0.0766` | `7545.0000` | 578.20 USD | 117,284.71 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0766` | `152103.0000` | 11,655.96 USD | 116,706.51 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0766` | `16594.0000` | 1,271.61 USD | 105,050.55 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0766` | `15942.0000` | 1,221.64 USD | 103,778.94 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0766` | `24638.0000` | 1,887.94 USD | 102,557.30 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0766` | `69129.0000` | 5,297.08 USD | 100,669.37 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0766` | `999.0000` | 76.55 USD | 95,372.29 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0766` | `3703.0000` | 283.73 USD | 95,295.74 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0766` | `518798.0000` | 39,751.34 USD | 95,012.01 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0766` | `403878.0000` | 30,945.54 USD | 55,260.67 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0766` | `19529.0000` | 1,496.31 USD | 24,315.13 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `0.0766` | `16499.0000` | 1,264.14 USD | 22,818.82 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0766` | `1034.0000` | 79.22 USD | 21,554.68 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0766` | `133664.0000` | 10,240.93 USD | 21,475.46 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0766` | `3916.0000` | 300.02 USD | 11,234.52 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `0.0766` | `14299.0000` | 1,095.49 USD | 10,934.50 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.0766` | `94189.0000` | 7,216.01 USD | 9,839.01 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `0.0766` | `1034.0000` | 79.22 USD | 2,623.00 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0766` | `27983.0000` | 2,143.75 USD | 2,543.79 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `0.0766` | `5222.0000` | 400.04 USD | 400.04 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `0.0766` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0766` | `56070.0000` | 4,294.91 USD | 4,294.91 USD | `1 orders` | `-0.00%` | `-` |
| `BID` | `0.0766` | `133725.0000` | 10,240.93 USD | 14,535.83 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0766` | `584128.0000` | 44,733.11 USD | 59,268.94 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `0.0766` | `26434.0000` | 2,024.05 USD | 61,292.99 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0766` | `121893.0000` | 9,333.23 USD | 70,626.22 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0766` | `146605.0000` | 11,224.96 USD | 81,851.18 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0766` | `1034.0000` | 79.17 USD | 81,930.34 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0766` | `14128.0000` | 1,081.68 USD | 83,012.02 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0766` | `26402.0000` | 2,021.36 USD | 85,033.39 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0766` | `20863.0000` | 1,597.27 USD | 86,630.66 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0766` | `14128.0000` | 1,081.60 USD | 87,712.26 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0766` | `152306.0000` | 11,659.48 USD | 99,371.74 USD | `3 orders` | `-0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:55:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `310` | `0xb83d...6e36` | `SHORT` | 7,851,592.10 USD | `102,645,925.00` | `0.0946` | `0.0762` | `1.43` | 1,855,749.56 USD | `+23.64%` | `3X Cross` |
| `313` | `0xc63a...a3cd` | `LONG` | 7,654,600.00 USD | `100,000,000.00` | `0.0856` | `0.0762` | `0.000000` | -910,221.96 USD | `-11.89%` | `10X Cross` |
| `315` | `0x610b...b613` | `LONG` | 7,517,789.51 USD | `98,666,424.00` | `0.0872` | `0.0762` | `0.0600` | -1,082,392.39 USD | `-14.40%` | `5X Cross` |
| `601` | `0x5b5d...c060` | `SHORT` | 3,781,923.93 USD | `49,478,955.00` | `0.0946` | `0.0762` | `3.43` | 899,592.68 USD | `+23.79%` | `3X Cross` |
| `637` | `0xca49...53c8` | `SHORT` | 3,562,932.87 USD | `46,542,649.00` | `0.0929` | `0.0762` | `0.3739` | 763,111.81 USD | `+21.42%` | `10X Cross` |
| `653` | `0x45d2...4029` | `SHORT` | 3,474,044.20 USD | `45,426,000.00` | `0.0954` | `0.0762` | `0.9160` | 861,585.02 USD | `+24.80%` | `10X Cross` |
| `797` | `0xecb6...2b00` | `SHORT` | 2,859,076.60 USD | `37,341,822.00` | `0.0795` | `0.0762` | `0.7446` | 110,074.38 USD | `+3.85%` | `10X Cross` |
| `1204` | `0x458d...ab3b` | `LONG` | 1,870,735.82 USD | `24,454,063.00` | `0.1002` | `0.0762` | `0.0714` | -580,186.08 USD | `-31.01%` | `3X Isolated` |
| `1233` | `0xeadc...9d55` | `LONG` | 1,832,319.10 USD | `24,317,440.00` | `0.0926` | `0.0762` | `0.000000` | -419,275.47 USD | `-22.88%` | `10X Cross` |
| `1279` | `0x9aa5...58af` | `SHORT` | 1,771,021.18 USD | `23,500,500.00` | `0.0907` | `0.0762` | `0.4572` | 359,733.77 USD | `+20.31%` | `10X Cross` |
| `1372` | `0xf48f...10fe` | `LONG` | 1,638,974.02 USD | `21,424,497.00` | `0.0968` | `0.0762` | `0.0441` | -435,330.59 USD | `-26.56%` | `4X Cross` |
| `1396` | `0x9946...0852` | `SHORT` | 1,601,090.11 USD | `20,910,149.00` | `0.0871` | `0.0762` | `0.1432` | 219,465.28 USD | `+13.71%` | `10X Cross` |
| `1583` | `0xcac1...26b3` | `SHORT` | 1,386,648.50 USD | `18,126,835.00` | `0.0943` | `0.0762` | `0.5288` | 322,810.70 USD | `+23.28%` | `10X Cross` |
| `1621` | `0x0d6a...ca57` | `LONG` | 1,342,712.84 USD | `17,626,455.00` | `0.0875` | `0.0762` | `0.0626` | -199,392.12 USD | `-14.85%` | `3X Isolated` |
| `1688` | `0x4808...a82c` | `LONG` | 1,268,185.68 USD | `16,828,143.00` | `0.0883` | `0.0762` | `0.0632` | -218,287.30 USD | `-17.21%` | `3X Cross` |
| `1799` | `0x31ef...f715` | `LONG` | 1,157,198.38 USD | `15,230,102.00` | `0.0936` | `0.0762` | `0.0668` | -268,497.55 USD | `-23.20%` | `3X Isolated` |
| `1809` | `0xbfc7...80b4` | `SHORT` | 1,149,225.26 USD | `15,020,000.00` | `0.0920` | `0.0762` | `0.3522` | 233,174.03 USD | `+20.29%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0799` | 5,566.56 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 5.57K USD at 0.0799 USD [API] | `2026-10-28 12:10:03` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 12,027.54 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 12.03K USD at 0.0792 USD [API] | `2026-10-28 12:47:08` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 9,558.22 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 9.56K USD at 0.0792 USD [API] | `2026-10-28 12:47:08` |
| `ANNOUNCEMENT` | `INFO` | `0.0793` | 10,341.98 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 10.34K USD at 0.0793 USD [API] | `2026-10-28 12:50:25` |
| `ANNOUNCEMENT` | `INFO` | `0.0793` | 6,984.34 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 6.98K USD at 0.0793 USD [API] | `2026-10-28 12:55:48` |
| `ANNOUNCEMENT` | `INFO` | `0.0792` | 7,723.00 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 7.72K USD at 0.0792 USD [API] | `2026-10-28 13:21:12` |
| `ANNOUNCEMENT` | `INFO` | `0.0791` | 7,000.41 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 7.00K USD at 0.0791 USD [API] | `2026-10-28 13:28:04` |
| `ANNOUNCEMENT` | `INFO` | `0.0789` | 7,000.46 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 7.00K USD at 0.0789 USD [API] | `2026-10-28 14:00:34` |
| `ANNOUNCEMENT` | `INFO` | `0.0786` | 10,241.00 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 10.24K USD at 0.0786 USD [API] | `2026-10-28 14:22:34` |
| `ANNOUNCEMENT` | `INFO` | `0.0789` | 10,443.96 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 10.44K USD at 0.0789 USD [API] | `2026-10-28 14:31:03` |
| `ANNOUNCEMENT` | `INFO` | `0.0758` | 15,715.80 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 15.72K USD at 0.0758 USD [API] | `2026-10-24 14:18:09` |
| `ANNOUNCEMENT` | `INFO` | `0.0758` | 9,553.22 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Liquidated Long: 9.55K USD at 0.0758 USD [API] | `2026-10-24 14:18:09` |
| `ANNOUNCEMENT` | `INFO` | `0.0789` | 13,883.91 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale SELL: 13.88K USD at 0.0789 USD [API] | `2026-10-28 14:41:44` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0826` (Vol: 395,700.00 USD, Dist: `+5.32%`) | Long MP=`0.0767` (Vol: 519,500.00 USD, Dist: `--2.24%`)
  * 48H Horizon: Short MP=`0.0821` (Vol: 478,200.00 USD, Dist: `+4.71%`) | Long MP=`0.0774` (Vol: 691,800.00 USD, Dist: `--1.36%`)
  * 3D Horizon: Short MP=`0.0823` (Vol: 539,400.00 USD, Dist: `+4.91%`) | Long MP=`0.0765` (Vol: 660,700.00 USD, Dist: `--2.43%`)
  * 7D Horizon: Short MP=`0.0821` (Vol: 746,800.00 USD, Dist: `+4.72%`) | Long MP=`0.0762` (Vol: 988,700.00 USD, Dist: `--2.83%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0158` | 1,510.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0163` | 4,060.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0176` | 1,930.00 USD | 16,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0192` | 22,220.00 USD | 16,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0193` | 1,450.00 USD | 16,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0203` | 110.00 USD | 16,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0209` | 31,040.00 USD | 16,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0210` | 127.37 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0214` | 337.22 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0219` | 3,350.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0225` | 268.70 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0231` | 20,600.00 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0232` | 143.67 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0232` | 345.98 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0233` | 747.20 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0234` | 915.70 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0261` | 449.70 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0267` | 13,320.00 USD | 16,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0267` | 535.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0272` | 2,670.00 USD | 16,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0276` | 889.81 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0278` | 317.82 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0284` | 13,970.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0305` | 153.38 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0312` | 141.48 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0330` | 6,190.00 USD | 16,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0338` | 1,690.00 USD | 16,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0348` | 5,170.00 USD | 16,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0369` | 463.46 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0370` | 35,200.00 USD | 16,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0379` | 1,800.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 246.45 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0382` | 172.70 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 4,020.00 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0387` | 857.50 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0389` | 208.34 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0391` | 400.78 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 221.10 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0394` | 4,810.00 USD | 16,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0396` | 135.76 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 115.12 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 419.28 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0410` | 705.32 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0416` | 58,540.00 USD | 16,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 266.05 USD | 16,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 1,670.00 USD | 16,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 493.84 USD | 16,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 455.06 USD | 16,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 1,010.00 USD | 16,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 3,620.00 USD | 16,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 16,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 6,430.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 6,780.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0437` | 116,590.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 1,610.00 USD | 16,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 16,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,060.00 USD | 16,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 16,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 16,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 248.63 USD | 16,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 16,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 16,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 5,470.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 114.36 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 362.87 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 1,710.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0471` | 1,210.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 1,600.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 1,420.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 593.13 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 2,010.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 59,060.00 USD | 15,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 2,410.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 11,270.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,060,000.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 18,690.00 USD | 14,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,410.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,650.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 334.89 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 19,640.00 USD | 14,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 2,730.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 12,190.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 2,160.00 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0513` | 385.13 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 309.15 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 277.72 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 8,670.00 USD | 14,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 315,650.00 USD | 14,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 1,170.00 USD | 14,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,640.00 USD | 14,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 395.09 USD | 14,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 14,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 673.52 USD | 14,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 182,630.00 USD | 14,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 9,240.00 USD | 14,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 325.27 USD | 14,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 314,750.00 USD | 14,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 942.48 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0537` | 111,250.00 USD | 13,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 13,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,550.00 USD | 13,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 13,510.00 USD | 13,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 150,780.00 USD | 13,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 237.95 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 3,230.00 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 892.81 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 907.02 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0558` | 1,500.00 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0559` | 1,440.00 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 144.08 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 40,620.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 351.85 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 131.48 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 568.50 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 667.34 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 13,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 644.99 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 329.02 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 3,910.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,590.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,600.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 17,090.00 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 3,940.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 485.94 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 172.78 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 9,120.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 889.30 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 4,040.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 2,650.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 5,750.00 USD | 13,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 2,830.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 7,210.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 13,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 5,960,000.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 1,970.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,090.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 1,220.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 717.73 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 2,220.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 913.21 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 1,320.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 2,330.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 59,700.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 158.08 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 1,740.00 USD | 7,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0622` | 428.53 USD | 7,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 2,270.00 USD | 7,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 3,660.00 USD | 7,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,140,000.00 USD | 7,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 168.28 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 694.83 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 6,830.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 3,080.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,070,000.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 5,770.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 16,700.00 USD | 5,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 633.38 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 2,150.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 5,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,770.00 USD | 5,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 633.29 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 9,150.00 USD | 5,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 2,170.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 23,050.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 603.22 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0646` | 3,520.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 86,870.00 USD | 5,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 9,910.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 21,910.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 6,530.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 5,340.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0658` | 66,820.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,600.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 11,990.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0662` | 776.93 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 2,450.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 27,600.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,030.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 66,550.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 1,320.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,020,000.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 389.18 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 13,530.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0672` | 899.27 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 33,870.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 96,190.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0674` | 11,830,000.00 USD | 11,830,000.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0674` | 3,300.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 310.73 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0676` | 11,820,000.00 USD | 11,820,000.00 USD | 45,230.00 USD | 30,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0677` | 8,210.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 140,600.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0678` | 11,750,000.00 USD | 11,750,000.00 USD | 3,200.00 USD | 39,890.00 USD | 58,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0678` | 55,180.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0679` | 20,030.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0680` | 11,650,000.00 USD | 11,650,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0682` | 1,680.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0682` | 11,610,000.00 USD | 11,610,000.00 USD | 2,550.00 USD | 33,950.00 USD | 134,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0683` | 55,650.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0683` | 1,290.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0684` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0684` | 6,000.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 4,690.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0687` | 595.81 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0688` | 69,020.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0688` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0688` | 1,170.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0691` | 3,670.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0692` | 8,350.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0692` | 11,410,000.00 USD | 11,410,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0693` | 2,160.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,840.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0696` | 14,930.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0696` | 11,410,000.00 USD | 11,410,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 8,340.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,420.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0698` | 11,410,000.00 USD | 11,410,000.00 USD | 39,980.00 USD | 38,520.00 USD | 36,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 25,750.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0699` | 1,310.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0700` | 11,290,000.00 USD | 11,290,000.00 USD | 142,320.00 USD | 78,270.00 USD | 57,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 264.58 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0702` | 1,590.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0702` | 11,020,000.00 USD | 11,020,000.00 USD | 114,140.00 USD | 54,820.00 USD | 27,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 791.79 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0703` | 5,060.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0704` | 10,820,000.00 USD | 10,820,000.00 USD | 132,460.00 USD | 55,620.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0706` | 10,570,000.00 USD | 10,570,000.00 USD | 71,470.00 USD | 54,000.00 USD | 59,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 94,410.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0708` | 10,380,000.00 USD | 10,380,000.00 USD | 79,650.00 USD | 38,000.00 USD | 49,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0708` | 9,150.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0710` | 10,220,000.00 USD | 10,220,000.00 USD | 32,660.00 USD | 46,420.00 USD | 48,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0711` | 8,840.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0712` | 10,090,000.00 USD | 10,090,000.00 USD | 79,710.00 USD | 21,060.00 USD | 45,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 389.38 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 9,940,000.00 USD | 9,940,000.00 USD | 77,730.00 USD | 100,220.00 USD | 71,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 2,370.00 USD | 683,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 681,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 9,700,000.00 USD | 9,700,000.00 USD | 55,590.00 USD | 40,440.00 USD | 38,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,150.00 USD | 672,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0717` | 2,700.00 USD | 671,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 9,560,000.00 USD | 9,560,000.00 USD | 83,040.00 USD | 44,590.00 USD | 54,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 960.13 USD | 669,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0720` | 778.93 USD | 668,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 9,380,000.00 USD | 9,380,000.00 USD | 77,220.00 USD | 32,390.00 USD | 42,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 24,050.00 USD | 667,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0722` | 9,230,000.00 USD | 9,230,000.00 USD | 174,670.00 USD | 97,110.00 USD | 34,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 5,720.00 USD | 643,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0723` | 10,980.00 USD | 637,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 8,920,000.00 USD | 8,920,000.00 USD | 64,810.00 USD | 253,560.00 USD | 245,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 5,290.00 USD | 626,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0726` | 260.74 USD | 621,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0726` | 8,360,000.00 USD | 8,360,000.00 USD | 88,190.00 USD | 22,980.00 USD | 23,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 948.37 USD | 621,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0727` | 452.21 USD | 620,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0728` | 8,220,000.00 USD | 8,220,000.00 USD | 223,190.00 USD | 85,670.00 USD | 387,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0728` | 646.11 USD | 619,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0730` | 72,950.00 USD | 618,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0730` | 7,530,000.00 USD | 7,530,000.00 USD | 39,900.00 USD | 8,400.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0731` | 10,040.00 USD | 546,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,930.00 USD | 536,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0732` | 7,460,000.00 USD | 7,460,000.00 USD | 90,450.00 USD | 0.00 USD | 100.25 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 29,280.00 USD | 534,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0734` | 7,370,000.00 USD | 7,370,000.00 USD | 23,950.00 USD | 0.00 USD | 70,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0735` | 3,930.00 USD | 504,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0736` | 4,060.00 USD | 500,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0736` | 7,270,000.00 USD | 7,270,000.00 USD | 262,120.00 USD | 151,300.00 USD | 299.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 5,490.00 USD | 496,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0737` | 10,740.00 USD | 491,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0738` | 6,860,000.00 USD | 6,860,000.00 USD | 83,700.00 USD | 199,460.00 USD | 285,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0738` | 1,740.00 USD | 480,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0740` | 19,840.00 USD | 478,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0740` | 6,290,000.00 USD | 6,290,000.00 USD | 67,420.00 USD | 161,430.00 USD | 78,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 455,080.00 USD | 459,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0741` | 641.77 USD | 3,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0742` | 5,980,000.00 USD | 5,980,000.00 USD | 323,330.00 USD | 0.00 USD | 666,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0742` | 1,280.00 USD | 3,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0743` | 1,180.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0744` | 4,990,000.00 USD | 4,990,000.00 USD | 138,520.00 USD | 274,150.00 USD | 183,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0745` | 176.30 USD | 821.27 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0746` | 4,400,000.00 USD | 4,400,000.00 USD | 232,670.00 USD | 232,630.00 USD | 150,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 644.98 USD | 644.98 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0748` | 3,780,000.00 USD | 3,780,000.00 USD | 391,880.00 USD | 181,940.00 USD | 161,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0750` | 3,050,000.00 USD | 3,050,000.00 USD | 203,330.00 USD | 0.00 USD | 269,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0760` | 10,740.00 USD | 10,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0760` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 883.41 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0761` | 5,230.00 USD | 15,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0762` | 2,570,000.00 USD | 2,570,000.00 USD | 604,660.00 USD | 706,100.00 USD | 590.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0764` | 1,260,000.00 USD | 1,260,000.00 USD | 756,300.00 USD | 505,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0766` | 2,010,000.00 USD | 2,010,000.00 USD | 1,320,000.00 USD | 690,020.00 USD | 912.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0768` | 3,780,000.00 USD | 3,780,000.00 USD | 609,920.00 USD | 633,440.00 USD | 521,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0770` | 5,110,000.00 USD | 5,110,000.00 USD | 480,320.00 USD | 448,120.00 USD | 402,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0772` | 6,730,000.00 USD | 6,730,000.00 USD | 502,750.00 USD | 241,160.00 USD | 878,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0774` | 7,080,000.00 USD | 7,080,000.00 USD | 65,160.00 USD | 186,530.00 USD | 102,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0776` | 7,100,000.00 USD | 7,100,000.00 USD | 7,430.00 USD | 12,000.00 USD | 355.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0778` | 7,680,000.00 USD | 7,680,000.00 USD | 16,790.00 USD | 347,140.00 USD | 213,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0780` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 117,930.00 USD | 141,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0782` | 8,120,000.00 USD | 8,120,000.00 USD | 118,220.00 USD | 61,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0784` | 192.04 USD | 16,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0784` | 8,760,000.00 USD | 8,760,000.00 USD | 273,810.00 USD | 186,580.00 USD | 184,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0785` | 10,530.00 USD | 26,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0786` | 9,650,000.00 USD | 9,650,000.00 USD | 356,780.00 USD | 227,550.00 USD | 298,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0788` | 10,900,000.00 USD | 10,900,000.00 USD | 374,310.00 USD | 488,720.00 USD | 386,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0790` | 11,350,000.00 USD | 11,350,000.00 USD | 245,210.00 USD | 121,550.00 USD | 82,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0791` | 150.07 USD | 26,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0792` | 11,490,000.00 USD | 11,490,000.00 USD | 48,420.00 USD | 45,770.00 USD | 52,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0794` | 11,570,000.00 USD | 11,570,000.00 USD | 75,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0795` | 1,080.00 USD | 27,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0796` | 11,810,000.00 USD | 11,810,000.00 USD | 149,220.00 USD | 0.00 USD | 88,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0798` | 5,330.00 USD | 33,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0798` | 12,520,000.00 USD | 12,520,000.00 USD | 220,340.00 USD | 250,960.00 USD | 241,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0799` | 1,970.00 USD | 35,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0800` | 13,140,000.00 USD | 13,140,000.00 USD | 178,150.00 USD | 156,700.00 USD | 290,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0800` | 3,450.00 USD | 38,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0802` | 13,150,000.00 USD | 13,150,000.00 USD | 7,730.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 13,210,000.00 USD | 13,210,000.00 USD | 11,880.00 USD | 10,910.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0806` | 13,610,000.00 USD | 13,610,000.00 USD | 84,020.00 USD | 58,270.00 USD | 256,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 15,150,000.00 USD | 15,150,000.00 USD | 634,220.00 USD | 339,110.00 USD | 564,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 16,580,000.00 USD | 16,580,000.00 USD | 771,010.00 USD | 517,160.00 USD | 144,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 17,260,000.00 USD | 17,260,000.00 USD | 202,360.00 USD | 340,900.00 USD | 135,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 17,960,000.00 USD | 17,960,000.00 USD | 74,410.00 USD | 108,600.00 USD | 515,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 19,320,000.00 USD | 19,320,000.00 USD | 675,530.00 USD | 335,640.00 USD | 348,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0818` | 241.90 USD | 38,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0818` | 20,690,000.00 USD | 20,690,000.00 USD | 613,810.00 USD | 315,240.00 USD | 438,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 22,000,000.00 USD | 22,000,000.00 USD | 310,650.00 USD | 532,960.00 USD | 472,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 23,050,000.00 USD | 23,050,000.00 USD | 472,760.00 USD | 248,830.00 USD | 327,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0824` | 532.64 USD | 39,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0824` | 23,990,000.00 USD | 23,990,000.00 USD | 422,760.00 USD | 301,930.00 USD | 207,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 24,690,000.00 USD | 24,690,000.00 USD | 278,370.00 USD | 206,840.00 USD | 217,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 25,160,000.00 USD | 25,160,000.00 USD | 278,450.00 USD | 124,170.00 USD | 66,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0830` | 25,940,000.00 USD | 25,940,000.00 USD | 396,370.00 USD | 209,720.00 USD | 178,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 3,450.00 USD | 42,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 26,490,000.00 USD | 26,490,000.00 USD | 320,350.00 USD | 100,300.00 USD | 128,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 27,210,000.00 USD | 27,210,000.00 USD | 275,130.00 USD | 162,910.00 USD | 282,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0836` | 27,770,000.00 USD | 27,770,000.00 USD | 132,320.00 USD | 216,570.00 USD | 208,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 293.44 USD | 43,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 44,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 28,150,000.00 USD | 28,150,000.00 USD | 238,020.00 USD | 86,330.00 USD | 59,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0840` | 28,290,000.00 USD | 28,290,000.00 USD | 89,110.00 USD | 15,480.00 USD | 29,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0842` | 28,390,000.00 USD | 28,390,000.00 USD | 50,900.00 USD | 2,010.00 USD | 47,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 104.72 USD | 44,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0844` | 28,500,000.00 USD | 28,500,000.00 USD | 112,650.00 USD | 0.00 USD | 574.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0846` | 28,610,000.00 USD | 28,610,000.00 USD | 90,570.00 USD | 16,670.00 USD | 264.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0848` | 28,630,000.00 USD | 28,630,000.00 USD | 22,580.00 USD | 0.00 USD | 284.68 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0848` | 723.94 USD | 45,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0850` | 28,660,000.00 USD | 28,660,000.00 USD | 23,830.00 USD | 0.00 USD | 448.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0852` | 28,730,000.00 USD | 28,730,000.00 USD | 35,100.00 USD | 24,590.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0854` | 28,810,000.00 USD | 28,810,000.00 USD | 40,150.00 USD | 13,930.00 USD | 20,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0856` | 29,100,000.00 USD | 29,100,000.00 USD | 159,460.00 USD | 78,270.00 USD | 56,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0858` | 29,300,000.00 USD | 29,300,000.00 USD | 121,210.00 USD | 54,820.00 USD | 27,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 45,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0860` | 29,550,000.00 USD | 29,550,000.00 USD | 130,590.00 USD | 55,620.00 USD | 60,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0862` | 29,720,000.00 USD | 29,720,000.00 USD | 54,010.00 USD | 54,000.00 USD | 57,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0862` | 2,340.00 USD | 48,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0864` | 29,760,000.00 USD | 29,760,000.00 USD | 22,510.00 USD | 20,050.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0866` | 29,880,000.00 USD | 29,880,000.00 USD | 57,180.00 USD | 17,950.00 USD | 44,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0868` | 30,010,000.00 USD | 30,010,000.00 USD | 32,660.00 USD | 46,420.00 USD | 48,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0870` | 30,140,000.00 USD | 30,140,000.00 USD | 68,060.00 USD | 21,060.00 USD | 42,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0872` | 30,380,000.00 USD | 30,380,000.00 USD | 67,420.00 USD | 100,220.00 USD | 71,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0874` | 30,450,000.00 USD | 30,450,000.00 USD | 19,050.00 USD | 8,830.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0876` | 30,510,000.00 USD | 30,510,000.00 USD | 30,130.00 USD | 31,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0878` | 30,660,000.00 USD | 30,660,000.00 USD | 50,320.00 USD | 44,590.00 USD | 54,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0880` | 30,760,000.00 USD | 30,760,000.00 USD | 50,910.00 USD | 17,330.00 USD | 38,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 48,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 48,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 49,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0895` | 1,230.00 USD | 50,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0911` | 743.15 USD | 51,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0912` | 4,040.00 USD | 55,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0914` | 171.19 USD | 55,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 55,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 13,800.00 USD | 69,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0953` | 47,620.00 USD | 117,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0954` | 928.33 USD | 118,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0959` | 195.05 USD | 118,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 118,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0978` | 1,880.00 USD | 120,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0979` | 39,190.00 USD | 159,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 160,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0984` | 4,430.00 USD | 164,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0984` | 10,510.00 USD | 175,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 7,630.00 USD | 182,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 185,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 186,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1032` | 1,330.00 USD | 187,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1048` | 2,460.00 USD | 190,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 196,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1070` | 4,150.00 USD | 200,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1085` | 3,240.00 USD | 203,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1120` | 1,870.00 USD | 205,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 205,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1129` | 142.88 USD | 205,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1132` | 3,390.00 USD | 209,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1139` | 3,530.00 USD | 212,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1187` | 106.19 USD | 212,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 796.83 USD | 213,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1237` | 893.35 USD | 214,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 214,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 214,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 3,340.00 USD | 218,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 218,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 218,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1353` | 34,940.00 USD | 253,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1373` | 22,260.00 USD | 275,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1376` | 2,060.00 USD | 277,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1388` | 416.25 USD | 278,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 278,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1411` | 1,800.00 USD | 280,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1432` | 1,860.00 USD | 282,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1444` | 1,540.00 USD | 284,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,300.00 USD | 292,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1497` | 1,980.00 USD | 294,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1502` | 3,140,000.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0158` | 16,520,000.00 USD | 0.00 USD | 1,510.00 USD | `-79.07%` | `95,954.00` |
| `Live` | `Long` | `0.0160` | 16,520,000.00 USD | 0.00 USD | 3,930.00 USD | `-78.68%` | `244,573.00` |
| `Live` | `Long` | `0.0163` | 16,510,000.00 USD | 0.00 USD | 4,060.00 USD | `-78.41%` | `250,000.00` |
| `Live` | `Long` | `0.0164` | 16,510,000.00 USD | 0.00 USD | 407.02 USD | `-78.14%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 16,510,000.00 USD | 0.00 USD | 5,290.00 USD | `-78.01%` | `319,394.00` |
| `Live` | `Long` | `0.0176` | 16,500,000.00 USD | 0.00 USD | 1,930.00 USD | `-76.55%` | `109,191.00` |
| `Live` | `Long` | `0.0192` | 16,500,000.00 USD | 0.00 USD | 22,220.00 USD | `-74.56%` | `1,160,480.00` |
| `Live` | `Long` | `0.0193` | 16,480,000.00 USD | 0.00 USD | 1,450.00 USD | `-74.29%` | `75,012.00` |
| `Live` | `Long` | `0.0203` | 16,480,000.00 USD | 0.00 USD | 110.00 USD | `-73.10%` | `5,432.00` |
| `Live` | `Long` | `0.0209` | 16,480,000.00 USD | 0.00 USD | 31,040.00 USD | `-72.30%` | `1,488,849.00` |
| `Live` | `Long` | `0.0210` | 16,450,000.00 USD | 0.00 USD | 127.37 USD | `-72.03%` | `6,051.00` |
| `Live` | `Long` | `0.0214` | 16,450,000.00 USD | 0.00 USD | 337.22 USD | `-71.63%` | `15,795.00` |
| `Live` | `Long` | `0.0219` | 16,450,000.00 USD | 0.00 USD | 3,350.00 USD | `-70.97%` | `153,201.00` |
| `Live` | `Long` | `0.0225` | 16,440,000.00 USD | 0.00 USD | 268.70 USD | `-70.17%` | `11,969.00` |
| `Live` | `Long` | `0.0231` | 16,440,000.00 USD | 0.00 USD | 20,600.00 USD | `-69.38%` | `893,720.00` |
| `Live` | `Long` | `0.0232` | 16,420,000.00 USD | 0.00 USD | 143.67 USD | `-69.24%` | `6,206.00` |
| `Live` | `Long` | `0.0232` | 16,420,000.00 USD | 0.00 USD | 345.98 USD | `-69.11%` | `14,881.00` |
| `Live` | `Long` | `0.0233` | 16,420,000.00 USD | 0.00 USD | 747.20 USD | `-68.98%` | `32,000.00` |
| `Live` | `Long` | `0.0234` | 16,420,000.00 USD | 0.00 USD | 915.70 USD | `-68.84%` | `39,049.00` |
| `Live` | `Long` | `0.0261` | 16,420,000.00 USD | 0.00 USD | 449.70 USD | `-65.39%` | `17,263.00` |
| `Live` | `Long` | `0.0267` | 16,420,000.00 USD | 0.00 USD | 13,320.00 USD | `-64.59%` | `500,000.00` |
| `Live` | `Long` | `0.0267` | 16,410,000.00 USD | 0.00 USD | 535.00 USD | `-64.46%` | `20,000.00` |
| `Live` | `Long` | `0.0272` | 16,410,000.00 USD | 0.00 USD | 2,670.00 USD | `-63.93%` | `98,319.00` |
| `Live` | `Long` | `0.0276` | 16,400,000.00 USD | 0.00 USD | 889.81 USD | `-63.40%` | `32,298.00` |
| `Live` | `Long` | `0.0278` | 16,400,000.00 USD | 0.00 USD | 317.82 USD | `-63.13%` | `11,453.00` |
| `Live` | `Long` | `0.0279` | 16,400,000.00 USD | 0.00 USD | 1,730.00 USD | `-62.87%` | `61,775.00` |
| `Live` | `Long` | `0.0284` | 16,400,000.00 USD | 0.00 USD | 13,970.00 USD | `-62.20%` | `491,018.00` |
| `Live` | `Long` | `0.0305` | 16,390,000.00 USD | 0.00 USD | 153.38 USD | `-59.54%` | `5,037.00` |
| `Live` | `Long` | `0.0306` | 16,390,000.00 USD | 0.00 USD | 137.41 USD | `-59.41%` | `4,498.00` |
| `Live` | `Long` | `0.0312` | 16,390,000.00 USD | 0.00 USD | 141.48 USD | `-58.61%` | `4,542.00` |
| `Live` | `Long` | `0.0330` | 16,390,000.00 USD | 0.00 USD | 6,190.00 USD | `-56.22%` | `187,979.00` |
| `Live` | `Long` | `0.0338` | 16,380,000.00 USD | 0.00 USD | 1,690.00 USD | `-55.16%` | `50,000.00` |
| `Live` | `Long` | `0.0348` | 16,380,000.00 USD | 0.00 USD | 5,170.00 USD | `-53.70%` | `148,480.00` |
| `Live` | `Long` | `0.0358` | 16,370,000.00 USD | 0.00 USD | 214.53 USD | `-52.37%` | `5,984.00` |
| `Live` | `Long` | `0.0369` | 16,370,000.00 USD | 0.00 USD | 463.46 USD | `-50.91%` | `12,543.00` |
| `Live` | `Long` | `0.0370` | 16,370,000.00 USD | 0.00 USD | 35,200.00 USD | `-50.77%` | `950,000.00` |
| `Live` | `Long` | `0.0379` | 16,340,000.00 USD | 0.00 USD | 1,800.00 USD | `-49.71%` | `47,501.00` |
| `Live` | `Long` | `0.0381` | 16,340,000.00 USD | 0.00 USD | 246.45 USD | `-49.45%` | `6,477.00` |
| `Live` | `Long` | `0.0382` | 16,330,000.00 USD | 0.00 USD | 172.70 USD | `-49.18%` | `4,515.00` |
| `Live` | `Long` | `0.0386` | 16,330,000.00 USD | 0.00 USD | 4,020.00 USD | `-48.78%` | `104,284.00` |
| `Live` | `Long` | `0.0387` | 16,330,000.00 USD | 0.00 USD | 857.50 USD | `-48.52%` | `22,129.00` |
| `Live` | `Long` | `0.0389` | 16,330,000.00 USD | 0.00 USD | 208.34 USD | `-48.25%` | `5,349.00` |
| `Live` | `Long` | `0.0391` | 16,330,000.00 USD | 0.00 USD | 400.78 USD | `-47.98%` | `10,237.00` |
| `Live` | `Long` | `0.0393` | 16,330,000.00 USD | 0.00 USD | 221.10 USD | `-47.85%` | `5,633.00` |
| `Live` | `Long` | `0.0394` | 16,330,000.00 USD | 0.00 USD | 4,810.00 USD | `-47.72%` | `122,306.00` |
| `Live` | `Long` | `0.0396` | 16,320,000.00 USD | 0.00 USD | 135.76 USD | `-47.32%` | `3,424.00` |
| `Live` | `Long` | `0.0404` | 16,320,000.00 USD | 0.00 USD | 115.12 USD | `-46.26%` | `2,846.00` |
| `Live` | `Long` | `0.0408` | 16,320,000.00 USD | 0.00 USD | 419.28 USD | `-45.86%` | `10,289.00` |
| `Live` | `Long` | `0.0410` | 16,320,000.00 USD | 0.00 USD | 705.32 USD | `-45.59%` | `17,224.00` |
| `Live` | `Long` | `0.0415` | 16,320,000.00 USD | 0.00 USD | 1,030.00 USD | `-44.80%` | `24,809.00` |
| `Live` | `Long` | `0.0416` | 16,320,000.00 USD | 0.00 USD | 58,540.00 USD | `-44.66%` | `1,405,488.00` |
| `Live` | `Long` | `0.0420` | 16,260,000.00 USD | 0.00 USD | 266.05 USD | `-44.26%` | `6,342.00` |
| `Live` | `Long` | `0.0423` | 16,260,000.00 USD | 0.00 USD | 1,670.00 USD | `-43.87%` | `39,500.00` |
| `Live` | `Long` | `0.0423` | 16,260,000.00 USD | 0.00 USD | 493.84 USD | `-43.73%` | `11,661.00` |
| `Live` | `Long` | `0.0425` | 16,260,000.00 USD | 0.00 USD | 455.06 USD | `-43.60%` | `10,720.00` |
| `Live` | `Long` | `0.0425` | 16,260,000.00 USD | 0.00 USD | 1,010.00 USD | `-43.47%` | `23,716.00` |
| `Live` | `Long` | `0.0427` | 16,260,000.00 USD | 0.00 USD | 3,620.00 USD | `-43.33%` | `84,760.00` |
| `Live` | `Long` | `0.0430` | 16,260,000.00 USD | 0.00 USD | 859.00 USD | `-42.94%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 16,250,000.00 USD | 0.00 USD | 6,430.00 USD | `-42.54%` | `148,704.00` |
| `Live` | `Long` | `0.0433` | 16,250,000.00 USD | 0.00 USD | 6,780.00 USD | `-42.40%` | `156,456.00` |
| `Live` | `Long` | `0.0437` | 16,240,000.00 USD | 0.00 USD | 116,590.00 USD | `-41.87%` | `2,664,805.00` |
| `Live` | `Long` | `0.0439` | 16,130,000.00 USD | 0.00 USD | 1,610.00 USD | `-41.74%` | `36,807.00` |
| `Live` | `Long` | `0.0440` | 16,120,000.00 USD | 0.00 USD | 750.58 USD | `-41.61%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 16,120,000.00 USD | 0.00 USD | 1,060.00 USD | `-41.47%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 16,120,000.00 USD | 0.00 USD | 101,440.00 USD | `-41.08%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 16,020,000.00 USD | 0.00 USD | 444.76 USD | `-40.68%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 16,020,000.00 USD | 0.00 USD | 248.63 USD | `-40.54%` | `5,556.00` |
| `Live` | `Long` | `0.0454` | 16,020,000.00 USD | 0.00 USD | 2,170.00 USD | `-39.61%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 16,020,000.00 USD | 0.00 USD | 32,650.00 USD | `-39.48%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 15,980,000.00 USD | 0.00 USD | 5,470.00 USD | `-39.22%` | `119,571.00` |
| `Live` | `Long` | `0.0461` | 15,980,000.00 USD | 0.00 USD | 4,500.00 USD | `-38.82%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 15,970,000.00 USD | 0.00 USD | 114.36 USD | `-38.68%` | `2,478.00` |
| `Live` | `Long` | `0.0464` | 15,970,000.00 USD | 0.00 USD | 362.87 USD | `-38.42%` | `7,829.00` |
| `Live` | `Long` | `0.0464` | 15,970,000.00 USD | 0.00 USD | 16,780.00 USD | `-38.29%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 15,960,000.00 USD | 0.00 USD | 1,710.00 USD | `-38.15%` | `36,724.00` |
| `Live` | `Long` | `0.0466` | 15,960,000.00 USD | 0.00 USD | 109.49 USD | `-38.02%` | `2,347.00` |
| `Live` | `Long` | `0.0471` | 15,960,000.00 USD | 0.00 USD | 1,210.00 USD | `-37.49%` | `25,729.00` |
| `Live` | `Long` | `0.0473` | 15,950,000.00 USD | 0.00 USD | 1,600.00 USD | `-37.22%` | `33,899.00` |
| `Live` | `Long` | `0.0474` | 15,950,000.00 USD | 0.00 USD | 1,420.00 USD | `-37.09%` | `29,884.00` |
| `Live` | `Long` | `0.0474` | 15,950,000.00 USD | 0.00 USD | 593.13 USD | `-36.96%` | `12,500.00` |
| `Live` | `Long` | `0.0476` | 15,950,000.00 USD | 0.00 USD | 2,010.00 USD | `-36.69%` | `42,211.00` |
| `Live` | `Long` | `0.0481` | 15,950,000.00 USD | 0.00 USD | 59,060.00 USD | `-36.03%` | `1,226,627.00` |
| `Live` | `Long` | `0.0483` | 15,890,000.00 USD | 0.00 USD | 2,410.00 USD | `-35.76%` | `49,758.00` |
| `Live` | `Long` | `0.0485` | 15,890,000.00 USD | 0.00 USD | 1,480.00 USD | `-35.63%` | `30,533.00` |
| `Live` | `Long` | `0.0488` | 15,890,000.00 USD | 0.00 USD | 1,280.00 USD | `-35.10%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 15,880,000.00 USD | 0.00 USD | 11,270.00 USD | `-34.96%` | `230,133.00` |
| `Live` | `Long` | `0.0491` | 15,870,000.00 USD | 0.00 USD | 1,080.00 USD | `-34.83%` | `21,989.00` |
| `Live` | `Long` | `0.0491` | 15,870,000.00 USD | 0.00 USD | 1,060,000.00 USD | `-34.70%` | `21,649,147.00` |
| `Live` | `Long` | `0.0495` | 14,810,000.00 USD | 0.00 USD | 18,690.00 USD | `-34.17%` | `377,099.00` |
| `Live` | `Long` | `0.0498` | 14,790,000.00 USD | 0.00 USD | 253.82 USD | `-33.90%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 14,790,000.00 USD | 0.00 USD | 501.50 USD | `-33.50%` | `10,020.00` |
| `Live` | `Long` | `0.0503` | 14,790,000.00 USD | 0.00 USD | 5,410.00 USD | `-33.24%` | `107,572.00` |
| `Live` | `Long` | `0.0503` | 14,780,000.00 USD | 0.00 USD | 5,650.00 USD | `-33.10%` | `112,151.00` |
| `Live` | `Long` | `0.0505` | 14,780,000.00 USD | 0.00 USD | 334.89 USD | `-32.97%` | `6,638.00` |
| `Live` | `Long` | `0.0507` | 14,780,000.00 USD | 0.00 USD | 1,040.00 USD | `-32.71%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,780,000.00 USD | 0.00 USD | 19,640.00 USD | `-32.57%` | `386,933.00` |
| `Live` | `Long` | `0.0510` | 14,760,000.00 USD | 0.00 USD | 2,730.00 USD | `-32.31%` | `53,578.00` |
| `Live` | `Long` | `0.0510` | 14,750,000.00 USD | 0.00 USD | 566.65 USD | `-32.17%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,750,000.00 USD | 0.00 USD | 12,190.00 USD | `-32.04%` | `238,328.00` |
| `Live` | `Long` | `0.0512` | 14,740,000.00 USD | 0.00 USD | 2,160.00 USD | `-31.91%` | `42,240.00` |
| `Live` | `Long` | `0.0513` | 14,740,000.00 USD | 0.00 USD | 385.13 USD | `-31.78%` | `7,500.00` |
| `Live` | `Long` | `0.0515` | 14,740,000.00 USD | 0.00 USD | 309.15 USD | `-31.51%` | `5,997.00` |
| `Live` | `Long` | `0.0520` | 14,740,000.00 USD | 0.00 USD | 277.72 USD | `-30.98%` | `5,346.00` |
| `Live` | `Long` | `0.0520` | 14,740,000.00 USD | 0.00 USD | 8,670.00 USD | `-30.85%` | `166,663.00` |
| `Live` | `Long` | `0.0522` | 14,730,000.00 USD | 0.00 USD | 315,650.00 USD | `-30.58%` | `6,041,244.00` |
| `Live` | `Long` | `0.0524` | 14,410,000.00 USD | 0.00 USD | 1,170.00 USD | `-30.31%` | `22,383.00` |
| `Live` | `Long` | `0.0525` | 14,410,000.00 USD | 0.00 USD | 5,640.00 USD | `-30.18%` | `107,299.00` |
| `Live` | `Long` | `0.0527` | 14,410,000.00 USD | 0.00 USD | 395.09 USD | `-30.05%` | `7,504.00` |
| `Live` | `Long` | `0.0527` | 14,410,000.00 USD | 0.00 USD | 2,110.00 USD | `-29.92%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,400,000.00 USD | 0.00 USD | 673.52 USD | `-29.78%` | `12,744.00` |
| `Live` | `Long` | `0.0529` | 14,400,000.00 USD | 0.00 USD | 182,630.00 USD | `-29.65%` | `3,449,122.00` |
| `Live` | `Long` | `0.0532` | 14,220,000.00 USD | 0.00 USD | 9,240.00 USD | `-29.38%` | `173,844.00` |
| `Live` | `Long` | `0.0534` | 14,210,000.00 USD | 0.00 USD | 325.27 USD | `-29.12%` | `6,097.00` |
| `Live` | `Long` | `0.0534` | 14,210,000.00 USD | 0.00 USD | 314,750.00 USD | `-28.99%` | `5,888,653.00` |
| `Live` | `Long` | `0.0536` | 13,900,000.00 USD | 0.00 USD | 942.48 USD | `-28.85%` | `17,600.00` |
| `Live` | `Long` | `0.0537` | 13,900,000.00 USD | 0.00 USD | 111,250.00 USD | `-28.59%` | `2,069,770.00` |
| `Live` | `Long` | `0.0539` | 13,780,000.00 USD | 0.00 USD | 5,290.00 USD | `-28.32%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 13,780,000.00 USD | 0.00 USD | 2,550.00 USD | `-28.19%` | `47,142.00` |
| `Live` | `Long` | `0.0541` | 13,780,000.00 USD | 0.00 USD | 13,510.00 USD | `-28.06%` | `249,542.00` |
| `Live` | `Long` | `0.0542` | 13,760,000.00 USD | 0.00 USD | 150,780.00 USD | `-27.92%` | `2,779,342.00` |
| `Live` | `Long` | `0.0544` | 13,610,000.00 USD | 0.00 USD | 237.95 USD | `-27.66%` | `4,370.00` |
| `Live` | `Long` | `0.0546` | 13,610,000.00 USD | 0.00 USD | 3,230.00 USD | `-27.39%` | `59,031.00` |
| `Live` | `Long` | `0.0548` | 13,610,000.00 USD | 0.00 USD | 892.81 USD | `-27.26%` | `16,307.00` |
| `Live` | `Long` | `0.0556` | 13,610,000.00 USD | 0.00 USD | 907.02 USD | `-26.20%` | `16,328.00` |
| `Live` | `Long` | `0.0558` | 13,610,000.00 USD | 0.00 USD | 1,500.00 USD | `-25.93%` | `26,900.00` |
| `Live` | `Long` | `0.0559` | 13,610,000.00 USD | 0.00 USD | 1,440.00 USD | `-25.66%` | `25,791.00` |
| `Live` | `Long` | `0.0561` | 13,600,000.00 USD | 0.00 USD | 144.08 USD | `-25.40%` | `2,566.00` |
| `Live` | `Long` | `0.0563` | 13,600,000.00 USD | 0.00 USD | 40,620.00 USD | `-25.27%` | `722,065.00` |
| `Live` | `Long` | `0.0563` | 13,560,000.00 USD | 0.00 USD | 351.85 USD | `-25.13%` | `6,244.00` |
| `Live` | `Long` | `0.0566` | 13,560,000.00 USD | 0.00 USD | 131.48 USD | `-24.87%` | `2,325.00` |
| `Live` | `Long` | `0.0568` | 13,560,000.00 USD | 0.00 USD | 568.50 USD | `-24.47%` | `10,000.00` |
| `Live` | `Long` | `0.0570` | 13,560,000.00 USD | 0.00 USD | 667.34 USD | `-24.34%` | `11,718.00` |
| `Live` | `Long` | `0.0570` | 13,560,000.00 USD | 0.00 USD | 8,350.00 USD | `-24.20%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,550,000.00 USD | 0.00 USD | 644.99 USD | `-24.07%` | `11,286.00` |
| `Live` | `Long` | `0.0573` | 13,550,000.00 USD | 0.00 USD | 329.02 USD | `-23.94%` | `5,747.00` |
| `Live` | `Long` | `0.0573` | 13,550,000.00 USD | 0.00 USD | 3,910.00 USD | `-23.80%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 13,550,000.00 USD | 0.00 USD | 3,590.00 USD | `-23.54%` | `62,330.00` |
| `Live` | `Long` | `0.0576` | 13,540,000.00 USD | 0.00 USD | 10,600.00 USD | `-23.40%` | `183,894.00` |
| `Live` | `Long` | `0.0578` | 13,530,000.00 USD | 0.00 USD | 17,090.00 USD | `-23.27%` | `295,980.00` |
| `Live` | `Long` | `0.0578` | 13,520,000.00 USD | 0.00 USD | 3,940.00 USD | `-23.14%` | `68,112.00` |
| `Live` | `Long` | `0.0580` | 13,510,000.00 USD | 0.00 USD | 431.14 USD | `-22.87%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 13,510,000.00 USD | 0.00 USD | 447.17 USD | `-22.74%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 13,510,000.00 USD | 0.00 USD | 485.94 USD | `-22.47%` | `8,328.00` |
| `Live` | `Long` | `0.0585` | 13,510,000.00 USD | 0.00 USD | 172.78 USD | `-22.21%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 13,510,000.00 USD | 0.00 USD | 9,120.00 USD | `-21.94%` | `155,271.00` |
| `Live` | `Long` | `0.0590` | 13,500,000.00 USD | 0.00 USD | 212.22 USD | `-21.68%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 13,500,000.00 USD | 0.00 USD | 26,980.00 USD | `-21.41%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 13,480,000.00 USD | 0.00 USD | 889.30 USD | `-21.15%` | `14,984.00` |
| `Live` | `Long` | `0.0595` | 13,470,000.00 USD | 0.00 USD | 4,040.00 USD | `-21.01%` | `67,874.00` |
| `Live` | `Long` | `0.0595` | 13,470,000.00 USD | 0.00 USD | 2,650.00 USD | `-20.88%` | `44,458.00` |
| `Live` | `Long` | `0.0599` | 13,470,000.00 USD | 0.00 USD | 5,750.00 USD | `-20.48%` | `96,079.00` |
| `Live` | `Long` | `0.0600` | 13,460,000.00 USD | 0.00 USD | 2,830.00 USD | `-20.35%` | `47,268.00` |
| `Live` | `Long` | `0.0600` | 13,460,000.00 USD | 0.00 USD | 7,210.00 USD | `-20.22%` | `120,088.00` |
| `Live` | `Long` | `0.0602` | 13,450,000.00 USD | 0.00 USD | 8,490.00 USD | `-20.08%` | `141,093.00` |
| `Live` | `Long` | `0.0604` | 13,440,000.00 USD | 0.00 USD | 5,960,000.00 USD | `-19.82%` | `98,689,541.00` |
| `Live` | `Long` | `0.0604` | 7,490,000.00 USD | 0.00 USD | 1,970.00 USD | `-19.68%` | `32,592.00` |
| `Live` | `Long` | `0.0605` | 7,490,000.00 USD | 0.00 USD | 32,090.00 USD | `-19.55%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 7,450,000.00 USD | 0.00 USD | 1,220.00 USD | `-19.29%` | `20,080.00` |
| `Live` | `Long` | `0.0609` | 7,450,000.00 USD | 0.00 USD | 717.73 USD | `-19.15%` | `11,795.00` |
| `Live` | `Long` | `0.0609` | 7,450,000.00 USD | 0.00 USD | 2,220.00 USD | `-19.02%` | `36,478.00` |
| `Live` | `Long` | `0.0612` | 7,450,000.00 USD | 0.00 USD | 913.21 USD | `-18.75%` | `14,934.00` |
| `Live` | `Long` | `0.0612` | 7,450,000.00 USD | 0.00 USD | 1,320.00 USD | `-18.62%` | `21,534.00` |
| `Live` | `Long` | `0.0614` | 7,450,000.00 USD | 0.00 USD | 655.16 USD | `-18.49%` | `10,679.00` |
| `Live` | `Long` | `0.0616` | 7,450,000.00 USD | 0.00 USD | 2,330.00 USD | `-18.22%` | `37,794.00` |
| `Live` | `Long` | `0.0617` | 7,440,000.00 USD | 0.00 USD | 59,700.00 USD | `-18.09%` | `968,374.00` |
| `Live` | `Long` | `0.0617` | 7,380,000.00 USD | 0.00 USD | 158.08 USD | `-17.96%` | `2,560.00` |
| `Live` | `Long` | `0.0621` | 7,380,000.00 USD | 0.00 USD | 26,790.00 USD | `-17.56%` | `431,787.00` |
| `Live` | `Long` | `0.0621` | 7,360,000.00 USD | 0.00 USD | 1,740.00 USD | `-17.43%` | `27,935.00` |
| `Live` | `Long` | `0.0622` | 7,360,000.00 USD | 0.00 USD | 428.53 USD | `-17.29%` | `6,884.00` |
| `Live` | `Long` | `0.0624` | 7,360,000.00 USD | 0.00 USD | 2,270.00 USD | `-17.16%` | `36,431.00` |
| `Live` | `Long` | `0.0624` | 7,350,000.00 USD | 0.00 USD | 3,660.00 USD | `-17.03%` | `58,632.00` |
| `Live` | `Long` | `0.0625` | 7,350,000.00 USD | 0.00 USD | 1,140,000.00 USD | `-16.89%` | `18,274,137.00` |
| `Live` | `Long` | `0.0626` | 6,210,000.00 USD | 0.00 USD | 168.28 USD | `-16.76%` | `2,686.00` |
| `Live` | `Long` | `0.0628` | 6,210,000.00 USD | 0.00 USD | 694.83 USD | `-16.63%` | `11,073.00` |
| `Live` | `Long` | `0.0629` | 6,210,000.00 USD | 0.00 USD | 6,830.00 USD | `-16.50%` | `108,608.00` |
| `Live` | `Long` | `0.0630` | 6,200,000.00 USD | 0.00 USD | 3,080.00 USD | `-16.23%` | `48,869.00` |
| `Live` | `Long` | `0.0631` | 6,200,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-16.10%` | `16,926,907.00` |
| `Live` | `Long` | `0.0633` | 5,130,000.00 USD | 0.00 USD | 5,770.00 USD | `-15.96%` | `91,237.00` |
| `Live` | `Long` | `0.0634` | 5,120,000.00 USD | 0.00 USD | 16,700.00 USD | `-15.83%` | `263,544.00` |
| `Live` | `Long` | `0.0635` | 5,100,000.00 USD | 0.00 USD | 1,690.00 USD | `-15.70%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 5,100,000.00 USD | 0.00 USD | 280.95 USD | `-15.57%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 5,100,000.00 USD | 0.00 USD | 633.38 USD | `-15.43%` | `9,951.00` |
| `Live` | `Long` | `0.0638` | 5,100,000.00 USD | 0.00 USD | 2,150.00 USD | `-15.30%` | `33,786.00` |
| `Live` | `Long` | `0.0639` | 5,100,000.00 USD | 0.00 USD | 23,220.00 USD | `-15.17%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 5,080,000.00 USD | 0.00 USD | 1,770.00 USD | `-15.03%` | `27,679.00` |
| `Live` | `Long` | `0.0641` | 5,070,000.00 USD | 0.00 USD | 633.29 USD | `-14.77%` | `9,872.00` |
| `Live` | `Long` | `0.0643` | 5,070,000.00 USD | 0.00 USD | 9,150.00 USD | `-14.64%` | `142,397.00` |
| `Live` | `Long` | `0.0644` | 5,060,000.00 USD | 0.00 USD | 2,170.00 USD | `-14.50%` | `33,693.00` |
| `Live` | `Long` | `0.0644` | 5,060,000.00 USD | 0.00 USD | 23,050.00 USD | `-14.37%` | `357,682.00` |
| `Live` | `Long` | `0.0645` | 5,040,000.00 USD | 0.00 USD | 603.22 USD | `-14.24%` | `9,345.00` |
| `Live` | `Long` | `0.0646` | 5,040,000.00 USD | 0.00 USD | 3,520.00 USD | `-14.10%` | `54,442.00` |
| `Live` | `Long` | `0.0648` | 5,040,000.00 USD | 0.00 USD | 86,870.00 USD | `-13.97%` | `1,341,590.00` |
| `Live` | `Long` | `0.0649` | 4,950,000.00 USD | 0.00 USD | 9,910.00 USD | `-13.84%` | `152,854.00` |
| `Live` | `Long` | `0.0649` | 4,940,000.00 USD | 0.00 USD | 21,910.00 USD | `-13.71%` | `337,347.00` |
| `Live` | `Long` | `0.0651` | 4,920,000.00 USD | 0.00 USD | 2,380.00 USD | `-13.44%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,910,000.00 USD | 0.00 USD | 13,770.00 USD | `-13.31%` | `210,965.00` |
| `Live` | `Long` | `0.0654` | 4,900,000.00 USD | 0.00 USD | 6,530.00 USD | `-13.17%` | `100,000.00` |
| `Live` | `Long` | `0.0655` | 4,890,000.00 USD | 0.00 USD | 5,340.00 USD | `-12.91%` | `81,453.00` |
| `Live` | `Long` | `0.0658` | 4,890,000.00 USD | 0.00 USD | 66,820.00 USD | `-12.64%` | `1,016,348.00` |
| `Live` | `Long` | `0.0659` | 4,820,000.00 USD | 0.00 USD | 14,600.00 USD | `-12.51%` | `221,719.00` |
| `Live` | `Long` | `0.0659` | 4,810,000.00 USD | 0.00 USD | 11,990.00 USD | `-12.38%` | `181,801.00` |
| `Live` | `Long` | `0.0662` | 4,800,000.00 USD | 0.00 USD | 776.93 USD | `-12.11%` | `11,745.00` |
| `Live` | `Long` | `0.0663` | 4,790,000.00 USD | 0.00 USD | 2,450.00 USD | `-11.98%` | `36,920.00` |
| `Live` | `Long` | `0.0664` | 4,790,000.00 USD | 0.00 USD | 27,600.00 USD | `-11.85%` | `415,904.00` |
| `Live` | `Long` | `0.0664` | 4,760,000.00 USD | 0.00 USD | 1,030.00 USD | `-11.71%` | `15,449.00` |
| `Live` | `Long` | `0.0665` | 4,760,000.00 USD | 0.00 USD | 66,550.00 USD | `-11.58%` | `1,000,000.00` |
| `Live` | `Long` | `0.0667` | 4,700,000.00 USD | 0.00 USD | 34,860.00 USD | `-11.45%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-11.31%` | `19,836.00` |
| `Live` | `Long` | `0.0669` | 4,660,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-11.18%` | `15,230,102.00` |
| `Live` | `Long` | `0.0669` | 3,640,000.00 USD | 0.00 USD | 389.18 USD | `-11.05%` | `5,813.00` |
| `Live` | `Long` | `0.0670` | 3,640,000.00 USD | 0.00 USD | 13,530.00 USD | `-10.92%` | `201,862.00` |
| `Live` | `Long` | `0.0672` | 3,630,000.00 USD | 0.00 USD | 899.27 USD | `-10.78%` | `13,392.00` |
| `Live` | `Long` | `0.0673` | 3,630,000.00 USD | 0.00 USD | 33,870.00 USD | `-10.65%` | `503,650.00` |
| `Live` | `Long` | `0.0673` | 3,590,000.00 USD | 0.00 USD | 96,190.00 USD | `-10.52%` | `1,428,139.00` |
| `Live` | `Long` | `0.0674` | 3,500,000.00 USD | 0.00 USD | 3,300.00 USD | `-10.38%` | `48,918.00` |
| `Live` | `Long` | `0.0675` | 3,490,000.00 USD | 0.00 USD | 310.73 USD | `-10.25%` | `4,600.00` |
| `Live` | `Long` | `0.0677` | 3,490,000.00 USD | 0.00 USD | 8,210.00 USD | `-10.12%` | `121,370.00` |
| `Live` | `Long` | `0.0678` | 3,490,000.00 USD | 0.00 USD | 140,600.00 USD | `-9.99%` | `2,075,221.00` |
| `Live` | `Long` | `0.0678` | 3,350,000.00 USD | 0.00 USD | 55,180.00 USD | `-9.85%` | `813,258.00` |
| `Live` | `Long` | `0.0679` | 3,290,000.00 USD | 0.00 USD | 20,030.00 USD | `-9.72%` | `294,729.00` |
| `Live` | `Long` | `0.0680` | 3,270,000.00 USD | 0.00 USD | 212.72 USD | `-9.59%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,270,000.00 USD | 0.00 USD | 1,680.00 USD | `-9.45%` | `24,721.00` |
| `Live` | `Long` | `0.0683` | 3,270,000.00 USD | 0.00 USD | 55,650.00 USD | `-9.32%` | `815,403.00` |
| `Live` | `Long` | `0.0683` | 3,210,000.00 USD | 0.00 USD | 1,290.00 USD | `-9.19%` | `18,879.00` |
| `Live` | `Long` | `0.0684` | 3,210,000.00 USD | 0.00 USD | 6,000.00 USD | `-9.06%` | `87,593.00` |
| `Live` | `Long` | `0.0685` | 3,210,000.00 USD | 0.00 USD | 4,690.00 USD | `-8.92%` | `68,414.00` |
| `Live` | `Long` | `0.0687` | 3,200,000.00 USD | 0.00 USD | 595.81 USD | `-8.79%` | `8,679.00` |
| `Live` | `Long` | `0.0688` | 3,200,000.00 USD | 0.00 USD | 69,020.00 USD | `-8.66%` | `1,003,929.00` |
| `Live` | `Long` | `0.0688` | 3,130,000.00 USD | 0.00 USD | 1,170.00 USD | `-8.52%` | `17,063.00` |
| `Live` | `Long` | `0.0689` | 3,130,000.00 USD | 0.00 USD | 507,660.00 USD | `-8.39%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,620,000.00 USD | 0.00 USD | 3,670.00 USD | `-8.26%` | `53,108.00` |
| `Live` | `Long` | `0.0692` | 2,620,000.00 USD | 0.00 USD | 8,350.00 USD | `-8.13%` | `120,766.00` |
| `Live` | `Long` | `0.0693` | 2,610,000.00 USD | 0.00 USD | 2,160.00 USD | `-7.86%` | `31,211.00` |
| `Live` | `Long` | `0.0694` | 2,610,000.00 USD | 0.00 USD | 4,840.00 USD | `-7.73%` | `69,669.00` |
| `Live` | `Long` | `0.0696` | 2,600,000.00 USD | 0.00 USD | 14,930.00 USD | `-7.59%` | `214,659.00` |
| `Live` | `Long` | `0.0697` | 2,590,000.00 USD | 0.00 USD | 8,340.00 USD | `-7.46%` | `119,702.00` |
| `Live` | `Long` | `0.0698` | 2,580,000.00 USD | 0.00 USD | 3,420.00 USD | `-7.33%` | `49,047.00` |
| `Live` | `Long` | `0.0698` | 2,580,000.00 USD | 0.00 USD | 25,750.00 USD | `-7.20%` | `368,644.00` |
| `Live` | `Long` | `0.0699` | 2,550,000.00 USD | 0.00 USD | 1,310.00 USD | `-7.06%` | `18,718.00` |
| `Live` | `Long` | `0.0701` | 2,550,000.00 USD | 0.00 USD | 264.58 USD | `-6.93%` | `3,777.00` |
| `Live` | `Long` | `0.0702` | 2,550,000.00 USD | 0.00 USD | 1,590.00 USD | `-6.80%` | `22,683.00` |
| `Live` | `Long` | `0.0703` | 2,550,000.00 USD | 0.00 USD | 791.79 USD | `-6.66%` | `11,271.00` |
| `Live` | `Long` | `0.0703` | 2,550,000.00 USD | 0.00 USD | 5,060.00 USD | `-6.53%` | `71,876.00` |
| `Live` | `Long` | `0.0704` | 2,540,000.00 USD | 0.00 USD | 216.56 USD | `-6.40%` | `3,074.00` |
| `Live` | `Long` | `0.0707` | 2,540,000.00 USD | 0.00 USD | 94,410.00 USD | `-6.00%` | `1,334,448.00` |
| `Live` | `Long` | `0.0708` | 2,450,000.00 USD | 0.00 USD | 9,150.00 USD | `-5.87%` | `129,200.00` |
| `Live` | `Long` | `0.0711` | 2,440,000.00 USD | 0.00 USD | 8,840.00 USD | `-5.60%` | `124,379.00` |
| `Live` | `Long` | `0.0712` | 2,430,000.00 USD | 0.00 USD | 389.38 USD | `-5.34%` | `5,465.00` |
| `Live` | `Long` | `0.0713` | 2,430,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-5.20%` | `24,460,119.00` |
| `Live` | `Long` | `0.0714` | 683,410.00 USD | 0.00 USD | 2,370.00 USD | `-5.07%` | `33,195.00` |
| `Live` | `Long` | `0.0716` | 681,040.00 USD | 0.00 USD | 8,120.00 USD | `-4.94%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 672,930.00 USD | 0.00 USD | 1,150.00 USD | `-4.80%` | `16,036.00` |
| `Live` | `Long` | `0.0717` | 671,780.00 USD | 0.00 USD | 2,700.00 USD | `-4.67%` | `37,666.00` |
| `Live` | `Long` | `0.0718` | 669,080.00 USD | 0.00 USD | 960.13 USD | `-4.54%` | `13,363.00` |
| `Live` | `Long` | `0.0720` | 668,120.00 USD | 0.00 USD | 778.93 USD | `-4.41%` | `10,826.00` |
| `Live` | `Long` | `0.0721` | 667,340.00 USD | 0.00 USD | 24,050.00 USD | `-4.27%` | `333,835.00` |
| `Live` | `Long` | `0.0722` | 643,280.00 USD | 0.00 USD | 5,720.00 USD | `-4.01%` | `79,141.00` |
| `Live` | `Long` | `0.0723` | 637,570.00 USD | 0.00 USD | 10,980.00 USD | `-3.87%` | `151,780.00` |
| `Live` | `Long` | `0.0725` | 626,580.00 USD | 0.00 USD | 5,290.00 USD | `-3.74%` | `73,027.00` |
| `Live` | `Long` | `0.0726` | 621,290.00 USD | 0.00 USD | 260.74 USD | `-3.61%` | `3,594.00` |
| `Live` | `Long` | `0.0727` | 621,030.00 USD | 0.00 USD | 948.37 USD | `-3.48%` | `13,054.00` |
| `Live` | `Long` | `0.0727` | 620,080.00 USD | 0.00 USD | 452.21 USD | `-3.34%` | `6,216.00` |
| `Live` | `Long` | `0.0728` | 619,630.00 USD | 0.00 USD | 646.11 USD | `-3.21%` | `8,869.00` |
| `Live` | `Long` | `0.0730` | 618,990.00 USD | 0.00 USD | 72,950.00 USD | `-3.08%` | `1,000,000.00` |
| `Live` | `Long` | `0.0731` | 546,040.00 USD | 0.00 USD | 10,040.00 USD | `-2.94%` | `137,397.00` |
| `Live` | `Long` | `0.0732` | 536,000.00 USD | 0.00 USD | 1,930.00 USD | `-2.81%` | `26,339.00` |
| `Live` | `Long` | `0.0732` | 534,070.00 USD | 0.00 USD | 29,280.00 USD | `-2.68%` | `399,671.00` |
| `Live` | `Long` | `0.0735` | 504,800.00 USD | 0.00 USD | 3,930.00 USD | `-2.41%` | `53,459.00` |
| `Live` | `Long` | `0.0736` | 500,870.00 USD | 0.00 USD | 4,060.00 USD | `-2.28%` | `55,170.00` |
| `Live` | `Long` | `0.0736` | 496,810.00 USD | 0.00 USD | 5,490.00 USD | `-2.15%` | `74,588.00` |
| `Live` | `Long` | `0.0737` | 491,320.00 USD | 0.00 USD | 10,740.00 USD | `-2.01%` | `145,658.00` |
| `Live` | `Long` | `0.0738` | 480,580.00 USD | 0.00 USD | 1,740.00 USD | `-1.88%` | `23,523.00` |
| `Live` | `Long` | `0.0740` | 478,840.00 USD | 0.00 USD | 19,840.00 USD | `-1.75%` | `268,267.00` |
| `Live` | `Long` | `0.0741` | 459,000.00 USD | 0.00 USD | 455,080.00 USD | `-1.62%` | `6,145,600.00` |
| `Live` | `Long` | `0.0741` | 3,920.00 USD | 0.00 USD | 641.77 USD | `-1.48%` | `8,655.00` |
| `Live` | `Long` | `0.0742` | 3,280.00 USD | 0.00 USD | 1,280.00 USD | `-1.35%` | `17,202.00` |
| `Live` | `Long` | `0.0743` | 2,000.00 USD | 0.00 USD | 1,180.00 USD | `-1.22%` | `15,867.00` |
| `Live` | `Long` | `0.0745` | 821.27 USD | 0.00 USD | 176.30 USD | `-1.08%` | `2,368.00` |
| `Live` | `Long` | `0.0746` | 644.98 USD | 0.00 USD | 644.98 USD | `-0.82%` | `8,640.00` |
| `Live` | `Short` | `0.0760` | 10,740.00 USD | 10,740.00 USD | 0.00 USD | `+0.91%` | `141,386.00` |
| `Live` | `Short` | `0.0761` | 15,970.00 USD | 5,230.00 USD | 0.00 USD | `+1.17%` | `68,638.00` |
| `Live` | `Short` | `0.0784` | 16,160.00 USD | 192.04 USD | 0.00 USD | `+4.10%` | `2,451.00` |
| `Live` | `Short` | `0.0785` | 26,690.00 USD | 10,530.00 USD | 0.00 USD | `+4.23%` | `134,228.00` |
| `Live` | `Short` | `0.0791` | 26,840.00 USD | 150.07 USD | 0.00 USD | `+5.16%` | `1,896.00` |
| `Live` | `Short` | `0.0795` | 27,920.00 USD | 1,080.00 USD | 0.00 USD | `+5.56%` | `13,564.00` |
| `Live` | `Short` | `0.0798` | 33,240.00 USD | 5,330.00 USD | 0.00 USD | `+5.96%` | `66,784.00` |
| `Live` | `Short` | `0.0799` | 35,220.00 USD | 1,970.00 USD | 0.00 USD | `+6.22%` | `24,701.00` |
| `Live` | `Short` | `0.0800` | 38,660.00 USD | 3,450.00 USD | 0.00 USD | `+6.36%` | `43,037.00` |
| `Live` | `Short` | `0.0818` | 38,900.00 USD | 241.90 USD | 0.00 USD | `+8.61%` | `2,959.00` |
| `Live` | `Short` | `0.0824` | 39,440.00 USD | 532.64 USD | 0.00 USD | `+9.41%` | `6,468.00` |
| `Live` | `Short` | `0.0832` | 42,890.00 USD | 3,450.00 USD | 0.00 USD | `+10.47%` | `41,543.00` |
| `Live` | `Short` | `0.0837` | 43,180.00 USD | 293.44 USD | 0.00 USD | `+11.14%` | `3,508.00` |
| `Live` | `Short` | `0.0838` | 44,760.00 USD | 1,570.00 USD | 0.00 USD | `+11.27%` | `18,767.00` |
| `Live` | `Short` | `0.0843` | 44,860.00 USD | 104.72 USD | 0.00 USD | `+11.94%` | `1,243.00` |
| `Live` | `Short` | `0.0848` | 45,580.00 USD | 723.94 USD | 0.00 USD | `+12.73%` | `8,532.00` |
| `Live` | `Short` | `0.0858` | 45,700.00 USD | 115.30 USD | 0.00 USD | `+14.06%` | `1,343.00` |
| `Live` | `Short` | `0.0862` | 48,040.00 USD | 2,340.00 USD | 0.00 USD | `+14.59%` | `27,165.00` |
| `Live` | `Short` | `0.0881` | 48,510.00 USD | 465.17 USD | 0.00 USD | `+16.99%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 48,920.00 USD | 411.53 USD | 0.00 USD | `+17.92%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 49,340.00 USD | 418.80 USD | 0.00 USD | `+18.31%` | `4,703.00` |
| `Live` | `Short` | `0.0895` | 50,570.00 USD | 1,230.00 USD | 0.00 USD | `+18.85%` | `13,799.00` |
| `Live` | `Short` | `0.0911` | 51,310.00 USD | 743.15 USD | 0.00 USD | `+21.10%` | `8,153.00` |
| `Live` | `Short` | `0.0912` | 55,360.00 USD | 4,040.00 USD | 0.00 USD | `+21.24%` | `44,324.00` |
| `Live` | `Short` | `0.0914` | 55,530.00 USD | 171.19 USD | 0.00 USD | `+21.37%` | `1,874.00` |
| `Live` | `Short` | `0.0921` | 55,700.00 USD | 171.49 USD | 0.00 USD | `+22.30%` | `1,863.00` |
| `Live` | `Short` | `0.0950` | 69,500.00 USD | 13,800.00 USD | 0.00 USD | `+26.15%` | `145,305.00` |
| `Live` | `Short` | `0.0953` | 117,120.00 USD | 47,620.00 USD | 0.00 USD | `+26.55%` | `500,000.00` |
| `Live` | `Short` | `0.0954` | 118,050.00 USD | 928.33 USD | 0.00 USD | `+26.68%` | `9,736.00` |
| `Live` | `Short` | `0.0959` | 118,250.00 USD | 195.05 USD | 0.00 USD | `+27.35%` | `2,035.00` |
| `Live` | `Short` | `0.0961` | 118,860.00 USD | 609.59 USD | 0.00 USD | `+27.75%` | `6,340.00` |
| `Live` | `Short` | `0.0978` | 120,730.00 USD | 1,880.00 USD | 0.00 USD | `+29.87%` | `19,213.00` |
| `Live` | `Short` | `0.0979` | 159,930.00 USD | 39,190.00 USD | 0.00 USD | `+30.01%` | `400,522.00` |
| `Live` | `Short` | `0.0983` | 160,400.00 USD | 477.50 USD | 0.00 USD | `+30.54%` | `4,860.00` |
| `Live` | `Short` | `0.0984` | 164,830.00 USD | 4,430.00 USD | 0.00 USD | `+30.67%` | `45,000.00` |
| `Live` | `Short` | `0.0984` | 175,340.00 USD | 10,510.00 USD | 0.00 USD | `+30.80%` | `106,785.00` |
| `Live` | `Short` | `0.1014` | 182,970.00 USD | 7,630.00 USD | 0.00 USD | `+34.79%` | `75,169.00` |
| `Live` | `Short` | `0.1017` | 185,940.00 USD | 2,970.00 USD | 0.00 USD | `+35.05%` | `29,214.00` |
| `Live` | `Short` | `0.1018` | 186,430.00 USD | 492.85 USD | 0.00 USD | `+35.32%` | `4,839.00` |
| `Live` | `Short` | `0.1032` | 187,760.00 USD | 1,330.00 USD | 0.00 USD | `+37.18%` | `12,841.00` |
| `Live` | `Short` | `0.1048` | 190,220.00 USD | 2,460.00 USD | 0.00 USD | `+39.31%` | `23,466.00` |
| `Live` | `Short` | `0.1061` | 196,330.00 USD | 6,110.00 USD | 0.00 USD | `+41.03%` | `57,554.00` |
| `Live` | `Short` | `0.1070` | 200,470.00 USD | 4,150.00 USD | 0.00 USD | `+42.10%` | `38,791.00` |
| `Live` | `Short` | `0.1085` | 203,710.00 USD | 3,240.00 USD | 0.00 USD | `+44.22%` | `29,849.00` |
| `Live` | `Short` | `0.1120` | 205,580.00 USD | 1,870.00 USD | 0.00 USD | `+48.87%` | `16,647.00` |
| `Live` | `Short` | `0.1127` | 205,790.00 USD | 214.15 USD | 0.00 USD | `+49.67%` | `1,901.00` |
| `Live` | `Short` | `0.1129` | 205,940.00 USD | 142.88 USD | 0.00 USD | `+50.07%` | `1,265.00` |
| `Live` | `Short` | `0.1132` | 209,330.00 USD | 3,390.00 USD | 0.00 USD | `+50.33%` | `29,960.00` |
| `Live` | `Short` | `0.1139` | 212,860.00 USD | 3,530.00 USD | 0.00 USD | `+51.26%` | `31,000.00` |
| `Live` | `Short` | `0.1187` | 212,960.00 USD | 106.19 USD | 0.00 USD | `+57.64%` | `895.00` |
| `Live` | `Short` | `0.1222` | 213,760.00 USD | 796.83 USD | 0.00 USD | `+62.42%` | `6,518.00` |
| `Live` | `Short` | `0.1237` | 214,650.00 USD | 893.35 USD | 0.00 USD | `+64.42%` | `7,219.00` |
| `Live` | `Short` | `0.1270` | 214,760.00 USD | 108.80 USD | 0.00 USD | `+68.67%` | `857.00` |
| `Live` | `Short` | `0.1296` | 214,930.00 USD | 171.66 USD | 0.00 USD | `+72.26%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 218,280.00 USD | 3,340.00 USD | 0.00 USD | `+74.25%` | `25,486.00` |
| `Live` | `Short` | `0.1318` | 218,380.00 USD | 102.97 USD | 0.00 USD | `+75.18%` | `781.00` |
| `Live` | `Short` | `0.1338` | 218,580.00 USD | 205.31 USD | 0.00 USD | `+77.70%` | `1,535.00` |
| `Live` | `Short` | `0.1353` | 253,530.00 USD | 34,940.00 USD | 0.00 USD | `+79.70%` | `258,360.00` |
| `Live` | `Short` | `0.1373` | 275,790.00 USD | 22,260.00 USD | 0.00 USD | `+82.35%` | `162,180.00` |
| `Live` | `Short` | `0.1376` | 277,850.00 USD | 2,060.00 USD | 0.00 USD | `+82.75%` | `15,003.00` |
| `Live` | `Short` | `0.1388` | 278,270.00 USD | 416.25 USD | 0.00 USD | `+84.35%` | `3,000.00` |
| `Live` | `Short` | `0.1404` | 278,930.00 USD | 663.63 USD | 0.00 USD | `+86.60%` | `4,725.00` |
| `Live` | `Short` | `0.1411` | 280,730.00 USD | 1,800.00 USD | 0.00 USD | `+87.53%` | `12,780.00` |
| `Live` | `Short` | `0.1432` | 282,600.00 USD | 1,860.00 USD | 0.00 USD | `+90.32%` | `13,010.00` |
| `Live` | `Short` | `0.1444` | 284,140.00 USD | 1,540.00 USD | 0.00 USD | `+91.79%` | `10,691.00` |
| `Live` | `Short` | `0.1479` | 292,440.00 USD | 8,300.00 USD | 0.00 USD | `+96.44%` | `56,144.00` |
| `Live` | `Short` | `0.1497` | 294,420.00 USD | 1,980.00 USD | 0.00 USD | `+98.96%` | `13,240.00` |
| `Live` | `Short` | `0.1502` | 3,440,000.00 USD | 3,140,000.00 USD | 0.00 USD | `+99.63%` | `20,910,149.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 460,870.00 USD | 0.00 USD | 375.42 USD | `-65.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 460,500.00 USD | 0.00 USD | 409.59 USD | `-46.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 460,090.00 USD | 0.00 USD | 132.68 USD | `-45.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0416` | 459,960.00 USD | 0.00 USD | 788.27 USD | `-44.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0418` | 459,170.00 USD | 0.00 USD | 527.05 USD | `-44.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 458,640.00 USD | 0.00 USD | 286.87 USD | `-40.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 458,350.00 USD | 0.00 USD | 252.42 USD | `-38.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 458,100.00 USD | 0.00 USD | 468.67 USD | `-37.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 457,630.00 USD | 0.00 USD | 5,160.00 USD | `-34.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 452,470.00 USD | 0.00 USD | 920.48 USD | `-34.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 451,550.00 USD | 0.00 USD | 1,730.00 USD | `-33.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 449,820.00 USD | 0.00 USD | 175.41 USD | `-31.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0541` | 449,650.00 USD | 0.00 USD | 2,670.00 USD | `-28.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 446,970.00 USD | 0.00 USD | 1,370.00 USD | `-26.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 445,600.00 USD | 0.00 USD | 437.58 USD | `-25.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 445,160.00 USD | 0.00 USD | 752.54 USD | `-22.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 444,410.00 USD | 0.00 USD | 9,830.00 USD | `-21.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 434,580.00 USD | 0.00 USD | 984.67 USD | `-21.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 433,590.00 USD | 0.00 USD | 668.84 USD | `-20.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 432,920.00 USD | 0.00 USD | 134.12 USD | `-19.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 432,790.00 USD | 0.00 USD | 8,800.00 USD | `-19.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 423,990.00 USD | 0.00 USD | 504.26 USD | `-17.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 423,490.00 USD | 0.00 USD | 2,280.00 USD | `-17.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 421,210.00 USD | 0.00 USD | 1,280.00 USD | `-17.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 419,930.00 USD | 0.00 USD | 920.18 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 419,010.00 USD | 0.00 USD | 370.79 USD | `-14.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 418,640.00 USD | 0.00 USD | 1,130.00 USD | `-13.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 417,510.00 USD | 0.00 USD | 362.24 USD | `-13.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 417,150.00 USD | 0.00 USD | 3,140.00 USD | `-12.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0658` | 414,010.00 USD | 0.00 USD | 1,100.00 USD | `-12.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 412,910.00 USD | 0.00 USD | 1,200.00 USD | `-12.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 411,710.00 USD | 0.00 USD | 996.31 USD | `-12.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 410,720.00 USD | 0.00 USD | 632.88 USD | `-11.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 410,080.00 USD | 0.00 USD | 115.57 USD | `-10.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 409,970.00 USD | 0.00 USD | 33,620.00 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 376,340.00 USD | 0.00 USD | 12,860.00 USD | `-10.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 363,480.00 USD | 0.00 USD | 1,260.00 USD | `-10.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 362,220.00 USD | 0.00 USD | 108.08 USD | `-10.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 362,110.00 USD | 0.00 USD | 2,960.00 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 359,150.00 USD | 0.00 USD | 1,430.00 USD | `-9.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 357,720.00 USD | 0.00 USD | 7,990.00 USD | `-9.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 349,730.00 USD | 0.00 USD | 8,580.00 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 341,150.00 USD | 0.00 USD | 606.47 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 340,550.00 USD | 0.00 USD | 38,710.00 USD | `-8.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 301,840.00 USD | 0.00 USD | 660.06 USD | `-8.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 301,180.00 USD | 0.00 USD | 102.34 USD | `-8.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0693` | 301,080.00 USD | 0.00 USD | 218.87 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0694` | 300,860.00 USD | 0.00 USD | 144.59 USD | `-7.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0696` | 300,720.00 USD | 0.00 USD | 925.29 USD | `-7.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 299,790.00 USD | 0.00 USD | 697.50 USD | `-7.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 299,090.00 USD | 0.00 USD | 16,840.00 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 282,250.00 USD | 0.00 USD | 1,800.00 USD | `-6.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 280,450.00 USD | 0.00 USD | 523.23 USD | `-6.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 279,930.00 USD | 0.00 USD | 235.12 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 279,690.00 USD | 0.00 USD | 204.40 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 279,490.00 USD | 0.00 USD | 107,570.00 USD | `-5.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 171,920.00 USD | 0.00 USD | 12,930.00 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 158,990.00 USD | 0.00 USD | 20,070.00 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 138,920.00 USD | 0.00 USD | 608.76 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 138,310.00 USD | 0.00 USD | 16,880.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 121,430.00 USD | 0.00 USD | 1,670.00 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 119,760.00 USD | 0.00 USD | 4,710.00 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 115,050.00 USD | 0.00 USD | 8,570.00 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 106,480.00 USD | 0.00 USD | 413.42 USD | `-4.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 106,070.00 USD | 0.00 USD | 881.82 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 105,190.00 USD | 0.00 USD | 1,330.00 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 103,850.00 USD | 0.00 USD | 621.12 USD | `-3.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 103,230.00 USD | 0.00 USD | 1,430.00 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 101,800.00 USD | 0.00 USD | 29,060.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 72,730.00 USD | 0.00 USD | 1,610.00 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 71,120.00 USD | 0.00 USD | 2,090.00 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 69,030.00 USD | 0.00 USD | 23,870.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 45,160.00 USD | 0.00 USD | 28,640.00 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 16,520.00 USD | 0.00 USD | 2,910.00 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 13,610.00 USD | 0.00 USD | 115.12 USD | `-2.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 13,500.00 USD | 0.00 USD | 4,680.00 USD | `-1.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 8,820.00 USD | 0.00 USD | 1,220.00 USD | `-1.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 7,600.00 USD | 0.00 USD | 2,900.00 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 4,710.00 USD | 0.00 USD | 107.66 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 4,600.00 USD | 0.00 USD | 744.50 USD | `-1.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 3,850.00 USD | 0.00 USD | 1,410.00 USD | `-0.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 2,440.00 USD | 0.00 USD | 375.86 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 2,070.00 USD | 0.00 USD | 193.90 USD | `-0.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 1,870.00 USD | 0.00 USD | 140.04 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 1,730.00 USD | 0.00 USD | 397.83 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 1,330.00 USD | 0.00 USD | 199.48 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 1,130.00 USD | 0.00 USD | 736.17 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0752` | 398.60 USD | 0.00 USD | 398.60 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 192.73 USD | 192.73 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0756` | 550.86 USD | 358.13 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0757` | 5,430.00 USD | 4,880.00 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0759` | 5,630.00 USD | 193.49 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0760` | 7,900.00 USD | 2,280.00 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 11,040.00 USD | 3,130.00 USD | 0.00 USD | `+1.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0761` | 11,840.00 USD | 806.81 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0762` | 12,200.00 USD | 359.60 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0764` | 12,540.00 USD | 335.56 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0765` | 13,800.00 USD | 1,260.00 USD | 0.00 USD | `+1.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 14,010.00 USD | 203.47 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0766` | 17,550.00 USD | 3,540.00 USD | 0.00 USD | `+1.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0767` | 17,740.00 USD | 192.95 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0769` | 18,040.00 USD | 297.49 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 18,850.00 USD | 816.05 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0770` | 34,250.00 USD | 15,400.00 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0771` | 38,230.00 USD | 3,980.00 USD | 0.00 USD | `+2.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0772` | 42,130.00 USD | 3,900.00 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0774` | 45,950.00 USD | 3,820.00 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 46,170.00 USD | 215.00 USD | 0.00 USD | `+2.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0775` | 46,770.00 USD | 604.81 USD | 0.00 USD | `+3.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0776` | 48,260.00 USD | 1,490.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0777` | 90,070.00 USD | 41,810.00 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0779` | 131,510.00 USD | 41,440.00 USD | 0.00 USD | `+3.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 134,520.00 USD | 3,000.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0780` | 136,520.00 USD | 2,010.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0781` | 137,870.00 USD | 1,350.00 USD | 0.00 USD | `+3.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0783` | 138,090.00 USD | 222.46 USD | 0.00 USD | `+3.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0784` | 142,460.00 USD | 4,370.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 143,030.00 USD | 573.31 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0785` | 158,820.00 USD | 15,790.00 USD | 0.00 USD | `+4.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0786` | 159,320.00 USD | 495.57 USD | 0.00 USD | `+4.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0788` | 162,350.00 USD | 3,030.00 USD | 0.00 USD | `+4.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0789` | 162,650.00 USD | 303.73 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 164,220.00 USD | 1,560.00 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0790` | 166,580.00 USD | 2,360.00 USD | 0.00 USD | `+5.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0791` | 171,170.00 USD | 4,600.00 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0793` | 173,430.00 USD | 2,260.00 USD | 0.00 USD | `+5.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0794` | 174,440.00 USD | 1,010.00 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 174,590.00 USD | 148.25 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0795` | 175,150.00 USD | 556.77 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 175,280.00 USD | 125.45 USD | 0.00 USD | `+5.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 175,510.00 USD | 230.40 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 175,820.00 USD | 319.16 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 176,940.00 USD | 1,120.00 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 199,480.00 USD | 22,540.00 USD | 0.00 USD | `+6.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 199,880.00 USD | 400.91 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 200,080.00 USD | 200.46 USD | 0.00 USD | `+6.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 200,340.00 USD | 259.13 USD | 0.00 USD | `+6.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 201,050.00 USD | 707.08 USD | 0.00 USD | `+6.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 203,310.00 USD | 2,260.00 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 300,090.00 USD | 96,780.00 USD | 0.00 USD | `+7.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 300,900.00 USD | 807.50 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 301,160.00 USD | 257.18 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 301,580.00 USD | 424.74 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 301,680.00 USD | 101.80 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 303,070.00 USD | 1,380.00 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 303,330.00 USD | 264.63 USD | 0.00 USD | `+7.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 304,770.00 USD | 1,430.00 USD | 0.00 USD | `+8.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 305,260.00 USD | 492.77 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 306,280.00 USD | 1,020.00 USD | 0.00 USD | `+8.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 308,840.00 USD | 2,560.00 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 309,860.00 USD | 1,030.00 USD | 0.00 USD | `+8.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 312,470.00 USD | 2,610.00 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 312,800.00 USD | 327.80 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 313,410.00 USD | 607.58 USD | 0.00 USD | `+9.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 320,290.00 USD | 6,880.00 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 321,090.00 USD | 800.79 USD | 0.00 USD | `+9.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 321,610.00 USD | 512.05 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 321,850.00 USD | 240.26 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 322,240.00 USD | 389.31 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 322,940.00 USD | 706.02 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 323,250.00 USD | 303.56 USD | 0.00 USD | `+10.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 323,360.00 USD | 112.89 USD | 0.00 USD | `+10.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 323,740.00 USD | 381.45 USD | 0.00 USD | `+10.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 323,900.00 USD | 155.82 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 325,330.00 USD | 1,430.00 USD | 0.00 USD | `+10.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 325,470.00 USD | 138.69 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 326,730.00 USD | 1,260.00 USD | 0.00 USD | `+10.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 326,940.00 USD | 210.88 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,080,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 2,080,000.00 USD | 3,150.00 USD | 0.00 USD | `+11.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 2,080,000.00 USD | 341.34 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 2,080,000.00 USD | 107.71 USD | 0.00 USD | `+11.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 2,080,000.00 USD | 2,690.00 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 2,090,000.00 USD | 1,330.00 USD | 0.00 USD | `+12.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 2,090,000.00 USD | 219.07 USD | 0.00 USD | `+12.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,090,000.00 USD | 326.97 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 2,090,000.00 USD | 242.84 USD | 0.00 USD | `+12.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 2,100,000.00 USD | 10,140.00 USD | 0.00 USD | `+12.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0851` | 2,100,000.00 USD | 152.92 USD | 0.00 USD | `+13.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 2,100,000.00 USD | 876.11 USD | 0.00 USD | `+13.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 2,100,000.00 USD | 205.59 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 2,100,000.00 USD | 126.76 USD | 0.00 USD | `+13.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,100,000.00 USD | 307.41 USD | 0.00 USD | `+13.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 2,100,000.00 USD | 614.09 USD | 0.00 USD | `+14.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 2,100,000.00 USD | 644.62 USD | 0.00 USD | `+14.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0861` | 2,100,000.00 USD | 180.45 USD | 0.00 USD | `+14.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,100,000.00 USD | 2,020.00 USD | 0.00 USD | `+14.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 2,150,000.00 USD | 43,760.00 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 2,150,000.00 USD | 1,080.00 USD | 0.00 USD | `+14.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 2,150,000.00 USD | 384.06 USD | 0.00 USD | `+15.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 2,150,000.00 USD | 1,840.00 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0876` | 2,150,000.00 USD | 2,760.00 USD | 0.00 USD | `+16.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 2,150,000.00 USD | 117.71 USD | 0.00 USD | `+16.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 2,150,000.00 USD | 111.61 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 2,150,000.00 USD | 571.18 USD | 0.00 USD | `+16.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 2,150,000.00 USD | 375.94 USD | 0.00 USD | `+17.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 2,150,000.00 USD | 627.55 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 2,150,000.00 USD | 211.04 USD | 0.00 USD | `+17.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 2,150,000.00 USD | 108.36 USD | 0.00 USD | `+17.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 2,150,000.00 USD | 543.32 USD | 0.00 USD | `+18.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 2,160,000.00 USD | 1,820.00 USD | 0.00 USD | `+18.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 2,160,000.00 USD | 2,080.00 USD | 0.00 USD | `+18.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,180,000.00 USD | 17,680.00 USD | 0.00 USD | `+18.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,180,000.00 USD | 1,640.00 USD | 0.00 USD | `+18.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0896` | 2,180,000.00 USD | 1,640.00 USD | 0.00 USD | `+18.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,180,000.00 USD | 5,010.00 USD | 0.00 USD | `+19.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,190,000.00 USD | 1,090.00 USD | 0.00 USD | `+19.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,190,000.00 USD | 224.86 USD | 0.00 USD | `+20.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,210,000.00 USD | 20,540.00 USD | 0.00 USD | `+20.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,210,000.00 USD | 114.93 USD | 0.00 USD | `+20.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,210,000.00 USD | 679.12 USD | 0.00 USD | `+20.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,210,000.00 USD | 173.36 USD | 0.00 USD | `+20.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,210,000.00 USD | 1,810.00 USD | 0.00 USD | `+21.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,210,000.00 USD | 1,530.00 USD | 0.00 USD | `+21.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,210,000.00 USD | 2,170.00 USD | 0.00 USD | `+22.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,210,000.00 USD | 541.32 USD | 0.00 USD | `+22.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,350,000.00 USD | 137,500.00 USD | 0.00 USD | `+22.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,350,000.00 USD | 691.07 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,360,000.00 USD | 6,250.00 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,370,000.00 USD | 13,480.00 USD | 0.00 USD | `+23.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,370,000.00 USD | 734.82 USD | 0.00 USD | `+23.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,370,000.00 USD | 1,230.00 USD | 0.00 USD | `+23.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,370,000.00 USD | 184.09 USD | 0.00 USD | `+24.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,370,000.00 USD | 1,120.00 USD | 0.00 USD | `+24.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,380,000.00 USD | 1,860.00 USD | 0.00 USD | `+24.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,380,000.00 USD | 512.15 USD | 0.00 USD | `+25.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,380,000.00 USD | 6,620.00 USD | 0.00 USD | `+25.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,380,000.00 USD | 404.96 USD | 0.00 USD | `+25.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,380,000.00 USD | 129.85 USD | 0.00 USD | `+26.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,390,000.00 USD | 3,740.00 USD | 0.00 USD | `+27.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0959` | 2,390,000.00 USD | 2,400.00 USD | 0.00 USD | `+27.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,390,000.00 USD | 409.17 USD | 0.00 USD | `+27.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,390,000.00 USD | 203.74 USD | 0.00 USD | `+28.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,390,000.00 USD | 2,800.00 USD | 0.00 USD | `+29.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,390,000.00 USD | 1,320.00 USD | 0.00 USD | `+29.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,400,000.00 USD | 694.56 USD | 0.00 USD | `+29.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,400,000.00 USD | 940.91 USD | 0.00 USD | `+30.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,400,000.00 USD | 2,980.00 USD | 0.00 USD | `+31.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,400,000.00 USD | 104.99 USD | 0.00 USD | `+31.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,400,000.00 USD | 1,930.00 USD | 0.00 USD | `+31.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,400,000.00 USD | 1,490.00 USD | 0.00 USD | `+32.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,400,000.00 USD | 1,090.00 USD | 0.00 USD | `+32.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,400,000.00 USD | 438.96 USD | 0.00 USD | `+32.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,410,000.00 USD | 973.76 USD | 0.00 USD | `+32.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,520,000.00 USD | 111,100.00 USD | 0.00 USD | `+32.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,520,000.00 USD | 175.59 USD | 0.00 USD | `+32.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,520,000.00 USD | 482.89 USD | 0.00 USD | `+33.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,520,000.00 USD | 201.90 USD | 0.00 USD | `+34.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,520,000.00 USD | 489.46 USD | 0.00 USD | `+34.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,520,000.00 USD | 103.68 USD | 0.00 USD | `+34.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,520,000.00 USD | 203.70 USD | 0.00 USD | `+35.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,520,000.00 USD | 3,810.00 USD | 0.00 USD | `+35.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,530,000.00 USD | 11,200.00 USD | 0.00 USD | `+35.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,540,000.00 USD | 4,330.00 USD | 0.00 USD | `+35.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,540,000.00 USD | 205.50 USD | 0.00 USD | `+36.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,540,000.00 USD | 3,490.00 USD | 0.00 USD | `+36.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1031` | 2,540,000.00 USD | 1,300.00 USD | 0.00 USD | `+36.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,540,000.00 USD | 207.50 USD | 0.00 USD | `+37.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,540,000.00 USD | 813.88 USD | 0.00 USD | `+38.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,570,000.00 USD | 23,160.00 USD | 0.00 USD | `+38.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,570,000.00 USD | 781.51 USD | 0.00 USD | `+38.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,570,000.00 USD | 209.30 USD | 0.00 USD | `+39.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,570,000.00 USD | 1,440.00 USD | 0.00 USD | `+39.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,570,000.00 USD | 5,140.00 USD | 0.00 USD | `+39.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,570,000.00 USD | 585.32 USD | 0.00 USD | `+39.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,570,000.00 USD | 210.90 USD | 0.00 USD | `+40.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,580,000.00 USD | 1,850.00 USD | 0.00 USD | `+40.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,580,000.00 USD | 105.75 USD | 0.00 USD | `+40.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,580,000.00 USD | 3,220.00 USD | 0.00 USD | `+40.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,580,000.00 USD | 1,600.00 USD | 0.00 USD | `+41.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,580,000.00 USD | 212.90 USD | 0.00 USD | `+41.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,580,000.00 USD | 472.63 USD | 0.00 USD | `+42.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,580,000.00 USD | 214.50 USD | 0.00 USD | `+42.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,580,000.00 USD | 1,040.00 USD | 0.00 USD | `+43.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,580,000.00 USD | 136.12 USD | 0.00 USD | `+43.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,580,000.00 USD | 216.10 USD | 0.00 USD | `+43.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,620,000.00 USD | 40,920.00 USD | 0.00 USD | `+44.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,630,000.00 USD | 217.90 USD | 0.00 USD | `+44.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,630,000.00 USD | 219.70 USD | 0.00 USD | `+45.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,630,000.00 USD | 7,920.00 USD | 0.00 USD | `+46.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,630,000.00 USD | 154.22 USD | 0.00 USD | `+46.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,630,000.00 USD | 221.30 USD | 0.00 USD | `+47.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,630,000.00 USD | 1,050.00 USD | 0.00 USD | `+47.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,660,000.00 USD | 24,440.00 USD | 0.00 USD | `+47.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,660,000.00 USD | 223.10 USD | 0.00 USD | `+48.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,660,000.00 USD | 2,120.00 USD | 0.00 USD | `+49.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,660,000.00 USD | 226.30 USD | 0.00 USD | `+50.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,660,000.00 USD | 351.57 USD | 0.00 USD | `+51.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,660,000.00 USD | 950.34 USD | 0.00 USD | `+51.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,660,000.00 USD | 229.50 USD | 0.00 USD | `+52.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,660,000.00 USD | 771.08 USD | 0.00 USD | `+52.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,660,000.00 USD | 230.90 USD | 0.00 USD | `+53.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,660,000.00 USD | 288.18 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,670,000.00 USD | 619.10 USD | 0.00 USD | `+53.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,670,000.00 USD | 1,250.00 USD | 0.00 USD | `+54.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,670,000.00 USD | 1,050.00 USD | 0.00 USD | `+54.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,670,000.00 USD | 232.30 USD | 0.00 USD | `+54.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,670,000.00 USD | 1,600.00 USD | 0.00 USD | `+55.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,670,000.00 USD | 1,050.00 USD | 0.00 USD | `+55.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,670,000.00 USD | 3,730.00 USD | 0.00 USD | `+55.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,670,000.00 USD | 676.22 USD | 0.00 USD | `+56.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,680,000.00 USD | 648.25 USD | 0.00 USD | `+56.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,680,000.00 USD | 1,510.00 USD | 0.00 USD | `+56.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,680,000.00 USD | 448.52 USD | 0.00 USD | `+57.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1186` | 2,680,000.00 USD | 136.93 USD | 0.00 USD | `+57.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,680,000.00 USD | 124.58 USD | 0.00 USD | `+57.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,680,000.00 USD | 1,050.00 USD | 0.00 USD | `+58.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,680,000.00 USD | 691.80 USD | 0.00 USD | `+59.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,800,000.00 USD | 117,860.00 USD | 0.00 USD | `+59.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,800,000.00 USD | 143.22 USD | 0.00 USD | `+59.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1207` | 2,800,000.00 USD | 803.95 USD | 0.00 USD | `+60.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,800,000.00 USD | 1,380.00 USD | 0.00 USD | `+60.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,800,000.00 USD | 2,270.00 USD | 0.00 USD | `+62.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,800,000.00 USD | 871.99 USD | 0.00 USD | `+62.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,830,000.00 USD | 24,560.00 USD | 0.00 USD | `+68.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,830,000.00 USD | 400.21 USD | 0.00 USD | `+68.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,840,000.00 USD | 13,850.00 USD | 0.00 USD | `+75.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,840,000.00 USD | 2,360.00 USD | 0.00 USD | `+75.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,850,000.00 USD | 4,160.00 USD | 0.00 USD | `+80.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,850,000.00 USD | 235.54 USD | 0.00 USD | `+85.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,850,000.00 USD | 1,160.00 USD | 0.00 USD | `+87.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,850,000.00 USD | 173.57 USD | 0.00 USD | `+88.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,850,000.00 USD | 380.09 USD | 0.00 USD | `+89.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,870,000.00 USD | 17,150.00 USD | 0.00 USD | `+89.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,870,000.00 USD | 433.35 USD | 0.00 USD | `+91.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,870,000.00 USD | 3,640.00 USD | 0.00 USD | `+95.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,930,000.00 USD | 55,720.00 USD | 0.00 USD | `+96.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,930,000.00 USD | 2,120.00 USD | 0.00 USD | `+96.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,950,000.00 USD | 18,810.00 USD | 0.00 USD | `+99.23%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.0674` | 11,830,000.00 USD | 0.00 USD | 11,830,000.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0676` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 45,230.00 USD | 30,260.00 USD | 0.00 USD |
| `1D` | `0.0678` | 11,750,000.00 USD | 0.00 USD | 11,750,000.00 USD | 3,200.00 USD | 39,890.00 USD | 58,170.00 USD |
| `1D` | `0.0680` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD |
| `1D` | `0.0682` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 2,550.00 USD | 33,950.00 USD | 134,240.00 USD |
| `1D` | `0.0684` | 11,440,000.00 USD | 0.00 USD | 11,440,000.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD |
| `1D` | `0.0688` | 11,440,000.00 USD | 0.00 USD | 11,440,000.00 USD | 0.00 USD | 0.00 USD | 28,060.00 USD |
| `1D` | `0.0692` | 11,410,000.00 USD | 0.00 USD | 11,410,000.00 USD | 1,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0696` | 11,410,000.00 USD | 0.00 USD | 11,410,000.00 USD | 2,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `1D` | `0.0698` | 11,410,000.00 USD | 0.00 USD | 11,410,000.00 USD | 39,980.00 USD | 38,520.00 USD | 36,010.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `1D` | `0.0700` | 11,290,000.00 USD | 0.00 USD | 11,290,000.00 USD | 142,320.00 USD | 78,270.00 USD | 57,790.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `1D` | `0.0702` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 114,140.00 USD | 54,820.00 USD | 27,690.00 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `1D` | `0.0704` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 132,460.00 USD | 55,620.00 USD | 61,970.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0706` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 71,470.00 USD | 54,000.00 USD | 59,120.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0708` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 79,650.00 USD | 38,000.00 USD | 49,380.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `1D` | `0.0710` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 32,660.00 USD | 46,420.00 USD | 48,880.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0712` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 79,710.00 USD | 21,060.00 USD | 45,140.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0714` | 9,940,000.00 USD | 0.00 USD | 9,940,000.00 USD | 77,730.00 USD | 100,220.00 USD | 71,010.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0716` | 9,700,000.00 USD | 0.00 USD | 9,700,000.00 USD | 55,590.00 USD | 40,440.00 USD | 38,710.00 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0718` | 9,560,000.00 USD | 0.00 USD | 9,560,000.00 USD | 83,040.00 USD | 44,590.00 USD | 54,340.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0720` | 9,380,000.00 USD | 0.00 USD | 9,380,000.00 USD | 77,220.00 USD | 32,390.00 USD | 42,780.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0722` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 174,670.00 USD | 97,110.00 USD | 34,100.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0724` | 8,920,000.00 USD | 0.00 USD | 8,920,000.00 USD | 64,810.00 USD | 253,560.00 USD | 245,320.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0726` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 88,190.00 USD | 22,980.00 USD | 23,840.00 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0728` | 8,220,000.00 USD | 0.00 USD | 8,220,000.00 USD | 223,190.00 USD | 85,670.00 USD | 387,260.00 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0730` | 7,530,000.00 USD | 0.00 USD | 7,530,000.00 USD | 39,900.00 USD | 8,400.00 USD | 18,940.00 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0732` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 90,450.00 USD | 0.00 USD | 100.25 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0734` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 23,950.00 USD | 0.00 USD | 70,160.00 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0736` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 262,120.00 USD | 151,300.00 USD | 299.76 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0738` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 83,700.00 USD | 199,460.00 USD | 285,000.00 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0740` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 67,420.00 USD | 161,430.00 USD | 78,750.00 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0742` | 5,980,000.00 USD | 0.00 USD | 5,980,000.00 USD | 323,330.00 USD | 0.00 USD | 666,950.00 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0744` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 138,520.00 USD | 274,150.00 USD | 183,260.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0746` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 232,670.00 USD | 232,630.00 USD | 150,360.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0748` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 391,880.00 USD | 181,940.00 USD | 161,700.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0750` | 3,050,000.00 USD | 0.00 USD | 3,050,000.00 USD | 203,330.00 USD | 0.00 USD | 269,050.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0760` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 883.41 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0762` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 604,660.00 USD | 706,100.00 USD | 590.17 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0764` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 756,300.00 USD | 505,620.00 USD | 0.00 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0766` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 1,320,000.00 USD | 690,020.00 USD | 912.09 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0768` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 609,920.00 USD | 633,440.00 USD | 521,110.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0770` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 480,320.00 USD | 448,120.00 USD | 402,900.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0772` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 502,750.00 USD | 241,160.00 USD | 878,520.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0774` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 65,160.00 USD | 186,530.00 USD | 102,410.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0776` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 7,430.00 USD | 12,000.00 USD | 355.85 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0778` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 16,790.00 USD | 347,140.00 USD | 213,010.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0780` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 0.00 USD | 117,930.00 USD | 141,980.00 USD |
| `1D` | `0.0782` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 118,220.00 USD | 61,820.00 USD | 0.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0784` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 273,810.00 USD | 186,580.00 USD | 184,660.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0786` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 356,780.00 USD | 227,550.00 USD | 298,550.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0788` | 10,900,000.00 USD | 10,900,000.00 USD | 0.00 USD | 374,310.00 USD | 488,720.00 USD | 386,640.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0790` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 245,210.00 USD | 121,550.00 USD | 82,210.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0792` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 48,420.00 USD | 45,770.00 USD | 52,050.00 USD |
| `1D` | `0.0794` | 11,570,000.00 USD | 11,570,000.00 USD | 0.00 USD | 75,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0796` | 11,810,000.00 USD | 11,810,000.00 USD | 0.00 USD | 149,220.00 USD | 0.00 USD | 88,390.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0798` | 12,520,000.00 USD | 12,520,000.00 USD | 0.00 USD | 220,340.00 USD | 250,960.00 USD | 241,210.00 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0800` | 13,140,000.00 USD | 13,140,000.00 USD | 0.00 USD | 178,150.00 USD | 156,700.00 USD | 290,300.00 USD |
| `1D` | `0.0802` | 13,150,000.00 USD | 13,150,000.00 USD | 0.00 USD | 7,730.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `0.0804` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 11,880.00 USD | 10,910.00 USD | 38,610.00 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0806` | 13,610,000.00 USD | 13,610,000.00 USD | 0.00 USD | 84,020.00 USD | 58,270.00 USD | 256,410.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0808` | 15,150,000.00 USD | 15,150,000.00 USD | 0.00 USD | 634,220.00 USD | 339,110.00 USD | 564,550.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0810` | 16,580,000.00 USD | 16,580,000.00 USD | 0.00 USD | 771,010.00 USD | 517,160.00 USD | 144,580.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0812` | 17,260,000.00 USD | 17,260,000.00 USD | 0.00 USD | 202,360.00 USD | 340,900.00 USD | 135,390.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0814` | 17,960,000.00 USD | 17,960,000.00 USD | 0.00 USD | 74,410.00 USD | 108,600.00 USD | 515,840.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0816` | 19,320,000.00 USD | 19,320,000.00 USD | 0.00 USD | 675,530.00 USD | 335,640.00 USD | 348,800.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0818` | 20,690,000.00 USD | 20,690,000.00 USD | 0.00 USD | 613,810.00 USD | 315,240.00 USD | 438,420.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0820` | 22,000,000.00 USD | 22,000,000.00 USD | 0.00 USD | 310,650.00 USD | 532,960.00 USD | 472,910.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0822` | 23,050,000.00 USD | 23,050,000.00 USD | 0.00 USD | 472,760.00 USD | 248,830.00 USD | 327,420.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0824` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 422,760.00 USD | 301,930.00 USD | 207,110.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0826` | 24,690,000.00 USD | 24,690,000.00 USD | 0.00 USD | 278,370.00 USD | 206,840.00 USD | 217,880.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0828` | 25,160,000.00 USD | 25,160,000.00 USD | 0.00 USD | 278,450.00 USD | 124,170.00 USD | 66,080.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0830` | 25,940,000.00 USD | 25,940,000.00 USD | 0.00 USD | 396,370.00 USD | 209,720.00 USD | 178,180.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0832` | 26,490,000.00 USD | 26,490,000.00 USD | 0.00 USD | 320,350.00 USD | 100,300.00 USD | 128,700.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0834` | 27,210,000.00 USD | 27,210,000.00 USD | 0.00 USD | 275,130.00 USD | 162,910.00 USD | 282,900.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0836` | 27,770,000.00 USD | 27,770,000.00 USD | 0.00 USD | 132,320.00 USD | 216,570.00 USD | 208,200.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0838` | 28,150,000.00 USD | 28,150,000.00 USD | 0.00 USD | 238,020.00 USD | 86,330.00 USD | 59,580.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0840` | 28,290,000.00 USD | 28,290,000.00 USD | 0.00 USD | 89,110.00 USD | 15,480.00 USD | 29,290.00 USD |
| `7D` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD |
| `1D` | `0.0842` | 28,390,000.00 USD | 28,390,000.00 USD | 0.00 USD | 50,900.00 USD | 2,010.00 USD | 47,720.00 USD |
| `7D` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `1D` | `0.0844` | 28,500,000.00 USD | 28,500,000.00 USD | 0.00 USD | 112,650.00 USD | 0.00 USD | 574.90 USD |
| `7D` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `1D` | `0.0846` | 28,610,000.00 USD | 28,610,000.00 USD | 0.00 USD | 90,570.00 USD | 16,670.00 USD | 264.82 USD |
| `7D` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
| `1D` | `0.0848` | 28,630,000.00 USD | 28,630,000.00 USD | 0.00 USD | 22,580.00 USD | 0.00 USD | 284.68 USD |
| `7D` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 0.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD |
| `1D` | `0.0850` | 28,660,000.00 USD | 28,660,000.00 USD | 0.00 USD | 23,830.00 USD | 0.00 USD | 448.19 USD |
| `7D` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 0.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD |
| `1D` | `0.0852` | 28,730,000.00 USD | 28,730,000.00 USD | 0.00 USD | 35,100.00 USD | 24,590.00 USD | 17,300.00 USD |
| `7D` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 0.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD |
| `1D` | `0.0854` | 28,810,000.00 USD | 28,810,000.00 USD | 0.00 USD | 40,150.00 USD | 13,930.00 USD | 20,220.00 USD |
| `7D` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 0.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD |
| `1D` | `0.0856` | 29,100,000.00 USD | 29,100,000.00 USD | 0.00 USD | 159,460.00 USD | 78,270.00 USD | 56,120.00 USD |
| `7D` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 0.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD |
| `1D` | `0.0858` | 29,300,000.00 USD | 29,300,000.00 USD | 0.00 USD | 121,210.00 USD | 54,820.00 USD | 27,690.00 USD |
| `7D` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 0.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD |
| `1D` | `0.0860` | 29,550,000.00 USD | 29,550,000.00 USD | 0.00 USD | 130,590.00 USD | 55,620.00 USD | 60,210.00 USD |
| `7D` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 0.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0862` | 29,720,000.00 USD | 29,720,000.00 USD | 0.00 USD | 54,010.00 USD | 54,000.00 USD | 57,860.00 USD |
| `7D` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 0.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0864` | 29,760,000.00 USD | 29,760,000.00 USD | 0.00 USD | 22,510.00 USD | 20,050.00 USD | 5,370.00 USD |
| `7D` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 0.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD |
| `1D` | `0.0866` | 29,880,000.00 USD | 29,880,000.00 USD | 0.00 USD | 57,180.00 USD | 17,950.00 USD | 44,690.00 USD |
| `7D` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 0.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD |
| `1D` | `0.0868` | 30,010,000.00 USD | 30,010,000.00 USD | 0.00 USD | 32,660.00 USD | 46,420.00 USD | 48,880.00 USD |
| `7D` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 0.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD |
| `1D` | `0.0870` | 30,140,000.00 USD | 30,140,000.00 USD | 0.00 USD | 68,060.00 USD | 21,060.00 USD | 42,320.00 USD |
| `7D` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 0.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0872` | 30,380,000.00 USD | 30,380,000.00 USD | 0.00 USD | 67,420.00 USD | 100,220.00 USD | 71,010.00 USD |
| `7D` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 0.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD |
| `1D` | `0.0874` | 30,450,000.00 USD | 30,450,000.00 USD | 0.00 USD | 19,050.00 USD | 8,830.00 USD | 36,110.00 USD |
| `7D` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD |
| `1D` | `0.0876` | 30,510,000.00 USD | 30,510,000.00 USD | 0.00 USD | 30,130.00 USD | 31,610.00 USD | 0.00 USD |
| `7D` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 0.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD |
| `1D` | `0.0878` | 30,660,000.00 USD | 30,660,000.00 USD | 0.00 USD | 50,320.00 USD | 44,590.00 USD | 54,340.00 USD |
| `7D` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 0.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD |
| `1D` | `0.0880` | 30,760,000.00 USD | 30,760,000.00 USD | 0.00 USD | 50,910.00 USD | 17,330.00 USD | 38,970.00 USD |
| `7D` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 0.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD |
| `7D` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 0.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD |
| `7D` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 0.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD |
| `7D` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 0.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD |
| `7D` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 0.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 0.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD |
| `7D` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 0.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD |
| `7D` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 0.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.07B` | Total OI Tokens: `14,074,573,945.3 DOGE`
  * 1h OI Change: `-3.11%` | 4h OI Change: `-4.79%` | 24h OI Change: `-6.69%`
  * Exchange Breakdown: Binance=`252.10M` | Bybit=`107.68M` | OKX=`108.71M` | Hyperliquid=`76.81M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `22.60K` | Last 24h: `83.91K` | Last 3d: `253.77K` | Last 7d: `336.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0069%` | **USDT KuCoin** | `0.0048%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0002%` | **USDT Bitget** | `0.0037%` |
| **CoinM Binance** | `0.0064%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `51.94%` | `48.06%` | `1.08` | 357,790,000.00 USD |
| `15M` | `Binance` | `50.7%` | `49.3%` | `1.03` | 185,940,000.00 USD |
| `15M` | `OKX` | `61.15%` | `38.85%` | `1.57` | 21,140,000.00 USD |
| `15M` | `Bybit` | `53.45%` | `46.55%` | `1.15` | 47,950,000.00 USD |
| `15M` | `KuCoin` | `45.72%` | `54.28%` | `0.84` | 1,410,000.00 USD |
| `15M` | `Gate` | `52.1%` | `47.9%` | `1.09` | 9,060,000.00 USD |
| `15M` | `Bitget` | `49.06%` | `50.94%` | `0.96` | 8,900,000.00 USD |
| `15M` | `BingX` | `48.57%` | `51.43%` | `0.94` | 2,350,000.00 USD |
| `15M` | `MEXC` | `51.63%` | `48.37%` | `1.07` | 4,400,000.00 USD |
| `15M` | `Bitunix` | `44.57%` | `55.43%` | `0.80` | 8,320,000.00 USD |
| `15M` | `Hyperliquid` | `54.34%` | `45.66%` | `1.19` | 51,600,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.65%` | `50.35%` | `0.99` | 2,580,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `19.75%` | `80.25%` | `0.25` | 455,490.00 USD |
| `15M` | `HTX` | `38.26%` | `61.74%` | `0.62` | 353,080.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `40.1%` | `59.9%` | `0.67` | 989,000.00 USD |
| `15M` | `Aster` | `49.74%` | `50.26%` | `0.99` | 8,600,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `51.39%` | `48.61%` | `1.06` | 3,750,000.00 USD |
| `15M` | `Whale Positions` | `50.7%` | `49.3%` | `1.03` | 185,940,000.00 USD |
| `15M` | `Global Accounts` | `51.94%` | `48.06%` | `1.08` | 357,790,000.00 USD |
| `1H` | `DOGE` | `45.41%` | `54.59%` | `0.83` | 1,900,000,000.00 USD |
| `1H` | `Binance` | `45.09%` | `54.91%` | `0.82` | 1,090,000,000.00 USD |
| `1H` | `OKX` | `46.61%` | `53.39%` | `0.87` | 117,400,000.00 USD |
| `1H` | `Bybit` | `44.2%` | `55.8%` | `0.79` | 221,600,000.00 USD |
| `1H` | `KuCoin` | `43.76%` | `56.24%` | `0.78` | 11,760,000.00 USD |
| `1H` | `Gate` | `49.62%` | `50.38%` | `0.98` | 40,580,000.00 USD |
| `1H` | `Bitget` | `36.96%` | `63.04%` | `0.59` | 51,000,000.00 USD |
| `1H` | `BingX` | `55.11%` | `44.89%` | `1.23` | 15,350,000.00 USD |
| `1H` | `MEXC` | `49.58%` | `50.42%` | `0.98` | 26,310,000.00 USD |
| `1H` | `Bitunix` | `44.37%` | `55.63%` | `0.80` | 44,620,000.00 USD |
| `1H` | `Hyperliquid` | `48.92%` | `51.08%` | `0.96` | 197,510,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.99%` | `47.01%` | `1.13` | 11,650,000.00 USD |
| `1H` | `Crypto.com` | `49.29%` | `50.71%` | `0.97` | 0.00 USD |
| `1H` | `WhiteBIT` | `19.44%` | `80.56%` | `0.24` | 2,950,000.00 USD |
| `1H` | `HTX` | `37.6%` | `62.4%` | `0.60` | 2,080,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.36%` | `55.64%` | `0.80` | 5,920,000.00 USD |
| `1H` | `Aster` | `48.76%` | `51.24%` | `0.95` | 41,140,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `56.89%` | `43.11%` | `1.32` | 21,740,000.00 USD |
| `1H` | `Whale Positions` | `45.09%` | `54.91%` | `0.82` | 1,090,000,000.00 USD |
| `1H` | `Global Accounts` | `45.41%` | `54.59%` | `0.83` | 1,900,000,000.00 USD |
| `4H` | `DOGE` | `46.31%` | `53.69%` | `0.86` | 2,050,000,000.00 USD |
| `4H` | `Binance` | `45.55%` | `54.45%` | `0.84` | 1,180,000,000.00 USD |
| `4H` | `OKX` | `48.02%` | `51.98%` | `0.92` | 127,930,000.00 USD |
| `4H` | `Bybit` | `45.18%` | `54.82%` | `0.82` | 230,020,000.00 USD |
| `4H` | `KuCoin` | `43.62%` | `56.38%` | `0.77` | 12,550,000.00 USD |
| `4H` | `Gate` | `48.79%` | `51.21%` | `0.95` | 49,300,000.00 USD |
| `4H` | `Bitget` | `37.78%` | `62.22%` | `0.61` | 57,050,000.00 USD |
| `4H` | `BingX` | `52.03%` | `47.97%` | `1.08` | 21,500,000.00 USD |
| `4H` | `MEXC` | `52.58%` | `47.42%` | `1.11` | 28,110,000.00 USD |
| `4H` | `Bitunix` | `44.86%` | `55.14%` | `0.81` | 48,850,000.00 USD |
| `4H` | `Hyperliquid` | `48.09%` | `51.91%` | `0.93` | 201,350,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.82%` | `44.18%` | `1.26` | 14,470,000.00 USD |
| `4H` | `Crypto.com` | `50.03%` | `49.97%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `28.3%` | `71.7%` | `0.39` | 3,610,000.00 USD |
| `4H` | `HTX` | `39.19%` | `60.81%` | `0.64` | 2,760,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.77%` | `55.23%` | `0.81` | 6,370,000.00 USD |
| `4H` | `Aster` | `46.24%` | `53.76%` | `0.86` | 42,370,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.96%` | `51.04%` | `0.96` | 22,440,000.00 USD |
| `4H` | `Whale Positions` | `45.55%` | `54.45%` | `0.84` | 1,180,000,000.00 USD |
| `4H` | `Global Accounts` | `46.31%` | `53.69%` | `0.86` | 2,050,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0791` | `0.0791` | `0.0791` | `0.0792` | `0.0790` | 1,623,560.28 USD | 710,933.62 USD | 912,626.66 USD | -201,693.05 USD | `-12.42%` | `1B / 6S` |
| `0:00 UTC` | `0.0794` | `0.0794` | `0.0794` | `0.0795` | `0.0791` | 2,224,641.24 USD | 1,501,047.07 USD | 723,594.17 USD | 777,452.89 USD | `+34.95%` | `11B / 0S` |
| `5:00 UTC` | `0.0793` | `0.0793` | `0.0793` | `0.0795` | `0.0792` | 1,861,645.62 USD | 802,421.72 USD | 1,059,223.91 USD | -256,802.19 USD | `-13.79%` | `3B / 2S` |
| `0:00 UTC` | `0.0785` | `0.0784` | `0.0785` | `0.0793` | `0.0779` | 23,632,878.19 USD | 10,124,152.20 USD | 13,508,725.98 USD | -3,384,573.78 USD | `-14.32%` | `7B / 41S` |
| `5:00 UTC` | `0.0785` | `0.0785` | `0.0785` | `0.0786` | `0.0783` | 4,602,184.99 USD | 2,513,950.11 USD | 2,088,234.88 USD | 425,715.23 USD | `+9.25%` | `2B / 3S` |
| `0:00 UTC` | `0.0760` | `0.0766` | `0.0760` | `0.0786` | `0.0752` | 55,822,204.41 USD | 22,894,150.54 USD | 32,928,053.87 USD | -10,033,903.33 USD | `-17.97%` | `2B / 33S` |
| `5:00 UTC` | `0.0757` | `0.0754` | `0.0757` | `0.0762` | `0.0742` | 60,549,155.39 USD | 27,187,435.52 USD | 33,361,719.87 USD | -6,174,284.35 USD | `-10.20%` | `1B / 21S` |
| `0:00 UTC` | `0.0753` | `0.0755` | `0.0753` | `0.0761` | `0.0749` | 29,212,143.58 USD | 15,504,806.30 USD | 13,707,337.28 USD | 1,797,469.02 USD | `+6.15%` | `8B / 1S` |
| `5:00 UTC` | `0.0766` | `0.0764` | `0.0766` | `0.0769` | `0.0759` | 15,471,814.11 USD | 7,521,434.27 USD | 7,950,379.84 USD | -428,945.57 USD | `-2.77%` | `7B / 6S` |
| `0:00 UTC` | `0.0767` | `0.0767` | `0.0767` | `0.0768` | `0.0766` | 1,233,200.54 USD | 626,570.88 USD | 606,629.66 USD | 19,941.21 USD | `+1.62%` | `6B / 5S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:51` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0795` | 0.00 USD | 0.00 USD |
| `10-28 20:12` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0790` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.0002` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0785` | 0.00 USD | 0.00 USD |
| `10-28 19:47` | `Volume 100M DOGE` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0785` | 0.00 USD | 0.00 USD |
| `10-28 19:19` | `Volume 100M DOGE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.0786` | 17,000,000.00 USD | 0.00 USD |
| `10-28 17:27` | `Range 0.0002` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0799` | 0.00 USD | 0.00 USD |
| `10-28 16:36` | `Range 0.0002` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.0800` | 0.00 USD | 0.00 USD |
| `10-28 16:07` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0803` | 0.00 USD | 0.00 USD |
| `10-28 15:16` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0806` | 0.00 USD | 0.00 USD |
| `10-28 15:13` | `Volume 100M DOGE` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0806` | 0.00 USD | 0.00 USD |
| `10-28 13:51` | `Volume 100M DOGE` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0804` | 0.00 USD | 0.00 USD |
| `10-28 13:31` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0802` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Volume 100M DOGE` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0797` | 0.00 USD | 0.00 USD |
| `10-28 07:56` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0793` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.0002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.0795` | 0.00 USD | 0.00 USD |
| `10-28 07:07` | `Range 0.0002` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.0794` | 74,000,000.00 USD | 0.00 USD |
| `10-28 06:32` | `Range 0.0002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.0790` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -261,290.00 USD | 689,960.00 USD | **`ACCUMULATION`** |
| `15m` | 45,340.00 USD | 3,890,000.00 USD | **`ACCUMULATION`** |
| `30m` | 472,930.00 USD | 4,270,000.00 USD | **`ACCUMULATION`** |
| `1h` | -7,050,000.00 USD | -28,770,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -9,060,000.00 USD | -32,450,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -10,970,000.00 USD | -33,850,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -12,570,000.00 USD | -34,610,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -11,420,000.00 USD | -30,140,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,910,000.00 USD | -36,100,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -13,410,000.00 USD | -52,940,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -50,190,000.00 USD | -160,730,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -277,320,000.00 USD | -780,770,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-261.29K` | 15m=`+45.34K` | 1h=`-7.05M` | 24h=`-13.41M`
* Futures Capital Netflows: 5m=`+689.96K` | 15m=`+3.89M` | 1h=`-28.77M` | 24h=`-52.94M`
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
  * `2026-10-30 02:53:46 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:14:46 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:00:46 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:59:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:59:46 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:59:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:46 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:46 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:46 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:46 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:46 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0744` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-1.13` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.08`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0757` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.28` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.93`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0771`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
