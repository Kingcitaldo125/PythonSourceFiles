import pygame

def color(name):
	return pygame.Color(name)

def main(win_size=600):
	pygame.display.init()

	screen = pygame.display.set_mode((win_size,win_size))
	midpoint = pygame.math.Vector2(win_size//2,win_size//2)

	bullets = []
	bullet_rad = 6
	bullet_velocity = 5
	bul_flag = False

	white = color("white")
	green = color("green")
	black = color("black")

	clock = pygame.time.Clock()
	running = True
	while running:
		nbullets = []
		for bullet in bullets:
			valid_x = bullet[0] + bullet_rad > 0 and bullet[0] - bullet_rad < win_size
			valid_y = bullet[1] + bullet_rad > 0 and bullet[1] - bullet_rad < win_size

			velocity = bullet[-1]
			bullet[0] += velocity.x
			bullet[1] += velocity.y

			if valid_x and valid_y:
				nbullets.append(bullet)

		bullets = nbullets

		events = pygame.event.get()
		for evt in events:
			if evt.type == pygame.QUIT:
				running = False
				break
			if evt.type == pygame.MOUSEBUTTONDOWN:
				mx,my = pygame.mouse.get_pos()
				mouse_vec = pygame.math.Vector2(mx,my)

				bullet_dir = (mouse_vec - midpoint)
				bullet_dir.scale_to_length(bullet_dir.length()//20)

				bullets.append([midpoint.x, midpoint.y, bullet_dir])
				bul_flag = True
			if evt.type == pygame.KEYDOWN:
				if evt.key == pygame.K_ESCAPE:
					running = False
					break

		screen.fill(black)
		pygame.draw.circle(screen, green, (midpoint.x, midpoint.y), 3)
		for bullet in bullets:
			pygame.draw.circle(screen, white, (int(bullet[0]), int(bullet[1])), bullet_rad)
		pygame.display.flip()
		clock.tick(60)

	pygame.display.quit()

if __name__ == "__main__":
	main()
