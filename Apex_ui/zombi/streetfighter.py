import pygame
from pygame.locals import *
pygame.init()

width=1200
height=500
black=0,0,0
blue=0,0,255

screen= pygame.display.set_mode((width,height))



sound_1=pygame.mixer.Sound('streetfighter/sounds/punch2.wav')
sound_2=pygame.mixer.Sound('streetfighter/sounds/kick.wav')
sound_3=pygame.mixer.Sound('streetfighter/sounds/attack.wav')


background= pygame.image.load("streetfighter/images/helipad.png")


class Spritesheet():
    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet=file_name

    def getImage(self, x, y, width,  height):
        image=pygame.Surface((width,height))
        image.blit(self.spriteSheet,(0,0),(x,y,width,height))
        image.set_colorkey(black)
        return image

    #def life(self):
       # screen = pygame.display.set_mode((width, height))
        #font = pygame.font.SysFont(None, 40)
       # text = font.render("life", True, black)
       # screen.blit(text, (10, 10))

class Player_1(pygame.sprite.Sprite):

    walking_frames=[]
    standingframes=[]
    punchframes=[]
    kickframes=[]
    dragonattackframes=[]
   # self.life()
    isAttack = False
    health = 450



    def __init__(self):
        super().__init__()

        spritesheet = Spritesheet(player_sprite)

        self.image=spritesheet.getImage(48,247,106,239)
        self.standingframes.append(self.image)
        self.image = spritesheet.getImage(264,240,113,249)
        self.standingframes.append(self.image)
        self.image = spritesheet.getImage(482,248,106,237)
        self.standingframes.append(self.image)
        self.image=spritesheet.getImage(687,247,112,241)
        self.standingframes.append(self.image)

        self.image=spritesheet.getImage(42,247,116,243)
        self.walking_frames.append(self.image)
        self.image=spritesheet.getImage(44,731,118,243)
        self.walking_frames.append(self.image)
        self.image=spritesheet.getImage(256,731,118,243)
        self.walking_frames.append(self.image)

        self.image = spritesheet.getImage(35,488,133,240)
        self.punchframes.append(self.image)
        self.image = spritesheet.getImage(264,491,156,238)
        self.punchframes.append(self.image)
        self.image = spritesheet.getImage(471,494,120,240)
        self.punchframes.append(self.image)

        self.image = spritesheet.getImage(20,1461,152,243)
        self.kickframes.append(self.image)
        self.image = spritesheet.getImage(211,1458,174,244)
        self.kickframes.append(self.image)
        self.image = spritesheet.getImage(427,1458,213,242)
        self.kickframes.append(self.image)
        self.image = spritesheet.getImage(677,1458,121,247)
        self.kickframes.append(self.image)
        self.image = spritesheet.getImage(911,1461,115,244)
        self.kickframes.append(self.image)

        self.image = spritesheet.getImage(29,8,155,225)
        self.dragonattackframes.append(self.image)
        self.image = spritesheet.getImage(242,17,158,216)
        self.dragonattackframes.append(self.image)
        self.image = spritesheet.getImage(442,26,192,207)
        self.dragonattackframes.append(self.image)
        self.image = spritesheet.getImage(661,26,192,207)
        self.dragonattackframes.append(self.image)
        #for i in range(1):
            #self.rect.center = (width / 2 - 300, height / 2)

            #self.image = spritesheet.getImage(26, 1033, 100, 72)
            #self.dragonattackframes.append(self.image)



        self.rect=self.image.get_rect()
        self.rect.center=(width/2-300,height/2+60)
        self.pos=0
        self.stand=True
        self.walk=False
        self.kick=False
        self.punch=False
        self.dragonattack=False

    def update(self):
        self.pos += 2
        self.moveX=0

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.walk = True
            self.moveX = 1
        elif keypressed[pygame.K_LEFT]:
            self.walk = True
            self.moveX = -1

        elif keypressed[pygame.K_UP]:
            #self.walk = True
            self.punch=True
            #self.moveX = -1


        elif keypressed[pygame.K_DOWN]:
            #self.walk = True
            self.kick=True
            #self.moveX = -1

        elif keypressed[pygame.K_F3]:
            #self.walk = True
            self.dragonattack=True
            #self.moveX = -1

        else:
            self.walk = False
            self.punch=False
            self.kick=False
            self.dragonattack=False
            self.moveX = 0
        self.rect.x+= self.moveX




        frame = (self.pos // 30) % len(self.standingframes)
        # print("Position",self.pos//30)
        # print("Frame",frame)
        self.image = self.standingframes[frame]

        self.hit = pygame.sprite.groupcollide(ken, ryu, False, False)

        if self.walk:
            frame=(self.pos//30)%len(self.walking_frames)
            self.image=self.walking_frames[frame]



        elif self.punch:
            frame=(self.pos//30)%len(self.punchframes)
            self.image=self.punchframes[frame]

            if self.hit:
                self.isAttack = True
                sound_1.play()
                player_2.health -= 1



        elif self.kick:
            frame=(self.pos//30)%len(self.kickframes)
            self.image=self.kickframes[frame]


            if self.hit:
                self.isAttack = True
                sound_2.play()
                player_2.health -= 3


        elif self.dragonattack:
            frame=(self.pos//30)%len(self.dragonattackframes)
            self.image=self.dragonattackframes[frame]

            if self.hit:
                self.isAttack = True
                sound_3.play()
                player_2.health -= 5




player_sprite=pygame.image.load("streetfighter/images/ken_.png")


class Player_2(pygame.sprite.Sprite):

    walking_frames2=[]
    standingframes2=[]
    punchframes2=[]
    kickframes2=[]
    dragonattackframes2=[]
    splitframes2=[]
    isAttack = False
    health = 450
    def __init__(self):
        super().__init__()
        spritesheet = Spritesheet(player_sprite2)

        self.image=spritesheet.getImage(2959,42,106,226)
        self.standingframes2.append(self.image)
        self.image = spritesheet.getImage(2750,39,103,229)
        self.standingframes2.append(self.image)
        self.image = spritesheet.getImage(2558,36,103,232)
        self.standingframes2.append(self.image)
        self.image=spritesheet.getImage(2360,39,103,229)
        self.standingframes2.append(self.image)

        self.image=spritesheet.getImage(2575,314,109,229)
        self.walking_frames2.append(self.image)
        self.image=spritesheet.getImage(2394,317,95,226)
        self.walking_frames2.append(self.image)
        self.image=spritesheet.getImage(22144,314,91,229)
        self.walking_frames2.append(self.image)

        self.image = spritesheet.getImage(2953,592,109,229)
        self.punchframes2.append(self.image)
        self.image = spritesheet.getImage(2738,592,155,229)
        self.punchframes2.append(self.image)
        self.image = spritesheet.getImage(2560,592,109,229)
        self.punchframes2.append(self.image)

        self.image = spritesheet.getImage(2950,895,109,230)
        self.kickframes2.append(self.image)
        self.image = spritesheet.getImage(2764,890,115,235)
        self.kickframes2.append(self.image)
        self.image = spritesheet.getImage(2497,884,195,241)
        self.kickframes2.append(self.image)
        self.image = spritesheet.getImage(2317,890,115,235)
        self.kickframes2.append(self.image)
        self.image = spritesheet.getImage(2950,895,109,230)
        self.kickframes2.append(self.image)

        self.image = spritesheet.getImage(2890,1896,146,212)
        self.dragonattackframes2.append(self.image)
        self.image = spritesheet.getImage(2661,1898,149,210)
        self.dragonattackframes2.append(self.image)
        self.image = spritesheet.getImage(2283,1904,320,197)
        self.dragonattackframes2.append(self.image)


        self.image = spritesheet.getImage(1196,305,89,212)
        self.splitframes2.append(self.image)
        self.image = spritesheet.getImage(1027,297,98,260)
        self.splitframes2.append(self.image)
        self.image = spritesheet.getImage(810,368,177,109)
        self.splitframes2.append(self.image)
        self.image = spritesheet.getImage(646,285,92,195)
        self.splitframes2.append(self.image)
        self.image = spritesheet.getImage(397,334,209,114)
        self.splitframes2.append(self.image)
        self.image = spritesheet.getImage(222,265,126,215)
        self.splitframes2.append(self.image)
        self.image = spritesheet.getImage(56,222,97,261)
        self.splitframes2.append(self.image)


        self.rect =self.image.get_rect()
        self.rect.center=(width-350,height/2+70)
        self.pos=0
        self.stand2=True
        self.walk2=False
        self.kick2=False
        self.punch2=False
        self.dragonattack2=False
        self.split2=False

    def update(self):
        self.pos += 2
        self.moveX=0

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_SPACE]:
            self.walk2 = True
            self.moveX = 1
        elif keypressed[pygame.K_TAB]:
            self.walk2 = True
            self.moveX = -1

        elif keypressed[pygame.K_F1]:
            self.punch2=True




        elif keypressed[pygame.K_F2]:
            self.kick2=True



        elif keypressed[pygame.K_F4]:
            self.dragonattack2=True


        elif keypressed[pygame.K_F6]:

           self.split2 = True


        else:
            self.walk2 = False
            self.punch2=False
            self.kick2=False
            self.dragonattack2=False
            self.splitframes2=False
            self.moveX = 0

        self.rect.x+= self.moveX




        frame = (self.pos // 30) % len(self.standingframes2)
        # print("Position",self.pos//30)
        # print("Frame",frame)
        self.image= self.standingframes2[frame]

        self.hit = pygame.sprite.groupcollide(ryu, ken, False, False)

        if self.walk2:
            frame=(self.pos//30)%len(self.walking_frames2)
            self.image=self.walking_frames2[frame]


        if self.punch2:
            frame=(self.pos//30)%len(self.punchframes2)
            self.image=self.punchframes2[frame]

            if self.hit:
                self.isAttack = True
                sound_1.play()
                player.health -= 1

        if self.kick2:
            frame=(self.pos//30)%len(self.kickframes2)
            self.image=self.kickframes2[frame]


            if self.hit:
                self.isAttack = True
                sound_2.play()
                player.health -= 3


        #if  self.split2:
           # frame=(self.pos//30)%len(self.splitframes2)
            #self.image=self.splitframes2[frame]

        if self.dragonattack2:
            frame=(self.pos//30)%len(self.dragonattackframes2)
            self.image=self.dragonattackframes2[frame]

            if self.hit:
                self.isAttack = True
                sound_3.play()
                player.health -= 5

pygame.time.set_timer(USEREVENT,1000)
def timer(seconds):
    red = 255,0,0
    font = pygame.font.SysFont(None, 50)
    text = font.render("{}".format(str(seconds)), True, red)
    screen.blit(text, (520,10))
clock = pygame.time.Clock()
FPS = 90


player_sprite2=pygame.image.load("streetfighter/images/ryu_.png")






all_sprites=pygame.sprite.Group()
player=Player_1()
player2=Player_2()

ken=pygame.sprite.Group()
ryu=pygame.sprite.Group()
ken.add(player)
ryu.add(player2)

all_sprites.add(player)
all_sprites.add(player2)

def kenHealth():
    pygame.draw.rect(screen, blue, [10,10,player.health,40])

def ryuHealth():
    pygame.draw.rect(screen, blue, [width - 490,10,player2.health,40])


def homeScreen():
    image_1 = pygame.image.load("streetfighter/images/image_1.jpg")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

        screen.blit(image_1, (0,0))
        pygame.display.update()


def main():
    seconds = 100
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == USEREVENT:
                seconds -= 1

        screen.blit(background,(0,0))

        all_sprites.update()
        all_sprites.draw(screen)

        kenHealth()
        ryuHealth()

        timer(seconds)

        pygame.display.update()
        clock.tick(FPS)

homeScreen()
