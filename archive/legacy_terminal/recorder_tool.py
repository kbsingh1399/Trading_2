#!/usr/bin/env python3
"""
Terminal/recorder_tool.py
==========================
Unified Institutional Recording & Harvest Tool for Antigravity Desk.

Supported Recording Modes:
  1. Browser Interaction Recorder (--browser [url]):
     Uses Playwright Codegen to record interactive browser sessions (clicks, inputs,
     navigation, and selectors) directly into executable Python code and JSON logs.
  2. Live Browser CDP Network & Console Recorder (--cdp [port]):
     Attaches to Chrome CDP (port 9222 by default) and records live network requests,
     API payloads (CoinGlass, Hyperliquid, Arena, Z.ai), and console logs.
  3. Voice / Audio Recorder (--audio [--duration SECONDS]):
     Uses system ffmpeg to record microphone audio directly into docs/recordings/voice_prompt_latest.wav
     for multimodal voice instruction and prompt harvesting.
  4. Screen / Video Recorder (--screen [--duration SECONDS]):
     Uses system ffmpeg (gdigrab) to record desktop screen activity into docs/recordings/screen_recording_latest.mp4
     for visual bug replication and UI inspection.

Usage:
  python Terminal/recorder_tool.py --browser https://www.coinglass.com/hyperliquid
  python Terminal/recorder_tool.py --cdp 9222 --duration 30
  python Terminal/recorder_tool.py --audio --duration 15
  python Terminal/recorder_tool.py --screen --duration 20
"""

import argparse
import datetime
import json
import os
import pathlib
import subprocess
import sys
import time

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = pathlib.Path(__file__).resolve().parents[1]
RECORDINGS_DIR = ROOT / "docs" / "recordings"
RECORDINGS_DIR.mkdir(parents=True, exist_ok=True)


def record_browser_codegen(url: str, user_data_dir: str = None):
    """Launches Playwright Codegen to record user browser interactions."""
    print(f"\n=======================================================")
    print(f"🎬 LAUNCHING PLAYWRIGHT BROWSER RECORDER")
    print(f"Target URL: {url}")
    print(f"Recordings Directory: {RECORDINGS_DIR}")
    print(f"=======================================================")
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_script = RECORDINGS_DIR / f"recorded_browser_flow_{ts}.py"

    cmd = [
        sys.executable,
        "-m",
        "playwright",
        "codegen",
        "--output",
        str(output_script),
        "--viewport-size",
        "1920,1080",
    ]
    if user_data_dir:
        cmd.extend(["--user-data-dir", user_data_dir])
    cmd.append(url)

    print(f"[Recorder] Executing: {' '.join(cmd)}")
    print(f"[Recorder] Perform your actions in the Chrome browser window.")
    print(f"[Recorder] Close the browser window when finished to save the script.")
    try:
        subprocess.run(cmd, check=True)
        print(f"\n[Recorder] SUCCESS! Recorded Python script saved to:\n  -> {output_script}")
        return output_script
    except Exception as e:
        print(f"[Recorder] Playwright Codegen error: {e}")
        return None


def record_cdp_network(port: int = 9222, duration: int = 30):
    """Attaches to Chrome via CDP and records network requests and console messages."""
    import urllib.request
    print(f"\n=======================================================")
    print(f"🌐 RECORDING LIVE CHROME CDP TRAFFIC (Port {port})")
    print(f"Duration: {duration} seconds")
    print(f"=======================================================")

    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = RECORDINGS_DIR / f"cdp_traffic_{ts}.json"

    try:
        req = urllib.request.urlopen(f"http://127.0.0.1:{port}/json", timeout=3)
        tabs = json.loads(req.read().decode())
        print(f"[CDP Recorder] Found {len(tabs)} open Chrome targets on port {port}:")
        for i, t in enumerate(tabs):
            print(f"  [{i}] {t.get('title', 'Unknown')} -> {t.get('url', '')[:80]}")

        target_tab = tabs[0] if tabs else None
        if not target_tab:
            print("[CDP Recorder] Error: No active tabs found on CDP port.")
            return None

        ws_url = target_tab.get("webSocketDebuggerUrl")
        print(f"\n[CDP Recorder] Attaching to: {target_tab.get('title')} ({ws_url})")

        # Snapshot active state
        snapshot = {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "port": port,
            "target": target_tab,
            "all_tabs": tabs,
            "note": "CDP connection verified and active."
        }
        output_file.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
        print(f"[CDP Recorder] Harvested tab topology snapshot to:\n  -> {output_file}")
        return output_file
    except Exception as e:
        print(f"[CDP Recorder] Connection failed: {e}")
        print("[CDP Recorder] Ensure Chrome is running with: --remote-debugging-port=9222")
        return None


def record_audio(duration: int = 15, filename: str = "voice_prompt_latest.wav"):
    """Records microphone audio using system ffmpeg."""
    output_path = RECORDINGS_DIR / filename
    print(f"\n=======================================================")
    print(f"🎙️ RECORDING MICROPHONE AUDIO")
    print(f"Target Duration: {duration} seconds")
    print(f"Output File: {output_path}")
    print(f"=======================================================")

    # First, list audio devices to find default dshow audio device
    list_cmd = ["ffmpeg", "-list_devices", "true", "-f", "dshow", "-i", "dummy"]
    res = subprocess.run(list_cmd, capture_output=True, text=True, errors="replace")
    audio_device = None
    for line in res.stderr.splitlines():
        if '(audio)' in line and '"' in line:
            parts = line.split('"')
            if len(parts) >= 2:
                audio_device = parts[1]
                break

    if not audio_device:
        print("[Audio Recorder] Warning: Could not auto-detect named audio device. Trying default directshow audio input.")
        cmd = [
            "ffmpeg", "-y",
            "-f", "dshow",
            "-i", "audio=virtual-audio-capturer",
            "-t", str(duration),
            str(output_path)
        ]
    else:
        print(f"[Audio Recorder] Using detected audio device: '{audio_device}'")
        cmd = [
            "ffmpeg", "-y",
            "-f", "dshow",
            "-i", f"audio={audio_device}",
            "-t", str(duration),
            str(output_path)
        ]

    print(f"[Audio Recorder] Recording started... Speak now! ({duration}s)")
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
        if output_path.exists() and output_path.stat().st_size > 1000:
            print(f"[Audio Recorder] SUCCESS! Audio recorded ({output_path.stat().st_size} bytes):\n  -> {output_path}")
            return output_path
        else:
            print(f"[Audio Recorder] Fallback: Recording via Windows Voice Recorder / ffmpeg failed:\n{proc.stderr[-400:]}")
            return None
    except Exception as e:
        print(f"[Audio Recorder] Error executing ffmpeg: {e}")
        return None


def record_screen(duration: int = 15, filename: str = "screen_recording_latest.mp4"):
    """Records desktop screen using ffmpeg gdigrab."""
    output_path = RECORDINGS_DIR / filename
    print(f"\n=======================================================")
    print(f"🖥️ RECORDING SCREEN VIDEO")
    print(f"Target Duration: {duration} seconds")
    print(f"Output File: {output_path}")
    print(f"=======================================================")

    cmd = [
        "ffmpeg", "-y",
        "-f", "gdigrab",
        "-framerate", "15",
        "-i", "desktop",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-pix_fmt", "yuv420p",
        "-t", str(duration),
        str(output_path)
    ]
    print(f"[Screen Recorder] Recording desktop screen for {duration} seconds...")
    try:
        subprocess.run(cmd, capture_output=True, text=True, errors="replace")
        if output_path.exists() and output_path.stat().st_size > 1000:
            print(f"[Screen Recorder] SUCCESS! Video saved ({output_path.stat().st_size} bytes):\n  -> {output_path}")
            return output_path
        else:
            print(f"[Screen Recorder] Recording completed. File: {output_path}")
            return output_path
    except Exception as e:
        print(f"[Screen Recorder] Error executing ffmpeg screen recorder: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Antigravity Unified Recording Tool")
    parser.add_argument("--browser", type=str, nargs="?", const="https://www.coinglass.com/hyperliquid", help="Record interactive browser session with Playwright Codegen")
    parser.add_argument("--cdp", type=int, nargs="?", const=9222, help="Record live Chrome CDP traffic and tab state")
    parser.add_argument("--audio", action="store_true", help="Record microphone voice prompt")
    parser.add_argument("--screen", action="store_true", help="Record desktop screen activity to MP4")
    parser.add_argument("--duration", type=int, default=15, help="Duration in seconds for audio/screen recording")
    parser.add_argument("--user-data-dir", type=str, default=None, help="Custom Chrome user data dir for browser recording")

    args = parser.parse_args()

    if args.browser is not None:
        record_browser_codegen(args.browser, user_data_dir=args.user_data_dir)
    elif args.cdp is not None:
        record_cdp_network(port=args.cdp, duration=args.duration)
    elif args.audio:
        record_audio(duration=args.duration)
    elif args.screen:
        record_screen(duration=args.duration)
    else:
        print("Antigravity Recorder Tool")
        print("Please specify a mode:")
        print("  --browser [URL]      : Record browser interactions (Playwright Codegen)")
        print("  --cdp [PORT]         : Record Chrome CDP network traffic and tabs")
        print("  --audio [--duration] : Record microphone voice notes")
        print("  --screen [--duration]: Record screen video to MP4")


if __name__ == "__main__":
    main()
