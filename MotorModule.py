import Adafruit_BBIO.PWM as PWM
import time

#The number you want to set to woudl equal on the range of 50 - 130. 95 being neautral >95 is backwards and <95 is forwards
#The further this number is away from 95 the faster it gets
#110 is a decent speed backwards and 80 for forwards.

right_wheel_motor_pin = "P8_13"
left_wheel_motor_pin = "P9_14"
steer_pin = "P9_42"

duty_min = 3
duty_max = 14.5
duty_span = duty_max - duty_min

#Motor 1
angle = 95  #NEUTRAL ANGLE
angle_f = float(angle)
duty = 100 - ((angle_f / 180) * duty_span + duty_min)

#Motor 2 accounts for speed diff
angle_2 = angle_f -1
duty2 = 100 - (((angle_2 / 180)) * duty_span + duty_min)



def start_motors():
    print 'Starting Motors and Steering Servo \n'
    PWM.start(right_wheel_motor_pin, (100-duty_min), 60.0, 1)
    PWM.start(left_wheel_motor_pin, (100-duty_min), 60.0, 1)
    PWM.start(steer_pin, (100-duty_min), 60.0, 1)  #Initializes motors to start sending signal

def neutral_motors():
    print 'Setting Neutral \n'
    PWM.set_duty_cycle(left_wheel_motor_pin, duty)  #Sets it to neutral so it can go forwards/backwards
    PWM.set_duty_cycle(right_wheel_motor_pin, duty2)
    PWM.set_duty_cycle(steer_pin, duty)  #Must set to Neutral when switching direction or starting motors first time

def wheels_backwards():
    backwards = 110 #ANGLE YOU WANT IT TO SET TO SEE LINE 4
    
    bf = float(backwards)
    bf2 = bf - 1 #adjusting for difference between speeds of motors. 
    
    bd = 100 - ((bf / 180) * duty_span + duty_min)
    bd2 = 100 - ((bf2 / 180 ) * duty_span + duty_min)
    print 'Going Backwards \n'
    PWM.set_duty_cycle(left_wheel_motor_pin, bd) 
    PWM.set_duty_cycle(right_wheel_motor_pin, bd2) #Wheels go back
    
def wheels_forwards():
    forward = 80 #ANGLE YOU WANT IT TO SET TO SEE LINE 4
    
    ff = float(forward)
    ff2 = ff - 1 #adjusting for difference between speeds of motors. 
    
    fd = 100 - ((ff / 180) * duty_span + duty_min)
    fd2 = 100 - ((ff2 / 180 ) * duty_span + duty_min)
    print 'Going Forward \n'
    PWM.set_duty_cycle(left_wheel_motor_pin, fd) 
    PWM.set_duty_cycle(right_wheel_motor_pin, fd2)     #Wheels go forward

def wheels_stop():  #sets to neutral and cleans PWM
    print 'STOPPING...'
    PWM.set_duty_cycle(left_wheel_motor_pin, duty) 
    PWM.set_duty_cycle(right_wheel_motor_pin, duty2)
    PWM.set_duty_cycle(steer_pin, duty) 
    
    PWM.stop(left_wheel_motor_pin)
    PWM.stop(right_wheel_motor_pin)
    PWM.stop(steer_pin)
    
    PWM.cleanup()    
    
def turn_right():
    print 'Turning Right \n'
    turn_r = 170
    TR = float(turn_r)
    right = 100 - ((TR / 180 ) * duty_span + duty_min)
    PWM.set_duty_cycle(steer_pin, right)

def turn_left():
    print 'Turning Left \n'
    turn_l = 10
    TL = float(turn_l)
    left = 100 - ((TL / 180 ) * duty_span + duty_min)
    PWM.set_duty_cycle(steer_pin, left)

def center_turn():
    print 'Turning Straight \n'
    turn_c = 90
    TC = float(turn_c)
    center = 100 - ((TC / 180 ) * duty_span + duty_min)
    PWM.set_duty_cycle(steer_pin, center)    


#Should go forwards, then turn right then stop
#Make sure to comment out the code below when used as a library, as it is only for testing purposes
#https://en.wikibooks.org/wiki/Python_Programming/Exceptions
#^^^if you want to learn more about "try and except" cases. Useful if theres a consistant error such as runtime error shown below
try:
    start_motors()
    neutral_motors()
    wheels_forwards()
    time.sleep(2)
    turn_right()
    time.sleep(4)
    neutral_motors()
    wheels_stop()
except RuntimeError:
    print 'Cut and Paste all 3 PWM start lines (29, 30, 31 in def start). Should fix it. Basically a problem with BeagleBoneBlack PWM pins not liking to cooperate'    
    