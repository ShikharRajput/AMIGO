import pygame
from pygame.locals import *
def main():

    pygame.init()

    global width
    global height
    width = 1014
    height = 675

    screen = pygame.display.set_mode((width,height))

    background = pygame.image.load("Simage/background.png")

    black = 0,0,0
    blue = 0,0,255
    class Spritesheet():
        def __init__(self,file_name):
            pygame.sprite.Sprite.__init__(self)
            self.spriteSheet = file_name
        def getImage(self, x, y, width, height):
            image = pygame.Surface((width, height))
            image.blit(self.spriteSheet, (0,0), (x, y, width, height))
            image.set_colorkey(black)

            return image
        
    class Player_1(pygame.sprite.Sprite):
        walking_frames = []
        standingFrames = []
        punch_frames = []
        kick_frames = []

        isAttack = False
        health = 450
        
        def __init__(self):
            super().__init__()
            spritesheet = Spritesheet(player_sprite)

            self.image = spritesheet.getImage(48,247,106,239)
            self.standingFrames.append(self.image)
            self.image = spritesheet.getImage(264,240,113,249)
            self.standingFrames.append(self.image)
            self.image = spritesheet.getImage(482,248,106,237)
            self.standingFrames.append(self.image)
            self.image = spritesheet.getImage(687,247,112,241)
            self.standingFrames.append(self.image)
            
            self.image = spritesheet.getImage(42,247,116,243)
            self.walking_frames.append(self.image)
            self.image = spritesheet.getImage(44,731,118,243)
            self.walking_frames.append(self.image)
            self.image = spritesheet.getImage(256,731,118,243)
            self.walking_frames.append(self.image)

            self.image = spritesheet.getImage(42,490,118,240)
            self.punch_frames.append(self.image)
            self.image = spritesheet.getImage(260,489,166,240)
            self.punch_frames.append(self.image)
            self.image = spritesheet.getImage(472,487,122,245)
            self.punch_frames.append(self.image)
            
            self.image = spritesheet.getImage(250,1451,118,250)
            self.kick_frames.append(self.image)
            self.image = spritesheet.getImage(428,1457,208,248)
            self.kick_frames.append(self.image)
            self.image = spritesheet.getImage(676,1461,120,244)
            self.kick_frames.append(self.image)

            self.rect = self.image.get_rect()
            self.rect.center = (width / 2 - 250, height / 2 + 150)

            self.pos = 0
            
            self.stand = True
            self.walk = False
            self.kick = False
            self.punch = False

        def update(self): 
            self.pos += 2

            self.moveX = 0

            keypressed = pygame.key.get_pressed()
            if keypressed[pygame.K_RIGHT]:
                self.walk = True
                if self.rect.x <= width-100:
                    self.moveX = 3
                else:
                    self.moveX = 0
                
            elif keypressed[pygame.K_LEFT]:
                self.walk = True
                if self.rect.x >= 0:
                    self.moveX = -3
                else:
                    self.moveX = 0
                    
            else:
                self.walk = False
                self.moveX = 0

            self.rect.x += self.moveX

            if keypressed[pygame.K_k]:
                self.kick = True

            if keypressed[pygame.K_p]:
                self.punch =True
                
                

            frame = (self.pos // 30) % len(self.standingFrames)
            #print("Position",self.pos//30)
            #print("Frame",frame)
            self.image = self.standingFrames[frame]

            self.hit = pygame.sprite.groupcollide(ken, ryu, False, False)

            if self.walk:
                frame = (self.pos // 30) % len(self.walking_frames)
                self.image = self.walking_frames[frame]
                
            elif self.kick:
                frame = (self.pos // 20) % len(self.kick_frames)
                self.image = self.kick_frames[frame]
                if frame == 2:
                    self.kick = False
                if self.hit:
                    self.isAttack = True
                    punchSound.play()
                    playerryu.health -=5
            elif self.punch:
                frame = (self.pos // 10) % len(self.punch_frames)
                self.image = self.punch_frames[frame]
                #print(frame)
                if frame == 2:
                    self.punch = False
                if self.hit:
                    self.isAttack = True
                    punchSound.play()
                    playerryu.health -= 1
                    

    class Player_2(pygame.sprite.Sprite):
        walking_frames = []
        standingFrames = []
        punch_frames = []
        kick_frames = []
        jump_frames = []
        leftpunch_frames = []
        power_frames = []
        sit_left_punch_frames = []
        sit_right_punch_frames = []

        health =450    
        
        def __init__(self):
            super().__init__()
            spritesheet = Spritesheet(player_sprite_2)

            #self.image = spritesheet.getImage(2174,50,88,212)
            #self.standingFrames.append(self.image)
            self.image = spritesheet.getImage(2360,39,103,229)
            self.standingFrames.append(self.image)
            self.image = spritesheet.getImage(2558,36,103,232)
            self.standingFrames.append(self.image)
            self.image = spritesheet.getImage(2750,39,103,229)
            self.standingFrames.append(self.image)
            self.image = spritesheet.getImage(2959,42,106,226)
            self.standingFrames.append(self.image)
            
            self.image = spritesheet.getImage(2214,314,91,229)
            self.walking_frames.append(self.image)
            self.image = spritesheet.getImage(2394,317,95,226)
            self.walking_frames.append(self.image)
            self.image = spritesheet.getImage(2575,314,109,229)
            self.walking_frames.append(self.image)
            self.image = spritesheet.getImage(2758,317,109,226)
            self.walking_frames.append(self.image)
            self.image = spritesheet.getImage(2962,331,88,212)
            self.walking_frames.append(self.image)

            self.image = spritesheet.getImage(2560,592,109,229)
            self.punch_frames.append(self.image)
            self.image = spritesheet.getImage(2738,592,155,229)
            self.punch_frames.append(self.image)
            self.image = spritesheet.getImage(2953,592,109,229)
            self.punch_frames.append(self.image)
            
            self.image = spritesheet.getImage(2317,890,115,235)
            self.kick_frames.append(self.image)
            self.image = spritesheet.getImage(2497,884,195,241)
            self.kick_frames.append(self.image)
            self.image = spritesheet.getImage(2764,890,115,235)
            self.kick_frames.append(self.image)
            self.image = spritesheet.getImage(2950,895,109,230)
            self.kick_frames.append(self.image)

            self.image = spritesheet.getImage(2111,1225,108,229)
            self.leftpunch_frames.append(self.image)
            self.image = spritesheet.getImage(2300,1216,129,238)
            self.leftpunch_frames.append(self.image)
            self.image = spritesheet.getImage(2495,1216,180,238)
            self.leftpunch_frames.append(self.image)
            self.image = spritesheet.getImage(2735,1216,129,238)
            self.leftpunch_frames.append(self.image)
            self.image = spritesheet.getImage(2944,1225,109,229)
            self.leftpunch_frames.append(self.image)

            self.image = spritesheet.getImage(388,0,98,259)
            self.jump_frames.append(self.image)
            #self.image = spritesheet.getImage(557,33,86,226)
            #self.jump_frames.append(self.image)
            #self.image = spritesheet.getImage(701,64,91,195)
            #self.jump_frames.append(self.image)
            #self.image = spritesheet.getImage(855,33,86,226)
            #self.jump_frames.append(self.image)
            #self.image = spritesheet.getImage(1022,0,97,259)
            #self.jump_frames.append(self.image)

            self.image = spritesheet.getImage(2890,1896,146,212)
            self.power_frames.append(self.image)
            self.image = spritesheet.getImage(2661,1898,149,210)
            self.power_frames.append(self.image)
            self.image = spritesheet.getImage(2423,1913,180,195)
            self.power_frames.append(self.image)

            self.image = spritesheet.getImage(1440,337,112,154)
            self.sit_left_punch_frames.append(self.image)
            self.image = spritesheet.getImage(1592,334,155,157)
            self.sit_left_punch_frames.append(self.image)
            self.image = spritesheet.getImage(1815,337,112,154)
            self.sit_left_punch_frames.append(self.image)

            self.image = spritesheet.getImage(1414,107,118,155)
            self.sit_right_punch_frames.append(self.image)
            self.image = spritesheet.getImage(1589,107,160,155)
            self.sit_right_punch_frames.append(self.image)
            self.image = spritesheet.getImage(1801,107,118,155)
            self.sit_right_punch_frames.append(self.image)
            self.image = spritesheet.getImage(1982,107,103,155)
            self.sit_right_punch_frames.append(self.image)

            self.rect = self.image.get_rect()
            self.rect.center = (width / 2 + 250, height / 2 + 120)

            self.pos = 0
            
            self.stand = True
            self.walk = False
            self.kick = False
            self.punch = False
            self.leftpunch = False
            self.jump = False
            self.power = False
            self.sit_left_punch = False
            self.sit_right_punch = False

            isAttack = False

        def update(self): 
            self.pos += 2

            self.moveX = 0
            #self.moveY = 0
            
            keypressed = pygame.key.get_pressed()
            if keypressed[pygame.K_d]:
                self.walk = True
                if self.rect.x <=  width-100:
                    self.moveX = 3
                else:
                    self.moveX = 0
                    
            elif keypressed[pygame.K_a]:
                self.walk = True
                if self.rect.x >= 0:
                    self.moveX = -3
                else:
                    self.moveX = 0
                
            else:
                self.walk = False
                self.moveX = 0

            self.rect.x += self.moveX
            if keypressed[pygame.K_f]:
                self.kick = True

            elif keypressed[pygame.K_g]:
                self.punch =True

            elif keypressed[pygame.K_t]:
                self.leftpunch =True

            elif keypressed[pygame.K_w]:
                self.jump = True
                self.rect.y = 100
            elif keypressed[pygame.K_TAB]:
                self.power = True
            elif keypressed[pygame.K_z]:
                self.sit_left_punch = True
                self.rect.y = 447
            elif keypressed[pygame.K_x]:
                self.sit_right_punch = True
                self.rect.y = 447
            else:
                self.sit_right_punch = False
                self.sit_left_punch = False
                self.rect.y = 375
            
            frame = (self.pos // 30) % len(self.standingFrames)
            #print("Position",self.pos//30)
            #print("Frame",frame)
            self.image = self.standingFrames[frame]

            self.hit = pygame.sprite.groupcollide(ken, ryu, False, False)
            
            if self.walk:
                frame = (self.pos // 30) % len(self.walking_frames)
                self.image = self.walking_frames[frame]
                    
            elif self.kick:
                frame = (self.pos // 20) % len(self.kick_frames)
                self.image = self.kick_frames[frame]
                if frame == 2:
                    self.kick = False
                if self.hit:
                    self.isAttack = True
                    punchSound.play()
                    player.health -=5
            elif self.punch:
                frame = (self.pos // 10) % len(self.punch_frames)
                self.image = self.punch_frames[frame]
                if frame == 2:
                    self.punch = False
                if self.hit:
                    self.isAttack = True
                    punchSound.play()
                    player.health -=2
                    
            elif self.leftpunch:
                frame = (self.pos // 10) % len(self.leftpunch_frames)
                self.image = self.leftpunch_frames[frame]
                if frame == 3:
                    self.leftpunch = False
                if self.hit:
                    self.isAttack = True
                    punchSound.play()
                    player.health -=1
            elif self.jump:
                frame = (self.pos // 2) % len(self.jump_frames)
                self.image = self.jump_frames[frame]
                if frame ==0 :
                    self.jump = False
            elif self.power:
                frame = (self.pos // 30) % len(self.power_frames)
                self.image = self.power_frames[frame]
                if frame == 2:
                    self.power = False
                if self.hit:
                    self.isAttack = True
                    punchSound.play()
                    player.health -=5
            elif self.sit_left_punch:
                frame = (self.pos // 30) % len(self.sit_left_punch_frames)
                self.image = self.sit_left_punch_frames[frame]
                if frame == 2:
                    self.sit_left_punch = False
                    #self.rect.y = 375
                if self.hit:
                    self.isAttack = True
                    punchSound.play()
                    player.health -=1
            elif self.sit_right_punch:
                frame = (self.pos // 30) % len(self.sit_right_punch_frames)
                self.image = self.sit_right_punch_frames[frame]
                if frame == 3:
                    self.sit_right_punch = False
                    #self.rect.y = 375
                if self.hit:
                    self.isAttack = True
                    punchSound.play()
                    player.health -=1

    pygame.time.set_timer(USEREVENT,1000)
    #seconds = 30

    def timer(seconds):
        red =255,0,0
        font = pygame.font.SysFont(None,50)
        text = font.render("{}".format(str(seconds)), True, red)
        screen.blit(text, (490,10))
    def timeout():
        font = pygame.font.SysFont(None,80)
        text = font.render("TIME OUT",True,black)
        screen.blit(text,(200,200))    
    clock = pygame.time.Clock()
    FPS=90
           
    player_sprite = pygame.image.load("Simage/ken_.png")
    player_sprite_2 = pygame.image.load("Simage/ryu_.png")

    punchSound = pygame.mixer.Sound("sounds/punch2.wav")


    all_sprites = pygame.sprite.Group()
    player = Player_1()
    playerryu = Player_2()

    ken = pygame.sprite.Group()
    ken.add(player)
    ryu = pygame.sprite.Group()
    ryu.add(playerryu)

    all_sprites.add(player)
    all_sprites.add(playerryu)

    def kenHealth():
        if player.health>0:
            pygame.draw.rect(screen, blue, [10,10,player.health,40])

    def ryuHealth():
        if playerryu.health>0:
            pygame.draw.rect(screen, blue, [width-460,10,playerryu.health,40])


    def homeScreen():
        image_1 = pygame.image.load("Simage/image_1.jpg")
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
        
        seconds = 30
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == USEREVENT:
                    seconds -=1
                elif seconds == 0:
                    #game = False
                    timeout()
                    quit()
                elif player.health<=0 or playerryu.health<=0:
                    quit()
        
            screen.blit(background,(0,0,))

            all_sprites.update()
            all_sprites.draw(screen)

            kenHealth()
            ryuHealth()
            timer(seconds)
            
            
            pygame.display.update()
            clock.tick(FPS)

    homeScreen()

        
