import MotorModule
import GPSModule
import UltrasonicModule

while 1: 
        answer = raw_input("what would you like to do: ")
    
        if answer =='stop':
                print "Ok!"
                neutral_motors()
                wheels_stop()
        
                GPIO.output(Range_pin,GPIO.LOW)
                GPIO.cleanup()
                break
                
            #elif answer == '':  #input answer and functions for whatever test that needs to be done
                #functions
    
