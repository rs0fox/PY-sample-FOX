#!/bin/bash

set -e

# Example: Start Python server
cd /home/ec2-user/PY_PIPE   # Adjust the directory path to match your actual app directory
nohup python3 server.py > server.log 2>&1 &
