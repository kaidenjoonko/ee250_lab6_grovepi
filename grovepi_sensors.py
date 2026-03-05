# Lab 6: GrovePi Sensors
# Team Members: Kaiden Joonko, <partner name here>

import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connected to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer, "INPUT")

# clear lcd screen before starting main loop
setText("")
setRGB(0, 255, 0)

while True:
    try:
        # Read distance value from Ultrasonic Ranger
        distance = grovepi.ultrasonicRead(ultrasonic_ranger)

        # Read threshold from potentiometer
        threshold = grovepi.analogRead(potentiometer)

        # Format LCD text according to threshold
        if distance < threshold:
            top_line = str(threshold) + " OBJ PRES"
        else:
            top_line = str(threshold) + " "

        bottom_line = str(distance)

        lcd_text = top_line + "\n" + bottom_line
        setText_norefresh(lcd_text)

        time.sleep(0.2)

    except KeyboardInterrupt:
        setText("")
        setRGB(0, 0, 0)
        break
    except IOError:
        print("Error")
