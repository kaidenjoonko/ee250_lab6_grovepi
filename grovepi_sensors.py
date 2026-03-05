# lab 6: grovepi sensors
# team members: Kaiden Joon Ko

import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# sensor ports
us = 2
pot = 0
grovepi.pinMode(pot, "INPUT")

# clear lcd
setText("")
setRGB(0, 255, 0)

while True:
    try:
        # read sensors
        dist = grovepi.ultrasonicRead(us)
        thresh = grovepi.analogRead(pot)

        # build top line
        if dist < thresh:
            top = str(thresh) + " OBJ PRES"
        else:
            top = str(thresh) + " "

        # build bottom line
        bot = str(dist)

        # pad lines to clear leftover chars
        top = top.ljust(16)
        bot = bot.ljust(16)

        # update lcd
        setText_norefresh(top + "\n" + bot)

        time.sleep(0.2)

    except KeyboardInterrupt:
        setText("")
        setRGB(0, 0, 0)
        break
    except IOError:
        print("Error")

