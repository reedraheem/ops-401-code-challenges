#! /usr/bin/python 3



# Script:   code challenge 6             
# Author: Raheem Sharif Reed                     
# Date of latest revision: July 24,2023      
# Purpose:In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:
#Utilize the scapy library
#Define host IP
#Define port range or specific set of ports to scan
#Test each port in the specified range using a for loopIf flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
#If flag 0x14 received, notify user the port is closed.
#If no flag is received, notify the user the port is filtered and silently dropped.

from scapy.all import sr1, IP, TCP

def tcp_port_scan_with_notifications(host, port_range):
    open_ports = []
    closed_ports = []
    filtered_ports = []
    
    for port in port_range:
        response = sr1(IP(dst=host)/TCP(dport=port, flags='S'), timeout=1, verbose=False)
        
        if response and response[0]:
            response_pkt = response[0][0]
            if response_pkt.haslayer(TCP) and response_pkt[TCP].flags == 0x12:  # Open port
                open_ports.append(port)
            elif response_pkt.haslayer(TCP) and response_pkt[TCP].flags == 0x14:  # Closed port
                closed_ports.append(port)
            else:  # Filtered port
                filtered_ports.append(port)
    
    return open_ports, closed_ports, filtered_ports

# Usage example:
host_ip = "127.0.0.1"  # Replace with the target IP address
port_range_to_scan = range(1, 1025)  # Scanning ports from 1 to 1024

open_ports, closed_ports, filtered_ports = tcp_port_scan_with_notifications(host_ip, port_range_to_scan)

print(f"Open ports: {open_ports}")
print(f"Closed ports: {closed_ports}")
print(f"Filtered ports (silently dropped): {filtered_ports}")
