#!/usr/bin/env bash
xfce4-terminal --command="python3 nc.py 192.168.245.132 | pv | buffer -s 100k -m 8m | vlc -"
xfce4-terminal --command="python3 nc.py 192.168.245.131 | pv | buffer -s 500k -m 30m | vlc - --audio-visual visual --effect-list spectrum --no-visual-80-bands"
xfce4-terminal --command="python3 nc.py 192.168.245.130"
xfce4-terminal --command="python3 nc.py 192.168.245.133"