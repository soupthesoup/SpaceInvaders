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
    for alien1 in alienArray1:
      if bulPosition.collide_rect(alien1):
        alienArray1.remove(alien1)
        pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
        hit = True
    for alien2 in alienArray2:
      if bulPosition.collide_rect(alien1):
        alienArray2.remove(alien2)
        pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
        hit = True
    for alien3 in alienArray3:
      if bulPosition.collide_rect(alein3):
        alienArray3.remove(alien3)
        pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
        hit = True
    for alien4 in alienArray4:
      if bulPositon.collide_rect(alien4):
        alienArray4.remove(alien4)
        pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
        hit = True
    for alien5 in alienArray5:
      if bulPositon.collide_rect(alien5):
        alienArray5.remove(alien5)
        pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
        hit = True
    for alien6 in alienArray6:
      if bulPositon.collide_rect(alien6):
        alienArray6.remove(alien6)
        pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
        hit = True
    for alien7 in alienArray7:
      if bulPositon.collide_rect(alien7):
        alienArray7.remove(alien7)
        pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
        hit = True
    for alien8 in alienArray8:
      if bulPositon.collide_rect(alien8):
        alienArray8.remove(alien8)
        pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
        hit = True
    for alien9 in alienArray9:
      if bulPositon.collide_rect(alien9):
        alienArray9.remove(alien9)
        pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
        hit = True
            for alien4 in alienArray4:
      if bulPositon.collide_rect(alien4):
        alienArray4.remove(alien4)
        pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
        hit = True
            for alien4 in alienArray4:
      if bulPositon.collide_rect(alien4):
        alienArray4.remove(alien4)
        pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
        hit = True
            for alien4 in alienArray4:
      if bulPositon.collide_rect(alien4):
        alienArray4.remove(alien4)
        pygame.draw.rect(screen, BLACK, (bulPosition, 5, 10), 0)
        hit = True
        
      #pygame.sprite.collide_rect()
      #find alien bulPosition in the array somehow call it alienNum or whatnot.
      #12 rows of aliens
    #Rect(left, top, width, height)
    #pygame.draw.rect(Surface, color, Rect, width=0) Width = line thickness 0 = full block

