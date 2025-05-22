import subprocess
import time

print("Capturing retransmissions...")
subprocess.Popen("tcpdump -i eth0 -tt udp port 9999 -w capture.pcap", shell=True)
time.sleep(12)
subprocess.call("pkill tcpdump", shell=True)

subprocess.call("tcpdump -nnr capture.pcap > result.txt", shell=True)
print("Analyze result.txt for retransmissions.")