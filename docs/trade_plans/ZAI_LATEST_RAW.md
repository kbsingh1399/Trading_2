INSTITUTIONAL CODE AUDIT & PIPELINE REVIEW — CONTINUOUS EXCEL RUNNER & HARVESTER SUITE

Auditor: Z.ai Sovereign Council (GLM) — Pipeline & Systems Review Branch
Repository: github.com/kbsingh1399/Trading_2, branch main
Repo HEAD (OOB-verified): 9bea11df9735e5ecdb08c22b4deb0f54bac14137 — "feat(sync): mirror full local workspace and telemetry [as_of 2026-10-25 15:54:31 UTC]"
User-stated commit: d57ef48d8 (superseded); last envelope provenance: c1285bd9… (superseded)
Method: full static read of 7 target files (2,493 LOC core) + forensic analysis of in-repo production telemetry (1,466 events, 2026-10-21 → 2026-10-23) + OOB banner-age audit of the mirrored 35-sheet workbook + empirical openpyxl cost measurement on the real 5.85 MB file.

[ALERT] TELEMETRY STALE WARNING
ARTIFACT
	
STATE @ MIRROR 2026-10-25 15:54:31 UTC
	
DIAGNOSIS

Data/DataBase_Trading.xlsx	31 / 32 canonical sheets STALE (>5m); only 3_Exchanges_LS_Ratio_4H fresh (4.6m)	Intra-phase lost-update annihilation + runner daemon outage
Worst offenders	7_Liq_Heapmap 269.9m · 7_Live_Liq 269.3m · 9_Liq_Max_Pain_48H 211.1m · 10_Whale_Orders 75.4m · 00_MT5_Account_Telemetry 67.0m · 5_OI 62.0m	MT5 staleness blinds the <4,600 hard-floor defense
Data/telemetry/pipeline_events.jsonl	Last event 2026-10-23 16:24:37 UTC — ~2d 5h observability blackout at mirror	Runner/telemetry emitter dead; no supervisor restarted it
Data/excel_health_audit.json	File does not exist in workspace	excel_data_quality_checker.py relative-path + fail-silent returns → never written (K-08/DR-22 root cause)
Data/excel_all_sheets_checklist.json	Written 15:54:30 UTC: 1/32 PASS (3.1%)	Honest scorecard; the "< 5m guarantee" is empirically operating at 3%
1. EXECUTIVE VERDICT

The suite is a well-intentioned, professionally-styled system whose core concurrency thesis is inverted. The engineering craft visible in excel_lock_hook.py (re-entrant thread-local locking, BytesIO snapshot loads, atomic rename under ~50 ms) is real — but it solves the wrong critical section. It serializes the rename, while the read→mutate→write transaction — the thing that actually defines workbook state — runs 100% unlocked for 45–240 seconds per module. With 3 concurrent writer subprocesses per phase, the workbook is a last-writer-wins battleground: every module's wb.save() serializes all 35 sheets from its own stale in-memory snapshot, so each late replacer silently annihilates every overlapping writer's sheet updates.

Three quantitative consequences, all empirically confirmed:

The observed 1/32 freshness pass rate is the stable equilibrium of this race, not bad luck. Each phase's last replacer determines surviving state; ~1–3 sheets per cycle can be fresh at audit time. The runner then spends the next cycle re-harvesting the annihilated sheets — a permanent refresh-wipe-refresh livelock that consumes 100% of pipeline capacity destroying its own output. This is the mechanism behind 11+ consecutive envelope cycles of excel_freshness_verified=false / K-08 "false freshness" and the 12-cycle DENIED_FAIL_CLOSED HOLD cascade on the trading council side.
The 5-minute SLA is arithmetically unreachable. Telemetry (n=80 FULL_PARALLEL_CYCLE) shows mean full-cycle time 764 s (12.7 min), p95 ≈ 1,594 s. Per-sheet refresh period ≈ cycle time + 120–180 s sleep ≈ 15 min ≫ 5 min. Browser-pool utilization at a uniform 300 s period is ρ ≈ 2.2 per 3 lanes — oversubscribed by more than 2×; no scheduler, priority heap, or token bucket can schedule an unschedulable workload.
Every module pays a ~21 s monolithic workbook tax. Measured on the real file: full load 13.78 s + full save 7.31 s, peak RSS 452–476 MB per process. × 32 modules = 675 s of serialized workbook I/O per cycle — 88% of the entire 5-minute SLA budget burned on openpyxl parse/serialize before any data is fetched. With 3 concurrent processes at ~450 MB each on a box already at 78% mean / 97% peak RAM load (telemetry), memory pressure is the observed throttle, not a hypothesis.

Secondary but severe: the production orchestrator that emitted the 1,466 telemetry events (API_PARALLEL_HARVEST, EDGE_CDP_JOB, BATCH_EXCEL_COMMIT) does not exist in the repository — the repo's runner.py imports neither logger_config nor emit_telemetry_event. The deployed pipeline is unversioned and unreproducible. And excel_data_quality_checker.py (the health-audit writer the envelopes depend on) uses relative paths and returns silently on every failure path, leaving whatever stale JSON exists standing forever — the precise anatomy of the frozen excel_health_audit.json.

Verdict: the architecture cannot be patched into compliance at its current shape. It requires the single-writer inversion (collect→commit), tiered scheduling, and a storage decoupling — all specified below with production-ready code. None of these findings warrant a shallow abort: every defect has a concrete, implementable remediation, and the harvester modules' CDP discipline (PUT /json/new, aria-scoped MUI interaction, single-reload hydration fallback) is genuinely above median for this class of scraper.

2. DIMENSION A — CONCURRENCY & LOST UPDATE PREVENTION
2.1 The answer to the headline question: YES — Process B wipes Process A's Sheet 1 update.

Openpyxl has no partial save. Workbook.save() serializes every sheet in the in-memory object to a complete new xlsx. Process B's in-memory workbook is the T=0 snapshot (loaded via locked_load_workbook, which releases the Windows handle — and the inter-process lock — after a ~5 ms byte-read). When B saves at T=15 s and atomically renames over the master, the installed file contains B's Sheet 2 mutation plus B's T=0 view of Sheet 1 — A's T=10 s Sheet 1 update is annihilated, atomically and silently. The lock hook's own docstring advertises the wound as a feature: "Temporary file saves (.tmp.xlsx) run 100% concurrently without lock contention"* — that concurrency window is the lost-update window.

2.2 Ground truth in the code

3_Exchanges_LS_Ratio_15M.py (identical in 1H/4H and 29 other modules):

python
# lines 415-426 — the lock wraps ONLY the load:
with (lock if lock else _NoLock()):
    wb = openpyxl.load_workbook(excel_path)      # lock released on block exit
# lines 428-551 — 120+ lines of UNLOCKED mutation (network already done;
#                 sheet remove/create, ~200 styled rows, banner stamp)
# lines 553-560 — save to tmp (unlocked by design), then:
temp_excel.replace(excel_path)                    # hook takes lock for ~50 ms rename

The vulnerable window per module is load → rename ≈ 45–240 s (telemetry means), and execute_full_cycle() runs ThreadPoolExecutor(max_workers=3) in each phase (runner.py lines 188, 203) — 3 overlapping writers per phase, guaranteed overlap.

2.3 Should the critical section encompass load → mutate → save?

No — not as the modules are currently shaped. The mutation window contains sheet construction and (in most modules) data collection is before it, but any critical section spanning network I/O (up to 240 s × 32 modules) serializes the whole pipeline into a 12+ hour cycle. The correct pattern is collect-then-commit:

Collect (parallel, unlocked, no workbook): each module's harvester returns Python records — network I/O, DOM extraction, all concurrently.
Commit (serial, locked, fast): exactly one process performs load-fresh → apply N sheet updates → tmp-save → fsync → atomic replace inside a single inter-process critical section.

This eliminates lost updates by construction (only one mutator ever exists), and collapses 32 × 21 s = 675 s of workbook I/O into one ~21–25 s batched commit per cycle. Empirical support that the deployed (unversioned) orchestrator was already groping toward this: the telemetry contains 61 BATCH_EXCEL_COMMIT events — the concept existed in production but was never formalized in the repo.

2.4 The definitive pattern ranking
RANK
	
PATTERN
	
LOST UPDATES
	
THROUGHPUT
	
VERDICT

1	Single-writer queue/daemon (modules emit records; one committer folds them)	Impossible	Highest (1 load+save/cycle)	Recommended target
2	Per-module collect→commit (module re-loads fresh under lock, mutates, saves, releases)	Impossible	32 × ~21 s serialized commits ≈ 675 s/cycle	Acceptable bridge
3	Critical section = full module incl. network	Impossible	Catastrophic (serializes all I/O)	Rejected
4	Status quo (lock at rename only)	Guaranteed	"High"	Defective
3. DIMENSION B — WINDOWS NTFS LOCKING & ATOMIC REPLACEMENT
3.1 What actually happens when an external reader holds the file

os.replace on Windows is MoveFileEx(MOVEFILE_REPLACE_EXISTING). It fails with PermissionError (WinError 32 sharing violation / WinError 5 access denied) whenever any handle to the target is open without FILE_SHARE_DELETE — which includes:

An analyst with the workbook open in Excel (Excel holds the file without share-delete);
Any background reader doing plain open(path, 'rb') (e.g. a script that doesn't go through the hook);
An antivirus / search indexer transiently touching the file.

So yes: with a shared-read handle active, the atomic replace fails, and the failure mode in the current code is a retry storm that holds the inter-process lock while retrying:

locked_path_replace retries 25 × sleep(0.05·attempt) ≈ 15 s while holding the FileLock;
The module-level loop around temp_excel.replace() (LS modules line 558) retries a further 30 × 1.0 s = 30 s, each iteration re-entering the lock/retry sandwich;
Because pathlib.Path.replace internally calls os.replace by module-global lookup at call time, and both are monkeypatched, the original Path.replace captured by the hook re-enters locked_os_replace — nested 25×25 retry loops;
After exhaustion the module raises → runner logs FAIL → sheet stale. Meanwhile every other writer in the pool was lock-blocked behind the retry storm.

Worst case with a human in Excel for 10 minutes: the entire writer pool thrashes, burns its subprocess timeouts, and strands .tmp.xlsx files (only reaped at next cycle start, and only if >10 s old).

3.2 Hardening locked_path_replace
Do not retry while holding the lock. Acquire → attempt once → release → backoff (exponential with jitter, capped) → re-acquire. Lock hold must remain ~ms.
Durability barrier: os.fsync() the temp file before rename (currently absent → power-loss can leave a zero-length master after a crash between rename and cache flush).
Bounded escalation: after N failures, write a sidecar version DataBase_Trading_<seq>.xlsx and atomically update a tiny pointer file (or directory junction Data/current → v<seq>); readers resolve through the pointer, held handles keep reading the old version (copy-on-write semantics for free), and no replace ever collides with a human again.
Sacrificial rename: if the pointer indirection is rejected, at minimum rename target → *.old (may also fail), then replace — never loop inside the lock.
python
def locked_path_replace_v2(self, target, *args, **kwargs):
    """Atomic replace with lock-free retry, fsync durability, sidecar escalation."""
    target = pathlib.Path(str(target))
    if "DataBase_Trading.xlsx" not in target.name or ".tmp." not in str(self):
        return _orig_path_replace(self, target, *args, **kwargs)
    # 1. durability: flush temp file contents before the rename
    with open(self, "rb+") as fh:
        os.fsync(fh.fileno())
    # 2. single attempt per lock acquisition; exponential backoff BETWEEN acquisitions
    for attempt in range(8):
        try:
            with get_lock(timeout=30.0):
                return _orig_path_replace(self, target, *args, **kwargs)
        except PermissionError:
            if attempt == 7:
                break
            time.sleep(min(5.0, 0.25 * (2 ** attempt)) * (0.5 + random.random()))
    # 3. sidecar escalation — never lose the commit to a reader collision
    seq = int(time.time() * 1000)
    sidecar = target.with_name(f"{target.stem}_v{seq}.xlsx")
    _orig_path_replace(self, sidecar)
    pointer = target.with_name("DataBase_Trading.current.json")
    tmp_ptr = pointer.with_suffix(".json.tmp")
    tmp_ptr.write_text(json.dumps({"version_file": sidecar.name, "committed_utc":
                      datetime.datetime.now(datetime.timezone.utc).isoformat()}), encoding="utf-8")
    _orig_path_replace(tmp_ptr, pointer)   # tiny file; collision probability ~0
    return sidecar
4. DIMENSION C — CDP AUTOMATION RESILIENCE & ANTI-STALL
4.1 Current design strengths (credit where due)
open_ephemeral_tab uses PUT /json/new (line 92) — already correct for Chrome/Edge 111+, where GET /json/new was removed. Many scrapers still ship that latent bug; this codebase does not.
Tab lifecycle is try/finally-closed (line 401–402); the runner additionally reaps strays while protecting Arena.ai / Z.ai tabs (reap_scraping_tabs, runner.py lines 107–129) — thoughtful operator-aware hygiene.
The 40-step readiness poll + single-reload fallback (lines 186–207) is a sound hydration-stall mitigation.
Timeframe selection is aria-scoped (aria-controls → listbox → option text), not class-hash-scraped — the right approach against MUI.
4.2 Confirmed fragilities (each observed or mechanically derivable)
Silent wrong-timeframe contamination (HIGH). After clicking the timeframe option (lines 240–258) the module sleeps 0.8 s and harvests — it never re-reads the button label. If the MUI menu opens virtually, the option click misses, or the listbox id from aria-controls is stale, the module harvests the default timeframe and writes it into the 15M/1H/4H sheet anyway — three near-identical modules can then all contain e.g. 1H data, corrupting every downstream LS-ratio signal with no error anywhere in the chain.
Readiness heuristic couples to layout cardinality. rows[0].children.length >= 15 (line 182) assumes ≥5 exchange blocks × 3 columns in the first .ant-row. Any CoinGlass change to virtualization, exchange count for minor assets, or column structure → readiness never true → reload → still false → [] → module FAIL → stale sheet. Same for the startsWith('Exchanges') heading walk, which walks querySelectorAll('*') and forces innerText (a reflow-forcing property) on every element — executed up to 40 × per asset × 18 assets. That is the single largest client-side CPU cost in the harvest and the reason readiness polling itself degrades under load.
Rapid Page.navigate × 18 per tab, per module, 20 modules/cycle. Consequences: renderer heap growth (Next.js keeps route state; detached DOM accumulates), ~0.5 s inter-asset dwell with no jitter (bot-signature pacing), and 3 concurrent ephemeral tabs per cycle hammering the same origin — Cloudflare challenge/429 risk. The single-reload fallback will loop into a challenge page if challenged (reload of a challenge serves another challenge) — currently indistinguishable from a hydration stall at the code level.
No heap management. Nothing calls HeapProfiler.collectGarbage or recycles the tab on a schedule; a 24/7 cadence accumulates memory until the renderer OOMs and the ws silently dies mid-cycle (surfacing as the module's generic exception → all_harvested partial return → partial sheet commit).
4.3 Ephemeral vs persistent tab — the verdict

Hybrid: one persistent, named tab per module-family, recycled on a schedule.

Ephemeral-per-cycle (current): clean process state each run, but pays ~0.5–1.5 s tab creation 20×/cycle, multiplies /json/new automation surface, and forfeits SPA warm state.
Fully persistent: fastest (client-side route navigation, no target churn), but unbounded heap growth over days.
Recommended: persistent tab per (site × timeframe) — for the LS family, three tabs each already locked to its timeframe (eliminating defect C.2.1 and the per-asset toggle entirely); forced GC (HeapProfiler.enable + collectGarbage) every cycle; full close/reopen every 30 min or after 3 consecutive extraction failures; navigation via Page.navigate between asset routes with jittered 1.5–3 s dwell.
python
async def cdp_eval(ws, expr, id_):
    await ws.send(json.dumps({"id": id_, "method": "Runtime.evaluate",
                              "params": {"expression": expr, "returnByValue": True}}))
    return json.loads(await ws.recv()).get("result", {}).get("result", {}).get("value")


# --- Post-toggle VERIFICATION (defect 4.2.1 fix) ---
read_tf = "(() => {const b = document.querySelector('button.MuiSelect-button,button[role=combobox']');"
           " return b ? b.innerText.trim() : null;})()"
for _ in range(10):
    if (await cdp_eval(ws, read_tf, 99) or "").lower() == target_timeframe.lower():
        break
    await asyncio.sleep(0.3)
else:
    raise TimeframeToggleError(f"{asset}: selector stuck at {await cdp_eval(ws, read_tf, 99)!r}; "
                               f"refusing to write wrong-timeframe rows into {SHEET_NAME}")


# --- Heap hygiene each cycle ---
await ws.send(json.dumps({"id": 90, "method": "HeapProfiler.enable"}))
await ws.recv()
await ws.send(json.dumps({"id": 91, "method": "HeapProfiler.collectGarbage"}))
await ws.recv()
5. DIMENSION D — MEMORY & CPU SCALABILITY

Measured on the real workbook (this audit, sandbox):

OPERATION
	
TIME
	
PEAK RSS

load_workbook (read-write)	13.78 s	452 MB
Workbook.save (full)	7.31 s	476 MB
read_only=True load + iterate 6,914 rows	1.43 s	(flat)

Per-cycle arithmetic at current shape: 32 modules × 21.08 s ≈ 675 s serialized workbook I/O, with 3 concurrent processes × ~450 MB — against telemetry showing the host at 78% mean / 97% peak RAM load. The pipeline is memory-throttled today; every additional sheet or row deepens it.

Why read_only=True / write_only=True cannot fix this: read_only cannot mutate; write_only builds a new workbook from scratch and cannot preserve the other 34 sheets. Mutation-in-place of a monolithic xlsx fundamentally requires whole-document materialization. The file format is the bottleneck, not the library.

Recommended target architecture (the only durable answer): Excel becomes a view, not the database.

Layer 1 — collection: harvesters append rows to SQLite (WAL mode) or per-sheet Parquet shards. O(row) cost, crash-safe, zero cross-process locks (WAL = single writer, many readers, by design — the exact semantics this pipeline needs and that NTFS+openpyxl cannot provide).
Layer 2 — projection: one compiler periodically assembles DataBase_Trading.xlsx from the store (single writer, one 21 s commit) purely for the human/Excel interface.
Layer 3 — consumers: the council, Role A/B estimators, and envelope packagers read the store directly — SQL queries replace DOM-of-Excel scraping, become reproducible, and can be digest-bound (the C347 "recipe undisclosed" DR-28 class of defect disappears when the estimator input is a versioned table reference).

Also: delete or archive the 3 orphan sheets (Crypto_ETF_Flows, Top_Institutions, ETF_Market_Overview) — present in the workbook, absent from CANONICAL_SHEETS and the runner registry; never refreshed, never audited, yet paid for in every one of the 32× loads and saves per cycle.

6. DIMENSION E — SCHEDULER OPTIMIZATION & FRESHNESS SLA
6.1 Why the current loop can never meet < 5.0m
Batch phases are head-of-line blocking: 20 browser modules ÷ 3 lanes × ~70 s mean ≈ 467 s for Phase 2 alone; + Phase 1 ≈ 260 s; + Phase 3 audit; + time.sleep(interval) after completion (runner.py line 360) → per-sheet refresh period ≈ 764–944 s. Telemetry confirms: FULL_PARALLEL_CYCLE mean 764 s, n=80.
Freshness is measured per sheet banner, so a sheet's age at next refresh = full cycle + interval + queue position — structurally ≥ 12–15 min.
Uniform cadence wastes capacity: ETF flows (daily data), Macro Calendar (daily), Max Pain 7D are re-scraped at the same cadence as Live Liquidations. Telemetry failure rates show the cost: ETF 36.6%, Calendar 34.2%, Whale 32.4%, News 28.9%, Auction 24.7% FAIL.

Utilization audit (uniform 300 s SLA, browser pool): Σc/p with telemetry means ≈ 20 modules × ~70 s / 300 s ≈ 4.67 → ρ = 1.56 per lane across 3 lanes > 1.0 → mathematically unschedulable. No scheduler fixes an oversubscribed workload; the workload must be re-tiered.

6.2 The blueprint — Tiered EDF with per-pool admission control

Tier table (periods matched to source velocity, post-Phase-0 runtimes):

TIER
	
PERIOD
	
DEADLINE
	
SHEETS

HIGH	60 s	55 s	00_MT5_Account_Telemetry (post-split ~25 s), 7_Live_Liq (websocket candidate)
MID	300 s	270 s	LS 15M, 5_OI, 5_Funding_Rate, 17_Orderbook, 18_CVD, 10_Whale_Orders, 20_Auction
SLOW-MID	900 s	810 s	LS 1H/4H, 6_Funding_Fee_Settlement, 2_Spot_Netflow_S, 12–16_Hyperdash*, 13_Hyperliquid, 4_Hyperliquid_Analysis, 8_*_Liq_Map*
LOW	1800–3600 s	0.9·p	9_*_Max_Pain_*, 19_News, 19_Calendar, 1_Crypto_ETF_Flows, 22_Forced_Liquidations_MTF

Schedulability after Phase 0 (collect→commit split removes ~15–20 s of workbook I/O from every module) + persistent tabs (−30% CDP time):

API pool (6 lanes): Σc/p ≈ 0.35 → comfortable.
CDP pool (3 lanes): Σc/p ≈ 2.3 → ρ ≈ 0.78 < 1.0 → schedulable with EDF, with deadline-miss ledger as the governor.
If the mandate truly requires all 32 sheets < 5.0 m: required ρ ≈ 4.0/3 lanes ≈ 1.33 even post-fix — reject the uniform SLA; re-state it per-tier (freshness is only meaningful relative to how fast the source changes).

Engine (asyncio, replaces the two sequential ThreadPoolExecutors):

python
import asyncio, heapq, time


TIERS = {  # sheet -> (period_s, pool)
    "00_MT5_Account_Telemetry": (60, api), "7_Live_Liq": (60, api),
    "3_Exchanges_LS_Ratio_15M": (300, cdp), "5_OI": (300, cdp), "17_Orderbook": (300, cdp),
    "18_CVD": (300, api), "5_Funding_Rate": (300, cdp), "10_Whale_Orders": (300, cdp),
    "19_News": (1800, cdp), "19_Calendar": (1800, cdp), "1_Crypto_ETF_Flows": (3600, cdp),
    # ... full table per §6.2
}
EWMA_ALPHA, pools = 0.25, {"api": asyncio.Semaphore(6), "cdp": asyncio.Semaphore(3)}


class Task:
    def __init__(self, sheet, period, pool):
        self.sheet, self.period, self.pool = sheet, period, pool
        self.next_due = time.monotonic()
        self.ewma, self.misses = 30.0, 0
    def __lt__(self, other): return self.next_due < other.next_due   # EDF ordering


async def scheduler(tasks, records_q, stop):
    heap = list(tasks); heapq.heapify(heap)
    while not stop.is_set():
        t = heap[0]
        wait = t.next_due - time.monotonic()
        if wait > 0:
            await asyncio.wait_for(stop.wait(), timeout=wait, return_when=asyncio.FIRST_COMPLETED) if not stop.is_set() else None
            continue
        heapq.heappop(heap)
        async with pools[t.pool]:
            t0 = time.monotonic()
            try:
                await asyncio.wait_for(run_module_collect(t.sheet, records_q),
                                       timeout=timeout_for(t))
                t.ewma += EWMA_ALPHA * ((time.monotonic() - t0) - t.ewma)
            except asyncio.TimeoutError:
                t.misses += 1
                await freshness_ledger.miss(t.sheet, "TIMEOUT")

Freshness ledger (the SLA governor): every module completion/timeout appends {sheet, started, duration, outcome, age_at_start} to Data/telemetry/freshness_ledger.jsonl; a small daemon folds it into excel_freshness.json every cycle, unconditionally (fail-loud: auditor failure writes {"status":"AUDITOR_FAIL",...}, never leaves a stale verdict standing — the K-08 lesson). Deadline misses escalate: 1 miss → log; 2 consecutive → halve concurrency pressure for that pool; 3 → alert + mark sheet DEGRADED in the envelope health block.

Supervision (the DR-24 lesson): the scheduler itself gets a heartbeat file touched every cycle; an external watchdog (NSSM/Task Scheduler with restart-on-exit, or the existing heretic daemon) restarts the runner if the heartbeat exceeds 2 × cycle budget. The mirror showed the runner dead for 2+ days with nothing reviving it — the freshness collapse is as much an availability problem as a concurrency one.

7. CONSOLIDATED BUG REGISTER
ID
	
SEVERITY
	
LOCATION
	
DEFECT

C-01	CRITICAL	excel_lock_hook.py design + all 31 harvester modules	Lost-update race: lock covers rename only; read→mutate→write unlocked 45–240 s; 3 concurrent writers/phase; openpyxl full-workbook save annihilates overlapping writers' sheets. Empirically: 1/32 fresh equilibrium, 11-cycle K-08 false-freshness, 12-cycle HOLD cascade
C-02	CRITICAL	runner.py batch loop + module costs	5.0m SLA unschedulable: cycle mean 764 s (n=80) + post-cycle sleep; browser ρ ≈ 1.56/lane
C-03	CRITICAL	ops	Runner/telemetry dead since 2026-10-23 16:24:37 UTC, no supervisor restart (2d+ blackout; 7_Liq_Heapmap 270 m stale)
C-04	CRITICAL	excel_data_quality_checker.py:32–33, 44–72	Relative paths + fail-silent returns; excel_health_audit.json never written (absent at mirror); stale verdicts stand forever
C-05	CRITICAL	repo vs production	Deployed orchestrator unversioned: telemetry emitters (API_PARALLEL_HARVEST/EDGE_CDP_JOB/BATCH_EXCEL_COMMIT) absent from repo runner.py
H-01	HIGH	LS modules 3_Exchanges_LS_Ratio_*.py:240–258	No post-toggle timeframe verification → silent wrong-timeframe contamination of 15M/1H/4H sheets
H-02	HIGH	ops	00_MT5_Account_Telemetry (hard-floor defense feed) 67 m stale at mirror — floor defense blind
H-03	HIGH	excel_lock_hook.py:95–102 + 22_Forced_Liquidations_MTF.py	Direct-save path holds inter-process lock for full 7–21 s save; plus Path.replace→os.replace double-patch nests 25×25 retry loops
H-04	HIGH	excel_lock_hook.py:105–132	Replace retries while holding lock (≈15 s hold) → writer-pool starvation on any external reader (Excel analyst)
H-05	HIGH	runner.py:259–267 + auditor JSON write	Checklist subprocess without timeout; JSON parse failure silently yields stale_sheets=[] → "All fresh" false-positive no-op cycles
H-06	HIGH	all modules	No os.fsync before rename → power-loss can corrupt master workbook
M-01	MED	LS modules :488–489	Unparseable pct defaults to 50.0 → extraction failure masked as neutral data
M-02	MED	LS modules :169–184	querySelectorAll('*') + innerText full-DOM reflow scans ×40 polls ×18 assets — dominant client CPU cost; readiness couples to children.length >= 15 layout cardinality
M-03	MED	workbook	3 orphan sheets carried in every load/save, never audited or refreshed
M-04	MED	excel_lock_hook.py:39–60	Re-entrancy keyed on thread depth, not lock path → nested different locks in one thread silently skipped; global filelock.FileLock patch affects unrelated users
M-05	MED	auditor :209	max(0, age) clamps future timestamps to fresh (clock-skew masking)
M-06	MED	docs/code	Docstring drift: "6 workers" vs max_workers=3; "5-Minute Guarantee" vs 764 s; "30-sheet" vs 32; interval 180 vs usage 120
M-07	MED	3 × LS modules	590-line triplicated module (timeframe constants only) — fix-once-impossible
M-08	MED	runner.py:149–165	Timeout kill strands .tmp.xlsx mid-replace; reaped only at next cycle start
L-01..L-05	LOW	misc	Redundant except (..., Exception) tuples; substring lock-target matching hits .lock/.bak; reused CDP message ids; silent sitecustomize import failure; loose "time" header matching in auditor
8. TARGETED FRESHNESS ARCHITECTURE (PHASED)

Phase 0 — Correctness hotfix (hours, deploy today)

Invert to collect→commit: harvesters return records (no workbook); one committer applies all pending sheets in a single locked_read_modify_write (§2.4 / code below). I/O per cycle: 675 s → ~25 s; lost updates → zero.
Absolute paths + always-write-fail-loud JSON in both auditors; delete the excel_health_audit.json stale-verdict failure mode.
Runner supervision + heartbeat; docstring drift cleanup; fsync before rename.

Phase 1 — Scheduling (this week)
4. Tiered EDF engine (§6.2): HIGH 60 s / MID 300 s / SLOW-MID 900 s / LOW 1800–3600 s; API pool 6 lanes, CDP pool 3 lanes; EWMA timeouts; freshness ledger feeding excel_freshness_verified honestly.
5. Persistent CDP tabs per site×timeframe + per-cycle GC + 30 min recycle + jittered dwell; post-toggle verification (§4.3).

Phase 2 — Storage decoupling (next sprint)
6. SQLite-WAL / Parquet system of record; xlsx as compiled view; council + envelope consumers query the store directly; estimator inputs become digest-bound table refs (closes DR-28-class reproducibility defects).
7. Per-tier SLA re-statement and scorecard weighting; alerting on deadline-miss ledger.

Expected steady state: HIGH-tier sheets ≤ ~90 s age; MID ≤ 5 m; LOW matched to source cadence; workbook commit once per ~60 s; RAM per module ≤ ~80 MB during collection; single committer peak ~480 MB bounded and constant.

The committer (drop-in for excel_lock_hook.py)
python
def commit_workbook_updates(filename, mutator, *, replace_retries: int = 8):
    """Single-writer batched commit: load-fresh -> mutate -> fsync -> atomic replace,
    ONE critical section. mutator(wb) must be fast and network-free."""
    target = pathlib.Path(str(filename))
    if "DataBase_Trading.xlsx" not in target.name:
        return mutator(_orig_load_workbook(str(target)))   # non-master: passthrough
    tmp = target.with_name(f"{target.stem}_c{os.getpid()}_{int(time.time()*1000)}.tmp.xlsx")
    with get_lock(timeout=120.0):
        wb = _orig_load_workbook(str(target))               # FRESH snapshot under lock
        try:
            mutator(wb)                                      # apply ALL pending sheets
            _orig_workbook_save(wb, str(tmp))
            with open(tmp, "rb+") as fh:
                os.fsync(fh.fileno())                        # durability barrier
            for attempt in range(replace_retries):           # lock held, but bounded & short
                try:
                    _orig_os_replace(str(tmp), str(target))
                    return True
                except PermissionError:
                    time.sleep(min(2.0, 0.25 * (attempt + 1)))
            raise RuntimeError(f"workbook commit blocked by external handle: {target}")
        finally:
            wb.close()
            try: tmp.unlink()
            except FileNotFoundError: pass

Module side becomes: records = harvest() (no lock, parallel) → pending/<sheet>.json payload or in-process queue → committer folds. The LS family's dump_ls_ratio_to_excel reduces to a mutator that recreates its sheet from records on the fresh workbook — same styling code, zero race.

9. META-REVIEW

If all available related skills are used, does it improve the response? Yes, demonstrably: static code reading alone yields the mechanism (lost update), but only telemetry forensics (1,466 events) + workbook banner OOB audit + empirical openpyxl measurement yield the magnitude (764 s cycles, 21.08 s/module, 78–97% RAM, 1/32 equilibrium) — and only schedulability math proves the SLA unschedulable rather than merely slow. Remaining upside not exhausted here: a live Windows reproduction rig (to confirm NTFS collision rates under a real Excel handle), a load-test against CoinGlass with 3 concurrent persistent tabs (Cloudflare tolerance curve), and a production-concurrency memory profile. Those are the next three experiments this desk should fund; each converts one remaining assumption in this report into a measurement.

Provenance notes: repo HEAD 9bea11df (mirror as_of 2026-10-25 15:54:31 UTC) postdates both the user-stated d57ef48d8 and the last envelope's c1285bd9 — the workspace moved forward again mid-audit; all empirical claims above are pinned to the mirror commit. The pending Cycle-20261025T101032Z envelope audit (superseder chain: 043004Z→065624Z→073815Z→082223Z→090553Z→093915Z→101032Z) remains queued for its own dispatch; the present code audit addresses the root cause of the excel_freshness_verified=false flag that has driven its HOLD cascade.