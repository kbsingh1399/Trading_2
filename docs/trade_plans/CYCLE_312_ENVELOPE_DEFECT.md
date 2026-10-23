# Cycle 312 — Envelope Integrity Failure (supersedes the provenance section of CYCLE_312_COUNCIL_EXPLANATION.md)

**Verdict: `DENIED_BAD_CYCLE_ENVELOPE`** — digest-mismatched required artifact. · **Cutoff** 2026-10-23 23:37:12 UTC · **Nonce** 9e2562d4-c54b-4b84-96d5-4e222ec3f88a · **Report** `7458972c42aae85a8e05f937bdb9b504e3a6d784309dc0dc3ba3646978dbca25`

## What changed since the 23:42 review

At 23:42 the dispatcher's commit `1f1c73e…` was absent from this clone, so I recorded the manifest/workbook digest mismatch as *"consistent with post-envelope regeneration, not proven tampering"* and issued a full ruling (`44dd879f…`) whose authorization was `DENIED_FAIL_CLOSED`. **I have now fetched `origin/main` (`be55e14`) and the commit resolves.** That converts an untestable assumption into a test — and the test fails.

| Field | Declared | Reality | Verdict |
|---|---|---|---|
| `risk_policy_sha256` | 4633e4af… | recomputed 4633e4af… | **MATCH** |
| `git_commit` | 1f1c73e… | present on `origin/main`, subtree intact | **MATCH** |
| `git_tree` | e07dec16… | `git rev-parse 1f1c73e^{tree}` = e07dec16… | **MATCH** |
| `evidence_manifest_sha256` | 5cf58f83… | 96da1ec7… at that commit, 15fc034c… on disk | MISMATCH (explainable: live index, ~5 min churn) |
| **`workbook_sha256`** | **fb6aebf6…** | **e855a87f… everywhere** | **MISMATCH — fatal** |
| `excel_freshness_verified` | `null` | audit 21:42:14 UTC, 29/33 fresh | NOT VERIFIED |

## Proof that the workbook digest is invalid, not merely stale

The workbook blob is byte-identical — `e855a87f…`, 2,724,657 bytes — in **ten consecutive commits** spanning the cutoff:

`ebd5f0a 23:12:25` · `cf28fa8 23:17:28` · `0f7cc8e 23:21:40` · `ef411c4 23:24:31` · `08d6f25 23:26:36` · `0382352 23:31:52` · **`1f1c73e 23:36:34`** · **`e995f28 23:42:16`** · `c69c4ff 23:44:54` · `be55e14 23:49:52` (all UTC)

The cutoff (23:37:12) sits between the seventh and eighth of those commits. The other two `.xlsx` files on disk are `188f8d35…` (`audit_copy.xlsx`) and `fe08566f…` (`tmp_database_read.xlsx`). **No artifact in the workspace and no commit in that 38-minute window has sha256 `fb6aebf6…`.**

That kills the "working tree was momentarily different" defence. For the declared digest to be honest, the workbook would have to have been rewritten to `fb6aebf6` between 23:36:34 and 23:42:16 and then restored **byte-identically** to `e855a87f` — which openpyxl cannot do, since it does not emit deterministic ZIPs. The digest therefore attests to nothing observable.

**Root cause (most probable):** `Terminal/generate_cycle_envelope.py` calls `sha256_file(WORKBOOK_PATH)` directly on a file the Excel pipeline daemon still writes. A torn read produces exactly this signature — a hash that matches no state, before or after. Secondary possibility: a cached hash reused across generations.

## Why this is a hard stop and not a footnote

The workbook *is* the evidence store: sheets `12_Hyperdash`, `18_CVD`, `10_Whale_Orders`, `7_Live_Liq` are the rows every candidate row cites. If the envelope cannot bind the workbook, then no cell can be tied to a cutoff, and every downstream number — inventory reconciliation, the 26.00 stress, the 68.07 headroom, `P_fill`, `P_TP` — would be presented over unattestable evidence. The protocol answers this directly: digest-invalid required evidence fails closed, and such an envelope is rejected outright.

The conservative direction is preserved: the previous ruling's authorization was already `DENIED_FAIL_CLOSED`, so **no unsafe action was ever authorised** — the denial was right even though its stated reason was too generous. What changes is the attribution: the provenance failures at Cycle 311/312 were *real integrity defects*, not benign drift.

## Ship-with-it fix

`Terminal/verify_cycle_envelope.py` (added in this commit) re-derives every provenance field in one command and exits non-zero on any mismatch:

```
$ python Terminal/verify_cycle_envelope.py Data/cycle_envelope.json
cycle    : Cycle 312 @ 2026-10-23 23:37:12 UTC
verdict  : REJECT_ENVELOPE
  [PASS] risk_policy_sha256
  [PASS] git_commit
  [PASS] git_tree
  [FAIL] evidence_manifest_sha256
  [FAIL] workbook_sha256
  [FAIL] workbook_sha256_at_declared_commit
  [FAIL] excel_freshness_verified
```

It uses `stable_sha256()`: hash twice with a pause, require size + `mtime_ns` + digest unchanged, else raise. That single change in the builder removes the torn-read class entirely. Recommended builder edit — emit `workbook_bytes` and `workbook_hash_stable: true`, and refuse to build if the workbook `mtime` is after the cutoff or the digest is not reproducible across two reads.

## Dispatch notes

- **Replay:** nonce `9e2562d4…` was already reviewed at 23:42. A duplicate dispatch cannot renew authority.
- **TTL:** 900 s from 23:37:12 → expired **23:52:12 UTC**; 71 s remained at review time (23:51:01).
- **Post-cutoff, informational only:** snapshot 23:48:55 UTC shows balance 4,865.07, flat, `trade_authorization: DENIED_UNVERIFIED_ORDERFLOW`. It cannot re-authorise the 23:37 cutoff.

## To clear this block

1. Patch `sha256_file()` usage to `stable_sha256()` and rebuild the envelope; the new `workbook_sha256` must equal the hash of `Data/DataBase_Trading.xlsx` **and** the blob at the declared commit.
2. Run `Terminal/verify_cycle_envelope.py` and attach `verdict: VERIFIED` to the dispatch.
3. Only then resubmit for a gate review — freshness, broker session, native venue, calendar and `order_check` are still independent requirements and will each still have to pass.
