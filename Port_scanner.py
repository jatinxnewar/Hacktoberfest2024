import socket

def port_scanner(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        return True
    except:
        return False

host = input("Enter host to scan: ")
for port in range(1, 1025):  # Scans ports 1 to 1024
    if port_scanner(host, port):
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
