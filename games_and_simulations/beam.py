import pygame
import math

black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
green = (0,128,64)

def clamp(x,y,n):
	if n < x:
		return x
	if n > y:
		return y
	return n

def main(winx=800, winy=600):
	pygame.display.init()

	screen = pygame.display.set_mode((winx, winy))
	clock = pygame.time.Clock()

	beamx,beamy = (winx//2,winy//8)
	beamrad = 3
	degrees = 0.0

	playerrad = 20

	beam_direction = 1

	beamposvec = pygame.math.Vector2(beamx,beamy)

	winx_dub = winx*2
	winy_dub = winy*2

	done = False

	while not done:
		dt = clock.tick(30)
		mx,my = pygame.mouse.get_pos()

		cursor_vec = pygame.math.Vector2(mx,my)
		playervec = (cursor_vec - beamposvec).normalize()

		beamendx,beamendy = math.cos(math.radians(degrees)), math.sin(math.radians(degrees))
		beamendx,beamendy = beamendx * winx_dub, beamendy * winy_dub

		beamvec = pygame.math.Vector2(beamendx,beamendy) - beamposvec

		a1dot = beamvec.dot(playervec)
		a1 = a1dot * playervec
		a2 = a1.distance_to(beamvec)

		player_fill = 0
		if a1dot > 0 and a2 <= playerrad * 2:
			player_fill = 1

		if player_fill == 0:
			degrees += 0.02 * dt * beam_direction
		else:
			degrees += 0.002 * dt * beam_direction

		if degrees >= 360.0:
			degrees = 0.0

		events = pygame.event.get()
		for e in events:
			if e.type == pygame.MOUSEBUTTONDOWN:
				if e.button == 3:
					beam_direction = 1
				elif e.button == 1:
					beam_direction = -1
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					done = True
					break

		screen.fill(black)
		pygame.draw.circle(screen, green, (mx, my), playerrad, player_fill)
		pygame.draw.circle(screen, red, (beamx, beamy), beamrad)
		pygame.draw.line(screen, white, (beamx, beamy), (beamendx, beamendy))
		pygame.display.flip()

	pygame.display.quit()

if __name__ == "__main__":
	main()
