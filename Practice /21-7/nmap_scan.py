#!/usr/bin/env python3

import nmap

target_address= "172.20.10.1"

port_start= 1
port_end=100

scanner = nmap.PortScanner()

print(f"scanning {target_address}")

for port in range(port_start, port_end+1):
    result = scanner.scan(target_address,str(port))
    port_status = result['scan'] [target_address]['tcp'][port]['state']
    print("\tPort: {0} is {1}".format(port,port_status))