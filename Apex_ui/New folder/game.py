def game():
    import pygame
    from pygame.locals import *
    import snake,space,Zombie_shooter,car_race
    pygame.init()

    width = 900
    height = 500
    red = 0,0,255
    black = 0,0,0
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_5.colliderect(rect_1):
                    snake.main()
                if rect_5.colliderect(rect_2):
                    space.main()
                if rect_5.colliderect(rect_3):
                    Zombie_shooter.main()
                if rect_5.colliderect(rect_4):
                    car_race.main()
                    
        
        screen.blit(Snake,(20,180,))
        screen.blit(Space,(240,180,))
        screen.blit(Zombie,(460,180,))
        screen.blit(Carrace,(680,180,))

        rect_1 = pygame.Rect(20,180,200,150)
        rect_2 = pygame.Rect(240,180,200,150)
        rect_3 = pygame.Rect(460,180,200,150)
        rect_4 = pygame.Rect(680,180,200,150)

        pos_x,pos_y = pygame.mouse.get_pos()
        rect_5 = pygame.Rect(pos_x,pos_y,10,10)
        
        pygame.display.update()
