import numpy as np
import cv2

class Draw:
	def __init__(self, width, height):
		self.height = height
		self.width = width

		self.clear_canvas()

	def clear_canvas(self):
		self.canvas = np.zeros((self.height, self.width, 3)).astype("uint8")

	def get_planet_mask(self, planet, planet_mask):
		x = int(planet.pos.x)
		y = int(planet.pos.y)

		cv2.circle(planet_mask, (x, y), planet.radius, (255, 255, 255), -1)

		return planet_mask

	def get_planet_tail(self, planet, planet_tail_mask):
		x = int(planet.pos.x)
		y = int(planet.pos.y)

		cv2.polylines(planet_tail_mask, [np.array(planet.tail)], False, 255, 1)

		return planet_tail_mask

	def draw_planets(self, planets):
		for planet in planets:
			x = int(planet.pos.x)
			y = int(planet.pos.y)

			cv2.circle(self.canvas, (x, y), planet.radius+2, planet.color, -1)
			cv2.polylines(self.canvas, [np.array(planet.tail)], False, planet.color, 3)

		self.canvas = cv2.GaussianBlur(self.canvas,(17,17),0)

		for planet in planets:
			x = int(planet.pos.x)
			y = int(planet.pos.y)

			cv2.circle(self.canvas, (x, y), planet.radius, planet.color, 1)
			cv2.polylines(self.canvas, [np.array(planet.tail)], False, planet.color, 1)




	def render(self):
		cv2.imshow("canvas", self.canvas)
		return cv2.waitKey(30)
