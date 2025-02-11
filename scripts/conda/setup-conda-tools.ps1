# Add conda cleanup function to PowerShell profile
$profileContent = @'

# Conda Environment Management
function Remove-CondaEnvironments {
    & python "$env:USERPROFILE\OneDrive\DevTools\scripts\conda\clean_envs.py"
}
Set-Alias conda-cleanup Remove-CondaEnvironments
'@

# Add the content to the PowerShell profile
Add-Content -Path $PROFILE -Value $profileContent

Write-Host "Conda cleanup tools have been added to your PowerShell profile."
Write-Host "You can now use the 'conda-cleanup' command to remove all conda environments except base."
Write-Host "Please restart PowerShell for the changes to take effect." 