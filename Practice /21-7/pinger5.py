#!/usr/bin/env python3

import os
import platform

def ping_host(ip):
    os_current = platform.system().lower()

    if os_current == "windows":
        ping_cmd = f"ping -n 4 {ip} > NUL"
    else:
        ping_cmd = f"ping -c 4 {ip} > /dev/null 2>&1"

    exit_code = os.system(ping_cmd)
    return exit_code

def import_ip():
    lines = []

    try:
        with open("ips.txt", "r") as f:
            for line in f:
                line = line.strip()
                lines.append(line)
    except FileNotFoundError:
        print("The file ips.txt was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines

ip_addresses = import_ip()

for ip in ip_addresses:
    exit_code = ping_host(ip)
    if exit_code == 0:
        print(f"{ip} is online")
    else:
        print(f"{ip} is offline or unreachable")

