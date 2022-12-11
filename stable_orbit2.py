from planet import Planet
from draw import Draw
from settings import *
from physics import Physics


renderer = Draw(WIDTH, HEIGHT)
physics_solver = Physics()

all_planets = []


p1 = Planet(x = WIDTH//2, y = HEIGHT//2, mass = 1000)
p1.radius = 30

p2 = Planet(x = WIDTH//3, y = HEIGHT//2, mass = 1)
p2.radius = 10
p2.tail_size = 400


p2.set_acceleration(x = 0, y = 175)

all_planets.append(p1)
all_planets.append(p2)

while True:
	renderer.clear_canvas()

	all_planets = physics_solver.solve_physics(all_planets)
	p1.pos.x = WIDTH//2
	p1.pos.y = HEIGHT//2

	renderer.draw_planets(all_planets)
	k = renderer.render()
	if k == ord("q"):
		break