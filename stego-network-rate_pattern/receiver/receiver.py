import subprocess
import time

print("Capturing UDP packets with tcpdump...")
subprocess.Popen("tcpdump -i eth0 -tt udp port 9999 -w capture.pcap", shell=True)
time.sleep(15)
subprocess.call("pkill tcpdump", shell=True)

print("Capture complete.")
subprocess.call("tcpdump -tt -nnr capture.pcap > result.txt", shell=True)