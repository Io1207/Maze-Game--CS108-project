import pygame
pygame.init()

#screen=pygame.display.set_mode((500,500))
object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))
 
print(object2.colliderect(object1))