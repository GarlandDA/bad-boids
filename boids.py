"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes
# 1st refactoring step: replacing magic numbers with constants

boid_number = 50

x_position_min = -450.0
x_position_max = 50.0
y_position_min = 300.0
y_position_max = 600.0

x_velocity_min = 0
x_velocity_max = 10.0
y_velocity_min = -20.0
y_velocity_max = 20.0

move_to_middle_strength = 0.01
alert_distance = 100
formation_flying_distance = 10000
formation_flying_strength = 0.125

# variables for the plot and animation
x_axis_min = -500
x_axis_max = 1500
y_axis_min = -500
y_axis_max = 1500
animation_frames = 50
animation_interval = 50

boids_x=[random.uniform(x_position_min,x_position_max) for x in range(boid_number)]
boids_y=[random.uniform(y_position_min,y_position_max) for x in range(boid_number)]
boid_x_velocities=[random.uniform(x_velocity_min,x_velocity_max) for x in range(boid_number)]
boid_y_velocities=[random.uniform(y_velocity_min,y_velocity_max) for x in range(boid_number)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
	xs,ys,xvs,yvs=boids
	# Fly towards the middle
	for i in range(len(xs)):
		for j in range(len(xs)):
			xvs[i]=xvs[i]+(xs[j]-xs[i])*move_to_middle_strength/len(xs)
	for i in range(len(xs)):
		for j in range(len(xs)):
			yvs[i]=yvs[i]+(ys[j]-ys[i])*move_to_middle_strength/len(xs)
	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < alert_distance:
				xvs[i]=xvs[i]+(xs[i]-xs[j])
				yvs[i]=yvs[i]+(ys[i]-ys[j])
	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < formation_flying_distance:
				xvs[i]=xvs[i]+(xvs[j]-xvs[i])*formation_flying_strength/len(xs)
				yvs[i]=yvs[i]+(yvs[j]-yvs[i])*formation_flying_strength/len(xs)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i]=xs[i]+xvs[i]
		ys[i]=ys[i]+yvs[i]


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