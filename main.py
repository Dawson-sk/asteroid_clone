import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()


	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)


	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	field = AsteroidField()

	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return


		for u in updatable:
			u.update(dt)

		screen.fill((0,0,0))


		for d in drawable:
			d.draw(screen)

		for a in asteroids:
			if a.collision(player) == True:
				print("Game over!")
				sys.exit()
			for s in shots:
				if s.collision(a):
					s.kill()
					a.kill()

		pygame.display.flip()


		dt = clock.tick(60) / 1000



if __name__ == "__main__":
	main()
