import socket

# specify the host to scan
host = input("Enter the host to scan: ")

# specify the range of ports to scan
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

# iterate over the range of ports and scan each one
for port in range(start_port, end_port+1):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    # try to connect to the host on the current port
    result = s.connect_ex((host, port))

    # if the connection was successful, try to get the port version
    if result == 0:
        try:
            banner = s.recv(1024)
            print(f"Port {port} is open. Version: {banner.decode().strip()}")
        except:
            print(f"Port {port} is open, but could not determine the version.")
        
    # close the socket object
    s.close()

