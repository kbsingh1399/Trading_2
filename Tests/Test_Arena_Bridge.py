"""Council dispatch preserves provenance and records advice without inventing state."""
import subprocess

import pytest

from Terminal import arena_bridge as arena


def test_lean_prompt_uses_canonical_links_without_local_account_fallback(monkeypatch, tmp_path):
    monkeypatch.setattr(arena, "TELEMETRY_SNAPSHOT", tmp_path / "missing.json")
    monkeypatch.setattr(subprocess, "check_output", lambda *args, **kwargs: "source-head")
    prompt = arena.build_48h_orderflow_prompt()
    assert "https://raw.githubusercontent.com/kbsingh1399/Trading_2/main/docs/telemetry/live_snapshot_latest.json" in prompt
    assert "arena/537c1eb8-trading-2" in prompt
    assert "MODEL 1" in prompt and "MODEL 2" in prompt and "ALL 24 assets" in prompt
    assert "PASSIVE LIMIT ORDERS ONLY" in prompt and "4,795.00" in prompt
    assert "generation_id" in prompt and "UNAVAILABLE" in prompt
    assert "capacity" in prompt and "pending_orders" in prompt
    assert len(prompt) < 16_000
    for invented_fact in ("4,896.55", "4,851.98", "100% Cash Flat", "768 verified", "Mirrored 1:1", "+0.3279R"):
        assert invented_fact not in prompt


@pytest.mark.parametrize("done", [False, True])
def test_cycle_journal_records_only_completed_advice(done, monkeypatch, tmp_path):
    monkeypatch.setattr(arena, "PROJECT_ROOT", tmp_path)
    desk = tmp_path / "docs" / "trade_plans" / "LIVE_COLLABORATIVE_ORDER_DESK.md"
    desk.parent.mkdir(parents=True)
    desk.write_text("## Section 1: Existing record\n", encoding="utf-8")
    before = desk.read_text(encoding="utf-8")
    async def dismiss():
        return True
    async def post(prompt):
        return True
    response = "PUNCH NONE " + "Observed evidence requires independent review. " * 3
    async def check():
        return done, response
    monkeypatch.setattr(arena, "dismiss_arena_popup", dismiss)
    monkeypatch.setattr(arena, "post_prompt_to_arena", post)
    monkeypatch.setattr(arena, "check_arena_response", check)
    monkeypatch.setattr(arena, "build_48h_orderflow_prompt", lambda: "linked council prompt")
    monkeypatch.setattr(arena.time, "sleep", lambda delay: None)
    assert arena.run_full_15m_cycle() == (done, response)
    content = desk.read_text(encoding="utf-8")
    if done:
        assert response in content and "Council Advice" in content
        assert "remain unverified" in content
        assert "4,813.99" not in content and "100% Cash Flat" not in content
        assert "Action Taken" not in content and "Exactly 1 Slot" not in content
    else:
        assert content == before
