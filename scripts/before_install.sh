#!/bin/bash
set -e

# Install Apache if not already installed
if ! command -v apache2 > /dev/null; then
    echo "Apache is not installed. Installing..."
    apt-get update
    apt-get install -y apache2
else
    echo "Apache is already installed."
fi

# Ensure the /var/www/html directory exists
if [ ! -d "/var/www/html" ]; then
    mkdir -p /var/www/html
fi

# Remove existing index.html if it exists
if [ -f "/var/www/html/index.html" ]; then
    echo "Removing existing /var/www/html/index.html"
    rm -f /var/www/html/index.html
fi

# Change ownership to root
chown -R root:root /var/www/html