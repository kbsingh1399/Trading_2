"""Signed headless microservice (OX_ALPHA_60 Deliverable 4.1).

A minimal, dependency-free async HTTP/1.1 server exposing:

  GET  /healthz              - liveness (process up; unsigned, for probes)
  GET  /readyz               - readiness (bridge + data quality; unsigned)
  POST /api/v1/evaluate_candle - runs one candle evaluation and returns the
                               Pioneer decision, orderflow conviction vector
                               and staged order tickets as SIGNED JSON

Signing: HMAC-SHA256 over ``ts + "." + canonical_json`` with a secret from
``OMNI_API_SECRET``. Responses carry ``X-Signature``/``X-Signature-Ts``;
requests to the evaluate endpoint must carry a valid signature themselves
(replay-window 30s) whenever a secret is configured. No secret configured =
local/unencrypted mode (still binds 0.0.0.0 for container probes).

The HTTP layer is deliberately tiny: fixed routes, hard limits (8 KB headers,
1 MB body), Connection: close. Everything substantive lives in the runtime,
which this service only calls.
"""
from __future__ import annotations

import asyncio
import hashlib
import hmac
import json
import time
from typing import Optional

from Terminal.Execution.remote_reconciler import (apply_command, verify_command,
                                                  purge_expired_test_limits)

MAX_HEADER_BYTES = 8192
MAX_BODY_BYTES = 1 << 20
REPLAY_WINDOW_SEC = 30.0


def canonical_json(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")


def sign_payload(payload, secret: str, ts: Optional[float] = None) -> dict:
    """Wrap a payload with its HMAC signature and timestamp."""
    ts = float(time.time() if ts is None else ts)
    body = canonical_json(payload)
    digest = hmac.new(secret.encode("utf-8"), f"{ts:.3f}".encode("utf-8") + b"." + body,
                      hashlib.sha256).hexdigest()
    return {"payload": payload, "ts": ts, "signature": digest}


def verify_signed(envelope: dict, secret: str, now: Optional[float] = None,
                  replay_window: float = REPLAY_WINDOW_SEC) -> bool:
    """Constant-time verification of a signed envelope."""
    if not isinstance(envelope, dict) or not secret:
        return False
    try:
        ts = float(envelope.get("ts", 0.0))
        if abs(float(now if now is not None else time.time()) - ts) > replay_window:
            return False
        body = canonical_json(envelope.get("payload"))
        expected = hmac.new(secret.encode("utf-8"), f"{ts:.3f}".encode("utf-8") + b"." + body,
                            hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected, str(envelope.get("signature", "")))
    except (TypeError, ValueError):
        return False


class HeadlessService:
    """Routes + signing around a HeadlessRuntime (or anything duck-compatible)."""

    def __init__(self, runtime, *, host: str = "0.0.0.0", port: int = 8080,
                 secret: Optional[str] = None, clock=time.time,
                 evaluate_timeout: float = 45.0):
        self.runtime = runtime
        self.host = host
        self.port = int(port)
        self.secret = secret or ""
        self.clock = clock
        self.evaluate_timeout = float(evaluate_timeout)
        self._server = None
        self._lock = asyncio.Lock()
        self._command_nonces = set()      # replay ledger for remote commands
        self._applied_commands = set()    # idempotency ledger

    # ------------------------------------------------------------- handlers
    def readiness(self) -> dict:
        try:
            ready, reasons = self.runtime.readiness()
            return {"ready": bool(ready), "reasons": list(reasons)}
        except Exception as exc:                      # noqa: BLE001 - probe isolation
            return {"ready": False, "reasons": [f"readiness_error:{exc!r}"]}

    async def _evaluate(self, body: dict) -> dict:
        force = bool((body or {}).get("force"))
        async with self._lock:                        # one evaluation at a time
            return await asyncio.wait_for(
                asyncio.to_thread(self.runtime.evaluate_candle, force=force),
                timeout=self.evaluate_timeout)

    def _dispatch(self, method: str, path: str, body: dict) -> tuple:
        if method == "GET" and path == "/healthz":
            return 200, {"ok": True, "service": "omni-headless", "ts": self.clock()}
        if method == "GET" and path == "/readyz":
            payload = self.readiness()
            return (200 if payload["ready"] else 503), payload
        return 404, {"error": "not_found", "path": path}

    # --------------------------------------------------------------- server
    async def handle(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        try:
            request = await asyncio.wait_for(reader.readline(), timeout=10.0)
            if not request:
                return
            parts = request.decode("latin-1").split()
            if len(parts) < 2:
                await self._respond(writer, 400, {"error": "bad_request_line"})
                return
            method, path = parts[0].upper(), parts[1].split("?")[0]
            headers = {}
            while True:
                line = await asyncio.wait_for(reader.readline(), timeout=10.0)
                if line in (b"\r\n", b"\n", b""):
                    break
                if sum(len(k) + len(v) for k, v in headers.items()) > MAX_HEADER_BYTES:
                    await self._respond(writer, 431, {"error": "headers_too_large"})
                    return
                key, _, value = line.decode("latin-1").partition(":")
                headers[key.strip().lower()] = value.strip()
            length = min(int(headers.get("content-length", "0") or 0), MAX_BODY_BYTES)
            raw = await reader.read(length) if length > 0 else b""
            body = {}
            if raw:
                try:
                    body = json.loads(raw)
                except ValueError:
                    await self._respond(writer, 400, {"error": "invalid_json"})
                    return

            if method == "POST" and path == "/api/v1/evaluate_candle":
                if self.secret:
                    try:
                        envelope = {"payload": body,
                                    "ts": float(headers.get("x-signature-ts", "0") or 0),
                                    "signature": headers.get("x-signature", "")}
                    except ValueError:
                        envelope = None
                    if not verify_signed(envelope, self.secret, now=self.clock()):
                        await self._respond(writer, 401, {"error": "invalid_signature"})
                        return
                try:
                    result = await self._evaluate(body)
                except asyncio.TimeoutError:
                    await self._respond(writer, 504, {"error": "evaluate_timeout"})
                    return
                except Exception as exc:              # noqa: BLE001 - service isolation
                    await self._respond(writer, 500, {"error": repr(exc)})
                    return
                await self._respond(writer, 200, result)
                return

            if method == "POST" and path == "/api/v1/market_state":
                # Live positions/orders/quotes/orderflow for the brain's
                # deliberation (OX_ALPHA_62). Signed envelope, read-only.
                if self.secret:
                    try:
                        envelope = {"payload": body,
                                    "ts": float(headers.get("x-signature-ts", "0") or 0),
                                    "signature": headers.get("x-signature", "")}
                    except ValueError:
                        envelope = None
                    if not verify_signed(envelope, self.secret, now=self.clock()):
                        await self._respond(writer, 401, {"error": "invalid_signature"})
                        return
                try:
                    assets = (body or {}).get("assets")
                    state = await asyncio.to_thread(self.runtime.market_state, assets)
                except Exception as exc:                  # noqa: BLE001 - probe isolation
                    state = {"service": "omni.headless.v1", "as_of": self.clock(),
                             "error": repr(exc)}
                await self._respond(writer, 200, state)
                return

            if method == "POST" and path == "/api/v1/status":
                # Muscle health for the brain (OX_ALPHA_61 follow-up): the
                # same signed-envelope discipline as evaluate_candle - the
                # brain proves itself before reading operational state.
                if self.secret:
                    try:
                        envelope = {"payload": body,
                                    "ts": float(headers.get("x-signature-ts", "0") or 0),
                                    "signature": headers.get("x-signature", "")}
                    except ValueError:
                        envelope = None
                    if not verify_signed(envelope, self.secret, now=self.clock()):
                        await self._respond(writer, 401, {"error": "invalid_signature"})
                        return
                try:
                    status = self.runtime.status()
                except Exception as exc:                  # noqa: BLE001 - probe isolation
                    status = {"service": "omni.headless.v1", "as_of": self.clock(),
                              "ready": False, "reasons": [f"status_error:{exc!r}"]}
                await self._respond(writer, 200, status)
                return

            if method == "POST" and path in ("/api/v1/stage_order",
                                             "/api/v1/modify_sltp",
                                             "/api/v1/cancel_order"):
                # Arena Brain -> laptop muscle command channel (OX_ALPHA_61).
                # The body IS a signed command envelope (protocol
                # omni.arena_remote.v1): HMAC-SHA256 + timestamp window +
                # single-use nonce + single-use command_id.
                if not self.secret:
                    await self._respond(writer, 503, {"error": "no_secret_configured"})
                    return
                verdict = verify_command(body, self.secret, now=self.clock(),
                                         seen_nonces=self._command_nonces,
                                         applied_ids=self._applied_commands)
                if not verdict["ok"]:
                    await self._respond(writer, 401, {"error": verdict["reason"]})
                    return
                bridge = getattr(self.runtime, "bridge", None)
                if bridge is None:
                    await self._respond(writer, 503, {"error": "no_bridge"})
                    return
                try:
                    result = await asyncio.wait_for(
                        asyncio.to_thread(apply_command, bridge, body,
                                          clock=self.clock,
                                          bars_provider=self._bars_provider()), 15.0)
                except asyncio.TimeoutError:
                    await self._respond(writer, 504, {"error": "command_timeout"})
                    return
                except Exception as exc:              # noqa: BLE001 - risk refusal
                    await self._respond(writer, 409, {"error": str(exc),
                                                      "command_id": body.get("command_id")})
                    return
                self._applied_commands.add(str(body.get("command_id")))
                await self._respond(writer, 200, {"command_id": body.get("command_id"),
                                                  "type": body.get("type"),
                                                  "result": result})
                return

            status, payload = self._dispatch(method, path, body)
            if isinstance(payload, tuple):            # pragma: no cover - defensive
                payload = {"error": "internal"}
            await self._respond(writer, status, payload)
        except (asyncio.TimeoutError, ConnectionError, asyncio.IncompleteReadError):
            return
        except Exception:                             # noqa: BLE001 - never crash the server
            try:
                await self._respond(writer, 500, {"error": "internal"})
            except Exception:                         # noqa: BLE001
                pass
        finally:
            try:
                writer.close()
            except Exception:                         # noqa: BLE001
                pass

    def _bars_provider(self):
        runtime = self.runtime
        def provider(symbol):
            bridge = getattr(runtime, "bridge", None)
            if bridge is None:
                return None
            try:
                return bridge.get_recent_bars(symbol, count=30)
            except Exception:                         # noqa: BLE001
                return None
        return provider

    async def _respond(self, writer, status: int, payload: dict):
        body = canonical_json(payload)
        headers = f"HTTP/1.1 {status} {'OK' if status == 200 else 'ERROR'}\r\n" \
                  f"Content-Type: application/json\r\n" \
                  f"Content-Length: {len(body)}\r\n" \
                  f"Connection: close\r\n"
        if self.secret and isinstance(payload, dict):
            envelope = sign_payload(payload, self.secret, ts=self.clock())
            headers += f"X-Signature: {envelope['signature']}\r\n" \
                       f"X-Signature-Ts: {envelope['ts']:.3f}\r\n"
        writer.write(headers.encode("latin-1") + b"\r\n" + body)
        await writer.drain()

    async def serve(self):
        self._server = await asyncio.start_server(self.handle, self.host, self.port)
        return self._server

    async def run(self):
        server = await self.serve()
        async with server:
            await server.serve_forever()
