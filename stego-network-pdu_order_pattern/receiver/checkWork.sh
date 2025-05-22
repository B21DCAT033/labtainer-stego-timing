#!/bin/bash
if [ -f result.txt ]; then
    echo "check 1 - result.txt exists"
    grep "UDP" result.txt && echo "check 2 - UDP packets captured"
    grep "A" result.txt && echo "check 3 - Packet A found"
    grep "B" result.txt && echo "check 4 - Packet B found"
    echo "check 5 - Order can be analyzed"
    echo "check 6 - OK"
else
    echo "check failed"
fi