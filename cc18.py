#! /usr/bin/python 3

#Reference: Chat Gpt Assisted

# Script:   code challenge 18         
# Author: Raheem Sharif Reed                     
# Date of latest revision: August 28,2023      
# Purpose:Prompt a user to type a URL or IP address
#Prompts the user to type a port number
#Performs banner grabbing using netcat against the target address at the target port,prints the results to the screen then moves on to the step below.
#Performs banner grabbing using telnet against the target address at the target port,prints the results to the screen then moves on to the step below.
#performs banner grabbing using Nmap against the target address of all well known ports,print the the results to the screen.
#Note:be sure to only target approved URLs like scanme.nmap.org or web servers you own.


import socket
import telnetlib
import nmap

def banner_grab_nc(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            banner = s.recv(1024).decode().strip()
            print(f"Netcat Banner: {banner}")
    except Exception as e:
        print(f"Netcat Error: {e}")

def banner_grab_telnet(host, port):
    try:
        with telnetlib.Telnet(host, port, timeout=5) as tn:
            banner = tn.read_until(b"\n", timeout=5).decode().strip()
            print(f"Telnet Banner: {banner}")
    except Exception as e:
        print(f"Telnet Error: {e}")

def banner_grab_nmap(host):
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=host, arguments='-p 1-1024')
        for host in nm.all_hosts():
            for port, data in nm[host].all_tcp().items():
                if 'product' in data:
                    print(f"Nmap Banner - Port {port}: {data['product']} {data['version']}")
    except Exception as e:
        print(f"Nmap Error: {e}")

def main():
    target_host = input("Enter target address: ")
    target_port = int(input("Enter target port: "))

    print("Banner Grabbing using Netcat:")
    banner_grab_nc(target_host, target_port)

    print("\nBanner Grabbing using Telnet:")
    banner_grab_telnet(target_host, target_port)

    print("\nBanner Grabbing using Nmap on well-known ports:")
    banner_grab_nmap(target_host)

if __name__ == "__main__":
    main()

