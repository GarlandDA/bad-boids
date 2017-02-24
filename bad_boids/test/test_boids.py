import yaml
import os
from ..boids import Boids
from nose.tools import assert_equal
import random
import numpy as np
from unittest.mock import patch
import unittest.mock as mock

def test_Boids():
    flock = Boids(boid_number=10,move_to_middle_strength=0.1,alert_distance=100,formation_flying_distance=900,formation_flying_strength=0.5,
                 x_position_min=0,x_position_max=200,y_position_min=-5,y_position_max=5,
                 x_velocity_min=-10,x_velocity_max=30,y_velocity_min=-20,y_velocity_max=20)
	# make sure the class is initialised correctly:			 
    assert_equal(flock.boid_number,10)
    assert_equal(flock.move_to_middle_strength,0.1)
    assert_equal(flock.all_the_boids,range(10))

def test_fly_to_middle():
	flock = Boids(boid_number=2,move_to_middle_strength=0.1,alert_distance=100,formation_flying_distance=900,formation_flying_strength=0.5,
                 x_position_min=0,x_position_max=200,y_position_min=-5,y_position_max=5,
                 x_velocity_min=-10,x_velocity_max=30,y_velocity_min=-20,y_velocity_max=20)
	# make sure self.all_the_boids corresponds to the right thing, i.e. range(self.boid_number)
	np.testing.assert_array_equal(range(2),flock.all_the_boids)
	assert_equal(flock.move_to_middle_strength,0.1)
	# make sure arrays are updated to what we expect them to - #1
	flock.x_velocities = [1, 2]
	flock.x_positions = [2, 1]
	flock.fly_to_middle()
	np.testing.assert_array_almost_equal(flock.x_velocities,[0.95,  2.05])
	# make sure arrays are updated to what we expect them to - #2
	flock.x_velocities = [5, 2]
	flock.x_positions = [2, 46]
	flock.fly_to_middle()
	np.testing.assert_array_almost_equal(flock.x_velocities,[7.2, -0.2])
	
def test_fly_away():
	flock = Boids(boid_number=2,move_to_middle_strength=0.1,alert_distance=100,formation_flying_distance=900,formation_flying_strength=0.5,
                 x_position_min=0,x_position_max=200,y_position_min=-5,y_position_max=5,
                 x_velocity_min=-10,x_velocity_max=30,y_velocity_min=-20,y_velocity_max=20)
	# make sure self.all_the_boids corresponds to the right thing, i.e. range(self.boid_number)
	np.testing.assert_array_equal(range(2),flock.all_the_boids)
	assert_equal(flock.alert_distance,100)
	# make sure arrays are updated to what we expect them to - #1
	flock.x_velocities = [1, 2]
	flock.x_positions = [2, 1]
	flock.fly_away()
	np.testing.assert_array_almost_equal(flock.x_velocities,[2,  1])
	# make sure arrays are updated to what we expect them to - #2
	flock.x_velocities = [5, 2]
	flock.x_positions = [2, 46]
	flock.fly_away()
	np.testing.assert_array_almost_equal(flock.x_velocities,[5, 2])

def test_match_speed():
	flock = Boids(boid_number=2,move_to_middle_strength=0.1,alert_distance=100,formation_flying_distance=900,formation_flying_strength=0.5,
                 x_position_min=0,x_position_max=200,y_position_min=-5,y_position_max=5,
                 x_velocity_min=-10,x_velocity_max=30,y_velocity_min=-20,y_velocity_max=20)
	# make sure self.all_the_boids corresponds to the right thing, i.e. range(self.boid_number)
	np.testing.assert_array_equal(range(2),flock.all_the_boids)
	assert_equal(flock.formation_flying_distance,900)
	assert_equal(flock.formation_flying_strength,0.5)
	# make sure arrays are updated to what we expect them to - #1
	flock.y_velocities = [1, 2]
	flock.match_speed()
	np.testing.assert_array_almost_equal(flock.y_velocities,[1.,  2.] )
	# make sure arrays are updated to what we expect them to - #2
	flock.y_velocities = [14, 15]
	flock.match_speed()
	np.testing.assert_array_almost_equal(flock.y_velocities,[14.,   15.])
	
def test_update_boids():
	flock = Boids(boid_number=2,move_to_middle_strength=0.1,alert_distance=100,formation_flying_distance=900,formation_flying_strength=0.5,
					x_position_min=0,x_position_max=200,y_position_min=-5,y_position_max=5,
					x_velocity_min=-10,x_velocity_max=30,y_velocity_min=-20,y_velocity_max=20)
	# test that update_boids() is called all right
	with mock.patch.object(flock,'update_boids') as mock_update:
		updated = flock.update_boids('')
		mock_update.assert_called_with('')
	# test that fly_to_middle() works
	with mock.patch.object(flock,'fly_to_middle') as mock_middle:
		flown_to_middle = flock.fly_to_middle('')
		mock_middle.assert_called_with('')
	# test that fly_away() works
	with mock.patch.object(flock,'fly_away') as mock_away:
		flown_away = flock.fly_away('')
		mock_away.assert_called_with('')
	# test that match_speed() works
	with mock.patch.object(flock,'match_speed') as mock_match:
		matched = flock.match_speed('')
		mock_match.assert_called_with('')
	# test that move() works
	with mock.patch.object(flock,'move') as mock_move:
		moved = flock.move('')
		mock_move.assert_called_with('')

def test_animate():
	flock = Boids(boid_number=2,move_to_middle_strength=0.1,alert_distance=100,formation_flying_distance=900,formation_flying_strength=0.5,
					x_position_min=0,x_position_max=200,y_position_min=-5,y_position_max=5,
					x_velocity_min=-10,x_velocity_max=30,y_velocity_min=-20,y_velocity_max=20)
	# test that animate() is called correctly
	with mock.patch.object(flock,'animate') as mock_animate:
		animated = flock.animate('frame')
		mock_animate.assert_called_with('frame')