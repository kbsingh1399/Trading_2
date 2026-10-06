# OMNI Institutional Hardening Audit — 2026-10-06
## End-to-End Execution Chain, Branches, and Incident Remediation (A / B / C)

**Scope:** forensic trace and remediation of the live autonomous 15-minute MT5 trader
(Blueberry Markets 5064568, balance 4,841.23 USD, hard floor 4,775.00 USD, 14-asset
universe, 41 bps mandatory round-trip friction, max 2 concurrent exposures).
**Status:** all findings below are remediated in code on this branch and locked by
`Tests/Test_Omni_Hardening.py` (22 tests) plus the existing 87-test suite, which is
unchanged from its pre-remediation baseline.

---

## 1. End-to-End Execution Chain Audit

### 1.1 Lifecycle trace (`run` → `_dispatch`)

```
run()  [~1s cycle, OS file lock, single writer]
 ├─ refresh_background()          poll all 14 feeds every 5s (thread pool, 8 workers)
 │    └─ flow.observe_walls()     L3 wall persistence tracking (30s freshness)
 ├─ manage_active_positions()     inventory → account → equity guard → reconcile
 │    ├─ _reconcile()             intent ↔ position ↔ deal-history convergence
 │    ├─ ratchet SL (executable_ratchet, friction-aware 0.35R/0.85R/runner)
 │    ├─ OCO governors (capacity=2, correlated-pair cancel at ρ≥0.55)
 │    ├─ structural invalidation (macro blackout, >3×ATR drift)
 │    └─ [NEW] OrderPersistenceGovernor.heartbeat()   TTL / wall-pull / re-centre
 ├─ refresh_broker_history()      512 M15 bars per asset every 900s; covariance
 │                               validate → Ledoit-Wolf refit on staleness
 ├─ capture_quotes()              broker quote sampling for uplift labels
 └─ evaluate_market()             minute-14 window [840+cadence_s, 898)
      ├─ slot idempotency latch (last_slot persisted BEFORE inference)
      ├─ capacity: positions + STAGED_LIMIT intents < 2
      ├─ per-asset: features → vetoes → sleeve → geometry → sizing
      ├─ uplift gate (paired replay estimand) + cognitive committee (advisory)
      └─ _dispatch()              PREPARED → ACKNOWLEDGED / STAGED_LIMIT / UNCERTAIN
```

### 1.2 Findings register

| ID | Severity | Finding | Disposition |
|----|----------|---------|-------------|
| F-01 | **Critical** | **Incident A — rigid limit TTL.** Live limits expired after a fixed `limit_expiration_seconds` bound to the decision cycle (default 3600s, broker-side `ORDER_TIME_SPECIFIED` in server time), while the PDL sweep the order was front-running resolved over 2–6 hours. The reconciler then silently marked intents `EXPIRED` and nothing re-staged: the book sat in cash through the entire reclaim. | §2: GTC persistent orders + survival-hazard TTL governor. |
| F-02 | **High** | **Dead wall-freshness clause.** The whale-bid/ask filters in `evaluate_market` referenced `globals().get("now")` / `globals().get("epoch")` — module-level names that do not exist in `Omni_Trader`. The clause short-circuited to *always true*, so stale L3 quotes (any age) qualified as verified whale walls. | `wall_clusters()` with a real `observed_at` freshness gate (≤30s); regression-tested in `Tests/Test_Microstructure.py` §6. |
| F-03 | **High** | **Self-vetoing cognitive wait.** The dispatch gate checked `book_as_of` of the *candidate's original* payload, but `refresh_background()` is not called during the up-to-28s inference wait, so the stamp aged past `max_book_age` and the post-inference dispatch was dropped wholesale — a systematic waste of the entire committee cycle. | Dispatch gate now re-checks the freshest polled book per asset. |
| F-04 | **Critical** | **Limit-expiry / fill race (`_reconcile`).** `positions_get` and `orders_get` are two IPC calls. An order that filled between them vanished from `pending` without appearing in `positions`; the `elif` precedence marked the intent `EXPIRED` *without ever consulting deal history*, orphaning a live filled position (no metadata → `initial_r` unknown → time-decay exit disabled) and freeing the capacity slot for a double exposure. | `_resolve_vanished_limit()`: history-first classification (`FILLED_CLOSED` / `filled_open→ACKNOWLEDGED` / `EXPIRED` / `uncertain`); bridge gains `intent_filled()`. |
| F-05 | **High** | **Unresolved-intent deadlock.** A crash between `PREPARED` persistence and `order_send` (or a timeout marked `UNCERTAIN`) permanently blocked all future entries with `unresolved_execution_intent`; no aging path existed. | Evidence-based aging: `PREPARED` >120s / `ACKNOWLEDGED,UNCERTAIN` >300s demote to `ABANDONED` **only** when the broker's deal history proves no fill; `ABANDONED` intents still reconcile if a phantom fill appears later. |
| F-06 | **High** | **Split time base across the IPC bridge.** Ticks were normalised to UTC (`_normalize_tick_msc`) but bar, position and pending-order timestamps were left in broker **server** time. On any non-UTC server: (a) `completed_statistics` sees every bar as "in the future" → per-asset vetoes / covariance refit failures; (b) position `time` is 3h in the future → the 24-bar time-decay exit can never fire (fail-open on a mandated risk exit). | `_utc_offset_seconds()`: per-symbol 30-min-snapped offset estimated from a fresh tick (0 when the server is UTC), applied to bars, positions, and pending orders. |
| F-07 | **Medium** | **DST-fragile broker expiration.** `stage_limit_order` computed `broker_now = tick.time` with a hard-coded `+10800` fallback — wrong for half the year on EET servers and across US/EU DST skew. | Persistent orders carry **no broker expiration at all** (`ORDER_TIME_GTC`); deadlines are UTC-local in the governor. |
| F-08 | **Critical** | **Incident B — unattested cognitive statistics.** The committee prompt supplied raw features and free prose; nothing constrained numeric claims to the data. An auxiliary persona asserted "+1.8σ CVD divergence" and an "empty ask book above 122.00" when the feed showed +0.92σ and an 8.04M wall at 122.34. | §3: sealed feature vector (SHA-256, per-asset hash chain) + mechanical numeric attestation; violations reject the decision and journal `cognitive_fabrication_rejection`. |
| F-09 | **High** | **Incident C — static R-target TP.** `target_r = 2.5` produced TPs without consulting overhead liquidity; the SOL plan staged 123.00 beyond an 8.04M sell wall at 122.34. Pullback and breakout also shared one passive entry path despite opposite microstructure geometry. | §4: `structural_exit()` wall-front-run TP with dynamic hurdle and net-payoff floor; deterministic sleeve classification (S1 passive / T1 aggressive). |
| F-10 | Medium | Capacity accounting `max_stageable = 2 - len(positions) - len(pending)` counts **manual/foreign** orders and positions against the OMNI budget. Conservative but can silently idle the system on a manually traded account. | Documented; unchanged by design (fail-closed). Operator note: keep account 5064568 single-purpose. |
| F-11 | Medium | `refresh_broker_history` pulls 512 bars × 14 symbols sequentially on one thread inside the 1s manage loop (up to multi-second stall per 900s). | Documented; acceptable at current scale. Recommendation: move to the data pool with a time budget if cycle jitter is observed in `runtime_errors.jsonl`. |
| F-12 | Low | GTC persistence risk: a daemon that dies and never restarts leaves working orders at the broker. | Mitigated by: single-writer lock; governor registry persisted in state (`resting_orders`) and re-adopted on restart; hard 6h cap enforced from `staged_at` even without renewal; MT5_Sentinel watchdog remains the outer alarm. |
| F-13 | Low | Fill-drift guard at reconciliation (`> 0.05·R`) warns but does not act. | Kept as journalled signal; the sizing re-check at dispatch already re-derives risk from the live quote. |

**Preserved invariants (verified unchanged):** 5,000 USD initial capital and 4.5%
drawdown latches; 10–45 USD conviction risk with `min(45, …)` caps; 2-position
cap incl. resting limits; 41 bps floor in `cost_bps`; minute-14 cadence and slot
idempotency; paper/live parity of the ratchet; single-writer OS lock;
fail-closed posture of every broker ambiguity (`uncertain` never retried blind).

---

## 2. Incident A — Dynamic Order Persistence & TTL Governor

### 2.1 The mathematics

Model the anchor wall's remaining life as exponential with a memoryless hazard
estimated from its observed persistence `s` and a 30-minute regularising prior
`s₀`:

```
λ̂ = 1 / (s + s₀),          s₀ = 1800 s
TTL(p*) = -ln(p*) / λ̂  =  -ln(p*) · (s + s₀),      p* = 0.35
```

The TTL is the horizon at which the modelled survival probability of the wall
falls to 35% — i.e. we rest no longer than the wall is likely to still defend
us. `-ln(0.35) ≈ 1.05`, so a wall observed for 2h earns ≈2.6h of resting life;
the policy band is clipped to **[2h, 6h]** (`--ttl-min 7200 --ttl-max 21600`).
While the wall keeps being observed the deadline is **renewed monotonically**
(each heartbeat: `deadline ← min(max(deadline, now+TTL), staged_at + 6h)`),
and the hard cap from `staged_at` can never be outrun by renewal.

### 2.2 The mechanism (`Terminal/Order_Persistence_Governor.py`)

* **Staging:** S1 candidates are sent as `ORDER_TIME_GTC` with **no broker
  expiration** (F-07). The governor owns the deadline in UTC on our side of
  the IPC. The 15-minute decision cadence is untouched: the governor acts on
  the ~1s manage cycle, so a multi-hour order never depends on minute-14.
* **State-machine hygiene:** the registry is keyed by intent id and released
  the moment the intent leaves `STAGED_LIMIT` or the order leaves the pending
  inventory — disappearance semantics belong exclusively to `_reconcile`
  (which is now fill-aware, F-04). No status is invented; no slot is double
  counted (`evaluate_market` continues to count `STAGED_LIMIT` intents toward
  the 2-position cap).
* **Wall tracking:** every heartbeat re-scans the entry side of the book
  (band `limit ± 2.5×ATR`, freshness ≤60s). The **primary anchor** is the
  cluster the limit front-runs. Pulled/thinned below 40% of anchored notional
  (or absent) → **cancel** (`anchor_wall_pulled`) — the adverse-selection
  guard.
* **Cancel/replace on wall shift:** if the primary is pulled but a qualifying
  institutional cluster (≥150k, within 75 bps, >5 bps actual shift) has
  re-posted, the governor cancels and re-stages at the new edge + 1 tick,
  preserving **R-geometry** (same volume, same R distance, same hurdle →
  identical USD risk and friction). Max 2 re-centres per order.
* **Fill-race safety:** a cancel returning `uncertain`/`unknown-order` marks
  the order `cancel_uncertain` and **never** stages a replacement in the same
  cycle; the cancel is retried on the next beat and the reconciler resolves
  any fill in the window.
* **Drift bounds:** cancel at >1.5×ATR (no anchor) or >3.0×ATR (anchored)
  adverse drift; the pre-existing 3.0×ATR structural check in
  `manage_active_positions` remains as defence in depth.
* **Crash/restart:** registry persisted to `state["resting_orders"]`,
  re-adopted on boot, stale entries cancelled on first heartbeat (F-12).

### 2.3 Why this fixes the SOL PDL sweep

On 2026-10-06 the sweep at 119.70 with a 4.93M bid at 119.41 justified resting
limits at 120.84/120.31/120.00 for the **2–6 hour** horizon over which the
discount liquidity was actually swept. Under the old regime the order died at
`expiration_seconds` and the slot was consumed. Under the governor: the order
rests GTC; TTL is continuously re-derived from the *live* wall persistence;
the order survives exactly as long as the wall does, and is pulled the moment
the whale support is.

---

## 3. Incident B — Sealed Deterministic Features & Numeric Attestation

### 3.1 Sealed vector (`Terminal/Deterministic_Features.py`)

The cognitive committee now receives **only** `snapshot.econometrics` — a
canonically serialised vector (`SEAL_KEYS`, sorted keys, 6-significant-digit
rounding) of pre-computed statistics from the normalizer pipeline:

| Key | Definition |
|-----|------------|
| `l2_robust_z` | MAD-scaled robust z of L2 imbalance: `z = (x − median)/ (1.4826·MAD)`, window 256, ≥24 obs, clipped ±3 (existing) |
| `aggressor_robust_z` | **[NEW]** same MAD z over the 60s exponentially-decayed aggressor (CVD) imbalance — the ground truth for the "+1.8σ" claim |
| `wall_imbalance_robust_z` | **[NEW]** MAD z of persistence-weighted whale imbalance |
| `friction_adjusted_fuel_ratio` | **[NEW]** `target_fuel_usd / (target_friction_usd + friction_ref_usd)` where `friction_ref_usd` is the 41 bps round-trip on a minimum-risk reference position (stop = 1.5·ATR, risk = `min_risk`) |
| `friction_bps`, `ffr`, `confluence`, `quality`, … | existing deterministic quantities |

Each seal carries `digest = SHA256(canonical_json(values))` and a per-asset
hash chain `chain_digest = SHA256(prev_chain ‖ digest)` persisted in
`state["feature_chain"]` — retro-editing any journalled vector is detectable
(`verify_seal`), and the chain head advances one seal per asset per slot.

### 3.2 Numeric attestation (the mechanical anti-hallucination gate)

Every numeric literal in `analyst_thesis`, `critic_objection` and
`rationale_summary` is extracted (K/M/B suffixes, percentages, signs,
thousands separators) and must match a numeric leaf of the snapshot:

* statistics `|v| ≤ 10`: within 2.5% relative, or a 0–2 decimal rounding;
* magnitudes (prices, notionals): within `max(0.02, 0.1%·|v|)`, or a **1–2
  decimal** rounding — integer-rounding a two-decimal price ("122.00" for
  122.34) is deliberately *not* an admissible variant;
* notionals ≥ 1000 may additionally be cited to 1–3 significant digits;
* small integer prose ordinals ("within 2 hours", "3 walls") are exempt.

Any unmatched claim ⇒ the decision is **rejected**, journalled as
`cognitive_fabrication_rejection` with the offending tokens, and the trader
treats it as an abstention. The exact Incident B output ("+1.8 standard
deviations", "empty ask book above 122.00" against a sealed +0.92 and a wall
price 122.34 / 8.04M — now included verbatim in `snapshot.walls`) is
reproduced and rejected in
`test_incident_b_exact_hallucination_is_rejected`.

**Boundary honesty:** attestation bounds *numeric* fabrication. Qualitative
inversions ("empty book") cannot be caught by number matching alone — they are
made **harmless** instead: exits, stops and sizing are computed exclusively by
the deterministic pipeline (§4), the committee is advisory on an
already-vetted candidate, and its `support_refs`/`invalidation_refs` must
resolve to real snapshot nodes. Fabricated statistics now fail loudly; fake
structure can no longer move money.

---

## 4. Incident C — Sleeve Decoupling & Orderbook-Aware Structural Exits

### 4.1 Deterministic sleeve classification (`classify_sleeve`)

```
T1_BREAKOUT  iff  liquidity_vacuum (opposing magnet present, zero target fuel)
             or   efficiency_ratio ≥ 0.35 AND |aggressor_imbalance| ≥ 0.35 AND tape aligned with direction
S1_PULLBACK  otherwise
```

* **S1 (pullback):** passive limit ahead of verified absorption walls —
  entry `edge + 1 tick` above the top qualifying BUY cluster (≥150k,
  ≥180s persistence, ≤30s fresh — the F-02 fix makes the freshness clause
  real), falling back through the FVG-CE / VWAP-1σ / S1 / P hierarchy.
  Staged **GTC under the governor** (§2).
* **T1 (breakout):** aggressive market entry into the vacuum — even when the
  process runs `--entry-mode limit` (`candidate.entry_mode` overrides).
* Both sleeves retain the full veto stack (confluence ≥ 0.35, FFR ≥ 0.50,
  covariance/sector conflicts, basis, spread, uplift gate).

### 4.2 Structural take-profit (`structural_exit`)

Scan the profit side of the L3 book (top 20 clusters, first cluster with
notional ≥ **2.0M USD** within 3.5R):

```
wall_r = (wall_edge − buffer·tick − entry) / R          (LONG; symmetric for SHORT)
TP     = entry + min(wall_r, 2.50R)                     if wall_r < 2.50R   → wall_front_run
TP     = entry + 2.50R                                   otherwise           → ratchet_band (cap 2.75R)
veto   if wall_r < 1.50R + friction_r                    → net_payoff_insufficient
```

* The TP **front-runs** the first major overhead cluster by `buffer_ticks`
  (2 ticks) — never stages beyond it. In the SOL geometry (entry 119.42,
  8.04M wall at 122.34) the TP snaps to 122.32 instead of 123.00.
* The R-multiple hurdle **flexes** with wall geometry (e.g. 1.93R when the
  wall binds) and the friction floor is evaluated on the *depressed* hurdle —
  a wall too close to clear `1.5R + friction` vetoes the candidate outright.
* The hurdle flows into the uplift gate (`candidate_net_target_r`), so the
  model sees the true net expectancy of the wall-clamped exit.
* SL remains liquidity-anchored (whale shield `edge − 2 ticks`, swing anchor,
  1.5×ATR volatility stop — widest of) with a new runaway guard: veto if the
  resulting stop exceeds 2.5×ATR (`stop_width_runaway`).

### 4.3 Governor interplay

While an S1 limit rests, the TP stays attached to the order; a
cancel/replace re-derives `sl/tp` from the preserved R-geometry, so a shifted
wall never leaves a stale target behind.

---

## 5. Code Map (drop-in)

| File | Change |
|------|--------|
| `Terminal/Orderbook_Structure.py` | **NEW** — pure wall-cluster analytics, hazard TTL, `structural_exit`, `classify_sleeve`, anchors, liveness. No I/O. |
| `Terminal/Order_Persistence_Governor.py` | **NEW** — GTC resting-order lifecycle: TTL renewal, wall-pull cancel, cancel/replace, fill-race safety, state export. |
| `Terminal/Deterministic_Features.py` | **NEW** — sealed vector, SHA-256 chain, numeric claim extraction and attestation. |
| `Terminal/Omni_Trader.py` | Governor + sealer wiring; `wall_clusters` replaces the dead `globals()` filters; sleeve routing; structural TP after friction is known; fill-aware `_resolve_vanished_limit`; intent aging (`ABANDONED`); fresh-book dispatch gate; anchors persisted on intents. |
| `Terminal/Risk_Sizing_Engine.py` | `aggressor_robust_z`, `wall_imbalance_robust_z`, `friction_adjusted_fuel_ratio`, `friction_bps` added to `features()` (additive schema). |
| `Terminal/Cognitive_Engine.py` | `build_snapshot(..., sealed=)` with attestation block, wall prices exposed; `evaluate_snapshot` runs the fabrication gate; `record_rejection` ledger. |
| `Terminal/MT5_Execution_Bridge.py` | `stage_limit_order(..., persistent=True)` → GTC/no expiration; `intent_filled()`; UTC offset estimation applied to bar/position/order timestamps. |
| `Terminal/OF_Strategy.py` | `--ttl-min`, `--ttl-max`, `--no-persistent-limits`. |
| `Tests/Test_Omni_Hardening.py` | **NEW** — 22 forensic tests reproducing incidents A/B/C and races F-02..F-06. |
| `Tests/Test_Microstructure.py` | Whale-eligibility section now exercises `wall_clusters` (incl. a stale-wall rejection case). |

State schema is additive: `resting_orders`, `feature_chain`, `anchors`,
`hurdle_r` join the existing `omni.state.v1` payload; old state files load
unchanged. No journal field was renamed or removed.

## 6. Verification

* `Tests/Test_Omni_Hardening.py` — 22/22 pass (TTL math, renewal, pull-cancel,
  shift-replace with risk invariance, uncertain-cancel safety, seal
  determinism/tamper-evidence, Incident B end-to-end rejection, structural TP
  front-run / band-cap / floor-veto / SHORT symmetry, sleeve routing through a
  full `evaluate_market`, vanished-limit race triage, intent aging, GTC
  staging request shape).
* Full suite: **109 passed**; the 4 remaining failures are pre-existing
  environment limitations on non-Windows hosts (`msvcrt`, `MetaTrader5`
  module) and two pre-existing feed tests — byte-identical to the pristine
  baseline verified via `git stash` on this branch.

## 7. Deployment notes

1. Rollout: `python -m Terminal.OF_Strategy --mode mt5-trader --live
   --entry-mode limit` (defaults enable persistent limits, TTL 2–6h).
   Rollback: add `--no-persistent-limits` to restore broker-expiring orders.
2. First restart after rollout: the governor adopts any `STAGED_LIMIT`
   intents from state; orders without anchors still receive TTL+drift
   management. Check `executions.jsonl` for `governor_register` /
   `governor_release` symmetry.
3. Watch new journal events: `governor_cancel` (`ttl_expired`,
   `anchor_wall_pulled`, `anchor_shifted_replace`, `adverse_drift`),
   `governor_replace`, `limit_filled_pending_reconcile`, `intent_aged_out`,
   `cognitive_fabrication_rejection` (in `Data/decision_ledger.jsonl`).
4. The uplift model was trained under `POLICY_VERSION …tp2.5…`; the default
   band target remains 2.50R so wall-clamped exits (hurdle < 2.5R) enter the
   gate as depressed-but-in-distribution `candidate_net_target_r`. Retrain
   the uplift artifact on wall-clamped episodes once ≥500 labelled rows
   accumulate before relying on gate calibration below 2.2R hurdles.
5. Keep account 5064568 single-purpose: manual orders/positions still consume
   OMNI capacity slots by design (F-10, fail-closed).
