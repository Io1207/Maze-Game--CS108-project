from utils import *

class Player:
    def __init__(self,x,startx,starty):#x will be the avatar chosen by clicking the avatar buttons at the start
        if x==1:
            self.standImage=pygame.image.load(AV1NORMAL)
        elif x==2:
            self.standImage=pygame.image.load(AV2NORMAL)
        elif x==3:
            self.standImage=pygame.image.load(AV3NORMAL)
    
    def __str__(self,name):
        return f"({self.x},{self.y})"
    
def renderPlayer(player:Player,position,screen):
    pygame.draw.rect(screen,BLACK,rect=(position[0],position[1],40,40))
    
