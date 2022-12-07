from planet import Planet
from draw import Draw
from settings import *
from physics import Physics



all_planets = []


p = Planet(x = WIDTH//2, y = HEIGHT//2, mass = 100000)
p.radius = 30
all_planets.append(p)
for i in range(NUM_PLANETS):
	p = Planet()
	p.randomize_acceleration()
	all_planets.append(p)

renderer = Draw(WIDTH, HEIGHT)
physics_solver = Physics()
while True:
	renderer.clear_canvas()

	physics_solver.solve_physics(all_planets)

	renderer.draw_planets(all_planets)
	k = renderer.render()
	if k == ord("q"):
		break