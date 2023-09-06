#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Custom Scan\n""")  # Updated the menu options
print("You have selected option: ", resp)

# Prompt the user to type in a port range for this tool to scan
port_range = input("Enter the port range (e.g., 1-100): ")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", list(scanner[ip_addr]['tcp'].keys()))
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sU')  # UDP scan
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", list(scanner[ip_addr]['udp'].keys()))
elif resp == '3':
    # Implement a custom scan here based on user input
    custom_scan_args = input("Enter custom Nmap scan arguments: ")
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, custom_scan_args)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    open_ports = []
    for protocol in scanner[ip_addr].all_protocols():
        open_ports.extend(scanner[ip_addr][protocol].keys())
    print("Open Ports: ", open_ports)
else:
    print("Please enter a valid option")
### TODO: Select what your third scan type will be
### TODO: Prompt the user to type in a port range for this tool to scan
### TODO: Add missing code block 


