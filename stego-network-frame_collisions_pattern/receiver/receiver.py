import subprocess
import time

print("Starting tcpdump...")
subprocess.Popen("tcpdump -i eth0 -w capture.pcap", shell=True)
print("Capturing for 10s...")
time.sleep(10)
subprocess.call("pkill tcpdump", shell=True)

print("Capture complete. Analyzing...")
subprocess.call("tcpdump -nnr capture.pcap > result.txt", shell=True)

# Gợi ý xử lý thêm để đếm khoảng cách thời gian hoặc số packet / giây sau này
print("Check result.txt for packet timing.")