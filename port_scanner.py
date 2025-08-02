import socket
import sys
from datetime import datetime

def scan_port(target, port):
    """
    Attempts to connect to a specific port on the target host.
    Returns 0 if the port is open, a non-zero value otherwise.
    """
    # Create a new socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a timeout for the connection attempt to avoid long waits
    sock.settimeout(1)

    # Attempt to connect to the port
    result = sock.connect_ex((target, port))
    sock.close()
    return result

def main():
    """
    Main function to run the port scanner.
    """
    # Get the target host from the command-line arguments or user input
    if len(sys.argv) == 2:
        target_host = sys.argv[1]
    else:
        target_host = input("Enter the target IP address or hostname: ")

    try:
        # Translate hostname to IPv4 address
        target = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("Invalid hostname. Exiting.")
        sys.exit()

    print("-" * 50)
    print(f"Scanning target: {target}")
    print("Time started:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-" * 50)

    # Define the port range to scan
    start_port = 1
    end_port = 1024  # Adjust this range as needed (e.g., 65535 for all ports)

    open_ports = []

    try:
        for port in range(start_port, end_port + 1):
            result = scan_port(target, port)
            if result == 0:
                print(f"Port {port}: Open")
                open_ports.append(port)

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to the server.")
        sys.exit()

    print("-" * 50)
    if open_ports:
        print("Scan complete. Open ports found:")
        for port in open_ports:
            try:
                # Attempt to get the service name for the open port
                service_name = socket.getservbyport(port)
                print(f"Port {port} ({service_name}): Open")
            except:
                print(f"Port {port}: Open")
    else:
        print("Scan complete. No open ports found in the specified range.")
    print("-" * 50)

if __name__ == "__main__":
    main()