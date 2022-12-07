from utils import *
from vector import Vector
import numpy as np

class Physics:
	def __init__(self):
		# Real Units 6.6743 × 10-11 m3 kg-1 s-2
		self.G = 6.6743e1

	def calculate_forces(self, p1, p2):
		direction = p1.pos - p2.pos
		R = direction.magnitude
		if R<max(p1.radius,p2.radius):
			return Vector(x = 0, y = 0)
		mag = -self.G*p1.mass*p2.mass/R**2
		F = direction.normalize()*mag
		return F

	def solve_physics(self, planets):
		planets_left = []
		pairs_solved = []
		
		for p1 in planets:
			F = Vector(x = 0, y = 0)
			for p2 in planets:
				if p1 == p2:
					continue

				f = self.calculate_forces(p1, p2)

				F = F.add(f)
			p1.update(F)
			planets_left.append(p1)