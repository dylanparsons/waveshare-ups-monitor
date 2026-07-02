#!/usr/bin/env python3
"""
Read voltage from Waveshare UPS via INA219 at 0x42.
Returns voltage and percentage based on cell count.
"""
import sys
from INA219 import INA219

def get_battery_voltage():
    try:
        ina219 = INA219(addr=0x42)
        return round(ina219.getBusVoltage_V(), 2)
    except:
        return None

def calculate_percentage(voltage, cells=4):
    """
    Calculate percentage for LiPo battery.
    3.0V (empty) to 4.2V (full) per cell.
    """
    empty = cells * 3.0
    full = cells * 4.2
    
    if voltage >= full:
        return 100
    elif voltage <= empty:
        return 0
    else:
        return int(((voltage - empty) / (full - empty)) * 100)

if __name__ == "__main__":
    voltage = get_battery_voltage()
    
    if voltage is None:
        print("Error: Can't read UPS")
        sys.exit(1)
    
    pct = calculate_percentage(voltage)
    print("{0}V ({1}%)".format(voltage, pct))
    
    # Continuous mode for testing
    if len(sys.argv) > 1 and sys.argv[1] == '--monitor':
        import time
        print("Monitoring (Ctrl+C to stop)...")
        try:
            while True:
                v = get_battery_voltage()
                if v:
                    print("{0}V ({1}%)".format(v, calculate_percentage(v)))
                time.sleep(2)
        except KeyboardInterrupt:
            print("\nStopped.")