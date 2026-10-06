from datetime import datetime, timezone
import json
from Terminal.MT5_Sentinel import next_wakeup, atomic_json, last_record


def test_wakeup_is_strictly_next_utc_slot():
    assert next_wakeup(datetime(2026,10,6,7,14,0,tzinfo=timezone.utc)) == '2026-10-06T07:29:00+00:00'
    assert next_wakeup(datetime(2026,10,6,23,59,3,tzinfo=timezone.utc)) == '2026-10-07T00:14:00+00:00'


def test_atomic_state_and_incomplete_ledger_line(tmp_path):
    path=tmp_path/'state.json'; atomic_json(path,{'halted':True})
    assert json.loads(path.read_text())['halted']
    assert not list(tmp_path.glob('*.tmp'))
    ledger=tmp_path/'audit.jsonl'; ledger.write_text('{"slot":42}\n{"partial":')
    assert last_record(ledger)=={'slot':42}
