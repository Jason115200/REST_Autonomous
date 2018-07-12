from MotorModule import *
from UltrasonicModule import *
killswitch = "P8_14"
GPIO.setup(killswitch, GPIO.IN)

while 1:
    if GPIO.input("P8_14"):
    #run code
        start_motors()
        neutral_motors()
        wheels_forwards()
        
        
        if ultrasonic_frontCenter_distance <= 30 and ultrasonic_frontLeft_distance <= 30 and ultrasonic_frontRight_distance <= 30:
            print('WE ARE SURROUNDED')
            print('Front Left', ultrasonic_frontLeft_distance, 'Front Center', ultrasonic_frontCenter_distance, 'Front Right', ultrasonic_frontRight_distance)
            stop()
            pass
        
        elif ultrasonic_frontCenter_distance >= 30 and ultrasonic_frontLeft_distance >= 30 and ultrasonic_frontRight_distance >= 30:
            print('Free to move')
            print('Front Left', ultrasonic_frontLeft_distance, 'Front Center', ultrasonic_frontCenter_distance, 'Front Right', ultrasonic_frontRight_distance)
            forward()
            pass
        
        elif ultrasonic_frontLeft_distance <= 30:
            print('Object detected to the left')
            slowforward()
            print('Front Left', ultrasonic_frontLeft_distance, 'Front Center', ultrasonic_frontCenter_distance, 'Front Right', ultrasonic_frontRight_distance)
            turn_right()
            pass
        
        elif ultrasonic_frontRight_distance <= 30:
            print('Object detected to the right')
            slowforward()
            print('Front Left', ultrasonic_frontLeft_distance, 'Front Center', ultrasonic_frontCenter_distance, 'Front Right', ultrasonic_frontRight_distance)
            turn_left()
            pass
    else:
        #While low
        print 'Killswitch Activated'
        start_motors()
        wheels_stop()
        break
    
