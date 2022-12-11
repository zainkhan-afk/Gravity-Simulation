from utils import *
from vector import Vector
import numpy as np

class Physics:
	def __init__(self):
		# Real Units 6.6743 × 10-11 m3 kg-1 s-2
		self.G = 6.6743e1

	def calculate_force(self, p1, p2):
		direction = p1.pos - p2.pos
		R = direction.magnitude
		if R<max(p1.radius,p2.radius):
			# mag = -self.G*p1.mass*p2.mass/R**2
			# F = direction.normalize()*mag*-1
			F = p2.acc*p2.mass
			return F, True
		mag = -self.G*p1.mass*p2.mass/R**2
		F = direction.normalize()*mag
		return F, False

	def calculate_orbital_velocity(self, p1, p2):
		direction = p1.pos - p2.pos
		R = direction.magnitude

		v = np.sqrt(self.G*p1.mass/R)
		vel = Vector(magnitude = v, angle = np.pi/2)
		return vel

	def solve_physics(self, planets):
		planets_left = []
		destroyed_planets = []
		collision_pairs = []

		for p1 in planets:
			collision = False
			for p2 in planets:
				if p1 == p2:
					continue
				if [p1, p2] in collision_pairs or [p2, p1] in collision_pairs:
					collision = True
					continue

				direction = p1.pos - p2.pos
				R = direction.magnitude

				if R<max(p1.radius,p2.radius):
					collision_pairs.append([p1, p2])
					collision = True

			if not collision:
				planets_left.append(p1)

		for pair in collision_pairs:
			p1, p2 = pair
			
			if p1.mass>p2.mass:
				p1.update(p2.acc*p2.mass)
				p1.mass += p2.mass
				p1.radius += p2.mass//25
				planets_left.append(p1)
			else:
				p2.update(p1.acc*p1.mass)
				p2.mass += p1.mass
				p2.radius += p1.mass//25
				planets_left.append(p2)

		
		for p1 in planets_left:
			F = Vector(x = 0, y = 0)
			for p2 in planets_left:
				if p1 == p2:
					continue

				f, collision = self.calculate_force(p1, p2)				
				F = F.add(f)
			p1.update(F)

		return planets_left