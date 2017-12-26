#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gpiozero import Button
import time
import subprocess
from signal import pause


logtext = ""
localtime = ""

def putinlog(logtext):
            localtime = time.asctime( time.localtime(time.time()) )
            log= open('logfile.txt', 'a')
            log.write('\n' + localtime + " --- " + logtext)
            log.close()
def button_press():

        putinlog("Button pressed")
        subprocess.call(["raspistill", "-o", "/home/pi/testpics/Latest.jpg"])
        subprocess.call(["mpack", "-s", "[Test] Hey there! Someone just put this in the foodbox. Come and get it before it's gone!", "/home/pi/testpics/Latest.jpg", "trigger@applet.ifttt.com"])
        putinlog("Image posted")

def say_bye():

        putinlog("Button released")

button = Button(21)

button.when_pressed = button_press
button.when_released = say_bye

pause()
