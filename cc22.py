#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 5  # Set a timeout value here (e.g., 5 seconds).
sockmod.settimeout(timeout)

hostip = input("Enter the host IP: ")  # Collect a host IP from the user.
portno = int(input("Enter the port number: "))  # Collect a port number from the user and convert it to an integer data type.

def portScanner(portno):
    try:
        sockmod.connect((hostip, portno))
        print("Port open")
        sockmod.close()
    except ConnectionRefusedError:
        print("Port closed")

portScanner(portno)


# TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
 # TODO: Collect a port number from the user, then convert it to an integer data type.
 # TODO: Collect a host IP from the user.
# TODO: Set a timeout value here.
