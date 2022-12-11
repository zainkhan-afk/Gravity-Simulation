import numpy as np
import random

class Vector:
	def __init__(self, x = None, y = None, angle = None, magnitude = None, randomize = False, random_range = [0, 1]):
		self.x = x
		self.y = y
		self.angle = angle
		self.magnitude = magnitude

		if randomize:
			RANGE = random_range[1] - random_range[0]
			self.x = random_range[1] - RANGE*random.random()
			self.y = random_range[1] - RANGE*random.random()
			self.get_magnitude()
			self.get_angle()

		else:
			if x != None and y != None:
				self.get_magnitude()
				self.get_angle()
			else:
				self.calcualte_cart()

	def get_magnitude(self):
		self.magnitude = np.sqrt(self.x**2 + self.y**2)
		return self.magnitude

	def get_angle(self):
		self.angle = np.arctan2(self.y, self.x)
		return self.angle

	def calcualte_cart(self):
		self.x = self.magnitude*np.cos(self.angle)
		self.y = self.magnitude*np.sin(self.angle)

	def add(self, other):
		return Vector(x = self.x + other.x, y = self.y + other.y)

	def zero(self):
		self.x = 0
		self.y = 0
		self.angle = 0
		self.magnitude = 0

	def clamp(self, MIN, MAX):
		if self.magnitude>MAX:
			self.magnitude = MAX
		if self.magnitude<MIN:
			self.magnitude = MIN

		return Vector(angle = self.angle, magnitude = self.magnitude)

	def normalize(self):
		return Vector(x = self.x/self.magnitude, y = self.y/self.magnitude)

	def rotate(self, angle, degrees = True):
		if degrees:
			angle = angle/180*np.pi
		return Vector(magnitude = self.magnitude, angle = self.angle + angle)

	def __str__(self):
		return f"X: {self.x}, Y: {self.y}, Magnitude: {self.magnitude}, Angle: {self.angle}"

	def __mul__(self, value):
		return Vector(x = self.x*value, y = self.y*value)

	def __add__(self, other):
		return Vector(x = self.x+other.x, y = self.y+other.y)

	def __sub__(self, other):
		return Vector(x = self.x-other.x, y = self.y-other.y)