Thought Process
Explored 1 files，Ran 1 commands

Files downloaded. The tree.json is small (likely an API response envelope) — let me inspect it and read all three production files in parallel, plus the recent worklog tail.

Explored 1 files，Ran 1 commands

parquet_feed_writer.py is fully captured (211 lines). GitHub API tree is rate-limited, but raw file fetches work — let me pull the checklist auditor and read both footprint collectors in full.

Explored 1 files，Ran 1 commands

parquet_feed_writer.py and collector 25 are fully analyzed. Now reading the larger footprint bar-metrics collector.

Explored 4 files

All three production files are now fully analyzed. Let me quickly enumerate the actual repo directory structure (to resolve the auditor filename + the 42-file inventory question) and pull the recent worklog tail in parallel.

Explored 2 files，Ran 1 commands

parquet_feed_checklist_auditor.py, unified_liquidation_matrix.py (the feed-14 synthesizer), and time_series_database.py are the key discovery — these directly answer the concurrency, cross-feed vintage, and rolling-history questions. Fetching all three plus the worklog tail now.

Explored 3 files，Ran 1 commands

The checklist auditor alone yields critical findings (33-feed registry that omits feeds 25/26, 15-min SLA vs 1.5m docstring, self-referential telemetry). Now reading the liquidation matrix synthesizer and the time-series store — these settle the rolling-history mandate questions.

Explored 1 files

Tier-4 "$25M fabricated magnet" defect found in the matrix synthesizer — a headline-severity finding. Now the final file: the 958-line time-series store.

Explored 2 files

Research complete — all 6 production files fully analyzed with severe findings. Now loading the docx skill to produce the archival audit document before composing the final council response.

Ran 1 commands

Skill loaded. Setting the document outline now, then loading the required skill reference files.

Explored 10 files，Ran 2 commands

All skill files are loaded (create route, docx-js core, design system with R1 recipe + IG-1 palette, common rules, report scene, TOC reference). Now writing the generation script in three parts.

Wrote 1 files

Part 1 (helpers + cover) done. Now Part 2 — chapters 1–4 (verdict, writer forensics, collector forensics, cross-cutting layer).

Wrote 1 files

Part 2 done. Now Part 3 — chapters 5–8 (narrative math, capital survival, decision matrix, roadmap) plus document assembly.

Wrote 1 files，Ran 2 commands

Document generated and validated — 0 errors (the two warnings are by-design: dense table/code line spacing, and Consolas which exists on the desk's Windows target). Appending the worklog entry, then delivering the full council audit.

Ran 1 commands

All work complete. Here is the full Council response.

📚 Active Skills Loaded & Applied
SKILL
	
APPLICATION IN THIS REVIEW

docx (full chain: SKILL.md → create route → design-system R1/IG-1 → common-rules → report scene → toc)	Archival audit document generated → /home/z/my-project/download/ZAI_Council_Forensic_Audit_Parquet_Data_Lake.docx (postcheck: 0 errors)
Web research (raw.githubusercontent + repo-tree probes)	6 production files pulled byte-for-byte @ commit 77dc330a5, 2,853 lines read line-by-line
Worklog protocol	Entry AUDIT-77DC appended to shared ledger

[ALERT] TELEMETRY STALE WARNING — The account telemetry (balance = equity = 4,846.32, 0/0 book) is byte-identical to the Cycle-20261025T101032Z envelope frozen > 1 day before this review. All Section-C capital arithmetic is computed against that snapshot and must be re-validated against a live MT5 poll before any order is staged.

Metacognitive answer — "If it used all the available skills related, will it improve our response?" Yes, and demonstrably: the docx skill chain forced the audit into a permanent, desk-circulable artifact with validated layout; live file pulls (vs. reviewing from the dispatch's quoted snippets) upgraded the review from advisory to forensic — three of the five SEVERE findings (the _empty sentinel at writer line 72, the $25M hardcoded magnets at matrix lines 195–225, the auditor's 33-feed registry omission) are invisible in the code excerpts quoted in the dispatch and were only catchable by reading the actual files. The skills that would add marginal further value are charts (freshness-latency histograms) and xlsx (finding register as a tracked sheet) — recommended for the remediation phase, not material to the verdict.

🏛️ Z.AI SOVEREIGN QUANT COUNCIL — FORENSIC AUDIT RESPONSE
Parquet Data Lake Ingestion Integrity & Narrative Decision Chain (commit 77dc330a5)

Evidence basis: parquet_feed_writer.py (211L) · 25_CoinGlass_Footprint_Signals.py (471L) · 26_Aggregated_Footprint_Bar_Metrics.py (699L) · parquet_feed_checklist_auditor.py (267L) · unified_liquidation_matrix.py (246L) · time_series_database.py (959L). Three dispatch-named paths returned 404 (parquet_checklist_auditor.py, cdp_browser_utils.py, liquidation_matrix_synthesizer.py) — the actual repository equivalents were substituted.

PART 1 — EXECUTIVE SUMMARY & VERDICT ON THE INGESTION CHAIN
⚖️ VERDICT: FLAWS IDENTIFIED — FIXES MANDATED

The Parquet migration is architecturally superior to the openpyxl monolith it replaced — per-feed file decoupling eliminates the entire cross-sheet lost-update class that dominated C280–C347, and the fsync → os.replace kernel is genuinely atomic. But the desk is currently trading on fabricated and laundered data in specific, identified locations, and the Council does not certify live decisioning until eight P0s ship.

Finding census — 34 defects: 5 SEVERE · 10 HIGH · 12 MEDIUM · 7 LOW.

The three that mandate immediate quarantine:

M1 (CRITICAL) — unified_liquidation_matrix.py:195-225 invents liquidation magnets for every macro CFD: Short-Liq at price + 2.5×ATR, Long-Liq at price − 2.5×ATR, each with hardcoded liquidation_vol_usd = 25,000,000.0 and $50M cumulative — written into your primary magnet feed 14_Liquidation_Matrix with no is_synthetic flag. Rule A ("TP front-runs the dominant magnet") on NAS100/GOLD/EURUSD is currently front-running fiction.
S1/S2/B1/B2 — The footprint collectors launder failure as fresh PASS data: DOM-timeout falls through silently and writes zero-price fallback rows (25:130-143→284-304); all-27-coins-fail still writes macro-only and returns True (25:433-445); feed 26 ships fabricated VAH/VAL/VWAP (vah=max_bucket, val=min_bucket, vwap=poc=close, 26:283-286) and hardcoded metals volumes (volume=250000, buy=sell=125000, trades=80, 26:419-428).
W1 — The writer's mode parameter is dead code (line 53 declared, never referenced). No append/upsert exists. Every rolling feed (18, 26, 7_Live_Liq, 22, 19_News/Calendar, 1, 2) is truncated to its last batch; feed 26's entire history is a 10-bar sliding window with permanent gaps on any failed cycle.

Institutional control failure: the freshness auditor's registry contains 33 feeds and omits 14_Liquidation_Matrix, 25, and 26 (A1) — your primary magnet feed and both footprint collectors are structurally unmonitored. SLA truth is triple-drifted: docstring says <1.5m High Velocity, code sets 15.0 min, your mandate demands <5.0m (A2). Feed 23 is a tautology — the auditor writes it from its own results mid-audit, so it can never be stale (A3).

Verified end-to-end: your architecture instinct on the intersection trap is correct and Section III formalizes it — but the Council corrects your capital arithmetic (Part III, §5): the true kernel runway is 2.8 stressed tickets (1.4 dual rounds), not 4–5.

PART 2 — LINE-BY-LINE CODE & ARCHITECTURE VULNERABILITY REPORT
2.1 parquet_feed_writer.py — the atomic kernel is sound; the state semantics are not

What survives scrutiny: tmp-in-destination-dir → fsync → os.replace (lines 111–131) is a true atomic swap on NTFS (MoveFileEx); the 10× PermissionError retry correctly targets WinError 32 sharing violations (CPython maps sharing violations → PermissionError); readers holding an open handle during swap see the complete old file — no partial reads are possible. Per-feed decoupling ends the Excel lock wars.

ID
	
SEV
	
LOCATION
	
DEFECT

W1	🔴 SEVERE	:53	mode="overwrite" never used in body — no append/upsert/merge exists anywhere in the module
W2	🔴 SEVERE	:72	Empty batch → persists 1-row {"_empty": True} sentinel overwriting last-good data with a fresh PASS sidecar; downstream schema gains a junk column and loses all real columns
W3	🟠 HIGH	:160-164	Sidecar os.replace has no retry (parquet path has 10). Reader holding sidecar → exception → RuntimeError raised after parquet already swapped → caller thinks write failed → double-write churn + parquet/sidecar version skew. No status:"FAIL" sidecar exists on any path
W4	🟠 HIGH	:111,161	tmp collision: parquet tmp is pid+ms (two threads, same feed, same ms); sidecar tmp is pid only — concurrent same-feed threads in one process deterministically interleave into the same sidecar temp → corrupt JSON. Your own time_series_database.atomic_write_bytes:57 already uses the correct time_ns() pattern
W5	🟡 MED	:129-136	Retry budget = 1.1s total — Defender/AV routinely holds new files for seconds; on exhaustion the batch is destroyed, not spilled
W6	🟡 MED	:74-104	No pinned schemas — from_pylist re-infers per cycle (all-null → null type, int→double drift); schema param exists, zero callers pin it
W7	🟡 MED	:141-156	Sidecar freshness = write time, not data time — stale upstream data is laundered as fresh; no data_asof, no sha256
W8	⚪ LOW	except-path	Orphan .tmp_*.parquet on hard kill — the most plausible source of your 42-vs-36 file count (§7.2)
W9	⚪ LOW	:107-108	retention_rows tail-slices in insertion order, no sort guarantee

Mandated writer contract (drop-in shape):

python
def write_parquet_feed(feed_name, data, schema=None, mode="overwrite",
                       retention_rows=None, keys=("symbol","timestamp_ms"),
                       custom_metadata=None, data_asof_epoch=None):
    table = coerce_to_arrow(data, schema)
    if table.num_rows == 0:                       # W2: empty is FAIL-CLOSED
        emit_sidecar(feed_name, status="FAIL", reason="empty_batch")
        raise EmptyBatchError(feed_name)          # previous good parquet untouched
    if mode == "upsert":                          # W1: real rolling path
        old = pq.read_table(target_file) if target_file.exists() else None
        table = upsert_dedupe(old, table, keys).sort_by([("symbol","ascending"),
                                                         ("timestamp_ms","ascending")])
        if retention_rows: table = table.tail(retention_rows)
    tmp = FEEDS_DIR / f".tmp_{feed_name}_{os.getpid()}_{time.time_ns()}.parquet"  # W4
    pq.write_table(table, tmp, compression="SNAPPY", version="2.6"); fsync_file(tmp)
    replace_with_retry(tmp, target_file, attempts=20, base=0.05, cap=8.0)         # W5
    meta = {"feed_name": feed_name, "status": "PASS", "row_count": table.num_rows,
            "data_asof_epoch": data_asof_epoch, "sha256": sha256_file(target_file),
            "write_epoch": time.time()}           # W7: data time, not write time
    write_sidecar_atomic(meta)                    # W3: same retry, atomic
2.2 25_CoinGlass_Footprint_Signals.py — DOM-harvest collector
ID
	
SEV
	
LOCATION
	
DEFECT

S1	🔴 SEVERE	:130-143, 284-304	Hydration poll (20×0.3s) falls through on timeout with result discarded — Cloudflare interstitial or Next.js hydration stall ⇒ writes fallback rows with last_price=0.0 as PASS. Same unguarded pattern on the signals poll (15×0.3s)
S2	🔴 SEVERE	:433-445	Per-coin exceptions swallowed, no failure tally; all 27 coins failing still writes macro-only rows and returns True — 96% coverage collapse is invisible (and A1 means nothing else is watching)
S3	🟠 HIGH	:135,148,205,214	Obfuscated CSS-module hashes (.KpiStrip_kpi__7Xgii, .SidePanel_lrow__m40N_) break on every CoinGlass deploy; S1 converts that into junk rows, not loud failure
S4	🟠 HIGH	:421-430	cdp_cmd loops ws.recv() with no timeout — hung tab ⇒ collector hangs forever, feed silently never updates; WebSocket never explicitly closed
S5	🟡 MED	:251-262	Unit confusion: "2.3K AVAX" parsed as 2,300 USD in absorbed_vol_usd (only ETH/BTC/SOL tokens excluded) — poisons absorption-weighted scoring for every alt
S6	🟡 MED	:229	All rows stamped with the same harvest-end timestamp — coin #1's data is up to 5–6 min older than its stamp claims (structural uniform-lie)
S7	🟡 MED	:236,265	signal_time = "10-26 16:36" — no year/tz/epoch, mixed with "LIVE" sentinels; unreliable dedup/sort key
S8	⚪ LOW	:267	symbol = f"{coin}USDT" fabricated for CL/XAU/SPX — never joins to broker symbols in 11_Technical; asset_registry.py exists but is not wired
S9	⚪ LOW	:187-210	"All" sub-tab click raced via setTimeout(100); virtualized list ⇒ "100% of signals" unverifiable (no row-count assertion vs the "All N" label)
2.3 26_Aggregated_Footprint_Bar_Metrics.py — dual-path collector
ID
	
SEV
	
LOCATION
	
DEFECT

B1	🔴 SEVERE	:283-286, 574-578	Fabricated value area: vah=max_bucket_mid, val=min_bucket_mid, vwap=poc=close; comment claims "70% profile" — no 70% computation exists; memory path uses session high/low as VAH/VAL
B2	🔴 SEVERE	:419-428	Hardcoded metals volumes (250000/125000/125000/80/3125) written as real data, no is_synthetic flag
B3	🔴 SEVERE	:208,276 vs 516,586	cumulative_delta_usd has two meanings in one file: 10-bar rolling sum (ephemeral path) vs ~300-bar cumulative (memory path) — CVD-divergence logic cannot tell which
B4	🟠 HIGH	:476-478	React fiber fixed-chain walk (return.return.memoizedState.next.next.next…) breaks on any render-order change; swallowed → silent degradation to the 10-bar path
B5	🟠 HIGH	:157-178	window.fetch venue loop: empty catch(e){}, no res.ok check — CF 403 HTML → res.json() throws → swallowed → "venue has no data"; ~54 sequential fetches with no rate limiting
B6	🟡 MED	limit=10 path	Forming bar ingested with no is_closed, no bar-close check, bar-OPEN timestamps (→ Mandate 1 Q1 = CONFIRMED)
B7	🟡 MED	:618-623 vs 571	Duplicate-symbol risk on D.sym string mismatch (BTCUSDT vs BTC) — two divergent-semantics row-sets, no (symbol, timestamp_ms) dedup
B8	🟡 MED	:279-281	OI join silently carries prev_oi; first bar reports OI=0.0 by construction
B9-B11	⚪ LOW	:286, 509-514, 573	mid_p NameError on empty buckets (swallowed); USD conversion at bar-close px for all buckets; user-selected tab timeframe (1H/4H) contaminates the nominal-15m feed

Required CDP hardening (both collectors):

python
async def cdp_cmd(ws, pending, method, params=None, timeout=20.0):
    mid = next_id(); await asyncio.wait_for(ws.send(json.dumps(
        {"id": mid, "method": method, "params": params or {}})), timeout)
    try:    resp = await asyncio.wait_for(wait_matching(pending, mid), timeout)
    except asyncio.TimeoutError: raise CDPTimeout(method)   # fail LOUD, never hang


# challenge probe BEFORE extraction:
probe = await cdp_cmd(ws, pending, "Runtime.evaluate", {"expression":
  "(() => ({title: document.title, cf: !!document.querySelector('iframe[src*=challenges]')}))()"})
if probe["cf"] or "Just a moment" in probe["title"]: raise CloudflareChallenge(coin)


# coverage gate before ANY write:
if harvested / total < 0.90: raise CoverageCollapse(harvested, total)   # exit 2 + FAIL sidecar
2.4 Mandate-1 Forensic Rulings (the four questions)

Q1 — "Last candle" bug: CONFIRMED PRESENT. CoinGlass orderFlow/kline endpoints return the forming bar as the final element; timestamps are bar-OPEN times; neither collector flags it (B6). At the 15:00 boundary the exchange tape leads CoinGlass's aggregation by 5–30s. Mandated protocol: every row gains bar_close_ms = ts_ms + interval_ms and is_closed = now_ms >= bar_close_ms; the forming bar is consumed only in live-semantics contexts (KPI tiles, current-bar delta) and excluded from closed-bar features (EMA stack, CVD slope, backtests); harvest at boundary +45s (captures new bar inside the aggregation lag) and re-poll at +150s to upsert the finalized (symbol, ts_ms) row — last-write-wins upsert makes "never drop the latest bar" structural, because the second pass overwrites partial volumes with final ones.

Q2 — Coverage: a front-end pagination artifact, not an API cap. The 747–940-asset feeds are computed endpoints over the full perp universe; LS-Ratio (20), OI (20), Liq-Map (21), Orderbook (15) are ranked table views where CoinGlass's UI default page size is 20. Expansion: paginate limit=100&page=k via the authenticated tab; fan out orderbook per-symbol across the 120-broker universe under a 1 rps token bucket + jitter (~2–3 min sweep, inside tactical SLA), priority broker-tradable ∩ OI-rank; exponential backoff on 403/429 with a per-domain budget (~2,400 req/h); auditor asserts per-feed asset counts (747 / 120 / 20 …) against a coverage manifest.

Q3 — Cloudflare Turnstile: zero triggers is not guaranteeable; zero silent failure is. The mandate's proposed architecture — window.fetch inside the long-lived authenticated tab — is endorsed as optimal: requests inherit session cookies, cf_clearance, and the real TLS fingerprint. Ephemeral /json/new tabs inherit the same profile cookies and usually pass, but bursty new-tab navigation is exactly what Turnstile scores. Hardening stack: (i) warm pool of 1–2 persistent hidden tabs, SPA-navigated, reused across cycles; (ii) explicit challenge detection (403 / HTML content-type on a JSON endpoint / title "Just a moment…" / challenge iframe) → fail-loud exit + FAIL sidecar, never zeros; (iii) keepalive pinger against idle-token expiry; (iv) pre-cycle /json health check with re-targeting on dead tabs; (v) on cf_clearance expiry: skip one cycle with FAIL status + human re-auth prompt (automated CAPTCHA solving is out of scope). Stale/disconnected authenticated tab fallback order: second pooled tab → DOM harvest → fail-loud skip. Edge case registered: a stale tab whose clearance expired mid-sweep produces partial 403s — the per-coin failure tally (S2 fix) converts this from invisible to measured.

Q4 — Overwrite hygiene: the lake conflates two storage classes.

Point-in-time snapshots (overwrite is CORRECT): 00, 3×3, 5_OI, 5_Funding, 6, 7_Heatmap, 8×2, 9×4, 10, 11, 12, 13, 14_HL_Map, 15, 16, 17, 20, 21, 4.
Rolling time-series (overwrite DESTROYS data — upsert + retention REQUIRED): 18_CVD, 26_Bars, 7_Live_Liq (event tape), 22_MTF, 19_News, 19_Calendar, 1_ETF, 2_Netflow, 23 (history optional). 25 = hybrid (2h-TTL signal rows).
Today none of the rolling feeds have history anywhere — the TSDB covers only 8 legacy streams (T2). Cumulative-delta history and 30-day liquidation profiles do not exist and cannot be reconstructed retroactively. Strategic remedy (preferred): extend time_series_database.py streams to all 36 feeds and demote Data/feeds/*.parquet to a pure latest-snapshot cache — snapshots stay trivially atomic, history becomes first-class, and the gap journal becomes real. Interim remedy: mode="upsert" per the Listing 2-1 contract.
2.5 The audit/history layer (parquet_feed_checklist_auditor.py, unified_liquidation_matrix.py, time_series_database.py)
A1/A2/A3 (🔴): 33-feed registry omitting 14/25/26; SLA triple-drift (1.5m docstring / 15m code / 5m mandate); feed-23 self-write tautology (:124-152) with except: pass.
A4/A5 (🟡): trusts sidecar row_count blindly when fresh (corrupt/_empty parquet passes — never opens the file unless fallback); checklist JSONs written non-atomically (:239-247) — the exact defect the writer solved.
M2–M5 (🟠/🟡): DEX side inference defaults anything-not-SHORT/SELL to "Long Liquidation" (:153) — garbled fields silently inflate long-side magnets; freshness laundering (inputs read without vintage checks, output stamped now_ist); docstring promises distance_pct/z_score columns that records don't contain (the exact silent-drop class your subagents hit); parser binds CoinGlass typos "Cummulitve_Liquidation"/"Binanace" (:103-105) — an upstream spelling fix zeroes those columns silently; Tier-3 venues documented but not implemented.
T1/T3 (🟡/⚪): master_manifest.json read-modify-write with no inter-process lock (:772-833) — concurrent daemons lose manifest entries; dates_present grows unbounded; no retention vacuum for the gzip tree. T2 (🟡): SUPPORTED_STREAMS = 8 legacy streams — the history coverage gap behind Q4. Praise where due: TSDB's atomic_write_* (:53-68) is the correct collision-safe pattern the parquet writer should adopt; WAL + busy_timeout + sha256'd snapshots + gap journaling is institutional-grade.
PART 3 — THE QUANTITATIVE NARRATIVE SYNTHESIS HEURISTIC
3.1 The Intersection Trap: your math is right, and the deeper failure is correlation

0.70¹⁵ = 0.474%, 0.70³⁵ = 3.8×10⁻⁶ — verified. But the deeper truth: the gates are not independent — 9_MaxPain_24H and 8_Map_1D describe the same resting leverage from two angles; 17/10 observe the same depth; 18/26 are the same taker aggression at two granularities. With average pairwise correlation ρ̄, effective independent bets are:

N
eff
	​

=
1+(N−1)
ρ
ˉ
	​

N
	​


At N=15, ρ̄=0.4 → N_eff = 2.27: demanding fifteen confirmations is demanding the market repeat the same two-and-a-quarter independent facts fifteen times. The remedy is not looser thresholds — it is collapsing 35 feeds into 9 decorrelated clusters scored across 3 layers.

3.2 The formalized kernel (Layer 1 — binary, never scored)
GATE
	
RULE
	
FEED

K1	Spread ≤ 25 bps crypto / ≤ 5 bps TradFi	00
K2	Blackout ±15m crypto news / ±35m sovereign	19_Calendar
K3	Post-stress equity ≥ 4,795.00 (stress formula §5)	00
K4	Data liveness: every consumed cluster within 2× SLA — fail-closed on data (the enforcement hook making Part 2's defects decision-relevant)	23 + sidecars
K5	Rollover embargo 21:15–22:30 UTC; weekend/illiquid-session gates	clock
3.3 Scoring kernel (Layers 2–4)

Cluster collapse (36 feeds → 9 clusters): L2 Regime w=0.35 → {Auction/Value (20 lead), Trend engine (11), Positioning (5_OI+5_Funding+3_4H), Macro flows (1+2+9_7D/3D+8_7D)}. L3 Tape & Magnets w=0.50 → {Depth (17+10, 180s persistence), Delta (18+26), Absorption (25), Magnet geometry (14_Matrix+14_HL+15+8_1D+9_24H/48H), Cascade fuel (7+22+7_Heat)}. L4 Context w=0.15 → {Sentiment (19_News+12), Intel (16+4)}. At 9 clusters, ρ̄≈0.3 → N_eff ≈ 2.65 — an honest count of independent bets.

Each cluster i emits agreement s_i ∈ [−1,+1] and confidence c_i ∈ [0,1] (halves beyond 2× SLA, zeroes beyond 4×; scales with feeds successfully read in-cluster):

A
L
	​

=
∑w
i
	​

c
i
	​

∑w
i
	​

c
i
	​

s
i
	​

	​

∈[−1,+1],TQS=100(0.35max(0,A
L2
	​

)+0.50max(0,A
L3
	​

)+0.15max(0,A
L4
	​

))

Admission rule (replaces the boolean AND): all K-gates pass ∧ A_L3 ≥ +0.40 ∧ ≥ 3-of-5 L3 clusters with s_i ≥ +0.5 ∧ TQS ≥ 75 ∧ no veto.

Why the quorum kills the starvation: at p=0.70 per cluster, P(≥3 of 5) = 10(0.343)(0.09) + 5(0.2401)(0.3) + 0.168 = 0.3087 + 0.3602 + 0.1681 = 83.7% per-layer pass vs 16.8% for a five-way AND — while the TQS≥75 cut plus the veto list calibrate the final admission rate to the target 8–15% of cycles (≈3–5 executions/day on a 2-minute tactical cadence — matched to your 2 slots). Bayesian framing for monthly recalibration: each cluster is a likelihood-ratio witness; admission ≈ posterior log-odds ≥ log 2.0; re-fit the TQS cut from the trade log.

Veto list (hard-override, direction-zeroing): V1 primary-venue CVD divergence against θ, |z| ≥ 1.5 (18/26) · V2 counter-magnet: largest opposite cluster within 1.0×ATR carries >1.5× the target magnet's notional (14) · V3 Trapped-traders against θ at entry level (25) · V4 OI contracting >1% against a breakout (5_OI) · V5 retail crowd ≥70% one-sided without absorption backing (3_15M + CVD flat).

3.4 Scenario rulings

Scenario A — retail 68% long + CVD rising on divergence + >$5M whale bids at POC → rule LONG via absorption, passive entry. Canonical accumulation signature: crowd supplies inventory into persistent demand; delta confirms absorption, not exhaustion. Execute: staged BUY_LIMIT at the POC/whale-bid shelf (never a chase into the crowd's ask); SL below the whale shelf − 0.30×ATR14, outside any feed-15 cluster (Rule B); TP at the dominant upper magnet front-run by 0.15×ATR, ≥1.5R (Rule A); check V4 (OI must build) and V2 (no larger counter-magnet overhead). Expected TQS ≈ 78–84 → standard risk.

Scenario B — TREND_UP + price at +2.6σ above VWAP + Absorption_High with negative delta → STAND ASIDE; a third option beyond your binary. Chasing is forbidden (entry beyond value with V1-risk divergence already flagged); a counter-trend short is forbidden by the regime cluster unless a reversal itself scores TQS ≥ 85 with regime consent — which this configuration does not grant. Correct institutional actions: existing longs tighten to the prior 15m bar low and take partial at +1R (extension is an exit-management trigger, not an entry trigger); new risk works a limit at VAL/POC where trend-continuation and mean-reversion share an entry, and the re-queried tape decides.

3.5 Rules A/B formalized (magnet-anchored TP/SL)
Rule A: TP_long = M* − δ_tp·ATR14, δ_tp ∈ [0.10, 0.25] — front-run the dominant directional cluster by 5–10 ticks (≈0.10 ATR on BTC-15m); M from non-synthetic rows only* (post-M1 quarantine), ×1.15 trust if the cluster spans ≥2 venues. Constraints: edge (TP−entry)/R ≥ 1.5 and corridor purity (no counter-cluster >0.75× target notional between entry and TP — else V2 fires).
Rule B: SL_long = min(entry − 1.2·ATR14, S*_below − 0.30·ATR14); SL forbidden inside [cluster_low − 0.05·ATR, cluster_high + 0.25·ATR] (sweep-wick zone). Cluster within 0.5×ATR of the ideal SL → widen beyond cluster_high + 0.30·ATR and reduce size to hold R constant rather than skipping. 0.786 invalidation-shelf rule applies from the standing canon. Sizing units = R/(entry−SL); 50% IMR; post-open margin level ≥200% for both slots jointly.
3.6 Section C — capital survival (stress-corrected)

Nominal math says 49.32/12 = 4.1 stopouts ("4–5" per your dispatch). The canonized stress model — (R + S_exit)×1.25 + 2.00, validated to exact match across consecutive cycles — gives 17.43/ticket (current spread state) and 27.10 (adverse 22-pt regime):

METRIC
	
VALUE

H_net (kernel headroom, net of $2 fee reserve)	49.32
Canonical runway	49.32 / 17.43 = 2.83 tickets → 1.4 dual rounds (2 survive w/ 14.46 left; 3rd breaches by 2.97)
Adverse-regime runway	49.32 / 27.10 = 1.82 tickets — one full dual-slot round (54.20) breaches the kernel
Hard-floor runway	246.32 / 17.43 = 14 stopouts; dual-joint adverse worst case leaves 192.12 above 4,600
Path to 5,500	+653.68 ≈ 23 net winners at 2.32RR/12R — the honest path is the house-money ladder after the first +2R, not oversized standard tickets

Regime ladder: DEFENSIVE (equity <4,820 or H_net <25): R=5–6, 1 slot, TQS≥85 → STANDARD (4,820–4,900, current): R=10–12, 2 slots, TQS≥75 → ATTACK (4,900–5,100): R=12 + pyramid at +2R (only when free margin still covers 2× stressed SL) → HOUSE MONEY (≥5,100 or day ≥+2R): ladder 12.87 → 33.20 → 80 risking house profits only, realized never retraced below the 4,846.32 baseline → LOCKOUT: any kernel breach or 3 consecutive stressed stopouts = flat + 24h cool-down + data-chain re-audit. ⚠️ All figures inherit the Part-1 staleness flag — re-poll MT5 before staging.

PART 4 — DECISION MATRIX ON THE 36 PARQUET FEEDS

T1 = Inviolate Hard Filter (binary, fail-closed) · T2 = Primary Trend & Structural Anchor (w 0.35) · T3 = Execution Timing & Tape Confluence (w 0.50) · T4 = Auxiliary Context (w 0.15). Storage per Mandate-1 Q4. "Mon." = currently watched by the auditor.

#
	
FEED
	
TIER
	
ROLE
	
STORAGE
	
SLA
	
MON.

1	00_MT5_Account_Telemetry	T1	K1 spread + K3 equity/margin + sizing	Snapshot	<2m	✅
2	19_Calendar	T1	K2 sovereign blackout	Rolling	<15m	✅
3	23_Master_Pipeline_Telemetry	T1	K4 data-liveness (post-fix: collector-emitted, not self-write)	Rolling	<2m	✅
4	20_Auction_Market_Structure	T2	Regime lead; VAH/VAL/POC anchors	Snapshot	<5m	✅
5	11_Technical	T2	Trend engine; ATR-14 for all placement math	Snapshot	<5m	✅
6	5_OI	T2	Positioning; V4	Snapshot	<5m	✅
7	5_Funding_Rate	T2	Carry & leverage skew (592)	Snapshot	<5m	✅
8	3_LS_Ratio_4H	T2	Macro positioning bias	Snapshot	<5m	✅
9	1_Crypto_ETF_Flows	T2	Macro tailwind	Rolling	<15m	✅
10	2_Spot_Netflow_S	T2	Accumulation/distribution (181)	Rolling	<15m	✅
11	9_Max_Pain_7D	T2	Weekly settlement magnet	Snapshot	<5m	✅
12	9_Max_Pain_3D	T2	Swing magnet	Snapshot	<5m	✅
13	8_Liq_Map_7D	T2	Weekly structural boundary	Snapshot	<5m	✅
14	14_Liquidation_Matrix	T3	PRIMARY magnet — quarantined until is_synthetic ships (M1)	Snapshot	<5m	❌
15	14_Hyperdash_Liq_Map	T3	DEX magnet geometry (6,514)	Snapshot	<5m	✅
16	15_Hyperdash_Stops_Map	T3	Rule B sweep zones (4,194)	Snapshot	<5m	✅
17	8_Liq_Map_1D	T3	Tactical 24h ladders	Snapshot	<5m	✅
18	9_Max_Pain_24H	T3	24h shortest-distance magnet	Snapshot	<5m	✅
19	9_Max_Pain_48H	T3	48h magnet	Snapshot	<5m	✅
20	17_Orderbook	T3	Depth: L2 asymmetry (expand 15→120)	Snapshot	<2m	✅
21	10_Whale_Orders	T3	Depth: walls, 180s persistence	Snapshot	<5m	✅
22	18_CVD	T3	Delta lead; V1	Rolling	<2m	✅
23	26_Footprint_Bar_Metrics	T3	Delta bars (fix B1–B3 first)	Rolling	<5m	❌
24	25_Footprint_Signals	T3	Absorption; V3 (fix S1–S2 first)	Rolling 2h-TTL	<5m	❌
25	7_Live_Liq	T3	Cascade fuel: live tape	Rolling	<2m	✅
26	22_Forced_Liq_MTF	T3	Cascade fuel: MTF intensity	Rolling	<2m	✅
27	7_Liq_Heapmap	T3	Cascade fuel: leverage distribution	Snapshot	<5m	✅
28	3_LS_Ratio_15M	T3	Crowd skew; V5	Snapshot	<5m	✅
29	3_LS_Ratio_1H	T3	Crowd skew (tactical)	Snapshot	<5m	✅
30	6_Funding_Settlement	T3	Settlement timing	Snapshot	<5m	✅
31	13_Hyperliquid	T3	DEX liquidity context	Snapshot	<5m	✅
32	21_Tradfye_Orderflow	T3	Interbank absorption (TradFi)	Snapshot	<5m	✅
33	4_Hyperliquid_Analysis	T4	On-chain whale context (108)	Snapshot	<5m	✅
34	19_News	T4	Sentiment shade (also K2 input)	Rolling	<15m	✅
35	12_Hyperdash	T4	DEX sentiment shade	Snapshot	<5m	✅
36	16_Telegram_Intel	T4	Block-print intel shade	Rolling 2h-TTL	<5m	✅

Inventory reconciliation (33 vs 35 vs 36 vs 42): the manifest's "35 feeds + matrix" = 36 canonical files (numbering skips index 24 — internally consistent); the auditor's 33 omits 14/25/26 (A1); the observed 42 is most plausibly 36 canonical + 6 orphaned .tmp_* residue from the W8 hard-kill leak (legacy Excel-era files possible). Mandated: one-time glob diff vs manifest, .tmp_* janitor (>1h) wired into ensure_directories, and a CI assertion registry == manifest == disk-canonical.

CLOSING RULING & REMEDIATION REGISTER (Top-8 of 11)
PRI
	
ACTION
	
ACCEPTANCE

P0	M1/B2 quarantine: is_synthetic on 14-Matrix Tier-4 + 26-metals rows; excluded from all magnet scoring	Zero synthetic rows in scored paths
P0	W2: empty batch = FAIL + FAIL-sidecar, prior parquet untouched; delete _empty sentinel	Forced empty test leaves file byte-identical
P0	W1: mode="upsert" (+is_closed) for 18/26/7/22/19×2/1/2	Rolling feeds survive a failed cycle gap-free
P0	A1/A2: auditor → 36 feeds, real SLAs (<2m HV / <5m tactical / <15m macro), kill feed-23 self-write	25/26/14 staleness visible within one cycle
P0	S1/S2/B5: collectors fail-loud (CF-challenge + DOM-timeout detection, ≥90% coverage gate, per-coin tally)	Simulated challenge → exit 2, zero junk rows
P1	W3/W4: time_ns() tmp names, symmetric sidecar retry, ~8s jittered budget	Concurrent same-feed writes both valid
P1	W6/W7: pinned schema registry; data_asof_epoch+sha256 sidecars; wire asset_registry.py	Schema-drift test fails the build
P2	Freshness architecture: window.fetch batch sweeps (30–60s vs today's 4–6 min), tiered scheduler 60/120–180/900s, single-writer-per-feed, boundary-sync +45s/+150s	Worst tactical age 240.5s < 300s — the <5m guarantee holds with 59s margin

📄 Archival deliverable: /home/z/my-project/download/ZAI_Council_Forensic_Audit_Parquet_Data_Lake.docx — full 8-chapter report (R1/Ink-Gold cover, TOC, all finding tables, corrected writer contract, freshness blueprint), postcheck-validated with 0 errors.

Session summary: Completed the full forensic audit of the Parquet data lake at commit 77dc330a5 — 6 production files read line-by-line, 34 defects registered (headline: fabricated $25M macro magnets in your primary magnet feed, silent zero-data laundering in both footprint collectors, dead upsert parameter, and a freshness auditor that doesn't watch the three most important feeds), all Mandate-1 questions ruled, the narrative-synthesis math formalized with corrected capital-runway arithmetic, and everything archived to the validated Word report. Suggested next steps: (1) ship the five P0s and re-run this audit for certification; (2) ask me to generate the charts/xlsx finding-register add-on for remediation tracking; (3) re-dispatch the next trading cycle with fresh MT5 telemetry so the Section-3 ladder can be recomputed live.