from particle import Particle as Planet
from draw import Draw
from settings import *
from physics import Physics



all_planets = []


p = Planet(x = WIDTH//2, y = HEIGHT//2, mass = 1000)
p.radius = 30
all_planets.append(p)

for i in range(NUM_PLANETS):
	p = Planet()
	p.randomize_acceleration()
	all_planets.append(p)

# p = Planet(x = WIDTH//2, y = HEIGHT//2)
# all_planets.append(p)

# p = Planet(x = WIDTH//2, y = HEIGHT//2 - 30)
# all_planets.append(p)

# p = Planet(x = WIDTH//2, y = HEIGHT//2 + 60)
# all_planets.append(p)

renderer = Draw(WIDTH, HEIGHT)
physics_solver = Physics()
while True:
	# print()
	renderer.clear_canvas()

	all_planets = physics_solver.solve_physics(all_planets)

	renderer.draw(all_planets)
	k = renderer.render()
	if k == ord("q"):
		break