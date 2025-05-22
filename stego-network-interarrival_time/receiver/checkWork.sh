#!/bin/bash
if [ -f result.txt ]; then
    echo "check 1 - result.txt exists"
    grep "UDP" result.txt && echo "check 2 - captured UDP packets"
else
    echo "check failed"
fi