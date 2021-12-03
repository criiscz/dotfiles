. (Resolve-Path ~/Documents/WindowsPowerShell/gitutils.ps1)

function prompt {
    $color = "Blue"
    $home_regex = $HOME.replace("\", "\\")
    Write-Host($env:USERDOMAIN.ToLower() + "@" + $env:USERNAME) -NoNewline -ForegroundColor "Green"
    if (isCurrentDirectoryGitRepository) {
        $patha = ([string]$pwd).split("\", [System.StringSplitOptions]::RemoveEmptyEntries)
        Write-Host(' ' + $patha[$patha.length - 1]) -NoNewline -ForegroundColor Magenta
    }
    elseif ( $(Get-Location) -match $home_regex ) {
        Write-Host(" " + ($(Get-Location) -replace `
                    $home_regex, "~")  ) -NoNewLine -ForegroundColor $Color
    }
    elseif ( $(Get-Location) -match $env:SystemDrive + "\\" ) {
        Write-Host(" " + ($(Get-Location) -replace `
                    $env:SystemDrive, "")) -NoNewLine -ForegroundColor $Color    
    }
    else {
        Write-Host(" " + $(Get-Location)) -NoNewLine -ForegroundColor $Color
    }

    if (isCurrentDirectoryGitRepository) {
        $status = gitStatus
        $currentBranch = $status["branch"]
      
        Write-Host(' ' + [char]0x2387 + ' ') -nonewline -foregroundcolor Magenta
        if ($status["ahead"] -eq $FALSE) {
            Write-Host($currentBranch) -nonewline -foregroundcolor Cyan
        }
        else {
            Write-Host($currentBranch) -nonewline -foregroundcolor Red
        }
        Write-Host(' +' + $status["added"]) -nonewline -foregroundcolor Green
        Write-Host(' ~' + $status["modified"]) -nonewline -foregroundcolor Yellow
        Write-Host(' -' + $status["deleted"]) -nonewline -foregroundcolor Red
      
        if ($status["untracked"] -ne $FALSE) {
            Write-Host(' !') -nonewline -foregroundcolor Red
        }
    }
    Write-Host(' $') -nonewline -foregroundcolor Blue    
    return " "
}

# Functions for git commands
function Show-Branch { git branch }

function Show-Branch-All { git branch -a }

function Create-Commit {
    param([string]$message)
    git commit -m $message
}

function Switch-Branch {
    param([string]$branch)
    git switch $branch
}

function Create-Branch {
    param(
        [string]$branch
    )

    git switch -c $branch
}

function Delete-Branch {
    param(
        [string]$branch
    )

    git switch -d $branch
}

function Add-All {
    git add -A
}

function Add-Files {
    param(
        [string[]]$files
    )

    foreach ($file in $files) {
        git add $file
    }
}

function Show-Status {
    git status
}

function Git-Fetch {
    git fetch
}

function Git-Pull {
    git pull
}

function Git-Fetch-Prune {
    git fetch -p
}

function Git-Push {
    param(
        [string]$remote,
        [string]$branch
    )

    git push $remote $branch
}

function Git-Switch-To-Develop {
    git switch develop
}

function Git-Switch-To-Master {
    git switch master
}


# Set aliases for git commands
Set-Alias gb Show-Branch
Set-Alias gba Show-Branch-All
Set-Alias gcc Create-Commit
Set-Alias gcb Create-Branch
Set-Alias gs Switch-Branch
Set-Alias gaa Add-All
Set-Alias ga Add-Files
Set-Alias gt Show-Status
Set-Alias gf Git-Fetch
Set-Alias gpp Git-Pull
Set-Alias gfp Git-Fetch-Prune
Set-Alias gph Git-Push
Set-Alias gdev Git-Switch-To-Develop
Set-Alias gmaster Git-Switch-To-Master

Set-Alias 'i.' Open-Intellij-Here
Set-Alias 'i' Open-Intellij-Path

function Open-Intellij-Here {
    start-process powershell.exe {-command idea $pwd } -WindowStyle Hidden
}

function Open-Intellij-Path {
    param([string]$path)
    idea $path &
}

Set-Alias petsgram Change-Petsgram
function Change-Petsgram {
    cd D:/MisionTic4a/Petsgram/petsgram/
}