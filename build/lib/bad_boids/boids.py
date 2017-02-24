"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

class Boids(object):
    def __init__(self,boid_number,move_to_middle_strength,alert_distance,formation_flying_distance,formation_flying_strength,
                 x_position_min,x_position_max,y_position_min,y_position_max,
                 x_velocity_min,x_velocity_max,y_velocity_min,y_velocity_max):
        self.boid_number = boid_number
        self.move_to_middle_strength = move_to_middle_strength
        self.alert_distance = alert_distance
        self.formation_flying_distance = formation_flying_distance
        self.formation_flying_strength = formation_flying_strength
        self.x_positions = [random.uniform(x_position_min,x_position_max) for boid_index in range(boid_number)]
        self.y_positions = [random.uniform(y_position_min,y_position_max) for boid_index in range(boid_number)]
        self.x_velocities = [random.uniform(x_velocity_min,x_velocity_max) for boid_index in range(boid_number)]
        self.y_velocities = [random.uniform(y_velocity_min,y_velocity_max) for boid_index in range(boid_number)]
        self.boids = (self.x_positions,self.y_positions,self.x_velocities,self.y_velocities) # to be used in adapted regression test
        self.all_the_boids = range(self.boid_number)
    
    def fly_to_middle(self):
            for i in self.all_the_boids:
                for j in range(self.boid_number):
                    self.x_velocities[i]+=(self.x_positions[j]-self.x_positions[i])*self.move_to_middle_strength/self.boid_number
                    self.y_velocities[i]+=(self.y_positions[j]-self.y_positions[i])*self.move_to_middle_strength/self.boid_number
            
    # Fly away from nearby boids
    def fly_away(self):
        for i in self.all_the_boids:
            for j in self.all_the_boids:
                if (self.x_positions[j]-self.x_positions[i])**2 + (self.y_positions[j]-self.y_positions[i])**2 < self.alert_distance:
                    self.x_velocities[i]+=self.x_positions[i]-self.x_positions[j]
                    self.y_velocities[i]+=self.y_positions[i]-self.y_positions[j]

    # Try to match speed with nearby boids
    def match_speed(self):
            for i in self.all_the_boids:
                for j in self.all_the_boids:
                    if (self.x_positions[j]-self.x_positions[i])**2 + (self.y_positions[j]-self.y_positions[i])**2 < self.formation_flying_distance:
                        self.x_velocities[i]+=(self.x_velocities[j]-self.x_velocities[i])*self.formation_flying_strength/self.boid_number
                        self.y_velocities[i]+=(self.y_velocities[j]-self.y_velocities[i])*self.formation_flying_strength/self.boid_number
    # Move according to velocities
    def move(self):
        for i in self.all_the_boids:
            self.x_positions[i]+=self.x_velocities[i]
            self.y_positions[i]+=self.y_velocities[i]
    
    def update_boids(self):
        # Calling the following methods will update the positions of the boids:
        
        self.fly_to_middle()
        self.fly_away()
        self.match_speed()
        self.move()        
                
    def animate(self,frame):
       self.update_boids()
       self.scatter.set_offsets(list(zip(self.x_positions,self.y_positions)))
        
    def visuals(self,x_axis_min,x_axis_max,y_axis_min,y_axis_max,animation_frames,animation_interval):
        figure=plt.figure()
        axes=plt.axes(xlim=(x_axis_min,x_axis_max), ylim=(y_axis_min,y_axis_max))
        self.scatter=axes.scatter(self.x_positions,self.y_positions)

        anim = animation.FuncAnimation(figure, self.animate,
                                       frames=animation_frames, interval=animation_interval)
        anim
        plt.show()