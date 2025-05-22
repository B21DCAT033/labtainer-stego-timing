import time
import os

# Chuỗi tin cần giấu: "10"
secret_bits = "10"

# Gửi ping nhanh (bit 1) hoặc chậm (bit 0) để tạo va chạm
for bit in secret_bits:
    if bit == "1":
        print("Sending fast ping for bit 1")
        os.system("ping -c 5 -i 0.1 192.168.1.255 &")
    else:
        print("Sending delayed ping for bit 0")
        os.system("ping -c 5 -i 1 192.168.1.255 &")
    time.sleep(2)  # Thời gian giữa các bit