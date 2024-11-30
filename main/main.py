
import socket

# Function to scan a port on a target host
def scan_port(host, port):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    # Attempt to connect to the port
    try:
        sock.connect((host, port))
        sock.shutdown(socket.SHUT_RDWR)
        print(f"Port {port} open.")
        return True
    except:
        print(f"Port {port} closed.")
        return False
    finally:
        sock.close()

# Function to scan a range of ports on a target host
def scan_range(host, start_port, end_port):
    # Initialize list of open ports
    open_ports = []

    # Scan each port in the range
    for port in range(start_port, end_port+1):
        if scan_port(host, port):
            open_ports.append(port)

    # Return list of open ports
    return open_ports

# Main function to get user input and call scan_range function
def main():
    # Get target host and port range from user
    host = input("Enter target host: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    # Scan port range and print open ports
    open_ports = scan_range(host, start_port, end_port)
    if len(open_ports) == 0:
        print("No open ports found.")
    else:
        print("Open ports:")
        for port in open_ports:
            print(port)

if __name__ == '__main__':
    main()
