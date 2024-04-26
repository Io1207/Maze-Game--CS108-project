from utils import *
from Player import *
            # if event.type==pygame.KEYDOWN and amIOnPlayScreen:
            #     keysPressed = pygame.key.get_pressed()
            #     playerMove(keysPressed)

def playLoop():
    print()
    
    
def display(grid,screen):
    width=1
    for i in range(10):
        for j in range(10):
            infople=grid[i][j]
            #print(infople)
            if infople[0]:
                pygame.draw.line(screen,WHITE,((i)*40,(j)*40),((i+1)*40,(j)*40),width)
            if infople[1]:
                pygame.draw.line(screen,WHITE,((i+1)*40,(j)*40),((i+1)*40,(j+1)*40),width)
            if infople[2]:
                pygame.draw.line(screen,WHITE,((i)*40,(j+1)*40),((i+1)*40,(j+1)*40),width)
            if infople[3]:
                pygame.draw.line(screen,WHITE,((i)*40,(j)*40),((i)*40,(j+1)*40),width)


def mazeDisplay(info,player:Player):
    print("entered maze display function")
    viewPort=pygame.display.set_mode((400,700))
    viewPort.fill(pygame.Color("pink"))
    array=info[0]
    presentGrid = [[] for _ in range(10)]
    for i in range(10):
        for j in range(10):
            curr=(player.x-4+i,player.y-4+j)
            walls=array[curr[0]][curr[1]].walls
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
            print()
    # def checkCell(x, y):
    #         if x < 0 or x > cols+3 or y < 0 or y > rows+3:
    #             return False
    #         return array[x][y]
    display(presentGrid,viewPort)
    pygame.display.flip()