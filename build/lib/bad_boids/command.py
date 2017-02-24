import yaml
from .boids import Boids # Note python 3 relative import

config=yaml.load(open("config.yaml")) # load configuration file

# read configuration file constants
# parameters for the boids
boid_number = config["boid_number"]

x_position_min = config["x_position_min"]
x_position_max = config["x_position_max"]
y_position_min = config["y_position_min"]
y_position_max = config["y_position_max"]

x_velocity_min = config["x_velocity_min"]
x_velocity_max = config["x_velocity_max"]
y_velocity_min = config["y_velocity_min"]
y_velocity_max = config["y_velocity_max"]

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

def process():
   
    # create an instance of the Boids class
    flock = Boids(boid_number,move_to_middle_strength,alert_distance,formation_flying_distance,formation_flying_strength,
                 x_position_min,x_position_max,y_position_min,y_position_max,
                 x_velocity_min,x_velocity_max,y_velocity_min,y_velocity_max)
    
    flock.visuals(x_axis_min,x_axis_max,y_axis_min,y_axis_max,animation_frames,animation_interval)    
    
if __name__ == "__main__":
    process()