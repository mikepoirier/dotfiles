#!/bin/bash

NOC=`nmcli d | grep -w connected | wc -l`

MSG=" : "

if (($NOC > 0)); then
    NETWORK=`nmcli d | grep wifi | awk '{print $4}'`

    STR=`nmcli d wifi | grep -m 1 PoirierNet | tr -d '*' | awk '{print $6}'`

    MSG+=$NETWORK"("$STR"%)"
else
    MSG+="Off"
fi

echo ${MSG}