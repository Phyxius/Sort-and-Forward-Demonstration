from getch import getch
import os, signal, subprocess
import sys

if len(sys.argv) is 1:
	print("Need one or more files!")
	sys.exit()

subproc = subprocess.call([cat] + sys.argv[1:], stdout=sys.stdout)
	