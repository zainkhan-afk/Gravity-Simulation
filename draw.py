import numpy as np
import cv2

class Draw:
	def __init__(self, width, height):
		self.height = height
		self.width = width

		self.clear_canvas()

	def clear_canvas(self):
		self.canvas = np.zeros((self.height, self.width, 3)).astype("uint8")

	def draw_planets(self, planets):
		for planet in planets:
			x = int(planet.pos.x)
			y = int(planet.pos.y)

			cv2.circle(self.canvas, (x, y), planet.radius, planet.color, -1)
			cv2.circle(self.canvas, (x, y), planet.radius, (255, 255, 255), 1)
			cv2.polylines(self.canvas, [np.array(planet.tail)], False, planet.color, 1)

			# ang = planet.acc.angle
			# x2 = int(np.cos(ang)*15)+x
			# y2 = int(np.sin(ang)*15)+y

			# cv2.line(self.canvas, (x, y), (x2, y2), (255, 0, 0), 2)

			# ang = planet.vel.angle
			# x2 = int(np.cos(ang)*15)+x
			# y2 = int(np.sin(ang)*15)+y

			# cv2.line(self.canvas, (x, y), (x2, y2), (0, 255, 0), 2)

	def render(self):
		cv2.imshow("canvas", self.canvas)
		return cv2.waitKey(30)
