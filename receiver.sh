#!/usr/bin/env bash
x-terminal-emulator -e 'bash -c "python3 nc.py 192.168.245.132 | pv | buffer -s 100k -m 8m | vlc - "'
x-terminal-emulator -e 'bash -c "python3 nc.py 192.168.245.131 | pv | buffer -s 500k -m 30m | vlc - --audio-visual visual --effect-list spectrum --no-visual-80-bands "'
x-terminal-emulator -e 'bash -c "python3 nc.py 192.168.245.130 "'
x-terminal-emulator -e 'bash -c "python3 nc.py 192.168.245.133"'