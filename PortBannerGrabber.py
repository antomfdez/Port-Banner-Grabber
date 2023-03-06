import socket
import sys
# specify the host to scan
host = sys.argv[1]

# specify the range of ports to scan
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
max_char = int(sys.argv[4])

print(f"Host : {host}")
print(f"Scanning from {start_port} to {end_port}\n--")
# iterate over the range of ports and scan each one
for port in range(start_port, end_port+1):
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # try to connect to the host on the current port
    result = s.connect_ex((host, port))

    # if the connection was successful, try to get the port version
    if result == 0:
        try:
            banner = s.recv(max_char)
            print(f"Port {port} is open. Info: {banner.decode().strip()}")
        except:
            print(f"Port {port} is open, but could not determine the banner info.")
        
    # close the socket object
    s.close()

