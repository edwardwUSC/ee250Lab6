#Team Members
#Lindsay Best
#Edward Whitesel



import sys
sys.path.append('~/Dexter/GrovePi/Software/Python')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")
setRGB(0,255,0)
while True:
  try:
    #gets distance in cm
    distance=grovepi.ultrasonicRead(ultrasonic_ranger)
    
    #gets pot as range of 0 to 1024
    pot_read = grovepi.analogRead(potentiometer)
    
    #convert to threhold 0-517
    threshhold = 517*pot_read/1024
    
    # TODO: format LCD text according to threshhold
    if(distance < threshhold):
         setRGB(255,0,0)#red
         #setText_norefresh for text ouput without clearing screen
         setText_norefresh(str(threshhold)+" cm "+"OBJ PRESS\n"+str(distance)+" cm")
    else:
         setRGB(0,255,0)#green
         setText_norefresh(str(threshhold)+" cm\n"+str(distance)+" cm")
  except IOError:
    print("Error")
