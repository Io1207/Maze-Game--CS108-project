from random import choice
from utils import *

# Setup
width, height = 700, 700
fps = 10000

CELLSIZE=20 
pygame.init()
sc = pygame.display.set_mode((1200, 750))
clock = pygame.time.Clock()

# Initialization
x, y = 5, 5 # Starting position
line_width=1
cols,rows=30,30
cellsize=24
line_width_2 = 1
half_size = cellsize//2
visited_color=BLACK

#wall_color=EASYMAZE

#wall_color=MEDIUMMAZE

wall_color=HARD
#wall_color = (40,195,255)
current_cell_color = pygame.Color('saddlebrown')
solution_color = pygame.Color('darkslategray')
flag = True
find_solution = False
paused = True


class Cell:
    def __init__(self,x,y):
        self.x, self.y = x, y
        self.walls = {'top':True, 'left':True, 'bottom':True, 'right':True}
        self.path = {'top':False, 'left':False, 'bottom':False, 'right':False}
        self.visited = False
        self.solution = False

    def draw(self):
        x, y = self.x * cellsize, self.y * cellsize
        if self.visited:
            pygame.draw.rect(sc, visited_color, (x, y, cellsize, cellsize))
        if self.solution:
                pygame.draw.rect(sc, solution_color, (x+CELLSIZE//6, y+CELLSIZE//6, CELLSIZE-CELLSIZE//3, CELLSIZE-CELLSIZE//3), CELLSIZE//10)
        if self.walls['top']:
            pygame.draw.line(sc, wall_color, (x,y), (x+cellsize,y), line_width)
        if self.walls['left']:
            pygame.draw.line(sc, wall_color, (x,y), (x,y+cellsize), line_width)
        if self.walls['bottom']:
            pygame.draw.line(sc, wall_color, (x,y+cellsize), (x+cellsize,y+cellsize), line_width)
        if self.walls['right']:
            pygame.draw.line(sc, wall_color, (x+cellsize,y), (x+cellsize,y+cellsize), line_width)

        #if self.path['top']:
            ##print(event)
            ##print("This caused it")
            #pygame.draw.line(sc, solution_color, (x+half_size,y), (x+half_size,y+half_size), line_width_2)
        #if self.path['left']:
            ##print(event)
            ##print("This caused it")
            #pygame.draw.line(sc, solution_color, (x,y+half_size), (x+half_size,y+half_size), line_width_2)
        #if self.path['bottom']:
            ##print(event)
            ##print("This caused it")
            #pygame.draw.line(sc, solution_color, (x+half_size,y+half_size), (x+half_size,y+cellsize), line_width_2)
        #if self.path['right']:
            ##print(event)
            ##print("This caused it")
            #pygame.draw.line(sc, solution_color, (x+half_size,y+half_size), (x+cellsize,y+half_size), line_width_2)
#   
    def draw_current_cell(self):
        x, y = self.x * cellsize, self.y * cellsize
        pygame.draw.rect(sc, current_cell_color, (x+line_width, y+line_width, cellsize-line_width, cellsize-line_width))
    
    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols-1 or y < 0 or y > rows-1:
            return False
        return grid_cells[find_index(x, y)]
    
    def check_neighbors(self):
        neighbors = []
        top = self.check_cell(self.x, self.y-1)
        left = self.check_cell(self.x-1, self.y)
        bottom = self.check_cell(self.x, self.y+1)
        right = self.check_cell(self.x+1, self.y)
        if top and not top.visited:
            neighbors.append(top)
        if left and not left.visited:
            neighbors.append(left)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if right and not right.visited:
            neighbors.append(right)
        return choice(neighbors) if neighbors else False
    

def remove_walls(current, next):
    dx, dy = current.x - next.x, current.y - next.y
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    if dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    if dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False


def add_solution_path(previous, current):
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
    
while True:        
    sc.fill(pygame.Color("darkslategray"))
    #cprint(grid_cells[0])
    for event in pygame.event.get():                
        if event.type == pygame.QUIT:   
            for x in grid_cells:
                print(x.path['left'],x.path['top'],x.path['right'],x.path['bottom'])   
            exit()                
        if event.type == pygame.KEYDOWN:                    
            if event.key == pygame.K_SPACE:                        
                find_solution = True                    
            if event.key == pygame.K_RETURN:                        
                paused = not paused        
    [cell.draw() for cell in grid_cells]        
    current_cell.visited = True        
    current_cell.draw_current_cell()        
    if not paused:
        next_cell = current_cell.check_neighbors()            
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
                    solution.pop()                    
                else:                        
                    previous_cell = current_cell
                    current_cell = grid_cells[0]
                    add_solution_path(previous_cell, current_cell)
    
    pygame.display.flip()        
    clock.tick(fps)
