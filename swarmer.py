import pygame

from random import randrange as rr

def clamp(a,b,c):
	if b <= a:
		return c
	if c < a:
		return a
	if c > b:
		return b
	return c

class Swarmer:
	def __init__(self, x, y):
		self.pos = pygame.math.Vector2(x,y)
		self.velocity = pygame.math.Vector2(0.0,0.0)
		self.accel = pygame.math.Vector2(0.0,0.0)
		self.min_acc = -0.5
		self.max_acc = 0.5
		self.min_vel = -10
		self.max_vel = 10

	def update(self, target):
		targvec = (target - self.pos).normalize()

		self.accel[0] = clamp(self.min_acc, self.max_acc, self.accel[0] + targvec[0])
		self.accel[1] = clamp(self.min_acc, self.max_acc, self.accel[1] + targvec[1])

		self.velocity[0] = clamp(self.min_vel, self.max_vel, self.velocity[0] + self.accel[0])
		self.velocity[1] = clamp(self.min_vel, self.max_vel, self.velocity[1] + self.accel[1])

		self.pos[0] += self.velocity[0]# * self.factor
		self.pos[1] += self.velocity[1]# * self.factor

	def draw(self,screen):
		pygame.draw.circle(screen, (255,255,255), (int(self.pos[0]), int(self.pos[1])), 5)

def random_pos(min, max):
	x=rr(min[0], min[1])
	y=rr(max[0], max[1])
	return [x,y]

def main(winx = 600, winy = 600):
	pygame.display.init()
	screen = pygame.display.set_mode((winx,winy))
	done = False
	swarm = []
	clock = pygame.time.Clock()
	while not done:
		clock.tick(60)

		mpos = pygame.mouse.get_pos()
		mpos_vec = pygame.math.Vector2(mpos[0], mpos[1])
		#print("mpos",mpos)

		for s in swarm:
			s.update(mpos_vec)

		for e in pygame.event.get():
			if e.type == pygame.MOUSEBUTTONDOWN:
				if e.button == 1:
					spos = random_pos([0,winx],[0,winy])
					swarm.append(Swarmer(spos[0], spos[1]))
				elif e.button == 3:
					if len(swarm) > 0:	
						swarm.pop(0)

			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					done = True
					break

		screen.fill((0,0,0))
		for s in swarm:
			s.draw(screen)

		pygame.display.flip()

	pygame.display.quit()

if __name__ == "__main__":
	main()
