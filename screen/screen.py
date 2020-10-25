import pygame
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
run = True
class iteam:
    def __init__(self):
        self.nen = pygame.image.load("map/nengach.png")
    def showiteam(iteamx,x,y):
        screen.blit(iteamx,(x,y))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #nengach:
    gachx = 0
    gachy = 0
    while gachx < 750:
        iteam.showiteam(iteam().nen, gachx, gachy)
        gachx = gachx + 30
        if gachx >= 740:
            gachy = gachy + 30
            gachx = 0
        elif gachy >= 540:
            break

    pygame.display.update()
pygame.quit()