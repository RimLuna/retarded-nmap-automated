#!/usr/bin/env python3

## Script to scan IP addresses in local subnet ##

import subprocess
import re

## function to execute command 
def exec(command):
	return(subprocess.check_output(['bash', '-c', command]))

def scan_me(ip_addr):
	print("Scanning ports on IP: %s" % ip_addr)
	exec('nmap -T4 -p- ' + ip_addr)	

interface = exec('find /sys/class/net ! -type d | xargs --max-args=1 realpath  | awk -F\/ \'/pci/{print $NF}\' | head -n 1').decode("utf-8").replace('\n', '')
mess = exec('ifconfig ' + interface + ' | grep "inet "').decode("utf-8")
ip_addr = mess.strip().split(" ")[1]

print("YOUR IP ADDRESS IS: ", ip_addr)
print("-" * 30)

octets = ".".join(ip_addr.split('.')[:-1])

subnet = octets + ".0/24"

print("Netdiscover on local subnet: ", subnet)

local_ips = exec('netdiscover -P -r ' + subnet + ' | grep "1" | cut -d" " -f 2').decode("utf-8").splitlines()

for khra in range(0, len(local_ips)):
	ip = local_ips[khra]
	print("%d. %s" % (khra + 1, ip))

miaw = int(input("Choose IP address (1-%d): " % len(local_ips)))
print("Chosen IP: %s" % local_ips[miaw - 1])

scan_me(local_ips[miaw - 1])
