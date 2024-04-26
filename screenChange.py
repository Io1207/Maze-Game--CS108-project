from utils import *
from HopefullyWorkingMazeGen import *
from Player import *

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

def screenChange(n):
    if n==0: #Going to game Screen
        #screen=pygame.display.set_mode((WIDTH,HEIGHT))
        
        screen=pygame.display.set_mode((WIDTH,HEIGHT))
        screen.fill(color=(0,0,0))
        
        screen.blit(LOGO,(((WIDTH//2)-(LOGO_EDGE/2)),10))   #blitting the logo
        #Displaying text
        font=pygame.font.Font('freesansbold.ttf',28)
        welcome=font.render("Welcome to Enigma Escape",True, WHITE)
        level1=font.render("Level1",True,WHITE)
        level2=font.render("Level2",True,WHITE)
        level3=font.render("Level3",True,WHITE)
        screen.blit(welcome,(((WIDTH//2)-175),330))
        pygame.display.set_icon(LOGO)
        pygame.display.set_caption("Enigma Escape")

        #Creating buttons for level
        #choosetext
        chooseLev=font.render("2. Choose your Level",True,WHITE)
        screen.blit(chooseLev,(WIDTH/2-150,400))
        #level1
        buttonEasy=pygame.Rect(WIDTH/2-55,440,110,50)
        pygame.draw.rect(screen,color=EASYBACKG,rect=buttonEasy)
        screen.blit(level1,(WIDTH/2-45,451))
        #level2
        buttonMedium=pygame.Rect(WIDTH/2-55,510,110,50)
        pygame.draw.rect(screen,color=MEDIUMBACKG,rect=buttonMedium)
        screen.blit(level2,(WIDTH/2-45,521))
        #level3
        buttonHard=pygame.Rect(WIDTH/2-55,580,110,50)
        pygame.draw.rect(screen,color=HARDBACKG,rect=buttonHard)
        screen.blit(level3,(WIDTH/2-45,591))

        #Choosing your Avatar

        #Start Button
        buttonStart=pygame.Rect(WIDTH/2-65,660,130,50)
        pygame.draw.rect(screen,color="blue",rect=buttonStart)
        start=font.render("START",True,WHITE)
        screen.blit(start,(WIDTH/2-40,671))
        pygame.display.flip()

        #Creating text box for name of player
        todisplay = font.render("1. Enter Your Name", True, WHITE)
        screen.blit(todisplay, [70, 400])
        pygame.display.update() 
        notentered = True
        playerName=''
        input_text = pygame.Rect(60, 450, 150, 40)
        while notentered:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        playerName = playerName[:-1]
                    elif event.key == pygame.K_RETURN:
                        if len(playerName)>0:
                            notentered = False
                        else:
                            continue
                    else:
                        if len(playerName)<15:
                            playerName += event.unicode
                if not notentered:
                    break

                pygame.draw.rect(screen, (0,0,200), input_text)
                text_surface = font.render(playerName, True, (255,255,255))
                screen.blit(text_surface, [input_text.x+5, input_text.y])
                input_text.w = 290
                pygame.display.flip()
                
        #print(playerName)
        info=[playerName,screen]  

    elif n==1:     #EasyLevel
        #print("entered screenChange")
        playscreen=pygame.display.set_mode((MAZEWIDTH,MAZEHEIGHT))
        playscreen.fill(EASYBACKG)
        #screenChange(5)
        pygame.display.set_icon(LOGO)
        mazeMakerInfo=mazeMaker(1)
        #mazeMaker(playScreen)
        #pygame.display.flip()
        info=[mazeMakerInfo]
    
    elif n==2:    #MedLevel
        #print("entered screenChange")
        playscreen=pygame.display.set_mode((MAZEWIDTH,MAZEHEIGHT))
        playscreen.fill(MEDIUMBACKG)
        #screenChange(5)
        pygame.display.set_icon(LOGO)
        mazeMakerInfo=mazeMaker(2)
        info=[mazeMakerInfo]
        #pygame.display.flip()
    
    elif n==3:   #Hard Level
        #print("entered screenChange")
        playscreen=pygame.display.set_mode((MAZEWIDTH,MAZEHEIGHT))
        playscreen.fill(HARDBACKG)
        #screenChange(5)
        pygame.display.set_icon(LOGO)
        mazeMakerInfo=mazeMaker(3)
        #pygame.display.flip()
        info=[mazeMakerInfo]
    
    elif n==4:   #Ending Screen
        #print("entered screenChange")
        playscreen=pygame.display.set_mode((WIDTH,HEIGHT))
        

    elif n==5:  #Waiting Screen
        waitScreen=pygame.display.set_mode((WAITWIDTH,WAITHEIGHT))
        waitScreen.blit(WAITIMG,(0,0))
        pygame.display.flip()
        info=[waitScreen]
        n=7
        ##Please add a button here saying that the player has read the instructions so that we can use it to
        #switch to viewport once we're back in game.py
    return info