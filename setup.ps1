# ----------------------------
# setup.ps1
# ----------------------------

# Initialize Git
git init

# Create .gitignore if it doesn't exist
if (-Not (Test-Path .gitignore)) {
    @"
.venv/
__pycache__/
"@ | Out-File -Encoding UTF8 .gitignore
}

# Initialize uv environment
uv init

# Add initial dependencies (edit as needed)
$deps = @("numpy")  # add your common starter libs
foreach ($dep in $deps) {
    uv add $dep
}

# Lock dependencies
uv lock

$today = Get-Date -Format "yyyy-MM-dd"

$readmeText = @"

Project initialized on $today

All needed commands are in commands.txt

"@

if (Test-Path README.md) {
    Add-Content -Encoding UTF8 README.md $readmeText
} else {
    Set-Content -Encoding UTF8 README.md $readmeText
}

Write-Host "Project setup complete!"
