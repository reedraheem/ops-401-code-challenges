#! /usr/bin/python 3

#Reference: Chat Gpt Assisted

# Script:   code challenge 7            
# Author: Raheem Sharif Reed                     
# Date of latest revision: July 25,2023      
# Purpose:In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:
#Utilize the scapy library
#Define host IP
#Define port range or specific set of ports to scan
#Test each port in the specified range using a for loopIf flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
#If flag 0x14 received, notify user the port is closed.
#If no flag is received, notify the user the port is filtered and silently dropped.
#User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
#CMP Ping Sweep tool Prompt user for network address including CIDR block
#Create a list of all addresses in the given network
#f ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
#Otherwise, inform the user that the host is responding.
#Count how many hosts are online and inform the user.

from scapy.all import sr1, IP, TCP, ICMP
import ipaddress

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

def icmp_ping_sweep(network_address):
    hosts_up = 0

    # Create a list of all addresses in the given network
    network = ipaddress.IPv4Network(network_address, strict=False)
    all_addresses = list(network.hosts())

    # Ping all addresses on the given network except for network address and broadcast address
    for address in all_addresses:
        if address != network.network_address and address != network.broadcast_address:
            response = sr1(IP(dst=str(address))/ICMP(), timeout=1, verbose=False)
            if response and response[0] and response[0][0].type == 0:  # Echo Reply
                print(f"Host {address} is responding.")
                hosts_up += 1
            elif response and response[0] and response[0][0].type == 3 and response[0][0].code in [1, 2, 3, 9, 10, 13]:
                print(f"Host {address} is actively blocking ICMP traffic.")
            else:
                print(f"Host {address} is down or unresponsive.")

    print(f"Total hosts online: {hosts_up} out of {len(all_addresses)}")

def main():
    print("Welcome to the Network Tool!")
    while True:
        print("\nChoose an option:")
        print("1. TCP Port Range Scanner mode")
        print("2. ICMP Ping Sweep mode")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            host_ip = input("Enter the target IP address for TCP port scanning: ")
            port_range_to_scan = range(1, 1025)  # Scanning ports from 1 to 1024
            open_ports, closed_ports, filtered_ports = tcp_port_scan_with_notifications(host_ip, port_range_to_scan)
            print(f"Open ports: {open_ports}")
            print(f"Closed ports: {closed_ports}")
            print(f"Filtered ports (silently dropped): {filtered_ports}")
        elif choice == '2':
            network_address = input("Enter the network address with CIDR block (e.g., 192.168.1.0/24): ")
            icmp_ping_sweep(network_address)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()


