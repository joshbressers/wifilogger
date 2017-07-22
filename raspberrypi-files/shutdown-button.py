#!/usr/bin/python  
# Simple script for shutting down the raspberry Pi at the press of a button.  
# by Inderpreet Singh  
  
import RPi.GPIO as GPIO  
import time  
import os  

presses = 0
press_time = 0
 
# Use the Broadcom SOC Pin numbers  
# Setup the Pin with Internal pullups enabled and PIN in reading mode.  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
 
# Our function on what to do when the button is pressed  
def Shutdown(channel):  
    global presses
    global press_time

    print "Button"

    # We're going to look for 3 fast presses to shut things down

    if (time.time() - press_time > 3):
        presses = 0
        press_time = time.time()

    presses = presses + 1
    if presses >= 5:
        if (time.time() - press_time) < 3:
            print "5"
            #os.system("sudo shutdown -h now")  

 
# Add our function to execute when the button pressed event happens  
GPIO.add_event_detect(18, GPIO.FALLING, callback = Shutdown, bouncetime = 500)  
 
# Now wait!  
while 1:  
    time.sleep(1)
