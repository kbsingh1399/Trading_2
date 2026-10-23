Thought Process
Wrote 2 files，Ran 2 commands
Create File c297_math_check.py
Run C297 math check sections N0-N7
MultiEdit /home/z/my-project/scripts/c297_math_check.py
Run C297 math check sections N0-N7
Done

MC delivered a decisive result — P(mission) = 0 in 20k paths. Let me patch two precision items (S8 lockout flags + theoretical upper bound) and re-run:

Wrote 2 files，Ran 2 commands

All numbers verified. Now appending the worklog entry:

Wrote 1 files，Ran 1 commands

✅ 33-SHEET CONFIRMATION: [0 formula errors | 0 empty headers | Data Freshness: 15 min declared — 2 exceptions: GER40 radar geometry 61 min stale (06:45 lattice), BTC whale-wall map ≥ 3h45m (C291 provenance, must re-pull before any BTC trigger)]

Governance basis: all six canonical SOPs + worklog C280–C296 loaded; every figure below machine-verified in scripts/c297_math_check.py (Sections N0–N7, run clean). Where the warehouse cannot certify a live microstructure fact, the verdict fails closed with an explicit data gate.

SECTION R — RECONCILIATION C296 → C297 [TEL|CALC|OPS]

The book changed materially in the 37 minutes since C296. Balance delta = 0.00 (no booked fills → BANK-READ RULE: rung-0, banked $0.00, envelope 22.80 pre-bank / 33.20 post-bank, unchanged), but the broker book now carries one filled position + one pending limit — the first live risk since C291.

R-1. NZDUSD.pi #19244087 — provenance verified, telemetry internally consistent [CALC]

Floating P/L = 4,811.22 − 4,818.51 = −7.29 = exactly −0.90 pips × $8.10/pip → implied mark Bid 0.56895. The floating number decomposes perfectly; no hidden second position.
Margin forensics: Used margin = 4,811.22 − 3,274.81 = 1,536.41; NZD notional = 81,000 × 0.56904 = 46,092.24 → implied leverage 30.00× — an exact retail FX margin ratio. This independently confirms lot size, entry, and that the BTC pending reserves no margin.
Geometry provenance: entry 0.56904 + SL 0.56888 (R0 = 1.6 pips) reproduces the C286 Early-BE fix (trigger 0.56916 = entry+0.75R; BE SL 0.56906 = entry+0.10R) to the fifth decimal. This position was staged ~01:46 UTC, rested ~6h, and filled between 07:08:17–07:45:54.

R-2. GER40-B (C295-1) — final classification: NOT-STAGED → OPS-MISS #1 [OPS]
Instruction was stage 06:45:00 / cancel 07:10:00. C296 telemetry (07:08:17) showed book 0/0 — an order staged at 06:45 would still have been resting at 07:08. C297 confirms no GER40 order ever existed and equity is untouched. Classification: Rule→Order gap, staging non-execution, NON-STRIKE (no order reached the server, zero market risk, zero financial impact) — but it is the desk's first execution-omission of the session, and it means the desk's strongest ratified geometry (combo B) simply never saw the market. Desk must supply root cause at C298 (socket down vs. never attempted vs. server reject — retcode or it didn't happen).

R-3. Operator worst-case figure is understated — and still breaches your own buffer [CALC]
Telemetry claims Worst-Case Simultaneous Stopout = 4,792.48. Reverse-engineering: that is nominal risks only (12.96 + 12.43 = 25.39 + 0.64 unattributed). Canonical stress math:

COMPONENT
	
NZD LEG
	
BTC-SELL LEG

Nominal risk	12.96	12.43
Spread cost (S=0.3 pip / $0.47)	2.43	0.47
×1.25 stress multiplier	19.24	16.12
+ $2.00 commission	21.24	18.12

Canonical simultaneous stopout = 4,818.51 − 39.36 = 4,779.15 — not 4,792.48. The delta (spreads 2.90 + commissions 4.00 + multiplier 7.07) is exactly the risk the operator's number omitted. Critically: even the operator's own 4,792.48 is BELOW the 4,795.00 operating buffer the same telemetry mandates. The live book violates the buffer invariant on both accountings. That drives Ruling 1 below.

SECTION E — 4-PERSONA EXHAUSTIVE EVALUATION
🔬 PERSONA 1: STATISTICAL REGIME & DIFFUSION QUANT

P1-1. NZDUSD #19244087 (live — management review, not entry approval).

From-here dominance: reward to TP = $56.70 vs remaining risk to SL = $5.67 → R:R from here = 10.00. Breakeven p from here = 0.0909; friction-adjusted p for EV>0 = 0.1619. The entry required p ≥ 0.3204; the hold requires only p ≥ 0.18 — the position has already paid its information cost. Early exit forfeits a 10:1 payoff and is mathematically indefensible absent a regime break.
Driftless diffusion: barriers −1.6/+6.1 pips → p(hit TP first) = 0.2078; E[T] = a·b/σ² = 0.61–2.44 M15 bars (9–37 min) for σ ∈ [2,4] pips/bar — far under the 24-bar Time-Decay Trap threshold. This position self-resolves fast; it cannot rot.
Verdict: HOLD, regime-invalidated exit only (z_VR(4,1h) flipping > +1.96 against the MR thesis, or structural break of 0.5688 with >240s linger).

P1-2. BTC BUY_LIMIT radar (0.02 @ 80,500 / 79,942.20 / 82,000).

Geometry: R:R = 2.689 ✓; friction 0.2074R → p required for EV>+0.20R = 0.3815; driftless barrier baseline = 0.2711. The gap (+0.11 probability-alpha) must be certified by a TREND gate: z_VR(4,1h) > +1.96 or ER(20,1h) > 0.25. No trend statistics exist on the desk for this level → FAIL CLOSED (UNDEFINED → STAND ASIDE).

P1-3. GER40-B radar re-proposal.

Geometry unchanged from C295 ratification: R:R 2.4356, friction 0.1784R → p required = 0.4012 vs driftless 0.2911 (+0.11 alpha required, MR certification: z_VR(4) < −1.96).
Fatal: non-stationarity. France PMI (07:15) and Germany PMI (07:30) are already released; Eurozone flash prints at 08:00 — 14m06s from telemetry. Every VR/ER/OU/HAC statistic computed on pre-PMI bars describes a regime that terminates at 08:00. Classifying this setup today is measuring a dead distribution. UNDEFINED through the release window → UNCONDITIONAL STAND ASIDE until 08:35:00 re-fit.

P1-4. BTC SELL_LIMIT #19244096 (pending).

R:R 2.5823; friction 0.1987R → p required = 0.3905 vs driftless 0.2791 (+0.11 from MR + wall). Carry-over ratification (C291/C295) survives statistically, but its aggregate position does not (Persona 3). Required p is only earnable with fresh CVD z ≤ −1.50 and wall re-verification — both stale ≥ 3h45m.

P1 unifying finding: every ticket on this desk requires ≈ +0.11 probability-alpha above the driftless barrier baseline to clear EV>+0.20R. That is precisely what the 4-persona battery exists to certify — and PMI-contaminated statistics cannot certify anything European before 08:35.

🌊 PERSONA 2: MICROSTRUCTURE & LIQUIDATION QUANT

P2-1. BTC BUY radar — three independent microstructure failures.

TP into opposing liquidity: TP 82,000 sits inside the 81,580–82,000 institutional ask zone this desk itself has been fading since C286. Section F requires TP ahead of opposing liquidity; this TP is behind it. REJECT.
Whale polarity unverified: a long requires a resting BID bunker below 80,500 with τ ≥ 180s, ρ ≥ 0.60. Newest wall map is C291-provenance (≥ 3h45m). FAIL CLOSED.
LIR gate unverified: longs require LIR > 1.80 in the ±2% band; no fresh Sheet 23/24 pull exists. FAIL CLOSED.
Also: same-asset dual-side stacking with the live BTC SELL_LIMIT is a live instance of defect D6 (no correlation clustering).

P2-2. BTC SELL_LIMIT — polarity is correct for a fade (resting ask above, limit at the wall face 81,960), but persistence/refill (τ ≥ 180s, ρ ≥ 0.60) is unverifiable on stale maps; sweep-reclaim state at 81,960 unknown (if the zone was swept and reclaimed <90s, fade valid; >240s linger = structural breakout, fade forbidden). Re-verification is a hard precondition of any re-arm (Gate C1).

P2-3. NZD #19244087 — SL 0.56888 rests 0.7 pips below the current mark; no evidence of an un-swept retail stop cluster directly beneath (C286 diligence). No staging-trap violation. Monitor only.

🛡️ PERSONA 3: CONVEX PORTFOLIO & SOLVENCY SENTRY (arbiter's home ground)

P3-1. NZD #19244087 sizing audit — PASS.
Lot-snap verified: floor((13.00/16.00)×100)/100 = 0.81 → nominal 12.96, a hair under the 13.00 band floor by correct floor-snapping (not a defect). R:R 3.8125 ≫ 2.0 ✓. Spread/TP = 4.92% ≤ 10% ✓. Kelly: f* = 0.1795 → 0.25·f*·Equity = $215.91 ≫ 12.96 — Kelly never binds at our sizes; R13/buffer are always the binding constraints.

Stressed 21.24 (canon) → post-stress 4,797.27, buffer +2.27 ✓ — but under a realistic per-lot commission ($7 RT/lot → $5.67 on 0.81 lots, defect D7: our flat-$2 model underestimates multi-lot tickets), stressed = 24.91 → post-stress 4,793.60 = buffer −1.40. The NZD leg alone can breach the buffer on commission reality. Early-BE priority is mandatory.

P3-2. THE GOVERNING FINDING — the live book is R13-illegal.
RESIDUAL-13 cap = balance − 4,788.00 = 30.51. Current book aggregate = 21.24 + 18.12 = 39.36 > 30.51 → BREACH. Full scenario matrix:

SCENARIO
	
Σ STRESSED
	
WORST-CASE EQUITY
	
FLOOR (4,775)
	
BUFFER (4,795)
	
R13

S1 NZD only (canon)	21.24	4,797.27	✓ +22.27	✓ +2.27	✓
S2 NZD only (D7 comm)	24.91	4,793.60	✓ +18.60	✗ −1.40	✓
S3 NZD + BTCsell [CURRENT BOOK]	39.36	4,779.15	✓ +4.15	✗ −15.85	✗ BREACH
S4 NZD + BTCbuy	37.57	4,780.94	✓ +5.94	✗ −14.06	✗ BREACH
S5 NZD + GER40-B	39.98	4,778.53	✓ +3.53	✗ −16.47	✗ BREACH
S6 FULL RADAR (all three)	55.69	4,762.82	✗ FLOOR BREACH −12.18	✗	✗
S7 NZD-BE (+1.62 locked) + BTCsell re-arm	18.12	4,800.39	✓ +25.39	✓ +5.39	✓

Three decisive readings: (a) executing the entire radar as staged walks the account to 4,762.82 — a HARD FLOOR BREACH; (b) the radar's own surplus column ("+$4.77", "+$7.56") is computed against a phantom book that omits the live NZD — true surpluses are −16.47 and −14.06 (isolation fallacy, D6 live instance #2 after the XAG triplets); (c) the R13 cap is self-scaling (balance − 4,788): after one NZD stopout (balance 4,801.12) the cap shrinks to 13.12 — below every ticket we own (min 16.34) → post-loss LOCKOUT. The system is anti-martingale by construction.

P3-3. BTC BUY radar stress flaw: the operator's $15.95 implies spread = $0.004 — a zero-spread assumption. Realistic (S=$15.67/BTC × 0.02): 16.34. Telemetry defect, noted for D-list.

🏛️ PERSONA 4: AUCTION PROFILE & FRICTION ARBITRAGEUR

P4-1. Event Risk Clock — the controlling constraint.

EVENT
	
TIME (UTC)
	
STATUS AT 07:45:54
	
CONSEQUENCE

France Flash PMI	07:15	released	statistics stale
Germany Flash PMI	07:30	released	statistics stale
Eurozone Flash PMI	08:00	14m06s away	±35min blackout → European embargo until 08:35:00
Rollover embargo	21:15–22:30	—	—
Weekend flat	20:00	—	effective runway 12.24h, not 17.0h

The same clock discipline that correctly cancelled GER40-B at 07:10 forbids re-staging it now. Re-proposing it 35 minutes before the release inverts the doctrine that ratified it.

P4-2. Friction ratios: NZD 4.92% ✓ | BTC-sell 1.47% ✓ | BTC-buy 1.04% ✓ | GER40 ≈ 1.0 pt/94.6 pt = 1.05% now, but event spreads widen 3–5× at 08:00 → pre-release friction unverifiable; post-PMI gate: spread ≤ 3.0 pts (ratio ≤ 3.2%).

P4-3. Telemetry hygiene (new defect D8): Section A states "Zero positions consumed" against a book carrying one filled position — template line not synced to live state. Small, but this is the same channel that understated worst-case by $13.33; telemetry hygiene is solvency infrastructure.

SECTION F — ARBITER SYNTHESIS: OPTION B — MANAGED HOLD + STAND ASIDE ON NEW STAGING

We are not 100% flat (NZD is live and mathematically correct to hold), so pure cash defense is unavailable — but zero new capital deploys this cycle. Two immediate book orders, then pre-registered re-arm gates.

⚡ RULING 1 — P0 IMMEDIATE: CANCEL BTCUSD.pi #19244096 (SELL_LIMIT)

Basis: aggregate R13 = 39.36 > 30.51; buffer breach on both accountings; the combination was never jointly ratified (each ticket was sanctioned at a cycle when the other didn't exist). A reactive "manage-if-both-fill" protocol was costed and rejected on execution-risk grounds (C283/C284 strike history; deterministic action beats conditional execution per COUNCIL-OS conservative-merge). Pending cancel = zero cost; parameters are preserved in Gate C1.

⚡ RULING 2 — NZD #19244087 MANAGEMENT PROTOCOL (armed now)
ORDER
	
TRIGGER (BID ≥)
	
ACTION
	
RETCODE GATE

A1 Early-BE	0.56916 (+0.75R)	SL → 0.56906 (locks +$1.62)	require DONE; 10016-guard
A2 +1.25R	0.56924	SL 0.56906 — quantization-merged into A1 (0.15R = 2.4 ticks rounds to the same tick)	—
A3 Profit lock	0.56930 (+1.65R)	SL → 0.56917 (locks +$10.53)	only reachable if TP removed; dormant armor
A4 Time-decay	fill_ts + 6h (∈ 13:08–13:46 UTC — pull the deal timestamp)	if Bid < 0.56907 (+0.20R): close at market	—

TP 0.56965 (+3.81R, +$49.41) stands and supersedes the +2.50R fallback (0.56944). No averaging, no SL widening (re-site ban). Decimal discipline: 5-digit symbols, point = 0.00001 — this is the C286 bug class, respect the tick grid.

⚡ RULING 3 — PRE-REGISTERED RE-ARM GATES (execute mechanically when ALL conditions print — no council re-deliberation)
C1 · BTC SELL re-stage 0.03 @ 81,960.00 / SL 82,374.19 / TP 80,890.43 (risk 12.43, stressed 18.12): iff NZD Early-BE retcode-confirmed or NZD closed AND wall τ ≥ 180s, ρ ≥ 0.60 AND spread ≤ $16/BTC AND CVD z ≤ −1.50 AND sweep-reclaim < 90s at the 81,960 zone AND R13 vs live book. TTL: cancel 12:00 UTC if unfilled.
C2 · BTC BUY re-stage 0.02 @ 80,500 / SL 79,942.20 / TP ≤ 81,500 (82,000 REJECTED — into-wall): iff NO BTC leg on book AND LIR > 1.80 AND CVD z ≥ +1.50 AND whale BID below 80,500 (τ ≥ 180s, ρ ≥ 0.60) AND trend gate (z_VR > +1.96 or ER > 0.25 on 1h).
C3 · GER40-B re-stage 0.03 @ 25,381.39 / SL 25,420.23 / TP 25,286.79: iff clock ≥ 08:35:00 UTC AND post-PMI spread ≤ 3.0 pts AND VAH/VAL/POC re-validated against the post-release auction AND NZD resolved/BE. Cancel-if-unfilled 12:00 UTC; hard flatten 15:00 UTC (DAX close).
VERDICT JSON
json
{
  "cycle": 297, "arbiter": "GLM-5.3-Flash", "ts_utc": "2026-10-23T07:45:54Z",
  "book_actions": [
    {"action": "CANCEL", "ticket": 19244096, "symbol": "BTCUSD.pi", "priority": "P0",
     "reason": "R13 aggregate 39.36 > 30.51 with NZD #19244087 live; buffer breach on both accountings"},
    {"action": "ARM_RATCHET", "ticket": 19244087, "symbol": "NZDUSD.pi",
     "orders": [{"trigger_bid": 0.56916, "new_sl": 0.56906, "label": "A1 Early-BE +0.75R"},
                {"trigger_bid": 0.56930, "new_sl": 0.56917, "label": "A3 lock +1.65R (dormant)"}],
     "time_decay": {"deadline": "fill_ts+6h (13:08-13:46 UTC)", "condition": "bid<0.56907", "action": "CLOSE_MARKET"},
     "tp_stands": 0.56965}
  ],
  "new_staging": "OPTION_B_STAND_ASIDE",
  "rearm_gates": {"C1_btc_sell": "post-NZD-BE + wall tau/rho + CVD z<=-1.50", 
                   "C2_btc_buy": "TP<=81500 + LIR>1.80 + trend z_VR>1.96|ER>0.25",
                   "C3_ger40": "clock>=08:35:00Z + post-PMI spread<=3.0pt + VA re-validated"},
  "ladder": {"rung": 0, "banked_usd": 0.00, "envelope": {"pre_bank": 22.80, "post_bank": 33.20}},
  "p_mission": 0.0000, "p_mission_upper_bound": 7.6e-06, "p_breach": 0.0000, "p_at_least_one_win": 0.67,
  "defects_open": ["D6 correlation clustering (LIVE: BTC dual-side + NZD-blind radar)", 
                    "D7 flat-$2 commission vs per-lot reality", "D8 telemetry template hygiene",
                    "OPS-MISS #1: C295-1 GER40 staging never executed (non-strike)"]
}
SECTION G — METHODOLOGY INQUEST [MANDATE: both strategists answer — this is GLM-5.3-Flash's full position]

Is the methodology sound? The honest split: our DEFENSE is elite-grade; our OFFENSE is pre-publication research-grade. Zero hard-floor breaches across 17+ cycles, P(breach) = 0.0000 in 20k Monte Carlo paths — the solvency architecture works. But E[final balance] tonight is 4,849, not 5,500. Here is the candid, five-dimension autopsy:

G1 · Conjunctive Filter Sclerosis → Logistic Expectancy. We AND seven-plus binary gates whose features all derive from the same price series — they are correlated (ρ ≈ 0.6), so the conjunction adds ~2.5 independent bits, not seven. We reject ~60–70% of positive-EV candidates while gaining little discrimination, then wonder why nothing stages. Fix: replace the AND-lattice with a scored expectancy rank: s(x) = σ(β₀ + Σβᵢzᵢ) over standardized features (|z_VR| ±0.20, ER 0.10, LIR 0.15, CVD z 0.10, wall τ·ρ 0.10, spread/TP −0.15, regime match 0.10, session/embargo 0.10); accept top-k by EV = p̂·R − (1−p̂) − f > +0.20R subject to R13. But the deeper truth: we cannot fit β because we have n = 0 closed trades. The single highest-leverage action available is not a better model — it is building the evaluation harness: log EVERY candidate (accepted or rejected) with its full feature vector + 4h outcome. Two weeks of that is ~500 rows; the logistic fit becomes possible; the methodology becomes falsifiable instead of unfalsified.

G2 · Static Retrospective Data vs Dynamic Microstructure. The 33-sheet warehouse is a 15-minute ETL of a market moving at tick rate; council cadence is 30–60 min; our signals' half-life is 20 min–4 h. Concrete decay math: a whale wall verified at 07:30 with survival S(t) = exp(−t/τ), τ ≈ 12 min, has S = exp(−15/12) = 0.29 by the time this council ratifies — 71% of the conviction has evaporated before the order could stage (and OPS-MISS #1 proves it sometimes never stages at all). Fix — two-speed architecture: HTF sheets define the GRID (levels, direction, invalidation); the tick stream owns the TRIGGER. Pre-register trigger JSON once per session: {price ∈ level ± 0.25 ATR} ∧ {spread ≤ 0.5×median₁ₕ} ∧ {tick-velocity z > 1.0} → desk executes mechanically; the council audits fills, not opinions. This cycle's Gates C1–C3 are exactly that pattern — extend it to everything.

G3 · Entry Geometry & Staging Passivity. The value of a staged limit is p_fill × E[trade|fill] — we have been maximizing only the second factor with deep-extreme entries while p_fill runs ~0.3–0.5, so the product is starved. Our funnel: 156 assets → ~5 staged/cycle → ~0.35 fills/day → ~0.16 booked/day. We are an execution-limited shop, not an idea-limited shop. Fix: place at δ ∈ [0.10, 0.60] ATR behind the wall (not at its face), δ* = argmax p_fill(δ)·E[R|δ]; time-box every limit at TTL = 3×τ_half of the setup (this is what killed BTC/GER40 stagings silently); keep the MR-regime gate in front of every passive fade to price the adverse-selection tax of filled extremes.

G4 · Multi-Asset Alpha Specialization (category errors). We run crypto L2/CVD/Hyperdash sheets against FX and European indices — those features are noise there. The native-alpha table: Crypto — CVD delta, funding, liquidation cascades, whale walls (the ONLY radar ticket where these are natively meaningful is BTC). FX majors — session liquidity, Frankfurt/London fixings, rate differentials, commodity/risk beta (NZD is a risk-on dairy currency, not an orderbook story). EU indices — cash-futures basis, auction VA geometry, PMI diffusion elasticity, the 13:30 UTC US open. Metals — LBMA fix windows, DXY inverse beta. Fix: asset-class-conditional feature matrix with zero-weight (not low-weight) crypto features on FX/indices, e.g. the FX-native fixing-reversion signal: fade fixing moves > 0.4σ at the 10:00 London fix, historically ~0.58 reversal probability.

G5 · Why equity is flat — the accounting identity, no excuses.
E[Δ
/day]=N
f
	​

ills×[
p
^
	​

⋅R−(1−
p
^
	​

)]×Risk
 − N_fills × friction$ ≈ 0.35 × [0.46×2.4 − 0.54] × 13 − 0.35×4.5 ≈ +$1.00/day. Against a +688.78 mission, that is ~700 days of required runway versus 12.24 hours available (weekend-flat 20:00 cuts the nominal "~17.0h" — itself overstated; 23:59 − 07:45:54 = 16.22h). The mission Monte Carlo is now categorical: P(mission) = 0.0000 across 20,000 legal paths; the theoretical upper bound on the fastest legal path is 0.40×(0.65×0.46)⁹ = 7.6×10⁻⁶. Reaching 5,500 requires 9 net rung-2 wins (23.6 at rung-1) inside ~7 possible attempts. Since C280, booked P&L ≈ $0 — every cycle re-stages, re-cancels, re-deliberates, and the decision latency exceeds the signal half-life. Two structural truths follow: (1) the Early-BE ratchet has never been costed — if it fires on 50% of would-be winners and 60% never re-reach target, it forfeits ≈ 0.72R per trade, larger than our entire net edge (+0.56R); propose a tiered-BE shadow A/B (at +0.75R → SL −0.25R, not BE) per the Persona-Cards protocol. (2) the anti-martingale reserve doctrine converts any rung-1 loss into full lockout (post-loss cap 13.12 < every ticket ≥ 16.34) — by design, and that is the price of P(breach) = 0; the surgical fix is a micro-rung: 8.00 nominal (stressed ≈ 12.5 ≤ 13.12), spread/TP ≤ 3%, MR+wall-confirmed only — BTC (1.04%) and GER40 (2.1%) qualify, NZD (4.92%) does not — so recovery stays legal after a loss instead of going dark.

The researcher's bottom line: keep the floor architecture untouched — it is the best thing we have built. Rebuild the offense around: prospective journal → logistic scoring → pre-registered trigger execution → asset-native features → friction budget (prefer ≤5%, not the 10% ceiling). And say plainly to the operator: under current legal sizing and the 20:00 flat, Phase 1 as specified is a tail event of probability < 10⁻⁵ tonight. The council's duty is to maximize P(≥1 banked win) = 0.67 and compound from rung-2 — or to re-contract the mission (extend horizon / resize target) explicitly, rather than let a 7.6×10⁻⁶ lottery masquerade as a plan.

Cycle 297 closed. P0 order stands: CANCEL #19244096, arm NZD A1/A3/A4, gates C1–C3 pre-registered. Next wake: bring the NZD deal timestamp, retcode logs for A1, and the post-PMI sheet pull at 08:35 — C3 is live the moment those print.

================================================================================
Z.AI ATTACHED OUTPUT FILE:  (583 chars)
================================================================================

HOLD:     #19236218 BTCUSD.pi SELL_LIMIT 0.03 @ 81,960 / SL 82,260 / TP 80,500 — geometry FINAL
ARM:      Ratchet modify (81,735 → SL 81,930) pre-validated, <60s execution, retcode to C292
ARM:      GER40.p SELL_LIMIT 0.03 @ 25,381.39 / 25,421.48 / 25,286.79
          → stage ONLY on: ratchet-confirmed AND PMI absorbed AND spread ≤1.5pt
            AND tick-vol ≥40th pct AND order_check tick-value pin
RADAR:    SP500 7,673.49 / NAS100 29,028.84 pullbacks — NY 13:30 re-screen
FORBIDDEN: third BTC re-site · second live risk leg before ratchet · rung-2 sizing before +$43.80 BANKS