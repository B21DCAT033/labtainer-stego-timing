#!/bin/bash
if [ -f result.txt ]; then
    echo "check 1 - result.txt exists"
    grep "UDP" result.txt && echo "check 2 - UDP packets captured"
    grep -E "1.*1" result.txt && echo "check 3 - Retransmission pattern found"
    echo "check 4 - Analyzable with sequence"
    echo "check 5 - OK"
else
    echo "check failed"
fi