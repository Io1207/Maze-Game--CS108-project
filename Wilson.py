import random

class WilsonMazeGenerator:

    def __init__(self,height,width):     
        self.cols = 2*(width//2) + 1  
        self.rows = 2*(height//2) + 1 
        
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]

        self.visited = []    
        self.unvisited = []  
        self.path = dict()  
        self.collectibles=0 

        self.directions = [(0,1),(1,0),(0,-1),(-1,0)]

        self.generated = False

        self.solution = []
        self.showSolution = False
        self.start = (0,0)
        self.end = (self.rows-1,self.cols-1)

    def collectiblesGen(self,n):
        arr=self.displayAptGrid()
        listOfPathTiles=[]
        
        for i in range(self.rows):
            for j in range(self.cols):
                if arr[i][j]==1:
                    listOfPathTiles.append((i,j))
        listOfPathTiles.pop(listOfPathTiles.index((0,0)))
        listOfPathTiles.pop(listOfPathTiles.index((self.end[0],self.end[1])))
        x=len(listOfPathTiles)
        print(x)

        numPortKeys=0 #P
        Hats=0
        Boots=0
        Trophy=0
        numWands=0  #W
        numTimeTurners=0 #T
        knuts=x//125
        sickles=x//125
        galleons=x//125

        if n==1:
            numPortKeys=x//200 #P
            numWands=x//200  #W
            numTimeTurners=x//200 #T
        elif n==2:
            numPortKeys=x//200 #P
            numWands=x//180  #W
            numTimeTurners=x//200 #T
        elif n==3:
            numPortKeys=x//200 #P
            numWands=x//150  #W
            numTimeTurners=x//150 #T
        
        if numPortKeys%3==0:
            Hats,Boots,Trophy=numPortKeys/3,numPortKeys/3,numPortKeys/3
        elif numPortKeys%3==1:
            Hats,Boots,Trophy=numPortKeys//3,1+numPortKeys//3,numPortKeys//3
        elif numPortKeys%3==2:
            Hats,Boots,Trophy=1+numPortKeys//3,numPortKeys//3,1+numPortKeys//3

        collectiblesArr=[[] for i in range(self.rows+5)]
        for i in range(self.rows+5):
            for j in range(self.cols+5):
                collectiblesArr[i].append(0)

        #Allotment
        running=True
        resources=[1,2,3,4,5,6,7,8]
        while running:
            p=random.choice(resources)
            if p==1:  #Knuts
                tile=random.choice(listOfPathTiles)
                a,b=tile[0],tile[1]
                collectiblesArr[a][b]='K'
                listOfPathTiles.pop(listOfPathTiles.index(tile))
                knuts-=1
                if knuts==0:
                    resources.pop(resources.index(1))
            elif p==2:  #Sickles
                tile=random.choice(listOfPathTiles)
                a,b=tile[0],tile[1]
                collectiblesArr[a][b]='S'
                listOfPathTiles.pop(listOfPathTiles.index(tile))
                sickles-=1
                if sickles==0:
                    resources.pop(resources.index(2))
            elif p==3:  #Galleons
                tile=random.choice(listOfPathTiles)
                a,b=tile[0],tile[1]
                collectiblesArr[a][b]='G'
                listOfPathTiles.pop(listOfPathTiles.index(tile))
                galleons-=1
                if galleons==0:
                    resources.pop(resources.index(3))
            elif p==4 and (not (j,i) in self.solution):  #portkeys
                tile=random.choice(listOfPathTiles)
                a,b=tile[0],tile[1]
                collectiblesArr[a][b]='H'
                listOfPathTiles.pop(listOfPathTiles.index(tile))
                numPortKeys-=1
                Hats-=1
                if Hats==0:
                    resources.pop(resources.index(4))
            elif p==5 and (not (j,i) in self.solution):  #portkeys
                tile=random.choice(listOfPathTiles)
                a,b=tile[0],tile[1]
                collectiblesArr[a][b]='B'
                listOfPathTiles.pop(listOfPathTiles.index(tile))
                numPortKeys-=1
                Boots-=1
                if Boots==0:
                    resources.pop(resources.index(5))
            elif p==6 and (not (j,i) in self.solution):  #portkeys
                # print(self.solution.index((j,i)))
                tile=random.choice(listOfPathTiles)
                a,b=tile[0],tile[1]
                collectiblesArr[a][b]='P'
                listOfPathTiles.pop(listOfPathTiles.index(tile))
                numPortKeys-=1
                Trophy-=1
                if Trophy==0:
                    resources.pop(resources.index(6))
            elif p==7:  #wands
                tile=random.choice(listOfPathTiles)
                a,b=tile[0],tile[1]
                collectiblesArr[a][b]='W'
                listOfPathTiles.pop(listOfPathTiles.index(tile))
                numWands-=1
                if numWands==0:
                    resources.pop(resources.index(7))
            elif p==8:  #timeturner
                tile=random.choice(listOfPathTiles)
                a,b=tile[0],tile[1]
                collectiblesArr[a][b]='T'
                listOfPathTiles.pop(listOfPathTiles.index(tile))
                numTimeTurners-=1
                if numTimeTurners==0:
                    resources.pop(resources.index(8))
            if len(resources)==0:
                running=False
        self.collectibles=collectiblesArr

    def displayAptGrid(self):
        arr=[]
        arr=[[] for i in range(self.rows+5)]
        for i in range(self.rows+5):
            for j in range(self.cols+5):
                if i>=0 and i<self.rows:
                    if j>=0 and j<self.rows:
                        arr[i].append(self.grid[i][j])
                    else:
                        arr[i].append(0)
                else:
                    arr[i].append(0)
        return arr
    
    def generate_maze(self):
        self.initialize_grid()

        current = self.unvisited.pop(random.randint(0,len(self.unvisited)-1))
        self.visited.append(current)
        self.cut(current)
 
        while len(self.unvisited) > 0:
            first = self.unvisited[random.randint(0,len(self.unvisited)-1)]
            current = first
            while True:
                dirNum = random.randint(0,3)
                while not self.is_valid_direction(current,dirNum):
                    dirNum = random.randint(0,3)
                self.path[current] = dirNum
                current = self.get_next_cell(current,dirNum,2)
                if (current in self.visited): 
                    break

            current = first 
            while True:
                self.visited.append(current)
                self.unvisited.remove(current) 
                self.cut(current)

                dirNum = self.path[current]
                crossed = self.get_next_cell(current,dirNum,1)
                self.cut(crossed) 

                current = self.get_next_cell(current,dirNum,2)
                if (current in self.visited): 
                    self.path = dict() 
                    break
                
        self.generated = True

    def solve_maze(self):
        if not self.generated:
            return None

        self.path = dict()
        current = self.start

        while True:
            while True:
                dirNum = random.randint(0,3)
                adjacent = self.get_next_cell(current,dirNum,1)
                if self.is_valid_direction(current,dirNum):
                    hasWall = (self.grid[adjacent[0]][adjacent[1]] == 0)
                    if not hasWall:
                        break
            self.path[current] = dirNum

            current = self.get_next_cell(current,dirNum,2)
            if current == self.end: 
                break 

        current = self.start
        self.solution.append(current)
        while not (current == self.end):
            dirNum = self.path[current] 
            crossed = self.get_next_cell(current,dirNum,1)
            current = self.get_next_cell(current,dirNum,2)
            self.solution.append(crossed)
            self.solution.append(current)

        self.path = dict()

    #Part of maze generation DO NOT MODIFY            
    def get_next_cell(self,cell,dirNum,fact):
        dirTup = self.directions[dirNum]
        return (cell[0]+fact*dirTup[0],cell[1]+fact*dirTup[1])

    #Part of maze generation DO NOT MODIFY
    def is_valid_direction(self,cell,dirNum):
        newCell = self.get_next_cell(cell,dirNum,2)
        tooSmall = newCell[0] < 0 or newCell[1] < 0
        tooBig = newCell[0] >= self.rows or newCell[1] >= self.cols
        return not (tooSmall or tooBig)

    #Part of maze generation DO NOT MODIFY
    def initialize_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = 0
                
        # fill up unvisited cells
        for r in range(self.rows):
            for c in range(self.cols):
                if r % 2 == 0 and c % 2 == 0:
                    self.unvisited.append((r,c))

        self.visited = []
        self.path = dict()
        self.generated = False

    def cut(self,cell):
        self.grid[cell[0]][cell[1]] = 1

    def Directions(self):
        length=len(self.solution)
        direction=[]
        for i in range(length-1):
            curr=self.solution[i]
            next=self.solution[i+1]
            dx,dy=curr[0]-next[0],curr[1]-next[1]
            if dx == -1:
                direction.append('R')
            elif dx == 1:
                direction.append('L')
            elif dy == -1:
                direction.append('D')
            elif dy == 1:
                direction.append('U')
            f=open("Path.txt",'w')
            for i in range(len(direction)):
                f.write(str(direction[i])+" ")
                if i%10==0 and i!=0:
                    f.write('\n')
            f.close()
        del direction
