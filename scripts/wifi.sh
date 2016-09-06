#!/bin/bash

RED="FF0000"
YELLOW="FFFF00"
GREEN="00FF00"

NOC=`nmcli d | grep -w connected | wc -l`

MSG=" : "

if (($NOC > 0)); then

    COLOR="!Y BG 0xFFFF0000 Y!"
    NETWORK=`nmcli d | grep wifi | awk '{print $4}'`

    STR=`nmcli d wifi | grep -m 1 ${NETWORK} | tr -d '*' | awk '{print $6}'`

    MSG+=${NETWORK}" ("${STR}"%)"
else
    MSG+="Off"
fi

echo ${MSG}