\n📚 **Active Skills Loaded & Applied:** `@[trader-signal]`, `@[trader-risk]`, `@[market-ingest]`, `@[market-pattern]`, `@[adaptive-wfo-epoch]`, `@[sharpe-ratio-non-iid-corrections]`, `@[time-series-decomposer]`, `@[clean-code]`, `@[systematic-debugging]`\n
\n`[ALERT] TELEMETRY STALE WARNING: Data/execution_preflight_receipt.json is post-cutoff & signature-mutated (Last updated: 2026-10-25 02:39:32 UTC / Tick: 2026-10-25 02:39:31 UTC vs Cutoff: 2026-10-25 02:39:18 UTC [+13.0s/+14.0s post-cutoff] and Current Cycle: 2026-10-25 02:39:27 UTC [+4.0s/+5.0s future-skewed]; dispatch_nonce mutated after receipt_sha256 signing)`\n
`[ALERT] TELEMETRY STALE WARNING: Data/DataBase_Trading.xlsx (19/32 canonical sheets > 20m stale at 02:39:27 UTC, including 22_Forced_Liquidations_MTF [00:59:55 UTC, 99.53m], 15_Hyperdash_Stops_Map [01:40:17 UTC, 59.17m], 21_Tradfye_Orderflow [01:45:03 UTC, 54.40m], 3_Exchanges_LS_Ratio_15M [01:48:49 UTC, 50.63m], 9_Liquidation_Max_Pain_7D [01:59:37 UTC, 39.83m], 10_Whale_Orders [02:00:26 UTC, 39.02m], 00_MT5_Account_Telemetry [02:07:27 UTC, 32.00m], 17_Orderbook [02:16:41 UTC, 22.77m], 18_CVD [02:17:47 UTC, 21.67m], and 20_Auction_Market_Structure [02:18:32 UTC, 20.92m]) and Data/excel_all_sheets_checklist.json is failing (Last updated: 2026-10-25 02:35:28 UTC [26/32 PASS, 6 WARN, all_passed: false] vs Current Cycle: 2026-10-25 02:39:27 UTC)`\n
`[ALERT] TELEMETRY STALE WARNING: Data/macro_calendar.json & Data/forex_factory_live.json are stale (Last updated: 2026-10-25 02:05:34.96 UTC [33.87m > 15.0m gate] & 2026-10-24 17:58:00 UTC [521.45m / 8.69h] vs Current Cycle: 2026-10-25 02:39:27 UTC)`\n\n---\n\n## 🧠 UNIVERSAL METACOGNITIVE INQUEST & SKILLS-GAP AUDIT\n\n\n### Mandatory Question Evaluation: "If it use all the available skills related will it improve our response?"\n\n\n**Explicit Answer: YES — unconditionally and measurably.** Deploying all nine loaded quantitative skills alongside repository-level forensic, microstructure, and risk-management toolkits transforms this deliberation from a single-line fail-closed abort into an institutional-grade 360° quantitative audit:\n\n1. **Cryptographic & Causality Root-Cause Proof (`@[systematic-debugging]`, `@[clean-code]`)**:
\n- By auditing `Data/cycle_envelope.json`, `Data/execution_preflight_receipt.json`, and the dispatcher code (`Terminal/generate_cycle_envelope.py`, `Terminal/execution_preflight.py`, and `Terminal/dispatch_dual_council.py`) against provenance commit `0bf033cbcdcc468ab4a4a4f94ac5eed3dbf1fdf7` (`2026-10-25T02:37:55Z`, `[as_of 2026-10-25 02:37:38 UTC]`), we proved **two exact pipeline defects**:
\n1. **Post-Cutoff Execution Order Inversion**: `Terminal/generate_cycle_envelope.py` froze `cutoff_utc` at `2026-10-25 02:39:18 UTC` (`Cycle-20261025T023918Z`) **before** `Terminal/execution_preflight.py` sampled MT5 at `tick_time_utc: 2026-10-25 02:39:31 UTC` and `observed_at_utc: 2026-10-25 02:39:32 UTC` (`+13.0s` and `+14.0s` **after** `cutoff_utc`, and `+4.0s`/`+5.0s` after the §1.4 item 6 reference clock `2026-10-25 02:39:27 UTC`).\n2. **Post-Signature Nonce Mutation**: `Terminal/execution_preflight.py` ran with `dispatch_nonce=""` (default CLI argument), computing `receipt_sha256 = "6045e28ce734236c25d90d05294ab40975731314c24cd58fb45515110b57417e"` over `json.dumps(receipt, sort_keys=True, indent=2)`. Subsequently, `Terminal/dispatch_dual_council.py` (lines 136–139) overwrote `rec_obj["dispatch_nonce"] = "050944d8-c50d-494b-8560-0faaa7bb2320"` in-place **without recomputing `receipt_sha256`**, changing the serialized `indent=2` SHA-256 of the receipt payload to `0598d7fb23e33739a61ff4145a65c08036302de47f9eba61d5d0a86bdb830682` (and compact canonical SHA-256 to `a8b90df00b803c5deffa89be513fa195255a8b774334bc1bd620645e3ffed394`).\n\n\n2. **Dynamic Spread & Solvency Tier Reconciliation (`@[trader-risk]`, `@[market-ingest]`)**:
\n- Cross-checking `00_MT5_Account_Telemetry` (`02:07:27 UTC`), `20_Auction_Market_Structure` (`02:18:32 UTC`), and `docs/telemetry/live_snapshot_latest.json` (`02:37:38 UTC`) caught **`SOLUSD.p` crossing the `25.0 bps` hard spread gate** (`22.45 bps` PASS at `02:07:27 UTC` →\to→ `29.41 bps` FAIL at `02:18:32 UTC` →\to→ `25.42 bps` FAIL at `02:37:38 UTC`), while also catching `BTCUSD.pi` widening from `1.98 bps` (`$16.00`) at `02:37:38 UTC` to `2.72 bps` (`$22.00`) in the `02:39:31 UTC` preflight receipt (increasing exit spread cost on `0.04` lot from `$0.64` to `$0.88` and stressed loss from `$26.80` to `$27.10`).\n- Reconciling the preflight receipt (`0.04` lot `BTCUSD.pi`, `base_nominal_risk_usd = $19.20`, `total_nominal_risk_usd = $20.08`) against `cycle_envelope.json` (`Balance = $4,846.32 <= $4,850.00`, `capital_mode = "TIER_1_STANDARD"`, `risk_min_usd = risk_max_usd = $12.00`) proves that `0.04` lot was sized for the operator baseline `TIER_2_HOUSE_MONEY` (`$15.00–$25.00`) and exceeds the reconciled `TIER_1_STANDARD` cap (`$12.00`) by `+$7.20` (`+$8.08` with exit spread), whereas rescoping to `0.02` lot @ `SL = $81,900.00` restores exact `$12.00` nominal risk.\n\n3. **Intraday Shelf Evolution & Re-Anchored Setup Engineering (`@[trader-signal]`, `@[market-pattern]`, `@[sharpe-ratio-non-iid-corrections]`, `@[time-series-decomposer]`)**:
\n- Between `01:52:46 UTC` and `02:37:38 UTC`, `ETHUSD.pi` pushed through its `0.786` invalidation shelf (`$2,361.92`) and `Asian_H` (`$2,361.90`) to `bid = $2,362.10 / ask = $2,365.00` (`mid = $2,363.55`, `Z_vwap = +3.31 SD`, `15m_delta = -$398,286.11`). Instead of leaving a stale limit order below spot at `$2,361.92`, we re-anchored `CAND_ETH_WALL_237400` at **`$2,374.00`**, directly front-running `pd_POC` (`$2,375.72`) and the **`$4,005,283.60` L3 ask wall at `$2,374.30`** (`Row 442` of `17_Orderbook`), defended overhead by `$6.84M` (`$2,383.00`), `$13.34M` (`$2,392.00`), and `$4.85M` (`$2,402.60`) L3 institutional ask walls.\n\n\n| Skill Identifier | Primary Persona | Concrete Mathematical & Empirical Application in `Cycle-20261025T023918Z` |\n| --- | --- | --- |\n| `@[trader-signal]` | Role A | Computed VR(4)VR(4)VR(4), z∗z^*z∗, ER(48)ER(48)ER(48), tNWt_{\text{NW}}tNW​, bOUb_{\text{OU}}bOU​, θOU\theta_{\text{OU}}θOU​, and Fib-Prime EMAs (`5, 13, 34, 89, 144, 233`) across `15m`/`1h`/`4h` bars at `02:37:38 UTC` (last closed 15m bar `02:30 UTC`). |\n| `@[sharpe-ratio-non-iid-corrections]` | Role A | Applied Lo-MacKinlay heteroskedastic kernel ϕ^(4)\hat{\phi}(4)ϕ^​(4) and Bartlett HAC lag L=4L=4L=4 (T=100T=100T=100) / L=3L=3L=3 (T=96T=96T=96) across all 14 crypto perpetuals. |\n| `@[time-series-decomposer]` | Role A | Separated HTF bearish secular drift (1h tNW∈[−15.28,−3.43]1\text{h } t_{\text{NW}} \in [-15.28, -3.43]1h tNW​∈[−15.28,−3.43]) from the `01:15–02:37 UTC` Asian session short-squeeze extension (Zvwap=+3.31 SDZ_{\text{vwap}} = +3.31\text{ SD}Zvwap​=+3.31 SD on `ETH`, +2.99 SD+2.99\text{ SD}+2.99 SD on `XRP`, +2.06 SD+2.06\text{ SD}+2.06 SD on `BNB`, +1.67 SD+1.67\text{ SD}+1.67 SD on `BTC`). |\n| `@[market-ingest]` | Role B | Parsed all 35 worksheets directly from `Data/DataBase_Trading.xlsx` (`sha256: 9394137d...6ce6`), reconciling `00_MT5_Account_Telemetry` (`02:07:27 UTC`), `10_Whale_Orders` (`02:00:26 UTC`), `17_Orderbook` (`02:16:41 UTC`), `18_CVD` (`02:17:47 UTC`), `20_Auction_Market_Structure` (`02:18:32 UTC`), `21_Tradfye_Orderflow` (`01:45:03 UTC`), and `22_Forced_Liquidations_MTF` (`00:59:55 UTC`). |\n| `@[market-pattern]` | Role B | Identified `ETHUSD.pi`'s `+3.31 SD` VWAP extension (`-$398.3k` 15m delta divergence) above `Asian_H` (`$2,361.90`) and `BTCUSD.pi`'s sweep of `Asian_H` (`$80,879.00`) at `02:39:31 UTC` (`ask = $80,887.00`, `-$364.7k` 15m delta). |\n| `@[trader-risk]` | Role C | Verified `$4,846.32` balance/equity, `$49.32` realized headroom above `$4,795.00` Solvency Kernel, Finding D3 50% margin collateralization (`$1,626.00` = `33.55%` equity, `298.05%` margin level), and `TIER_1_STANDARD` (`$12.00`) vs `TIER_2_HOUSE_MONEY` (`$19.20`) lot rescoping. |\n| `@[adaptive-wfo-epoch]` | Role A / Part 2 | Enforced the n≥100n \ge 100n≥100 closed-trade sample gate (`n = 17`, `11` wins, Clopper-Pearson 95% LCB `0.4197` uncalibrated   ⟹  \implies⟹ `HOLD`). |\n| `@[clean-code]` & `@[systematic-debugging]` | Role D | Proved why `receipt_sha256` (`6045e28c...417e`) matched `dispatch_nonce=""` and why `Terminal/dispatch_dual_council.py` broke the signature while `execution_preflight.py` ran `+13s/+14s` after `cutoff_utc`. |\n\n\n---\n\n## 🏛️ PART 1: EXHAUSTIVE 4-PERSONA QUANTITATIVE AUDIT (§1 – §7)\n\n\n### §1. ROLE D: MARKET CLOCK, AUCTION & PROVENANCE AUDITOR (@[clean-code], @[systematic-debugging])\n\n\n#### 1.1 Cryptographic Provenance & Post-Cutoff / Post-Signature Mutation Forensics\n\n\nWe audited the embedded `cycle_envelope.json` (`Cycle-20261025T023918Z`, `uuid: c78b9a5d-dee4-4ca8-91c3-cc95e69fdd06`, `dispatch_nonce: 050944d8-c50d-494b-8560-0faaa7bb2320`, `cutoff_utc: 2026-10-25 02:39:18 UTC`) and `execution_preflight_receipt.json` against `origin/main` HEAD commit `0bf033cbcdcc468ab4a4a4f94ac5eed3dbf1fdf7` (`2026-10-25T02:37:55Z`, `[as_of 2026-10-25 02:37:38 UTC]`, tree `99d3628da7260b00ba334ebe035e83a8b2071a7a`):\n\n| Artifact / Parameter | Embedded Envelope / Receipt Value | Provenance Commit `0bf033cb` (`02:37:55 UTC`) | Verification Verdict |\n| --- | --- | --- | --- |\n| `provenance.git_commit` | `0bf033cbcdcc468ab4a4a4f94ac5eed3dbf1fdf7` | `0bf033cbcdcc468ab4a4a4f94ac5eed3dbf1fdf7` | **EXACT MATCH (`100%`)** |\n| `provenance.git_tree` | `99d3628da7260b00ba334ebe035e83a8b2071a7a` | `99d3628da7260b00ba334ebe035e83a8b2071a7a` | **EXACT MATCH (`100%`)** |\n| `Data/DataBase_Trading.xlsx` SHA-256 | `9394137d72672a3eda14cabfc2efa91700eec0f45e933271919e8281a1c66ce6` | `9394137d72672a3eda14cabfc2efa91700eec0f45e933271919e8281a1c66ce6` (`5,699,459` B, 35 sheets) | **EXACT MATCH (`100%`)** |\n| `Data/history/master_manifest.json` SHA-256 | `76557d2de9635ef40671648d17d1b4a0166bd768d5ba3d62df11fed2a1f0ec15` | `76557d2de9635ef40671648d17d1b4a0166bd768d5ba3d62df11fed2a1f0ec15` (`344,294` B) | **EXACT MATCH (`100%`)** |\n| `risk_policy_sha256` | `f4805622f9a19e213361bbbffeb7fc2228bc9ffba86bcb49f22aa9ad86ae9529` | `f4805622f9a19e213361bbbffeb7fc2228bc9ffba86bcb49f22aa9ad86ae9529` | **EXACT MATCH (`100%`)** |\n| `excel_freshness_verified` / `scorecard_fresh` | `false` / `false` | `false` / `false` (`26/32 PASS`, `6 WARN` at `02:35:28 UTC`) | **FAIL-CLOSED (`false`)** |\n| `execution_preflight_receipt.json` Timestamps | `tick_time_utc: 02:39:31 UTC`, `observed_at_utc: 02:39:32 UTC` | Prior receipt (`01:53:43 UTC`, nonce `50f58804...`) | **FAIL (`+13.0s`/`+14.0s` POST-CUTOFF)** |\n| `execution_preflight_receipt.json` `receipt_sha256` | `6045e28ce734236c25d90d05294ab40975731314c24cd58fb45515110b57417e` | Signed over `dispatch_nonce: ""` (`indent=2`) | **FAIL (NONCE MUTATED POST-SIGNING)** |\n\n\n**Forensic Proof of Dual Defect (`DIS-344-01`)**:\n\n1. **Violation of Physical Cutoff Causality (§1.4 item 1)**:\n
tick_time_utc (02:39:31 UTC)−cutoff_utc (02:39:18 UTC)=+13.0 s>0\text{tick\_time\_utc } (02\text{:}39\text{:}31\text{ UTC}) - \text{cutoff\_utc } (02\text{:}39\text{:}18\text{ UTC}) = +13.0\text{ s} > 0tick_time_utc (02:39:31 UTC)−cutoff_utc (02:39:18 UTC)=+13.0 s>0\n
observed_at_utc (02:39:32 UTC)−cutoff_utc (02:39:18 UTC)=+14.0 s>0\text{observed\_at\_utc } (02\text{:}39\text{:}32\text{ UTC}) - \text{cutoff\_utc } (02\text{:}39\text{:}18\text{ UTC}) = +14.0\text{ s} > 0observed_at_utc (02:39:32 UTC)−cutoff_utc (02:39:18 UTC)=+14.0 s>0\n
Against the §1.4 item 6 reference cycle clock (`2026-10-25 02:39:27 UTC`), `tick_time_utc` is **`+4.0s`** and `observed_at_utc` is **`+5.0s` in the future** because `Terminal/generate_cycle_envelope.py` ran at `02:39:18 UTC`, `Terminal/dispatch_dual_council.py` initialized `utc_now` at `02:39:27 UTC`, and `Terminal/execution_preflight.py` finished at `02:39:32 UTC`.\n2. **Cryptographic Signature Break via In-Place Nonce Injection**:
\n- When `dispatch_nonce` is set to `""` in the embedded `execution_preflight_receipt.json` payload, `hashlib.sha256(json.dumps(receipt_empty_nonce, sort_keys=True, indent=2).encode("utf-8")).hexdigest()` equals **`6045e28ce734236c25d90d05294ab40975731314c24cd58fb45515110b57417e`** (exact match to the embedded `receipt_sha256`).\n- `Terminal/dispatch_dual_council.py` (lines 136–139) then mutated `rec_obj["dispatch_nonce"] = "050944d8-c50d-494b-8560-0faaa7bb2320"` in-place **without recomputing `receipt_sha256`**, changing the post-mutation `indent=2` SHA-256 to `0598d7fb23e33739a61ff4145a65c08036302de47f9eba61d5d0a86bdb830682` (and compact canonical SHA-256 to `a8b90df00b803c5deffa89be513fa195255a8b774334bc1bd620645e3ffed394`).\n\n\n#### 1.2 Comprehensive 35-Worksheet Timestamp & Staleness Audit (Data/DataBase_Trading.xlsx)\n\n\nWe inspected all 35 worksheets inside `Data/DataBase_Trading.xlsx` (`sha256: 9394137d72672a3eda14cabfc2efa91700eec0f45e933271919e8281a1c66ce6`) from commit `0bf033cbcdcc468ab4a4a4f94ac5eed3dbf1fdf7` (`02:37:55 UTC`) and measured every sheet's age against both `cutoff_utc` (`2026-10-25 02:39:18 UTC`) and the §1.4 item 6 reference clock (`2026-10-25 02:39:27 UTC`):\n\n| # | Worksheet Name | Rows | Last Updated (IST) | Last Updated (UTC) | Age vs `02:39:18Z` | Age vs `02:39:27Z` | Checklist (`02:35:28Z`) | Freshness Status (`<= 20m`) |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| 1 | `00_MT5_Account_Telemetry` | 170 | `2026-10-25 07:37:27 IST` | `2026-10-25 02:07:27 UTC` | `31.85m` | `32.00m` | PASS | **STALE (`32.00m > 20m`)** |\n| 2 | `Crypto_ETF_Flows` *(Aux)* | 13,764 | Daily table (`2026-10-23`) | `2026-10-23 00:00:00 UTC` | Aux | Aux | N/A | Auxiliary Historical Table |\n| 3 | `Top_Institutions` *(Aux)* | 2,128 | Daily table | Static | Aux | Aux | N/A | Auxiliary Historical Table |\n| 4 | `ETF_Market_Overview` *(Aux)* | 1,607 | Daily table | Static | Aux | Aux | N/A | Auxiliary Historical Table |\n| 5 | `1_Crypto_ETF_Flows` | 41 | `2026-10-25 07:51:05 IST` | `2026-10-25 02:21:05 UTC` | `18.22m` | `18.37m` | PASS | **FRESH (`<= 20m`)** |\n| 6 | `2_Spot_Netflow_S` | 202 | `2026-10-25 07:52:25 IST` | `2026-10-25 02:22:25 UTC` | `16.88m` | `17.03m` | PASS | **FRESH (`<= 20m`)** |\n| 7 | `3_Exchanges_LS_Ratio_15M` | 416 | `2026-10-25 07:18:49 IST` | `2026-10-25 01:48:49 UTC` | `50.48m` | `50.63m` | WARN | **STALE (`50.63m > 20m`)** |\n| 8 | `3_Exchanges_LS_Ratio_1H` | 416 | `2026-10-25 07:55:47 IST` | `2026-10-25 02:25:47 UTC` | `13.52m` | `13.67m` | PASS | **FRESH (`<= 20m`)** |\n| 9 | `3_Exchanges_LS_Ratio_4H` | 350 | `2026-10-25 07:57:10 IST` | `2026-10-25 02:27:10 UTC` | `12.13m` | `12.28m` | PASS | **FRESH (`<= 20m`)** |\n| 10 | `4_Hyperliquid_Analysis` | 502 | `2026-10-25 07:38:12 IST` | `2026-10-25 02:08:12 UTC` | `31.10m` | `31.25m` | PASS | **STALE (`31.25m > 20m`)** |\n| 11 | `5_OI` | 372 | `2026-10-25 07:39:53 IST` | `2026-10-25 02:09:53 UTC` | `29.42m` | `29.57m` | PASS | **STALE (`29.57m > 20m`)** |\n| 12 | `22_Forced_Liquidations_MTF` | 1,002 | `2026-10-25 06:29:55 IST` | `2026-10-25 00:59:55 UTC` | `99.38m` | `99.53m` | WARN | **STALE (`99.53m > 20m`)** |\n| 13 | `5_Funding_Rate` | 203 | `2026-10-25 07:40:34 IST` | `2026-10-25 02:10:34 UTC` | `28.73m` | `28.88m` | PASS | **STALE (`28.88m > 20m`)** |\n| 14 | `9_Liquidation_Max_Pain_24H` | 748 | `2026-10-25 08:02:24 IST` | `2026-10-25 02:32:24 UTC` | `6.90m` | `7.05m` | PASS | **FRESH (`<= 20m`)** |\n| 15 | `9_Liquidation_Max_Pain_48H` | 748 | `2026-10-25 08:03:00 IST` | `2026-10-25 02:33:00 UTC` | `6.30m` | `6.45m` | PASS | **FRESH (`<= 20m`)** |\n| 16 | `9_Liquidation_Max_Pain_3D` | 748 | `2026-10-25 08:03:37 IST` | `2026-10-25 02:33:37 UTC` | `5.68m` | `5.83m` | PASS | **FRESH (`<= 20m`)** |\n| 17 | `9_Liquidation_Max_Pain_7D` | 748 | `2026-10-25 07:29:37 IST` | `2026-10-25 01:59:37 UTC` | `39.68m` | `39.83m` | WARN | **STALE (`39.83m > 20m`)** |\n| 18 | `6_Funding_Fee_Settlement` | 502 | `2026-10-25 07:41:13 IST` | `2026-10-25 02:11:13 UTC` | `28.08m` | `28.23m` | PASS | **STALE (`28.23m > 20m`)** |\n| 19 | `10_Whale_Orders` | 176 | `2026-10-25 07:30:26 IST` | `2026-10-25 02:00:26 UTC` | `38.87m` | `39.02m` | WARN | **STALE (`39.02m > 20m`)** |\n| 20 | `11_Technical` | 224 | `2026-10-25 07:41:52 IST` | `2026-10-25 02:11:52 UTC` | `27.43m` | `27.58m` | PASS | **STALE (`27.58m > 20m`)** |\n| 21 | `12_Hyperdash` | 511 | `2026-10-25 07:42:53 IST` | `2026-10-25 02:12:53 UTC` | `26.42m` | `26.57m` | PASS | **STALE (`26.57m > 20m`)** |\n| 22 | `13_Hyperliquid` | 473 | `2026-10-25 07:43:44 IST` | `2026-10-25 02:13:44 UTC` | `25.57m` | `25.72m` | PASS | **STALE (`25.72m > 20m`)** |\n| 23 | `7_Liq_Heapmap` | 91 | `2026-10-25 07:57:54 IST` | `2026-10-25 02:27:54 UTC` | `11.40m` | `11.55m` | PASS | **FRESH (`<= 20m`)** |\n| 24 | `7_Live_Liq` | 1,003 | `2026-10-25 07:59:19 IST` | `2026-10-25 02:29:19 UTC` | `9.98m` | `10.13m` | PASS | **FRESH (`<= 20m`)** |\n| 25 | `8_Exchange_Liquidation_Map_1D` | 2,323 | `2026-10-25 08:00:33 IST` | `2026-10-25 02:30:33 UTC` | `8.75m` | `8.90m` | PASS | **FRESH (`<= 20m`)** |\n| 26 | `8_Exchange_Liquidation_Map_7D` | 2,489 | `2026-10-25 08:01:49 IST` | `2026-10-25 02:31:49 UTC` | `7.48m` | `7.63m` | PASS | **FRESH (`<= 20m`)** |\n| 27 | `14_Hyperdash_Liq_Map` | 5,862 | `2026-10-25 07:44:27 IST` | `2026-10-25 02:14:27 UTC` | `24.85m` | `25.00m` | PASS | **STALE (`25.00m > 20m`)** |\n| 28 | `15_Hyperdash_Stops_Map` | 3,748 | `2026-10-25 07:10:17 IST` | `2026-10-25 01:40:17 UTC` | `59.02m` | `59.17m` | WARN | **STALE (`59.17m > 20m`)** |\n| 29 | `16_Hyperdash_telegram_Intel` | 1,002 | `2026-10-25 07:45:35 IST` | `2026-10-25 02:15:35 UTC` | `23.72m` | `23.87m` | PASS | **STALE (`23.87m > 20m`)** |\n| 30 | `17_Orderbook` | 5,427 | `2026-10-25 07:46:41 IST` | `2026-10-25 02:16:41 UTC` | `22.62m` | `22.77m` | PASS | **STALE (`22.77m > 20m`)** |\n| 31 | `18_CVD` | 1,502 | `2026-10-25 07:47:47 IST` | `2026-10-25 02:17:47 UTC` | `21.52m` | `21.67m` | PASS | **STALE (`21.67m > 20m`)** |\n| 32 | `19_News` | 38 | `2026-10-25 08:04:43 IST` | `2026-10-25 02:34:43 UTC` | `4.58m` | `4.73m` | PASS | **FRESH (`<= 20m`)** |\n| 33 | `20_Auction_Market_Structure` | 173 | `2026-10-25 07:48:32 IST` | `2026-10-25 02:18:32 UTC` | `20.77m` | `20.92m` | PASS | **STALE (`20.92m > 20m`)** |\n| 34 | `19_Calendar` | 46 | `2026-10-25 08:05:16 IST` | `2026-10-25 02:35:16 UTC` | `4.03m` | `4.18m` | PASS | **FRESH (`<= 20m`)** |\n| 35 | `21_Tradfye_Orderflow` | 6,914 | `2026-10-25 07:15:03 IST` | `2026-10-25 01:45:03 UTC` | `54.25m` | `54.40m` | WARN | **STALE (`54.40m > 20m`)** |\n\n\n**Diagnostic Feedback for Operator & Antigravity**:\n\n1. **Staggered Excel Daemon Sweep**: Between `02:07 UTC` and `02:35 UTC`, the Excel writer refreshed two partial batches (`00_MT5_Account_Telemetry` through `20_Auction_Market_Structure` between `02:07:27 UTC` and `02:18:32 UTC`, followed by `1_Crypto_ETF_Flows` through `19_Calendar` between `02:21:05 UTC` and `02:35:16 UTC`), but **skipped `21_Tradfye_Orderflow` (`01:45:03 UTC`, `54.40m` old), `22_Forced_Liquidations_MTF` (`00:59:55 UTC`, `99.53m` old), `15_Hyperdash_Stops_Map` (`01:40:17 UTC`, `59.17m` old), `3_Exchanges_LS_Ratio_15M` (`01:48:49 UTC`, `50.63m` old), `9_Liquidation_Max_Pain_7D` (`01:59:37 UTC`, `39.83m` old), and `10_Whale_Orders` (`02:00:26 UTC`, `39.02m` old)**. Consequently, `Data/excel_all_sheets_checklist.json` (`02:35:28 UTC`) reported `26/32 PASS`, `6 WARN`, and `all_passed: false`.\n2. **Stale Calendar Artifacts**: `Data/macro_calendar.json` (`verified_at: 2026-10-25T02:05:34.955592+00:00`) is `2,032.04s` (`33.87m`) old vs `02:39:27 UTC` (violating the `< 900s` gate in §1.4 item 2), and `Data/forex_factory_live.json` (`2026-10-24 17:58:00 UTC`) is `31,287.0s` (`8.69h`) old.\n\n#### 1.3 Session & 156-Asset Universe Classification (Highlighting SOLUSD.p Spread Widening)\n\n\n- **98 TradFi Assets**: Weekend halt until Sunday `21:00 UTC`   ⟹  \implies⟹ `CLOSED / WATCHLIST_ONLY`.\n- **58 Crypto Perpetuals**: Open 24/7/365 (`SYMBOL_TRADE_MODE_FULL = 4`), rollover embargo inactive.\n- **Broker Spread Gate (`<= 25.0 bps`) Reconciliation (`DIS-344-04`)**:
\n- In `docs/telemetry/live_snapshot_latest.json` (`02:37:38 UTC`) and `20_Auction_Market_Structure` (`02:18:32 UTC`), **only 5 of the 14 tracked crypto perpetuals in `live_snapshot_latest.json` pass `<= 25.0 bps`**:
\n1. `BTCUSD.pi` (`1.98 bps` at `02:37:38 UTC`; `2.72 bps` at `02:39:31 UTC` preflight),\n2. `BNBUSD.p` (`9.42 bps` at `02:37:38 UTC`),\n3. `ETHUSD.pi` (`12.27 bps` at `02:37:38 UTC`),\n4. `BCHUSD.p` (`20.93 bps` at `02:37:38 UTC`),\n5. `XRPUSD.pi` (`22.93 bps` at `02:37:38 UTC`).\n\n- **`SOLUSD.p` Spread Gate Disqualification**: While `SOLUSD.p` passed at `02:07:27 UTC` (`22.45 bps` in `00_MT5_Account_Telemetry`), its spread widened to **`29.41 bps`** in `20_Auction_Market_Structure` (`02:18:32 UTC`) and **`25.42 bps`** (`bid = $102.15`, `ask = $102.41`, `spread_raw = $0.26`) in `live_snapshot_latest.json` (`02:37:38 UTC`), exceeding the `<= 25.0 bps` gate by `+0.42 bps`. The remaining 8 tracked crypto perpetuals in `live_snapshot_latest.json` also fail `<= 25.0 bps` (`TRXUSD.p` `27.35 bps`, `AVXUSD.p` `33.43 bps`, `LTCUSD.pi` `52.58 bps`, `NERUSD.p` `66.90 bps`, `LNKUSD.p` `72.48 bps`, `ADAUSD.p` `101.03 bps`, `DOTUSD.pi` `191.75 bps`, `DOGUSD.p` `270.10 bps`).\n\n\n---\n\n### §2. ROLE A: STATISTICAL REGIME, DIFFUSION & DUAL-ENGINE DIALECTIC QUANT (@[trader-signal], @[sharpe-ratio-non-iid-corrections], @[time-series-decomposer])\n\n\nWe computed exact Lo-MacKinlay heteroskedasticity-consistent variance ratios VR(q=4)VR(q=4)VR(q=4) and z∗z^*z∗, Kaufman Efficiency Ratios ER(48)ER(48)ER(48), Newey-West HAC log-price drift ttt-statistics (L=4L=4L=4 for T=100T=100T=100, L=3L=3L=3 for T=96T=96T=96), discrete Ornstein-Uhlenbeck parameters (bOU,θOUb_{\text{OU}}, \theta_{\text{OU}}bOU​,θOU​), `ATR(14)`, and Fibonacci Prime EMA Ribbons (`5, 13, 34, 89, 144, 233`) across all 14 crypto perpetuals in `docs/telemetry/live_snapshot_latest.json` (`02:37:38 UTC`, last closed 15m bar `02:30 UTC`):\n\n| Asset (`Broker Symbol`) | 15m Close (`ATR14`) | 15m VR(4)VR(4)VR(4) (z∗z^*z∗) | 15m ER(48)ER(48)ER(48) | 15m tNWt_{\text{NW}}tNW​ | 1h VR(4)VR(4)VR(4) (z∗z^*z∗) / ER(48)ER(48)ER(48) / tNWt_{\text{NW}}tNW​ | 4h VR(4)VR(4)VR(4) (z∗z^*z∗) / ER(48)ER(48)ER(48) / tNWt_{\text{NW}}tNW​ | OU bOUb_{\text{OU}}bOU​ / θOU\theta_{\text{OU}}θOU​ (`15m`) | 15m Fib-Prime EMA Ribbon (`5 / 13 / 34 / 89 / 144 / 233`) | Regime & Dialectic Classification |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| `BTC` (`BTCUSD.pi`) | `80,735.00` (`166.37`) | `1.1714` (`+0.5598`) | `0.1357` | `-1.9241` | `1.0902` (`+0.4183`) / `0.0534` / `-8.1949` | `0.9206` (`-0.3111`) / `0.0406` / `-3.2062` | `-0.0558` / **`80,477.60`** | `80735.9 > 80677.8 > 80528.4 > 80481.2 < 80520.5 < 80571.8` | **HTF Bearish Drift / 15m Rotational Squeeze** (`Z_vwap=+1.67`, `ER48=0.1357 < 0.15`) |\n| `ETH` (`ETHUSD.pi`) | `2,359.90` (`5.8985`) | `1.4169` (`+1.0621`) | `0.0819` | `-4.3003` | `1.0528` (`+0.2220`) / `0.0742` / `-8.7352` | `0.7804` (`-0.8294`) / `0.0805` / `-7.0658` | `-0.0307` / **`2,347.17`** | `2357.79 > 2353.33 > 2345.73 < 2348.28 < 2353.55 < 2358.99` | **Extreme VWAP Extension (`Z_vwap=+3.31 SD`, `15m_delta=-$398.3k`)** |\n| `BNB` (`BNBUSD.p`) | `742.20` (`1.6169`) | `1.3683` (`+1.3866`) | `0.2965` | `-0.8450` | `1.3355` (`+1.6201`) / `0.1260` / `-3.4262` | `0.7495` (`-0.9154`) / `0.1162` / `-2.2189` | `-0.0072` / **`739.66`** | `741.64 > 739.64 > 735.44 > 733.28 < 733.66 < 734.42` | **15m Trend Expansion (`ER48=0.2965`, `Z_vwap=+2.06 SD`)** |\n| `BCH` (`BCHUSD.p`) | `276.86` (`1.0094`) | `1.0972` (`+0.3828`) | `0.0800` | `-2.1324` | `1.0034` (`+0.0133`) / `0.0213` / `-5.3881` | `0.8991` (`-0.4062`) / `0.0007` / `+1.1179` | `-0.0677` / **`275.11`** | `276.92 > 276.56 > 275.59 > 275.51 < 276.04 < 276.68` | **Rotational Balance Below `Asian_H` (`$278.26`)** |\n| `XRP` (`XRPUSD.pi`) | `1.3040` (`0.0047`) | `1.0304` (`+0.1158`) | `0.2650` | `+1.1929` | `1.2743` (`+1.8678`) / `0.0249` / `-7.2116` | `0.8967` (`-0.4261`) / `0.0022` / `-7.2226` | `-0.0211` / **`1.2932`** | `1.3026 > 1.2992 > 1.2923 > 1.2862 > 1.2849 > 1.2843` | **1h Super-Diffusive (`z*=1.8678`), Extreme `Z_vwap=+2.99 SD`** |\n| `SOL` (`SOLUSD.p`) | `102.11` (`0.3127`) | `1.1891` (`+0.6612`) | `0.1871` | `-1.7485` | `1.0674` (`+0.3448`) / `0.0995` / `-9.6512` | `0.6600` (`-1.0662`) / `0.0517` / `-7.0604` | `-0.0351` / **`101.34`** | `102.12 > 101.98 > 101.55 > 101.40 < 101.52 < 101.68` | **Disqualified by Spread (`25.42 bps > 25.0 bps` at `02:37:38Z`)** |\n| `TRX` (`TRXUSD.p`) | `0.3286` (`0.0002`) | `1.0938` (`+0.4753`) | `0.0943` | `-9.0730` | `1.1655` (`+0.9468`) / `0.0492` / `-5.9297` | `0.8591` (`-0.5652`) / `0.2287` / `-0.9455` | `-0.0504` / `0.3288` | `0.3286 = 0.3286 = 0.3286 < 0.3288 < 0.3290 < 0.3291` | Disqualified by Spread (`27.35 bps > 25.0 bps`) |\n| `AVAX` (`AVXUSD.p`) | `8.9400` (`0.0275`) | `1.0692` (`+0.2685`) | `0.1702` | `-1.8122` | `1.0038` (`+0.0157`) / `0.0583` / `-12.2087` | `0.8082` (`-0.6469`) / `0.2120` / `-10.0211` | `-0.0474` / `8.8941` | `8.962 > 8.958 > 8.924 > 8.917 < 8.933 < 8.954` | Disqualified by Spread (`33.43 bps > 25.0 bps`) |\n| `LTC` (`LTCUSD.pi`) | `56.905` (`0.1480`) | `0.8634` (`-0.6077`) | `0.2517` | `-0.8341` | `1.1446` (`+0.6914`) / `0.1603` / `-15.2764` | `0.9622` (`-0.1439`) / `0.0981` / `-7.5841` | `-0.0360` / `56.4106` | `56.916 > 56.835 > 56.609 > 56.478 < 56.525 < 56.606` | Disqualified by Spread (`52.58 bps > 25.0 bps`) |\n| `NEAR` (`NERUSD.p`) | `4.4570` (`0.0267`) | `0.9214` (`-0.3454`) | `0.1404` | `-4.7309` | `0.8527` (`-0.6559`) / `0.2113` / `-9.7120` | `1.0340` (`+0.1513`) / `0.1380` / `-2.5036` | `-0.0369` / `4.4505` | `4.469 < 4.471 > 4.460 < 4.479 < 4.505 < 4.532` | Disqualified by Spread (`66.90 bps > 25.0 bps`) |\n| `LINK` (`LNKUSD.p`) | `11.543` (`0.0322`) | `1.1785` (`+0.5543`) | `0.0746` | `-4.4039` | `1.0191` (`+0.0870`) / `0.1459` / `-10.1147` | `0.8228` (`-0.6514`) / `0.1236` / `-8.5817` | `-0.0297` / `11.4942` | `11.551 > 11.546 > 11.520 < 11.547 < 11.589 < 11.633` | Disqualified by Spread (`72.48 bps > 25.0 bps`) |\n| `ADA` (`ADAUSD.p`) | `0.2068` (`0.0007`) | `1.1419` (`+0.4480`) | `0.1184` | `-3.6179` | `1.0696` (`+0.3237`) / `0.0760` / `-12.6228` | `0.8837` (`-0.4472`) / `0.1584` / `-9.8549` | `-0.0348` / `0.2057` | `0.2072 > 0.2069 > 0.2061 < 0.2063 < 0.2070 < 0.2077` | Disqualified by Spread (`101.03 bps > 25.0 bps`) |\n| `DOT` (`DOTUSD.pi`) | `1.0330` (`0.0045`) | `1.0535` (`+0.2326`) | `0.0385` | `-6.4470` | `1.2145` (`+1.0304`) / `0.2558` / `-8.7540` | `0.8149` (`-0.8453`) / `0.1396` / `-5.3141` | `-0.0232` / `1.0305` | `1.0377 > 1.0374 > 1.0351 < 1.0416 < 1.0478 < 1.0538` | Disqualified by Spread (`191.75 bps > 25.0 bps`) |\n| `DOGE` (`DOGUSD.p`) | `0.0767` (`0.0002`) | `1.4088` (`+1.4755`) | `0.2459` | `-3.1287` | `1.0171` (`+0.0871`) / `0.0683` / `-10.4314` | `0.7870` (`-0.7338`) / `0.0760` / `-9.6195` | `-0.0309` / `0.0761` | `0.0767 > 0.0766 > 0.0763 = 0.0763 < 0.0766 < 0.0768` | Disqualified by Spread (`270.10 bps > 25.0 bps`) |\n\n\n---\n\n### §3. ROLE B: FILL, MICROSTRUCTURE & ORDER GEOMETRY QUANT (@[market-ingest], @[market-pattern])\n\n\n1. **Exhaustion & Negative Bar Delta at Session Extremes (`live_snapshot_latest.json` at `02:37:38 UTC` & `Sheet 20` at `02:18:32 UTC`)**:
\n- At `02:30 UTC` (`live_snapshot_latest.json`), as `ETHUSD.pi` extended to `Z_vwap = +3.31 SD` (`bid = $2,362.10`, `ask = $2,365.00`) and `BTCUSD.pi` extended to `Z_vwap = +1.67 SD` (`bid = $80,782.00` at `02:37:38 UTC` →\to→ `bid = $80,865.00 / ask = $80,887.00` at `02:39:31 UTC`, sweeping `Asian_H = $80,879.00`), the `02:30 UTC` 15m bar recorded **negative taker delta across `ETH`, `BTC`, `SOL`, and `BNB`**:
\n- `ETH`: `bar_delta_15m_usd = -$398,286.11` (`Z_vwap = +3.31 SD`),\n- `BTC`: `bar_delta_15m_usd = -$364,706.60` (`Z_vwap = +1.67 SD`),\n- `SOL`: `bar_delta_15m_usd = -$139,973.04` (`Z_vwap = +2.07 SD`),\n- `BNB`: `bar_delta_15m_usd = -$18,100.04` (`Z_vwap = +2.06 SD`).\n\n- Meanwhile, `Sheet 21_Tradfye_Orderflow` (`01:45:03 UTC`, `54.40m` stale) remains frozen at the `01:30:00 UTC` bar (`BTC` Deribit `MaxPain = $78,000`, `CallW = $95,000`, `PutW = $60,000`; `ETH` Deribit `MaxPain = $2,300`, `CallW = $3,200`, `PutW = $2,300`).\n\n2. **180-Second Whale Wall Persistence Audit (`Sheet 17_Orderbook` at `02:16:41 UTC` & `Sheet 10_Whale_Orders` at `02:00:26 UTC`)**:
\n- **Spoof Rejection in `Sheet 10_Whale_Orders` (`02:00:26 UTC`)**: Rows 3–6 and 13–17 (`$80,985.10–$81,038.10`) have `Order Duration` of `0s`, `16s`, `41s`, and `1m 09s` (`< 180s`) and are **rejected**. Only the multi-hour walls at **`$81,000.00`** (`OKX` `$4.50M` `9h 10m`, `Coinbase` `$4.36M` `18h 51m`, `OKX` `$2.95M` `19h 22m`, `Bybit` `$1.54M` `8h 24m`, `Binance` `$3.19M` `17h 06m`, plus `Bybit` `$2.43M` @ `$80,999.90` `6h 19m` = **`$18.97M` combined persistent resistance at `$81,000.00`**) pass the `>= 180s` persistence filter.\n- **Wallet-Attributed L3 Institutional Walls (`Sheet 17_Orderbook` at `02:16:41 UTC`)**:
\n- **`ETHUSD.pi`**: SELL walls at **`$2,374.30`** (`$4,005,283.60`, `1,686.93 ETH`, `Row 442`), **`$2,383.00`** (`$6,839,142.56`, `2,869.97 ETH`, `Row 437`), **`$2,392.00`** (`$13,337,298.53`, `5,575.79 ETH`, `Row 435`), and **`$2,402.60`** (`$4,850,040.20`, `2,018.66 ETH`, `Row 439`). BUY walls at `$2,349.50` (`$4.01M`), `$2,348.40` (`$6.74M`), `$2,328.00` (`$12.98M`), and `$2,321.70` (`$4.63M`).\n- **`BTCUSD.pi`**: SELL walls at **`$81,192.00`** (`$7,474,638.63`, `92.06 BTC`, `Row 48`), **`$81,414.00`** (`$14,695,354.01`, `180.50 BTC`, `Row 44`), **`$81,713.00`** (`$6,239,082.53`, `76.35 BTC`, `Row 53`), **`$81,999.00`** (`$7,097,375.07`, `86.55 BTC`, `Row 50`), and **`$82,352.00`** (`$8,227,501.74`, `99.91 BTC`, `Row 46`). BUY walls at `$80,639.00` (`$7.42M`), `$80,274.00` (`$14.49M`), `$79,965.00` (`$6.43M`), `$79,685.00` (`$7.07M`), and `$79,267.00` (`$7.66M`).\n- **`BNBUSD.p`**: SELL walls at **`$745.16`** (`$344,264.67`, `Row 1220`), **`$747.14`** (`$1,306,644.01`, `1,748.86 BNB`, `Row 1217`), and **`$748.90`** (`$134,948.04`, `Row 1223`).\n- **`XRPUSD.pi`**: SELL walls at **`$1.3100`** (`$2,002,652.49` + `$1,502,340.19`), **`$1.3200`** (`$2,762,035.81`, `2,096,581 XRP`, `Row 1531`), and **`$1.3300`** (`$5,397,835.03`, `4,068,311 XRP`, `Row 1529`).\n- **`SOLUSD.p`**: SELL walls at **`$102.83`** (`$2,813,155.27`, `Row 830`), **`$103.37`** (`$5,536,876.57`, `Row 828`), and **`$104.05`** (`$7,132,896.99`, `Row 826`).\n\n\n\n---\n\n### §4. ROLE C: SOLVENCY, PORTFOLIO & BROKER MATH SENTRY (@[trader-risk])\n\n\n#### 4.1 Account #5064568 Solvency & Tier-Mode Audit\n\n\n- **Account State**: `Balance = Equity = Margin_Free = $4,846.32`, `Margin_Used = $0.00`, `Active_Positions = 0`, `Pending_Orders = 0`.\n- **Triple-Floor Cushions**: Hard Floor (`$4,600.00`) cushion = `+$246.32`; Operating Buffer (`$4,650.00`) cushion = `+$196.32`; Solvency Kernel (`$4,795.00`) cushion = `+$51.32`; Net Realized Headroom Hnet=$4,846.32−$4,795.00−$2.00=+$49.32H_{\text{net}} = \$4,846.32 - \$4,795.00 - \$2.00 = +\$49.32Hnet​=$4,846.32−$4,795.00−$2.00=+$49.32; Post-Joint-Stress Equity = `$4,844.32`.\n- **Reconciled Envelope Tier vs Operator Baseline (`DIS-344-02`)**: Because `$4,846.32 <= $4,850.00` (`$3.68` below Tier 2 unlock), `cycle_envelope.json` enforces `"capital_mode": "TIER_1_STANDARD"` (`risk_min_usd = risk_max_usd = $12.00`).\n\n#### 4.2 Sub-Penny Verification of Embedded execution_preflight_receipt.json (02:39:32 UTC)\n\n\nFor `BTCUSD.pi` `SELL_LIMIT` `0.04` lot @ `$81,300.00`, `SL = $81,780.00`, `TP = $79,850.00` (`bid = $80,865.00`, `ask = $80,887.00`):\n\n1. **Quote & Spread Math**:\n
Mid=80,865.00+80,887.002=$80,876.00,Spreadraw=80,887.00−80,865.00=$22.00\text{Mid} = \frac{80,865.00 + 80,887.00}{2} = \$80,876.00, \quad \text{Spread}_{\text{raw}} = 80,887.00 - 80,865.00 = \$22.00Mid=280,865.00+80,887.00​=$80,876.00,Spreadraw​=80,887.00−80,865.00=$22.00\n
Spreadbps=22.0080,876.00×10,000=2.7202 bps→2.72 bps≤25.0 bps (PASS)\text{Spread}_{\text{bps}} = \frac{22.00}{80,876.00} \times 10,000 = 2.7202\text{ bps} \to 2.72\text{ bps} \le 25.0\text{ bps (PASS)}Spreadbps​=80,876.0022.00​×10,000=2.7202 bps→2.72 bps≤25.0 bps (PASS)\n
Exit Spread Cost (0.04 lot)=22.00×0.04×1.0=$0.88 (EXACT MATCH)\text{Exit Spread Cost (0.04 lot)} = 22.00 \times 0.04 \times 1.0 = \$0.88\text{ (EXACT MATCH)}Exit Spread Cost (0.04 lot)=22.00×0.04×1.0=$0.88 (EXACT MATCH)\n2. **Stop Loss, Take Profit & Stressed Loss Valuation (`0.04` Lot)**:\n
Profit at SL=(81,300.00−81,780.00)×0.04=−$19.20,Profit at TP=(81,300.00−79,850.00)×0.04=+$58.00 (3.0208R)\text{Profit at SL} = (81,300.00 - 81,780.00) \times 0.04 = -\$19.20, \quad \text{Profit at TP} = (81,300.00 - 79,850.00) \times 0.04 = +\$58.00\text{ (3.0208R)}Profit at SL=(81,300.00−81,780.00)×0.04=−$19.20,Profit at TP=(81,300.00−79,850.00)×0.04=+$58.00 (3.0208R)\n
Total Nominal Risk=19.20+0.88=$20.08\text{Total Nominal Risk} = 19.20 + 0.88 = \$20.08Total Nominal Risk=19.20+0.88=$20.08\n
Ticket Stress (Preflight Model)=1.25×(19.20+0.88)+2.00=25.10+2.00=$27.10 (EXACT MATCH)\text{Ticket Stress (Preflight Model)} = 1.25 \times (19.20 + 0.88) + 2.00 = 25.10 + 2.00 = \$27.10\text{ (EXACT MATCH)}Ticket Stress (Preflight Model)=1.25×(19.20+0.88)+2.00=25.10+2.00=$27.10 (EXACT MATCH)\n
*(Role C §1.3 item 4 formula: `1.25 * 19.20 + 0.88 + 2.00 = $26.88`; conservative preflight `$27.10` leaves `post_joint_stop_balance = $4,846.32 - $2.00 - $27.10 = $4,817.22 >= $4,795.00`, `+$22.22` Kernel cushion.)*\n3. **Finding D3 Margin Collateralization & Tier-1 Rescoping**:\n
Marginreq(0.04 lot)=0.04×81,300.00×0.50=$1,626.00 (33.55% equity≤50%, Margin Level=298.05%≥200.0%)\text{Margin}_{\text{req}}(0.04\text{ lot}) = 0.04 \times 81,300.00 \times 0.50 = \$1,626.00\text{ (33.55\% equity} \le 50\%\text{, Margin Level} = 298.05\% \ge 200.0\%\text{)}Marginreq​(0.04 lot)=0.04×81,300.00×0.50=$1,626.00 (33.55% equity≤50%, Margin Level=298.05%≥200.0%)
\n- **Tier-1 (`$12.00`) Rescoped Specification**: Sizing `0.02` lot with `SL = $81,900.00` (behind the `$81,713.00` `$6.24M` wall and front-running the `$81,999.00` `$7.10M` wall) yields exact `Nominal Risk = 600.00 * 0.02 = $12.00`, `Reward = $29.00` (`2.4167R`), `Spread Cost = $0.44`, `Stressed Loss = $17.55`, and `Margin_Req = $813.00` (`16.78%` equity, `596.10%` margin level).\n\n\n---\n\n### §5. AFFIRMATIVE 6-CANDIDATE DISCOVERY & STRUCTURAL GEOMETRY AUDIT\n\n\n| Rank | Candidate ID (`Symbol`) | Side & Type | Entry / SL / TP (`Lots`) | Nominal Risk / Reward (`R:R`) | Spread Cost / Stressed Loss | Margin Req (`Margin Level`) | Post-Stop Balance | Backing L3 Institutional Whale Walls (`Sheet 17` / `Sheet 10`) & Microstructure Confluence | Verdict |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| **1** | `CAND_ETH_WALL_237400` (`ETHUSD.pi`) | `SELL_LIMIT` | `2374.00` / `2418.44` / `2276.50` (`0.27` lot) | `$12.00` / `$26.33` (`2.1942R`) | `$0.78` (`12.27 bps`) / `$17.98` | `$320.49` (`1,512.16%`) | `$4,826.34` | **Re-anchored above `02:37Z` sweep (`$2,363.55`, `Z_vwap = +3.31 SD`, `15m_delta = -$398.3k`) to front-run `pd_POC` (`$2,375.72`) and `$4.01M` L3 ask wall (`$2,374.30`, `Row 442`)**. Defended by `$6.84M` (`$2,383.00`), `$13.34M` (`$2,392.00`), and `$4.85M` (`$2,402.60`) L3 ask walls; SL `$2,418.44` clears `pdH` (`$2,400.30`) and `$2,402.60` wall. TP `$2,276.50` front-runs `CWL`/`pdL` (`$2,275.30`). | `HOLD` |\n| **2** | `CAND_BTC_PREFLIGHT_81300` (`BTCUSD.pi`) | `SELL_LIMIT` | `81300.00` / `81780.00` / `79850.00` (`0.04` lot; `0.02` lot @ `SL 81900` for Tier 1) | `$19.20` (`$12.00` Tier 1) / `$58.00` (`3.0208R`) | `$0.88` (`2.72 bps`) / `$27.10` (`$17.55` Tier 1) | `$1,626.00` (`298.05%`) | `$4,817.22` | **Front-runs `pdH` (`$81,405.00`) & `$14.70M` L3 ask wall (`180.50 BTC` @ `$81,414.00`, `Row 44`)** after `02:39:31Z` ask (`$80,887.00`) swept `Asian_H` (`$80,879.00`). Defended by `$6.24M` (`$81,713.00`) and `$7.10M` (`$81,999.00`) L3 walls; TP `$79,850.00` front-runs `$7.07M` L3 buy wall (`$79,685.00`) and `PWL` (`$79,634.00`). | `HOLD` |\n| **3** | `CAND_BNB_WALL_74700` (`BNBUSD.p`) | `SELL_LIMIT` | `747.00` / `759.00` / `722.50` (`1.00` lot) | `$12.00` / `$24.50` (`2.0417R`) | `$0.70` (`9.42 bps`) / `$17.88` | `$373.50` (`1,297.54%`) | `$4,826.44` | **Front-runs `$1.31M` L3 ask wall (`1,748.86 BNB` @ `$747.14`, `Row 1217`) below `PWH` (`$748.60`) and `CWH` (`$750.90`)** with `Z_vwap = +2.06 SD` and negative `02:30Z` delta (`-$18.1k`). TP `$722.50` front-runs `pd_VAL` (`$722.23`) and `0.786` shelf (`$722.30`). | `HOLD` |\n| **4** | `CAND_BCH_INV_27829` (`BCHUSD.p`) | `SELL_LIMIT` | `278.29` / `284.29` / `265.00` (`2.00` lots) | `$12.00` / `$26.58` (`2.2150R`) | `$1.16` (`20.93 bps`) / `$18.45` | `$278.29` (`1,741.46%`) | `$4,825.87` | **Anchored at `Asian_H` (`$278.26`) / prior `0.786` shelf (`$278.29`) below `Fib Swing High` (`$279.06`) and `pd_VAH` (`$280.00`)**, with SL `$284.29` behind `pdH` (`$283.50`) and `PWH` (`$283.96`). Disqualified by **absence of L3 whale walls** in `Sheet 17_Orderbook`. | `HOLD` |\n| **5** | `CAND_XRP_WALL_13180` (`XRPUSD.pi`) | `SELL_LIMIT` | `1.3180` / `1.3300` / `1.2870` (`1.00` lot, `cs=1000`) | `$12.00` / `$31.00` (`2.5833R`) | `$3.00` (`22.93 bps`) / `$20.75` | `$659.00` (`735.41%`) | `$4,823.57` | **Extreme VWAP extension (`Z_vwap = +2.99 SD`, `RSI14 = 70.83`) front-running `Mon_H` (`$1.3190`) and `$2.76M` L3 ask wall (`$1.3200`, `Row 1531`)**, with SL at `$5.40M` L3 wall (`$1.3300`, `Row 1529`) and TP at `d_VAL` (`$1.2871`) / `Mon_Mid` (`$1.2860`). | `HOLD` |\n| **6** | `CAND_SOL_WALL_10280_SPREAD_WIDENED` (`SOLUSD.p`) | `SELL_LIMIT` | `102.80` / `107.00` / `94.00` (`2.86` lots) | `$12.01` / `$25.17` (`2.0958R`) | `$0.74` (`25.42 bps`) / `$17.94` | `$147.00` (`3,296.82%`) | `$4,826.38` | **Anchored at `pd_VAH` (`$102.79`) + `$2.81M` L3 ask wall (`$102.83`, `Row 830`)**, backed by `$5.54M` (`$103.37`) and `$7.13M` (`$104.05`) L3 walls; **disqualified at `02:37:38 UTC` because spread widened to `25.42 bps > 25.0 bps` (`29.41 bps` in `Sheet 20`)**. | `HOLD` |\n\n\n---\n\n## 🏛️ PART 2: MATHEMATICAL SOFT RANKING & CALIBRATED UTILITY\n\n\nBecause closed-trade calibration sample size is n=17<100n = 17 < 100n=17<100 (`11` wins, Clopper-Pearson 95% LCB `0.4197`, `p_win_lower_bound_calibrated: false`), `p_fill`, `p_win_given_fill`, `ev_net_usd`, `ev_lcb_5pct_usd`, and `utility` are strictly set to `null` (`verdict = "HOLD"`). Below is the soft ranking across all 6 candidates by friction-inclusive breakeven probability PBE=(Lossnet+Spread)/(Gainnet+Lossnet+Spread)P_{\text{BE}} = (\text{Loss}_{\text{net}} + \text{Spread}) / (\text{Gain}_{\text{net}} + \text{Loss}_{\text{net}} + \text{Spread})PBE​=(Lossnet​+Spread)/(Gainnet​+Lossnet​+Spread), distance to Ornstein-Uhlenbeck equilibrium θOU\theta_{\text{OU}}θOU​, and L3 orderbook protection:\n\n| Soft Rank | Candidate ID (`Symbol`) | Gainnet\text{Gain}_{\text{net}}Gainnet​ (USD) | Lossnet+Spread\text{Loss}_{\text{net}} + \text{Spread}Lossnet​+Spread (USD) | Breakeven PBEP_{\text{BE}}PBE​ | Margin vs PLCB,95%P_{\text{LCB},95\%}PLCB,95%​ (`0.4197`) | Distance to θOU\theta_{\text{OU}}θOU​ (`ATR14` units) | 3h Tied-Up Capital-Minutes (`Margin_Req * 180m`) | Structural Confluence & Microstructure Edge |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| **1** | `CAND_ETH_WALL_237400` (`ETHUSD.pi`) | `$26.33` | `$12.00 + $0.78 = $12.78` | **`32.68%`** | **`+9.29%`** | `+$26.83` (`+4.55 ATR`) | `57,688.20 USD-min` | **Best Live Extreme & Wall Stack**: `Z_vwap = +3.31 SD` with negative `02:30Z` delta (`-$398.3k`), staged at `$2,374.00` in front of `pd_POC` (`$2,375.72`) and `$29.03M` of L3 ask walls (`$2,374.30–$2,402.60`), compliant with `TIER_1_STANDARD` (`$12.00` risk). |\n| **2** | `CAND_BTC_PREFLIGHT_81300` (`BTCUSD.pi`) | `$58.00` (`$29.00` Tier 1) | `$19.20 + $0.88 = $20.08` (`$12.44` Tier 1) | **`25.72%`** (`30.02%` Tier 1) | **`+16.25%`** (`+11.95%` Tier 1) | `+$822.40` (`+4.94 ATR`) | `292,680.00 USD-min` (`146,340.00` Tier 1) | **Lowest Spread (`1.98–2.72 bps`) & Highest R:R (`3.0208R`)**: Front-runs `pdH` (`$81,405.00`) and `$14.70M` L3 ask wall (`$81,414.00`); penalized by post-cutoff preflight receipt (`+13s/+14s`), post-signing nonce mutation, and `$19.20 > $12.00` Tier 1 risk cap at `0.04` lot. |\n| **3** | `CAND_BNB_WALL_74700` (`BNBUSD.p`) | `$24.50` | `$12.00 + $0.70 = $12.70` | **`34.14%`** | **`+7.83%`** | `+$7.34` (`+4.54 ATR`) | `67,230.00 USD-min` | **Tight Spread (`9.42 bps`) & `$1.31M` L3 Wall (`$747.14`)**: `Z_vwap = +2.06 SD` with `02:30Z` negative delta (`-$18.1k`) below `PWH` (`$748.60`) and `CWH` (`$750.90`). |\n| **4** | `CAND_BCH_INV_27829` (`BCHUSD.p`) | `$26.58` | `$12.00 + $1.16 = $13.16` | **`33.12%`** | **`+8.85%`** | `+$3.18` (`+3.15 ATR`) | `50,092.20 USD-min` | **Clean `Asian_H` (`$278.26`) / `0.786` Shelf (`$278.29`)**: Strong OU pull (bOU=−0.0677b_{\text{OU}} = -0.0677bOU​=−0.0677), but lacks L3 whale wall telemetry in `Sheet 17_Orderbook`. |\n| **5** | `CAND_XRP_WALL_13180` (`XRPUSD.pi`) | `$31.00` | `$12.00 + $3.00 = $15.00` | **`32.61%`** | **`+9.36%`** | `+$0.0248` (`+5.28 ATR`) | `118,620.00 USD-min` | **Extreme `Z_vwap = +2.99 SD` at `Mon_H` (`$1.3190`) + `$2.76M`/`$5.40M` L3 Walls (`$1.3200`/`$1.3300`)**: Penalized by `22.93 bps` spread (`$3.00` exit spread) and bullish 15m EMA stack. |\n| **6** | `CAND_SOL_WALL_10280_SPREAD_WIDENED` (`SOLUSD.p`) | `$25.17` | `$12.01 + $0.74 = $12.75` | **`33.62%`** | **`+8.35%`** | `+$1.46` (`+4.66 ATR`) | `26,460.00 USD-min` | **Spread Gate Disqualified (`25.42 bps > 25.0 bps` at `02:37:38Z`)**: Strong `$2.81M`/`$5.54M`/`$7.13M` L3 wall structure, but must wait for spread compression `<= 25.0 bps`. |\n\n\n---\n\n## 🏛️ PART 3: SECTION 8 CONTINUOUS KAIZEN & METHODOLOGY IMPROVEMENT INQUEST\n\n\n### 8.1 Skills & Methodology Optimization\n\n\n1. **Eliminating Post-Cutoff Preflight & Post-Signing Nonce Mutation (`@[systematic-debugging]`, `@[clean-code]`)**:
\n- For the second consecutive cycle (`Cycle-20261025T015327Z` and `Cycle-20261025T023918Z`), `Terminal/generate_cycle_envelope.py` ran **13–16 seconds before** `Terminal/execution_preflight.py`, and `Terminal/dispatch_dual_council.py` (lines 136–139) mutated `rec_obj["dispatch_nonce"]` after `execution_preflight.py` had already signed `receipt_sha256` with `dispatch_nonce=""`.\n- **Actionable Code Fix**:
\n- In `Terminal/dispatch_dual_council.py` (lines 136–140), replace the raw mutation with:
\n```\nif (
    isinstance(env_obj, dict)
    and env_obj.get("dispatch_nonce")
    and rec_obj.get("dispatch_nonce") != env_obj["dispatch_nonce"]
):
  rec_obj["dispatch_nonce"] = env_obj["dispatch_nonce"]
  rec_obj.pop("receipt_sha256", None)
  serialized = json.dumps(rec_obj, sort_keys=True, indent=2).encode(
      "utf-8"
  )
  rec_obj["receipt_sha256"] = hashlib.sha256(serialized).hexdigest()\n```\n\n- Execute `Terminal/execution_preflight.py --nonce <NONCE>` **prior to** `Terminal/generate_cycle_envelope.py --nonce <NONCE>` so `generate_cycle_envelope.py` sets `cutoff_dt = max(now, obs_dt + 2s)` and guarantees `tick_time < observed_at < cutoff_utc`.\n\n\n\n### 8.2 Omitted Risk Dimensions\n\n\n1. **Intraday Spread Regime Transitions (`SOLUSD.p` `22.45 bps` →\to→ `29.41 bps` →\to→ `25.42 bps`)**:
\n- Between `02:07:27 UTC` and `02:37:38 UTC`, `SOLUSD.p` drifted across the `25.0 bps` spread boundary (`22.45 bps` in `Sheet 00` →\to→ `29.41 bps` in `Sheet 20` →\to→ `25.42 bps` in `live_snapshot_latest.json`), while `BTCUSD.pi` widened from `1.98 bps` (`$16.00`) to `2.72 bps` (`$22.00`) at `02:39:31 UTC`. Relying on a static 11-asset spread list without continuous spread-distribution filtering risks staging orders on instruments whose exit spread erodes R:R at trigger time.\n\n2. **54.4-Minute Footprint Blind Spot in `Sheet 21_Tradfye_Orderflow`**:
\n- Because `Sheet 21_Tradfye_Orderflow` stopped updating at `01:45:03 UTC` (last bar `01:30:00 UTC`), the `01:45 UTC`, `02:00 UTC`, `02:15 UTC`, and `02:30 UTC` footprint bars during which `ETHUSD.pi` swept `$2,361.92` (`Z_vwap = +3.31 SD`) and `BTCUSD.pi` swept `Asian_H` (`$80,879.00`) are absent from the Excel workbook and had to be cross-verified via `live_snapshot_latest.json` (`bar_delta_15m_usd = -$398.3k` on `ETH`, `-$364.7k` on `BTC`).\n\n3. **Cross-Asset Short-Squeeze Correlation (ρ≈0.85–0.92\rho \approx 0.85\text{–}0.92ρ≈0.85–0.92)**:
\n- Simultaneous high-Z extensions across `ETH` (`+3.31 SD`), `XRP` (`+2.99 SD`), `SOL` (`+2.07 SD`), `BNB` (`+2.06 SD`), and `BTC` (`+1.67 SD`) reflect a single correlated Sunday-Asian crypto squeeze factor.\n\n\n### 8.3 Algorithmic Alternatives for Next Cycle Integration\n\n\n1. **Bivariate Hawkes Process for L3 Queue-Depletion & Fill/Markout Probability**:
\n- Model buy/sell market-order arrivals against `Sheet 17_Orderbook` L3 walls (`$4.01M` `ETH` @ `$2,374.30`, `$14.70M` `BTC` @ `$81,414.00`) to estimate P(fill before TTL∣queue,ΔCVD)P(\text{fill before TTL} \mid \text{queue}, \Delta_{\text{CVD}})P(fill before TTL∣queue,ΔCVD​) and post-fill markout AS(t+5m)\text{AS}(t+5\text{m})AS(t+5m).\n\n2. **State-Space Kalman Filter for Dynamic Spread Gating**:
\n- Replace point-in-time spread checks with a Kalman filter tracking latent spread s^t∣t\hat{s}_{t|t}s^t∣t​ and enforcing s^t∣t+1.645Pt∣t≤25.0 bps\hat{s}_{t|t} + 1.645\sqrt{P_{t|t}} \le 25.0\text{ bps}s^t∣t​+1.645Pt∣t​​≤25.0 bps, automatically disqualifying borderline symbols like `SOLUSD.p` before they breach `25.0 bps`.\n\n3. **GJR-GARCH(1,1) Volatility Cones for Stop Buffer Scaling**:
\n- Scale stop buffers dynamically behind L3 institutional walls using asymmetric GJR-GARCH(1,1) volatility cones rather than static `0.40 ATR(14)`.\n\n4. **Hierarchical Beta-Binomial Shrinkage + Isotonic Regression (n=17→100n = 17 \to 100n=17→100)**:
\n- Bridge the n=17<100n = 17 < 100n=17<100 calibration cold-start using empirical Bayes Beta-Binomial shrinkage pooled across setup classes, paired with Politis-Romano stationary block bootstrap once n≥100n \ge 100n≥100.\n\n\n---\n\n## 🏛️ PART 4: REQUIRED RESPONSE SCHEMA (JSON v1.1.0)\n\n\n```\n{
  "schema_version": "1.1.0",
  "cycle_id": "Cycle-20261025T023918Z",
  "cutoff_utc": "2026-10-25 02:39:18 UTC",
  "evidence_manifest_sha256": "76557d2de9635ef40671648d17d1b4a0166bd768d5ba3d62df11fed2a1f0ec15",
  "prompt_sha256": "7ecd929f4b7915d8ff821877f504de889759332e89f76e4f1265e4758724c63b",
  "dispatch_nonce": "050944d8-c50d-494b-8560-0faaa7bb2320",
  "provenance_status": "DENIED_FAIL_CLOSED",
  "inventory_status": "VERIFIED_FLAT_CASH_DEFENSE",
  "hard_gate_results": {
    "envelope_schema_and_digests": {
      "status": "PASS_AT_PROVENANCE_COMMIT_0BF033CB",
      "git_commit_bound": "0bf033cbcdcc468ab4a4a4f94ac5eed3dbf1fdf7",
      "git_tree_bound": "99d3628da7260b00ba334ebe035e83a8b2071a7a",
      "workbook_sha256_bound": "9394137d72672a3eda14cabfc2efa91700eec0f45e933271919e8281a1c66ce6",
      "evidence_manifest_sha256_bound": "76557d2de9635ef40671648d17d1b4a0166bd768d5ba3d62df11fed2a1f0ec15",
      "risk_policy_sha256_bound": "f4805622f9a19e213361bbbffeb7fc2228bc9ffba86bcb49f22aa9ad86ae9529",
      "envelope_file_sha256_in_0bf033cb": "af797fa408d22324fe8fc595f7861b94219b532ce77aaeda2367e21415a68e33",
      "preflight_receipt_file_sha256_in_0bf033cb": "e908e62d3d0ae5ecbe9ca91650ad6128c1055ade7ff0c9a4ea4cf25eee5fdf06"
    },
    "physical_cutoff_causality_and_finding_d9_gate": {
      "status": "FAIL_CLOSED",
      "cutoff_utc": "2026-10-25 02:39:18 UTC",
      "reference_cycle_utc": "2026-10-25 02:39:27 UTC",
      "preflight_observed_at_utc": "2026-10-25 02:39:32 UTC",
      "preflight_tick_time_utc": "2026-10-25 02:39:31 UTC",
      "tick_age_at_observation_seconds": 1.0,
      "cutoff_minus_tick_time_seconds": -13.0,
      "cutoff_minus_observed_at_seconds": -14.0,
      "reference_minus_cutoff_seconds": 9.0,
      "reference_minus_tick_time_seconds": -4.0,
      "reference_minus_observed_at_seconds": -5.0,
      "preflight_receipt_sha256_embedded": "6045e28ce734236c25d90d05294ab40975731314c24cd58fb45515110b57417e",
      "preflight_receipt_sha256_with_empty_nonce_indent2": "6045e28ce734236c25d90d05294ab40975731314c24cd58fb45515110b57417e",
      "preflight_receipt_sha256_post_nonce_injection_indent2": "0598d7fb23e33739a61ff4145a65c08036302de47f9eba61d5d0a86bdb830682",
      "preflight_receipt_sha256_post_nonce_injection_compact": "a8b90df00b803c5deffa89be513fa195255a8b774334bc1bd620645e3ffed394",
      "reason": "Terminal/generate_cycle_envelope.py froze cutoff_utc at 2026-10-25 02:39:18 UTC BEFORE Terminal/execution_preflight.py ran at 02:39:32 UTC (tick_time_utc 02:39:31 UTC). Consequently, tick_time_utc (+13.0s) and observed_at_utc (+14.0s) are strictly post-cutoff, violating tick_time < observed_at < cutoff_utc (\u00a71.4 item 1). Furthermore, execution_preflight.py was invoked with dispatch_nonce='' (sealing receipt_sha256=6045e28ce734236c25d90d05294ab40975731314c24cd58fb45515110b57417e) and Terminal/dispatch_dual_council.py (lines 136-139) subsequently mutated dispatch_nonce to '050944d8-c50d-494b-8560-0faaa7bb2320' without recomputing receipt_sha256 (post-mutation indent=2 SHA-256 is 0598d7fb23e33739a61ff4145a65c08036302de47f9eba61d5d0a86bdb830682)."
    },
    "excel_freshness_and_scorecard_gate": {
      "status": "FAIL_CLOSED",
      "excel_freshness_verified": false,
      "excel_audit_scorecard_fresh": false,
      "checklist_0bf033cb_timestamp_utc": "2026-10-25 02:35:28 UTC",
      "checklist_0bf033cb_age_vs_cutoff_seconds": 230.0,
      "checklist_0bf033cb_age_vs_023927_seconds": 239.0,
      "checklist_0bf033cb_passed_sheets": "26/32",
      "checklist_0bf033cb_failed_or_stale_sheets": [
        "3_Exchanges_LS_Ratio_15M",
        "9_Liquidation_Max_Pain_7D",
        "10_Whale_Orders",
        "15_Hyperdash_Stops_Map",
        "21_Tradfye_Orderflow",
        "22_Forced_Liquidations_MTF"
      ],
      "workbook_0bf033cb_total_worksheets": 35,
      "workbook_0bf033cb_fresh_canonical_sheets_vs_023927": "13/32",
      "workbook_0bf033cb_stale_canonical_sheets_vs_023927": "19/32",
      "stale_sheets_over_20m_at_023927_utc": [
        "20_Auction_Market_Structure (02:18:32 UTC, 20.92m)",
        "18_CVD (02:17:47 UTC, 21.67m)",
        "17_Orderbook (02:16:41 UTC, 22.77m)",
        "16_Hyperdash_telegram_Intel (02:15:35 UTC, 23.87m)",
        "14_Hyperdash_Liq_Map (02:14:27 UTC, 25.00m)",
        "13_Hyperliquid (02:13:44 UTC, 25.72m)",
        "12_Hyperdash (02:12:53 UTC, 26.57m)",
        "11_Technical (02:11:52 UTC, 27.58m)",
        "6_Funding_Fee_Settlement (02:11:13 UTC, 28.23m)",
        "5_Funding_Rate (02:10:34 UTC, 28.88m)",
        "5_OI (02:09:53 UTC, 29.57m)",
        "4_Hyperliquid_Analysis (02:08:12 UTC, 31.25m)",
        "00_MT5_Account_Telemetry (02:07:27 UTC, 32.00m)",
        "10_Whale_Orders (02:00:26 UTC, 39.02m)",
        "9_Liquidation_Max_Pain_7D (01:59:37 UTC, 39.83m)",
        "3_Exchanges_LS_Ratio_15M (01:48:49 UTC, 50.63m)",
        "21_Tradfye_Orderflow (01:45:03 UTC, 54.40m)",
        "15_Hyperdash_Stops_Map (01:40:17 UTC, 59.17m)",
        "22_Forced_Liquidations_MTF (00:59:55 UTC, 99.53m)"
      ],
      "reason": "cycle_envelope.json explicitly flags excel_freshness_verified: false and excel_audit_scorecard_fresh: false; Data/excel_all_sheets_checklist.json (02:35:28 UTC) reports 26/32 PASS and 6 WARN (all_passed: false), and 19/32 canonical sheets in DataBase_Trading.xlsx exceed the 20-minute freshness window at 02:39:27 UTC (including 21_Tradfye_Orderflow at 54.40m and 17_Orderbook at 22.77m)."
    },
    "macro_calendar_freshness_gate": {
      "status": "FAIL_CLOSED",
      "verified_at_utc": "2026-10-25T02:05:34.955592+00:00",
      "age_at_cutoff_seconds": 2023.04,
      "age_at_023927_reference_seconds": 2032.04,
      "max_allowed_age_seconds": 900.0,
      "forex_factory_live_harvested_at_utc": "2026-10-24 17:58:00 UTC",
      "forex_factory_live_age_at_023927_seconds": 31287.0,
      "active_tier1_red_folder_blackout": false,
      "reason": "Data/macro_calendar.json verified_at (02:05:34.96 UTC) is 2,023.04s (33.72m) old at cutoff_utc (02:39:18 UTC) and 2,032.04s (33.87m) old at 02:39:27 UTC, exceeding the 900s (15m) freshness threshold (\u00a71.4 item 2); Data/forex_factory_live.json is 31,287.0s (521.45m / 8.69h) old."
    },
    "solvency_and_margin_collateralization_gate": {
      "status": "FAIL_CLOSED_PREFLIGHT_NOMINAL_RISK_OVER_TIER_1_CAP",
      "balance_usd": 4846.32,
      "equity_usd": 4846.32,
      "solvency_kernel_usd": 4795.0,
      "realized_headroom_usd": 49.32,
      "capital_mode": "TIER_1_STANDARD",
      "risk_min_usd": 12.0,
      "risk_max_usd": 12.0,
      "preflight_candidate_volume": 0.04,
      "preflight_base_nominal_risk_usd": 19.2,
      "preflight_total_nominal_risk_usd": 20.08,
      "preflight_ticket_stress_usd": 27.1,
      "preflight_margin_required_usd": 1626.0,
      "preflight_margin_level_pct": 298.05,
      "max_allowed_margin_used_usd": 2423.16,
      "rescoped_tier1_compliant_volume_lots": 0.02,
      "rescoped_tier1_compliant_sl": 81900.0,
      "rescoped_tier1_nominal_risk_usd": 12.0,
      "reason": "Preflight candidate BTCUSD.pi SELL_LIMIT 0.04 lot @ 81300.0 (SL 81780.0) passes Finding D3 margin collateralization (margin_required_usd = $1,626.00 = 33.55% of equity <= 50%, post-order margin_level = 298.05% >= 200.0%) and Solvency Kernel headroom (ticket_stress_usd = $27.10 <= $49.32 realized headroom, post_joint_stop_balance = $4,817.22 >= $4,795.00), and matches the Tier 2 House Money risk band ($15.00-$25.00 USD). However, because Account #5064568 realized balance is $4,846.32 (<= $4,850.00 Tier 2 threshold), cycle_envelope.json enforces TIER_1_STANDARD (risk_min_usd = risk_max_usd = $12.00), so base_nominal_risk_usd = $19.20 ($20.08 with $0.88 exit spread) exceeds risk_max_usd ($12.00) by +$7.20 (+$8.08). Rescoping to 0.025 lot @ SL 81780.0 (or 0.02 lot @ SL 81900.0 / 0.03 lot @ SL 81700.0 on the 0.01-lot step grid) restores exact $12.00 nominal risk."
    },
    "probability_calibration_and_orderflow_gate": {
      "status": "FAIL_CLOSED",
      "trade_authorization_snapshot": "DENIED_UNVERIFIED_ORDERFLOW",
      "p_win_lower_bound": 0.4197,
      "p_win_lower_bound_calibrated": false,
      "p_win_calibration_sample_n": 17,
      "p_win_calibration_wins": 11,
      "p_win_calibration_minimum_sample": 100,
      "s_whale_status": "GATED_FAIL_CLOSED",
      "s_whale_gate_reason": "SNAPSHOT_STALE_EXCEEDS_1800S"
    }
  },
  "universe_coverage": {
    "total_broker_symbols_audited": 156,
    "tradfi_weekend_halted_count": 98,
    "crypto_perpetuals_open_24_7_count": 58,
    "crypto_spread_gate_pass_00_mt5_sheet_020727_utc_count": 13,
    "crypto_spread_gate_pass_00_mt5_sheet_020727_utc_symbols": [
      "BTCUSD.pi (1.98 bps)",
      "ZECUSD.p (5.74 bps)",
      "XMRUSD.p (5.84 bps)",
      "BNBUSD.p (6.72 bps)",
      "NETH25.p (7.06 bps)",
      "DSHUSD.p (10.53 bps)",
      "ETHUSD.pi (12.27 bps)",
      "YFIUSD.p (14.84 bps)",
      "BCHUSD.p (17.25 bps)",
      "XLMUSD.p (17.42 bps)",
      "AVEUSD.p (18.87 bps)",
      "SOLUSD.p (22.45 bps at 02:07:27Z; widened to 29.41 bps at 02:18:32Z and 25.42 bps at 02:37:38Z)",
      "XRPUSD.pi (22.91 bps)"
    ],
    "crypto_spread_gate_pass_live_snapshot_023738_utc_count": 5,
    "crypto_spread_gate_pass_live_snapshot_023738_utc_symbols": [
      "BTCUSD.pi (1.98 bps; 2.72 bps at 02:39:31 UTC preflight)",
      "BNBUSD.p (9.42 bps)",
      "ETHUSD.pi (12.27 bps)",
      "BCHUSD.p (20.93 bps)",
      "XRPUSD.pi (22.93 bps)"
    ],
    "crypto_spread_disqualified_live_snapshot_023738_utc_symbols": [
      "SOLUSD.p (25.42 bps > 25.0 bps; 29.41 bps in Sheet 20 at 02:18:32 UTC)",
      "TRXUSD.p (27.35 bps > 25.0 bps)",
      "AVXUSD.p (33.43 bps > 25.0 bps)",
      "LTCUSD.pi (52.58 bps > 25.0 bps)",
      "NERUSD.p (66.90 bps > 25.0 bps)",
      "LNKUSD.p (72.48 bps > 25.0 bps)",
      "ADAUSD.p (101.03 bps > 25.0 bps)",
      "DOTUSD.pi (191.75 bps > 25.0 bps)",
      "DOGUSD.p (270.10 bps > 25.0 bps)"
    ],
    "crypto_spread_disqualified_00_mt5_sheet_count": 45
  },
  "account_tier_and_contingent_capacity": {
    "account_login": 5064568,
    "server": "BlueberryMarketsSVG-Live",
    "balance_usd": 4846.32,
    "equity_usd": 4846.32,
    "floating_pnl_credited_usd": 0.0,
    "margin_used_usd": 0.0,
    "margin_free_usd": 4846.32,
    "hard_floor_usd": 4600.0,
    "operating_buffer_usd": 4650.0,
    "solvency_kernel_usd": 4795.0,
    "hard_floor_cushion_usd": 246.32,
    "operating_buffer_cushion_usd": 196.32,
    "kernel_cushion_usd": 51.32,
    "global_contingency_reserve_usd": 2.0,
    "existing_ticket_stress_usd": 0.0,
    "realized_headroom_usd": 49.32,
    "post_joint_stress_equity_usd": 4844.32,
    "capital_mode_reconciled_envelope": "TIER_1_STANDARD",
    "capital_mode_operator_baseline_disputed": "TIER_2_HOUSE_MONEY",
    "tier_2_unlock_threshold_usd": 4850.0,
    "shortfall_to_tier_2_usd": 3.68,
    "risk_min_usd": 12.0,
    "risk_max_usd": 12.0,
    "nominal_risk_capacity_usd": 12.0,
    "max_concurrent_tickets": 2,
    "max_equity_margin_utilization_pct": 50.0,
    "max_margin_used_cap_usd": 2423.16,
    "min_post_order_margin_level_pct": 200.0
  },
  "global_contingency_usd": 2.0,
  "existing_ticket_actions": [],
  "candidate_rows": [
    {
      "candidate_id": "CAND_ETH_WALL_237400",
      "symbol": "ETHUSD.pi",
      "native_market": "CRYPTO_PERPETUAL_24_7",
      "clock_status": "OPEN_24_7_WEEKEND_ELIGIBLE",
      "quote_timestamp": "2026-10-25 02:37:38 UTC",
      "evidence_availability_timestamps": {
        "live_snapshot_latest_utc": "2026-10-25 02:37:38 UTC",
        "sheet_20_auction_structure_utc": "2026-10-25 02:18:32 UTC",
        "sheet_17_orderbook_utc": "2026-10-25 02:16:41 UTC",
        "sheet_18_cvd_utc": "2026-10-25 02:17:47 UTC",
        "sheet_21_tradfye_orderflow_utc": "2026-10-25 01:45:03 UTC",
        "sheet_22_forced_liquidations_mtf_utc": "2026-10-25 00:59:55 UTC"
      },
      "evidence_max_age_seconds": 5963.0,
      "evidence_age_at_cutoff_seconds": 100.0,
      "row_causality_status": "CAUSAL_PRE_CUTOFF_WORKBOOK_PARTIALLY_STALE",
      "authorization_expiry_utc": "2026-10-25 03:00:00 UTC",
      "side": "SELL_LIMIT",
      "order_type": "SELL_LIMIT",
      "entry": 2374.0,
      "stop": 2418.44,
      "target": 2276.5,
      "volume": 0.27,
      "broker_risk_usd": 12.0,
      "broker_reward_usd": 26.33,
      "rr": 2.1942,
      "spread_cost_usd": 0.78,
      "stressed_loss_usd": 17.98,
      "post_joint_stop_balance": 4826.34,
      "p_fill": null,
      "p_win_given_fill": null,
      "probability_calibration_status": "UNCALIBRATED_N17_LT_100_FAIL_CLOSED",
      "estimator_references": [
        "Lo-MacKinlay VR(4)=1.4169 (z*=1.0621) on 15m; 1h VR(4)=1.0528 (z*=0.2220); 4h VR(4)=0.7804 (z*=-0.8294)",
        "Kaufman ER(48)=0.0819 (15m), 0.0742 (1h), 0.0805 (4h)",
        "Newey-West HAC drift t_NW=-4.3003 (15m), -8.7352 (1h), -7.0658 (4h)",
        "Ornstein-Uhlenbeck b_OU=-0.0307, theta_OU=2347.1663 USD (Entry 2374.00 > theta_OU 2347.17 -> +26.83 USD favorable downward drift to equilibrium)",
        "Clopper-Pearson 95% LCB=0.4197 (11/17 wins, uncalibrated < 100 minimum sample)"
      ],
      "calibration_diagnostics": {
        "closed_trades_n": 17,
        "wins": 11,
        "required_min_n": 100,
        "clopper_pearson_95_lcb": 0.4197,
        "calibrated": false
      },
      "effective_sample_size": 17,
      "probability_confidence_intervals": {
        "p_win_95pct_lcb": 0.4197,
        "status": "UNDER_SAMPLE_FLOOR_100"
      },
      "outcome_model_and_timeout_branches": {
        "tp_branch_usd": 26.33,
        "sl_branch_usd": -12.0,
        "timeout_ttl_minutes": 180,
        "timeout_policy": "CANCEL_IF_UNFILLED_AT_TTL"
      },
      "cost_ledger_and_conditioning": {
        "entry_spread_bps": 12.27,
        "exit_spread_cost_usd": 0.78,
        "fee_reserve_usd": 2.0,
        "stress_multiplier": 1.25,
        "stressed_loss_formula": "1.25 * (12.00 + 0.78) + 2.00 = 17.98 USD",
        "role_c_formula_note": "1.25 * 12.00 + 0.78 + 2.00 = 17.78 USD; conservative preflight stress = 17.98 USD; Margin_Req = 0.27 * 2374.00 * 0.50 = 320.49 USD (6.61% equity, post-order margin level 1512.16% >= 200%)"
      },
      "wait_cost_usd": null,
      "ev_net_usd": null,
      "ev_lcb_5pct_usd": null,
      "expected_capital_minutes": null,
      "utility": null,
      "uncertainty_method": "TIME_BLOCKED_BOOTSTRAP_GATED_NULL_DUE_TO_N17_LT_100",
      "adverse_selection_usd": null,
      "evidence_ids": [
        "Data/DataBase_Trading.xlsx#20_Auction_Market_Structure:Row4",
        "Data/DataBase_Trading.xlsx#17_Orderbook:Row435-442",
        "Data/DataBase_Trading.xlsx#21_Tradfye_Orderflow:Row387-391",
        "Data/DataBase_Trading.xlsx#22_Forced_Liquidations_MTF:Row14-21",
        "docs/telemetry/live_snapshot_latest.json#assets_matrix_24.ETH"
      ],
      "verdict": "HOLD",
      "fib_prime_ema_alignment": "COUNTERTREND_EXTREME_EXTENSION (15m EMA5=2357.79 > EMA13=2353.33 > EMA34=2345.73 < EMA89=2348.28 < EMA144=2353.55 < EMA233=2358.99; Z_vwap=+3.31 SD, 15m_delta=-398.3k USD; HTF t_NW=-4.30/-8.74/-7.07 BEARISH)",
      "fib_golden_zone_confluence": {
        "gp_0618": 2343.4,
        "gp_0650": 2346.93,
        "ote_0702": 2352.66,
        "invalidation_shelf_0786": 2361.92,
        "entry_status": "SWEPT_0786_SHELF_2361.92_AT_0237Z_MID_2363.55_STAGED_AT_PD_POC_2375.72_AND_4.01M_L3_WALL_AT_2374.30"
      },
      "auction_extreme_interaction": {
        "monday_ib_relation": "BELOW_MON_MID_2394.65_AND_ABOVE_MON_L_2347.30 (Mon_H=2442.00)",
        "session_extreme_sweep": "SWEPT_ASIAN_H_2361.90_AND_DAILY_VAH_2361.79_AT_0237Z_WITH_Z_VWAP_3.31_SD_AND_NEGATIVE_15M_DELTA",
        "macro_shelf_relation": "FRONT_RUNNING_PD_POC_2375.72_AND_PD_VAH_2384.05_BACKED_BY_4.01M_2374.30_6.84M_2383.00_13.34M_2392.00_4.85M_2402.60_L3_WALLS",
        "value_area_status": "ABOVE_DAILY_VAH_2361.79_RETESTING_PRIOR_DAY_VALUE_AREA (pd_POC=2375.72, pd_VAH=2384.05, pd_VAL=2334.05)"
      },
      "rejection_reasons": [
        "PROVENANCE_AND_FRESHNESS_GATE_FAIL_CLOSED: excel_freshness_verified=false, excel_audit_scorecard_fresh=false, 19/32 canonical sheets > 20m stale (including 21_Tradfye_Orderflow at 54.40m and 17_Orderbook at 22.77m), macro_calendar.json age 2023.04s > 900s, and preflight receipt is post-cutoff (+13s/+14s) with post-signature nonce mutation.",
        "PROBABILITY_CALIBRATION_GATE_FAIL_CLOSED: p_win_calibration_sample_n=17 < 100 required sample floor; S_whale is null/fail-closed.",
        "REGIME_DIFFUSION_GATE: 15m ER(48)=0.0819 < 0.15 and 15m z*=1.0621 < 1.64 (rotational balance regime)."
      ]
    },
    {
      "candidate_id": "CAND_BTC_PREFLIGHT_81300",
      "symbol": "BTCUSD.pi",
      "native_market": "CRYPTO_PERPETUAL_24_7",
      "clock_status": "OPEN_24_7_WEEKEND_ELIGIBLE",
      "quote_timestamp": "2026-10-25 02:39:31 UTC",
      "evidence_availability_timestamps": {
        "execution_preflight_receipt_utc": "2026-10-25 02:39:32 UTC",
        "live_snapshot_latest_utc": "2026-10-25 02:37:38 UTC",
        "sheet_20_auction_structure_utc": "2026-10-25 02:18:32 UTC",
        "sheet_17_orderbook_utc": "2026-10-25 02:16:41 UTC",
        "sheet_10_whale_orders_utc": "2026-10-25 02:00:26 UTC",
        "sheet_21_tradfye_orderflow_utc": "2026-10-25 01:45:03 UTC"
      },
      "evidence_max_age_seconds": 3255.0,
      "evidence_age_at_cutoff_seconds": -14.0,
      "row_causality_status": "VIOLATED_POST_CUTOFF_PREFLIGHT_QUOTE_AND_MUTATED_NONCE",
      "authorization_expiry_utc": "2026-10-25 03:00:00 UTC",
      "side": "SELL_LIMIT",
      "order_type": "SELL_LIMIT",
      "entry": 81300.0,
      "stop": 81780.0,
      "target": 79850.0,
      "volume": 0.04,
      "broker_risk_usd": 19.2,
      "broker_reward_usd": 58.0,
      "rr": 3.0208,
      "spread_cost_usd": 0.88,
      "stressed_loss_usd": 27.1,
      "post_joint_stop_balance": 4817.22,
      "p_fill": null,
      "p_win_given_fill": null,
      "probability_calibration_status": "UNCALIBRATED_N17_LT_100_FAIL_CLOSED",
      "estimator_references": [
        "Lo-MacKinlay VR(4)=1.1714 (z*=0.5598) on 15m; 1h VR(4)=1.0902 (z*=0.4183); 4h VR(4)=0.9206 (z*=-0.3111)",
        "Kaufman ER(48)=0.1357 (15m), 0.0534 (1h), 0.0406 (4h)",
        "Newey-West HAC drift t_NW=-1.9241 (15m), -8.1949 (1h), -3.2062 (4h)",
        "Ornstein-Uhlenbeck b_OU=-0.0558, theta_OU=80477.5962 USD (Entry 81300.0 > theta_OU 80477.60 -> +822.40 USD favorable downward drift)",
        "Clopper-Pearson 95% LCB=0.4197 (11/17 wins, uncalibrated < 100 minimum sample)"
      ],
      "calibration_diagnostics": {
        "closed_trades_n": 17,
        "wins": 11,
        "required_min_n": 100,
        "clopper_pearson_95_lcb": 0.4197,
        "calibrated": false
      },
      "effective_sample_size": 17,
      "probability_confidence_intervals": {
        "p_win_95pct_lcb": 0.4197,
        "status": "UNDER_SAMPLE_FLOOR_100"
      },
      "outcome_model_and_timeout_branches": {
        "tp_branch_usd": 58.0,
        "sl_branch_usd": -19.2,
        "timeout_ttl_minutes": 180,
        "timeout_policy": "CANCEL_IF_UNFILLED_AT_TTL"
      },
      "cost_ledger_and_conditioning": {
        "entry_spread_bps": 2.72,
        "exit_spread_cost_usd": 0.88,
        "fee_reserve_usd": 2.0,
        "stress_multiplier": 1.25,
        "stressed_loss_formula": "1.25 * (19.20 + 0.88) + 2.00 = 27.10 USD (Role C formula: 1.25 * 19.20 + 0.88 + 2.00 = 26.88 USD)",
        "tier_1_rescoped_alternative": "At 0.02 lot with SL=81900.0 (behind 81414.0 $14.70M wall and 81713.0 $6.24M wall, front-running 81999.0 $7.10M wall), nominal risk = 12.00 USD (exact TIER_1_STANDARD match), reward = 29.00 USD (2.4167R), spread = 0.44 USD, stressed_loss = 17.55 USD, margin_required = 813.00 USD (596.10% margin level)."
      },
      "wait_cost_usd": null,
      "ev_net_usd": null,
      "ev_lcb_5pct_usd": null,
      "expected_capital_minutes": null,
      "utility": null,
      "uncertainty_method": "TIME_BLOCKED_BOOTSTRAP_GATED_NULL_DUE_TO_N17_LT_100",
      "adverse_selection_usd": null,
      "evidence_ids": [
        "Data/execution_preflight_receipt.json",
        "Data/DataBase_Trading.xlsx#20_Auction_Market_Structure:Row3",
        "Data/DataBase_Trading.xlsx#17_Orderbook:Row44-53",
        "Data/DataBase_Trading.xlsx#10_Whale_Orders:Row3-17",
        "Data/DataBase_Trading.xlsx#21_Tradfye_Orderflow:Row3-7",
        "docs/telemetry/live_snapshot_latest.json#assets_matrix_24.BTC"
      ],
      "verdict": "HOLD",
      "fib_prime_ema_alignment": "COUNTERTREND_BOUNCE_ABOVE_RIBBON (15m EMA5=80735.92 > EMA13=80677.81 > EMA34=80528.45 > EMA89=80481.17 < EMA144=80520.52 < EMA233=80571.83; Z_vwap=+1.67 SD, 15m_delta=-364.7k USD; HTF t_NW=-1.92/-8.19/-3.21 BEARISH)",
      "fib_golden_zone_confluence": {
        "gp_0618": 80259.41,
        "gp_0650": 80320.95,
        "ote_0702": 80420.95,
        "invalidation_shelf_0786": 80582.48,
        "entry_status": "STRUCTURE_INVALIDATED_ON_80994_SWING_FRONT_RUNNING_PDH_81405_AND_14.70M_L3_WALL_AT_81414"
      },
      "auction_extreme_interaction": {
        "monday_ib_relation": "ABOVE_MON_L_80743.00_AND_BELOW_MON_MID_81915.25 (Mon_H=83087.50)",
        "session_extreme_sweep": "SWEPT_ASIAN_H_80879.00_AT_023931Z_ASK_80887.00_ENTRY_STAGED_AT_81300_BELOW_PDH_81405",
        "macro_shelf_relation": "BELOW_PDH_81405_AND_WEEKLY_POC_81635.46_TARGETING_79850_ABOVE_PWL_79634_AND_7.07M_L3_BUY_WALL_AT_79685",
        "value_area_status": "AT_DAILY_VAH_80876.45 (d_POC=80713.47, d_VAL=80387.49; pd_VAH=80914.86)"
      },
      "rejection_reasons": [
        "POST_CUTOFF_CAUSALITY_AND_SIGNATURE_MUTATION: execution_preflight_receipt.json tick_time_utc (02:39:31 UTC) and observed_at_utc (02:39:32 UTC) are +13.0s and +14.0s AFTER cutoff_utc (02:39:18 UTC), and dispatch_dual_council.py mutated dispatch_nonce after receipt_sha256 signing.",
        "TIER_1_STANDARD_RISK_CAP_EXCEEDED: At 0.04 lot, base_nominal_risk_usd = $19.20 ($20.08 total) > risk_max_usd = $12.00 under TIER_1_STANDARD (Balance $4,846.32 <= $4,850.00). Requires rescoping to 0.02 lot @ SL 81900.0 ($12.00 risk).",
        "PROVENANCE_AND_CALIBRATION_GATES_FAIL_CLOSED: excel_freshness_verified=false, macro_calendar.json age 2023.04s > 900s, and p_win_calibration_sample_n=17 < 100."
      ]
    },
    {
      "candidate_id": "CAND_BNB_WALL_74700",
      "symbol": "BNBUSD.p",
      "native_market": "CRYPTO_PERPETUAL_24_7",
      "clock_status": "OPEN_24_7_WEEKEND_ELIGIBLE",
      "quote_timestamp": "2026-10-25 02:37:38 UTC",
      "evidence_availability_timestamps": {
        "live_snapshot_latest_utc": "2026-10-25 02:37:38 UTC",
        "sheet_20_auction_structure_utc": "2026-10-25 02:18:32 UTC",
        "sheet_17_orderbook_utc": "2026-10-25 02:16:41 UTC",
        "sheet_21_tradfye_orderflow_utc": "2026-10-25 01:45:03 UTC"
      },
      "evidence_max_age_seconds": 3255.0,
      "evidence_age_at_cutoff_seconds": 100.0,
      "row_causality_status": "CAUSAL_PRE_CUTOFF_WORKBOOK_PARTIALLY_STALE",
      "authorization_expiry_utc": "2026-10-25 03:00:00 UTC",
      "side": "SELL_LIMIT",
      "order_type": "SELL_LIMIT",
      "entry": 747.0,
      "stop": 759.0,
      "target": 722.5,
      "volume": 1.0,
      "broker_risk_usd": 12.0,
      "broker_reward_usd": 24.5,
      "rr": 2.0417,
      "spread_cost_usd": 0.7,
      "stressed_loss_usd": 17.88,
      "post_joint_stop_balance": 4826.44,
      "p_fill": null,
      "p_win_given_fill": null,
      "probability_calibration_status": "UNCALIBRATED_N17_LT_100_FAIL_CLOSED",
      "estimator_references": [
        "Lo-MacKinlay VR(4)=1.3683 (z*=1.3866) on 15m; 1h VR(4)=1.3355 (z*=1.6201); 4h VR(4)=0.7495 (z*=-0.9154)",
        "Kaufman ER(48)=0.2965 (15m), 0.1260 (1h), 0.1162 (4h)",
        "Newey-West HAC drift t_NW=-0.8450 (15m), -3.4262 (1h), -2.2189 (4h)",
        "Ornstein-Uhlenbeck b_OU=-0.0072, theta_OU=739.6568 USD (Entry 747.00 > theta_OU 739.66 -> +7.34 USD downward drift)"
      ],
      "calibration_diagnostics": {
        "closed_trades_n": 17,
        "wins": 11,
        "required_min_n": 100,
        "clopper_pearson_95_lcb": 0.4197,
        "calibrated": false
      },
      "effective_sample_size": 17,
      "probability_confidence_intervals": {
        "p_win_95pct_lcb": 0.4197,
        "status": "UNDER_SAMPLE_FLOOR_100"
      },
      "outcome_model_and_timeout_branches": {
        "tp_branch_usd": 24.5,
        "sl_branch_usd": -12.0,
        "timeout_ttl_minutes": 180,
        "timeout_policy": "CANCEL_IF_UNFILLED_AT_TTL"
      },
      "cost_ledger_and_conditioning": {
        "entry_spread_bps": 9.42,
        "exit_spread_cost_usd": 0.7,
        "fee_reserve_usd": 2.0,
        "stress_multiplier": 1.25,
        "stressed_loss_formula": "1.25 * (12.00 + 0.70) + 2.00 = 17.88 USD; Margin_Req = 1.00 * 747.00 * 0.50 = 373.50 USD (7.71% equity, post-order margin level 1297.54%)"
      },
      "wait_cost_usd": null,
      "ev_net_usd": null,
      "ev_lcb_5pct_usd": null,
      "expected_capital_minutes": null,
      "utility": null,
      "uncertainty_method": "TIME_BLOCKED_BOOTSTRAP_GATED_NULL_DUE_TO_N17_LT_100",
      "adverse_selection_usd": null,
      "evidence_ids": [
        "Data/DataBase_Trading.xlsx#20_Auction_Market_Structure:Row6",
        "Data/DataBase_Trading.xlsx#17_Orderbook:Row1217-1226",
        "Data/DataBase_Trading.xlsx#21_Tradfye_Orderflow:Row1155-1159",
        "docs/telemetry/live_snapshot_latest.json#assets_matrix_24.BNB"
      ],
      "verdict": "HOLD",
      "fib_prime_ema_alignment": "BULLISH_SHORT_END_STACK (15m EMA5=741.64 > EMA13=739.64 > EMA34=735.44 > EMA89=733.28 < EMA144=733.66 < EMA233=734.42; Z_vwap=+2.06 SD, RSI14=77.70, 15m_delta=-18.1k USD)",
      "fib_golden_zone_confluence": {
        "gp_0618": 725.99,
        "gp_0650": 726.85,
        "ote_0702": 724.58,
        "invalidation_shelf_0786": 722.3,
        "entry_status": "TREND_UP_ACCEPTANCE_ABOVE_PDH_741.40_STAGED_AT_1.31M_L3_WALL_747.14_NEAR_PWH_748.60_CWH_750.90"
      },
      "auction_extreme_interaction": {
        "monday_ib_relation": "ABOVE_MON_H_729.50 (Mon_Mid=718.25, Mon_L=707.00)",
        "session_extreme_sweep": "TESTING_ASIAN_H_743.60_AT_0237Z_ASK_743.80 (Z_vwap=+2.06 SD)",
        "macro_shelf_relation": "BELOW_PWH_748.60_AND_CWH_750.90_FRONT_RUNNING_1.31M_L3_ASK_WALL_AT_747.14",
        "value_area_status": "ABOVE_VALUE_IMBALANCE (d_VAH=739.78, d_POC=731.50, d_VAL=730.14)"
      },
      "rejection_reasons": [
        "REGIME_NOT_SUB_DIFFUSIVE_FOR_MODEL_1: 15m ER(48)=0.2965 and 15m VR(4)=1.3683 (z*=1.3866) show super-diffusive expansion rather than Model 1 sub-diffusive exhaustion (VR(4) < 0.85, z* < -1.64).",
        "PROVENANCE_AND_CALIBRATION_GATES_FAIL_CLOSED: excel_freshness_verified=false, macro_calendar.json age > 900s, p_win_calibration_sample_n=17 < 100."
      ]
    },
    {
      "candidate_id": "CAND_BCH_INV_27829",
      "symbol": "BCHUSD.p",
      "native_market": "CRYPTO_PERPETUAL_24_7",
      "clock_status": "OPEN_24_7_WEEKEND_ELIGIBLE",
      "quote_timestamp": "2026-10-25 02:37:38 UTC",
      "evidence_availability_timestamps": {
        "live_snapshot_latest_utc": "2026-10-25 02:37:38 UTC",
        "sheet_20_auction_structure_utc": "2026-10-25 02:18:32 UTC",
        "sheet_21_tradfye_orderflow_utc": "2026-10-25 01:45:03 UTC"
      },
      "evidence_max_age_seconds": 3255.0,
      "evidence_age_at_cutoff_seconds": 100.0,
      "row_causality_status": "CAUSAL_PRE_CUTOFF_WORKBOOK_PARTIALLY_STALE",
      "authorization_expiry_utc": "2026-10-25 03:00:00 UTC",
      "side": "SELL_LIMIT",
      "order_type": "SELL_LIMIT",
      "entry": 278.29,
      "stop": 284.29,
      "target": 265.0,
      "volume": 2.0,
      "broker_risk_usd": 12.0,
      "broker_reward_usd": 26.58,
      "rr": 2.215,
      "spread_cost_usd": 1.16,
      "stressed_loss_usd": 18.45,
      "post_joint_stop_balance": 4825.87,
      "p_fill": null,
      "p_win_given_fill": null,
      "probability_calibration_status": "UNCALIBRATED_N17_LT_100_FAIL_CLOSED",
      "estimator_references": [
        "Lo-MacKinlay VR(4)=1.0972 (z*=0.3828) on 15m; 1h VR(4)=1.0034 (z*=0.0133); 4h VR(4)=0.8991 (z*=-0.4062)",
        "Kaufman ER(48)=0.0800 (15m), 0.0213 (1h), 0.0007 (4h)",
        "Newey-West HAC drift t_NW=-2.1324 (15m), -5.3881 (1h), +1.1179 (4h)",
        "Ornstein-Uhlenbeck b_OU=-0.0677, theta_OU=275.1101 USD (Entry 278.29 > theta_OU 275.11 -> +3.18 USD favorable downward drift)"
      ],
      "calibration_diagnostics": {
        "closed_trades_n": 17,
        "wins": 11,
        "required_min_n": 100,
        "clopper_pearson_95_lcb": 0.4197,
        "calibrated": false
      },
      "effective_sample_size": 17,
      "probability_confidence_intervals": {
        "p_win_95pct_lcb": 0.4197,
        "status": "UNDER_SAMPLE_FLOOR_100"
      },
      "outcome_model_and_timeout_branches": {
        "tp_branch_usd": 26.58,
        "sl_branch_usd": -12.0,
        "timeout_ttl_minutes": 180,
        "timeout_policy": "CANCEL_IF_UNFILLED_AT_TTL"
      },
      "cost_ledger_and_conditioning": {
        "entry_spread_bps": 20.93,
        "exit_spread_cost_usd": 1.16,
        "fee_reserve_usd": 2.0,
        "stress_multiplier": 1.25,
        "stressed_loss_formula": "1.25 * (12.00 + 1.16) + 2.00 = 18.45 USD; Margin_Req = 2.00 * 278.29 * 0.50 = 278.29 USD (5.74% equity, post-order margin level 1741.46%)"
      },
      "wait_cost_usd": null,
      "ev_net_usd": null,
      "ev_lcb_5pct_usd": null,
      "expected_capital_minutes": null,
      "utility": null,
      "uncertainty_method": "TIME_BLOCKED_BOOTSTRAP_GATED_NULL_DUE_TO_N17_LT_100",
      "adverse_selection_usd": null,
      "evidence_ids": [
        "Data/DataBase_Trading.xlsx#20_Auction_Market_Structure:Row13",
        "Data/DataBase_Trading.xlsx#21_Tradfye_Orderflow:Row5379-5383",
        "docs/telemetry/live_snapshot_latest.json#assets_matrix_24.BCH"
      ],
      "verdict": "HOLD",
      "fib_prime_ema_alignment": "COUNTERTREND_BOUNCE_ABOVE_EMA233 (15m EMA5=276.92 > EMA13=276.56 > EMA34=275.59 > EMA89=275.51 < EMA144=276.04 < EMA233=276.68; HTF t_NW=-2.13/-5.39 BEARISH)",
      "fib_golden_zone_confluence": {
        "gp_0618": 274.59,
        "gp_0650": 274.96,
        "ote_0702": 275.57,
        "invalidation_shelf_0786": 276.56,
        "entry_status": "STAGED_AT_ASIAN_H_278.26_AND_PRIOR_0786_SHELF_278.29_BELOW_FIB_SWING_HIGH_279.06_AND_PD_VAH_280.00"
      },
      "auction_extreme_interaction": {
        "monday_ib_relation": "ABOVE_MON_MID_272.41_BELOW_MON_H_280.06 (Mon_L=264.76)",
        "session_extreme_sweep": "AT_ASIAN_H_278.26_ABOVE_DAILY_VAH_277.77",
        "macro_shelf_relation": "BELOW_PD_VAH_280.00_AND_PDH_283.50_TARGETING_CWL_MON_L_264.76",
        "value_area_status": "INSIDE_VALUE (d_POC=277.14, d_VAH=277.77, d_VAL=275.02)"
      },
      "rejection_reasons": [
        "NO_OBSERVED_L3_WHALE_WALL_ANCHOR: BCHUSD.p is absent from Sheet 17_Orderbook L3 resting orderbook telemetry and Sheet 10_Whale_Orders, failing the mandatory >= 100,000 USD / >= 180s whale wall persistence gate (\u00a71.2 item 1).",
        "PROVENANCE_AND_CALIBRATION_GATES_FAIL_CLOSED: excel_freshness_verified=false, macro_calendar.json age > 900s, p_win_calibration_sample_n=17 < 100."
      ]
    },
    {
      "candidate_id": "CAND_XRP_WALL_13180",
      "symbol": "XRPUSD.pi",
      "native_market": "CRYPTO_PERPETUAL_24_7",
      "clock_status": "OPEN_24_7_WEEKEND_ELIGIBLE",
      "quote_timestamp": "2026-10-25 02:37:38 UTC",
      "evidence_availability_timestamps": {
        "live_snapshot_latest_utc": "2026-10-25 02:37:38 UTC",
        "sheet_20_auction_structure_utc": "2026-10-25 02:18:32 UTC",
        "sheet_17_orderbook_utc": "2026-10-25 02:16:41 UTC",
        "sheet_21_tradfye_orderflow_utc": "2026-10-25 01:45:03 UTC"
      },
      "evidence_max_age_seconds": 3255.0,
      "evidence_age_at_cutoff_seconds": 100.0,
      "row_causality_status": "CAUSAL_PRE_CUTOFF_WORKBOOK_PARTIALLY_STALE",
      "authorization_expiry_utc": "2026-10-25 03:00:00 UTC",
      "side": "SELL_LIMIT",
      "order_type": "SELL_LIMIT",
      "entry": 1.318,
      "stop": 1.33,
      "target": 1.287,
      "volume": 1.0,
      "broker_risk_usd": 12.0,
      "broker_reward_usd": 31.0,
      "rr": 2.5833,
      "spread_cost_usd": 3.0,
      "stressed_loss_usd": 20.75,
      "post_joint_stop_balance": 4823.57,
      "p_fill": null,
      "p_win_given_fill": null,
      "probability_calibration_status": "UNCALIBRATED_N17_LT_100_FAIL_CLOSED",
      "estimator_references": [
        "Lo-MacKinlay VR(4)=1.0304 (z*=0.1158) on 15m; 1h VR(4)=1.2743 (z*=1.8678); 4h VR(4)=0.8967 (z*=-0.4261)",
        "Kaufman ER(48)=0.2650 (15m), 0.0249 (1h), 0.0022 (4h)",
        "Newey-West HAC drift t_NW=+1.1929 (15m), -7.2116 (1h), -7.2226 (4h)",
        "Ornstein-Uhlenbeck b_OU=-0.0211, theta_OU=1.2932 USD (Entry 1.3180 > theta_OU 1.2932 -> +0.0248 USD favorable downward drift)"
      ],
      "calibration_diagnostics": {
        "closed_trades_n": 17,
        "wins": 11,
        "required_min_n": 100,
        "clopper_pearson_95_lcb": 0.4197,
        "calibrated": false
      },
      "effective_sample_size": 17,
      "probability_confidence_intervals": {
        "p_win_95pct_lcb": 0.4197,
        "status": "UNDER_SAMPLE_FLOOR_100"
      },
      "outcome_model_and_timeout_branches": {
        "tp_branch_usd": 31.0,
        "sl_branch_usd": -12.0,
        "timeout_ttl_minutes": 180,
        "timeout_policy": "CANCEL_IF_UNFILLED_AT_TTL"
      },
      "cost_ledger_and_conditioning": {
        "entry_spread_bps": 22.93,
        "exit_spread_cost_usd": 3.0,
        "fee_reserve_usd": 2.0,
        "stress_multiplier": 1.25,
        "stressed_loss_formula": "1.25 * (12.00 + 3.00) + 2.00 = 20.75 USD (assuming contract_size=1,000 XRP/lot); Margin_Req = 1.00 * 1,000 * 1.3180 * 0.50 = 659.00 USD (13.60% equity, post-order margin level 735.41%)"
      },
      "wait_cost_usd": null,
      "ev_net_usd": null,
      "ev_lcb_5pct_usd": null,
      "expected_capital_minutes": null,
      "utility": null,
      "uncertainty_method": "TIME_BLOCKED_BOOTSTRAP_GATED_NULL_DUE_TO_N17_LT_100",
      "adverse_selection_usd": null,
      "evidence_ids": [
        "Data/DataBase_Trading.xlsx#20_Auction_Market_Structure:Row7",
        "Data/DataBase_Trading.xlsx#17_Orderbook:Row1529-1536",
        "Data/DataBase_Trading.xlsx#21_Tradfye_Orderflow:Row1539-1543",
        "docs/telemetry/live_snapshot_latest.json#assets_matrix_24.XRP"
      ],
      "verdict": "HOLD",
      "fib_prime_ema_alignment": "BULLISH_15M_RIBBON_STACK (15m EMA5=1.3026 > EMA13=1.2992 > EMA34=1.2923 > EMA89=1.2862 > EMA144=1.2849 > EMA233=1.2843; Z_vwap=+2.99 SD, RSI14=70.83)",
      "fib_golden_zone_confluence": {
        "gp_0618": 1.271,
        "gp_0650": 1.2728,
        "ote_0702": 1.268,
        "invalidation_shelf_0786": 1.2632,
        "entry_status": "EXTREME_MEAN_REVERSION_AT_MON_H_1.3190_AND_2.76M_L3_WALL_AT_1.3200 (Z_vwap=+2.99 SD)"
      },
      "auction_extreme_interaction": {
        "monday_ib_relation": "STAGED_JUST_BELOW_MON_H_1.3190_TARGETING_MON_MID_1.2860_D_VAL_1.2871 (Mon_L=1.2530)",
        "session_extreme_sweep": "SWEPT_ASIAN_H_1.3080_AT_0237Z_ASK_1.3100",
        "macro_shelf_relation": "SWEPT_PDH_1.3080_FRONT_RUNNING_2.76M_L3_WALL_AT_1.3200_WITH_SL_AT_5.40M_L3_WALL_1.3300",
        "value_area_status": "ABOVE_VALUE_IMBALANCE (d_VAH=1.3003, d_POC=1.2900, d_VAL=1.2871)"
      },
      "rejection_reasons": [
        "SPREAD_FRICTION_DRAG: Spread is 22.93 bps ($0.0030/XRP = 25.0% of the $0.0120 stop distance), creating excessive exit spread friction.",
        "REGIME_NOT_SUB_DIFFUSIVE_FOR_MODEL_1: 15m ER(48)=0.2650, 15m VR(4)=1.0304, and 1h VR(4)=1.2743 (z*=1.8678) with full bullish 15m Fib-Prime EMA stack oppose counter-trend shorting until tape exhaustion is confirmed.",
        "PROVENANCE_AND_CALIBRATION_GATES_FAIL_CLOSED: excel_freshness_verified=false, macro_calendar.json age > 900s, p_win_calibration_sample_n=17 < 100."
      ]
    },
    {
      "candidate_id": "CAND_SOL_WALL_10280_SPREAD_WIDENED",
      "symbol": "SOLUSD.p",
      "native_market": "CRYPTO_PERPETUAL_24_7",
      "clock_status": "OPEN_24_7_WEEKEND_ELIGIBLE",
      "quote_timestamp": "2026-10-25 02:37:38 UTC",
      "evidence_availability_timestamps": {
        "live_snapshot_latest_utc": "2026-10-25 02:37:38 UTC",
        "sheet_20_auction_structure_utc": "2026-10-25 02:18:32 UTC",
        "sheet_17_orderbook_utc": "2026-10-25 02:16:41 UTC",
        "sheet_21_tradfye_orderflow_utc": "2026-10-25 01:45:03 UTC"
      },
      "evidence_max_age_seconds": 3255.0,
      "evidence_age_at_cutoff_seconds": 100.0,
      "row_causality_status": "CAUSAL_PRE_CUTOFF_SPREAD_GATE_DISQUALIFIED_AT_023738Z",
      "authorization_expiry_utc": "2026-10-25 03:00:00 UTC",
      "side": "SELL_LIMIT",
      "order_type": "SELL_LIMIT",
      "entry": 102.8,
      "stop": 107.0,
      "target": 94.0,
      "volume": 2.86,
      "broker_risk_usd": 12.01,
      "broker_reward_usd": 25.17,
      "rr": 2.0958,
      "spread_cost_usd": 0.74,
      "stressed_loss_usd": 17.94,
      "post_joint_stop_balance": 4826.38,
      "p_fill": null,
      "p_win_given_fill": null,
      "probability_calibration_status": "UNCALIBRATED_N17_LT_100_FAIL_CLOSED",
      "estimator_references": [
        "Lo-MacKinlay VR(4)=1.1891 (z*=0.6612) on 15m; 1h VR(4)=1.0674 (z*=0.3448); 4h VR(4)=0.6600 (z*=-1.0662)",
        "Kaufman ER(48)=0.1871 (15m), 0.0995 (1h), 0.0517 (4h)",
        "Newey-West HAC drift t_NW=-1.7485 (15m), -9.6512 (1h), -7.0604 (4h)",
        "Ornstein-Uhlenbeck b_OU=-0.0351, theta_OU=101.3431 USD (Entry 102.80 > theta_OU 101.34 -> +1.46 USD favorable downward drift)"
      ],
      "calibration_diagnostics": {
        "closed_trades_n": 17,
        "wins": 11,
        "required_min_n": 100,
        "clopper_pearson_95_lcb": 0.4197,
        "calibrated": false
      },
      "effective_sample_size": 17,
      "probability_confidence_intervals": {
        "p_win_95pct_lcb": 0.4197,
        "status": "UNDER_SAMPLE_FLOOR_100"
      },
      "outcome_model_and_timeout_branches": {
        "tp_branch_usd": 25.17,
        "sl_branch_usd": -12.01,
        "timeout_ttl_minutes": 180,
        "timeout_policy": "CANCEL_IF_UNFILLED_AT_TTL"
      },
      "cost_ledger_and_conditioning": {
        "entry_spread_bps": 25.42,
        "exit_spread_cost_usd": 0.74,
        "fee_reserve_usd": 2.0,
        "stress_multiplier": 1.25,
        "stressed_loss_formula": "1.25 * (12.01 + 0.74) + 2.00 = 17.94 USD; Margin_Req = 2.86 * 102.80 * 0.50 = 147.00 USD (3.03% equity, post-order margin level 3296.82%)"
      },
      "wait_cost_usd": null,
      "ev_net_usd": null,
      "ev_lcb_5pct_usd": null,
      "expected_capital_minutes": null,
      "utility": null,
      "uncertainty_method": "TIME_BLOCKED_BOOTSTRAP_GATED_NULL_DUE_TO_N17_LT_100",
      "adverse_selection_usd": null,
      "evidence_ids": [
        "Data/DataBase_Trading.xlsx#20_Auction_Market_Structure:Row5",
        "Data/DataBase_Trading.xlsx#17_Orderbook:Row826-833",
        "Data/DataBase_Trading.xlsx#21_Tradfye_Orderflow:Row771-775",
        "docs/telemetry/live_snapshot_latest.json#assets_matrix_24.SOL"
      ],
      "verdict": "HOLD",
      "fib_prime_ema_alignment": "COUNTERTREND_BOUNCE (15m EMA5=102.12 > EMA13=101.98 > EMA34=101.55 > EMA89=101.40 < EMA144=101.52 < EMA233=101.68; Z_vwap=+2.07 SD, 15m_delta=-140.0k USD; HTF t_NW=-1.75/-9.65/-7.06 BEARISH)",
      "fib_golden_zone_confluence": {
        "gp_0618": 101.16,
        "gp_0650": 101.3,
        "ote_0702": 101.54,
        "invalidation_shelf_0786": 101.92,
        "entry_status": "STRUCTURE_INVALIDATED_ON_102.90_SWING_STAGED_AT_PD_VAH_102.79_AND_2.81M_L3_WALL_AT_102.83"
      },
      "auction_extreme_interaction": {
        "monday_ib_relation": "BELOW_MON_MID_103.38_AND_ABOVE_MON_L_100.78 (Mon_H=105.99)",
        "session_extreme_sweep": "TESTED_ASIAN_H_102.39_AT_0237Z_ASK_102.41",
        "macro_shelf_relation": "AT_PD_VAH_102.79_BELOW_PDH_103.62_AND_5.54M_7.13M_WALLS_AT_103.37_104.05",
        "value_area_status": "INSIDE_VALUE (d_POC=102.12, d_VAH=102.38, d_VAL=101.49)"
      },
      "rejection_reasons": [
        "SPREAD_GATE_VIOLATION_AT_LIVE_SNAPSHOT_AND_SHEET_20: SOLUSD.p spread widened from 22.45 bps (02:07:27 UTC in Sheet 00) to 29.41 bps (02:18:32 UTC in Sheet 20) and 25.42 bps ($0.26 raw spread on $102.28 mid at 02:37:38 UTC in live_snapshot_latest.json), exceeding the <= 25.0 bps hard gate by +0.42 bps.",
        "PROVENANCE_AND_CALIBRATION_GATES_FAIL_CLOSED: excel_freshness_verified=false, macro_calendar.json age > 900s, p_win_calibration_sample_n=17 < 100."
      ]
    }
  ],
  "arithmetic_validation": {
    "account_capital_reconciliation": {
      "balance_usd": 4846.32,
      "equity_usd": 4846.32,
      "hard_floor_cushion_check": "4846.32 - 4600.00 = 246.32 USD (EXACT_MATCH)",
      "operating_buffer_cushion_check": "4846.32 - 4650.00 = 196.32 USD (EXACT_MATCH)",
      "kernel_cushion_check": "4846.32 - 4795.00 = 51.32 USD (EXACT_MATCH)",
      "realized_headroom_check": "4846.32 - 4795.00 - 2.00 - 0.00 = 49.32 USD (EXACT_MATCH)",
      "post_joint_stress_equity_check": "4846.32 - 2.00 - 0.00 = 4844.32 USD (EXACT_MATCH)"
    },
    "preflight_receipt_btcusd_004_lot_reconciliation": {
      "symbol": "BTCUSD.pi",
      "side": "SELL_LIMIT",
      "volume": 0.04,
      "entry": 81300.0,
      "sl": 81780.0,
      "tp": 79850.0,
      "bid": 80865.0,
      "ask": 80887.0,
      "mid_check": "(80865.0 + 80887.0) / 2 = 80876.00 USD (EXACT_MATCH)",
      "spread_raw_check": "80887.0 - 80865.0 = 22.00 USD (EXACT_MATCH)",
      "spread_bps_check": "(22.00 / 80876.00) * 10000 = 2.7202 bps -> 2.72 bps (EXACT_MATCH)",
      "spread_cost_usd_check": "22.00 * 0.04 * 1.0 = 0.88 USD (EXACT_MATCH)",
      "profit_at_sl_usd_check": "(81300.0 - 81780.0) * 0.04 * 1.0 = -19.20 USD (EXACT_MATCH)",
      "profit_at_tp_usd_check": "(81300.0 - 79850.0) * 0.04 * 1.0 = +58.00 USD (EXACT_MATCH)",
      "rr_ratio_check": "58.00 / 19.20 = 3.020833R",
      "margin_required_usd_check": "0.04 * 81300.0 * 0.50 = 1626.00 USD (EXACT_MATCH)",
      "equity_margin_utilization_pct_check": "(1626.00 / 4846.32) * 100 = 33.5512% <= 50.0% (PASS_FINDING_D3)",
      "margin_level_post_order_pct_check": "(4846.32 / 1626.00) * 100 = 298.0517% -> 298.05% >= 200.0% (EXACT_MATCH_PASS_FINDING_D3)",
      "margin_free_post_order_usd_check": "4846.32 - 1626.00 = 3220.32 USD (EXACT_MATCH)",
      "total_nominal_risk_usd_check": "19.20 + 0.88 = 20.08 USD (EXACT_MATCH)",
      "ticket_stress_preflight_model_check": "1.25 * (19.20 + 0.88) + 2.00 = 25.10 + 2.00 = 27.10 USD (EXACT_MATCH)",
      "ticket_stress_role_c_model_check": "1.25 * 19.20 + 0.88 + 2.00 = 24.00 + 2.88 = 26.88 USD (-0.22 USD difference because preflight multiplies exit_spread by 1.25)",
      "post_joint_stop_balance_check": "4846.32 - 2.00 - 27.10 = 4817.22 USD >= 4795.00 USD (+22.22 USD Solvency Kernel buffer)",
      "tier_1_vs_tier_2_nominal_risk_check": "19.20 USD is inside TIER_2_HOUSE_MONEY [15.00, 25.00 USD] but exceeds TIER_1_STANDARD risk_max_usd (12.00 USD) by +7.20 USD (+8.08 USD including exit spread)"
    }
  },
  "disputes": [
    {
      "dispute_id": "DIS-344-01",
      "severity": "CRITICAL_FAIL_CLOSED",
      "jurisdiction": "ROLE_D_CAUSALITY_AND_CRYPTOGRAPHIC_PROVENANCE",
      "title": "Post-Cutoff Preflight Execution (tick_time +13s, observed_at +14s After cutoff_utc) & Post-Signature Nonce Mutation in Terminal/dispatch_dual_council.py",
      "details": "In Cycle-20261025T023918Z, Terminal/generate_cycle_envelope.py froze cutoff_utc at 2026-10-25 02:39:18 UTC before Terminal/execution_preflight.py sampled MT5 at tick_time_utc 2026-10-25 02:39:31 UTC and observed_at_utc 2026-10-25 02:39:32 UTC (+13.0s and +14.0s AFTER cutoff_utc, and +4.0s/+5.0s after reference clock 02:39:27 UTC), violating tick_time < observed_at < cutoff_utc (\u00a71.4 item 1). Moreover, execution_preflight.py was invoked with dispatch_nonce='' (signing receipt_sha256=6045e28ce734236c25d90d05294ab40975731314c24cd58fb45515110b57417e), and Terminal/dispatch_dual_council.py (lines 136-139) subsequently overwrote rec_obj['dispatch_nonce'] = '050944d8-c50d-494b-8560-0faaa7bb2320' without recomputing receipt_sha256 (post-mutation indent=2 SHA-256 is 0598d7fb23e33739a61ff4145a65c08036302de47f9eba61d5d0a86bdb830682)."
    },
    {
      "dispute_id": "DIS-344-02",
      "severity": "HIGH_SOLVENCY_TIER_MISMATCH",
      "jurisdiction": "ROLE_C_SOLVENCY_AND_CAPITAL_TIER_GOVERNANCE",
      "title": "Operator Baseline ($4,865.07, TIER_2_HOUSE_MONEY, 0.04 Lot BTCUSD.pi = $19.20 Risk) vs Reconciled Envelope ($4,846.32, TIER_1_STANDARD, $12.00 Risk Cap)",
      "details": "Account #5064568 realized balance is $4,846.32 ($3.68 below the $4,850.00 TIER_2_HOUSE_MONEY threshold), placing the account in TIER_1_STANDARD (risk_min_usd = risk_max_usd = $12.00, 0 open positions). However, execution_preflight.py was invoked with volume=0.04 lot on BTCUSD.pi (SL 81780.0 vs Entry 81300.0), producing base_nominal_risk_usd = $19.20 ($20.08 total nominal risk with $0.88 exit spread), which satisfies TIER_2_HOUSE_MONEY ($15.00-$25.00) and Finding D3 margin collateralization ($1,626.00 margin = 33.55% equity, 298.05% margin level) but exceeds TIER_1_STANDARD risk_max_usd ($12.00) by +$7.20 (+$8.08). Rescoping to 0.02 lot @ SL 81900.0 (or 0.03 lot @ SL 81700.0) yields exact $12.00 nominal risk."
    },
    {
      "dispute_id": "DIS-344-03",
      "severity": "HIGH_TELEMETRY_STALENESS",
      "jurisdiction": "ROLE_D_WORKBOOK_AND_CALENDAR_FRESHNESS",
      "title": "Unverified Workbook Scorecard (excel_freshness_verified: false, 26/32 Checklist PASS, 19/32 Canonical Sheets > 20m Stale Including 21_Tradfye_Orderflow at 54.40m & 17_Orderbook at 22.77m) & Stale Macro Calendar (33.87m > 15m)",
      "details": "In provenance commit 0bf033cbcdcc468ab4a4a4f94ac5eed3dbf1fdf7 (02:37:55 UTC), Data/excel_all_sheets_checklist.json (02:35:28 UTC) reports 26/32 PASS and 6 WARN (3_Exchanges_LS_Ratio_15M, 9_Liquidation_Max_Pain_7D, 10_Whale_Orders, 15_Hyperdash_Stops_Map, 21_Tradfye_Orderflow, 22_Forced_Liquidations_MTF; all_passed: false), leaving excel_freshness_verified: false. Direct XML inspection of Data/DataBase_Trading.xlsx (9394137d72672a3eda14cabfc2efa91700eec0f45e933271919e8281a1c66ce6) at 02:39:27 UTC shows only 13/32 canonical sheets are <= 20m old, while 19/32 exceed 20m (including 22_Forced_Liquidations_MTF at 99.53m, 15_Hyperdash_Stops_Map at 59.17m, 21_Tradfye_Orderflow at 54.40m, 3_Exchanges_LS_Ratio_15M at 50.63m, 9_Liquidation_Max_Pain_7D at 39.83m, 10_Whale_Orders at 39.02m, 00_MT5_Account_Telemetry at 32.00m, 17_Orderbook at 22.77m, 18_CVD at 21.67m, and 20_Auction_Market_Structure at 20.92m). Additionally, Data/macro_calendar.json (02:05:34.96 UTC) is 2,032.04s (33.87m > 900s) old and Data/forex_factory_live.json (17:58:00 UTC) is 521.45m (8.69h) old."
    },
    {
      "dispute_id": "DIS-344-04",
      "severity": "MEDIUM_SPREAD_DRIFT",
      "jurisdiction": "ROLE_B_SPREAD_CENSUS_RECONCILIATION",
      "title": "SOLUSD.p Spread Widening Across the 25.0 bps Threshold (22.45 bps at 02:07:27Z -> 29.41 bps at 02:18:32Z -> 25.42 bps at 02:37:38Z)",
      "details": "Of the 11 crypto symbols named in \u00a71.4 item 3, only 4 pass <= 25.0 bps in live_snapshot_latest.json at 02:37:38 UTC (BTCUSD.pi 1.98 bps [2.72 bps at 02:39:31Z preflight], BNBUSD.p 9.42 bps, ETHUSD.pi 12.27 bps, XRPUSD.pi 22.93 bps) plus BCHUSD.p (20.93 bps) = 5 live snapshot survivors, because SOLUSD.p widened to 25.42 bps ($102.15/$102.41, +0.42 bps over the 25.0 bps gate; 29.41 bps in Sheet 20 at 02:18:32 UTC), alongside TRXUSD.p (27.35 bps), AVXUSD.p (33.43 bps), NERUSD.p (66.90 bps), LNKUSD.p (72.48 bps), ADAUSD.p (101.03 bps), and DOGUSD.p (270.10 bps)."
    }
  ],
  "unknowns": [
    "Exact calibrated conditional fill probability P_fill and conditional barrier win probability P_TP across the candidate universe (closed-trade sample n=17 < 100 minimum sample requirement; Clopper-Pearson 95% LCB = 0.4197 uncalibrated).",
    "Exact composite whale score S_whale (gated fail-closed because whale snapshot tau_s exceeds the 1,800s freshness threshold in live_snapshot_latest.json).",
    "Post-01:45:03 UTC 15m footprint bars in Sheet 21_Tradfye_Orderflow (54.40m old at 02:39:27 UTC) and post-00:59:55 UTC bars in Sheet 22_Forced_Liquidations_MTF (99.53m old at 02:39:27 UTC).",
    "Exact MT5 broker contract_size for altcoin perpetuals not yet preflighted via Terminal/execution_preflight.py (ETHUSD.pi, BNBUSD.p, BCHUSD.p, XRPUSD.pi, SOLUSD.p)."
  ],
  "methodology_critique_and_improvements": [
    "Enforce strict pipeline ordering in the master cycle orchestrator: (1) generate nonce -> (2) run workbook & macro_calendar refresh + excel_all_sheets_checklist.py -> (3) run Terminal/execution_preflight.py --nonce <NONCE> using capital_mode-aware lot sizing from account solvency -> (4) run Terminal/generate_cycle_envelope.py --nonce <NONCE> -> (5) commit to git and embed without post-hoc JSON mutation.",
    "Fix Terminal/dispatch_dual_council.py (lines 136-139) so that if rec_obj['dispatch_nonce'] is updated, rec_obj['receipt_sha256'] is popped and recomputed via hashlib.sha256(json.dumps(rec_obj, sort_keys=True, indent=2).encode('utf-8')).hexdigest().",
    "Bind execution_preflight.py lot-size selection dynamically to solvency.capital_mode (sizing 0.02 lot @ SL 81900.0 for $12.00 risk under TIER_1_STANDARD vs 0.04 lot for $19.20 risk under TIER_2_HOUSE_MONEY).",
    "Ensure the background Excel writer loop completes a full 32-sheet sweep (specifically 21_Tradfye_Orderflow, 22_Forced_Liquidations_MTF, 15_Hyperdash_Stops_Map, 10_Whale_Orders, and 3_Exchanges_LS_Ratio_15M) within <15m prior to council dispatch."
  ],
  "section_8_kaizen": {
    "skills_and_methodology_optimization": "Integrating all 9 loaded quantitative skills (@[trader-signal], @[trader-risk], @[market-ingest], @[market-pattern], @[adaptive-wfo-epoch], @[sharpe-ratio-non-iid-corrections], @[time-series-decomposer], @[clean-code], @[systematic-debugging]) plus repository skills (@[backtesting-frameworks], @[orderflow-footprint], @[hawkes-queue-dynamics]) directly prevented premature single-line vetoes, proved the exact cryptographic root cause of the receipt_sha256 mismatch in Terminal/dispatch_dual_council.py (lines 136-139), caught SOLUSD.p's spread widening across the 25.0 bps gate (22.45 bps -> 29.41 bps -> 25.42 bps), and re-anchored ETHUSD.pi's short limit at $2,374.00 (front-running pd_POC $2,375.72 and the $4.01M L3 ask wall at $2,374.30) after price swept $2,361.92 to $2,363.55 (Z_vwap = +3.31 SD).",
    "omitted_risk_dimensions": "1. Intraday spread regime transitions on borderline altcoin perpetuals (SOLUSD.p crossed from 22.45 bps PASS at 02:07:27 UTC to 29.41 bps FAIL at 02:18:32 UTC and 25.42 bps FAIL at 02:37:38 UTC; BTCUSD.pi widened from 1.98 bps to 2.72 bps at 02:39:31 UTC); 2. Stale footprint telemetry in Sheet 21_Tradfye_Orderflow (frozen at 01:45:03 UTC, 54.40m old) masking the 01:45-02:30 UTC orderflow bars during which ETH swept its 0.786 shelf ($2,361.92) and BTC swept Asian_H ($80,879.00); 3. Cross-asset perpetual beta (~0.85-0.92 across BTC/ETH/BNB/XRP) during the ongoing Asian session short squeeze.",
    "algorithmic_alternatives": "1. Bivariate Hawkes Process for L3 queue-depletion and fill/adverse-selection probability P(fill, AS | queue, delta); 2. State-Space Kalman Filter for dynamic spread bps gating (to catch SOLUSD.p's 22.45 -> 25.42 bps drift before order staging); 3. GJR-GARCH(1,1) volatility cones for dynamic stop buffers behind L3 institutional walls; 4. Hierarchical Beta-Binomial shrinkage + Isotonic Regression to bridge the n=17 -> n=100 probability calibration cold-start."
  },
  "authorization": "DENIED_FAIL_CLOSED",
  "response_sha256": "40f83c09c1c78785d15f8e283168af92262eb4763e115a900fad3d87eb614191"
}\n```\n