def pathValidity(path):
    right=left=down=up=0
    for i in range(1,np.size(path)):
        for j in path[0:i]:
            if j==1:
                up=up+1
            elif j==2:
                down=down+1
            elif j==3:
                right=right+1
            elif j==4:
                left=left+1
        if left>right:
            return False
        if (right-left)>=30:
            return False
        if up>down:
            return False
        if (down-up)>=30:
            return False
    return True

def randomise(path):
    intPath=path
    size=np.size(path)
    intSize=np.size(intPath)
    index=rand.randint(intSize)

    print()

def pathFinder(n):
#1 for up,2 for down,3 for right, 4 for left
    if n==1:
        noOfSteps=88
    elif n==2:
        noOfSteps=118
    elif n==3:
        noOfSteps=148
    twists=(noOfSteps-60)//2
    rawpath=np.zeros(noOfSteps-2)
    #for easy level we have 20 extra steps => 60necessary steps+20 frivolous ones
    #so the 20 frivolous ones need to cancel each other out which is why 10 twists and the same logic in other cases too
    necRight=29
    necDown=29
    x=twists//4
    prob=rand.randint(1,2)   #1for right and 2 for down
    y=rand.randint(twists//2-x,twists//2+x)

    if prob==1:
        noDown=y+necDown
        noRight=(twists-y)+necRight
        noLeft=(twists-y)
        noUp=y
    else:
        noRight=y+necDown
        noDown=(twists-y)+necRight
        noUp=(twists-y)
        noLeft=y
        noRight=rand.randint(twists//2-x,twists//2+x)+noOfSteps//2
        noDown=twists-noRight+noOfSteps//2

    #at start and end we can leave/arrive either right or down
    probStart=rand.randint(1,2)     #1 for right and 2 for down
    probEnd=rand.randint(1,2)


    if probStart==probEnd:
        if probStart==1:
            a=1
        else:
            a=2
    elif probStart==1:
        a=3
    else:
        a=4
    
    for i in range(noLeft):#putting the lefts in the path
        rawpath[i]=4
    for i in range(noLeft,noLeft+noUp):
        rawpath[i]=1
    if a==1:       #both starting and ending step is right
        for i in range(noLeft+noUp,noLeft+noUp+noRight-2):
            rawpath[i]=3
        for i in range(noLeft+noUp+noRight-2,noOfSteps-2):
            rawpath[i]=2
        #randomise(rawpath)
        #print(np.size(path))
        rawpath=np.insert(rawpath,0,[3])
        rawpath=np.append(rawpath,[3],0)
    if a==2:       #both starting and ending step is down
        for i in range(noLeft+noUp,noLeft+noUp+noDown-2):
            rawpath[i]=2
        for i in range(noLeft+noUp+noDown-2,noOfSteps-2):
            rawpath[i]=3
        #randomise (rawpath)
        #print(np.size(path))
        rawpath=np.insert(rawpath,0,[2])
        rawpath=np.append(rawpath,[2],0)
    if a==3:       #start right end down
        for i in range(noLeft+noUp,noLeft+noUp+noRight-1):
            rawpath[i]=3
        for i in range(noLeft+noUp+noRight-1,noOfSteps-2):
            rawpath[i]=2
        #randomise(rawpath)
        #print(np.size(path))
        rawpath=np.insert(rawpath,0,[3])
        rawpath=np.append(rawpath,[2],0)
    if a==4:       #start down end right
        for i in range(noLeft+noUp,noLeft+noUp+noDown-1):
            rawpath[i]=3
        for i in range(noLeft+noUp+noDown-1,noOfSteps-2):
            rawpath[i]=2
        #randomise(rawpath)
        #print(np.size(path))
        rawpath=np.insert(rawpath,0,[2])
        rawpath=np.append(rawpath,[3],0)
    #print(path)
    #return rawpath

import random
import pygame
# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create a grid for the maze
grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]

def generate_maze(x, y):
    grid[x][y] = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + 2 * dx, y + 2 * dy
        if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny]:
            grid[nx][ny] = 0
            grid[x + dx][y + dy] = 0
            generate_maze(nx, ny)

def draw_grid():
    screen.fill(WHITE)
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, BLACK, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

def main():
    start_x, start_y = random.randint(0, (ROWS - 3) // 2) * 2, random.randint(0, (COLS - 3) // 2) * 2
    generate_maze(start_x, start_y)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_grid()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

def pathFinder(n):
    #1 for up,2 for down,3 for right, 4 for left
    if n==1:
        noOfSteps=84
    elif n==2:
        noOfSteps=104
    elif n==3:
        noOfSteps=144
    twists=(noOfSteps-54)//2
    #for easy level we have 20 extra steps => 58necessary steps+30 frivolous ones
    #so the 30 frivolous ones need to cancel each other out which is why 10 twists and the same logic in other cases too
    necRight=27
    necDown=27
    x=twists//4
    prob=rand.randint(1,2)   #1for right and 2 for down
    y=rand.randint(x,3*x)

    if prob==1:
        noDown=y+necDown
        noRight=(twists-y)+necRight
        noLeft=(twists-y)
        noUp=y
    else:
        noRight=y+necDown
        noDown=(twists-y)+necRight
        noUp=(twists-y)
        noLeft=y
        noRight=rand.randint(twists//2-x,twists//2+x)+noOfSteps//2
        noDown=twists-noRight+noOfSteps//2

    info=[noRight,noLeft,noUp,noDown]
    #print(rawpath)
    #info=[rawpath,noOfSteps]
    return info



'''def mazeMaker(screen):
    grid = [[1 for _ in range(COLS)] for _ in range(ROWS)]   #creates the grid
    #print(math.sqrt(np.size(grid)))
    for x in range(30):
        for y in range(30):
            if (x,y) in path:
                print()
    grid[0][0]=0
    grid[29][29]=0
    current=(0,0)'''
    
    #for i in range(30):
        #for j in range(30):
            #if grid[i][j]==1:
                #loc=pygame.Rect(25*i,25*j,25,25)
                #location=pygame.draw.rect(screen,color=EASYMAZE,rect=loc)
                #screen.blit(EMAZE,25*i,25*j)
                #pygame.display.flip()
'''for i in grid:
        print(i)'''
'''for i in path:
            print(i,end=" ")
            if i==1:
                current=(current[0],current[1]-1)
                grid[current[0]][current[1]]=0
            elif i==2:
                current=(current[0],current[1]+1)
                grid[current[0]][current[1]]=0
            elif i==3:
                current=(current[0]+1,current[1])
                grid[current[0]][current[1]]=0
            elif i==4:
                current=(current[0]-1,current[1])
                grid[current[0]][current[1]]=0'''

def mazeMaker(playScreen,n):
    '''for i in range(30):
        if i==0 or i==29:
            for j in range(30):
                grid[i][j]=1
        else:
            grid[i][29]=1
            grid[i][0]=1
    for x in grid:
        print(x)'''
    start=(0,0)
    #start=(0,0)
    #current=(0,0)
    if n==1:
        pygame.draw.line(playScreen,color=EASYMAZE,start_pos=(0,0),end_pos=(750,0),width=2)
        pygame.draw.line(playScreen,color=EASYMAZE,start_pos=(750,750),end_pos=(750,0),width=2)
        pygame.draw.line(playScreen,color=EASYMAZE,start_pos=(0,748),end_pos=(750,748),width=2)
        pygame.draw.line(playScreen,color=EASYMAZE,start_pos=(0,0),end_pos=(0,750),width=2)
    if n==2:
        pygame.draw.line(playScreen,color=MEDIUMMAZE,start_pos=(0,0),end_pos=(750,0),width=2)
        pygame.draw.line(playScreen,color=MEDIUMMAZE,start_pos=(750,750),end_pos=(750,0),width=2)
        pygame.draw.line(playScreen,color=MEDIUMMAZE,start_pos=(0,748),end_pos=(750,748),width=2)
        pygame.draw.line(playScreen,color=MEDIUMMAZE,start_pos=(0,0),end_pos=(0,750),width=2)
    if n==3:
        pygame.draw.line(playScreen,color=BLACK,start_pos=(0,0),end_pos=(750,0),width=2)
        pygame.draw.line(playScreen,color=BLACK,start_pos=(750,750),end_pos=(750,0),width=2)
        pygame.draw.line(playScreen,color=BLACK,start_pos=(0,748),end_pos=(750,748),width=2)
        pygame.draw.line(playScreen,color=BLACK,start_pos=(0,0),end_pos=(0,750),width=2)
    
    '''info=pathFinder(n)
    #few cases-4 corners, 4 types of boundaries
    #conditions: noLeft never exceeds noRight noRight-noLeft<=29
    probStart=rand.randint(1,2)     #1 for right and 2 for down
    probEnd=rand.randint(1,2)
    if probStart==probEnd:
        if probStart==1:
            #both start and end are right
            info[0]=info[0]+2
            a=1
        else:
            #both start and end are down
            info[3]=info[3]+2
            a=2
    elif probStart==1:
        #start is right end is down
        info[0]=info[0]+1
        info[3]=info[3]+1
        a=3
    else:
        #start is down end is right
        info[0]=info[0]+1
        info[3]=info[3]+1
        a=4
    
    noOfSteps=info[0]+info[1]+info[2]+info[3]
    current=(0,0)
    check1=info[0]-info[1]   #net right
    check2=info[4]-info[3]   #net down
    lastMove=0

    for i in range(noOfSteps):
        if current==(0,0):
            if a==1 or a==3:    #start with a right
                current=(current[0]+1,current[1])
                info[0]=info[0]-1
                lastMove='right'
            elif a==2 or a==4:     #start with a down
                current=(current[0],current[1]+1)
                info[3]=info[3]-1
                lastMove='down'
        elif current==(29,0):
            if (check1>=0 and check1<=29) and (check2>=0 and check2<=29) and info[1]>0 and info[3]>0:
                chance=rand.randint(0,1)
                if chance==0 and lastMove!='right':    #left
                    current=(current[0]-1,current[1])
                    info[1]=info[0]-1
                    lastMove='left'
                elif (chance==1 and lastMove!="up") or (chance==0 and lastMove=='right'):      #down
                    current=(current[0],current[1]+1)
                    info[3]=info[3]-1
                    lastMove='down'
            if info[1]<=0 and info[3]>0:    #down
                current=(current[0],current[1]+1)
                info[3]=info[3]-1
                lastMove='down'
        elif current==(0,29):        
            if (check1>=0 and check1<=29) and (check2>=0 and check2<=29) and info[0]>0 and info[4]>0:
                chance=rand.randint(0,1)
                if chance==0:      #right
                    current=(current[0]+1,current[1])
                    info[0]=info[0]-1
                    lastMove='right'
                else:      #up
                    current=(current[0],current[1]-1)
                    info[2]=info[2]-1
                    lastMove='up'
            elif info[2]<=0 and info[0]>0:
                #right
                current=(current[0]+1,current[1])
                info[0]=info[0]-1
                lastMove='right'
            elif info[0]<=0 and info[2]>0:
                #up
                current=(current[0],current[1]-1)
                info[2]=info[2]-1
                lastMove='up'''

"""if __name__=="__main__":
    screen=pygame.display.set_mode((1000,750))
    mazeMaker(screen)
    pygame.display.flip()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False"""