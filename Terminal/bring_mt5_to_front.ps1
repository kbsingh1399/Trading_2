Add-Type -TypeDefinition @"
using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
public class WindowFinder {
    public delegate bool EnumWindowsProc(IntPtr hWnd, IntPtr lParam);
    [DllImport("user32.dll")]
    public static extern bool EnumWindows(EnumWindowsProc enumProc, IntPtr lParam);
    [DllImport("user32.dll")]
    public static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint lpdwProcessId);
    [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    public static extern int GetWindowText(IntPtr hWnd, System.Text.StringBuilder lpString, int nMaxCount);
    [DllImport("user32.dll")]
    public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
    [DllImport("user32.dll")]
    public static extern bool SetForegroundWindow(IntPtr hWnd);

    public static List<Tuple<IntPtr, uint, string>> FindWindowsForProcess(uint targetPid) {
        var list = new List<Tuple<IntPtr, uint, string>>();
        EnumWindows((hWnd, lParam) => {
            uint pid;
            GetWindowThreadProcessId(hWnd, out pid);
            if (pid == targetPid) {
                var sb = new System.Text.StringBuilder(256);
                GetWindowText(hWnd, sb, 256);
                list.Add(new Tuple<IntPtr, uint, string>(hWnd, pid, sb.ToString()));
            }
            return true;
        }, IntPtr.Zero);
        return list;
    }
}
"@

$procs = Get-Process terminal64 -ErrorAction SilentlyContinue
if (-not $procs) {
    Write-Host "MT5 not running. Starting..."
    Start-Process "C:\Program Files\MetaTrader 5\terminal64.exe"
    Start-Sleep -Seconds 3
    $procs = Get-Process terminal64 -ErrorAction SilentlyContinue
}

foreach ($p in $procs) {
    Write-Host "Checking PID: $($p.Id)"
    $wins = [WindowFinder]::FindWindowsForProcess($p.Id)
    foreach ($w in $wins) {
        Write-Host "Window Handle: $($w.Item1) Title: '$($w.Item3)'"
        if ($w.Item3 -and $w.Item3.Length -gt 0) {
            [WindowFinder]::ShowWindow($w.Item1, 3) # SW_MAXIMIZE
            [WindowFinder]::SetForegroundWindow($w.Item1)
            Write-Host "SUCCESS: Brought '$($w.Item3)' to foreground and maximized!"
        }
    }
}
