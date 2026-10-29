# 🏛️ SOVEREIGN CANDIDATE DOSSIER: SOL
**Canonical Key**: `SOL` | **Broker Instrument**: `SOLUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 01:29:56 IST` (`2026-10-29 19:59:56 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `99.81` | **Live Ask Quote**: `100.05` | **Mid Price**: `99.93`
- **Spread Points**: `24.00` | **Spread BPS**: `24.02 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `100.42` | VWAP Z-Score: `-0.68` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4698` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `34.73` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `102.97` | Lower -3.00σ Band: `97.87`
  * Upper +2.51σ Band: `102.55` | Lower -2.51σ Band: `98.28`
  * Upper +2.01σ Band: `102.12` | Lower -2.01σ Band: `98.71`
  * Upper +2.00σ Band: `102.12` | Lower -2.00σ Band: `98.72`
  * Upper +1.28σ Band: `101.50` | Lower -1.28σ Band: `99.33`
  * Upper +1.00σ Band: `101.27` | Lower -1.00σ Band: `99.57`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`100.37` | EMA-20=`100.71` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`100.71` (Slope: `+0.0000`) | EMA-100=`100.76`
  * Institutional Anchors: EMA-144=`100.78` | EMA-200=`100.74` (Slope: `-0.0143`) | EMA-233=`100.70`
- **Range Boundaries**: 24H High=`103.63` | 24H Low=`98.95` | Weekly High=`103.63` | Weekly Low=`98.85`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `101.25` (Distance: `-1.30%`)
  * Point of Control (POC) = `99.92` (Distance: `+0.01%`)
  * Value Area Low (VAL) = `99.18` (Distance: `+0.76%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.11` | POC=`100.90` | VAL=`100.63`
  * Prior Day Extremes: PDH=`103.63` | PDL=`100.15` | PDC=`102.27`
  * Monday Range Blueprint: High=`102.46` | Mid=`101.01` | Low=`99.56`
  * Developing Weekly Value Area: Weekly VAH=`101.48` | Weekly POC=`100.91` | Weekly VAL=`99.69`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.77` | Low=`98.95`
  * London Session (08:00-16:00 UTC): High=`100.61` | Low=`99.44`
  * New York Session (13:00-21:00 UTC): High=`102.93` | Low=`99.78`
  * Initial Balance (First Hour): IB High=`100.61` | IB Low=`99.91`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `99.53` - `100.33`
  * Optimal Trade Entry (OTE 0.705): `100.13`
  * Structural Invalidation Anchor (0.786): `100.73`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `100.18` | `100.37` | `100.18` | `100.24` | `42,426` | 4,254,239.57 USD | 615,741.61 USD | `+14.47%` | -71,289,687.20 USD | `+0.61` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `100.24` | `100.24` | `100.10` | `100.11` | `52,275` | 5,235,928.43 USD | 2,039,225.45 USD | `+38.95%` | -69,250,461.75 USD | `+1.46` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `100.11` | `100.20` | `100.08` | `100.10` | `47,169` | 4,723,411.86 USD | 323,406.75 USD | `+6.85%` | -68,927,055.00 USD | `+0.36` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `100.57` | `100.61` | `100.24` | `100.27` | `94,842` | 9,521,682.83 USD | -44,411.28 USD | `-0.47%` | -70,635,604.28 USD | `+0.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `100.27` | `100.42` | `100.15` | `100.19` | `109,464` | 10,974,925.19 USD | -1,269,824.53 USD | `-11.57%` | -71,905,428.81 USD | `-0.06` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `100.18` | `100.37` | `100.08` | `100.10` | `141,870` | 14,213,579.86 USD | 2,978,373.81 USD | `+20.95%` | -68,927,055.00 USD | `+1.47` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `101.87` | `101.93` | `100.71` | `101.06` | `773,410` | 78,387,335.50 USD | -11,810,112.06 USD | `-15.07%` | -67,707,300.30 USD | `-1.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.06` | `101.18` | `100.29` | `100.57` | `555,290` | 55,901,104.31 USD | -7,049,401.02 USD | `-12.61%` | -74,756,701.33 USD | `-0.46` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `100.57` | `100.61` | `100.08` | `100.12` | `346,886` | 34,781,171.81 USD | 1,726,586.65 USD | `+4.96%` | -73,030,114.68 USD | `+0.62` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -42,310,715.88 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -43,868,643.21 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `100.08` | `100.12` | `2,775,561` | 281,657,684.29 USD | -29,157,752.38 USD | `-10.35%` | -73,026,395.60 USD | `-1.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `102.37` | `102.50` | `99.16` | `99.64` | `3,450,297` | 345,810,531.49 USD | -35,022,306.76 USD | `-10.13%` | -43,673,756.58 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `99.63` | `100.78` | `99.40` | `99.71` | `1,690,194` | 169,196,763.38 USD | 5,656,394.57 USD | `+3.34%` | -38,017,362.01 USD | `+1.09` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `99.71` | `100.79` | `99.70` | `100.34` | `1,518,349` | 152,283,655.59 USD | -4,293,353.88 USD | `-2.82%` | -42,310,715.88 USD | `+0.42` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `100.34` | `102.70` | `100.03` | `102.66` | `4,178,003` | 423,242,147.26 USD | -1,557,927.33 USD | `-0.37%` | -43,868,643.21 USD | `+0.52` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `102.66` | `103.16` | `100.08` | `100.12` | `2,775,561` | 281,657,684.29 USD | -29,157,752.38 USD | `-10.35%` | -73,026,395.60 USD | `-1.15` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`99.93`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `99.98` | `198.6800` | 19,865.02 USD | 1,908,513.06 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `99.99` | `4.9900` | 498.97 USD | 1,553,974.00 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `99.99` | `1556.0500` | 155,592.55 USD | 1,709,566.55 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `99.99` | `266.8000` | 26,677.60 USD | 1,736,244.15 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `99.99` | `207.3500` | 20,732.93 USD | 1,756,977.07 USD | `8 orders` | `-0.07%` | `-` |
| `BID` | `99.99` | `77.7500` | 7,774.14 USD | 1,764,751.22 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `99.99` | `82.4600` | 8,245.01 USD | 1,772,996.23 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `99.99` | `1156.6800` | 115,651.81 USD | 1,888,648.04 USD | `2 orders` | `-0.08%` | `-` |
| `BID` | `100.00` | `2374.9200` | 237,492.00 USD | 1,400,217.42 USD | `53 orders` | `-0.06%` | `-` |
| `BID` | `100.00` | `244.4200` | 24,441.76 USD | 1,424,659.18 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `100.00` | `79.5400` | 7,953.84 USD | 1,432,613.02 USD | `3 orders` | `-0.07%` | `-` |
| `BID` | `100.00` | `891.0600` | 89,103.33 USD | 1,521,716.35 USD | `3 orders` | `-0.07%` | `-` |
| `BID` | `100.00` | `269.4600` | 26,944.92 USD | 1,548,661.27 USD | `4 orders` | `-0.07%` | `-` |
| `BID` | `100.00` | `48.1400` | 4,813.76 USD | 1,553,475.03 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `100.01` | `3300.0000` | 330,033.00 USD | 1,162,725.42 USD | `25 orders` | `-0.05%` | `-` |
| `BID` | `100.02` | `2191.2300` | 219,166.82 USD | 832,692.42 USD | `29 orders` | `-0.04%` | `-` |
| `BID` | `100.03` | `2287.2000` | 228,788.62 USD | 613,525.60 USD | `27 orders` | `-0.03%` | `-` |
| `BID` | `100.04` | `1269.8500` | 127,035.79 USD | 384,736.98 USD | `25 orders` | `-0.02%` | `-` |
| `BID` | `100.05` | `1835.1100` | 183,602.76 USD | 257,701.19 USD | `7 orders` | `-0.01%` | `-` |
| `MID_SPREAD` | `100.06` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 100.06` | `0.00%` | `-` |
| `BID` | `100.06` | `740.5400` | 74,098.43 USD | 74,098.43 USD | `10 orders` | `-0.00%` | `-` |
| `ASK` | `100.07` | `1279.1700` | 128,006.54 USD | 128,006.54 USD | `38 orders` | `+0.00%` | `-` |
| `ASK` | `100.08` | `1062.7700` | 106,362.02 USD | 234,368.56 USD | `19 orders` | `+0.01%` | `-` |
| `ASK` | `100.09` | `1617.1600` | 161,861.54 USD | 396,230.11 USD | `25 orders` | `+0.02%` | `-` |
| `ASK` | `100.10` | `3306.5900` | 330,989.66 USD | 727,219.77 USD | `26 orders` | `+0.03%` | `-` |
| `ASK` | `100.11` | `1522.3600` | 152,403.46 USD | 879,623.23 USD | `18 orders` | `+0.04%` | `-` |
| `ASK` | `100.12` | `3248.0500` | 325,194.77 USD | 1,204,817.99 USD | `16 orders` | `+0.05%` | `-` |
| `ASK` | `100.13` | `1826.3900` | 182,876.43 USD | 1,387,694.42 USD | `19 orders` | `+0.06%` | `-` |
| `ASK` | `100.14` | `2594.4600` | 259,809.22 USD | 1,647,503.65 USD | `11 orders` | `+0.07%` | `-` |
| `ASK` | `100.15` | `1070.7900` | 107,239.62 USD | 1,754,743.27 USD | `16 orders` | `+0.08%` | `-` |
| `ASK` | `100.16` | `4764.0300` | 477,165.24 USD | 2,231,908.51 USD | `17 orders` | `+0.09%` | `-` |
| `ASK` | `100.17` | `3674.8900` | 368,113.73 USD | 2,600,022.24 USD | `16 orders` | `+0.10%` | `-` |
| `ASK` | `100.18` | `1502.4800` | 150,518.45 USD | 2,750,540.69 USD | `12 orders` | `+0.11%` | `-` |
| `ASK` | `100.19` | `3841.0600` | 384,835.80 USD | 3,135,376.49 USD | `13 orders` | `+0.12%` | `-` |
| `ASK` | `100.20` | `690.6500` | 69,203.13 USD | 3,204,579.62 USD | `12 orders` | `+0.13%` | `-` |
| `ASK` | `100.21` | `3235.3400` | 324,213.42 USD | 3,528,793.04 USD | `12 orders` | `+0.14%` | `-` |
| `ASK` | `100.22` | `1264.6400` | 126,742.22 USD | 3,655,535.26 USD | `12 orders` | `+0.15%` | `-` |
| `ASK` | `100.23` | `4755.7200` | 476,665.82 USD | 4,132,201.08 USD | `13 orders` | `+0.16%` | `-` |
| `ASK` | `100.24` | `1762.8300` | 176,706.08 USD | 4,308,907.16 USD | `10 orders` | `+0.17%` | `-` |
| `ASK` | `100.25` | `4802.1000` | 481,410.53 USD | 4,790,317.68 USD | `14 orders` | `+0.18%` | `-` |
| `ASK` | `100.26` | `249.7200` | 25,036.93 USD | 4,815,354.61 USD | `5 orders` | `+0.19%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:23:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `14` | `0x5b5d...c060` | `SHORT` | 72,145,372.61 USD | `721,165.26` | `94.33` | `100.05` | `316.86` | -4,114,482.20 USD | `-5.70%` | `7X Cross` |
| `21` | `0x9c6a...a4ed` | `LONG` | 55,030,772.51 USD | `550,087.69` | `80.86` | `100.05` | `68.18` | 10,551,786.12 USD | `+19.17%` | `20X Cross` |
| `48` | `0xb83d...6e36` | `SHORT` | 25,937,781.00 USD | `259,300.02` | `91.42` | `100.05` | `609.67` | -2,232,647.98 USD | `-8.61%` | `5X Cross` |
| `78` | `0x3dc9...54b0` | `SHORT` | 22,008,819.01 USD | `220,000.19` | `105.90` | `100.05` | `165.84` | 1,290,288.27 USD | `+5.86%` | `20X Cross` |
| `101` | `0x9c89...600e` | `LONG` | 18,954,828.90 USD | `189,472.50` | `115.21` | `100.05` | `34.72` | -2,874,186.36 USD | `-15.16%` | `20X Cross` |
| `113` | `0x4a20...3c26` | `LONG` | 18,005,400.00 USD | `180,000.00` | `106.43` | `100.05` | `65.46` | -1,152,878.71 USD | `-6.40%` | `20X Cross` |
| `136` | `0xecb6...2b00` | `SHORT` | 15,017,508.60 USD | `150,115.04` | `102.72` | `100.05` | `282.78` | 402,118.34 USD | `+2.68%` | `20X Cross` |
| `221` | `0x7a5a...0394` | `SHORT` | 10,225,164.63 USD | `102,220.98` | `100.91` | `100.05` | `126.21` | 89,473.20 USD | `+0.88%` | `10X Cross` |
| `230` | `0xc63a...a3cd` | `LONG` | 10,003,000.00 USD | `100,000.00` | `112.22` | `100.05` | `0.000000` | -1,219,108.97 USD | `-12.19%` | `20X Cross` |
| `245` | `0x13da...08be` | `LONG` | 9,574,000.34 USD | `95,711.29` | `100.55` | `100.05` | `98.09` | -49,740.34 USD | `-0.52%` | `20X Isolated` |
| `269` | `0xb581...6f4f` | `LONG` | 9,003,600.00 USD | `90,000.00` | `114.59` | `100.05` | `0.000000` | -1,309,692.29 USD | `-14.55%` | `3X Cross` |
| `290` | `0x645b...87b8` | `SHORT` | 8,363,873.21 USD | `83,605.29` | `103.91` | `100.05` | `335.22` | 323,255.95 USD | `+3.86%` | `20X Cross` |
| `299` | `0xdb3a...cf3b` | `LONG` | 8,187,633.55 USD | `81,851.78` | `106.04` | `100.05` | `47.16` | -492,113.30 USD | `-6.01%` | `4X Cross` |
| `318` | `0xe927...98ef` | `LONG` | 7,804,680.00 USD | `78,000.00` | `96.34` | `100.05` | `38.44` | 290,538.52 USD | `+3.72%` | `3X Cross` |
| `326` | `0xca49...53c8` | `SHORT` | 7,396,563.30 USD | `73,943.45` | `110.70` | `100.05` | `273.89` | 789,058.96 USD | `+10.67%` | `20X Cross` |
| `329` | `0x8ae4...3d60` | `LONG` | 7,220,552.96 USD | `72,180.05` | `111.72` | `100.05` | `1.84` | -843,607.28 USD | `-11.68%` | `10X Cross` |
| `336` | `0xa0b7...6165` | `SHORT` | 7,114,388.22 USD | `71,044.42` | `107.87` | `100.05` | `190.90` | 549,078.98 USD | `+7.72%` | `2X Cross` |
| `351` | `0xf517...c032` | `SHORT` | 6,779,886.36 USD | `67,778.53` | `84.64` | `100.05` | `228.33` | -1,042,855.19 USD | `-15.38%` | `20X Cross` |
| `479` | `0x7e23...5a5a` | `LONG` | 4,858,398.58 USD | `48,564.56` | `105.17` | `100.05` | `78.11` | -249,170.58 USD | `-5.13%` | `5X Isolated` |
| `579` | `0x2e2b...2fab` | `LONG` | 4,001,600.00 USD | `40,000.00` | `119.55` | `100.05` | `53.98` | -780,435.64 USD | `-19.50%` | `10X Cross` |
| `584` | `0x7fda...17d1` | `SHORT` | 3,978,955.95 USD | `39,773.65` | `103.76` | `100.05` | `1002.52` | 147,909.67 USD | `+3.72%` | `20X Cross` |
| `603` | `0xf899...88db` | `SHORT` | 3,860,170.45 USD | `38,586.27` | `87.86` | `100.05` | `117.02` | -469,795.26 USD | `-12.17%` | `20X Cross` |
| `617` | `0x9946...0852` | `SHORT` | 3,779,613.54 USD | `37,784.80` | `112.11` | `100.05` | `129.71` | 456,613.77 USD | `+12.08%` | `20X Cross` |
| `642` | `0x27b8...12fc` | `LONG` | 3,610,016.43 USD | `36,085.73` | `110.86` | `100.05` | `14.05` | -390,328.82 USD | `-10.81%` | `10X Cross` |
| `648` | `0x9c16...4a6f` | `SHORT` | 3,578,988.37 USD | `35,779.15` | `90.45` | `100.05` | `128.60` | -342,883.34 USD | `-9.58%` | `20X Cross` |
| `652` | `0x3440...32c5` | `SHORT` | 3,553,977.87 USD | `35,529.12` | `95.02` | `100.05` | `167.31` | -177,956.44 USD | `-5.01%` | `20X Cross` |
| `734` | `0x96a7...79df` | `LONG` | 3,201,280.00 USD | `32,000.00` | `74.39` | `100.05` | `0.000000` | 820,874.15 USD | `+25.64%` | `20X Cross` |
| `735` | `0x023a...2355` | `SHORT` | 3,198,386.84 USD | `31,971.08` | `101.46` | `100.05` | `360.77` | 45,294.93 USD | `+1.42%` | `20X Cross` |
| `779` | `0xbe19...8bd1` | `SHORT` | 3,046,082.55 USD | `30,451.69` | `97.62` | `100.05` | `741.21` | -73,535.92 USD | `-2.41%` | `3X Cross` |
| `781` | `0x482b...cae4` | `SHORT` | 3,031,958.31 USD | `30,310.49` | `88.03` | `100.05` | `154.72` | -363,710.03 USD | `-12.00%` | `20X Cross` |
| `793` | `0x610b...b613` | `LONG` | 2,964,599.37 USD | `29,634.14` | `101.23` | `100.05` | `70.39` | -35,399.98 USD | `-1.19%` | `3X Isolated` |
| `794` | `0xfc66...ca06` | `SHORT` | 2,957,108.37 USD | `29,559.26` | `102.17` | `100.05` | `1289.43` | 62,877.93 USD | `+2.13%` | `20X Cross` |
| `804` | `0x45d2...4029` | `SHORT` | 2,922,876.60 USD | `29,220.00` | `93.28` | `100.05` | `1368.58` | -197,100.62 USD | `-6.74%` | `20X Cross` |
| `813` | `0xa61c...66b9` | `LONG` | 2,889,666.64 USD | `28,888.00` | `104.39` | `100.05` | `0.000000` | -125,897.48 USD | `-4.36%` | `5X Cross` |
| `845` | `0x458d...ab3b` | `LONG` | 2,740,146.10 USD | `27,385.03` | `117.17` | `100.05` | `81.07` | -468,516.42 USD | `-17.10%` | `3X Isolated` |
| `885` | `0xfc27...9d9d` | `SHORT` | 2,580,129.81 USD | `25,793.56` | `102.76` | `100.05` | `656.03` | 70,357.99 USD | `+2.73%` | `20X Cross` |
| `913` | `0x051c...693c` | `LONG` | 2,514,975.59 USD | `25,139.70` | `89.76` | `100.05` | `22.94` | 258,414.26 USD | `+10.28%` | `20X Cross` |
| `949` | `0x638f...f5f0` | `LONG` | 2,400,720.00 USD | `24,000.00` | `136.71` | `100.05` | `42.22` | -880,248.54 USD | `-36.67%` | `20X Cross` |
| `1012` | `0x7178...0854` | `LONG` | 2,255,200.36 USD | `22,545.24` | `110.94` | `100.05` | `30.65` | -245,944.12 USD | `-10.91%` | `10X Cross` |
| `1029` | `0x739c...cfb2` | `LONG` | 2,200,880.00 USD | `22,000.00` | `91.95` | `100.05` | `72.92` | 177,972.69 USD | `+8.09%` | `20X Cross` |
| `1038` | `0x69cc...14fd` | `SHORT` | 2,170,808.05 USD | `21,701.57` | `99.01` | `100.05` | `460.77` | -22,155.30 USD | `-1.02%` | `20X Cross` |
| `1065` | `0xb90d...870c` | `SHORT` | 2,112,854.80 USD | `21,120.10` | `102.00` | `100.05` | `111.36` | 41,469.97 USD | `+1.96%` | `20X Cross` |
| `1103` | `0x7737...bf66` | `SHORT` | 2,039,017.52 USD | `20,384.06` | `102.94` | `100.05` | `976.50` | 59,324.37 USD | `+2.91%` | `10X Cross` |
| `1132` | `0xea00...a918` | `LONG` | 2,003,069.91 USD | `20,022.69` | `66.09` | `100.05` | `0.000000` | 679,761.31 USD | `+33.94%` | `20X Cross` |
| `1136` | `0xbfc7...80b4` | `SHORT` | 2,000,800.00 USD | `20,000.00` | `85.98` | `100.05` | `326.78` | -281,265.50 USD | `-14.06%` | `20X Cross` |
| `1137` | `0x3fc5...c0c1` | `SHORT` | 2,000,800.00 USD | `20,000.00` | `98.28` | `100.05` | `204.07` | -35,240.16 USD | `-1.76%` | `20X Cross` |
| `1138` | `0xdf60...d3c7` | `LONG` | 2,000,800.00 USD | `20,000.00` | `120.12` | `100.05` | `94.00` | -401,608.53 USD | `-20.07%` | `7X Isolated` |
| `1139` | `0x5986...89d9` | `LONG` | 2,000,800.00 USD | `20,000.00` | `101.84` | `100.05` | `46.08` | -35,997.53 USD | `-1.80%` | `20X Cross` |
| `1140` | `0x251f...6e5d` | `LONG` | 2,000,600.00 USD | `20,000.00` | `101.15` | `100.05` | `46.36` | -22,497.77 USD | `-1.12%` | `20X Cross` |
| `1156` | `0xb322...d51f` | `LONG` | 1,978,075.24 USD | `19,774.82` | `102.98` | `100.05` | `55.65` | -58,396.16 USD | `-2.95%` | `20X Cross` |
| `1166` | `0x34e6...8d74` | `LONG` | 1,969,397.64 USD | `19,688.07` | `101.19` | `100.05` | `53.20` | -22,766.15 USD | `-1.16%` | `20X Cross` |
| `1183` | `0x936c...bb0f` | `SHORT` | 1,944,559.51 USD | `19,437.82` | `105.65` | `100.05` | `636.59` | 108,954.87 USD | `+5.60%` | `20X Cross` |
| `1185` | `0x7160...d47c` | `LONG` | 1,943,993.02 USD | `19,434.10` | `105.03` | `100.05` | `80.38` | -97,228.27 USD | `-5.00%` | `20X Cross` |
| `1205` | `0xe097...d0fe` | `LONG` | 1,900,144.87 USD | `18,995.75` | `109.71` | `100.05` | `0.000000` | -183,852.02 USD | `-9.68%` | `20X Cross` |
| `1293` | `0xe98b...8cd5` | `SHORT` | 1,762,993.92 USD | `17,622.89` | `187.95` | `100.05` | `260.53` | 1,549,226.81 USD | `+87.87%` | `20X Cross` |
| `1310` | `0xdf95...7d72` | `SHORT` | 1,745,037.74 USD | `17,443.40` | `104.70` | `100.05` | `2211.33` | 81,225.92 USD | `+4.65%` | `20X Cross` |
| `1333` | `0xee2b...d67e` | `LONG` | 1,696,827.90 USD | `16,963.19` | `119.86` | `100.05` | `20.70` | -336,443.74 USD | `-19.83%` | `4X Cross` |
| `1341` | `0x123d...3bff` | `LONG` | 1,692,519.74 USD | `16,918.43` | `89.53` | `100.05` | `0.000000` | 177,733.25 USD | `+10.50%` | `10X Cross` |
| `1369` | `0x7277...0b98` | `SHORT` | 1,660,809.09 USD | `16,603.11` | `101.18` | `100.05` | `179.10` | 19,119.11 USD | `+1.15%` | `20X Cross` |
| `1450` | `0x73d7...8be1` | `LONG` | 1,567,365.07 USD | `15,668.95` | `106.60` | `100.05` | `70.36` | -102,975.89 USD | `-6.57%` | `20X Cross` |
| `1460` | `0xc74a...ab93` | `LONG` | 1,554,458.84 USD | `15,536.82` | `64.06` | `100.05` | `54.88` | 559,230.01 USD | `+35.98%` | `5X Isolated` |
| `1505` | `0xc7d1...51af` | `SHORT` | 1,500,600.00 USD | `15,000.00` | `105.79` | `100.05` | `138.76` | 86,275.00 USD | `+5.75%` | `20X Cross` |
| `1541` | `0xffb2...5ed6` | `LONG` | 1,450,985.16 USD | `14,504.05` | `117.89` | `100.05` | `89.66` | -258,919.55 USD | `-17.84%` | `20X Cross` |
| `1566` | `0x0d6a...ca57` | `LONG` | 1,421,233.27 USD | `14,206.65` | `110.41` | `100.05` | `91.59` | -147,357.09 USD | `-10.37%` | `5X Isolated` |
| `1850` | `0x2482...0e55` | `LONG` | 1,136,852.56 USD | `11,363.98` | `122.03` | `100.05` | `94.24` | -249,849.36 USD | `-21.98%` | `20X Isolated` |
| `1871` | `0xe105...6a47` | `LONG` | 1,120,841.15 USD | `11,205.05` | `107.11` | `100.05` | `92.14` | -79,315.90 USD | `-7.08%` | `20X Cross` |
| `1883` | `0x45db...86eb` | `LONG` | 1,110,333.00 USD | `11,100.00` | `110.69` | `100.05` | `67.97` | -118,348.90 USD | `-10.66%` | `5X Cross` |
| `1911` | `0x1d04...7c43` | `LONG` | 1,081,824.71 USD | `10,811.76` | `111.55` | `100.05` | `19.90` | -124,236.79 USD | `-11.48%` | `6X Cross` |
| `1959` | `0xa6a1...29eb` | `LONG` | 1,042,698.24 USD | `10,420.73` | `100.78` | `100.05` | `0.000000` | -7,532.14 USD | `-0.72%` | `20X Cross` |
| `2044` | `0x0daf...47e0` | `SHORT` | 1,000,353.00 USD | `10,000.00` | `99.07` | `100.05` | `251.18` | -9,640.78 USD | `-0.96%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `130.74` | 1,361.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.36K USD at 130.7400 USD [API] | `2026-01-21 15:16:43` |
| `ANNOUNCEMENT` | `INFO` | `122.75` | 4,485.28 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.49K USD at 122.7500 USD [API] | `2025-12-23 13:36:37` |
| `ANNOUNCEMENT` | `INFO` | `124.95` | 3,751.00 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 3.75K USD at 124.9500 USD [API] | `2025-12-19 07:07:44` |
| `ANNOUNCEMENT` | `INFO` | `124.95` | 820.92 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 0.82K USD at 124.9500 USD [API] | `2025-12-19 07:07:44` |
| `ANNOUNCEMENT` | `INFO` | `126.81` | 3,182.93 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 3.18K USD at 126.8100 USD [API] | `2025-12-17 15:52:14` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,808.50 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.81K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,998.67 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 2.00K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `125.94` | 1,510.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 1.51K USD at 125.9400 USD [API] | `2025-12-15 16:36:52` |
| `ANNOUNCEMENT` | `INFO` | `129.25` | 4,809.39 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 4.81K USD at 129.2500 USD [API] | `2025-12-14 23:27:00` |
| `ANNOUNCEMENT` | `INFO` | `134.26` | 5,544.94 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 5.54K USD at 134.2600 USD [API] | `2025-12-11 18:35:47` |
| `ANNOUNCEMENT` | `INFO` | `128.92` | 6,032.17 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.03K USD at 128.9200 USD [API] | `2025-12-07 14:24:53` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 6,367.77 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 6.37K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 19.68 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.02K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 12.65 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.01K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `140.60` | 202.46 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Long: 0.20K USD at 140.6000 USD [API] | `2025-12-04 18:46:05` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 1,588.63 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.59K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 2,040.30 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.04K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `129.79` | 2,710.02 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.71K USD at 129.7900 USD [API] | `2025-12-02 13:16:02` |
| `ANNOUNCEMENT` | `INFO` | `140.45` | 1,543.55 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 1.54K USD at 140.4500 USD [API] | `2025-11-25 23:19:31` |
| `ANNOUNCEMENT` | `INFO` | `140.45` | 2,490.18 USD | `-` | `NEWS_INTEL` | `-` | #SOL Liquidated Short: 2.49K USD at 140.4500 USD [API] | `2025-11-25 23:19:31` |
| `ANNOUNCEMENT` | `INFO` | `101.15` | 86,233.41 USD | `-` | `NEWS_INTEL` | `-` | #SOL Whale SELL: 86.23K USD at 101.1500 USD [API] | `2026-10-27 23:35:20` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.65` (Vol: 2,900,000.00 USD, Dist: `+3.51%`) | Long MP=`98.78` (Vol: 4,200,000.00 USD, Dist: `--1.35%`)
  * 48H Horizon: Short MP=`104.08` (Vol: 4,800,000.00 USD, Dist: `+3.95%`) | Long MP=`99.30` (Vol: 5,000,000.00 USD, Dist: `--0.83%`)
  * 3D Horizon: Short MP=`104.03` (Vol: 4,200,000.00 USD, Dist: `+3.90%`) | Long MP=`99.07` (Vol: 5,800,000.00 USD, Dist: `--1.06%`)
  * 7D Horizon: Short MP=`104.05` (Vol: 6,100,000.00 USD, Dist: `+3.91%`) | Long MP=`98.63` (Vol: 8,800,000.00 USD, Dist: `--1.50%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `20.50` | 23,250.00 USD | 141,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.50` | 544,040.00 USD | 141,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.50` | 62,010.00 USD | 140,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.50` | 62,020.00 USD | 140,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.50` | 645,300.00 USD | 140,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.50` | 58,760.00 USD | 140,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.50` | 18,480.00 USD | 140,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 17,520.00 USD | 140,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 190,510.00 USD | 140,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 45,390.00 USD | 139,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 308,240.00 USD | 139,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 876,640.00 USD | 139,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 18,410.00 USD | 138,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.50` | 7,870.00 USD | 138,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 6,590,000.00 USD | 138,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 175,700.00 USD | 131,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.50` | 66,810.00 USD | 131,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.50` | 234,310.00 USD | 131,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 3,020,000.00 USD | 131,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.50` | 57,940.00 USD | 128,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 76,680.00 USD | 128,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 29,060.00 USD | 128,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.50` | 1,040,000.00 USD | 128,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 155,310.00 USD | 127,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 216,380.00 USD | 127,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 60,640.00 USD | 126,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.50` | 4,760,000.00 USD | 126,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.50` | 144,140.00 USD | 122,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.50` | 1,040,000.00 USD | 121,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 76,710.00 USD | 120,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.50` | 95,290.00 USD | 120,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 745,920.00 USD | 120,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `52.50` | 191,460.00 USD | 119,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.50` | 3,380,000.00 USD | 119,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 1,160,000.00 USD | 116,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 190,340.00 USD | 115,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,260,000.00 USD | 115,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 453,280.00 USD | 113,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 238,880.00 USD | 113,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.50` | 140,510.00 USD | 113,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 188,530.00 USD | 112,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 215,540.00 USD | 112,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 209,880.00 USD | 112,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 277,870.00 USD | 112,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.50` | 144,330.00 USD | 112,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 11,970,000.00 USD | 111,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 93,730.00 USD | 99,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 1,050,000.00 USD | 99,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 37,980,000.00 USD | 98,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 166,780.00 USD | 60,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 2,440,000.00 USD | 60,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 1,410,000.00 USD | 58,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 2,200,000.00 USD | 56,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 593,320.00 USD | 54,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 614,790.00 USD | 54,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 754,900.00 USD | 53,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 203,660.00 USD | 52,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 1,430,000.00 USD | 52,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,940,000.00 USD | 51,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 333,690.00 USD | 46,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.50` | 2,060,000.00 USD | 45,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.50` | 2,610,000.00 USD | 43,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 1,470,000.00 USD | 41,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 739,670.00 USD | 39,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 710,900.00 USD | 38,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 879,320.00 USD | 38,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 839,590.00 USD | 37,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,450,000.00 USD | 36,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 3,950,000.00 USD | 34,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 1,940,000.00 USD | 31,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `89.80` | 384,700,000.00 USD | 384,700,000.00 USD | 950,870.00 USD | 471,760.00 USD | 639,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.00` | 190,270,000.00 USD | 190,270,000.00 USD | 475,910.00 USD | 591,730.00 USD | 620,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.00` | 382,630,000.00 USD | 382,630,000.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.20` | 188,590,000.00 USD | 188,590,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.20` | 380,910,000.00 USD | 380,910,000.00 USD | 1,250,000.00 USD | 573,800.00 USD | 724,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.40` | 187,260,000.00 USD | 187,260,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.40` | 378,360,000.00 USD | 378,360,000.00 USD | 796,240.00 USD | 30,920.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `90.50` | 374,770.00 USD | 29,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `90.60` | 185,900,000.00 USD | 185,900,000.00 USD | 270,180.00 USD | 392,650.00 USD | 477,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.60` | 376,840,000.00 USD | 376,840,000.00 USD | 978,100.00 USD | 994,460.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `90.80` | 184,760,000.00 USD | 184,760,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `90.80` | 373,720,000.00 USD | 373,720,000.00 USD | 1,210,000.00 USD | 685,900.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.00` | 184,550,000.00 USD | 184,550,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.00` | 370,740,000.00 USD | 370,740,000.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.20` | 184,370,000.00 USD | 184,370,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.20` | 368,680,000.00 USD | 368,680,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.40` | 184,340,000.00 USD | 184,340,000.00 USD | 3,800.00 USD | 125,680.00 USD | 43,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.40` | 366,350,000.00 USD | 366,350,000.00 USD | 1,180,000.00 USD | 1,000,000.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `91.50` | 3,160,000.00 USD | 28,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `91.60` | 184,160,000.00 USD | 184,160,000.00 USD | 25,530.00 USD | 96,080.00 USD | 1,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.60` | 363,030,000.00 USD | 363,030,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `91.80` | 184,040,000.00 USD | 184,040,000.00 USD | 229,430.00 USD | 103,030.00 USD | 11,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `91.80` | 361,400,000.00 USD | 361,400,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.00` | 183,700,000.00 USD | 183,700,000.00 USD | 137,240.00 USD | 74,290.00 USD | 90,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.00` | 359,200,000.00 USD | 359,200,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.20` | 183,390,000.00 USD | 183,390,000.00 USD | 153,400.00 USD | 41,040.00 USD | 107,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.20` | 357,460,000.00 USD | 357,460,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.40` | 183,090,000.00 USD | 183,090,000.00 USD | 145,850.00 USD | 72,380.00 USD | 782,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.40` | 356,600,000.00 USD | 356,600,000.00 USD | 415,170.00 USD | 289,690.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `92.50` | 2,250,000.00 USD | 25,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `92.60` | 182,090,000.00 USD | 182,090,000.00 USD | 31,270.00 USD | 106,430.00 USD | 115,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.60` | 354,690,000.00 USD | 354,690,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `92.80` | 181,840,000.00 USD | 181,840,000.00 USD | 55,570.00 USD | 0.00 USD | 98,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `92.80` | 353,610,000.00 USD | 353,610,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.00` | 181,680,000.00 USD | 181,680,000.00 USD | 45,270.00 USD | 0.00 USD | 120,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.00` | 353,390,000.00 USD | 353,390,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.20` | 181,520,000.00 USD | 181,520,000.00 USD | 0.00 USD | 54,140.00 USD | 155,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.20` | 353,000,000.00 USD | 353,000,000.00 USD | 54,470.00 USD | 4,160.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `93.40` | 181,310,000.00 USD | 181,310,000.00 USD | 0.00 USD | 51,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.40` | 352,890,000.00 USD | 352,890,000.00 USD | 11,220.00 USD | 2,430.00 USD | 1,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `93.50` | 3,120,000.00 USD | 23,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `93.60` | 352,870,000.00 USD | 352,870,000.00 USD | 238,200.00 USD | 299,520.00 USD | 114,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `93.80` | 352,220,000.00 USD | 352,220,000.00 USD | 349,450.00 USD | 179,760.00 USD | 146,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.00` | 351,540,000.00 USD | 351,540,000.00 USD | 78,790.00 USD | 153,680.00 USD | 64,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.20` | 351,250,000.00 USD | 351,250,000.00 USD | 172,550.00 USD | 229,720.00 USD | 258,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.40` | 350,590,000.00 USD | 350,590,000.00 USD | 109,990.00 USD | 0.00 USD | 184,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `94.50` | 2,970,000.00 USD | 20,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `94.60` | 350,290,000.00 USD | 350,290,000.00 USD | 79,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `94.80` | 350,210,000.00 USD | 350,210,000.00 USD | 0.00 USD | 15,050.00 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.00` | 350,190,000.00 USD | 350,190,000.00 USD | 418,320.00 USD | 532,260.00 USD | 13,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.20` | 181,260,000.00 USD | 181,260,000.00 USD | 13,360.00 USD | 0.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.20` | 349,230,000.00 USD | 349,230,000.00 USD | 47,840.00 USD | 200,720.00 USD | 138,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.40` | 181,240,000.00 USD | 181,240,000.00 USD | 321,380.00 USD | 189,450.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.40` | 348,840,000.00 USD | 348,840,000.00 USD | 627,890.00 USD | 225,150.00 USD | 669,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `95.50` | 1,810,000.00 USD | 17,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `95.60` | 180,720,000.00 USD | 180,720,000.00 USD | 906,290.00 USD | 706,940.00 USD | 949,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.60` | 347,320,000.00 USD | 347,320,000.00 USD | 1,740,000.00 USD | 1,320,000.00 USD | 986,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `95.80` | 178,160,000.00 USD | 178,160,000.00 USD | 1,710,000.00 USD | 1,320,000.00 USD | 797,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `95.80` | 343,270,000.00 USD | 343,270,000.00 USD | 1,870,000.00 USD | 1,030,000.00 USD | 1,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.00` | 174,330,000.00 USD | 174,330,000.00 USD | 1,310,000.00 USD | 1,290,000.00 USD | 1,270,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.00` | 339,030,000.00 USD | 339,030,000.00 USD | 1,380,000.00 USD | 1,890,000.00 USD | 3,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.20` | 170,460,000.00 USD | 170,460,000.00 USD | 1,970,000.00 USD | 1,310,000.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.20` | 332,590,000.00 USD | 332,590,000.00 USD | 3,950,000.00 USD | 2,080,000.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.40` | 165,940,000.00 USD | 165,940,000.00 USD | 1,540,000.00 USD | 1,270,000.00 USD | 1,590,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.40` | 323,980,000.00 USD | 323,980,000.00 USD | 3,260,000.00 USD | 643,110.00 USD | 2,910,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `96.50` | 1,350,000.00 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `96.60` | 161,540,000.00 USD | 161,540,000.00 USD | 1,040,000.00 USD | 839,050.00 USD | 934,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.60` | 317,170,000.00 USD | 317,170,000.00 USD | 3,250,000.00 USD | 2,480,000.00 USD | 2,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `96.80` | 158,730,000.00 USD | 158,730,000.00 USD | 327,640.00 USD | 738,000.00 USD | 729,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `96.80` | 309,070,000.00 USD | 309,070,000.00 USD | 3,000,000.00 USD | 2,770,000.00 USD | 2,960,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.00` | 156,930,000.00 USD | 156,930,000.00 USD | 310,450.00 USD | 114,330.00 USD | 170,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.00` | 300,330,000.00 USD | 300,330,000.00 USD | 5,510,000.00 USD | 2,530,000.00 USD | 2,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.20` | 156,340,000.00 USD | 156,340,000.00 USD | 336,680.00 USD | 6,890.00 USD | 336,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.20` | 290,250,000.00 USD | 290,250,000.00 USD | 5,490,000.00 USD | 4,350,000.00 USD | 3,980,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.40` | 155,660,000.00 USD | 155,660,000.00 USD | 821,270.00 USD | 642,050.00 USD | 150,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.40` | 276,430,000.00 USD | 276,430,000.00 USD | 4,530,000.00 USD | 2,410,000.00 USD | 3,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `97.50` | 2,510,000.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `97.60` | 154,040,000.00 USD | 154,040,000.00 USD | 1,940,000.00 USD | 1,700,000.00 USD | 1,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.60` | 266,020,000.00 USD | 266,020,000.00 USD | 5,190,000.00 USD | 5,230,000.00 USD | 4,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `97.80` | 148,480,000.00 USD | 148,480,000.00 USD | 3,790,000.00 USD | 3,090,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `97.80` | 250,670,000.00 USD | 250,670,000.00 USD | 5,700,000.00 USD | 2,970,000.00 USD | 4,790,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.00` | 139,770,000.00 USD | 139,770,000.00 USD | 3,230,000.00 USD | 2,990,000.00 USD | 2,920,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.00` | 237,210,000.00 USD | 237,210,000.00 USD | 7,970,000.00 USD | 7,990,000.00 USD | 8,720,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.20` | 130,630,000.00 USD | 130,630,000.00 USD | 4,520,000.00 USD | 2,920,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.20` | 212,520,000.00 USD | 212,520,000.00 USD | 9,810,000.00 USD | 6,890,000.00 USD | 6,860,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.40` | 120,480,000.00 USD | 120,480,000.00 USD | 5,020,000.00 USD | 3,620,000.00 USD | 4,380,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.40` | 188,970,000.00 USD | 188,970,000.00 USD | 10,080,000.00 USD | 2,950,000.00 USD | 10,690,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `98.50` | 11,170,000.00 USD | 11,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `98.60` | 107,460,000.00 USD | 107,460,000.00 USD | 6,300,000.00 USD | 4,610,000.00 USD | 6,750,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.60` | 165,240,000.00 USD | 165,240,000.00 USD | 13,730,000.00 USD | 10,810,000.00 USD | 10,950,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `98.80` | 89,810,000.00 USD | 89,810,000.00 USD | 7,340,000.00 USD | 6,980,000.00 USD | 5,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `98.80` | 129,750,000.00 USD | 129,750,000.00 USD | 12,600,000.00 USD | 9,880,000.00 USD | 13,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.00` | 70,430,000.00 USD | 70,430,000.00 USD | 5,430,000.00 USD | 5,240,000.00 USD | 5,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.00` | 94,200,000.00 USD | 94,200,000.00 USD | 14,280,000.00 USD | 10,590,000.00 USD | 16,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.20` | 54,130,000.00 USD | 54,130,000.00 USD | 8,120,000.00 USD | 5,060,000.00 USD | 5,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.20` | 52,520,000.00 USD | 52,520,000.00 USD | 16,630,000.00 USD | 7,420,000.00 USD | 8,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.40` | 34,970,000.00 USD | 34,970,000.00 USD | 6,080,000.00 USD | 5,170,000.00 USD | 6,670,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.40` | 20,190,000.00 USD | 20,190,000.00 USD | 3,530,000.00 USD | 599,290.00 USD | 8,830,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `99.50` | 260,560.00 USD | 366,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `99.60` | 17,050,000.00 USD | 17,050,000.00 USD | 3,520,000.00 USD | 3,320,000.00 USD | 2,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.60` | 7,230,000.00 USD | 7,230,000.00 USD | 2,030,000.00 USD | 1,930,000.00 USD | 507,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `99.80` | 7,240,000.00 USD | 7,240,000.00 USD | 1,490,000.00 USD | 2,600,000.00 USD | 3,150,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `99.80` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 490,550.00 USD | 2,270,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.00` | 3,250,000.00 USD | 3,250,000.00 USD | 2,090,000.00 USD | 501,110.00 USD | 657,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.00` | 6,490,000.00 USD | 6,490,000.00 USD | 2,090,000.00 USD | 501,110.00 USD | 657,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.00` | 1,410,000.00 USD | 1,410,000.00 USD | 1,380,000.00 USD | 36,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.00` | 2,830,000.00 USD | 2,830,000.00 USD | 1,380,000.00 USD | 36,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.20` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.40` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.40` | 2,980,000.00 USD | 2,980,000.00 USD | 78,970.00 USD | 68,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `100.50` | 105,480.00 USD | 105,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `100.60` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 167,670.00 USD | 2,790,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.60` | 4,750,000.00 USD | 4,750,000.00 USD | 46,010.00 USD | 245,560.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `100.80` | 10,550,000.00 USD | 10,550,000.00 USD | 274,280.00 USD | 802,330.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `100.80` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 981,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.00` | 17,400,000.00 USD | 17,400,000.00 USD | 5,250,000.00 USD | 1,430,000.00 USD | 175,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.00` | 14,020,000.00 USD | 14,020,000.00 USD | 0.00 USD | 4,560,000.00 USD | 3,730,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.20` | 34,360,000.00 USD | 34,360,000.00 USD | 5,880,000.00 USD | 6,710,000.00 USD | 4,360,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.20` | 28,740,000.00 USD | 28,740,000.00 USD | 6,220,000.00 USD | 3,670,000.00 USD | 4,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.40` | 41,400,000.00 USD | 41,400,000.00 USD | 3,360,000.00 USD | 1,720,000.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.40` | 42,620,000.00 USD | 42,620,000.00 USD | 4,250,000.00 USD | 0.00 USD | 9,630,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `101.50` | 2,210.00 USD | 2,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `101.60` | 61,440,000.00 USD | 61,440,000.00 USD | 4,610,000.00 USD | 2,550,000.00 USD | 12,880,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.60` | 52,460,000.00 USD | 52,460,000.00 USD | 3,650,000.00 USD | 0.00 USD | 6,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `101.80` | 68,010,000.00 USD | 68,010,000.00 USD | 212,730.00 USD | 142,780.00 USD | 6,210,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `101.80` | 61,810,000.00 USD | 61,810,000.00 USD | 2,970,000.00 USD | 453,970.00 USD | 5,920,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.00` | 71,130,000.00 USD | 71,130,000.00 USD | 1,330,000.00 USD | 679,810.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.00` | 64,490,000.00 USD | 64,490,000.00 USD | 843,730.00 USD | 0.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.20` | 77,960,000.00 USD | 77,960,000.00 USD | 3,030,000.00 USD | 1,390,000.00 USD | 2,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.20` | 71,200,000.00 USD | 71,200,000.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,520,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.40` | 82,450,000.00 USD | 82,450,000.00 USD | 1,360,000.00 USD | 569,360.00 USD | 2,560,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.40` | 75,910,000.00 USD | 75,910,000.00 USD | 1,760,000.00 USD | 299,640.00 USD | 2,650,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `102.50` | 39,060.00 USD | 41,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `102.60` | 82,940,000.00 USD | 82,940,000.00 USD | 289,550.00 USD | 190,630.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.60` | 78,330,000.00 USD | 78,330,000.00 USD | 1,400,000.00 USD | 979,270.00 USD | 37,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `102.80` | 86,780,000.00 USD | 86,780,000.00 USD | 1,410,000.00 USD | 1,870,000.00 USD | 563,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `102.80` | 86,210,000.00 USD | 86,210,000.00 USD | 7,600,000.00 USD | 0.00 USD | 277,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.00` | 91,150,000.00 USD | 91,150,000.00 USD | 2,600,000.00 USD | 1,430,000.00 USD | 340,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.00` | 100,730,000.00 USD | 100,730,000.00 USD | 11,690,000.00 USD | 0.00 USD | 2,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.20` | 96,480,000.00 USD | 96,480,000.00 USD | 1,840,000.00 USD | 1,670,000.00 USD | 1,820,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.20` | 115,020,000.00 USD | 115,020,000.00 USD | 13,650,000.00 USD | 4,380.00 USD | 631,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.40` | 103,710,000.00 USD | 103,710,000.00 USD | 3,920,000.00 USD | 1,790,000.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.40` | 130,020,000.00 USD | 130,020,000.00 USD | 12,210,000.00 USD | 219,070.00 USD | 2,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `103.50` | 39,100.00 USD | 80,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `103.60` | 118,100,000.00 USD | 118,100,000.00 USD | 4,250,000.00 USD | 2,110,000.00 USD | 8,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.60` | 148,410,000.00 USD | 148,410,000.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `103.80` | 127,580,000.00 USD | 127,580,000.00 USD | 3,350,000.00 USD | 2,690,000.00 USD | 3,430,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `103.80` | 160,760,000.00 USD | 160,760,000.00 USD | 7,920,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.00` | 137,750,000.00 USD | 137,750,000.00 USD | 3,100,000.00 USD | 3,240,000.00 USD | 3,840,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.00` | 189,180,000.00 USD | 189,180,000.00 USD | 11,400,000.00 USD | 6,910,000.00 USD | 10,110,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.20` | 146,360,000.00 USD | 146,360,000.00 USD | 3,720,000.00 USD | 2,180,000.00 USD | 2,700,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.20` | 210,990,000.00 USD | 210,990,000.00 USD | 8,520,000.00 USD | 7,010,000.00 USD | 6,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.40` | 155,000,000.00 USD | 155,000,000.00 USD | 3,300,000.00 USD | 1,930,000.00 USD | 3,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.40` | 227,960,000.00 USD | 227,960,000.00 USD | 5,100,000.00 USD | 3,700,000.00 USD | 8,170,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `104.50` | 756,860.00 USD | 837,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `104.60` | 163,040,000.00 USD | 163,040,000.00 USD | 2,200,000.00 USD | 1,920,000.00 USD | 3,910,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.60` | 245,520,000.00 USD | 245,520,000.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 6,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `104.80` | 169,340,000.00 USD | 169,340,000.00 USD | 1,630,000.00 USD | 1,620,000.00 USD | 3,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `104.80` | 262,650,000.00 USD | 262,650,000.00 USD | 5,170,000.00 USD | 4,150,000.00 USD | 7,820,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.00` | 171,910,000.00 USD | 171,910,000.00 USD | 708,730.00 USD | 754,560.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.00` | 279,780,000.00 USD | 279,780,000.00 USD | 5,730,000.00 USD | 5,070,000.00 USD | 6,330,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.20` | 173,240,000.00 USD | 173,240,000.00 USD | 514,940.00 USD | 4,110.00 USD | 814,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.20` | 292,490,000.00 USD | 292,490,000.00 USD | 5,340,000.00 USD | 4,850,000.00 USD | 2,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.40` | 174,270,000.00 USD | 174,270,000.00 USD | 299,190.00 USD | 2,770.00 USD | 727,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.40` | 304,450,000.00 USD | 304,450,000.00 USD | 2,960,000.00 USD | 4,450,000.00 USD | 4,540,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `105.50` | 58,280.00 USD | 895,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `105.60` | 175,820,000.00 USD | 175,820,000.00 USD | 273,980.00 USD | 638,670.00 USD | 642,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.60` | 321,920,000.00 USD | 321,920,000.00 USD | 5,650,000.00 USD | 6,010,000.00 USD | 5,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `105.80` | 176,880,000.00 USD | 176,880,000.00 USD | 225,560.00 USD | 542,960.00 USD | 287,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `105.80` | 332,680,000.00 USD | 332,680,000.00 USD | 3,540,000.00 USD | 3,020,000.00 USD | 4,200,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.00` | 177,940,000.00 USD | 177,940,000.00 USD | 377,210.00 USD | 456,530.00 USD | 222,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.00` | 342,660,000.00 USD | 342,660,000.00 USD | 4,000,000.00 USD | 2,430,000.00 USD | 3,550,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.20` | 179,340,000.00 USD | 179,340,000.00 USD | 606,390.00 USD | 420,460.00 USD | 375,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.20` | 357,010,000.00 USD | 357,010,000.00 USD | 6,980,000.00 USD | 3,540,000.00 USD | 3,830,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.40` | 180,440,000.00 USD | 180,440,000.00 USD | 583,540.00 USD | 313,010.00 USD | 207,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.40` | 365,170,000.00 USD | 365,170,000.00 USD | 3,590,000.00 USD | 2,670,000.00 USD | 1,900,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `106.50` | 11,260.00 USD | 906,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `106.60` | 182,970,000.00 USD | 182,970,000.00 USD | 887,290.00 USD | 440,970.00 USD | 1,200,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.60` | 374,380,000.00 USD | 374,380,000.00 USD | 2,470,000.00 USD | 2,360,000.00 USD | 4,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `106.80` | 184,970,000.00 USD | 184,970,000.00 USD | 653,630.00 USD | 182,880.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `106.80` | 380,260,000.00 USD | 380,260,000.00 USD | 1,340,000.00 USD | 1,750,000.00 USD | 2,800,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.00` | 185,960,000.00 USD | 185,960,000.00 USD | 199,140.00 USD | 320,120.00 USD | 464,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.00` | 385,820,000.00 USD | 385,820,000.00 USD | 1,370,000.00 USD | 1,260,000.00 USD | 2,930,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.20` | 186,340,000.00 USD | 186,340,000.00 USD | 138,920.00 USD | 0.00 USD | 245,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.20` | 387,540,000.00 USD | 387,540,000.00 USD | 866,170.00 USD | 389,810.00 USD | 461,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.40` | 186,820,000.00 USD | 186,820,000.00 USD | 113,170.00 USD | 0.00 USD | 363,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.40` | 388,530,000.00 USD | 388,530,000.00 USD | 0.00 USD | 280,650.00 USD | 703,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `107.50` | 351,530.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `107.60` | 187,310,000.00 USD | 187,310,000.00 USD | 47,730.00 USD | 187,760.00 USD | 253,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.60` | 388,890,000.00 USD | 388,890,000.00 USD | 213,520.00 USD | 0.00 USD | 154,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `107.80` | 187,620,000.00 USD | 187,620,000.00 USD | 46,620.00 USD | 128,660.00 USD | 134,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `107.80` | 389,670,000.00 USD | 389,670,000.00 USD | 489,650.00 USD | 10,400.00 USD | 277,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.00` | 389,710,000.00 USD | 389,710,000.00 USD | 25,580.00 USD | 6,070.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.20` | 391,820,000.00 USD | 391,820,000.00 USD | 860,420.00 USD | 826,850.00 USD | 427,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.40` | 394,310,000.00 USD | 394,310,000.00 USD | 1,410,000.00 USD | 528,370.00 USD | 548,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `108.50` | 100,500.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `108.60` | 395,560,000.00 USD | 395,560,000.00 USD | 401,600.00 USD | 515,740.00 USD | 332,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `108.80` | 398,240,000.00 USD | 398,240,000.00 USD | 627,810.00 USD | 1,190,000.00 USD | 855,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.00` | 187,620,000.00 USD | 187,620,000.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.00` | 398,780,000.00 USD | 398,780,000.00 USD | 248,800.00 USD | 112,280.00 USD | 176,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.20` | 187,630,000.00 USD | 187,630,000.00 USD | 7,480.00 USD | 2,460.00 USD | 2,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.20` | 400,000,000.00 USD | 400,000,000.00 USD | 596,270.00 USD | 82,160.00 USD | 544,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.40` | 187,760,000.00 USD | 187,760,000.00 USD | 118,540.00 USD | 6,900.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.40` | 400,340,000.00 USD | 400,340,000.00 USD | 158,460.00 USD | 81,870.00 USD | 92,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `109.50` | 427,240.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `109.60` | 188,420,000.00 USD | 188,420,000.00 USD | 319,220.00 USD | 155,520.00 USD | 184,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.60` | 401,400,000.00 USD | 401,400,000.00 USD | 525,760.00 USD | 188,400.00 USD | 347,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `109.80` | 189,450,000.00 USD | 189,450,000.00 USD | 478,690.00 USD | 349,260.00 USD | 197,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `109.80` | 402,380,000.00 USD | 402,380,000.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.00` | 190,610,000.00 USD | 190,610,000.00 USD | 256,140.00 USD | 449,140.00 USD | 454,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.00` | 404,110,000.00 USD | 404,110,000.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.20` | 191,930,000.00 USD | 191,930,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.20` | 406,660,000.00 USD | 406,660,000.00 USD | 1,250,000.00 USD | 573,800.00 USD | 724,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.40` | 193,290,000.00 USD | 193,290,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.40` | 408,180,000.00 USD | 408,180,000.00 USD | 796,240.00 USD | 30,920.00 USD | 694,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `110.50` | 194,170.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `110.60` | 193,740,000.00 USD | 193,740,000.00 USD | 110,850.00 USD | 104,840.00 USD | 240,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.60` | 409,280,000.00 USD | 409,280,000.00 USD | 506,360.00 USD | 293,650.00 USD | 301,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `110.80` | 194,430,000.00 USD | 194,430,000.00 USD | 159,320.00 USD | 287,810.00 USD | 237,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `110.80` | 411,300,000.00 USD | 411,300,000.00 USD | 471,740.00 USD | 700,800.00 USD | 841,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.00` | 194,640,000.00 USD | 194,640,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.00` | 414,280,000.00 USD | 414,280,000.00 USD | 1,210,000.00 USD | 685,900.00 USD | 1,080,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.20` | 194,830,000.00 USD | 194,830,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.20` | 416,340,000.00 USD | 416,340,000.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `111.40` | 194,850,000.00 USD | 194,850,000.00 USD | 27,610.00 USD | 769.97 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.40` | 418,670,000.00 USD | 418,670,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `111.50` | 88,260.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `111.60` | 419,630,000.00 USD | 419,630,000.00 USD | 662,880.00 USD | 172,700.00 USD | 122,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `111.80` | 421,990,000.00 USD | 421,990,000.00 USD | 515,920.00 USD | 829,010.00 USD | 1,020,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.00` | 423,610,000.00 USD | 423,610,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.20` | 425,820,000.00 USD | 425,820,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.40` | 427,560,000.00 USD | 427,560,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `112.50` | 2,490,000.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `112.60` | 428,420,000.00 USD | 428,420,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `112.80` | 429,290,000.00 USD | 429,290,000.00 USD | 207,390.00 USD | 162,590.00 USD | 505,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.00` | 430,330,000.00 USD | 430,330,000.00 USD | 207,780.00 USD | 127,100.00 USD | 702,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.20` | 431,410,000.00 USD | 431,410,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.40` | 431,630,000.00 USD | 431,630,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `113.50` | 155,490.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `113.60` | 432,020,000.00 USD | 432,020,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `113.80` | 432,030,000.00 USD | 432,030,000.00 USD | 2,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `114.50` | 51,280.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.50` | 2,010,000.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `116.50` | 135,940.00 USD | 6,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `117.50` | 4,860,000.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.50` | 40,610.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `119.50` | 152,830.00 USD | 11,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.50` | 186,470.00 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.50` | 72,730.00 USD | 12,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.50` | 137,850.00 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.50` | 15,050.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.50` | 214,090.00 USD | 12,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `125.50` | 517,660.00 USD | 13,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.50` | 12,720,000.00 USD | 25,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.50` | 769,380.00 USD | 26,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.50` | 5,640,000.00 USD | 32,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.50` | 148,750.00 USD | 32,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 5,500,000.00 USD | 37,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 14,090.00 USD | 37,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 119,170.00 USD | 38,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 175,260.00 USD | 38,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.50` | 30,810.00 USD | 38,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.50` | 1,530,000.00 USD | 39,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 51,040.00 USD | 39,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 225,800.00 USD | 40,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,320,000.00 USD | 42,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 67,400.00 USD | 42,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,080,000.00 USD | 43,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 462,490.00 USD | 43,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 96,220.00 USD | 44,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 62,920.00 USD | 44,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 87,980.00 USD | 44,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 1,030,000.00 USD | 45,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `146.50` | 689,270.00 USD | 45,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.50` | 12,450.00 USD | 45,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.50` | 2,390,000.00 USD | 48,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.50` | 18,880.00 USD | 48,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 38,370.00 USD | 48,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 53,640.00 USD | 48,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 976,210.00 USD | 49,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `153.50` | 416,970.00 USD | 49,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 8,740.00 USD | 49,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 129,920.00 USD | 49,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.50` | 4,840,000.00 USD | 54,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.50` | 1,650,000.00 USD | 56,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 337,110.00 USD | 56,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `159.50` | 82,340.00 USD | 56,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `160.50` | 2,150,000.00 USD | 59,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `161.50` | 215,730.00 USD | 59,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.50` | 145,240.00 USD | 59,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.50` | 1,610.00 USD | 59,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.50` | 209,200.00 USD | 59,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `165.50` | 36,490,000.00 USD | 96,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 337,280.00 USD | 96,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 1,000,000.00 USD | 97,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 6,330,000.00 USD | 103,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 138,280.00 USD | 103,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.50` | 102,300.00 USD | 104,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 3,430.00 USD | 104,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `172.50` | 108,350.00 USD | 104,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 17,240.00 USD | 104,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.50` | 562,640.00 USD | 104,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,370.00 USD | 104,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `176.50` | 27,570.00 USD | 104,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.50` | 78,780.00 USD | 104,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.50` | 4,180.00 USD | 104,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `179.50` | 5,740.00 USD | 104,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.50` | 3,010,000.00 USD | 107,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 289,190.00 USD | 108,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.50` | 28,040.00 USD | 108,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 93,060.00 USD | 108,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.50` | 533,820.00 USD | 108,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 9,460.00 USD | 108,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 793,890.00 USD | 109,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 223,740.00 USD | 109,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.50` | 176,580.00 USD | 109,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 568,880.00 USD | 110,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `190.50` | 13,540,000.00 USD | 124,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 123,640.00 USD | 124,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.50` | 222,880.00 USD | 124,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 160,020.00 USD | 124,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 20,120.00 USD | 124,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 14,910.00 USD | 124,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 62,700.00 USD | 124,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `197.50` | 533,520.00 USD | 125,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `198.50` | 111,020.00 USD | 125,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `199.50` | 52,390.00 USD | 125,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 5,230.00 USD | 125,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `201.50` | 55,500.00 USD | 125,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `20.50` | 141,440,000.00 USD | 0.00 USD | 23,250.00 USD | `-79.63%` | `1,133.91` |
| `Live` | `Long` | `21.50` | 141,420,000.00 USD | 0.00 USD | 544,040.00 USD | `-78.63%` | `25,304.35` |
| `Live` | `Long` | `22.50` | 140,870,000.00 USD | 0.00 USD | 62,010.00 USD | `-77.64%` | `2,756.07` |
| `Live` | `Long` | `23.50` | 140,810,000.00 USD | 0.00 USD | 62,020.00 USD | `-76.65%` | `2,639.24` |
| `Live` | `Long` | `24.50` | 140,750,000.00 USD | 0.00 USD | 645,300.00 USD | `-75.65%` | `26,338.79` |
| `Live` | `Long` | `25.50` | 140,100,000.00 USD | 0.00 USD | 58,760.00 USD | `-74.66%` | `2,304.13` |
| `Live` | `Long` | `26.50` | 140,040,000.00 USD | 0.00 USD | 18,480.00 USD | `-73.67%` | `697.20` |
| `Live` | `Long` | `27.50` | 140,020,000.00 USD | 0.00 USD | 17,520.00 USD | `-72.67%` | `636.97` |
| `Live` | `Long` | `28.50` | 140,010,000.00 USD | 0.00 USD | 190,510.00 USD | `-71.68%` | `6,684.52` |
| `Live` | `Long` | `29.50` | 139,820,000.00 USD | 0.00 USD | 45,390.00 USD | `-70.68%` | `1,538.48` |
| `Live` | `Long` | `30.50` | 139,770,000.00 USD | 0.00 USD | 308,240.00 USD | `-69.69%` | `10,106.09` |
| `Live` | `Long` | `31.50` | 139,460,000.00 USD | 0.00 USD | 876,640.00 USD | `-68.70%` | `27,829.85` |
| `Live` | `Long` | `32.50` | 138,590,000.00 USD | 0.00 USD | 18,410.00 USD | `-67.70%` | `566.60` |
| `Live` | `Long` | `33.50` | 138,570,000.00 USD | 0.00 USD | 7,870.00 USD | `-66.71%` | `235.05` |
| `Live` | `Long` | `34.50` | 138,560,000.00 USD | 0.00 USD | 6,590,000.00 USD | `-65.72%` | `190,908.48` |
| `Live` | `Long` | `35.50` | 131,970,000.00 USD | 0.00 USD | 175,700.00 USD | `-64.72%` | `4,949.32` |
| `Live` | `Long` | `36.50` | 131,800,000.00 USD | 0.00 USD | 66,810.00 USD | `-63.73%` | `1,830.53` |
| `Live` | `Long` | `37.50` | 131,730,000.00 USD | 0.00 USD | 234,310.00 USD | `-62.73%` | `6,248.15` |
| `Live` | `Long` | `38.50` | 131,500,000.00 USD | 0.00 USD | 3,020,000.00 USD | `-61.74%` | `78,450.68` |
| `Live` | `Long` | `39.50` | 128,480,000.00 USD | 0.00 USD | 57,940.00 USD | `-60.75%` | `1,466.71` |
| `Live` | `Long` | `40.50` | 128,420,000.00 USD | 0.00 USD | 76,680.00 USD | `-59.75%` | `1,893.34` |
| `Live` | `Long` | `41.50` | 128,340,000.00 USD | 0.00 USD | 29,060.00 USD | `-58.76%` | `700.31` |
| `Live` | `Long` | `42.50` | 128,310,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-57.76%` | `24,384.40` |
| `Live` | `Long` | `43.50` | 127,280,000.00 USD | 0.00 USD | 155,310.00 USD | `-56.77%` | `3,570.36` |
| `Live` | `Long` | `44.50` | 127,120,000.00 USD | 0.00 USD | 216,380.00 USD | `-55.78%` | `4,862.47` |
| `Live` | `Long` | `45.50` | 126,910,000.00 USD | 0.00 USD | 60,640.00 USD | `-54.78%` | `1,332.78` |
| `Live` | `Long` | `46.50` | 126,840,000.00 USD | 0.00 USD | 4,760,000.00 USD | `-53.79%` | `102,329.93` |
| `Live` | `Long` | `47.50` | 122,090,000.00 USD | 0.00 USD | 144,140.00 USD | `-52.80%` | `3,034.45` |
| `Live` | `Long` | `48.50` | 121,940,000.00 USD | 0.00 USD | 1,040,000.00 USD | `-51.80%` | `21,399.98` |
| `Live` | `Long` | `49.50` | 120,900,000.00 USD | 0.00 USD | 76,710.00 USD | `-50.81%` | `1,549.72` |
| `Live` | `Long` | `50.50` | 120,830,000.00 USD | 0.00 USD | 95,290.00 USD | `-49.81%` | `1,887.00` |
| `Live` | `Long` | `51.50` | 120,730,000.00 USD | 0.00 USD | 745,920.00 USD | `-48.82%` | `14,483.94` |
| `Live` | `Long` | `52.50` | 119,990,000.00 USD | 0.00 USD | 191,460.00 USD | `-47.83%` | `3,646.77` |
| `Live` | `Long` | `53.50` | 119,790,000.00 USD | 0.00 USD | 3,380,000.00 USD | `-46.83%` | `63,257.90` |
| `Live` | `Long` | `54.50` | 116,410,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-45.84%` | `21,299.56` |
| `Live` | `Long` | `55.50` | 115,250,000.00 USD | 0.00 USD | 190,340.00 USD | `-44.85%` | `3,429.52` |
| `Live` | `Long` | `56.50` | 115,060,000.00 USD | 0.00 USD | 1,260,000.00 USD | `-43.85%` | `22,338.98` |
| `Live` | `Long` | `57.50` | 113,800,000.00 USD | 0.00 USD | 453,280.00 USD | `-42.86%` | `7,883.05` |
| `Live` | `Long` | `58.50` | 113,340,000.00 USD | 0.00 USD | 238,880.00 USD | `-41.86%` | `4,083.44` |
| `Live` | `Long` | `59.50` | 113,100,000.00 USD | 0.00 USD | 140,510.00 USD | `-40.87%` | `2,361.54` |
| `Live` | `Long` | `60.50` | 112,960,000.00 USD | 0.00 USD | 188,530.00 USD | `-39.88%` | `3,116.27` |
| `Live` | `Long` | `61.50` | 112,780,000.00 USD | 0.00 USD | 215,540.00 USD | `-38.88%` | `3,504.68` |
| `Live` | `Long` | `62.50` | 112,560,000.00 USD | 0.00 USD | 209,880.00 USD | `-37.89%` | `3,358.11` |
| `Live` | `Long` | `63.50` | 112,350,000.00 USD | 0.00 USD | 277,870.00 USD | `-36.90%` | `4,375.97` |
| `Live` | `Long` | `64.50` | 112,070,000.00 USD | 0.00 USD | 144,330.00 USD | `-35.90%` | `2,237.65` |
| `Live` | `Long` | `65.50` | 111,930,000.00 USD | 0.00 USD | 11,970,000.00 USD | `-34.91%` | `182,672.60` |
| `Live` | `Long` | `66.50` | 99,960,000.00 USD | 0.00 USD | 93,730.00 USD | `-33.91%` | `1,409.40` |
| `Live` | `Long` | `67.50` | 99,870,000.00 USD | 0.00 USD | 1,050,000.00 USD | `-32.92%` | `15,615.65` |
| `Live` | `Long` | `68.50` | 98,820,000.00 USD | 0.00 USD | 37,980,000.00 USD | `-31.93%` | `554,400.53` |
| `Live` | `Long` | `69.50` | 60,840,000.00 USD | 0.00 USD | 166,780.00 USD | `-30.93%` | `2,399.68` |
| `Live` | `Long` | `70.50` | 60,670,000.00 USD | 0.00 USD | 2,440,000.00 USD | `-29.94%` | `34,551.91` |
| `Live` | `Long` | `71.50` | 58,240,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-28.95%` | `19,744.20` |
| `Live` | `Long` | `72.50` | 56,820,000.00 USD | 0.00 USD | 2,200,000.00 USD | `-27.95%` | `30,378.07` |
| `Live` | `Long` | `73.50` | 54,620,000.00 USD | 0.00 USD | 593,320.00 USD | `-26.96%` | `8,072.32` |
| `Live` | `Long` | `74.50` | 54,030,000.00 USD | 0.00 USD | 614,790.00 USD | `-25.96%` | `8,252.21` |
| `Live` | `Long` | `75.50` | 53,410,000.00 USD | 0.00 USD | 754,900.00 USD | `-24.97%` | `9,998.66` |
| `Live` | `Long` | `76.50` | 52,660,000.00 USD | 0.00 USD | 203,660.00 USD | `-23.98%` | `2,662.17` |
| `Live` | `Long` | `77.50` | 52,460,000.00 USD | 0.00 USD | 1,430,000.00 USD | `-22.98%` | `18,436.01` |
| `Live` | `Long` | `78.50` | 51,030,000.00 USD | 0.00 USD | 4,940,000.00 USD | `-21.99%` | `62,983.95` |
| `Live` | `Long` | `79.50` | 46,080,000.00 USD | 0.00 USD | 333,690.00 USD | `-21.00%` | `4,197.36` |
| `Live` | `Long` | `80.50` | 45,750,000.00 USD | 0.00 USD | 2,060,000.00 USD | `-20.00%` | `25,634.79` |
| `Live` | `Long` | `81.50` | 43,690,000.00 USD | 0.00 USD | 2,610,000.00 USD | `-19.01%` | `32,076.77` |
| `Live` | `Long` | `82.50` | 41,070,000.00 USD | 0.00 USD | 1,470,000.00 USD | `-18.01%` | `17,816.94` |
| `Live` | `Long` | `83.50` | 39,600,000.00 USD | 0.00 USD | 739,670.00 USD | `-17.02%` | `8,858.32` |
| `Live` | `Long` | `84.50` | 38,860,000.00 USD | 0.00 USD | 710,900.00 USD | `-16.03%` | `8,413.02` |
| `Live` | `Long` | `85.50` | 38,150,000.00 USD | 0.00 USD | 879,320.00 USD | `-15.03%` | `10,284.44` |
| `Live` | `Long` | `86.50` | 37,270,000.00 USD | 0.00 USD | 839,590.00 USD | `-14.04%` | `9,706.20` |
| `Live` | `Long` | `87.50` | 36,430,000.00 USD | 0.00 USD | 1,450,000.00 USD | `-13.05%` | `16,621.55` |
| `Live` | `Long` | `88.50` | 34,980,000.00 USD | 0.00 USD | 3,950,000.00 USD | `-12.05%` | `44,647.32` |
| `Live` | `Long` | `89.50` | 31,030,000.00 USD | 0.00 USD | 1,940,000.00 USD | `-11.06%` | `21,726.56` |
| `Live` | `Long` | `90.50` | 29,080,000.00 USD | 0.00 USD | 374,770.00 USD | `-10.06%` | `4,141.11` |
| `Live` | `Long` | `91.50` | 28,710,000.00 USD | 0.00 USD | 3,160,000.00 USD | `-9.07%` | `34,499.74` |
| `Live` | `Long` | `92.50` | 25,550,000.00 USD | 0.00 USD | 2,250,000.00 USD | `-8.08%` | `24,325.41` |
| `Live` | `Long` | `93.50` | 23,300,000.00 USD | 0.00 USD | 3,120,000.00 USD | `-7.08%` | `33,408.47` |
| `Live` | `Long` | `94.50` | 20,180,000.00 USD | 0.00 USD | 2,970,000.00 USD | `-6.09%` | `31,393.63` |
| `Live` | `Long` | `95.50` | 17,210,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-5.10%` | `18,936.34` |
| `Live` | `Long` | `96.50` | 15,400,000.00 USD | 0.00 USD | 1,350,000.00 USD | `-4.10%` | `13,989.82` |
| `Live` | `Long` | `97.50` | 14,050,000.00 USD | 0.00 USD | 2,510,000.00 USD | `-3.11%` | `25,762.76` |
| `Live` | `Long` | `98.50` | 11,540,000.00 USD | 0.00 USD | 11,170,000.00 USD | `-2.11%` | `113,431.74` |
| `Live` | `Long` | `99.50` | 366,040.00 USD | 0.00 USD | 260,560.00 USD | `-1.12%` | `2,618.70` |
| `Live` | `Long` | `100.50` | 105,480.00 USD | 0.00 USD | 105,480.00 USD | `-0.13%` | `1,049.56` |
| `Live` | `Short` | `101.50` | 2,210.00 USD | 2,210.00 USD | 0.00 USD | `+0.87%` | `21.78` |
| `Live` | `Short` | `102.50` | 41,270.00 USD | 39,060.00 USD | 0.00 USD | `+1.86%` | `381.03` |
| `Live` | `Short` | `103.50` | 80,360.00 USD | 39,100.00 USD | 0.00 USD | `+2.85%` | `377.74` |
| `Live` | `Short` | `104.50` | 837,220.00 USD | 756,860.00 USD | 0.00 USD | `+3.85%` | `7,242.66` |
| `Live` | `Short` | `105.50` | 895,500.00 USD | 58,280.00 USD | 0.00 USD | `+4.84%` | `552.45` |
| `Live` | `Short` | `106.50` | 906,760.00 USD | 11,260.00 USD | 0.00 USD | `+5.84%` | `105.72` |
| `Live` | `Short` | `107.50` | 1,260,000.00 USD | 351,530.00 USD | 0.00 USD | `+6.83%` | `3,270.03` |
| `Live` | `Short` | `108.50` | 1,360,000.00 USD | 100,500.00 USD | 0.00 USD | `+7.82%` | `926.28` |
| `Live` | `Short` | `109.50` | 1,790,000.00 USD | 427,240.00 USD | 0.00 USD | `+8.82%` | `3,901.70` |
| `Live` | `Short` | `110.50` | 1,980,000.00 USD | 194,170.00 USD | 0.00 USD | `+9.81%` | `1,757.21` |
| `Live` | `Short` | `111.50` | 2,070,000.00 USD | 88,260.00 USD | 0.00 USD | `+10.80%` | `791.60` |
| `Live` | `Short` | `112.50` | 4,560,000.00 USD | 2,490,000.00 USD | 0.00 USD | `+11.80%` | `22,115.34` |
| `Live` | `Short` | `113.50` | 4,710,000.00 USD | 155,490.00 USD | 0.00 USD | `+12.79%` | `1,369.94` |
| `Live` | `Short` | `114.50` | 4,760,000.00 USD | 51,280.00 USD | 0.00 USD | `+13.79%` | `447.86` |
| `Live` | `Short` | `115.50` | 6,780,000.00 USD | 2,010,000.00 USD | 0.00 USD | `+14.78%` | `17,433.68` |
| `Live` | `Short` | `116.50` | 6,910,000.00 USD | 135,940.00 USD | 0.00 USD | `+15.77%` | `1,166.84` |
| `Live` | `Short` | `117.50` | 11,780,000.00 USD | 4,860,000.00 USD | 0.00 USD | `+16.77%` | `41,396.32` |
| `Live` | `Short` | `118.50` | 11,820,000.00 USD | 40,610.00 USD | 0.00 USD | `+17.76%` | `342.71` |
| `Live` | `Short` | `119.50` | 11,970,000.00 USD | 152,830.00 USD | 0.00 USD | `+18.76%` | `1,278.92` |
| `Live` | `Short` | `120.50` | 12,160,000.00 USD | 186,470.00 USD | 0.00 USD | `+19.75%` | `1,547.49` |
| `Live` | `Short` | `121.50` | 12,230,000.00 USD | 72,730.00 USD | 0.00 USD | `+20.74%` | `598.64` |
| `Live` | `Short` | `122.50` | 12,370,000.00 USD | 137,850.00 USD | 0.00 USD | `+21.74%` | `1,125.33` |
| `Live` | `Short` | `123.50` | 12,380,000.00 USD | 15,050.00 USD | 0.00 USD | `+22.73%` | `121.85` |
| `Live` | `Short` | `124.50` | 12,600,000.00 USD | 214,090.00 USD | 0.00 USD | `+23.72%` | `1,719.56` |
| `Live` | `Short` | `125.50` | 13,110,000.00 USD | 517,660.00 USD | 0.00 USD | `+24.72%` | `4,124.79` |
| `Live` | `Short` | `126.50` | 25,830,000.00 USD | 12,720,000.00 USD | 0.00 USD | `+25.71%` | `100,528.45` |
| `Live` | `Short` | `127.50` | 26,600,000.00 USD | 769,380.00 USD | 0.00 USD | `+26.71%` | `6,034.37` |
| `Live` | `Short` | `128.50` | 32,240,000.00 USD | 5,640,000.00 USD | 0.00 USD | `+27.70%` | `43,910.64` |
| `Live` | `Short` | `129.50` | 32,390,000.00 USD | 148,750.00 USD | 0.00 USD | `+28.69%` | `1,148.67` |
| `Live` | `Short` | `130.50` | 37,890,000.00 USD | 5,500,000.00 USD | 0.00 USD | `+29.69%` | `42,147.45` |
| `Live` | `Short` | `131.50` | 37,910,000.00 USD | 14,090.00 USD | 0.00 USD | `+30.68%` | `107.14` |
| `Live` | `Short` | `132.50` | 38,030,000.00 USD | 119,170.00 USD | 0.00 USD | `+31.67%` | `899.37` |
| `Live` | `Short` | `133.50` | 38,200,000.00 USD | 175,260.00 USD | 0.00 USD | `+32.67%` | `1,312.84` |
| `Live` | `Short` | `134.50` | 38,230,000.00 USD | 30,810.00 USD | 0.00 USD | `+33.66%` | `229.10` |
| `Live` | `Short` | `135.50` | 39,760,000.00 USD | 1,530,000.00 USD | 0.00 USD | `+34.66%` | `11,272.94` |
| `Live` | `Short` | `136.50` | 39,810,000.00 USD | 51,040.00 USD | 0.00 USD | `+35.65%` | `373.94` |
| `Live` | `Short` | `137.50` | 40,040,000.00 USD | 225,800.00 USD | 0.00 USD | `+36.64%` | `1,642.19` |
| `Live` | `Short` | `138.50` | 42,350,000.00 USD | 2,320,000.00 USD | 0.00 USD | `+37.64%` | `16,740.33` |
| `Live` | `Short` | `139.50` | 42,420,000.00 USD | 67,400.00 USD | 0.00 USD | `+38.63%` | `483.13` |
| `Live` | `Short` | `140.50` | 43,500,000.00 USD | 1,080,000.00 USD | 0.00 USD | `+39.62%` | `7,710.96` |
| `Live` | `Short` | `141.50` | 43,970,000.00 USD | 462,490.00 USD | 0.00 USD | `+40.62%` | `3,268.45` |
| `Live` | `Short` | `142.50` | 44,060,000.00 USD | 96,220.00 USD | 0.00 USD | `+41.61%` | `675.20` |
| `Live` | `Short` | `143.50` | 44,130,000.00 USD | 62,920.00 USD | 0.00 USD | `+42.61%` | `438.47` |
| `Live` | `Short` | `144.50` | 44,210,000.00 USD | 87,980.00 USD | 0.00 USD | `+43.60%` | `608.89` |
| `Live` | `Short` | `145.50` | 45,250,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+44.59%` | `7,111.90` |
| `Live` | `Short` | `146.50` | 45,940,000.00 USD | 689,270.00 USD | 0.00 USD | `+45.59%` | `4,704.94` |
| `Live` | `Short` | `147.50` | 45,950,000.00 USD | 12,450.00 USD | 0.00 USD | `+46.58%` | `84.38` |
| `Live` | `Short` | `148.50` | 48,340,000.00 USD | 2,390,000.00 USD | 0.00 USD | `+47.57%` | `16,073.53` |
| `Live` | `Short` | `149.50` | 48,360,000.00 USD | 18,880.00 USD | 0.00 USD | `+48.57%` | `126.26` |
| `Live` | `Short` | `150.50` | 48,400,000.00 USD | 38,370.00 USD | 0.00 USD | `+49.56%` | `254.96` |
| `Live` | `Short` | `151.50` | 48,450,000.00 USD | 53,640.00 USD | 0.00 USD | `+50.56%` | `354.05` |
| `Live` | `Short` | `152.50` | 49,420,000.00 USD | 976,210.00 USD | 0.00 USD | `+51.55%` | `6,401.39` |
| `Live` | `Short` | `153.50` | 49,840,000.00 USD | 416,970.00 USD | 0.00 USD | `+52.54%` | `2,716.39` |
| `Live` | `Short` | `154.50` | 49,850,000.00 USD | 8,740.00 USD | 0.00 USD | `+53.54%` | `56.59` |
| `Live` | `Short` | `155.50` | 49,980,000.00 USD | 129,920.00 USD | 0.00 USD | `+54.53%` | `835.52` |
| `Live` | `Short` | `156.50` | 54,820,000.00 USD | 4,840,000.00 USD | 0.00 USD | `+55.52%` | `30,912.73` |
| `Live` | `Short` | `157.50` | 56,470,000.00 USD | 1,650,000.00 USD | 0.00 USD | `+56.52%` | `10,461.37` |
| `Live` | `Short` | `158.50` | 56,800,000.00 USD | 337,110.00 USD | 0.00 USD | `+57.51%` | `2,126.88` |
| `Live` | `Short` | `159.50` | 56,890,000.00 USD | 82,340.00 USD | 0.00 USD | `+58.51%` | `516.24` |
| `Live` | `Short` | `160.50` | 59,040,000.00 USD | 2,150,000.00 USD | 0.00 USD | `+59.50%` | `13,413.09` |
| `Live` | `Short` | `161.50` | 59,250,000.00 USD | 215,730.00 USD | 0.00 USD | `+60.49%` | `1,335.78` |
| `Live` | `Short` | `162.50` | 59,400,000.00 USD | 145,240.00 USD | 0.00 USD | `+61.49%` | `893.79` |
| `Live` | `Short` | `163.50` | 59,400,000.00 USD | 1,610.00 USD | 0.00 USD | `+62.48%` | `9.85` |
| `Live` | `Short` | `164.50` | 59,610,000.00 USD | 209,200.00 USD | 0.00 USD | `+63.47%` | `1,271.73` |
| `Live` | `Short` | `165.50` | 96,100,000.00 USD | 36,490,000.00 USD | 0.00 USD | `+64.47%` | `220,467.98` |
| `Live` | `Short` | `166.50` | 96,430,000.00 USD | 337,280.00 USD | 0.00 USD | `+65.46%` | `2,025.72` |
| `Live` | `Short` | `167.50` | 97,440,000.00 USD | 1,000,000.00 USD | 0.00 USD | `+66.46%` | `5,997.79` |
| `Live` | `Short` | `168.50` | 103,770,000.00 USD | 6,330,000.00 USD | 0.00 USD | `+67.45%` | `37,594.08` |
| `Live` | `Short` | `169.50` | 103,910,000.00 USD | 138,280.00 USD | 0.00 USD | `+68.44%` | `815.84` |
| `Live` | `Short` | `170.50` | 104,010,000.00 USD | 102,300.00 USD | 0.00 USD | `+69.44%` | `600.00` |
| `Live` | `Short` | `171.50` | 104,020,000.00 USD | 3,430.00 USD | 0.00 USD | `+70.43%` | `19.98` |
| `Live` | `Short` | `172.50` | 104,130,000.00 USD | 108,350.00 USD | 0.00 USD | `+71.42%` | `628.11` |
| `Live` | `Short` | `173.50` | 104,140,000.00 USD | 17,240.00 USD | 0.00 USD | `+72.42%` | `99.36` |
| `Live` | `Short` | `174.50` | 104,710,000.00 USD | 562,640.00 USD | 0.00 USD | `+73.41%` | `3,224.32` |
| `Live` | `Short` | `175.50` | 104,710,000.00 USD | 5,370.00 USD | 0.00 USD | `+74.41%` | `30.60` |
| `Live` | `Short` | `176.50` | 104,740,000.00 USD | 27,570.00 USD | 0.00 USD | `+75.40%` | `156.23` |
| `Live` | `Short` | `177.50` | 104,820,000.00 USD | 78,780.00 USD | 0.00 USD | `+76.39%` | `443.83` |
| `Live` | `Short` | `178.50` | 104,820,000.00 USD | 4,180.00 USD | 0.00 USD | `+77.39%` | `23.41` |
| `Live` | `Short` | `179.50` | 104,830,000.00 USD | 5,740.00 USD | 0.00 USD | `+78.38%` | `31.98` |
| `Live` | `Short` | `180.50` | 107,840,000.00 USD | 3,010,000.00 USD | 0.00 USD | `+79.37%` | `16,680.65` |
| `Live` | `Short` | `181.50` | 108,130,000.00 USD | 289,190.00 USD | 0.00 USD | `+80.37%` | `1,593.33` |
| `Live` | `Short` | `182.50` | 108,160,000.00 USD | 28,040.00 USD | 0.00 USD | `+81.36%` | `153.65` |
| `Live` | `Short` | `183.50` | 108,250,000.00 USD | 93,060.00 USD | 0.00 USD | `+82.36%` | `507.13` |
| `Live` | `Short` | `184.50` | 108,780,000.00 USD | 533,820.00 USD | 0.00 USD | `+83.35%` | `2,893.35` |
| `Live` | `Short` | `185.50` | 108,790,000.00 USD | 9,460.00 USD | 0.00 USD | `+84.34%` | `50.99` |
| `Live` | `Short` | `186.50` | 109,590,000.00 USD | 793,890.00 USD | 0.00 USD | `+85.34%` | `4,256.77` |
| `Live` | `Short` | `187.50` | 109,810,000.00 USD | 223,740.00 USD | 0.00 USD | `+86.33%` | `1,193.30` |
| `Live` | `Short` | `188.50` | 109,990,000.00 USD | 176,580.00 USD | 0.00 USD | `+87.32%` | `936.76` |
| `Live` | `Short` | `189.50` | 110,560,000.00 USD | 568,880.00 USD | 0.00 USD | `+88.32%` | `3,002.01` |
| `Live` | `Short` | `190.50` | 124,090,000.00 USD | 13,540,000.00 USD | 0.00 USD | `+89.31%` | `71,053.17` |
| `Live` | `Short` | `191.50` | 124,210,000.00 USD | 123,640.00 USD | 0.00 USD | `+90.31%` | `645.65` |
| `Live` | `Short` | `192.50` | 124,440,000.00 USD | 222,880.00 USD | 0.00 USD | `+91.30%` | `1,157.80` |
| `Live` | `Short` | `193.50` | 124,600,000.00 USD | 160,020.00 USD | 0.00 USD | `+92.29%` | `826.98` |
| `Live` | `Short` | `194.50` | 124,620,000.00 USD | 20,120.00 USD | 0.00 USD | `+93.29%` | `103.43` |
| `Live` | `Short` | `195.50` | 124,630,000.00 USD | 14,910.00 USD | 0.00 USD | `+94.28%` | `76.28` |
| `Live` | `Short` | `196.50` | 124,700,000.00 USD | 62,700.00 USD | 0.00 USD | `+95.28%` | `319.06` |
| `Live` | `Short` | `197.50` | 125,230,000.00 USD | 533,520.00 USD | 0.00 USD | `+96.27%` | `2,701.39` |
| `Live` | `Short` | `198.50` | 125,340,000.00 USD | 111,020.00 USD | 0.00 USD | `+97.26%` | `559.31` |
| `Live` | `Short` | `199.50` | 125,390,000.00 USD | 52,390.00 USD | 0.00 USD | `+98.26%` | `262.61` |
| `Live` | `Short` | `200.50` | 125,400,000.00 USD | 5,230.00 USD | 0.00 USD | `+99.25%` | `26.07` |
| `Live` | `Short` | `201.50` | 125,450,000.00 USD | 55,500.00 USD | 0.00 USD | `+100.24%` | `275.42` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `23.50` | 10,870,000.00 USD | 0.00 USD | 15,240.00 USD | `-76.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.50` | 10,850,000.00 USD | 0.00 USD | 3,830.00 USD | `-74.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `26.50` | 10,850,000.00 USD | 0.00 USD | 105.20 USD | `-73.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.50` | 10,850,000.00 USD | 0.00 USD | 502.03 USD | `-69.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `33.50` | 10,850,000.00 USD | 0.00 USD | 829.46 USD | `-66.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `34.50` | 10,840,000.00 USD | 0.00 USD | 1,320.00 USD | `-65.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.50` | 10,840,000.00 USD | 0.00 USD | 199.88 USD | `-62.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.50` | 10,840,000.00 USD | 0.00 USD | 205.21 USD | `-61.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.50` | 10,840,000.00 USD | 0.00 USD | 3,620.00 USD | `-60.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.50` | 10,840,000.00 USD | 0.00 USD | 423.63 USD | `-59.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.50` | 10,840,000.00 USD | 0.00 USD | 170,330.00 USD | `-57.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.50` | 10,670,000.00 USD | 0.00 USD | 104.40 USD | `-56.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.50` | 10,670,000.00 USD | 0.00 USD | 64,090.00 USD | `-54.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.50` | 10,600,000.00 USD | 0.00 USD | 249.71 USD | `-53.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.50` | 10,600,000.00 USD | 0.00 USD | 332.50 USD | `-52.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.50` | 10,600,000.00 USD | 0.00 USD | 102.82 USD | `-51.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.50` | 10,600,000.00 USD | 0.00 USD | 5,510.00 USD | `-49.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.50` | 10,600,000.00 USD | 0.00 USD | 4,070.00 USD | `-48.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.50` | 10,590,000.00 USD | 0.00 USD | 427.88 USD | `-47.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.50` | 10,590,000.00 USD | 0.00 USD | 26,860.00 USD | `-46.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.50` | 10,570,000.00 USD | 0.00 USD | 785.89 USD | `-45.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.50` | 10,570,000.00 USD | 0.00 USD | 210.90 USD | `-44.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.50` | 10,570,000.00 USD | 0.00 USD | 5,860.00 USD | `-43.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.50` | 10,560,000.00 USD | 0.00 USD | 6,550.00 USD | `-42.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.50` | 10,550,000.00 USD | 0.00 USD | 159.71 USD | `-41.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `59.50` | 10,550,000.00 USD | 0.00 USD | 10,860.00 USD | `-40.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `60.50` | 10,540,000.00 USD | 0.00 USD | 40,470.00 USD | `-39.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `61.50` | 10,500,000.00 USD | 0.00 USD | 18,990.00 USD | `-38.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `62.50` | 10,480,000.00 USD | 0.00 USD | 4,810.00 USD | `-37.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `63.50` | 10,480,000.00 USD | 0.00 USD | 13,260.00 USD | `-36.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `64.50` | 10,470,000.00 USD | 0.00 USD | 129.00 USD | `-35.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `65.50` | 10,460,000.00 USD | 0.00 USD | 4,650.00 USD | `-34.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `66.50` | 10,460,000.00 USD | 0.00 USD | 7,690.00 USD | `-33.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `67.50` | 10,450,000.00 USD | 0.00 USD | 607.50 USD | `-32.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `68.50` | 10,450,000.00 USD | 0.00 USD | 7,360.00 USD | `-31.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `69.50` | 10,440,000.00 USD | 0.00 USD | 54,850.00 USD | `-30.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `70.50` | 10,390,000.00 USD | 0.00 USD | 50,700.00 USD | `-29.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `71.50` | 10,340,000.00 USD | 0.00 USD | 1,200.00 USD | `-28.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `72.50` | 10,340,000.00 USD | 0.00 USD | 153,140.00 USD | `-27.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `73.50` | 10,180,000.00 USD | 0.00 USD | 139.65 USD | `-26.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `74.50` | 10,180,000.00 USD | 0.00 USD | 52,170.00 USD | `-25.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `75.50` | 10,130,000.00 USD | 0.00 USD | 26,730.00 USD | `-24.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `76.50` | 10,110,000.00 USD | 0.00 USD | 16,050.00 USD | `-23.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `77.50` | 10,090,000.00 USD | 0.00 USD | 14,790.00 USD | `-22.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `78.50` | 10,070,000.00 USD | 0.00 USD | 81,220.00 USD | `-21.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `79.50` | 9,990,000.00 USD | 0.00 USD | 13,780.00 USD | `-21.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `80.50` | 9,980,000.00 USD | 0.00 USD | 118,650.00 USD | `-20.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `81.50` | 9,860,000.00 USD | 0.00 USD | 78,820.00 USD | `-19.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `82.50` | 9,780,000.00 USD | 0.00 USD | 27,520.00 USD | `-18.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `83.50` | 9,750,000.00 USD | 0.00 USD | 74,090.00 USD | `-17.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `84.50` | 9,680,000.00 USD | 0.00 USD | 24,890.00 USD | `-16.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `85.50` | 9,660,000.00 USD | 0.00 USD | 173,420.00 USD | `-15.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `86.50` | 9,480,000.00 USD | 0.00 USD | 16,550.00 USD | `-14.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `87.50` | 9,470,000.00 USD | 0.00 USD | 231,120.00 USD | `-13.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `88.50` | 9,230,000.00 USD | 0.00 USD | 282,560.00 USD | `-12.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `89.50` | 8,950,000.00 USD | 0.00 USD | 69,740.00 USD | `-11.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `90.50` | 8,880,000.00 USD | 0.00 USD | 176,870.00 USD | `-10.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `91.50` | 8,710,000.00 USD | 0.00 USD | 431,250.00 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `92.50` | 8,270,000.00 USD | 0.00 USD | 67,860.00 USD | `-8.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `93.50` | 8,210,000.00 USD | 0.00 USD | 1,070,000.00 USD | `-7.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `94.50` | 7,140,000.00 USD | 0.00 USD | 588,910.00 USD | `-6.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `95.50` | 6,550,000.00 USD | 0.00 USD | 970,270.00 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `96.50` | 5,580,000.00 USD | 0.00 USD | 766,810.00 USD | `-4.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `97.50` | 4,820,000.00 USD | 0.00 USD | 492,480.00 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `98.50` | 4,320,000.00 USD | 0.00 USD | 3,050,000.00 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `99.50` | 1,270,000.00 USD | 0.00 USD | 781,380.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `100.50` | 492,500.00 USD | 0.00 USD | 492,500.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `101.50` | 129,930.00 USD | 129,930.00 USD | 0.00 USD | `+0.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.50` | 894,140.00 USD | 764,210.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.50` | 1,190,000.00 USD | 297,830.00 USD | 0.00 USD | `+2.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `104.50` | 1,490,000.00 USD | 300,780.00 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `105.50` | 1,860,000.00 USD | 369,240.00 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `106.50` | 2,220,000.00 USD | 360,910.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `107.50` | 2,410,000.00 USD | 188,070.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.50` | 2,770,000.00 USD | 357,200.00 USD | 0.00 USD | `+7.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.50` | 7,090,000.00 USD | 4,320,000.00 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `110.50` | 8,420,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.50` | 8,460,000.00 USD | 42,320.00 USD | 0.00 USD | `+10.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.50` | 8,680,000.00 USD | 222,460.00 USD | 0.00 USD | `+11.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `113.50` | 9,050,000.00 USD | 362,790.00 USD | 0.00 USD | `+12.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `114.50` | 9,080,000.00 USD | 32,290.00 USD | 0.00 USD | `+13.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `115.50` | 9,220,000.00 USD | 145,270.00 USD | 0.00 USD | `+14.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.50` | 9,270,000.00 USD | 47,920.00 USD | 0.00 USD | `+15.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `117.50` | 9,530,000.00 USD | 255,160.00 USD | 0.00 USD | `+16.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `118.50` | 9,700,000.00 USD | 177,700.00 USD | 0.00 USD | `+17.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `119.50` | 9,940,000.00 USD | 239,490.00 USD | 0.00 USD | `+18.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `120.50` | 10,100,000.00 USD | 152,250.00 USD | 0.00 USD | `+19.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `121.50` | 10,170,000.00 USD | 75,800.00 USD | 0.00 USD | `+20.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `122.50` | 10,700,000.00 USD | 528,840.00 USD | 0.00 USD | `+21.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `123.50` | 11,760,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+22.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `124.50` | 11,930,000.00 USD | 166,110.00 USD | 0.00 USD | `+23.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `125.50` | 12,490,000.00 USD | 558,940.00 USD | 0.00 USD | `+24.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `126.50` | 12,600,000.00 USD | 114,230.00 USD | 0.00 USD | `+25.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `127.50` | 12,880,000.00 USD | 275,030.00 USD | 0.00 USD | `+26.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `128.50` | 12,940,000.00 USD | 58,000.00 USD | 0.00 USD | `+27.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `129.50` | 15,600,000.00 USD | 2,660,000.00 USD | 0.00 USD | `+28.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `130.50` | 15,660,000.00 USD | 68,340.00 USD | 0.00 USD | `+29.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `131.50` | 15,840,000.00 USD | 179,050.00 USD | 0.00 USD | `+30.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `132.50` | 15,870,000.00 USD | 26,010.00 USD | 0.00 USD | `+31.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `133.50` | 15,880,000.00 USD | 13,090.00 USD | 0.00 USD | `+32.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `134.50` | 16,130,000.00 USD | 250,640.00 USD | 0.00 USD | `+33.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `135.50` | 16,210,000.00 USD | 74,880.00 USD | 0.00 USD | `+34.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `136.50` | 16,210,000.00 USD | 3,770.00 USD | 0.00 USD | `+35.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `137.50` | 16,250,000.00 USD | 34,120.00 USD | 0.00 USD | `+36.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `138.50` | 23,000,000.00 USD | 6,760,000.00 USD | 0.00 USD | `+37.64%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `139.50` | 25,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | `+38.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `140.50` | 25,550,000.00 USD | 331,100.00 USD | 0.00 USD | `+39.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `141.50` | 25,560,000.00 USD | 10,520.00 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `142.50` | 25,910,000.00 USD | 346,440.00 USD | 0.00 USD | `+41.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `143.50` | 25,910,000.00 USD | 529.51 USD | 0.00 USD | `+42.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `144.50` | 26,180,000.00 USD | 269,670.00 USD | 0.00 USD | `+43.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `145.50` | 26,190,000.00 USD | 13,070.00 USD | 0.00 USD | `+44.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `146.50` | 26,390,000.00 USD | 198,500.00 USD | 0.00 USD | `+45.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `147.50` | 26,440,000.00 USD | 46,350.00 USD | 0.00 USD | `+46.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `148.50` | 27,770,000.00 USD | 1,330,000.00 USD | 0.00 USD | `+47.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `149.50` | 28,280,000.00 USD | 512,760.00 USD | 0.00 USD | `+48.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `150.50` | 28,550,000.00 USD | 268,780.00 USD | 0.00 USD | `+49.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `151.50` | 28,570,000.00 USD | 16,890.00 USD | 0.00 USD | `+50.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `152.50` | 28,580,000.00 USD | 12,020.00 USD | 0.00 USD | `+51.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `153.50` | 28,590,000.00 USD | 10,650.00 USD | 0.00 USD | `+52.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `154.50` | 28,600,000.00 USD | 12,110.00 USD | 0.00 USD | `+53.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `155.50` | 28,620,000.00 USD | 13,650.00 USD | 0.00 USD | `+54.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `156.50` | 28,620,000.00 USD | 2,230.00 USD | 0.00 USD | `+55.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `158.50` | 28,640,000.00 USD | 22,350.00 USD | 0.00 USD | `+57.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `159.50` | 28,640,000.00 USD | 815.04 USD | 0.00 USD | `+58.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `160.50` | 28,880,000.00 USD | 242,540.00 USD | 0.00 USD | `+59.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `161.50` | 28,880,000.00 USD | 282.62 USD | 0.00 USD | `+60.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `163.50` | 28,890,000.00 USD | 5,030.00 USD | 0.00 USD | `+62.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `165.50` | 28,970,000.00 USD | 83,570.00 USD | 0.00 USD | `+64.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `166.50` | 28,970,000.00 USD | 517.81 USD | 0.00 USD | `+65.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `167.50` | 28,980,000.00 USD | 2,030.00 USD | 0.00 USD | `+66.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `168.50` | 28,980,000.00 USD | 5,560.00 USD | 0.00 USD | `+67.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `169.50` | 28,980,000.00 USD | 1,410.00 USD | 0.00 USD | `+68.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `170.50` | 29,030,000.00 USD | 42,950.00 USD | 0.00 USD | `+69.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `171.50` | 29,030,000.00 USD | 686.00 USD | 0.00 USD | `+70.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `172.50` | 29,060,000.00 USD | 36,070.00 USD | 0.00 USD | `+71.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `173.50` | 29,070,000.00 USD | 6,550.00 USD | 0.00 USD | `+72.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `175.50` | 29,140,000.00 USD | 74,640.00 USD | 0.00 USD | `+74.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `176.50` | 29,150,000.00 USD | 1,450.00 USD | 0.00 USD | `+75.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `177.50` | 29,150,000.00 USD | 2,140.00 USD | 0.00 USD | `+76.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `178.50` | 29,150,000.00 USD | 2,990.00 USD | 0.00 USD | `+77.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `179.50` | 29,150,000.00 USD | 262.07 USD | 0.00 USD | `+78.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `180.50` | 29,250,000.00 USD | 102,680.00 USD | 0.00 USD | `+79.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `181.50` | 29,260,000.00 USD | 2,730.00 USD | 0.00 USD | `+80.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `182.50` | 29,280,000.00 USD | 19,620.00 USD | 0.00 USD | `+81.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `183.50` | 29,830,000.00 USD | 550,500.00 USD | 0.00 USD | `+82.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `185.50` | 29,860,000.00 USD | 29,490.00 USD | 0.00 USD | `+84.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `187.50` | 30,050,000.00 USD | 191,020.00 USD | 0.00 USD | `+86.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `188.50` | 30,190,000.00 USD | 141,530.00 USD | 0.00 USD | `+87.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `190.50` | 30,230,000.00 USD | 38,960.00 USD | 0.00 USD | `+89.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `194.50` | 30,230,000.00 USD | 4,280.00 USD | 0.00 USD | `+93.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `195.50` | 30,230,000.00 USD | 1,760.00 USD | 0.00 USD | `+94.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `196.50` | 30,490,000.00 USD | 253,980.00 USD | 0.00 USD | `+95.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `197.50` | 30,580,000.00 USD | 94,590.00 USD | 0.00 USD | `+96.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `198.50` | 30,960,000.00 USD | 374,220.00 USD | 0.00 USD | `+97.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `199.50` | 30,980,000.00 USD | 28,310.00 USD | 0.00 USD | `+98.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `200.50` | 31,290,000.00 USD | 302,360.00 USD | 0.00 USD | `+99.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `201.50` | 31,290,000.00 USD | 398.97 USD | 0.00 USD | `+100.24%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `89.80` | 384,700,000.00 USD | 0.00 USD | 384,700,000.00 USD | 950,870.00 USD | 471,760.00 USD | 639,640.00 USD |
| `1D` | `90.00` | 190,270,000.00 USD | 0.00 USD | 190,270,000.00 USD | 475,910.00 USD | 591,730.00 USD | 620,590.00 USD |
| `7D` | `90.00` | 382,630,000.00 USD | 0.00 USD | 382,630,000.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD |
| `1D` | `90.20` | 188,590,000.00 USD | 0.00 USD | 188,590,000.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD |
| `7D` | `90.20` | 380,910,000.00 USD | 0.00 USD | 380,910,000.00 USD | 1,250,000.00 USD | 573,800.00 USD | 724,920.00 USD |
| `1D` | `90.40` | 187,260,000.00 USD | 0.00 USD | 187,260,000.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD |
| `7D` | `90.40` | 378,360,000.00 USD | 0.00 USD | 378,360,000.00 USD | 796,240.00 USD | 30,920.00 USD | 694,770.00 USD |
| `1D` | `90.60` | 185,900,000.00 USD | 0.00 USD | 185,900,000.00 USD | 270,180.00 USD | 392,650.00 USD | 477,510.00 USD |
| `7D` | `90.60` | 376,840,000.00 USD | 0.00 USD | 376,840,000.00 USD | 978,100.00 USD | 994,460.00 USD | 1,140,000.00 USD |
| `1D` | `90.80` | 184,760,000.00 USD | 0.00 USD | 184,760,000.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD |
| `7D` | `90.80` | 373,720,000.00 USD | 0.00 USD | 373,720,000.00 USD | 1,210,000.00 USD | 685,900.00 USD | 1,080,000.00 USD |
| `1D` | `91.00` | 184,550,000.00 USD | 0.00 USD | 184,550,000.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD |
| `7D` | `91.00` | 370,740,000.00 USD | 0.00 USD | 370,740,000.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD |
| `1D` | `91.20` | 184,370,000.00 USD | 0.00 USD | 184,370,000.00 USD | 27,610.00 USD | 769.97 USD | 307.73 USD |
| `7D` | `91.20` | 368,680,000.00 USD | 0.00 USD | 368,680,000.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD |
| `1D` | `91.40` | 184,340,000.00 USD | 0.00 USD | 184,340,000.00 USD | 3,800.00 USD | 125,680.00 USD | 43,950.00 USD |
| `7D` | `91.40` | 366,350,000.00 USD | 0.00 USD | 366,350,000.00 USD | 1,180,000.00 USD | 1,000,000.00 USD | 1,140,000.00 USD |
| `1D` | `91.60` | 184,160,000.00 USD | 0.00 USD | 184,160,000.00 USD | 25,530.00 USD | 96,080.00 USD | 1,680.00 USD |
| `7D` | `91.60` | 363,030,000.00 USD | 0.00 USD | 363,030,000.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD |
| `1D` | `91.80` | 184,040,000.00 USD | 0.00 USD | 184,040,000.00 USD | 229,430.00 USD | 103,030.00 USD | 11,420.00 USD |
| `7D` | `91.80` | 361,400,000.00 USD | 0.00 USD | 361,400,000.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD |
| `1D` | `92.00` | 183,700,000.00 USD | 0.00 USD | 183,700,000.00 USD | 137,240.00 USD | 74,290.00 USD | 90,460.00 USD |
| `7D` | `92.00` | 359,200,000.00 USD | 0.00 USD | 359,200,000.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD |
| `1D` | `92.20` | 183,390,000.00 USD | 0.00 USD | 183,390,000.00 USD | 153,400.00 USD | 41,040.00 USD | 107,850.00 USD |
| `7D` | `92.20` | 357,460,000.00 USD | 0.00 USD | 357,460,000.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD |
| `1D` | `92.40` | 183,090,000.00 USD | 0.00 USD | 183,090,000.00 USD | 145,850.00 USD | 72,380.00 USD | 782,700.00 USD |
| `7D` | `92.40` | 356,600,000.00 USD | 0.00 USD | 356,600,000.00 USD | 415,170.00 USD | 289,690.00 USD | 1,210,000.00 USD |
| `1D` | `92.60` | 182,090,000.00 USD | 0.00 USD | 182,090,000.00 USD | 31,270.00 USD | 106,430.00 USD | 115,700.00 USD |
| `7D` | `92.60` | 354,690,000.00 USD | 0.00 USD | 354,690,000.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD |
| `1D` | `92.80` | 181,840,000.00 USD | 0.00 USD | 181,840,000.00 USD | 55,570.00 USD | 0.00 USD | 98,160.00 USD |
| `7D` | `92.80` | 353,610,000.00 USD | 0.00 USD | 353,610,000.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD |
| `1D` | `93.00` | 181,680,000.00 USD | 0.00 USD | 181,680,000.00 USD | 45,270.00 USD | 0.00 USD | 120,780.00 USD |
| `7D` | `93.00` | 353,390,000.00 USD | 0.00 USD | 353,390,000.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD |
| `1D` | `93.20` | 181,520,000.00 USD | 0.00 USD | 181,520,000.00 USD | 0.00 USD | 54,140.00 USD | 155,120.00 USD |
| `7D` | `93.20` | 353,000,000.00 USD | 0.00 USD | 353,000,000.00 USD | 54,470.00 USD | 4,160.00 USD | 49,310.00 USD |
| `1D` | `93.40` | 181,310,000.00 USD | 0.00 USD | 181,310,000.00 USD | 0.00 USD | 51,460.00 USD | 0.00 USD |
| `7D` | `93.40` | 352,890,000.00 USD | 0.00 USD | 352,890,000.00 USD | 11,220.00 USD | 2,430.00 USD | 1,290.00 USD |
| `7D` | `93.60` | 352,870,000.00 USD | 0.00 USD | 352,870,000.00 USD | 238,200.00 USD | 299,520.00 USD | 114,860.00 USD |
| `7D` | `93.80` | 352,220,000.00 USD | 0.00 USD | 352,220,000.00 USD | 349,450.00 USD | 179,760.00 USD | 146,240.00 USD |
| `7D` | `94.00` | 351,540,000.00 USD | 0.00 USD | 351,540,000.00 USD | 78,790.00 USD | 153,680.00 USD | 64,980.00 USD |
| `7D` | `94.20` | 351,250,000.00 USD | 0.00 USD | 351,250,000.00 USD | 172,550.00 USD | 229,720.00 USD | 258,370.00 USD |
| `7D` | `94.40` | 350,590,000.00 USD | 0.00 USD | 350,590,000.00 USD | 109,990.00 USD | 0.00 USD | 184,090.00 USD |
| `7D` | `94.60` | 350,290,000.00 USD | 0.00 USD | 350,290,000.00 USD | 79,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `94.80` | 350,210,000.00 USD | 0.00 USD | 350,210,000.00 USD | 0.00 USD | 15,050.00 USD | 8,930.00 USD |
| `7D` | `95.00` | 350,190,000.00 USD | 0.00 USD | 350,190,000.00 USD | 418,320.00 USD | 532,260.00 USD | 13,320.00 USD |
| `1D` | `95.20` | 181,260,000.00 USD | 0.00 USD | 181,260,000.00 USD | 13,360.00 USD | 0.00 USD | 6,080.00 USD |
| `7D` | `95.20` | 349,230,000.00 USD | 0.00 USD | 349,230,000.00 USD | 47,840.00 USD | 200,720.00 USD | 138,220.00 USD |
| `1D` | `95.40` | 181,240,000.00 USD | 0.00 USD | 181,240,000.00 USD | 321,380.00 USD | 189,450.00 USD | 7,360.00 USD |
| `7D` | `95.40` | 348,840,000.00 USD | 0.00 USD | 348,840,000.00 USD | 627,890.00 USD | 225,150.00 USD | 669,320.00 USD |
| `1D` | `95.60` | 180,720,000.00 USD | 0.00 USD | 180,720,000.00 USD | 906,290.00 USD | 706,940.00 USD | 949,070.00 USD |
| `7D` | `95.60` | 347,320,000.00 USD | 0.00 USD | 347,320,000.00 USD | 1,740,000.00 USD | 1,320,000.00 USD | 986,050.00 USD |
| `1D` | `95.80` | 178,160,000.00 USD | 0.00 USD | 178,160,000.00 USD | 1,710,000.00 USD | 1,320,000.00 USD | 797,660.00 USD |
| `7D` | `95.80` | 343,270,000.00 USD | 0.00 USD | 343,270,000.00 USD | 1,870,000.00 USD | 1,030,000.00 USD | 1,330,000.00 USD |
| `1D` | `96.00` | 174,330,000.00 USD | 0.00 USD | 174,330,000.00 USD | 1,310,000.00 USD | 1,290,000.00 USD | 1,270,000.00 USD |
| `7D` | `96.00` | 339,030,000.00 USD | 0.00 USD | 339,030,000.00 USD | 1,380,000.00 USD | 1,890,000.00 USD | 3,170,000.00 USD |
| `1D` | `96.20` | 170,460,000.00 USD | 0.00 USD | 170,460,000.00 USD | 1,970,000.00 USD | 1,310,000.00 USD | 1,250,000.00 USD |
| `7D` | `96.20` | 332,590,000.00 USD | 0.00 USD | 332,590,000.00 USD | 3,950,000.00 USD | 2,080,000.00 USD | 2,580,000.00 USD |
| `1D` | `96.40` | 165,940,000.00 USD | 0.00 USD | 165,940,000.00 USD | 1,540,000.00 USD | 1,270,000.00 USD | 1,590,000.00 USD |
| `7D` | `96.40` | 323,980,000.00 USD | 0.00 USD | 323,980,000.00 USD | 3,260,000.00 USD | 643,110.00 USD | 2,910,000.00 USD |
| `1D` | `96.60` | 161,540,000.00 USD | 0.00 USD | 161,540,000.00 USD | 1,040,000.00 USD | 839,050.00 USD | 934,330.00 USD |
| `7D` | `96.60` | 317,170,000.00 USD | 0.00 USD | 317,170,000.00 USD | 3,250,000.00 USD | 2,480,000.00 USD | 2,380,000.00 USD |
| `1D` | `96.80` | 158,730,000.00 USD | 0.00 USD | 158,730,000.00 USD | 327,640.00 USD | 738,000.00 USD | 729,790.00 USD |
| `7D` | `96.80` | 309,070,000.00 USD | 0.00 USD | 309,070,000.00 USD | 3,000,000.00 USD | 2,770,000.00 USD | 2,960,000.00 USD |
| `1D` | `97.00` | 156,930,000.00 USD | 0.00 USD | 156,930,000.00 USD | 310,450.00 USD | 114,330.00 USD | 170,180.00 USD |
| `7D` | `97.00` | 300,330,000.00 USD | 0.00 USD | 300,330,000.00 USD | 5,510,000.00 USD | 2,530,000.00 USD | 2,040,000.00 USD |
| `1D` | `97.20` | 156,340,000.00 USD | 0.00 USD | 156,340,000.00 USD | 336,680.00 USD | 6,890.00 USD | 336,920.00 USD |
| `7D` | `97.20` | 290,250,000.00 USD | 0.00 USD | 290,250,000.00 USD | 5,490,000.00 USD | 4,350,000.00 USD | 3,980,000.00 USD |
| `1D` | `97.40` | 155,660,000.00 USD | 0.00 USD | 155,660,000.00 USD | 821,270.00 USD | 642,050.00 USD | 150,290.00 USD |
| `7D` | `97.40` | 276,430,000.00 USD | 0.00 USD | 276,430,000.00 USD | 4,530,000.00 USD | 2,410,000.00 USD | 3,470,000.00 USD |
| `1D` | `97.60` | 154,040,000.00 USD | 0.00 USD | 154,040,000.00 USD | 1,940,000.00 USD | 1,700,000.00 USD | 1,920,000.00 USD |
| `7D` | `97.60` | 266,020,000.00 USD | 0.00 USD | 266,020,000.00 USD | 5,190,000.00 USD | 5,230,000.00 USD | 4,930,000.00 USD |
| `1D` | `97.80` | 148,480,000.00 USD | 0.00 USD | 148,480,000.00 USD | 3,790,000.00 USD | 3,090,000.00 USD | 1,820,000.00 USD |
| `7D` | `97.80` | 250,670,000.00 USD | 0.00 USD | 250,670,000.00 USD | 5,700,000.00 USD | 2,970,000.00 USD | 4,790,000.00 USD |
| `1D` | `98.00` | 139,770,000.00 USD | 0.00 USD | 139,770,000.00 USD | 3,230,000.00 USD | 2,990,000.00 USD | 2,920,000.00 USD |
| `7D` | `98.00` | 237,210,000.00 USD | 0.00 USD | 237,210,000.00 USD | 7,970,000.00 USD | 7,990,000.00 USD | 8,720,000.00 USD |
| `1D` | `98.20` | 130,630,000.00 USD | 0.00 USD | 130,630,000.00 USD | 4,520,000.00 USD | 2,920,000.00 USD | 2,700,000.00 USD |
| `7D` | `98.20` | 212,520,000.00 USD | 0.00 USD | 212,520,000.00 USD | 9,810,000.00 USD | 6,890,000.00 USD | 6,860,000.00 USD |
| `1D` | `98.40` | 120,480,000.00 USD | 0.00 USD | 120,480,000.00 USD | 5,020,000.00 USD | 3,620,000.00 USD | 4,380,000.00 USD |
| `7D` | `98.40` | 188,970,000.00 USD | 0.00 USD | 188,970,000.00 USD | 10,080,000.00 USD | 2,950,000.00 USD | 10,690,000.00 USD |
| `1D` | `98.60` | 107,460,000.00 USD | 0.00 USD | 107,460,000.00 USD | 6,300,000.00 USD | 4,610,000.00 USD | 6,750,000.00 USD |
| `7D` | `98.60` | 165,240,000.00 USD | 0.00 USD | 165,240,000.00 USD | 13,730,000.00 USD | 10,810,000.00 USD | 10,950,000.00 USD |
| `1D` | `98.80` | 89,810,000.00 USD | 0.00 USD | 89,810,000.00 USD | 7,340,000.00 USD | 6,980,000.00 USD | 5,060,000.00 USD |
| `7D` | `98.80` | 129,750,000.00 USD | 0.00 USD | 129,750,000.00 USD | 12,600,000.00 USD | 9,880,000.00 USD | 13,080,000.00 USD |
| `1D` | `99.00` | 70,430,000.00 USD | 0.00 USD | 70,430,000.00 USD | 5,430,000.00 USD | 5,240,000.00 USD | 5,630,000.00 USD |
| `7D` | `99.00` | 94,200,000.00 USD | 0.00 USD | 94,200,000.00 USD | 14,280,000.00 USD | 10,590,000.00 USD | 16,810,000.00 USD |
| `1D` | `99.20` | 54,130,000.00 USD | 0.00 USD | 54,130,000.00 USD | 8,120,000.00 USD | 5,060,000.00 USD | 5,970,000.00 USD |
| `7D` | `99.20` | 52,520,000.00 USD | 0.00 USD | 52,520,000.00 USD | 16,630,000.00 USD | 7,420,000.00 USD | 8,280,000.00 USD |
| `1D` | `99.40` | 34,970,000.00 USD | 0.00 USD | 34,970,000.00 USD | 6,080,000.00 USD | 5,170,000.00 USD | 6,670,000.00 USD |
| `7D` | `99.40` | 20,190,000.00 USD | 0.00 USD | 20,190,000.00 USD | 3,530,000.00 USD | 599,290.00 USD | 8,830,000.00 USD |
| `1D` | `99.60` | 17,050,000.00 USD | 0.00 USD | 17,050,000.00 USD | 3,520,000.00 USD | 3,320,000.00 USD | 2,970,000.00 USD |
| `7D` | `99.60` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 2,030,000.00 USD | 1,930,000.00 USD | 507,990.00 USD |
| `1D` | `99.80` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 1,490,000.00 USD | 2,600,000.00 USD | 3,150,000.00 USD |
| `7D` | `99.80` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 0.00 USD | 490,550.00 USD | 2,270,000.00 USD |
| `1D` | `100.00` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 2,090,000.00 USD | 501,110.00 USD | 657,190.00 USD |
| `1D` | `100.00` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 2,090,000.00 USD | 501,110.00 USD | 657,190.00 USD |
| `7D` | `100.00` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,380,000.00 USD | 36,980.00 USD | 0.00 USD |
| `7D` | `100.00` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 1,380,000.00 USD | 36,980.00 USD | 0.00 USD |
| `1D` | `100.20` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,440.00 USD |
| `1D` | `100.40` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,240.00 USD |
| `7D` | `100.40` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 78,970.00 USD | 68,710.00 USD | 0.00 USD |
| `1D` | `100.60` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 0.00 USD | 167,670.00 USD | 2,790,000.00 USD |
| `7D` | `100.60` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 46,010.00 USD | 245,560.00 USD | 1,480,000.00 USD |
| `1D` | `100.80` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 274,280.00 USD | 802,330.00 USD | 4,380.00 USD |
| `7D` | `100.80` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 981,100.00 USD | 0.00 USD |
| `1D` | `101.00` | 17,400,000.00 USD | 17,400,000.00 USD | 0.00 USD | 5,250,000.00 USD | 1,430,000.00 USD | 175,880.00 USD |
| `7D` | `101.00` | 14,020,000.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 4,560,000.00 USD | 3,730,000.00 USD |
| `1D` | `101.20` | 34,360,000.00 USD | 34,360,000.00 USD | 0.00 USD | 5,880,000.00 USD | 6,710,000.00 USD | 4,360,000.00 USD |
| `7D` | `101.20` | 28,740,000.00 USD | 28,740,000.00 USD | 0.00 USD | 6,220,000.00 USD | 3,670,000.00 USD | 4,820,000.00 USD |
| `1D` | `101.40` | 41,400,000.00 USD | 41,400,000.00 USD | 0.00 USD | 3,360,000.00 USD | 1,720,000.00 USD | 1,950,000.00 USD |
| `7D` | `101.40` | 42,620,000.00 USD | 42,620,000.00 USD | 0.00 USD | 4,250,000.00 USD | 0.00 USD | 9,630,000.00 USD |
| `1D` | `101.60` | 61,440,000.00 USD | 61,440,000.00 USD | 0.00 USD | 4,610,000.00 USD | 2,550,000.00 USD | 12,880,000.00 USD |
| `7D` | `101.60` | 52,460,000.00 USD | 52,460,000.00 USD | 0.00 USD | 3,650,000.00 USD | 0.00 USD | 6,200,000.00 USD |
| `1D` | `101.80` | 68,010,000.00 USD | 68,010,000.00 USD | 0.00 USD | 212,730.00 USD | 142,780.00 USD | 6,210,000.00 USD |
| `7D` | `101.80` | 61,810,000.00 USD | 61,810,000.00 USD | 0.00 USD | 2,970,000.00 USD | 453,970.00 USD | 5,920,000.00 USD |
| `1D` | `102.00` | 71,130,000.00 USD | 71,130,000.00 USD | 0.00 USD | 1,330,000.00 USD | 679,810.00 USD | 1,120,000.00 USD |
| `7D` | `102.00` | 64,490,000.00 USD | 64,490,000.00 USD | 0.00 USD | 843,730.00 USD | 0.00 USD | 1,840,000.00 USD |
| `1D` | `102.20` | 77,960,000.00 USD | 77,960,000.00 USD | 0.00 USD | 3,030,000.00 USD | 1,390,000.00 USD | 2,410,000.00 USD |
| `7D` | `102.20` | 71,200,000.00 USD | 71,200,000.00 USD | 0.00 USD | 2,390,000.00 USD | 803,220.00 USD | 3,520,000.00 USD |
| `1D` | `102.40` | 82,450,000.00 USD | 82,450,000.00 USD | 0.00 USD | 1,360,000.00 USD | 569,360.00 USD | 2,560,000.00 USD |
| `7D` | `102.40` | 75,910,000.00 USD | 75,910,000.00 USD | 0.00 USD | 1,760,000.00 USD | 299,640.00 USD | 2,650,000.00 USD |
| `1D` | `102.60` | 82,940,000.00 USD | 82,940,000.00 USD | 0.00 USD | 289,550.00 USD | 190,630.00 USD | 9,420.00 USD |
| `7D` | `102.60` | 78,330,000.00 USD | 78,330,000.00 USD | 0.00 USD | 1,400,000.00 USD | 979,270.00 USD | 37,570.00 USD |
| `1D` | `102.80` | 86,780,000.00 USD | 86,780,000.00 USD | 0.00 USD | 1,410,000.00 USD | 1,870,000.00 USD | 563,120.00 USD |
| `7D` | `102.80` | 86,210,000.00 USD | 86,210,000.00 USD | 0.00 USD | 7,600,000.00 USD | 0.00 USD | 277,920.00 USD |
| `1D` | `103.00` | 91,150,000.00 USD | 91,150,000.00 USD | 0.00 USD | 2,600,000.00 USD | 1,430,000.00 USD | 340,360.00 USD |
| `7D` | `103.00` | 100,730,000.00 USD | 100,730,000.00 USD | 0.00 USD | 11,690,000.00 USD | 0.00 USD | 2,830,000.00 USD |
| `1D` | `103.20` | 96,480,000.00 USD | 96,480,000.00 USD | 0.00 USD | 1,840,000.00 USD | 1,670,000.00 USD | 1,820,000.00 USD |
| `7D` | `103.20` | 115,020,000.00 USD | 115,020,000.00 USD | 0.00 USD | 13,650,000.00 USD | 4,380.00 USD | 631,060.00 USD |
| `1D` | `103.40` | 103,710,000.00 USD | 103,710,000.00 USD | 0.00 USD | 3,920,000.00 USD | 1,790,000.00 USD | 1,530,000.00 USD |
| `7D` | `103.40` | 130,020,000.00 USD | 130,020,000.00 USD | 0.00 USD | 12,210,000.00 USD | 219,070.00 USD | 2,580,000.00 USD |
| `1D` | `103.60` | 118,100,000.00 USD | 118,100,000.00 USD | 0.00 USD | 4,250,000.00 USD | 2,110,000.00 USD | 8,040,000.00 USD |
| `7D` | `103.60` | 148,410,000.00 USD | 148,410,000.00 USD | 0.00 USD | 11,460,000.00 USD | 1,720,000.00 USD | 5,210,000.00 USD |
| `1D` | `103.80` | 127,580,000.00 USD | 127,580,000.00 USD | 0.00 USD | 3,350,000.00 USD | 2,690,000.00 USD | 3,430,000.00 USD |
| `7D` | `103.80` | 160,760,000.00 USD | 160,760,000.00 USD | 0.00 USD | 7,920,000.00 USD | 1,880,000.00 USD | 2,550,000.00 USD |
| `1D` | `104.00` | 137,750,000.00 USD | 137,750,000.00 USD | 0.00 USD | 3,100,000.00 USD | 3,240,000.00 USD | 3,840,000.00 USD |
| `7D` | `104.00` | 189,180,000.00 USD | 189,180,000.00 USD | 0.00 USD | 11,400,000.00 USD | 6,910,000.00 USD | 10,110,000.00 USD |
| `1D` | `104.20` | 146,360,000.00 USD | 146,360,000.00 USD | 0.00 USD | 3,720,000.00 USD | 2,180,000.00 USD | 2,700,000.00 USD |
| `7D` | `104.20` | 210,990,000.00 USD | 210,990,000.00 USD | 0.00 USD | 8,520,000.00 USD | 7,010,000.00 USD | 6,280,000.00 USD |
| `1D` | `104.40` | 155,000,000.00 USD | 155,000,000.00 USD | 0.00 USD | 3,300,000.00 USD | 1,930,000.00 USD | 3,410,000.00 USD |
| `7D` | `104.40` | 227,960,000.00 USD | 227,960,000.00 USD | 0.00 USD | 5,100,000.00 USD | 3,700,000.00 USD | 8,170,000.00 USD |
| `1D` | `104.60` | 163,040,000.00 USD | 163,040,000.00 USD | 0.00 USD | 2,200,000.00 USD | 1,920,000.00 USD | 3,910,000.00 USD |
| `7D` | `104.60` | 245,520,000.00 USD | 245,520,000.00 USD | 0.00 USD | 7,180,000.00 USD | 3,550,000.00 USD | 6,830,000.00 USD |
| `1D` | `104.80` | 169,340,000.00 USD | 169,340,000.00 USD | 0.00 USD | 1,630,000.00 USD | 1,620,000.00 USD | 3,060,000.00 USD |
| `7D` | `104.80` | 262,650,000.00 USD | 262,650,000.00 USD | 0.00 USD | 5,170,000.00 USD | 4,150,000.00 USD | 7,820,000.00 USD |
| `1D` | `105.00` | 171,910,000.00 USD | 171,910,000.00 USD | 0.00 USD | 708,730.00 USD | 754,560.00 USD | 1,100,000.00 USD |
| `7D` | `105.00` | 279,780,000.00 USD | 279,780,000.00 USD | 0.00 USD | 5,730,000.00 USD | 5,070,000.00 USD | 6,330,000.00 USD |
| `1D` | `105.20` | 173,240,000.00 USD | 173,240,000.00 USD | 0.00 USD | 514,940.00 USD | 4,110.00 USD | 814,780.00 USD |
| `7D` | `105.20` | 292,490,000.00 USD | 292,490,000.00 USD | 0.00 USD | 5,340,000.00 USD | 4,850,000.00 USD | 2,530,000.00 USD |
| `1D` | `105.40` | 174,270,000.00 USD | 174,270,000.00 USD | 0.00 USD | 299,190.00 USD | 2,770.00 USD | 727,360.00 USD |
| `7D` | `105.40` | 304,450,000.00 USD | 304,450,000.00 USD | 0.00 USD | 2,960,000.00 USD | 4,450,000.00 USD | 4,540,000.00 USD |
| `1D` | `105.60` | 175,820,000.00 USD | 175,820,000.00 USD | 0.00 USD | 273,980.00 USD | 638,670.00 USD | 642,780.00 USD |
| `7D` | `105.60` | 321,920,000.00 USD | 321,920,000.00 USD | 0.00 USD | 5,650,000.00 USD | 6,010,000.00 USD | 5,810,000.00 USD |
| `1D` | `105.80` | 176,880,000.00 USD | 176,880,000.00 USD | 0.00 USD | 225,560.00 USD | 542,960.00 USD | 287,640.00 USD |
| `7D` | `105.80` | 332,680,000.00 USD | 332,680,000.00 USD | 0.00 USD | 3,540,000.00 USD | 3,020,000.00 USD | 4,200,000.00 USD |
| `1D` | `106.00` | 177,940,000.00 USD | 177,940,000.00 USD | 0.00 USD | 377,210.00 USD | 456,530.00 USD | 222,920.00 USD |
| `7D` | `106.00` | 342,660,000.00 USD | 342,660,000.00 USD | 0.00 USD | 4,000,000.00 USD | 2,430,000.00 USD | 3,550,000.00 USD |
| `1D` | `106.20` | 179,340,000.00 USD | 179,340,000.00 USD | 0.00 USD | 606,390.00 USD | 420,460.00 USD | 375,050.00 USD |
| `7D` | `106.20` | 357,010,000.00 USD | 357,010,000.00 USD | 0.00 USD | 6,980,000.00 USD | 3,540,000.00 USD | 3,830,000.00 USD |
| `1D` | `106.40` | 180,440,000.00 USD | 180,440,000.00 USD | 0.00 USD | 583,540.00 USD | 313,010.00 USD | 207,870.00 USD |
| `7D` | `106.40` | 365,170,000.00 USD | 365,170,000.00 USD | 0.00 USD | 3,590,000.00 USD | 2,670,000.00 USD | 1,900,000.00 USD |
| `1D` | `106.60` | 182,970,000.00 USD | 182,970,000.00 USD | 0.00 USD | 887,290.00 USD | 440,970.00 USD | 1,200,000.00 USD |
| `7D` | `106.60` | 374,380,000.00 USD | 374,380,000.00 USD | 0.00 USD | 2,470,000.00 USD | 2,360,000.00 USD | 4,380,000.00 USD |
| `1D` | `106.80` | 184,970,000.00 USD | 184,970,000.00 USD | 0.00 USD | 653,630.00 USD | 182,880.00 USD | 1,160,000.00 USD |
| `7D` | `106.80` | 380,260,000.00 USD | 380,260,000.00 USD | 0.00 USD | 1,340,000.00 USD | 1,750,000.00 USD | 2,800,000.00 USD |
| `1D` | `107.00` | 185,960,000.00 USD | 185,960,000.00 USD | 0.00 USD | 199,140.00 USD | 320,120.00 USD | 464,190.00 USD |
| `7D` | `107.00` | 385,820,000.00 USD | 385,820,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,260,000.00 USD | 2,930,000.00 USD |
| `1D` | `107.20` | 186,340,000.00 USD | 186,340,000.00 USD | 0.00 USD | 138,920.00 USD | 0.00 USD | 245,400.00 USD |
| `7D` | `107.20` | 387,540,000.00 USD | 387,540,000.00 USD | 0.00 USD | 866,170.00 USD | 389,810.00 USD | 461,600.00 USD |
| `1D` | `107.40` | 186,820,000.00 USD | 186,820,000.00 USD | 0.00 USD | 113,170.00 USD | 0.00 USD | 363,300.00 USD |
| `7D` | `107.40` | 388,530,000.00 USD | 388,530,000.00 USD | 0.00 USD | 0.00 USD | 280,650.00 USD | 703,710.00 USD |
| `1D` | `107.60` | 187,310,000.00 USD | 187,310,000.00 USD | 0.00 USD | 47,730.00 USD | 187,760.00 USD | 253,610.00 USD |
| `7D` | `107.60` | 388,890,000.00 USD | 388,890,000.00 USD | 0.00 USD | 213,520.00 USD | 0.00 USD | 154,920.00 USD |
| `1D` | `107.80` | 187,620,000.00 USD | 187,620,000.00 USD | 0.00 USD | 46,620.00 USD | 128,660.00 USD | 134,200.00 USD |
| `7D` | `107.80` | 389,670,000.00 USD | 389,670,000.00 USD | 0.00 USD | 489,650.00 USD | 10,400.00 USD | 277,390.00 USD |
| `7D` | `108.00` | 389,710,000.00 USD | 389,710,000.00 USD | 0.00 USD | 25,580.00 USD | 6,070.00 USD | 5,560.00 USD |
| `7D` | `108.20` | 391,820,000.00 USD | 391,820,000.00 USD | 0.00 USD | 860,420.00 USD | 826,850.00 USD | 427,140.00 USD |
| `7D` | `108.40` | 394,310,000.00 USD | 394,310,000.00 USD | 0.00 USD | 1,410,000.00 USD | 528,370.00 USD | 548,050.00 USD |
| `7D` | `108.60` | 395,560,000.00 USD | 395,560,000.00 USD | 0.00 USD | 401,600.00 USD | 515,740.00 USD | 332,360.00 USD |
| `7D` | `108.80` | 398,240,000.00 USD | 398,240,000.00 USD | 0.00 USD | 627,810.00 USD | 1,190,000.00 USD | 855,850.00 USD |
| `1D` | `109.00` | 187,620,000.00 USD | 187,620,000.00 USD | 0.00 USD | 5,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `109.00` | 398,780,000.00 USD | 398,780,000.00 USD | 0.00 USD | 248,800.00 USD | 112,280.00 USD | 176,770.00 USD |
| `1D` | `109.20` | 187,630,000.00 USD | 187,630,000.00 USD | 0.00 USD | 7,480.00 USD | 2,460.00 USD | 2,770.00 USD |
| `7D` | `109.20` | 400,000,000.00 USD | 400,000,000.00 USD | 0.00 USD | 596,270.00 USD | 82,160.00 USD | 544,580.00 USD |
| `1D` | `109.40` | 187,760,000.00 USD | 187,760,000.00 USD | 0.00 USD | 118,540.00 USD | 6,900.00 USD | 2,610.00 USD |
| `7D` | `109.40` | 400,340,000.00 USD | 400,340,000.00 USD | 0.00 USD | 158,460.00 USD | 81,870.00 USD | 92,530.00 USD |
| `1D` | `109.60` | 188,420,000.00 USD | 188,420,000.00 USD | 0.00 USD | 319,220.00 USD | 155,520.00 USD | 184,630.00 USD |
| `7D` | `109.60` | 401,400,000.00 USD | 401,400,000.00 USD | 0.00 USD | 525,760.00 USD | 188,400.00 USD | 347,790.00 USD |
| `1D` | `109.80` | 189,450,000.00 USD | 189,450,000.00 USD | 0.00 USD | 478,690.00 USD | 349,260.00 USD | 197,340.00 USD |
| `7D` | `109.80` | 402,380,000.00 USD | 402,380,000.00 USD | 0.00 USD | 410,490.00 USD | 283,370.00 USD | 291,850.00 USD |
| `1D` | `110.00` | 190,610,000.00 USD | 190,610,000.00 USD | 0.00 USD | 256,140.00 USD | 449,140.00 USD | 454,010.00 USD |
| `7D` | `110.00` | 404,110,000.00 USD | 404,110,000.00 USD | 0.00 USD | 182,220.00 USD | 445,120.00 USD | 1,090,000.00 USD |
| `1D` | `110.20` | 191,930,000.00 USD | 191,930,000.00 USD | 0.00 USD | 489,160.00 USD | 406,910.00 USD | 432,190.00 USD |
| `7D` | `110.20` | 406,660,000.00 USD | 406,660,000.00 USD | 0.00 USD | 1,250,000.00 USD | 573,800.00 USD | 724,920.00 USD |
| `1D` | `110.40` | 193,290,000.00 USD | 193,290,000.00 USD | 0.00 USD | 505,770.00 USD | 339,750.00 USD | 509,430.00 USD |
| `7D` | `110.40` | 408,180,000.00 USD | 408,180,000.00 USD | 0.00 USD | 796,240.00 USD | 30,920.00 USD | 694,770.00 USD |
| `1D` | `110.60` | 193,740,000.00 USD | 193,740,000.00 USD | 0.00 USD | 110,850.00 USD | 104,840.00 USD | 240,140.00 USD |
| `7D` | `110.60` | 409,280,000.00 USD | 409,280,000.00 USD | 0.00 USD | 506,360.00 USD | 293,650.00 USD | 301,670.00 USD |
| `1D` | `110.80` | 194,430,000.00 USD | 194,430,000.00 USD | 0.00 USD | 159,320.00 USD | 287,810.00 USD | 237,370.00 USD |
| `7D` | `110.80` | 411,300,000.00 USD | 411,300,000.00 USD | 0.00 USD | 471,740.00 USD | 700,800.00 USD | 841,270.00 USD |
| `1D` | `111.00` | 194,640,000.00 USD | 194,640,000.00 USD | 0.00 USD | 106,320.00 USD | 101,660.00 USD | 1,720.00 USD |
| `7D` | `111.00` | 414,280,000.00 USD | 414,280,000.00 USD | 0.00 USD | 1,210,000.00 USD | 685,900.00 USD | 1,080,000.00 USD |
| `1D` | `111.20` | 194,830,000.00 USD | 194,830,000.00 USD | 0.00 USD | 57,100.00 USD | 882.42 USD | 129,600.00 USD |
| `7D` | `111.20` | 416,340,000.00 USD | 416,340,000.00 USD | 0.00 USD | 1,190,000.00 USD | 575,820.00 USD | 295,620.00 USD |
| `1D` | `111.40` | 194,850,000.00 USD | 194,850,000.00 USD | 0.00 USD | 27,610.00 USD | 769.97 USD | 0.00 USD |
| `7D` | `111.40` | 418,670,000.00 USD | 418,670,000.00 USD | 0.00 USD | 946,940.00 USD | 807,150.00 USD | 576,400.00 USD |
| `7D` | `111.60` | 419,630,000.00 USD | 419,630,000.00 USD | 0.00 USD | 662,880.00 USD | 172,700.00 USD | 122,050.00 USD |
| `7D` | `111.80` | 421,990,000.00 USD | 421,990,000.00 USD | 0.00 USD | 515,920.00 USD | 829,010.00 USD | 1,020,000.00 USD |
| `7D` | `112.00` | 423,610,000.00 USD | 423,610,000.00 USD | 0.00 USD | 500,280.00 USD | 295,810.00 USD | 827,850.00 USD |
| `7D` | `112.20` | 425,820,000.00 USD | 425,820,000.00 USD | 0.00 USD | 932,400.00 USD | 581,530.00 USD | 688,730.00 USD |
| `7D` | `112.40` | 427,560,000.00 USD | 427,560,000.00 USD | 0.00 USD | 681,440.00 USD | 586,560.00 USD | 471,340.00 USD |
| `7D` | `112.60` | 428,420,000.00 USD | 428,420,000.00 USD | 0.00 USD | 210,560.00 USD | 354,230.00 USD | 294,010.00 USD |
| `7D` | `112.80` | 429,290,000.00 USD | 429,290,000.00 USD | 0.00 USD | 207,390.00 USD | 162,590.00 USD | 505,740.00 USD |
| `7D` | `113.00` | 430,330,000.00 USD | 430,330,000.00 USD | 0.00 USD | 207,780.00 USD | 127,100.00 USD | 702,160.00 USD |
| `7D` | `113.20` | 431,410,000.00 USD | 431,410,000.00 USD | 0.00 USD | 175,470.00 USD | 267,710.00 USD | 636,520.00 USD |
| `7D` | `113.40` | 431,630,000.00 USD | 431,630,000.00 USD | 0.00 USD | 92,010.00 USD | 62,840.00 USD | 69,630.00 USD |
| `7D` | `113.60` | 432,020,000.00 USD | 432,020,000.00 USD | 0.00 USD | 0.00 USD | 109,950.00 USD | 281,490.00 USD |
| `7D` | `113.80` | 432,030,000.00 USD | 432,030,000.00 USD | 0.00 USD | 2,370.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `6.24B` | Total OI Tokens: `62,411,840.9 SOL`
  * 1h OI Change: `+0.07%` | 4h OI Change: `-2.05%` | 24h OI Change: `-3.09%`
  * Exchange Breakdown: Binance=`1.09B` | Bybit=`616.06M` | OKX=`352.70M` | Hyperliquid=`565.24M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `181.61K` | Last 24h: `361.48K` | Last 3d: `1.27M` | Last 7d: `2.42M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0079%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0036%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `SOL` | `57.40%` | `42.60%` | `1.35` | 12,870,000.00 USD |
| `15M` | `Binance` | `49.89%` | `50.11%` | `1.00` | 4,060,000.00 USD |
| `15M` | `OKX` | `50.96%` | `49.04%` | `1.04` | 911,630.00 USD |
| `15M` | `Bybit` | `59.9%` | `40.1%` | `1.49` | 749,960.00 USD |
| `15M` | `KuCoin` | `57.84%` | `42.16%` | `1.37` | 103,650.00 USD |
| `15M` | `Gate` | `51.59%` | `48.41%` | `1.07` | 960,970.00 USD |
| `15M` | `Bitget` | `39.51%` | `60.49%` | `0.65` | 614,310.00 USD |
| `15M` | `BingX` | `49.06%` | `50.94%` | `0.96` | 186,500.00 USD |
| `15M` | `MEXC` | `45.35%` | `54.65%` | `0.83` | 2,230,000.00 USD |
| `15M` | `Bitunix` | `52.24%` | `47.76%` | `1.09` | 694,320.00 USD |
| `15M` | `Hyperliquid` | `81.39%` | `18.61%` | `4.37` | 146,240.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `65.47%` | `34.53%` | `1.90` | 70,830.00 USD |
| `15M` | `Crypto.com` | `72.96%` | `27.04%` | `2.70` | 37,240.00 USD |
| `15M` | `WhiteBIT` | `99.99%` | `0.01%` | `9999.00` | 1,920,000.00 USD |
| `15M` | `HTX` | `75.02%` | `24.98%` | `3.00` | 8,930.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `60.27%` | `39.73%` | `1.52` | 34,320.00 USD |
| `15M` | `Aster` | `34.27%` | `65.73%` | `0.52` | 105,790.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `25.08%` | `74.92%` | `0.33` | 33,450.00 USD |
| `15M` | `Whale Positions` | `49.89%` | `50.11%` | `1.00` | 4,060,000.00 USD |
| `15M` | `Global Accounts` | `57.40%` | `42.60%` | `1.35` | 12,870,000.00 USD |
| `1H` | `SOL` | `54.49%` | `45.51%` | `1.20` | 78,160,000.00 USD |
| `1H` | `Binance` | `49.48%` | `50.52%` | `0.98` | 23,150,000.00 USD |
| `1H` | `OKX` | `58.17%` | `41.83%` | `1.39` | 7,330,000.00 USD |
| `1H` | `Bybit` | `44.1%` | `55.9%` | `0.79` | 9,680,000.00 USD |
| `1H` | `KuCoin` | `51.16%` | `48.84%` | `1.05` | 97,200.00 USD |
| `1H` | `Gate` | `53.49%` | `46.51%` | `1.15` | 5,600,000.00 USD |
| `1H` | `Bitget` | `50.9%` | `49.1%` | `1.04` | 3,300,000.00 USD |
| `1H` | `BingX` | `20.34%` | `79.66%` | `0.26` | 4,030,000.00 USD |
| `1H` | `MEXC` | `54.46%` | `45.54%` | `1.20` | 8,960,000.00 USD |
| `1H` | `Bitunix` | `51.1%` | `48.9%` | `1.04` | 5,890,000.00 USD |
| `1H` | `Hyperliquid` | `77.06%` | `22.94%` | `3.36` | 1,070,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `69.33%` | `30.67%` | `2.26` | 392,970.00 USD |
| `1H` | `Crypto.com` | `69.17%` | `30.83%` | `2.24` | 144,740.00 USD |
| `1H` | `WhiteBIT` | `99.8%` | `0.2%` | `499.00` | 7,350,000.00 USD |
| `1H` | `HTX` | `72.32%` | `27.68%` | `2.61` | 88,290.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `52.83%` | `47.17%` | `1.12` | 256,480.00 USD |
| `1H` | `Aster` | `57.03%` | `42.97%` | `1.33` | 704,170.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `30.24%` | `69.76%` | `0.43` | 107,660.00 USD |
| `1H` | `Whale Positions` | `49.48%` | `50.52%` | `0.98` | 23,150,000.00 USD |
| `1H` | `Global Accounts` | `54.49%` | `45.51%` | `1.20` | 78,160,000.00 USD |
| `4H` | `SOL` | `45.49%` | `54.51%` | `0.83` | 521,330,000.00 USD |
| `4H` | `Binance` | `45.6%` | `54.4%` | `0.84` | 169,170,000.00 USD |
| `4H` | `OKX` | `45.46%` | `54.54%` | `0.83` | 54,230,000.00 USD |
| `4H` | `Bybit` | `41.78%` | `58.22%` | `0.72` | 73,590,000.00 USD |
| `4H` | `KuCoin` | `45.42%` | `54.58%` | `0.83` | 4,360,000.00 USD |
| `4H` | `Gate` | `47.77%` | `52.23%` | `0.91` | 24,170,000.00 USD |
| `4H` | `Bitget` | `43.31%` | `56.69%` | `0.76` | 37,340,000.00 USD |
| `4H` | `BingX` | `29.63%` | `70.37%` | `0.42` | 14,880,000.00 USD |
| `4H` | `MEXC` | `49.23%` | `50.77%` | `0.97` | 65,790,000.00 USD |
| `4H` | `Bitunix` | `48.16%` | `51.84%` | `0.93` | 30,360,000.00 USD |
| `4H` | `Hyperliquid` | `45.04%` | `54.96%` | `0.82` | 10,030,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `58.27%` | `41.73%` | `1.40` | 2,260,000.00 USD |
| `4H` | `Crypto.com` | `52.78%` | `47.22%` | `1.12` | 724,880.00 USD |
| `4H` | `WhiteBIT` | `52.14%` | `47.86%` | `1.09` | 25,140,000.00 USD |
| `4H` | `HTX` | `64.01%` | `35.99%` | `1.78` | 445,760.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `49.45%` | `50.55%` | `0.98` | 2,670,000.00 USD |
| `4H` | `Aster` | `41.54%` | `58.46%` | `0.71` | 5,630,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.03%` | `55.97%` | `0.79` | 560,650.00 USD |
| `4H` | `Whale Positions` | `45.6%` | `54.4%` | `0.84` | 169,170,000.00 USD |
| `4H` | `Global Accounts` | `45.49%` | `54.51%` | `0.83` | 521,330,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `101.00` | `101.32` | `101.00` | `101.77` | `100.97` | 23,345,961.64 USD | 9,081,895.18 USD | 14,264,066.46 USD | -5,182,171.27 USD | `-22.20%` | `6B / 20S` |
| `5:00 UTC` | `100.91` | `100.89` | `100.91` | `101.13` | `100.72` | 21,682,501.47 USD | 10,212,926.11 USD | 11,469,575.36 USD | -1,256,649.25 USD | `-5.80%` | `6B / 4S` |
| `0:00 UTC` | `101.07` | `101.03` | `101.07` | `101.19` | `100.90` | 11,845,890.84 USD | 5,647,320.15 USD | 6,198,570.68 USD | -551,250.53 USD | `-4.65%` | `2B / 1S` |
| `5:00 UTC` | `100.81` | `100.98` | `100.81` | `101.18` | `100.75` | 7,681,327.85 USD | 3,539,960.94 USD | 4,141,366.91 USD | -601,405.98 USD | `-7.83%` | `5B / 12S` |
| `0:00 UTC` | `100.38` | `100.47` | `100.38` | `100.81` | `100.30` | 26,755,803.01 USD | 9,721,488.50 USD | 17,034,314.50 USD | -7,312,826.00 USD | `-27.33%` | `0B / 21S` |
| `5:00 UTC` | `100.66` | `100.58` | `100.66` | `100.78` | `100.34` | 9,618,082.62 USD | 5,517,082.05 USD | 4,101,000.56 USD | 1,416,081.49 USD | `+14.72%` | `9B / 2S` |
| `0:00 UTC` | `100.38` | `100.40` | `100.38` | `100.62` | `100.25` | 9,521,682.83 USD | 4,738,635.78 USD | 4,783,047.06 USD | -44,411.28 USD | `-0.47%` | `0B / 7S` |
| `5:00 UTC` | `100.31` | `100.27` | `100.31` | `100.43` | `100.16` | 10,974,925.19 USD | 4,852,550.33 USD | 6,122,374.86 USD | -1,269,824.53 USD | `-11.57%` | `4B / 3S` |
| `0:00 UTC` | `100.10` | `100.18` | `100.10` | `100.38` | `100.09` | 16,033,450.26 USD | 8,994,633.57 USD | 7,038,816.68 USD | 1,955,816.89 USD | `+12.20%` | `5B / 2S` |
| `5:00 UTC` | `100.00` | `99.99` | `100.00` | `100.22` | `99.77` | 29,130,727.54 USD | 13,748,642.60 USD | 15,382,084.94 USD | -1,633,442.34 USD | `-5.61%` | `8B / 8S` |

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
| `5m` | 536,620.00 USD | 1,630,000.00 USD | **`ACCUMULATION`** |
| `15m` | 1,320,000.00 USD | 1,380,000.00 USD | **`ACCUMULATION`** |
| `30m` | 1,630,000.00 USD | 859,370.00 USD | **`ACCUMULATION`** |
| `1h` | 2,220,000.00 USD | 3,260,000.00 USD | **`ACCUMULATION`** |
| `2h` | 2,270,000.00 USD | -10,800,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -576,250.00 USD | -60,620,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 12,850,000.00 USD | -26,710,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 15,690,000.00 USD | -57,530,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 26,050,000.00 USD | -51,140,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 22,220,000.00 USD | -108,840,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 88,840,000.00 USD | -302,970,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 64,420,000.00 USD | -1,880,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+536.62K` | 15m=`+1.32M` | 1h=`+2.22M` | 24h=`+22.22M`
* Futures Capital Netflows: 5m=`+1.63M` | 15m=`+1.38M` | 1h=`+3.26M` | 24h=`-108.84M`
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
  * `2026-10-30 00:58:24 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:29:24 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:29:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `99.18` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `98.26` (Risk Distance: `0.9238` pts)
  * +2.5R Take Profit: `101.49`
  * Mathematical Lot Sizing: **`10.82 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `101.25` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `102.17` (Risk Distance: `0.9238` pts)
  * +2.5R Take Profit: `98.94`
  * Mathematical Lot Sizing: **`10.82 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`100.73`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
