import pygame
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
run = True
class iteam:
    def __init__(self,imageiteam):
        self.iteams = pygame.image.load(imageiteam)
        self.nhanvat = pygame.image.load(imageiteam)
    def showiteam(iteamx,x,y):
        screen.blit(iteamx,(x,y))
up = 0
down = 0
left = 0
right = 0
changex = 200
changey = 200
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if event.type == pygame.KEYDOWN:
       if event.key == pygame.K_DOWN:
            down = down + 1
            changey = changey + 2
            up = 0
            left = 0
            right = 0
       elif event.key == pygame.K_UP:
            up = up + 1
            changey = changey - 2
            down = 0
            left = 0
            right = 0
       elif event.key == pygame.K_LEFT:
            left = left + 1
            changex = changex - 2
            down= 0
            up = 0
            right =0
       elif event.key == pygame.K_RIGHT:
            right = right + 1
            changex = changex + 2
            up = 0
            down =0
            left = 0

    #nengach:
    gachx = 0
    gachy = 0
    while gachx < 750:
        iteam.showiteam(iteam("map/nengach.png").iteams, gachx, gachy)
        gachx = gachx + 30
        if gachx >= 740:
            gachy = gachy + 30
            gachx = 0
        elif gachy >= 540:
            break

    #nvDown:

    if down == 1:
        iteam.showiteam(iteam("nhanvat/down1.png").iteams,changex,changey)
    if down == 2:
        iteam.showiteam(iteam("nhanvat/down2.png").iteams, changex, changey)
    if down == 3:
        iteam.showiteam(iteam("nhanvat/down3.png").iteams, changex, changey)
    if down == 4:
        iteam.showiteam(iteam("nhanvat/down4.png").iteams, changex, changey)
        down = 1
    #nvUP:
    if up == 1:
        iteam.showiteam(iteam("nhanvat/up1.png").iteams, changex, changey)
    if up == 2:
        iteam.showiteam(iteam("nhanvat/up2.png").iteams, changex, changey)
    if up == 3:
        iteam.showiteam(iteam("nhanvat/up3.png").iteams, changex, changey)
    if up == 4:
        iteam.showiteam(iteam("nhanvat/up4.png").iteams, changex, changey)
        up = 1
    #nvleft:
    if left == 1:
        iteam.showiteam(iteam("nhanvat/left1.png").iteams, changex, changey)
    if left == 2:
        iteam.showiteam(iteam("nhanvat/left2.png").iteams, changex, changey)
    if left == 3:
        iteam.showiteam(iteam("nhanvat/left3.png").iteams, changex, changey)
    if left == 4:
        iteam.showiteam(iteam("nhanvat/left4.png").iteams, changex, changey)
        left = 1
    #nvright:
    if right == 1:
        iteam.showiteam(iteam("nhanvat/right1.png").iteams, changex, changey)
    if right == 2:
        iteam.showiteam(iteam("nhanvat/right2.png").iteams, changex, changey)
    if right == 3:
        iteam.showiteam(iteam("nhanvat/right3.png").iteams, changex, changey)
    if right == 4:
        iteam.showiteam(iteam("nhanvat/right4.png").iteams, changex, changey)
        right = 1
    pygame.display.update()
pygame.quit()