import socket
import time

ip = "192.168.1.100"
port = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message_bits = "10101"

for bit in message_bits:
    sock.sendto(bit.encode(), (ip, port))
    if bit == "1":
        time.sleep(0.2)
        sock.sendto(bit.encode(), (ip, port))  # retransmit
    time.sleep(1)

sock.close()