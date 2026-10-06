"""OMNI production: 16 assets, causal orderflow, covariance sizing and uplift.

python -m Terminal.OF_Strategy --mode mt5-trader       (paper)
python -m Terminal.OF_Strategy --mode mt5-trader --live
Legacy candle-only research is not a validation of this execution policy.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0, str(ROOT))
from Terminal.Asset_Universe import UNIVERSE
from Terminal.Omni_Trader import AI15mMT5Trader
from Terminal.Risk_Sizing_Engine import RiskPolicy

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("mt5-trader", "dry-run", "backtest", "inspect"), default="mt5-trader")
    parser.add_argument("--coin", default="SOL", help="Compatibility option; all allowed assets are scanned")
    parser.add_argument("--assets", default=",".join(UNIVERSE))
    parser.add_argument("--host", default="http://localhost:8095")
    parser.add_argument("--ticks", type=int, default=0, help="Maximum loop cycles; zero runs continuously")
    parser.add_argument("--paper", action="store_true")
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--risk", type=float, default=10, help="Compatibility option; confluence determines risk")
    parser.add_argument("--min-risk", type=float, default=10)
    parser.add_argument("--max-risk", type=float, default=45)
    parser.add_argument("--min-confluence", type=float, default=0.35, help="Minimum confluence score required for candidate selection")
    parser.add_argument("--sigma-budget", type=float, default=45, help="Maximum portfolio standard deviation in USD over 15 minutes")
    parser.add_argument("--cadence-minute", type=int, default=14)
    parser.add_argument("--cadence-second", type=int, default=30)
    parser.add_argument("--entry-mode", choices=("market", "limit"), default="limit")
    parser.add_argument("--ttl-min", type=float, default=7200, help="Minimum resting limit TTL seconds (Order Persistence Governor)")
    parser.add_argument("--ttl-max", type=float, default=21600, help="Maximum resting limit TTL seconds (hard cap)")
    parser.add_argument("--no-persistent-limits", action="store_true", help="Disable GTC persistent limits; fall back to broker-expiring orders")
    parser.add_argument("--account-id", type=int)
    parser.add_argument("--max-spread-points", type=float, default=None, help="Optional broker-specific cap; cost gates always apply")
    parser.add_argument("--state-file")
    parser.add_argument("--covariance", default=str(ROOT/"Data/Hyperdash_Historical/ledoit_wolf_covariance.parquet"))
    parser.add_argument("--uplift-model", default=str(ROOT/"Data/Models/omni_uplift"))
    parser.add_argument("--calendar", default=str(ROOT/"Data/macro_calendar.json"))
    parser.add_argument("--no-cognitive", action="store_true", help="Explicitly run the deterministic econometric policy")
    parser.add_argument("--no-pioneer", action="store_true", help="Disable the Pioneer decision engine conviction layer")
    parser.add_argument("--data-dir", default="Binance_Data")
    parser.add_argument("--forex-dir", default="Forex_Data")
    parser.add_argument("--chart", default="Terminal/of_equity_curve.png")
    args = parser.parse_args()
    if args.live and args.paper: parser.error("Choose one execution mode")
    if args.mode == "backtest":
        from Terminal.OF_Backtest_Legacy import run_master_walkforward
        print("LEGACY RESEARCH ONLY: this does not validate OMNI L2/L3 or uplift execution.")
        run_master_walkforward(Path(args.data_dir), Path(args.forex_dir), args.chart)
        return
    if args.mode == "inspect":
        from Terminal.Uplift_Model import UpliftGate
        from Terminal.Risk_Sizing_Engine import CovarianceGate
        from Terminal.Market_Intelligence import MarketIntelligenceEngine
        from Terminal.Data_Factory import DataFactory
        from Terminal.Pioneer_Decision_Engine import PioneerDecisionEngine
        import time
        report = {"assets": UNIVERSE, "live_orders": False}
        try:
            cov = CovarianceGate.load(args.covariance); cov.validate_time(time.time())
            report["covariance"] = cov.metadata
        except Exception as exc: report["covariance_error"] = str(exc)
        gate = UpliftGate(args.uplift_model)
        report["uplift"] = gate.error or gate.meta
        df = DataFactory(assets=UNIVERSE)
        macro = MarketIntelligenceEngine(calendar_path=args.calendar)
        macro.attach_data_factory(df)
        report["blackout"] = macro.check_macro_blackout(); report["calendar_error"] = macro.calendar_error
        pioneer = PioneerDecisionEngine()
        report["pioneer"] = {"policy_version": pioneer.policy.version,
                             "weights": pioneer.policy.weights,
                             "min_quality": pioneer.policy.min_quality,
                             "friction_bps": pioneer.policy.friction_bps}
        report["data_factory"] = df.macro_snapshot()
        print(json.dumps(report, indent=2)); return

    from Terminal.Market_Intelligence import MarketIntelligenceEngine
    from Terminal.Data_Factory import DataFactory, CrossSourceValidator
    from Terminal.Pioneer_Decision_Engine import PioneerDecisionEngine

    assets_list = [a.strip() for a in args.assets.split(",") if a.strip()]
    data_factory = DataFactory(assets=assets_list)
    validator = CrossSourceValidator(data_factory)

    def quality_provider(asset):
        if not data_factory.bus.book(asset):
            return None
        try:
            rep = validator.quality_report([asset])
            return rep.get("assets", {}).get(asset, rep)
        except Exception:
            return None

    intel = MarketIntelligenceEngine(calendar_path=args.calendar)
    intel.attach_data_factory(data_factory)

    trader = AI15mMT5Trader(coin=args.coin, host=args.host, paper_mode=not args.live,
                           min_risk_usd=args.min_risk, max_risk_usd=args.max_risk,
                           cadence_minute=args.cadence_minute, cadence_second=args.cadence_second,
                           entry_mode=args.entry_mode,
                           account_id=args.account_id, max_spread_points=args.max_spread_points,
                           state_file=args.state_file, allow_list=assets_list,
                           covariance_path=args.covariance, uplift_path=args.uplift_model,
                           intel=intel,
                           cognitive_enabled=not args.no_cognitive,
                           ttl_min_seconds=args.ttl_min, ttl_max_seconds=args.ttl_max,
                           persistent_limits=not args.no_persistent_limits,
                           policy=RiskPolicy(min_risk=args.min_risk, max_risk=args.max_risk, sigma_budget_usd=args.sigma_budget,
                                             min_confluence=args.min_confluence, max_book_age=30.0, max_future_skew_sec=30.0))

    if not args.no_pioneer:
        pioneer = PioneerDecisionEngine(quality_provider=quality_provider)
        trader.attach_pioneer(pioneer)

    trader.run(max_cycles=args.ticks)

if __name__ == "__main__": main()
