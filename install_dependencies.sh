#!/bin/bash

sudo apt update

sudo apt install -y python3
sudo apt install -y python3-pip
sudo apt install -y python3-dbg
    
pip3 install --upgrade pip setuptools wheel
	
echo "INSTALLATION COMPLETE"
