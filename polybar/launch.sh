#!/bin/bash

killall -q polybar

while pgrep -x polybar >/dev/null; do sleep 1; done

polybar -r top &
polybar -r bottom &

echo "Bars launched..."

