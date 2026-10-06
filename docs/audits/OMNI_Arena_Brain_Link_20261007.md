# OMNI Arena Brain Link — Hybrid Cloud Brain + Laptop Muscle Execution
**Prompt:** OX_ALPHA_61_HYBRID_BRAIN_MUSCLE · **Date:** 2026-10-07
**Branch:** `arena/4adf3661-trading-2` (layered on `adf40b3`, the 24-asset universe baseline)
**Suite:** 267 passed / 4 pre-existing environment failures (was 250 + 17 new, zero regressions)

The Arena.ai cloud brain is now the primary decision-maker with verifiable, signed,
replay-proof command authority over MT5 account 5064568 — while every risk invariant
stays enforced on the laptop, where it belongs.

---

## DELIVERABLE 1 — The secure bidirectional tunnel

### 1.1 Pathway evaluation

| | A. Cloudflare Tunnel | B. MetaApi cloud REST | C. Polling reconciler |
|---|---|---|---|
| Open router ports | **zero** (outbound-only) | zero | **zero** (outbound-only) |
| Dispatch latency | **sub-second** (direct POST) | sub-second | poll-interval bound (5 s default) |
| Replay protection | HMAC + ts window + nonce | provider-dependent | HMAC + ts window + nonce |
| Local gates apply | **yes** (laptop applies) | **no** — cloud code trades live money directly | **yes** |
| Cost | 0 USD (quick tunnel) | paid beyond free tier | 0 USD (Gist/Supabase free) |
| Failure mode | tunnel URL changes on restart | gateway outage = no control | store outage = stale, never wrong |

**Selection: Pathway A primary, Pathway C fallback, Pathway B rejected as the command
channel.** Rationale: the mandate is that Arena.ai *dictates trades* while the
invariants (4,775.00 USD floor, 10–20 USD risk, MAX_CONCURRENT = 2, exhaustion gate)
are enforced where the credentials live. Pathway B hands cloud-side code live-money
authority with none of the laptop's fail-closed gates — it remains available as an
execution *backend* (`Terminal/Execution/headless_rest.py`), never as the command
*channel*. Pathway C is the dead-man's-switch: if the tunnel drops, the laptop keeps
pulling signed commands from any HTTPS JSON store; a dead store means no new commands,
never a wrong one.

### 1.2 The shared security model (both pathways)

`Terminal/Execution/remote_reconciler.py` defines one command envelope, protocol
`omni.arena_remote.v1`:

    {"protocol", "command_id", "type", "ts", "nonce", "params", "signature"}

- **HMAC-SHA256** over the canonical JSON of everything except the signature, key from
  `OMNI_API_SECRET` (env on both sides — never hardcoded, never in a URL).
- **Timestamp window** (30 s default): stale captures are refused.
- **Nonce ledger**: every accepted nonce is single-use — a replayed command is refused
  even inside the window (`nonce_replayed`).
- **Idempotency**: `command_id` is single-use — a store that re-delivers an old command
  is a no-op (`command_already_applied`), never a double order.
- **Command isolation**: one bad command never stops the loop; one dead poll never
  kills the reconciler; every refusal and application is journalled to
  `arena_protocol.jsonl`.

Command types: `STAGE_TEST_LIMIT`, `STAGE_ORDER`, `MODIFY_SLTP`, `CANCEL_ORDER`,
`PURGE_TEST_LIMITS`.

### 1.3 What was built

| Piece | File | Role |
|---|---|---|
| Command protocol | `Terminal/Execution/remote_reconciler.py` | signing, verification, nonce/idempotency ledgers, `apply_command` (shared risk-enforcing applier) |
| Pathway A endpoints | `Terminal/Headless/server.py` | `POST /api/v1/stage_order`, `/api/v1/modify_sltp`, `/api/v1/cancel_order` — signed envelopes, 401 on bad signature/nonce/replay, **409 on any risk refusal**, 200 with the broker result |
| Pathway C reconciler | `Terminal/Execution/remote_reconciler.py` | `RemoteCommandReconciler` — polls any JSON store (`gist_fetch` covers Gist raw / Supabase / Redis-over-HTTP), verifies, applies, purges; injectable clock for deterministic tests |
| Brain-side client | `Terminal/Headless/brain_client.py` | `BrainClient` signs and sends; `publish_to_gist` for Pathway C; CLI for manual verification |
| Laptop setup | `deploy/start_tunnel.ps1` | one-time setup: secret generation, headless service start (`EXECUTION_BACKEND=native_mt5`, fail-closed), cloudflared quick tunnel, verification commands |

Setup is three steps on the laptop (run `deploy/start_tunnel.ps1` as Admin): install
cloudflared, set the shared secret on both sides, start the service + tunnel. The
printed `https://<id>.trycloudflare.com` URL becomes `ARENA_TUNNEL_URL` on the brain
side. Zero router configuration, zero opened ports — the tunnel is outbound-only.

---

## DELIVERABLE 2 — The ARENA:TEST_LIMIT_v1 protocol

The exact sequence (all pieces tested offline against `PaperSimulatedBridge`, and the
same code path runs against `NativeMT5Bridge` on the laptop):

1. **Candidate** — GOLD (XAUUSD.pi) SELL LIMIT at 4,182.00 USD (above the ask — it
   rests, it does not cross; enforced by `_assert_non_crossing`), volume 0.01 lots
   (broker minimum).
2. **Stops** — SL = entry + 1.5 x Wilder ATR(14) (4,188.15 for ATR 4.10), TP = entry
   − 2.5 x ATR (4,171.75). Wilder smoothing is implemented in `wilder_atr` and
   hand-verified by test.
3. **Risk cap** — risk = volume x contract_size x stop_distance = 0.01 x 100 x 6.15 =
   **6.15 USD <= 10.00 USD**. `plan_test_limit` REFUSES (raises) any geometry that
   breaches the cap — with 0.01 lots the ATR would have to exceed ~6.7 USD before a
   GOLD test limit is refused, and refusal is the correct behavior when it does.
4. **Staging** — via the signed command:

       python -m Terminal.Headless.brain_client --url <ARENA_TUNNEL_URL> \
           --stage-test-limit --symbol XAUUSD.pi --direction SHORT \
           --price 4182.00 --volume 0.01 --atr 4.1

   which POSTs `{"type": "STAGE_TEST_LIMIT", "params": {...}, "signature": ...}` to
   `/api/v1/stage_order`. The laptop-side `apply_command` enforces, in order: capacity
   (MAX_CONCURRENT = 2), quote availability, non-crossing, ATR availability (Wilder
   from bridge bars if not passed), the risk cap — then calls
   `BaseExecutionBridge.stage_limit_order(..., comment="ARENA:TEST_LIMIT_v1",
   expiration_seconds=21600)`.
5. **Auto-purge** — double-guarded: the broker-side expiration (24 bars = 21,600 s =
   6 hours) plus `purge_expired_test_limits`, which runs on every reconciler poll and
   every `PURGE_TEST_LIMITS` command, cancelling any unfilled `ARENA:TEST_LIMIT_v1`
   order older than 24 bars by its staged timestamp. Tested: resting at 5 hours,
   purged at 6 hours + 1 second.
6. **Verification** — the response carries the broker ticket, the computed SL/TP, the
   risk in USD, the expiry and the protocol version; the order is visible in the MT5
   terminal with the `ARENA:TEST_LIMIT_v1` comment tag, proving end-to-end
   bidirectional control.

---

## DELIVERABLE 3 — The multi-agent deliberation contract

`Terminal/Headless/swarm.py` formalizes the tri-specialist swarm. Every perspective is
a bounded, deterministic transform of the same sealed data the local engine sees; LLM
agents fill the identical schema (the deterministic analysts are the offline path and
the attestation baseline):

- **Agent 1 — Orderflow Analyst** (`orderflow_analyst`): CVD 1m-vs-5m pace divergence
  (0.35), L2 20-level depth imbalance (0.30), and resting whale walls — only walls
  with notional >= 150,000 USD persisting >= 180 s count (0.35); a 900,000 USD wall
  seen for 40 s is excluded by test.
- **Agent 2 — Position Manager** (`position_manager`): per-position R-multiples with
  the 3-phase ratchet labels (OPEN / BE_LOCK at +0.80R / PROFIT_LOCK at +1.50R /
  RUNNER at +2.00R — the live GOLD short 18576872 at +0.44R labels OPEN),
  MAX_CONCURRENT = 2 capacity, same-asset guard, and 0.60 correlation damping.
- **Agent 3 — Macro Risk Analyst** (`macro_risk_analyst`): Tier-1 blackout blocks
  outright (conviction 0, `blocked: True`); source-weighted sentiment, Coinbase
  premium, ETF net flows contribute; the cushion versus the 4,775.00 USD hard floor
  is cited in every record and a cushion below 50 USD halves conviction; below the
  floor blocks.

**Synthesis** (`deliberate` + `build_brain_request`): the three perspectives are
evidence, never authority. The conviction vector is computed by the **unchanged**
`PioneerDecisionEngine` (orderflow 30 percent, cascade 25, stops 15, whale 15, macro
15), and the final SELECT/HOLD is an attested response under
`Terminal/Headless/llm_contract.py` — the deliberation record rides inside the
consultation envelope so specialist drivers are citeable as
`/deliberation/perspectives/N/...`, and the validator enforces exact numeric echoes
(a moved stop or a stretched target is rejected), the invariant digest, and resolvable
JSON pointers. Tested both directions: a clean SELECT passes; a moved SL is rejected
with `sl_not_echoed`.

---

## DELIVERABLE 4 — Alpha squeeze & absorption detection

### 4.1 Root cause of the ETH stop-out

Ticket 18593333: LONG 0.85 lots at 2,695.50, stopped at 2,686.00 (−8.08 USD), price
then bounced to 2,691.00. Two compounding causes:

1. **Entry timing** — the limit rested at a static VWAP-band level while aggressive
   sellers were still pressing: the tape had not exhausted. The bounce arrived only
   after the last sellers spent themselves — exactly the moment the entry should have
   been staged, and the moment the position was already stopped out.
2. **Stop geometry** — the stop sat a couple of ticks under the structural swing: the
   wick that swept the swing took the stop with it. The swing held (price bounced
   from above it); the stop did not survive the sweep of it.

### 4.2 The Taker Delta Exhaustion Gate (implemented, wired, tested)

`Terminal/Orderbook_Structure.taker_delta_exhaustion` — a passive limit (S1 pullback
sleeve) now stages only when BOTH hold:

1. **Deceleration** — the pressing side is fading: 1-minute CVD pace better than
   0.60 x the 5-minute per-minute average, with the 5-minute CVD still on the
   pressing side (there was pressure to exhaust — no setup otherwise).
2. **Absorption** — the opposing side is lifting at the level: 1-minute taker flow
   on the absorbing side >= 25,000 USD and >= 0.20 x its 5-minute total (a live
   tape, not a dead one).

Mirrored for SHORTs. Data honesty: with no orderflow tape in the payload the gate
passes marked `UNVERIFIED_NO_TAPE` (the live Chrome feed has no tape; the remote
Arena protocol instead REFUSES — `apply_command` requires proof before touching live
money via `STAGE_ORDER`). Wired into `evaluate_market` as a hard veto
(`exhaustion_gate:seller_pressure_not_decelerating`, etc.), sealed into the candidate
features.

### 4.3 The Adaptive Volatility Stop Buffer (implemented, wired, tested)

`Terminal/Orderbook_Structure.adaptive_stop_level`:

    stop distance = max(1.5 x ATR_15m, structural swing buffered by 0.2 x ATR_15m)

- LONG: stop <= swing_low − 0.2 x ATR — the sweep that takes the swing no longer
  reaches the stop (tested with the exact ETH geometry: a wick to swing − 0.1 ATR
  cannot take the stop).
- The 1.5 x ATR floor preserves volatility honesty; the existing 2.5 x ATR runaway
  veto still caps pathological widths.
- Lot size scales through the unchanged `size_trade` to hold the exact risk budget
  (10–20 USD): a wider stop means smaller volume, never more risk.
- Wired into both LONG and SHORT limit branches of `evaluate_market`, alongside the
  whale-shield and broker-minimum distances.

The end-to-end proof: the real `AI15mMT5Trader` in limit mode refuses the identical
S1 setup while sellers press, stages it once the tape is exhausted and absorbed, and
the staged stop honours the 1.5 x ATR floor.

---

## System invariants (all preserved, all re-tested)

5,000.00 USD initial capital · **4,775.00 USD hard floor** · **10.00–20.00 USD risk
budget** (test limits strictly <= 10.00 USD) · **MAX_CONCURRENT = 2** enforced on the
remote command path itself · **41 bps round-trip friction** (crypto) / broker spread
(metals) · sealed deterministic vectors only · zero-hallucination LLM contract ·
nonce + timestamp + idempotency replay protection on every remote command.

## File map

| File | Status |
|---|---|
| `Terminal/Orderbook_Structure.py` | + `taker_delta_exhaustion`, `adaptive_stop_level` |
| `Terminal/Omni_Trader.py` | exhaustion gate veto + adaptive stops wired into the limit branch |
| `Terminal/Execution/remote_reconciler.py` | new — command protocol, signing/verification, `apply_command`, `plan_test_limit`, `wilder_atr`, purge, `RemoteCommandReconciler`, `gist_fetch` |
| `Terminal/Headless/server.py` | + signed command endpoints (`stage_order`, `modify_sltp`, `cancel_order`) with nonce ledgers |
| `Terminal/Headless/swarm.py` | new — tri-specialist deliberation contract + synthesis |
| `Terminal/Headless/brain_client.py` | new — brain-side signed client, gist publisher, CLI |
| `deploy/start_tunnel.ps1` | new — laptop setup script |
| `Tests/Test_Arena_Brain_Link.py` | new — 17 offline deterministic tests |

---

## Follow-up hardening (same day, post-review)

Three operational gaps found on re-review of the delivered link, now closed
(+3 tests, suite 267 → 270):

1. **One-command Pathway-C fallback.** `python -m Terminal.Execution.remote_reconciler`
   is now a proper CLI: env-driven (`ARENA_COMMANDS_URL`, `OMNI_API_SECRET`,
   `ARENA_POLL_INTERVAL`), fail-closed bridge discovery (identical semantics to
   `Terminal.Headless` — paper only when `OMNI_ALLOW_PAPER=1`), clean SIGINT/SIGTERM
   shutdown, and a final stats line. `deploy/start_tunnel.ps1` step 6 now references
   it instead of an inline python -c.
2. **Guaranteed test-limit purge in Pathway-A-only deployments.** The broker-side
   expiration and the reconciler's scans both required either the broker clock or the
   fallback loop to be alive; now the trader's own ~1-second manage cadence scans for
   expired `ARENA:TEST_LIMIT_v1` orders too (throttled to one scan per 5 minutes,
   failure-isolated, journalled). Tested: a stale limit is purged while a fresh one
   survives, and the throttle holds on an immediate second call.
3. **Muscle health visibility for the brain.** `POST /api/v1/status` (signed with the
   same envelope discipline as evaluate_candle) plus `HeadlessRuntime.status()` and
   `BrainClient.status()`: bridge backend/health, per-pillar freshness and stall
   streaks, sealed data quality (score + digest), and the last evaluation summary.
   Deliberately carries NO account balances — health only; the macro analyst's equity
   context comes from the signed evaluate_candle payloads. Tested both the runtime
   composition (ready, backend name, no balance keys) and the endpoint over a real
   socket (401 unsigned, 200 signed).
