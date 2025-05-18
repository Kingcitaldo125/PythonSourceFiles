import numpy as np
from itertools import combinations_with_replacement as cwr

def ray_intersects_cube(ray_origin, ray_direction, cube_min, cube_max):
    # Ensure the direction components are not exactly zero to avoid division by zero
    ray_direction = np.array(ray_direction, dtype=float)
    cube_min = np.array(cube_min)
    cube_max = np.array(cube_max)

    inv_dir = 1.0 / np.where(ray_direction != 0, ray_direction, np.inf)
    print("inv_dir", inv_dir)

    t_min = (cube_min - ray_origin) * inv_dir
    t_max = (cube_max - ray_origin) * inv_dir
    print("t_min", t_min)
    print("t_max", t_max)

    t1 = np.minimum(t_min, t_max)
    t2 = np.maximum(t_min, t_max)
    print("t1", t1)
    print("t2", t2)

    t_entry = max(t1)
    t_exit = min(t2)
    print("t_entry", t_entry)
    print("t_exit", t_exit)

    if t_entry <= t_exit and t_exit >= 0:
        return True, t_entry, t_exit  # Collision detected with entry and exit distances
    return False, None, None

# Test Example
ray_origin = np.array([1, 1, 1])
ray_direction = np.array([1, 1, 1])
cube_min = np.array([2, 2, 2])
cube_max = np.array([4, 4, 4])

matx = list(cwr(np.array([-1.0,0.0,1.0]),3))

for idx,dir in enumerate(matx):
	print(idx)
	hit, t_entry, t_exit = ray_intersects_cube(ray_origin, dir, cube_min, cube_max)
	if hit:
		print(f"Ray intersects the cube at t_entry={t_entry} and exits at t_exit={t_exit}")
	else:
		print("Ray does not intersect the cube.")
