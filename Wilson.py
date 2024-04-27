import random

class WilsonMazeGenerator:

    def __init__(self,height,width):     
        self.cols = 2*(width//2) + 1   # Make width odd
        self.rows = 2*(height//2) + 1 # Make height odd
        # grid of cells
        self.grid = [[0 for j in range(self.cols)] for i in range(self.rows)]

        # declare instance variable
        self.visited = []    # visited cells
        self.unvisited = []  # unvisited cells
        self.path = dict()   # random walk path

        # valid directions in random walk
        self.directions = [(0,1),(1,0),(0,-1),(-1,0)]

        # indicates whether a maze is generated
        self.generated = False

        # shortest solution
        self.solution = []
        self.showSolution = False
        self.start = (self.rows-1,0)
        self.end = (0,self.cols-1)

    def __str__(self):
        arr=[]

        out = "##"*(self.cols+1)+"\n"
        for i in range(self.rows):
            out += "#"
            for j in range(self.cols):
                if self.grid[i][j] == 0:
                    out += "##"
                else:
                    if not self.showSolution:
                        out += "  "
                    elif (i,j) in self.solution:
                        out += "**"
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

        # loop until all cells have been visited
        while len(self.unvisited) > 0:
            # choose a random cell to start the walk (Step 2)
            first = self.unvisited[random.randint(0,len(self.unvisited)-1)]
            current = first
            # loop until the random walk reaches a visited cell
            while True:
                # choose direction to walk (Step 3)
                dirNum = random.randint(0,3)
                # check if direction is valid. If not, choose new direction
                while not self.is_valid_direction(current,dirNum):
                    dirNum = random.randint(0,3)
                # save the cell and direction in the path
                self.path[current] = dirNum
                # get the next cell in that direction
                current = self.get_next_cell(current,dirNum,2)
                if (current in self.visited): # visited cell is reached (Step 5)
                    break

            current = first # go to start of path
            # loop until the end of path is reached
            while True:
                # add cell to visited and cut into the maze
                self.visited.append(current)
                self.unvisited.remove(current) # (Step 6.b)
                self.cut(current)

                # follow the direction to next cell (Step 6.a)
                dirNum = self.path[current]
                crossed = self.get_next_cell(current,dirNum,1)
                self.cut(crossed) # cut crossed edge

                current = self.get_next_cell(current,dirNum,2)
                if (current in self.visited): # end of path is reached
                    self.path = dict() # clear the path
                    break
                
        self.generated = True

    def solve_maze(self):
        # if there is no maze to solve, cut the method
        if not self.generated:
            return None

        # initialize with empty path at starting cell
        self.path = dict()
        current = self.start

        # loop until the ending cell is reached
        while True:
            while True:
                # choose valid direction
                # must remain in the grid
                # also must not cross a wall
                dirNum = random.randint(0,3)
                adjacent = self.get_next_cell(current,dirNum,1)
                if self.is_valid_direction(current,dirNum):
                    hasWall = (self.grid[adjacent[0]][adjacent[1]] == 0)
                    if not hasWall:
                        break
            # add cell and direction to path
            self.path[current] = dirNum

            # get next cell
            current = self.get_next_cell(current,dirNum,2)
            if current == self.end: 
                break # break if ending cell is reached

        # go to start of path
        current = self.start
        self.solution.append(current)
        # loop until end of path is reached
        while not (current == self.end):
            dirNum = self.path[current] # get direction
            # add adjacent and crossed cells to solution
            crossed = self.get_next_cell(current,dirNum,1)
            current = self.get_next_cell(current,dirNum,2)
            self.solution.append(crossed)
            self.solution.append(current)

        self.path = dict()
                
    ## Private Methods ##
    ## Do Not Use Outside This Class ##
                
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

    def directions(self):
        length=len(self.solution)
        direction=[]
        for i in range(length):
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
        return direction
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