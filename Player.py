from utils import *
import random

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
        self.timeTurn=False
        self.portKey=False


    
    def __str__(self,name):
        return f"({self.x},{self.y})"
    
    def getPlayerReso(self):
        reso=[self.name,self.x,self.y,self.wandAttacks,self.knuts,self.galleons,self.sickles]
        return reso

    
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

def turnTime(player:Player,time):
    if player.timeTurn==True:
        time+=10
    player.timeTurn=False

def teleport(player:Player,solution:list,n):
        a=len(solution)
        b=0
        destinations=[]
        if n==1:
            b=a//6
            destinations=solution[b:a//2+b//2]
        elif n==2:
            b=a//4
            destinations=solution[a//2-b//2:a//2+b]
        elif n==3:
            b=a//4
            destinations=solution[a//2-b:a//2+b]
        final=random.choice(destinations)
        player.x=final[0]
        player.y=final[1]
        player.portKey=False
        print(f"({player.x},{player.y})")
        print(solution.index((player.x,player.y)))


    
def playerMove(player:Player,keyPressed,grid,collectibles,time,solution,n):
    #print(grid)
    # print("move function called")
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
    if a=='K':
        # print("collectibles called")
        player.knuts+=1
        collectibles[player.x][player.y]=0
    elif a=='S':
        player.sickles+=1
        collectibles[player.x][player.y]=0
    elif a=='G':
        player.galleons+=1
        collectibles[player.x][player.y]=0
    elif a=='H':
        player.portKey=True
        collectibles[player.x][player.y]=0
        teleport(player,solution,n)
    elif a=='B':
        player.portKey=True
        collectibles[player.x][player.y]=0
        teleport(player,solution,n)
    elif a=='P':
        player.portKey=True
        collectibles[player.x][player.y]=0
        teleport(player,solution,n)
    elif a=='T':
        player.timeTurn=True
        turnTime(player,time)
        collectibles[player.x][player.y]=0
    elif a=='W':
        player.wandAttacks+=1
        collectibles[player.x][player.y]=0
