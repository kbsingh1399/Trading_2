# Cycle 185 — not ratified. Audit committed locally as 4c8bc9f (188 lines), presented.

The dispatch says the fixes are live and verified. The committed artifacts at `940f5d78` (23:33:57Z) show the daemon has stopped and the harvester guard does not do what the dispatch says. I did not ratify any of the four questions as written.

## Verdicts

| Q | Verdict | Why |
| --- | --- | --- |
| **Q1** F29 freshness | **Partial** | L1/L2/L4/L5/L6 ages are now positive and recompute exactly. L7 age is a fallback (`or time.time()`) plus a 0.01 floor. L3 is correctly DEGRADED at 729 s, but the dispatch says HEALTHY at 697.3 s and 42.5 s. |
| **Q2** F42 aggregation | **Not certified** | Level sums reproduce $18.01M across the four BTC levels. But G-7 tests the level's max duration and max single order, not one order. Row identity is not guaranteed, so the sum can double count. The dispatch's SELL 84,000 = $6.05M is $10k off the committed $6.04M. |
| **Q3** pass-through | **Certified as a gating interface** | The boundary partition is correct in code and in the served block. `tau_s` 657.3 and `decay_factor` 0.6724 reconcile with the C183 decay curve. The C184 engine fields (`p_eff`, `R_req`, size, sign persistence, shelf flag) are still not in the block. |
| **Q4** harvester guard | **Not certified** | This is the main finding. See below. |

## The harvester guard (Q4)

- `click_opt_js` returns `false` when no option matches. The caller discards that return value, sleeps, and extracts anyway.
- The guard then reads the search box. The harvester set that box to the target with `insertText` just before, so the guard passes whether or not the click worked.
- The extract reads the rows currently on screen. After a failed switch, those are the previous asset's rows, written under the target's key.
- The dispatch says the code "throws an error and skips the asset." It does not.

Removing `options[0]` closed the visible hole. This one is still open.

## Daemon

- `coinglass_harvester_status.json` now exists, which resolves the C184 404. It is also the reason the dispatch's "daemon is currently active" claim is checkable.
- The last harvest is 23:19:25Z. At the served as-of of 23:31:34Z, that is 729 s of silence, about four missed 180 s cycles.
- The committed `latest` snapshot still shows 611 orders from 23:13:51Z, while the archive and the served block show 570 from 23:19:25Z. Two artifacts disagree at HEAD.
- The 180 s cadence rests on one daemon-era gap (179.6 s). That is n = 1, not a certification.

## Dispatch numbers

Most of Part 1 and Part 2 does not match the HEAD served block. The Q2 example JSON (score 0.2436) is not a served artifact; the served BTC score is 0.2373. I treated the dispatch's numbers as claims and graded them against the artifacts.

## New findings

F44–F52 are in the audit. The P1s are: daemon silence (F44), the stale `latest` file (F45), the harvester guard (F46), row identity under F42 (F48). Part 7 lists what must be fixed before re-ratification.

**Limits:** I could not reach the sandbox desktop, so daemon liveness is inferred from committed artifacts only. I did not fetch the served BTC wall-level rows.

Desk posture is unchanged: shadow run only, no orders. Equity 4,863.74, cushion +88.74, 0 positions. W0 is still open.