#!/usr/bin/env bash

# Define the list of programs and their required packages
PROGRAMS=(
  "futurerestore"
  "img4tool"
  "Kernel64Patcher"
  "iBoot64Patcher"
  "ldid"
  "asr64_patcher"
  "restored_external64_patcher"
  # `hfsplus` comes from libdmg-hfsplus
  "hfsplus" 
)

# Define the package managers for each distribution
PACKAGE_MANAGERS=(
  "apt-get"  # Ubuntu, Debian, and other Debian-based distributions
  "yum"      # RedHat, CentOS, and other RedHat-based distributions
  "dnf"      # Fedora
  "zypper"   # openSUSE
)

# Install the required packages for each program
for program in "${PROGRAMS[@]}"; do
  for pm in "${PACKAGE_MANAGERS[@]}"; do
    if command -v "$pm" >/dev/null 2>&1; then
      echo "Installing dependencies for $program using $pm..."
      if "$pm" install -y "${program}_dependencies"; then
        break
      else
        echo "Failed to install dependencies for $program using $pm."
      fi
    fi
  done
done

echo "All dependencies are installed!"
echo "Made by Aditya:)"
