# Bookmap Development Tools

## Overview
Tools for creating and managing Bookmap Java projects, with automatic setup and easy access commands.

## Quick Start
- Run `bookmap_proj` from PowerShell (recommended)
- Or run `create-bookmap-project` from any terminal

## Directory Structure
```
%USERPROFILE%\OneDrive\DevTools\
    ├── scripts\
    │   └── bookmap\
    │       ├── create_project.py
    │       └── README.md
    ├── templates\
    │   └── bookmap\
    └── bin\
        └── create-bookmap-project.bat
```

## Location
- Main script: `~/OneDrive/DevTools/scripts/bookmap/create_project.py`
- Batch file: `~/OneDrive/DevTools/bin/create-bookmap-project.bat`
- PowerShell profile scripts: `~/OneDrive/DevTools/scripts/powershell/`

## Requirements
- Python 3.x
- Java JDK 21
- Maven
- OneDrive configured and synced
- PowerShell (for enhanced functionality)

## Initial Setup

### 1. Directory Structure Setup
```batch
@echo off
mkdir "%USERPROFILE%\OneDrive\DevTools"
mkdir "%USERPROFILE%\OneDrive\DevTools\scripts"
mkdir "%USERPROFILE%\OneDrive\DevTools\scripts\bookmap"
mkdir "%USERPROFILE%\OneDrive\DevTools\templates"
mkdir "%USERPROFILE%\OneDrive\DevTools\templates\bookmap"
mkdir "%USERPROFILE%\OneDrive\DevTools\bin"
```
Save as `setup-devtools.bat` and run.

### 2. PowerShell Profile Setup
```powershell
# Save as setup-profile.ps1 and run in PowerShell as Administrator
if (!(Test-Path -Path $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE -Force
}

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
'@

Add-Content -Path $PROFILE -Value $profileContent
```

### 3. Enable Script Execution
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Usage

### PowerShell Commands
- `bookmap_proj` - Create new Bookmap project
- `odt` - Open DevTools directory

### Manual Method
1. Open command prompt or PowerShell
2. Type `create-bookmap-project`
3. Follow the prompts

## Project Features
- Maven-based Java project structure
- Bookmap API dependencies pre-configured
- Template files included
- Automatic JAR deployment to Bookmap addons directory

## Profile Locations
- PowerShell 5.1: `%USERPROFILE%\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1`
- PowerShell 7+: `%USERPROFILE%\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`

## Maintenance

### View/Edit Profile
```powershell
# Using Notepad
notepad $PROFILE

# Using VS Code
code $PROFILE
```

### Update PATH
Ensure `%USERPROFILE%\OneDrive\DevTools\bin` is in your system PATH.

## Troubleshooting

### Common Issues
1. Script not found:
   - Check OneDrive sync status
   - Verify PATH environment variable
   - Ensure all directories exist

2. PowerShell commands not working:
   - Restart PowerShell
   - Check if profile is loaded (`$PROFILE`)
   - Verify execution policy

## Updates
- Last modified: October 29, 2024
- Version: 2.0

## Support
- Check OneDrive sync status if scripts aren't found
- Ensure PATH environment variable includes OneDrive DevTools bin
- Verify PowerShell profile is properly configured