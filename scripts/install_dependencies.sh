#!/bin/bash

# Update package lists and install necessary system packages
sudo apt-get update
sudo apt-get install -y wget gnupg  # Example system packages

# Install Python pip (if not already installed)
sudo apt-get install -y python3-pip

# Install Python dependencies from requirements.txt
sudo pip3 install -r /home/ubuntu/myapp/requirements.txt

# Additional installation commands as needed
