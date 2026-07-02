# UPS Battery Monitor

Simple battery monitoring dashboard for Raspberry Pi. Reads voltage from an INA219 sensor on I2C, calculates percentage, serves a web dashboard and JSON API.

## Setup

```bash
git clone https://github.com/yourusername/ups-battery-monitor
cd ups-battery-monitor
sudo chmod +x install.sh
sudo ./install.sh
```

Installs Python deps, enables I2C, copies files to `/usr/local/bin` and web root.

## Usage

**Dashboard:**
`http://your-pi/dashboard.html`

**Command line:**
```bash
python3 /usr/local/bin/battery_monitor.py
```

**API:**
```bash
curl http://localhost/battery_status.php
```

Returns:
```json
{
  "voltage": 8.2,
  "percentage": 75,
  "timestamp": "2026-07-02 14:30:45"
}
```

## Demo

To preview the dashboard UI without hardware, open `demo.html` in a browser. Shows battery states cycling through good, low, and critical.

## Configuration

Edit `battery_monitor.py` to set your battery's empty/full voltage thresholds.

Default assumes 4-cell setup (12V-16.8V). Adjust the `calculate_percentage()` function for your battery:

```python
# Example for 3-cell (9V-12.6V)
empty = 3 * 3.0  # 9V
full = 3 * 4.2   # 12.6V
```

## Troubleshooting

**Can't read voltage**

Check I2C: `i2cdetect -y 1`

Should show `42`. If nothing appears, verify connections or enable I2C in `raspi-config`.

**Dashboard shows dashes**

Test the script directly: `sudo python3 /usr/local/bin/battery_monitor.py`

If that fails, I2C isn't connected. Check physical wiring.

If script works but dashboard doesn't, verify `battery_status.php` can execute:
```bash
sudo usermod -aG i2c www-data
sudo systemctl restart apache2
```

## Files

- `battery_monitor.py` - INA219 driver
- `battery_status.php` - JSON API endpoint
- `dashboard.html` - Web UI
- `style.css` - Styling
- `demo.html` - Demo (no hardware required)
- `install.sh` - Setup script

## License

MIT