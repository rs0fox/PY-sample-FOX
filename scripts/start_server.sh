#!/bin/bash

set -e

# Example: Start Python server
cd /home/ubuntu/myapp
nohup python3 server.py > server.log 2>&1 &
