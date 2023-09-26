#! /usr/bin/python 3



# Script:   code challenge 1               
# Author: Raheem Sharif Reed                     
# Date of latest revision: July 11,2023     
# Purpose:Transmit a single ICMP (ping) packet to a specific IP every two seconds.
#Evaluate the response as either success or failure.
#Assign success or failure to a status variable.
#For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.


import os
import time

def transmit_icmp_packet(destination_ip):
    while True:
        response = os.system("ping -c 1 " + destination_ip)  # Sending a single ICMP packet
        if response == 0:
            status = "Success"
        else:
            status = "Failure"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Timestamp: {timestamp} | Destination IP: {destination_ip} | Status: {status}")
        time.sleep(2)  # Wait for 2 seconds before sending the next ICMP packet

def main():
    destination_ip = "192.168.0.1"  # Specify the destination IP
    transmit_icmp_packet(destination_ip)

# Execute the main function
if __name__ == "__main__":
    main()
