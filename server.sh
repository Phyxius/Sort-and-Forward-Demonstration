#!/usr/bin/env bash
xfce4-terminal --command="python3 forwarder.py" &
sleep 1
xfce4-terminal --command="pv -L 500k Data/demodata/video.avi | nc -u localhost 13339" &
xfce4-terminal --command="pv -L 80k Data/demodata/audio.mp3 | nc -u localhost 13338" &
xfce4-terminal --command="pv -L 10 Data/demodata/text.txt | nc -u localhost 13337" &
xfce4-terminal --command="nc -u localhost 13340" &