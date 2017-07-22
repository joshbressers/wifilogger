#!/usr/bin/env python

import glob
import subprocess
import time
import os

while 1:
	files = glob.glob('/home/pi/kismet/*')
	files.sort(key=os.path.getmtime)

	#remove the last file
	files = files[:-1]

	for i in files:
		ret = subprocess.call(['/home/pi/filter_tshark.sh', i])
		os.remove(i)
		# Do we care if something goes wrong?

	time.sleep(1)
