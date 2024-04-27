import random

class WilsonMazeGenerator:

    def __init__(self,height,width):     
        self.cols = 2*(width//2) + 1  
        self.rows = 2*(height//2) + 1 
        
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]

        self.visited = []    
        self.unvisited = []  
        self.path = dict()   

        self.directions = [(0,1),(1,0),(0,-1),(-1,0)]

        self.generated = False

        self.solution = []
        self.showSolution = False
        self.start = (0,0)
        self.end = (self.rows-1,self.cols-1)

    def __str__(self):
        arr=[]

        out = "##"*(self.cols+1)+"\n"
        for i in range(self.rows):
            out += "#"
            for j in range(self.cols):
                if self.grid[i][j] == 0:
                    out += "##"
                else:
                    if self.showSolution:
                        out += "  "
                    elif (i,j) in self.solution:
                        out += "__"
                    else:
                        out += "  "
            out += "#\n"
        return out + "##"*(self.cols+1)

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
        
    

    # def get_grid(self):
    #     return self.grid

    def get_solution(self):
        return self.solution

    def show_solution(self,show):
        self.showSolution = show
    
    def generate_maze(self):
        # reset the grid before generation
        self.initialize_grid()

        # choose the first cell to put in the visited list
        # see Step 1 of the algorithm.
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
                
    def get_next_cell(self,cell,dirNum,fact):
        dirTup = self.directions[dirNum]
        return (cell[0]+fact*dirTup[0],cell[1]+fact*dirTup[1])

    def is_valid_direction(self,cell,dirNum):
        newCell = self.get_next_cell(cell,dirNum,2)
        tooSmall = newCell[0] < 0 or newCell[1] < 0
        tooBig = newCell[0] >= self.rows or newCell[1] >= self.cols
        return not (tooSmall or tooBig)

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

    def revGrid(self):
        #reversing the solGrid
        for i in self.grid:
            print(i)
        intermed=[[] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                intermed[i].append(self.grid[i][self.rows-j-1])
        self.grid=intermed
        del intermed

    def Directions(self):
        length=len(self.solution)
        direction=[]
        for i in range(length-2):
            curr=self.solution[i]
            next=self.solution[i+1]
            dx,dy=curr[0]-next[0],curr[1]-next[1]
            if dx == -1:
                direction.append('D')
            elif dx == 1:
                direction.append('U')
            elif dy == -1:
                direction.append('R')
            elif dy == 1:
                direction.append('L')
            f=open("Path.txt",'w')
            for i in range(len(direction)):
                f.write(str(direction[i])+" ")
                if i%10==0:
                    f.write('\n')
            f.close()
        del direction
################
                
# gen = WilsonMazeGenerator(10,10)
# gen.generate_maze()
# print("Maze Generated")
# gen.solve_maze()
# print("Solution Generated")
# quest = 'y'
# gen.show_solution(quest.strip().lower() == "y")
# print(gen)
# #reversing the solGrid
# for i in gen.grid:
#     print(i)
# intermed=[[] for i in range(gen.rows)]
# for i in range(gen.rows):
#     for j in range(gen.cols):
#         intermed[i].append(gen.grid[i][gen.rows-j-1])
# gen.grid=intermed
# del intermed
# print(len(gen.grid))
# arr=gen.displayAptGrid()
# for i in gen.grid:
#     print(i)
# for i in arr:
#     print(i)
# for i in gen.solution:
#     print(i)