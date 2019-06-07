import pygame
from pygame.locals import *

pygame.init()

width = 800
height = 500

screen = pygame.display.set_mode((width,height))

Snake = pygame.image.load("snake.jpg")
Space = pygame.image.load("space.png")
Zombie = pygame.image.load("zombie.jpg")
Carrace = pygame.image.load("car.jpg")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(Snake,(0,0,))
    screen.blit(Space,(0,0,))
    screen.blit(Zombie,(0,0,))
    screen.blit(Carrace,(0,0,))

    pygame.display.update()
