import pygame
import random

pygame.init()
count=0
white=255,255,255
def score(count):
    font=pygame.font.SysFont(None,40)
    text=font.render("score{}".format(count),True,white)
    screen.blit(text,(10,10))




width=1000
height=500

screen=pygame.display.set_mode((width,height))
bg_img=pygame.image.load(r"C:\Users\golat\PycharmProjects\zombi\images\background.png")
zombielist=[]
for i in range(4):
    zombie=pygame.image.load("images/zombie_{}.png".format(i+1))
    zombielist.append(zombie)

zombieimage=random.choice(zombielist)
zombieheight=zombieimage.get_height()
zombiewidth=zombieimage.get_width()

random_x=random.randrange(0,width - zombiewidth)
random_y=random.randrange(0,height - zombieheight)
gun_aim=pygame.image.load("images/aim_pointer.png")
gun_image=pygame.image.load("images/gun_1.png")
gun_y=height-200
sound_1=pygame.mixer.Sound(r"C:\Users\golat\Desktop\shot_sound.wav")
game=True
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()


        if event.type==pygame.MOUSEBUTTONDOWN:


             if rect_1.colliderect(rect_2):
                 count += 1
                 sound_1.play()




                 print("counter",count)
                 zombieimage = random.choice(zombielist)

                 random_x = random.randrange(0, width - zombiewidth)
                 random_y = random.randrange(0, height - zombieheight)
             score(count)
    pos_x,pos_y=pygame.mouse.get_pos()
    screen.blit(bg_img,(0,0))
    screen.blit(zombieimage,(random_x,random_y))
    screen.blit(gun_aim,(pos_x-gun_aim.get_width()/2,pos_y-gun_aim.get_height()/2))
    screen.blit(gun_image,(pos_x,gun_y))

    rect_1=pygame.Rect(pos_x,pos_y,gun_aim.get_width(),gun_aim.get_height())
    rect_2=pygame.Rect(random_x,random_y,zombieimage.get_width(),zombieimage.get_height())

    pygame.display.update()