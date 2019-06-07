import pygame
from pygame.locals import *
import snake,space,Zombie_shooter,car_race,project,StreetFighter
def main():
    pygame.init()

    width = 900
    height = 500
    red = 0,0,255
    black = 0,0,0
    screen = pygame.display.set_mode((width,height))

    Snake = pygame.image.load("snakeimg.jpg")
    Space = pygame.image.load("space.png")
    Zombie = pygame.image.load("zombie.jpg")
    Carrace = pygame.image.load("car.jpg")
    PlantNZombie = pygame.image.load("plantNzombie.jpg")
    StreetFight = pygame.image.load("sf.jpg")
    
    screen.blit(Snake,(20,280,))
    screen.blit(Space,(240,280,))
    screen.blit(Zombie,(460,280,))
    screen.blit(Carrace,(680,280,))
    screen.blit(PlantNZombie,(460,70,))
    screen.blit(StreetFight,(240,70,))
    
    while True:
        rect_1 = pygame.Rect(20,280,200,150)
        rect_2 = pygame.Rect(240,280,200,150)
        rect_3 = pygame.Rect(460,280,200,150)
        rect_4 = pygame.Rect(680,280,200,150)
        rect_5 = pygame.Rect(460,70,200,150)
        rect_6 = pygame.Rect(240,70,200,150)
        
        pos_x,pos_y = pygame.mouse.get_pos()
        rect = pygame.Rect(pos_x,pos_y,10,10)

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect.colliderect(rect_1):
                    snake.main()
                elif rect.colliderect(rect_2):
                    space.main()
                elif rect.colliderect(rect_3):
                    Zombie_shooter.main()
                elif rect.colliderect(rect_4):
                    car_race.main()
                elif rect.colliderect(rect_5):
                    project.main()
                elif rect.colliderect(rect_6):
                    StreetFighter.main()

