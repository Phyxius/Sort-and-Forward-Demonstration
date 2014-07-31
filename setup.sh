#! /bin/bash
sudo apt-get update
sudo apt-get remove thunderbird firefox gnumeric abiword pidgin gmusicbrowser parole simple-scan transmission-common xchat -y
sudo apt-get update
sudo apt-get dist-upgrade -y
sudo apt-get update
sudo apt-get dist-upgrade -y
sudo apt-get install vlc python3-pip wireshark pv libav-tools -y
sudo apt-get update
sudo apt-get autoremove -y
sudo apt-get autoclean
ln -s "/mnt/hgfs/VM Shared Folder/" "~/Desktop/"
sudo reboot
