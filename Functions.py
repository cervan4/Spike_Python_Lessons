
#imports
from spike import PrimeHub, LightMatrix, Button, StatusLight, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

#objects 
hub = PrimeHub()
wheels = MotorPair('C','D')

#functions
def right_turn():
    hub.motion_sensor.reset_yaw_angle()
    while hub.motion_sensor.get_yaw_angle() < 90:
        wheels.start(100)
    wheels.stop()

def custom_turn(angle):
    hub.motion_sensor.reset_yaw_angle()
    while hub.motion_sensor.get_yaw_angle() < angle:
        wheels.start(100)
    wheels.stop()

    
hub.light_matrix.show_image('HAPPY')
wheels.set_default_speed(20)
custom_turn(45)