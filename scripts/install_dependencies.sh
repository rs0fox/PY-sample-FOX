#!/bin/bash

# Update package lists and install necessary packages
sudo apt-get update
sudo apt-get install -y package1 package2 package3  # Replace with actual package names

# Additional installation steps (if needed)
# ...

# Clean up
sudo apt-get autoremove -y
sudo apt-get clean

echo "Dependencies installed successfully!"
