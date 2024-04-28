from utils import *
#from HopefullyWorkingMazeGen import *

def ScoreCalculation(n,playerEnd):
    maxTime=0
    timeB=0
    if n==1:
        maxTime=210
        timeB=10*playerEnd[1]//10
    if n==2:
        maxTime=300
        timeB=15*playerEnd[1]//10
    if n==3:
        maxTime=360
        timeB=20*playerEnd[1]//10
    
    wandB=100*playerEnd[0][3]
    knutB=10*playerEnd[0][4]
    galleonB=30*playerEnd[0][5]
    sickleB=20*playerEnd[0][6]
    score=timeB+wandB+knutB+galleonB+sickleB
    return score

def topFive(arr):
    descendSort=sorted(arr, key=lambda x: x[1], reverse=True)
    topFive=descendSort[0:5]
    return topFive

def screenChange(difficult,n,playerEnd,navigation,rows):
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

    elif n==4:  #End Screen
        endScreen=pygame.display.set_mode((WAITWIDTH,WAITHEIGHT))
        endScreen.blit(WAITIMG,(0,0))
        endScreen.blit(pygame.image.load("Images\scroll.png"),(WAITWIDTH/2-257,20))
        pygame.display.set_icon(LOGO)
        pygame.display.set_caption("Enigma Escape")
        font=pygame.font.SysFont('freesansbold.ttf',30)
        font1=pygame.font.SysFont('arial',40)
        font2=pygame.font.SysFont('arial',30)
        font3=pygame.font.SysFont('arial',20)
        victory=False
        #Start Button
        Message2=""
        Message1="Well, atleast you didn't get expelled!"
        Message=font.render(Message1,True,BLACK)
        herm="-Hermione, maybe"
        if playerEnd[1]>=0 and [playerEnd[0][1],playerEnd[0][2]]==[0,0]:
            victory=True
            print("Victory")
        if victory:
            Message2="Mischief Managed!"
            Message=font.render(Message2,True,BLACK)
            endScreen.blit(Message,(WAITWIDTH//2-100,120))
        else:
            endScreen.blit(Message,(WAITWIDTH//2-200,120))
            endScreen.blit(font.render(herm,True,BLACK),(WAITWIDTH//2+10,155))
        score="You Couldn't Find the End"

        if victory:
            score=ScoreCalculation(difficult,playerEnd)
            endScreen.blit(font1.render(str("Your Score: "+str(score)),True,BLACK),(WAITWIDTH//2-130,170))
        else:
            endScreen.blit(font2.render(str(score),True,BLACK),(WAITWIDTH//2-190,200))
            score=0

        f=open('scores.txt','a')
        f.write(f"{playerEnd[0][0]} {score}")
        f.write('\n')
        f.close()
        arr=[]

        #TopScore
        f=open('scores.txt','r')
        f.readline()
        for x in f.readlines():
            a=x.split()
            arr.append((a[0],int(a[1])))
        f.close()

        bestFive=topFive(arr)
        Message="TOP 5 SCORES"
        scoreDisplayHead=font2.render(Message,True,BLACK)

        Name1=bestFive[0][0]
        Score1=bestFive[0][1]
        Name1=font3.render(Name1,True,BLACK)
        Score1=font3.render(str(Score1),True,BLACK)

        Name2=bestFive[1][0]
        Score2=bestFive[1][1]
        Name2=font3.render(Name2,True,BLACK)
        Score2=font3.render(str(Score2),True,BLACK)

        Name3=bestFive[2][0]
        Score3=bestFive[2][1]
        Name3=font3.render(Name3,True,BLACK)
        Score3=font3.render(str(Score3),True,BLACK)

        Name4=bestFive[3][0]
        Score4=bestFive[3][1]
        Name4=font3.render(Name4,True,BLACK)
        Score4=font3.render(str(Score4),True,BLACK)

        Name5=bestFive[4][0]
        Score5=bestFive[4][1]
        Name5=font3.render(Name5,True,BLACK)
        Score5=font3.render(str(Score5),True,BLACK)

        #Blitting Top Scores
        endScreen.blit(scoreDisplayHead,(WAITWIDTH//2-70,260))
        endScreen.blit(font2.render("Name",True,BLACK),(WAITWIDTH//2-125,310))
        endScreen.blit(font2.render("Score",True,BLACK),(WAITWIDTH//2+70,310))
        
        #Blitting Names
        endScreen.blit(Name1,(WAITWIDTH//2-150,350))
        endScreen.blit(Name2,(WAITWIDTH//2-150,380))
        endScreen.blit(Name3,(WAITWIDTH//2-150,410))
        endScreen.blit(Name4,(WAITWIDTH//2-150,440))
        endScreen.blit(Name5,(WAITWIDTH//2-150,470))

        #Blitting Scores
        endScreen.blit(Score1,(WAITWIDTH//2+70,350))
        endScreen.blit(Score2,(WAITWIDTH//2+70,380))
        endScreen.blit(Score3,(WAITWIDTH//2+70,410))
        endScreen.blit(Score4,(WAITWIDTH//2+70,440))
        endScreen.blit(Score5,(WAITWIDTH//2+70,470))

        pygame.display.flip()    
        running=True
        while running:
            for event in pygame.event.get():    
                if event.type==pygame.QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    keyPressed=pygame.key.get_pressed()
                    if keyPressed[pygame.K_m]:
                        screen=0
                    elif keyPressed[pygame.K_q]:
                        exit()
                    elif keyPressed[pygame.K_r]:
                        screen=2
                    #print(mousePos)
                    
        info=[screen]
        #info=[waitScreen]
        ##Please add a button here saying that the player has read the instructions so that we can use it to
        #switch to viewport once we're back in game.py

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