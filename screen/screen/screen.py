import pygame
pygame.init()
size = (700,500)
screen = pygame.display.set_mode(size)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()