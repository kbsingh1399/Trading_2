#!/usr/bin/env python3
"""
Hyperdash & Hyperliquid Historical Data Downloader CLI
Bulk-downloads historical OHLCV candles, historical funding rates,
and liquidation profiles across any of the 234 assets on Hyperdash.
"""

import sys
import argparse
import pathlib

root_dir = pathlib.Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from Terminal.Api_Client import HyperdashClient
from rich.console import Console
from rich.table import Table

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Hyperdash Bulk Historical Data Downloader")
    parser.add_argument("--coin", type=str, default="BTC", help="Asset ticker (e.g. BTC, ETH, SOL) or 'ALL'")
    parser.add_argument("--timeframe", type=str, default="15m", choices=["1m", "5m", "15m", "1h", "4h", "1d"], help="Candle timeframe")
    parser.add_argument("--days", type=int, default=30, help="Number of historical days to download")
    parser.add_argument("--outdir", type=str, default="Data/Hyperdash_Historical", help="Output directory for Parquet files")
    parser.add_argument("--funding-only", action="store_true", help="Download only funding rate history")
    parser.add_argument("--candles-only", action="store_true", help="Download only candle history")

    args = parser.parse_args()
    client = HyperdashClient()

    console.print(f"[bold bright_cyan]HYPERDASH HISTORICAL DATA DOWNLOADER[/bold bright_cyan]")
    console.print(f"Target: [bold yellow]{args.coin}[/bold yellow] | Timeframe: [bold green]{args.timeframe}[/bold green] | Lookback: [bold magenta]{args.days} days[/bold magenta]")

    assets = client.fetch_all_assets()
    target_coins = []

    if args.coin.upper() == "ALL":
        target_coins = [a["coin"] for a in assets]
        console.print(f"[yellow]Downloading for ALL {len(target_coins)} active perpetual assets![/yellow]")
    else:
        target_coins = [args.coin.upper()]

    table = Table(title="DOWNLOAD SUMMARY", box=None)
    table.add_column("Symbol", style="bold bright_cyan")
    table.add_column("Candles File", style="green")
    table.add_column("Funding File", style="magenta")
    table.add_column("Status", justify="center")

    for coin in target_coins:
        c_path = "Skipped"
        f_path = "Skipped"
        status = "[green]SUCCESS[/green]"

        try:
            if not args.funding_only:
                c_path = client.download_historical_candles(coin, interval=args.timeframe, days=args.days, output_dir=args.outdir)
            if not args.candles_only:
                f_path = client.download_historical_funding(coin, days=args.days, output_dir=args.outdir)
        except Exception as e:
            status = f"[red]FAIL ({e})[/red]"

        table.add_row(coin, str(c_path), str(f_path), status)

    console.print(table)
    console.print(f"\n[bold bright_green]All downloads saved to '{args.outdir}'.[/bold bright_green]")

if __name__ == "__main__":
    main()
