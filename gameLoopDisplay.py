from utils import *
from Player import *
import random as rand
import sys

def chooseBG(x:int,screen:pygame.Surface):
    if x==1:
        screen.fill((0,0,128))
        screen.blit(BG1,(0,0))
    elif x==2:
        screen.fill((86,2,25))
        screen.blit(BG2,(0,0))
    elif x==3:
        screen.fill((0,0,128))
        screen.blit(BG3,(0,0))
    elif x==4:
        screen.fill((246,190,0))
        screen.blit(BG4,(0,0))
    elif x==5:
        screen.fill((26,71,42))
        screen.blit(BG5,(0,0))

def collectibles(i,j,screen:pygame.Surface,cellsize,status):
    
    if status=='K':
        # print("collectibles called")
        screen.blit(KNUTS,(i*cellsize,j*cellsize))
    if status=='S':
        screen.blit(SICKLES,(i*cellsize,j*cellsize))
    if status=='G':
        screen.blit(GALLEONS,(i*cellsize,j*cellsize))
    if status=='H':
        screen.blit(HAT,(i*cellsize,j*cellsize))
    if status=='B':
        screen.blit(BOOT,(i*cellsize,j*cellsize))
    if status=='P':
        screen.blit(TROPHY,(i*cellsize,j*cellsize))
    if status=='T':
        screen.blit(TURNER,(i*cellsize,j*cellsize))
    if status=='W':
        screen.blit(WAND,(i*cellsize,j*cellsize))


def makeWalls(i,j,screen:pygame.Surface,size):
    screen.blit(WALLS,(i*size,j*size))
    # print("wall ",end="")

def playLoop(player:Player,info,collect,a,n,solution):
    running=True
    viewPort=pygame.display.set_mode((500,750))
    x=rand.randint(1,5)
    pygame.mixer.music.load('BackGTheme.mp3')
    pygame.mixer.music.play(3)
    arr=info
    arr2=collect
    cellsize=50
    fps=720
    detectCollision=True
    # f=open('debug.txt','w')
    # for i in range(len(arr)):
    #     f.write(str(arr[i]))
    #     f.write('\n')
    # f.close()
    clock=pygame.time.Clock()
    time=0
    # dt=0
    if n==1:
        time=210
        # dt=clock.tick(59)/16
    if n==2:
        time=300
        # dt=clock.tick(60)/17
    if n==3:
        time=360
        # dt=clock.tick(60)/17
    # f=open("arr.txt",'w')
    # f.write(str(arr))
    # f.close()
    # f=open("debug.txt",'w')
    while running:
        for event in pygame.event.get():
            if event.type!=pygame.MOUSEMOTION:
                if event.type==pygame.QUIT:
                    #print(player.getPlayerReso())
                    exit()
                if event.type==pygame.KEYDOWN and (event.key in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_m,pygame.K_e]):
                    keyPressed=pygame.key.get_pressed()
                    # print("Before: ", player.x, player.y)
                    if keyPressed[pygame.K_e]:
                        detectCollision=not detectCollision
                        print(detectCollision)
                    if not keyPressed[pygame.K_m]:
                        playerMove(player,keyPressed,presentGrid,collect,time,solution,n)
                    # print("After: ", player.x, player.y)
            
                chooseBG(x,viewPort)
                
                presentGrid = [[] for i in range(10)]
                for i in range(10):
                    for j in range(10):
                        curr=(player.x-4+i,player.y-4+j)
                        presentGrid[i].append(arr[curr[0]][curr[1]])

                presentCollectibles = [[] for i in range(10)]
                for i in range(10):
                    for j in range(10):
                        curr=(player.x-4+i,player.y-4+j)
                        presentCollectibles[i].append(arr2[curr[0]][curr[1]])
                #Debugging
                # f=open("arr.txt",'w')
                # for i in range(10):
                #     f.write(str(presentGrid[i]))
                #     f.write('\n')
                # f.close()

                for i in range(10):
                    for j in range(10):
                        cellStatus=presentGrid[j][i]
                        collectibleStatus=presentCollectibles[i][j]
                        #print(cellStatus)
                        if cellStatus==0:
                            makeWalls(j,i,viewPort,cellsize)
                            # pygame.draw.line(viewPort,WHITE,(((i+1)*cellsize)-1,((j)*cellsize)-1),(((i+1)*cellsize-1),((j+1)*cellsize-1)),width)
                        if collectibleStatus!=0:
                            collectibles(i,j,viewPort,cellsize,collectibleStatus)
                    
        # if time>0:
        #     time=time-dt
            
        #Debugging
        # f=open("debug.txt",'w')
        # f.write(str(time)+"  ")
        # f.write('\n')
        # f.close()
        renderPlayer(player,(200,200),viewPort,a)
        pygame.draw.rect(viewPort,BLACK,(0,475,500,80))
        pygame.display.flip()
        if (player.x,player.y)==(len(info)-6,len(info)-6):
            # print("End game")
        # if (player.x,player.y)==(1,0) or (player.x,player.y)==(0,1):
            running=False
            break
        clock.tick(fps)

        # clock.tick(FPS)
        ####
    # f.close()
    return [player.getPlayerReso() ,time]
    