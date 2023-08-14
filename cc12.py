#! /usr/bin/python 3

#Reference: Chat Gpt Assisted

# Script:   code challenge 12          
# Author: Raheem Sharif Reed                     
# Date of latest revision: August 14,2023      
# Purpose:By now, you will have created several Python scripts in your public repo. Select one of your Python tools created during this class so far that does not have a logging feature. On that tool:
#Add logging capabilities to your Python tool using the logging library.
#Experiment with log types. Build in some error handling, then induce some errors. Send log data to a file in the local directory.
#Confirm your logging feature is working as expected.



import os
import time
import logging

def transmit_icmp_packet(destination_ip):
    while True:
        try:
            response = os.system("ping -c 1 " + destination_ip)  # Sending a single ICMP packet
            if response == 0:
                status = "Success"
            else:
                status = "Failure"
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"Timestamp: {timestamp} | Destination IP: {destination_ip} | Status: {status}"
            
            # Logging
            logging.info(log_message)
            
            print(log_message)
        except Exception as e:
            # Handle errors and log them
            error_message = f"An error occurred: {str(e)}"
            logging.error(error_message)
            
        time.sleep(2)  # Wait for 2 seconds before sending the next ICMP packet

def main():
    # Configure logging
    logging.basicConfig(filename="icmp_transmitter.log", level=logging.DEBUG,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    
    destination_ip = "192.168.0.1"  # Specify the destination IP
    transmit_icmp_packet(destination_ip)

# Execute the main function
if __name__ == "__main__":
    main()

