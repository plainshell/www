#!/bin/bash

# Check for Linux Distro
if [ -f /etc/os-release ]; then
    . /etc/os-release
    distro=$ID
elif type lsb_release >/dev/null 2>&1; then
    distro=$(lsb_release -si)
elif [ -f /etc/lsb-release ]; then
    . /etc/lsb-release
    distro=$DISTRIB_ID
elif [ -f /etc/debian_version ]; then
    distro=Debian
elif [ -f /etc/SuSe-release ]; then
    distro=SuSE
elif [ -f /etc/redhat-release ]; then
    distro=RHEL
else
    distro=UNKNOWN
fi

# Ubuntu-based
if [ "$distro" == "ubuntu" ] || [ "$distro" == "debian" ] || [ "$distro" == "linuxmint" ]; then
    sudo apt-get update
    sudo apt-get install python3 -y
    sudo apt-get install python3-pip -y
# CentOS/RHEL
elif [ "$distro" == "rhel" ] || [ "$distro" == "centos" ] || [ "$distro" == "fedora" ]; then 
    sudo yum install python3 -y
    sudo yum install python3-pip -y
fi

# Checking if installed correctly
#python3 --version
#pip3 --version

python3 script.py
