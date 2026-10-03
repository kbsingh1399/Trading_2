"""
Terminal/__main__.py
Unified CLI entry point for the Parquet Quant Trading Terminal.

Usage:
  python -m Terminal                  # Launch native desktop terminal window
  python -m Terminal --web            # Launch modern browser-based trading terminal
  python -m Terminal --hyperdash       # Launch institutional live continuous Hyperdash terminal
  python -m Terminal --file <path>    # Load a specific parquet dataset immediately
"""
import sys
import argparse
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

def main():
    parser = argparse.ArgumentParser(description="Parquet Quant Trading Terminal")
    parser.add_argument("--file", "-f", type=str, default=None, help="Path to Parquet file to load")
    parser.add_argument("--web", "-w", action="store_true", help="Launch web trading terminal in browser")
    parser.add_argument("--hyperdash", "-hd", action="store_true", help="Launch live continuous Hyperdash terminal")
    parser.add_argument("--coin", "-c", type=str, default="BTC", help="Initial coin for Hyperdash terminal (default: BTC)")
    parser.add_argument("--port", "-p", type=int, default=8090, help="Port for web trading terminal (default: 8090)")
    parser.add_argument("--bars", "-b", type=int, default=1000, help="Initial number of bars to render (default: 1000)")
    
    args = parser.parse_args()
    
    if args.hyperdash:
        from Terminal.Hyperdash_Terminal import HyperdashTerminal
        term = HyperdashTerminal(default_coin=args.coin)
        term.run()
    elif args.web:
        from Terminal.Web_Terminal import start_server
        start_server(port=args.port, auto_open=True)
    else:
        from Terminal.Desktop_App import DesktopQuantTerminal
        app = DesktopQuantTerminal(initial_file=args.file, max_bars=args.bars)
        app.run()

if __name__ == '__main__':
    main()
