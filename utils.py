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

WAITIMGPATH="Images\\BAckGrounds\\WaitScreenBetter.jpg"
WAITIMG=pygame.image.load(WAITIMGPATH)

BG1PATH="Images\\BAckGrounds\\OIP.jpg"
BG1=pygame.image.load(BG1PATH)

BG2PATH="Images\\BAckGrounds\\Gryffindor (1).jpg"
BG2=pygame.image.load(BG2PATH)

BG3PATH="Images\\BAckGrounds\\Raven.jpg"
BG3=pygame.image.load(BG3PATH)

BG4PATH="Images\\BackGrounds\\hufflepuff.jpg"
BG4=pygame.image.load(BG4PATH)

BG5PATH="Images\\BackGrounds\\slytherin.jpg"
BG5=pygame.image.load(BG5PATH)

WALLSPATH="Images\wallsRed.jpg"
WALLS=pygame.image.load(WALLSPATH)

EASYBACKG=(125,227,125)

MEDIUMBACKG=(20,82,163)

HARDBACKG=pygame.Color('darkslategray')

LOGO_EDGE=300
LOGO=pygame.image.load("Images\\logoreduced.jpg")


FPS=10000

#######
#Avatars
HARRYPATH="Images\Characters\Harry.png"

HERMPATH="Images\Characters\hermione.png"

RONPATH="Images\Characters\ron-removebg.png"

DUMBPATH="Images\Characters\Dumbledore.png"

DRACOPATH="Images\Characters\Draco.png"

DOBBYPATH="Images\Characters\Dobby.png"

HAGRIDPATH="Images\Characters\Hagrid.png"

LUNAPATH="Images\Characters\Luna.png"

MCGPATH="Images\Characters\McG.png"

SIRIUSPATH="Images\Characters\Sirius.png"

SNAPEPATH="Images\Characters\Snape.png"
#######

PATHFILE=("Path.txt")