# OMNI Continuous Autonomous Brain — Endless Loop & Live Tunnel Control
**Prompt:** OX_ALPHA_62_AUTONOMOUS_ENDLESS_BRAIN_ORCHESTRATION · **Date:** 2026-10-07
**Branch:** `arena/4adf3661-trading-2` (on `52d2895`, the live-tunnel commit)
**Suite:** 281 passed / 4 pre-existing environment failures (was 270 + 11 new; spec required ≥ 267)
**Live proof at spec time:** Ticket #18595858 — `ARENA:TEST_LIMIT_v1` GOLD sell limit 4,182.00 USD staged from the cloud through the tunnel onto account 5064568.

---

## Deliverable 1 — `Terminal/Headless/arena_continuous_brain.py`

The self-contained 24/7 brain loop, driving the laptop muscle exclusively through
the signed tunnel protocol (`omni.arena_remote.v1`, HMAC-SHA256 + nonce + window):

### The cadence

| Rhythm | Action |
|---|---|
| every 15 s (`--interval`, min 5) | `POST /api/v1/market_state` (signed) → live positions, pending orders, full quote specs, per-asset orderflow snapshots, macro block, account equity → **Position Manager**: exact R-multiples, 3-phase ratchet dispatch, 24-bar time decay |
| minute 14 of every candle (:14:45 — after the muscle's own :14:30 execution window closes, so the brain sees this slot's outcome) | `POST /api/v1/evaluate_candle` + market_state → **full tri-specialist deliberation** (`swarm.py`) → macro CLEAR_TO_TRADE / BLOCKED verdict → staging policy |

Run it anywhere with outbound HTTPS:

    python -m Terminal.Headless.arena_continuous_brain
    # ARENA_TUNNEL_URL / OMNI_API_SECRET override the configured defaults
    # --journal Data/Omni/brain/brain_journal.jsonl (default)

### The Position Manager (the live GOLD short #18576872, exactly as specified)

Initial R is locked at first sight of an unprotected stop (entry 4,176.00,
SL 4,186.50 → R = 10.50). Tested against the spec's own numbers:

- **Phase 0** — price ≤ 4,167.60 (+0.80R) → signed `modify_sltp(ticket=18576872,
  sl=4174.425)`: entry − 0.15R (the spec's 4174.40 is the same lock at a coarse
  tick). Dispatched ONCE (phase ledger dedupe).
- **Phase 1** — +1.50R → SL to entry − 0.85R (4,167.075).
- **Phase 2** — +2.00R → runner trail at price + 0.65R (SHORT trails the ask),
  re-armed only on ≥ 0.05R further gain (no 15-second spam).
- **Only-ever-tightening guard** — a computed stop that would widen the current
  one, or land through the current price, is never dispatched.
- **Time decay** — no +0.20R within 24 bars → signed `CLOSE_POSITION`
  (reason `time_decay_24bars`), once. A position that reached +0.20R never
  decays out.

### The deliberation + staging policy (supplement-only, fail-closed)

The brain stages at most ONE validated limit per slot, and only when ALL hold:

1. the muscle abstained this slot (its own decision was not LIMIT_STAGED /
   ORDER_FILLED / PAPER_FILLED) — the brain supplements, never duplicates;
2. capacity: filled + pending < 2 (the spec's "exactly 1 open slot" counting —
   the resting `ARENA:TEST_LIMIT_v1` consumes a slot until it resolves);
3. macro verdict CLEAR_TO_TRADE: no blackout and equity > 4,775.00 USD;
4. |pioneer conviction| ≥ 0.50 on an asset with a live orderflow snapshot;
5. the **taker-delta exhaustion gate** passes on that snapshot (OX_ALPHA_61 D4);
6. sizing sanity: volume = 10.00 USD risk / (1.5 × ATR × contract size) floored
   to the lot step; if even the minimum lot would exceed the budget, the brain
   refuses (the muscle re-enforces the 20.00 USD cap on arrival regardless).

Staged orders carry SL = entry ∓ 1.5 × ATR (the adaptive floor), TP = 2.50R,
comment `ARENA:BRAIN_v1`, and are journalled with their full basis.

### Error recovery (tested)

A dead tunnel, a malformed payload, a non-list positions field — every failure
is counted, journalled, and isolated; the loop never raises and never dies;
recovery on the next successful call is immediate (tested: dead → healthy on
the same engine instance).

## New muscle-side surface (read-only, signed)

- `POST /api/v1/market_state` — positions, pending orders, full quote specs
  (tick/contract/lot geometry so the brain can size locally), asset→symbol map,
  fresh (≤ 120 s) per-asset orderflow snapshots with ATR, macro block, account
  balances. Signed envelope; unsigned → 401. No credentials ever leave.
- `CLOSE_POSITION` command type — the time-decay actuator, through the same
  fail-closed `apply_command` risk path as every other command.
- `BrainClient.market_state()` / `BrainClient.close_position()`.

## Deliverable 2 — `Tests/Test_Continuous_Brain.py` (11 tests, 100 % offline)

Scripted fake client (mutating SL like a real broker), injectable clock, no
network: the GOLD ratchet geometry end-to-end (phase 0/1/2 with re-arm and
dedupe); never-widen / never-cross guards; time-decay close (once, and never
for a healthy position); minute-14 window alignment (once per slot, skipped
outside); the full staging policy matrix (clear / capacity-blocked /
muscle-staged / exhaustion-refused / blackout-blocked); min-lot risk refusal;
dead-tunnel loop survival + recovery; garbage-payload isolation; the
CLOSE_POSITION command on a real bridge; the signed market_state endpoint over
a real socket.

## Operational notes

- **Tunnel URL rotation:** `trycloudflare.com` quick-tunnel URLs change on every
  `cloudflared` restart. The brain reads `ARENA_TUNNEL_URL` at startup — update
  it (or move to a named Cloudflare tunnel with a stable hostname) when the
  muscle restarts. The current URL was not reachable from this sandbox (egress
  restrictions), which the loop treats as a counted, recoverable error by design.
- **Secret hygiene:** the shared secret now lives in `deploy/run_headless.py`
  and the prompt file per your specification. It authenticates command
  INTENT only — every risk cap is enforced muscle-side — but it should be
  rotated once testing concludes, and a named tunnel + secret manager
  (`OMNI_API_SECRET` env, never in the repo) is the steady-state pattern.
- **Where to run the brain:** any always-on box with outbound HTTPS — a cloud
  worker, a second machine, or the laptop itself. It holds no broker
  credentials and cannot reach the broker directly.

## System invariants (all preserved, muscle-enforced, re-tested)

5,000.00 USD initial capital · **4,775.00 USD hard floor** (macro verdict blocks
below it) · **10.00–20.00 USD risk budget** (brain stages 10.00 USD; the muscle
refuses anything above 20.00 USD) · **MAX_CONCURRENT = 2** (filled + pending) ·
41 bps round-trip friction (crypto) / broker spread (metals) · 3-phase piecewise
ratchet (0.80R→0.15R, 1.50R→0.85R, 2.00R trail 0.65R, target 2.50R) · 24-bar
time decay · signed, nonce-protected, idempotent commands only.

## File map

| File | Status |
|---|---|
| `Terminal/Headless/arena_continuous_brain.py` | new — the endless loop + CLI |
| `Terminal/Headless/runtime.py` | + `market_state()` (positions/orders/quotes/orderflow/macro/account) |
| `Terminal/Headless/server.py` | + signed `POST /api/v1/market_state` |
| `Terminal/Headless/brain_client.py` | + `market_state()`, `close_position()` |
| `Terminal/Execution/remote_reconciler.py` | + `CLOSE_POSITION` command type |
| `Tests/Test_Continuous_Brain.py` | new — 11 offline deterministic tests |
