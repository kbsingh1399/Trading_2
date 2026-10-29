# 🏛️ SOVEREIGN CANDIDATE DOSSIER: DOGE
**Canonical Key**: `DOGE` | **Broker Instrument**: `DOGUSD.p` | **Asset Class**: `Crypto Meme`
**Timestamp**: `2026-10-30 00:32:19 IST` (`2026-10-29 19:02:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.0782` | **Live Ask Quote**: `0.0803` | **Mid Price**: `0.0793`
- **Spread Points**: `21.00` | **Spread BPS**: `264.98 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.0777` | VWAP Z-Score: `+0.28` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000436` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `43.19` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.0805` | Lower -3.00σ Band: `0.0750`
  * Upper +2.51σ Band: `0.0800` | Lower -2.51σ Band: `0.0755`
  * Upper +2.01σ Band: `0.0796` | Lower -2.01σ Band: `0.0759`
  * Upper +2.00σ Band: `0.0796` | Lower -2.00σ Band: `0.0759`
  * Upper +1.28σ Band: `0.0789` | Lower -1.28σ Band: `0.0766`
  * Upper +1.00σ Band: `0.0787` | Lower -1.00σ Band: `0.0768`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.0785` | EMA-20=`0.0785` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.0781` (Slope: `+0.0000`) | EMA-100=`0.0780`
  * Institutional Anchors: EMA-144=`0.0779` | EMA-200=`0.0777` (Slope: `+0.1863`) | EMA-233=`0.0775`
- **Range Boundaries**: 24H High=`0.0803` | 24H Low=`0.0763` | Weekly High=`0.0803` | Weekly Low=`0.0755`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.0786` (Distance: `+0.78%`)
  * Point of Control (POC) = `0.0767` (Distance: `+3.34%`)
  * Value Area Low (VAL) = `0.0764` (Distance: `+3.74%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.0789` | POC=`0.0786` | VAL=`0.0776`
  * Prior Day Extremes: PDH=`0.0798` | PDL=`0.0768` | PDC=`0.0791`
  * Monday Range Blueprint: High=`0.0770` | Mid=`0.0759` | Low=`0.0748`
  * Developing Weekly Value Area: Weekly VAH=`0.0781` | Weekly POC=`0.0761` | Weekly VAL=`0.0755`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.0794` | Low=`0.0763`
  * London Session (08:00-16:00 UTC): High=`0.0779` | Low=`0.0765`
  * New York Session (13:00-21:00 UTC): High=`0.0803` | Low=`0.0768`
  * Initial Balance (First Hour): IB High=`0.0779` | IB Low=`0.0772`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.0789` - `0.0796`
  * Optimal Trade Entry (OTE 0.705): `0.0794`
  * Structural Invalidation Anchor (0.786): `0.0799`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.0791` | `0.0792` | `0.0790` | `0.0792` | `16,508,114` | 1,305,517.14 USD | 517,664.07 USD | `+39.65%` | -8,228,093.93 USD | `+1.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.0792` | `0.0792` | `0.0790` | `0.0791` | `9,755,638` | 771,650.83 USD | -73,081.33 USD | `-9.47%` | -8,301,175.26 USD | `+0.13` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.0791` | `0.0794` | `0.0791` | `0.0794` | `12,912,486` | 1,023,779.39 USD | 458,766.43 USD | `+44.81%` | -7,842,408.83 USD | `+1.45` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.0795` | `0.0797` | `0.0793` | `0.0794` | `42,253,825` | 3,357,728.54 USD | 136,747.43 USD | `+4.07%` | -8,076,083.78 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.0794` | `0.0794` | `0.0789` | `0.0792` | `68,069,369` | 5,383,971.27 USD | -151,451.19 USD | `-2.81%` | -8,227,534.98 USD | `-0.17` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.0792` | `0.0794` | `0.0790` | `0.0793` | `22,821,448` | 1,807,596.47 USD | 373,518.85 USD | `+20.66%` | -7,854,016.13 USD | `+0.62` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.0806` | `0.0815` | `0.0799` | `0.0801` | `488,172,743` | 39,342,413.57 USD | -1,193,889.47 USD | `-3.03%` | -5,713,397.42 USD | `-0.42` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.0801` | `0.0802` | `0.0792` | `0.0796` | `261,755,492` | 20,864,959.87 USD | -2,385,280.59 USD | `-11.43%` | -8,098,678.01 USD | `-1.07` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.0796` | `0.0797` | `0.0789` | `0.0793` | `168,740,811` | 13,381,167.24 USD | 244,661.88 USD | `+1.83%` | -7,854,016.13 USD | `+0.58` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -10,443,207.77 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -5,854,456.34 USD | `+1.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0794` | `918,668,227` | 73,588,475.70 USD | -3,334,443.20 USD | `-4.53%` | -9,188,899.55 USD | `-0.42` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.0797` | `0.0799` | `0.0774` | `0.0778` | `998,970,852` | 78,232,937.14 USD | -7,024,064.25 USD | `-8.98%` | -3,060,763.89 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0778` | `0.0790` | `0.0775` | `0.0777` | `649,981,168` | 50,850,515.04 USD | -4,359,439.36 USD | `-8.57%` | -7,420,203.26 USD | `-0.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.0777` | `0.0788` | `0.0776` | `0.0786` | `503,385,445` | 39,374,059.36 USD | -3,023,004.52 USD | `-7.68%` | -10,443,207.77 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.0786` | `0.0807` | `0.0785` | `0.0806` | `1,040,365,871` | 82,785,086.25 USD | 4,588,751.43 USD | `+5.54%` | -5,854,456.34 USD | `+1.24` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.0806` | `0.0815` | `0.0789` | `0.0794` | `918,668,227` | 73,588,475.70 USD | -3,334,443.20 USD | `-4.53%` | -9,188,899.55 USD | `-0.42` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.0793`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `0.0793` | `78529.0000` | 6,231.12 USD | 15,563.68 USD | `8 orders` | `+0.01%` | `-` |
| `ASK` | `0.0793` | `117617.0000` | 9,332.56 USD | 9,332.56 USD | `9 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `0.0793` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 0.08` | `0.00%` | `-` |
| `BID` | `0.0793` | `79969.0000` | 6,344.50 USD | 6,344.50 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.0793` | `520938.0000` | 41,327.05 USD | 47,671.55 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `0.0793` | `120444.0000` | 9,554.94 USD | 57,226.50 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `0.0793` | `1034.0000` | 82.03 USD | 57,308.52 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `0.0793` | `484775.0000` | 38,454.29 USD | 95,762.82 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `0.0793` | `87938.0000` | 6,974.98 USD | 102,737.79 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0793` | `145543.0000` | 11,543.89 USD | 114,281.68 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `0.0793` | `120492.0000` | 9,556.82 USD | 123,838.51 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `0.0793` | `92856.0000` | 7,364.78 USD | 131,203.29 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `0.0793` | `349674.0000` | 27,733.69 USD | 158,936.98 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0793` | `78894.0000` | 6,257.00 USD | 165,193.98 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `0.0793` | `16967.0000` | 1,345.62 USD | 166,539.60 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `0.0793` | `117689.0000` | 9,333.09 USD | 175,872.69 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0793` | `12241.0000` | 970.74 USD | 176,843.43 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0793` | `18023.0000` | 1,429.24 USD | 178,272.67 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.0793` | `134715.0000` | 10,682.90 USD | 188,955.57 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `0.0793` | `120515.0000` | 9,556.72 USD | 198,512.29 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `0.0793` | `9180.0000` | 727.95 USD | 199,240.24 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `0.0793` | `230739.0000` | 18,296.45 USD | 217,536.69 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `0.0793` | `126259.0000` | 10,011.58 USD | 227,548.27 USD | `1 orders` | `-0.06%` | `-` |
| `ASK` | `0.0794` | `109642.0000` | 8,703.38 USD | 118,613.53 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `0.0794` | `97742.0000` | 7,758.56 USD | 109,910.15 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `0.0794` | `389739.0000` | 30,936.31 USD | 102,151.58 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0794` | `20216.0000` | 1,604.67 USD | 71,215.27 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0794` | `5039.0000` | 399.97 USD | 69,610.61 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0794` | `88190.0000` | 6,999.99 USD | 69,210.64 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `0.0794` | `136770.0000` | 10,855.85 USD | 62,210.64 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0794` | `18308.0000` | 1,453.14 USD | 51,354.80 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `0.0794` | `23937.0000` | 1,899.90 USD | 49,901.66 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0794` | `19526.0000` | 1,549.78 USD | 48,001.75 USD | `2 orders` | `+0.04%` | `-` |
| `ASK` | `0.0794` | `23937.0000` | 1,899.86 USD | 46,451.97 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0794` | `130948.0000` | 10,392.95 USD | 44,552.12 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0794` | `31138.0000` | 2,471.30 USD | 34,159.17 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0794` | `5040.0000` | 400.00 USD | 31,687.87 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `0.0794` | `5070.0000` | 402.37 USD | 31,287.87 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `0.0794` | `57082.0000` | 4,530.03 USD | 30,885.50 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `0.0794` | `123750.0000` | 9,820.43 USD | 26,355.48 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `0.0794` | `12241.0000` | 971.37 USD | 16,535.05 USD | `1 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:25:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `301` | `0xb83d...6e36` | `SHORT` | 8,146,904.42 USD | `102,645,925.00` | `0.0946` | `0.0794` | `1.30` | 1,560,437.23 USD | `+19.15%` | `3X Cross` |
| `310` | `0xc63a...a3cd` | `LONG` | 7,933,300.00 USD | `100,000,000.00` | `0.0856` | `0.0794` | `0.000000` | -631,521.96 USD | `-7.96%` | `10X Cross` |
| `317` | `0x610b...b613` | `LONG` | 7,831,055.41 USD | `98,666,424.00` | `0.0872` | `0.0794` | `0.0578` | -769,126.50 USD | `-9.82%` | `5X Cross` |
| `596` | `0x5b5d...c060` | `SHORT` | 3,929,024.86 USD | `49,478,955.00` | `0.0946` | `0.0794` | `3.09` | 752,491.75 USD | `+19.15%` | `3X Cross` |
| `633` | `0xca49...53c8` | `SHORT` | 3,692,367.97 USD | `46,542,649.00` | `0.0929` | `0.0794` | `0.3488` | 633,676.71 USD | `+17.16%` | `10X Cross` |
| `645` | `0x45d2...4029` | `SHORT` | 3,604,053.41 USD | `45,426,000.00` | `0.0954` | `0.0794` | `0.8443` | 731,575.81 USD | `+20.30%` | `10X Cross` |
| `796` | `0xecb6...2b00` | `SHORT` | 2,950,696.13 USD | `37,157,740.00` | `0.0796` | `0.0794` | `0.7787` | 6,655.40 USD | `+0.23%` | `10X Cross` |
| `1182` | `0x458d...ab3b` | `LONG` | 1,940,894.53 USD | `24,454,063.00` | `0.1002` | `0.0794` | `0.0714` | -510,027.38 USD | `-26.28%` | `3X Isolated` |
| `1187` | `0xeadc...9d55` | `LONG` | 1,930,999.28 USD | `24,317,440.00` | `0.0926` | `0.0794` | `0.000000` | -320,595.30 USD | `-16.60%` | `10X Cross` |
| `1237` | `0x9aa5...58af` | `SHORT` | 1,864,694.17 USD | `23,500,500.00` | `0.0907` | `0.0794` | `0.3943` | 266,060.78 USD | `+14.27%` | `10X Cross` |
| `1340` | `0xf48f...10fe` | `LONG` | 1,700,440.90 USD | `21,424,497.00` | `0.0968` | `0.0794` | `0.0339` | -373,863.70 USD | `-21.99%` | `4X Cross` |
| `1370` | `0x9946...0852` | `SHORT` | 1,659,513.07 USD | `20,910,149.00` | `0.0871` | `0.0794` | `0.1297` | 161,042.32 USD | `+9.70%` | `10X Cross` |
| `1549` | `0xcac1...26b3` | `SHORT` | 1,438,618.13 USD | `18,126,835.00` | `0.0943` | `0.0794` | `0.5023` | 270,841.07 USD | `+18.83%` | `10X Cross` |
| `1592` | `0x0d6a...ca57` | `LONG` | 1,398,994.11 USD | `17,626,455.00` | `0.0875` | `0.0794` | `0.0626` | -143,110.85 USD | `-10.23%` | `3X Isolated` |
| `1640` | `0x4808...a82c` | `LONG` | 1,335,094.38 USD | `16,828,143.00` | `0.0883` | `0.0794` | `0.0631` | -151,378.60 USD | `-11.34%` | `3X Cross` |
| `1769` | `0x31ef...f715` | `LONG` | 1,208,797.97 USD | `15,230,102.00` | `0.0936` | `0.0794` | `0.0668` | -216,897.96 USD | `-17.94%` | `3X Isolated` |
| `1784` | `0xbfc7...80b4` | `SHORT` | 1,191,641.74 USD | `15,020,000.00` | `0.0920` | `0.0794` | `0.3706` | 190,757.55 USD | `+16.01%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.0786` | 9,558.66 USD | `-` | `NEWS_INTEL` | `-` | #DOGE Whale BUY: 9.56K USD at 0.0786 USD [API] | `2026-10-27 22:43:16` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.0826` (Vol: 395,700.00 USD, Dist: `+4.16%`) | Long MP=`0.0767` (Vol: 519,500.00 USD, Dist: `--3.33%`)
  * 48H Horizon: Short MP=`0.0821` (Vol: 478,200.00 USD, Dist: `+3.55%`) | Long MP=`0.0774` (Vol: 691,800.00 USD, Dist: `--2.46%`)
  * 3D Horizon: Short MP=`0.0823` (Vol: 539,400.00 USD, Dist: `+3.75%`) | Long MP=`0.0765` (Vol: 660,700.00 USD, Dist: `--3.51%`)
  * 7D Horizon: Short MP=`0.0821` (Vol: 746,800.00 USD, Dist: `+3.56%`) | Long MP=`0.0762` (Vol: 988,700.00 USD, Dist: `--3.91%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0160` | 3,930.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0163` | 187.26 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0164` | 407.02 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0165` | 5,290.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0169` | 292.61 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0191` | 16,770.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0193` | 291.59 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0196` | 121.33 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0208` | 4,660.00 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0209` | 296.97 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0210` | 295.48 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0211` | 423.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0232` | 4,720.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0237` | 473.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0242` | 11,860.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0244` | 633.16 USD | 15,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0261` | 450.41 USD | 15,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0268` | 5,540.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0270` | 740.40 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0278` | 1,090.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0279` | 1,730.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0284` | 129.22 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0290` | 2,320.00 USD | 15,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0299` | 162.15 USD | 15,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0301` | 4,040.00 USD | 15,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0301` | 2,360.00 USD | 15,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0306` | 137.41 USD | 15,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0318` | 1,510.00 USD | 15,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0321` | 688,800.00 USD | 15,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0324` | 194.34 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0330` | 1,650.00 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0331` | 149.22 USD | 15,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0338` | 1,690.00 USD | 15,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0341` | 918.63 USD | 15,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0343` | 32,540.00 USD | 15,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0345` | 3,110.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0350` | 17,480.00 USD | 15,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0353` | 73,050.00 USD | 15,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0355` | 4,340.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0358` | 214.53 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0362` | 980.96 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0364` | 194.44 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0369` | 28,590.00 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0377` | 3,810.00 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0381` | 246.45 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0386` | 121.74 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0387` | 928.92 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0391` | 981.92 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0393` | 221.10 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0394` | 104,570.00 USD | 14,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0404` | 115.12 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0408` | 419.28 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0413` | 2,070.00 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 252.72 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 1,030.00 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0416` | 3,570.00 USD | 14,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0420` | 671.41 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 2,090.00 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0423` | 59,790.00 USD | 14,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 1,070.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 1,010.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0427` | 3,620.00 USD | 14,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0430` | 859.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0432` | 6,430.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0433` | 2,450.00 USD | 14,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0439` | 1,610.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 750.58 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0440` | 1,060.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0444` | 101,440.00 USD | 14,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 444.76 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0447` | 248.63 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0454` | 2,170.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0456` | 32,650.00 USD | 14,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0457` | 5,470.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 4,500.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0461` | 114.36 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 2,650.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0464` | 16,780.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0466` | 109.49 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0473` | 18,360.00 USD | 14,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0474` | 593.13 USD | 14,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0476` | 105.02 USD | 14,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0478` | 259.23 USD | 14,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 56,440.00 USD | 14,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0481` | 2,500.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0483` | 2,280.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 1,480.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0486` | 315.50 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0488` | 1,280.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0490` | 5,470.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0491` | 1,080.00 USD | 14,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0493` | 1,420.00 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 340.41 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 18,690.00 USD | 14,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0498` | 253.82 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0500` | 501.50 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0502` | 384.95 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 5,410.00 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0503` | 1,330.00 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 646.42 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0507` | 1,040.00 USD | 14,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0508` | 5,350.00 USD | 14,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 535.43 USD | 14,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0510` | 566.65 USD | 14,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 11,000.00 USD | 14,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0512` | 1,490.00 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0513` | 385.13 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 308.55 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 296.26 USD | 14,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0519` | 51,690.00 USD | 14,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 1,480.00 USD | 14,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0520` | 3,990.00 USD | 14,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0522` | 275,090.00 USD | 14,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0524` | 1,170.00 USD | 14,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,640.00 USD | 14,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 395.09 USD | 14,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0527` | 2,110.00 USD | 14,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 1,260.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0529` | 181,690.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0532` | 8,770.00 USD | 13,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0534` | 314,750.00 USD | 13,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0536` | 1,690.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0539` | 5,290.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 2,290.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0541` | 13,510.00 USD | 13,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0542` | 96,530.00 USD | 13,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0544` | 237.95 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 12,420.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0546` | 1,420.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0548` | 188.07 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0556` | 907.02 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0561` | 39,500.00 USD | 13,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 1,820.00 USD | 13,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0563` | 47,560.00 USD | 13,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 131.48 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0566` | 610.80 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0568` | 747.06 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 421.03 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0570` | 8,350.00 USD | 13,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0571` | 644.99 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0573` | 3,910.00 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 15,970.00 USD | 13,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 3,590.00 USD | 13,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0576` | 10,990.00 USD | 13,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 17,890.00 USD | 13,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0578` | 5,710,000.00 USD | 13,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0580` | 431.14 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0582` | 447.17 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0583` | 116.82 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 172.78 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0587` | 9,120.00 USD | 7,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0588` | 715.85 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0590` | 212.22 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0592` | 26,980.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0593` | 889.30 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 3,660.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 2,650.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0599` | 4,560.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 380.38 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0600` | 11,540.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0602` | 8,490.00 USD | 7,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 737.18 USD | 7,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0604` | 2,730.00 USD | 7,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 32,090.00 USD | 7,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 1,080.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0607` | 1,220.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 717.73 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0609` | 2,220.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 913.21 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0612` | 298.17 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 655.16 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0614` | 368.58 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0616` | 1,400.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 13,460.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0617` | 158.08 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0621` | 26,790.00 USD | 7,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0622` | 1,820.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 1,900.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0624` | 3,470.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,100,000.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0626` | 3,900.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0628` | 461.78 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0629` | 6,400.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 255.95 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0630` | 3,080.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0631` | 1,100,000.00 USD | 6,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0633` | 1,210.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0634` | 12,890.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 1,690.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 280.95 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0636` | 633.38 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0638` | 8,670.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0639` | 23,220.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 1,360.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0640` | 2,170.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0641` | 633.29 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0643` | 9,150.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 2,170.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0644` | 23,930.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0646` | 6,350.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0648` | 107,370.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 10,520.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0649` | 44,290.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0651` | 2,380.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0653` | 13,770.00 USD | 4,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0654` | 6,530.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0655` | 5,340.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0658` | 71,100.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 14,870.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0659` | 11,990.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0662` | 339.48 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0663` | 1,630.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 27,760.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0664` | 1,030.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 66,720.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0667` | 34,860.00 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0668` | 1,490.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 1,020,000.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0669` | 389.18 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0670` | 6,240.00 USD | 3,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0672` | 899.27 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 196.64 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0673` | 96,400.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0674` | 4,860.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 310.73 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0677` | 8,210.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 5,100.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0678` | 55,180.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0679` | 20,030.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0680` | 212.72 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0682` | 1,680.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0683` | 6,220.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0683` | 1,290.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0684` | 88,260.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 4,690.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0687` | 1,410.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0688` | 69,020.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0688` | 517.48 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0689` | 507,660.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0691` | 3,670.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0692` | 8,350.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0693` | 52,390.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0694` | 4,840.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0696` | 106,510.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0696` | 66,770,000.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0697` | 5,240.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,420.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0698` | 65,900,000.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0698` | 3,630.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0699` | 9,500.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0700` | 65,390,000.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0701` | 264.58 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0702` | 1,590.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0702` | 64,770,000.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0703` | 2,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0703` | 5,060.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0704` | 64,400,000.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0704` | 216.56 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0706` | 93,610.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0706` | 64,140,000.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0707` | 536.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.0708` | 63,840,000.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0710` | 23,690,000.00 USD | 23,690,000.00 USD | 32,660.00 USD | 46,420.00 USD | 48,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0710` | 63,550,000.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0711` | 111.69 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0711` | 23,560,000.00 USD | 23,560,000.00 USD | 16,230.00 USD | 8,560.00 USD | 24,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0712` | 23,510,000.00 USD | 23,510,000.00 USD | 50,000.00 USD | 12,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0712` | 63,090,000.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0712` | 2,600.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0713` | 23,450,000.00 USD | 23,450,000.00 USD | 28,210.00 USD | 45,410.00 USD | 62,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0713` | 1,750,000.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0714` | 23,320,000.00 USD | 23,320,000.00 USD | 26,980.00 USD | 32,280.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0714` | 62,580,000.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0714` | 2,220.00 USD | 759,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0715` | 23,250,000.00 USD | 23,250,000.00 USD | 9,490.00 USD | 1,820.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0716` | 8,120.00 USD | 757,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0716` | 23,200,000.00 USD | 23,200,000.00 USD | 42,760.00 USD | 43,290.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0716` | 62,080,000.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 560.88 USD | 749,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0717` | 23,100,000.00 USD | 23,100,000.00 USD | 22,320.00 USD | 11,700.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0717` | 1,520.00 USD | 748,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0718` | 23,050,000.00 USD | 23,050,000.00 USD | 63,040.00 USD | 41,450.00 USD | 50,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0718` | 61,650,000.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0718` | 10,850.00 USD | 747,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0719` | 22,890,000.00 USD | 22,890,000.00 USD | 15,840.00 USD | 9,450.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0720` | 778.93 USD | 736,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0720` | 22,860,000.00 USD | 22,860,000.00 USD | 48,000.00 USD | 15,600.00 USD | 31,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0720` | 61,290,000.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0721` | 23,870.00 USD | 735,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0721` | 22,760,000.00 USD | 22,760,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0722` | 22,700,000.00 USD | 22,700,000.00 USD | 29,680.00 USD | 15,630.00 USD | 27,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0722` | 60,720,000.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0722` | 5,720.00 USD | 711,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0723` | 22,630,000.00 USD | 22,630,000.00 USD | 30,830.00 USD | 73,610.00 USD | 7,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0723` | 4,900.00 USD | 705,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0724` | 22,510,000.00 USD | 22,510,000.00 USD | 32,170.00 USD | 17,780.00 USD | 84,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0724` | 60,340,000.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0725` | 598.51 USD | 700,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0725` | 22,380,000.00 USD | 22,380,000.00 USD | 82,840.00 USD | 40,520.00 USD | 32,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0726` | 260.74 USD | 700,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0726` | 22,220,000.00 USD | 22,220,000.00 USD | 31,660.00 USD | 0.00 USD | 142.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0726` | 59,850,000.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 948.37 USD | 700,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0727` | 22,190,000.00 USD | 22,190,000.00 USD | 20,420.00 USD | 0.00 USD | 200.42 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0727` | 3,170.00 USD | 699,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0728` | 22,170,000.00 USD | 22,170,000.00 USD | 15,580.00 USD | 802.30 USD | 419.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0728` | 59,350,000.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0728` | 646.11 USD | 696,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0729` | 22,150,000.00 USD | 22,150,000.00 USD | 17,820.00 USD | 0.00 USD | 18,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0730` | 72,950.00 USD | 695,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0730` | 22,120,000.00 USD | 22,120,000.00 USD | 14,450.00 USD | 0.00 USD | 223.21 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0730` | 58,930,000.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0731` | 10,300.00 USD | 622,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0731` | 22,100,000.00 USD | 22,100,000.00 USD | 42,980.00 USD | 0.00 USD | 100.25 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 1,930.00 USD | 612,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0732` | 22,060,000.00 USD | 22,060,000.00 USD | 42,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0732` | 58,610,000.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0732` | 5,410.00 USD | 610,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0733` | 22,020,000.00 USD | 22,020,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0734` | 22,010,000.00 USD | 22,010,000.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0734` | 57,050,000.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0735` | 7,000.00 USD | 604,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0735` | 22,000,000.00 USD | 22,000,000.00 USD | 24,100.00 USD | 0.00 USD | 41.24 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 4,060.00 USD | 597,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0736` | 21,980,000.00 USD | 21,980,000.00 USD | 8,600.00 USD | 0.00 USD | 258.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0736` | 56,150,000.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0736` | 5,490.00 USD | 593,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0737` | 21,970,000.00 USD | 21,970,000.00 USD | 45,400.00 USD | 0.00 USD | 475.78 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0737` | 10,390.00 USD | 588,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0738` | 21,920,000.00 USD | 21,920,000.00 USD | 29,080.00 USD | 0.00 USD | 162.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0738` | 54,660,000.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0738` | 5,630.00 USD | 577,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0739` | 21,890,000.00 USD | 21,890,000.00 USD | 32,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0740` | 13,570.00 USD | 572,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0740` | 21,860,000.00 USD | 21,860,000.00 USD | 32,660.00 USD | 0.00 USD | 267.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0740` | 53,220,000.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 455,270.00 USD | 558,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0741` | 21,830,000.00 USD | 21,830,000.00 USD | 31,820.00 USD | 0.00 USD | 560.08 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0741` | 777.39 USD | 103,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0742` | 21,790,000.00 USD | 21,790,000.00 USD | 34,770.00 USD | 0.00 USD | 145.18 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0742` | 50,600,000.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0742` | 2,360.00 USD | 102,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0743` | 21,760,000.00 USD | 21,760,000.00 USD | 33,450.00 USD | 27,500.00 USD | 162.32 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0743` | 2,140.00 USD | 100,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0744` | 21,700,000.00 USD | 21,700,000.00 USD | 42,800.00 USD | 1,840.00 USD | 15,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0744` | 47,850,000.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0745` | 2,040.00 USD | 98,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0745` | 21,640,000.00 USD | 21,640,000.00 USD | 106,370.00 USD | 57,220.00 USD | 24,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 581.34 USD | 96,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0746` | 21,450,000.00 USD | 21,450,000.00 USD | 238,810.00 USD | 175,410.00 USD | 125,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0746` | 45,780,000.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0746` | 1,050.00 USD | 95,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0747` | 20,910,000.00 USD | 20,910,000.00 USD | 272,470.00 USD | 121,590.00 USD | 63,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0747` | 359.77 USD | 94,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0748` | 20,450,000.00 USD | 20,450,000.00 USD | 169,810.00 USD | 65,720.00 USD | 98,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0748` | 42,890,000.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0749` | 20,120,000.00 USD | 20,120,000.00 USD | 194,160.00 USD | 144,960.00 USD | 9,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0750` | 1,370.00 USD | 94,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0750` | 19,770,000.00 USD | 19,770,000.00 USD | 233,830.00 USD | 83,730.00 USD | 121,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0750` | 39,780,000.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 451.13 USD | 92,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0751` | 19,330,000.00 USD | 19,330,000.00 USD | 260,780.00 USD | 82,120.00 USD | 65,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0751` | 2,450.00 USD | 92,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0752` | 18,920,000.00 USD | 18,920,000.00 USD | 117,830.00 USD | 19,450.00 USD | 85,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0752` | 37,910,000.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0752` | 3,910.00 USD | 89,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0753` | 18,700,000.00 USD | 18,700,000.00 USD | 131,890.00 USD | 72,710.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0754` | 617.57 USD | 85,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0754` | 18,470,000.00 USD | 18,470,000.00 USD | 87,330.00 USD | 62,330.00 USD | 19,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0754` | 34,560,000.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0755` | 4,060.00 USD | 85,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0755` | 18,300,000.00 USD | 18,300,000.00 USD | 121,750.00 USD | 15,650.00 USD | 68,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0756` | 12,630.00 USD | 81,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0756` | 18,090,000.00 USD | 18,090,000.00 USD | 171,830.00 USD | 147,310.00 USD | 111,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0756` | 32,160,000.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0756` | 356.24 USD | 68,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0757` | 17,660,000.00 USD | 17,660,000.00 USD | 91,080.00 USD | 44,210.00 USD | 104,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0757` | 2,510.00 USD | 68,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0758` | 17,420,000.00 USD | 17,420,000.00 USD | 68,430.00 USD | 31,960.00 USD | 60,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0758` | 26,980,000.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0759` | 5,070.00 USD | 65,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0759` | 17,260,000.00 USD | 17,260,000.00 USD | 181,950.00 USD | 106,750.00 USD | 8,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0760` | 32,080.00 USD | 60,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0760` | 16,960,000.00 USD | 16,960,000.00 USD | 219,840.00 USD | 259,920.00 USD | 277,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0760` | 22,370,000.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 1,690.00 USD | 28,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0761` | 16,210,000.00 USD | 16,210,000.00 USD | 486,610.00 USD | 431,520.00 USD | 272,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0761` | 1,130.00 USD | 26,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0762` | 15,020,000.00 USD | 15,020,000.00 USD | 540,050.00 USD | 279,200.00 USD | 216,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0762` | 18,040,000.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0762` | 181.93 USD | 25,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0763` | 13,980,000.00 USD | 13,980,000.00 USD | 315,400.00 USD | 180,850.00 USD | 197,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0764` | 11,510.00 USD | 25,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0764` | 13,290,000.00 USD | 13,290,000.00 USD | 401,670.00 USD | 363,400.00 USD | 52,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0764` | 14,900,000.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0765` | 9,890.00 USD | 14,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0765` | 12,470,000.00 USD | 12,470,000.00 USD | 525,820.00 USD | 223,110.00 USD | 314,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0766` | 11,410,000.00 USD | 11,410,000.00 USD | 621,080.00 USD | 274,850.00 USD | 280,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0766` | 12,660,000.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0767` | 10,230,000.00 USD | 10,230,000.00 USD | 238,180.00 USD | 103,410.00 USD | 213,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0768` | 9,670,000.00 USD | 9,670,000.00 USD | 426,850.00 USD | 236,860.00 USD | 142,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0768` | 10,740,000.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0769` | 8,870,000.00 USD | 8,870,000.00 USD | 227,680.00 USD | 193,080.00 USD | 70,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0770` | 8,380,000.00 USD | 8,380,000.00 USD | 296,720.00 USD | 91,840.00 USD | 270,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0770` | 9,050,000.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0771` | 7,720,000.00 USD | 7,720,000.00 USD | 231,550.00 USD | 266,030.00 USD | 190,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0772` | 7,030,000.00 USD | 7,030,000.00 USD | 169,730.00 USD | 297,590.00 USD | 333,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0772` | 7,390,000.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0773` | 6,230,000.00 USD | 6,230,000.00 USD | 272,980.00 USD | 149,960.00 USD | 241,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0774` | 5,570,000.00 USD | 5,570,000.00 USD | 143,850.00 USD | 97,350.00 USD | 167,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0774` | 5,610,000.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0775` | 5,160,000.00 USD | 5,160,000.00 USD | 340,690.00 USD | 103,510.00 USD | 17,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0776` | 4,700,000.00 USD | 4,700,000.00 USD | 106,410.00 USD | 237,880.00 USD | 381,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0776` | 3,770,000.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0777` | 3,970,000.00 USD | 3,970,000.00 USD | 48,260.00 USD | 163,400.00 USD | 146.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0778` | 3,760,000.00 USD | 3,760,000.00 USD | 69,720.00 USD | 72,030.00 USD | 187,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0778` | 3,290,000.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0779` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 85,950.00 USD | 253.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0780` | 3,340,000.00 USD | 3,340,000.00 USD | 217,760.00 USD | 88,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0781` | 3,040,000.00 USD | 3,040,000.00 USD | 16,920.00 USD | 33,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0782` | 2,990,000.00 USD | 2,990,000.00 USD | 44,780.00 USD | 75,640.00 USD | 85,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0782` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0783` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 47,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0784` | 2,730,000.00 USD | 2,730,000.00 USD | 265,800.00 USD | 132,460.00 USD | 158,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0784` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0785` | 2,180,000.00 USD | 2,180,000.00 USD | 168,930.00 USD | 110,520.00 USD | 61,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0786` | 1,840,000.00 USD | 1,840,000.00 USD | 170,030.00 USD | 120,480.00 USD | 233,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0786` | 2,370,000.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0787` | 1,310,000.00 USD | 1,310,000.00 USD | 150,580.00 USD | 312,480.00 USD | 128,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0788` | 720,770.00 USD | 720,770.00 USD | 36,540.00 USD | 98,050.00 USD | 288,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0788` | 1,700,000.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.0789` | 4,160.00 USD | 4,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.0789` | 298,000.00 USD | 298,000.00 USD | 127,940.00 USD | 35,430.00 USD | 66,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0790` | 67,940.00 USD | 67,940.00 USD | 0.00 USD | 3,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0790` | 970,610.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0791` | 64,690.00 USD | 64,690.00 USD | 0.00 USD | 3,690.00 USD | 30,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.0792` | 30,970.00 USD | 30,970.00 USD | 0.00 USD | 30,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.0794` | 643,260.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0796` | 16,260.00 USD | 16,260.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0797` | 414,540.00 USD | 414,540.00 USD | 123,730.00 USD | 33,340.00 USD | 241,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0798` | 569,220.00 USD | 569,220.00 USD | 0.00 USD | 154,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0799` | 912,240.00 USD | 912,240.00 USD | 169,980.00 USD | 1,740.00 USD | 171,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0800` | 917,850.00 USD | 917,850.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0804` | 928,750.00 USD | 928,750.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0805` | 145.88 USD | 145.88 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0806` | 1,030,000.00 USD | 1,030,000.00 USD | 3,520.00 USD | 0.00 USD | 98,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0807` | 1,410,000.00 USD | 1,410,000.00 USD | 181,700.00 USD | 160,730.00 USD | 40,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0808` | 2,340,000.00 USD | 2,340,000.00 USD | 380,920.00 USD | 23,520.00 USD | 522,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0809` | 3,030,000.00 USD | 3,030,000.00 USD | 419,190.00 USD | 273,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0810` | 3,500,000.00 USD | 3,500,000.00 USD | 214,090.00 USD | 132,380.00 USD | 118,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0811` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 243,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0812` | 4,100,000.00 USD | 4,100,000.00 USD | 93,910.00 USD | 75,260.00 USD | 192,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0813` | 4,360,000.00 USD | 4,360,000.00 USD | 27,080.00 USD | 18,240.00 USD | 209,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0814` | 4,790,000.00 USD | 4,790,000.00 USD | 22,430.00 USD | 18,210.00 USD | 386,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0815` | 5,350,000.00 USD | 5,350,000.00 USD | 249,400.00 USD | 201,730.00 USD | 112,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0816` | 6,230,000.00 USD | 6,230,000.00 USD | 441,880.00 USD | 245,220.00 USD | 189,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0817` | 6,870,000.00 USD | 6,870,000.00 USD | 361,650.00 USD | 152,470.00 USD | 130,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0818` | 710.08 USD | 855.96 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0818` | 7,650,000.00 USD | 7,650,000.00 USD | 298,910.00 USD | 161,880.00 USD | 321,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0819` | 8,350,000.00 USD | 8,350,000.00 USD | 171,350.00 USD | 368,950.00 USD | 156,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0820` | 9,340,000.00 USD | 9,340,000.00 USD | 215,860.00 USD | 275,570.00 USD | 499,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0821` | 10,060,000.00 USD | 10,060,000.00 USD | 383,530.00 USD | 167,310.00 USD | 171,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0822` | 10,660,000.00 USD | 10,660,000.00 USD | 258,140.00 USD | 184,710.00 USD | 156,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0823` | 10,970,000.00 USD | 10,970,000.00 USD | 250,780.00 USD | 51,750.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0824` | 11,480,000.00 USD | 11,480,000.00 USD | 131,550.00 USD | 172,750.00 USD | 198,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0825` | 11,690,000.00 USD | 11,690,000.00 USD | 110,900.00 USD | 84,710.00 USD | 21,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0826` | 11,980,000.00 USD | 11,980,000.00 USD | 63,310.00 USD | 36,010.00 USD | 183,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0827` | 12,090,000.00 USD | 12,090,000.00 USD | 63,060.00 USD | 49,420.00 USD | 55.02 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0828` | 12,470,000.00 USD | 12,470,000.00 USD | 269,440.00 USD | 73,490.00 USD | 36,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0829` | 12,860,000.00 USD | 12,860,000.00 USD | 234,870.00 USD | 88,990.00 USD | 72,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0829` | 27,290.00 USD | 28,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0830` | 13,380,000.00 USD | 13,380,000.00 USD | 258,290.00 USD | 110,610.00 USD | 151,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0831` | 13,590,000.00 USD | 13,590,000.00 USD | 102,690.00 USD | 64,510.00 USD | 42,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0832` | 11,330.00 USD | 39,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0832` | 14,010,000.00 USD | 14,010,000.00 USD | 233,350.00 USD | 91,440.00 USD | 86,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0833` | 14,260,000.00 USD | 14,260,000.00 USD | 158,470.00 USD | 68,410.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0834` | 14,600,000.00 USD | 14,600,000.00 USD | 146,880.00 USD | 60,550.00 USD | 133,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0835` | 14,990,000.00 USD | 14,990,000.00 USD | 122,400.00 USD | 184,470.00 USD | 78,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0835` | 205.70 USD | 39,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0836` | 15,370,000.00 USD | 15,370,000.00 USD | 78,450.00 USD | 84,520.00 USD | 221,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0837` | 13.30 USD | 39,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0837` | 15,660,000.00 USD | 15,660,000.00 USD | 191,180.00 USD | 61,550.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0838` | 1,570.00 USD | 41,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0838` | 15,930,000.00 USD | 15,930,000.00 USD | 145,530.00 USD | 76,380.00 USD | 48,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0839` | 16,000,000.00 USD | 16,000,000.00 USD | 67,620.00 USD | 0.00 USD | 639.31 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0839` | 104.69 USD | 41,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0840` | 16,050,000.00 USD | 16,050,000.00 USD | 35,250.00 USD | 15,480.00 USD | 584.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0840` | 17,520.00 USD | 58,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0841` | 16,090,000.00 USD | 16,090,000.00 USD | 32,120.00 USD | 2,010.00 USD | 709.20 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0842` | 9,530.00 USD | 68,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0842` | 16,160,000.00 USD | 16,160,000.00 USD | 30,040.00 USD | 0.00 USD | 47,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0843` | 104.72 USD | 68,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0843` | 16,200,000.00 USD | 16,200,000.00 USD | 34,480.00 USD | 0.00 USD | 1,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0844` | 16,280,000.00 USD | 16,280,000.00 USD | 78,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0845` | 16,290,000.00 USD | 16,290,000.00 USD | 15,700.00 USD | 0.00 USD | 320.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0846` | 16,380,000.00 USD | 16,380,000.00 USD | 71,250.00 USD | 16,670.00 USD | 75.71 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0847` | 213.74 USD | 68,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0847` | 16,390,000.00 USD | 16,390,000.00 USD | 12,740.00 USD | 0.00 USD | 284.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0848` | 16,420,000.00 USD | 16,420,000.00 USD | 20,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0849` | 16,430,000.00 USD | 16,430,000.00 USD | 11,280.00 USD | 0.00 USD | 292.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0850` | 16,450,000.00 USD | 16,450,000.00 USD | 22,320.00 USD | 0.00 USD | 413.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0851` | 214.75 USD | 68,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0851` | 16,490,000.00 USD | 16,490,000.00 USD | 26,040.00 USD | 11,000.00 USD | 750.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0852` | 16,490,000.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 304.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0853` | 16,500,000.00 USD | 16,500,000.00 USD | 12,910.00 USD | 737.47 USD | 212.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0854` | 16,560,000.00 USD | 16,560,000.00 USD | 35,960.00 USD | 13,190.00 USD | 10,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0855` | 16,710,000.00 USD | 16,710,000.00 USD | 64,150.00 USD | 45,460.00 USD | 36,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0856` | 16,850,000.00 USD | 16,850,000.00 USD | 92,490.00 USD | 32,810.00 USD | 19,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0857` | 16,950,000.00 USD | 16,950,000.00 USD | 50,540.00 USD | 18,030.00 USD | 27,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0858` | 17,030,000.00 USD | 17,030,000.00 USD | 48,130.00 USD | 36,780.00 USD | 164.89 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0858` | 115.30 USD | 69,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0859` | 17,170,000.00 USD | 17,170,000.00 USD | 72,260.00 USD | 20,870.00 USD | 40,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0860` | 17,250,000.00 USD | 17,250,000.00 USD | 44,920.00 USD | 22,170.00 USD | 20,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0861` | 17,310,000.00 USD | 17,310,000.00 USD | 20,430.00 USD | 0.00 USD | 32,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0862` | 17,380,000.00 USD | 17,380,000.00 USD | 33,780.00 USD | 29,080.00 USD | 11,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0862` | 2,340.00 USD | 71,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0863` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 0.00 USD | 219.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0864` | 17,430,000.00 USD | 17,430,000.00 USD | 22,510.00 USD | 20,050.00 USD | 5,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0865` | 17,480,000.00 USD | 17,480,000.00 USD | 31,770.00 USD | 1,280.00 USD | 18,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0866` | 17,540,000.00 USD | 17,540,000.00 USD | 25,410.00 USD | 16,310.00 USD | 19,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0867` | 17,620,000.00 USD | 17,620,000.00 USD | 24,580.00 USD | 37,120.00 USD | 14,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0868` | 17,670,000.00 USD | 17,670,000.00 USD | 8,080.00 USD | 9,300.00 USD | 34,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0869` | 17,720,000.00 USD | 17,720,000.00 USD | 16,230.00 USD | 8,560.00 USD | 24,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0870` | 17,780,000.00 USD | 17,780,000.00 USD | 50,000.00 USD | 12,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0871` | 17,920,000.00 USD | 17,920,000.00 USD | 28,210.00 USD | 45,410.00 USD | 62,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0872` | 17,980,000.00 USD | 17,980,000.00 USD | 26,980.00 USD | 32,280.00 USD | 8,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0873` | 18,030,000.00 USD | 18,030,000.00 USD | 9,490.00 USD | 1,820.00 USD | 36,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0875` | 18,060,000.00 USD | 18,060,000.00 USD | 13,160.00 USD | 17,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0876` | 9,620.00 USD | 81,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0876` | 18,130,000.00 USD | 18,130,000.00 USD | 29,600.00 USD | 26,100.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0877` | 18,180,000.00 USD | 18,180,000.00 USD | 22,320.00 USD | 11,700.00 USD | 21,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0878` | 18,340,000.00 USD | 18,340,000.00 USD | 63,040.00 USD | 41,450.00 USD | 50,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0879` | 18,370,000.00 USD | 18,370,000.00 USD | 15,840.00 USD | 9,450.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0880` | 18,470,000.00 USD | 18,470,000.00 USD | 48,000.00 USD | 15,600.00 USD | 31,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0881` | 465.17 USD | 81,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.0881` | 18,530,000.00 USD | 18,530,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0882` | 18,600,000.00 USD | 18,600,000.00 USD | 25,340.00 USD | 15,630.00 USD | 27,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0883` | 18,710,000.00 USD | 18,710,000.00 USD | 22,710.00 USD | 73,610.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.0884` | 18,800,000.00 USD | 18,800,000.00 USD | 7,860.00 USD | 0.00 USD | 83,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0884` | 38,190,000.00 USD | 38,190,000.00 USD | 99,540.00 USD | 15,290.00 USD | 154,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0886` | 38,290,000.00 USD | 38,290,000.00 USD | 67,460.00 USD | 27,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0887` | 411.53 USD | 81,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0888` | 38,330,000.00 USD | 38,330,000.00 USD | 39,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.0890` | 38,330,000.00 USD | 38,330,000.00 USD | 6,350.00 USD | 0.00 USD | 277.28 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0891` | 418.80 USD | 82,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0892` | 38,410,000.00 USD | 38,410,000.00 USD | 43,710.00 USD | 0.00 USD | 31,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0892` | 106.21 USD | 82,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0895` | 285.70 USD | 82,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0900` | 226.85 USD | 82,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.0900` | 38,410,000.00 USD | 38,410,000.00 USD | 2,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.0902` | 878.67 USD | 83,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0906` | 4,070.00 USD | 87,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0909` | 3,510.00 USD | 91,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0911` | 743.15 USD | 92,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0912` | 4,040.00 USD | 96,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0914` | 171.19 USD | 96,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0917` | 344.43 USD | 96,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0921` | 171.49 USD | 96,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0927` | 188.75 USD | 97,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0935` | 3,300.00 USD | 100,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0949` | 573.84 USD | 100,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0950` | 13,800.00 USD | 114,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0951` | 114,180.00 USD | 228,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0959` | 747.55 USD | 229,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0961` | 609.59 USD | 230,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0965` | 48,270.00 USD | 278,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0979` | 39,190.00 USD | 317,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0983` | 477.50 USD | 318,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.0984` | 10,510.00 USD | 328,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1001` | 1,280.00 USD | 330,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1014` | 8,630.00 USD | 338,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 2,970.00 USD | 341,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1017` | 178.77 USD | 341,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1018` | 492.85 USD | 342,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1061` | 6,110.00 USD | 348,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1066` | 1,580.00 USD | 349,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1072` | 3,210.00 USD | 353,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1109` | 3,440.00 USD | 356,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1127` | 214.15 USD | 356,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1129` | 142.88 USD | 356,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1130` | 2,370.00 USD | 359,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1187` | 121.85 USD | 359,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1212` | 363.75 USD | 359,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1222` | 796.83 USD | 360,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1255` | 1,520.00 USD | 362,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1268` | 633.75 USD | 362,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1270` | 108.80 USD | 362,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1273` | 486.73 USD | 363,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1286` | 2,690,000.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1296` | 171.66 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1311` | 2,140.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1318` | 102.97 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1338` | 205.31 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1388` | 1,000.00 USD | 3,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1394` | 22,620.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1396` | 1,820.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1404` | 663.63 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1411` | 1,800.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1436` | 677.99 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1436` | 135.03 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1479` | 8,360.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1487` | 393.33 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1489` | 2,380.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1509` | 340.62 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1514` | 56,670.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1515` | 2,010.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1525` | 267.55 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1527` | 389.72 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1535` | 30,270.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1563` | 340.06 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1570` | 4,830.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1570` | 980.15 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0160` | 15,880,000.00 USD | 0.00 USD | 3,930.00 USD | `-79.83%` | `244,573.00` |
| `Live` | `Long` | `0.0163` | 15,870,000.00 USD | 0.00 USD | 187.26 USD | `-79.46%` | `11,453.00` |
| `Live` | `Long` | `0.0164` | 15,870,000.00 USD | 0.00 USD | 407.02 USD | `-79.33%` | `24,743.00` |
| `Live` | `Long` | `0.0165` | 15,870,000.00 USD | 0.00 USD | 5,290.00 USD | `-79.21%` | `319,394.00` |
| `Live` | `Long` | `0.0169` | 15,870,000.00 USD | 0.00 USD | 292.61 USD | `-78.70%` | `17,263.00` |
| `Live` | `Long` | `0.0191` | 15,870,000.00 USD | 0.00 USD | 16,770.00 USD | `-76.07%` | `880,408.00` |
| `Live` | `Long` | `0.0193` | 15,850,000.00 USD | 0.00 USD | 291.59 USD | `-75.69%` | `15,069.00` |
| `Live` | `Long` | `0.0196` | 15,850,000.00 USD | 0.00 USD | 121.33 USD | `-75.44%` | `6,206.00` |
| `Live` | `Long` | `0.0208` | 15,850,000.00 USD | 0.00 USD | 4,660.00 USD | `-73.93%` | `224,650.00` |
| `Live` | `Long` | `0.0209` | 15,840,000.00 USD | 0.00 USD | 296.97 USD | `-73.68%` | `14,175.00` |
| `Live` | `Long` | `0.0210` | 15,840,000.00 USD | 0.00 USD | 295.48 USD | `-73.55%` | `14,037.00` |
| `Live` | `Long` | `0.0211` | 15,840,000.00 USD | 0.00 USD | 423.00 USD | `-73.43%` | `20,000.00` |
| `Live` | `Long` | `0.0232` | 15,840,000.00 USD | 0.00 USD | 4,720.00 USD | `-70.79%` | `202,860.00` |
| `Live` | `Long` | `0.0237` | 15,840,000.00 USD | 0.00 USD | 473.00 USD | `-70.29%` | `20,000.00` |
| `Live` | `Long` | `0.0242` | 15,840,000.00 USD | 0.00 USD | 11,860.00 USD | `-69.66%` | `491,018.00` |
| `Live` | `Long` | `0.0244` | 15,830,000.00 USD | 0.00 USD | 633.16 USD | `-69.28%` | `25,896.00` |
| `Live` | `Long` | `0.0261` | 15,830,000.00 USD | 0.00 USD | 450.41 USD | `-67.14%` | `17,224.00` |
| `Live` | `Long` | `0.0268` | 15,820,000.00 USD | 0.00 USD | 5,540.00 USD | `-66.27%` | `206,497.00` |
| `Live` | `Long` | `0.0270` | 15,820,000.00 USD | 0.00 USD | 740.40 USD | `-66.14%` | `27,473.00` |
| `Live` | `Long` | `0.0278` | 15,820,000.00 USD | 0.00 USD | 1,090.00 USD | `-65.01%` | `39,049.00` |
| `Live` | `Long` | `0.0279` | 15,820,000.00 USD | 0.00 USD | 1,730.00 USD | `-64.88%` | `61,775.00` |
| `Live` | `Long` | `0.0284` | 15,820,000.00 USD | 0.00 USD | 129.22 USD | `-64.25%` | `4,542.00` |
| `Live` | `Long` | `0.0290` | 15,820,000.00 USD | 0.00 USD | 2,320.00 USD | `-63.50%` | `80,000.00` |
| `Live` | `Long` | `0.0299` | 15,810,000.00 USD | 0.00 USD | 162.15 USD | `-62.50%` | `5,432.00` |
| `Live` | `Long` | `0.0301` | 15,810,000.00 USD | 0.00 USD | 4,040.00 USD | `-62.24%` | `134,443.00` |
| `Live` | `Long` | `0.0301` | 15,810,000.00 USD | 0.00 USD | 2,360.00 USD | `-62.12%` | `78,319.00` |
| `Live` | `Long` | `0.0306` | 15,810,000.00 USD | 0.00 USD | 137.41 USD | `-61.62%` | `4,498.00` |
| `Live` | `Long` | `0.0318` | 15,810,000.00 USD | 0.00 USD | 1,510.00 USD | `-60.11%` | `47,501.00` |
| `Live` | `Long` | `0.0321` | 15,810,000.00 USD | 0.00 USD | 688,800.00 USD | `-59.61%` | `21,424,497.00` |
| `Live` | `Long` | `0.0324` | 15,120,000.00 USD | 0.00 USD | 194.34 USD | `-59.23%` | `5,989.00` |
| `Live` | `Long` | `0.0330` | 15,120,000.00 USD | 0.00 USD | 1,650.00 USD | `-58.60%` | `50,000.00` |
| `Live` | `Long` | `0.0331` | 15,110,000.00 USD | 0.00 USD | 149.22 USD | `-58.48%` | `4,515.00` |
| `Live` | `Long` | `0.0338` | 15,110,000.00 USD | 0.00 USD | 1,690.00 USD | `-57.60%` | `50,000.00` |
| `Live` | `Long` | `0.0341` | 15,110,000.00 USD | 0.00 USD | 918.63 USD | `-57.09%` | `26,900.00` |
| `Live` | `Long` | `0.0343` | 15,110,000.00 USD | 0.00 USD | 32,540.00 USD | `-56.97%` | `950,000.00` |
| `Live` | `Long` | `0.0345` | 15,080,000.00 USD | 0.00 USD | 3,110.00 USD | `-56.59%` | `90,000.00` |
| `Live` | `Long` | `0.0350` | 15,080,000.00 USD | 0.00 USD | 17,480.00 USD | `-56.09%` | `500,000.00` |
| `Live` | `Long` | `0.0353` | 15,060,000.00 USD | 0.00 USD | 73,050.00 USD | `-55.59%` | `2,066,606.00` |
| `Live` | `Long` | `0.0355` | 14,990,000.00 USD | 0.00 USD | 4,340.00 USD | `-55.46%` | `122,306.00` |
| `Live` | `Long` | `0.0358` | 14,980,000.00 USD | 0.00 USD | 214.53 USD | `-54.96%` | `5,984.00` |
| `Live` | `Long` | `0.0362` | 14,980,000.00 USD | 0.00 USD | 980.96 USD | `-54.45%` | `27,061.00` |
| `Live` | `Long` | `0.0364` | 14,980,000.00 USD | 0.00 USD | 194.44 USD | `-54.33%` | `5,349.00` |
| `Live` | `Long` | `0.0369` | 14,980,000.00 USD | 0.00 USD | 28,590.00 USD | `-53.70%` | `775,729.00` |
| `Live` | `Long` | `0.0377` | 14,950,000.00 USD | 0.00 USD | 3,810.00 USD | `-52.70%` | `101,126.00` |
| `Live` | `Long` | `0.0381` | 14,950,000.00 USD | 0.00 USD | 246.45 USD | `-52.19%` | `6,477.00` |
| `Live` | `Long` | `0.0386` | 14,950,000.00 USD | 0.00 USD | 121.74 USD | `-51.56%` | `3,158.00` |
| `Live` | `Long` | `0.0387` | 14,950,000.00 USD | 0.00 USD | 928.92 USD | `-51.31%` | `23,972.00` |
| `Live` | `Long` | `0.0391` | 14,950,000.00 USD | 0.00 USD | 981.92 USD | `-50.81%` | `25,081.00` |
| `Live` | `Long` | `0.0393` | 14,950,000.00 USD | 0.00 USD | 221.10 USD | `-50.69%` | `5,633.00` |
| `Live` | `Long` | `0.0394` | 14,940,000.00 USD | 0.00 USD | 104,570.00 USD | `-50.56%` | `2,657,324.00` |
| `Live` | `Long` | `0.0404` | 14,840,000.00 USD | 0.00 USD | 115.12 USD | `-49.18%` | `2,846.00` |
| `Live` | `Long` | `0.0408` | 14,840,000.00 USD | 0.00 USD | 419.28 USD | `-48.80%` | `10,289.00` |
| `Live` | `Long` | `0.0413` | 14,840,000.00 USD | 0.00 USD | 2,070.00 USD | `-48.05%` | `50,080.00` |
| `Live` | `Long` | `0.0415` | 14,840,000.00 USD | 0.00 USD | 252.72 USD | `-47.92%` | `6,097.00` |
| `Live` | `Long` | `0.0415` | 14,840,000.00 USD | 0.00 USD | 1,030.00 USD | `-47.80%` | `24,809.00` |
| `Live` | `Long` | `0.0416` | 14,840,000.00 USD | 0.00 USD | 3,570.00 USD | `-47.67%` | `85,771.00` |
| `Live` | `Long` | `0.0420` | 14,830,000.00 USD | 0.00 USD | 671.41 USD | `-47.29%` | `16,005.00` |
| `Live` | `Long` | `0.0423` | 14,830,000.00 USD | 0.00 USD | 2,090.00 USD | `-46.92%` | `49,468.00` |
| `Live` | `Long` | `0.0423` | 14,830,000.00 USD | 0.00 USD | 59,790.00 USD | `-46.79%` | `1,411,805.00` |
| `Live` | `Long` | `0.0425` | 14,770,000.00 USD | 0.00 USD | 1,070.00 USD | `-46.66%` | `25,181.00` |
| `Live` | `Long` | `0.0425` | 14,770,000.00 USD | 0.00 USD | 1,010.00 USD | `-46.54%` | `23,716.00` |
| `Live` | `Long` | `0.0427` | 14,770,000.00 USD | 0.00 USD | 3,620.00 USD | `-46.41%` | `84,760.00` |
| `Live` | `Long` | `0.0430` | 14,760,000.00 USD | 0.00 USD | 859.00 USD | `-46.04%` | `20,000.00` |
| `Live` | `Long` | `0.0432` | 14,760,000.00 USD | 0.00 USD | 6,430.00 USD | `-45.66%` | `148,704.00` |
| `Live` | `Long` | `0.0433` | 14,760,000.00 USD | 0.00 USD | 2,450.00 USD | `-45.53%` | `56,456.00` |
| `Live` | `Long` | `0.0439` | 14,750,000.00 USD | 0.00 USD | 1,610.00 USD | `-44.91%` | `36,807.00` |
| `Live` | `Long` | `0.0440` | 14,750,000.00 USD | 0.00 USD | 750.58 USD | `-44.78%` | `17,078.00` |
| `Live` | `Long` | `0.0440` | 14,750,000.00 USD | 0.00 USD | 1,060.00 USD | `-44.65%` | `24,073.00` |
| `Live` | `Long` | `0.0444` | 14,750,000.00 USD | 0.00 USD | 101,440.00 USD | `-44.28%` | `2,287,370.00` |
| `Live` | `Long` | `0.0447` | 14,650,000.00 USD | 0.00 USD | 444.76 USD | `-43.90%` | `9,961.00` |
| `Live` | `Long` | `0.0447` | 14,650,000.00 USD | 0.00 USD | 248.63 USD | `-43.78%` | `5,556.00` |
| `Live` | `Long` | `0.0454` | 14,650,000.00 USD | 0.00 USD | 2,170.00 USD | `-42.90%` | `47,847.00` |
| `Live` | `Long` | `0.0456` | 14,650,000.00 USD | 0.00 USD | 32,650.00 USD | `-42.77%` | `716,802.00` |
| `Live` | `Long` | `0.0457` | 14,610,000.00 USD | 0.00 USD | 5,470.00 USD | `-42.52%` | `119,571.00` |
| `Live` | `Long` | `0.0461` | 14,610,000.00 USD | 0.00 USD | 4,500.00 USD | `-42.14%` | `97,667.00` |
| `Live` | `Long` | `0.0461` | 14,600,000.00 USD | 0.00 USD | 114.36 USD | `-42.02%` | `2,478.00` |
| `Live` | `Long` | `0.0464` | 14,600,000.00 USD | 0.00 USD | 2,650.00 USD | `-41.76%` | `57,146.00` |
| `Live` | `Long` | `0.0464` | 14,600,000.00 USD | 0.00 USD | 16,780.00 USD | `-41.64%` | `361,202.00` |
| `Live` | `Long` | `0.0466` | 14,580,000.00 USD | 0.00 USD | 109.49 USD | `-41.39%` | `2,347.00` |
| `Live` | `Long` | `0.0473` | 14,580,000.00 USD | 0.00 USD | 18,360.00 USD | `-40.63%` | `388,542.00` |
| `Live` | `Long` | `0.0474` | 14,570,000.00 USD | 0.00 USD | 593.13 USD | `-40.38%` | `12,500.00` |
| `Live` | `Long` | `0.0476` | 14,570,000.00 USD | 0.00 USD | 105.02 USD | `-40.13%` | `2,204.00` |
| `Live` | `Long` | `0.0478` | 14,570,000.00 USD | 0.00 USD | 259.23 USD | `-40.01%` | `5,429.00` |
| `Live` | `Long` | `0.0481` | 14,570,000.00 USD | 0.00 USD | 56,440.00 USD | `-39.63%` | `1,174,709.00` |
| `Live` | `Long` | `0.0481` | 14,510,000.00 USD | 0.00 USD | 2,500.00 USD | `-39.50%` | `51,918.00` |
| `Live` | `Long` | `0.0483` | 14,510,000.00 USD | 0.00 USD | 2,280.00 USD | `-39.25%` | `47,258.00` |
| `Live` | `Long` | `0.0485` | 14,500,000.00 USD | 0.00 USD | 1,480.00 USD | `-39.13%` | `30,533.00` |
| `Live` | `Long` | `0.0486` | 14,500,000.00 USD | 0.00 USD | 315.50 USD | `-38.87%` | `6,485.00` |
| `Live` | `Long` | `0.0488` | 14,500,000.00 USD | 0.00 USD | 1,280.00 USD | `-38.62%` | `26,109.00` |
| `Live` | `Long` | `0.0490` | 14,500,000.00 USD | 0.00 USD | 5,470.00 USD | `-38.50%` | `111,841.00` |
| `Live` | `Long` | `0.0491` | 14,500,000.00 USD | 0.00 USD | 1,080.00 USD | `-38.37%` | `21,989.00` |
| `Live` | `Long` | `0.0493` | 14,490,000.00 USD | 0.00 USD | 1,420.00 USD | `-38.00%` | `28,854.00` |
| `Live` | `Long` | `0.0495` | 14,490,000.00 USD | 0.00 USD | 340.41 USD | `-37.87%` | `6,884.00` |
| `Live` | `Long` | `0.0495` | 14,490,000.00 USD | 0.00 USD | 18,690.00 USD | `-37.74%` | `377,099.00` |
| `Live` | `Long` | `0.0498` | 14,470,000.00 USD | 0.00 USD | 253.82 USD | `-37.49%` | `5,102.00` |
| `Live` | `Long` | `0.0500` | 14,470,000.00 USD | 0.00 USD | 501.50 USD | `-37.12%` | `10,020.00` |
| `Live` | `Long` | `0.0502` | 14,470,000.00 USD | 0.00 USD | 384.95 USD | `-36.99%` | `7,676.00` |
| `Live` | `Long` | `0.0503` | 14,470,000.00 USD | 0.00 USD | 5,410.00 USD | `-36.86%` | `107,572.00` |
| `Live` | `Long` | `0.0503` | 14,470,000.00 USD | 0.00 USD | 1,330.00 USD | `-36.74%` | `26,380.00` |
| `Live` | `Long` | `0.0505` | 14,470,000.00 USD | 0.00 USD | 646.42 USD | `-36.61%` | `12,813.00` |
| `Live` | `Long` | `0.0507` | 14,470,000.00 USD | 0.00 USD | 1,040.00 USD | `-36.36%` | `20,518.00` |
| `Live` | `Long` | `0.0508` | 14,460,000.00 USD | 0.00 USD | 5,350.00 USD | `-36.24%` | `105,363.00` |
| `Live` | `Long` | `0.0510` | 14,460,000.00 USD | 0.00 USD | 535.43 USD | `-35.99%` | `10,509.00` |
| `Live` | `Long` | `0.0510` | 14,460,000.00 USD | 0.00 USD | 566.65 USD | `-35.86%` | `11,100.00` |
| `Live` | `Long` | `0.0512` | 14,460,000.00 USD | 0.00 USD | 11,000.00 USD | `-35.73%` | `215,121.00` |
| `Live` | `Long` | `0.0512` | 14,450,000.00 USD | 0.00 USD | 1,490.00 USD | `-35.61%` | `29,005.00` |
| `Live` | `Long` | `0.0513` | 14,450,000.00 USD | 0.00 USD | 385.13 USD | `-35.48%` | `7,500.00` |
| `Live` | `Long` | `0.0515` | 14,450,000.00 USD | 0.00 USD | 308.55 USD | `-35.36%` | `5,997.00` |
| `Live` | `Long` | `0.0515` | 14,450,000.00 USD | 0.00 USD | 296.26 USD | `-35.23%` | `5,747.00` |
| `Live` | `Long` | `0.0519` | 14,440,000.00 USD | 0.00 USD | 51,690.00 USD | `-34.85%` | `996,821.00` |
| `Live` | `Long` | `0.0520` | 14,390,000.00 USD | 0.00 USD | 1,480.00 USD | `-34.73%` | `28,553.00` |
| `Live` | `Long` | `0.0520` | 14,390,000.00 USD | 0.00 USD | 3,990.00 USD | `-34.60%` | `76,663.00` |
| `Live` | `Long` | `0.0522` | 14,390,000.00 USD | 0.00 USD | 275,090.00 USD | `-34.35%` | `5,264,820.00` |
| `Live` | `Long` | `0.0524` | 14,110,000.00 USD | 0.00 USD | 1,170.00 USD | `-34.10%` | `22,383.00` |
| `Live` | `Long` | `0.0525` | 14,110,000.00 USD | 0.00 USD | 5,640.00 USD | `-33.97%` | `107,299.00` |
| `Live` | `Long` | `0.0527` | 14,110,000.00 USD | 0.00 USD | 395.09 USD | `-33.85%` | `7,504.00` |
| `Live` | `Long` | `0.0527` | 14,110,000.00 USD | 0.00 USD | 2,110.00 USD | `-33.72%` | `40,035.00` |
| `Live` | `Long` | `0.0529` | 14,100,000.00 USD | 0.00 USD | 1,260.00 USD | `-33.60%` | `23,863.00` |
| `Live` | `Long` | `0.0529` | 14,100,000.00 USD | 0.00 USD | 181,690.00 USD | `-33.47%` | `3,431,434.00` |
| `Live` | `Long` | `0.0532` | 13,920,000.00 USD | 0.00 USD | 8,770.00 USD | `-33.22%` | `165,000.00` |
| `Live` | `Long` | `0.0534` | 13,910,000.00 USD | 0.00 USD | 314,750.00 USD | `-32.84%` | `5,888,653.00` |
| `Live` | `Long` | `0.0536` | 13,600,000.00 USD | 0.00 USD | 1,690.00 USD | `-32.72%` | `31,629.00` |
| `Live` | `Long` | `0.0539` | 13,600,000.00 USD | 0.00 USD | 5,290.00 USD | `-32.22%` | `98,005.00` |
| `Live` | `Long` | `0.0541` | 13,590,000.00 USD | 0.00 USD | 2,290.00 USD | `-32.09%` | `42,349.00` |
| `Live` | `Long` | `0.0541` | 13,590,000.00 USD | 0.00 USD | 13,510.00 USD | `-31.96%` | `249,542.00` |
| `Live` | `Long` | `0.0542` | 13,570,000.00 USD | 0.00 USD | 96,530.00 USD | `-31.84%` | `1,779,342.00` |
| `Live` | `Long` | `0.0544` | 13,480,000.00 USD | 0.00 USD | 237.95 USD | `-31.59%` | `4,370.00` |
| `Live` | `Long` | `0.0546` | 13,480,000.00 USD | 0.00 USD | 12,420.00 USD | `-31.46%` | `227,742.00` |
| `Live` | `Long` | `0.0546` | 13,460,000.00 USD | 0.00 USD | 1,420.00 USD | `-31.34%` | `25,899.00` |
| `Live` | `Long` | `0.0548` | 13,460,000.00 USD | 0.00 USD | 188.07 USD | `-31.21%` | `3,435.00` |
| `Live` | `Long` | `0.0556` | 13,460,000.00 USD | 0.00 USD | 907.02 USD | `-30.21%` | `16,328.00` |
| `Live` | `Long` | `0.0561` | 13,460,000.00 USD | 0.00 USD | 39,500.00 USD | `-29.45%` | `703,392.00` |
| `Live` | `Long` | `0.0563` | 13,420,000.00 USD | 0.00 USD | 1,820.00 USD | `-29.33%` | `32,433.00` |
| `Live` | `Long` | `0.0563` | 13,420,000.00 USD | 0.00 USD | 47,560.00 USD | `-29.20%` | `844,065.00` |
| `Live` | `Long` | `0.0566` | 13,370,000.00 USD | 0.00 USD | 131.48 USD | `-28.95%` | `2,325.00` |
| `Live` | `Long` | `0.0566` | 13,370,000.00 USD | 0.00 USD | 610.80 USD | `-28.82%` | `10,782.00` |
| `Live` | `Long` | `0.0568` | 13,370,000.00 USD | 0.00 USD | 747.06 USD | `-28.70%` | `13,164.00` |
| `Live` | `Long` | `0.0570` | 13,370,000.00 USD | 0.00 USD | 421.03 USD | `-28.45%` | `7,393.00` |
| `Live` | `Long` | `0.0570` | 13,370,000.00 USD | 0.00 USD | 8,350.00 USD | `-28.32%` | `146,318.00` |
| `Live` | `Long` | `0.0571` | 13,360,000.00 USD | 0.00 USD | 644.99 USD | `-28.20%` | `11,286.00` |
| `Live` | `Long` | `0.0573` | 13,360,000.00 USD | 0.00 USD | 3,910.00 USD | `-27.94%` | `68,249.00` |
| `Live` | `Long` | `0.0575` | 13,360,000.00 USD | 0.00 USD | 15,970.00 USD | `-27.82%` | `277,921.00` |
| `Live` | `Long` | `0.0575` | 13,340,000.00 USD | 0.00 USD | 3,590.00 USD | `-27.69%` | `62,330.00` |
| `Live` | `Long` | `0.0576` | 13,340,000.00 USD | 0.00 USD | 10,990.00 USD | `-27.57%` | `190,602.00` |
| `Live` | `Long` | `0.0578` | 13,330,000.00 USD | 0.00 USD | 17,890.00 USD | `-27.44%` | `309,753.00` |
| `Live` | `Long` | `0.0578` | 13,310,000.00 USD | 0.00 USD | 5,710,000.00 USD | `-27.32%` | `98,734,536.00` |
| `Live` | `Long` | `0.0580` | 7,600,000.00 USD | 0.00 USD | 431.14 USD | `-27.06%` | `7,427.00` |
| `Live` | `Long` | `0.0582` | 7,600,000.00 USD | 0.00 USD | 447.17 USD | `-26.94%` | `7,690.00` |
| `Live` | `Long` | `0.0583` | 7,600,000.00 USD | 0.00 USD | 116.82 USD | `-26.69%` | `2,002.00` |
| `Live` | `Long` | `0.0585` | 7,600,000.00 USD | 0.00 USD | 172.78 USD | `-26.44%` | `2,951.00` |
| `Live` | `Long` | `0.0587` | 7,600,000.00 USD | 0.00 USD | 9,120.00 USD | `-26.19%` | `155,271.00` |
| `Live` | `Long` | `0.0588` | 7,590,000.00 USD | 0.00 USD | 715.85 USD | `-26.06%` | `12,164.00` |
| `Live` | `Long` | `0.0590` | 7,590,000.00 USD | 0.00 USD | 212.22 USD | `-25.93%` | `3,600.00` |
| `Live` | `Long` | `0.0592` | 7,590,000.00 USD | 0.00 USD | 26,980.00 USD | `-25.68%` | `456,145.00` |
| `Live` | `Long` | `0.0593` | 7,560,000.00 USD | 0.00 USD | 889.30 USD | `-25.43%` | `14,984.00` |
| `Live` | `Long` | `0.0595` | 7,560,000.00 USD | 0.00 USD | 3,660.00 USD | `-25.31%` | `61,626.00` |
| `Live` | `Long` | `0.0595` | 7,560,000.00 USD | 0.00 USD | 2,650.00 USD | `-25.18%` | `44,458.00` |
| `Live` | `Long` | `0.0599` | 7,550,000.00 USD | 0.00 USD | 4,560.00 USD | `-24.80%` | `76,220.00` |
| `Live` | `Long` | `0.0600` | 7,550,000.00 USD | 0.00 USD | 380.38 USD | `-24.68%` | `6,345.00` |
| `Live` | `Long` | `0.0600` | 7,550,000.00 USD | 0.00 USD | 11,540.00 USD | `-24.55%` | `192,164.00` |
| `Live` | `Long` | `0.0602` | 7,540,000.00 USD | 0.00 USD | 8,490.00 USD | `-24.43%` | `141,093.00` |
| `Live` | `Long` | `0.0604` | 7,530,000.00 USD | 0.00 USD | 737.18 USD | `-24.17%` | `12,215.00` |
| `Live` | `Long` | `0.0604` | 7,530,000.00 USD | 0.00 USD | 2,730.00 USD | `-24.05%` | `45,226.00` |
| `Live` | `Long` | `0.0605` | 7,520,000.00 USD | 0.00 USD | 32,090.00 USD | `-23.92%` | `530,006.00` |
| `Live` | `Long` | `0.0607` | 7,490,000.00 USD | 0.00 USD | 1,080.00 USD | `-23.80%` | `17,849.00` |
| `Live` | `Long` | `0.0607` | 7,490,000.00 USD | 0.00 USD | 1,220.00 USD | `-23.67%` | `20,080.00` |
| `Live` | `Long` | `0.0609` | 7,490,000.00 USD | 0.00 USD | 717.73 USD | `-23.55%` | `11,795.00` |
| `Live` | `Long` | `0.0609` | 7,490,000.00 USD | 0.00 USD | 2,220.00 USD | `-23.42%` | `36,478.00` |
| `Live` | `Long` | `0.0612` | 7,490,000.00 USD | 0.00 USD | 913.21 USD | `-23.17%` | `14,934.00` |
| `Live` | `Long` | `0.0612` | 7,490,000.00 USD | 0.00 USD | 298.17 USD | `-23.04%` | `4,868.00` |
| `Live` | `Long` | `0.0614` | 7,490,000.00 USD | 0.00 USD | 655.16 USD | `-22.92%` | `10,679.00` |
| `Live` | `Long` | `0.0614` | 7,490,000.00 USD | 0.00 USD | 368.58 USD | `-22.79%` | `5,998.00` |
| `Live` | `Long` | `0.0616` | 7,480,000.00 USD | 0.00 USD | 1,400.00 USD | `-22.67%` | `22,725.00` |
| `Live` | `Long` | `0.0617` | 7,480,000.00 USD | 0.00 USD | 13,460.00 USD | `-22.54%` | `218,374.00` |
| `Live` | `Long` | `0.0617` | 7,470,000.00 USD | 0.00 USD | 158.08 USD | `-22.42%` | `2,560.00` |
| `Live` | `Long` | `0.0621` | 7,470,000.00 USD | 0.00 USD | 26,790.00 USD | `-22.04%` | `431,787.00` |
| `Live` | `Long` | `0.0622` | 7,440,000.00 USD | 0.00 USD | 1,820.00 USD | `-21.79%` | `29,227.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 1,900.00 USD | `-21.66%` | `30,433.00` |
| `Live` | `Long` | `0.0624` | 7,440,000.00 USD | 0.00 USD | 3,470.00 USD | `-21.54%` | `55,505.00` |
| `Live` | `Long` | `0.0625` | 7,440,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-21.41%` | `17,642,013.00` |
| `Live` | `Long` | `0.0626` | 6,330,000.00 USD | 0.00 USD | 3,900.00 USD | `-21.29%` | `62,300.00` |
| `Live` | `Long` | `0.0628` | 6,330,000.00 USD | 0.00 USD | 461.78 USD | `-21.16%` | `7,359.00` |
| `Live` | `Long` | `0.0629` | 6,330,000.00 USD | 0.00 USD | 6,400.00 USD | `-21.03%` | `101,900.00` |
| `Live` | `Long` | `0.0630` | 6,320,000.00 USD | 0.00 USD | 255.95 USD | `-20.91%` | `4,066.00` |
| `Live` | `Long` | `0.0630` | 6,320,000.00 USD | 0.00 USD | 3,080.00 USD | `-20.78%` | `48,869.00` |
| `Live` | `Long` | `0.0631` | 6,320,000.00 USD | 0.00 USD | 1,100,000.00 USD | `-20.66%` | `17,355,385.00` |
| `Live` | `Long` | `0.0633` | 5,220,000.00 USD | 0.00 USD | 1,210.00 USD | `-20.53%` | `19,161.00` |
| `Live` | `Long` | `0.0634` | 5,220,000.00 USD | 0.00 USD | 12,890.00 USD | `-20.41%` | `203,485.00` |
| `Live` | `Long` | `0.0635` | 5,210,000.00 USD | 0.00 USD | 1,690.00 USD | `-20.28%` | `26,615.00` |
| `Live` | `Long` | `0.0635` | 5,210,000.00 USD | 0.00 USD | 280.95 USD | `-20.15%` | `4,421.00` |
| `Live` | `Long` | `0.0636` | 5,210,000.00 USD | 0.00 USD | 633.38 USD | `-20.03%` | `9,951.00` |
| `Live` | `Long` | `0.0638` | 5,210,000.00 USD | 0.00 USD | 8,670.00 USD | `-19.90%` | `136,018.00` |
| `Live` | `Long` | `0.0639` | 5,200,000.00 USD | 0.00 USD | 23,220.00 USD | `-19.78%` | `363,642.00` |
| `Live` | `Long` | `0.0640` | 5,170,000.00 USD | 0.00 USD | 1,360.00 USD | `-19.65%` | `21,194.00` |
| `Live` | `Long` | `0.0640` | 5,170,000.00 USD | 0.00 USD | 2,170.00 USD | `-19.53%` | `33,802.00` |
| `Live` | `Long` | `0.0641` | 5,170,000.00 USD | 0.00 USD | 633.29 USD | `-19.40%` | `9,872.00` |
| `Live` | `Long` | `0.0643` | 5,170,000.00 USD | 0.00 USD | 9,150.00 USD | `-19.27%` | `142,397.00` |
| `Live` | `Long` | `0.0644` | 5,160,000.00 USD | 0.00 USD | 2,170.00 USD | `-19.15%` | `33,693.00` |
| `Live` | `Long` | `0.0644` | 5,160,000.00 USD | 0.00 USD | 23,930.00 USD | `-19.02%` | `371,302.00` |
| `Live` | `Long` | `0.0646` | 5,130,000.00 USD | 0.00 USD | 6,350.00 USD | `-18.77%` | `98,215.00` |
| `Live` | `Long` | `0.0648` | 5,130,000.00 USD | 0.00 USD | 107,370.00 USD | `-18.65%` | `1,658,260.00` |
| `Live` | `Long` | `0.0649` | 5,020,000.00 USD | 0.00 USD | 10,520.00 USD | `-18.52%` | `162,199.00` |
| `Live` | `Long` | `0.0649` | 5,010,000.00 USD | 0.00 USD | 44,290.00 USD | `-18.40%` | `681,858.00` |
| `Live` | `Long` | `0.0651` | 4,970,000.00 USD | 0.00 USD | 2,380.00 USD | `-18.14%` | `36,466.00` |
| `Live` | `Long` | `0.0653` | 4,960,000.00 USD | 0.00 USD | 13,770.00 USD | `-18.02%` | `210,965.00` |
| `Live` | `Long` | `0.0654` | 4,950,000.00 USD | 0.00 USD | 6,530.00 USD | `-17.89%` | `100,000.00` |
| `Live` | `Long` | `0.0655` | 4,940,000.00 USD | 0.00 USD | 5,340.00 USD | `-17.64%` | `81,453.00` |
| `Live` | `Long` | `0.0658` | 4,940,000.00 USD | 0.00 USD | 71,100.00 USD | `-17.39%` | `1,081,348.00` |
| `Live` | `Long` | `0.0659` | 4,870,000.00 USD | 0.00 USD | 14,870.00 USD | `-17.26%` | `225,881.00` |
| `Live` | `Long` | `0.0659` | 4,850,000.00 USD | 0.00 USD | 11,990.00 USD | `-17.14%` | `181,801.00` |
| `Live` | `Long` | `0.0662` | 4,840,000.00 USD | 0.00 USD | 339.48 USD | `-16.89%` | `5,132.00` |
| `Live` | `Long` | `0.0663` | 4,840,000.00 USD | 0.00 USD | 1,630.00 USD | `-16.76%` | `24,626.00` |
| `Live` | `Long` | `0.0664` | 4,840,000.00 USD | 0.00 USD | 27,760.00 USD | `-16.64%` | `418,455.00` |
| `Live` | `Long` | `0.0664` | 4,810,000.00 USD | 0.00 USD | 1,030.00 USD | `-16.51%` | `15,449.00` |
| `Live` | `Long` | `0.0665` | 4,810,000.00 USD | 0.00 USD | 66,720.00 USD | `-16.39%` | `1,002,594.00` |
| `Live` | `Long` | `0.0667` | 4,740,000.00 USD | 0.00 USD | 34,860.00 USD | `-16.26%` | `523,056.00` |
| `Live` | `Long` | `0.0668` | 4,710,000.00 USD | 0.00 USD | 1,490.00 USD | `-16.13%` | `22,334.00` |
| `Live` | `Long` | `0.0669` | 4,710,000.00 USD | 0.00 USD | 1,020,000.00 USD | `-16.01%` | `15,241,324.00` |
| `Live` | `Long` | `0.0669` | 3,690,000.00 USD | 0.00 USD | 389.18 USD | `-15.88%` | `5,813.00` |
| `Live` | `Long` | `0.0670` | 3,690,000.00 USD | 0.00 USD | 6,240.00 USD | `-15.76%` | `93,089.00` |
| `Live` | `Long` | `0.0672` | 3,680,000.00 USD | 0.00 USD | 899.27 USD | `-15.63%` | `13,392.00` |
| `Live` | `Long` | `0.0673` | 3,680,000.00 USD | 0.00 USD | 196.64 USD | `-15.51%` | `2,924.00` |
| `Live` | `Long` | `0.0673` | 3,680,000.00 USD | 0.00 USD | 96,400.00 USD | `-15.38%` | `1,431,289.00` |
| `Live` | `Long` | `0.0674` | 3,580,000.00 USD | 0.00 USD | 4,860.00 USD | `-15.25%` | `72,079.00` |
| `Live` | `Long` | `0.0675` | 3,580,000.00 USD | 0.00 USD | 310.73 USD | `-15.13%` | `4,600.00` |
| `Live` | `Long` | `0.0677` | 3,580,000.00 USD | 0.00 USD | 8,210.00 USD | `-15.00%` | `121,370.00` |
| `Live` | `Long` | `0.0678` | 3,570,000.00 USD | 0.00 USD | 5,100.00 USD | `-14.88%` | `75,221.00` |
| `Live` | `Long` | `0.0678` | 3,560,000.00 USD | 0.00 USD | 55,180.00 USD | `-14.75%` | `813,258.00` |
| `Live` | `Long` | `0.0679` | 3,510,000.00 USD | 0.00 USD | 20,030.00 USD | `-14.63%` | `294,729.00` |
| `Live` | `Long` | `0.0680` | 3,490,000.00 USD | 0.00 USD | 212.72 USD | `-14.50%` | `3,126.00` |
| `Live` | `Long` | `0.0682` | 3,490,000.00 USD | 0.00 USD | 1,680.00 USD | `-14.37%` | `24,721.00` |
| `Live` | `Long` | `0.0683` | 3,490,000.00 USD | 0.00 USD | 6,220.00 USD | `-14.25%` | `91,110.00` |
| `Live` | `Long` | `0.0683` | 3,480,000.00 USD | 0.00 USD | 1,290.00 USD | `-14.12%` | `18,879.00` |
| `Live` | `Long` | `0.0684` | 3,480,000.00 USD | 0.00 USD | 88,260.00 USD | `-14.00%` | `1,289,438.00` |
| `Live` | `Long` | `0.0685` | 3,390,000.00 USD | 0.00 USD | 4,690.00 USD | `-13.87%` | `68,414.00` |
| `Live` | `Long` | `0.0687` | 3,390,000.00 USD | 0.00 USD | 1,410.00 USD | `-13.75%` | `20,568.00` |
| `Live` | `Long` | `0.0688` | 3,390,000.00 USD | 0.00 USD | 69,020.00 USD | `-13.62%` | `1,003,929.00` |
| `Live` | `Long` | `0.0688` | 3,320,000.00 USD | 0.00 USD | 517.48 USD | `-13.50%` | `7,516.00` |
| `Live` | `Long` | `0.0689` | 3,320,000.00 USD | 0.00 USD | 507,660.00 USD | `-13.37%` | `7,362,765.00` |
| `Live` | `Long` | `0.0691` | 2,810,000.00 USD | 0.00 USD | 3,670.00 USD | `-13.24%` | `53,108.00` |
| `Live` | `Long` | `0.0692` | 2,800,000.00 USD | 0.00 USD | 8,350.00 USD | `-13.12%` | `120,766.00` |
| `Live` | `Long` | `0.0693` | 2,800,000.00 USD | 0.00 USD | 52,390.00 USD | `-12.87%` | `755,504.00` |
| `Live` | `Long` | `0.0694` | 2,740,000.00 USD | 0.00 USD | 4,840.00 USD | `-12.74%` | `69,669.00` |
| `Live` | `Long` | `0.0696` | 2,740,000.00 USD | 0.00 USD | 106,510.00 USD | `-12.62%` | `1,531,348.00` |
| `Live` | `Long` | `0.0697` | 2,630,000.00 USD | 0.00 USD | 5,240.00 USD | `-12.49%` | `75,229.00` |
| `Live` | `Long` | `0.0698` | 2,630,000.00 USD | 0.00 USD | 3,420.00 USD | `-12.36%` | `49,047.00` |
| `Live` | `Long` | `0.0698` | 2,620,000.00 USD | 0.00 USD | 3,630.00 USD | `-12.24%` | `51,974.00` |
| `Live` | `Long` | `0.0699` | 2,620,000.00 USD | 0.00 USD | 9,500.00 USD | `-12.11%` | `135,877.00` |
| `Live` | `Long` | `0.0701` | 2,610,000.00 USD | 0.00 USD | 264.58 USD | `-11.99%` | `3,777.00` |
| `Live` | `Long` | `0.0702` | 2,610,000.00 USD | 0.00 USD | 1,590.00 USD | `-11.86%` | `22,683.00` |
| `Live` | `Long` | `0.0703` | 2,610,000.00 USD | 0.00 USD | 2,000.00 USD | `-11.74%` | `28,486.00` |
| `Live` | `Long` | `0.0703` | 2,610,000.00 USD | 0.00 USD | 5,060.00 USD | `-11.61%` | `71,876.00` |
| `Live` | `Long` | `0.0704` | 2,600,000.00 USD | 0.00 USD | 216.56 USD | `-11.48%` | `3,074.00` |
| `Live` | `Long` | `0.0706` | 2,600,000.00 USD | 0.00 USD | 93,610.00 USD | `-11.36%` | `1,326,872.00` |
| `Live` | `Long` | `0.0707` | 2,510,000.00 USD | 0.00 USD | 536.00 USD | `-11.11%` | `7,576.00` |
| `Live` | `Long` | `0.0711` | 2,510,000.00 USD | 0.00 USD | 111.69 USD | `-10.73%` | `1,572.00` |
| `Live` | `Long` | `0.0712` | 2,510,000.00 USD | 0.00 USD | 2,600.00 USD | `-10.48%` | `36,465.00` |
| `Live` | `Long` | `0.0713` | 2,500,000.00 USD | 0.00 USD | 1,750,000.00 USD | `-10.35%` | `24,460,119.00` |
| `Live` | `Long` | `0.0714` | 759,520.00 USD | 0.00 USD | 2,220.00 USD | `-10.23%` | `31,003.00` |
| `Live` | `Long` | `0.0716` | 757,300.00 USD | 0.00 USD | 8,120.00 USD | `-10.10%` | `113,420.00` |
| `Live` | `Long` | `0.0717` | 749,190.00 USD | 0.00 USD | 560.88 USD | `-9.98%` | `7,828.00` |
| `Live` | `Long` | `0.0717` | 748,630.00 USD | 0.00 USD | 1,520.00 USD | `-9.85%` | `21,127.00` |
| `Live` | `Long` | `0.0718` | 747,110.00 USD | 0.00 USD | 10,850.00 USD | `-9.73%` | `151,060.00` |
| `Live` | `Long` | `0.0720` | 736,260.00 USD | 0.00 USD | 778.93 USD | `-9.60%` | `10,826.00` |
| `Live` | `Long` | `0.0721` | 735,480.00 USD | 0.00 USD | 23,870.00 USD | `-9.47%` | `331,347.00` |
| `Live` | `Long` | `0.0722` | 711,610.00 USD | 0.00 USD | 5,720.00 USD | `-9.22%` | `79,141.00` |
| `Live` | `Long` | `0.0723` | 705,890.00 USD | 0.00 USD | 4,900.00 USD | `-9.10%` | `67,698.00` |
| `Live` | `Long` | `0.0725` | 700,990.00 USD | 0.00 USD | 598.51 USD | `-8.97%` | `8,261.00` |
| `Live` | `Long` | `0.0726` | 700,390.00 USD | 0.00 USD | 260.74 USD | `-8.85%` | `3,594.00` |
| `Live` | `Long` | `0.0727` | 700,130.00 USD | 0.00 USD | 948.37 USD | `-8.72%` | `13,054.00` |
| `Live` | `Long` | `0.0727` | 699,180.00 USD | 0.00 USD | 3,170.00 USD | `-8.60%` | `43,539.00` |
| `Live` | `Long` | `0.0728` | 696,010.00 USD | 0.00 USD | 646.11 USD | `-8.47%` | `8,869.00` |
| `Live` | `Long` | `0.0730` | 695,370.00 USD | 0.00 USD | 72,950.00 USD | `-8.34%` | `1,000,000.00` |
| `Live` | `Long` | `0.0731` | 622,420.00 USD | 0.00 USD | 10,300.00 USD | `-8.22%` | `141,047.00` |
| `Live` | `Long` | `0.0732` | 612,120.00 USD | 0.00 USD | 1,930.00 USD | `-8.09%` | `26,339.00` |
| `Live` | `Long` | `0.0732` | 610,190.00 USD | 0.00 USD | 5,410.00 USD | `-7.97%` | `73,796.00` |
| `Live` | `Long` | `0.0735` | 604,780.00 USD | 0.00 USD | 7,000.00 USD | `-7.72%` | `95,360.00` |
| `Live` | `Long` | `0.0736` | 597,780.00 USD | 0.00 USD | 4,060.00 USD | `-7.59%` | `55,170.00` |
| `Live` | `Long` | `0.0736` | 593,720.00 USD | 0.00 USD | 5,490.00 USD | `-7.46%` | `74,588.00` |
| `Live` | `Long` | `0.0737` | 588,230.00 USD | 0.00 USD | 10,390.00 USD | `-7.34%` | `140,949.00` |
| `Live` | `Long` | `0.0738` | 577,830.00 USD | 0.00 USD | 5,630.00 USD | `-7.21%` | `76,281.00` |
| `Live` | `Long` | `0.0740` | 572,200.00 USD | 0.00 USD | 13,570.00 USD | `-7.09%` | `183,446.00` |
| `Live` | `Long` | `0.0741` | 558,630.00 USD | 0.00 USD | 455,270.00 USD | `-6.96%` | `6,148,098.00` |
| `Live` | `Long` | `0.0741` | 103,370.00 USD | 0.00 USD | 777.39 USD | `-6.84%` | `10,484.00` |
| `Live` | `Long` | `0.0742` | 102,590.00 USD | 0.00 USD | 2,360.00 USD | `-6.71%` | `31,741.00` |
| `Live` | `Long` | `0.0743` | 100,230.00 USD | 0.00 USD | 2,140.00 USD | `-6.58%` | `28,845.00` |
| `Live` | `Long` | `0.0745` | 98,090.00 USD | 0.00 USD | 2,040.00 USD | `-6.46%` | `27,364.00` |
| `Live` | `Long` | `0.0746` | 96,050.00 USD | 0.00 USD | 581.34 USD | `-6.33%` | `7,798.00` |
| `Live` | `Long` | `0.0746` | 95,470.00 USD | 0.00 USD | 1,050.00 USD | `-6.21%` | `14,085.00` |
| `Live` | `Long` | `0.0747` | 94,420.00 USD | 0.00 USD | 359.77 USD | `-6.08%` | `4,813.00` |
| `Live` | `Long` | `0.0750` | 94,060.00 USD | 0.00 USD | 1,370.00 USD | `-5.83%` | `18,241.00` |
| `Live` | `Long` | `0.0751` | 92,690.00 USD | 0.00 USD | 451.13 USD | `-5.71%` | `6,011.00` |
| `Live` | `Long` | `0.0751` | 92,240.00 USD | 0.00 USD | 2,450.00 USD | `-5.58%` | `32,634.00` |
| `Live` | `Long` | `0.0752` | 89,790.00 USD | 0.00 USD | 3,910.00 USD | `-5.45%` | `51,995.00` |
| `Live` | `Long` | `0.0754` | 85,870.00 USD | 0.00 USD | 617.57 USD | `-5.33%` | `8,196.00` |
| `Live` | `Long` | `0.0755` | 85,260.00 USD | 0.00 USD | 4,060.00 USD | `-5.20%` | `53,747.00` |
| `Live` | `Long` | `0.0756` | 81,200.00 USD | 0.00 USD | 12,630.00 USD | `-5.08%` | `167,209.00` |
| `Live` | `Long` | `0.0756` | 68,570.00 USD | 0.00 USD | 356.24 USD | `-4.95%` | `4,709.00` |
| `Live` | `Long` | `0.0757` | 68,210.00 USD | 0.00 USD | 2,510.00 USD | `-4.83%` | `33,158.00` |
| `Live` | `Long` | `0.0759` | 65,700.00 USD | 0.00 USD | 5,070.00 USD | `-4.70%` | `66,803.00` |
| `Live` | `Long` | `0.0760` | 60,630.00 USD | 0.00 USD | 32,080.00 USD | `-4.57%` | `422,343.00` |
| `Live` | `Long` | `0.0761` | 28,560.00 USD | 0.00 USD | 1,690.00 USD | `-4.45%` | `22,243.00` |
| `Live` | `Long` | `0.0761` | 26,870.00 USD | 0.00 USD | 1,130.00 USD | `-4.32%` | `14,810.00` |
| `Live` | `Long` | `0.0762` | 25,740.00 USD | 0.00 USD | 181.93 USD | `-4.20%` | `2,386.00` |
| `Live` | `Long` | `0.0764` | 25,560.00 USD | 0.00 USD | 11,510.00 USD | `-4.07%` | `150,696.00` |
| `Live` | `Long` | `0.0765` | 14,050.00 USD | 0.00 USD | 9,890.00 USD | `-3.95%` | `129,368.00` |
| `Live` | `Long` | `0.0789` | 4,160.00 USD | 0.00 USD | 4,160.00 USD | `-0.93%` | `52,764.00` |
| `Live` | `Short` | `0.0805` | 145.88 USD | 145.88 USD | 0.00 USD | `+1.20%` | `1,811.00` |
| `Live` | `Short` | `0.0818` | 855.96 USD | 710.08 USD | 0.00 USD | `+2.71%` | `8,686.00` |
| `Live` | `Short` | `0.0829` | 28,140.00 USD | 27,290.00 USD | 0.00 USD | `+4.22%` | `328,961.00` |
| `Live` | `Short` | `0.0832` | 39,470.00 USD | 11,330.00 USD | 0.00 USD | `+4.47%` | `136,223.00` |
| `Live` | `Short` | `0.0835` | 39,680.00 USD | 205.70 USD | 0.00 USD | `+4.97%` | `2,462.00` |
| `Live` | `Short` | `0.0837` | 39,690.00 USD | 13.30 USD | 0.00 USD | `+5.10%` | `159.00` |
| `Live` | `Short` | `0.0838` | 41,260.00 USD | 1,570.00 USD | 0.00 USD | `+5.23%` | `18,767.00` |
| `Live` | `Short` | `0.0839` | 41,370.00 USD | 104.69 USD | 0.00 USD | `+5.48%` | `1,247.00` |
| `Live` | `Short` | `0.0840` | 58,880.00 USD | 17,520.00 USD | 0.00 USD | `+5.60%` | `208,401.00` |
| `Live` | `Short` | `0.0842` | 68,420.00 USD | 9,530.00 USD | 0.00 USD | `+5.73%` | `113,306.00` |
| `Live` | `Short` | `0.0843` | 68,520.00 USD | 104.72 USD | 0.00 USD | `+5.85%` | `1,243.00` |
| `Live` | `Short` | `0.0847` | 68,730.00 USD | 213.74 USD | 0.00 USD | `+6.36%` | `2,525.00` |
| `Live` | `Short` | `0.0851` | 68,950.00 USD | 214.75 USD | 0.00 USD | `+6.86%` | `2,525.00` |
| `Live` | `Short` | `0.0858` | 69,060.00 USD | 115.30 USD | 0.00 USD | `+7.86%` | `1,343.00` |
| `Live` | `Short` | `0.0862` | 71,410.00 USD | 2,340.00 USD | 0.00 USD | `+8.37%` | `27,165.00` |
| `Live` | `Short` | `0.0876` | 81,030.00 USD | 9,620.00 USD | 0.00 USD | `+10.00%` | `109,908.00` |
| `Live` | `Short` | `0.0881` | 81,500.00 USD | 465.17 USD | 0.00 USD | `+10.63%` | `5,283.00` |
| `Live` | `Short` | `0.0887` | 81,910.00 USD | 411.53 USD | 0.00 USD | `+11.51%` | `4,637.00` |
| `Live` | `Short` | `0.0891` | 82,330.00 USD | 418.80 USD | 0.00 USD | `+11.88%` | `4,703.00` |
| `Live` | `Short` | `0.0892` | 82,430.00 USD | 106.21 USD | 0.00 USD | `+12.14%` | `1,190.00` |
| `Live` | `Short` | `0.0895` | 82,720.00 USD | 285.70 USD | 0.00 USD | `+12.39%` | `3,194.00` |
| `Live` | `Short` | `0.0900` | 82,940.00 USD | 226.85 USD | 0.00 USD | `+13.02%` | `2,522.00` |
| `Live` | `Short` | `0.0902` | 83,820.00 USD | 878.67 USD | 0.00 USD | `+13.39%` | `9,736.00` |
| `Live` | `Short` | `0.0906` | 87,900.00 USD | 4,070.00 USD | 0.00 USD | `+13.77%` | `45,000.00` |
| `Live` | `Short` | `0.0909` | 91,410.00 USD | 3,510.00 USD | 0.00 USD | `+14.15%` | `38,669.00` |
| `Live` | `Short` | `0.0911` | 92,150.00 USD | 743.15 USD | 0.00 USD | `+14.52%` | `8,153.00` |
| `Live` | `Short` | `0.0912` | 96,200.00 USD | 4,040.00 USD | 0.00 USD | `+14.65%` | `44,324.00` |
| `Live` | `Short` | `0.0914` | 96,370.00 USD | 171.19 USD | 0.00 USD | `+14.77%` | `1,874.00` |
| `Live` | `Short` | `0.0917` | 96,710.00 USD | 344.43 USD | 0.00 USD | `+15.28%` | `3,754.00` |
| `Live` | `Short` | `0.0921` | 96,890.00 USD | 171.49 USD | 0.00 USD | `+15.65%` | `1,863.00` |
| `Live` | `Short` | `0.0927` | 97,070.00 USD | 188.75 USD | 0.00 USD | `+16.53%` | `2,035.00` |
| `Live` | `Short` | `0.0935` | 100,370.00 USD | 3,300.00 USD | 0.00 USD | `+17.41%` | `35,291.00` |
| `Live` | `Short` | `0.0949` | 100,950.00 USD | 573.84 USD | 0.00 USD | `+19.17%` | `6,050.00` |
| `Live` | `Short` | `0.0950` | 114,740.00 USD | 13,800.00 USD | 0.00 USD | `+19.30%` | `145,305.00` |
| `Live` | `Short` | `0.0951` | 228,920.00 USD | 114,180.00 USD | 0.00 USD | `+19.55%` | `1,200,000.00` |
| `Live` | `Short` | `0.0959` | 229,670.00 USD | 747.55 USD | 0.00 USD | `+20.55%` | `7,791.00` |
| `Live` | `Short` | `0.0961` | 230,280.00 USD | 609.59 USD | 0.00 USD | `+20.81%` | `6,340.00` |
| `Live` | `Short` | `0.0965` | 278,560.00 USD | 48,270.00 USD | 0.00 USD | `+21.31%` | `500,000.00` |
| `Live` | `Short` | `0.0979` | 317,750.00 USD | 39,190.00 USD | 0.00 USD | `+22.94%` | `400,522.00` |
| `Live` | `Short` | `0.0983` | 318,220.00 USD | 477.50 USD | 0.00 USD | `+23.44%` | `4,860.00` |
| `Live` | `Short` | `0.0984` | 328,740.00 USD | 10,510.00 USD | 0.00 USD | `+23.69%` | `106,785.00` |
| `Live` | `Short` | `0.1001` | 330,020.00 USD | 1,280.00 USD | 0.00 USD | `+25.71%` | `12,841.00` |
| `Live` | `Short` | `0.1014` | 338,650.00 USD | 8,630.00 USD | 0.00 USD | `+27.46%` | `85,018.00` |
| `Live` | `Short` | `0.1017` | 341,620.00 USD | 2,970.00 USD | 0.00 USD | `+27.72%` | `29,214.00` |
| `Live` | `Short` | `0.1017` | 341,800.00 USD | 178.77 USD | 0.00 USD | `+27.84%` | `1,757.00` |
| `Live` | `Short` | `0.1018` | 342,290.00 USD | 492.85 USD | 0.00 USD | `+27.97%` | `4,839.00` |
| `Live` | `Short` | `0.1061` | 348,400.00 USD | 6,110.00 USD | 0.00 USD | `+33.37%` | `57,554.00` |
| `Live` | `Short` | `0.1066` | 349,980.00 USD | 1,580.00 USD | 0.00 USD | `+34.00%` | `14,835.00` |
| `Live` | `Short` | `0.1072` | 353,190.00 USD | 3,210.00 USD | 0.00 USD | `+34.75%` | `29,960.00` |
| `Live` | `Short` | `0.1109` | 356,630.00 USD | 3,440.00 USD | 0.00 USD | `+39.27%` | `31,000.00` |
| `Live` | `Short` | `0.1127` | 356,840.00 USD | 214.15 USD | 0.00 USD | `+41.54%` | `1,901.00` |
| `Live` | `Short` | `0.1129` | 356,990.00 USD | 142.88 USD | 0.00 USD | `+41.91%` | `1,265.00` |
| `Live` | `Short` | `0.1130` | 359,350.00 USD | 2,370.00 USD | 0.00 USD | `+42.04%` | `20,943.00` |
| `Live` | `Short` | `0.1187` | 359,480.00 USD | 121.85 USD | 0.00 USD | `+49.07%` | `1,027.00` |
| `Live` | `Short` | `0.1212` | 359,840.00 USD | 363.75 USD | 0.00 USD | `+52.34%` | `3,000.00` |
| `Live` | `Short` | `0.1222` | 360,640.00 USD | 796.83 USD | 0.00 USD | `+53.60%` | `6,518.00` |
| `Live` | `Short` | `0.1255` | 362,150.00 USD | 1,520.00 USD | 0.00 USD | `+57.62%` | `12,089.00` |
| `Live` | `Short` | `0.1268` | 362,790.00 USD | 633.75 USD | 0.00 USD | `+59.25%` | `5,000.00` |
| `Live` | `Short` | `0.1270` | 362,900.00 USD | 108.80 USD | 0.00 USD | `+59.50%` | `857.00` |
| `Live` | `Short` | `0.1273` | 363,380.00 USD | 486.73 USD | 0.00 USD | `+60.01%` | `3,822.00` |
| `Live` | `Short` | `0.1286` | 3,050,000.00 USD | 2,690,000.00 USD | 0.00 USD | `+61.64%` | `20,910,149.00` |
| `Live` | `Short` | `0.1296` | 3,050,000.00 USD | 171.66 USD | 0.00 USD | `+62.90%` | `1,324.00` |
| `Live` | `Short` | `0.1311` | 3,060,000.00 USD | 2,140.00 USD | 0.00 USD | `+64.78%` | `16,310.00` |
| `Live` | `Short` | `0.1318` | 3,060,000.00 USD | 102.97 USD | 0.00 USD | `+65.66%` | `781.00` |
| `Live` | `Short` | `0.1338` | 3,060,000.00 USD | 205.31 USD | 0.00 USD | `+68.05%` | `1,535.00` |
| `Live` | `Short` | `0.1388` | 3,060,000.00 USD | 1,000.00 USD | 0.00 USD | `+74.33%` | `7,219.00` |
| `Live` | `Short` | `0.1394` | 3,080,000.00 USD | 22,620.00 USD | 0.00 USD | `+75.21%` | `162,180.00` |
| `Live` | `Short` | `0.1396` | 3,080,000.00 USD | 1,820.00 USD | 0.00 USD | `+75.33%` | `13,010.00` |
| `Live` | `Short` | `0.1404` | 3,080,000.00 USD | 663.63 USD | 0.00 USD | `+76.46%` | `4,725.00` |
| `Live` | `Short` | `0.1411` | 3,080,000.00 USD | 1,800.00 USD | 0.00 USD | `+77.34%` | `12,780.00` |
| `Live` | `Short` | `0.1436` | 3,080,000.00 USD | 677.99 USD | 0.00 USD | `+80.36%` | `4,723.00` |
| `Live` | `Short` | `0.1436` | 3,080,000.00 USD | 135.03 USD | 0.00 USD | `+80.49%` | `940.00` |
| `Live` | `Short` | `0.1479` | 3,090,000.00 USD | 8,360.00 USD | 0.00 USD | `+85.76%` | `56,553.00` |
| `Live` | `Short` | `0.1487` | 3,090,000.00 USD | 393.33 USD | 0.00 USD | `+86.77%` | `2,646.00` |
| `Live` | `Short` | `0.1489` | 3,100,000.00 USD | 2,380.00 USD | 0.00 USD | `+87.14%` | `16,000.00` |
| `Live` | `Short` | `0.1509` | 3,100,000.00 USD | 340.62 USD | 0.00 USD | `+89.53%` | `2,258.00` |
| `Live` | `Short` | `0.1514` | 3,150,000.00 USD | 56,670.00 USD | 0.00 USD | `+90.16%` | `374,415.00` |
| `Live` | `Short` | `0.1515` | 3,150,000.00 USD | 2,010.00 USD | 0.00 USD | `+90.41%` | `13,240.00` |
| `Live` | `Short` | `0.1525` | 3,160,000.00 USD | 267.55 USD | 0.00 USD | `+91.54%` | `1,755.00` |
| `Live` | `Short` | `0.1527` | 3,160,000.00 USD | 389.72 USD | 0.00 USD | `+91.79%` | `2,553.00` |
| `Live` | `Short` | `0.1535` | 3,190,000.00 USD | 30,270.00 USD | 0.00 USD | `+92.92%` | `197,142.00` |
| `Live` | `Short` | `0.1563` | 3,190,000.00 USD | 340.06 USD | 0.00 USD | `+96.44%` | `2,175.00` |
| `Live` | `Short` | `0.1570` | 3,190,000.00 USD | 4,830.00 USD | 0.00 USD | `+97.20%` | `30,755.00` |
| `Live` | `Short` | `0.1570` | 3,190,000.00 USD | 980.15 USD | 0.00 USD | `+97.32%` | `6,241.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0259` | 588,450.00 USD | 0.00 USD | 375.42 USD | `-67.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0401` | 588,070.00 USD | 0.00 USD | 409.59 USD | `-49.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0408` | 587,660.00 USD | 0.00 USD | 132.68 USD | `-48.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0449` | 587,530.00 USD | 0.00 USD | 286.87 USD | `-43.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0464` | 587,240.00 USD | 0.00 USD | 252.42 USD | `-41.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0471` | 586,990.00 USD | 0.00 USD | 468.67 USD | `-40.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0490` | 586,520.00 USD | 0.00 USD | 5,160.00 USD | `-38.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0493` | 581,360.00 USD | 0.00 USD | 920.48 USD | `-38.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0500` | 580,440.00 USD | 0.00 USD | 1,860.00 USD | `-37.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0513` | 578,580.00 USD | 0.00 USD | 175.41 USD | `-35.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0554` | 578,400.00 USD | 0.00 USD | 1,370.00 USD | `-30.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0561` | 577,030.00 USD | 0.00 USD | 437.58 USD | `-29.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0585` | 576,590.00 USD | 0.00 USD | 752.54 USD | `-26.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0590` | 575,840.00 USD | 0.00 USD | 9,830.00 USD | `-25.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0592` | 566,010.00 USD | 0.00 USD | 1,270.00 USD | `-25.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0600` | 564,740.00 USD | 0.00 USD | 1,560.00 USD | `-24.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0602` | 563,180.00 USD | 0.00 USD | 134.12 USD | `-24.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 563,050.00 USD | 0.00 USD | 8,800.00 USD | `-23.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0619` | 554,250.00 USD | 0.00 USD | 504.26 USD | `-22.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0621` | 553,740.00 USD | 0.00 USD | 4,200.00 USD | `-22.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0624` | 549,540.00 USD | 0.00 USD | 1,280.00 USD | `-21.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0640` | 548,260.00 USD | 0.00 USD | 920.18 USD | `-19.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0641` | 547,340.00 USD | 0.00 USD | 370.79 USD | `-19.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0650` | 546,970.00 USD | 0.00 USD | 1,130.00 USD | `-18.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0654` | 545,840.00 USD | 0.00 USD | 362.24 USD | `-17.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 545,480.00 USD | 0.00 USD | 3,140.00 USD | `-17.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 542,340.00 USD | 0.00 USD | 1,200.00 USD | `-17.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0659` | 541,140.00 USD | 0.00 USD | 996.31 USD | `-17.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0669` | 540,140.00 USD | 0.00 USD | 632.88 USD | `-15.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0672` | 539,510.00 USD | 0.00 USD | 115.57 USD | `-15.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 539,400.00 USD | 0.00 USD | 33,620.00 USD | `-15.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0673` | 505,770.00 USD | 0.00 USD | 12,860.00 USD | `-15.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0674` | 492,910.00 USD | 0.00 USD | 1,260.00 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 491,650.00 USD | 0.00 USD | 108.08 USD | `-15.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0677` | 491,540.00 USD | 0.00 USD | 2,960.00 USD | `-15.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0678` | 488,580.00 USD | 0.00 USD | 1,430.00 USD | `-14.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0679` | 487,150.00 USD | 0.00 USD | 7,990.00 USD | `-14.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0680` | 479,160.00 USD | 0.00 USD | 8,580.00 USD | `-14.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0682` | 470,580.00 USD | 0.00 USD | 606.47 USD | `-14.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0688` | 469,970.00 USD | 0.00 USD | 38,710.00 USD | `-13.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0689` | 431,270.00 USD | 0.00 USD | 660.06 USD | `-13.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0692` | 430,610.00 USD | 0.00 USD | 102.34 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 430,510.00 USD | 0.00 USD | 697.50 USD | `-12.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0698` | 429,810.00 USD | 0.00 USD | 699.90 USD | `-12.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0699` | 429,110.00 USD | 0.00 USD | 17,020.00 USD | `-12.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0703` | 412,090.00 USD | 0.00 USD | 895.27 USD | `-11.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0704` | 411,190.00 USD | 0.00 USD | 523.23 USD | `-11.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 410,670.00 USD | 0.00 USD | 235.12 USD | `-11.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0707` | 410,430.00 USD | 0.00 USD | 134.92 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0709` | 410,300.00 USD | 0.00 USD | 107,230.00 USD | `-10.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 303,070.00 USD | 0.00 USD | 12,930.00 USD | `-10.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0712` | 290,140.00 USD | 0.00 USD | 20,070.00 USD | `-10.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0713` | 270,070.00 USD | 0.00 USD | 233.74 USD | `-10.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0714` | 269,840.00 USD | 0.00 USD | 16,880.00 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0717` | 252,960.00 USD | 0.00 USD | 1,670.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0718` | 251,290.00 USD | 0.00 USD | 4,710.00 USD | `-9.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0720` | 246,580.00 USD | 0.00 USD | 15,380.00 USD | `-9.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0721` | 231,190.00 USD | 0.00 USD | 413.42 USD | `-9.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0722` | 230,780.00 USD | 0.00 USD | 703.43 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0723` | 230,080.00 USD | 0.00 USD | 621.12 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0727` | 229,460.00 USD | 0.00 USD | 1,700.00 USD | `-8.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0728` | 227,760.00 USD | 0.00 USD | 29,060.00 USD | `-8.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0730` | 198,700.00 USD | 0.00 USD | 976.95 USD | `-8.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0732` | 197,720.00 USD | 0.00 USD | 2,090.00 USD | `-8.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0733` | 195,630.00 USD | 0.00 USD | 28,750.00 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0736` | 166,880.00 USD | 0.00 USD | 2,710.00 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0737` | 164,170.00 USD | 0.00 USD | 115.12 USD | `-7.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0738` | 164,060.00 USD | 0.00 USD | 4,680.00 USD | `-7.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0740` | 159,380.00 USD | 0.00 USD | 1,640.00 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0742` | 157,740.00 USD | 0.00 USD | 2,900.00 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0743` | 154,840.00 USD | 0.00 USD | 107.66 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0745` | 154,730.00 USD | 0.00 USD | 5,000.00 USD | `-6.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 149,740.00 USD | 0.00 USD | 1,410.00 USD | `-6.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0746` | 148,320.00 USD | 0.00 USD | 375.86 USD | `-6.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0747` | 147,950.00 USD | 0.00 USD | 193.90 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0748` | 147,750.00 USD | 0.00 USD | 140.04 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0750` | 147,610.00 USD | 0.00 USD | 10,030.00 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 137,580.00 USD | 0.00 USD | 323.62 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0751` | 137,260.00 USD | 0.00 USD | 736.17 USD | `-5.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 136,520.00 USD | 0.00 USD | 192.73 USD | `-5.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0756` | 136,330.00 USD | 0.00 USD | 358.13 USD | `-4.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0757` | 135,970.00 USD | 0.00 USD | 4,880.00 USD | `-4.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0759` | 131,090.00 USD | 0.00 USD | 193.49 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0760` | 130,900.00 USD | 0.00 USD | 2,280.00 USD | `-4.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 128,620.00 USD | 0.00 USD | 3,130.00 USD | `-4.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0761` | 125,490.00 USD | 0.00 USD | 806.81 USD | `-4.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0762` | 124,680.00 USD | 0.00 USD | 359.60 USD | `-4.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0765` | 124,320.00 USD | 0.00 USD | 1,320.00 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0766` | 123,000.00 USD | 0.00 USD | 1,130.00 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0766` | 121,870.00 USD | 0.00 USD | 3,540.00 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0767` | 118,330.00 USD | 0.00 USD | 176.91 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0769` | 118,160.00 USD | 0.00 USD | 193.74 USD | `-3.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0770` | 117,960.00 USD | 0.00 USD | 11,510.00 USD | `-3.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0771` | 106,450.00 USD | 0.00 USD | 4,340.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0772` | 102,110.00 USD | 0.00 USD | 4,340.00 USD | `-2.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0774` | 97,780.00 USD | 0.00 USD | 323.40 USD | `-2.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0775` | 97,460.00 USD | 0.00 USD | 2,450.00 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0775` | 95,010.00 USD | 0.00 USD | 604.81 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0776` | 94,400.00 USD | 0.00 USD | 992.37 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0777` | 93,410.00 USD | 0.00 USD | 41,810.00 USD | `-2.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0779` | 51,610.00 USD | 0.00 USD | 17,270.00 USD | `-2.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0780` | 34,340.00 USD | 0.00 USD | 3,000.00 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0780` | 31,330.00 USD | 0.00 USD | 1,700.00 USD | `-1.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0781` | 29,630.00 USD | 0.00 USD | 1,350.00 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0783` | 28,290.00 USD | 0.00 USD | 120.66 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0784` | 28,170.00 USD | 0.00 USD | 4,200.00 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 23,960.00 USD | 0.00 USD | 573.31 USD | `-1.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 23,390.00 USD | 0.00 USD | 166.84 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0786` | 23,220.00 USD | 0.00 USD | 495.57 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0788` | 22,730.00 USD | 0.00 USD | 3,030.00 USD | `-1.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0789` | 19,700.00 USD | 0.00 USD | 497.86 USD | `-0.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0790` | 19,200.00 USD | 0.00 USD | 706.60 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0790` | 18,490.00 USD | 0.00 USD | 10,230.00 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0791` | 8,270.00 USD | 0.00 USD | 4,600.00 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0793` | 3,670.00 USD | 0.00 USD | 2,260.00 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0794` | 1,410.00 USD | 0.00 USD | 1,010.00 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0795` | 397.17 USD | 0.00 USD | 148.25 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0795` | 248.91 USD | 0.00 USD | 248.91 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0796` | 2,130.00 USD | 2,130.00 USD | 0.00 USD | `+0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0798` | 2,480.00 USD | 342.85 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 6,940.00 USD | 4,460.00 USD | 0.00 USD | `+0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0799` | 8,060.00 USD | 1,120.00 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0800` | 12,400.00 USD | 4,350.00 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0801` | 12,850.00 USD | 443.63 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0803` | 13,190.00 USD | 346.04 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 13,330.00 USD | 141.34 USD | 0.00 USD | `+0.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0804` | 14,040.00 USD | 707.08 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0805` | 16,300.00 USD | 2,260.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0806` | 113,080.00 USD | 96,780.00 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0808` | 113,350.00 USD | 264.54 USD | 0.00 USD | `+1.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 115,500.00 USD | 2,160.00 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0809` | 115,930.00 USD | 424.74 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0810` | 116,940.00 USD | 1,010.00 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0811` | 118,320.00 USD | 1,380.00 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0813` | 118,580.00 USD | 264.63 USD | 0.00 USD | `+2.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 120,020.00 USD | 1,430.00 USD | 0.00 USD | `+2.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0814` | 120,510.00 USD | 492.77 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0815` | 121,890.00 USD | 1,380.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0817` | 124,800.00 USD | 2,920.00 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0818` | 134,160.00 USD | 9,360.00 USD | 0.00 USD | `+2.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 137,170.00 USD | 3,010.00 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0819` | 137,710.00 USD | 534.72 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0820` | 138,110.00 USD | 402.62 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0822` | 151,910.00 USD | 13,790.00 USD | 0.00 USD | `+3.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0823` | 155,890.00 USD | 3,980.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 156,400.00 USD | 512.05 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0824` | 157,480.00 USD | 1,080.00 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0825` | 157,870.00 USD | 389.31 USD | 0.00 USD | `+3.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0828` | 158,170.00 USD | 303.56 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0829` | 158,280.00 USD | 112.89 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0830` | 158,670.00 USD | 381.45 USD | 0.00 USD | `+4.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0832` | 158,820.00 USD | 155.82 USD | 0.00 USD | `+4.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 159,220.00 USD | 399.52 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0833` | 159,570.00 USD | 348.82 USD | 0.00 USD | `+4.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0834` | 160,830.00 USD | 1,260.00 USD | 0.00 USD | `+4.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0835` | 161,040.00 USD | 210.88 USD | 0.00 USD | `+4.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,910,000.00 USD | 1,750,000.00 USD | 0.00 USD | `+5.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0838` | 1,920,000.00 USD | 3,380.00 USD | 0.00 USD | `+5.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0839` | 1,920,000.00 USD | 692.34 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0842` | 1,920,000.00 USD | 107.71 USD | 0.00 USD | `+5.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0843` | 1,920,000.00 USD | 2,690.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0844` | 1,920,000.00 USD | 1,330.00 USD | 0.00 USD | `+6.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0846` | 1,920,000.00 USD | 2,360.00 USD | 0.00 USD | `+6.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,920,000.00 USD | 326.97 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0848` | 1,920,000.00 USD | 242.84 USD | 0.00 USD | `+6.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0849` | 1,930,000.00 USD | 10,140.00 USD | 0.00 USD | `+6.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0851` | 1,930,000.00 USD | 152.92 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0852` | 1,940,000.00 USD | 876.11 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0854` | 1,940,000.00 USD | 205.59 USD | 0.00 USD | `+7.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0857` | 1,940,000.00 USD | 126.76 USD | 0.00 USD | `+7.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,940,000.00 USD | 307.41 USD | 0.00 USD | `+7.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0858` | 1,940,000.00 USD | 942.20 USD | 0.00 USD | `+7.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0859` | 1,940,000.00 USD | 644.62 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0861` | 1,940,000.00 USD | 180.45 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,940,000.00 USD | 2,020.00 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0862` | 1,980,000.00 USD | 43,760.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0864` | 1,980,000.00 USD | 164.86 USD | 0.00 USD | `+8.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0866` | 1,980,000.00 USD | 1,080.00 USD | 0.00 USD | `+8.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0869` | 1,990,000.00 USD | 384.06 USD | 0.00 USD | `+9.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0872` | 1,990,000.00 USD | 1,840.00 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0877` | 1,990,000.00 USD | 117.71 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0880` | 1,990,000.00 USD | 111.61 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0881` | 1,990,000.00 USD | 571.18 USD | 0.00 USD | `+10.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0882` | 1,990,000.00 USD | 375.94 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0883` | 1,990,000.00 USD | 627.55 USD | 0.00 USD | `+11.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0885` | 1,990,000.00 USD | 211.04 USD | 0.00 USD | `+11.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0887` | 1,990,000.00 USD | 108.36 USD | 0.00 USD | `+11.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0888` | 1,990,000.00 USD | 543.32 USD | 0.00 USD | `+11.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0890` | 1,990,000.00 USD | 1,820.00 USD | 0.00 USD | `+11.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0891` | 1,990,000.00 USD | 2,080.00 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0892` | 2,010,000.00 USD | 17,680.00 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0893` | 2,010,000.00 USD | 1,810.00 USD | 0.00 USD | `+12.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0896` | 2,010,000.00 USD | 1,640.00 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0900` | 2,020,000.00 USD | 5,340.00 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0901` | 2,020,000.00 USD | 1,090.00 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0905` | 2,020,000.00 USD | 224.86 USD | 0.00 USD | `+13.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0906` | 2,040,000.00 USD | 20,540.00 USD | 0.00 USD | `+13.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0909` | 2,040,000.00 USD | 114.93 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0910` | 2,040,000.00 USD | 840.47 USD | 0.00 USD | `+14.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0911` | 2,040,000.00 USD | 173.36 USD | 0.00 USD | `+14.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0916` | 2,050,000.00 USD | 4,690.00 USD | 0.00 USD | `+15.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0917` | 2,050,000.00 USD | 1,970.00 USD | 0.00 USD | `+15.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0921` | 2,050,000.00 USD | 2,170.00 USD | 0.00 USD | `+15.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0922` | 2,050,000.00 USD | 541.32 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0924` | 2,190,000.00 USD | 137,500.00 USD | 0.00 USD | `+16.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0925` | 2,190,000.00 USD | 691.07 USD | 0.00 USD | `+16.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0926` | 2,200,000.00 USD | 6,250.00 USD | 0.00 USD | `+16.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0927` | 2,210,000.00 USD | 13,480.00 USD | 0.00 USD | `+16.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0930` | 2,210,000.00 USD | 734.82 USD | 0.00 USD | `+16.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0931` | 2,210,000.00 USD | 1,230.00 USD | 0.00 USD | `+17.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0934` | 2,210,000.00 USD | 184.09 USD | 0.00 USD | `+17.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0938` | 2,210,000.00 USD | 1,120.00 USD | 0.00 USD | `+17.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0940` | 2,220,000.00 USD | 1,860.00 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0943` | 2,220,000.00 USD | 512.15 USD | 0.00 USD | `+18.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0945` | 2,220,000.00 USD | 6,620.00 USD | 0.00 USD | `+18.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0948` | 2,220,000.00 USD | 404.96 USD | 0.00 USD | `+19.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0955` | 2,220,000.00 USD | 129.85 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0958` | 2,230,000.00 USD | 3,740.00 USD | 0.00 USD | `+20.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0959` | 2,230,000.00 USD | 2,400.00 USD | 0.00 USD | `+20.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0960` | 2,230,000.00 USD | 409.17 USD | 0.00 USD | `+20.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0966` | 2,230,000.00 USD | 203.74 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0973` | 2,230,000.00 USD | 2,800.00 USD | 0.00 USD | `+22.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0974` | 2,230,000.00 USD | 1,320.00 USD | 0.00 USD | `+22.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0975` | 2,230,000.00 USD | 694.56 USD | 0.00 USD | `+22.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0984` | 2,240,000.00 USD | 940.91 USD | 0.00 USD | `+23.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0989` | 2,240,000.00 USD | 2,980.00 USD | 0.00 USD | `+24.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0990` | 2,240,000.00 USD | 104.99 USD | 0.00 USD | `+24.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0993` | 2,240,000.00 USD | 1,930.00 USD | 0.00 USD | `+24.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0994` | 2,240,000.00 USD | 1,490.00 USD | 0.00 USD | `+24.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0995` | 2,240,000.00 USD | 1,090.00 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0997` | 2,240,000.00 USD | 438.96 USD | 0.00 USD | `+25.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0998` | 2,240,000.00 USD | 973.76 USD | 0.00 USD | `+25.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.0999` | 2,360,000.00 USD | 113,580.00 USD | 0.00 USD | `+25.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1001` | 2,360,000.00 USD | 175.59 USD | 0.00 USD | `+25.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1008` | 2,360,000.00 USD | 588.78 USD | 0.00 USD | `+26.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1009` | 2,360,000.00 USD | 201.90 USD | 0.00 USD | `+26.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1012` | 2,360,000.00 USD | 489.46 USD | 0.00 USD | `+27.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1016` | 2,360,000.00 USD | 103.68 USD | 0.00 USD | `+27.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1018` | 2,360,000.00 USD | 203.70 USD | 0.00 USD | `+27.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1019` | 2,360,000.00 USD | 3,810.00 USD | 0.00 USD | `+28.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1021` | 2,370,000.00 USD | 11,200.00 USD | 0.00 USD | `+28.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1022` | 2,380,000.00 USD | 4,330.00 USD | 0.00 USD | `+28.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1027` | 2,380,000.00 USD | 205.50 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1029` | 2,380,000.00 USD | 1,540.00 USD | 0.00 USD | `+29.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1037` | 2,380,000.00 USD | 207.50 USD | 0.00 USD | `+30.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1042` | 2,380,000.00 USD | 813.88 USD | 0.00 USD | `+30.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1045` | 2,410,000.00 USD | 23,160.00 USD | 0.00 USD | `+31.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1046` | 2,410,000.00 USD | 781.51 USD | 0.00 USD | `+31.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,410,000.00 USD | 209.30 USD | 0.00 USD | `+31.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1047` | 2,410,000.00 USD | 1,440.00 USD | 0.00 USD | `+31.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1051` | 2,410,000.00 USD | 5,140.00 USD | 0.00 USD | `+31.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1053` | 2,410,000.00 USD | 585.32 USD | 0.00 USD | `+32.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1055` | 2,410,000.00 USD | 210.90 USD | 0.00 USD | `+32.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1056` | 2,420,000.00 USD | 1,850.00 USD | 0.00 USD | `+32.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1057` | 2,420,000.00 USD | 105.75 USD | 0.00 USD | `+32.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1060` | 2,420,000.00 USD | 3,220.00 USD | 0.00 USD | `+33.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1062` | 2,420,000.00 USD | 1,600.00 USD | 0.00 USD | `+33.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1065` | 2,420,000.00 USD | 212.90 USD | 0.00 USD | `+33.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1071` | 2,420,000.00 USD | 472.63 USD | 0.00 USD | `+34.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1072` | 2,420,000.00 USD | 214.50 USD | 0.00 USD | `+34.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1077` | 2,420,000.00 USD | 1,040.00 USD | 0.00 USD | `+35.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,420,000.00 USD | 136.12 USD | 0.00 USD | `+35.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1080` | 2,420,000.00 USD | 216.10 USD | 0.00 USD | `+35.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1087` | 2,460,000.00 USD | 40,920.00 USD | 0.00 USD | `+36.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1090` | 2,460,000.00 USD | 217.90 USD | 0.00 USD | `+36.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1099` | 2,460,000.00 USD | 219.70 USD | 0.00 USD | `+38.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1100` | 2,470,000.00 USD | 7,920.00 USD | 0.00 USD | `+38.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1105` | 2,470,000.00 USD | 154.22 USD | 0.00 USD | `+38.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1106` | 2,470,000.00 USD | 221.30 USD | 0.00 USD | `+39.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1108` | 2,470,000.00 USD | 1,050.00 USD | 0.00 USD | `+39.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1110` | 2,500,000.00 USD | 24,440.00 USD | 0.00 USD | `+39.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1115` | 2,500,000.00 USD | 223.10 USD | 0.00 USD | `+40.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1124` | 2,500,000.00 USD | 2,120.00 USD | 0.00 USD | `+41.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1132` | 2,500,000.00 USD | 226.30 USD | 0.00 USD | `+42.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,500,000.00 USD | 351.57 USD | 0.00 USD | `+43.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1139` | 2,500,000.00 USD | 950.34 USD | 0.00 USD | `+43.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1148` | 2,500,000.00 USD | 229.50 USD | 0.00 USD | `+44.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1149` | 2,500,000.00 USD | 771.08 USD | 0.00 USD | `+44.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1154` | 2,500,000.00 USD | 230.90 USD | 0.00 USD | `+45.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1155` | 2,500,000.00 USD | 288.18 USD | 0.00 USD | `+45.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1158` | 2,500,000.00 USD | 619.10 USD | 0.00 USD | `+45.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1159` | 2,500,000.00 USD | 1,250.00 USD | 0.00 USD | `+45.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1161` | 2,510,000.00 USD | 1,050.00 USD | 0.00 USD | `+45.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1162` | 2,510,000.00 USD | 232.30 USD | 0.00 USD | `+45.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1168` | 2,510,000.00 USD | 1,600.00 USD | 0.00 USD | `+46.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1169` | 2,510,000.00 USD | 1,050.00 USD | 0.00 USD | `+46.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1172` | 2,510,000.00 USD | 3,730.00 USD | 0.00 USD | `+47.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1178` | 2,510,000.00 USD | 676.22 USD | 0.00 USD | `+48.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1179` | 2,510,000.00 USD | 648.25 USD | 0.00 USD | `+48.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1181` | 2,520,000.00 USD | 1,510.00 USD | 0.00 USD | `+48.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1182` | 2,520,000.00 USD | 448.52 USD | 0.00 USD | `+48.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1186` | 2,520,000.00 USD | 136.93 USD | 0.00 USD | `+48.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1187` | 2,520,000.00 USD | 433.07 USD | 0.00 USD | `+49.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1191` | 2,520,000.00 USD | 1,050.00 USD | 0.00 USD | `+49.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1197` | 2,520,000.00 USD | 691.80 USD | 0.00 USD | `+50.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1201` | 2,640,000.00 USD | 118,550.00 USD | 0.00 USD | `+50.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1203` | 2,640,000.00 USD | 143.22 USD | 0.00 USD | `+51.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1207` | 2,640,000.00 USD | 803.95 USD | 0.00 USD | `+51.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1211` | 2,640,000.00 USD | 1,380.00 USD | 0.00 USD | `+52.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1220` | 2,640,000.00 USD | 2,270.00 USD | 0.00 USD | `+53.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1224` | 2,640,000.00 USD | 871.99 USD | 0.00 USD | `+53.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1268` | 2,670,000.00 USD | 24,560.00 USD | 0.00 USD | `+59.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1270` | 2,670,000.00 USD | 400.21 USD | 0.00 USD | `+59.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1318` | 2,680,000.00 USD | 13,850.00 USD | 0.00 USD | `+65.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1321` | 2,680,000.00 USD | 2,360.00 USD | 0.00 USD | `+65.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1356` | 2,690,000.00 USD | 4,160.00 USD | 0.00 USD | `+70.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1399` | 2,690,000.00 USD | 235.54 USD | 0.00 USD | `+75.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1414` | 2,690,000.00 USD | 1,160.00 USD | 0.00 USD | `+77.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1421` | 2,690,000.00 USD | 173.57 USD | 0.00 USD | `+78.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1422` | 2,690,000.00 USD | 380.09 USD | 0.00 USD | `+78.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1424` | 2,710,000.00 USD | 17,150.00 USD | 0.00 USD | `+78.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1444` | 2,710,000.00 USD | 433.35 USD | 0.00 USD | `+81.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1469` | 2,710,000.00 USD | 3,640.00 USD | 0.00 USD | `+84.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1477` | 2,770,000.00 USD | 55,720.00 USD | 0.00 USD | `+85.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1482` | 2,770,000.00 USD | 2,120.00 USD | 0.00 USD | `+86.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1499` | 2,790,000.00 USD | 18,810.00 USD | 0.00 USD | `+88.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1532` | 2,790,000.00 USD | 4,750.00 USD | 0.00 USD | `+92.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1552` | 2,790,000.00 USD | 630.53 USD | 0.00 USD | `+94.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1590` | 2,800,000.00 USD | 2,670.00 USD | 0.00 USD | `+99.83%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.0696` | 66,770,000.00 USD | 0.00 USD | 66,770,000.00 USD | 350,400.00 USD | 216,390.00 USD | 299,380.00 USD |
| `7D` | `0.0698` | 65,900,000.00 USD | 0.00 USD | 65,900,000.00 USD | 169,310.00 USD | 191,410.00 USD | 147,730.00 USD |
| `7D` | `0.0700` | 65,390,000.00 USD | 0.00 USD | 65,390,000.00 USD | 260,280.00 USD | 212,380.00 USD | 151,100.00 USD |
| `7D` | `0.0702` | 64,770,000.00 USD | 0.00 USD | 64,770,000.00 USD | 215,900.00 USD | 46,980.00 USD | 104,870.00 USD |
| `7D` | `0.0704` | 64,400,000.00 USD | 0.00 USD | 64,400,000.00 USD | 166,690.00 USD | 78,940.00 USD | 17,990.00 USD |
| `7D` | `0.0706` | 64,140,000.00 USD | 0.00 USD | 64,140,000.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `7D` | `0.0708` | 63,840,000.00 USD | 0.00 USD | 63,840,000.00 USD | 156,500.00 USD | 31,400.00 USD | 107,800.00 USD |
| `1D` | `0.0710` | 23,690,000.00 USD | 0.00 USD | 23,690,000.00 USD | 32,660.00 USD | 46,420.00 USD | 48,880.00 USD |
| `7D` | `0.0710` | 63,550,000.00 USD | 0.00 USD | 63,550,000.00 USD | 229,480.00 USD | 157,140.00 USD | 74,710.00 USD |
| `1D` | `0.0711` | 23,560,000.00 USD | 0.00 USD | 23,560,000.00 USD | 16,230.00 USD | 8,560.00 USD | 24,000.00 USD |
| `1D` | `0.0712` | 23,510,000.00 USD | 0.00 USD | 23,510,000.00 USD | 50,000.00 USD | 12,500.00 USD | 0.00 USD |
| `7D` | `0.0712` | 63,090,000.00 USD | 0.00 USD | 63,090,000.00 USD | 278,270.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0713` | 23,450,000.00 USD | 0.00 USD | 23,450,000.00 USD | 28,210.00 USD | 45,410.00 USD | 62,350.00 USD |
| `1D` | `0.0714` | 23,320,000.00 USD | 0.00 USD | 23,320,000.00 USD | 26,980.00 USD | 32,280.00 USD | 8,650.00 USD |
| `7D` | `0.0714` | 62,580,000.00 USD | 0.00 USD | 62,580,000.00 USD | 236,020.00 USD | 151,040.00 USD | 113,330.00 USD |
| `1D` | `0.0715` | 23,250,000.00 USD | 0.00 USD | 23,250,000.00 USD | 9,490.00 USD | 1,820.00 USD | 36,110.00 USD |
| `1D` | `0.0716` | 23,200,000.00 USD | 0.00 USD | 23,200,000.00 USD | 42,760.00 USD | 43,290.00 USD | 11,490.00 USD |
| `7D` | `0.0716` | 62,080,000.00 USD | 0.00 USD | 62,080,000.00 USD | 315,320.00 USD | 44,250.00 USD | 71,880.00 USD |
| `1D` | `0.0717` | 23,100,000.00 USD | 0.00 USD | 23,100,000.00 USD | 22,320.00 USD | 11,700.00 USD | 21,830.00 USD |
| `1D` | `0.0718` | 23,050,000.00 USD | 0.00 USD | 23,050,000.00 USD | 63,040.00 USD | 41,450.00 USD | 50,850.00 USD |
| `7D` | `0.0718` | 61,650,000.00 USD | 0.00 USD | 61,650,000.00 USD | 221,290.00 USD | 41,090.00 USD | 100,120.00 USD |
| `1D` | `0.0719` | 22,890,000.00 USD | 0.00 USD | 22,890,000.00 USD | 15,840.00 USD | 9,450.00 USD | 7,440.00 USD |
| `1D` | `0.0720` | 22,860,000.00 USD | 0.00 USD | 22,860,000.00 USD | 48,000.00 USD | 15,600.00 USD | 31,960.00 USD |
| `7D` | `0.0720` | 61,290,000.00 USD | 0.00 USD | 61,290,000.00 USD | 277,980.00 USD | 185,970.00 USD | 107,720.00 USD |
| `1D` | `0.0721` | 22,760,000.00 USD | 0.00 USD | 22,760,000.00 USD | 33,000.00 USD | 19,660.00 USD | 12,510.00 USD |
| `1D` | `0.0722` | 22,700,000.00 USD | 0.00 USD | 22,700,000.00 USD | 29,680.00 USD | 15,630.00 USD | 27,970.00 USD |
| `7D` | `0.0722` | 60,720,000.00 USD | 0.00 USD | 60,720,000.00 USD | 205,190.00 USD | 62,150.00 USD | 114,670.00 USD |
| `1D` | `0.0723` | 22,630,000.00 USD | 0.00 USD | 22,630,000.00 USD | 30,830.00 USD | 73,610.00 USD | 7,860.00 USD |
| `1D` | `0.0724` | 22,510,000.00 USD | 0.00 USD | 22,510,000.00 USD | 32,170.00 USD | 17,780.00 USD | 84,070.00 USD |
| `7D` | `0.0724` | 60,340,000.00 USD | 0.00 USD | 60,340,000.00 USD | 312,920.00 USD | 15,290.00 USD | 159,690.00 USD |
| `1D` | `0.0725` | 22,380,000.00 USD | 0.00 USD | 22,380,000.00 USD | 82,840.00 USD | 40,520.00 USD | 32,900.00 USD |
| `1D` | `0.0726` | 22,220,000.00 USD | 0.00 USD | 22,220,000.00 USD | 31,660.00 USD | 0.00 USD | 142.34 USD |
| `7D` | `0.0726` | 59,850,000.00 USD | 0.00 USD | 59,850,000.00 USD | 317,280.00 USD | 116,040.00 USD | 63,820.00 USD |
| `1D` | `0.0727` | 22,190,000.00 USD | 0.00 USD | 22,190,000.00 USD | 20,420.00 USD | 0.00 USD | 200.42 USD |
| `1D` | `0.0728` | 22,170,000.00 USD | 0.00 USD | 22,170,000.00 USD | 15,580.00 USD | 802.30 USD | 419.85 USD |
| `7D` | `0.0728` | 59,350,000.00 USD | 0.00 USD | 59,350,000.00 USD | 195,910.00 USD | 89,490.00 USD | 138,620.00 USD |
| `1D` | `0.0729` | 22,150,000.00 USD | 0.00 USD | 22,150,000.00 USD | 17,820.00 USD | 0.00 USD | 18,720.00 USD |
| `1D` | `0.0730` | 22,120,000.00 USD | 0.00 USD | 22,120,000.00 USD | 14,450.00 USD | 0.00 USD | 223.21 USD |
| `7D` | `0.0730` | 58,930,000.00 USD | 0.00 USD | 58,930,000.00 USD | 214,490.00 USD | 67,400.00 USD | 35,740.00 USD |
| `1D` | `0.0731` | 22,100,000.00 USD | 0.00 USD | 22,100,000.00 USD | 42,980.00 USD | 0.00 USD | 100.25 USD |
| `1D` | `0.0732` | 22,060,000.00 USD | 0.00 USD | 22,060,000.00 USD | 42,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0732` | 58,610,000.00 USD | 0.00 USD | 58,610,000.00 USD | 809,110.00 USD | 656,850.00 USD | 95,700.00 USD |
| `1D` | `0.0733` | 22,020,000.00 USD | 0.00 USD | 22,020,000.00 USD | 11,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0734` | 22,010,000.00 USD | 0.00 USD | 22,010,000.00 USD | 4,580.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0734` | 57,050,000.00 USD | 0.00 USD | 57,050,000.00 USD | 646,280.00 USD | 190,810.00 USD | 58,930.00 USD |
| `1D` | `0.0735` | 22,000,000.00 USD | 0.00 USD | 22,000,000.00 USD | 24,100.00 USD | 0.00 USD | 41.24 USD |
| `1D` | `0.0736` | 21,980,000.00 USD | 0.00 USD | 21,980,000.00 USD | 8,600.00 USD | 0.00 USD | 258.52 USD |
| `7D` | `0.0736` | 56,150,000.00 USD | 0.00 USD | 56,150,000.00 USD | 637,870.00 USD | 489,000.00 USD | 364,800.00 USD |
| `1D` | `0.0737` | 21,970,000.00 USD | 0.00 USD | 21,970,000.00 USD | 45,400.00 USD | 0.00 USD | 475.78 USD |
| `1D` | `0.0738` | 21,920,000.00 USD | 0.00 USD | 21,920,000.00 USD | 29,080.00 USD | 0.00 USD | 162.16 USD |
| `7D` | `0.0738` | 54,660,000.00 USD | 0.00 USD | 54,660,000.00 USD | 742,990.00 USD | 384,950.00 USD | 312,490.00 USD |
| `1D` | `0.0739` | 21,890,000.00 USD | 0.00 USD | 21,890,000.00 USD | 32,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0740` | 21,860,000.00 USD | 0.00 USD | 21,860,000.00 USD | 32,660.00 USD | 0.00 USD | 267.65 USD |
| `7D` | `0.0740` | 53,220,000.00 USD | 0.00 USD | 53,220,000.00 USD | 1,160,000.00 USD | 887,040.00 USD | 573,560.00 USD |
| `1D` | `0.0741` | 21,830,000.00 USD | 0.00 USD | 21,830,000.00 USD | 31,820.00 USD | 0.00 USD | 560.08 USD |
| `1D` | `0.0742` | 21,790,000.00 USD | 0.00 USD | 21,790,000.00 USD | 34,770.00 USD | 0.00 USD | 145.18 USD |
| `7D` | `0.0742` | 50,600,000.00 USD | 0.00 USD | 50,600,000.00 USD | 996,050.00 USD | 823,340.00 USD | 937,250.00 USD |
| `1D` | `0.0743` | 21,760,000.00 USD | 0.00 USD | 21,760,000.00 USD | 33,450.00 USD | 27,500.00 USD | 162.32 USD |
| `1D` | `0.0744` | 21,700,000.00 USD | 0.00 USD | 21,700,000.00 USD | 42,800.00 USD | 1,840.00 USD | 15,430.00 USD |
| `7D` | `0.0744` | 47,850,000.00 USD | 0.00 USD | 47,850,000.00 USD | 515,970.00 USD | 887,390.00 USD | 661,780.00 USD |
| `1D` | `0.0745` | 21,640,000.00 USD | 0.00 USD | 21,640,000.00 USD | 106,370.00 USD | 57,220.00 USD | 24,990.00 USD |
| `1D` | `0.0746` | 21,450,000.00 USD | 0.00 USD | 21,450,000.00 USD | 238,810.00 USD | 175,410.00 USD | 125,570.00 USD |
| `7D` | `0.0746` | 45,780,000.00 USD | 0.00 USD | 45,780,000.00 USD | 1,220,000.00 USD | 1,100,000.00 USD | 575,960.00 USD |
| `1D` | `0.0747` | 20,910,000.00 USD | 0.00 USD | 20,910,000.00 USD | 272,470.00 USD | 121,590.00 USD | 63,440.00 USD |
| `1D` | `0.0748` | 20,450,000.00 USD | 0.00 USD | 20,450,000.00 USD | 169,810.00 USD | 65,720.00 USD | 98,750.00 USD |
| `7D` | `0.0748` | 42,890,000.00 USD | 0.00 USD | 42,890,000.00 USD | 1,520,000.00 USD | 1,110,000.00 USD | 472,150.00 USD |
| `1D` | `0.0749` | 20,120,000.00 USD | 0.00 USD | 20,120,000.00 USD | 194,160.00 USD | 144,960.00 USD | 9,040.00 USD |
| `1D` | `0.0750` | 19,770,000.00 USD | 0.00 USD | 19,770,000.00 USD | 233,830.00 USD | 83,730.00 USD | 121,130.00 USD |
| `7D` | `0.0750` | 39,780,000.00 USD | 0.00 USD | 39,780,000.00 USD | 1,170,000.00 USD | 472,580.00 USD | 226,050.00 USD |
| `1D` | `0.0751` | 19,330,000.00 USD | 0.00 USD | 19,330,000.00 USD | 260,780.00 USD | 82,120.00 USD | 65,480.00 USD |
| `1D` | `0.0752` | 18,920,000.00 USD | 0.00 USD | 18,920,000.00 USD | 117,830.00 USD | 19,450.00 USD | 85,710.00 USD |
| `7D` | `0.0752` | 37,910,000.00 USD | 0.00 USD | 37,910,000.00 USD | 1,520,000.00 USD | 1,070,000.00 USD | 772,500.00 USD |
| `1D` | `0.0753` | 18,700,000.00 USD | 0.00 USD | 18,700,000.00 USD | 131,890.00 USD | 72,710.00 USD | 28,530.00 USD |
| `1D` | `0.0754` | 18,470,000.00 USD | 0.00 USD | 18,470,000.00 USD | 87,330.00 USD | 62,330.00 USD | 19,200.00 USD |
| `7D` | `0.0754` | 34,560,000.00 USD | 0.00 USD | 34,560,000.00 USD | 832,140.00 USD | 827,860.00 USD | 732,420.00 USD |
| `1D` | `0.0755` | 18,300,000.00 USD | 0.00 USD | 18,300,000.00 USD | 121,750.00 USD | 15,650.00 USD | 68,560.00 USD |
| `1D` | `0.0756` | 18,090,000.00 USD | 0.00 USD | 18,090,000.00 USD | 171,830.00 USD | 147,310.00 USD | 111,780.00 USD |
| `7D` | `0.0756` | 32,160,000.00 USD | 0.00 USD | 32,160,000.00 USD | 1,700,000.00 USD | 2,120,000.00 USD | 1,360,000.00 USD |
| `1D` | `0.0757` | 17,660,000.00 USD | 0.00 USD | 17,660,000.00 USD | 91,080.00 USD | 44,210.00 USD | 104,970.00 USD |
| `1D` | `0.0758` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 68,430.00 USD | 31,960.00 USD | 60,590.00 USD |
| `7D` | `0.0758` | 26,980,000.00 USD | 0.00 USD | 26,980,000.00 USD | 1,450,000.00 USD | 1,620,000.00 USD | 1,540,000.00 USD |
| `1D` | `0.0759` | 17,260,000.00 USD | 0.00 USD | 17,260,000.00 USD | 181,950.00 USD | 106,750.00 USD | 8,670.00 USD |
| `1D` | `0.0760` | 16,960,000.00 USD | 0.00 USD | 16,960,000.00 USD | 219,840.00 USD | 259,920.00 USD | 277,230.00 USD |
| `7D` | `0.0760` | 22,370,000.00 USD | 0.00 USD | 22,370,000.00 USD | 1,570,000.00 USD | 1,750,000.00 USD | 1,010,000.00 USD |
| `1D` | `0.0761` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 486,610.00 USD | 431,520.00 USD | 272,010.00 USD |
| `1D` | `0.0762` | 15,020,000.00 USD | 0.00 USD | 15,020,000.00 USD | 540,050.00 USD | 279,200.00 USD | 216,560.00 USD |
| `7D` | `0.0762` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 1,270,000.00 USD | 1,090,000.00 USD | 778,190.00 USD |
| `1D` | `0.0763` | 13,980,000.00 USD | 0.00 USD | 13,980,000.00 USD | 315,400.00 USD | 180,850.00 USD | 197,140.00 USD |
| `1D` | `0.0764` | 13,290,000.00 USD | 0.00 USD | 13,290,000.00 USD | 401,670.00 USD | 363,400.00 USD | 52,370.00 USD |
| `7D` | `0.0764` | 14,900,000.00 USD | 0.00 USD | 14,900,000.00 USD | 1,450,000.00 USD | 521,150.00 USD | 270,760.00 USD |
| `1D` | `0.0765` | 12,470,000.00 USD | 0.00 USD | 12,470,000.00 USD | 525,820.00 USD | 223,110.00 USD | 314,140.00 USD |
| `1D` | `0.0766` | 11,410,000.00 USD | 0.00 USD | 11,410,000.00 USD | 621,080.00 USD | 274,850.00 USD | 280,330.00 USD |
| `7D` | `0.0766` | 12,660,000.00 USD | 0.00 USD | 12,660,000.00 USD | 952,190.00 USD | 512,910.00 USD | 455,820.00 USD |
| `1D` | `0.0767` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 238,180.00 USD | 103,410.00 USD | 213,850.00 USD |
| `1D` | `0.0768` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 426,850.00 USD | 236,860.00 USD | 142,100.00 USD |
| `7D` | `0.0768` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 722,060.00 USD | 464,510.00 USD | 497,060.00 USD |
| `1D` | `0.0769` | 8,870,000.00 USD | 0.00 USD | 8,870,000.00 USD | 227,680.00 USD | 193,080.00 USD | 70,010.00 USD |
| `1D` | `0.0770` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 296,720.00 USD | 91,840.00 USD | 270,410.00 USD |
| `7D` | `0.0770` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 541,310.00 USD | 297,490.00 USD | 826,790.00 USD |
| `1D` | `0.0771` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 231,550.00 USD | 266,030.00 USD | 190,250.00 USD |
| `1D` | `0.0772` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 169,730.00 USD | 297,590.00 USD | 333,150.00 USD |
| `7D` | `0.0772` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 449,040.00 USD | 888,890.00 USD | 443,520.00 USD |
| `1D` | `0.0773` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 272,980.00 USD | 149,960.00 USD | 241,270.00 USD |
| `1D` | `0.0774` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 143,850.00 USD | 97,350.00 USD | 167,140.00 USD |
| `7D` | `0.0774` | 5,610,000.00 USD | 0.00 USD | 5,610,000.00 USD | 961,290.00 USD | 430,510.00 USD | 442,500.00 USD |
| `1D` | `0.0775` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 340,690.00 USD | 103,510.00 USD | 17,130.00 USD |
| `1D` | `0.0776` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 106,410.00 USD | 237,880.00 USD | 381,410.00 USD |
| `7D` | `0.0776` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 153,950.00 USD | 197,200.00 USD | 130,190.00 USD |
| `1D` | `0.0777` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 48,260.00 USD | 163,400.00 USD | 146.30 USD |
| `1D` | `0.0778` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 69,720.00 USD | 72,030.00 USD | 187,050.00 USD |
| `7D` | `0.0778` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 245,110.00 USD | 102,580.00 USD | 79,560.00 USD |
| `1D` | `0.0779` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 0.00 USD | 85,950.00 USD | 253.82 USD |
| `1D` | `0.0780` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 217,760.00 USD | 88,770.00 USD | 0.00 USD |
| `1D` | `0.0781` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 16,920.00 USD | 33,540.00 USD | 0.00 USD |
| `1D` | `0.0782` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 44,780.00 USD | 75,640.00 USD | 85,130.00 USD |
| `7D` | `0.0782` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 33,700.00 USD | 52,820.00 USD |
| `1D` | `0.0783` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 47,310.00 USD |
| `1D` | `0.0784` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 265,800.00 USD | 132,460.00 USD | 158,340.00 USD |
| `7D` | `0.0784` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 326,130.00 USD | 76,930.00 USD |
| `1D` | `0.0785` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 168,930.00 USD | 110,520.00 USD | 61,840.00 USD |
| `1D` | `0.0786` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 170,030.00 USD | 120,480.00 USD | 233,900.00 USD |
| `7D` | `0.0786` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 185,820.00 USD | 151,330.00 USD | 335,920.00 USD |
| `1D` | `0.0787` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 150,580.00 USD | 312,480.00 USD | 128,220.00 USD |
| `1D` | `0.0788` | 720,770.00 USD | 0.00 USD | 720,770.00 USD | 36,540.00 USD | 98,050.00 USD | 288,180.00 USD |
| `7D` | `0.0788` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 229,300.00 USD | 62,200.00 USD | 439,710.00 USD |
| `1D` | `0.0789` | 298,000.00 USD | 0.00 USD | 298,000.00 USD | 127,940.00 USD | 35,430.00 USD | 66,690.00 USD |
| `1D` | `0.0790` | 67,940.00 USD | 0.00 USD | 67,940.00 USD | 0.00 USD | 3,260.00 USD | 0.00 USD |
| `7D` | `0.0790` | 970,610.00 USD | 0.00 USD | 970,610.00 USD | 199,910.00 USD | 70,600.00 USD | 56,840.00 USD |
| `1D` | `0.0791` | 64,690.00 USD | 0.00 USD | 64,690.00 USD | 0.00 USD | 3,690.00 USD | 30,030.00 USD |
| `1D` | `0.0792` | 30,970.00 USD | 0.00 USD | 30,970.00 USD | 0.00 USD | 30,970.00 USD | 0.00 USD |
| `1D` | `0.0793` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0794` | 643,260.00 USD | 0.00 USD | 643,260.00 USD | 0.00 USD | 168,430.00 USD | 474,830.00 USD |
| `1D` | `0.0796` | 16,260.00 USD | 16,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD |
| `7D` | `0.0796` | 868,210.00 USD | 868,210.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `7D` | `0.0796` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 499,060.00 USD | 238,550.00 USD | 130,600.00 USD |
| `1D` | `0.0797` | 414,540.00 USD | 414,540.00 USD | 0.00 USD | 123,730.00 USD | 33,340.00 USD | 241,210.00 USD |
| `1D` | `0.0798` | 569,220.00 USD | 569,220.00 USD | 0.00 USD | 0.00 USD | 154,680.00 USD | 0.00 USD |
| `7D` | `0.0798` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 600,260.00 USD | 46,270.00 USD | 41,520.00 USD |
| `1D` | `0.0799` | 912,240.00 USD | 912,240.00 USD | 0.00 USD | 169,980.00 USD | 1,740.00 USD | 171,300.00 USD |
| `1D` | `0.0800` | 917,850.00 USD | 917,850.00 USD | 0.00 USD | 0.00 USD | 5,610.00 USD | 0.00 USD |
| `1D` | `0.0804` | 928,750.00 USD | 928,750.00 USD | 0.00 USD | 0.00 USD | 10,910.00 USD | 0.00 USD |
| `7D` | `0.0804` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 95,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0806` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 3,520.00 USD | 0.00 USD | 98,970.00 USD |
| `7D` | `0.0806` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 149,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.0807` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 181,700.00 USD | 160,730.00 USD | 40,790.00 USD |
| `1D` | `0.0808` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 380,920.00 USD | 23,520.00 USD | 522,290.00 USD |
| `7D` | `0.0808` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD |
| `1D` | `0.0809` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 419,190.00 USD | 273,060.00 USD | 0.00 USD |
| `1D` | `0.0810` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 214,090.00 USD | 132,380.00 USD | 118,770.00 USD |
| `7D` | `0.0810` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 119,970.00 USD | 1,290,000.00 USD | 0.00 USD |
| `1D` | `0.0811` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 243,800.00 USD | 0.00 USD |
| `1D` | `0.0812` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 93,910.00 USD | 75,260.00 USD | 192,820.00 USD |
| `7D` | `0.0812` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 126,600.00 USD | 572,140.00 USD | 0.00 USD |
| `1D` | `0.0813` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 27,080.00 USD | 18,240.00 USD | 209,180.00 USD |
| `1D` | `0.0814` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 22,430.00 USD | 18,210.00 USD | 386,300.00 USD |
| `7D` | `0.0814` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 215,950.00 USD | 876,360.00 USD | 2,260.00 USD |
| `1D` | `0.0815` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 249,400.00 USD | 201,730.00 USD | 112,300.00 USD |
| `1D` | `0.0816` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 441,880.00 USD | 245,220.00 USD | 189,500.00 USD |
| `7D` | `0.0816` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,230,000.00 USD | 1,070,000.00 USD | 682,410.00 USD |
| `1D` | `0.0817` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 361,650.00 USD | 152,470.00 USD | 130,180.00 USD |
| `1D` | `0.0818` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 298,910.00 USD | 161,880.00 USD | 321,810.00 USD |
| `7D` | `0.0818` | 14,120,000.00 USD | 14,120,000.00 USD | 0.00 USD | 1,650,000.00 USD | 936,710.00 USD | 916,550.00 USD |
| `1D` | `0.0819` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 171,350.00 USD | 368,950.00 USD | 156,890.00 USD |
| `1D` | `0.0820` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 215,860.00 USD | 275,570.00 USD | 499,340.00 USD |
| `7D` | `0.0820` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 990,880.00 USD | 836,130.00 USD | 918,680.00 USD |
| `1D` | `0.0821` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 383,530.00 USD | 167,310.00 USD | 171,040.00 USD |
| `1D` | `0.0822` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 258,140.00 USD | 184,710.00 USD | 156,220.00 USD |
| `7D` | `0.0822` | 19,350,000.00 USD | 19,350,000.00 USD | 0.00 USD | 1,460,000.00 USD | 680,570.00 USD | 344,010.00 USD |
| `1D` | `0.0823` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 250,780.00 USD | 51,750.00 USD | 8,520.00 USD |
| `1D` | `0.0824` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 131,550.00 USD | 172,750.00 USD | 198,580.00 USD |
| `7D` | `0.0824` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 912,190.00 USD | 552,170.00 USD | 305,450.00 USD |
| `1D` | `0.0825` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 110,900.00 USD | 84,710.00 USD | 21,620.00 USD |
| `1D` | `0.0826` | 11,980,000.00 USD | 11,980,000.00 USD | 0.00 USD | 63,310.00 USD | 36,010.00 USD | 183,350.00 USD |
| `7D` | `0.0826` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 945,330.00 USD | 392,890.00 USD | 419,590.00 USD |
| `1D` | `0.0827` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 63,060.00 USD | 49,420.00 USD | 55.02 USD |
| `1D` | `0.0828` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 269,440.00 USD | 73,490.00 USD | 36,570.00 USD |
| `7D` | `0.0828` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 740,640.00 USD | 163,460.00 USD | 215,010.00 USD |
| `1D` | `0.0829` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 234,870.00 USD | 88,990.00 USD | 72,740.00 USD |
| `1D` | `0.0830` | 13,380,000.00 USD | 13,380,000.00 USD | 0.00 USD | 258,290.00 USD | 110,610.00 USD | 151,470.00 USD |
| `7D` | `0.0830` | 24,970,000.00 USD | 24,970,000.00 USD | 0.00 USD | 431,690.00 USD | 205,960.00 USD | 338,310.00 USD |
| `1D` | `0.0831` | 13,590,000.00 USD | 13,590,000.00 USD | 0.00 USD | 102,690.00 USD | 64,510.00 USD | 42,470.00 USD |
| `1D` | `0.0832` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 233,350.00 USD | 91,440.00 USD | 86,220.00 USD |
| `7D` | `0.0832` | 26,470,000.00 USD | 26,470,000.00 USD | 0.00 USD | 676,300.00 USD | 537,000.00 USD | 283,680.00 USD |
| `1D` | `0.0833` | 14,260,000.00 USD | 14,260,000.00 USD | 0.00 USD | 158,470.00 USD | 68,410.00 USD | 31,430.00 USD |
| `1D` | `0.0834` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 146,880.00 USD | 60,550.00 USD | 133,230.00 USD |
| `7D` | `0.0834` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 704,830.00 USD | 441,890.00 USD | 401,100.00 USD |
| `1D` | `0.0835` | 14,990,000.00 USD | 14,990,000.00 USD | 0.00 USD | 122,400.00 USD | 184,470.00 USD | 78,760.00 USD |
| `1D` | `0.0836` | 15,370,000.00 USD | 15,370,000.00 USD | 0.00 USD | 78,450.00 USD | 84,520.00 USD | 221,700.00 USD |
| `7D` | `0.0836` | 29,170,000.00 USD | 29,170,000.00 USD | 0.00 USD | 488,990.00 USD | 229,170.00 USD | 439,080.00 USD |
| `1D` | `0.0837` | 15,660,000.00 USD | 15,660,000.00 USD | 0.00 USD | 191,180.00 USD | 61,550.00 USD | 34,400.00 USD |
| `1D` | `0.0838` | 15,930,000.00 USD | 15,930,000.00 USD | 0.00 USD | 145,530.00 USD | 76,380.00 USD | 48,790.00 USD |
| `7D` | `0.0838` | 29,970,000.00 USD | 29,970,000.00 USD | 0.00 USD | 480,150.00 USD | 257,510.00 USD | 57,010.00 USD |
| `1D` | `0.0839` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 67,620.00 USD | 0.00 USD | 639.31 USD |
| `1D` | `0.0840` | 16,050,000.00 USD | 16,050,000.00 USD | 0.00 USD | 35,250.00 USD | 15,480.00 USD | 584.63 USD |
| `7D` | `0.0840` | 30,280,000.00 USD | 30,280,000.00 USD | 0.00 USD | 238,290.00 USD | 64,060.00 USD | 9,350.00 USD |
| `1D` | `0.0841` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 32,120.00 USD | 2,010.00 USD | 709.20 USD |
| `1D` | `0.0842` | 16,160,000.00 USD | 16,160,000.00 USD | 0.00 USD | 30,040.00 USD | 0.00 USD | 47,110.00 USD |
| `7D` | `0.0842` | 30,730,000.00 USD | 30,730,000.00 USD | 0.00 USD | 330,280.00 USD | 33,520.00 USD | 85,740.00 USD |
| `1D` | `0.0843` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 34,480.00 USD | 0.00 USD | 1,050.00 USD |
| `1D` | `0.0844` | 16,280,000.00 USD | 16,280,000.00 USD | 0.00 USD | 78,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0844` | 31,190,000.00 USD | 31,190,000.00 USD | 0.00 USD | 274,110.00 USD | 108,480.00 USD | 81,250.00 USD |
| `1D` | `0.0845` | 16,290,000.00 USD | 16,290,000.00 USD | 0.00 USD | 15,700.00 USD | 0.00 USD | 320.28 USD |
| `1D` | `0.0846` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 71,250.00 USD | 16,670.00 USD | 75.71 USD |
| `7D` | `0.0846` | 31,590,000.00 USD | 31,590,000.00 USD | 0.00 USD | 187,390.00 USD | 107,550.00 USD | 104,390.00 USD |
| `1D` | `0.0847` | 16,390,000.00 USD | 16,390,000.00 USD | 0.00 USD | 12,740.00 USD | 0.00 USD | 284.68 USD |
| `1D` | `0.0848` | 16,420,000.00 USD | 16,420,000.00 USD | 0.00 USD | 20,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.0848` | 32,240,000.00 USD | 32,240,000.00 USD | 0.00 USD | 326,610.00 USD | 180,440.00 USD | 140,140.00 USD |
| `1D` | `0.0849` | 16,430,000.00 USD | 16,430,000.00 USD | 0.00 USD | 11,280.00 USD | 0.00 USD | 292.60 USD |
| `1D` | `0.0850` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 22,320.00 USD | 0.00 USD | 413.16 USD |
| `7D` | `0.0850` | 33,030,000.00 USD | 33,030,000.00 USD | 0.00 USD | 286,650.00 USD | 206,450.00 USD | 299,500.00 USD |
| `1D` | `0.0851` | 16,490,000.00 USD | 16,490,000.00 USD | 0.00 USD | 26,040.00 USD | 11,000.00 USD | 750.73 USD |
| `1D` | `0.0852` | 16,490,000.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 304.58 USD |
| `7D` | `0.0852` | 33,270,000.00 USD | 33,270,000.00 USD | 0.00 USD | 68,050.00 USD | 87,540.00 USD | 79,060.00 USD |
| `1D` | `0.0853` | 16,500,000.00 USD | 16,500,000.00 USD | 0.00 USD | 12,910.00 USD | 737.47 USD | 212.49 USD |
| `1D` | `0.0854` | 16,560,000.00 USD | 16,560,000.00 USD | 0.00 USD | 35,960.00 USD | 13,190.00 USD | 10,120.00 USD |
| `7D` | `0.0854` | 33,640,000.00 USD | 33,640,000.00 USD | 0.00 USD | 196,480.00 USD | 103,870.00 USD | 77,560.00 USD |
| `1D` | `0.0855` | 16,710,000.00 USD | 16,710,000.00 USD | 0.00 USD | 64,150.00 USD | 45,460.00 USD | 36,330.00 USD |
| `1D` | `0.0856` | 16,850,000.00 USD | 16,850,000.00 USD | 0.00 USD | 92,490.00 USD | 32,810.00 USD | 19,870.00 USD |
| `7D` | `0.0856` | 34,310,000.00 USD | 34,310,000.00 USD | 0.00 USD | 299,530.00 USD | 212,380.00 USD | 153,050.00 USD |
| `1D` | `0.0857` | 16,950,000.00 USD | 16,950,000.00 USD | 0.00 USD | 50,540.00 USD | 18,030.00 USD | 27,880.00 USD |
| `1D` | `0.0858` | 17,030,000.00 USD | 17,030,000.00 USD | 0.00 USD | 48,130.00 USD | 36,780.00 USD | 164.89 USD |
| `7D` | `0.0858` | 34,680,000.00 USD | 34,680,000.00 USD | 0.00 USD | 216,230.00 USD | 46,980.00 USD | 108,120.00 USD |
| `1D` | `0.0859` | 17,170,000.00 USD | 17,170,000.00 USD | 0.00 USD | 72,260.00 USD | 20,870.00 USD | 40,140.00 USD |
| `1D` | `0.0860` | 17,250,000.00 USD | 17,250,000.00 USD | 0.00 USD | 44,920.00 USD | 22,170.00 USD | 20,180.00 USD |
| `7D` | `0.0860` | 34,920,000.00 USD | 34,920,000.00 USD | 0.00 USD | 148,110.00 USD | 78,940.00 USD | 17,990.00 USD |
| `1D` | `0.0861` | 17,310,000.00 USD | 17,310,000.00 USD | 0.00 USD | 20,430.00 USD | 0.00 USD | 32,450.00 USD |
| `1D` | `0.0862` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 33,780.00 USD | 29,080.00 USD | 11,330.00 USD |
| `7D` | `0.0862` | 35,220,000.00 USD | 35,220,000.00 USD | 0.00 USD | 100,930.00 USD | 91,260.00 USD | 103,120.00 USD |
| `1D` | `0.0863` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 219.34 USD |
| `1D` | `0.0864` | 17,430,000.00 USD | 17,430,000.00 USD | 0.00 USD | 22,510.00 USD | 20,050.00 USD | 5,150.00 USD |
| `7D` | `0.0864` | 35,270,000.00 USD | 35,270,000.00 USD | 0.00 USD | 19,600.00 USD | 732.43 USD | 28,010.00 USD |
| `1D` | `0.0865` | 17,480,000.00 USD | 17,480,000.00 USD | 0.00 USD | 31,770.00 USD | 1,280.00 USD | 18,020.00 USD |
| `1D` | `0.0866` | 17,540,000.00 USD | 17,540,000.00 USD | 0.00 USD | 25,410.00 USD | 16,310.00 USD | 19,340.00 USD |
| `7D` | `0.0866` | 35,530,000.00 USD | 35,530,000.00 USD | 0.00 USD | 146,420.00 USD | 30,660.00 USD | 80,410.00 USD |
| `1D` | `0.0867` | 17,620,000.00 USD | 17,620,000.00 USD | 0.00 USD | 24,580.00 USD | 37,120.00 USD | 14,130.00 USD |
| `1D` | `0.0868` | 17,670,000.00 USD | 17,670,000.00 USD | 0.00 USD | 8,080.00 USD | 9,300.00 USD | 34,750.00 USD |
| `7D` | `0.0868` | 35,960,000.00 USD | 35,960,000.00 USD | 0.00 USD | 199,460.00 USD | 157,140.00 USD | 74,470.00 USD |
| `1D` | `0.0869` | 17,720,000.00 USD | 17,720,000.00 USD | 0.00 USD | 16,230.00 USD | 8,560.00 USD | 24,000.00 USD |
| `1D` | `0.0870` | 17,780,000.00 USD | 17,780,000.00 USD | 0.00 USD | 50,000.00 USD | 12,500.00 USD | 0.00 USD |
| `7D` | `0.0870` | 36,360,000.00 USD | 36,360,000.00 USD | 0.00 USD | 181,240.00 USD | 165,720.00 USD | 56,090.00 USD |
| `1D` | `0.0871` | 17,920,000.00 USD | 17,920,000.00 USD | 0.00 USD | 28,210.00 USD | 45,410.00 USD | 62,350.00 USD |
| `1D` | `0.0872` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 26,980.00 USD | 32,280.00 USD | 8,650.00 USD |
| `7D` | `0.0872` | 36,770,000.00 USD | 36,770,000.00 USD | 0.00 USD | 148,660.00 USD | 151,040.00 USD | 112,220.00 USD |
| `1D` | `0.0873` | 18,030,000.00 USD | 18,030,000.00 USD | 0.00 USD | 9,490.00 USD | 1,820.00 USD | 36,110.00 USD |
| `7D` | `0.0874` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 100,710.00 USD | 2,060.00 USD | 29,540.00 USD |
| `1D` | `0.0875` | 18,060,000.00 USD | 18,060,000.00 USD | 0.00 USD | 13,160.00 USD | 17,190.00 USD | 0.00 USD |
| `1D` | `0.0876` | 18,130,000.00 USD | 18,130,000.00 USD | 0.00 USD | 29,600.00 USD | 26,100.00 USD | 11,490.00 USD |
| `7D` | `0.0876` | 37,130,000.00 USD | 37,130,000.00 USD | 0.00 USD | 146,430.00 USD | 42,190.00 USD | 41,140.00 USD |
| `1D` | `0.0877` | 18,180,000.00 USD | 18,180,000.00 USD | 0.00 USD | 22,320.00 USD | 11,700.00 USD | 21,830.00 USD |
| `1D` | `0.0878` | 18,340,000.00 USD | 18,340,000.00 USD | 0.00 USD | 63,040.00 USD | 41,450.00 USD | 50,850.00 USD |
| `7D` | `0.0878` | 37,350,000.00 USD | 37,350,000.00 USD | 0.00 USD | 77,160.00 USD | 41,090.00 USD | 94,240.00 USD |
| `1D` | `0.0879` | 18,370,000.00 USD | 18,370,000.00 USD | 0.00 USD | 15,840.00 USD | 9,450.00 USD | 7,440.00 USD |
| `1D` | `0.0880` | 18,470,000.00 USD | 18,470,000.00 USD | 0.00 USD | 48,000.00 USD | 15,600.00 USD | 31,960.00 USD |
| `7D` | `0.0880` | 37,640,000.00 USD | 37,640,000.00 USD | 0.00 USD | 111,530.00 USD | 131,210.00 USD | 51,000.00 USD |
| `1D` | `0.0881` | 18,530,000.00 USD | 18,530,000.00 USD | 0.00 USD | 33,000.00 USD | 19,660.00 USD | 12,510.00 USD |
| `1D` | `0.0882` | 18,600,000.00 USD | 18,600,000.00 USD | 0.00 USD | 25,340.00 USD | 15,630.00 USD | 27,880.00 USD |
| `7D` | `0.0882` | 37,920,000.00 USD | 37,920,000.00 USD | 0.00 USD | 107,150.00 USD | 62,150.00 USD | 112,570.00 USD |
| `1D` | `0.0883` | 18,710,000.00 USD | 18,710,000.00 USD | 0.00 USD | 22,710.00 USD | 73,610.00 USD | 7,630.00 USD |
| `1D` | `0.0884` | 18,800,000.00 USD | 18,800,000.00 USD | 0.00 USD | 7,860.00 USD | 0.00 USD | 83,950.00 USD |
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
  * Total Open Interest: `1.12B` | Total OI Tokens: `14,081,769,273.7 DOGE`
  * 1h OI Change: `+0.32%` | 4h OI Change: `-0.33%` | 24h OI Change: `-2.29%`
  * Exchange Breakdown: Binance=`270.86M` | Bybit=`111.08M` | OKX=`115.68M` | Hyperliquid=`80.16M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `43.90K` | Last 24h: `83.91K` | Last 3d: `253.77K` | Last 7d: `336.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0083%` | **USDT Bitget** | `0.0089%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `DOGE` | `62.10%` | `37.90%` | `1.64` | 4,000,000.00 USD |
| `15M` | `Binance` | `61.7%` | `38.3%` | `1.61` | 2,590,000.00 USD |
| `15M` | `OKX` | `85.13%` | `14.87%` | `5.72` | 299,160.00 USD |
| `15M` | `Bybit` | `55.58%` | `44.42%` | `1.25` | 105,630.00 USD |
| `15M` | `KuCoin` | `82.21%` | `17.79%` | `4.62` | 18,720.00 USD |
| `15M` | `Gate` | `56.68%` | `43.32%` | `1.31` | 175,090.00 USD |
| `15M` | `Bitget` | `57.18%` | `42.82%` | `1.34` | 41,110.00 USD |
| `15M` | `BingX` | `55.75%` | `44.25%` | `1.26` | 339,500.00 USD |
| `15M` | `MEXC` | `41.16%` | `58.84%` | `0.70` | 43,410.00 USD |
| `15M` | `Bitunix` | `56.38%` | `43.62%` | `1.29` | 81,730.00 USD |
| `15M` | `Hyperliquid` | `88.79%` | `11.21%` | `7.92` | 27,100.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `62.85%` | `37.15%` | `1.69` | 48,370.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `59.71%` | `40.29%` | `1.48` | 76,110.00 USD |
| `15M` | `HTX` | `54.35%` | `45.65%` | `1.19` | 44,490.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `6.87%` | `93.13%` | `0.07` | 10,720.00 USD |
| `15M` | `Aster` | `81.78%` | `18.22%` | `4.49` | 41,160.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `35.78%` | `64.22%` | `0.56` | 50,420.00 USD |
| `15M` | `Whale Positions` | `61.7%` | `38.3%` | `1.61` | 2,590,000.00 USD |
| `15M` | `Global Accounts` | `62.10%` | `37.90%` | `1.64` | 4,000,000.00 USD |
| `1H` | `DOGE` | `54.24%` | `45.76%` | `1.19` | 23,870,000.00 USD |
| `1H` | `Binance` | `54.12%` | `45.88%` | `1.18` | 14,000,000.00 USD |
| `1H` | `OKX` | `65.83%` | `34.17%` | `1.93` | 1,760,000.00 USD |
| `1H` | `Bybit` | `50.54%` | `49.46%` | `1.02` | 587,950.00 USD |
| `1H` | `KuCoin` | `41.89%` | `58.11%` | `0.72` | 161,360.00 USD |
| `1H` | `Gate` | `57.95%` | `42.05%` | `1.38` | 1,540,000.00 USD |
| `1H` | `Bitget` | `78.15%` | `21.85%` | `3.58` | 1,420,000.00 USD |
| `1H` | `BingX` | `30.84%` | `69.16%` | `0.45` | 2,100,000.00 USD |
| `1H` | `MEXC` | `37.18%` | `62.82%` | `0.59` | 230,490.00 USD |
| `1H` | `Bitunix` | `48.45%` | `51.55%` | `0.94` | 683,480.00 USD |
| `1H` | `Hyperliquid` | `21.53%` | `78.47%` | `0.27` | 222,020.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `55.57%` | `44.43%` | `1.25` | 500,350.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `84.01%` | `15.99%` | `5.25` | 182,250.00 USD |
| `1H` | `HTX` | `79.79%` | `20.21%` | `3.95` | 170,140.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `39.74%` | `60.26%` | `0.66` | 22,480.00 USD |
| `1H` | `Aster` | `59.71%` | `40.29%` | `1.48` | 173,990.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `45.65%` | `54.35%` | `0.84` | 123,810.00 USD |
| `1H` | `Whale Positions` | `54.12%` | `45.88%` | `1.18` | 14,000,000.00 USD |
| `1H` | `Global Accounts` | `54.24%` | `45.76%` | `1.19` | 23,870,000.00 USD |
| `4H` | `DOGE` | `48.71%` | `51.29%` | `0.95` | 181,800,000.00 USD |
| `4H` | `Binance` | `48.2%` | `51.8%` | `0.93` | 116,840,000.00 USD |
| `4H` | `OKX` | `47.87%` | `52.13%` | `0.92` | 10,710,000.00 USD |
| `4H` | `Bybit` | `41.83%` | `58.17%` | `0.72` | 5,620,000.00 USD |
| `4H` | `KuCoin` | `45.97%` | `54.03%` | `0.85` | 969,240.00 USD |
| `4H` | `Gate` | `56.68%` | `43.32%` | `1.31` | 16,060,000.00 USD |
| `4H` | `Bitget` | `60.57%` | `39.43%` | `1.54` | 4,170,000.00 USD |
| `4H` | `BingX` | `39.04%` | `60.96%` | `0.64` | 8,110,000.00 USD |
| `4H` | `MEXC` | `52.06%` | `47.94%` | `1.09` | 2,730,000.00 USD |
| `4H` | `Bitunix` | `44.02%` | `55.98%` | `0.79` | 5,090,000.00 USD |
| `4H` | `Hyperliquid` | `31%` | `69%` | `0.45` | 1,250,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.84%` | `49.16%` | `1.03` | 4,400,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `89.54%` | `10.46%` | `8.56` | 872,780.00 USD |
| `4H` | `HTX` | `51.05%` | `48.95%` | `1.04` | 919,470.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `61.37%` | `38.63%` | `1.59` | 209,940.00 USD |
| `4H` | `Aster` | `48.13%` | `51.87%` | `0.93` | 1,570,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.27%` | `51.73%` | `0.93` | 2,280,000.00 USD |
| `4H` | `Whale Positions` | `48.2%` | `51.8%` | `0.93` | 116,840,000.00 USD |
| `4H` | `Global Accounts` | `48.71%` | `51.29%` | `0.95` | 181,800,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.0802` | `0.0801` | `0.0802` | `0.0802` | `0.0799` | 3,513,799.11 USD | 1,857,314.90 USD | 1,656,484.22 USD | 200,830.68 USD | `+5.72%` | `2B / 5S` |
| `0:00 UTC` | `0.0800` | `0.0800` | `0.0800` | `0.0802` | `0.0799` | 4,173,492.18 USD | 1,857,641.00 USD | 2,315,851.18 USD | -458,210.19 USD | `-10.98%` | `2B / 1S` |
| `5:00 UTC` | `0.0800` | `0.0800` | `0.0800` | `0.0801` | `0.0799` | 3,085,332.02 USD | 1,558,385.55 USD | 1,526,946.46 USD | 31,439.09 USD | `+1.02%` | `2B / 2S` |
| `0:00 UTC` | `0.0796` | `0.0798` | `0.0796` | `0.0802` | `0.0795` | 5,871,793.04 USD | 2,200,842.18 USD | 3,670,950.86 USD | -1,470,108.68 USD | `-25.04%` | `4B / 23S` |
| `5:00 UTC` | `0.0793` | `0.0794` | `0.0793` | `0.0796` | `0.0792` | 7,734,342.64 USD | 3,622,970.91 USD | 4,111,371.72 USD | -488,400.81 USD | `-6.31%` | `4B / 4S` |
| `0:00 UTC` | `0.0795` | `0.0796` | `0.0795` | `0.0797` | `0.0794` | 2,831,870.97 USD | 1,358,858.88 USD | 1,473,012.09 USD | -114,153.20 USD | `-4.03%` | `5B / 6S` |
| `5:00 UTC` | `0.0795` | `0.0795` | `0.0795` | `0.0797` | `0.0793` | 3,357,728.54 USD | 1,747,237.98 USD | 1,610,490.56 USD | 136,747.43 USD | `+4.07%` | `3B / 4S` |
| `0:00 UTC` | `0.0791` | `0.0791` | `0.0791` | `0.0794` | `0.0789` | 5,383,971.27 USD | 2,616,260.04 USD | 2,767,711.23 USD | -151,451.19 USD | `-2.81%` | `3B / 9S` |
| `5:00 UTC` | `0.0793` | `0.0793` | `0.0793` | `0.0795` | `0.0790` | 3,072,363.78 USD | 1,995,905.48 USD | 1,076,458.30 USD | 919,447.18 USD | `+29.93%` | `17B / 6S` |
| `0:00 UTC` | `0.0792` | `0.0792` | `0.0792` | `0.0793` | `0.0791` | 573,072.14 USD | 180,363.94 USD | 392,708.20 USD | -212,344.27 USD | `-37.05%` | `2B / 8S` |

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
| `5m` | 57,640.00 USD | 993,760.00 USD | **`ACCUMULATION`** |
| `15m` | 65,320.00 USD | 1,090,000.00 USD | **`ACCUMULATION`** |
| `30m` | -723,090.00 USD | -467,910.00 USD | **`DISTRIBUTION`** |
| `1h` | -990,930.00 USD | 1,630,000.00 USD | **`ACCUMULATION`** |
| `2h` | -1,980,000.00 USD | -1,450,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -3,070,000.00 USD | -1,330,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,960,000.00 USD | 1,260,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 71,000.00 USD | -2,720,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -123,360.00 USD | -4,050,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,920,000.00 USD | -9,950,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -41,800,000.00 USD | -123,740,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -268,610,000.00 USD | -749,490,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+57.64K` | 15m=`+65.32K` | 1h=`-990.93K` | 24h=`-2.92M`
* Futures Capital Netflows: 5m=`+993.76K` | 15m=`+1.09M` | 1h=`+1.63M` | 24h=`-9.95M`
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
  * `2026-10-30 00:17:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:30:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:29:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:31:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.0764` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.0727` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0869`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.0786` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.0823` (Risk Distance: `0.0042` pts)
  * +2.5R Take Profit: `0.0681`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.0799`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
