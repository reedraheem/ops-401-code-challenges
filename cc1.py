#! /usr/bin/python 3

# Script:   code challenge 1               
# Author: Raheem Sharif Reed                     
# Date of latest revision: July 11,2023     
# Purpose:Transmit a single ICMP (ping) packet to a specific IP every two seconds.
#Evaluate the response as either success or failure.
#Assign success or failure to a status variable.
#For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.


import time
import datetime
import ping3

def check_host_status(destination_ip):
    while True:
        try:
            response_time = ping3.ping(destination_ip)
            if response_time is not None:
                status = "Success"
            else:
                status = "Failure"
        except ping3.errors.PingError:
            status = "Failure"
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Destination IP: {destination_ip} | Status: {status}")

        time.sleep(2)

# Specify the destination IP address you want to monitor
destination_ip = "192.168.0.1"

check_host_status(destination_ip)
