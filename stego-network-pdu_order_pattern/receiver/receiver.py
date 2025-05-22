import subprocess
import time

print("Capturing UDP packet order...")
subprocess.Popen("tcpdump -i eth0 -tt udp port 9999 -w capture.pcap", shell=True)
time.sleep(10)
subprocess.call("pkill tcpdump", shell=True)

subprocess.call("tcpdump -nnr capture.pcap > result.txt", shell=True)
print("Analyze result.txt for order of packets A and B.")