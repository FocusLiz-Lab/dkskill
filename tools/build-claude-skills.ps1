param(
  [string]$OutputDir = ".\claude-dist"
)

$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $PSScriptRoot
$Python = "python"
$Script = Join-Path $PSScriptRoot "build-skills.py"

& $Python $Script --root $Root --out $OutputDir --claude
