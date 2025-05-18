import pygame

from time import sleep
from random import randrange as rr


def gen_food(screen, winx, winy, pellet_size):
	return (rr(pellet_size, winx-pellet_size), rr(pellet_size, winy-pellet_size))

def update_snake_parts(snake_parts, direction, pellet_size, offset, speed=10):
	sp_copy = [[i[0], i[1]] for i in snake_parts]

	for i in range(1, len(snake_parts)):
		if direction == 1: # Up
			snake_parts[i][0] = sp_copy[i - 1][0]
			snake_parts[i][1] = sp_copy[i - 1][1]
		elif direction == 2: # Down
			snake_parts[i][0] = sp_copy[i - 1][0]
			snake_parts[i][1] = sp_copy[i - 1][1]
		elif direction == 3: # Left
			snake_parts[i][0] = sp_copy[i - 1][0]
			snake_parts[i][1] = sp_copy[i - 1][1]
		elif direction == 4: # Right
			snake_parts[i][0] = sp_copy[i - 1][0]
			snake_parts[i][1] = sp_copy[i - 1][1]

	return snake_parts

def main(winx=400,winy=400):
	pygame.display.init()
	screen = pygame.display.set_mode((winx, winy))
	done = False
	sleep_inter = 0.45
	pellet_size = 20

	red = (255,0,0)
	green = (0,255,0)
	snake_parts = [[winx//2, winy//2]]

	# Food pellet pos
	fx = winx//4
	fy = winy//2

	direction = 3 # left
	speed = 10
	offset = 10

	while not done:
		# Check for collision
		hit = False
		snake_head = snake_parts[0]
		for s_part in range(1,len(snake_parts)):
			part = snake_parts[s_part]

			coll_offset = offset*0.8
			xcond1 = snake_head[0] + coll_offset >= part[0]
			xcond2 = snake_head[0] <= part[0] + coll_offset

			if xcond1 and xcond2:
				ycond1 = snake_head[1] + coll_offset >= part[1]
				ycond2 = snake_head[1] <= part[1] + coll_offset

				if ycond1 and ycond2:
					hit = True
					break

		# Hit a section of the body
		if hit:
			print("Hit!")
			sleep(3)
			done = True
			break

		# Hit a wall
		if snake_parts[0][0] <= 0 or snake_parts[0][1] + pellet_size >= winx:
			print("Hit Wall!")
			sleep(3)
			done = True
			break

		if snake_parts[0][1] <= 0 or snake_parts[0][1] + pellet_size  >= winy:
			print("Hit Wall!")
			sleep(3)
			done = True
			break

		snake_parts = update_snake_parts(snake_parts, direction, pellet_size, offset)

		# Move snake head
		if direction == 1: # Up
			snake_parts[0][1] -= speed
		elif direction == 2: # Down
			snake_parts[0][1] += speed
		elif direction == 3: # Left
			snake_parts[0][0] -= speed
		elif direction == 4: # Right
			snake_parts[0][0] += speed

		# Ate a pellet
		if snake_parts[0][0] + pellet_size >= fx and snake_parts[0][0] <= fx + pellet_size:
			if snake_parts[0][1] + pellet_size >= fy and snake_parts[0][1] <= fy + pellet_size:
				npx = 0
				npy = 0

				if direction == 1: # Up
					npx = snake_parts[-1][0]
					npy = snake_parts[-1][1] + offset
				elif direction == 2: # Down
					npx = snake_parts[-1][0]
					npy = snake_parts[-1][1] - offset
				elif direction == 3: # Left
					npx = snake_parts[-1][0] + offset
					npy = snake_parts[-1][1]
				elif direction == 4: # Right
					npx = snake_parts[-1][0] - offset
					npy = snake_parts[-1][1]

				snake_parts.append([npx, npy])

				fx,fy = gen_food(screen, winx, winy, pellet_size)
				sleep_inter = max(sleep_inter - 0.05, 0.05)

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					direction = 1
				elif event.key == pygame.K_DOWN:
					direction = 2
				elif event.key == pygame.K_LEFT:
					direction = 3
				elif event.key == pygame.K_RIGHT:
					direction = 4
				elif event.key == pygame.K_ESCAPE:
					done = True

		screen.fill((0,0,0))

		# Draw pellet
		pygame.draw.rect(screen, red, (fx, fy, pellet_size, pellet_size))

		# Draw snake parts
		for pt in snake_parts:
			pygame.draw.rect(screen, green, (pt[0], pt[1], pellet_size, pellet_size))

		pygame.display.flip()
		sleep(sleep_inter)

	pygame.display.quit()

if __name__ == "__main__":
	main()
