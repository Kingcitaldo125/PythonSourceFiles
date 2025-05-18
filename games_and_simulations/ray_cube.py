from math import inf
from pygame.math import Vector3
from itertools import combinations_with_replacement as cwr

def ray_intersects_cube(ray_origin, ray_direction, cube_min, cube_max):
	inv_dir = [1/inf if ray_direction[i] == 0.0 else 1/ray_direction[i] for i in range(3)]
	print(f"inv_dir {inv_dir}")

	t_min = [0 for i in range(3)]
	t_max = [0 for i in range(3)]

	for i in range(3):
		t_min[i] = (cube_min[i] - ray_origin[i]) * inv_dir[i]
		t_max[i] = (cube_max[i] - ray_origin[i]) * inv_dir[i]

	t_entry = min(min(t_min), min(t_max))
	t_exit = max(max(t_min), max(t_max))

	#t_entry = max(t1)
	#t_exit = min(t2)

	if t_entry <= t_exit and t_exit >= 0:
		return True, t_entry, t_exit  # Collision detected with entry and exit distances
	return False, None, None

# Test Example
ray_origin = Vector3(0.0, 0.0, 0.0)
cube_min = Vector3(1.0, 1.0, 1.0)
cube_max = Vector3(2.0, 2.0, 2.0)

matx = list(cwr([-1.0,0.0,1.0,-0.5,0.5],3))

for idx,dir in enumerate(matx):
	print(idx)
	hit, t_entry, t_exit = ray_intersects_cube(ray_origin, dir, cube_min, cube_max)
	if hit:
		print(f"Ray intersects the cube at t_entry={t_entry} and exits at t_exit={t_exit}")
	else:
		print("Ray does not intersect the cube.")
