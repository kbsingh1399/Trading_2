# OMNI Queue Governance Consultation — Ox Alpha / Arena.ai
**Date:** 2026-10-06 · **Scope:** Multi-asset limit-order queue governance, commodity tick-volume VWAP fusion, asymmetric exits, causal parquet ingestion
**Baseline:** `OMNI_Hardening_Audit_20261006.md` (all 13 findings remediated, 109 tests green)
**This delivery:** 5 new/extended modules, 46 new tests → **155 passed / 4 pre-existing environment failures**, zero regressions.

Production frame engaged throughout: 14-asset universe, 3.47M 15m candles OOS-validated, 41 bps round-trip friction, 4,841.23 balance / 4,775 floor / 66.23 cushion, 10–12 USD DD budget, 2 max filled, 5 resting limits under first-fill OCO, 10 s daemon cadence, and the three live orders (SOL 118.50 / ETH 2732.80 / GOLD 4176.00).

---

## Q1 — Multi-asset limit queue governance

### Q1a. Microsecond fill collisions (2 fill while the 3rd is cancelling)

The race is structural: broker-side fill and our cancel are asynchronous IPC events. Between our cancel dispatch `t₀` and the broker's acknowledgement `t₀+τ` (τ ≈ 50–300 ms over the MT5 bridge), any resting order can fill. A policy that stages a replacement or frees capacity inside that window can transiently exceed the 2-filled cap by exactly the number of in-flight cancels.

**The governing invariant is not "never race" — it is "the ledger owns ambiguity."** The architecture already implements the four required properties:

1. **Single writer.** One process owns the intent ledger (OS lock, `run()`); no second client can act on a stale inventory.
2. **Uncertain-cancel semantics.** A cancel that errors, times out, or returns "order unknown" leaves the intent in `UNCERTAIN`; the governor never stages a replacement while `cancel_uncertain_at > 0` and retries the cancel on the next 10 s beat. The worst case is a *duplicate cancel*, never a duplicate position.
3. **Fill-before-expiry reconciliation.** A pending limit that vanishes from the inventory snapshot is checked against deal history *before* it may be marked `EXPIRED` (`_resolve_vanished_limit`); a fill inside the race window reconciles as a position. Evidence-free demotion is impossible: without history the intent is kept (fail-closed).
4. **Capacity accounting that counts in-flight legs.** Staging is vetoed while any intent is `PREPARED/ACKNOWLEDGED/UNCERTAIN`; filled capacity is `len(positions)`, and the first-fill OCO governor purges every remaining limit the moment positions reach 2.

**This consultation adds the missing piece — decoupled capacity gates** matching the production spec:

```python
elif self.entry_mode == "limit" and (len(positions) >= 2 or active_limits >= 5):
    report.update(reason="max_filled_2" if len(positions) >= 2 else "max_resting_limits_5")
elif self.entry_mode != "limit" and len(positions) + active_limits >= 2:
    report.update(reason="maximum_two_positions")   # market mode keeps the coupled cap
```

and `max_stageable = max(0, 5 - active_limits)` for passive staging. Limit staging is gated by *resting* count (5) and *filled* count (2) independently; market entries keep the coupled `positions + limits ≥ 2` cap because an instant fill plus a resting limit is already two risk legs.

**Why the OCO purge bounds the collision loss.** With 5 resting and 2-fills-allowed, the adversarial event is "both fills arrive inside one 10 s beat while 3 more are pending." The purge is idempotent (cancel by ticket; unknown-ticket = already filled/cancelled) and ordered before any new staging. Expected residual exposure:

  E[excess risk] = P(fill during τ for order i) × risk_i ≤ (τ/Δ) · Σᵢ risk_i · μ_fill

With τ ≤ 0.3 s, daemon beat Δ = 10 s and at most 5 resting orders of ≤ 45 USD each, the transient worst case is bounded by the OCO purge to a single beat, and the structural worst case (two fills acknowledged) is exactly the allowed cap. The 3-live-order state (0 filled, 3 resting) is legal in both the old and new gate; the 4th and 5th rest only under the new decoupled gate.

### Q1b. Cancel/replace vs queue priority when the whale shifts (SOL 118.41 → 118.45)

**Queue-value model.** Let our order rest at distance behind a wall of notional `W` with queue-jumping arrivals at rate `λₐ` (orders pricing ahead of us per second) and price-taking flow toward the level at rate `μ` (notional/s). With our queue position `q` (notional ahead of us) and an adverse-move hazard `h` (the wall pulling or price trading through, per second), the fill probability over the order's TTL `T` is approximately

  P_fill(q) ≈ (μ/(μ+h)) · (1 − e^{−μT/W′}),  W′ = W + q,

and the *marginal* queue value of moving forward Δq is ∂P_fill/∂q > 0: every unit of queue we cede to a re-center is paid for in fill probability. A cancel/replace onto a shifted wall resets `q` to the back of the *new* wall's queue and additionally re-crosses the spread risk during the IPC window τ.

**Replace-vs-keep inequality.** Re-center iff

  [P_fill(q_new) − P_keep(q_old)] · E[edge per fill]  >  P(transient shift) · QV_lost + Δfriction,

where `QV_lost = P_fill(q_old) · E[edge]` is the entire queue value at risk if the "shift" is a feint. The inequality is *rarely* true for small shifts, because `P(transient)` is high (spoof/flicker reposts) and `P_fill` differences are second-order in Δq. This is why the implementation is a **hysteresis gate, not a tracker**:

```python
threshold_bps = max(min_shift_bps,               # 5 bps absolute floor
                    2 × MAD(tracked edge shifts),  # noise-adaptive: the wall's own breathing
                    proximity_bps if |mid − limit| ≤ 0.25·ATR else 0)  # 25 bps near the touch
replace iff dwell ≥ 240 s  AND  threshold_bps ≤ shift ≤ 75 bps  AND  recenters < 2
```

Applied to the live SOL case: 118.41 → 118.45 is a **3.4 bps** relocation. It is absorbed at *three* layers before the threshold is even consulted: (1) cluster aggregation tolerance (10 bps) merges the reposted levels into one cluster; (2) anchor liveness match tolerance (15 bps) still sees the primary anchor alive, so no cancel is even considered; (3) the 5 bps shift floor. **The correct action for the SOL order resting at 118.50 is: do nothing.** Queue priority is preserved, zero IPC risk, and the whale's 8.68 M bid remains the anchor with TTL renewed from its observed persistence span.

Only a relocation that (a) breaks the 15 bps liveness match, (b) clears the adaptive threshold, and (c) has itself persisted ≥ 240 s (past the scan's 180 s floor — a flicker filter: a genuine institutional relocation survives 24 daemon beats) earns a re-center, which preserves R-geometry exactly (same volume, same R distance, same hurdle), capped at `max_recenters = 2`.

**The adaptive floor in numbers.** The wall's own micro-movements are tracked per heartbeat (`edge_history`, last 16). If the anchor has been breathing ±20 bps between beats, 2 × MAD ≈ 40 bps and a 17.6 bps relocation is *inside noise* — cancel, don't chase (tested). If the anchor is quiet (±0.2 bps jitter), the floor stays at 5 bps and the same relocation qualifies (tested). Near the touch (within 0.25 ATR) the floor widens to 25 bps because queue value is maximal exactly when fills are imminent (tested).

### Q1c. Book-flow metrics that abort a resting limit BEFORE price arrives

New module `Terminal/Adverse_Selection.py` — `AdverseSelectionMonitor`, wired into every governor heartbeat (10 s cadence, deduped by book timestamp so the window measures feed polls, not heartbeats):

| Metric | Definition | Alarm threshold | Rationale |
|---|---|---|---|
| Book-thinning velocity | d ln(V_defense)/dt on the side defending the order (bids under a buy limit) | rate ≤ −ln2/180 s (halving faster than a 180 s half-life) | The wall's *side of the book* draining is the earliest precursor of a pull-through |
| Book collapse | 2× the thinning rate | rate ≤ −ln2/90 s | A collapse scores 3 alone: the wall is being swept, not rebalanced |
| Cancel-to-trade intensity | notional removed from the defending side ÷ traded notional (window) | CTR ≥ 2.5 | Book is being *pulled* faster than consumed — classic pre-move spoof unwind |
| Aggressor pressure | share of aggressive volume on the side that would run at our level, while mid is within 1 ATR of the limit | share ≥ 0.60 | One-sided tape into the level = the fill we get is the adverse one |
| Spread velocity | bps of spread widening per minute | ≥ 3 bps/min | MMs pulling quotes before a repricing |

**Corroboration rule:** abort at composite score ≥ 2, except collapse alone = 3. A single soft alarm never cancels a resting order — resting limit orders are *supposed* to survive noise; only corroborated flow states or an outright collapse abort. All alarms are journalled in the cancel record (`reason="adverse_selection_hazard", detail.alarms`).

Worked example (tested): SOL buy limit 119.42 resting on a live 4.93 M anchor; the anchor *persists* in L3 but the L2 bid defense collapses from ~24 M to ~2 M notional over 60 s (rate −0.0146/s ≤ −0.0077/s). The order aborts at score 3+ even though the wall itself still rests — exactly the "abort before price reaches the level" requirement, because by the time price touches, the queue ahead has already been consumed by the sweep.

---

## Q2 — Commodity tick-volume VWAP fusion (Gold/Silver MR on MT5 CFDs)

New module `Terminal/Commodity_Microstructure.py`. With no L3 depth on `XAUUSD.pi`/`XAGUSD.pi` but 7,000+ ticks per 15 m candle, the microstructure evidence is reconstructed from the tick tape itself.

### Is plain VWAP σ sufficient? No — use volume-weighted MAD bands

The plain volume-weighted σ is inflated by exactly the outliers that *define* the mean-reversion entry:

  σ_vw² = Σᵢ wᵢ(xᵢ − VWAP)² / Σᵢ wᵢ   ← squared deviations: one news bar dominates
  σ_mad = 1.4826 · wmedian(|xᵢ − VWAP|)   ← 50% breakdown point

On the news-spike pattern (39 quiet bars ±3 pts around 4160, then one 9,000-lot bar spiking to 4188): **σ_vw = 4.77 vs σ_mad = 3.73** — the news bar balloons the plain band by 28% (`ballooning_ratio = 1.28`), while z_plain = 1.34 (no signal) but **z_mad = 1.71 at the wick extreme** (signal). The anchor VWAP + 2σ moves from 4169.6 (plain) to 4169.1 (MAD): the robust anchor is *closer to the market*, so passive entries fill earlier with better queue priority and less adverse selection — and during quiet sessions the two coincide (MAD is a consistent estimator of σ under symmetry: 1.4826 = 1/Φ⁻¹(3/4)), so nothing is lost. **The ballooning ratio itself is a feature:** σ_vw/σ_mad > ~1.2 labels the session news-contaminated, which feeds regime labelling (Q3's stressed bucket).

### The deterministic MR gate (all four conditions required)

```python
commodity_mr_gate(bars, direction)  →  confirmed iff:
  1. z_extreme ≥ 1.75  — the trigger bar's session extreme (the wick), measured
     in MAD σ against the 00:00 UTC session VWAP. Measuring at the *wick* not
     the close is essential: the required close-back has already pulled the
     close inside the band, so z_close understates the extension by design.
  2. wick ratio ≥ 0.50 — the opposing wick is at least half the bar's range
     (pin-bar rejection).
  3. close position ≤ 0.45 (short) / ≥ 0.55 (long) — close back inside the range.
  4. fresh session extreme — the trigger bar's extreme is the session extreme;
     a stale high from earlier bars is not liquidity rejection.
```

Applied to the live GOLD sell limit 4176.00 (anchor "VWAP+2SD @ 4176.09", z ≈ 2.11 plain-σ): the anchor itself is consistent with the robust-band entry zone, but the order rests *without* conditions 2–4 — it will fill into any touch, including a momentum continuation through the band. **Recommendation:** either (a) hold the resting limit but delegate its liveness to the AdverseSelectionMonitor (aggressor pressure ≥ 0.60 into the level aborts before the fill), or (b) require the closed-bar rejection for commodity MR sleeves (the gate above) and stage on the bar close. The residual risk of (a) is the single-tick fill inside one 10 s beat; of (b), the missed session extreme. With 41 bps friction on a 25 bps stop (see Q3), the gate is the cheaper miss.

### Supporting estimators

- **POC/VAH/VAL** — exact tick histogram (`tick_volume_profile`, 480 bins over the session's observed range, 70% value area grown from POC by the standard two-sided expansion), or the bar-level uniform-allocation fallback (`volume_profile`, flagged lower quality). Fed into exits via the new `magnet_price` path (below).
- **Tick-rule delta** (`tick_delta`) — Lee–Ready classification: sign = sign(Δp), zero-increments inherit the previous sign; returns buy/sell/delta notional and the normalized delta. Use as the *absorption divergence*: price prints a new session high while cumulative delta is one-sided against the extreme ⇒ absorption, corroborating the wick rejection.
- **Garman–Klass variance** (`gk_vol`) — 0.5·ln²(H/L) − (2ln2−1)·ln²(C/O), ~7.4× more efficient than close–close on the same bar count, so 14 bars carry the information of ~100. Used both for the Q3 vol regime and (14-bar vs 96-bar ratio) as the regime classifier.

`commodity_override` merges the session-anchored robust VWAP + POC/VAH/VAL into the pivot dict the entry hierarchy already consumes — the MR sleeve gets the same structural anchor vocabulary the crypto sleeves get from L3.

### Structural TP for commodity MR: the VWAP/POC magnet

`Orderbook_Structure.structural_exit` gains `magnet_price` (from `commodity_override`): with no L3 walls on the CFD, the session POC/VWAP acts as the take-profit magnet — the TP front-runs it by 2 buffer ticks (mode `vwap_poc_magnet`), the hurdle flexes to the magnet distance in R, and if the magnet sits inside the net-payoff floor (`min_net_target_r + friction_r`) the candidate is vetoed rather than staged. Real L3 walls, when present, still take precedence (`wall_front_run`).

---

## Q3 — Asymmetric exits: condition the ratchet on asset class × GK-vol × session × sleeve

The uniform ladder (BE 0.80R → lock 0.35R; 1.50R → 0.85R; trail gain−0.65 above 2.0R; target 2.4–2.9R; 24-bar decay) is retained as the **frozen v2 label policy** — uplift training labels stay paired and comparable — and a conditional overlay (`RATCHET_POLICY_VERSION = "omni.ratchet.session_conditional.v1"`) manages live positions. Backward compatibility is exact: `params=None` reproduces v2 bit-for-bit (tested across the gain grid × friction on/off × both directions).

### The friction arithmetic first (it dominates Gold)

With the live GOLD geometry — entry 4176.00, SL 4186.50, R = 10.50 = **25 bps of notional** — the 41 bps round-trip friction is **1.63R**. The cost-aware lock floor is

  lock_min = friction_bps/10⁴ × entry / R + buffer = 1.63 + 0.05 = **1.68R**,

so *any* BE lock before 1.68R gain locks a net-negative outcome; the executable ratchet correctly refuses (the proposed stop would sit beyond the market). Consequences for the user's uniform 0.80R BE on Gold:

- BE@0.80R is un-fundable at 25 bps stops — it either does nothing (cost-aware floor holds the stop) or locks a loss (naive BE). The ladder already handles this conservatively; the point is that **no session conditioning can fix a stop that is 1.6× friction wide.**
- Structural fix: Gold MR stops should sit at the *robust band edge + POC buffer* (≥ 90–100 bps), making friction ≤ 0.45R and BE@0.8R fundable. The alternative — accepting that Gold "BE" is really a 1.68R friction-BE — is what the current code does and is defensible, but it should be a *choice*, not an accident.

### The conditional table (implemented in `Uplift_Model.RATCHET_CONDITIONAL`)

| Class / Session / Vol / Sleeve | BE trigger | 2nd lock | Runner trail | Target | Decay | Rationale |
|---|---|---|---|---|---|---|
| CRYPTO us_hours normal trend | 0.80 | 1.50/0.85 | 0.65 | 2.60 | 24 | Deepest books, momentum pays for itself; run the runner |
| CRYPTO us_hours stressed | 1.00 | 1.50/0.85 | 0.80 | 2.60 | 24 | 2× vol noise would stop out a 0.8R BE instantly; widen everything |
| CRYPTO us_hours calm | 0.75 | 1.50/0.85 | 0.55 | 2.50 | 24 | Tight tape: adverse selection risk low, protect earlier |
| CRYPTO asia normal | 0.90 | 1.50/0.85 | 0.65 | 2.50 | 18 | Thin books: edge decays faster, don't gift back 0.8R |
| CRYPTO weekend | 1.00 | 1.50/0.85 | 0.80 | 2.20 | 16 | Thinnest tape of the week: take what the market gives |
| CRYPTO us_data (13:30–14:00 UTC) | 1.10 | 1.50/0.85 | 0.90 | 2.50 | 24 | Post-print whipsaw; effectively "no fresh BE through data" |
| COMMODITY london/ny normal **trend** | 0.85 | 1.40/0.80 | 0.55 | 2.20 | 24 | Deep liquidity, but gold trends mean-revert locally: bank earlier |
| COMMODITY asia normal **reversion** | 0.90 | 1.20/0.75 | 0.35 (from 1.60R) | 1.80 | 12 | The MR edge *is* the reversion; once it pays, it decays — trail hard |
| COMMODITY london/ny normal **reversion** | 0.80 | 1.30/0.75 | 0.40 | 2.00 | 16 | Same, but liquidity lets the reversion run one more leg |
| COMMODITY us_data | 1.10 | 1.50/0.85 | 0.90 | 2.60 | 24 | CPI/NFP prints: 10 pt gold spikes stop out any tight ladder |
| COMMODITY london/ny stressed | 1.00 | 1.50/0.85 | 0.75 | 2.50 | 24 | Vol regime widens trails across the board |
| COMMODITY london calm reversion | 0.80 | 1.50/0.85 | 0.35 | 1.80 | 12 | Quiet tape: the reversion completes cleanly |
| INDEX ny normal | 0.80 | 1.50/0.85 | 0.60 | 2.40 | 24 | Index momentum in NY hours |
| INDEX asia | 0.95 | 1.50/0.85 | 0.75 | 2.00 | 16 | Overnight index tape is thin and mean-reverting |

Resolution precedence is most-specific-first (class, session, vol, sleeve → class, session, vol → … → class), missing keys fall back to the v2 baseline, and **the friction-aware lock floor always dominates any table value** (tested: at the live GOLD geometry every row locks exactly the 1.68R floor). The regime actually used is stamped into position meta (`ratchet_regime`: policy version, session, vol bucket, GK ratio, sleeve, resolved params) and journalled.

The conditional decay is live: a zero-gain SOL position closes at 18 bars (CRYPTO asia) where the uniform policy would have kept it 24 (tested) — dead inventory is recycled faster exactly when the sleeve's session says the edge has decayed.

### How should Gold trail? (direct answer)

- **Mean-reversion sleeve (VWAP/POC anchored):** trail the *structure*, not the volatility — the `vwap_poc_magnet` TP at the session POC (or VWAP) is the exit; behind it a hard 0.35–0.40R runner trail and the 12–16 bar decay. A plain ATR chandelier in Asia's thin tape whipsaws out of trades that are mathematically complete.
- **Trend sleeve (London/NY continuation):** chandelier on structural swing pivots with the wider 0.55R runner trail; VWAP is the *wrong* trail here — session VWAP lags a trending tape by construction and would cap every winner at ~1.5R.
- **Always:** ATR (GK-scaled) remains the floor for stop validity and the drift guards; the vol regime shifts every trail width as in the table; through 13:30–14:00 UTC data the ladder effectively freezes (BE 1.10R, trail 0.90R).

---

## Q4 — Causal parquet ingestion: zero-leak, zero-latency, 100% crash recovery

New module `Terminal/Causal_Candle_Stream.py` replaces full-recompute candle processing (O(N) per 15 m close, O(N²) per session across 14 assets × 3.47M bars) with an event-sourced stream.

### Causality contract (no future bars, ever)

- A bar **commits only when its close time has passed** (`open_time + 900 ≤ now`); forming bars are rejected and counted (`rejected_forming`). Indicators can therefore never see a partial bar.
- **Disconnects and weekend gaps are ledgered, never filled.** A hole > 1.5 × timeframe emits a gap record `{from, to, missing_buckets}` and sets `gap_flag` on the bar that bridges it (clearing on the next contiguous bar) so the trader can distrust ATR/RSI for exactly one bar. No synthetic candles are invented — a filled gap is a fabricated price path and would leak into every downstream statistic.
- Indicators stay *honest* across gaps by construction: True Range uses the previous close (`max(H−L, |H−prevC|, |L−prevC|)`), so the weekend's jump shows up as one wide TR rather than a silent discontinuity; the session VWAP resets at the 00:00 UTC boundary anyway (the Friday→Sunday gap spans midnight by definition).
- **Broker corrections** (MT5 rewriting a completed bar) are idempotent by `open_time`: a second bar with the same stamp restores the prior snapshot and re-applies exactly once (tested: `state.bars == 300`, ATR equals the batch reference of the corrected history). Stale bars (older than the last commit) are rejected.

### O(1) incremental engine

`IncrementalIndicators` maintains Wilder-recursive ATR and RSI (seeded by running mean over the first 14, then `(prev·13 + x)/14`), the recursive EMA, and the session-anchored VWAP (Σ tp·v / Σ v, reset at UTC midnight) — each **O(1) per bar**, and bit-identical to the batch recursion (`batch_reference` exists only to prove the equivalence in tests; it is never run in production). Per 15 m close across 14 assets: 14 constant-time updates instead of 14 × 96-bar (or × full-history) recomputes.

### WAL crash recovery (100%)

Every state mutation is journalled *before* it happens: `wal/{symbol}_{tf}_wal.jsonl` receives the bar/correction/gap event (fsync), then the updated full-state snapshot (a handful of scalars) after each bar. Recovery (`recover()`) seeks the **last snapshot record** and applies at most the one or two events after it — a crash can leave at most one un-snapshotted bar:

| Crash point | Recovery path | Tested |
|---|---|---|
| Clean (after snapshot) | load snapshot, replay 0 events | ✓ |
| Mid-batch | snapshot + ≤1 bar replay, then resume ingest | ✓ |
| Torn tail write (partial JSON line) | line discarded, state = last snapshot | ✓ |
| Mid-correction (correction journalled, snapshot not) | restore pre-correction snapshot, re-apply corrected bar (1 event) | ✓ |

WAL rotation compacts to a single baseline snapshot every 4,096 events (atomic tmp+rename), bounding both file size and worst-case recovery — corrections only ever touch the most recent bar, so the baseline is always sufficient. Post-rotation recovery is verified identical.

### Parquet reconciliation (the 3.47M-candle store)

`reconcile_parquet(store, bars, now)` — appends newly committed bars, rewrites broker-corrected rows in place (`unique(subset=["time"], keep="last")`), refuses any batch containing a bar whose close time is in the future (`future_bar_rejected` — the store is causally sealed by contract), writes atomically (tmp + `os.replace`), and verifies monotonic unique `open_time` on every write (`parquet_store_corrupt` otherwise). Idempotent re-ingest appends 0 / corrects N. Report gives appended/corrected/total/max_time.

---

## Production drift ports (Omni_Trader)

Your pasted production build carries five drifts vs the remediated workspace; all are now ported *without* unwinding the incident fixes (your paste still carries pre-remediation behaviour in the reconciler and the anchors re-adoption path — those stay as fixed here):

| Drift | Ported behaviour |
|---|---|
| 10 s cadence, bars before manage | `run()` now orders `refresh_broker_history()` **before** `manage_active_positions()` so the ratchet/ATR/drift guards see the freshest completed history each beat |
| 900 s bar throttle | `refresh_broker_history` skips when `now − last_bars < 900` (was already present; now load-bearing with the reorder) |
| Pending drift bound | cancel at `max(6·ATR, 3% of mid)` from the limit (was 3·ATR): wide enough for weekend gaps, tight enough to recycle dead queue priority (tested at the 6·ATR edge) |
| Decoupled capacity | 2 filled / 5 resting gates as in Q1a; market mode keeps the coupled cap (both tested) |
| First-fill OCO | unchanged (purge at 2 fills + correlated-cancel at 1 fill) — matches your production semantics |

---

## File map

| File | Status | Contents |
|---|---|---|
| `Terminal/Adverse_Selection.py` | **new** | Q1c monitor: 5 flow metrics, dedupe, corroboration scoring |
| `Terminal/Order_Persistence_Governor.py` | extended | Q1b hysteresis: dwell 240 s, adaptive MAD threshold, proximity floor, edge history, adverse abort wiring |
| `Terminal/Commodity_Microstructure.py` | **new** | Q2: robust session VWAP + MAD bands, ballooning ratio, POC/VAH/VAL (tick + bar), tick-rule delta, wick rejection, MR gate, GK vol, pivot override |
| `Terminal/Orderbook_Structure.py` | extended | `structural_exit(..., magnet_price=...)` → `vwap_poc_magnet` TP mode |
| `Terminal/Uplift_Model.py` | extended | Q3: `RATCHET_BASE`/`RATCHET_CONDITIONAL`, `ratchet_params`, `session_regime`, `asset_class_of`, `gk_vol_bucket`, params-plumbed `ratchet`/`executable_ratchet`/`replay_episode` (labels unchanged) |
| `Terminal/Causal_Candle_Stream.py` | **new** | Q4: O(1) indicators, causal ingest, gap ledger, corrections, WAL + rotation + recovery, parquet reconciliation |
| `Terminal/Omni_Trader.py` | extended | drift ports above + conditional ratchet wiring with regime stamping |
| `Tests/Test_Omni_Consultation.py` | **new** | 46 tests across all four pillars and the drift ports |

**Suite:** `Tests/Test_Omni_Consultation.py` 46/46 · full suite **155 passed / 4 pre-existing environment failures** (msvcrt lock, MetaTrader5 import, two UI/serve fixtures — unchanged from baseline). All tests offline with broker doubles; nothing touches a terminal.

## Standing invariants (unchanged)

5,000 USD initial capital · 4.50% hard DD floor at 4,775 · 10–45 USD risk per trade · ≥ 41 bps round-trip friction in all sizing/payoff math · max 2 concurrent filled positions · 5 resting limits under first-fill OCO · cognitive layer advisory only, sealed deterministic vectors · legacy candle-only backtest remains non-validating for execution policy.
