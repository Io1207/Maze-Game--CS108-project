from utils import *
from HopefullyWorkingMazeGen import *


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
        mazeMakerInfo=mazeMaker(playscreen,1)
        #mazeMaker(playScreen)
        #pygame.display.flip()
        info=[mazeMakerInfo]
        n=7
    
    elif n==2:    #MedLevel
        #print("entered screenChange")
        playscreen=pygame.display.set_mode((MAZEWIDTH,MAZEHEIGHT))
        playscreen.fill(MEDIUMBACKG)
        #screenChange(5)
        pygame.display.set_icon(LOGO)
        mazeMakerInfo=mazeMaker(playscreen,2)
        info=[mazeMakerInfo]
        #pygame.display.flip()
        n=7
    
    elif n==3:   #Hard Level
        #print("entered screenChange")
        playscreen=pygame.display.set_mode((MAZEWIDTH,MAZEHEIGHT))
        playscreen.fill(HARDBACKG)
        #screenChange(5)
        pygame.display.set_icon(LOGO)
        mazeMakerInfo=mazeMaker(playscreen,3)
        #pygame.display.flip()
        info=[mazeMakerInfo]
        n=7
    
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


def mazeDisplay(info,player):
    viewPort=pygame.display.set_mode((400,700))
    screen=info[0]
    array=info[1]
    for i in range(10):
        for j in range(10):
            