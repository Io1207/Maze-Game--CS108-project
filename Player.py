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

    
    def __str__(self,name):
        return f"({self.x},{self.y})"
    
    

    
def renderPlayer(player:Player,position,screen):

    # playerRect=pygame.draw.rect(screen,BLACK,rect=(position[0],position[1],50,50))
    # playerRect.set_alpha(10)

    #Create a rectangle
    rect = pygame.Rect(position[0], position[1], 50, 50)

    rect_surface = pygame.Surface((rect.width, rect.height))

    # Draw the rectangle onto the surface
    pygame.draw.rect(rect_surface, BLACK, (0,0,50,50))

    #Set the alpha value of the surface
    rect_surface.set_alpha(100)

    screen.blit(rect_surface, (position[0], position[1]))
    
def playerMove(player,keyPressed,grid):
    #print(grid)
    #player's position in the grid is always (4,4)
    if keyPressed[pygame.K_LEFT]:
        if grid[4][3]!=0:
            player.x -= 1
    if keyPressed[pygame.K_RIGHT]:
        if grid[4][5]!=0:
            player.x += 1
    if keyPressed[pygame.K_UP]:
        if grid[3][4]!=0:
            player.y -= 1
    if keyPressed[pygame.K_DOWN]:
        if grid[5][4]!=0:
            player.y += 1
