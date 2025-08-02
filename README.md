# Port-Scanner
Python script that prompts for a target IP address, iterates through a specified range of ports, and logs which ports are open.

# Python Port Scanner
This is a simple, educational port scanner built with Python. It provides a foundational example for understanding network communication and the use of the socket library. This tool is designed for learning and ethical use, helping to demonstrate how to programmatically check for open ports on a network host.

Features
Host Resolution: The script can translate hostnames (like example.com) into IP addresses.

Port Range Scanning: It can scan a specific range of TCP ports to identify which are open.

Clear Output: The program provides real-time updates as it discovers open ports and a final summary upon completion.

Service Identification: For common ports, the script attempts to identify the associated service (e.g., HTTP on port 80).

Prerequisites
To run this project, you will need:

A working installation of Python 3.x.

The project relies solely on Python's standard library, so no additional dependencies need to be installed.

How to Use
To use this program, you will need to open a terminal and run the port_scanner.py file. The script will then prompt you to enter the target IP address or hostname you wish to scan. Alternatively, you can provide the target directly as a command-line argument. The program will then begin its scan, displaying the results as it finds them.

Disclaimer
This tool is for educational purposes only. Do not use this script to scan any network or computer without explicit permission from the owner. Unauthorized network scanning may be considered illegal in some jurisdictions and is generally unethical. Please use this tool responsibly.
