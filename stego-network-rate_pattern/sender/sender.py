import time
import socket

message_bits = "110010"
ip = "192.168.1.100"
port = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for bit in message_bits:
    if bit == "1":
        for _ in range(10):  # gửi nhanh
            sock.sendto(b"H", (ip, port))
            time.sleep(0.05)
    else:
        for _ in range(10):  # gửi chậm
            sock.sendto(b"L", (ip, port))
            time.sleep(0.3)
    time.sleep(1)

sock.close()