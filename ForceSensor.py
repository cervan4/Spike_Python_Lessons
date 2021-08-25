#imports
from spike import PrimeHub, LightMatrix, Button, StatusLight, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

#objects 
hub = PrimeHub()
force = ForceSensor('B')
motor = Motor('E')

while True:
    newtons = force.get_force_newton()
    motor.start(speed = newtons*10)