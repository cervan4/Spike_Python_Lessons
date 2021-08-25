#imports
from spike import PrimeHub, LightMatrix, Button, StatusLight, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

#objects 
hub = PrimeHub()

distance_sensor = DistanceSensor("A")
motor = Motor("F")

while True: 
    dist_cm = distance_sensor.get_distance_cm()

    if dist_cm == None:
        motor.start()

    elif dist_cm >= 10:
        motor.start()

    else: 
        motor.stop()
