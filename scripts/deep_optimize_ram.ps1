# Deep RAM & Process Optimization Utility

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   SYSTEM RAM & APPLICATION DEEP OPTIMIZATION PROTOCOL    " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 0. Initial RAM Status
$osInitial = Get-CimInstance Win32_OperatingSystem
$totalGB = [math]::Round($osInitial.TotalVisibleMemorySize / 1MB, 2)
$freeInitialGB = [math]::Round($osInitial.FreePhysicalMemory / 1MB, 2)
$usedInitialGB = [math]::Round(($osInitial.TotalVisibleMemorySize - $osInitial.FreePhysicalMemory) / 1MB, 2)
$pctInitial = [math]::Round(($usedInitialGB / $totalGB) * 100, 1)

Write-Host "BEFORE OPTIMIZATION:" -ForegroundColor Yellow
Write-Host "  Total RAM: $totalGB GB | Used: $usedInitialGB GB ($pctInitial%) | Free: $freeInitialGB GB" -ForegroundColor White

# 1. Close Requested User Applications (Chrome, Office, etc. - NEVER EDGE)
$targetAppNames = @(
    'chrome',
    # 'msedge', <-- EXPLICIT OPERATOR DIRECTIVE: DO NOT FLUSH OR CLOSE MICROSOFT EDGE
    'brave',
    'firefox',
    'opera',
    'excel',
    'winword',
    'powerpnt',
    'acrobat',
    'acrord32',
    'slack',
    'teams',
    'discord',
    'spotify',
    'telegram',
    'notion'
)

$closedReport = @()

foreach ($appName in $targetAppNames) {
    $procs = Get-Process -Name $appName -ErrorAction SilentlyContinue
    if ($procs) {
        $count = $procs.Count
        $memMB = [math]::Round(($procs | Measure-Object -Property WorkingSet64 -Sum).Sum / 1MB, 1)
        $procs | ForEach-Object { Stop-Process -Id $_.Id -Force -ErrorAction SilentlyContinue }
        Write-Host "  [CLOSED] $appName ($count instances, freed ~$memMB MB)" -ForegroundColor Green
        $closedReport += [PSCustomObject]@{
            Application = $appName
            Instances = $count
            MemoryFreedMB = $memMB
        }
    }
}

# 2. Prune Zombie / Orphaned Background Node & Python Workers
$zombieNodes = Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'node.exe' -and ($_.CommandLine -match 'npx-cli\.js' -or $_.CommandLine -match 'jest') }
if ($zombieNodes) {
    $zombieNodes | ForEach-Object {
        Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue
        Write-Host "  [PRUNED] Zombie Node worker PID $($_.ProcessId)" -ForegroundColor Yellow
    }
}

$duplicateWatchers = Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'python.exe' -and $_.CommandLine -match 'code_review_graph' }
if ($duplicateWatchers) {
    $duplicateWatchers | ForEach-Object {
        Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue
        Write-Host "  [PRUNED] Duplicate graph watcher PID $($_.ProcessId)" -ForegroundColor Yellow
    }
}

# 3. NT Native Working Set Trimming & Standby Cache Flushing
$ntCode = @"
using System;
using System.Runtime.InteropServices;

public class NativeMemoryOptimizer {
    [DllImport("psapi.dll")]
    public static extern int EmptyWorkingSet(IntPtr hwProc);
    
    [DllImport("ntdll.dll")]
    public static extern UInt32 NtSetSystemInformation(int InfoClass, IntPtr Info, int Length);

    public static void TrimWorkingSet(int pid) {
        try {
            using (var proc = System.Diagnostics.Process.GetProcessById(pid)) {
                EmptyWorkingSet(proc.Handle);
            }
        } catch {}
    }

    public static void PurgeStandbyList() {
        int[] commands = new int[] { 1, 2, 3, 4 };
        foreach (int cmd in commands) {
            try {
                int c = cmd;
                GCHandle handle = GCHandle.Alloc(c, GCHandleType.Pinned);
                NtSetSystemInformation(80, handle.AddrOfPinnedObject(), Marshal.SizeOf(c));
                handle.Free();
            } catch {}
        }
    }
}
"@

if (-not ([System.Management.Automation.PSTypeName]'NativeMemoryOptimizer').Type) {
    Add-Type -TypeDefinition $ntCode -ErrorAction SilentlyContinue
}

Write-Host "  Trimming working sets across all active processes (preserving Edge)..." -ForegroundColor Cyan
Get-Process | Where-Object { $_.WorkingSet64 -gt 10MB -and $_.ProcessName -notmatch 'msedge' } | ForEach-Object {
    [NativeMemoryOptimizer]::TrimWorkingSet($_.Id)
}

Write-Host "  Flushing Windows Standby memory list & garbage collection..." -ForegroundColor Cyan
[NativeMemoryOptimizer]::PurgeStandbyList()
[System.GC]::Collect()

Start-Sleep -Milliseconds 800

# 4. Final RAM Status & Savings
$osFinal = Get-CimInstance Win32_OperatingSystem
$freeFinalGB = [math]::Round($osFinal.FreePhysicalMemory / 1MB, 2)
$usedFinalGB = [math]::Round(($osFinal.TotalVisibleMemorySize - $osFinal.FreePhysicalMemory) / 1MB, 2)
$pctFinal = [math]::Round(($usedFinalGB / $totalGB) * 100, 1)

$reclaimedGB = [math]::Round($freeFinalGB - $freeInitialGB, 2)

Write-Host "`nAFTER OPTIMIZATION:" -ForegroundColor Green
Write-Host "  Total RAM:     $totalGB GB" -ForegroundColor White
Write-Host "  Used RAM:      $usedFinalGB GB ($pctFinal% used)" -ForegroundColor White
Write-Host "  Free RAM:      $freeFinalGB GB" -ForegroundColor Green
Write-Host "  RAM Reclaimed: $reclaimedGB GB" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
