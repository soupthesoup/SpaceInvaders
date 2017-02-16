import pygame
import sys

pygame.init()

size = (1000,800)
screen = pygame.display.set_mode(size)

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,51,51)
GREEN = (0,255,0)
BLUE = (0,0,255)

x1 = 150
x2 = 350
x3 = 550
x4 = 750
y = 650
barrier1 = []
barrier2 = []
barrier3 = []
barrier4 = []

screen.fill(BLACK)
pygame.display.update()

game = True

barrier = [
        "WWWWWWWWWWWWWWWWWWWW",
        "WWWWWWWWWWWWWWWWWWWW",
        "WWWWWWWWWWWWWWWWWWWW",
        "WWWWW          WWWWW",
        ]

for row in barrier:
    for col in row:
        if col == "W":
            wallR1 = pygame.Rect(x1,y,5,10)
            barrier1.append(wallR1)
            wallR2 = pygame.Rect(x2,y,5,10)
            barrier2.append(wallR2)
            wallR3 = pygame.Rect(x3,y,5,10)
            barrier3.append(wallR3)
            wallR4 = pygame.Rect(x4,y,5,10)
            barrier4.append(wallR4)
        x1 += 5
        x2 += 5
        x3 += 5
        x4 += 5
    y += 10
    x1 = 150
    x2 = 350
    x3 = 550
    x4 = 750

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    screen.fill(BLACK)

    for WALL1 in barrier1:
        pygame.draw.rect(screen,GREEN,WALL1,0)

    for WALL2 in barrier2:
        pygame.draw.rect(screen,GREEN,WALL2,0)

    for WALL3 in barrier3:
        pygame.draw.rect(screen,GREEN,WALL3,0)

    for WALL4 in barrier4:
        pygame.draw.rect(screen,GREEN,WALL4,0)

    pygame.display.update()
    

pygame.quit()
sys.exit()
        
 ##This is all the working barriers.
