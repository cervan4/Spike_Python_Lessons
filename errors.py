
#imports
from spike import PrimeHub, LightMatrix, Button, StatusLight, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

#objects 
hub = PrimeHub()
wheels = MotorPair('C','D')
favorite_number = 5

#run code
hub.light_matrix.show_image('HAPPY')
#print('My favorite number is'+ str(favorite_number))
#print('My favorite number is', favorite_number)
if favorite_number == 5:
    print('Yes my favorite number')
