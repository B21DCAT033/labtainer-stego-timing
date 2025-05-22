import subprocess
import time

print("Listening for packets and capturing timestamps...")

subprocess.Popen("tcpdump -i eth0 -tt udp port 9999 -w capture.pcap", shell=True)
time.sleep(10)
subprocess.call("pkill tcpdump", shell=True)

print("Capture complete. Use tcpdump -tt to analyze timing.")
subprocess.call("tcpdump -tt -nnr capture.pcap > result.txt", shell=True)