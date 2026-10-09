"""Refresh dated CPI/NFP/FOMC windows from BLS ICS and Fed monthly HTML."""
from __future__ import annotations
import argparse
import calendar
from datetime import datetime, timezone, timedelta
from pathlib import Path
import json
import math
import re
import urllib.request
from zoneinfo import ZoneInfo

BLS = "https://www.bls.gov/schedule/news_release/bls.ics"
FED = "https://www.federalreserve.gov/newsevents/{year}-{month}.htm"


def event_window_utc(event, default_pre=30, default_post=30):
    """Resolve explicit UTC windows or validated per-event minute buffers."""
    if not isinstance(event, dict):
        raise ValueError("calendar event must be an object")
    def stamp(value):
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return datetime.fromtimestamp(value, timezone.utc)
        result = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        if result.tzinfo is None:
            raise ValueError("calendar timestamp must include timezone")
        return result.astimezone(timezone.utc)

    def minutes(key, default):
        value = float(event.get(key, default))
        if isinstance(event.get(key), bool) or not math.isfinite(value) or not 0 <= value <= 240:
            raise ValueError(f"invalid {key}")
        return value

    when = stamp(event["time_utc"])
    pre = minutes("pre_blackout_m", default_pre)
    post = minutes("post_blackout_m", default_post)
    start = stamp(event["blackout_start_utc"]) if event.get("blackout_start_utc") else when - timedelta(minutes=pre)
    end = stamp(event["blackout_end_utc"]) if event.get("blackout_end_utc") else when + timedelta(minutes=post)
    if event.get("purge_at_utc"):
        start = min(start, stamp(event["purge_at_utc"]))
    if end <= start or not start <= when <= end:
        raise ValueError("invalid calendar blackout window")
    return when, start, end


def retain_supplemental_events(path, events, start, end):
    """A CPI/NFP/FOMC refresh must not erase verified supplemental releases."""
    try:
        previous = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        previous = {}
    def key(event):
        return event["name"], event_window_utc(event)[0]
    retained = {key(event): event for event in previous.get("events", [])}
    window_fields = ("currency", "currencies", "pre_blackout_m", "post_blackout_m",
                     "purge_at_utc", "blackout_start_utc", "blackout_end_utc")
    for event in events:
        old = retained.get(key(event), {})
        event.update({field: old[field] for field in window_fields if field in old})
        event.setdefault("currency", "USD")
        event.setdefault("pre_blackout_m", 30)
        event.setdefault("post_blackout_m", 30)
    core_names = {"CPI", "NFP", "FOMC", "FOMC Minutes", "FOMC Press Conference"}
    for event in retained.values():
        if event["name"] not in core_names and start <= key(event)[1] < end:
            if not str(event.get("source", "")).startswith("https://"):
                raise ValueError("supplemental macro event lacks source")
            events.append(event)
    return sorted(events, key=lambda event: key(event)[1])

def download(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (OMNI calendar refresh)"})
    with urllib.request.urlopen(request, timeout=5) as response: return response.read().decode("utf-8")

def parse_bls(text):
    text = re.sub(r"\r?\n[ \t]", "", text)
    events = []
    for block in text.split("BEGIN:VEVENT")[1:]:
        fields = {}
        for line in block.split("END:VEVENT")[0].splitlines():
            if ":" in line:
                key, value = line.split(":", 1); fields[key] = value
        title = fields.get("SUMMARY", "")
        name = "CPI" if "Consumer Price Index" in title else "NFP" if "Employment Situation" in title else None
        if name is None: continue
        stamps = [(k,v) for k,v in fields.items() if k.startswith("DTSTART")]
        if len(stamps) != 1: raise ValueError("BLS event lacks DTSTART")
        key, value = stamps[0]
        if value.endswith("Z"):
            stamp = datetime.strptime(value, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
        else:
            zone = key.split("TZID=")[-1] if "TZID=" in key else "America/New_York"
            if "Eastern" in zone: zone = "America/New_York"
            stamp = datetime.strptime(value, "%Y%m%dT%H%M%S").replace(tzinfo=ZoneInfo(zone)).astimezone(timezone.utc)
        events.append({"name": name, "time_utc": stamp.isoformat(), "impact": "HIGH", "source": BLS})
    if not events: raise ValueError("BLS calendar format changed or has no CPI/NFP dates")
    return events

def parse_fed(html, year, month, url):
    from lxml import html as parser
    document = parser.fromstring(html)
    headings = document.xpath('//h4[contains(normalize-space(.), "FOMC Meetings")]')
    if len(headings) != 1: raise ValueError("Fed calendar format changed: FOMC section missing")
    section = headings[0].getparent()
    events = []
    for node in section.itersiblings():
        if node.xpath('.//h4'): break
        for panel in node.xpath('.//div[contains(@class, "panel-body")]'):
            columns = panel.xpath('./div/div')
            if len(columns) != 3: continue
            title = " ".join(columns[1].itertext()).strip()
            if "FOMC" not in title: continue
            match = re.search(r'(\d+):(\d+)\s*([ap])\.m\.', " ".join(columns[0].itertext()), re.I)
            days = re.findall(r'\b\d{1,2}\b', " ".join(columns[2].itertext()))
            if not match or not days: raise ValueError("Fed event time/date unparseable")
            hour = int(match[1])%12 + (12 if match[3].lower()=="p" else 0)
            name = "FOMC Minutes" if "Minutes" in title else "FOMC Press Conference" if "Press Conference" in title and "FOMC Meeting" not in title else "FOMC"
            for day in days:
                stamp = datetime(year, month, int(day), hour, int(match[2]), tzinfo=ZoneInfo("America/New_York")).astimezone(timezone.utc)
                events.append({"name": name, "time_utc": stamp.isoformat(), "impact": "HIGH", "source": url})
    return events

def refresh_calendar(path, as_of=None, downloader=download):
    now = as_of or datetime.now(timezone.utc)
    bls = parse_bls(downloader(BLS))
    year, month = now.year, now.month
    months = [(year, month), (year+(month==12), 1 if month==12 else month+1)]
    events, covered_end = [], None
    for y,m in months:
        start = datetime(y,m,1,tzinfo=timezone.utc)
        end = datetime(y+(m==12),1 if m==12 else m+1,1,tzinfo=timezone.utc)
        releases = [e for e in bls if start <= datetime.fromisoformat(e["time_utc"]) < end]
        if not {"CPI", "NFP"}.issubset({e["name"] for e in releases}):
            if covered_end: break
            raise ValueError("BLS calendar lacks complete current-month CPI/NFP coverage")
        url = FED.format(year=y, month=calendar.month_name[m].lower())
        try: fed = parse_fed(downloader(url), y, m, url)
        except Exception:
            if covered_end: break
            raise
        events += releases+fed; covered_end=end
    coverage_start = datetime(year,month,1,tzinfo=timezone.utc)
    events = retain_supplemental_events(path, events, coverage_start, covered_end)
    result = {"schema": "omni.calendar.v1", "verified_at": now.isoformat(),
              "coverage_start": datetime(year,month,1,tzinfo=timezone.utc).isoformat(),
              "coverage_end": covered_end.isoformat(), "required_series": ["CPI","NFP","FOMC"],
              "events": events}
    try:
        previous = json.loads(Path(path).read_text(encoding="utf-8"))
        for field in ("supplemental_coverage_start", "supplemental_coverage_end", "verification_notes"):
            if field in previous:
                result[field] = previous[field]
    except (OSError, ValueError):
        pass
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix(".tmp");temporary.write_text(json.dumps(result,indent=2),encoding="utf-8");temporary.replace(path)
    return result

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",default=str(Path(__file__).resolve().parents[1]/"Data/macro_calendar.json"))
    args=parser.parse_args();print(json.dumps(refresh_calendar(args.output),indent=2))
