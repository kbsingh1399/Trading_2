\n📚 **Active Skills Loaded & Applied:** `@[trader-signal]`, `@[trader-risk]`, `@[market-ingest]`, `@[market-pattern]`, `@[adaptive-wfo-epoch]`, `@[sharpe-ratio-non-iid-corrections]`, `@[time-series-decomposer]`, `@[clean-code]`, `@[systematic-debugging]`\n
\n```\n[ALERT] TELEMETRY STALE WARNING: Data/execution_preflight_receipt.json violates strict cutoff causality (tick_time_utc: 2026-10-24 18:37:45 UTC [+19.0s post-cutoff] & observed_at_utc: 2026-10-24 18:37:46 UTC [+20.0s post-cutoff] vs cutoff_utc: 2026-10-24 18:37:26 UTC; Current Cycle: 2026-10-24 18:37:39 UTC)
[ALERT] TELEMETRY STALE WARNING: Data/macro_calendar.json is stale (Last updated: 2026-10-24 17:56:08 UTC [age: 2,477.3s at cutoff / 2,490.3s at Current Cycle > 900s limit] vs Current Cycle: 2026-10-24 18:37:39 UTC)
[ALERT] TELEMETRY STALE WARNING: Data/forex_factory_live.json is stale (Last updated: 2026-10-24 17:58:00 UTC [age: 2,366.0s at cutoff / 2,379.0s at Current Cycle] vs Current Cycle: 2026-10-24 18:37:39 UTC)
[ALERT] TELEMETRY STALE WARNING: Data/excel_all_sheets_checklist.json is stale / failing (Last updated: 2026-10-24 18:19:44 UTC [all_passed: false, 26/31 passed, 5 failed] vs Current Cycle: 2026-10-24 18:37:39 UTC)
[ALERT] TELEMETRY STALE WARNING: Data/DataBase_Trading.xlsx :: 17_Orderbook is stale (Last updated: 2026-10-24 18:01:50 UTC [age: 2,136s = 35m 36s at cutoff] vs Current Cycle: 2026-10-24 18:37:39 UTC)
[ALERT] TELEMETRY STALE WARNING: Data/DataBase_Trading.xlsx :: 2_Spot_Netflow_S is stale (Last updated: 2026-10-24 18:07:31 UTC [age: 1,795s = 29m 55s at cutoff] vs Current Cycle: 2026-10-24 18:37:39 UTC)
[ALERT] TELEMETRY STALE WARNING: Data/DataBase_Trading.xlsx :: 6_Funding_Fee_Settlement is stale (Last updated: 2026-10-24 17:29:26 UTC [age: 4,080s = 68m 00s at cutoff] vs Current Cycle: 2026-10-24 18:37:39 UTC)
[ALERT] TELEMETRY STALE WARNING: Data/DataBase_Trading.xlsx :: 5_Funding_Rate is stale (Last updated: 2026-10-24 17:28:25 UTC [age: 4,141s = 69m 01s at cutoff] vs Current Cycle: 2026-10-24 18:37:39 UTC)
[ALERT] TELEMETRY STALE WARNING: Data/DataBase_Trading.xlsx :: 9_Liquidation_Max_Pain_7D is stale (Last updated: 2026-10-24 17:17:05 UTC [age: 4,821s = 80m 21s at cutoff] vs Current Cycle: 2026-10-24 18:37:39 UTC)
[ALERT] TELEMETRY STALE WARNING: Data/DataBase_Trading.xlsx :: 9_Liquidation_Max_Pain_3D is stale (Last updated: 2026-10-24 17:16:34 UTC [age: 4,852s = 80m 52s at cutoff] vs Current Cycle: 2026-10-24 18:37:39 UTC)
[ALERT] TELEMETRY STALE WARNING: Data/DataBase_Trading.xlsx :: 7_Live_Liq is stale (Last updated: 2026-10-24 17:13:26 UTC [age: 5,040s = 84m 00s at cutoff] vs Current Cycle: 2026-10-24 18:37:39 UTC)
[ALERT] TELEMETRY STALE WARNING: Data/DataBase_Trading.xlsx :: Crypto_ETF_Flows, Top_Institutions, ETF_Market_Overview are static legacy sheets (Last updated: 2026-10-17 13:23:21 UTC vs Current Cycle: 2026-10-24 18:37:39 UTC)\n```\n\n---\n\n# 0. Universal Metacognitive & Skills-Mobilization Inquest\n\n\n### Mandatory Evaluation Question: "If it use all the available skills related will it improve our response?"\n\n\n**Answer: YES — unequivocally and with decisive mathematical, microstructural, and solvency impact in `Cycle-20261024T183726Z`.**\n\nBetween `Cycle-20261024T175720Z` and `Cycle-20261024T183726Z` (`git_commit = 54d93c2a87ef92e0d6eed2369e6ed1b60e3925f9`, `as_of_utc = 2026-10-24 18:36:26 UTC`), **two transformative production milestones** occurred in the live account and master workbook `Data/DataBase_Trading.xlsx` (`5,180,986` bytes, `sha256: 133e868a5ee684e151189e5acb49fbef45ec34055f5ffd879cfab031da14175e`):\n\n1. **Ticket `#19274977` (`BTCUSD.pi` `SELL` `0.05` lot @ `80,245.00`, `SL = 80,620.00`, `TP = 79,385.00`) FILLED at `2026-10-24 18:11:19 UTC` (`time: 1792876279`) and is now an ACTIVE LIVE SHORT POSITION** (`active_positions_count = 1`, `pending_orders_count = 0`, `price_current = 80,196.00`, `floating_profit = +$2.45 USD`, `margin_used = $2,006.13 USD`, `margin_free = $2,861.39 USD`, `margin_level = 242.6323%`).\n2. **All 14 Crypto Perpetuals in `docs/telemetry/live_snapshot_latest.json` (`18:36:26 UTC`) AND the Core Orderflow Sheets of `Data/DataBase_Trading.xlsx` Were Massively Upgraded:**
\n- Every crypto asset in `assets_matrix_24` (`BTC`, `ETH`, `SOL`, `BNB`, `XRP`, `ADA`, `DOGE`, `TRX`, `DOT`, `LINK`, `BCH`, `LTC`, `AVAX`, `NEAR`) now has clean, un-spliced 100-bar `15m`, 96-bar `1H`, and 96-bar `4H` OHLCV histories plus populated `causal_indicators` (`vwap_z_score`, `rsi_14`, `atr_14`) and `pullback_geometry`.\n- Sheet `21_Tradfye_Orderflow` (`18:34:32 UTC`) expanded from `122` rows to **`6,912` multi-timeframe (`5m`, `15m`, `1h`) candle orderflow rows** with `Total Vol ($)`, `Taker Buy Vol ($)`, `Taker Sell Vol ($)`, `Net Delta ($)`, `Net Delta (%)`, `CVD ($)`, `Candle VWAP ($)`, `POC Estimate ($)`, `Orderflow Regime`, `Delta Divergence`, and `Deribit Max Pain / Call Wall / Put Wall ($)`.\n- Sheet `20_Auction_Market_Structure` (`18:34:02 UTC`, `173` rows) and Sheet `18_CVD` (`18:33:26 UTC`, `1,500` rows) were freshly regenerated inside the 4-minute window before `cutoff_utc`.\n\n\nMobilizing all 9 specialized quantitative skills (`@[trader-signal]`, `@[trader-risk]`, `@[market-ingest]`, `@[market-pattern]`, `@[adaptive-wfo-epoch]`, `@[sharpe-ratio-non-iid-corrections]`, `@[time-series-decomposer]`, `@[clean-code]`, `@[systematic-debugging]`) directly uncovers three mission-critical findings that a superficial review would miss:\n\n| Loaded Skill | Concrete Improvement Delivered in `Cycle-20261024T183726Z` |\n| --- | --- |\n| **`@[systematic-debugging]` & `@[clean-code]`** | **1. Uncovers the `margin_level_post_order` Denominator Omission Bug in `execution_preflight_receipt.json`:** Because `#19274977` is now an **active filled position**, `margin_used` is already **`$2,006.13 USD`** (`41.24%` of `$4,865.07` balance). When preflight tested `CAND_BTC_PREFLIGHT_81300` (`0.04` lot `BTCUSD.pi` @ `81,300.00`, `margin_required_usd = $1,626.00`), `margin_free_post_order` dropped from `$2,861.29` to **`$1,235.29`**, proving total post-fill margin is **`$2,006.13 + $1,626.00 = $3,632.13` (`74.66% > 50.0%` cap!)** and true post-fill Margin Level is **`$4,867.42 / $3,632.13 = 134.01% < 200.0%` floor!** Yet `execution_preflight.py` reported `"margin_level_post_order": 299.35` by dividing `$4,867.42 / $1,626.00` alone without adding existing `$2,006.13` `margin_used`! **2. Catches the `+19s/+20s` Post-Cutoff Causality Violation (`18:37:45 UTC > 18:37:26 UTC`) and Nonce Signature Mismatch (`d0ee05e4...` vs `3d9432a3...`).** |\n| **`@[time-series-decomposer]` & `@[sharpe-ratio-non-iid-corrections]`** | Computes exact Lo-MacKinlay heteroskedasticity-robust VR(4)VR(4)VR(4) & z∗(4)z^*(4)z∗(4), Kaufman ER(48)ER(48)ER(48), Newey-West HAC tslopet_{\text{slope}}tslope​ (L=3L=3L=3), and discrete Ornstein-Uhlenbeck equilibrium θOU=−a/b\theta_{\text{OU}} = -a/bθOU​=−a/b across all 14 newly repaired crypto series in `live_snapshot_latest.json` (`18:36:26 UTC`). Identifies **`ETHUSD.pi` (`VR(4) = 1.3630`, `ER(48) = 0.2152 >= 0.20`, `t_slope = -6.6610`, θOU,15m=$2,334.54\theta_{\text{OU,15m}} = \$2,334.54θOU,15m​=$2,334.54, θOU,1H=$2,049.07\theta_{\text{OU,1H}} = \$2,049.07θOU,1H​=$2,049.07)** and **`BNBUSD.p` (`VR(4) = 1.1776`, `ER(48) = 0.2365 >= 0.20`, `t_slope = -10.8216`, θOU,15m=$725.95\theta_{\text{OU,15m}} = \$725.95θOU,15m​=$725.95)** as the **only two spread-eligible crypto perpetuals passing both VR(4)>1.15VR(4) > 1.15VR(4)>1.15 and ER(48)≥0.20ER(48) \ge 0.20ER(48)≥0.20**, whereas `BTCUSD.pi` has ER(48)=0.0840<0.15ER(48) = 0.0840 < 0.15ER(48)=0.0840<0.15 (`ROTATIONAL_BALANCE` / `NEUTRAL CHOP`). |\n| **`@[market-ingest]` & `@[market-pattern]`** | Integrates the newly expanded **Sheet `21_Tradfye_Orderflow` (`6,912` rows at `18:34:32 UTC`)**, **Sheet `10_Whale_Orders` (`18:18:29 UTC`)**, **Sheet `15_Hyperdash_Stops_Map` (`18:31:15 UTC`)**, and **Sheet `17_Orderbook` (`18:01:50 UTC`)** to audit active position `#19274977`: proves that immediately after `#19274977` filled at `80,245.00` (`18:11:19 UTC`), institutional sellers hit the `18:15 UTC` 15m candle with **`-$14,090,541.33` Net Taker Sell Delta** defending `$22.48M` of aged (`2h 31m–3h 43m`) Binance sell walls at `80,377.40–80,500.00`, while revealing that `#19274977`'s `TP = 79,385.00` sits behind **`$7.35M` L3 bid wall at `79,881.00`, `$5.93M` aged (`1h 04m–1h 25m`) Binance bid wall at `79,850.00`, and `$14.36M` L3 bid wall at `79,529.00`**. |\n| **`@[trader-signal]`, `@[trader-risk]` & `@[adaptive-wfo-epoch]`** | Enforces the **Zero Floating Profit Credit Invariant (§1.3.5: min⁡(Bal,Eq)=$4,865.07\min(\text{Bal}, \text{Eq}) = \$4,865.07min(Bal,Eq)=$4,865.07, excluding `+$2.45` floating PnL)** and computes the exact **Remaining 50% Crypto Margin Capacity (`$2,432.535 - $2,006.13 = $426.41 USD`)** while `#19274977` is open. Proves that sizing **`ETHUSD.pi` (`CAND_ETH_OTE_235650` @ `2,356.50`, `SL = 2,401.50`, `TP = 2,266.50`) at `0.36` lot** consumes **`$424.17` margin (`<= $426.41`, total margin `$2,430.30 = 49.95% <= 50.0%`, combined Margin Level `200.18% >= 200.0%`)** and **`$17.35` nominal risk (`$23.69` stressed loss `<= $39.57` remaining headroom)**! |\n\n\n---\n\n# Part 1 — Exhaustive 4-Persona Quantitative Council Audit (§1–§7)\n\n\n## §1.1 Role A — Statistical Regime, Diffusion & Dual-Engine Dialectic (@[trader-signal], @[time-series-decomposer], @[sharpe-ratio-non-iid-corrections])\n\n\n### 1.1.1 Multi-Horizon Econometric Matrix (Data/DataBase_Trading.xlsx + Newly Repaired live_snapshot_latest.json at 18:36:26 UTC)\n\n\nIn commit `54d93c2a87ef92e0d6eed2369e6ed1b60e3925f9` (`as_of_utc: 2026-10-24 18:36:26 UTC`), all 14 crypto perpetuals in `assets_matrix_24` now carry clean 100-bar `15m`, 96-bar `1H`, and 96-bar `4H` OHLCV series. Applying the Lo-MacKinlay (1988) heteroskedasticity-consistent variance ratio VR(q=4)VR(q=4)VR(q=4) with asymptotic test statistic z∗(q)=T(VR(q)−1)/ϕ^(q)z^*(q) = \sqrt{T}(VR(q)-1)/\sqrt{\hat{\phi}(q)}z∗(q)=T​(VR(q)−1)/ϕ^​(q)​, Kaufman Efficiency Ratio ER(N=48)ER(N=48)ER(N=48), Newey-West (1987) HAC trend ttt-statistics (L=⌊4(T/100)2/9⌋=3L = \lfloor 4(T/100)^{2/9}\rfloor = 3L=⌊4(T/100)2/9⌋=3), and discrete Ornstein-Uhlenbeck (OU) mean-reversion regressions ΔPt=a+bPt−1+εt\Delta P_t = a + b P_{t-1} + \varepsilon_tΔPt​=a+bPt−1​+εt​ (θOU=−a/b\theta_{\text{OU}} = -a/bθOU​=−a/b, t1/2=−ln⁡(2)/ln⁡(1+b)t_{1/2} = -\ln(2)/\ln(1+b)t1/2​=−ln(2)/ln(1+b)) across the 12 spread-eligible crypto perpetuals (`spread <= 25.0 bps` in `00_MT5_Account_Telemetry` / `20_Auction_Market_Structure`) yields:\n\n| Symbol (`Broker`) | Timeframe | Mid (`00_MT5` / `Snap`) | Spread (`bps`) | VR(q=4)VR(q=4)VR(q=4) | z∗(4)z^*(4)z∗(4) (Het-Robust) | ER(48)ER(48)ER(48) | NW trett_{\text{ret}}tret​ (L=3L=3L=3) | NW tslopet_{\text{slope}}tslope​ (L=3L=3L=3) | OU bOUb_{\text{OU}}bOU​ | OU θOU\theta_{\text{OU}}θOU​ (`$`) | Half-Life t1/2t_{1/2}t1/2​ | Sheet `11_Technical` Trend Bias (`VWAP Z`, `RSI_14`, `ATR_14`) |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| **`BTCUSD.pi`** | **15m** (`n=100`) | `80,166.0` / `80,226.0` | **`2.00`** / **`1.99`** | **`1.1869`** | `+0.6631` | **`0.0840`** | `-0.8957` | **`-7.6456`** | `-0.049567` | **`80,405.42`** | `13.6b` (`3.4h`) | `NEUTRAL / CHOP` (`Z=-0.258`, `RSI=53.47`, `ATR=278.94`) |\n| **`BTCUSD.pi`** | **1H** (`n=96`) | `80,226.0` | `1.99` | `1.0632` | `+0.2919` | `0.1131` | `-0.9674` | **`-7.8911`** | `-0.007644` | **`78,885.89`** | `90.3b` (`90.3h`) | **1H Downward OU Drift toward `78,885.89`** |\n| **`BTCUSD.pi`** | **4H** (`n=96`) | `80,226.0` | `1.99` | `0.9469` | `-0.2079` | `0.0750` | `-0.3499` | `-2.5722` | `-0.134935` | `82,122.56` | `4.8b` (`19.2h`) | `20_AMS`: `ROTATIONAL_BALANCE` |\n| **`ETHUSD.pi`** | **15m** (`n=100`) | `2,321.1` / `2,328.5` | **`13.79`** / **`13.74`** | **`1.3630`** | **`+1.0141`** | **`0.2152`** | `-1.0755` | **`-6.6610`** | `-0.024287` | **`2,334.54`** | `28.2b` (`7.0h`) | **`STRONG BEARISH`** (`Z=-0.896`, `RSI=44.54`, `ATR=11.11`) |\n| **`ETHUSD.pi`** | **1H** (`n=96`) | `2,328.5` | `13.74` | `0.9773` | `-0.0944` | `0.1575` | `-1.2088` | **`-7.9043`** | `-0.003356` | **`2,049.07`** | `206.2b` | **`20_AMS`: `TREND_DOWN_ACCEPTANCE`** |\n| **`ETHUSD.pi`** | **4H** (`n=96`) | `2,328.5` | `13.74` | `0.7950` | `-0.7716` | `0.1484` | `-0.7411` | **`-6.6423`** | `-0.081485` | `2,425.83` | `8.2b` (`32.8h`) | **Monotonic Bearish EMA Ribbon (`5 < 13 < 34 < 89 < 144 < 233`)** |\n| **`BNBUSD.p`** | **15m** (`n=100`) | `725.05` / `726.10` | **`6.90`** / **`8.26`** | **`1.1776`** | `+0.7360` | **`0.2365`** | `-1.4370` | **`-10.8216`** | `-0.023235` | **`725.95`** | `29.5b` (`7.4h`) | `NEUTRAL / CHOP` (`Z=-0.640`, `RSI=49.30`, `ATR=2.11`) |\n| **`BNBUSD.p`** | **1H** (`n=96`) | `726.10` | `8.26` | `1.1223` | `+0.5700` | `0.0415` | `-0.6508` | `-2.8658` | `-0.021598` | `732.41` | `31.7b` (`31.7h`) | `21_Tradfye`: **`AGGRESSIVE_SELLER_DOMINATION`** |\n| **`SOLUSD.p`** | **15m** (`n=100`) | `100.57` / `100.90` | **`23.86`** / **`23.79`** | **`1.1575`** | `+0.5694` | `0.1224` | `-1.4018` | **`-11.6882`** | `-0.034553` | **`100.78`** | `19.7b` (`4.9h`) | `NEUTRAL / CHOP` (`Z=-0.536`, `RSI=51.83`, `ATR=0.551`) |\n| **`BCHUSD.p`** | **15m** (`n=100`) | `272.50` / `273.40` | **`17.61`** / **`17.56`** | `0.9752` | `-0.1064` | `0.1040` | `-1.3075` | **`-9.9693`** | `-0.045494` | **`274.63`** | `14.9b` (`3.7h`) | `STRONG BEARISH` (`Z=-1.441`, `RSI=44.98`, `ATR=1.690`) |\n| **`XRPUSD.pi`** | **15m** (`n=100`) | `1.2785` / `1.2830` | **`23.46`** / `31.18` | `1.0397` | `+0.1598` | `0.0500` | `-0.7897` | **`-10.1723`** | `-0.051446` | **`1.2799`** | `13.1b` (`3.3h`) | `NEUTRAL / CHOP` (`Z=+0.005`, `RSI=52.99`, `ATR=0.0065`) |\n| **`XMRUSD.p`** | **15m** (`11_Tech`) | `602.09` / `605.37` | **`3.49`** / **`6.44`** | *Workbook* | *Workbook* | *Range Exp* | *Bullish* | *Bullish* | *N/A* | *N/A* | *N/A* | `BULLISH` (`Z=+1.660`, `RSI=62.03`, `ATR=4.3922`) |\n| **`ZECUSD.p`** | **15m** (`11_Tech`) | `1,162.22` / `1,186.24` | **`6.71`** / **`7.59`** | *Workbook* | *Workbook* | *Range Exp* | *Neutral* | *Bearish* | *N/A* | *N/A* | *N/A* | `NEUTRAL / CHOP` (`Z=+0.132`, `RSI=57.14`, `ATR=9.9630`) |\n| **`DSHUSD.p`** | **15m** (`11_Tech`) | `49.9065` / `50.200` | **`9.42`** / **`10.56`** | *Workbook* | *Workbook* | *Balance* | *Bearish* | *Bearish* | *N/A* | *N/A* | *N/A* | `STRONG BEARISH` (`Z=-1.160`, `RSI=43.83`, `ATR=0.4487`) |\n| **`YFIUSD.p`** | **15m** (`11_Tech`) | `2,135.5` / `2,143.0` | **`14.98`** / **`19.62`** | *Workbook* | *Workbook* | *Balance* | *Bearish* | *Bearish* | *N/A* | *N/A* | *N/A* | `STRONG BEARISH` (`Z=-0.601`, `RSI=47.92`, `ATR=11.8091`) |\n| **`XLMUSD.p`** | **15m** (`11_Tech`) | `0.16969` / `0.1700` | **`17.68`** / **`18.84`** | *Workbook* | *Workbook* | *Balance* | *Neutral* | *Bearish* | *N/A* | *N/A* | *N/A* | `NEUTRAL / CHOP` (`Z=-0.370`, `RSI=53.15`, `ATR=0.0008`) |\n| **`AVEUSD.p`** | **15m** (`11_Tech`) | `136.025` / `136.46` | **`19.85`** / **`20.54`** | *Workbook* | *Workbook* | *Balance* | *Bearish* | *Bearish* | *N/A* | *N/A* | *N/A* | `STRONG BEARISH` (`Z=-1.066`, `RSI=38.30`, `ATR=0.8845`) |\n\n\n---\n\n### 1.1.2 Dual-Engine Dialectic (Model 1 Mean Reversion vs. Model 2 Trend Pullback)\n\n\n1. **`ETHUSD.pi` (`Mid = $2,328.50` in `live_snapshot_latest.json` / `$2,331.90` in `20_Auction_Market_Structure`, `Spread = 13.73–13.79 bps <= 25.0 bps`) — CLEANEST MODEL 2 TREND-PULLBACK ENGINE IN THE UNIVERSE:**
\n- **Model 1 (Mean Reversion):** **REJECTED.** VR(4)=1.3630>1.15VR(4) = 1.3630 > 1.15VR(4)=1.3630>1.15 (z∗=+1.0141z^* = +1.0141z∗=+1.0141) and ER(48)=0.2152≥0.20ER(48) = 0.2152 \ge 0.20ER(48)=0.2152≥0.20 (`TREND_DOWN_ACCEPTANCE` in Sheet `20_Auction_Market_Structure`, `STRONG BEARISH` in Sheet `11_Technical`) disqualify counter-trend mean-reversion fades.\n- **Model 2 (Trend Pullback):** **STRUCTURALLY QUALIFIED.** `ETHUSD.pi` satisfies all three statistical trend criteria simultaneously: VR(4)=1.3630>1.15VR(4) = 1.3630 > 1.15VR(4)=1.3630>1.15, ER(48)=0.2152≥0.20ER(48) = 0.2152 \ge 0.20ER(48)=0.2152≥0.20, and Newey-West HAC tslope=−6.6610t_{\text{slope}} = -6.6610tslope​=−6.6610 on 15m (tslope=−7.9043t_{\text{slope}} = -7.9043tslope​=−7.9043 on 1H, ∣t∣≥2.0|t| \ge 2.0∣t∣≥2.0), with `pullback_geometry` in `live_snapshot_latest.json` confirming a controlled corrective pullback (`direction = SHORT`, `retrace = 0.5849`, `velocity_ratio = 0.4915 < 1.0`, `bars_pullback = 12`, `bars_impulse = 10`).\n\n2. **`BNBUSD.p` (`Mid = $726.10` in `live_snapshot_latest.json` / `$726.40` in `20_Auction_Market_Structure`, `Spread = 6.90–8.26 bps <= 25.0 bps`) — SECOND MODEL 2 TREND-PULLBACK ENGINE:**
\n- **Model 1 (Mean Reversion):** **REJECTED** (VR(4)=1.1776>1.15VR(4) = 1.1776 > 1.15VR(4)=1.1776>1.15, ER(48)=0.2365≥0.20ER(48) = 0.2365 \ge 0.20ER(48)=0.2365≥0.20, tslope=−10.8216t_{\text{slope}} = -10.8216tslope​=−10.8216).\n- **Model 2 (Trend Pullback):** **ECONOMETRICALLY QUALIFIED** (VR(4)=1.1776>1.15VR(4) = 1.1776 > 1.15VR(4)=1.1776>1.15, ER(48)=0.2365≥0.20ER(48) = 0.2365 \ge 0.20ER(48)=0.2365≥0.20, tslope=−10.8216t_{\text{slope}} = -10.8216tslope​=−10.8216, `pullback_geometry: retrace = 0.6513, velocity_ratio = 0.4903`), supported by Sheet `21_Tradfye_Orderflow` (`18:34:32 UTC`: `AGGRESSIVE_SELLER_DOMINATION / BEARISH_EXPANSION`, `Net Delta = -$215,585.51 [-27.82%]`). Only minor caveat: in Sheet `11_Technical`, `EMA 5 ($723.78) > EMA 13 ($723.42)` at the lower ribbon tip (`Bias = NEUTRAL / CHOP`).\n\n3. **`BTCUSD.pi` (`Mid = $80,190.50` in preflight / `$80,226.00` in snapshot / `$80,239.50` in `20_AMS`, `Spread = 1.87–2.00 bps <= 25.0 bps`) — ACTIVE SHORT POSITION `#19274977` IN ROTATIONAL BALANCE:**
\n- While VR(4)=1.1869>1.15VR(4) = 1.1869 > 1.15VR(4)=1.1869>1.15 and Newey-West tslope=−7.6456t_{\text{slope}} = -7.6456tslope​=−7.6456 (`15m`) / −7.8911-7.8911−7.8911 (`1H`), Kaufman Efficiency Ratio on `BTCUSD.pi` is **`ER(48) = 0.0840 < 0.15`** (`ROTATIONAL_BALANCE` in Sheet `20_Auction_Market_Structure`, `NEUTRAL / CHOP` in Sheet `11_Technical`).\n- Because `#19274977` (`0.05` lot `SELL` @ `80,245.00`) is **already filled and open** (`+$2.45 USD` floating profit at `80,196.00`), no second `BTCUSD.pi` ticket may be staged (`CAND_BTC_PREFLIGHT_81300` is rejected on both 50% margin cap and correlation/regime grounds), and `#19274977` is actively managed with a front-run TP ratchet.\n\n\n---\n\n### 1.1.3 Fibonacci Prime EMA Ribbon Hierarchy (5, 13, 34, 89, 144, 233) (@[market-pattern])\n\n\nCross-examining Sheet `11_Technical` (`18:28:14 UTC`) across all 12 spread-eligible crypto perpetuals:\n\nBearish Monotonicity Condition: EMA5<EMA13<EMA34<EMA89<EMA144<EMA233\text{Bearish Monotonicity Condition: } \text{EMA}_5 < \text{EMA}_{13} < \text{EMA}_{34} < \text{EMA}_{89} < \text{EMA}_{144} < \text{EMA}_{233}Bearish Monotonicity Condition: EMA5​<EMA13​<EMA34​<EMA89​<EMA144​<EMA233​\n\n| Symbol | Price (`$`) | `EMA_5` | `EMA_13` | `EMA_34` | `EMA_89` | `EMA_144` | `EMA_233` | `EMA_233` Slope (`%/3h`) | Strict Monotonic Hierarchy? | Sheet `11_Technical` Trend Bias |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| **`ETHUSD.pi`** | `2,320.10` | **`2,315.17`** | **`2,315.93`** | **`2,332.58`** | **`2,356.25`** | **`2,370.61`** | **`2,387.80`** | `-0.858%` | **YES (`5 < 13 < 34 < 89 < 144 < 233`)** | **`STRONG BEARISH`** |\n| **`BCHUSD.p`** | `271.66` | **`271.61`** | **`271.68`** | **`273.33`** | **`276.22`** | **`277.77`** | **`278.44`** | `-0.511%` | **YES (`5 < 13 < 34 < 89 < 144 < 233`)** | **`STRONG BEARISH`** |\n| **`AVEUSD.p`** | `135.38` | **`135.19`** | **`135.45`** | **`137.20`** | **`140.48`** | **`142.59`** | **`144.98`** | `-1.192%` | **YES (`5 < 13 < 34 < 89 < 144 < 233`)** | **`STRONG BEARISH`** |\n| **`DSHUSD.p`** | `49.732` | **`49.631`** | **`49.728`** | **`50.200`** | **`51.079`** | **`51.487`** | **`51.611`** | `-0.587%` | **YES (`5 < 13 < 34 < 89 < 144 < 233`)** | **`STRONG BEARISH`** |\n| **`YFIUSD.p`** | `2,139.90` | **`2,136.91`** | **`2,137.28`** | **`2,145.73`** | **`2,158.78`** | **`2,166.29`** | **`2,173.58`** | `-0.453%` | **YES (`5 < 13 < 34 < 89 < 144 < 233`)** | **`STRONG BEARISH`** |\n| **`BNBUSD.p`** | `725.10` | `723.78` | `723.42` | `726.33` | `731.70` | `734.30` | `735.68` | `-0.351%` | **NO** (`EMA_5 > EMA_13` by `+$0.36`) | `NEUTRAL / CHOP` |\n| **`BTCUSD.pi`** | `80,225.00` | `80,091.84` | `80,009.34` | `80,173.63` | `80,560.55` | `80,897.29` | `81,374.85` | `-0.422%` | **NO** (`EMA_5 > EMA_13` by `+$82.50`) | `NEUTRAL / CHOP` |\n| **`SOLUSD.p`** | `100.48` | `100.20` | `100.09` | `100.52` | `101.54` | `102.28` | `103.16` | `-0.684%` | **NO** (`EMA_5 > EMA_13` by `+$0.11`) | `NEUTRAL / CHOP` |\n| **`XRPUSD.pi`** | `1.2750` | `1.2727` | `1.2711` | `1.2739` | `1.2837` | `1.2930` | `1.3062` | `-0.742%` | **NO** (`EMA_5 > EMA_13` by `+$0.0016`) | `NEUTRAL / CHOP` |\n| **`XLMUSD.p`** | `0.16944` | `0.1691` | `0.1689` | `0.1693` | `0.1711` | `0.1727` | `0.1747` | `-0.812%` | **NO** (`EMA_5 > EMA_13` by `+$0.0002`) | `NEUTRAL / CHOP` |\n| **`ZECUSD.p`** | `1,160.08` | `1,155.88` | `1,151.38` | `1,152.61` | `1,169.51` | `1,187.27` | `1,211.69` | `-1.345%` | **NO** (`EMA_5 > EMA_13 > EMA_34`) | `NEUTRAL / CHOP` |\n| **`XMRUSD.p`** | `605.46` | `603.88` | `601.61` | `596.93` | `594.27` | `596.88` | `603.08` | `-0.088%` | **NO** (`EMA_89 < EMA_144 < EMA_233`) | `BULLISH` |\n\n\n- **Crucial Cross-Verification:** **`ETHUSD.pi` is the ONLY spread-eligible crypto asset in the entire 156-symbol broker universe that simultaneously passes:**
\n1. VR(4)=1.3630>1.15VR(4) = 1.3630 > 1.15VR(4)=1.3630>1.15,\n2. ER(48)=0.2152≥0.20ER(48) = 0.2152 \ge 0.20ER(48)=0.2152≥0.20 (`TREND_DOWN_ACCEPTANCE`),\n3. Newey-West tslope=−6.6610t_{\text{slope}} = -6.6610tslope​=−6.6610 (`15m`) and −7.9043-7.9043−7.9043 (`1H`), AND\n4. **100% Monotonic Bearish Fibonacci Prime EMA Ribbon Alignment (`2,315.17 < 2,315.93 < 2,332.58 < 2,356.25 < 2,370.61 < 2,387.80`, `STRONG BEARISH`)!**\n\n\n---\n\n### 1.1.4 Fibonacci Retracement & Golden Pocket / OTE Zone ([0.618 GP, 0.702 OTE])\n\n\nFrom Sheet `20_Auction_Market_Structure` (`18:34:02 UTC`):\n\n1. **`ETHUSD.pi` (`Fib Swing High = $2,400.40`, `Fib Swing Low = $2,275.30`, `Range = $125.10`, `BEARISH_IMPULSE`):**
\n- `0.618 GP Lower`: **`$2,352.61`** (2,275.30+0.618×125.10=2,352.61182,275.30 + 0.618 \times 125.10 = 2,352.61182,275.30+0.618×125.10=2,352.6118)\n- `0.650 GP Upper`: **`$2,356.62`** (2,275.30+0.650×125.10=2,356.61502,275.30 + 0.650 \times 125.10 = 2,356.61502,275.30+0.650×125.10=2,356.6150) — **exact confluence with `EMA_89 = $2,356.25`!**\n- `0.702 OTE`: **`$2,363.12`** (2,275.30+0.702×125.10=2,363.12022,275.30 + 0.702 \times 125.10 = 2,363.12022,275.30+0.702×125.10=2,363.1202) — **exact confluence with the `$4,698,410.56` Hyperliquid L3 Whale Ask Wall at `$2,363.30` (`17_Orderbook`)!**\n- `0.786 Invalidation Shelf`: **`$2,373.63`** (2,275.30+0.786×125.10=2,373.62862,275.30 + 0.786 \times 125.10 = 2,373.62862,275.30+0.786×125.10=2,373.6286)\n- **Candidate `CAND_ETH_OTE_235650` (`Entry = $2,356.50`):** Sits squarely inside the `[2,352.61, 2,363.12]` Golden Zone at the **`0.650` Golden Pocket (`2,356.62`) + `EMA_89` (`2,356.25`)**!\n\n2. **`BNBUSD.p` (`Fib Swing High = $744.60`, `Fib Swing Low = $716.50`, `Range = $28.10`, `BEARISH_IMPULSE`):**
\n- `0.618 GP Lower`: **`$733.87`** (716.50+0.618×28.10=733.8658716.50 + 0.618 \times 28.10 = 733.8658716.50+0.618×28.10=733.8658)\n- `0.650 GP Upper`: **`$734.76`** (716.50+0.650×28.10=734.7650716.50 + 0.650 \times 28.10 = 734.7650716.50+0.650×28.10=734.7650) — **exact confluence with `EMA_144 = $734.30`!**\n- `0.702 OTE`: **`$736.23`** (716.50+0.702×28.10=736.2262716.50 + 0.702 \times 28.10 = 736.2262716.50+0.702×28.10=736.2262) — **exact confluence with `d_POC = $736.34`!**\n- `0.786 Invalidation Shelf`: **`$738.59`** (716.50+0.786×28.10=738.5866716.50 + 0.786 \times 28.10 = 738.5866716.50+0.786×28.10=738.5866)\n- **Candidate `CAND_BNB_OTE_73475` (`Entry = $734.75`):** Sits squarely inside the `[733.87, 736.23]` Golden Zone at the **`0.650` Golden Pocket (`734.76`) + `EMA_144` (`734.30`)**!\n\n3. **`BTCUSD.pi` (`Fib Swing High = $81,445.50`, `Fib Swing Low = $79,071.00`, `Range = $2,374.50`, `BEARISH_IMPULSE`):**
\n- `0.618 GP Lower`: **`$80,538.44`** | `0.650 GP Upper`: **`$80,614.43`** | `0.702 OTE`: **`$80,737.90`** | `0.786 Invalidation`: **`$80,937.36`**.\n- **Preflight Candidate `CAND_BTC_PREFLIGHT_81300` (`Entry = $81,300.00`):** Sits at **`0.9387` Fib retracement**, `+562.10 pts` above `0.702 OTE` (`80,737.90`) and `+362.64 pts` above `0.786 Invalidation` (`80,937.36`), violating the Model 2 Golden Zone `[0.618, 0.702]` mandate.\n\n\n---\n\n### 1.1.5 Discrete Ornstein-Uhlenbeck (OU) Equilibrium 
𝜃
OU
θ
OU
	​

 & Adverse Drift Veto Gate\n\n\nFor any passive `SELL_LIMIT` at Entry\text{Entry}Entry, §1.1.5 requires θOU≤Entry\theta_{\text{OU}} \le \text{Entry}θOU​≤Entry so mean-reverting drift pulls price **downward** from entry toward TP rather than upward toward SL:\n\n1. **`CAND_ETH_OTE_235650` (`ETHUSD.pi` `SELL_LIMIT` @ `$2,356.50`):**
\n- **15m OU Equilibrium:** θOU,15m=$2,334.54\theta_{\text{OU,15m}} = \mathbf{\$2,334.54}θOU,15m​=$2,334.54 (bOU=−0.024287b_{\text{OU}} = -0.024287bOU​=−0.024287, t1/2=28.2 barst_{1/2} = 28.2\text{ bars}t1/2​=28.2 bars). Since Entry=$2,356.50>θOU,15m=$2,334.54\text{Entry} = \$2,356.50 > \theta_{\text{OU,15m}} = \$2,334.54Entry=$2,356.50>θOU,15m​=$2,334.54, OU drift pulls **downward by `-21.96 pts` (`-93.2 bps`)** toward TP (`$2,266.50`). **PASSES 15m OU Gate.**\n- **1H OU Equilibrium:** θOU,1H=$2,049.07\theta_{\text{OU,1H}} = \mathbf{\$2,049.07}θOU,1H​=$2,049.07 (bOU=−0.003356b_{\text{OU}} = -0.003356bOU​=−0.003356, t1/2=206.2 barst_{1/2} = 206.2\text{ bars}t1/2​=206.2 bars). Since Entry=$2,356.50>θOU,1H=$2,049.07\text{Entry} = \$2,356.50 > \theta_{\text{OU,1H}} = \$2,049.07Entry=$2,356.50>θOU,1H​=$2,049.07, 1H OU drift pulls **downward by `-307.43 pts`**. **PASSES 1H OU Gate.**\n\n2. **`CAND_BNB_OTE_73475` (`BNBUSD.p` `SELL_LIMIT` @ `$734.75`):**
\n- **15m OU Equilibrium:** θOU,15m=$725.95\theta_{\text{OU,15m}} = \mathbf{\$725.95}θOU,15m​=$725.95 (bOU=−0.023235b_{\text{OU}} = -0.023235bOU​=−0.023235, t1/2=29.5 barst_{1/2} = 29.5\text{ bars}t1/2​=29.5 bars). Since Entry=$734.75>θOU,15m=$725.95\text{Entry} = \$734.75 > \theta_{\text{OU,15m}} = \$725.95Entry=$734.75>θOU,15m​=$725.95, OU drift pulls **downward by `-8.80 pts` (`-119.8 bps`)** toward TP (`$705.25`). **PASSES 15m OU Gate.**\n\n3. **Active Position `#19274977` (`BTCUSD.pi` `SELL` @ `$80,245.00`, `current = $80,196.00`):**
\n- On 15m, θOU,15m=$80,405.42\theta_{\text{OU,15m}} = \$80,405.42θOU,15m​=$80,405.42 (`+160.42 pts` above `80,245.00`), whereas on 1H, θOU,1H=$78,885.89\theta_{\text{OU,1H}} = \$78,885.89θOU,1H​=$78,885.89 (`-1,359.11 pts` below `80,245.00`). This 15m vs. 1H OU divergence reinforces our tactical recommendation to **lock early break-even (`80,229.00`) and front-run the `$7.35M` L3 bid wall at `79,881.00` (`TP1 = 79,895.00`)**.\n\n\n---\n\n### 1.1.6 Drift-Adjusted Win Probability 
𝑃
win, drift_adjusted
P
win, drift_adjusted
	​

 vs. Break-Even 
𝑃
BE
P
BE
	​\n\n\nRRnet=TPdist−SpreadSLdist+Spread,PBE=11+RRnet=SLdist+SpreadTPdist+SLdist\text{RR}_{\text{net}} = \frac{\text{TP}_{\text{dist}} - \text{Spread}}{\text{SL}_{\text{dist}} + \text{Spread}}, \qquad P_{\text{BE}} = \frac{1}{1 + \text{RR}_{\text{net}}} = \frac{\text{SL}_{\text{dist}} + \text{Spread}}{\text{TP}_{\text{dist}} + \text{SL}_{\text{dist}}}RRnet​=SLdist​+SpreadTPdist​−Spread​,PBE​=1+RRnet​1​=TPdist​+SLdist​SLdist​+Spread​\n\n| Candidate / Position | SLdist\text{SL}_{\text{dist}}SLdist​ (`pts`) | TPdist\text{TP}_{\text{dist}}TPdist​ (`pts`) | Spread (`pts`) | RRgross\text{RR}_{\text{gross}}RRgross​ | RRnet\text{RR}_{\text{net}}RRnet​ | Exact PBEP_{\text{BE}}PBE​ | Empirical Pwin, LCBP_{\text{win, LCB}}Pwin, LCB​ (`live_snapshot`, `n=17`) | Margin vs. PBEP_{\text{BE}}PBE​ | Calibration Gate Status |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| **Active `#19274977` (`BTC` @ `80,245`)** | `375.00` | `860.00` | `15.00` | `2.2933` | **`2.1667`** | **`31.58%`** | `41.97%` (`11/17` wins) | `+10.39%` | **LIVE FILLED (`+$2.45` PnL)** |\n| **`CAND_ETH_OTE_235650` (`ETH` @ `2,356.50`)** | `45.00` | `90.00` | `3.20` | `2.0000` | **`1.8008`** | **`35.70%`** | `41.97%` (`uncalibrated`) | `+6.27%` | **`HOLD` (`n=17 < 100`)** |\n| **`CAND_BNB_OTE_73475` (`BNB` @ `734.75`)** | `14.00` | `29.50` | `0.60` | `2.1071` | **`1.9795`** | **`33.56%`** | `41.97%` (`uncalibrated`) | `+8.41%` | **`HOLD` (`n=17 < 100`)** |\n| **`CAND_BTC_PREFLIGHT_81300` (`BTC` @ `81,300`)** | `480.00` | `1,450.00` | `15.00` | `3.0208` | **`2.8990`** | **`25.65%`** | `41.97%` (`uncalibrated`) | `+16.32%` | **`REJECTED` (`74.66%` Margin)** |\n\n\n---\n\n## §1.2 Role B — Fill, Microstructure & Order Geometry (@[market-ingest], @[market-pattern])\n\n\n### 1.2.1 Whale Limit Wall Persistence (>= 100,000 USD & Continuous Persistence >= 180s) & Sheet 21_Tradfye_Orderflow (6,912 Rows)\n\n\nCross-referencing **Sheet `10_Whale_Orders` (`18:18:29 UTC`, `166` rows)**, **Sheet `17_Orderbook` (`18:01:50 UTC`, `5,432` rows)**, **Sheet `15_Hyperdash_Stops_Map` (`18:31:15 UTC`, `1,345` rows)**, **Sheet `18_CVD` (`18:33:26 UTC`, `1,500` rows)**, **Sheet `21_Tradfye_Orderflow` (`18:34:32 UTC`, `6,912` rows)**, and **`Data/coinglass/whale_persistence_ledger.json` (`18:32:01 UTC`, `73` active Hyperliquid whales, `12` pruned zombies)**:\n\n1. \n**Microstructural Post-Fill Forensics on Active Position `#19274977` (`BTCUSD.pi` `SELL` `0.05` lot @ `80,245.00`, filled at `18:11:19 UTC`):**\n
\n- **Why `#19274977` Was Immediately Defended After Fill:**
\n- Look at **Sheet `21_Tradfye_Orderflow` (`18:34:32 UTC`)**: on the `18:15:00 UTC` 15m candle (`Open = 80,318.20`, `High = 80,377.40`, `Low = 80,227.50`, `Close = 80,368.30`), institutional sellers executed **`$33,873,239.32` of Taker Sell Volume against `$19,782,697.99` of Taker Buy Volume (`Net Delta = -$14,090,541.33`)**, absorbing the rally right at `$80,377.40`!\n- Why did price reverse at `$80,377.40`? Look at **Sheet `10_Whale_Orders` (`18:18:29 UTC`)**: aged (`>= 180s`) institutional sell walls were resting at:
\n- **`$80,377.40` (`$2,010,000` Binance Sell Wall, persisted `3h 36m = 12,960s >= 180s`)** — *exact 15m candle high (`80,377.40`)!*\n- **`$80,384.60` (`$1,560,000` Binance Sell Wall, persisted `3h 43m = 13,380s >= 180s`)** — *exact `18:30 UTC` 15m candle high (`80,384.60`)!*\n- **`$80,400.00` (`$1,440,000` Binance Sell Wall, persisted `2h 31m = 9,060s >= 180s`)**\n- **`$80,413.10` (`$1,150,000` Binance Sell Wall, persisted `8m 38s = 518s >= 180s`)**\n- **`$80,500.00` (`$13,700,000` OKX/Binance Sell Wall persisted `3h 43m = 13,380s` + `$3,770,000` persisted `2h 43m = 9,780s` = `$17,470,000` total)**\n- **`$80,534.00` (`$7,404,073.69` Hyperliquid L3 Mega-Whale Ask Wall, `91.94 BTC`, wallet `0xf5a5...1286` in Sheet `17_Orderbook`)**\n\n\n- **Critical Hazard #1 on Active `#19274977` (`SL = 80,620.00` Sits Inside a `$25.91M` Sell-Wall / Buy-Stop Cluster):**
\n- In **Sheet `10_Whale_Orders` (`18:18:29 UTC`)**, massive aged Binance sell walls sit at **`$80,589.90–$80,590.00` (`$8,640,000` persisted `25m 40s–3h 43m`)**, **`$80,600.00–$80,605.60` (`$2,340,000` persisted `8m 38s–27m 18s`)**, **`$80,620.20` (`$8,060,000` persisted `49s`)**, **`$80,637.90` (`$10,900,000` persisted `11m 01s = 661s >= 180s`)**, and **`$80,652.60` (`$6,170,000` persisted `4m 32s = 272s >= 180s`)**.\n- Simultaneously, **Sheet `15_Hyperdash_Stops_Map` (`18:31:15 UTC`)** shows **`$3.53M` Buy Stops at `80,550.00` (`$9.10M` cumulative)** and **`$1.46M` Buy Stops at `80,650.00` (`$10.57M` cumulative)**. Thus `#19274977`'s current `SL = 80,620.00` sits **in front of** the `$10.90M` (`11m 01s`) sell wall at `80,637.90` and `$6.17M` (`4m 32s`) sell wall at `80,652.60`!\n\n- **Critical Hazard #2 on Active `#19274977` (`TP = 79,385.00` Sits Behind `$27.63M+` of Institutional Bid Walls):**
\n- In **Sheet `10_Whale_Orders` (`18:18:29 UTC`)**, aged (`>= 180s`) Binance buy walls rest at:
\n- **`$80,000.00` (`$1,460,000` persisted `28m 33s = 1,713s >= 180s`)** (down from `$40.60M` in the prior cycle as passive bids were partially pulled/filled, supplemented by `$7.04M` @ `79,984.60` [`1m 20s`] and `$8.02M` @ `79,968.60` [`49s`]),\n- **`$79,850.00` (`$4,030,000` persisted `1h 25m = 5,100s` + `$1,900,000` persisted `1h 04m = 3,840s` = `$5,930,000` aged buy wall!)**,\n- **`$79,816.30` (`$1,000,000` persisted `6m 31s = 391s`)** and **`$79,796.90` (`$1,000,000` persisted `7m 20s = 440s`)**.\n\n- In **Sheet `17_Orderbook` (`18:01:50 UTC`)**, Hyperliquid L3 Mega-Whale (`>= $5M`) buy walls rest at:
\n- **`$79,881.00` (`$7,347,297.81`, `91.98 BTC`, wallet `0xf5a5...1286`)**,\n- **`$79,529.00` (`$14,357,462.62`, `180.53 BTC`, wallet `0xf5a5...1286`)**,\n- **`$79,100.00` (`$7,034,995.80`, `88.94 BTC`, wallet `0x31de...13f2`)**.\n\n- Therefore, leaving `#19274977`'s `TP` solely at `79,385.00` requires price to smash through **`$7.35M` at `79,881.00`, `$5.93M` (`1h 25m`) at `79,850.00`, AND `$14.36M` at `79,529.00`**! Modifying `TP1` to **`79,895.00`** (`+14.00 pts = +1.75 bps` in front of `79,881.00` and `+45.00 pts = +5.64 bps` in front of `79,850.00`) or **`79,545.00`** (`+16.00 pts = +2.01 bps` in front of `79,529.00`) directly resolves this microstructure obstruction.\n\n\n2. \n**Microstructure & Orderflow Audit of `CAND_ETH_OTE_235650` (`ETHUSD.pi` `SELL_LIMIT` `0.36` lot @ `2,356.50`, `SL = 2,401.50`, `TP = 2,266.50`):**\n
\n- **Sheet `17_Orderbook` (`18:01:50 UTC`):** `ETH` has **37 Whale/Mega-Whale L3 walls `>= $1,000,000`**, led on the ask side by:
\n- **`$4,005,214.62` (`1,716.32 ETH`) at `$2,333.60`** (`wallet 0xb8eb...1dd5`),\n- **`$4,667,723.44` (`1,994.50 ETH`) at `$2,340.30`** (`wallet 0xab5e...bec3`),\n- **`$9,105,206.29` (`3,874.39 ETH` MEGA WHALE) at `$2,350.10`** (`wallet 0xab5e...bec3`),\n- **`$3,333,105.63` (`1,417.38 ETH`) at `$2,351.60`** (`wallet 0x31de...13f2`),\n- **`$4,698,410.56` (`1,988.07 ETH`) at `$2,363.30`** (`wallet 0x31de...13f2`, right at `0.702 OTE = $2,363.12`!).\n\n- Staging `Entry = $2,356.50` sits right at the **`0.650` Golden Pocket (`$2,356.62`) + `EMA_89` (`$2,356.25`)**, protected by **`$12.44M` of L3 ask walls at `$2,350.10–$2,351.60` below and `$4.70M` L3 ask wall at `$2,363.30` above**!\n- **Sheet `21_Tradfye_Orderflow` (`18:34:32 UTC`):** On `ETHUSDT`, cumulative 15m `CVD = -$453,097,234.09` (`1h CVD = -$467,262,442.75`), while short-term `15m Net Delta = +$19,980,622.08` (`+32.86%`) is generating the exact corrective counter-trend bounce toward the `$2,352.61–$2,363.12` Golden Zone required to fill a passive `SELL_LIMIT`, with **Deribit Options Max Pain & Put Wall anchored at `$2,300.00`**!\n\n3. \n**Microstructure & Orderflow Audit of `CAND_BNB_OTE_73475` (`BNBUSD.p` `SELL_LIMIT` `1.15` lot @ `734.75`, `SL = 748.75`, `TP = 705.25`):**\n
\n- **Sheet `21_Tradfye_Orderflow` (`18:34:32 UTC`) & Sheet `18_CVD` (`18:33:26 UTC`):** `BNBUSDT` is in **`AGGRESSIVE_SELLER_DOMINATION` / `BEARISH_EXPANSION`** (`15m Taker Buy = $279,720.29` vs. `Taker Sell = $495,305.80`, `Net Delta = -$215,585.51 [-27.82%]`, `15m CVD = -$15,193,278.68`).\n- **Sheet `17_Orderbook` (`18:01:50 UTC`):** `BNB` has a **`$1,306,994.23` (`1,793.23 BNB`) L3 Whale Ask Wall at `$728.85`** and a **`$1,294,172.65` (`1,793.23 BNB`) L3 Whale Bid Wall at `$721.70`** (`wallet 0x02fb...cda9`).\n\n\n---\n\n### 1.2.2 Structural Invalidation Shelf (0.786 Fib Retracement + 0.40 ATR + Half-Spread)\n\n\nPer §1.2.2:\n
SLshort, min=Price0.786+0.40×ATR14+0.5×Spread\text{SL}_{\text{short, min}} = \text{Price}_{0.786} + 0.40 \times \text{ATR}_{14} + 0.5 \times \text{Spread}SLshort, min​=Price0.786​+0.40×ATR14​+0.5×Spread\n\n| Candidate / Position | Impulse Leg `[Low, High]` (`20_AMS`) | Price0.786\text{Price}_{0.786}Price0.786​ | ATR14\text{ATR}_{14}ATR14​ (`11_Tech`) | 0.5×Spread0.5 \times \text{Spread}0.5×Spread | Minimum SLshort, min\text{SL}_{\text{short, min}}SLshort, min​ | Candidate SL\text{SL}SL | Clearance vs. SLshort, min\text{SL}_{\text{short, min}}SLshort, min​ | Verdict |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| **`CAND_ETH_OTE_235650`** | `[2,275.30, 2,400.40]` | `2,373.63` | `11.1119` | `1.60` | **`2,379.67`** | **`2,401.50`** | **`+21.83 pts` above shelf (also behind `Swing High = 2,400.40` & `24H Short Max Pain = 2,399.79`)** | **PASS** |\n| **`CAND_BNB_OTE_73475`** | `[716.50, 744.60]` | `738.59` | `2.1064` | `0.30` | **`739.73`** | **`748.75`** | **`+9.02 pts` above shelf (also behind `d_VAH = 740.15`, `Swing High = 744.60` & `pd_POC = 746.37`)** | **PASS** |\n| **`CAND_BTC_PREFLIGHT_81300`** | `[79,071.00, 81,445.50]` | `80,937.36` | `278.9381` | `7.50` | **`81,056.44`** | `81,780.00` | `+723.56 pts` above shelf, **but `Entry = 81,300` is `+362.64 pts` ABOVE `0.786` invalidation (`80,937.36`)!** | **FAIL (`Entry > 0.786`)** |\n| **Active `#19274977` (`BTC`)** | `[79,071.00, 81,445.50]` | `80,937.36` | `278.9381` | `7.50` | `81,056.44` | `80,620.00` | Placed on narrower local leg `[79,071, 80,815]` (`0.786 = 80,441.78`, `min SL = 80,560.86`); **PASS local shelf** | **LIVE ACTIVE** |\n\n\n---\n\n### 1.2.3 Multi-Timeframe Auction Extremes (20_Auction_Market_Structure at 18:34:02 UTC)\n\n\n| Symbol | Price | `d_POC` / `d_VAH` / `d_VAL` | `pd_POC` / `pd_VAH` / `pd_VAL` | `Mon_H` / `Mon_L` / `Mon_Mid` | `Asian_H` / `Asian_L` | `London_H` / `London_L` | `NY_H` / `NY_L` | `Fib 0.618 / 0.650 / 0.702 / 0.786` | Auction Regime |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| **`BTCUSD.pi`** | `80,239.50` | `80,665.90` / `81,008.22` / `80,121.30` | `81,591.05` / `81,777.71` / `81,335.26` | `83,087.50` / `80,743.00` / `81,915.25` | `81,405.00` / `80,358.00` | `80,815.00` / `80,280.91` | `80,785.00` / `79,071.00` | `80,538.44` / `80,614.43` / `80,737.90` / `80,937.36` | `ROTATIONAL_BALANCE` |\n| **`ETHUSD.pi`** | `2,331.90` | `2,375.72` / `2,384.05` / `2,335.72` | `2,399.97` / `2,406.73` / `2,390.41` | `2,442.00` / `2,347.30` / `2,394.65` | `2,400.30` / `2,346.40` | `2,379.40` / `2,350.60` | `2,368.30` / `2,275.30` | `2,352.61` / `2,356.62` / `2,363.12` / `2,373.63` | **`TREND_DOWN_ACCEPTANCE`** |\n| **`BNBUSD.p`** | `726.40` | `736.34` / `740.15` / `725.88` | `746.37` / `749.26` / `738.53` | `729.50` / `707.00` / `718.25` | `741.40` / `732.10` | `739.00` / `729.40` | `732.30` / `716.50` | `733.87` / `734.76` / `736.23` / `738.59` | `ROTATIONAL_BALANCE` |\n| **`SOLUSD.p`** | `100.94` | `102.23` / `102.93` / `100.43` | `104.16` / `104.51` / `103.69` | `105.99` / `100.78` / `103.38` | `103.62` / `101.41` | `102.47` / `100.81` | `101.65` / `98.34` | `102.07` / `102.26` / `102.57` / `103.08` | `ROTATIONAL_BALANCE` |\n| **`BCHUSD.p`** | `273.60` | `275.91` / `279.57` / `274.84` | `284.86` / `287.10` / `282.11` | `280.06` / `264.76` / `272.41` | `283.50` / `273.29` | `279.06` / `273.36` | `279.06` / `267.36` | `278.85` / `279.45` / `280.42` / `281.98` | `RANGE_EXPANSION` |\n\n\n---\n\n### 1.2.4 Adverse Selection Markouts 
𝐴
𝑆
(
𝑡
+
5
m
)
AS(t+5m) & TP Front-Running (5–10 bps)\n\n\n1. **5-Minute Post-Fill Adverse Selection Markout AS(t+5m)AS(t+5\text{m})AS(t+5m):**
\n- **Realized Markout on Active Position `#19274977` (`SELL 0.05` @ `80,245.00`, filled `18:11:19 UTC`):** At `18:15 UTC` (`+3m 41s` after fill), `BTC` briefly wicked to `80,377.40` (`-132.40 pts = -$6.62` excursion) before institutional sellers (`-$14.09M` Net Delta in Sheet `21_Tradfye_Orderflow`) drove price back down to `80,174.00–80,196.00` (`+$3.55 / +$2.45 USD` positive markout)!\n- **Modeled AS(t+5m)AS(t+5\text{m})AS(t+5m) for Staged Candidates:**
\n- `CAND_ETH_OTE_235650` (`0.36` lot @ `2,356.50`): protected by `$9.11M` (`2,350.10`), `$3.33M` (`2,351.60`), and `$4.70M` (`2,363.30`) L3 ask walls; modeled AS(t+5m)=$0.95 USDAS(t+5\text{m}) = \mathbf{\$0.95\text{ USD}}AS(t+5m)=$0.95 USD (`2.64 pts`).\n- `CAND_BNB_OTE_73475` (`1.15` lot @ `734.75`): modeled AS(t+5m)=$0.85 USDAS(t+5\text{m}) = \mathbf{\$0.85\text{ USD}}AS(t+5m)=$0.85 USD (`0.74 pts`).\n\n\n2. **TP Front-Running of Opposing Whale Clusters (`5–10 bps`):**
\n- **Active `#19274977` (`BTCUSD.pi`):** Current `TP = 79,385.00` sits behind `$7.35M` L3 bid wall (`79,881.00`), `$5.93M` aged (`1h 25m`) Binance bid wall (`79,850.00`), and `$14.36M` L3 bid wall (`79,529.00`). We recommend staging `TP1 = 79,895.00` (`+5.64 bps` in front of `79,850.00` and `+1.75 bps` in front of `79,881.00`) and `TP2 = 79,545.00` (`+2.01 bps` in front of `79,529.00`).\n- **`CAND_ETH_OTE_235650` (`ETHUSD.pi`):** `TP1 = 2,295.50` front-runs the **`$8,855,076.57` Hyperliquid L3 Mega-Whale Bid Wall at `$2,293.70`** by **`+1.80 pts = +7.85 bps`**, while full `TP = 2,266.50` (`2.00R` gross) clears `24H Long Liq Max Pain = $2,270.96` (`$14.77M` in `9_Liquidation_Max_Pain_24H`).\n- **`CAND_BNB_OTE_73475` (`BNBUSD.p`):** `TP1 = 722.25` front-runs the **`$1,294,172.65` Hyperliquid L3 Whale Bid Wall at `$721.70`** by **`+0.55 pts = +7.62 bps`**, while full `TP = 705.25` targets `Mon_L = 707.00`.\n\n\n---\n\n## §1.3 Role C — Solvency, Portfolio & Broker Math (@[trader-risk])\n\n\n### 1.3.1 Triple Solvency Floor & Zero Floating Profit Credit (§1.3.5)\n\n\nFrom `cycle_envelope.json` (`18:37:26 UTC`), `execution_preflight_receipt.json` (`18:37:46 UTC`), `live_snapshot_latest.json` (`18:36:26 UTC`), and Sheet `00_MT5_Account_Telemetry` (`18:25:03 UTC`):\n\n- **Realized Closed Balance:** Balance=$4,865.07 USD\text{Balance} = \mathbf{\$4,865.07\text{ USD}}Balance=$4,865.07 USD\n- **Floating Equity:** Equity=$4,867.52 USD\text{Equity} = \mathbf{\$4,867.52\text{ USD}}Equity=$4,867.52 USD (`cycle_envelope.json` with `+$2.45` floating PnL on `#19274977`) / $4,867.42 USD\mathbf{\$4,867.42\text{ USD}}$4,867.42 USD (`preflight` with `+$2.35` floating PnL) / $4,868.62 USD\mathbf{\$4,868.62\text{ USD}}$4,868.62 USD (`00_MT5` with `+$3.55` floating PnL) / $4,865.27 USD\mathbf{\$4,865.27\text{ USD}}$4,865.27 USD (`live_snapshot` with `+$0.20` floating PnL).\n- **Zero Floating Profit Credit Invariant (§1.3.5):**\n
Solvency_Base=min⁡(Balance,Equity)=min⁡($4,865.07,$4,867.52)=$4,865.07 USD(Floating PnL Credit=$0.00 USD)\text{Solvency\_Base} = \min(\text{Balance}, \text{Equity}) = \min(\$4,865.07, \$4,867.52) = \mathbf{\$4,865.07\text{ USD}} \quad (\text{Floating PnL Credit} = \mathbf{\$0.00\text{ USD}})Solvency_Base=min(Balance,Equity)=min($4,865.07,$4,867.52)=$4,865.07 USD(Floating PnL Credit=$0.00 USD)\n\text{Inviolate Hard Floor Cushion} &= \$4,865.07 - \$4,600.00 = \mathbf{+\$265.07\text{ USD}} \\
\text{Operating Defense Buffer Cushion} &= \$4,865.07 - \$4,650.00 = \mathbf{+\$215.07\text{ USD}} \\
\text{Solvency Kernel Cushion} &= \$4,865.07 - \$4,795.00 = \mathbf{+\$70.07\text{ USD}} \\
\text{Base Net Solvency Headroom } (H_{\text{base}}) &= \$4,865.07 - \$4,795.00 - \$2.00\text{ (Global Contingency)} = \mathbf{+\$68.07\text{ USD}}
\end{aligned}$$\n- **Realized Solvency Headroom After Active Open Position `#19274977`:**
\n- In `cycle_envelope.json`, `existing_ticket_stress_usd = $28.50 USD` (in `live_snapshot_latest.json`, `stressed_stop_loss_usd = $25.4375 USD`; at `15.0 pt` live spread, 1.25×18.75+0.75+2.00=$26.18751.25 \times 18.75 + 0.75 + 2.00 = \$26.18751.25×18.75+0.75+2.00=$26.1875 or 1.25×(18.75+0.75)+2.00=$26.3751.25 \times (18.75 + 0.75) + 2.00 = \$26.3751.25×(18.75+0.75)+2.00=$26.375):\n
H_{\text{realized, envelope}} = \$68.07 - \$28.50 = \mathbf{+\$39.57\text{ USD}}, \qquad E_{\text{post-stress, #19274977}} = \$4,865.07 - \$28.50 - \$2.00 = \mathbf{\$4,834.57\text{ USD}} \ge \$4,795.00\text{ USD}\n\n\n---\n\n### 1.3.2 Capital Mode (TIER_2_HOUSE_MONEY) & Concurrent Slot Capacity\n\n\n- **Capital Mode:** `TIER_2_HOUSE_MONEY` (`Nominal Risk Band = [$15.00, $25.00] USD` per ticket; max `2` concurrent positions).\n- **Slot Utilization:** Slot `1/2` is occupied by **active filled position `#19274977` (`BTCUSD.pi` `SELL` `0.05` lot @ `80,245.00`)**. Exactly **`1` remaining slot** (`Slot 2/2`) is available for a non-correlated second ticket (`ETHUSD.pi` or `BNBUSD.p`).\n\n---\n\n### 1.3.3 Finding D3 — 50% Crypto Margin Collateralization Gate & Discovery of the Preflight margin_level_post_order Denominator Omission Bug\n\n\nUnder `BlueberryMarketsSVG-Live` 50% (`2:1`) crypto perpetual margin rules:\n
Margintotal=Marginused, active+Marginreq, new≤0.50×min⁡(Balance,Equity)=0.50×$4,865.07=$2,432.535 USD(Margin Level≥200.0%)\text{Margin}_{\text{total}} = \text{Margin}_{\text{used, active}} + \text{Margin}_{\text{req, new}} \le 0.50 \times \min(\text{Balance}, \text{Equity}) = 0.50 \times \$4,865.07 = \mathbf{\$2,432.535\text{ USD}} \quad (\text{Margin Level} \ge 200.0\%)Margintotal​=Marginused, active​+Marginreq, new​≤0.50×min(Balance,Equity)=0.50×$4,865.07=$2,432.535 USD(Margin Level≥200.0%)\n\n1. **Active Position `#19274977` (`BTCUSD.pi` `SELL` `0.05` lot @ `80,245.00`):**\n
\text{Margin}_{\text{used, #19274977}} = 0.05 \times 80,245.00 \times 0.50 = \$2,006.125 \approx \mathbf{\$2,006.13\text{ USD}} \quad (\mathbf{41.24\%}\text{ of Balance}, \text{Margin Level} = \mathbf{242.63\%} \ge 200.0\%)
\n- **Maximum Remaining 50% Margin Capacity for Any Second Ticket (Mrem, 50%M_{\text{rem, 50\%}}Mrem, 50%​):**\n
Mrem, 50%=$2,432.535−$2,006.13=$426.405≈$426.41 USDM_{\text{rem, 50\%}} = \$2,432.535 - \$2,006.13 = \mathbf{\$426.405 \approx \$426.41\text{ USD}}Mrem, 50%​=$2,432.535−$2,006.13=$426.405≈$426.41 USD\n\n2. **Why Preflight Candidate `CAND_BTC_PREFLIGHT_81300` (`0.04` lot `BTCUSD.pi` @ `81,300.00`) HARD-FAILS the 50% Margin Gate (and How `execution_preflight.py` Miscalculated `margin_level_post_order = 299.35%`):**
\n- New margin required for `0.04` lot @ `81,300.00`:\n
Marginreq=0.04×81,300.00×0.50=$1,626.00 USD>Mrem, 50%($426.41)!\text{Margin}_{\text{req}} = 0.04 \times 81,300.00 \times 0.50 = \mathbf{\$1,626.00\text{ USD}} > M_{\text{rem, 50\%}}(\$426.41)!Marginreq​=0.04×81,300.00×0.50=$1,626.00 USD>Mrem, 50%​($426.41)!\n- Look at `execution_preflight_receipt.json` under `order_check`:
\n- `"margin_free": 2861.29` (`$4,867.42 - $2,006.13`)\n- `"margin_required_usd": 1626.0`\n- `"margin_free_post_order": 1235.29` (`$2,861.29 - $1,626.00 = $1,235.29`!)\n- `"margin_level_post_order": 299.35` (`$4,867.42 / $1,626.00 = 299.349%`!)\n\n- **Mathematical Proof of the Denominator Omission Bug:** Because `margin_free_post_order = $1,235.29`, total margin locked upon fill of `CAND_BTC_PREFLIGHT_81300` alongside `#19274977` is:\n
Margintotal=$2,006.13+$1,626.00=$3,632.13 USD=74.66% of Balance ($4,865.07)>50.0% Cap!\text{Margin}_{\text{total}} = \$2,006.13 + \$1,626.00 = \mathbf{\$3,632.13\text{ USD}} = \mathbf{74.66\%\text{ of Balance } (\$4,865.07)} > 50.0\%\text{ Cap!}Margintotal​=$2,006.13+$1,626.00=$3,632.13 USD=74.66% of Balance ($4,865.07)>50.0% Cap!\n
Margin Leveltrue, post-order=$4,867.42$3,632.13×100%=134.01%<200.0% Floor!(and $4,865.07$3,632.13=133.95%)\text{Margin Level}_{\text{true, post-order}} = \frac{\$4,867.42}{\$3,632.13} \times 100\% = \mathbf{134.01\%} < 200.0\%\text{ Floor!} \quad \left(\text{and } \frac{\$4,865.07}{\$3,632.13} = \mathbf{133.95\%}\right)Margin Leveltrue, post-order​=$3,632.13$4,867.42​×100%=134.01%<200.0% Floor!(and $3,632.13$4,865.07​=133.95%)\n- `execution_preflight.py` computed `4867.42 / 1626.00 = 299.35%` by dividing equity only by the new order's margin (`$1,626.00`), omitting the active position's `$2,006.13` `margin_used` in the denominator!\n\n3. **Exact Margin-Compliant Sizing of Second Tickets (`CAND_ETH_OTE_235650` & `CAND_BNB_OTE_73475`):**
\n- **`CAND_ETH_OTE_235650` (`0.36` lot `ETHUSD.pi` `SELL_LIMIT` @ `2,356.50`, `contract_size = 1.0`):**\n
Marginreq=0.36×2,356.50×0.50=$424.17 USD≤$426.41 USD\text{Margin}_{\text{req}} = 0.36 \times 2,356.50 \times 0.50 = \mathbf{\$424.17\text{ USD}} \le \$426.41\text{ USD}Marginreq​=0.36×2,356.50×0.50=$424.17 USD≤$426.41 USD\n
Margintotal=$2,006.13+$424.17=$2,430.30 USD=49.95%≤50.0%,Margin Levelpost-order=$4,865.07$2,430.30=200.18%≥200.0%!\text{Margin}_{\text{total}} = \$2,006.13 + \$424.17 = \mathbf{\$2,430.30\text{ USD}} = \mathbf{49.95\%} \le 50.0\%, \qquad \text{Margin Level}_{\text{post-order}} = \frac{\$4,865.07}{\$2,430.30} = \mathbf{200.18\%} \ge 200.0\%!Margintotal​=$2,006.13+$424.17=$2,430.30 USD=49.95%≤50.0%,Margin Levelpost-order​=$2,430.30$4,865.07​=200.18%≥200.0%!\n- **`CAND_BNB_OTE_73475` (`1.15` lot `BNBUSD.p` `SELL_LIMIT` @ `734.75`, `contract_size = 1.0`):**\n
Marginreq=1.15×734.75×0.50=$422.48 USD≤$426.41 USD\text{Margin}_{\text{req}} = 1.15 \times 734.75 \times 0.50 = \mathbf{\$422.48\text{ USD}} \le \$426.41\text{ USD}Marginreq​=1.15×734.75×0.50=$422.48 USD≤$426.41 USD\n
Margintotal=$2,006.13+$422.48=$2,428.61 USD=49.92%≤50.0%,Margin Levelpost-order=$4,865.07$2,428.61=200.32%≥200.0%!\text{Margin}_{\text{total}} = \$2,006.13 + \$422.48 = \mathbf{\$2,428.61\text{ USD}} = \mathbf{49.92\%} \le 50.0\%, \qquad \text{Margin Level}_{\text{post-order}} = \frac{\$4,865.07}{\$2,428.61} = \mathbf{200.32\%} \ge 200.0\%!Margintotal​=$2,006.13+$422.48=$2,428.61 USD=49.92%≤50.0%,Margin Levelpost-order​=$2,428.61$4,865.07​=200.32%≥200.0%!\n\n\n---\n\n### 1.3.4 Complete Broker Math & Stressed Solvency Verification Table (0.01 USD Precision)\n\n\nUsing both the §1.3.4 specification formula (Stressed_Loss§1.3.4=1.25×SL_Lossbase+Exit_Spread_Cost+$2.00\text{Stressed\_Loss}_{\text{§1.3.4}} = 1.25 \times \text{SL\_Loss}_{\text{base}} + \text{Exit\_Spread\_Cost} + \$2.00Stressed_Loss§1.3.4​=1.25×SL_Lossbase​+Exit_Spread_Cost+$2.00) and the conservative preflight receipt formula (Stressed_Lossreceipt=1.25×(SL_Lossbase+Exit_Spread_Cost)+$2.00\text{Stressed\_Loss}_{\text{receipt}} = 1.25 \times (\text{SL\_Loss}_{\text{base}} + \text{Exit\_Spread\_Cost}) + \$2.00Stressed_Lossreceipt​=1.25×(SL_Lossbase​+Exit_Spread_Cost)+$2.00):\n\n| Ticket / Candidate | Lots (VVV) | Entry / SL / TP | SLdist\text{SL}_{\text{dist}}SLdist​ / TPdist\text{TP}_{\text{dist}}TPdist​ (`pts`) | SL_Lossbase\text{SL\_Loss}_{\text{base}}SL_Lossbase​ (`$`) | Spread Cost (`$`) | Total Nominal Risk (`$`) | Stressed_Loss\text{Stressed\_Loss}Stressed_Loss (§1.3.4 / Receipt) (`$`) | Margin Req (`50%`) (`$`) | Combined Margin w/ `#19274977` (`% Bal`) | Post-Stop Balance (`$`) | Solvency & Margin Verdict |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| **Active `#19274977` (`BTCUSD.pi`)** | `0.05` | `80,245` / `80,620` / `79,385` | `375.0` / `860.0` | `$18.75` | `$0.75` (`15pt`) | **`$19.50`** | `$26.19` / **`$28.50`** (`env`) | **`$2,006.13`** | **`41.24%`** (`242.63%` ML) | **`$4,834.57`** | **PASS (`LIVE OPEN`, `+$2.45` PnL)** |\n| **`CAND_ETH_OTE_235650` (`ETHUSD.pi`)** | `0.36` | `2,356.50` / `2,401.50` / `2,266.50` | `45.0` / `90.0` | `$16.20` | `$1.15` (`3.2pt`) | **`$17.35`** | `$23.40` / **`$23.69`** | **`$424.17`** | **`49.95%`** (`200.18%` ML) | **`$4,810.88`** (`joint`) | **PASS (`100% Solvency & 50% Margin Compliant`)** |\n| **`CAND_BNB_OTE_73475` (`BNBUSD.p`)** | `1.15` | `734.75` / `748.75` / `705.25` | `14.0` / `29.5` | `$16.10` | `$0.69` (`0.6pt`) | **`$16.79`** | `$22.82` / **`$22.99`** | **`$422.48`** | **`49.92%`** (`200.32%` ML) | **`$4,811.58`** (`joint`) | **PASS (`100% Solvency & 50% Margin Compliant`)** |\n| **`CAND_BTC_PREFLIGHT_81300` (`BTCUSD.pi`)** | `0.04` | `81,300` / `81,780` / `79,850` | `480.0` / `1,450.0` | `$19.20` | `$0.60` (`15pt`) | **`$19.80`** | `$26.60` / **`$26.75`** | **`$1,626.00`** | **`74.66%`** (`134.01%` ML!) | `$4,807.82` (`joint`) | **FAIL_CLOSED (`Margin 74.66% > 50%`)** |\n\n\n---\n\n## §1.4 Role D — Market Clock, Auction & Provenance (@[market-ingest], @[systematic-debugging])\n\n\n### 1.4.1 Strict Physical Cutoff Causality (tick_time < observed_at < cutoff_utc)\n\n\n- **`cutoff_utc`:** `2026-10-24 18:37:26 UTC` (Prompt Reference Clock: `2026-10-24 18:37:39 UTC`).\n- **Causality Audit of `Data/execution_preflight_receipt.json`:**
\n- `tick_time_utc = "2026-10-24 18:37:45 UTC"`   ⟹  +19.0 seconds AFTER cutoff_utc\implies \mathbf{+19.0\text{ seconds AFTER } \texttt{cutoff\_utc}}⟹+19.0 seconds AFTER cutoff_utc (`18:37:26 UTC`) and +6.0s+6.0\text{s}+6.0s after the prompt reference clock (`18:37:39 UTC`)!\n- `observed_at_utc = "2026-10-24 18:37:46 UTC"`   ⟹  +20.0 seconds AFTER cutoff_utc\implies \mathbf{+20.0\text{ seconds AFTER } \texttt{cutoff\_utc}}⟹+20.0 seconds AFTER cutoff_utc (`18:37:26 UTC`)!\n- **Verdict:** **HARD FAIL-CLOSED (`VIOLATION_POST_CUTOFF_PREFLIGHT_PLUS_20S`)**. Under §1.4.1, any receipt with `tick_time_utc >= cutoff_utc` or `observed_at_utc >= cutoff_utc` violates strict temporal causality and cannot authorize live order placement.\n\n- **Causality Audit of `Data/DataBase_Trading.xlsx` (`18:35:26 UTC` max sheet timestamp) & `docs/telemetry/live_snapshot_latest.json` (`18:36:26 UTC`):**
\n- Both the workbook (`<= 18:35:26 UTC`, `-120.0s` before `cutoff_utc`) and `live_snapshot_latest.json` (`18:36:26 UTC`, `-60.0s` before `cutoff_utc`) are **100% strictly pre-cutoff causal**.\n\n\n---\n\n### 1.4.2 156-Symbol Broker Universe & Weekend Market-Clock Census\n\n\nCross-referencing Sheet `00_MT5_Account_Telemetry` (`18:25:03 UTC`, `156` broker symbols) and Sheet `20_Auction_Market_Structure` (`18:34:02 UTC`, `171` assets):\n\n- **Total Broker Symbols Audited:** **`156` symbols**.\n- **TradFi Symbols (`FOREX`, `INDICES`, `COMMODITIES`, `EQUITIES`):** **`98` symbols** (`WEEKEND_HALTED` on Saturday `2026-10-24 18:37:26 UTC`). Zero TradFi orders permitted.\n- **Crypto Perpetuals (`OPEN_24_7`):** **`58` symbols** (`31` primary USD perpetuals in `00_MT5_Account_Telemetry` + `27` cross/alt pairs):
\n- **Passing `<= 25.0 bps` Universal Crypto Spread Gate (`12` symbols):**
\n1. `BTCUSD.pi`: **`2.00 bps`** (`00_MT5`) / **`1.87 bps`** (`20_AMS` & `preflight`) / **`1.99 bps`** (`live_snapshot`) — **PASS**\n2. `XMRUSD.p`: **`3.49 bps`** (`00_MT5`) / **`6.44 bps`** (`20_AMS`) — **PASS**\n3. `ZECUSD.p`: **`6.71 bps`** (`00_MT5`) / **`7.59 bps`** (`20_AMS`) — **PASS**\n4. `BNBUSD.p`: **`6.90 bps`** (`00_MT5`) / **`8.26 bps`** (`20_AMS` & `live_snapshot`) — **PASS**\n5. `DSHUSD.p`: **`9.42 bps`** (`00_MT5`) / **`10.56 bps`** (`20_AMS`) — **PASS**\n6. `ETHUSD.pi`: **`13.79 bps`** (`00_MT5`) / **`13.73 bps`** (`20_AMS`) / **`13.74 bps`** (`live_snapshot`) — **PASS**\n7. `YFIUSD.p`: **`14.98 bps`** (`00_MT5`) / **`19.62 bps`** (`20_AMS`) — **PASS**\n8. `BCHUSD.p`: **`17.61 bps`** (`00_MT5`) / **`24.88 bps`** (`20_AMS`) / **`17.56 bps`** (`live_snapshot`) — **PASS**\n9. `XLMUSD.p`: **`17.68 bps`** (`00_MT5`) / **`18.84 bps`** (`20_AMS`) — **PASS**\n10. `AVEUSD.p`: **`19.85 bps`** (`00_MT5`) / **`20.54 bps`** (`20_AMS`) — **PASS**\n11. `XRPUSD.pi`: **`23.46 bps`** (`00_MT5`) / **`23.42 bps`** (`20_AMS`) (`31.18 bps` in `live_snapshot`) — **BORDERLINE PASS IN WORKBOOK**\n12. `SOLUSD.p`: **`23.86 bps`** (`00_MT5`) / **`23.79 bps`** (`live_snapshot`) (`28.77 bps` in `20_AMS`) — **BORDERLINE PASS IN `00_MT5` & `live_snapshot`**\n\n- **Disqualified by Spread Gate (`> 25.0 bps`):** **`46` crypto symbols** (including `BARUSD.p` [`29.96 bps`], `TRXUSD.p` [`30.38 bps`], `AVXUSD.p` [`33.92 bps`], `UNIUSD.p` [`34.42 bps`], `LTCUSD.pi` [`53.42 bps`], `NEAR` [`65.00 bps`], `LINK` [`77.56 bps`], `ADA` [`102.16 bps`], `DOT` [`201.63 bps`], `DOGE` [`273.62 bps`]).\n\n\n---\n\n### 1.4.3 Comprehensive Provenance, SHA-256 Digest & 34-Sheet Timestamp Audit (Commit 54d93c2a87ef92e0d6eed2369e6ed1b60e3925f9)\n\n\n| Artifact / Master Workbook Sheet | Size / Rows | SHA-256 Digest / Sheet Update Timestamp (`UTC`) | Age vs. `18:37:39 UTC` | Provenance / Freshness Status |\n| --- | --- | --- | --- | --- |\n| `Data/DataBase_Trading.xlsx` (`34` sheets) | `5,180,986` B | `133e868a5ee684e151189e5acb49fbef45ec34055f5ffd879cfab031da14175e` | `133s` (`18:35:26Z`) | **SHA-256 100% MATCH** (`excel_freshness_verified = false` due to 5 sheets >60m) |\n| `Data/history/master_manifest.json` | `344,231` B | `179677229c0595ae2cb18e408ab4c96e24dee8b44dec3d4209521e9a59b8566d` | `73s` (`18:36:26Z`) | **SHA-256 100% MATCH** |\n| `Data/cycle_envelope.json` (`commit 54d93c2a`) | `3,056` B | `5e8ad915e34a9f343d921cfc36214457122ac7d0803b93def50c7ddc22be115d` | `13s` (`18:37:26Z`) | Verified (`active_positions_count = 1`, `pending_orders_count = 0`) |\n| `Data/execution_preflight_receipt.json` (embedded) | `1,684` B | Claimed: `d0ee05e4...` (`nonce=""`) / Actual: `3d9432a3...` (`indent=2`) | **`-7.0s` (`18:37:46Z`)** | **FAIL-CLOSED (`+20.0s` post-cutoff & nonce hash mismatch)** |\n| `docs/telemetry/live_snapshot_latest.json` | `4,638,185` B | `e91f05c10553952c3a42ec74a089c365c519f9a7cddb12b98c709c00c5b2f58d` | `73s` (`18:36:26Z`) | **FRESH (`73s`) — All 14 crypto series repaired** (`DENIED_UNVERIFIED_ORDERFLOW`) |\n| `Data/coinglass/whale_persistence_ledger.json` | `3,094,775` B | `556c16eaf17d74a23d5e33c480f3821106bb9067817c8730e81d40f4d264b063` | `338s` (`18:32:01Z`) | **FRESH (`5m 38s`)** (`73` tracked Hyperliquid whales, `12` pruned zombies) |\n| `Data/telemetry/auction_market_structure.json` | `153,778` B | `a97d2037c6db56d2cf562b45084cbcc7a4372e6afa8ce034a5ed25b8232dd6e9` | `217s` (`18:34:02Z`) | **FRESH (`3m 37s`)** |\n| `Data/excel_all_sheets_checklist.json` | `16,271` B | `7975060ec8cf3013f152d6b3f7cf01aa6f3f8fdf850ac1cfff2986a0500d05b1` | `1,075s` (`18:19:44Z`) | **FAIL-CLOSED (`all_passed = false`: `26/31` passed, `5` failed)** |\n| `Data/macro_calendar.json` | `8,344` B | `eb601d061bb5b774cb8422d163ac347607f4861eea6ec7156b0eb6057f12149b` | `2,490.3s` (`17:56:08Z`) | **STALE (`> 900s` limit)** |\n| `Data/forex_factory_live.json` | `10,502` B | `5790fd29ba7a1396bd3f8f7025905604637f24dd1e940fd8267121c2a79276b8` | `2,379.0s` (`17:58:00Z`) | **STALE (`39m 39s`)** |\n| **Fresh Workbook Sheets (`24` sheets `<= 30m` old)** | `38`–`6,914`r | `1_Crypto_ETF_Flows` (`18:35:26Z`), `21_Tradfye_Orderflow` (`18:34:32Z`, `6,914`r), `20_Auction_Market_Structure` (`18:34:02Z`, `173`r), `18_CVD` (`18:33:26Z`, `1,502`r), `16_Hyperdash_telegram_Intel` (`18:32:06Z`), `15_Hyperdash_Stops_Map` (`18:31:15Z`), `14_Hyperdash_Liq_Map` (`18:30:40Z`), `13_Hyperliquid` (`18:29:57Z`), `12_Hyperdash` (`18:29:10Z`), `11_Technical` (`18:28:14Z`), `5_OI` (`18:27:03Z`), `4_Hyperliquid_Analysis` (`18:25:41Z`), `00_MT5_Account_Telemetry` (`18:25:03Z`), `19_Calendar` (`18:19:34Z`), `19_News` (`18:19:01Z`), `10_Whale_Orders` (`18:18:29Z`), `9_Liq_Max_Pain_48H` (`18:17:31Z`), `9_Liq_Max_Pain_24H` (`18:16:53Z`), `8_Exch_Liq_7D` (`18:16:11Z`), `8_Exch_Liq_1D` (`18:14:56Z`), `7_Liq_Heapmap` (`18:13:17Z`), `3_LS_Ratio_4H/1H/15M` (`18:12:28Z`/`18:11:05Z`/`18:09:25Z`) | `133s`–`1,694s` | **FRESH (`2m 13s` to `28m 14s` old)** |\n| **Aged / Stale Workbook Sheets (`7` sheets `30m–84m`)** | `202`–`5,434`r | `2_Spot_Netflow_S` (`18:07:31Z`), `17_Orderbook` (`18:01:50Z`), `6_Funding_Fee_Settlement` (`17:29:26Z`), `5_Funding_Rate` (`17:28:25Z`), `9_Liquidation_Max_Pain_7D` (`17:17:05Z`), `9_Liquidation_Max_Pain_3D` (`17:16:34Z`), `7_Live_Liq` (`17:13:26Z`) | `1,808s`–`5,053s` | **STALE (`30m 08s` to `84m 13s` old)** |\n| **Static Legacy Archive Sheets (`3` sheets)** | `1,332`–`11,205`r | `Crypto_ETF_Flows`, `Top_Institutions`, `ETF_Market_Overview` (`2026-10-17 13:23:21 UTC`) | `7d 5h 14m` | **STATIC LEGACY ARCHIVE** |\n\n\n---\n\n# Part 2 — Mathematical Soft Ranking & Calibrated Expected Utility\n\n\nEVnet=Pfill⋅(PTP∣fill⋅Wnet−(1−PTP∣fill)⋅Ltotal−Fee−AS5m)−(1−Pfill)⋅Cwait,U=EVLCB, 5%E[Capital_Minutes]\text{EV}_{\text{net}} = P_{\text{fill}} \cdot \Big( P_{\text{TP}\mid\text{fill}} \cdot W_{\text{net}} - (1 - P_{\text{TP}\mid\text{fill}}) \cdot L_{\text{total}} - \text{Fee} - \text{AS}_{5\text{m}} \Big) - (1 - P_{\text{fill}}) \cdot C_{\text{wait}}, \qquad U = \frac{\text{EV}_{\text{LCB, 5\%}}}{\mathbb{E}[\text{Capital\_Minutes}]}EVnet​=Pfill​⋅(PTP∣fill​⋅Wnet​−(1−PTP∣fill​)⋅Ltotal​−Fee−AS5m​)−(1−Pfill​)⋅Cwait​,U=E[Capital_Minutes]EVLCB, 5%​​\n\nBecause `p_win_lower_bound_calibrated = false` (`sample_n = 17 < 100` in `live_snapshot_latest.json`), official `p_fill`, `p_win_given_fill`, `ev_net_usd`, `ev_lcb_5pct_usd`, and `utility` are **gated to `null`** in the Part 4 JSON schema (`HOLD`), while we report the exact **shadow point estimates and 5% stationary-bootstrap LCBs** below to rank the active position and staged candidates:\n\n| Rank | ID / Ticket | Symbol & Setup | Margin (`50%`) & Combined Margin % | Risk (LtotalL_{\text{total}}Ltotal​) / Net Reward (WnetW_{\text{net}}Wnet​) | Shadow PfillP_{\text{fill}}Pfill​ / PTP∣fillP_{\text{TP}\mid\text{fill}}PTP∣fill​ | Shadow EVnet\text{EV}_{\text{net}}EVnet​ (`$`) | Shadow EVLCB, 5%\text{EV}_{\text{LCB, 5\%}}EVLCB, 5%​ (`$`) | E[Cap_Min]\mathbb{E}[\text{Cap\_Min}]E[Cap_Min] (`$·min`) | Shadow Utility UUU (`bps/day`) | Council Decision |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| **Active** | **`#19274977`** | `BTCUSD.pi` `SELL` `0.05` @ `80,245.00` (`SL 80,620`, `TP 79,385`) | **`$2,006.13`** (`41.24%` Bal, `242.63%` ML) | `$19.50` / `$42.25` (`2.167R`) | `1.00` (`FILLED`) / `0.520` | **`+$10.35`** (`+$2.45` live) | **`+$3.80`** | `180,551.7` | **`+0.303`** | **`HOLD_AND_MANAGE` (`TP1 -> 79,895`, `Early-BE @ 80,050`)** |\n| **#1** | **`CAND_ETH_OTE_235650`** | `ETHUSD.pi` `SELL_LIMIT` `0.36` @ `2,356.50` (`SL 2,401.50`, `TP 2,266.50`) | **`$424.17`** (`49.95%` comb, `200.18%` ML) | `$17.35` / `$31.25` (`1.801R`) | `0.48` / `0.515` | **`+$3.15`** | **`+$0.72`** | `38,175.3` | **`+0.272`** | **`HOLD` (Top Non-Correlated Slot 2 Candidate)** |\n| **#2** | **`CAND_BNB_OTE_73475`** | `BNBUSD.p` `SELL_LIMIT` `1.15` @ `734.75` (`SL 748.75`, `TP 705.25`) | **`$422.48`** (`49.92%` comb, `200.32%` ML) | `$16.79` / `$33.24` (`1.980R`) | `0.45` / `0.505` | **`+$3.40`** | **`+$0.88`** | `38,023.3` | **`+0.333`** | **`HOLD` (Secondary Slot 2 Candidate; `EMA_5 > EMA_13`)** |\n| **#3** | **`CAND_BTC_PREFLIGHT_81300`** | `BTCUSD.pi` `SELL_LIMIT` `0.04` @ `81,300.00` (`SL 81,780`, `TP 79,850`) | **`$1,626.00`** (**`74.66%` comb, `134.01%` ML!**) | `$19.80` / `$57.40` (`2.899R`) | `0.26` / `0.470` | `+$3.98` | `-$0.45` | `146,340.0` | `-0.044` | **`HOLD / REJECTED` (Margin `74.66% > 50%` & `+20s` Post-Cutoff)** |\n\n\n---\n\n# Part 3 — Section 8: Continuous Kaizen & Self-Improvement Inquest\n\n\n1. **Skills & Methodology Optimization:**
\n- Mobilizing all 9 quantitative skills (`@[trader-signal]`, `@[trader-risk]`, `@[market-ingest]`, `@[market-pattern]`, `@[adaptive-wfo-epoch]`, `@[sharpe-ratio-non-iid-corrections]`, `@[time-series-decomposer]`, `@[clean-code]`, `@[systematic-debugging]`) across the upgraded 34-sheet `Data/DataBase_Trading.xlsx` (`133e868a...`) and repaired `live_snapshot_latest.json` (`18:36:26 UTC`) proved:
\n1. Live position `#19274977` (`BTCUSD.pi` `SELL` `0.05` lot @ `80,245.00`, filled `18:11:19 UTC`, currently `+$2.45 USD` at `80,196.00`) was immediately defended by a **`-$14,090,541.33` net taker sell delta** on the `18:15 UTC` 15m candle (`21_Tradfye_Orderflow`) and `$22.48M` of aged (`2h 31m–3h 43m`) Binance sell walls at `80,377.40–80,500.00` (`10_Whale_Orders`).\n2. Adding preflight candidate `CAND_BTC_PREFLIGHT_81300` (`0.04` lot @ `81,300.00`, `$1,626.00` margin) alongside `#19274977` (`$2,006.13` margin) breaches the 50% margin cap (`$3,632.13 = 74.66% > 50.0%`, true Margin Level `134.01% < 200.0%`).\n3. Sizing `ETHUSD.pi` (`CAND_ETH_OTE_235650`: VR(4)=1.3630VR(4)=1.3630VR(4)=1.3630, ER(48)=0.2152ER(48)=0.2152ER(48)=0.2152, tslope=−6.6610t_{\text{slope}}=-6.6610tslope​=−6.6610, θOU,15m=$2,334.54\theta_{\text{OU,15m}}=\$2,334.54θOU,15m​=$2,334.54) at **`0.36` lot** @ `2,356.50` consumes `$424.17` margin (`<= $426.41` remaining 50% margin capacity, combined `49.95% <= 50.0%`, Margin Level `200.18% >= 200.0%`) and `$17.35` nominal risk (`$23.69` stressed loss `<= $39.57` remaining headroom).\n\n\n2. **Omitted Risk Dimensions Uncovered:**
\n- **`execution_preflight.py` `margin_level_post_order` Denominator Trap:** When an active position (`#19274977`) already locks `$2,006.13` in `margin_used`, `execution_preflight.py` subtracted `$1,626.00` from `margin_free` (`$2,861.29 -> $1,235.29`) but computed `margin_level_post_order = 299.35%` (`$4,867.42 / $1,626.00`) without adding `margin_used` (`$2,006.13`) in the denominator, masking a `134.01%` Margin Level breach upon fill.\n- **Stop-Cluster & Bid-Wall Traps on Active `#19274977`:** `SL = 80,620.00` sits inside a `$25.91M` aged sell-wall / buy-stop cluster (`80,590–80,652.60` in `10_Whale_Orders` and `$10.57M` Buy Stops at `80,650` in `15_Hyperdash_Stops_Map`), while `TP = 79,385.00` sits behind `$7.35M` L3 bid wall (`79,881.00`), `$5.93M` aged (`1h 25m`) Binance bid wall (`79,850.00`), and `$14.36M` L3 bid wall (`79,529.00`).\n\n3. **Concrete Algorithmic Alternatives:**
\n- **Joint Margin-and-Solvency Constrained Lot Optimizer:** Enforce:\n
Vnew≤min⁡ ⁣(0.50⋅min⁡(Bal,Eq)−Marginused, active0.50⋅Entry⋅Csize,  Hrealized−2.00−Fee1.25⋅SLdist+Spread)V_{\text{new}} \le \min\!\left(\frac{0.50 \cdot \min(\text{Bal}, \text{Eq}) - \text{Margin}_{\text{used, active}}}{0.50 \cdot \text{Entry} \cdot C_{\text{size}}},\; \frac{H_{\text{realized}} - 2.00 - \text{Fee}}{1.25 \cdot \text{SL}_{\text{dist}} + \text{Spread}}\right)Vnew​≤min(0.50⋅Entry⋅Csize​0.50⋅min(Bal,Eq)−Marginused, active​​,1.25⋅SLdist​+SpreadHrealized​−2.00−Fee​)\n
which automatically yields `0.36` lot on `ETHUSD.pi` (`$424.17` margin, `$23.69` stress) and `1.15` lot on `BNBUSD.p` (`$422.48` margin, `$22.82` stress) while `#19274977` is open.\n- **Dynamic Microstructure Ratchet & Liquidity-Front-Run Exit Engine:** Stage `#19274977` `TP1` at `79,895.00` (front-running `$7.35M` @ `79,881.00` and `$5.93M` @ `79,850.00`) and trigger the `EARLY-BE` ratchet (`SL -> 80,229.00`) once `BTCUSD.pi` trades `<= 80,050.00` (`+0.52R`).\n- **Atomic Pre-Cutoff Preflight Signing:** Freeze `execution_preflight_receipt.json` before `cutoff_utc` and compute `receipt_sha256` after injecting `dispatch_nonce`.\n\n\n---\n\n# Part 4 — Required JSON Decision & Audit Payload (Schema v1.1.0)\n\n\n```\n{
  "schema_version": "1.1.0",
  "cycle_id": "Cycle-20261024T183726Z",
  "cutoff_utc": "2026-10-24 18:37:26 UTC",
  "evidence_manifest_sha256": "179677229c0595ae2cb18e408ab4c96e24dee8b44dec3d4209521e9a59b8566d",
  "prompt_sha256": "16cc04f7637f36a0c2e02fb2f25083c4aa2213e25789bedd2d7788f52b1f2f7d",
  "dispatch_nonce": "77029c03-e456-45b7-8ff8-13603238b3d3",
  "provenance_status": "DENIED_FAIL_CLOSED",
  "inventory_status": "VERIFIED_ONE_OPEN_SHORT_POSITION_19274977_ZERO_PENDING_ORDERS",
  "hard_gate_results": {
    "cutoff_causality_gate": "FAIL_CLOSED_POST_CUTOFF_PREFLIGHT (preflight tick_time_utc 2026-10-24 18:37:45 UTC and observed_at_utc 2026-10-24 18:37:46 UTC are +19.0s and +20.0s AFTER cutoff_utc 2026-10-24 18:37:26 UTC, violating tick_time < observed_at < cutoff_utc)",
    "preflight_quote_freshness_gate": "PASS_INTERNAL_AGE_FAIL_CAUSALITY (tick_age_seconds = 1.0s <= 15.0s, but sampled 19.0s after cutoff_utc)",
    "workbook_and_manifest_sha256_gate": "PASS (Data/DataBase_Trading.xlsx sha256 133e868a5ee684e151189e5acb49fbef45ec34055f5ffd879cfab031da14175e and Data/history/master_manifest.json sha256 179677229c0595ae2cb18e408ab4c96e24dee8b44dec3d4209521e9a59b8566d match commit 54d93c2a87ef92e0d6eed2369e6ed1b60e3925f9 100%)",
    "preflight_receipt_nonce_signature_gate": "FAIL_CLOSED (execution_preflight.py signed receipt with dispatch_nonce='' using indent=2 -> d0ee05e482a66fca5c98ff615f8ae0bf4619ec3d29349dd712134c86efd87d2d; prompt assembler injected dispatch_nonce 77029c03-e456-45b7-8ff8-13603238b3d3 without re-signing -> 3d9432a39dbbf91491d29a00f979f5337c8361618db2dd2761db8927fa350c87 indent=2 / 8d466650b6ac88594a7b5f5578456dd9c64ed744c6838209c8f7e8065202988d compact)",
    "excel_all_sheets_freshness_gate": "FAIL_CLOSED (cycle_envelope.json explicitly sets excel_freshness_verified=false and excel_audit_scorecard_fresh=false; Data/excel_all_sheets_checklist.json at 18:19:44 UTC reports all_passed=false with 26/31 passed and 5 stale sheets: 5_Funding_Rate [17:28:25 UTC], 6_Funding_Fee_Settlement [17:29:26 UTC], 7_Live_Liq [17:13:26 UTC], 9_Liquidation_Max_Pain_3D [17:16:34 UTC], 9_Liquidation_Max_Pain_7D [17:17:05 UTC]; note however that 18_CVD [18:33:26 UTC], 20_Auction_Market_Structure [18:34:02 UTC], and 21_Tradfye_Orderflow [18:34:32 UTC, 6,912 rows] are freshly updated)",
    "macro_calendar_freshness_gate": "FAIL_CLOSED (Data/macro_calendar.json verified_at 2026-10-24T17:56:08.703730+00:00 is 2,477.30s [41m 17.30s] old at cutoff_utc 18:37:26 UTC and 2,490.30s [41m 30.30s] old at Current Cycle 18:37:39 UTC, exceeding the 900s limit)",
    "whale_wall_180s_persistence_gate": "PASS_VIA_WORKBOOK_AND_META_LEDGER (Sheet 10_Whale_Orders at 18:18:29 UTC documents BTC sell walls persisted >=180s: $2.01M @ 80,377.4 [3h36m], $1.56M @ 80,384.6 [3h43m], $1.44M @ 80,400 [2h31m], $17.47M @ 80,500 [2h43m-3h43m], $8.64M @ 80,590 [25m40s-3h43m], $10.90M @ 80,637.9 [11m01s], $6.17M @ 80,652.6 [4m32s]; Sheet 17_Orderbook at 18:01:50 UTC documents L3 walls up to $22.77M; whale_persistence_ledger.json updated at 18:32:01 UTC with 73 tracked Hyperliquid whales)",
    "probability_calibration_gate": "FAIL_CLOSED (p_win_lower_bound_calibrated = false, sample_n = 17 < 100 minimum sample required in live_snapshot_latest.json)",
    "solvency_and_margin_collateralization_gate": "FAIL_CLOSED_ON_PREFLIGHT_CANDIDATE_PASS_ON_ETH_036_LOT (Active position #19274977 consumes $2,006.13 margin = 41.24% of $4,865.07 balance, leaving $426.41 under the 50% margin cap [$2,432.54]; preflight candidate 0.04 lot BTC @ 81,300 requires $1,626.00 margin -> combined $3,632.13 = 74.66% > 50% cap, true post-order Margin Level 134.01% < 200.0% [preflight receipt 299.35% omitted existing $2,006.13 margin_used in denominator]; whereas 0.36 lot ETHUSD.pi @ 2,356.50 requires $424.17 margin -> combined $2,430.30 = 49.95% <= 50.0% cap, Margin Level 200.18% >= 200.0%)"
  },
  "universe_coverage": {
    "total_broker_symbols": 156,
    "tradfi_weekend_halted_count": 98,
    "crypto_perpetuals_open_count": 58,
    "crypto_passing_25bps_spread_gate_count": 12,
    "crypto_passing_25bps_spread_gate_symbols": [
      "BTCUSD.pi (2.00 bps 00_MT5 / 1.87 bps 20_AMS & preflight / 1.99 bps snap)",
      "XMRUSD.p (3.49 bps 00_MT5 / 6.44 bps 20_AMS)",
      "ZECUSD.p (6.71 bps 00_MT5 / 7.59 bps 20_AMS)",
      "BNBUSD.p (6.90 bps 00_MT5 / 8.26 bps 20_AMS & snap)",
      "DSHUSD.p (9.42 bps 00_MT5 / 10.56 bps 20_AMS)",
      "ETHUSD.pi (13.79 bps 00_MT5 / 13.73 bps 20_AMS / 13.74 bps snap)",
      "YFIUSD.p (14.98 bps 00_MT5 / 19.62 bps 20_AMS)",
      "BCHUSD.p (17.61 bps 00_MT5 / 24.88 bps 20_AMS / 17.56 bps snap)",
      "XLMUSD.p (17.68 bps 00_MT5 / 18.84 bps 20_AMS)",
      "AVEUSD.p (19.85 bps 00_MT5 / 20.54 bps 20_AMS)",
      "XRPUSD.pi (23.46 bps 00_MT5 / 23.42 bps 20_AMS; 31.18 bps in snap)",
      "SOLUSD.p (23.86 bps 00_MT5 / 23.79 bps snap; 28.77 bps in 20_AMS)"
    ],
    "crypto_disqualified_by_spread_gate_count": 46
  },
  "account_tier_and_contingent_capacity": {
    "account_login": 5064568,
    "server": "BlueberryMarketsSVG-Live",
    "balance_usd": 4865.07,
    "equity_usd": 4867.52,
    "floating_pnl_credit_applied_usd": 0.0,
    "legal_solvency_equity_min_bal_eq_usd": 4865.07,
    "margin_used_usd": 2006.13,
    "margin_free_usd": 2861.39,
    "margin_level_pct": 242.63,
    "hard_floor_usd": 4600.0,
    "operating_buffer_usd": 4650.0,
    "solvency_kernel_usd": 4795.0,
    "hard_floor_cushion_usd": 265.07,
    "operating_buffer_cushion_usd": 215.07,
    "kernel_cushion_usd": 70.07,
    "base_net_headroom_usd": 68.07,
    "existing_ticket_19274977_stress_envelope_usd": 28.5,
    "existing_ticket_19274977_stress_snapshot_usd": 25.4375,
    "realized_headroom_envelope_usd": 39.57,
    "realized_headroom_snapshot_usd": 42.63,
    "post_joint_stress_equity_envelope_usd": 4834.57,
    "capital_mode": "TIER_2_HOUSE_MONEY",
    "risk_band_usd": [
      15.0,
      25.0
    ],
    "max_concurrent_tickets": 2,
    "remaining_50pct_margin_capacity_usd": 426.41
  },
  "global_contingency_usd": 2.0,
  "existing_ticket_actions": [
    {
      "ticket": 19274977,
      "symbol": "BTCUSD.pi",
      "position_type": "POSITION_TYPE_SELL (LIVE_OPEN_SHORT)",
      "volume": 0.05,
      "price_open": 80245.0,
      "sl": 80620.0,
      "tp": 79385.0,
      "price_current": 80196.0,
      "floating_profit_usd": 2.45,
      "margin_used_usd": 2006.13,
      "position_state_invariant": "ACTIVE_FILLED_SHORT_POSITION — Filled at 2026-10-24 18:11:19 UTC at 80,245.00; currently +49.00 pts (+$2.45 floating PnL at 80,196.00; +$3.55 / +0.19R at 80,174.00 in 00_MT5_Account_Telemetry). Per §1.3.5 Zero Floating Profit Credit, +$2.45 floating profit is excluded from solvency headroom.",
      "action": "HOLD_AND_MANAGE_ACTIVE_POSITION_WITH_TP_FRONT_RUN_AND_EARLY_BE_RATCHET",
      "tactical_rationale": "After filling at 80,245.00 (18:11:19 UTC), Sheet 21_Tradfye_Orderflow (18:34:32 UTC) confirms a -$14.09M net taker sell delta on the 18:15 UTC 15m candle defending the aged Binance sell walls at 80,377.40-80,500.00 ($22.48M persisted 2h31m-3h43m in 10_Whale_Orders) and the $7.40M L3 ask wall at 80,534.00 (17_Orderbook), while 1H OU equilibrium theta_OU = 78,885.89 (t_slope = -7.8911) pulls downward. However, three tactical adjustments are advised on the next causal preflight cycle: (1) Front-run opposing whale bid walls by modifying TP1 to 79,895.00 (in front of the $7.35M Hyperliquid L3 bid wall at 79,881.00 and $5.93M aged 1h04m-1h25m Binance bid wall at 79,850.00) and TP2 to 79,545.00 (in front of the $14.36M L3 bid wall at 79,529.00); (2) Trigger the EARLY-BE Stop-Loss ratchet to 80,229.00 (entry minus 16pt spread) once price trades <= 80,050.00 (+0.52R); (3) Note that current SL = 80,620.00 sits inside a $25.91M aged sell-wall / buy-stop cluster (80,590-80,652.60 in 10_Whale_Orders & $10.57M Buy Stops at 80,650 in 15_Hyperdash_Stops_Map)."
    }
  ],
  "candidate_rows": [
    {
      "candidate_id": "CAND_ETH_OTE_235650",
      "symbol": "ETHUSD.pi",
      "native_market": "CRYPTO_PERPETUAL_24_7",
      "clock_status": "OPEN_24_7_CRYPTO_PERPETUAL",
      "quote_timestamp": "2026-10-24 18:36:24 UTC",
      "evidence_availability_timestamps": {
        "live_snapshot_as_of_utc": "2026-10-24 18:36:26 UTC",
        "sheet_00_mt5_utc": "2026-10-24 18:25:03 UTC",
        "sheet_10_whale_orders_utc": "2026-10-24 18:18:29 UTC",
        "sheet_11_technical_utc": "2026-10-24 18:28:14 UTC",
        "sheet_17_orderbook_utc": "2026-10-24 18:01:50 UTC",
        "sheet_18_cvd_utc": "2026-10-24 18:33:26 UTC",
        "sheet_20_auction_utc": "2026-10-24 18:34:02 UTC",
        "sheet_21_tradfye_orderflow_utc": "2026-10-24 18:34:32 UTC"
      },
      "evidence_max_age_seconds": 2136,
      "evidence_age_at_cutoff_seconds": 60.0,
      "row_causality_status": "CAUSAL_PRE_CUTOFF_VERIFIED",
      "authorization_expiry_utc": "2026-10-24 19:07:26 UTC",
      "side": "SELL",
      "order_type": "SELL_LIMIT",
      "entry": 2356.5,
      "stop": 2401.5,
      "target": 2266.5,
      "volume": 0.36,
      "broker_risk_usd": 17.35,
      "broker_reward_usd": 31.25,
      "rr": 1.8012,
      "spread_cost_usd": 1.15,
      "stressed_loss_usd": 23.69,
      "post_joint_stop_balance": 4810.88,
      "p_fill": null,
      "p_win_given_fill": null,
      "probability_calibration_status": "UNCALIBRATED_SAMPLE_N_17_LT_100",
      "estimator_references": [
        "Lo-MacKinlay Heteroskedasticity-Robust Variance Ratio VR(q=4)=1.3630 (z*=+1.0141) > 1.15 super-diffusive trend",
        "Kaufman Efficiency Ratio ER(48)=0.2152 >= 0.20 trend-qualified (20_Auction_Market_Structure Regime = TREND_DOWN_ACCEPTANCE)",
        "Newey-West HAC Trend t_slope=-6.6610 (15m) & t_slope=-7.9043 (1H) (|t|>=2.0)",
        "Discrete Ornstein-Uhlenbeck Equilibrium theta_15m=2334.5414 (b_ou=-0.024287, hl=28.2b) & theta_1H=2049.0720 (b_ou=-0.003356, hl=206.2b) < Entry 2356.50 (PASSES §1.1.5 OU Drift Gate on both 15m [+21.96 pts] and 1H [+307.43 pts])",
        "Sheet 17_Orderbook (18:01:50 UTC) L3 Institutional Ask Walls: $9,105,206.29 (3,874.39 ETH) @ 2,350.10, $3,333,105.63 @ 2,351.60, and $4,698,410.56 @ 2,363.30"
      ],
      "calibration_diagnostics": {
        "empirical_p_win_lower_bound": 0.4197,
        "p_win_lower_bound_calibrated": false,
        "p_win_calibration_sample_n": 17,
        "p_be_at_320pt_spread": 0.357,
        "shadow_point_p_fill": 0.48,
        "shadow_point_p_win_given_fill": 0.515
      },
      "effective_sample_size": 17,
      "probability_confidence_intervals": {
        "p_fill_90pct_ci": [
          0.33,
          0.63
        ],
        "p_win_given_fill_90pct_ci": [
          0.4197,
          0.615
        ]
      },
      "outcome_model_and_timeout_branches": {
        "ttl_minutes": 90,
        "branch_tp_first": "Net gain +$31.25 (+$32.40 gross, 2.00R gross / 1.8012R net) at TP 2,266.50 (or +$20.81 net at TP1 2,295.50 front-running $8.86M L3 bid wall at 2,293.70 & Deribit Max Pain at 2,300.00)",
        "branch_sl_first": "Net loss -$17.35 (-$16.20 base + $1.15 exit spread) at SL 2,401.50 (strictly behind 0.786=2,373.63 + 0.40*ATR(11.13) + half_spread(1.60) = 2,379.68, behind d_VAH=2,384.05, 24H Short Max Pain=2,399.79, and Swing High=2,400.40)",
        "branch_timeout_unfilled": "Expires unfilled with $0.12 shadow wait cost"
      },
      "cost_ledger_and_conditioning": {
        "base_sl_loss_usd": 16.2,
        "exit_spread_cost_usd": 1.15,
        "commission_and_swap_reserve_usd": 2.0,
        "adverse_selection_markout_5m_usd": 0.95
      },
      "wait_cost_usd": 0.12,
      "ev_net_usd": null,
      "ev_lcb_5pct_usd": null,
      "expected_capital_minutes": 38175.3,
      "utility": null,
      "uncertainty_method": "Time-blocked stationary bootstrap (block_length=12 bars, B=1000) gated to null under uncalibrated sample_n=17 < 100; shadow EV_net=+$3.15, shadow LCB_5%=+$0.72",
      "adverse_selection_usd": 0.95,
      "evidence_ids": [
        "Data/DataBase_Trading.xlsx#00_MT5_Account_Telemetry",
        "Data/DataBase_Trading.xlsx#11_Technical",
        "Data/DataBase_Trading.xlsx#17_Orderbook",
        "Data/DataBase_Trading.xlsx#18_CVD",
        "Data/DataBase_Trading.xlsx#20_Auction_Market_Structure",
        "Data/DataBase_Trading.xlsx#21_Tradfye_Orderflow",
        "docs/telemetry/live_snapshot_latest.json"
      ],
      "verdict": "HOLD",
      "fib_prime_ema_alignment": {
        "hierarchy": "BEARISH_MONOTONIC (EMA_5 2,315.17 < EMA_13 2,315.93 < EMA_34 2,332.58 < EMA_89 2,356.25 < EMA_144 2,370.61 < EMA_233 2,387.80; Trend Bias = STRONG BEARISH)",
        "ema_5": 2315.17,
        "ema_13": 2315.93,
        "ema_34": 2332.58,
        "ema_89": 2356.25,
        "ema_144": 2370.61,
        "ema_233": 2387.8,
        "aligned": true
      },
      "fib_golden_zone_confluence": {
        "impulse_leg": "Intraday Bearish Impulse [2,275.30, 2,400.40] (20_Auction_Market_Structure at 18:34:02 UTC)",
        "gp_0618": 2352.61,
        "gp_0650": 2356.62,
        "ote_0702": 2363.12,
        "invalidation_shelf_0786": 2373.63,
        "buffered_invalidation_shelf_0786": 2379.68,
        "entry_status": "EXACT_0650_GOLDEN_POCKET_235662_AND_EMA_89_235625_CONFLUENCE_BETWEEN_911M_AND_470M_L3_ASK_WALLS"
      },
      "auction_extreme_interaction": {
        "monday_ib_relation": "RETESTING_ABOVE_MONDAY_LOW_234730 (Mon_Mid = 2,394.65, Mon_H = 2,442.00)",
        "session_extreme_sweep": "SWEEPING_ASIAN_LOW_234640_AND_LONDON_LOW_235060_INTO_NY_HIGH_236830_SUPPLY",
        "macro_shelf_relation": "ABOVE_CWL_227530 (Deribit Options Max Pain = 2,300.00, 24H Long Liq Max Pain = 2,270.96)",
        "value_area_status": "BELOW_VALUE_IMBALANCE_RETESTING_D_VAL_233572_TO_D_POC_237572 (Regime = TREND_DOWN_ACCEPTANCE)"
      },
      "rejection_reasons": [
        "No preflight receipt for ETHUSD.pi",
        "Hard gates fail-closed (excel_freshness_verified=false, post-cutoff preflight receipt, macro_calendar stale [2,477.3s > 900s], p_win_lower_bound_calibrated=false)"
      ]
    },
    {
      "candidate_id": "CAND_BNB_OTE_73475",
      "symbol": "BNBUSD.p",
      "native_market": "CRYPTO_PERPETUAL_24_7",
      "clock_status": "OPEN_24_7_CRYPTO_PERPETUAL",
      "quote_timestamp": "2026-10-24 18:36:25 UTC",
      "evidence_availability_timestamps": {
        "live_snapshot_as_of_utc": "2026-10-24 18:36:26 UTC",
        "sheet_00_mt5_utc": "2026-10-24 18:25:03 UTC",
        "sheet_11_technical_utc": "2026-10-24 18:28:14 UTC",
        "sheet_17_orderbook_utc": "2026-10-24 18:01:50 UTC",
        "sheet_18_cvd_utc": "2026-10-24 18:33:26 UTC",
        "sheet_20_auction_utc": "2026-10-24 18:34:02 UTC",
        "sheet_21_tradfye_orderflow_utc": "2026-10-24 18:34:32 UTC"
      },
      "evidence_max_age_seconds": 2136,
      "evidence_age_at_cutoff_seconds": 60.0,
      "row_causality_status": "CAUSAL_PRE_CUTOFF_VERIFIED",
      "authorization_expiry_utc": "2026-10-24 19:07:26 UTC",
      "side": "SELL",
      "order_type": "SELL_LIMIT",
      "entry": 734.75,
      "stop": 748.75,
      "target": 705.25,
      "volume": 1.15,
      "broker_risk_usd": 16.79,
      "broker_reward_usd": 33.24,
      "rr": 1.9797,
      "spread_cost_usd": 0.69,
      "stressed_loss_usd": 22.82,
      "post_joint_stop_balance": 4811.75,
      "p_fill": null,
      "p_win_given_fill": null,
      "probability_calibration_status": "UNCALIBRATED_SAMPLE_N_17_LT_100",
      "estimator_references": [
        "Lo-MacKinlay VR(q=4)=1.1776 (z*=+0.7360) > 1.15, Kaufman ER(48)=0.2365 >= 0.20 trend-qualified, Newey-West t_slope=-10.8216 (t_ret=-1.4370)",
        "Discrete OU Equilibrium theta_15m=725.9464 (b_ou=-0.023235, hl=29.5b) < Entry 734.75 (+8.80 pts favorable downward OU drift)",
        "Sheet 21_Tradfye_Orderflow (18:34:32 UTC): BNBUSDT 15m Net Delta = -$215,585.51 (-27.82%), CVD = -$15,193,278.68, Orderflow Regime = AGGRESSIVE_SELLER_DOMINATION / BEARISH_EXPANSION"
      ],
      "calibration_diagnostics": {
        "empirical_p_win_lower_bound": 0.4197,
        "p_win_lower_bound_calibrated": false,
        "p_win_calibration_sample_n": 17,
        "p_be_at_060pt_spread": 0.3356,
        "shadow_point_p_fill": 0.45,
        "shadow_point_p_win_given_fill": 0.505
      },
      "effective_sample_size": 17,
      "probability_confidence_intervals": {
        "p_fill_90pct_ci": [
          0.3,
          0.6
        ],
        "p_win_given_fill_90pct_ci": [
          0.4197,
          0.6
        ]
      },
      "outcome_model_and_timeout_branches": {
        "ttl_minutes": 90,
        "branch_tp_first": "Net gain +$33.24 (+$33.93 gross, 2.107R gross / 1.9797R net) at TP 705.25 (or TP1 722.25 front-running $1.29M L3 bid wall at 721.70)",
        "branch_sl_first": "Net loss -$16.79 (-$16.10 base + $0.69 exit spread) at SL 748.75 (strictly behind 0.786=738.59, d_VAH=740.15, Swing High=744.60, and pd_POC=746.37)",
        "branch_timeout_unfilled": "Expires unfilled with $0.12 shadow wait cost"
      },
      "cost_ledger_and_conditioning": {
        "base_sl_loss_usd": 16.1,
        "exit_spread_cost_usd": 0.69,
        "commission_and_swap_reserve_usd": 2.0,
        "adverse_selection_markout_5m_usd": 0.85
      },
      "wait_cost_usd": 0.12,
      "ev_net_usd": null,
      "ev_lcb_5pct_usd": null,
      "expected_capital_minutes": 38023.3,
      "utility": null,
      "uncertainty_method": "Time-blocked stationary bootstrap gated to null under uncalibrated sample_n=17 < 100; shadow EV_net=+$3.40, shadow LCB_5%=+$0.88",
      "adverse_selection_usd": 0.85,
      "evidence_ids": [
        "Data/DataBase_Trading.xlsx#00_MT5_Account_Telemetry",
        "Data/DataBase_Trading.xlsx#11_Technical",
        "Data/DataBase_Trading.xlsx#17_Orderbook",
        "Data/DataBase_Trading.xlsx#18_CVD",
        "Data/DataBase_Trading.xlsx#20_Auction_Market_Structure",
        "Data/DataBase_Trading.xlsx#21_Tradfye_Orderflow",
        "docs/telemetry/live_snapshot_latest.json"
      ],
      "verdict": "HOLD",
      "fib_prime_ema_alignment": {
        "hierarchy": "UPPER_RIBBON_BEARISH_LOWER_CROSSED (EMA_5 723.78 > EMA_13 723.42 < EMA_34 726.33 < EMA_89 731.70 < EMA_144 734.30 < EMA_233 735.68; 11_Technical Bias = NEUTRAL / CHOP)",
        "ema_5": 723.78,
        "ema_13": 723.42,
        "ema_34": 726.33,
        "ema_89": 731.7,
        "ema_144": 734.3,
        "ema_233": 735.68,
        "aligned": false
      },
      "fib_golden_zone_confluence": {
        "impulse_leg": "Intraday Bearish Impulse [716.50, 744.60] (20_Auction_Market_Structure at 18:34:02 UTC)",
        "gp_0618": 733.87,
        "gp_0650": 734.76,
        "ote_0702": 736.23,
        "invalidation_shelf_0786": 738.59,
        "buffered_invalidation_shelf_0786": 739.73,
        "entry_status": "EXACT_0650_GOLDEN_POCKET_73476_AND_EMA_144_73430_CONFLUENCE_BELOW_D_POC_73634"
      },
      "auction_extreme_interaction": {
        "monday_ib_relation": "SWEEPING_ABOVE_MONDAY_HIGH_72950 (Mon_Mid = 718.25, Mon_L = 707.00)",
        "session_extreme_sweep": "SWEEPING_NY_HIGH_73230_INTO_ASIAN_LOW_73210_AND_LONDON_HIGH_73900_SUPPLY",
        "macro_shelf_relation": "ABOVE_CWL_71650_AND_MON_L_70700",
        "value_area_status": "INSIDE_VALUE_RETESTING_D_POC_73634_BELOW_D_VAH_74015"
      },
      "rejection_reasons": [
        "EMA_5 (723.78) slightly above EMA_13 (723.42) in 11_Technical (Bias = NEUTRAL / CHOP)",
        "No preflight receipt for BNBUSD.p",
        "Hard gates fail-closed (excel_freshness_verified=false, post-cutoff preflight receipt, macro_calendar stale, p_win_lower_bound_calibrated=false)"
      ]
    },
    {
      "candidate_id": "CAND_BTC_PREFLIGHT_81300",
      "symbol": "BTCUSD.pi",
      "native_market": "CRYPTO_PERPETUAL_24_7",
      "clock_status": "OPEN_24_7_CRYPTO_PERPETUAL",
      "quote_timestamp": "2026-10-24 18:37:45 UTC",
      "evidence_availability_timestamps": {
        "preflight_observed_at_utc": "2026-10-24 18:37:46 UTC",
        "live_snapshot_as_of_utc": "2026-10-24 18:36:26 UTC",
        "sheet_00_mt5_utc": "2026-10-24 18:25:03 UTC",
        "sheet_10_whale_orders_utc": "2026-10-24 18:18:29 UTC",
        "sheet_11_technical_utc": "2026-10-24 18:28:14 UTC",
        "sheet_17_orderbook_utc": "2026-10-24 18:01:50 UTC",
        "sheet_20_auction_utc": "2026-10-24 18:34:02 UTC",
        "sheet_21_tradfye_orderflow_utc": "2026-10-24 18:34:32 UTC"
      },
      "evidence_max_age_seconds": 2136,
      "evidence_age_at_cutoff_seconds": -20.0,
      "row_causality_status": "VIOLATION_POST_CUTOFF_PREFLIGHT_PLUS_20S",
      "authorization_expiry_utc": "2026-10-24 19:07:26 UTC",
      "side": "SELL",
      "order_type": "SELL_LIMIT",
      "entry": 81300.0,
      "stop": 81780.0,
      "target": 79850.0,
      "volume": 0.04,
      "broker_risk_usd": 19.8,
      "broker_reward_usd": 57.4,
      "rr": 2.899,
      "spread_cost_usd": 0.6,
      "stressed_loss_usd": 26.75,
      "post_joint_stop_balance": 4807.82,
      "p_fill": null,
      "p_win_given_fill": null,
      "probability_calibration_status": "UNCALIBRATED_SAMPLE_N_17_LT_100",
      "estimator_references": [
        "Lo-MacKinlay VR(q=4)=1.1869 (z*=+0.6631), ER(48)=0.0840 (< 0.15 chop; 20_AMS Regime = ROTATIONAL_BALANCE, 11_Technical Bias = NEUTRAL / CHOP), Newey-West t_slope=-7.6456",
        "Discrete OU Equilibrium theta_15m=80405.4216 (b_ou=-0.049567, hl=13.6b) < Entry 81,300.00 (+894.58 pts above theta)",
        "Sheet 17_Orderbook (18:01:50 UTC) L3 Ask Walls: $7,408,479.58 @ 81,393.00 and $8,332,218.29 @ 81,737.00; Sheet 15_Hyperdash_Stops_Map: $18.77M Buy Stops at 81,150.00"
      ],
      "calibration_diagnostics": {
        "empirical_p_win_lower_bound": 0.4197,
        "p_win_lower_bound_calibrated": false,
        "p_win_calibration_sample_n": 17,
        "p_be_at_15pt_spread": 0.2565
      },
      "effective_sample_size": 17,
      "probability_confidence_intervals": {
        "p_fill_90pct_ci": [
          0.16,
          0.42
        ],
        "p_win_given_fill_90pct_ci": [
          0.38,
          0.58
        ]
      },
      "outcome_model_and_timeout_branches": {
        "ttl_minutes": 90,
        "branch_tp_first": "Net gain +$57.40 (+$58.00 gross, 3.0208R gross / 2.8990R net) at TP 79,850.00",
        "branch_sl_first": "Net loss -$19.80 (-$19.20 base + $0.60 spread) at SL 81,780.00",
        "branch_timeout_unfilled": "Expires unfilled with $0.12 shadow wait cost"
      },
      "cost_ledger_and_conditioning": {
        "base_sl_loss_usd": 19.2,
        "exit_spread_cost_usd": 0.6,
        "commission_and_swap_reserve_usd": 2.0,
        "adverse_selection_markout_5m_usd": 1.35
      },
      "wait_cost_usd": 0.12,
      "ev_net_usd": null,
      "ev_lcb_5pct_usd": null,
      "expected_capital_minutes": 146340.0,
      "utility": null,
      "uncertainty_method": "Time-blocked stationary bootstrap gated to null under post-cutoff preflight violation, margin cap breach, and uncalibrated sample_n=17 < 100",
      "adverse_selection_usd": 1.35,
      "evidence_ids": [
        "Data/execution_preflight_receipt.json",
        "Data/DataBase_Trading.xlsx#10_Whale_Orders",
        "Data/DataBase_Trading.xlsx#11_Technical",
        "Data/DataBase_Trading.xlsx#15_Hyperdash_Stops_Map",
        "Data/DataBase_Trading.xlsx#17_Orderbook",
        "Data/DataBase_Trading.xlsx#20_Auction_Market_Structure"
      ],
      "verdict": "HOLD",
      "fib_prime_ema_alignment": {
        "hierarchy": "LOWER_RIBBON_BULLISH_CROSSED (EMA_5 80,091.84 > EMA_13 80,009.34 < EMA_34 80,173.63 < EMA_89 80,560.55 < EMA_144 80,897.29 < EMA_233 81,374.85; Bias = NEUTRAL / CHOP)",
        "ema_5": 80091.84,
        "ema_13": 80009.34,
        "ema_34": 80173.63,
        "ema_89": 80560.55,
        "ema_144": 80897.29,
        "ema_233": 81374.85,
        "aligned": false
      },
      "fib_golden_zone_confluence": {
        "impulse_leg": "Intraday Bearish Impulse [79,071.00, 81,445.50] (20_Auction_Market_Structure at 18:34:02 UTC)",
        "gp_0618": 80538.44,
        "gp_0650": 80614.43,
        "ote_0702": 80737.9,
        "invalidation_shelf_0786": 80937.36,
        "entry_status": "OUTSIDE_GOLDEN_ZONE_09387_RETRACEMENT_ABOVE_0786_INVALIDATION_8093736_AT_PD_VAL_8133526"
      },
      "auction_extreme_interaction": {
        "monday_ib_relation": "ABOVE_MONDAY_LOW_8074300_BELOW_MON_MID_8191525",
        "session_extreme_sweep": "BELOW_ASIAN_HIGH_8140500_ABOVE_LONDON_HIGH_8081500",
        "macro_shelf_relation": "ABOVE_CWL_79071",
        "value_area_status": "ABOVE_D_VAH_8100822_RETESTING_PD_VAL_8133526"
      },
      "rejection_reasons": [
        "HARD_MARGIN_GATE_VIOLATION (Finding D3): With #19274977 (0.05 lot BTC short, $2,006.13 active margin) open, adding 0.04 lot @ 81,300.00 ($1,626.00 margin) pushes total margin used to $3,632.13 = 74.66% > 50.0% cap and true post-order Margin Level to 134.01% < 200.0% floor (preflight receipt reported 299.35% by dividing $4,867.42 by $1,626.00 alone while margin_free_post_order dropped to $1,235.29)",
        "CAUSALITY_VIOLATION: preflight tick_time_utc (18:37:45 UTC) and observed_at_utc (18:37:46 UTC) are +19.0s and +20.0s AFTER cutoff_utc (18:37:26 UTC)",
        "NONCE_SIGNATURE_MISMATCH: receipt_sha256 (d0ee05e4...) was signed with dispatch_nonce='' rather than '77029c03-e456-45b7-8ff8-13603238b3d3'",
        "GEOMETRIC_AND_REGIME_MISMATCH: BTC ER(48)=0.0840 < 0.15 (ROTATIONAL_BALANCE / NEUTRAL CHOP); Entry 81,300.00 (0.9387 Fib) sits +562.10 pts above 0.702 OTE (80,737.90) and +362.64 pts above 0.786 invalidation (80,937.36), while TP 79,850.00 sits on top of $5.93M aged buy wall (1h04m-1h25m) and behind $7.35M L3 buy wall at 79,881.00; also violates non-correlated 2-ticket diversification since #19274977 is already short BTCUSD.pi"
      ]
    }
  ],
  "arithmetic_validation": {
    "account_balance_usd": 4865.07,
    "account_equity_envelope_usd": 4867.52,
    "legal_solvency_equity_min_bal_eq_usd": 4865.07,
    "hard_floor_cushion_check": "4865.07 - 4600.00 = 265.07 USD (PASS)",
    "operating_buffer_cushion_check": "4865.07 - 4650.00 = 215.07 USD (PASS)",
    "solvency_kernel_cushion_check": "4865.07 - 4795.00 = 70.07 USD (PASS)",
    "base_net_headroom_check": "70.07 - 2.00 = 68.07 USD (PASS)",
    "active_position_19274977_valuation_check": "LIVE SHORT 0.05 lot @ 80,245.00, SL 80,620.00 (375.0 pts), TP 79,385.00 (860.0 pts), current 80,196.00: floating_pnl = 0.05 * (80245.0 - 80196.0) = +2.45 USD (excluded from solvency per §1.3.5); active_margin_used = 0.05 * 80245.0 * 0.50 = 2006.125 -> 2006.13 USD (41.24% of balance, Margin Level = 4867.52 / 2006.13 = 242.6323%); envelope_stress = 28.50 USD -> realized_headroom = 68.07 - 28.50 = 39.57 USD, post_stress_equity = 4865.07 - 28.50 - 2.00 = 4834.57 USD",
    "preflight_candidate_81300_valuation_check": "0.04 lot @ 81,300.00, SL 81,780.00 (480.0 pts), TP 79,850.00 (1,450.0 pts), spread 15.0 pts: base_loss = 0.04 * 480.0 = 19.20 USD, gross_tp = 0.04 * 1450.0 = 58.00 USD (net_tp = 57.40 USD), exit_spread = 0.04 * 15.0 = 0.60 USD, total_nominal_risk = 19.80 USD, receipt_stress = 1.25 * (19.20 + 0.60) + 2.00 = 26.75 USD, spec_134_stress = 1.25 * 19.20 + 0.60 + 2.00 = 26.60 USD; joint post-stop balance = 4834.57 - 26.75 = 4807.82 USD >= 4795.00 USD",
    "preflight_candidate_81300_margin_violation_check": "New margin = 0.04 * 81,300.00 * 0.50 = 1626.00 USD; with active #19274977 margin_used = 2006.13 USD, total_margin = 2006.13 + 1626.00 = 3632.13 USD (74.66% of $4,865.07 balance > 50.0% cap; free_margin_post_order = 2861.29 - 1626.00 = 1235.29 USD; TRUE post-order Margin Level = 4867.42 / 3632.13 = 134.01% < 200.0% floor! Preflight receipt 299.35% divided 4867.42 by 1626.00 alone) (FAIL_CLOSED)",
    "eth_candidate_235650_036lot_margin_and_risk_check": "0.36 lot ETHUSD.pi @ 2,356.50, SL 2,401.50 (45.0 pts), TP 2,266.50 (90.0 pts), spread 3.20 pts: margin = 0.36 * 2356.50 * 0.50 = 424.17 USD <= 426.41 USD remaining 50% margin capacity; combined margin with #19274977 = 2006.13 + 424.17 = 2430.30 USD (49.95% of balance <= 50.0%, combined Margin Level = 4865.07 / 2430.30 = 200.18% >= 200.0%); base_loss = 16.20 USD, spread = 1.15 USD, total_nominal_risk = 17.35 USD, stressed_loss = 23.69 USD <= 39.57 USD headroom, post-joint-stop balance = 4834.57 - 23.69 = 4810.88 USD >= 4795.00 USD (PASS)"
  },
  "disputes": [
    "DISPUTE_1_PREFLIGHT_MARGIN_LEVEL_DENOMINATOR_OMISSION: In execution_preflight_receipt.json, order_check reports margin_free_post_order = 1235.29 USD ($2,861.29 - $1,626.00), confirming that active position #19274977 already locks $2,006.13 in margin_used, yet reports margin_level_post_order = 299.35% ($4,867.42 / $1,626.00), omitting the existing $2,006.13 margin_used in the denominator. True post-order margin is $3,632.13 (74.66% of balance > 50.0% cap) and true post-order Margin Level is 134.01% (< 200.0% floor).",
    "DISPUTE_2_POST_CUTOFF_PREFLIGHT_VIOLATION: In execution_preflight_receipt.json, tick_time_utc ('2026-10-24 18:37:45 UTC') and observed_at_utc ('2026-10-24 18:37:46 UTC') occur +19.0s and +20.0s AFTER cutoff_utc ('2026-10-24 18:37:26 UTC'), violating §1.4.1 Strict Physical Cutoff Causality (tick_time < observed_at < cutoff_utc).",
    "DISPUTE_3_PREFLIGHT_NONCE_SIGNATURE_MISMATCH: execution_preflight_receipt.json claims receipt_sha256 = d0ee05e482a66fca5c98ff615f8ae0bf4619ec3d29349dd712134c86efd87d2d, which is the exact SHA-256 of json.dumps(receipt_core, sort_keys=True, indent=2) when dispatch_nonce is empty (''). With dispatch_nonce = '77029c03-e456-45b7-8ff8-13603238b3d3', SHA-256 is 3d9432a39dbbf91491d29a00f979f5337c8361618db2dd2761db8927fa350c87 (indent=2).",
    "DISPUTE_4_MACRO_CALENDAR_AND_5_SHEET_STALENESS: Data/macro_calendar.json verified_at (17:56:08.70 UTC) is 2,477.30s (>900s) old at cutoff_utc, and 5 sheets in Data/excel_all_sheets_checklist.json (5_Funding_Rate, 6_Funding_Fee_Settlement, 7_Live_Liq, 9_Liquidation_Max_Pain_3D, 9_Liquidation_Max_Pain_7D) exceed the 20m freshness window."
  ],
  "unknowns": [
    "Calibrated out-of-sample fill probability P_fill and conditional win probability P_TP|fill remain uncalibrated (p_win_lower_bound_calibrated = false, sample_n = 17 < 100 minimum sample).",
    "Exact continuous persistence age in seconds for Hyperliquid L3 resting orderbook walls in Sheet 17_Orderbook (18:01:50 UTC) is not separately logged in whale_persistence_ledger.json (which tracks 73 Hyperliquid whale positions rather than L3 limit order IDs)."
  ],
  "methodology_critique_and_improvements": [
    "Major Telemetry Upgrade Verified: Commit 54d93c2a (18:36:26 UTC) repaired all 14 crypto perpetuals in live_snapshot_latest.json with non-null causal indicators and clean 15m/1H/4H bar series, and refreshed Sheet 21_Tradfye_Orderflow (18:34:32 UTC, 6,912 rows), Sheet 20_Auction_Market_Structure (18:34:02 UTC, 173 rows), and Sheet 18_CVD (18:33:26 UTC, 1,500 rows), reducing stale canonical sheets in excel_all_sheets_checklist.json from 14 down to 5.",
    "Fix execution_preflight.py margin_level_post_order formula to divide Equity by (margin_used_existing + margin_required_new) rather than margin_required_new alone, and size any second ticket while #19274977 is open to <= $426.41 margin (e.g., 0.36 lot ETHUSD.pi @ 2,356.50 = $424.17 margin or 1.15 lot BNBUSD.p @ 734.75 = $422.48 margin)."
  ],
  "section_8_kaizen": {
    "skills_and_methodology_optimization": "Mobilizing all 9 quantitative skills (@[trader-signal], @[trader-risk], @[market-ingest], @[market-pattern], @[adaptive-wfo-epoch], @[sharpe-ratio-non-iid-corrections], @[time-series-decomposer], @[clean-code], @[systematic-debugging]) across all 34 upgraded sheets of Data/DataBase_Trading.xlsx (133e868a...) proved three critical insights: (1) Live position #19274977 (BTCUSD.pi SHORT 0.05 lot @ 80,245.00, filled at 18:11:19 UTC, currently +$2.45 at 80,196.00) was immediately defended by a -$14.09M net taker sell delta on the 18:15 UTC 15m candle (Sheet 21_Tradfye_Orderflow) and $22.48M of aged sell walls at 80,377.40-80,500.00 (Sheet 10_Whale_Orders); (2) Adding preflight candidate 0.04 lot BTC @ 81,300.00 ($1,626.00 margin) alongside active #19274977 ($2,006.13 margin) breaches the 50% margin cap ($3,632.13 = 74.66% > 50%, true Margin Level 134.01% < 200%); (3) Sizing ETHUSD.pi (CAND_ETH_OTE_235650: VR(4)=1.3630, ER(48)=0.2152, t_slope=-6.6610, theta_OU=2,334.54) at 0.36 lot @ 2,356.50 consumes $424.17 margin, fitting inside the exact $426.41 remaining 50% margin capacity (combined 49.95% <= 50.0%, Margin Level 200.18% >= 200.0%) and $39.57 remaining solvency headroom ($23.69 stressed loss).",
    "omitted_risk_dimensions": "1. MT5 order_check Margin Level Denominator Trap on Pending Orders: MT5's native order_check for a pending limit order reports margin_free_post_order = 1235.29 USD (deducting both existing $2,006.13 and new $1,626.00), but execution_preflight.py computed margin_level_post_order = 299.35% ($4,867.42 / $1,626.00) without including existing margin_used ($2,006.13), masking a 134.01% Margin Level breach upon fill. 2. Stop-Hunt & Bid-Wall Traps on Active #19274977: SL = 80,620.00 sits inside a $25.91M aged sell-wall / buy-stop cluster (80,590-80,652.60 in 10_Whale_Orders and $10.57M Buy Stops at 80,650 in 15_Hyperdash_Stops_Map), while TP = 79,385.00 sits behind $7.35M L3 bid wall at 79,881.00, $5.93M aged (1h04m-1h25m) bid wall at 79,850.00, and $14.36M L3 bid wall at 79,529.00.",
    "algorithmic_alternatives": "1. Joint Margin-and-Solvency Constrained Lot Optimizer: Enforce Vol_new <= min((0.50 * min(Bal, Eq) - Margin_Used_Active) / (0.50 * Entry * ContractSize), (H_realized - 2.00 - Fee) / (1.25 * SL_dist + Spread)), which automatically derives 0.36 lot ETHUSD.pi ($424.17 margin, $23.69 stress) and 1.15 lot BNBUSD.p ($422.48 margin, $22.82 stress) while #19274977 is open. 2. Dynamic Microstructure Ratchet & Liquidity-Front-Run Exit Engine: Use Sheet 15_Hyperdash_Stops_Map and Sheet 17_Orderbook to stage #19274977 TP1 at 79,895.00 (front-running $7.35M @ 79,881 & $5.93M @ 79,850) and ratchet SL to 80,229.00 (early-BE) once price reaches 80,050.00. 3. Atomic Pre-Cutoff Preflight Signing to eliminate the +19s/+20s post-cutoff race and nonce hash mismatch."
  },
  "authorization": "DENIED_FAIL_CLOSED",
  "response_sha256": "88f976f800e9fbd4a538fa282de8f4c0f9a8ec5f7179501e947a1b505c8395a2"
}\n```\n