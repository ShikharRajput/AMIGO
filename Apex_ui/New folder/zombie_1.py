def main():
    import pygame
    import random

    pygame.init()

    width = 1000
    height = 500

    red = 255,0,0
    green = 0,255,0
    blue = 0,0,255
    white = 255,255,255
    black = 0,0,0

    bg_img = pygame.image.load("images/background.png")

    zombieList = []

    for i in range(4):
        zombie = pygame.image.load("images/zombie_{}.png".format(i+1))
        zombieList.append(zombie)

    zombieImage = random.choice(zombieList)
    zombieHeight = zombieImage.get_height()
    zombieWidth = zombieImage.get_width()
    #----------print(dir(zombieImage))

    sound_1 = pygame.mixer.Sound("shotgun.wav")
    sound_2 = pygame.mixer.Sound("gunreload.wav")

    random_x = random.randrange(0,width - zombieWidth)
    random_y = random.randrange(0,height - zombieHeight)

    screen = pygame.display.set_mode((width,height))

    gun_aim = pygame.image.load("images/aim_pointer.png")
    gun_image = pygame.image.load("images/gun_1.png")
    gun_y = height - 200
    #----------print(gun_image.get_height())

    score_1=0

    def score():
        font = pygame.font.SysFont(None,30)
        text = font.render("Score : "+str(score_1),True,white)
        screen.blit(text,(0,0))
        print(score_1)

    game = True
    while game:

        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            

            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_1.play()
                
                if rect_1.colliderect(rect_2):
                    
                    
                    zombieImage = random.choice(zombieList)
                    random_x = random.randrange(0,width - zombieWidth)
                    random_y = random.randrange(0,height - zombieHeight)

                    score_1+=1
                    
        

        pos_x,pos_y = pygame.mouse.get_pos()
        pos_x = pos_x - gun_aim.get_width()/2
        pos_y = pos_y - gun_aim.get_height()/2
        
        screen.blit(bg_img,(0,0))

        screen.blit(zombieImage, (random_x, random_y))
        screen.blit(gun_aim, (pos_x ,pos_y))
        screen.blit(gun_image, (pos_x, gun_y))
        score()

        rect_1 = pygame.Rect(pos_x, pos_y, gun_aim.get_width(), gun_aim.get_height())
        rect_2 = pygame.Rect(random_x, random_y, zombieImage.get_width(), zombieImage.get_height())
        
        pygame.display.update()



