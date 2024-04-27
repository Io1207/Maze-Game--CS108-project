from utils import *
from Player import *
import random as rand

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

def makeWalls(i,j,screen:pygame.Surface,size):
    screen.blit(WALLS,(i*size,j*size))
    # print("wall ",end="")

def playLoop(player:Player,info,a):
    running=True
    viewPort=pygame.display.set_mode((500,750))
    x=rand.randint(1,5)
    
    arr=info
    cellsize=50
    f=open('debug.txt','w')
    for i in range(len(arr)):
        f.write(str(arr[i]))
        f.write('\n')
    f.close()
    # f=open("arr.txt",'w')
    # f.write(str(arr))
    # f.close()
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.KEYDOWN:
                keyPressed=pygame.key.get_pressed()
                # print("Before: ", player.x, player.y)
                playerMove(player,keyPressed,presentGrid)
                # print("After: ", player.x, player.y)
        
            chooseBG(x,viewPort)

            presentGrid = [[] for i in range(10)]
            for i in range(10):
                for j in range(10):
                    curr=(player.x-4+i,player.y-4+j)
                    presentGrid[i].append(arr[curr[0]][curr[1]])

            #Debugging
            # f=open("arr.txt",'w')
            # for i in range(10):
            #     f.write(str(presentGrid[i]))
            #     f.write('\n')
            # f.close()

            for i in range(10):
                for j in range(10):
                    cellStatus=presentGrid[j][i]
                    #print(cellStatus)
                    if cellStatus==0:
                            makeWalls(j,i,viewPort,cellsize)
                        # pygame.draw.line(viewPort,WHITE,(((i+1)*cellsize)-1,((j)*cellsize)-1),(((i+1)*cellsize-1),((j+1)*cellsize-1)),width)
            renderPlayer(player,(200,200),viewPort,a)
            pygame.display.flip()
        ####
    return    
    
    
# def display(grid,screen):
#     width=1
#     for i in range(10):
#         for j in range(10):
#             cellStatus=grid[i][j]
#             #print(cellStatus)
#             if cellStatus[0]:
#                 pygame.draw.line(screen,WHITE,((i)*cellsize,(j)*cellsize),((i+1)*cellsize,(j)*cellsize),width)
#             if cellStatus[1]:
#                 pygame.draw.line(screen,WHITE,((i+1)*cellsize,(j)*cellsize),((i+1)*cellsize,(j+1)*cellsize),width)
#             if cellStatus[2]:
#                 pygame.draw.line(screen,WHITE,((i)*cellsize,(j+1)*cellsize),((i+1)*cellsize,(j+1)*cellsize),width)
#             if cellStatus[3]:
#                 pygame.draw.line(screen,WHITE,((i)*cellsize,(j)*cellsize),((i)*cellsize,(j+1)*cellsize),width)


# def mazeDisplay(info,player:Player):
#     print("entered maze display function")
#     viewPort=pygame.display.set_mode((400,700))
#     viewPort.fill(pygame.Color("Cyan"))
#     array=info[0]
#     presentGrid = [[] for _ in range(10)]
#     for i in range(10):
#         for j in range(10):
#             curr=(player.x-4+i,player.y-4+j)
#             walls=array[curr[0]][curr[1]].walls
#             # curr=Cell(player.x-4+i,player.y-4+j)
#             # walls=curr.walls
#             #print(walls)
#             walltuple=(0,0,0,0)
#             if walls['top']:
#                 walltuple=(1,walltuple[1],walltuple[2],walltuple[3])
#             if walls['right']:
#                 walltuple=(walltuple[0],1,walltuple[2],walltuple[3])
#             if walls['bottom']:
#                 walltuple=(walltuple[0],walltuple[1],1,walltuple[3])
#             if walls['left']:
#                 walltuple=(walltuple[0],walltuple[1],walltuple[2],1)
#             presentGrid[i].append(walltuple)
#             print()
#     # def checkCell(x, y):
#     #         if x < 0 or x > cols+3 or y < 0 or y > rows+3:
#     #             return False
#     #         return array[x][y]
#     display(presentGrid,viewPort)
#     pygame.display.flip()