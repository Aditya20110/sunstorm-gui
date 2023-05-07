#!/usr/bin/env bash

set -e

program_list=(
    'futurerestore'
    'img4tool'
    'Kernel64Patcher'
    'iBoot64Patcher'
    'ldid'
    'asr64_patcher'
    'restored_external64_patcher'
    'hfsplus'
)

# Check if Homebrew is installed
if command -v brew >/dev/null 2>&1; then
    PM="brew"
else
    echo "Error: Homebrew not found"
    exit 1
fi

# Install required packages
echo "Updating package lists"
sudo $PM update >/dev/null
echo "Installing required packages"
sudo $PM install build-essential openssl libssl-dev curl libbz2 libbz2-dev readline \
    libreadline-dev libusb libusb-dev libxml2 libxml2-dev libzip libzip-dev cmake \
    python3 ncurses unzip libffi libffi-dev liblzma liblzma-dev ossp-uuid

# Install hfsplus package
if command -v hfsplus >/dev/null 2>&1; then
    echo "hfsplus already installed"
else
    echo "Installing hfsplus package"
    brew install hfsprogs
fi

# Install program_list packages
echo "Installing program_list packages"
for program in "${program_list[@]}"; do
    if command -v "$program" >/dev/null 2>&1; then
        echo "$program already installed"
    else
        echo "Installing $program package"
        sudo pip3 install "$program"
    fi
done

echo "Done! Thanks for using GUI"
echo "Made by Aditya :)"
