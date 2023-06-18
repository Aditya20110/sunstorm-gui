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

# Determine the package manager
if command -v apt-get >/dev/null 2>&1; then
    PM="apt-get"
elif command -v dnf >/dev/null 2>&1; then
    PM="dnf"
elif command -v yum >/dev/null 2>&1; then
    PM="yum"
else
    echo "Error: Package manager not found"
    exit 1
fi

# Install required packages
if [ "$PM" = "apt-get" ]; then
    # Debian/Ubuntu-based distributions
    echo "Updating package lists"
    sudo $PM update -qq >/dev/null
    echo "Installing required packages"
    sudo $PM install -yqq build-essential libssl-dev libcurl4-openssl-dev libreadline-dev \
        libusb-1.0-0-dev libusbmuxd-dev libplist-dev libzip-dev curl libbz2-dev cmake \
        python3-pip python3-dev libncurses-dev unzip libtinfo5 libxml2-dev libssl-dev \
        libffi-dev libbz2-dev liblzma-dev uuid-dev libfuse-dev
    # Install hfsplus package
    if command -v hfsplus >/dev/null 2>&1; then
        echo "hfsplus already installed"
    else
        echo "Installing hfsplus package"
        sudo $PM install -yqq hfsprogs
    fi
elif [ "$PM" = "dnf" ] || [ "$PM" = "yum" ]; then
    # Red Hat/CentOS-based distributions
    echo "Updating package lists"
    sudo $PM update -y >/dev/null
    echo "Installing required packages"
    sudo $PM install -y gcc gcc-c++ openssl-devel readline-devel libusb-devel libplist-devel \
        curl-devel libxml2-devel libzip-devel libcurl-devel bzip2-devel cmake python3-pip \
        ncurses-devel unzip libtinfo libffi-devel liblzma-devel uuid-devel fuse-devel
    # Install hfsplus package
    if command -v hfsplus >/dev/null 2>&1; then
        echo "hfsplus already installed"
    else
        echo "Installing hfsplus package"
        sudo $PM install -y hfsplus-tools
    fi
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

# install pyqt5
echo "installing pyqt5"
pip install pyqt5

# fix shitty xcb error!
echo "fixing xcb error"
sudo apt-get install libxcb-xinerama0

echo "Done! All dependencies are installed"
echo "Made by Aditya:)"
