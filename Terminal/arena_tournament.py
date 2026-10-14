#!/usr/bin/env python3
"""arena_tournament.py: repo-native arbitration of competing trade hypotheses.

WHY THIS EXISTS
---------------
The operational arena workflow (`.agent/skills/arena/SKILL.md` + `rubric.md`)
was run by hand once per council cycle: competing hypotheses were argued in a
chat, scored against the written rubric, and the ruling was executed. That
worked but it was not reproducible and it was not available to the repo. This
module makes the same methodology a first-class, deterministic repo feature:

  1. every competing hypothesis (stage / modify / hold / delete / stand aside)
     is a machine-readable card,
  2. every card is attacked by the five council personas against the live
     snapshot,
  3. the attacks are scored with the arena rubric weights
     (correctness 30 / completeness 25 / specificity 15 / robustness 20 /
     clarity 10), the fatal rule is applied, and a single-elimination bracket
     decides the winner,
  4. the whole trace (input hash, per-card findings, per-match scores, bracket,
     winner) is written to a persistent artifact directory so an operator can
     re-run it and get the identical answer.

OPERATOR DIRECTIVES ENCODED HERE
--------------------------------
* Purchase-side sweep clusters are the primary hazard. For a SHORT the
  dangerous sweep pool is the BUY-stop cluster (purchase-side stops) above the
  entry, plus overhead short-squeeze fuel. For a LONG it is the SELL-stop
  cluster below. Findings raised on that side carry the `purchase_side` flag
  and are weighted hardest by the red-team persona.
* No stop loss may sit inside a sweep cluster: the SL must clear the OUTER edge
  of the contiguous hazard union by `SL_BUFFER_ATR_MIN` (0.35) to
  `SL_BUFFER_ATR_MAX` (0.50) ATR.
* Macro blackout enforcement is permanently disabled by operator mandate; this
  engine never vetoes on calendar events.
* Deleting / holding / modifying a resting limit is decided on the same hard
  gates as staging a new one, so a stale limit cannot survive on optimism.

NOT a money-maker: this is a falsification harness. It says "this card is
contradicted by the snapshot" or "no fatal flaw found". It never proves profit.

USAGE
-----
    python Terminal/arena_tournament.py --cards docs/trade_plans/arena_cards/cycle106_20261014.json
    python Terminal/arena_tournament.py --cards ... --out docs/trade_plans/arena_runs --seed 106
    python Terminal/arena_tournament.py --cards ... --print          # stdout summary only

Artifacts (default `docs/trade_plans/arena_runs/<run_id>/`): run.json (full
trace) and REPORT.md (human-readable bracket + rulings). A symlink-free
`LATEST` text file records the newest run id.

Python 3.9+, standard library only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

# --------------------------------------------------------------------------
# Desk invariants (single source of truth; edit here, nowhere else)
# --------------------------------------------------------------------------
HARD_FLOOR_USD = 4775.00
OPERATING_BUFFER_USD = 4795.00
RISK_MIN_USD = 7.50
RISK_MAX_USD = 14.50
STRESS_MULTIPLIER = 1.25
STRESS_PER_TICKET_USD = 2.00

ENTRY_PROXIMITY_ATR_MAX = 2.00       # playbook section 3.A.3
SL_BUFFER_ATR_MIN = 0.35             # archetype-1 invariant
SL_BUFFER_ATR_MAX = 0.50             # gate R-1
FRICTION_MAX = 0.15                  # playbook section 7.4
FRICTION_MAX_ETH = 0.15              # same rule; ETH is charged the live spread
SPREAD_ATR_MAX = 0.18                # playbook section 5.1
SPREAD_BPS_MAX = {"CRYPTO": 35.0, "TRADFI": 5.0}
RR_MIN = 2.00
# Playbook 7.4 graduates the two friction-heaviest admitted instruments to a higher
# target: ETHUSD.pi (Grade B, spread ~12 bps) requires >= 2.2R and SOLUSD.p (Grade B-,
# spread ~21 bps) requires >= 2.5R. Every other asset keeps the flat 2.0R desk floor.
RR_MIN_BY_ASSET: Dict[str, float] = {"ETHUSD.pi": 2.20, "SOLUSD.p": 2.50}
MAGNET_MATERIAL_USD = 500_000.0      # playbook section 5.6 "real notional"
FRONT_RUN_BPS_LOW = 5.0
FRONT_RUN_BPS_HIGH = 10.0
TARGET_HORIZON_ATR = 3.50            # magnet must exist within 3.5 ATR of mid (reachable payoff doctrine)

# Gate R-2 asset-class whale/bunker thresholds (playbook section 7.4)
WALL_THRESHOLD_USD = {
    "CRYPTO_MAJOR": 5_000_000.0,
    "CRYPTO_ALT": 5_000_000.0,
    "INDEX": 1_000_000.0,
    "COMMODITY": 750_000.0,
    "FX": 500_000.0,
}
CRYPTO_MAJOR = {"BTCUSD.pi", "ETHUSD.pi"}
COMMODITY_SYMBOLS = {"XAUUSD.pi", "XAGUSD.pi", "USWTI.p"}
INDEX_SYMBOLS = {"SP500.p", "NAS100.p", "DJ30.p", "GER40.p"}
FX_SYMBOLS = {"EURUSD.pi", "GBPUSD.pi", "USDJPY.pi"}

# Loss-archetype registry: every finding cites the trap it defends against.
ARCHETYPES = {
    "A1": "SL inside sweep band / insufficient structural buffer",
    "A2": "Counter-trend entry against HTF regime or unabsorbed opposing CVD",
    "A3": "Insufficient structural buffer (sub-0.35 ATR clearance)",
    "A4": "Ephemeral wall defense (unverified persistence / relocated wall)",
    "A5": "Retracement overshoot and premature stop-out (Gate R-1/R-2/R-3/R-4)",
    "A6": "Unpayable geometry (no reachable front-runnable liquidity magnet)",
    "A7": "Friction drag (broker spread consumes the risk budget)",
    "A8": "Stop-on-stop / entry parked inside un-swept opposing stop fuel",
    "A9": "Macro-invalidated thesis (RETIRED: blackout enforcement disabled)",
}

SEVERITY_ORDER = {"FATAL": 3, "MAJOR": 2, "MINOR": 1, "INFO": 0}


# --------------------------------------------------------------------------
# Snapshot plumbing
# --------------------------------------------------------------------------
def load_snapshot(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def load_evidence_ledgers(paths: Sequence[str]) -> List[Dict[str, Any]]:
    """Earlier council evidence ledgers. Used ONLY to re-establish L3 wall
    continuity when the current generation's persistence sampler has rolled
    over (the documented Cycle-105/106 discontinuity: every wall in a fresh
    generation is re-labelled SINGLE_SAMPLE with first_seen == generation start)."""
    out = []
    for p in paths:
        if not p or not os.path.exists(p):
            continue
        try:
            with open(p, "r", encoding="utf-8") as fh:
                out.append(json.load(fh))
        except (OSError, json.JSONDecodeError):
            continue
    return out


def _ledger_walls(ledger: Dict[str, Any], asset_key: str) -> List[Dict[str, Any]]:
    node = (ledger.get("assets") or {}).get(asset_key) or {}
    blocks = node.get("source_blocks") or node
    ob = (blocks or {}).get("orderbook_live_depth") or {}
    return ob.get("whale_walls_l3") or []


def wall_continuity(table: Dict[Tuple[str, str], Dict[str, Any]],
                    asset_key: str, address: str) -> Optional[Dict[str, Any]]:
    return table.get((asset_key, (address or "").lower()))


def build_continuity_table(ledgers: Sequence[Dict[str, Any]],
                           now_epoch: float) -> Dict[Tuple[str, str], Dict[str, Any]]:
    """(asset, address) -> best previously observed wall: max persist_s seen,
    largest notional seen, and the age of the observation relative to now."""
    table: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for led in ledgers:
        for asset_key in ((led.get("assets") or {}).keys()):
            for w in _ledger_walls(led, asset_key):
                addr = (w.get("address") or "").lower()
                if not addr:
                    continue
                key = (asset_key, addr)
                rec = table.get(key)
                observed = w.get("observed_at") or 0.0
                notional = float(w.get("notional_usd") or 0.0)
                persist = float(w.get("persist_s") or 0.0)
                if rec is None:
                    rec = {"max_persist_s": persist, "max_notional_usd": notional,
                           "observed_at": observed, "side": w.get("side"),
                           "prices": set()}
                    table[key] = rec
                rec["max_persist_s"] = max(rec["max_persist_s"], persist)
                rec["max_notional_usd"] = max(rec["max_notional_usd"], notional)
                rec["observed_at"] = min(rec["observed_at"] or observed, observed) if rec["observed_at"] else observed
                try:
                    rec["prices"].add(float(w.get("price")))
                except (TypeError, ValueError):
                    pass
    for rec in table.values():
        rec["age_s"] = max(0.0, now_epoch - (rec.get("observed_at") or now_epoch))
    return table


# --------------------------------------------------------------------------
# Card + evaluation model
# --------------------------------------------------------------------------
# STAGE cards carry their own levels. HOLD / DELETE / MODIFY cards carry the
# levels of the card they act upon in `meta.evaluates`, so they are audited by
# building an internal STAGE probe from those levels: a resting limit is judged
# by exactly the same hard gates as a fresh one.
TRADE_ACTIONS = {"STAGE", "STAGE_BATCH"}
PASSIVE_ACTIONS = {"HOLD", "DELETE", "MODIFY", "WATCH", "STAND_ASIDE"}


@dataclass
class Card:
    id: str
    action: str
    thesis: str = ""
    asset: str = ""
    side: str = ""
    entry: Optional[float] = None
    sl: Optional[float] = None
    tp: Optional[float] = None
    lots: Optional[float] = None
    engine: Optional[int] = None
    target_ticket: Optional[int] = None
    batch_count: int = 1
    meta: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_json(cls, d: Dict[str, Any]) -> "Card":
        known = {f for f in cls.__dataclass_fields__}
        payload = {k: v for k, v in d.items() if k in known}
        payload.setdefault("meta", {})
        return cls(**payload)


@dataclass
class Finding:
    code: str
    severity: str
    archetype: str
    message: str
    values: Dict[str, Any] = field(default_factory=dict)
    purchase_side: bool = False

    def as_dict(self) -> Dict[str, Any]:
        return {"code": self.code, "severity": self.severity, "archetype": self.archetype,
                "message": self.message, "values": self.values, "purchase_side": self.purchase_side}


def _asset_class(symbol: str) -> str:
    if symbol in CRYPTO_MAJOR:
        return "CRYPTO_MAJOR"
    if symbol in INDEX_SYMBOLS:
        return "INDEX"
    if symbol in COMMODITY_SYMBOLS:
        return "COMMODITY"
    if symbol in FX_SYMBOLS:
        return "FX"
    return "CRYPTO_ALT"


def _usd_factor(symbol: str, mid: Optional[float]) -> float:
    """Convert quote-currency P&L into account currency (USD).

    Everything on this book is USD-quoted except the JPY crosses: for `USDJPY.pi` a
    one-point move on 100,000 units is 100,000 **JPY**, not 100,000 USD. Without the
    conversion the engine overstates the risk of a JPY ticket by the FX rate itself
    (~158x live) and fabricates FLOOR_BREACH verdicts. R-multiples are unaffected
    (risk and reward scale together); USD risk, stress and floor math are not.
    """
    core = symbol.upper().split(".")[0]                        # drop the broker suffix (.pi / .p)
    core = "".join(ch for ch in core if ch.isalpha())          # keep the letters only (SP500 -> SP)
    if mid and core.endswith("JPY"):
        return 1.0 / float(mid)
    return 1.0


def _bins(raw: Optional[List[Dict[str, Any]]]) -> List[Tuple[float, float, float]]:
    out = []
    for c in raw or []:
        if not isinstance(c, dict):
            continue
        try:
            lo = float(c["min_price"]); hi = float(c["max_price"])
        except (KeyError, TypeError, ValueError):
            continue
        out.append((min(lo, hi), max(lo, hi), float(c.get("notional_usd") or 0.0)))
    return sorted(out)


def _dedupe(bins: Sequence[Tuple[float, float, float]]) -> List[Tuple[float, float, float]]:
    """Collapse duplicate interval references (the same bin appears in both the
    `nearest_*` and `top_*` lists) without double-counting notional."""
    best: Dict[Tuple[float, float], float] = {}
    for lo, hi, n in bins:
        key = (lo, hi)
        best[key] = max(best.get(key, 0.0), n)
    return sorted((lo, hi, n) for (lo, hi), n in best.items())


def _merge_sources(*groups: Sequence[Tuple[float, float, float]]) -> List[Tuple[float, float, float]]:
    """Sum genuinely different fuel sources (stop clusters + liquidation bands)
    that share an interval; dedupe inside each source first."""
    merged: Dict[Tuple[float, float], float] = {}
    for g in groups:
        for lo, hi, n in _dedupe(g):
            merged[(lo, hi)] = merged.get((lo, hi), 0.0) + n
    return sorted((lo, hi, n) for (lo, hi), n in merged.items())


def _dedupe(bins: Sequence[Tuple[float, float, float]]) -> List[Tuple[float, float, float]]:
    """Collapse duplicate list references (the same interval can appear in both the
    `nearest_*` and `top_*` lists). Keeping the max preserves the source's notional
    instead of double counting it."""
    best: Dict[Tuple[float, float], float] = {}
    for lo, hi, notional in bins:
        key = (lo, hi)
        best[key] = max(best.get(key, 0.0), notional)
    return sorted((lo, hi, n) for (lo, hi), n in best.items())


def hazard_union(bins: Sequence[Tuple[float, float, float]], price: float
                 ) -> Tuple[Optional[float], Optional[float], List[Tuple[float, float, float]]]:
    """The contiguous belt that contains `price`. The desk measures stop clearance from the
    OUTER edge of the belt, not from the bin that happens to contain the stop (Cycle 43B/44,
    Cycle 93). Returns (None, None, []) when the price sits in a book gap."""
    for lo, hi, members in _runs(bins):
        if lo <= price <= hi:
            return lo, hi, members
    return None, None, []


def _runs(bins: Sequence[Tuple[float, float, float]]) -> List[Tuple[float, float, List[Tuple[float, float, float]]]]:
    """Group touching bins into contiguous runs ("belts"). A belt is the sweep ladder
    the desk reasons about: it ends where the book has a gap."""
    runs: List[Tuple[float, float, List[Tuple[float, float, float]]]] = []
    for lo, hi, n in sorted(bins):
        if runs and lo <= runs[-1][1] + 1e-6:
            r_lo, r_hi, mem = runs[-1]
            runs[-1] = (r_lo, max(r_hi, hi), mem + [(lo, hi, n)])
        else:
            runs.append((lo, hi, [(lo, hi, n)]))
    return runs


def _front_run(edge: float, direction: str, bps: float = 7.5) -> float:
    """Front-run a magnet edge by `bps` so the exit fills before the pool is hit."""
    if direction == "SHORT":
        return edge * (1.0 + bps / 10_000.0)
    return edge * (1.0 - bps / 10_000.0)


class CardEvaluation:
    def __init__(self, card: Card, asset: Dict[str, Any], snap: Dict[str, Any],
                 continuity: Dict[Tuple[str, str], Dict[str, Any]]):
        self.card = card
        self.asset = asset
        self.snap = snap
        self.continuity = continuity
        self.findings: List[Finding] = []
        self.metrics: Dict[str, Any] = {}
        self.qualified = False
        self.action_contradicted = False

    # -- helpers -----------------------------------------------------------
    def add(self, code: str, sev: str, arch: str, msg: str, purchase_side: bool = False, **values: Any) -> None:
        self.findings.append(Finding(code, sev, arch, msg, values, purchase_side))

    def worst(self) -> int:
        return max((SEVERITY_ORDER[f.severity] for f in self.findings), default=-1)

    def count(self, sev: str) -> int:
        return sum(1 for f in self.findings if f.severity == sev)

    def fatal(self) -> bool:
        return self.count("FATAL") > 0


def _evaluate_portfolio(ev: CardEvaluation, card: Card, snap: Dict[str, Any],
                        continuity: Dict[Tuple[str, str], Dict[str, Any]]) -> CardEvaluation:
    """Portfolio-level cards carry no single asset: STAND_ASIDE proves itself by running
    every card in its universe through the same gates, WATCH documents an armed trigger."""
    if card.action == "STAND_ASIDE":
        qualified = []
        for c in card.meta.get("universe") or []:
            sub = evaluate_card(Card.from_json(c), snap, continuity)
            ev.metrics.setdefault("universe_probe", []).append({
                "id": c.get("id"), "fatal": sub.fatal(), "qualified": sub.qualified,
                "fatal_codes": [f.code for f in sub.findings if f.severity == "FATAL"],
                "major_codes": [f.code for f in sub.findings if f.severity == "MAJOR"],
                "best_reachable_rr": sub.metrics.get("best_reachable_rr"),
            })
            if sub.qualified:
                qualified.append(c.get("id"))
        ev.metrics["qualified_candidates"] = qualified
        if qualified:
            ev.add("STAND_ASIDE_CONTRADICTED", "FATAL", "A6",
                   f"stand aside contradicts {len(qualified)} fully qualified card(s): {qualified}")
            ev.action_contradicted = True
        else:
            ev.add("STAND_ASIDE_JUSTIFIED", "INFO", "A6",
                   f"every one of the {len(card.meta.get('universe') or [])} candidate cards in the "
                   "universe carries at least one fatal gate failure")
    elif card.action == "WATCH":
        ev.metrics["untriggered"] = True
        trig = card.meta.get("condition")
        if trig:
            ev.add("CONDITIONAL_UNTRIGGERED", "INFO", "A5",
                   f"armed trigger has not fired in this generation: {trig}", condition=trig)
            ev.metrics["armed_trigger"] = trig
            ev.metrics["invalidation"] = card.meta.get("invalidation")
        else:
            ev.add("NOT_EVALUATED", "MINOR", "A6",
                   "card carries no geometry, no evaluated target and no armed trigger")
    else:
        ev.add("NOT_EVALUATED", "MINOR", "A6",
               f"portfolio action {card.action!r} has no evaluator")
    return ev


def evaluate_card(card: Card, snap: Dict[str, Any],
                  continuity: Dict[Tuple[str, str], Dict[str, Any]]) -> CardEvaluation:
    asset = (snap.get("assets_matrix_24") or {}).get(card.asset) or {}
    ev = CardEvaluation(card, asset, snap, continuity)
    if not asset and card.asset:
        ev.metrics["asset_present"] = False
        ev.add("ASSET_MISSING", "MAJOR", "A6", f"asset {card.asset!r} is not in assets_matrix_24")
        return ev
    if not asset:
        # portfolio-level card (STAND_ASIDE / WATCH): the universe probes carry the assets
        ev.metrics["asset_present"] = None
        ev.metrics["card_class"] = "PORTFOLIO"
        return _evaluate_portfolio(ev, card, snap, continuity)

    q = asset.get("quotes") or {}
    es = asset.get("execution_specs") or {}
    ci = asset.get("causal_indicators") or {}
    sc = asset.get("structural_stop_clusters") or {}
    rl = asset.get("reconstructed_liquidations") or {}
    ob = asset.get("orderbook_live_depth") or {}
    mh = asset.get("multi_horizon_cvd") or {}
    tf = asset.get("tradfi_orderflow") or {}

    symbol = asset.get("symbol_broker", card.asset)
    cls = _asset_class(symbol)
    mid = float(q.get("mid") or 0.0)
    atr = ci.get("atr_14")
    regime = ci.get("trend_regime")
    spread_price = float(q.get("spread_price") or 0.0)
    spread_bps = float(q.get("spread_bps") or 0.0)
    contract = float(es.get("contract_size") or 1.0)
    min_lot = float(es.get("min_lot") or 0.01)
    usd_factor = _usd_factor(symbol, mid)

    ev.metrics.update({
        "symbol": symbol, "asset_class": cls, "mid": mid, "atr_14": atr,
        "regime": regime, "spread_price": spread_price, "spread_bps": spread_bps,
        "contract_size": contract, "min_lot": min_lot,
        "quote_freshness": q.get("quote_freshness"),
    })

    if regime in (None, "INSUFFICIENT_HISTORY", "UNDEFINED"):
        ev.add("REGIME_UNVERIFIED", "FATAL" if card.action in TRADE_ACTIONS else "INFO", "A2",
               f"trend_regime={regime!r}: neither engine can be certified on this snapshot",
               regime=regime)
    elif regime == "RANGE_BOUND":
        # Operator rule: in non-trending noise neither engine applies and the mathematically
        # correct action is stand aside. A discretionary card in range-bound conditions is a
        # forced trade, so it fails the gate; a posture card (WATCH / STAND_ASIDE) may record
        # the state.
        ev.add("REGIME_GATED_STAND_ASIDE", "FATAL" if card.action in TRADE_ACTIONS else "INFO", "A2",
               "trend_regime=RANGE_BOUND: neither engine applies in non-trending noise", regime=regime)
    if atr in (None, 0):
        ev.add("ATR_UNAVAILABLE", "FATAL" if card.action in TRADE_ACTIONS else "INFO", "A3",
               "ATR(14) unavailable; stop distance, buffers and friction ratios are undefined")

    # ---- spread / friction ceilings ------------------------------------
    spread_cap = SPREAD_BPS_MAX["CRYPTO"] if cls.startswith("CRYPTO") else SPREAD_BPS_MAX["TRADFI"]
    ev.metrics["spread_cap_bps"] = spread_cap
    if spread_bps > spread_cap:
        ev.add("SPREAD_CEILING", "MAJOR", "A7",
               f"spread {spread_bps:.2f} bps exceeds the {spread_cap:.0f} bps {cls} ceiling",
               spread_bps=spread_bps, cap_bps=spread_cap)
    if atr:
        ratio = spread_price / float(atr)
        ev.metrics["spread_over_atr"] = ratio
        if ratio > SPREAD_ATR_MAX:
            ev.add("SPREAD_OVER_ATR", "MAJOR", "A7",
                   f"spread/ATR {ratio:.3f} exceeds {SPREAD_ATR_MAX}", ratio=ratio)
    min_lot_cash = spread_price * contract * min_lot * usd_factor
    ev.metrics["min_lot_spread_cash_usd"] = min_lot_cash
    if min_lot_cash > FRICTION_MAX * RISK_MAX_USD:
        ev.add("MIN_LOT_FRICTION", "MAJOR", "A7",
               f"spread cash at min lot ({min_lot} lot) is {min_lot_cash:.2f} USD, above "
               f"{FRICTION_MAX * RISK_MAX_USD:.3f} USD (15% of max risk)",
               min_lot_spread_cash_usd=min_lot_cash)

    # ---- trade cards ----------------------------------------------------
    # STAGE / STAGE_BATCH carry their own levels. HOLD / DELETE / MODIFY are audited
    # against an internal STAGE probe built from `meta.evaluates` (see the passive
    # branch below), so a resting order faces the identical gate set as a fresh one.
    target = card.meta.get("evaluates") or {}
    if card.action in TRADE_ACTIONS:
        ev.metrics["asset_present"] = True
        side = card.side or "SHORT"
        entry, sl, tp, lots = card.entry, card.sl, card.tp, card.lots
        if entry is None or sl is None or tp is None or lots is None:
            ev.add("CARD_INCOMPLETE", "FATAL", "A6", "trade card is missing entry/SL/TP/lots")
            ev.action_contradicted = True
            return ev

        stop_pts = abs(sl - entry)
        risk_usd = stop_pts * contract * lots * usd_factor
        reward_usd = abs(entry - tp) * contract * lots * usd_factor
        rr = (reward_usd / risk_usd) if risk_usd else 0.0
        ev.metrics.update({"side": side, "entry": entry, "sl": sl, "tp": tp, "lots": lots,
                           "stop_points": stop_pts, "risk_usd": risk_usd,
                           "reward_usd": reward_usd, "rr_gross": rr,
                           "usd_factor": usd_factor})
        rr_min = RR_MIN_BY_ASSET.get(symbol, RR_MIN)
        ev.metrics["rr_min_required"] = rr_min

        # entry proximity to mid (playbook 3.A.3)
        if atr:
            prox = abs(entry - mid) / float(atr)
            ev.metrics["entry_distance_atr"] = prox
            if prox > ENTRY_PROXIMITY_ATR_MAX:
                ev.add("ENTRY_TOO_FAR", "FATAL", "A5",
                       f"entry is {prox:.2f} ATR from mid (>{ENTRY_PROXIMITY_ATR_MAX} ATR bound)",
                       entry_distance_atr=prox, limit=ENTRY_PROXIMITY_ATR_MAX)
            if side == "SHORT" and entry <= q.get("ask", entry):
                ev.add("NOT_PASSIVE", "MAJOR", "A5",
                       "sell limit is not resting strictly above the ask (passive-only mandate)",
                       ask=q.get("ask"), entry=entry)

        # friction on the traded stop distance
        if stop_pts > 0:
            friction = spread_price / stop_pts
            ev.metrics["friction_pct"] = friction * 100.0
            if friction > FRICTION_MAX:
                ev.add("FRICTION_BUDGET", "FATAL", "A7",
                       f"spread {spread_price} / stop distance {stop_pts:.3f} = {friction*100:.2f}% "
                       f"of risk, above the 15% dynamic friction ceiling", friction_pct=friction * 100.0)
            if not (RISK_MIN_USD <= risk_usd <= RISK_MAX_USD) and not card.meta.get("allow_out_of_envelope"):
                ev.add("RISK_ENVELOPE", "MAJOR", "A5",
                       f"nominal risk {risk_usd:.2f} USD outside [{RISK_MIN_USD}, {RISK_MAX_USD}]",
                       risk_usd=risk_usd)

        # ---- hazard geometry -------------------------------------------------
        # A SHORT's hazard is the purchase-side (BUY) stop cluster above plus the
        # short-squeeze fuel above it; its reward magnets are the SELL-stop clusters and
        # long cascades below. A LONG is the exact mirror image. Getting this orientation
        # wrong is what makes a "defended" stop land inside the sweep that hunts it.
        buy_above = _merge_sources(_bins(sc.get("nearest_buy_stop_clusters_above")),
                                   _bins(sc.get("top_buy_stop_clusters_above")))
        squeeze_above = _dedupe(_bins(rl.get("nearest_short_squeeze_bands_above")) +
                                _bins(rl.get("top_short_squeeze_bands_above")))
        sell_below = _merge_sources(_bins(sc.get("nearest_sell_stop_clusters_below")),
                                    _bins(sc.get("top_sell_stop_clusters_below")))
        cascade_below = _dedupe(_bins(rl.get("nearest_long_cascade_bands_below")) +
                                _bins(rl.get("top_long_cascade_bands_below")))

        if side == "SHORT":
            hazard = _dedupe(buy_above + squeeze_above)
            entry_fuel = buy_above
            magnets = _merge_sources(sell_below, cascade_below)
            magnets.sort(key=lambda b: -b[1])
        else:
            hazard = _dedupe(sell_below + cascade_below)
            entry_fuel = sell_below
            magnets = _merge_sources(buy_above, squeeze_above)
            magnets.sort(key=lambda b: b[0])
        magnets = [(lo, hi, n) for lo, hi, n in magnets if n >= MAGNET_MATERIAL_USD]

        runs = _runs(hazard)
        ev.metrics["hazard_runs"] = [[lo, hi, round(sum(m[2] for m in mem), 2)] for lo, hi, mem in runs][:10]

        def _containing(price: float):
            for r_lo, r_hi, mem in runs:
                if r_lo <= price <= r_hi:
                    return r_lo, r_hi, mem
            return None, None, []

        # Belt adjacent to the entry: the contiguous ladder any compliant stop must clear.
        ent_lo, ent_hi, _ent_mem = _containing(entry) if side == "SHORT" else _containing(entry)
        ev.metrics["entry_run"] = [ent_lo, ent_hi]

        # 1) the stop may not sit inside any belt
        u_lo, u_hi, members = _containing(sl)
        ev.metrics["hazard_union"] = [u_lo, u_hi]
        ev.metrics["hazard_union_usd"] = sum(m[2] for m in members)
        ev.metrics["hazard_union_members"] = [[m[0], m[1], m[2]] for m in members]
        if u_lo is not None:
            ev.add("SL_INSIDE_SWEEP", "FATAL", "A1",
                   f"SL {sl} sits INSIDE the {'purchase-side' if side == 'SHORT' else 'sale-side'} "
                   f"sweep belt [{u_lo}, {u_hi}] carrying {sum(m[2] for m in members)/1e6:.3f}M USD",
                   purchase_side=(side == "SHORT"), union=[u_lo, u_hi],
                   union_usd=sum(m[2] for m in members))
            ev.metrics["sl_clearance_atr"] = (-abs(min(sl - u_lo, u_hi - sl)) / float(atr)) if atr else None
        elif atr:
            # 2) outside every belt: clearance is measured from the nearest belt edge the
            #    stop has to survive, not from an arbitrary bin.
            if side == "SHORT":
                below = [r for r in runs if r[1] < sl]
                gov = max(below, key=lambda r: r[1]) if below else None
                edge = gov[1] if gov else None
            else:
                above = [r for r in runs if r[0] > sl]
                gov = min(above, key=lambda r: r[0]) if above else None
                edge = gov[0] if gov else None
            if edge is None:
                ev.add("SL_HAS_NO_HAZARD_REFERENCE", "INFO", "A3",
                       "no sweep belt on the stop's side of price: clearance is bounded by the "
                       "0.35 ATR minimum only")
                ev.metrics["sl_clearance_atr"] = None
            else:
                clearance = ((sl - edge) if side == "SHORT" else (edge - sl)) / float(atr)
                ev.metrics["sl_clearance_atr"] = clearance
                ev.metrics["sl_clearance_reference"] = edge
                if clearance < SL_BUFFER_ATR_MIN:
                    ev.add("SL_BUFFER_THIN", "FATAL", "A3",
                           f"SL clearance {clearance:.3f} ATR < {SL_BUFFER_ATR_MIN} ATR outside the belt edge "
                           f"{edge}", clearance_atr=clearance)
                elif clearance > SL_BUFFER_ATR_MAX * 1.6:
                    ev.add("SL_BUFFER_WIDE", "MINOR", "A5",
                           f"SL clearance {clearance:.3f} ATR is wide; the geometry must still pay >= {rr_min}R",
                           clearance_atr=clearance)

        # 3) entry parked inside un-swept opposing fuel (autopsy #18786372 mirrored)
        if ent_lo is not None and _ent_mem:
            notional = sum(m[2] for m in _ent_mem)
            if notional >= MAGNET_MATERIAL_USD:
                ev.add("ENTRY_IN_FUEL", "MAJOR", "A8",
                       f"entry {entry} sits inside un-swept "
                       f"{'purchase-side' if side == 'SHORT' else 'sale-side'} stop fuel "
                       f"[{ent_lo}, {ent_hi}] = {notional/1e6:.3f}M USD",
                       purchase_side=(side == "SHORT"), union=[ent_lo, ent_hi], union_usd=notional)
                ev.metrics["entry_fuel_usd"] = notional

        # ---- in-range whale bunker (gate R-2) with continuity rescue
        walls = ob.get("whale_walls_l3") or []
        threshold = WALL_THRESHOLD_USD[cls]
        in_range, best = [], None
        for w in walls:
            try:
                px = float(w.get("price")); notional = float(w.get("notional_usd") or 0.0)
            except (TypeError, ValueError):
                continue
            side_ok = (w.get("side") == ("SELL" if side == "SHORT" else "BUY"))
            if not side_ok:
                continue
            # Gate R-2: the wall must stand BETWEEN the entry and the stop. A wall beyond the
            # stop cannot absorb anything before the stop is touched, so it is not shelter.
            inside = (entry < px <= sl) if side == "SHORT" else (sl <= px < entry)
            if not inside:
                continue
            persist = float(w.get("persist_s") or 0.0)
            cont = wall_continuity(continuity, card.asset, w.get("address") or "")
            verified = persist >= 180.0 or bool(cont and cont.get("age_s", 0) >= 180.0)
            # Continuity is only a legitimate defense when the same wallet was seen at a
            # re-pegged but comparable price: within 2.0 ATR of the current quote. A wall
            # that moved further than that is a different defense, not a continuation.
            cont_price_ok = True
            if cont and atr:
                cont_price_ok = any(abs(px - prev) <= 2.0 * float(atr)
                                    for prev in cont.get("prices") or [])
            if cont and not cont_price_ok:
                verified = False
            rec = {"price": px, "notional_usd": notional, "persist_s": persist,
                   "address": w.get("address"), "continuity_age_s": (cont or {}).get("age_s"),
                   "continuity_max_persist_s": (cont or {}).get("max_persist_s"),
                   "continuity_price_ok": cont_price_ok,
                   "verified": verified, "wall_class": w.get("wall_class")}
            in_range.append(rec)
            if best is None or notional > best["notional_usd"]:
                best = rec
        defense = sum(w["notional_usd"] for w in in_range if w["verified"])
        ev.metrics["in_range_defense_usd"] = defense
        ev.metrics["in_range_walls"] = in_range[:8]
        ev.metrics["wall_threshold_usd"] = threshold
        if best is None:
            ev.add("NO_BUNKER_WALL", "MAJOR", "A4",
                   f"no {'ask' if side == 'SHORT' else 'bid'} whale wall at or inside the SL", purchase_side=(side == "SHORT"))
        else:
            if not any(w["verified"] for w in in_range):
                ev.add("PERSISTENCE_UNVERIFIED", "MAJOR", "A4",
                       "in-range wall exists but neither persist_s >= 180s nor cross-generation continuity could be verified",
                       purchase_side=(side == "SHORT"), best=best)
            if best["notional_usd"] < threshold:
                ev.add("BUNKER_WALL_THIN", "MAJOR", "A4",
                       f"largest in-range wall {best['notional_usd']/1e6:.3f}M < {threshold/1e6:.2f}M {cls} requirement",
                       purchase_side=(side == "SHORT"), best=best)

        # ---- forced-fuel overwhelm ratio (playbook 3.B)
        # Fuel is the hazard notional the stop must actually survive: the bins standing
        # between the entry and the stop. (A belt that contains the SL is already fatal on
        # its own; this keeps the ratio honest when the SL correctly sits outside it.)
        if side == "SHORT":
            fuel_bins = [b for b in hazard if b[1] > entry and b[0] <= sl]
        else:
            fuel_bins = [b for b in hazard if b[0] < entry and b[1] >= sl]
        fuel = sum(b[2] for b in fuel_bins)
        ev.metrics["corridor_fuel_usd"] = fuel
        ev.metrics["corridor_fuel_bins"] = [[b[0], b[1], b[2]] for b in fuel_bins]
        ev.metrics["overwhelm_ratio"] = (fuel / defense) if defense else None
        if defense and fuel / defense > 2.0:
            ev.add("OVERWHELM_RATIO", "FATAL", "A5",
                   f"forced fuel {fuel/1e6:.3f}M exceeds in-range verified defense {defense/1e6:.3f}M "
                   f"by {fuel/defense:.2f}:1 (> 2.0:1 cap)", purchase_side=(side == "SHORT"))

        # ---- take profit front-run + reachability
        if magnets:
            # Contiguous magnet bins are one ladder, not independent pools. Front-running the
            # near edge of an INTERIOR bin parks the TP inside the neighbouring bin of the same
            # ladder — a TP the engine's own TP_INSIDE_MAGNET gate then rejects, which used to
            # inflate `max_achievable_rr` on every asset whose stops/cascades are binned
            # adjacently. Merge the ladder first, then front-run its near edge.
            ladder = []
            for lo, hi, n in sorted(magnets):
                if ladder and lo <= ladder[-1][1] + 1e-9:
                    ladder[-1] = (ladder[-1][0], max(ladder[-1][1], hi), ladder[-1][2] + n)
                else:
                    ladder.append((lo, hi, n))
            if side == "SHORT":
                cand = [(lo, hi, n, _front_run(hi, "SHORT", FRONT_RUN_BPS_HIGH)) for lo, hi, n in ladder if hi < mid]
                cand.sort(key=lambda c: -c[3])
            else:
                cand = [(lo, hi, n, _front_run(lo, "LONG", FRONT_RUN_BPS_HIGH)) for lo, hi, n in ladder if lo > mid]
                cand.sort(key=lambda c: c[3])
            horizon = (float(atr) * TARGET_HORIZON_ATR) if atr else None
            # Fail closed: without an ATR there is no way to certify that a pool is reachable,
            # so nothing is treated as reachable.
            reachable = [c for c in cand if horizon is not None and abs(mid - c[3]) <= horizon]
            ev.metrics["magnets_considered"] = [[c[0], c[1], c[2], round(c[3], 4)] for c in cand[:6]]
            ev.metrics["magnets_reachable"] = [[c[0], c[1], c[2], round(c[3], 4), round(abs(entry - c[3]), 2)]
                                               for c in reachable[:6]]
            straddle = [(lo, hi, n) for lo, hi, n in ladder if lo <= mid <= hi]
            if straddle:
                s_lo, s_hi, s_n = max(straddle, key=lambda b: b[2])
                ev.add("PRICE_INSIDE_MAGNET_LADDER", "MINOR", "A6",
                       f"mid {mid} sits inside the "
                       f"{'sell-stop/long-cascade' if side == 'SHORT' else 'buy-stop/squeeze'} "
                       f"ladder [{s_lo}, {s_hi}] carrying {s_n/1e6:.3f}M USD: no front-runnable TP "
                       f"exists inside the ladder, the exit must clear its near edge",
                       ladder=[s_lo, s_hi], ladder_usd=s_n)
            if not reachable:
                ev.add("NO_REACHABLE_MAGNET", "FATAL", "A6",
                       f"no magnet within {TARGET_HORIZON_ATR} ATR of mid ({mid}) to front-run; "
                       f"nearest qualifying pool is {cand[0][0]}-{cand[0][1]} USD "
                       f"{abs(mid - cand[0][3])/float(atr):.2f} ATR from mid" if atr and cand else
                       f"no magnet within {TARGET_HORIZON_ATR} ATR of mid")
            else:
                best_r = max(abs(entry - c[3]) for c in reachable)
                best_rr = best_r / stop_pts if stop_pts else 0.0
                ev.metrics["best_reachable_rr"] = best_rr
                ev.metrics["best_reachable_reward_points"] = best_r
                ev.metrics["best_reachable_tp"] = max(reachable, key=lambda c: abs(entry - c[3]))[3]
                if best_rr < rr_min:
                    ev.add("UNPAYABLE_GEOMETRY", "FATAL", "A6",
                           f"best reachable front-runnable target yields {best_rr:.2f}R at this card's stop "
                           f"< required {rr_min}R", best_reachable_rr=best_rr)

                # Asset-level verdict: what can ANY card on this asset pay? Pair the best
                # reachable front-runnable target with the MINIMUM compliant stop, i.e. the
                # stop that clears the outermost purchase-side fuel edge by 0.35 ATR.
                if atr:
                    # Minimum compliant stop = clear the belt adjacent to the entry by 0.35 ATR.
                    # Anchor on the entry's own run; fall back to the nearest run beyond it when the
                    # entry itself sits in a gap.
                    anchor = ent_hi if side == "SHORT" else ent_lo
                    if anchor is None:
                        if side == "SHORT":
                            beyond = [r for r in runs if r[0] > entry]
                            anchor = min(beyond, key=lambda r: r[0])[1] if beyond else None
                        else:
                            beyond = [r for r in runs if r[1] < entry]
                            anchor = max(beyond, key=lambda r: r[1])[0] if beyond else None
                    if anchor is None:
                        anchor = entry
                    # Convergence: a stop derived from `anchor` must not land inside a FURTHER
                    # belt, nor inside the buffer band immediately in front of one. Clearing the
                    # first cluster by 0.35 ATR can park the stop inside a second cluster sitting
                    # just beyond it (live XAGUSD.pi case), which is the archetype-1 error wearing
                    # a compliant mask. Walk the anchor outward, bounded, until the derived stop
                    # sits in free space with a full buffer to the next cluster.
                    buf = SL_BUFFER_ATR_MIN * float(atr)
                    for _ in range(12):
                        if side == "SHORT":
                            stop_try = anchor + buf
                            offending = [r for r in runs
                                         if (r[0] <= stop_try <= r[1]) or (stop_try < r[0] <= stop_try + buf)]
                            next_anchor = max((r[1] for r in offending), default=None)
                        else:
                            stop_try = anchor - buf
                            offending = [r for r in runs
                                         if (r[0] <= stop_try <= r[1]) or (stop_try - buf <= r[1] < stop_try)]
                            next_anchor = min((r[0] for r in offending), default=None)
                        if next_anchor is None or next_anchor == anchor:
                            break
                        anchor = next_anchor
                    min_stop_pts = abs(anchor - entry) + SL_BUFFER_ATR_MIN * float(atr)
                    if min_stop_pts > 0:
                        max_rr = best_r / min_stop_pts
                        ev.metrics["min_compliant_stop_points"] = min_stop_pts
                        ev.metrics["min_compliant_stop_anchor"] = anchor
                        ev.metrics["max_achievable_rr"] = max_rr
                        if max_rr < rr_min:
                            ev.add("NO_PAYABLE_SETUP", "FATAL", "A6",
                                   f"asset-level verdict: the best front-runnable target pays "
                                   f"{max_rr:.2f}R against the minimum compliant stop "
                                   f"({min_stop_pts:.1f} points = clear the {anchor} fuel edge by "
                                   f"{SL_BUFFER_ATR_MIN} ATR), so no card on this asset can be staged "
                                   f"at >= {rr_min}R in this generation",
                                   max_achievable_rr=max_rr, min_stop_points=min_stop_pts)

            # the TP itself must front-run a magnet, never sit inside one
            inside = [b for b in magnets if b[0] <= tp <= b[1]]
            if inside:
                b = max(inside, key=lambda x: x[2])
                ev.add("TP_INSIDE_MAGNET", "FATAL", "A6",
                       f"TP {tp} sits INSIDE the magnet pool [{b[0]}, {b[1]}] carrying {b[2]/1e6:.3f}M USD "
                       f"instead of front-running it", magnet=[b[0], b[1]], magnet_usd=b[2])
            elif magnets:
                if side == "SHORT":
                    pool = [b for b in magnets if b[1] < tp]
                    b = max(pool, key=lambda x: x[1]) if pool else None
                else:
                    pool = [b for b in magnets if b[0] > tp]
                    b = min(pool, key=lambda x: x[0]) if pool else None
                if b is not None:
                    edge = b[1] if side == "SHORT" else b[0]
                    off_bps = abs(tp - edge) / edge * 10_000.0
                    ev.metrics["tp_front_run_bps"] = abs(off_bps)
                    ev.metrics["tp_governing_magnet"] = [b[0], b[1], b[2]]
                    if not (FRONT_RUN_BPS_LOW <= off_bps <= FRONT_RUN_BPS_HIGH):
                        ev.add("TP_FRONT_RUN_OFF", "MAJOR", "A6",
                               f"TP {tp} is {off_bps:.2f} bps from the governing magnet edge {edge}; desk doctrine "
                               f"is a {FRONT_RUN_BPS_LOW:.0f}-{FRONT_RUN_BPS_HIGH:.0f} bps front-run",
                               magnet=[b[0], b[1]], off_bps=off_bps)
        else:
            ev.add("NO_MAGNETS", "FATAL", "A6", "no opposing stop/liquidation magnet >= 0.50M USD on the target side")
        if rr < rr_min:
            ev.add("RR_BELOW_MIN", "FATAL" if rr < 1.0 else "MAJOR", "A6",
                   f"quoted geometry {rr:.2f}R < {rr_min}R required for {symbol}")

        # ---- regime alignment + CVD
        if regime == "BEARISH" and side == "LONG":
            ev.add("COUNTER_TREND", "FATAL", "A2", "Model 1/2 longs are banned in a verified BEARISH regime")
        if regime == "BULLISH" and side == "SHORT":
            ev.add("COUNTER_TREND", "FATAL", "A2", "shorts are banned in a verified BULLISH regime")
        session_cvd = mh.get("session_cvd_usd")
        if session_cvd is None:
            session_cvd = tf.get("session_tick_cvd")
        ev.metrics["session_cvd"] = session_cvd
        if session_cvd is not None:
            if side == "SHORT" and session_cvd > 0:
                ev.add("COUNTER_CVD", "MAJOR", "A2", f"short against positive session CVD {session_cvd:,.0f}", purchase_side=True)
            if side == "LONG" and session_cvd < 0:
                ev.add("COUNTER_CVD", "MAJOR", "A2", f"long against negative session CVD {session_cvd:,.0f}", purchase_side=True)

        # ---- capacity / floor defense
        risk_node = snap.get("risk") or {}
        cap_node = snap.get("capacity") or {}
        existing_stress = float(risk_node.get("total_contingent_stress_usd") or 0.0)
        balance = float(((snap.get("account") or {}).get("balance_usd")) or 0.0)
        tickets_wanted = max(1, card.batch_count)
        available_slots = cap_node.get("available")
        card_stress = (STRESS_MULTIPLIER * risk_usd + STRESS_PER_TICKET_USD) * tickets_wanted
        post = balance - existing_stress - card_stress
        ev.metrics.update({"existing_stress_usd": existing_stress, "card_stress_usd": card_stress,
                           "stress_multiplier": STRESS_MULTIPLIER, "stress_per_ticket_usd": STRESS_PER_TICKET_USD,
                           "post_stop_equity_usd": post, "available_slots": available_slots,
                           "tickets_wanted": tickets_wanted,
                           "required_post_stop_equity_usd": risk_node.get("required_post_stop_equity_usd")})
        if available_slots is not None and tickets_wanted > int(available_slots):
            ev.add("CAPACITY_EXCEEDED", "FATAL", "A5",
                   f"card asks for {tickets_wanted} joint-fill slot(s) but the snapshot exposes only "
                   f"{available_slots} available (4-slot joint-fill policy)",
                   tickets_wanted=tickets_wanted, available_slots=available_slots)
        if post < OPERATING_BUFFER_USD:
            ev.add("FLOOR_BREACH", "FATAL", "A5",
                   f"joint post-stop equity {post:.3f} USD < {OPERATING_BUFFER_USD} USD operating buffer",
                   post_stop_equity_usd=post)

        ev.qualified = not ev.fatal()
        ev.action_contradicted = ev.fatal()

    # ---- passive actions -------------------------------------------------
    else:
        if card.action == "WATCH":
            ev.metrics["untriggered"] = True
            trig = card.meta.get("condition")
            if trig:
                ev.add("CONDITIONAL_UNTRIGGERED", "INFO", "A5",
                       f"armed trigger has not fired in this generation: {trig}", condition=trig)
                ev.metrics["armed_trigger"] = trig
                ev.metrics["invalidation"] = card.meta.get("invalidation")
            else:
                ev.add("NOT_EVALUATED", "MINOR", "A6",
                       "card carries no geometry, no evaluated target and no armed trigger")
        elif card.action in ("HOLD", "DELETE", "MODIFY") and target:
            probe = Card(id=f"{card.id}::probe", action="STAGE",
                         asset=target.get("asset", card.asset), side=target.get("side"),
                         entry=target.get("entry"), sl=target.get("sl"),
                         tp=target.get("tp"), lots=target.get("lots"), meta=card.meta)
            sub = evaluate_card(probe, snap, continuity)
            probe_fatal = sub.fatal()
            probe_majors = sub.count("MAJOR")
            ev.metrics.update({k: sub.metrics.get(k) for k in (
                "symbol", "mid", "atr_14", "regime", "entry", "sl", "tp", "lots", "stop_points",
                "risk_usd", "reward_usd", "rr_gross", "entry_distance_atr", "friction_pct",
                "sl_clearance_atr", "hazard_union", "hazard_union_usd", "in_range_defense_usd",
                "overwhelm_ratio", "best_reachable_rr", "best_reachable_tp", "post_stop_equity_usd",
                "spread_over_atr", "spread_bps", "min_lot_spread_cash_usd",
                "tp_front_run_bps", "tp_governing_magnet", "max_achievable_rr",
                "min_compliant_stop_points", "min_compliant_stop_anchor", "entry_run",
                "entry_fuel_usd", "sl_clearance_reference")})
            # The probe's findings are EVIDENCE about the order under audit, not flaws in the
            # recommendation itself. They move into metrics; only the action-level ruling
            # below stays in `findings` and can contradict the card.
            ev.metrics["probe_findings"] = [f.as_dict() for f in sub.findings]
            ev.metrics["probe_fatal"] = probe_fatal
            ev.metrics["probe_majors"] = probe_majors
            ev.metrics["probe_fatal_codes"] = [f.code for f in sub.findings if f.severity == "FATAL"]
            ev.metrics["probe_major_codes"] = [f.code for f in sub.findings if f.severity == "MAJOR"]
            # The probe's own findings are the EVIDENCE for the ruling, so they are carried
            # into `findings` downgraded: they must not themselves mark the recommendation
            # as contradicted. The action-level verdict below does that.
            for f in sub.findings:
                if f.severity in ("FATAL", "MAJOR"):
                    ev.findings.append(Finding("PROBE_" + f.code, "MINOR", f.archetype,
                                               f.message, f.values, f.purchase_side))
            if card.action == "DELETE":
                if not probe_fatal and probe_majors == 0:
                    ev.add("DELETE_UNJUSTIFIED", "FATAL", "A5",
                           "DELETE recommended for an order that clears every hard gate")
                    ev.action_contradicted = True
                else:
                    ev.metrics["delete_justification"] = ev.metrics["probe_fatal_codes"] + \
                        ev.metrics["probe_major_codes"]
                    ev.qualified = not probe_fatal
            elif card.action == "HOLD":
                if probe_fatal:
                    ev.add("HOLD_CONTRADICTED", "FATAL", "A1",
                           "HOLD-as-is recommended for an order with fatal gate failures",
                           probe_fatal_codes=ev.metrics["probe_fatal_codes"])
                    ev.action_contradicted = True
                elif probe_majors > 3:
                    ev.add("HOLD_FRAGILE", "MAJOR", "A4",
                           f"HOLD kept on an order carrying {probe_majors} MAJOR advisories")
            elif card.action == "MODIFY":
                if probe_fatal:
                    ev.add("MODIFY_STILL_FATAL", "FATAL", "A1",
                           "the modified geometry still carries a fatal flaw",
                           probe_fatal_codes=ev.metrics["probe_fatal_codes"])
                    ev.action_contradicted = True
                else:
                    ev.add("MODIFY_VIABLE", "INFO" if probe_majors == 0 else "MINOR", "A1",
                           "the modified geometry clears every hard gate; residual advisories: "
                           + (", ".join(ev.metrics["probe_major_codes"]) or "none"))

    # One consistent meaning across every card type: a card is verified when it survives
    # every attack (no FATAL finding of its own). Untriggered conditionals are advisory only.
    if card.action in TRADE_ACTIONS:
        ev.qualified = not ev.fatal()
    elif card.action == "WATCH":
        ev.qualified = False
    else:
        ev.qualified = not ev.fatal()
    ev.action_contradicted = ev.fatal()
    return ev


# --------------------------------------------------------------------------
# Five personas + arena rubric
# --------------------------------------------------------------------------
PERSONAS = (
    ("Orderflow & Microstructure", {"A4": 2.0, "A8": 2.0, "A2": 1.5, "A7": 1.0}),
    ("Structural Price Action", {"A5": 1.5, "A3": 2.0, "A1": 1.5, "A6": 1.5}),
    ("Liquidation & Stop Forensic", {"A1": 2.5, "A8": 2.0, "A6": 1.5, "A4": 1.0}),
    ("Macro Risk & Portfolio Governor", {"A7": 2.0, "A5": 1.5, "A6": 1.0, "A4": 1.0}),
    ("Adversarial Pre-Mortem Red Team", {"A1": 1.5, "A2": 1.5, "A3": 1.5, "A4": 1.0, "A5": 1.0, "A6": 1.0, "A7": 1.0, "A8": 1.0}),
)
RUBRIC_WEIGHTS = (("correctness", 30), ("completeness", 25), ("specificity", 15),
                  ("robustness", 20), ("clarity", 10))


def _persona_scores(ev: CardEvaluation, emphasis: Dict[str, float]) -> Dict[str, Any]:
    penal = 0.0
    for f in ev.findings:
        w = emphasis.get(f.archetype, 0.5)
        if f.severity == "FATAL":
            penal += 3.0 * w
        elif f.severity == "MAJOR":
            penal += 1.5 * w
        elif f.severity == "MINOR":
            penal += 0.5 * w
    if ev.metrics.get("purchase_side_flagged"):
        penal *= 1.15
    details = 0.0
    if ev.metrics.get("hazard_union") and ev.metrics["hazard_union"][0] is not None:
        details += 2.0
    if ev.metrics.get("in_range_walls") is not None:
        details += 2.0
    if ev.metrics.get("best_reachable_rr") is not None or ev.metrics.get("probe"):
        details += 2.0
    if ev.metrics.get("friction_pct") is not None:
        details += 2.0
    base = 9.0
    correctness = max(0.0, min(10.0, base - penal))
    codes = {f.code for f in ev.findings}
    if "NOT_EVALUATED" in codes:
        completeness = 3.0
    elif "CONDITIONAL_UNTRIGGERED" in codes:
        completeness = 4.0
    else:
        completeness = max(0.0, min(10.0, 5.0 + details))
    specificity = max(0.0, min(10.0, 4.0 + details))
    robustness = max(0.0, min(10.0, 9.0 - penal * 0.9))
    clarity = 8.0 if ev.card.thesis else 6.0
    return {"correctness": round(correctness, 2), "completeness": round(completeness, 2),
            "specificity": round(specificity, 2), "robustness": round(robustness, 2),
            "clarity": round(clarity, 2)}


def persona_opinions(ev: CardEvaluation) -> Dict[str, Dict[str, str]]:
    """Each council seat interrogates the card with its OWN evidence before the synthesis.
    The opinions are independent read-outs of the snapshot, not a restatement of the
    findings list: a seat can object even when no gate fired, and can stay silent when a
    gate fired on another seat's discipline."""
    A = ev.asset or {}
    m = ev.metrics
    q = A.get("quotes") or {}
    ci = A.get("causal_indicators") or {}
    mh = A.get("multi_horizon_cvd") or {}
    tf = A.get("tradfi_orderflow") or {}
    ob = A.get("orderbook_live_depth") or {}
    _trap = A.get("trapped_traders_signal")
    trap = _trap.get("signal") if isinstance(_trap, dict) else _trap
    side = m.get("side") or (ev.card.side or "SHORT")
    cvd = mh.get("session_cvd_usd")
    if cvd is None:
        cvd = tf.get("session_tick_cvd")
    div = mh.get("divergence") or tf.get("flow_bias")
    imb = ob.get("book_imbalance")
    cvd = cvd if isinstance(cvd, (int, float)) else None
    imb = imb if isinstance(imb, (int, float)) else None

    of = []
    if cvd is not None:
        aligned = (cvd < 0) == (side == "SHORT")
        of.append(f"session CVD {cvd:,.0f} ({'with' if aligned else 'AGAINST'} the {side})")
    if div:
        of.append(f"tape {div}")
    if imb is not None:
        of.append(f"L2 imbalance {imb:+.4f}")
    if trap:
        of.append(f"trap signal {trap}")

    sp = []
    if ci.get("ema_20") and q.get("mid"):
        sp.append(f"mid {q['mid']} vs EMA20 {ci['ema_20']:.4f} / EMA50 {ci.get('ema_50')} / EMA200 {ci.get('ema_200')}")
    if ci.get("session_vwap_utc"):
        sp.append(f"VWAP {ci['session_vwap_utc']:.4f} sigma {ci.get('session_sigma')}")
    if m.get("entry_run"):
        sp.append(f"entry belt {m['entry_run']}")
    if m.get("sl_clearance_atr") is not None:
        sp.append(f"stop clearance {m['sl_clearance_atr']:+.3f} ATR")

    lf = []
    if m.get("entry_fuel_usd"):
        lf.append(f"{m['entry_fuel_usd']/1e6:.2f}M USD of un-swept fuel at the entry")
    if m.get("hazard_union_usd"):
        lf.append(f"{m['hazard_union_usd']/1e6:.2f}M USD in the SL belt")
    if m.get("in_range_defense_usd") is not None:
        lf.append(f"in-range wall defense {m['in_range_defense_usd']/1e6:.2f}M USD")
    if m.get("sl_clearance_reference") is not None:
        lf.append(f"governing belt edge {m['sl_clearance_reference']}")

    mg = []
    if m.get("max_achievable_rr") is not None:
        mg.append(f"asset ceiling {m['max_achievable_rr']:.2f}R")
    if m.get("friction_pct") is not None:
        mg.append(f"friction {m['friction_pct']:.2f}% of risk")
    if m.get("min_lot_spread_cash_usd") is not None:
        mg.append(f"min-lot spread cash {m['min_lot_spread_cash_usd']:.2f} USD")
    if m.get("card_stress_usd") is not None:
        mg.append(f"card stress {m['card_stress_usd']:.2f} USD, post-stop {m.get('post_stop_equity_usd'):.2f} USD")

    rt = []
    if m.get("best_reachable_rr") is not None and m.get("max_achievable_rr") is not None:
        rt.append(f"best reachable {m['best_reachable_rr']:.2f}R vs ceiling {m['max_achievable_rr']:.2f}R")
    if m.get("tp_front_run_bps") is not None:
        rt.append(f"TP front-run offset {m['tp_front_run_bps']:.2f} bps")
    if m.get("entry_distance_atr") is not None:
        rt.append(f"entry {m['entry_distance_atr']:.2f} ATR from mid")
    if m.get("hazard_runs"):
        rt.append(f"book structure {len(m['hazard_runs'])} fuel belts overhead")

    if not A:
        # portfolio-level card: the seats read the book, not an asset
        snap = ev.snap or {}
        acct = snap.get("account") or {}
        risk = snap.get("risk") or {}
        cap = snap.get("capacity") or {}
        assets = snap.get("assets_matrix_24") or {}
        with_ci = sum(1 for a in assets.values()
                      if (a.get("causal_indicators") or {}).get("trend_regime") not in (None, "INSUFFICIENT_HISTORY"))
        walls = [w for a in assets.values()
                 for w in ((a.get("orderbook_live_depth") or {}).get("whale_walls_l3") or [])]
        big = [w for w in walls if float(w.get("notional_usd") or 0) >= 500_000]
        pers = [w for w in big if float(w.get("persist_s") or 0) >= 180]
        port = [f"balance {acct.get('balance_usd')} USD",
                f"contingent stress {risk.get('total_contingent_stress_usd')} USD",
                f"post-joint-stop {risk.get('post_joint_stop_equity_usd')} USD vs {risk.get('required_post_stop_equity_usd')} buffer",
                f"joint-fill slots used {cap.get('used_joint_fill')}/{cap.get('max_concurrent')}",
                f"causal-indicator coverage {with_ci}/{len(assets)} assets",
                f"walls >= 500k USD {len(big)}, with persist >= 180 s {len(pers)}"]
        of = ["flow coverage: " + (f"{with_ci}/{len(assets)} assets report taker CVD / tick CVD")]
        sp = [f"regime coverage: {with_ci}/{len(assets)} assets carry a trend regime"]
        lf = [f"verified wall defense across the book: {len(pers)} wall(s) with persist >= 180 s"]
        mg = port
        rt = ["worst case: every card in the universe was probed by the full gate set"] 
    fatal_codes = {f.code for f in ev.findings if f.severity == "FATAL"}
    out = {}
    for name, evidence, codes in (
        ("Orderflow & Microstructure", of, {"A2", "A4", "A7", "A8"}),
        ("Structural Price Action", sp, {"A1", "A3", "A5", "A6"}),
        ("Liquidation & Stop Forensic", lf, {"A1", "A6", "A8"}),
        ("Macro Risk & Portfolio Governor", mg, {"A5", "A7"}),
        ("Adversarial Pre-Mortem Red Team", rt, {"A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"}),
    ):
        mine = {f.code for f in ev.findings
                if f.severity == "FATAL" and f.archetype in codes}
        mine |= {c[len("PROBE_"):] for c in fatal_codes if c.startswith("PROBE_")} if name == \
            "Adversarial Pre-Mortem Red Team" else set()
        out[name] = {
            "vote": "CONTRADICTS" if mine else "NO OBJECTION",
            "evidence": "; ".join(evidence) or "no evidence in this generation",
            "fatal_seen": sorted(mine),
        }
    return out


def persona_verdicts(ev: CardEvaluation) -> List[Dict[str, Any]]:
    purchase = [f for f in ev.findings if f.purchase_side and f.severity in ("FATAL", "MAJOR")]
    if purchase:
        ev.metrics["purchase_side_flagged"] = [f.code for f in purchase]
    opinions = persona_opinions(ev)
    out = []
    for name, emphasis in PERSONAS:
        sc = _persona_scores(ev, emphasis)
        total = sum(sc[k] * w for k, w in RUBRIC_WEIGHTS) / 10.0
        op = opinions[name]
        note = "no fatal flaw found" if not ev.fatal() else \
            "fatal: " + ", ".join(f.code for f in ev.findings if f.severity == "FATAL")
        if purchase:
            note += " | purchase-side sweep hazard: " + ", ".join(f.code for f in purchase)
        out.append({"persona": name, "scores": sc, "weighted_total": round(total, 2), "note": note,
                    "vote": op["vote"], "evidence": op["evidence"],
                    "fatal_seen": op["fatal_seen"]})
    return out


def rubric_total(verdicts: Sequence[Dict[str, Any]]) -> float:
    return round(sum(v["weighted_total"] for v in verdicts) / max(1, len(verdicts)), 2)


# --------------------------------------------------------------------------
# Bracket
# --------------------------------------------------------------------------
def head_to_head(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    """Fatal rule first (arena rubric 'The fatal rule'), then weighted totals."""
    af, bf = a["fatal"], b["fatal"]
    if af and not bf:
        winner, reason = b["id"], f"{a['id']} is contradicted by the snapshot; {b['id']} is not"
    elif bf and not af:
        winner, reason = a["id"], f"{b['id']} is contradicted by the snapshot; {a['id']} is not"
    elif a["total"] > b["total"]:
        winner, reason = a["id"], f"higher rubric total ({a['total']} vs {b['total']})"
    elif b["total"] > a["total"]:
        winner, reason = b["id"], f"higher rubric total ({b['total']} vs {a['total']})"
    else:
        winner, reason = a["id"], "exact tie: fewer standing attacks (deterministic order)"
    return {"a": a["id"], "b": b["id"], "winner": winner, "reason": reason,
            "a_total": a["total"], "b_total": b["total"], "a_fatal": af, "b_fatal": bf}


def run_bracket(entries: List[Dict[str, Any]], seed: int) -> Dict[str, Any]:
    rng = random.Random(seed)
    alive = list(entries)
    rng.shuffle(alive)
    rounds: List[Dict[str, Any]] = []
    rnd = 1
    while len(alive) > 1:
        nxt: List[Dict[str, Any]] = []
        matches = []
        for i in range(0, len(alive) - 1, 2):
            res = head_to_head(alive[i], alive[i + 1])
            matches.append(res)
            nxt.append(alive[i] if res["winner"] == alive[i]["id"] else alive[i + 1])
        bye = None
        if len(alive) % 2 == 1:
            bye = alive[-1]
            nxt.append(bye)
        rounds.append({"round": rnd, "matches": matches,
                       "bye": bye["id"] if bye else None,
                       "survivors": [x["id"] for x in nxt]})
        alive = nxt
        rnd += 1
    return {"rounds": rounds, "winner": alive[0]["id"] if alive else None}


# --------------------------------------------------------------------------
# Runner
# --------------------------------------------------------------------------
def evaluate_all(cards: Sequence[Card], snap: Dict[str, Any],
                 continuity: Dict[Tuple[str, str], Dict[str, Any]]) -> List[Dict[str, Any]]:
    entries = []
    for card in cards:
        ev = evaluate_card(card, snap, continuity)
        verdicts = persona_verdicts(ev)
        entries.append({
            "id": card.id, "action": card.action, "asset": card.asset, "side": card.side,
            "thesis": card.thesis, "engine": card.engine, "target_ticket": card.target_ticket,
            "metrics": ev.metrics, "findings": [f.as_dict() for f in ev.findings],
            "personas": verdicts, "total": rubric_total(verdicts),
            "fatal": ev.fatal(), "action_contradicted": ev.action_contradicted,
            "verified": ev.qualified,
        })
    return entries


def build_report(run: Dict[str, Any]) -> str:
    L: List[str] = []
    L.append(f"# Arena tournament {run['run_id']}")
    L.append("")
    L.append(f"- snapshot: `{run['snapshot_path']}` generation `{run['generation_id']}` as_of `{run['as_of_utc']}`")
    L.append(f"- cards: `{run['cards_path']}` sha256 `{run['cards_sha256'][:16]}`")
    L.append(f"- evidence ledgers: {', '.join('`%s`' % p for p in run['evidence_paths']) or 'none'}")
    L.append(f"- seed: {run['seed']} | rubric weights: " + ", ".join(f"{k} {w}" for k, w in RUBRIC_WEIGHTS))
    L.append(f"- **winner: `{run['bracket']['winner']}`**")
    L.append("")
    L.append("## Scoreboard")
    L.append("")
    L.append("| card | action | fatal | purchase-side hazard | rubric /100 | verdict |")
    L.append("|---|---|---|---|---:|---|")
    for e in sorted(run["entries"], key=lambda x: -x["total"]):
        ps = ", ".join(e["metrics"].get("purchase_side_flagged") or []) or "-"
        verdict = "CONTRADICTED" if e["fatal"] else ("VERIFIED" if e["verified"] else "advisory only")
        L.append(f"| `{e['id']}` | {e['action']} | {'YES' if e['fatal'] else 'no'} | {ps} | "
                 f"{e['total']:.2f} | {verdict} |")
    L.append("")
    L.append("## Bracket")
    for r in run["bracket"]["rounds"]:
        L.append(f"### Round {r['round']}")
        for m in r["matches"]:
            L.append(f"- `{m['a']}` ({m['a_total']}, fatal={m['a_fatal']}) vs `{m['b']}` "
                     f"({m['b_total']}, fatal={m['b_fatal']}) -> **{m['winner']}** — {m['reason']}")
        if r["bye"]:
            L.append(f"- bye: `{r['bye']}`")
    L.append("")
    L.append("## Findings per card")
    for e in run["entries"]:
        L.append(f"### `{e['id']}` — {e['action']}" + (f" {e['side']} {e['asset']}" if e["asset"] else ""))
        if e["thesis"]:
            L.append(f"> {e['thesis']}")
        m = e["metrics"]
        keep = ["symbol", "mid", "atr_14", "regime", "entry", "sl", "tp", "lots", "stop_points",
                "risk_usd", "reward_usd", "rr_gross", "rr_min_required", "entry_distance_atr",
                "friction_pct", "sl_clearance_atr", "hazard_union", "hazard_union_usd",
                "in_range_defense_usd", "overwhelm_ratio", "best_reachable_rr", "best_reachable_tp",
                "post_stop_equity_usd", "min_lot_spread_cash_usd", "qualified_candidates",
                "delete_justification", "probe_fatal"]
        L.append("- metrics: " + ", ".join(f"{k}={m.get(k)}" for k in keep if k in m))
        if not e["findings"]:
            L.append("- findings: none")
        for f in e["findings"]:
            tag = " [purchase-side]" if f["purchase_side"] else ""
            L.append(f"- {f['severity']}{tag} `{f['code']}` ({f['archetype']}: {ARCHETYPES.get(f['archetype'],'')}) — {f['message']}")
        for f in m.get("probe_findings") or []:
            tag = " [purchase-side]" if f.get("purchase_side") else ""
            L.append(f"- probe {f['severity']}{tag} `{f['code']}` ({f['archetype']}) — {f['message']}")
        for p in e["personas"]:
            L.append(f"  - {p['persona']}: {p['weighted_total']}/100 — {p['note']}")
        L.append("")
    L.append("## Runtime disclosure")
    L.append("")
    L.append("Deterministic harness: same snapshot + same cards + same seed reproduces this report byte-for-byte "
             "for the decision layer. It is a falsification engine, not a profit proof: modelled stress is not "
             "immunity to unbounded gaps, and no broker execution was performed.")
    return "\n".join(L) + "\n"


def run_tournament(snapshot_path: str, cards_path: str, out_dir: str, seed: int,
                   evidence_paths: Sequence[str], run_id: Optional[str] = None) -> Dict[str, Any]:
    snap = load_snapshot(snapshot_path)
    with open(cards_path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    cards_doc = json.loads(raw)
    cards = [Card.from_json(c) for c in cards_doc.get("cards", [])]
    continuity = build_continuity_table(load_evidence_ledgers(evidence_paths),
                                        float(snap.get("as_of_epoch") or 0.0))
    entries = evaluate_all(cards, snap, continuity)
    bracket = run_bracket(entries, seed)
    run_id = run_id or f"cycle_{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    run = {
        "run_id": run_id, "seed": seed, "snapshot_path": snapshot_path,
        "snapshot_generation": snap.get("generation_id"), "generation_id": snap.get("generation_id"),
        "as_of_utc": snap.get("as_of_utc"), "trade_authorization": snap.get("trade_authorization"),
        "cards_path": cards_path, "cards_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        "evidence_paths": [p for p in evidence_paths if os.path.exists(p)],
        "continuity_keys": len(continuity),
        "entries": entries, "bracket": bracket,
        "rubric_weights": dict(RUBRIC_WEIGHTS),
        "invariants": {
            "hard_floor_usd": HARD_FLOOR_USD, "operating_buffer_usd": OPERATING_BUFFER_USD,
            "risk_envelope_usd": [RISK_MIN_USD, RISK_MAX_USD], "stress_multiplier": STRESS_MULTIPLIER,
            "stress_per_ticket_usd": STRESS_PER_TICKET_USD,
            "entry_proximity_atr_max": ENTRY_PROXIMITY_ATR_MAX,
            "sl_buffer_atr": [SL_BUFFER_ATR_MIN, SL_BUFFER_ATR_MAX],
            "friction_max": FRICTION_MAX, "rr_min": RR_MIN, "target_horizon_atr": TARGET_HORIZON_ATR,
        },
    }
    os.makedirs(out_dir, exist_ok=True)
    run_dir = os.path.join(out_dir, run_id)
    os.makedirs(run_dir, exist_ok=True)
    with open(os.path.join(run_dir, "run.json"), "w", encoding="utf-8") as fh:
        json.dump(run, fh, indent=1, default=str)
    report = build_report(run)
    with open(os.path.join(run_dir, "REPORT.md"), "w", encoding="utf-8") as fh:
        fh.write(report)
    with open(os.path.join(out_dir, "LATEST"), "w", encoding="utf-8") as fh:
        fh.write(run_id + "\n")
    run["run_dir"] = run_dir
    run["report"] = report
    return run


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Run the repo-native arena tournament over trade hypothesis cards.")
    ap.add_argument("--snapshot", default="docs/telemetry/live_snapshot_latest.json")
    ap.add_argument("--cards", required=True)
    ap.add_argument("--out", default="docs/trade_plans/arena_runs")
    ap.add_argument("--evidence", nargs="*", default=None,
                    help="earlier evidence ledgers used to re-establish wall continuity")
    ap.add_argument("--seed", type=int, default=106)
    ap.add_argument("--run-id", default=None)
    ap.add_argument("--print", action="store_true", help="print the report to stdout")
    args = ap.parse_args(argv)

    evidence = args.evidence
    if evidence is None:
        base = "docs/trade_plans"
        evidence = []
        if os.path.isdir(base):
            for name in sorted(os.listdir(base)):
                if name.startswith("ARENA_COUNCIL_EVIDENCE_") and name.endswith(".json"):
                    evidence.append(os.path.join(base, name))

    run = run_tournament(args.snapshot, args.cards, args.out, args.seed, evidence, args.run_id)
    if args.print:
        sys.stdout.write(run["report"])
    else:
        print(f"run {run['run_id']} -> {run['run_dir']}")
        print(f"winner: {run['bracket']['winner']}")
        for e in sorted(run["entries"], key=lambda x: -x["total"]):
            print(f"  {e['id']:<28} total={e['total']:>6.2f} fatal={e['fatal']!s:<5} "
                  f"verified={e['verified']!s:<5} purchase_side={e['metrics'].get('purchase_side_flagged')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
