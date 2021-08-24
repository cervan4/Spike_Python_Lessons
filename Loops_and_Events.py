#imports
from spike import PrimeHub, LightMatrix, Button, StatusLight, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

#objects 
hub = PrimeHub()
movement_motors = MotorPair('C','D')
distance_sensor = DistanceSensor('F')
lifting_arm = Motor("E")

#execute
driving_base.light_matrix.show_image('HAPPY')

#for Loop 
"""
for i in range (0,8,1):
    lifting_arm.run_for_rotation(-0.2,20)
    lifting_arm.run_for_rotation(0.2,20)
    
"""
while True: 
    hub.left_button.wait_until_pressed()
    #while loop
    x = 0
    while x < 8 :
        lifting_arm.run_for_rotation(-0.2,20)
        lifting_arm.run_for_rotation(0.2,20)
        #x = x + 1
        x+1 #This is how it will incroment
