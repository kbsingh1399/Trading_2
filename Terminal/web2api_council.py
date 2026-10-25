"""
Terminal/web2api_council.py
Institutional Auxiliary Quantitative Council Client for Gemini Web2API (Endogen Architecture).

Connects to http://127.0.0.1:8081/v1/chat/completions (Bearer sk-gemini).
Provides zero-token auxiliary model opinions from Gemini 3.7 Flash / Gemini 3.5 Flash Thinking.
Saves complete responses to docs/trade_plans/GEMINI_WEB2API_LATEST_RAW.md
"""

import argparse
import datetime
import json
import logging
import pathlib
import sys
import time
import urllib.request

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_PROMPT_FILE = ROOT / "docs" / "trade_plans" / "LATEST_COUNCIL_CYCLE_PROMPT.txt"
OUTPUT_FILE = ROOT / "docs" / "trade_plans" / "GEMINI_WEB2API_LATEST_RAW.md"
STATUS_FILE = ROOT / "Data" / "web2api_completion_status.json"
LOG_FILE = ROOT / "Data" / "web2api_council.log"

WEB2API_URL = "http://127.0.0.1:8081/v1/chat/completions"
API_KEY = "sk-gemini"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][Web2APICouncil] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8")
    ]
)
logger = logging.getLogger("Web2APICouncil")


def sanitize_prompt_for_gemini_web(prompt: str) -> str:
    """
    Sanitizes prompt to eliminate characters that trigger Google Workspace extensions
    (e.g., @Gmail, @Drive, @Docs) or malformed regex triggers in Gemini Web reverse proxy.
    """
    cleaned = prompt.replace("@[", "[").replace("@c:\\", "c:\\").replace("@C:\\", "C:\\")
    cleaned = cleaned.replace("@", "")
    return cleaned


def query_web2api(prompt: str, model: str = "gemini-3.8-flash", timeout: int = 180) -> str:
    clean_prompt = sanitize_prompt_for_gemini_web(prompt)
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
    
    logger.info("Sending prompt (%d chars) to %s (Model: %s)...", len(clean_prompt), WEB2API_URL, model)
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
        logger.info("Received response (%d chars) in %.1fs", len(content), elapsed)
        return content


def run_web2api_council(prompt_path: pathlib.Path = DEFAULT_PROMPT_FILE, model: str = "gemini-3.8-flash") -> int:
    if not prompt_path.exists():
        logger.error("Prompt file %s not found.", prompt_path)
        return 1
    
    prompt = prompt_path.read_text(encoding="utf-8")
    try:
        response_text = query_web2api(prompt, model=model)
    except Exception as e:
        logger.error("Request failed: %s", e)
        return 1
    
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(response_text, encoding="utf-8")
    logger.info("Saved response to %s", OUTPUT_FILE)
    
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
    parser.add_argument("--model", default="gemini-3.8-flash", help="Web2API model name")
    args = parser.parse_args()
    
    exit_code = run_web2api_council(pathlib.Path(args.file), model=args.model)
    sys.exit(exit_code)

