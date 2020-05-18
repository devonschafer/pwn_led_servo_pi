#This code uses python3. Be sure to adapt this code for python2, or just use python3 :).
#This code runs on Raspberry Pi.

#import RPi.GPIO module.
import RPi.GPIO as GPIO
#import the time module.
import time
#import the ramdon module.
import random
#import the math module.
import math
#set GPIO warnings to False to eliminate possible errors.
GPIO.setwarnings(False)
#set mode to BOARD, you can change this to BCM if you like. I do not.
GPIO.setmode(GPIO.BOARD)
#setup the GPIO pins you want to use.
#pin 8 for the servo.
GPIO.setup(8, GPIO.OUT)
#pin 10 for the LED.
GPIO.setup(10, GPIO.OUT)

#this sets the pin and the Hertz (frequency).
#my servo uses 50hz.
p = GPIO.PWM(8, 50)
#led looks better at 120hz.
q = GPIO.PWM(10, 120)

#this sets the PWM to a value between 0 and 100. If you wanted an LED to be half on when code starts
# you would set this to 50 etc. (0 being off, 100 being full 3.3v form GPIO).
p.start(0)
q.start(0)

#This frange stuff is for the servo motor to produce smaller increments for smoother servo control
#Looks confusing, just dig into it.
def frange_up(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step
        
def servo_up():
    for i in frange_up(2.0, 12.0, .1):
        p.ChangeDutyCycle(round(i, 2))
        print(round(i, 2))
        time.sleep(.025)
        
def frange_down(start, stop, step):
    i = start
    while i > stop:
        yield i
        i += step
        
def servo_down():
    for i in frange_down(12.0, 2.0, -0.1):
        p.ChangeDutyCycle(round(i, 2))
        print(round(i, 2))
        time.sleep(.025)

#This function is for the LED.
def led_up():
    for i in frange_up(0.0, 100.0, 2):
        q.ChangeDutyCycle(round(i, 2))
        print(round(i, 2))
        time.sleep(.025)

def led_down():
    for i in frange_down(100.0, 0.0, -2):
        q.ChangeDutyCycle(round(i, 2))
        print(round(i, 2))
        time.sleep(.025)

#this is the run loop. Uncomment whichever function you would like to use.
try:
    while True:
        servo_up()
        servo_down()
        #led_up()
        #led_down()
        #time.sleep(.1)

        
except KeyboardInterrupt:
    p.stop()
    q.stop()
    GPIO.cleanup()
