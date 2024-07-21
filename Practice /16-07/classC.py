#!/usr/bin/env python3

import os
import platform

ip_prefix = "192.168.0."
os_current = platform.system().lower()

for final_octet in range(254):
    ip = ip_prefix + str(final_octet + 1)
    if os_current == "windows":
        ping_cmd = f"ping -n 4 {ip} > NUL"
    else:
        ping_cmd = f"ping -c 4 {ip} > /dev/null 2>&1"
    
    exit_code = os.system(ping_cmd)
    
    if exit_code == 0:
        print(f"{ip} is online")
