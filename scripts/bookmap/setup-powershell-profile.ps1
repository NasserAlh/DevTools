# Check if profile exists and create if it doesn't
if (!(Test-Path -Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
    Write-Host "Created new PowerShell profile at: $PROFILE"
}

# Add our functions to the profile
$profileContent = @'

# Bookmap Development Tools Functions
function New-BookmapProject {
    & "$env:USERPROFILE\OneDrive\DevTools\bin\create-bookmap-project.bat"
}
Set-Alias bookmap_proj New-BookmapProject

# Quick access to DevTools directory
function Open-DevTools {
    Start-Process "$env:USERPROFILE\OneDrive\DevTools"
}
Set-Alias odt Open-DevTools

# Add a comment to show when this was added
Write-Output "`n# Added Bookmap DevTools functions on $(Get-Date -Format 'yyyy-MM-dd')"
'@

# Add the content to the profile
Add-Content -Path $PROFILE -Value $profileContent

Write-Host "`nProfile updated successfully!"
Write-Host "Profile location: $PROFILE"
Write-Host "`nNew commands available after restarting PowerShell:"
Write-Host "- bookmap_proj : Creates new Bookmap project"
Write-Host "- odt : Opens DevTools directory"
Write-Host "`nWould you like to open the profile in Notepad to verify? (Y/N)"
$response = Read-Host
if ($response -eq 'Y') {
    notepad $PROFILE
}
