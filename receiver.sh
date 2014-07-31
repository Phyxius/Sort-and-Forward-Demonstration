#! /usr/bin/env bash
x-terminal-emulator -e 'bash -c "python3 nc.py 0x11 | pv | buffer -s 500k -m 30m | avplay -"' #'audio'
x-terminal-emulator -e 'bash -c "python3 nc.py 0x22 | pv | buffer -s 100k -m 8m | avplay -"' #video
x-terminal-emulator -e 'bash -c "python3 nc.py 0x33"' #text
x-terminal-emulator -e 'bash -c "python3 nc.py 0x44"' #auxiliary