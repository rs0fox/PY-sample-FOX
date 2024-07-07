#!/bin/bash

set -e

# Example: Install Python dependencies
apt-get update
apt-get install -y python3-pip
pip3 install -r /home/ubuntu/myapp/requirements.txt
