# UPS Battery Monitor

Battery monitoring for Raspberry Pi using an INA219 sensor over I²C. It calculates battery percentage and provides a web dashboard and JSON API.

## Setup

```bash
git clone https://github.com/dylanparsons/waveshare-ups-monitor.git
cd waveshare-ups-monitor
sudo chmod +x install.sh
sudo ./install.sh
```

The installer installs Python dependencies, enables I²C, and copies files to `/usr/local/bin` and the web root.

## Usage

**Dashboard:** open `http://your-pi/dashboard.html`

**Command line:**
```bash
python3 /usr/local/bin/battery_monitor.py
```

**API:**
```bash
curl http://localhost/battery_status.php
```

Example response:
```json
{
  "voltage": 8.2,
  "percentage": 75,
  "timestamp": "2026-07-02 14:30:45"
}
```

## Demo

Open `demo.html` to preview the dashboard without hardware. The demo cycles through good, low, and critical battery states.

## Configuration

Edit `battery_monitor.py` to set the battery's empty and full voltage thresholds. The defaults assume a four-cell pack (12–16.8 V). For a three-cell pack, use 9–12.6 V.

## Troubleshooting

- If the sensor is not detected, check wiring, enable I²C in `raspi-config`, and run `i2cdetect -y 1`. The expected address is `0x42`.
- If the dashboard shows dashes, run the monitor script directly to check sensor communication.
- If the script works but the web API does not, check the web server's I²C permissions and restart Apache after changing group membership.

## Files

- `battery_monitor.py` — INA219 monitoring
- `battery_status.php` — JSON API endpoint
- `dashboard.html` — Web dashboard
- `style.css` — Dashboard styles
- `demo.html` — Hardware-free dashboard demo
- `install.sh` — Installer

## License

MIT
