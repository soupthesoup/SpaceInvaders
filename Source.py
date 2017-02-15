import pygame
import sys
import random from randint
pygame.init()
screenSize (1000,800) 
screen = pygame.display.set_mode((screenSize), 0)
pygame.display.set_caption("Space Invaders")
White(255,255,255)
Green(0,255,0)
Black(0,0,0)

screen.fill(Black)
pygame.display.update()

Main = True
Game = False
Controls = False
loser = False
Choose = True

while Main:
	moveClock = pygame.time.Clock()
	move_tick_count = 0
	moveClock2 = pygame.time.Clock()
	move_tick_count2 = 0
	moveClock3 = pygame.time.Clock()
	move_tick_count3 = 0
	moveClock4 = pygame.time.Clock()
	move_tick_count4 = 0
	moveClock5 = pygame.time.Clock()
	move_tick_count5 = 0
	

