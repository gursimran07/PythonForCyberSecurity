#!/usr/bin/env python3

import os
import platform

ip = input("Enter the IP address: ")
os_current = platform.system().lower()

if os_current == "windows":
    ping_cmd = f"ping -n 4 {ip} > NUL"
else:
    ping_cmd = f"ping -c 4 {ip} > /dev/null 2>&1"

exit_code = os.system(ping_cmd)

print(exit_code)
