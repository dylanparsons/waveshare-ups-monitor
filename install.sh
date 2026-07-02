#!/bin/bash
set -e

echo "Installing Waveshare UPS Monitor..."

# Install Python dependencies
pip3 install INA219

# Copy files to /usr/local/bin and web root
sudo cp battery_monitor.py /usr/local/bin/
sudo chmod +x /usr/local/bin/battery_monitor.py

WEB_ROOT=${1:-/var/www/html}
sudo cp battery_status.php "$WEB_ROOT/"
sudo cp dashboard.html "$WEB_ROOT/"
sudo cp style.css "$WEB_ROOT/"

sudo chown www-data:www-data "$WEB_ROOT/battery_status.php"
sudo chown www-data:www-data "$WEB_ROOT/dashboard.html"
sudo chown www-data:www-data "$WEB_ROOT/style.css"

echo "✓ Installed to $WEB_ROOT"
echo "✓ Visit: http://[your-pi]/dashboard.html"