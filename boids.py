"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes
# Replace constants by configuration file. This might be the most elegant way of doing it. I'll come back to this if I have time.

import yaml
config=yaml.load(open("config.yaml")) 

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

x_axis_min = config["x_axis_min"]
x_axis_max = config["x_axis_max"]
y_axis_min = config["y_axis_min"]
y_axis_max = config["y_axis_max"]
animation_frames = config["animation_frames"]
animation_interval = config["animation_interval"]

x_positions=[random.uniform(x_position_min,x_position_max) for boid_index in range(boid_number)]
y_positions=[random.uniform(y_position_min,y_position_max) for boid_index in range(boid_number)]
x_velocities=[random.uniform(x_velocity_min,x_velocity_max) for boid_index in range(boid_number)]
y_velocities=[random.uniform(y_velocity_min,y_velocity_max) for boid_index in range(boid_number)]
boids=(x_positions,y_positions,x_velocities,y_velocities)


def update_boids(boids):
    xs,ys,xvs,yvs=boids
    # Fly towards the middle
    for i in range(len(xs)):
        for j in range(len(xs)):
            xvs[i]+=(xs[j]-xs[i])*move_to_middle_strength/len(xs)
            yvs[i]+=(ys[j]-ys[i])*move_to_middle_strength/len(xs)
    # Fly away from nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < alert_distance:
                xvs[i]+=(xs[i]-xs[j])
                yvs[i]+=(ys[i]-ys[j])
    # Try to match speed with nearby boids
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < formation_flying_distance:
                xvs[i]+=(xvs[j]-xvs[i])*formation_flying_strength/len(xs)
                yvs[i]+=(yvs[j]-yvs[i])*formation_flying_strength/len(xs)
    # Move according to velocities
    for i in range(len(xs)):
        xs[i]+=xvs[i]
        ys[i]+=yvs[i]


figure=plt.figure()
axes=plt.axes(xlim=(x_axis_min,x_axis_max), ylim=(y_axis_min,y_axis_max))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(boids[0])


anim = animation.FuncAnimation(figure, animate,
                               frames=animation_frames, interval=animation_interval)

if __name__ == "__main__":
    plt.show()