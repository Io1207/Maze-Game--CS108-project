from utils import *

class Player:
    def __init__(self,pos1,pos2,name):#x will be the avatar chosen by clicking the avatar buttons at the start
        # if x==1:
        #     self.standImage=pygame.image.load(AV1NORMAL)
        # elif x==2:
        #     self.standImage=pygame.image.load(AV2NORMAL)
        # elif x==3:
        #     self.standImage=pygame.image.load(AV3NORMAL)
        self.x=pos1
        self.y=pos2
        self.name=name
    
    def __str__(self,name):
        return f"({self.x},{self.y})"
    

    
def renderPlayer(player:Player,position,screen):
    pygame.draw.rect(screen,BLACK,rect=(position[0],position[1],39,39))
    
def playerMove(player,keyPressed,presentWalls):
    #print(presentWalls)
    if keyPressed[pygame.K_LEFT]:
        if presentWalls[3]!=1:
            player.x -= 1
    if keyPressed[pygame.K_RIGHT]:
        if presentWalls[1]!=1:
            player.x += 1
    if keyPressed[pygame.K_UP]:
        if presentWalls[0]!=1:
            player.y -= 1
    if keyPressed[pygame.K_DOWN]:
        if presentWalls[2]!=1:
            player.y += 1