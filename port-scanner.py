import socket

# define target IP and port range
target_ip = input("Enter target IP address: ")
start_port = int(input("Enter starting port number: "))
end_port = int(input("Enter ending port number: "))

# display banner
print("*" * 50)
print("Hackervegas001 Port Scanner")
print("*" * 50)

# scan ports and display open ones
for port in range(start_port, end_port+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"Port {port} is open.")
    s.close()
