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



import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import time

# Function to send email notification
def send_email(sender_email, sender_password, receiver_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Create SMTP connection and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, "wmbp ylwe zhlh ualv")
        smtp.send_message(msg)

# Function to check host status
def check_host_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "up"
        else:
            return "down"
    except requests.ConnectionError:
        return "down"

# Main function
def main():
    # Get user email and password
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password: ")
    receiver_email = input("Enter the receiver's email address: ")

    # Dictionary to store host statuses
    host_statuses = {}

    while True:
        # Specify the host URLs to monitor
        hosts = {
            'Google': 'https://www.google.com',
            'Facebook': 'https://www.facebook.com',
            'Twitter': 'https://www.twitter.com'
        }

        for host, url in hosts.items():
            current_status = check_host_status(url)
            if host not in host_statuses:
                host_statuses[host] = current_status
                continue

            previous_status = host_statuses[host]
            if current_status != previous_status:
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                message = f"Host: {host}\nStatus Changed: {previous_status} -> {current_status}\nTimestamp: {timestamp}"
                subject = f"Host Status Changed: {host} is {current_status.upper()}"
                send_email(sender_email, sender_password, receiver_email, subject, message)
                host_statuses[host] = current_status

        # Wait for 5 minutes before checking again
        time.sleep(300)

if __name__ == "__main__":
    main()





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
