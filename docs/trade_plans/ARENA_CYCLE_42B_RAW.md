🏛️ ARENA.AI COUNCIL — CYCLE 42B · CORRECTIVE ADDENDUM

Cycle Timestamp: 2026-10-12 13:33:00 UTC · generation ac1877c104284ba7a40f48a92460eacd @ 13:31:20 UTC
Disposition: 🔴 ETHUSD.pi PROPOSAL WITHDRAWN IN FULL. Three flaws accepted, one citation corrected, one piece of evidence rejected as unstable. Ledger pushed 7f53c56.

FLAW 1 — ACCEPTED ON THE ARITHMETIC. THE CITATION IS WRONG.

Verified: ETH mid 2,524.55, ATR_14 8.7571. Entry 2,495.00 sits 29.55 USD = 3.3744 ATR below mid. A 2.0 ATR cap implies a minimum entry of 2,507.04. The proposal fails.

The failure that actually matters is internal, not codified. In Section 4 of my own Cycle 42 report I rejected SOL SHORT (4.51 ATR), ETH SHORT (4.86 ATR), SP500 LONG (5.65 ATR), EURUSD LONG (30.77 ATR) and GBPUSD SHORT (38.44 ATR) as spurious on exactly this criterion — then proposed ETH LONG at 3.3744 ATR without applying it. I held the test in my own hands and applied it selectively. That is worse than not knowing the rule, because the report reads as though the screen was uniform.

⚠️ But the rule is not where the audit says it is

I read the playbook's headings and searched it directly:

§4 is titled "Empirical Lessons Learned from Session Chat History" — a table of ticket forensics (#18791527, Cycle 40/40B BTC TP, #18785248, #18734917, #18740569, #18723453, Retail Altcoins). It contains no Entry Proximity Rule and no ATR cap.
The <= 2.0 ATR bound does exist, at §6.B lines 272 and 274 — and it governs Mandate 3, auditing unfilled orders, not Mandate 1 proposals:
L272: "(A) Viable & Wait to be Filled As-Is: …distance <= 2.0 ATR…"
L274: "(C) Delete / Cancel Immediately: …price drifted > 2.0 ATR away…"

Action for the desk: as written, a Mandate 1 new-order proposal has no codified proximity bound at all. The margin argument says it should have one. Amendment recommended for §3.A or the §5 checklist.

Margin — now exact: mt5.order_calc_margin = **$1,322.35**, matching my Cycle 42 estimate to the cent and closing the item I had flagged unverified. Encumbering $1,322.35 (29.84% of free margin) on an order needing a 3.37 ATR crash merely to reach entry is poor allocation irrespective of any rule.

FLAW 2 — CVD HALF ACCEPTED. L2 HALF REJECTED AS UNSTABLE.

Accepted: CVD is deeply negative on all three windows (−877,846 / −2,129,136 / −2,456,165). I disclosed this as Caveat 3 in Cycle 42 and recommended the trade anyway. Disclosing a disqualifier and then overriding it is not analysis — it is a warning label on a decision already made. That was the wrong call.

Not accepted as stated: the audit cites book_imbalance = −0.9688 (63:1 ask-heavy). Re-polled across three generations:

Generation	bid	ask	book_imbalance	Ratio
ac1877c1	$28,465.87	$336,019.88	−0.8438	11.8:1 ask-heavy
7442c212	$350,435.07	$94,994.34	+0.5735	0.3:1 bid-heavy
0b162e6a	$75,254.02	$132,656.46	−0.2761	1.8:1 ask-heavy

The sign flipped from +0.5735 to −0.8438 inside ~2 minutes. My own Cycle 42 reading (bid-weighted) was also genuine at its generation. Neither figure can disqualify or qualify a setup.

🔴 Systemic finding — this is the third volatile feed
Cycle	Feed	Observed behaviour
41	whale_walls_l3 counts	0 eligible across all 24 assets, then 329–585
42	cvd_1m_buckets	BTC 15m: −780,892 → +768,227 → +4,405,681
42B	book_imbalance	+0.5735 → −0.2761 → −0.8438 (sign flip)

Recommendation: any orderflow limb gating a trade on a single generation of these three fields should require confirmation across ≥ 3 consecutive generations. I will hold myself to that from Cycle 43.

FLAW 3 — THE OMISSION IS ACCEPTED. THE RATIO NO LONGER REPRODUCES.

Accepted without qualification: I never computed an overwhelm ratio. Cycle 42 disclosed the $44.24M cascade as Caveat 1 but never set it against the $13.23M wall. Comparing forced fuel to resting defence is the most obvious calculation in the Liquidity Bunker framework, and I skipped it. At generation 3d9e0b25 the audit's arithmetic was right: $51.78M vs $13.23M = 3.91:1.

Does not reproduce now: at ac1877c1 the [2,490, 2,500] band publishes only the $7.53M sell-stop cluster — the $44.24M cascade has drained out of it, and the $13.23M wall no longer sits within $3 of 2,496. The fuel that defined the risk moved in eleven minutes.

That strengthens the withdrawal rather than weakening it. A setup whose central risk metric changes by an order of magnitude within one cycle cannot be staged as a resting order. The honest statement is that the [2,490, 2,500] zone is in flux — neither my original caveat nor the audit's ratio is the live picture.

FLAW 4 — ACCEPTED

1.06 × 78.00 = **$82.68**. I quoted unscaled 78.00 as "reward" beside lot-scaled $10.07 risk. Mixing scaled and unscaled figures in one table is a defect even where the ratio is invariant — 78.00/9.50 = 82.68/10.07 = 8.2105 either way.

FINAL STATE
Item	Value
Mandate 1 — new orders	0 (ETHUSD.pi withdrawn)
Mandate 2 — #18795304	HELD AS-IS (audit-ratified). SL 108.79, TP 113.40, R:R 2.3897. Do not tighten into the $21.95M band.
Mandate 3 — pending	[] — nothing to audit
Joint worst-case risk	$10.88 (SOL only)
Stressed post-stop equity	$4,863.30 = +68.30 over buffer, +88.30 over hard floor ✅
Margin encumbered	$440.60 — the $1,322.35 ETH reservation released
Capacity	1 of 4 · correlated crypto capped at one ticket ✅

Across Cycles 40, 41, 42 and 42B I have proposed exactly one new ticket, and it did not survive verification. The correct reading of four cycles is that this market is not offering tradeable confluence — not that a series of unlucky arithmetic slips intervened.

Three playbook amendments recommended
§3.A / §5 — codify the proximity bound for Mandate 1. No such bound currently binds new proposals; only §6.B governs already-resting orders.
§3.B — require an overwhelm ratio. Forced fuel inside [min_price, max_price] vs resting L3 defence; above 2:1 reject regardless of R:R.
§1/§2 — require ≥3-generation confirmation for book_imbalance, cvd_1m_buckets, whale_walls_l3 counts.

Ledger: 7f53c56 — pushed first attempt, rebased over eaf1896, 1 file / 66 insertions, no telemetry. All four signed entries (C40B / C41 / C42 / C42B) confirmed on the remote; local HEAD == remote HEAD.

What I ran and what came back: read the playbook's full heading structure and grepped it for proximity / 2.0 ATR / deep-fish / encumber, locating the bound at §6.B L272/274 rather than §4; re-polled ETH's book_imbalance across three generations and caught the sign flip; recomputed the [2,490,2,500] fuel and found the $44.24M cascade had drained, leaving $7.53M; recomputed entry distance at 3.3744 ATR and the 2.0 ATR floor at 2,507.04; re-verified 10 addendum figures and found one error — my own 3.95:1, which should have been 3.91:1, the audit's figure — and corrected it before committing. No decision-gate script was executed.

What I got wrong in Cycle 42, stated plainly: I applied a 2.0 ATR reachability test to reject five setups and then exempted my own recommendation from it; I disclosed a persistently negative CVD and recommended against it anyway; I never computed the overwhelm ratio that the framework exists to compute; and I mixed scaled and unscaled figures in one table. The audit was right on all four. Its §4 citation was not, and the desk should know the rule it is relying on is not actually written down.