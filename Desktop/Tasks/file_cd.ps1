# Create three new folders
New-Item -ItemType Directory -Path "scripting1"
New-Item -ItemType Directory -Path "scripting2"
New-Item -ItemType Directory -Path "scripting3"

# Navigate into Folder1
Set-Location -Path "Folder1"

# Create three new folders inside Folder1
New-Item -ItemType Directory -Path "Subscripting1"
New-Item -ItemType Directory -Path "Subscripting2"
New-Item -ItemType Directory -Path "Subscripting3"

# Remove two of the subfolders
Remove-Item -Path "Subscripting2"
Remove-Item -Path "Subscripting3"

# Navigate back to the original directory
Set-Location -Path ".."