<#
.SYNOPSIS
  Download the NAM Starter Pack presets: amp/pedal captures and IRs, one folder per preset.

.DESCRIPTION
  Reads presets\presets.json and downloads every file a preset uses into
  <Destination>\Presets\<preset name>\, numbered in signal-chain order, with a Recipe.txt
  describing the chain. -Full also downloads the whole library (~1,250 files) into
  <Destination>\Library\ using the same folder layout PiPedal uses.

.EXAMPLE
  powershell -ExecutionPolicy Bypass -File .\windows\Get-NamStarterPack.ps1
.EXAMPLE
  powershell -ExecutionPolicy Bypass -File .\windows\Get-NamStarterPack.ps1 -Full
#>
param(
    [string]$Destination = (Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'NAM Starter Pack'),
    [switch]$Full
)
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'   # Invoke-WebRequest is very slow with the progress bar on
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$repo = Split-Path -Parent $PSScriptRoot
$presets = Get-Content -Raw -Encoding UTF8 (Join-Path $repo 'presets/presets.json') | ConvertFrom-Json
$cache = Join-Path $Destination '.cache'
[void][IO.Directory]::CreateDirectory($cache)
$script:ok = 0; $script:skipped = 0; $script:failed = 0

function Get-File([string]$Url, [string]$Target) {
    if ((Test-Path -LiteralPath $Target) -and (Get-Item -LiteralPath $Target).Length -gt 0) { $script:skipped++; return }
    # Several presets share files, so fetch each URL once and copy it from the cache.
    $cached = Join-Path $cache (Split-Path -Leaf $Url)
    if (-not (Test-Path -LiteralPath $cached)) {
        for ($try = 1; $try -le 3; $try++) {
            try { Invoke-WebRequest -UseBasicParsing -Uri $Url -OutFile $cached -TimeoutSec 120; break }
            catch {
                Remove-Item -LiteralPath $cached -ErrorAction SilentlyContinue
                if ($try -eq 3) { Write-Warning "FAILED: $Target ($Url)"; $script:failed++; return }
                Start-Sleep -Seconds 2
            }
        }
    }
    [void][IO.Directory]::CreateDirectory((Split-Path -Parent $Target))
    Copy-Item -LiteralPath $cached -Destination $Target
    $script:ok++
}

foreach ($p in $presets) {
    $dir = Join-Path (Join-Path $Destination 'Presets') $p.folder
    Write-Host "$($p.name)"
    $recipe = @("$($p.name)   [$($p.bank)]", '')
    foreach ($s in $p.steps) {
        if ($s.url) {
            $local = '{0} {1} - {2}' -f $s.n, $s.kind, $s.file
            Get-File $s.url (Join-Path $dir $local)
            $recipe += '{0}. {1,-8} {2}' -f $s.n, $s.kind, $local
            $recipe += "           -> $($s.where); $($s.notes)"
        } else {
            $recipe += '{0}. {1,-8} {2}: {3}' -f $s.n, $s.kind, $s.where, $s.notes
        }
    }
    [void][IO.Directory]::CreateDirectory($dir)
    Set-Content -LiteralPath (Join-Path $dir 'Recipe.txt') -Value $recipe -Encoding UTF8
}

if ($Full) {
    $dirs = @{ amp = 'NeuralAmpModels/T3K Starter Pack'; pedal = 'NeuralAmpModels/T3K Pedals';
               cab = 'CabIR/T3K Starter Pack'; rev = 'ReverbImpulseFiles/T3K Starter Pack' }
    Get-ChildItem (Join-Path $repo 'manifests/manifest*.tsv') | ForEach-Object {
        Write-Host "Library: $($_.Name)"
        Get-Content -Encoding UTF8 $_.FullName | Where-Object { $_ } | ForEach-Object {
            $kind, $title, $name, $url = $_ -split "`t"
            Get-File $url (Join-Path $Destination "Library/$($dirs[$kind])/$title/$name")
        }
    }
}

Write-Host ''
Write-Host "downloaded=$($script:ok) already-there=$($script:skipped) failed=$($script:failed)"
Write-Host "Presets are in: $(Join-Path $Destination 'Presets')"
if ($script:failed -gt 0) { Write-Host 'Run the script again to retry the failed files.' }
