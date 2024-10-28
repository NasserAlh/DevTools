# Read current profile content
$content = Get-Content -Path $PROFILE -Raw

# Replace the old alias with the new one
$updatedContent = $content -replace 'Set-Alias nbp New-BookmapProject', 'Set-Alias bookmap_proj New-BookmapProject'

# Write back to profile
$updatedContent | Set-Content -Path $PROFILE

Write-Host "Updated alias from 'nbp' to 'bookmap_proj'"
Write-Host "Please restart PowerShell for the changes to take effect"
