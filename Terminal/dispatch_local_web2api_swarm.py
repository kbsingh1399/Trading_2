#!/usr/bin/env python3
"""
Terminal/dispatch_local_web2api_swarm.py
Concurrently dispatches the 4 local quantitative subagent prompts
(Statistical Regime, Microstructure, Solvency, Clock Provenance)
to the local Gemini Web2API proxy (http://localhost:8081) using gemini-3.7-flash / gemini-3.8-flash.
Saves outputs to Data/subagent_outputs/cycle_{cycle_id}_role_{a,b,c,d}.json.
Saves 100% of Antigravity context tokens while delivering deep quantitative output!
"""

import json
import pathlib
import sys
import time
import urllib.request
import re
import concurrent.futures

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROMPTS_DIR = ROOT / "Data" / "subagent_prompts"
OUTPUTS_DIR = ROOT / "Data" / "subagent_outputs"
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

WEB2API_URL = "http://localhost:8081/v1/chat/completions"
MODEL = "gemini-3.7-flash"

def sanitize_prompt(text: str) -> str:
    """Removes @ mentions to avoid triggering Gemini Web Google Workspace extension errors."""
    text = re.sub(r'@\[(.*?)\]', r'[Skill: \1]', text)
    text = text.replace('@', '')
    return text

def dispatch_single_role(role_key: str, prompt_file: pathlib.Path, cycle_id: str):
    if not prompt_file.exists():
        return role_key, {"error": f"Prompt file {prompt_file} not found"}
    
    prompt_text = sanitize_prompt(prompt_file.read_text(encoding="utf-8"))
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": f"You are acting as {role_key.upper()} for {cycle_id} of the Blueberry Markets MT5 autonomous quant desk.\n"
                           f"Read and follow STANDARDIZED_TRADING_DECISION_CHAIN.md and AUTONOMOUS_WAKEUP_CHECKLIST.md strictly.\n\n"
                           f"{prompt_text}"
            }
        ]
    }
    
    start_time = time.time()
    req = urllib.request.Request(
        WEB2API_URL,
        headers={"Authorization": "Bearer sk-gemini", "Content-Type": "application/json"},
        data=json.dumps(payload).encode("utf-8")
    )
    
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            content = data["choices"][0]["message"]["content"]
            elapsed = time.time() - start_time
            out_path = OUTPUTS_DIR / f"cycle_{cycle_id}_{role_key}.json"
            out_path.write_text(content, encoding="utf-8")
            return role_key, {"status": "SUCCESS", "elapsed": round(elapsed, 2), "chars": len(content), "path": str(out_path)}
    except Exception as e:
        return role_key, {"status": "ERROR", "error": str(e), "elapsed": round(time.time() - start_time, 2)}

def run_swarm(cycle_id: str = "Cycle 357"):
    roles = ["role_a", "role_b", "role_c", "role_d"]
    # Look for files matching cycle_id
    tasks = {}
    for r in roles:
        # Check possible filename patterns
        f1 = PROMPTS_DIR / f"cycle_{cycle_id}_{r}.txt"
        f2 = PROMPTS_DIR / f"cycle_357_{r}.txt"
        chosen = f1 if f1.exists() else f2
        tasks[r] = chosen
    
    print(f"[Web2APISwarm] Concurrently dispatching 4 roles for {cycle_id} using {MODEL}...")
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_map = {executor.submit(dispatch_single_role, r, p, cycle_id): r for r, p in tasks.items()}
        for future in concurrent.futures.as_completed(future_map):
            r_key, res = future.result()
            results[r_key] = res
            print(f"  * {r_key}: {res.get('status')} ({res.get('chars', 0)} chars in {res.get('elapsed', 0)}s)")
    
    # Save swarm summary
    summary_path = OUTPUTS_DIR / f"swarm_summary_{cycle_id.replace(' ', '_')}.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"[Web2APISwarm] All roles completed. Summary saved to {summary_path}")

if __name__ == "__main__":
    cid = sys.argv[1] if len(sys.argv) > 1 else "Cycle 357"
    run_swarm(cid)
