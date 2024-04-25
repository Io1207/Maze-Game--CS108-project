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

#Easy Maze Settings
EASYMAZE=(0,255,0)
EASYBACKG=(125,227,125)


MEDIUMMAZE=(40,195,255) #bluish something
MEDIUMBACKG=(20,82,163)

HARD=(194,36,194)

HARDBACKG=pygame.Color('darkslategray')
HARDMAZE=pygame.Color('darkorange')

LOGO_EDGE=300
LOGO=pygame.image.load("Images\\logoreduced.jpg")


FPS=10000

AV1NORMAL="hjcb"

AV2NORMAL="hjcb"

AV3NORMAL="hjcb"

PATHFILE=("Path.txt")