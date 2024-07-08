#!/usr/bin/env python3

import os
import platform

ip = "10.110.115.168"

ping_cmd = f"ping -c 4 {ip} > /dev/null 2>&1"

exit = os.system(ping_cmd)

print(exit)
