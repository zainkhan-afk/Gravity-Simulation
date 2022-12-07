import numpy as np

def get_distance(p1, p2):
	m = np.sqrt((p1.pos.x - p2.pos.x)**2 + (p1.pos.y - p2.pos.y)**2)

	quadrant = get_quadrant(p1, p2)
	
	return m

def get_angle(p1, p2):
	ang = np.arctan2((p1.pos.y - p2.pos.y),(p1.pos.x - p2.pos.x))
	quadrant = get_quadrant(p1, p2)
	
	return ang

def get_quadrant(p1, p2):
	diff_x = p1.pos.x - p2.pos.x
	diff_y = p1.pos.y - p2.pos.y

	if diff_y<=0:
		if diff_x<0:
			return 3

		else:
			return 4
	
	else:
		if diff_x<0:
			return 2

		else:
			return 1