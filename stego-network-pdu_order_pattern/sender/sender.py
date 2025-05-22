import socket
import time

ip = "192.168.1.100"
port = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Chuỗi bit 10 → thứ tự A B (bit 1), B A (bit 0)
bit_sequence = ["1", "0", "1", "1", "0", "0"]

for bit in bit_sequence:
    if bit == "1":
        sock.sendto(b"A", (ip, port))
        sock.sendto(b"B", (ip, port))
    else:
        sock.sendto(b"B", (ip, port))
        sock.sendto(b"A", (ip, port))
    time.sleep(1)

sock.close()