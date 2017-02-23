from boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml

config=yaml.load(open("config.yaml"))

#parameters for the boids
boid_number = config["boid_number"]

x_position_min = config["x_position_min"]
x_position_max = config["x_position_max"]
y_position_min = config["y_position_min"]
y_position_max = config["y_position_max"]

x_velocity_min = config["x_velocity_min"]
x_velocity_max = config["x_velocity_max"]
y_velocity_min = config["y_velocity_min"]
y_velocity_max = config["x_velocity_max"]

move_to_middle_strength = config["move_to_middle_strength"]
alert_distance = config["alert_distance"]
formation_flying_distance = config["formation_flying_distance"]
formation_flying_strength = config["formation_flying_strength"]

# parameters for the animation
x_axis_min = config["x_axis_min"]
x_axis_max = config["x_axis_max"]
y_axis_min = config["y_axis_min"]
y_axis_max = config["y_axis_max"]
animation_frames = config["animation_frames"]
animation_interval = config["animation_interval"]
def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    boids=Boids(boid_number,move_to_middle_strength,alert_distance,formation_flying_distance,formation_flying_strength,
                x_position_min,x_position_max,y_position_min,y_position_max,
                x_velocity_min,x_velocity_max,y_velocity_min,y_velocity_max)
    boids.boids = boid_data
    boids.update_boids()
    for after,before in zip(regression_data["after"],boids.boids):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
	
