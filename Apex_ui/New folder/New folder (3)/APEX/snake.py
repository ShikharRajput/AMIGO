def main():

    import pygame
    import random
      
    pygame.init()

    width=800
    height=500

    screen = pygame.display.set_mode((width,height))

    snake1 = pygame.image.load("snake.png")


    red=0,0,255
    black=0,0,0
    white=255,255,255

    x,y=0,0


    moveX = 0
    moveY = 0

    score_1 = 0

    random_x = random.randrange(0,width-50)
    random_y = random.randrange(0,height-50)

    snakelist = []
    snakelength = 1
    clock = pygame.time.Clock()
    FPS=90

    sound_1 = pygame.mixer.Sound('game_over.wav')
    sound_2 = pygame.mixer.Sound('point.wav')

    def snake(snakelist):
        for i in range(len(snakelist)):
            pygame.draw.rect(screen,black,[snakelist[i][0],snakelist[i][1],50,50])

    def gameover():
        font = pygame.font.SysFont(None,80)
        text = font.render("GAME OVER",True,black)
        screen.blit(text,(200,200))

    def score():
        font = pygame.font.SysFont(None,20)
        text = font.render("Score"+str(score_1),True,black)
        screen.blit(text,(0,0))
        

    game = True

    while game:
        for event in pygame.event.get():
            #print(event)--> give position & action
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 6
                    moveY = 0
                elif event.key == pygame.K_LEFT:
                    moveX = -6
                    moveY = 0
                elif event.key == pygame.K_DOWN:
                    moveY = 6
                    moveX = 0
                elif event.key == pygame.K_UP:
                    moveY = -6
                    moveX = 0
                
        screen.fill(red)

            
        #rect_1 = pygame.draw.rect(screen,black,[x,y,50,50])
        #rect_2 = pygame.draw.rect(screen,white,[random_x,random_y,20,20])

        rect_1 = pygame.Rect(x,y,50,50)
        rect_2 = pygame.Rect(random_x,random_y,50,50)
        
        screen.blit(snake1,(random_x,random_y))
        
        x += moveX
        y += moveY

        snakehead = []
        snakehead.append(x)
        snakehead.append(y)

        snakelist.append(snakehead)

        if len(snakelist) > snakelength:
            del snakelist[0]

        snake(snakelist)
        score()
        
        if rect_1.colliderect(rect_2):
            random_x = random.randrange(0,width-50)
            random_y = random.randrange(0,height-50)

            snakelength += 5

            sound_2.play()
            score_1 += 5

        for each in snakelist[:-1]:
            if snakelist[-1] == each:
                #print("Game Over")
                sound_1.play()
                gameover()
                game = False
            
        
        if x > width :
            x = -50
        elif y > height :
            y = -50
        elif x <  -50:
            x = width
        elif y <  -50:
            y = height
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
        
