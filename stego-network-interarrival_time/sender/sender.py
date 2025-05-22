import time
import socket

message_bits = "101001"
ip = "192.168.1.100"  # IP của receiver, giả định trong mạng LAN
port = 9999

print("Sending encoded bits via UDP interarrival timing...")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for bit in message_bits:
    if bit == "1":
        interval = 0.1
    else:
        interval = 0.5
    sock.sendto(b"secret", (ip, port))
    print(f"Sent bit {bit}, sleeping {interval}s")
    time.sleep(interval)

sock.close()