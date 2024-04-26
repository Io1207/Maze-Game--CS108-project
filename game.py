from screenChange import *
#from mazeGenImp import *
from utils import *
from gameLoopDisplay import *

def gameRunner():
    n=0
    entered=False
    
    infoStart=screenChange(n)
    startSceen=infoStart[1]
    playerName=infoStart[0]
    running=True
    start=False 
    avatarChosen=False
    amIOnStartScreen=True
    amIOnEndScreen=False
    amIOnPlayScreen=False

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit()

            #if presentWindow==startScreen:
            #if button goes on start game, flip screen display make a different file containing functions
            if amIOnStartScreen:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    if WIDTH/2-55<mousePos[0]<WIDTH/2+55 and 440<mousePos[1]<490:
                    #print("Hello") this was just for debugging
                        n=1
                    elif WIDTH/2-55<mousePos[0]<WIDTH/2+55 and 510<mousePos[1]<560:
                        n=2
                    elif WIDTH/2-55<mousePos[0]<WIDTH/2+55 and 580<mousePos[1]<630:
                        n=3
                
                    ##Taking name
                    if len(playerName)>0:
                        entered=True
                        #print(playerName)
                        player=Player(0,0,playerName)
                    ##Start Button
                    if WIDTH/2-65<mousePos[0]<WIDTH/2+65 and 660<mousePos[1]<710:
                        start=True

                    if (n==1 or n==2 or n==3) and entered and start:
                        amIonStartScreen=False
                        info=screenChange(n) # info=[[mazeScreen,arrayWithCellInfo,rows]]
                        n=7
                        amIOnPlayScreen=True
                        print("came back to game.py")
                
            if amIOnPlayScreen:
                assert (n==7)
                playLoop(player,info[0])
                
                # if n==5:
                #     mazeDisplay(screen)
            
gameRunner()