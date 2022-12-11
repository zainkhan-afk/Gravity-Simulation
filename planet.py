import numpy as np
from vector import Vector
import random
from settings import *

class Planet:
	def __init__(self, x = None, y = None, mass = None):
		if x != None and y!= None:
			self.pos = Vector(x = x, y = y)
		else:
			self.pos = Vector(randomize = True, random_range = [0, HEIGHT])
		self.prev_pos = self.pos
		self.vel = Vector(x = 0, y = 0)
		self.acc = Vector(x = 0, y = 0)
		self.f   = Vector(x = 0, y = 0)

		self.mass = mass
		self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

		self.tail_size = 15
		self.tail = []


		if self.mass == None:
			self.mass = random.randint(10, 100)
			
		self.radius = self.mass//10


	def set_velocity(self, x, y):
		self.vel = Vector(x = x, y = y)

	def set_acceleration(self, x, y):
		self.acc = Vector(x = x, y = y)

	def randomize_velocity(self):
		self.vel = Vector(randomize = True, random_range = [-50, 50])

	def randomize_acceleration(self):
		self.acc = Vector(randomize = True, random_range = [-50, 50])

	def update(self, F):
		self.f = F
		self.a = Vector(x = F.x/self.mass, y = F.y/self.mass)

		self.vel = self.vel + self.acc * DELTA_T
		
		temp = self.pos
		# self.pos = self.pos + self.vel * DELTA_T 
		
		self.pos = self.pos  * 2 - self.prev_pos + self.acc * (DELTA_T**2) # Verlet integration method of position update.
		self.prev_pos = temp
		self.acc = self.a

		# Uncomment for wrapping motion
		# if self.pos.x>WIDTH:
		# 	self.pos.x = 0
		# if self.pos.x<0:
		# 	self.pos.x = WIDTH

		# if self.pos.y>HEIGHT:
		# 	self.pos.y = 0
		# if self.pos.y<0:
		# 	self.pos.y = HEIGHT

		self.tail.append([int(self.pos.x), int(self.pos.y)])

		while len(self.tail)>self.tail_size:
			self.tail.reverse()
			self.tail.pop()
			self.tail.reverse()

	def __str__(self):
		print(self.vel)
		print(self.pos)
		return f"Planet - Mass: {self.mass}, Radius: {self.radius}"