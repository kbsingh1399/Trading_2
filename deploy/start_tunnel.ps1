# ============================================================================
# OX_ALPHA_61 - Laptop "muscle" side setup (Windows PowerShell, run as Admin)
# Zero open router ports: an outbound-only Cloudflare quick tunnel.
# ============================================================================

# 1) One-time: install cloudflared (winget) ---------------------------------
#    winget install --id Cloudflare.cloudflared

# 2) Configure the secret (32+ random bytes, base64). The SAME secret goes in
#    the Arena brain environment (OMNI_API_SECRET). Never commit it.
$secret = [Convert]::ToBase64String((1..32 | ForEach-Object { Get-Random -Max 256 }))
Write-Host "OMNI_API_SECRET=$secret" -ForegroundColor Yellow
Write-Host "Set this exact value in BOTH environments before continuing." -ForegroundColor Yellow
Read-Host "Press Enter after the secret is set on both sides"

# 3) Start the headless service (the laptop keeps MT5 terminal64.exe running;
#    EXECUTION_BACKEND=native_mt5 is fail-closed: no terminal, no trading).
$env:EXECUTION_BACKEND = "native_mt5"
$env:OMNI_API_SECRET = $secret
$env:OMNI_ASSETS = "BTC,ETH,SOL,GOLD"
$env:OMNI_ALLOW_PAPER = "0"
$service = Start-Process -FilePath "python" -ArgumentList "-m", "Terminal.Headless" `
    -WorkingDirectory $PSScriptRoot\.. -PassThru -WindowStyle Minimized
Write-Host "Headless service PID $($service.Id) on 0.0.0.0:8080"

# 4) Start the quick tunnel (no account, no config, outbound-only). The
#    printed https://<id>.trycloudflare.com URL is the ARENA_TUNNEL_URL.
Write-Host "Starting Cloudflare quick tunnel (outbound-only, zero open ports)..."
cloudflared tunnel --url http://127.0.0.1:8080

# 5) Verify bidirectional control from the Arena side (brain machine):
#    python -m Terminal.Headless.brain_client --url <ARENA_TUNNEL_URL> `
#        --stage-test-limit --symbol XAUUSD.pi --direction SHORT `
#        --price 4182.00 --volume 0.01
#    -> stages ARENA:TEST_LIMIT_v1 (risk <= 10.00 USD, 6h auto-purge).
#
# 6) Pathway C fallback (tunnel down): the laptop runs the reconciler loop
#    polling a secret GitHub Gist:
#    python -c "from Terminal.Execution.remote_reconciler import RemoteCommandReconciler, gist_fetch; import os; RemoteCommandReconciler(bridge, secret=os.environ['OMNI_API_SECRET'], fetch=lambda: gist_fetch(os.environ['ARENA_GIST_URL'])).run_forever()"
#    The brain publishes with Terminal.Headless.brain_client.publish_to_gist.
