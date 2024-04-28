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
        self.wandAttacks=5
        self.knuts=0
        self.galleons=0
        self.sickles=0
        self.time=0
        self.portKey=False


    
    def __str__(self,name):
        return f"({self.x},{self.y})"
    
    

    
def renderPlayer(player:Player,position,screen,a):

    # playerRect=pygame.draw.rect(screen,BLACK,rect=(position[0],position[1],50,50))
    # playerRect.set_alpha(10)

    #Create a rectangle
    rect = pygame.Rect(position[0], position[1], 50, 50)

    #rect_surface = pygame.Surface((rect.width, rect.height))

    #x=pygame.draw.rect(rect_surface, BLACK, (0,0,50,50))

    #rect_surface.set_alpha(100)

    if a==1:
        screen.blit(HARRY, (position[0], position[1]))
    elif a==2:
        screen.blit(HERM, (position[0], position[1]))
    elif a==3:
        screen.blit(RON, (position[0], position[1]))
    elif a==4:
        screen.blit(DUMB, (position[0], position[1]))
    elif a==5:
        screen.blit(MCG, (position[0], position[1]))
    elif a==6:
        screen.blit(DRACO, (position[0], position[1]))
    elif a==7:
        screen.blit(DOBBY, (position[0], position[1]))
    elif a==8:
        screen.blit(LUNA, (position[0], position[1]))
    elif a==9:
        screen.blit(SIRIUS, (position[0], position[1]))
    elif a==10:
        screen.blit(HAGRID, (position[0], position[1]))
    elif a==11:
        screen.blit(SNAPE, (position[0], position[1]))

    
    
def playerMove(player:Player,keyPressed,grid,collectibles):
    #print(grid)
    #player's position in the grid is always (4,4)
    if keyPressed[pygame.K_LEFT]:
        if grid[3][4]!=0:
            player.x -= 1
    if keyPressed[pygame.K_RIGHT]:
        if grid[5][4]!=0:
            player.x += 1
    if keyPressed[pygame.K_UP]:
        if grid[4][3]!=0:
            player.y -= 1
    if keyPressed[pygame.K_DOWN]:
        if grid[4][5]!=0:
            player.y += 1
    a=collectibles[player.x][player.y]
    
