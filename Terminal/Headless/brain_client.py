"""Arena Brain client - the cloud side of the link (OX_ALPHA_61 D1/D2).

The brain NEVER holds broker credentials and NEVER talks to the broker. It
sends signed command envelopes to the laptop over Pathway A (Cloudflare
Tunnel -> HeadlessService) or publishes them to a JSON store for Pathway C
(the laptop's RemoteCommandReconciler polls them).

    from Terminal.Headless.brain_client import BrainClient
    brain = BrainClient("https://<tunnel-id>.trycloudflare.com", os.environ["OMNI_API_SECRET"])
    result = brain.stage_test_limit(symbol="XAUUSD.pi", direction="SHORT",
                                    limit_price=4182.00, volume=0.01, atr=4.1)
    brain.modify_sltp(ticket=18576872, sl=4169.50)

CLI (for manual verification):
    python -m Terminal.Headless.brain_client --url https://... --stage-test-limit \
        --symbol XAUUSD.pi --direction SHORT --price 4182.00 --volume 0.01 --atr 4.1
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from typing import Dict, List, Optional

from Terminal.Execution.remote_reconciler import (new_command, sign_command,
                                                  purge_expired_test_limits,
                                                  TEST_LIMIT_COMMENT)

DEFAULT_TIMEOUT = 10.0


class BrainClient:
    """Signed HTTP client for the laptop's HeadlessService command routes."""

    def __init__(self, base_url: str, secret: str, *, timeout: float = DEFAULT_TIMEOUT,
                 clock=time.time):
        self.base_url = str(base_url).rstrip("/")
        self.secret = str(secret)
        self.timeout = float(timeout)
        self.clock = clock

    # ------------------------------------------------------------- plumbing
    def _post(self, path: str, command: Dict) -> Dict:
        signed = sign_command(command, self.secret)
        request = urllib.request.Request(self.base_url + path,
                                         data=json.dumps(signed).encode("utf-8"),
                                         method="POST",
                                         headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read() or b"{}")
        except urllib.error.HTTPError as exc:
            body = exc.read()
            try:
                return {"http_status": exc.code, **json.loads(body or b"{}")}
            except ValueError:
                return {"http_status": exc.code, "error": body.decode("utf-8", "replace")}
        except (urllib.error.URLError, OSError) as exc:
            return {"http_status": 0, "error": f"tunnel_unreachable:{exc}"}

    def _command(self, type_: str, params: Dict) -> Dict:
        return new_command(type_, params, ts=self.clock())

    # ------------------------------------------------------------- commands
    def stage_test_limit(self, *, symbol: str, direction: str, limit_price: float,
                         volume: float, atr: Optional[float] = None,
                         magic: int = 100895) -> Dict:
        """Stage the ARENA:TEST_LIMIT_v1 verification order (D2)."""
        params = {"symbol": symbol, "direction": direction,
                  "limit_price": float(limit_price), "volume": float(volume),
                  "magic": int(magic)}
        if atr is not None:
            params["atr"] = float(atr)
        return self._post("/api/v1/stage_order", self._command("STAGE_TEST_LIMIT", params))

    def stage_order(self, *, symbol: str, direction: str, volume: float,
                    limit_price: float, sl: float, tp: float,
                    comment: str = "ARENA:ORDER") -> Dict:
        """Stage a generic signed limit order (risk <= 20.00 USD enforced laptop-side)."""
        return self._post("/api/v1/stage_order", self._command("STAGE_ORDER", {
            "symbol": symbol, "direction": direction, "volume": float(volume),
            "limit_price": float(limit_price), "sl": float(sl), "tp": float(tp),
            "comment": comment}))

    def modify_sltp(self, *, ticket: int, sl: float, tp: Optional[float] = None) -> Dict:
        return self._post("/api/v1/modify_sltp", self._command("MODIFY_SLTP", {
            "ticket": int(ticket), "sl": float(sl), "tp": tp}))

    def cancel_order(self, *, ticket: int) -> Dict:
        return self._post("/api/v1/cancel_order", self._command("CANCEL_ORDER", {
            "ticket": int(ticket)}))

    def evaluate_candle(self, *, force: bool = False, secret: Optional[str] = None) -> Dict:
        """Pull one evaluation payload (signed with the envelope wrapper)."""
        from Terminal.Headless.server import sign_payload
        secret = secret or self.secret
        envelope = sign_payload({"force": bool(force)}, secret, ts=self.clock())
        request = urllib.request.Request(
            self.base_url + "/api/v1/evaluate_candle",
            data=json.dumps(envelope["payload"]).encode("utf-8"), method="POST",
            headers={"Content-Type": "application/json",
                     "X-Signature": envelope["signature"],
                     "X-Signature-Ts": f"{envelope['ts']:.3f}"})
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read() or b"{}")
        except urllib.error.HTTPError as exc:
            return {"http_status": exc.code, "error": exc.read().decode("utf-8", "replace")}
        except (urllib.error.URLError, OSError) as exc:
            return {"http_status": 0, "error": f"tunnel_unreachable:{exc}"}

    def status(self) -> Dict:
        """Fetch muscle health (signed): bridge, pillars, quality, last evaluation."""
        from Terminal.Headless.server import sign_payload
        envelope = sign_payload({}, self.secret, ts=self.clock())
        request = urllib.request.Request(
            self.base_url + "/api/v1/status",
            data=json.dumps(envelope["payload"]).encode("utf-8"), method="POST",
            headers={"Content-Type": "application/json",
                     "X-Signature": envelope["signature"],
                     "X-Signature-Ts": f"{envelope['ts']:.3f}"})
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read() or b"{}")
        except urllib.error.HTTPError as exc:
            return {"http_status": exc.code, "error": exc.read().decode("utf-8", "replace")}
        except (urllib.error.URLError, OSError) as exc:
            return {"http_status": 0, "error": f"tunnel_unreachable:{exc}"}

    def purge_test_limits(self) -> Dict:
        return self._post("/api/v1/stage_order", self._command("PURGE_TEST_LIMITS", {}))


# ------------------------------------------------------------- pathway C
def publish_to_gist(commands: List[Dict], *, gist_id: str, token: Optional[str] = None,
                    filename: str = "arena_commands.json") -> Dict:
    """Publish signed command envelopes to a GitHub Gist (Pathway C store).

    The gist is secret-side (never public); the laptop pulls the raw URL with
    its own read access. Sign BEFORE publishing - signatures cover the full
    envelope, the gist is only a transport."""
    token = token or os.environ.get("GIST_TOKEN", "")
    if not token:
        raise ValueError("gist_token_required:GIST_TOKEN")
    if not commands:
        raise ValueError("no_commands")
    payload = {"files": {filename: {"content": json.dumps(
        {"commands": commands}, indent=2)}}}
    request = urllib.request.Request(
        f"https://api.github.com/gists/{gist_id}",
        data=json.dumps(payload).encode("utf-8"), method="PATCH",
        headers={"Authorization": f"Bearer {token}",
                 "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.loads(response.read() or b"{}")


def gist_raw_url(gist_id: str, filename: str = "arena_commands.json") -> str:
    return f"https://gist.githubusercontent.com/arena/{gist_id}/raw/{filename}"


def _main(argv=None):
    import argparse
    parser = argparse.ArgumentParser(description="Arena Brain command client")
    parser.add_argument("--url", default=os.environ.get("ARENA_TUNNEL_URL", ""))
    parser.add_argument("--secret", default=os.environ.get("OMNI_API_SECRET", ""))
    parser.add_argument("--stage-test-limit", action="store_true")
    parser.add_argument("--purge", action="store_true")
    parser.add_argument("--symbol", default="XAUUSD.pi")
    parser.add_argument("--direction", default="SHORT")
    parser.add_argument("--price", type=float, default=4182.00)
    parser.add_argument("--volume", type=float, default=0.01)
    parser.add_argument("--atr", type=float, default=None)
    args = parser.parse_args(argv)
    if not args.url or not args.secret:
        parser.error("--url (ARENA_TUNNEL_URL) and --secret (OMNI_API_SECRET) required")
    brain = BrainClient(args.url, args.secret)
    if args.purge:
        print(json.dumps(brain.purge_test_limits(), indent=2, default=str))
        return
    if args.stage_test_limit:
        result = brain.stage_test_limit(symbol=args.symbol, direction=args.direction,
                                        limit_price=args.price, volume=args.volume,
                                        atr=args.atr)
        print(json.dumps(result, indent=2, default=str))
        print(f"comment tag: {TEST_LIMIT_COMMENT} (auto-purged after 24 bars / 6h)")


if __name__ == "__main__":
    _main()
