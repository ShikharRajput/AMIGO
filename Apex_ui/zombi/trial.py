import pygame

pygame.init()

width=1200
height=500


screen= pygame.display.set_mode((width,height))

background= pygame.image.load("streetfighter/images/helipad.png")

black=0,0,0
class Spritesheet():
    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet=file_name

    def getImage(self, x, y, width,  height):
        image=pygame.Surface((width,height))
        image.blit(self.spriteSheet,(0,0),(x,y,width,height))
        image.set_colorkey(black)
        return image
class Player_2(pygame.sprite.Sprite):

    walking_frames2=[]
    standingframes2=[]
    punchframes2=[]
    kickframes2=[]

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

        self.rect=self.image.get_rect()
        self.rect.center=(width-270,height/2+70)
        self.pos=0
        self.stand2=True
        self.walk2=False
        self.kick2=False
        self.punch2=False

    def update(self):
        self.pos += 2
        self.moveX=0

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_LEFT]:
            self.walk2 = True
            self.moveX = 1
        elif keypressed[pygame.K_UP]:
            self.walk2 = True
            self.moveX = -1

        elif keypressed[pygame.K_DOWN]:
            #self.walk2 = True
            self.punch2=True
            self.moveX = -1


        elif keypressed[pygame.K_RIGHT]:
            #self.walk2 = True
            self.kick2=True
            self.moveX = -1

        else:
            self.walk2 = False
            self.punch2=False
            self.kick2=False
            self.moveX = 0
            self.rect.x+= self.moveX




        frame = (self.pos // 30) % len(self.standingframes2)
        # print("Position",self.pos//30)
        # print("Frame",frame)
        self.image2 = self.standingframes2[frame]

        if self.walk2:
            frame=(self.pos//15)%len(self.walking_frames2)
            self.image2=self.walking_frames2[frame]


        if self.punch2:
            frame=(self.pos//15)%len(self.punchframes2)
            self.image2=self.punchframes2[frame]


        if self.kick2:
            frame=(self.pos//15)%len(self.kickframes2)
            self.image2=self.kickframes2[frame]




player_sprite2=pygame.image.load("streetfighter/images/ryu_.png")




all_sprites=pygame.sprite.Group()
player2=Player_2()
ryu=pygame.sprite.Group()
ryu.add(player2)



all_sprites.add(player2)

while True:
     for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
     screen.blit(background ,(0,0))
     all_sprites.update()
     all_sprites.draw(screen)
     pygame.display.update()
