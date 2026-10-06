# OMNI Headless Cloud Execution & Desktop Dependency Abstraction
**Prompt:** OX_ALPHA_60_HEADLESS_CLOUD_ARCHITECTURE · **Date:** 2026-10-07
**Branch:** `arena/4adf3661-trading-2` · **Baseline:** 247 tests passed / 4 pre-existing environment failures (was 225; +22 new, zero regressions)

The three desktop dependencies are now fully abstracted. The entire decision and execution
chain runs 24/7 in a Linux container with **zero** Windows GUI, zero browser, zero
MetaTrader5 import — with the live account's risk invariants enforced in code, not config.

| Dependency | Was | Now |
|---|---|---|
| 1. Windows MT5 desktop IPC | `MT5ExecutionBridge` (named pipes to `terminal64.exe`) | `Terminal/Execution/` polymorphic bridges: **NativeMT5Bridge** (local), **HeadlessRESTBridge** (cloud gateway), **PaperSimulatedBridge** (deterministic tick matching) |
| 2. Browser CDP scraping | `Chrome_Terminal.py` over CDP :9222 | already replaced by `Terminal/Data_Factory/` (consultations 3–4); this consultation closes the last gap: **persistent ≥180s whale-wall enforcement** |
| 3. Local process scheduling | Windows tasks | `Terminal/Headless/`: `CandleScheduler` (:14/:29/:44/:59 drift-compensated wakes), `HeadlessService` (signed HTTP), `HeadlessRuntime` (composition root), `python -m Terminal.Headless` |

---

## DELIVERABLE 1 — Polymorphic broker execution adapter architecture

### 1.1 The contract — `Terminal/Execution/base.py`

`BaseExecutionBridge` (ABC) defines the **exact surface `Omni_Trader` already calls**
(recon: 15 call sites in `Terminal/Omni_Trader.py` — `_dispatch` L1091/L1113,
`manage_active_positions`, `_reconcile`, `_quote`, `evaluate_market`):

| Tier | Methods |
|---|---|
| Mandatory (abstract) | `get_account_summary()`, `get_open_positions()`, `get_pending_orders()`, `get_symbol_price()`, `stage_limit_order()`, `modify_position_sltp()`, `cancel_pending_order()` (+ `cancel_order` alias) |
| Extended (fail-closed defaults) | `resolve_symbol()`, `get_recent_bars()`, `estimate_order()`, `execute_market_order()`, `close_position()`, `position_deals()`, `reconcile_intent_history()`, `intent_filled()` |
| Health | `health()` — probes `get_account_summary()`; used by discovery and readiness |

Every method returns the dict shapes the trader and `OrderPersistenceGovernor` already
consume (`ticket/symbol/direction/volume/price_open/sl/tp/profit_usd/time/magic/comment`
for positions; `success/ticket/expires_at` for staging) — **drop-in by construction**,
proven by the full-stack test where the *real* `AI15mMT5Trader` executes a T1 breakout
through `PaperSimulatedBridge` with no test broker double in sight.

### 1.2 Backend A — `NativeMT5Bridge` (`Terminal/Execution/native_mt5.py`)

Subclasses the existing, battle-tested `MT5ExecutionBridge` (`Terminal/MT5_Execution_Bridge.py`,
L37–650) unchanged; adds the ABC contract and a `health()` that re-asserts
`ensure_connected()`. MRO places the concrete class first so MT5's real methods win
attribute resolution. This remains the high-speed local path (your Windows machine,
account 5064568).

### 1.3 Backend B — `HeadlessRESTBridge` (`Terminal/Execution/headless_rest.py`)

Linux/cloud REST execution (MetaApi-shaped routes; any gateway — MetaApi, a Blueberry
REST/FIX adapter — plugs in by overriding the path map):

- `GET /users/current/accounts/{id}/account-summary|positions|pendingOrders`,
  `GET …/symbolPrice/{symbol}`, `POST …/trade`
  (`ORDER_TYPE_BUY_LIMIT/SELL_LIMIT/BUY/SELL`, `MODIFY_POSITION`, `CANCEL_ORDER`,
  `CLOSE_POSITION`) — normalized into the trader's dict contract.
- **Secrets only via environment** (`METAAPI_TOKEN`, `METAAPI_ACCOUNT_ID`,
  `METAAPI_DOMAIN`); the token rides the `auth` header, never the URL (tested).
- **Injectable transport** — `transport(method, url, headers, payload) → (status, json)`;
  the offline suite drives the full account-state mapping with canned responses mirroring
  your live book (ticket 18593333 ETH 0.85-lot long, the four resting limits).
- **Fail-closed:** any non-2xx raises `BridgeError` — order state is never assumed.
  `intent_filled()` answers from a client-side ledger + live pending/positions state,
  never from optimism.

### 1.4 Backend C — `PaperSimulatedBridge` (`Terminal/Execution/paper.py`)

Zero-dependency institutional matching engine:

- resting limits fill when the quote crosses (BUY at ask ≤ limit, SELL at bid ≥ limit,
  fill at limit-or-better); market orders fill at quote ± configurable slippage bps;
- **LONG risk fires on the BID, SHORT on the ASK** (no phantom spread fills); SL/TP
  fill exactly at level — the server-side semantics the 3-phase ratchet assumes;
- full account math: cash + floating equity, margin used/free (deterministic,
  injectable clock);
- `PaperSimulatedBridge.from_bus(bus, assets)` binds quotes to the Data Factory bus
  mids — headless simulation streams straight off the live venue tape;
- direction vocabulary normalized (`LONG/SHORT` canonical, `BUY/SELL` tolerated).

### 1.5 Auto-discovery & fail-closed fallback — `create_bridge()`

```
EXECUTION_BACKEND=native_mt5|headless_rest|paper   → EXACTLY that backend; if its
                                                    health probe fails, STARTUP FAILS.
                                                    (Never silently fall back from
                                                    the operator's intent.)
unset → auto: native MT5 (package + terminal probe) → cloud REST (token + probe)
        → paper ONLY if OMNI_ALLOW_PAPER=1 → else NoExecutionBackend (no trading).
```

Runtime degradation is handled one level up: `HeadlessRuntime.readiness()` flips false
on bridge health failure, `evaluate_candle()` returns a `NO_TRADE_FAIL_CLOSED` payload,
and **new entries stop while open positions remain protected by their broker-server-side
SL/TP** (the ratchets are already server-side once armed — a cloud outage cannot orphan
a stop). Tested end-to-end.

---

## DELIVERABLE 2 — Pure-Python zero-browser L2/L3 aggregation

Consultations 3–4 delivered the aggregation; this consultation closes the final gap the
audit found:

**`_WallTracker.l3_orders()` now enforces `min_persistence_sec` (it was a stored but
dead parameter).** A resting whale wall must now satisfy **notional ≥ 150,000 USD AND
persistence ≥ 180 s** (with the >30 s unseen-drop reset). A wall observed once is
fleeting depth, not a resting cluster — tested both ways, plus the sub-150k exclusion.

The complete zero-browser pipeline (no Chrome, no CDP, no :8095 hop):

```
Binance @depth20@100ms ─┐
Coinbase level2_batch  ─┼→ streams.py parsers → IntelligenceBus ring buffers (1024)
Hyperliquid l2Book     ─┘        (per-venue monotonicity, CVD/footprint, sub-ms reads)
                                        │
                        _WallTracker: 10 bps cluster tolerance, ≥150k USD, ≥180 s
                                        │
                        factory.payload(): l2_book + l3_orders + recent_trades +
                        projected_liquidations + observed_stops + orderflow snapshot
                                        │
             Risk_Sizing_Engine.OrderflowModel.features  ← 100% schema parity
             Pioneer_Decision_Engine.evaluate            ← (tested end-to-end)
```

Schema parity is asserted by tests at both consumers; `payload_fetcher()` remains the
one-argument swap into `AI15mMT5Trader(fetcher=…)`.

---

## DELIVERABLE 3 — Production containerization & deployment blueprint

### 3.1 `deploy/Dockerfile` (multi-stage, minimal, non-root)

- **Stage 1** (`python:3.11-slim`): `pip wheel` into `/wheels` from
  `deploy/requirements-headless.txt` — just `numpy`, `websockets`, `requests`,
  `polars`; everything else is stdlib (asyncio, hmac, hashlib, urllib).
- **Stage 2**: wheels installed and deleted; app code copied; dedicated `omni` user
  (`nologin` shell); `HEALTHCHECK` via in-image python urllib against `/healthz`;
  `CMD ["python", "-m", "Terminal.Headless"]`.

### 3.2 `deploy/docker-compose.yml`

- `restart: unless-stopped`, `stop_grace_period: 30s` (let the current slot land);
- resource envelope: **1 CPU / 1 GiB** (limits) with 0.25 CPU / 256 MiB reservations,
  `memswap_limit` = memory (no swap spillover: fail, don't crawl);
- `../Data:/app/Data` volume — state, journals, seals, covariance survive restarts;
- healthcheck (30 s interval, 3 retries, 30 s start period);
  JSON-file logs capped at 5×50 MiB; `no-new-privileges` hardening.

### 3.3 Secrets — `deploy/.env.example`

Every credential enters via env (`METAAPI_TOKEN`, `METAAPI_ACCOUNT_ID`, `MT5_ACCOUNT_ID`,
`OMNI_API_SECRET`, `OMNI_LLM_*`); nothing is hardcoded; the populated `.env` is never
committed. The REST bridge carries the token only in the `auth` header — asserted by test.

### 3.4 Candle-boundary synchronization — `Terminal/Headless/scheduler.py`

`CandleScheduler` wakes at **HH:14:30, HH:29:30, HH:44:30, HH:59:30 UTC**
(minute 14 + `cadence_second=30`, matching the trader's own window gate
`840+30 ≤ elapsed < 898` in `evaluate_market`):

- **Drift compensation:** the target is recomputed from the wall clock every iteration
  (error never accumulates); coarse sleep to T−0.5 s, then a fine phase of ≤50 ms
  increments. Tested with a virtual clock: wakes land on the boundary with **zero
  residual drift**, and a skipped deadline (system suspend) fires exactly once and
  resynchronizes to the next boundary.

---

## DELIVERABLE 4 — Institutional conviction & decision-making in the cloud

### 4.1 The signed microservice — `Terminal/Headless/server.py`

`HeadlessService` (dependency-free async HTTP/1.1 over `asyncio.start_server`, hard
limits: 8 KB headers, 1 MB bodies):

| Endpoint | Semantics |
|---|---|
| `GET /healthz` | liveness — unsigned, for the container healthcheck |
| `GET /readyz` | readiness — bridge health + fresh book; **503 with reasons** when degraded |
| `POST /api/v1/evaluate_candle` | one candle evaluation → **signed JSON**: decision, Pioneer conviction vector (per-asset conviction/advice/quality/friction floor/digest), staged order tickets (asset, direction, ticket, limit, SL/TP, volume, risk, expiry), sealed data quality (score + digest) |

Signing: **HMAC-SHA256** over `ts ‖ canonical_json` with `OMNI_API_SECRET`;
responses carry `X-Signature`/`X-Signature-Ts`; requests must themselves be signed
(30 s replay window, constant-time compare) — unsigned requests get 401, stale
signatures get 401, malformed JSON 400, unknown routes 404. All tested over a real
socket. One evaluation at a time (lock + 45 s timeout → 504).

### 4.2 The LLM contract — `Terminal/Headless/llm_contract.py`

If Claude/DeepSeek/Gemini is consulted at candle close, the prompt/response is
**deterministic by construction — the model cannot introduce numbers**:

**Request** (`build_consultation_request`): sealed feature vector + digest, the Pioneer
advisory, the pre-computed candidate (entry/SL/TP/hurdle/risk), and the full
**invariant envelope** — hard floor 4,775.00 USD, 4.50% max drawdown, risk budget
10–20 USD (env-tunable, `OMNI_RISK_MIN/MAX_USD`), 41 bps round-trip friction,
MAX_CONCURRENT = 2, 5 resting limits, and the 3-phase piecewise ratchet table
(`Uplift_Model.RATCHET_BASE`: 0.80R→0.35R, 1.50R→0.85R, 2.00R trail 0.65R, target
2.50R max 2.75R) — hashed into `invariant_digest` (SHA-256).

**Response** (`validate_consultation_response`) — accept only if:
- `action ∈ {SELECT, HOLD}`; HOLD must be silent (no candidate id, no order terms);
- SELECT must name the pipeline's exact `candidate_id` and **echo `risk_usd`/`sl`/`tp`
  to 1e-9** — a "better" stop, a bigger risk, or a stretched target is a violation
  (the ratchet and sizing math stay on our side of the wall);
- risk within the envelope budget; `invariant_digest` echoed unchanged;
- `support_refs`/`invalidation_refs` are JSON pointers that **resolve inside the
  request** (same discipline as `CognitiveEngine.validate_decision`, which remains the
  in-process path with its numeric-prose attestation).

This composes with the existing `CognitiveEngine` (`Terminal/Cognitive_Engine.py` L201–
L300: `evaluate_snapshot` → `validate_decision` → `attest_decision` → ledger) — the
cloud contract is the same philosophy tightened for an untrusted remote endpoint.

### 4.3 Composition root — `Terminal/Headless/runtime.py`

`HeadlessRuntime.from_env()` wires factory + runner + validator + pioneer + bridge +
trader (risk envelope 10/20 USD by default; the 4,775 floor and 41 bps friction are
**code-enforced, not env-tunable**). `evaluate_candle()` is fail-closed at every seam:
unready bridge → `NO_TRADE_FAIL_CLOSED`; no payloads → same; any exception → same.
`run_forever()` starts the data runner, the scheduler and (optionally) the HTTP service
under one stop event; `python -m Terminal.Headless` is the container entrypoint.

---

## Test suite — `Tests/Test_Headless_Cloud.py` (22 tests, 100% offline)

- **Execution (8):** ABC contract on all three backends; paper fills on crossing quotes
  (limit-or-better), SL/TP on the correct side of the spread with exact-level fills,
  market slippage + equity/margin math, pending/intent/deal ledgers; REST account-state
  mapping with canned live-book responses (auth header, token never in URL), trade +
  fail-closed 5xx + health probe; discovery fail-closed on explicit-unhealthy and
  unknown backends; auto-discovery yields paper only when allowed.
- **Walls (1):** ≥150k AND ≥180s persistence enforced; fleeting and thin depth excluded.
- **Scheduler (2):** exact boundaries (:14:30 …), zero residual drift, coarse/fine phases.
- **Service (3):** HMAC roundtrip/tamper/replay; healthz/readyz (200/503) + 404;
  evaluate_candle auth (401 unsigned/stale), signed response verification, 400 malformed.
- **LLM contract (3):** clean SELECT/HOLD accepted; invented/moved numbers, wrong
  candidate, stale digest, unresolved pointers, noisy HOLD all rejected; the envelope
  encodes the production ratchet/floor/friction set.
- **Runtime (5):** readiness fail-closed (no bridge / unhealthy / stale book);
  evaluate_candle fail-closed without consulting the trader; the full microservice
  contract; **the real `AI15mMT5Trader` trading a T1 breakout through
  `PaperSimulatedBridge`** — order filled, position live with SL/TP, and the ratchet
  actuator moving the stop under the appreciated bid.

**Suite state:** 247 passed / the same 4 pre-existing environment failures (msvcrt,
MetaTrader5, two Chrome_Terminal UI fixtures) — unchanged since consultation 1.

## Implementation roadmap (applied, not just designed)

1. **Local parity first** — run `EXECUTION_BACKEND=native_mt5 python -m Terminal.Headless`
   beside the current loop; the trader, pioneer and governor are the same objects.
2. **Cloud cutover** — `deploy/.env` with `EXECUTION_BACKEND=headless_rest` +
   MetaApi credentials; `docker compose -f deploy/docker-compose.yml up -d`; verify
   `/readyz` shows the live account (5064568) and the four resting limits.
3. **Blueberry direct REST/FIX** — subclass `HeadlessRESTBridge`, override the path map
   and position normalization; the contract test suite is the acceptance gate.
4. **Optional LLM consultation** — point `OMNI_LLM_*` at your endpoint; the contract
   validator is the gate; start with `OMNI_PAPER=1` shadow mode.

## Standing invariants (all preserved, all re-tested)

5,000 USD capital · **4,775.00 hard floor** (code-enforced) · **10–20 USD dynamic risk
budget** (headless default; RiskPolicy envelope) · **41 bps round-trip friction** ·
**MAX_CONCURRENT = 2 filled / 5 resting** under first-fill OCO · 3-phase piecewise
ratchets (`RATCHET_BASE`) · sealed deterministic vectors only · zero-hallucination LLM
contract (numeric echo enforcement).

## File map

| File | Status |
|---|---|
| `Terminal/Execution/{base,native_mt5,headless_rest,paper}.py` | new (4 modules) |
| `Terminal/Headless/{runtime,scheduler,server,llm_contract,__main__,__init__}.py` | new (6 modules) |
| `Terminal/Data_Factory/factory.py` | wall persistence ≥180 s now enforced |
| `deploy/{Dockerfile,docker-compose.yml,requirements-headless.txt,.env.example}` | new |
| `Tests/Test_Headless_Cloud.py` | new, 22 tests |
| `Tests/Test_Zero_Cost_Data_Factory.py` | wall-persistence priming fixture |
