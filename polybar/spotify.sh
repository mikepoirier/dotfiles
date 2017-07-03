#!/bin/bash

if ! pgrep -x spotify >/dev/null; then
    echo "Spotify not running"
    exit
fi

icon=""

status=$(playerctl status --player=spotify)

case $status in
   Playing)
       icon=" "
       ;;
   Paused)
       icon=" "
       ;;
   *)
       ;;
esac

track=$(playerctl metadata title)
artist=$(playerctl metadata artist)

echo "$icon $artist - $track"
