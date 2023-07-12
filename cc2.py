#! /usr/bin/python 3

#Reference: Chat Gpt Assisted

# Script:   code challenge 2               
# Author: Raheem Sharif Reed                     
# Date of latest revision: July 12,2023     
# Purpose:Transmit a single ICMP (ping) packet to a specific IP every two seconds.
#Evaluate the response as either success or failure.
#Assign success or failure to a status variable.
#For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
#Ask the user for an email address and password to use for sending notifications.
#Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
#Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.



import datetime
import os
import time
import smtplib


#declare Variable
email = input("enter your email")
password = ("enter your password:")
ip=input("please porvide an ip address")
up= "host is down"
down= "host is down"

#check the status change
last=0

#declare functions

#functions that handles when the host goes from down to up
def send_notification_email(email, password, recipient, host, previous_status, current_status):

#gets timestamp
 def get_current_timestamp():
    timestamp = datetime.datetime.now()
    return timestamp

# Example usage
current_timestamp = "get_current_timestamp"()
print("Current Timestamp:", current_timestamp)

#creates smtp session
s= smtplib.smtp('smtp.gmail.com,587')


#start tls for security
s= "starttls"()

#authentication
s.login("raheem6463@gmail.com,wmbp ylwe zhlh ualv")

#message to be sent
message = "surpass your limits"

#sending the mail
s.sendmail("raheem6463@gmail.com,receiver_email_id,message")

#terminating the session
s.quit()




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
