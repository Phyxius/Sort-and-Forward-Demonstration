#!/usr/bin/env bash
x-terminal-emulator -e 'bash -c "python3 forwarder.py"' #forwarder script
sleep 1
x-terminal-emulator -e 'bash -c "pv -L 80k Data/demodata/audio_5fps.avi | nc -u localhost 13337"' #audio
x-terminal-emulator -e 'bash -c "pv -L 500k Data/demodata/video.avi | nc -u localhost 13338 "' #video
x-terminal-emulator -e 'bash -c "pv -L 10 Data/demodata/text.txt | nc -u localhost 13339"' #text
x-terminal-emulator -e 'bash -c "nc -u localhost 13340"' #auxiliary