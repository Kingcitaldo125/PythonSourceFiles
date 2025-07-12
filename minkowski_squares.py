"""
PyGame app simulating two squares colliding using the Minkowski Difference
https://en.wikipedia.org/wiki/Minkowski_addition
"""
import pygame
from pygame.math import Vector2
from time import sleep
from random import randrange

def ran_col():
	return tuple([randrange(0,255) for i in range(3)])

class Square:
	def __init__(self,center_vec,size):
		self.vertices = []
		self.center_vec = center_vec
		self.size = size
		self.color = ran_col()
		self.update()

	def update(self):
		self.vertices = []
		xhalf = self.size // 2
		# Create the 4 vertices of the square
		self.vertices.append(Vector2(self.center_vec.x - xhalf, self.center_vec.y - xhalf))
		self.vertices.append(Vector2(self.center_vec.x + xhalf, self.center_vec.y + xhalf))
		self.vertices.append(Vector2(self.center_vec.x + xhalf, self.center_vec.y - xhalf))
		self.vertices.append(Vector2(self.center_vec.x - xhalf, self.center_vec.y + xhalf))

	def render(self,screen):
		xrect = (self.vertices[0][0], self.vertices[0][1], self.size, self.size)
		pygame.draw.rect(screen, self.color, xrect, 1)

def minkowski_diff(a,b,debug=False):
	collision_points = set([])

	for averts in a.vertices:
		for bverts in b.vertices:
			a1,a2 = averts.x,averts.y
			b1,b2 = bverts.x,bverts.y

			collision_points.add((a1-b1,a2-b2))

	if debug:
		print("collision_points",collision_points)

	return (0,0) in collision_points

def main():
	pygame.display.init()

	screen = pygame.display.set_mode((400,400))

	s1 = Square(Vector2(100,200),100)
	s2 = Square(Vector2(300,200),100)

	for i in range(200):
		s1.center_vec.x += 1
		s2.center_vec.x -= 1
		s1.update()
		s2.update()

		if (minkowski_diff(s1,s2)):
			print("Collide")

		screen.fill("black")

		s1.render(screen)
		s2.render(screen)

		pygame.display.flip()

		sleep(0.1)

	pygame.display.quit()

if __name__ == "__main__":
	main()
