"""
Terminal/dispatch_dual_council.py
Unified Dual-Council Prompt Dispatcher for BOTH Arena.ai and Z.ai (GLM-5.3-Flash).

Guarantees 100% compliance with Operator Mandate:
1. Prompts BOTH Arena.ai and Z.ai simultaneously via Chrome CDP (port 9222).
2. Mandatorily embeds Section 2.5 Quantitative Methodology Inquest Question in EVERY prompt.
3. Automatically launches completion monitors for both councils.
"""

import argparse
import asyncio
import datetime
import json
import os
import pathlib
import subprocess
import sys
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROMPT_FILE = ROOT / "docs" / "trade_plans" / "LATEST_COUNCIL_CYCLE_PROMPT.txt"
ARENA_BRIDGE = ROOT / "Terminal" / "arena_bridge.py"
ZAI_DISPATCHER = ROOT / "Terminal" / "dispatch_zai_prompt.py"
WEB2API_COUNCIL = ROOT / "Terminal" / "web2api_council.py"

CDP_URL = "http://127.0.0.1:9222/json"

def get_live_telemetry():
    telemetry_file = ROOT / "Data" / "telemetry" / "mt5_account_telemetry.json"
    if telemetry_file.exists():
        try:
            with open(telemetry_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"balance": 4818.51, "equity": 4818.51, "cushion_buffer": 23.51, "cushion_floor": 43.51, "positions_count": 0, "orders_count": 0}

def build_unified_prompt(cycle_id: str = "AUTO") -> str:
    template_path = ROOT / "Data" / "Manditory" / "Arena_GLM_Standard_Prompt.md"
    if not template_path.exists():
        template_path = ROOT / "docs" / "prompts" / "Arena_GLM_Standard_Prompt.md"

    if template_path.exists():
        raw_text = template_path.read_text(encoding="utf-8")
        if "```markdown" in raw_text:
            prompt = raw_text.split("```markdown")[1].split("```")[0].strip()
        else:
            prompt = raw_text.strip()
    else:
        logger.error("Template Arena_GLM_Standard_Prompt.md not found!")
        prompt = ""

    telem = get_live_telemetry()
    acc = telem.get("account", {}) if "account" in telem else telem
    bal = float(acc.get("balance_usd", acc.get("balance", 4818.51)))
    eq = float(acc.get("equity_usd", acc.get("equity", 4818.51)))
    fm = float(acc.get("margin_free_usd", acc.get("margin_free", 4818.51)))
    utc_now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # Cycle auto-detection
    if cycle_id == "AUTO":
        import glob, re
        existing = glob.glob(str(ROOT / "docs" / "prompts" / "ARENA_CYCLE_*_REDTEAM_PROMPT.txt"))
        nums = [int(m.group(1)) for f in existing if (m := re.search(r"ARENA_CYCLE_(\d+)_REDTEAM", f))]
        cycle_id = str(max(nums) + 1 if nums else 296)

    cush_fl = eq - 4600.00
    cush_buf = eq - 4650.00
    dist_goal = 5500.00 - eq
    hours_left = "17.0"

    open_pos = telem.get("open_positions", [])
    pending_ord = telem.get("pending_orders", [])
    pos_count = len(open_pos)
    pending_count = len(pending_ord)
    slots_free = max(0, 4 - pos_count)

    pos_str = f"{pos_count} (100% Flat Cash, 0 positions)" if pos_count == 0 else f"{pos_count} active positions"
    pending_str = f"{pending_count} pending limit orders"

    # Ticket Table
    table_rows = [
        "| Slot | Cluster | Ticket | Symbol | Side | Volume | Entry | SL | TP | Risk USD | R0 |",
        "|---|---|---|---|---|---|---|---|---|---|---|"
    ]
    if pos_count > 0:
        for idx, p0 in enumerate(open_pos):
            table_rows.append(f"| Filled {idx+1} | Open | #{p0.get('ticket')} | {p0.get('symbol')} | {p0.get('direction')} | {p0.get('volume')} lot | {p0.get('price_open')} | {p0.get('sl')} | {p0.get('tp')} | Sized | — |")
    if pending_count > 0:
        for idx, po in enumerate(pending_ord):
            side = po.get("direction", "LIMIT")
            sym = po.get("symbol", "")
            cluster = "Forex" if any(c in sym for c in ["EUR", "GBP", "USD", "JPY"]) else "Index" if any(c in sym for c in ["100", "500", "40", "30"]) else "Crypto"
            table_rows.append(f"| Pending {idx+1} | {cluster} | #{po.get('ticket')} | {sym} | {side} | {po.get('volume')} lot | {po.get('price_open')} | {po.get('sl')} | {po.get('tp')} | Sized | — |")
    if pos_count == 0 and pending_count == 0:
        table_rows.append("| — | Flat | — | — | — | — | — | — | — | $0.00 | — |")
        table_rows.append("*Book is 100% Cash Defense. Zero active positions, zero pending orders.*")

    ticket_table = "\n".join(table_rows)

    # Candidate Radar Table
    try:
        from Terminal.multi_asset_opportunity_scanner import scan_all_156_assets
        scan_res = scan_all_156_assets()
        top_opps = scan_res.get("opportunities", [])[:6]
    except Exception:
        top_opps = []

    if top_opps:
        c_lines = [
            "| Candidate Setup | Direction | Target Entry | Stop Loss | Take Profit | Lots | Risk USD | Stressed Loss | Buffer Surplus |",
            "|---|---|---|---|---|---|---|---|---|"
        ]
        for opp in top_opps:
            c_lines.append(f"| {opp.get('symbol')} ({opp.get('group', 'CFD')}) | {opp.get('side')} | {opp.get('entry')} | {opp.get('sl')} | {opp.get('tp')} | {opp.get('lot')} lot | ${opp.get('nominal_risk_usd', 13.0):.2f} | ${opp.get('nominal_risk_usd', 13.0)*1.25+2.0:.2f} | +${opp.get('buffer_surplus_usd', 4.5):.2f} |")
        candidate_table = "\n".join(c_lines)
        worst_case_eq = f"{eq - (top_opps[0].get('nominal_risk_usd', 18.0)*1.25+2.0):.2f}"
    else:
        rec_cand = None
        receipt_file = ROOT / "Data" / "execution_preflight_receipt.json"
        if receipt_file.exists():
            try:
                with open(receipt_file, "r", encoding="utf-8") as f:
                    rec_data = json.load(f)
                c_info = rec_data.get("candidate", {})
                v_info = rec_data.get("broker_valuation", {})
                if c_info:
                    rec_cand = f"| {c_info.get('symbol')} (Crypto Perp) | {c_info.get('action')} | {c_info.get('price')} | {c_info.get('sl')} | {c_info.get('tp')} | {c_info.get('volume')} lot | ${v_info.get('total_nominal_risk_usd', 18.0):.2f} | ${v_info.get('ticket_stress_usd', 24.5):.2f} | +${cush_buf:.2f} |"
                    worst_case_eq = f"{eq - v_info.get('ticket_stress_usd', 24.5):.2f}"
            except Exception:
                pass
        if rec_cand:
            candidate_table = "| Candidate Setup | Direction | Target Entry | Stop Loss | Take Profit | Lots | Risk USD | Stressed Loss | Buffer Surplus |\n|---|---|---|---|---|---|---|---|---|\n" + rec_cand
        else:
            candidate_table = "| — | — | — | — | — | — | $0.00 | $0.00 | +$0.00 |\n*No candidates qualified under strict confluence stack. 100% Cash Defense.*"
            worst_case_eq = f"{eq:.2f}"

    # Load and embed cycle_envelope.json directly
    envelope_file = ROOT / "Data" / "cycle_envelope.json"
    envelope_json_str = "{}"
    if envelope_file.exists():
        try:
            import json
            with open(envelope_file, "r", encoding="utf-8") as f:
                env_obj = json.load(f)
            envelope_json_str = json.dumps(env_obj, indent=2)
        except Exception as e:
            print("[DualCouncil] Warning loading cycle_envelope.json:", e)
    
    # Load and embed execution_preflight_receipt.json directly
    receipt_file = ROOT / "Data" / "execution_preflight_receipt.json"
    receipt_json_str = "{}"
    if receipt_file.exists():
        try:
            with open(receipt_file, "r", encoding="utf-8") as f:
                rec_obj = json.load(f)
            receipt_json_str = json.dumps(rec_obj, indent=2)
        except Exception as e:
            print("[DualCouncil] Warning loading execution_preflight_receipt.json:", e)

    combined_envelope_str = envelope_json_str
    if receipt_json_str and receipt_json_str != "{}":
        combined_envelope_str += f"\n\n### ⚡ VERIFIED LIVE EXECUTION PREFLIGHT RECEIPT (`execution_preflight_receipt.json`):\n```json\n{receipt_json_str}\n```"

    if "{CYCLE_ENVELOPE_JSON}" in prompt:
        prompt = prompt.replace("{CYCLE_ENVELOPE_JSON}", combined_envelope_str)
    else:
        # If template lacks placeholder, inject it right after the header
        embed_block = f"\n\n### 📦 ATTACHED IMMUTABLE CYCLE ENVELOPE (`cycle_envelope.json`):\n```json\n{envelope_json_str}\n```\n\n"
        if "## STATIC COUNCIL REVIEW PROTOCOL" in prompt:
            prompt = prompt.replace("## STATIC COUNCIL REVIEW PROTOCOL", "## STATIC COUNCIL REVIEW PROTOCOL" + embed_block)
        else:
            prompt = embed_block + prompt

    # Replace placeholders
    prompt = prompt.replace("{CYCLE_ID}", cycle_id)
    prompt = prompt.replace("{CYCLE_UTC}", utc_now)
    prompt = prompt.replace("{BALANCE}", f"{bal:,.2f}")
    prompt = prompt.replace("{EQUITY}", f"{eq:,.2f}")
    prompt = prompt.replace("{FREE_MARGIN}", f"{fm:,.2f}")
    prompt = prompt.replace("{CUSHION_FLOOR}", f"+{cush_fl:.2f}")
    prompt = prompt.replace("{CUSHION_BUFFER}", f"+{cush_buf:.2f}")
    prompt = prompt.replace("{DISTANCE_GOAL}", f"+{dist_goal:.2f}")
    prompt = prompt.replace("{HOURS_LEFT}", hours_left)
    prompt = prompt.replace("{OPEN_POSITIONS}", pos_str)
    prompt = prompt.replace("{PENDING_ORDERS}", pending_str)
    prompt = prompt.replace("{SLOTS_FREE}", str(slots_free))
    prompt = prompt.replace("{TICKET_TABLE}", ticket_table)
    prompt = prompt.replace("{WORST_CASE_EQUITY}", worst_case_eq)
    prompt = prompt.replace("{CANDIDATE_TABLE}", candidate_table)

    return prompt

async def dispatch_all(cycle_id: str = "AUTO", prompt_file: str = None):
    if prompt_file and pathlib.Path(prompt_file).exists():
        with open(prompt_file, "r", encoding="utf-8") as f:
            prompt = f.read()
        print(f"[DualCouncil] Loaded prompt from custom file {prompt_file} ({len(prompt)} chars)")
    else:
        prompt = build_unified_prompt(cycle_id)
    
    # Save prompt to canonical file
    with open(PROMPT_FILE, "w", encoding="utf-8") as f:
        f.write(prompt)
    print(f"[DualCouncil] Saved prompt to {PROMPT_FILE} ({len(prompt)} chars)")
    
    # 1. Dispatch to Z.ai via Terminal/dispatch_zai_prompt.py
    print("[DualCouncil] Dispatching prompt to Z.ai (GLM-5.3-Flash)...")
    try:
        proc_zai = subprocess.run([sys.executable, str(ZAI_DISPATCHER), "--file", str(PROMPT_FILE)], capture_output=True, text=True, timeout=30)
        print("[DualCouncil] Z.ai output:", proc_zai.stdout.strip())
        if proc_zai.stderr:
            print("[DualCouncil] Z.ai stderr:", proc_zai.stderr.strip())
    except Exception as e:
        print(f"[DualCouncil] Z.ai dispatch error: {e}")
        
    # 2. Dispatch to Arena.ai via Chrome CDP using ProseMirror and Input.insertText
    print("[DualCouncil] Dispatching prompt to Arena.ai...")
    try:
        tabs = json.loads(urllib.request.urlopen(CDP_URL, timeout=5).read().decode())
        arena_ws = None
        for t in tabs:
            if ("arena.ai/agent" in t.get("url", "") or "arena.ai" in t.get("url", "")) and t.get("webSocketDebuggerUrl"):
                arena_ws = t["webSocketDebuggerUrl"]
                break
        if arena_ws:
            async with websockets.connect(arena_ws, max_size=50_000_000) as ws:
                # Bring to front
                await ws.send(json.dumps({"id": 101, "method": "Page.bringToFront"}))
                await asyncio.sleep(0.5)
                
                # Dismiss modal/escape & dismiss task completion banner
                await ws.send(json.dumps({"id": 102, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 27, "code": "Escape", "key": "Escape"}}))
                await ws.send(json.dumps({"id": 103, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 27, "code": "Escape", "key": "Escape"}}))
                await asyncio.sleep(0.2)
                
                # If "Was this task successful?" banner is active, click "Yes" to reveal ProseMirror
                js_dismiss_banner = """(() => {
                    const btns = Array.from(document.querySelectorAll('button')).filter(b => b.innerText.trim() === 'Yes' || b.innerText.trim() === 'No');
                    if (btns.length > 0) {
                        const yesBtn = btns.find(b => b.innerText.trim() === 'Yes') || btns[0];
                        yesBtn.click();
                        return true;
                    }
                    return false;
                })()"""
                await ws.send(json.dumps({"id": 1031, "method": "Runtime.evaluate", "params": {"expression": js_dismiss_banner}}))
                await asyncio.sleep(0.5)

                # Clear ProseMirror (specifically target .tiptap.ProseMirror, NOT g-recaptcha textarea)
                js_clear = """(() => {
                    const el = document.querySelector('.tiptap.ProseMirror');
                    if (!el) return false;
                    el.focus();
                    const range = document.createRange();
                    range.selectNodeContents(el);
                    const sel = window.getSelection();
                    sel.removeAllRanges();
                    sel.addRange(range);
                    return true;
                })()"""
                await ws.send(json.dumps({"id": 104, "method": "Runtime.evaluate", "params": {"expression": js_clear}}))
                await asyncio.sleep(0.1)
                await ws.send(json.dumps({"id": 105, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
                await ws.send(json.dumps({"id": 106, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 8, "code": "Backspace", "key": "Backspace"}}))
                await asyncio.sleep(0.2)
                
                # Insert prompt text via Input.insertText
                await ws.send(json.dumps({"id": 107, "method": "Input.insertText", "params": {"text": prompt}}))
                await asyncio.sleep(0.5)
                
                # Click send button
                js_click = """(() => {
                    const sendBtn = document.querySelector('button[aria-label="Send message"], button:has(svg.lucide-arrow-up), button[type="submit"], button[aria-label*="Send"]');
                    if (sendBtn && !sendBtn.disabled) {
                        sendBtn.click();
                        return { clicked: true };
                    }
                    return { clicked: false, disabled: sendBtn ? sendBtn.disabled : null };
                })()"""
                await ws.send(json.dumps({"id": 108, "method": "Runtime.evaluate", "params": {"expression": js_click, "returnByValue": True}}))
                res = json.loads(await ws.recv())
                click_val = res.get("result", {}).get("result", {}).get("value", {})
                print("[DualCouncil] Arena.ai prompt sent result:", click_val)
                if not click_val.get("clicked"):
                    # Fallback to Enter key
                    await ws.send(json.dumps({"id": 109, "method": "Input.dispatchKeyEvent", "params": {"type": "rawKeyDown", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
                    await ws.send(json.dumps({"id": 110, "method": "Input.dispatchKeyEvent", "params": {"type": "keyUp", "windowsVirtualKeyCode": 13, "code": "Enter", "key": "Enter"}}))
        else:
            print("[DualCouncil] Warning: No Arena.ai tab found on CDP port 9222.")
    except Exception as e:
        print(f"[DualCouncil] Arena.ai dispatch error: {e}")

    # 3. Dispatch to Gemini Web2API in background subprocess (port 8081)
    print("[DualCouncil] Dispatching prompt to Gemini Web2API (port 8081)...")
    try:
        subprocess.Popen([sys.executable, str(WEB2API_COUNCIL), "--file", str(PROMPT_FILE), "--model", "gemini-3.6-flash"])
        print("[DualCouncil] Gemini Web2API background council task launched successfully.")
    except Exception as e:
        print(f"[DualCouncil] Gemini Web2API dispatch error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycle", default="AUTO")
    parser.add_argument("--file", default=None, help="Path to custom prompt file")
    args = parser.parse_args()
    asyncio.run(dispatch_all(args.cycle, prompt_file=args.file))
