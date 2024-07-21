#!/usr/bin/env python3

ip_file= open("ips.txt", "r")

ip_addresses= ip_file.read()
print(ip_addresses)

ip_file.close()