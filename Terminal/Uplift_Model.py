"""Paired broker-quote replay and purged chronological LightGBM uplift gate.

The estimand is marginal net equity over a fixed six-hour holding episode.
Both branches manage the same existing book; only one accepts the candidate.
No win/loss labels or unobserved rejected-trade outcomes are invented.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
from Terminal.Risk_Sizing_Engine import number

FEATURES = ("confluence", "quality", "l2_signal", "macro_score", "wall_imbalance",
            "aggressor_imbalance", "liquidation_delta", "sigma_h", "efficiency_ratio",
            "friction_bps", "risk_usd", "existing_floating_r", "existing_age_bars",
            "signed_correlation", "variance_before", "incremental_variance", "drawdown_room",
            "candidate_net_target_r")
POLICY_VERSION = "omni.ratchet.costaware_0.8-0.35_1.5-0.85_runner-0.65_tp2.5_24bars.v2"

def ratchet(entry, initial_r, direction, gain_r, current_sl, atr, friction_bps: float = 41.0, buffer_r: float = 0.05):
    sign = 1 if direction == "LONG" else -1
    lock = None
    if gain_r >= 0.8:
        base_lock = 0.35
        if friction_bps > 0 and initial_r > 0:
            required_lock_r = (friction_bps / 10000.0 * entry / initial_r) + buffer_r
            lock = max(base_lock, required_lock_r)
        else:
            lock = base_lock
    if gain_r >= 1.5:
        base_lock = 0.85
        if friction_bps > 0 and initial_r > 0:
            required_lock_r = (friction_bps / 10000.0 * entry / initial_r) + buffer_r
            lock = max(base_lock, required_lock_r)
        else:
            lock = base_lock
    if gain_r >= 2.0: lock = max(lock or 0.85, gain_r-0.65)
    if lock is None: return current_sl
    proposed = entry+sign*lock*initial_r
    if current_sl <= 0: return proposed
    return max(current_sl, proposed) if sign == 1 else min(current_sl, proposed)

def executable_ratchet(entry, initial_r, direction, gain_r, current_sl, atr, bid, ask, tick_size, stop_distance,
                       friction_bps: float = 41.0, buffer_r: float = 0.05):
    sign = 1 if direction == "LONG" else -1
    proposed = ratchet(entry, initial_r, direction, gain_r, current_sl, atr, friction_bps=friction_bps, buffer_r=buffer_r)
    proposed = (math.floor(proposed/tick_size) if sign==1 else math.ceil(proposed/tick_size))*tick_size
    valid = proposed < bid-stop_distance if sign==1 else proposed > ask+stop_distance
    return proposed if valid and sign*(proposed-current_sl) >= tick_size*0.99 else current_sl

def feature_vector(mapping):
    values = np.array([number(mapping.get(k), float("nan")) for k in FEATURES])
    if not np.isfinite(values).all(): raise ValueError("uplift_features_missing_or_nonfinite")
    return values

def replay_episode(episode, ticks):
    start, end = episode["as_of"], episode["as_of"]+24*900
    equity = number(episode["equity_usd"])
    floor = number(episode["hard_floor_usd"])
    existing = copy.deepcopy(episode["existing_positions"])
    candidate = copy.deepcopy(episode["candidate"])
    states = [{"cash": equity, "positions": copy.deepcopy(existing), "halted": False},
              {"cash": equity, "positions": copy.deepcopy(existing)+[candidate], "halted": False}]
    # Existing floating PnL is already included in equity at the decision.
    for state in states:
        for p in state["positions"]:
            p["initial_mark_pnl"] = 0.0 if p is candidate else number(p.get("profit_usd"))
            if p.get("candidate_id") == candidate.get("candidate_id"): p["initial_mark_pnl"] = 0.0
    last = {}
    rows = sorted((t for t in ticks if start < t["time"] <= end), key=lambda t: t["time"])
    required = {p["symbol"] for p in existing+[candidate]}
    counts = {s: 0 for s in required}
    first_seen, last_seen = {}, {}
    for t in rows:
        if t["symbol"] not in required: continue
        bid, ask = number(t.get("bid")), number(t.get("ask"))
        if not 0 < bid < ask: continue
        last[t["symbol"]] = t
        counts[t["symbol"]] += 1
        first_seen.setdefault(t["symbol"], t["time"]); last_seen[t["symbol"]] = t["time"]
        for state in states:
            if state["halted"]: continue
            for p in list(state["positions"]):
                if p["symbol"] != t["symbol"]: continue
                sign = 1 if p["direction"] == "LONG" else -1
                mark = bid if sign == 1 else ask
                gain = sign*(mark-p["price_open"])/p["initial_r"]
                stop_hit = sign*(mark-p["sl"]) <= 0
                target_hit = sign*(mark-p["tp"]) >= 0
                timeout = (t["time"]-p["time"] >= 24*900 and gain < 0.20)
                # Evaluate existing stop before changing it on this quote.
                if stop_hit or target_hit or timeout:
                    pnl = sign*(mark-p["price_open"])*p["volume"]*p["contract_size"]
                    state["cash"] += pnl-p["initial_mark_pnl"]-number(p.get("residual_cost_usd"))
                    state["positions"].remove(p)
                else:
                    p_fric = number(p.get("sizing", {}).get("friction_bps", p.get("friction_bps", 41.0)))
                    p["sl"] = executable_ratchet(p["price_open"], p["initial_r"], p["direction"], gain, p["sl"],
                                                  p.get("atr", p["initial_r"]*0.5), bid, ask,
                                                  number(t.get("tick_size"), number(p.get("tick_size"), .01)),
                                                  number(t.get("stop_distance"), number(p.get("stop_distance"), .01)),
                                                  friction_bps=p_fric, buffer_r=0.05)
            mark_equity = state["cash"]
            for p in state["positions"]:
                quote = last.get(p["symbol"])
                if quote:
                    px = quote["bid"] if p["direction"] == "LONG" else quote["ask"]
                    sign = 1 if p["direction"] == "LONG" else -1
                    mark_equity += sign*(px-p["price_open"])*p["volume"]*p["contract_size"]-p["initial_mark_pnl"]-number(p.get("residual_cost_usd"))
                else: mark_equity -= number(p.get("residual_cost_usd"))
            if mark_equity <= floor:
                # A book cannot be flattened until every instrument has a causal quote.
                if all(p["symbol"] in last for p in state["positions"]):
                    state["cash"] = mark_equity; state["positions"] = []; state["halted"] = True
    if any(counts[s] < 2 or first_seen.get(s, end)-start > 30 or end-last_seen.get(s, start) > 30 for s in required):
        raise ValueError("episode_quote_coverage_incomplete")
    # Session gaps / long outages invalidate labels instead of implying perfect fills.
    for symbol in required:
        times = [t["time"] for t in rows if t["symbol"] == symbol]
        if any(b-a > 30 for a, b in zip(times, times[1:])): raise ValueError("episode_quote_gap")
    finals = []
    for state in states:
        net = state["cash"]
        for p in state["positions"]:
            q = last[p["symbol"]]
            sign = 1 if p["direction"] == "LONG" else -1
            px = q["bid"] if sign == 1 else q["ask"]
            net += sign*(px-p["price_open"])*p["volume"]*p["contract_size"]-p["initial_mark_pnl"]-number(p.get("residual_cost_usd"))
        finals.append(net)
    return {"episode_id": episode["episode_id"], "as_of": start, "label_end": end,
            "features": episode["features"], "uplift_usd": finals[1]-finals[0], "equity_reject": finals[0],
            "equity_accept": finals[1], "policy_version": POLICY_VERSION, "source": "paired_MT5_quote_replay",
            "tick_quality": "FULL_MT5_TICKS" if rows and all(t.get("feed_kind")=="FULL_MT5_TICKS" for t in rows) else "POLLED_QUOTES"}

def label_episodes(episodes_path, ticks_path, output):
    import polars as pl
    episodes = [json.loads(x) for x in Path(episodes_path).read_text(encoding="utf-8").splitlines() if x.strip()]
    source = pl.scan_parquet(str(ticks_path)) if str(ticks_path).endswith(".parquet") else pl.scan_ndjson(str(ticks_path))
    labels, errors = [], []
    for e in episodes:
        try:
            symbols = list({p["symbol"] for p in e["existing_positions"]+[e["candidate"]]})
            ticks = source.filter((pl.col("time")>e["as_of"]) & (pl.col("time")<=e["as_of"]+21600) & pl.col("symbol").is_in(symbols)).collect().to_dicts()
            labels.append(replay_episode(e, ticks))
        except ValueError as exc: errors.append({"episode_id": e["episode_id"], "reason": str(exc)})
    Path(output).write_text("".join(json.dumps(l)+"\n" for l in labels), encoding="utf-8")
    return {"labels": len(labels), "excluded": errors}

def train_uplift(labels_path, output_dir, min_train=200):
    import lightgbm as lgb
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import brier_score_loss
    rows = sorted([json.loads(x) for x in Path(labels_path).read_text(encoding="utf-8").splitlines() if x.strip()], key=lambda x: x["as_of"])
    if len(rows) < min_train+120: raise ValueError("Need at least 320 complete replay labels")
    if any(r["label_end"] > time.time() for r in rows): raise ValueError("Future uplift outcomes are not observable")
    if any(r.get("source") != "paired_MT5_quote_replay" or r.get("policy_version") != POLICY_VERSION for r in rows):
        raise ValueError("Unverified or incompatible uplift labels")
    for r in rows:
        target = number(r.get("uplift_usd"), math.nan)
        accept = number(r.get("equity_accept"), math.nan)
        reject = number(r.get("equity_reject"), math.nan)
        if not all(math.isfinite(v) for v in (target, accept, reject)) or abs(target-(accept-reject)) > 1e-6:
            raise ValueError("Uplift target must equal paired net equity difference")
        if r["label_end"] != r["as_of"]+21600: raise ValueError("Uplift horizon mismatch")
    split1, split2 = int(len(rows)*0.60), int(len(rows)*0.80)
    # Training labels must have ended before calibration starts; calibration
    # labels must end before the untouched final test. Embargo is one full episode.
    cal_start, test_start = rows[split1]["as_of"], rows[split2]["as_of"]
    train = [r for r in rows[:split1] if r["label_end"]+24*900 < cal_start]
    cal = [r for r in rows[split1:split2] if r["label_end"]+24*900 < test_start]
    test = rows[split2:]
    if len(train) < min_train or len(cal) < 40 or len(test) < 40: raise ValueError("Insufficient purged chronological folds")
    def xy(data):
        return np.stack([feature_vector(r["features"]) for r in data]), np.array([r["uplift_usd"] for r in data])
    X, y = xy(train); Xc, yc = xy(cal); Xt, yt = xy(test)
    if len(np.unique(y > 0)) < 2 or len(np.unique(yc > 0)) < 2: raise ValueError("Need both positive and negative uplift episodes")
    params = dict(n_estimators=160, max_depth=3, num_leaves=7, learning_rate=0.03,
                  min_child_samples=30, reg_alpha=1.5, reg_lambda=3.0, random_state=895,
                  n_jobs=2, verbosity=-1)
    classifier = lgb.LGBMClassifier(**params).fit(X, y > 0)
    expectancy = lgb.LGBMRegressor(**params).fit(X, y)
    calibrator = LogisticRegression(C=0.5).fit(classifier.predict(Xc, raw_score=True).reshape(-1, 1), yc > 0)
    probabilities = calibrator.predict_proba(classifier.predict(Xt, raw_score=True).reshape(-1, 1))[:, 1]
    predicted = expectancy.predict(Xt)
    selected = (probabilities >= 0.60) & (predicted > 0)
    residual = yc-expectancy.predict(Xc)
    uncertainty = float(np.quantile(np.abs(residual), 0.80))
    conservative = selected & (predicted > uncertainty)
    # Only one second slot exists. Do not count overlapping counterfactual
    # episodes as simultaneously achievable portfolio profits.
    available_at = -math.inf
    for i, r in enumerate(test):
        if conservative[i] and r["as_of"] >= available_at: available_at = r["label_end"]
        else: conservative[i] = False
    # Estimate clustered uncertainty by decision day, never assume episodes iid.
    daily = {}
    for r, value, choose in zip(test, yt, conservative):
        if choose: daily[int(r["as_of"]//86400)] = daily.get(int(r["as_of"]//86400), 0)+value
    rng = np.random.default_rng(895)
    values = np.array(list(daily.values()))
    lower = float(np.quantile(np.mean(rng.choice(values, (2000, len(values)), replace=True), axis=1), 0.05)) if len(values) >= 10 else -math.inf
    full_ticks = all(r.get("tick_quality") == "FULL_MT5_TICKS" for r in rows)
    eligible = bool(full_ticks and np.sum(conservative) >= 40 and lower > 0)
    directory = Path(output_dir); directory.mkdir(parents=True, exist_ok=True)
    classifier.booster_.save_model(str(directory/"uplift_classifier.txt"))
    expectancy.booster_.save_model(str(directory/"uplift_expectancy.txt"))
    meta = {"schema": "omni.uplift.v1", "features": list(FEATURES), "policy_version": POLICY_VERSION,
            "created_at": time.time(), "label_end": max(r["label_end"] for r in rows),
            "max_age_seconds": 30*86400, "live_eligible": eligible, "probability_threshold": 0.60,
            "calibration_coef": float(calibrator.coef_[0, 0]), "calibration_intercept": float(calibrator.intercept_[0]),
            "expectancy_buffer_usd": uncertainty, "train_rows": len(train), "calibration_rows": len(cal),
            "test_rows": len(test), "selected_test_rows": int(np.sum(conservative)),
            "selected_test_net_uplift": float(yt[conservative].sum()), "daily_bootstrap_lower_mean": lower if math.isfinite(lower) else None,
            "brier": float(brier_score_loss(yt > 0, probabilities)), "estimand": "six_hour_fixed_book_marginal_equity",
            "tick_quality": "FULL_MT5_TICKS" if full_ticks else "POLLED_QUOTES_RESEARCH_ONLY",
            "labels_sha256": hashlib.sha256(Path(labels_path).read_bytes()).hexdigest(),
            "sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in directory.glob("uplift_*.txt")}}
    (directory/"manifest.json").write_text(json.dumps(meta, indent=2, allow_nan=False), encoding="utf-8")
    return meta

class UpliftGate:
    def __init__(self, directory):
        self.error, self.meta, self.classifier, self.expectancy = None, {}, None, None
        try:
            import lightgbm as lgb
            path = Path(directory); self.meta = json.loads((path/"manifest.json").read_text(encoding="utf-8"))
            if self.meta.get("features") != list(FEATURES) or self.meta.get("policy_version") != POLICY_VERSION: raise ValueError("uplift_schema_mismatch")
            for name in ("uplift_classifier.txt", "uplift_expectancy.txt"):
                if hashlib.sha256((path/name).read_bytes()).hexdigest() != self.meta["sha256"][name]: raise ValueError("uplift_checksum_mismatch")
            self.classifier = lgb.Booster(model_file=str(path/"uplift_classifier.txt"))
            self.expectancy = lgb.Booster(model_file=str(path/"uplift_expectancy.txt"))
        except Exception as exc: self.error = str(exc)

    def decide(self, features, as_of):
        if self.error or self.classifier is None: return {"accepted": False, "reason": "uplift_model_unavailable", "detail": self.error}
        if not self.meta.get("live_eligible"): return {"accepted": False, "reason": "uplift_oos_not_qualified"}
        data_end, created = number(self.meta.get("label_end")), number(self.meta.get("created_at"))
        age_limit = self.meta.get("max_age_seconds", 0)
        if not data_end or not created or data_end > as_of or created > as_of or as_of-data_end > age_limit or as_of-created > age_limit:
            return {"accepted": False, "reason": "uplift_stale_or_future"}
        values = feature_vector(features).reshape(1, -1)
        raw = float(self.classifier.predict(values, raw_score=True)[0])
        logit = self.meta["calibration_coef"]*raw+self.meta["calibration_intercept"]
        probability = 1/(1+math.exp(-max(-50, min(50, logit))))
        expectancy = float(self.expectancy.predict(values)[0])
        accepted = probability >= self.meta["probability_threshold"] and expectancy > self.meta["expectancy_buffer_usd"]
        return {"accepted": accepted, "reason": "uplift_positive" if accepted else "uplift_expectancy_veto",
                "probability_positive": probability, "expectancy_usd": expectancy,
                "expectancy_buffer_usd": self.meta["expectancy_buffer_usd"]}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    label = sub.add_parser("label"); label.add_argument("--episodes", required=True); label.add_argument("--ticks", required=True); label.add_argument("--output", required=True)
    train = sub.add_parser("train"); train.add_argument("--labels", required=True); train.add_argument("--output", required=True)
    args = parser.parse_args()
    result = label_episodes(args.episodes, args.ticks, args.output) if args.command == "label" else train_uplift(args.labels, args.output)
    print(json.dumps(result, indent=2))
