"""
Terminal/web2api_council.py
Institutional Auxiliary Quantitative Council Client for Gemini Web2API (Endogen Architecture).

Connects to http://127.0.0.1:8081/v1/chat/completions (Bearer sk-gemini).
Provides zero-token auxiliary model opinions from Gemini 3.6 Flash / Gemini 3.5 Flash Thinking.
Saves complete responses to docs/trade_plans/GEMINI_WEB2API_LATEST_RAW.md
"""

import argparse
import datetime
import json
import pathlib
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_PROMPT_FILE = ROOT / "docs" / "trade_plans" / "LATEST_COUNCIL_CYCLE_PROMPT.txt"
OUTPUT_FILE = ROOT / "docs" / "trade_plans" / "GEMINI_WEB2API_LATEST_RAW.md"
STATUS_FILE = ROOT / "Data" / "web2api_completion_status.json"

WEB2API_URL = "http://127.0.0.1:8081/v1/chat/completions"
API_KEY = "sk-gemini"

def query_web2api(prompt: str, model: str = "gemini-3.6-flash", timeout: int = 180) -> str:
    # Sanitize '@' to prevent triggering Gemini Web Workspace extension mentions (e.g. @Gmail, @Drive)
    clean_prompt = prompt.replace("@[", "[").replace("@c:\\", "c:\\").replace("@C:\\", "C:\\").replace("@", "")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": clean_prompt
            }
        ]
    }
    
    print(f"[Web2API Council] Sending prompt ({len(clean_prompt)} chars) to {WEB2API_URL} (Model: {model})...", flush=True)
    req = urllib.request.Request(WEB2API_URL, data=json.dumps(payload).encode("utf-8"), headers=headers)
    
    start_t = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        if resp.status != 200:
            raise RuntimeError(f"Web2API returned status code {resp.status}")
        data = json.loads(resp.read().decode("utf-8"))
        elapsed = time.time() - start_t
        
        choices = data.get("choices", [])
        if not choices:
            raise RuntimeError("Web2API returned 0 choices")
        
        content = choices[0].get("message", {}).get("content", "")
        print(f"[Web2API Council] Received response ({len(content)} chars) in {elapsed:.1f}s", flush=True)
        return content

def run_web2api_council(prompt_path: pathlib.Path = DEFAULT_PROMPT_FILE, model: str = "gemini-3.6-flash") -> int:
    if not prompt_path.exists():
        print(f"[Web2API Council] Error: Prompt file {prompt_path} not found.", file=sys.stderr)
        return 1
    
    prompt = prompt_path.read_text(encoding="utf-8")
    try:
        response_text = query_web2api(prompt, model=model)
    except Exception as e:
        print(f"[Web2API Council] Request failed: {e}", file=sys.stderr)
        return 1
    
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(response_text, encoding="utf-8")
    print(f"[Web2API Council] Saved response to {OUTPUT_FILE}")
    
    status_payload = {
        "completed_at_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "completed_at_epoch": time.time(),
        "model": model,
        "prompt_chars": len(prompt),
        "response_chars": len(response_text),
        "output_path": str(OUTPUT_FILE)
    }
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATUS_FILE.write_text(json.dumps(status_payload, indent=2), encoding="utf-8")
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default=str(DEFAULT_PROMPT_FILE), help="Path to prompt text file")
    parser.add_argument("--model", default="gemini-3.6-flash", help="Web2API model name")
    args = parser.parse_args()
    
    exit_code = run_web2api_council(pathlib.Path(args.file), model=args.model)
    sys.exit(exit_code)
