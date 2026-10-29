Get-CimInstance Win32_Process | Where-Object { $_.Name -match "python" } | ForEach-Object { "$($_.ProcessId): $($_.CommandLine)" }
