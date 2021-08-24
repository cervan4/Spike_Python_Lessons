#imports
from spike import PrimeHub, LightMatrix, Button, StatusLight, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

#objects 
driving_base = PrimeHub()
movement_motors = MotorPair('C','D')
distance_sensor = DistanceSensor('F')

#execute
driving_base.light_matrix.show_image('HAPPY')
#movement_motors.move(20,'cm', 0)
movement_motors.start()
distance_sensor.wait_for_distance_closer_than(15,'cm')
movement_motors.stop()