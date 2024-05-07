#For the love of sweet God, please work
from utils import *
from random import choice
#import numpy as np

def directionBcozTAAsked(path:list):
    startIndex=0
    currentIndex=path[startIndex]
    nextIndex=path[startIndex+1]
    direction=[]
    while startIndex<len(path)-2:
        current=Cell(currentIndex[0],currentIndex[1])
        next=Cell(nextIndex[0],nextIndex[1])
        dx, dy = current.x - next.x, current.y - next.y
        if dx == -1:
            direction.append('R')
        elif dx == 1:
            direction.append('L')
        elif dy == -1:
            direction.append('D')
        elif dy == 1:
            direction.append('U')
        startIndex=startIndex+1
        currentIndex=path[startIndex]
        nextIndex=path[startIndex+1]
    j=1
    f=open(PATHFILE,"w")
    f.write("(")
    for i in direction:
        f.write(f"{i} ")
        if j%10==0:
            f.write('\n')
        j=j+1
    f.write(")")
    f.close()

class Cell:
        def __init__(cell,x,y):
            cell.x, cell.y = x, y
            cell.walls = {'top':True, 'left':True, 'bottom':True, 'right':True}
            cell.path = {'top':False, 'left':False, 'bottom':False, 'right':False}
            cell.visited = False
            cell.solution = False

        def __str__(cell):
            return f"({cell.x},{cell.y})"


def mazeMaker(n):
    print("entered maze gen")
    clock = pygame.time.Clock()

    # Initialization
    x, y = 0, 0 # Starting position
    
    if n==1:
        cols,rows=30,30
        wall_color=EASYMAZE
    if n==2:
        cols, rows=35,35
        wall_color=MEDIUMMAZE
    if n==3:
        cols,rows=40,40
        wall_color=HARDMAZE
    
    flag = True
    find_solution = True
    paused = False
    fps=100000

    #Add the text for when the person wants to start, maybe include some instructions 
    #and tell them that it is also taking time to make the maze, they're not the only deciding factors here

    # def draw(cell:Cell):
    #     x, y = cell.x * size, cell.y * size
    #     if cell.visited:
    #         pygame.draw.rect(sc, visited_color, (x, y, size, size))
    # #  if cell.solution:
    # #     pygame.draw.rect(sc, solution_color, (x+size//6, y+size//6, size-size//3, size-size//3), size//10)
    #     if cell.walls['top']:
    #         pygame.draw.line(sc, wall_color, (x,y), (x+size,y), line_width)
    #     if cell.walls['left']:
    #         pygame.draw.line(sc, wall_color, (x,y), (x,y+size), line_width)
    #     if cell.walls['bottom']:
    #         pygame.draw.line(sc, wall_color, (x,y+size), (x+size,y+size), line_width)
    #     if cell.walls['right']:
    #         pygame.draw.line(sc, wall_color, (x+size,y), (x+size,y+size), line_width)

    #     # if cell.path['top']:
    #     #     pygame.draw.line(sc, solution_color, (x+half_size,y), (x+half_size,y+half_size), line_width_2)
    #     # if cell.path['left']:
    #     #     pygame.draw.line(sc, solution_color, (x,y+half_size), (x+half_size,y+half_size), line_width_2)
    #     # if cell.path['bottom']:
    #     #     pygame.draw.line(sc, solution_color, (x+half_size,y+half_size), (x+half_size,y+size), line_width_2)
    #     # if cell.path['right']:
    #     #     pygame.draw.line(sc, solution_color, (x+half_size,y+half_size), (x+size,y+half_size), line_width_2)

    # def draw_current_cell(cell:Cell):
    #     x, y = cell.x * size, cell.y * size
    #     pygame.draw.rect(sc, current_cell_color, (x+line_width, y+line_width, size-line_width, size-line_width))

    def checkCell(x, y):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols-1 or y < 0 or y > rows-1:
            return False
        return grid_cells[find_index(x, y)]

    def check_neighbors(cell:Cell):
        neighbors = []
        top = checkCell(cell.x, cell.y-1)
        left = checkCell(cell.x-1, cell.y)
        bottom = checkCell(cell.x, cell.y+1)
        right = checkCell(cell.x+1, cell.y)
        if top and not top.visited:
            neighbors.append(top)
        if left and not left.visited:
            neighbors.append(left)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if right and not right.visited:
            neighbors.append(right)
        return choice(neighbors) if neighbors else False


    def remove_walls(current:Cell, next:Cell):
        x1,y1=current.x,current.y
        x2,y2=next.x,next.y
        dx, dy = x1 - x2, y1 - y2
        if dx == 1:
            current.walls['left'] = False
            next.walls['right'] = False
            cellGrid[x1][y1].walls['left']=False
            cellGrid[x2][y2].walls['right'] = False
        if dx == -1:
            current.walls['right'] = False
            next.walls['left'] = False
            cellGrid[x1][y1].walls['right']=False
            cellGrid[x2][y2].walls['left'] = False
        if dy == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
            cellGrid[x1][y1].walls['top']=False
            cellGrid[x2][y2].walls['bottom'] = False
        if dy == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
            cellGrid[x1][y1].walls['bottom']=False
            cellGrid[x2][y2].walls['top'] = False
        if x1==0 and y1==0:
            print("Changed the origin's walls")
            cellGrid[x1][y1].walls['bottom']=False
            cellGrid[x1][y1].walls['right']=False
            cellGrid[x1+1][y1].walls['top']=False
            cellGrid[x1][y1+1].walls['left']=False
            print(cellGrid[1][0].walls)
            print(cellGrid[0][1].walls)
            print(cellGrid[0][0].walls)

    def add_solution_path(previous:Cell, current:Cell):
        dx, dy = current.x - previous.x, current.y - previous.y
        if dx == 1:
            current.path['left'] = True
            previous.path['right'] = True
        if dx == -1:
            current.path['right'] = True
            previous.path['left'] = True
        if dy == 1:
            current.path['top'] = True
            previous.path['bottom'] = True
        if dy == -1:
            current.path['bottom'] = True
            previous.path['top'] = True
        

    grid_cells = [Cell(col,row) for row in range(rows) for col in range(cols)]
    current_cell = grid_cells[0]
    stack = []
    solution = []
    path=[]

    print("declared grid_cells")

    cellGrid=[]
    cellGrid = [[] for _ in range(rows + 5)]
    for i in range(rows+5):
        for j in range(cols+5):
            curr=Cell(i,j)
            cellGrid[i].append(curr)
    for i in range(rows,rows+5):
        for j in range(cols,cols+5):
            curr=Cell(i,j)
            print("changed padding cells' walls")
            curr.walls = {'top':False, 'left':False, 'bottom':False, 'right':False}
            curr.path = {'top':False, 'left':False, 'bottom':False, 'right':False}
            curr.visited = True
            curr.solution = False

    #print("declared cell grid with padding",len(cellGrid))

    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                
        current_cell.visited = True
     

        if not paused:
        
            next_cell = check_neighbors(current_cell)
            if next_cell:
                next_cell.visited = True
                stack.append(current_cell)
                remove_walls(current_cell, next_cell)
                current_cell = next_cell
                if flag:
                    solution.append(current_cell)
            elif stack:
                if current_cell.x == cols-1 and current_cell.y == rows-1:
                    flag = False # solution is found
                if flag:
                    solution.pop()
                current_cell = stack.pop()
            else:
                if find_solution:
                    
                    if solution:
                        previous_cell = current_cell
                        current_cell = solution[-1]
                        current_cell.solution = True
                        add_solution_path(previous_cell, current_cell)
                        path.append((current_cell.x,current_cell.y))
                        solution.pop()
                    else:
                        previous_cell = current_cell
                        current_cell = grid_cells[0]
                        add_solution_path(previous_cell, current_cell)
                    if current_cell.x==0 and current_cell.y==0:
                        find_solution=False
                elif (current_cell.x==0 and current_cell.y==0):
                    path.append((0,0))
                    path=list(reversed(path))
                    directionBcozTAAsked(path)
                    info=[cellGrid]
                    pygame.display.flip()
                    return info

        #pygame.display.flip()
        clock.tick(fps)