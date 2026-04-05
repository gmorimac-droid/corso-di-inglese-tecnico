param(
    [string]$Root = ".\docs",
    [switch]$WhatIf = $false,
    [switch]$CreateBackup = $true
)

$ErrorActionPreference = "Stop"

$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$Utf8 = [System.Text.Encoding]::UTF8
$Cp1252 = [System.Text.Encoding]::GetEncoding(1252)

function Get-SuspiciousScore {
    param([string]$Text)

    $score = 0
    foreach ($ch in $Text.ToCharArray()) {
        $code = [int][char]$ch
        if ($code -eq 195 -or $code -eq 194 -or $code -eq 226 -or $code -eq 65533) {
            $score++
        }
    }
    return $score
}

function Read-FileUtf8 {
    param([string]$Path)
    $bytes = [System.IO.File]::ReadAllBytes($Path)
    return $Utf8.GetString($bytes)
}

function Write-FileUtf8NoBom {
    param(
        [string]$Path,
        [string]$Content
    )
    [System.IO.File]::WriteAllText($Path, $Content, $Utf8NoBom)
}

function Repair-MojibakeOnce {
    param([string]$Text)
    $bytes = $Cp1252.GetBytes($Text)
    return $Utf8.GetString($bytes)
}

function Repair-Text {
    param([string]$Text)

    $current = $Text
    $beforeScore = Get-SuspiciousScore -Text $current

    if ($beforeScore -eq 0) {
        return $current
    }

    for ($i = 0; $i -lt 3; $i++) {
        $candidate = Repair-MojibakeOnce -Text $current
        $candidateScore = Get-SuspiciousScore -Text $candidate

        if ($candidateScore -lt $beforeScore) {
            $current = $candidate
            $beforeScore = $candidateScore
        }
        else {
            break
        }
    }

    return $current
}

function Process-File {
    param([System.IO.FileInfo]$File)

    $original = Read-FileUtf8 -Path $File.FullName
    $fixed = Repair-Text -Text $original

    $fixed = $fixed.Replace([string][char]160, " ")

    $changed = ($fixed -ne $original)

    if ($changed) {
        if ($CreateBackup) {
            $backupPath = "$($File.FullName).bak"
            if (-not (Test-Path -LiteralPath $backupPath)) {
                Copy-Item -LiteralPath $File.FullName -Destination $backupPath
            }
        }

        if (-not $WhatIf) {
            Write-FileUtf8NoBom -Path $File.FullName -Content $fixed
        }
    }

    return [PSCustomObject]@{
        File      = $File.FullName
        Changed   = $changed
        Backup    = $CreateBackup
        Simulated = [bool]$WhatIf
    }
}

if (-not (Test-Path -LiteralPath $Root)) {
    throw "Path not found: $Root"
}

$files = Get-ChildItem -Path $Root -Filter *.md -File -Recurse

if (-not $files -or $files.Count -eq 0) {
    Write-Host "No Markdown files found under $Root" -ForegroundColor Yellow
    exit 0
}

Write-Host "Found $($files.Count) Markdown files under $Root" -ForegroundColor Cyan

$results = foreach ($file in $files) {
    Process-File -File $file
}

$changedFiles = $results | Where-Object { $_.Changed }

Write-Host ""
Write-Host "Summary" -ForegroundColor Cyan
Write-Host "-------"
Write-Host "Scanned files : $($results.Count)"
Write-Host "Changed files : $($changedFiles.Count)"
Write-Host "WhatIf mode   : $([bool]$WhatIf)"
Write-Host ""

if ($changedFiles.Count -gt 0) {
    Write-Host "Changed files:" -ForegroundColor Green
    $changedFiles | ForEach-Object {
        Write-Host " - $($_.File)"
    }
}
else {
    Write-Host "No files required changes." -ForegroundColor Yellow
}