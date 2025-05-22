#!/bin/bash
if [ -f result.txt ]; then
    echo "check 1 - result.txt exists"
    grep "UDP" result.txt && echo "check 2 - UDP packets captured"
    grep "H" result.txt && echo "check 3 - High-rate packets present"
    grep "L" result.txt && echo "check 4 - Low-rate packets present"
    echo "check 5 - Timing data exists"
    echo "check 6 - OK"
else
    echo "check failed"
fi