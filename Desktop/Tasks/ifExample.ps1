# Check if new_folder exists and create if_folder if it does
if (Test-Path -Path "new_folder") {
    New-Item -ItemType Directory -Path "if_folder" -Force
}

# Check if if_folder exists and create appropriate folder
if (Test-Path -Path "if_folder") {
    New-Item -ItemType Directory -Path "hyperionDev" -Force
} else {
    New-Item -ItemType Directory -Path "new-projects" -Force
}