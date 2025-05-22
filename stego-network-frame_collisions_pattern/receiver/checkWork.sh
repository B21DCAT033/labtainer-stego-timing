#!/bin/bash
if [ -f result.txt ]; then
    echo "check 1 - result.txt exists"
    grep ICMP result.txt && echo "check 2 - captured ICMP packets"
else
    echo "check failed"
fi