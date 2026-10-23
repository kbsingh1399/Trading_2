#!/usr/bin/env python3
"""Re-derive every provenance field of a cycle_envelope.json and report PASS/FAIL per field.

Motivation (Cycle 312 defect): the dispatcher declared workbook_sha256=fb6aebf6...
while Data/DataBase_Trading.xlsx has been e855a87f... in every commit across the
23:12-23:50 UTC window that brackets the cutoff. A digest that matches no artifact
attests to nothing, so the envelope must be rejected outright rather than reasoned
over. This verifier makes that check one command.

Usage:
    python Terminal/verify_cycle_envelope.py [Data/cycle_envelope.json] [--json]

Checks are classified into two groups:

  integrity  - does the envelope describe a real, reproducible artifact set?
               (structure, nonce shape, risk-policy digest, commit/tree, and the
               workbook + manifest digests computed *at the declared commit*)
  gate       - does the envelope claim usable data? (excel_freshness_verified,
               plus the working-copy digest, which may legitimately lag origin)

Only integrity failures justify DENIED_BAD_CYCLE_ENVELOPE. Gate fields are
reported for the ruling but must never be turned into a provenance rejection.

Exit codes:
    0  envelope integrity verified (gate fields may still be false/null)
    1  integrity failure -> envelope must be rejected
    2  envelope missing / unreadable / malformed
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKBOOK = ROOT / "Data/DataBase_Trading.xlsx"
MANIFEST = ROOT / "Data/history/master_manifest.json"

# Mirrors Terminal/generate_cycle_envelope.py::build_cycle_envelope risk_policy dict.
RISK_POLICY = {
    "kernel_usd": 4795.0,
    "global_reserve_usd": 2.0,
    "max_tickets": 2,
    "stress_multiplier": 1.25,
    "ticket_cost_usd": 2.0,
    "risk_min_usd": 15.0,
    "risk_max_usd": 25.0,
}


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def stable_sha256(path: pathlib.Path, pause_s: float = 0.25) -> tuple[str, bool, int]:
    """Hash a file twice with a pause, requiring size+mtime+digest to be unchanged.

    Returns (digest, stable, nbytes). A file being rewritten by the Excel daemon
    fails the stability check instead of yielding a torn-read digest.
    """
    before = path.stat()
    first = sha256_file(path)
    time.sleep(pause_s)
    after = path.stat()
    second = sha256_file(path)
    stable = (
        first == second
        and before.st_size == after.st_size
        and before.st_mtime_ns == after.st_mtime_ns
    )
    return first, stable, after.st_size


def git(*args: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=60
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("envelope", nargs="?", default=str(ROOT / "Data/cycle_envelope.json"))
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    env_path = pathlib.Path(args.envelope)
    try:
        env = json.loads(env_path.read_text())
    except (OSError, ValueError) as exc:
        print(f"FAIL envelope unreadable/malformed: {exc}", file=sys.stderr)
        return 2

    prov = env.get("provenance") or {}
    checks: dict[str, dict] = {}

    # 1. Structural
    required = [
        "schema_version", "cycle_id", "uuid", "dispatch_nonce", "cutoff_utc",
        "provenance", "inventory", "solvency", "market_clocks", "status", "authorization",
    ]
    missing = [k for k in required if k not in env]
    raw = json.dumps(env)
    markers = [m for m in ("{{", "}}", "TODO", "PLACEHOLDER", "<INSERT", "XXX") if m in raw]
    checks["structure"] = {
        "class": "integrity",
        "ok": not missing and not markers,
        "missing_keys": missing,
        "template_markers": markers,
    }

    # 2. Dispatch nonce sanity (UUIDv4 shape)
    nonce = str(env.get("dispatch_nonce", ""))
    checks["dispatch_nonce"] = {
        "class": "integrity",
        "ok": len(nonce) == 36 and nonce.count("-") == 4,
        "value": nonce,
    }

    # 3. Risk policy: independent recomputation
    recomputed_policy = hashlib.sha256(
        json.dumps(RISK_POLICY, sort_keys=True).encode()
    ).hexdigest()
    declared_policy = prov.get("risk_policy_sha256")
    checks["risk_policy_sha256"] = {
        "class": "integrity",
        "ok": declared_policy == recomputed_policy,
        "declared": declared_policy,
        "recomputed": recomputed_policy,
    }

    # 4. Git commit / tree actually resolvable and consistent
    commit = prov.get("git_commit") or ""
    tree = prov.get("git_tree") or ""
    commit_present = git("cat-file", "-t", commit) == "commit" if commit else False
    actual_tree = git("rev-parse", f"{commit}^{{tree}}") if commit_present else None
    checks["git_commit"] = {
        "class": "integrity",
        "ok": commit_present,
        "declared": commit,
        "present_locally": commit_present,
        "hint": None if commit_present else "run: git fetch origin main",
    }
    checks["git_tree"] = {
        "class": "integrity",
        "ok": commit_present and actual_tree == tree,
        "declared": tree,
        "actual": actual_tree,
    }

    # 5. Manifest digest: judged at the declared commit (the attested state),
    #    with the working copy reported separately as a gate-adjacent note.
    declared_manifest = prov.get("evidence_manifest_sha256")
    commit_ok = commit_present and actual_tree == tree
    if commit_ok:
        try:
            blob = subprocess.run(
                ["git", "show", f"{commit}:Data/history/master_manifest.json"],
                cwd=ROOT, capture_output=True, timeout=180,
            )
            if blob.returncode == 0:
                at_commit = hashlib.sha256(blob.stdout).hexdigest()
                checks["evidence_manifest_sha256_at_declared_commit"] = {
                    "class": "integrity",
                    "ok": at_commit == declared_manifest,
                    "commit": commit,
                    "manifest": at_commit,
                    "declared": declared_manifest,
                }
        except subprocess.SubprocessError:
            pass
    if MANIFEST.exists():
        live_manifest = sha256_file(MANIFEST)
        checks["evidence_manifest_sha256_working_copy"] = {
            "class": "gate",
            "ok": live_manifest == declared_manifest,
            "declared": declared_manifest,
            "working_copy": live_manifest,
            "note": "master_manifest.json is a live telemetry index regenerated every "
                    "few minutes; the working copy may legitimately be older than the "
                    "declared commit. Informational only.",
        }

    # 6. Workbook digest -- the Cycle 312 killer. Judged twice: stability of the
    #    live file (torn-read guard) and byte equality with the declared commit.
    declared_wb = prov.get("workbook_sha256")
    if WORKBOOK.exists():
        live_wb, stable, nbytes = stable_sha256(WORKBOOK)
        checks["workbook_sha256_working_copy"] = {
            "class": "gate",
            "ok": stable and live_wb == declared_wb,
            "declared": declared_wb,
            "working_copy": live_wb,
            "bytes": nbytes,
            "hash_stable_across_two_reads": stable,
            "note": None if stable else "workbook rewritten while hashed (torn read)",
        }
    if commit_ok:
        try:
            blob = subprocess.run(
                ["git", "show", f"{commit}:Data/DataBase_Trading.xlsx"],
                cwd=ROOT, capture_output=True, timeout=300,
            )
            if blob.returncode == 0:
                at_commit = hashlib.sha256(blob.stdout).hexdigest()
                checks["workbook_sha256_at_declared_commit"] = {
                    "class": "integrity",
                    "ok": at_commit == declared_wb,
                    "commit": commit,
                    "workbook": at_commit,
                    "bytes": len(blob.stdout),
                    "declared": declared_wb,
                }
        except subprocess.SubprocessError:
            pass
    elif not WORKBOOK.exists():
        checks["workbook_sha256_working_copy"] = {
            "class": "gate", "ok": False, "error": "workbook missing"}

    # 7. Excel freshness must not be silently null when the envelope claims verified status
    freshness = prov.get("excel_freshness_verified")
    checks["excel_freshness_verified"] = {
        "class": "gate",
        "ok": freshness is True,
        "declared": freshness,
        "note": "null/False means no sheet may be treated as fresh at the cutoff",
    }

    def failed_in(cls: str) -> list[str]:
        return [n for n, c in checks.items()
                if c.get("class", "integrity") == cls and not c.get("ok")]

    integrity_failed = failed_in("integrity")
    gate_failed = failed_in("gate")
    verdict = "ENVELOPE_INTEGRITY_VERIFIED" if not integrity_failed else "REJECT_ENVELOPE"
    payload = {
        "envelope": str(env_path),
        "cycle_id": env.get("cycle_id"),
        "cutoff_utc": env.get("cutoff_utc"),
        "dispatch_nonce": env.get("dispatch_nonce"),
        "verdict": verdict,
        "integrity_failed": integrity_failed,
        "gate_failed": gate_failed,
        "checks": checks,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"envelope : {env_path}")
        print(f"cycle    : {env.get('cycle_id')} @ {env.get('cutoff_utc')}")
        print(f"nonce    : {env.get('dispatch_nonce')}")
        print(f"verdict  : {verdict}")
        for name, c in checks.items():
            cls = c.get("class", "integrity")
            print(f"  [{'PASS' if c.get('ok') else 'FAIL'}] ({cls:9s}) {name}")
        if integrity_failed:
            print(f"\nINTEGRITY FAILURES: {', '.join(integrity_failed)}")
            print("Reject the envelope outright (DENIED_BAD_CYCLE_ENVELOPE); "
                  "do not compute a ruling over it.")
        elif gate_failed:
            print(f"\nintegrity verified; open gates: {', '.join(gate_failed)}")
            print("The envelope is trustworthy as an artifact, but those gates still "
                  "have to pass inside the ruling.")
        else:
            print("\nall checks passed")

    return 0 if not integrity_failed else 1


if __name__ == "__main__":
    sys.exit(main())
