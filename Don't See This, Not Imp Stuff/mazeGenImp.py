from utils import *
from random import choice
#import numpy as np

def mazeMaker(screen,n):
    print("entered mazeMaker")
    clock=pygame.time.Clock()

    if n==1:
        cols,rows=20,20
        cellsize=25
        wallColor=EASYMAZE
    if n==2:
        cols, rows=25,25
        cellsize=25
        wallColor=MEDIUMMAZE
    if n==3:
        cols,rows=30,30
        cellsize=25
        wallColor=HARDMAZE
    
    #general settings
    visitedColor=BLACK
    current_cell_color=WHITE
    wallWidth=1
    flag=True
    paused=False
    findSolution=True

    class Cell:
        def __init__(self,x,y):
            self.row,self.col=x,y
            self.walls={"top":True,"right":True,"bottom":True,'left':True}
            self.solution=False
            self.approach={"in":0,"out":0}
            self.visited=False
            #self.WallCount=4

        def __str__(self):
            return f"({self.row},{self.col})"

        def drawCell(self):
            if self.visited:
                pygame.draw.rect(screen, visitedColor, (self.row*cellsize, self.col*cellsize, cellsize, cellsize))
            if self.walls['top']:
                pygame.draw.line(screen,wallColor,(self.row*cellsize,self.col*cellsize),((self.row+1)*cellsize,(self.col)*cellsize),wallWidth)
            if self.walls['right']:
                pygame.draw.line(screen,wallColor,((self.row+1)*cellsize,self.col*cellsize),((self.row+1)*cellsize,(self.col+1)*cellsize),wallWidth)
            if self.walls['bottom']:
                pygame.draw.line(screen,wallColor,(self.row*cellsize,(self.col+1)*cellsize),((self.row+1)*cellsize,(self.col+1)*cellsize),wallWidth)
            if self.walls['left']:
                pygame.draw.line(screen,wallColor,(self.row*cellsize,self.col*cellsize),((self.row)*cellsize,(self.col+1)*cellsize),wallWidth)
            if self.visited:
                pygame.draw.rect(screen,visitedColor,rect=(self.row*cellsize,self.col*cellsize,(self.row+1)*cellsize,(self.col+1)*cellsize))
            
        #def drawPath():
            #print()
        
        def check_cell(self, x, y):
            if x < 0 or x > cols-1 or y < 0 or y > rows-1:
                return False
            return cellGrid[x][y]

        def check_neighbors(self):
            neighbors = []
            top = self.check_cell(self.row, self.col-1)
            left = self.check_cell(self.row-1, self.col)
            bottom = self.check_cell(self.row, self.col+1)
            right = self.check_cell(self.row+1, self.col)
            if top and not top.visited:
                neighbors.append(top)
            if left and not left.visited:
                neighbors.append(left)
            if bottom and not bottom.visited:
                neighbors.append(bottom)
            if right and not right.visited:
                neighbors.append(right)
            return choice(neighbors) if neighbors else False
        
        
        def draw_current_cell(self):
            x, y = self.row * cellsize, self.col * cellsize
            pygame.draw.rect(screen, current_cell_color, (x+wallWidth, y+wallWidth, cellsize-wallWidth, cellsize-wallWidth))

    def findPath():
        current=(0,0)
        path=[(0,0)]
        curr=Cell(current[0],current[1])
        while current!=(cols-1,rows-1):
            if current.approach['in']==1:
                current=(current[0]-1,current[1])
            elif current.approach['in']==3:
                current=(current[0]+1,current[1])
            elif current.approach['in']==2:
                current=(current[0],current[1]+1)
            elif current.approach['in']==4:
                current=(current[0],current[1]-1)
            path.append(current)
        return path
    
    def remove_walls(curr, next):
            dx, dy = curr.row - next.row, curr.col - next.col
            if dx == 1:
                curr.walls['left'] = False
                next.walls['right'] = False
            if dx == -1:
                curr.walls['right'] = False
                next.walls['left'] = False
            if dy == 1:
                curr.walls['top'] = False
                next.walls['bottom'] = False
            if dy == -1:
                curr.walls['bottom'] = False
                next.walls['top'] = False
    
    def add_solution_path(previous:Cell, current:Cell):
        dx, dy = current.row - previous.row, current.col - previous.col
        if dx == 1:
            #current.solution=True
            #previous.solution=True
            current.approach['in']=4
            previous.approach['out']=2
        elif dx == -1:
            #current.solution=True
            #previous.solution=True
            current.approach['in']=2
            previous.approach['out']=4
        if dy == 1:
            #current.solution=True
            #previous.solution=True
            current.approach['in']=1
            previous.approach['out']=3
        elif dy == -1:
            #current.solution=True
            #previous.solution=True
            current.approach['in']=3
            previous.approach['out']=1

    #Initialising a grid of cells in a matrix form to hopefully make the rest of my life with this project easier
    cellGrid=[]
    for i in range(rows):
        cellGrid.append([])
    for i in range(rows):
        for j in range(cols):
            curr=Cell(i,j)
            cellGrid[i].append(curr)
    
    grid_cells = [Cell(col,row) for row in range(rows) for col in range(cols)]
    current_cell = grid_cells[0]
    stack = []
    solution = []
    runFunction=True

    while runFunction:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #path=findPath()
                    exit()

        [cell.drawCell() for cell in grid_cells]   #draw all the cells 
        current_cell.visited = True
        
        current_cell.draw_current_cell()


        if not paused:
            #print("Entered the maze making part")
            next_cell = current_cell.check_neighbors()
            if next_cell:
                #print("moving on to different parts of the maze")
                next_cell.visited = True
                stack.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
                if flag:
                    solution.append(current_cell)
            elif stack:
                print("hi")
                if current_cell.row == cols-1 and current_cell.col == rows-1:
                    flag = False # solution is found
                if flag:
                    solution.pop()
                current_cell = stack.pop()
            else:
                ###########
                print(current_cell)
                if findSolution:
                    if solution:
                        previous_cell = current_cell
                        current_cell = solution[-1]
                        current_cell.solution = True
                        add_solution_path(previous_cell, current_cell)
                        solution.pop()
                    else:
                        previous_cell = current_cell
                        current_cell = grid_cells[0]
                        add_solution_path(previous_cell, current_cell)
                elif current_cell.x==0 and current_cell.y==0:
                    #path=findPath()
                    #print(path)
                    print("Hi")
                    return
                ###########
                

        pygame.display.flip()
        clock.tick(FPS)