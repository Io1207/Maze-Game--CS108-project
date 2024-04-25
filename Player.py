from utils import *

class Player:
    def __init__(self,x,pos1,pos2):#x will be the avatar chosen by clicking the avatar buttons at the start
        if x==1:
            self.standImage=pygame.image.load(AV1NORMAL)
        elif x==2:
            self.standImage=pygame.image.load(AV2NORMAL)
        elif x==3:
            self.standImage=pygame.image.load(AV3NORMAL)
        self.x=pos1
        self.y=pos2
        
    
    def __str__(self,name):
        return f"({self.x},{self.y})"
    

    
def renderPlayer(player:Player,position,screen):
    pygame.draw.rect(screen,BLACK,rect=(position[0],position[1],40,40))
    
def playerMove(player,keyPressed):
    if keyPressed[pygame.K_LEFT]:
        player.x -= 40
    if keyPressed[pygame.K_RIGHT]:
        player.x += 40
    if keyPressed[pygame.K_UP]:
        player.y -= 40
    if keyPressed[pygame.K_DOWN]:
        player.y += 40