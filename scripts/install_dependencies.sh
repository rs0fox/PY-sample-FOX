#!/bin/bash

# Update package lists and install necessary packages
sudo yum update -y
#sudo yum install -y package1 package2 package3  # Replace with actual package names

# Additional installation steps (if needed)
# ...

# Clean up
sudo yum autoremove -y
sudo yum clean all

echo "Dependencies installed successfully!"
