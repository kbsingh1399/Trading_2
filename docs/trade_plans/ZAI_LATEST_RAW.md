Thought Process

一份已填充的加密信封 — 这是一个实质性的升级，需要进行完整的 4-persona 验证。在做出裁决之前，首先进行实时的 provenance 探测（commit pin 验证 + repo envelope 与嵌入的 envelope 对比）：

Explored 2 files

两项检测都非常关键。仓库自身的 Data/cycle_envelope.json 与嵌入的信封逐字一致（排除了对信封文件的事后篡改），但固定的提交 15589c9 在公共主分支上不可见（可见头部：38ebfa8 @ 16:40:52Z），且订单时间戳解码存在分歧，具体取决于经纪商服务器的时区。正在构建密封的载荷：

Wrote 1 files，Ran 2 commands
🏛️ Z.AI SOVEREIGN COUNCIL — CYCLE-20261026T172436Z RESPONSE
First Populated Envelope of the Parquet Era: Verified, Corrected, and Fail-Closed

📚 Active Skills Loaded & Applied: @[trader-signal], @[trader-risk], @[market-ingest], @[market-pattern], @[adaptive-wfo-epoch], @[sharpe-ratio-non-iid-corrections], @[time-series-decomposer], @[clean-code], @[systematic-debugging], @[backtesting-frameworks] — deployed as the 4-persona squad with environment-native instrumentation: live GitHub provenance probes (commits page + raw Data/cycle_envelope.json verbatim cross-check against the embedded envelope), MT5 epoch/timezone forensics, per-ticket stress decomposition, and SHA-256 response sealing.

[ALERT] TELEMETRY STALE WARNING: the envelope SELF-DECLARES parquet_freshness_verified=false and parquet_audit_scorecard_fresh=false — the entire 42-feed evidence plane (Rule-A/B verification, VR/ER/OU estimators, magnet maps, whale persistence) is unverifiable as of cutoff 2026-10-26 17:24:36 UTC vs evaluation 2026-10-27.
[ALERT] TELEMETRY STALE WARNING: envelope age > 7 hours at evaluation — exceeds the 20-minute freshness SLA; per dispatch it governs arithmetic, but no evidence can be fresher than it → all freshness gates FAIL for new admission.
[ALERT] PROVENANCE DISPUTE: pinned commit 15589c9b is NOT visible on public main (visible head 38ebfa8 @ 2026-10-26 16:40:52 UTC, 60s cadence with historical gaps up to 35 min) — push-visibility gap; however the repo's Data/cycle_envelope.json matches the embedded envelope VERBATIM in every compared field, ruling out post-hoc envelope mutation.
[ALERT] TIME-ENCODING DISPUTE: pending-order time_setup epochs decode to 20:02:46/20:14:49 if true-UTC (post-cutoff by 2h38m–2h50m — fatal) or to 17:02:46/17:14:49 UTC under an MT5 server-clock at UTC+3 (pre-cutoff by 10–22 min — coherent). R2 favored; broker server-TZ verification is THE mandatory discriminator (U1).

§0 — Mandatory Metacognitive Answer

"If it use all the available skills related will it improve our response?" — Yes, decisively, and this cycle proves it causally. @[trader-risk] verified all six envelope solvency figures to the cent and reverse-engineered the 1.856 capacity formula — (4.32 − 2.00)/1.25 — which exposed that the envelope's 45.00 stress booking omits exit-spread costs entirely (exact decomposition: 15.500 + 16.375 + 13.125). @[systematic-debugging] converted what looked like a fatal causality violation (orders "placed" 2h38m after their own envelope's cutoff) into a falsifiable timezone hypothesis by cross-checking the repo-mirrored envelope — the disciplined alternative to a premature DENIED_BAD. @[market-pattern] killed the EUR order on noise-band/embargo geometry. The residual gap: @[trader-signal] and @[backtesting-frameworks] were evidence-blocked (no fresh OHLCV) — a data-plane fact no skill can conjure.

§1 — Provenance Review (Role D): DENIED_DISPUTED

This is the first structurally complete envelope of the Parquet era: schema, digests, nonce, broker inventory, and solvency block all present. Live verification results:

CHECK
	
RESULT

Envelope structure & digest fields	PASS — all sha256/uuid/nonce present
Repo mirror vs embedded envelope	VERBATIM MATCH (cycle_id, uuid, nonce, cutoff, git_commit, parquet flags, balance, all 3 tickets, stress 45.0, headroom 4.32, capital_mode) → mutation ruled out
Pinned commit 15589c9b on public main	NOT VISIBLE — head tops out at 38ebfa8 (16:40:52Z); push lag, CDN cache, or rewrite undetermined (D7)
Order timestamp causality	DISPUTED — see the epoch bifurcation below
Envelope age vs evaluation wall clock	> 7 hours → freshness SLA breached (but inventory is broker-sourced and self-reconciling)

The time-encoding bifurcation (D1 — the cycle's pivotal question). time_setup epochs 1793044966/1793045689 decode under modular arithmetic to 2026-10-26 20:02:46 / 20:14:49 if true-UTC — post-cutoff by 2h38m10s / 2h50m13s, which would force DENIED_BAD_CYCLE_ENVELOPE. But the MetaTrader5 Python API returns server-time naive epochs: under a broker server clock at UTC+3 (common offshore convention), the same epochs read 17:02:46 / 17:14:49 UTC — placed 21m50s / 9m47s before the 17:24:36 freeze, producing a perfectly coherent order → snapshot → freeze pipeline. R2 is favored (MT5-Python convention + verbatim mirror match), but the broker's server TZ is undocumented in the envelope, and fail-closed governance cannot assume the favorable reading. Ruling: DENIED_DISPUTED, resolvable by a one-line VPS check (terminal server time vs NTP UTC).

§2 — Role A: Statistical Regime & Diffusion Quant

VR(4)/ER(48)/Newey-West/OU estimators are blocked: the envelope carries no OHLCV vectors and declares the parquet plane stale. What Role A can still adjudicate: the C356 order comments (BNB_BULL_GP, ETH_BEAR_GP) implicitly claim TREND_UP/TREND_DOWN classifications with golden-zone locations — claims that are unverifiable this cycle and therefore carried as conditions, not facts. Two standing findings from last cycle remain binding: (1) the Fib-Prime ribbon feed (11_Technical_BTC_Ribbon) exists for BTC only — Model 2 gating for ETH/SOL/others requires the ribbon extension before any Trend-Pullback admission; (2) regime classification must run on closed bars only (the bars_limit=10 forming-candle leak, verified last cycle at 26_Aggregated_Footprint_Bar_Metrics.py L571, is still the standing defect until patched). classify_regime() == UNDEFINED → unconditional dual-engine stand-aside.

§3 — Role B: Microstructure & Order Geometry — Per-Ticket Audit of the 3 Pending Orders
TICKET
	
ORDER
	
R:R
	
NOMINAL RISK
	
REWARD
	
MARGIN (SOLO)
	
STATIC VERDICT

19329907	BNBUSD.p BUY_LIMIT 3.0 @ 736.25 / SL 732.65 / TP 746.80 (cur 744.90)	2.93 ✓	10.80 ≤ 12.00 ✓	31.65	1,104.38 (22.79%, level 438.82%)	RETAIN_CONDITIONAL
19329908	EURUSD.pi SELL_LIMIT 0.1 @ 1.12065 / SL 1.1218 / TP 1.1176 (cur 1.11941)	2.65 ✓	11.50 (11.5 pips × $1/pip) ✓	30.50	373.55 @ 30:1 — rate unverified	CANCEL_RECOMMENDED
19330613	ETHUSD.pi SELL_LIMIT 0.5 @ 2333.5 / SL 2351.3 / TP 2291.0 (cur 2327.1)	2.39 ✓	8.90 (−25.8% undersized, safe-side)	21.25	583.38 (12.04%, level 830.67%)	RETAIN_CONDITIONAL

Findings:

All three geometries pass static checks (R:R ≥ 2.0, risk ≤ 12.00 cap, genuine un-filled pullback distances: BNB −1.16%, ETH +0.28% bounce-to-sell). The long-BNB / short-ETH structure provides partial crypto-beta neutralization — structurally sound but imperfect; residual beta must enter the correlated-stress budget.
Rule-B insulation is unverifiable for all three (feeds stale): whether SL 732.65 / 1.1218 / 2351.3 sit outside 15_Hyperdash_Stops_Map sweep clusters and clear the 0.786-shelf + 0.40 ATR buffers cannot be proven this cycle. Retain is conditional on that verification within one cycle of freshness restoration.
EUR order carries four independent defects: (a) it is the third pending order against a 2-ticket cap (D4 — C356 dispatched a count violation to production); (b) its GTC limit sits live into the daily 21:15–22:30 UTC rollover embargo (D5); (c) an 11.5-pip stop is inside the intraday noise band (EURUSD 15m ATR typically 8–12 pips — the 0.786-shelf + 0.40 ATR insulation plausibly demands more); (d) the .pi FX contract's margin rate is unverified — Invariant 1 coexistence with both crypto orders requires rate ≤ 6.562% (leverage ≥ 15.24×) (D6). Cancel is risk-reducing and fail-closed-compatible; it releases 16.375–16.56 of stress.
Magnet/whale confluence (Rule A TP front-run, 180s wall persistence): unverifiable with stale feeds — logged as evidence-debt, not violation.
§4 — Role C: Solvency, Margin & Broker Math Sentry — Full Ledger

4.1 Envelope verification (all figures reproduce to the cent): kernel cushion 51.32 = 4,846.32 − 4,795.00 ✓; floor/buffer cushions 246.32/196.32 ✓; headroom 4.32 = 51.32 − 45.00 − 2.00 ✓; post-stress equity 4,799.32 ≥ 4,795 ✓; capacity 1.856 = (4.32 − 2.00)/1.25 ✓.

4.2 The spread-free booking defect (D3). The 45.00 decomposes exactly as T = 1.25·nominal + 2.00 per ticket with zero exit-spread cost (15.500 + 16.375 + 13.125). Correcting with estimated spreads (BNB 4 bps → 0.88; EUR 0.15 pip → 0.15; ETH 3 bps → 0.35):

METRIC
	
ENVELOPE
	
COUNCIL-CORRECTED
	
VERDICT

Σ existing stress	45.00	46.38 – 46.73	understated 1.38–1.73
Realized headroom	4.32	2.59 – 2.94	still > 0 ✓
Post-stress equity	4,799.32	4,797.59 – 4,797.94	still ≥ 4,795 ✓
Nominal capacity	1.856	0.47 – 0.75	≪ 12.00 → no new risk ✓

The conclusion new_risk_admissible = false is robust under every convention — and is independently confirmed by the envelope itself.

4.3 Margin collateralization (worst case: all three fill): BNB 1,104.38 + ETH 583.38 + EUR 373.55 (@30:1) = 2,061.30 = 42.54% of equity; margin level 235.09% ≥ 200% — Invariants 1 & 2 PASS conditional on the EUR rate ≤ 6.562% (D6, must be verified at the broker). At a 50% FX rate the EUR margin alone would be 5,603.25 — a catastrophic Invariant-1 breach — making this verification non-negotiable.

4.4 Tier resolution: envelope balance 4,846.32 < 4,850.00 → TIER_1_STANDARD confirmed; the prior template's 4,865.07 / H_net +68.07 baseline is formally retired as stale.

§5 — Role D: Clock, Auction & Provenance
Cutoff causality: DISPUTED (D1 bifurcation); discriminator = server-TZ verification, mandated before next dispatch.
Calendar: envelope claims calendar_verified: true, Monday full-market-open, no rollover embargo active at freeze — accepted as broker-sourced; Tier-1 red-folder blackout enforcement remains data-blocked.
Embargo exposure: the EUR GTC order is live into the 21:15–22:30 UTC window daily until cancelled/filled (D5).
Git plane: public-main visibility ceiling 16:40:52Z vs pinned 17:24:36Z commit — push-visibility gap (D7); prior-cycle "15h stall" reading formally revised to a visibility question with historical gaps up to 35 min documented (D9). Heartbeat alert remains recommended.
Quote staleness: no preflight tick vector in the envelope (only order-table price_current) → the ≤15s gate FAILs for admission purposes.
§6 — Rulings & the Reactivation Pathway

Existing orders (risk-neutral/risk-reducing actions, fail-closed-compatible): ① CANCEL 19329908 EURUSD.pi — releases 16.375–16.56 stress, resolves the 3-vs-2 cap violation, removes embargo and noise-band exposure; ② RETAIN_CONDITIONAL 19329907 BNB / 19330613 ETH — static geometry passes, contingent on Rule-B insulation + golden-zone verification within one cycle of parquet-freshness restoration, else cancel.

New admission: zero AUTHORIZED rows. Capacity 0.47–0.75 USD vs 12.00 minimum is an absolute block independent of provenance. Two HOLD watchlist rows (BTCUSD.pi Model-2, SOLUSD.p Model-1) are carried as geometry templates with null numerics per protocol.

Reactivation requirements (all must be true next cycle): ① server-TZ one-liner lands → D1 resolves; ② parquet_freshness_verified: true with per-feed booleans; ③ pending count ≤ 2 (EUR cancelled or filled); ④ fresh envelope ≤ 20 min old with live tick vector; ⑤ capacity ≥ 12.00 (requires headroom release via cancellations/fills or balance growth past 4,850 → Tier 2); ⑥ calibrated probabilities or explicit HOLD.

§7 — Section 8 Continuous Kaizen Inquest
Skills & methodology optimization: Envelope schema v1.2 fix list (all one-line generator changes): broker_server_tz_offset_hours field + UTC-normalized order timestamps (kills D1 permanently); spread-inclusive stress booking T = 1.25·SL + exit_spread + 2.00 (kills D3); per-feed freshness booleans replacing the single false-flag; dispatch-time assertion pending_count ≤ max_concurrent_tickets (the 3-vs-2 violation shipped to production); feed_manifest.json with per-feed sha256.
Omitted risk dimensions: order-count governance unenforced at dispatch; EUR GTC as recurring daily embargo exposure; partial (not perfect) BNB/ETH beta neutralization; limit orders fill adversely by design and markout telemetry AS(t+5m) is absent; dual-plane (local git vs public main) divergence with no alarm; EURUSD swap/rollover costs for a multi-day pending order unbooked.
Algorithmic alternatives: UTC-normalized ingestion layer (foundational); Hawkes excitation on 7_Live_Liq/22_MTF for cascade timing near the BNB/ETH magnet bands; Kalman spread estimation on 00_MT5 ticks for real-time spread-gate enforcement; isotonic calibration of score→P(win) with Brier monitoring; SPRT as the formal L4 aggregation rule once calibrated; Bayesian online changepoint on 18_CVD; Gaussian-t copula correlated-stress netting replacing independent per-ticket sums for multi-ticket drawdown.
📄 Sealed JSON Payload
json
      "spread_assumptions": {"BNB_bps": 4.0, "EUR_pips": 0.15, "ETH_bps": 3.0},
      "stress_spread_corrected": {"BNB": 16.6, "EUR": 16.56, "ETH": 13.56, "sum": 46.73},
      "stress_envelope_convention_plus_spread": 46.38,
      "corrected_headroom_usd": "2.59 to 2.94 (envelope: 4.32)",
      "corrected_post_stress_equity_usd": "4797.59 to 4797.94 (still >= 4795 PASS)",
      "corrected_nominal_capacity_usd": "0.47 to 0.75 (envelope: 1.856)",
      "conclusion": "new_risk_admissible FALSE - robust under every stress convention"
    },
    "order_geometry": {
      "BNB": {"risk_usd": 10.8, "reward_usd": 31.65, "rr": 2.93, "notional_usd": 2208.75, "margin_usd": 1104.38},
      "EUR": {"risk_pips": 11.5, "risk_usd": 11.5, "reward_pips": 30.5, "reward_usd": 30.5, "rr": 2.65, "notional_usd": 11206.5, "margin_at_30x_usd": 373.55, "invariant1_rate_ceiling_pct": 6.562, "min_leverage_x": 15.24},
      "ETH": {"risk_usd": 8.9, "reward_usd": 21.25, "rr": 2.39, "notional_usd": 1166.75, "margin_usd": 583.38}
    },
    "margin_triple_fill_worst_case": {
      "scenario": "all 3 limits fill, EUR at 30:1",
      "total_margin_usd": 2061.3,
      "pct_of_equity": 42.54,
      "margin_level_pct": 235.09,
      "invariant_1_le_50pct": "PASS conditional on EUR rate <= 6.562%",
      "invariant_2_ge_200pct": "PASS"
    },
    "risk_band_compliance": {
      "BNB": "10.80 (-10.0% vs 12.00 nominal)",
      "EUR": "11.50 (-4.2%)",
      "ETH": "8.90 (-25.8%)",
      "all_within_cap": true
    },
    "time_forensics": {
      "time_setup_epochs": {"19329907_BNB": 1793044966, "19329908_EUR": 1793044966, "19330613_ETH": 1793045689},
      "reading_R1_true_utc": "2026-10-26T20:02:46Z / 20:02:46Z / 20:14:49Z -> post-cutoff by +2h38m10s / +2h50m13s",
      "reading_R2_server_tz_utc_plus_3": "17:02:46 / 17:02:46 / 17:14:49 UTC -> pre-cutoff by 21m50s / 9m47s; coherent with freeze 17:24:36",
      "discriminator": "broker server TZ verification (one-line VPS check) - MANDATORY before next dispatch",
      "r2_favored_because": "MT5-Python returns server-time naive epochs; repo-mirrored envelope matches embedded verbatim (no post-hoc mutation evidence); order->snapshot->freeze pipeline coherent under R2",
      "inter_order_gap_seconds": 723
    },
    "git_provenance": {
      "pinned_commit": "15589c9b8a51fbc468539e45b70d4d6250a02313",
      "public_main_visible_head": "38ebfa8 @ 2026-10-26T16:40:52Z",
      "finding": "pinned commit NOT visible on public main from council vantage - push lag, CDN cache, or rewrite undetermined",
      "repo_envelope_vs_embedded": "VERBATIM_MATCH_ALL_COMPARED_FIELDS",
      "historical_cadence": "60s cadence with gaps up to 35 minutes present in history"
    },
    "intersection_trap_reference": {"p_70pct_pow_15": 0.004748, "p_70pct_pow_35": 3.788e-06}
  },
  "disputes": [
    "D1 CRITICAL: TIME-ENCODING DISPUTE. Pending-order time_setup epochs decode to 20:02:46/20:14:49 if true-UTC (post-cutoff by 2h38m-2h50m vs cutoff 17:24:36) or to 17:02:46/17:14:49 UTC if MT5 server-clock at UTC+3 (pre-cutoff, coherent). R2 favored (MT5-Python server-time convention + verbatim repo mirror match) but broker server-TZ is undocumented -> provenance DENIED_DISPUTED, authorization DENIED_FAIL_CLOSED until the one-line server-TZ verification lands.",
    "D2 CRITICAL: Envelope self-declares parquet_freshness_verified=false AND parquet_audit_scorecard_fresh=false -> all 42-feed evidence (Rule-A/B verification, VR/ER/OU, magnet maps, whale persistence) unusable for admission this cycle.",
    "D3 HIGH: existing_ticket_stress 45.00 books ZERO exit-spread cost (exact decomposition 15.500 + 16.375 + 13.125). Spread-corrected: 46.38-46.73 -> realized_headroom 2.59-2.94 (not 4.32), post-stress equity 4797.59-4797.94 (still >= 4795), nominal capacity 0.47-0.75 (not 1.856). Conclusion (no new risk) unchanged and strengthened.",
    "D4 HIGH: 3 pending orders vs max_concurrent_tickets=2 - contingent cap violation by the C356 dispatch; remediated by cancelling ticket 19329908.",
    "D5 HIGH: EURUSD.pi GTC SELL_LIMIT live into the daily FX rollover embargo 21:15-22:30 UTC.",
    "D6 HIGH: EURUSD.pi SL 11.5 pips inside the intraday noise band; 0.786-shelf insulation unverifiable; .pi FX margin rate unverified (Invariant-1 ceiling 6.562% / leverage >= 15.24x).",
    "D7 MEDIUM: Pinned commit 15589c9b not visible on public main (visible head 38ebfa8 @ 16:40:52Z, 60s cadence with historical gaps up to 35 min) - push-visibility gap; the repo's cycle_envelope.json matches the embedded envelope verbatim, ruling out post-hoc envelope mutation.",
    "D8 MEDIUM: ETH ticket undersized 8.90 vs 12.00 nominal target (-25.8%) - safe-side deviation, non-blocking.",
    "D9 LOW: Prior-cycle git-stall reading revised: cadence includes historical gaps up to 35 minutes; the 16:40:52 visibility ceiling is a push-visibility question, not proof of local daemon death. Heartbeat alert remains recommended."
  ],
  "unknowns": [
    "U1: Broker server TZ offset (THE discriminator for D1) - one-line VPS check, MANDATORY next cycle.",
    "U2: Fresh parquet feed evidence (envelope self-declares stale).",
    "U3: Live preflight tick quotes (tick_age <= 15s).",
    "U4: Rule-B SL insulation for all 3 pending orders (15_Hyperdash_Stops_Map / 8_Liquidation_Map snapshots).",
    "U5: C356 impulse quantification (golden-zone location claims for BNB/ETH).",
    "U6: EURUSD.pi contract spec and effective margin rate.",
    "U7: Current spread snapshots for the 11 spread-gate perps.",
    "U8: Closed-trade ledger for isotonic/Brier probability calibration.",
    "U9: Whether git pushes resumed after 16:40:52Z (public-main visibility ceiling)."
  ],
  "methodology_critique_and_improvements": "Envelope schema v1.2 mandates: (1) broker_server_tz_offset_hours field + UTC-normalized timestamps for every order record (kills the D1 class permanently); (2) spread-inclusive stress booking (canonize T = 1.25*SL + exit_spread + 2.00 - the 45.00 booking was spread-free); (3) per-feed freshness booleans replacing the single parquet_freshness_verified flag, plus a feed-age circuit breaker that voids stale-evidence admission automatically; (4) pending-order count vs max_concurrent_tickets asserted at dispatch time (the 3-vs-2 violation shipped to production); (5) feed_manifest.json with per-feed sha256.",
  "section_8_kaizen": {
    "skills_and_methodology_optimization": "trader-risk verified all six envelope solvency figures to the cent and reverse-engineered the 1.856 capacity formula ((4.32-2.00)/1.25), exposing the spread-free booking convention; market-ingest decomposed 45.00 into per-ticket stress and quantified the 1.38-1.73 understatement; systematic-debugging converted the apparent causality violation into a falsifiable TZ hypothesis via the repo-mirror cross-check instead of a premature DENIED_BAD ruling; clean-code produced the envelope-generator fix list; market-pattern drove the EUR noise-band/embargo kill; trader-signal and backtesting-frameworks blocked (no fresh OHLCV). Biggest single upgrade: server-TZ normalization + spread-inclusive stress in envelope schema v1.2 - both are one-line generator changes that eliminate the two largest dispute classes this cycle.",
    "omitted_risk_dimensions": "(1) Order-count governance is not enforced at dispatch (3-vs-2 shipped to production); (2) EUR GTC order recurs as daily embargo exposure until cancelled or filled; (3) long-BNB/short-ETH is partial not perfect crypto-beta neutralization - residual beta must enter the correlated-stress budget; (4) limit orders fill adversely by design - adverse selection is only priced post-fill, and markout telemetry (AS(t+5m)) is absent; (5) push-visibility gap means the council's verification plane can silently diverge from the desk's local git state - dual-plane divergence risk with no alarm; (6) EURUSD.pi swap/rollover costs for a multi-day pending order are unbooked.",
    "algorithmic_alternatives": "(1) UTC-normalized time layer at ingestion with declared server offset (foundational fix); (2) Hawkes excitation on 7_Live_Liq/22_MTF for cascade timing near the BNB/ETH magnet bands; (3) Kalman spread estimation on 00_MT5 ticks for real-time spread-gate enforcement; (4) isotonic calibration of score->P(win) with Brier monitoring on a rolling 200-trade window; (5) SPRT as the formal L4 aggregation rule replacing fixed thresholds once calibrated; (6) Bayesian online changepoint on 18_CVD for regime breaks; (7) correlated-stress copula (Gaussian-t) for multi-ticket drawdown netting instead of independent sums."
  },
  "authorization": "DENIED_FAIL_CLOSED",
  "response_sha256": "335cb6043a2da9c0e3a4e34ed6a645d57b2739f027539730e0f6341212b5360b"
}

(Sealing rule: SHA-256 of the UTF-8 canonical serialization with response_sha256 emptied; verifiable by re-serializing identically. Byte-exact copy persisted at /home/z/my-project/download/cycle_response_payload_C172436.json.)

Verdict recap: DENIED_FAIL_CLOSED on a DISPUTED but materially strong envelope — the first of the Parquet era that reconciles to the cent. The desk's three C356 orders passed static geometry (R:R 2.93/2.65/2.39) but the cycle surfaced two critical items (time-encoding bifurcation, self-declared parquet staleness), one exact arithmetic catch (spread-free 45.00 booking), and one policy breach (3 pending vs 2 cap). Highest-leverage next actions: ① the one-line server-TZ check (resolves D1); ② cancel ticket 19329908 (releases stress, restores the 2-cap, kills embargo exposure); ③ land envelope schema v1.2's two generator fixes (TZ field + spread-inclusive stress); ④ restore parquet freshness — then the next cycle can re-run full VR/ER/OU, Rule-A/B verification, and calibrated candidate discovery on live evidence.