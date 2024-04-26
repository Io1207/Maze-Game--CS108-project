from utils import *
from Player import *
            # if event.type==pygame.KEYDOWN and amIOnPlayScreen:
            #     keysPressed = pygame.key.get_pressed()
            #     playerMove(keysPressed)

def playLoop(player:Player,info):
    print("Entered the display")
    running=True
    viewPort=pygame.display.set_mode((400,700))
    arr=info[0]
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()
            if event.type==pygame.KEYDOWN:
                keyPressed=pygame.key.get_pressed()
                #print(f"({player.x},{player.y})",end="  ")
                playerMove(player,keyPressed,presentGrid[4][4])

        ####   
        #print("Yes here", end=" ")
        viewPort.fill(pygame.Color("Navy Blue"))
        presentGrid = [[] for _ in range(10)]
        for i in range(10):
            for j in range(10):
                curr=(player.x-4+i,player.y-4+j)
                walls=arr[curr[0]][curr[1]].walls
                # curr=Cell(player.x-4+i,player.y-4+j)
                # walls=curr.walls
                #print(walls)
                walltuple=(0,0,0,0)
                if walls['top']:
                    walltuple=(1,walltuple[1],walltuple[2],walltuple[3])
                if walls['right']:
                    walltuple=(walltuple[0],1,walltuple[2],walltuple[3])
                if walls['bottom']:
                    walltuple=(walltuple[0],walltuple[1],1,walltuple[3])
                if walls['left']:
                    walltuple=(walltuple[0],walltuple[1],walltuple[2],1)
                presentGrid[i].append(walltuple)
        width=1
        for i in range(10):
            for j in range(10):
                infople=presentGrid[i][j]
                #print(infople)
                if infople[0]:
                    pygame.draw.line(viewPort,WHITE,(((i)*40)-1,((j)*40)-1),(((i+1)*40-1),((j)*40)-1),width)
                if infople[1]:
                    pygame.draw.line(viewPort,WHITE,(((i+1)*40)-1,((j)*40)-1),(((i+1)*40-1),((j+1)*40-1)),width)
                if infople[2]:
                    pygame.draw.line(viewPort,WHITE,(((i)*40)-1,((j+1)*40)-1),(((i+1)*40)-1,((j+1)*40)-1),width)
                if infople[3]:
                    pygame.draw.line(viewPort,WHITE,(((i)*40)-1,((j)*40)-1),(((i)*40)-1,((j+1)*40)-1),width)
        renderPlayer(player,(160,160),viewPort)
        pygame.display.flip()
        ####
    return    
    
    
# def display(grid,screen):
#     width=1
#     for i in range(10):
#         for j in range(10):
#             infople=grid[i][j]
#             #print(infople)
#             if infople[0]:
#                 pygame.draw.line(screen,WHITE,((i)*40,(j)*40),((i+1)*40,(j)*40),width)
#             if infople[1]:
#                 pygame.draw.line(screen,WHITE,((i+1)*40,(j)*40),((i+1)*40,(j+1)*40),width)
#             if infople[2]:
#                 pygame.draw.line(screen,WHITE,((i)*40,(j+1)*40),((i+1)*40,(j+1)*40),width)
#             if infople[3]:
#                 pygame.draw.line(screen,WHITE,((i)*40,(j)*40),((i)*40,(j+1)*40),width)


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