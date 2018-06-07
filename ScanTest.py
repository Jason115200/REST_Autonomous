import time
import math

import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
#To install...
#https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/installation-on-ubuntu

the_amount_of_times_to_be_looped = 0
Range_pin = "P9_41"
GPIO.setup(Range_pin, GPIO.OUT)
GPIO.output(Range_pin,GPIO.HIGH)

#Starts ranging Ultrasonics
ADC.setup()
#Ultrasonics have to get the reading, scale up the voltage and then scale down to to the bealgebone logic
ultrasonic_frontLeft_data_pin = "P9_40"
ultrasonic_frontCenter_data_pin = "P9_36"
ultrasonic_frontRight_data_pin = "P9_38"




def scan():
    
    while 1:
        
        GPIO.output(Range_pin,GPIO.HIGH) #Allows the ultrasonics to be ranged at the same time

        ultrasonic_frontLeft_value = ADC.read(ultrasonic_frontLeft_data_pin)
        ultrasonic_frontLeft_voltage = ultrasonic_frontLeft_value * 1.8 #1.8V
        ultrasonic_frontLeft_distance = ultrasonic_frontLeft_voltage/0.00699

        
        ultrasonic_frontCenter_value = ADC.read(ultrasonic_frontCenter_data_pin)
        ultrasonic_frontCenter_voltage = ultrasonic_frontCenter_value * 1.8 #1.8V
        ultrasonic_frontCenter_distance = ultrasonic_frontCenter_voltage/0.00699

        ultrasonic_frontRight_value = ADC.read(ultrasonic_frontRight_data_pin)
        ultrasonic_frontRight_voltage = ultrasonic_frontRight_value * 1.8 #1.8V
        ultrasonic_frontRight_distance = ultrasonic_frontRight_voltage/0.00699
        
        
        print('Front Left', ultrasonic_frontLeft_distance, 'Front Center', ultrasonic_frontCenter_distance, 'Front Right', ultrasonic_frontRight_distance)
        GPIO.output(Range_pin,GPIO.LOW)
        time.sleep(2)
        
scan()