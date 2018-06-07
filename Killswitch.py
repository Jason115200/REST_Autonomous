import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_14", GPIO.IN)
while 1:
    if GPIO.input("P8_14"):
        print("HIGH")
        answer = raw_input ("ask me something: ")
        print answer
    else:
        print("LOW")
        break