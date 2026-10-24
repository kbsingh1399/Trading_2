# Cycle 313 — Co-Equal Council Ruling · cutoff 2026-10-24 00:02:46 UTC

**Nonce** 46044d1a-ecf4-44eb-8c85-769ebc85f29b · **Commit** f73a6513 / tree acde38c4 · **Manifest** 4c273f64 · **Workbook** e855a87f · **Ruling** `b2a5ba2b…` · **TTL** 00:17:46 UTC (≈13 min left at review)

**Headline:** the envelope is clean for the second cycle running — and this time the review refuses to blame the market. I measured the dispatcher's own cadence and found that the 15-second quote gate **cannot be satisfied by any envelope this pipeline can produce**. Every failed cycle in the sequence has one shared cause, and it is a design flaw, not a market condition.

---

## 1. Provenance — integrity verified, again

| Field | Declared | Verified | Result |
|---|---|---|---|
| `risk_policy_sha256` | 4633e4af… | recomputed 4633e4af… | **MATCH** |
| `git_commit` | f73a6513… | on `origin/main`, subject `[as_of 23:58:53 UTC]` | **MATCH** |
| `git_tree` | acde38c4… | `rev-parse f73a6513^{tree}` = acde38c4… | **MATCH** |
| `workbook_sha256` | e855a87f… | blob at commit **and** on disk = e855a87f… | **MATCH both** |
| `evidence_manifest_sha256` | 4c273f64… | blob at commit = 4c273f64… | **MATCH** |
| `excel_freshness_verified` | `null` | audit 8,432 s old | gate open |

`verify_cycle_envelope.py` → `ENVELOPE_INTEGRITY_VERIFIED`. Note the commit's own `as_of` is 23:58:53, **233 s before the cutoff** — that gap is not a bug in the commit, it *is* the freshness failure, quantified.

## 2. The finding: a gate that cannot be passed

I pulled every `live_snapshot_latest.json` from the last twelve commits and measured the interval between generations:

```
gaps (s): 294, 261, 302, 311, 282, 344, 110, 297, 302, 296, 292
median 296 s   min 110 s   max 344 s
```

The quote gate is **15 s**. The pipeline's median cadence is **19.7 × too slow**, and even its fastest observed gap is **7.3 × too slow**. Meanwhile the quote age *at generation* is 0.3–2.8 s — the ticks are fresh, they are simply never exposed at the cutoff. For this cutoff the arithmetic is brutal: the newest pre-cutoff snapshot is 233 s old, and the next is 00:03:46, **60 s after the cutoff**, which is future evidence and fails closed on principle.

This also explains something that looked like progress. Last cycle I reported "Binance L2 depth 169 s, Hyperliquid 173 s — PASS." This cycle the same layers measure **254 s and 258 s — FAIL**. Same pipeline, same data quality, opposite verdicts, purely because the nearest snapshot was 146 s away in one case and 233 s in the other. **Layer status is sampling luck, not data quality** (`DIS-313-04`).

**The fix is structural, not operational:** the 15 s quote rule belongs to an *emission-time preflight*, not to a 5-minute snapshot. I have shipped `Terminal/execution_preflight.py`, which captures one tick, the symbol spec, `order_calc_profit`, `order_calc_margin` and `order_check` inside a single sub-second call, self-checks `0 ≤ available_at − observed_at ≤ 15 s`, and emits a hashed receipt bound to the dispatch nonce. It never sends an order. Run it on the trading host; here it correctly refuses with `MT5_UNAVAILABLE`.

## 3. Inventory and solvency — unchanged and sound

Flat: balance = equity = **4,865.07**, margin 0.00, 0 positions, 0 pendings, risk block `BROKER_VALUED` with 0 tickets. `4,865.07 − 2.00 = 4,863.07 ≥ 4,795.00` → headroom **68.07** (265.07 above 4,600; 215.07 above 4,650).

| Scenario | Stress | Post | Cushion |
|---|---|---|---|
| BTC | 26.00 | 4,837.07 | 42.07 |
| SOL | 29.50 | 4,833.57 | 38.57 |
| **BTC + SOL** | **55.50** | **4,807.57** | **12.57** |
| Sovereign 2×(1.25×25+2) | 70.00 | 4,796.57 | 1.57 |

## 4. Candidate mathematics — and a hurdle I can now compute

**(a) BTCUSD.pi — SELL LIMIT 81,300 / SL 81,780 / TP 79,850 / 0.04 lot.** Mid 81,069 sits 0.26 % below VAL 81,283.68; weekly CVD −142.9 M; entry is 231 pts (2.30 σ) above mid, so the limit asks for a modest pullback into broken value.

- Risk 0.04 × 480 = **19.20** · Reward 0.04 × 1,450 = **58.00** · **R:R 3.02** · spread 16 pts = **0.64** · stress **26.00** → **4,837.07**

**(b) SOLUSD.p — SELL LIMIT 103.60 / SL 104.70 / TP 100.50 / 0.20 lot.** Mid 102.695 is 0.97 % below VAL; weekly CVD −26.2 M. Risk **22.00**, reward **62.00**, **R:R 2.82**, spread 0.23 × 20 = **4.60**, stress **29.50** → **4,833.57**.

### The break-even hurdle (new, and the most useful thing here)

I can't estimate `P_TP`, but I *can* compute the probability the setup must beat, from the barrier geometry alone:

- **BTC**: a driftless walk hits TP first with probability 480/(480+1,450) = **0.24870**, at which point EV is *exactly zero*. Charging the measured spread lifts the break-even to **0.25699** — the trade needs **+0.83 pp** of real directional edge before commission.
- **SOL**: driftless probability 110/(110+310) = **0.26190**; after the 4.60 spread, break-even is **0.31667** — it needs **+5.48 pp** of edge, **6.6 × more** than BTC.

That is a quantitative answer to "which would you rank higher," and it isn't close. SOL's 21 %-of-risk spread makes it a materially worse bet than BTC at otherwise similar structure.

### Horizon mismatch

Measured BTC 5-minute mid-move sd is **100.36 pts** (11 steps; mean |move| 88.55; max 209.50). So SL = 4.78 σ and TP = **14.45 σ**. Pure diffusion needs `(1450/100.36)² × 5 min ≈ 1,044 min ≈ 17.4 hours` to traverse the target — against a **900 s** authorization. The trade cannot complete inside its own TTL; it would have to be carried through the weekend on an unpriced swap and gap basis (no swap table exists; single BTC datapoint −0.81). That is exactly why the two-outcome formula is inadequate, now with numbers attached.

**(c) ETH — veto narrowed.** I must correct my own prior cycle: the Cycle 312 rev3 veto leaned on a +0.8645 book imbalance. Twelve snapshots show imbalance has **sd 0.543, range 1.575, and 8 sign flips in 11 steps** — that reading was noise. The veto survives only on CVD grounds (+54.6 M 24 h absorption and a positive 15 m delta against a SHORT classifier). BTC's headline −0.62 → +0.29 "adverse-selection flip" from last cycle is likewise **retracted** (`DIS-313-02`).

**(d) GER40 / EURUSD / XAUUSD — all closed.** Last ticks 20:00:00 UTC (22:00 CEST), 20:59:59 UTC and 21:00:00 UTC. XAUUSD additionally has **no volume profile at all**, so it could not anchor a structural stop even if COMEX were open.

## 5. Methodology

Four personas, affirmative and adversarial. New empirical evidence this cycle: a 12-snapshot microstructure series (the first time the council has looked at a *distribution* rather than a point), a cadence measurement, a σ-scaled horizon test, and a barrier break-even hurdle. `P_fill` and `P_TP` remain null — the published 0.4197 is an 11/17 Clopper–Pearson bound with `calibrated=false` against a 100-trade minimum, and turning it into `P_TP` would be exactly the small-sample overreach the SOP forbids. `EV_net`, `LCB_5%` and `Utility` are null, not zero.

## 6. Verdict

**`DENIED_FAIL_CLOSED`.** Integrity verified, capital sound, two coherent ideas ranked, and a hurdle computed. Five gates still fail: no quote inside 15 s (structurally impossible), broker session null, native venue null (three of four classes closed), calendar 23,266 s stale, no `order_check`.

The difference from every prior cycle is that the binding constraint now has a name and a measured size. Adding another envelope will not fix it. **`execution_preflight.py` + a broker receipt is the only path that can.** BTC at 81,300 / SL 81,780 / TP 79,850 is the row to test first — it needs 0.83 pp of edge versus SOL's 5.48 pp.
