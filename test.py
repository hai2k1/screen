import pygame
import random

WIDTH = 700
HEIGHT = 500
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
class iteam(pygame.sprite.Sprite):
    def __init__(self,iteamx,range_x,range_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(iteamx)
        self.rect = self.image.get_rect()
        self.rect.x = range_x
        self.rect.y = range_y
all_sprites = pygame.sprite.Group()
#backgroud:
gachx = 0
gachy = 0
while  gachx < 750:
    gach = iteam("map/nengach.png", gachx, gachy)
    gachx += 30
    all_sprites.add(gach)
    if gachx >= 740:
        gachy = gachy + 30
        gachx = 0
    elif gachy >= 540:
        break
#house:
nhax = 0
while nhax < 350:
    Iteamnha = iteam("map/house.png", nhax, 0)
    nhax += 70
    all_sprites.add(Iteamnha)

# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()