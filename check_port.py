## \file ../src/utils/check_port.py
﻿# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Check ports 
 a simple utility in Python that attempts to establish a connection 
 with each port in the range from start_port to end_port on the local host. 
 If the connection fails, it prints a message indicating that the port is free."""
...

import socket
import numpy as np



def check_port(port):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Try to connect to the port
        s.connect(('localhost', port))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except Exception as ex:
        # Print a message if there's an error
        print(f"Port {port} is free")
        return
    finally:
        # Always close the connection
        s.close()
        
def check_ports(start_port, end_port):
    # Check all ports in the range
    for port in range(start_port, end_port+1):
        check_port(port)
        

if __name__ == "__main__":
    start_port = 440
    end_port = 65535
    check_ports(start_port, end_port)



