from utils import *
#from HopefullyWorkingMazeGen import *


def screenChange(n):
    if n==0: #Going to game Screen
        #screen=pygame.display.set_mode((WIDTH,HEIGHT))
        
        screen=pygame.display.set_mode((WIDTH,HEIGHT))
        bg=pygame.image.load("Images\\BackGrounds\\startBG (1).jpg")
        screen.blit(bg,(0,0))

        #LogoDisplay
        pygame.draw.rect(screen,BLACK,((WIDTH//2-LOGO_EDGE/2)-5,5,LOGO_EDGE+10,LOGO_EDGE+10))
        screen.blit(LOGO,(((WIDTH//2)-(LOGO_EDGE/2)),10))   #blitting the logo
        
        
        #Displaying text
        font=pygame.font.Font('freesansbold.ttf',28)
        font1=font2=pygame.font.SysFont('freesansbold.ttf',40)
        font2=pygame.font.SysFont('arial.ttf',28)
        welcome=font2.render("Welcome to Enigma Escape",True, WHITE)
        level1=font.render("Level1",True,WHITE)
        level2=font.render("Level2",True,WHITE)
        level3=font.render("Level3",True,WHITE)
        chooseLev=font.render("2. Choose your Level",True,WHITE)
        chooseAvatar=font.render("3. Choose your Avatar",True,WHITE)
        
        #Welcome Message
        screen.blit(welcome,(((WIDTH//2)-125),286))
        pygame.display.set_icon(LOGO)
        pygame.display.set_caption("Enigma Escape")

        #Creating buttons for level
        #choosetext
        screen.blit(chooseLev,(WIDTH/2-150,330))
        #level1
        buttonEasy=pygame.Rect(WIDTH/2-55,370,110,60)
        pygame.draw.rect(screen,color=EASYBACKG,rect=buttonEasy)
        screen.blit(level1,(WIDTH/2-45,386))
        #level2
        buttonMedium=pygame.Rect(WIDTH/2-55,440,110,60)
        pygame.draw.rect(screen,color=MEDIUMBACKG,rect=buttonMedium)
        screen.blit(level2,(WIDTH/2-45,456))
        #level3
        buttonHard=pygame.Rect(WIDTH/2-55,510,110,60)
        pygame.draw.rect(screen,color=HARDBACKG,rect=buttonHard)
        screen.blit(level3,(WIDTH/2-45,525))

        ##Creating buttons for avatars
        screen.blit(chooseAvatar,(850,330))
        #pygame.draw.rect(screen,WHITE,(850,500,309,50))
        #
        pygame.draw.rect(screen,WHITE,(780,370,100,100))
        screen.blit(AHARRY,(780,370,100,100))
        pygame.draw.rect(screen,WHITE,(885,370,100,100))
        screen.blit(AHERM,(885,370,100,100))
        pygame.draw.rect(screen,WHITE,(990,370,100,100))
        screen.blit(ARON,(990,370,100,100))
        pygame.draw.rect(screen,WHITE,(1095,370,100,100))
        screen.blit(ADUMB,(1095,370,100,100))
        #
        pygame.draw.rect(screen,WHITE,(780,475,100,100))
        screen.blit(AMCG,(780,475,100,100))
        pygame.draw.rect(screen,WHITE,(885,475,100,100))
        screen.blit(ADRACO,(885,475,100,100))
        pygame.draw.rect(screen,WHITE,(990,475,100,100))
        screen.blit(ADOBBY,(990,475,100,100))
        pygame.draw.rect(screen,WHITE,(1095,475,100,100))
        screen.blit(ALUNA,(1095,475,100,100))
        #
        pygame.draw.rect(screen,WHITE,(833,580,100,100))
        screen.blit(ASIRIUS,(833,580,100,100))
        pygame.draw.rect(screen,WHITE,(938,580,100,100))
        screen.blit(AHAGRID,(938,580,100,100))
        pygame.draw.rect(screen,WHITE,(1043,580,100,100))
        screen.blit(ASNAPE,(1043,580,100,100))
        #
        

        #Start Button
        buttonStart=pygame.Rect(WIDTH/2-65,660,130,50)
        pygame.draw.rect(screen,color="blue",rect=buttonStart)
        start=font.render("START",True,WHITE)
        screen.blit(start,(WIDTH/2-40,671))
        pygame.display.flip()

        #Creating text box for name of player
        todisplay = font.render("1. Enter Your Name", True, WHITE)
        screen.blit(todisplay, (70, 330))
        pygame.display.update() 
        notentered = True
        playerName=''
        input_text = pygame.Rect(60, 370, 150, 40)
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

    

    elif n==5:  #Waiting Screen
        waitScreen=pygame.display.set_mode((WAITWIDTH,WAITHEIGHT))
        waitScreen.blit(WAITIMG,(0,0))
        pygame.display.set_icon(LOGO)
        pygame.display.set_caption("Enigma Escape")
        pygame.display.flip()

        #Start Button
        font=pygame.font.Font('freesansbold.ttf',28)
        buttonStart=pygame.Rect(WAITWIDTH/2-65,660,130,50)
        pygame.draw.rect(waitScreen,color="blue",rect=buttonStart)
        start=font.render("START",True,WHITE)
        waitScreen.blit(start,(WIDTH/2-40,671))
        pygame.display.flip()
        count=0
        running=True
        while running:
            for event in pygame.event.get():    
                if event.type==pygame.QUIT:
                    exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    #print(mousePos)
                    if WIDTH/2-65<mousePos[0]<WIDTH/2+65 and 660<mousePos[1]<710:
                            #print("entered the break block")
                            running=False
                            break
                    else:
                        continue
                count+=1
        del count,running
        info=[]
        #info=[waitScreen]
        ##Please add a button here saying that the player has read the instructions so that we can use it to
        #switch to viewport once we're back in game.py
    return info