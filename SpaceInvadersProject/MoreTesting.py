import pygame
import sys

pygame.init()

size = (1000,800)
screen = pygame.display.set_mode(size)

def terminate():
    pygame.quit()
    sys.exit()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,51,51)
GREEN = (0,255,0)
BLUE = (0,0,255)

Ax = 500
Ay = 400
Adx = 0
Ady = 0
AL1a = pygame.image.load("Alien1a.png")
AL1b = pygame.image.load("Alien1b.png")
go = True

screen.fill(BLACK)
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Ady = -5
            if event.key == pygame.K_s:
                Ady = 5
            if event.key == pygame.K_a:
                Adx = -5
            if event.key == pygame.K_d:
                Adx = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                Ady = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                Adx = 0
    
    Ax = Ax + Adx
    Ay = Ay + Ady

    screen.fill(BLACK)
    if Ax % 2 == 0:
        screen.blit(AL1a,(Ax,Ay))
    elif Ax % 2 != 0:
        screen.blit(AL1b,(Ax,Ay))
    pygame.display.update()

terminate()
