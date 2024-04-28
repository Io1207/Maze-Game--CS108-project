import pygame
pygame.init()

#Game's Parameters
WIDTH=1200
HEIGHT=760
WHITE=(255,255,255)
BLACK=(0,0,0)

#MUAHAHA=pygame.image.load("Images\\start")
WAITWIDTH=1350
WAITHEIGHT=759

MAZEWIDTH=700
MAZEHEIGHT=700

###Background Paths

WAITIMGPATH="Images\\BackGrounds\\WaitScreenBetter.jpg"
WAITIMG=pygame.image.load(WAITIMGPATH)

BG1PATH="Images\\BackGrounds\\OIP.jpg"
BG1=pygame.image.load(BG1PATH)

BG2PATH="Images\\BackGrounds\\Gryffindor (1).jpg"
BG2=pygame.image.load(BG2PATH)

BG3PATH="Images\\BackGrounds\\Raven.jpg"
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

##Collectibles
KNUTPATH="Images\Collectibles\knut.png"
KNUTS=pygame.image.load(KNUTPATH)
SICKLEPATH="Images\Collectibles\sickle.png"
SICKLES=pygame.image.load(SICKLEPATH)
GALLPATH="Images\Collectibles\galleon.png"
GALLEONS=pygame.image.load(GALLPATH)
BOOTPATH="Images\\Collectibles\\bootPortkey.png"
BOOT=pygame.image.load(BOOTPATH)
HATPATH="Images\Collectibles\hat.png"
HAT=pygame.image.load(HATPATH)
WPATH="Images\Collectibles\wandwbg.png"
WAND=pygame.image.load(WPATH)
TRPATH="Images\\Collectibles\\trophyPort.png"
TROPHY=pygame.image.load(TRPATH)
TPATH="Images\\Collectibles\\timeTurn-removebg.png"
TURNER=pygame.image.load(TPATH)




#######
#Avatars
HARRYPATH="Images\Characters\Harry.png"
HARRY=pygame.image.load(HARRYPATH)

HERMPATH="Images\Characters\hermione.png"
HERM=pygame.image.load(HERMPATH)

RONPATH="Images\\Characters\\ron-removebg.png"
RON=pygame.image.load(RONPATH)

DUMBPATH="Images\Characters\Dumbledore.png"
DUMB=pygame.image.load(DUMBPATH)

DRACOPATH="Images\Characters\Draco.png"
DRACO=pygame.image.load(DRACOPATH)

DOBBYPATH="Images\Characters\Dobby.png"
DOBBY=pygame.image.load(DOBBYPATH)

HAGRIDPATH="Images\Characters\Hagrid.png"
HAGRID=pygame.image.load(HAGRIDPATH)

LUNAPATH="Images\Characters\Luna.png"
LUNA=pygame.image.load(LUNAPATH)

MCGPATH="Images\Characters\McG.png"
MCG=pygame.image.load(MCGPATH)

SIRIUSPATH="Images\Characters\Sirius.png"
SIRIUS=pygame.image.load(SIRIUSPATH)

SNAPEPATH="Images\Characters\Snape.png"
SNAPE=pygame.image.load(SNAPEPATH)

#######

##Avatars for buttons
SHARRYPATH="Images\AvatarSelSize\Harry.png"
AHARRY=pygame.image.load(SHARRYPATH)

SHERMPATH="Images\AvatarSelSize\hermione.png"
AHERM=pygame.image.load(SHERMPATH)

SRONPATH="Images\\AvatarSelSize\\ron-removebg.png"
ARON=pygame.image.load(SRONPATH)

SDUMBPATH="Images\AvatarSelSize\Dumbledore.png"
ADUMB=pygame.image.load(SDUMBPATH)

SDRACOPATH="Images\AvatarSelSize\Draco.png"
ADRACO=pygame.image.load(SDRACOPATH)

SDOBBYPATH="Images\AvatarSelSize\Dobby.png"
ADOBBY=pygame.image.load(SDOBBYPATH)

SHAGRIDPATH="Images\AvatarSelSize\Hagrid.png"
AHAGRID=pygame.image.load(SHAGRIDPATH)

SLUNAPATH="Images\AvatarSelSize\Luna.png"
ALUNA=pygame.image.load(SLUNAPATH)

SMCGPATH="Images\AvatarSelSize\McG.png"
AMCG=pygame.image.load(SMCGPATH)

SSIRIUSPATH="Images\AvatarSelSize\Sirius.png"
ASIRIUS=pygame.image.load(SSIRIUSPATH)

SSNAPEPATH="Images\AvatarSelSize\Snape.png"
ASNAPE=pygame.image.load(SSNAPEPATH)


PATHFILE=("Path.txt")