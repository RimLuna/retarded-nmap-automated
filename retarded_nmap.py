#!/usr/bin/python3

import pyfiglet
import nmap

kill_me = pyfiglet.figlet_format("Eat The Rich!!")
print(kill_me)

scanner = nmap.PortScanner()

ip_addr = input("IP address to scan: ")
print("IP entered: ", ip_addr)
type(ip_addr)

opt = input("""\nEnter type of scan to run
			1. SYN ACK Scan
			2. UDP Scan
			3. Comprehensive Scan\n""")

print("You have selected option: ", opt)

if opt == '1':
	print("Nmap Version: ", scanner.nmap_version())
	scanner.scan(ip_addr, '1-1024', '-v -sS')
	print(scanner.scaninfo())
	print("IP Status: ", scanner[ip_addr].state())
	print(scanner[ip_addr].all_protocols())
	print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif opt == '2':
	print("Nmap Version: ", scanner.nmap_version())
	scanner.scan(ip_addr, '1-1024', '-v -sU')
	print(scanner.scaninfo())
	print("IP Status: ", scanner[ip_addr].state())
	print(scanner[ip_addr].all_protocols())
	print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif opt == '3':
	print("Nmap Version: ", scanner.nmap_version())
	scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
	print(scanner.scaninfo())
	print("IP Status: ", scanner[ip_addr].state())
	print(scanner[ip_addr].all_protocols())
	print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif opt == '4':
	print("Enter a valid option")
