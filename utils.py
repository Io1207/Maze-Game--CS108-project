import pygame
pygame.init()

#Game's Parameters
WIDTH=1200
HEIGHT=760
WHITE=(255,255,255)
BLACK=(0,0,0)

#MUAHAHA=pygame.image.load("Images\\start")
WAITWIDTH=1200
WAITHEIGHT=675

MAZEWIDTH=700
MAZEHEIGHT=700

WAITIMGPATH="Images\\WaitScreenBetter.jpg"
WAITIMG=pygame.image.load(WAITIMGPATH)

BG1PATH="Images\OIP.jpg"
BG1=pygame.image.load(BG1PATH)

BG2PATH="Images\Gryffindor (1).jpg"
BG2=pygame.image.load(BG2PATH)

BG3PATH="Images\Raven.jpg"
BG3=pygame.image.load(BG3PATH)

BG4PATH="Images\hufflepuff.jpg"
BG4=pygame.image.load(BG4PATH)

BG5PATH="Images\slytherin.jpg"
BG5=pygame.image.load(BG5PATH)

WALLSPATH="Images\wallsRed.jpg"
WALLS=pygame.image.load(WALLSPATH)

EASYBACKG=(125,227,125)

MEDIUMBACKG=(20,82,163)

HARDBACKG=pygame.Color('darkslategray')

LOGO_EDGE=300
LOGO=pygame.image.load("Images\\logoreduced.jpg")


FPS=10000

AV1NORMAL="hjcb"

AV2NORMAL="hjcb"

AV3NORMAL="hjcb"

PATHFILE=("Path.txt")