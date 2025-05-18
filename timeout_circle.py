import pygame
import math
from random import randrange
import time


def get_angle_pos(angle):
	"""
	Given an angle, in degrees, return the resulting normalized x,y polar coordinate.
	"""
	anglex = math.cos(math.radians(angle))
	angley = math.sin(math.radians(angle))

	return (anglex, angley)

def draw_at_angle(screen, winx, winy, white_col, i, direction=1):
	circle_rad = 25

	apos = get_angle_pos(i)

	anglex = apos[0]
	angley = apos[1]

	anglex = int(winx//2) + circle_rad * anglex
	angley = int(winy//2) + circle_rad * (angley * direction)

	screen.set_at((int(anglex), int(angley)), white_col)

def lerp(v0, v1, t):
	if v1 == t:
		return v1
	return v0 + t * (v1 - v0);

def main(winx, winy):
	"""
	Driver code. Houses all of the main application logic.
	"""
	pygame.display.init()

	black_col = (18,22,28)
	grey_col = (170,170,170)
	white_col = (255,255,255)

	screen = pygame.display.set_mode((winx, winy))

	clock = pygame.time.Clock()

	done = False

	start_angle = 270
	seconds = 0
	angle_seconds = seconds
	total_seconds = 10

	xtime = (time.time() / 1000)
	while not done:
		dT = clock.tick(60) / 1000
		sec_ratio = angle_seconds/total_seconds
		sangle = start_angle - (start_angle * sec_ratio)

		if seconds >= total_seconds:
			done = True

		seconds += 1 * dT
		angle_seconds += 1.25 * dT

		print("seconds", seconds)

		# Input
		for e in pygame.event.get():
			if e.type == pygame.KEYDOWN:
				if e.key == 27: # Esc
					print("Quitting..")
					done = True

		# Render
		screen.fill(black_col)

		for i in range(-90,int(sangle)):
			draw_at_angle(screen, winx, winy, white_col, i, direction=1)
		pygame.display.flip()

		#time.sleep(1)

	pygame.display.quit()


if __name__ == "__main__":
	winx = 600
	winy = winx

	main(winx, winy)
