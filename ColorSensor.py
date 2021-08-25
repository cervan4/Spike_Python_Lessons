#imports
from spike import PrimeHub, LightMatrix, Button, StatusLight, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

#objects 
hub = PrimeHub()

color_sensor = ColorSensor('E')
motor = Motor('C')

while True:
    color_sensor.wait_until_color('yellow')
    wait_for_seconds(1)
    motor.run_for_degree(120)
    motor.run_for_degree(-120)
