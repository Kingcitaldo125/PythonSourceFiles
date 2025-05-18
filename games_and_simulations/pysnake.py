import pygame
from random import randrange
import math
import time

def update(segments, velocity, direction):
	prev_seg = [i.copy() for i in segments]

	segments[0][0] += velocity * direction[0]
	segments[0][1] += velocity * direction[1]

	for i in range(1,len(prev_seg)):
		px,py = prev_seg[i - 1]
		segments[i][0] = px
		segments[i][1] = py

	return segments

def main(winx,winy):
	pygame.display.init()
	screen = pygame.display.set_mode((winx,winy))
	pellet_size = 20

	make_pellet = lambda: [randrange(pellet_size, winx - pellet_size), randrange(pellet_size, winy - pellet_size)]

	segments = [[winx//2,winy//2]]
	direction = [-1,0]
	pellet = make_pellet()
	velocity = pellet_size
	seg_offset = 2
	timeout = 0.5
	score = 0
	done = False

	while not done:
		# Update
		segments = update(segments, velocity, direction)
		shead = segments[0]

		if shead[0] < 0 or shead[0] >= winx:
			print("Hit Wall!")
			print(f"Score: {score}")
			time.sleep(1)
			break

		if shead[1] < 0 or shead[1] >= winy:
			print("Hit Wall!")
			print(f"Score: {score}")
			time.sleep(1)
			break

		if math.hypot(pellet[0] - shead[0], pellet[1] - shead[1]) <= pellet_size:
			pellet = make_pellet()
			timeout = max(0.07, timeout - 0.05)
			last = segments[-1]

			nx = last[0] + (pellet_size * direction[0] * -1)
			ny = last[1] + (pellet_size * direction[1] * -1)

			segments.append([nx, ny])
			score += 1

		hit_self = False
		for sg in range(1,len(segments)):
			seg = segments[sg]
			if math.hypot(seg[0] - shead[0], seg[1] - shead[1]) <= (pellet_size - seg_offset):
				hit_self = True
				break

		if hit_self:
			print("Hit Self!")
			print(f"Score: {score}")
			time.sleep(1)
			break

		# Input
		events = pygame.event.get()
		for e in events:
			if e.type == pygame.QUIT:
				done = True
				break
			elif e.type == pygame.KEYDOWN:
				if e.key == pygame.K_UP:
					direction = [0,-1]
				elif e.key == pygame.K_DOWN:
					direction = [0,1]
				elif e.key == pygame.K_LEFT:
					direction = [-1,0]
				elif e.key == pygame.K_RIGHT:
					direction = [1,0]
				elif e.key == pygame.K_ESCAPE:
					done = True
					break

		# Draw
		screen.fill((0,0,0))

		pygame.draw.rect(screen, (255,0,0), (int(pellet[0]), int(pellet[1]), pellet_size, pellet_size))
		for sg in segments:
			pygame.draw.rect(screen, (0,255,0), (int(sg[0]), int(sg[1]), pellet_size, pellet_size))

		pygame.display.flip()
		time.sleep(timeout)

	pygame.display.quit()

if __name__ == "__main__":
	main(400,400)
