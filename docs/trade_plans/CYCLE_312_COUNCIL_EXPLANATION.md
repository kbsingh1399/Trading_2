# Cycle 312 (rev 3) — Co-Equal Council Ruling · cutoff 2026-10-23 23:56:23 UTC

**Nonce** b8771d9e-73a0-4182-9e02-20aebe701985 · **Commit** b0d2d833 / tree 3be66270 · **Manifest** ce3423dd · **Workbook** e855a87f · **Ruling** `6eab82e5…` · **TTL** expires 00:11:23 UTC

**Delta vs the 23:37 envelope:** this is the **first envelope in the sequence whose integrity actually verifies**. It also carries the sharpest microstructure improvement yet — the L2/depth layers now pass their own freshness limits. Authorization is still `DENIED_FAIL_CLOSED`, but the *reason* has changed from "the evidence cannot be trusted" to "the tradable quote is 145 seconds old and no broker receipt exists."

---

## 1. Provenance — integrity verified, and the earlier defect is closed

| Field | Declared | Independently obtained | Result |
|---|---|---|---|
| `risk_policy_sha256` | 4633e4af… | recomputed 4633e4af… | **MATCH** |
| `git_commit` | b0d2d833… | present on `origin/main` | **MATCH** |
| `git_tree` | 3be66270… | `rev-parse b0d2d833^{tree}` = 3be66270… | **MATCH** |
| `workbook_sha256` | e855a87f… | **blob at commit = e855a87f…, live file = e855a87f…** | **MATCH (both)** |
| `evidence_manifest_sha256` | ce3423dd… | blob at commit = ce3423dd… | **MATCH (at commit)** |
| `excel_freshness_verified` | `null` | audit 21:42:14 UTC (8,049 s old) | NULL — gate open |

The workbook digest — the thing that killed the 23:37 envelope — now matches at the commit *and* on disk, and `stable_sha256()` (double read, size + `mtime_ns` + digest unchanged) passes. The Cycle 312 defect was real and is now genuinely fixed rather than papered over. `Terminal/verify_cycle_envelope.py` returns:

```
verdict  : ENVELOPE_INTEGRITY_VERIFIED
  [PASS] (integrity) risk_policy_sha256
  [PASS] (integrity) git_commit
  [PASS] (integrity) git_tree
  [PASS] (integrity) workbook_sha256_at_declared_commit
  [PASS] (integrity) evidence_manifest_sha256_at_declared_commit
  [FAIL] (gate) excel_freshness_verified
```

The verifier now separates **integrity** from **gate** class: only an integrity failure justifies `DENIED_BAD_CYCLE_ENVELOPE`; a null freshness flag is a gate that must be argued inside the ruling. One residual note: `Data/cycle_envelope.json` committed at b0d2d833 still holds the 23:37 envelope — the dispatch is one generation ahead of the repo. That is a lag, not a digest failure.

**Freshness ledger at 23:56:23 UTC** (snapshot 23:53:57, lag 146 s). Policy: quote 15 s (10 s FX), depth 180 s, liquidation/CVD 900 s, calendar 900 s, broker preflight 0 s.

| Evidence | Age | Limit | Result |
|---|---|---|---|
| BTC / ETH / SOL L1 quotes | 145 / 148 / 146 s | 15 s | **FAIL** |
| Binance L2 depth | 169 s | 180 s | **PASS** |
| Hyperliquid L2/L3 | 173 s | 180 s | **PASS** |
| Liquidation map | 360 s | 900 s | **PASS** |
| MT5 telemetry bridge | 152 s | — | health only, not a receipt |
| `12_Hyperdash` sheet row | 8,517 s | 900 s | FAIL |
| Macro calendar | 22,883 s | 900 s | FAIL |
| EURUSD / GER40 quotes | 10,583 / 14,183 s | 10 / 15 s | FAIL (venue closed) |

This is the first cycle where the depth layers clear their own limits while the *quote* is the sole freshness blocker on crypto. It is a genuine convergence signal: the pipeline is nearly fast enough, and the remaining gap is the last two minutes of broker telemetry.

## 2. Inventory — reconciled flat

`balance = equity = 4,865.07`, margin used 0.00, free 4,865.07, 0 positions, 0 pendings; the 23:53:57 snapshot reproduces it to the cent. Ledger #19267445 closed 22:54 UTC at +66.00 gross / +65.19 net after −0.81 swap; #19270994 canceled. No residual.

## 3. Strict solvency

`4,865.07 − 2.00 = 4,863.07 ≥ 4,795.00` → headroom **68.07** (265.07 above 4,600; 215.07 above 4,650).

| Scenario | Stress | Post | Kernel cushion |
|---|---|---|---|
| BTC only | 26.00 | 4,837.07 | 42.07 |
| SOL only | 29.50 | 4,833.57 | 38.57 |
| **BTC + SOL jointly** | **55.50** | **4,807.57** | **12.57** |
| Sovereign 2×(1.25×25+2) | 70.00 | 4,796.57 | 1.57 |

Floating P/L credited zero. Tier 2 (balance > 4,850) allows 15–25 USD per ticket and at most 2 concurrent tickets; the snapshot's 4-slot policy is overridden. BTC and SOL shorts are crypto-beta correlated, so they are joint-stressed rather than counted as independent.

## 4. Candidate mathematics — two live ideas, both structurally sound

**(a) BTCUSD.pi — value rejection short.** Bid 81,071 / ask 81,086; mid 81,078.5 sits **0.16 % below VAL 81,283.68** (POC 81,650.76, VAH 81,730.56). Weekly CVD −142.9 M, pullback SHORT at 0.42 retrace, ATR14(15m) = 220.03.

- **SELL LIMIT 81,300** (reclaim of the broken VAL) · **SL 81,780** (2.18 ATR, above VAH) · **TP 79,850** (in front of the 61.7 M USD sell-stop cascade at 79,500–79,600) · **0.04 lot**
- Risk 0.04 × 480 = **19.20** (inside 15–25 band) · Reward 0.04 × 1,450 = **58.00** · **R:R 3.02**
- Exit spread 15 pts × 0.04 = **0.60**; stress 1.25 × 19.20 + 2.00 = **26.00** → **4,837.07**

**(b) SOLUSD.p — deep-discount short.** 102.73 / 102.95 versus VAL 103.7012; weekly CVD −26.2 M, 24 h −7.69 M; contract size 100.

- **SELL LIMIT 103.60** · **SL 104.70** (above VAH 104.5604) · **TP 100.50** (above the 1.0 M cluster at 100–101) · **0.20 lot**
- Risk 0.20 × 100 × 1.10 = **22.00** · Reward 0.20 × 100 × 3.10 = **62.00** · **R:R 2.82**
- Exit spread 0.22 × 20 = **4.40 — 20 % of the risk**, the widest measured friction of any row; stress **29.50** → **4,833.57**

**(c) ETHUSD.pi — vetoed, not shortlisted.** A **13.8 : 1 bid-heavy book** (+0.8645 imbalance, 522 k bid vs 38 k ask) and +54.6 M 24 h absorption say buyers control the tape, while the pullback classifier says SHORT. No invalidation level is defensible, so no geometry is proposed — the honest answer is "don't know," not a coin flip.

**(d) EURUSD.pi and GER40.p — closed.** Last ticks 20:59:59 UTC and 20:00:00 UTC (22:00 CEST, still summer time until 25 Oct). A 24/7 crypto venue cannot authorise them.

## 5. The conflict that matters most

BTC's book imbalance flipped from **−0.6216 to +0.2906 in 42 minutes** while price rose 0.77 %. Either that is real bid absorption — in which case a passive sell limit at 81,300 is leaning into a 1.8 : 1 bid stack and faces genuine adverse selection — or the aggregation method changed between snapshot generations. I cannot distinguish the two from the artefacts available, so it is recorded as `DIS-312C-01` (severity 3) and `UNK-312C-07`, and the fix is trivial: publish the estimator version and `generation_id` alongside each derived microstructure field.

The same pattern appears cross-asset: BTC +0.29, ETH +0.86, SOL +0.30, GOLD +0.51 — all bid-heavy — while CVD divergences are bearish. Both readings (broad bid-support regime, or shared artefact) argue against treating short ideas as independent tickets, which is exactly why the pair is joint-stressed to 4,807.57.

## 6. Methodology and calibration

Four personas ran affirmatively and adversarially: regime/calibration (value rejection on BTC and SOL versus ETH's contradiction), fill/microstructure (15 pts BTC vs 21 bps SOL exit friction, stop cascades, maker-vs-taker), solvency/portfolio (26.00 / 29.50 / 55.50 stress, 2-slot cap, correlation), and clock/provenance (digests, ages, session clocks, DST).

`P_fill` and `P_TP` remain **null**. The published `p_win_lower_bound = 0.4197` is an exact one-sided Clopper–Pearson 95 % bound on **11/17** trades with `calibrated = false` and a stated 100-trade minimum — an account-wide diagnostic that would smuggle a small-sample point estimate into the formula if used as `P_TP`. No Brier score, log-loss, reliability curve, ESS ≥ 100, fill model or time-blocked OOS window exists. So `EV_net`, `LCB_5%` and `Utility` are **null, not zero**, and the two-outcome form is explicitly noted as insufficient for a resting limit: unfilled, partial-fill and time-stop are separate branches, and timeout mass is not folded into `P_TP`.

## 7. Verdict and what unblocks it

**`DENIED_FAIL_CLOSED`.** Capital passes, the envelope is now attestable, and two structurally coherent ideas exist. Five binary gates remain failed or unknown at the cutoff: quote freshness (145–149 s vs 15 s), broker session (`null`), native venue (`null`; FX and DAX closed), calendar verification (22,883 s stale) and broker `order_check` (absent).

To re-arm: (1) an envelope with quotes ≤ 15 s **at its own cutoff**; (2) `order_calc_profit` / `order_calc_margin` / `order_check` bound to that nonce; (3) verified venue calendars covering the 2026-10-25 DST roll; (4) a calibrated `P_fill`/`P_TP` with ≥ 100 time-blocked labels. Items 1–2 are engineering, item 3 is a calendar fetch, and item 4 is the only genuine research problem left. BTC at 81,300 with SL 81,780 / TP 79,850 is the first row worth re-testing the moment those land.
