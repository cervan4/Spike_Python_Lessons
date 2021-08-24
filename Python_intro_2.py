#imports
from spike import PrimeHub, LightMatrix, Button, StatusLight, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

#objects 
driving_base = PrimeHub()
movement_motors = MotorPair('C','D')
distance_sensor = DistanceSensor('F')
lifting_arm = Motor("E")

#execute
"""
driving_base.light_matrix.show_image('HAPPY')
#movement_motors.move(20,'cm', 0)
movement_motors.set_default_speed(20)
lifting_arm.run_for_seconds(1,-20)
movement_motors.start()
distance_sensor.wait_for_distance_closer_than(16,'cm')
movement_motors.stop()
lifting_arm.run_for_seconds(1,20)
movement_motors.move(7,'cm',0)
lifting_arm.run_for_seconds(1,-20)
movement_motors.move(-7,'cm',0)

"""

#move motors with rotations
"""
lifting_arm.run_for_rotation(0.2,20)
"""

#move motors with degree
"""
lifting_arm.run_for_degree(40,-20)
"""

#move motors to position
lifting_arm.run_to_position(0,"shortest path",20)
#you can substitute 'shortest path' with 'clockwise' or 'counterclockwise'

#Tank Drive

movement_motors.move_tank(20,'cm',50,30)