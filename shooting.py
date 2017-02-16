import pygame
import pygame.locals






#Need invader location for instantiating
def shoot():
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  GREEN = (0, 204, 0) #Alien colour placeholder
  bulletYspeed = -3
  #tank being the tank sprite.
  bulPosition = tank.get_rect()
  bulPosition.centerx = tank.get_rect().centerx
  bulPosition.centery = tank.get_rect().centery - 10
  
  #done = False
  #while not done:
  #  for event in pygame.event.get():
  #    if event.type == pygame.KEYDOWN:
  #      if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
  #Check Surface name!!!
  #bulPosition +Animated ship bulPosition to be above it and in the middle
  hit = False
  while not hit:
    if bulPosition.y > 0: #Change white to background colour
      pygame.draw.rect(screen, WHITE, (bulPosition, 5, 10), 0)
      bulPosition.top += dy
      pygame.display.update()
    elif bulPosition.top < 0:
      pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
      pygame.display.update()
    elif pygame.colliderect(alien):
      #pygame.sprite.collide_rect()
      #find alien bulPosition in the array somehow call it alienNum or whatnot.
      pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
      del alienArray[alienNum]
      hit = True
    #Rect(left, top, width, height)
    #pygame.draw.rect(Surface, color, Rect, width=0) Width = line thickness 0 = full block

