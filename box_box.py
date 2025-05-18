import pygame

from time import sleep

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
green = (0,128,64)

class Box():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	
	def get_left_x(self):
		return self.x

	def get_right_x(self):
		return self.x + self.width

	def get_left_y(self):
		return self.y

	def get_right_y(self):
		return self.y + self.height
	
	def get_area(self):
		return self.width * self.height

	def render(self, screen, color, wireframe=0):
		pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height), wireframe)

def intersect(box1, box2):
	xintersect = box1.x + box1.width >= box2.x and box1.x <= box2.x + box2.width
	yintersect = box1.y + box1.height >= box2.y and box1.y <= box2.y + box2.height

	return xintersect and yintersect

def get_internal_area(box1, box2):
	xbox_left_bounds = max(box1.x, box2.x)
	xbox_right_bounds = min(box1.x + box1.width, box2.x + box2.width)

	ybox_left_bounds = max(box1.y, box2.y)
	ybox_right_bounds = min(box1.y + box1.height, box2.y + box2.height)
	
	xdiff = abs(xbox_left_bounds - xbox_right_bounds)
	ydiff = abs(ybox_left_bounds - ybox_right_bounds)

	print("xdiff", xdiff)
	print("ydiff", ydiff)
	print()

	if xdiff == box1.width and ydiff == box1.height:
		print("Box 1 area")
		return box1.get_area()

	if xdiff == box2.width and ydiff == box2.height:
		print("Box 2 area")
		return box2.get_area()

	return xdiff * ydiff

def main(winx=800, winy=600):
	pygame.display.init()

	screen = pygame.display.set_mode((winx, winy))
	clock = pygame.time.Clock()
	
	b1 = Box(winx // 2 - 100, winy // 2 - 100, 200, 200)
	b2 = Box(100, b1.y, 50, 100)

	speed = 25

	done = False

	while not done:
		#clock.tick(10)

		does = intersect(b1, b2)

		if does:	
			print("Area:", get_internal_area(b1,b2))

		events = pygame.event.get()
		for e in events:
			if e.type == pygame.MOUSEBUTTONDOWN:
				if e.button == 4:
					speed = min(50, speed + 5)
					print("speed", speed)
				if e.button == 5:
					speed = max(5, speed - 5)
					print("speed", speed)
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_UP:
					b2.y -= speed
				if e.key == pygame.K_DOWN:
					b2.y += speed
				if e.key == pygame.K_LEFT:
					b2.x -= speed
				if e.key == pygame.K_RIGHT:
					b2.x += speed
				if e.key == pygame.K_ESCAPE:
					done = True
					break

		screen.fill(black)

		b1.render(screen, green, 1 if does else 0)
		b2.render(screen, red, 1 if does else 0)

		pygame.display.flip()
		sleep(0.75)

	pygame.display.quit()

if __name__ == "__main__":
	main()
