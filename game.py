from screenChange import *
#from mazeGenImp import *
from utils import *
from gameLoopDisplay import *
from Wilson import *

def gameRunner():
    n=0
    entered=False
    
    infoStart=screenChange(n)
    playerName=infoStart[0]
    running=True
    start=False 
    avatarChosen=False
    amIOnStartScreen=True
    amIOnEndScreen=False
    amIOnPlayScreen=False
    counter=0
    mazegrid=0
    player=0
    a=0
    screen=0

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()

            #if presentWindow==startScreen:
            #if button goes on start game, flip screen display make a different file containing functions
            if amIOnStartScreen:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    if WIDTH/2-55<mousePos[0]<WIDTH/2+55 and 370<mousePos[1]<430:
                    #print("Hello") this was just for debugging
                        n=1
                    elif WIDTH/2-55<mousePos[0]<WIDTH/2+55 and 440<mousePos[1]<500:
                        n=2
                    elif WIDTH/2-55<mousePos[0]<WIDTH/2+55 and 510<mousePos[1]<570:
                        n=3
                    print(n)
                
                    ##Taking name
                    if len(playerName)>0:
                        entered=True
                        #print(playerName)
                        player=Player(0,0,playerName)
                    ##Start Button
                    # if WIDTH/2-65<mousePos[0]<WIDTH/2+65 and 660<mousePos[1]<710:
                    #     start=True

                    #Choosing Avatar


                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    if 780<mousePos[0]<880:
                        if 370<mousePos[1]<470:
                            a=1
                        elif 475<mousePos[1]<575:
                            a=5
                    if 885<mousePos[0]<985:
                        if 370<mousePos[1]<470:
                            a=2
                        elif 475<mousePos[1]<575:
                            a=6
                    if 990<mousePos[0]<1090:
                        if 370<mousePos[1]<470:
                            a=3
                        elif 475<mousePos[1]<575:
                            a=7
                    if 1095<mousePos[0]<1195:
                        if 370<mousePos[1]<470:
                            a=4
                        elif 475<mousePos[1]<575:
                            a=8
                    if 833<mousePos[0]<933 and 580<mousePos[1]<680:
                        a=9
                    elif 938<mousePos[0]<1038 and 580<mousePos[1]<680:
                        a=10
                    if 1043<mousePos[0]<1143 and 580<mousePos[1]<680:
                        a=11

                    # print(a)

                    
                    if n==1:
                        cols,rows=40,40
                    if n==2:
                        cols, rows=60,60
                    if n==3:
                        cols,rows=90,90

                    if entered and (n==1 or n==2 or n==3) and a!=0:
                        amIOnStartScreen=False
                        screenChange(5)
                        amIOnPlayScreen=True
                        # print("Coming out of wait screen")

                    if amIOnPlayScreen and counter==0:
                        myMaze=WilsonMazeGenerator(cols,rows)
                        myMaze.generate_maze()
                        myMaze.solve_maze()
                        #print(myMaze)
                        #print(myMaze.solution)
                        myMaze.Directions()
                        myMaze.collectiblesGen(n)
                        counter +=1
                        screen=2
                        mazegrid=myMaze.displayAptGrid()
                        print(myMaze.collectibles)
                        # if n==5:
                        #     mazeDisplay(screen)
                
                    # if (n==1 or n==2 or n==3) and entered and start:
                    #     amIonStartScreen=False
                    #     info=screenChange(n) # info=[[mazeScreen,arrayWithCellInfo,rows]]
                    #     n=7
                    #     amIOnPlayScreen=True
                    #     print("came back to game.py")

                    
            
            if amIOnPlayScreen and screen==2:
                playLoop(player,mazegrid,myMaze.collectibles,a,n)

            
            
gameRunner()