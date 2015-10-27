#####################################
# Simple Python prgram that reads motion sensor
# from PILand and takes picture if sensor change from low to high
#
# The picture will be sent to ?????
#
# sudo python camera-on-piland.py
#
####################################

import time
import requests
import sys
import picamera
import os
import ftplib

# Pi Land Setting
room = 405
slot = 1

baseurl = "http://piland.socialdevices.io"
baseurl = baseurl + "/" + str(room) + "/read/" + str(slot)

prev_state = "LOW"
curr_state = "LOW"

camera = picamera.PiCamera()

while True:
	# print "Getting:", baseurl
	response = requests.get(baseurl)
	prev_state = curr_state
	if response.status_code != requests.codes.ok:
		print "Error reading ", baseurl

	curr_state = response.text
	if curr_state != prev_state:
		if curr_state == "HIGH":
			print "Picture is Taken"
			prev_state = curr_state
			os.remove('/home/pi/sensED/image.jpg')
                        camera.capture('/home/pi/sensED/image.jpg')
			print(time.strftime("%H:%M:%S"))
		if curr_state == "LOW":
			print "Room is empty"
			prev_state = "LOW"
	time.sleep(1)

	
# except KeyboardInterrupt:
#	"Control-C"
#	break
