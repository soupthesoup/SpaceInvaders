import pygame
import pygame.locals






#Need invader location for instantiating
def shoot():
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  GREEN = (0, 204, 0) #Alien colour placeholder
  dy = 1
  #tank being the tank sprite.
  position = tank.get_rect()
  position.centerx = tank.get_rect().centerx
  position.centery = tank.get_rect().centery - 10
  #done = False
  #while not done:
  #  for event in pygame.event.get():
  #    if event.type == pygame.KEYDOWN:
  #      if event.key == pygame.K_UP or event.key == pygame.K_SPACE:

  #Check Surface name!!!
  #Position +Animated ship position to be above it and in the middle
  if position.y <= 800 and screen.get_at(position.x, position.y + 1) == (BLACK): #Change white to background colour
    pygame.draw.rect(screen, WHITE, (position, 5, 10), 0)
    position.y += dy
    pygame.display.update()
  elif screen.get_at(position.x, position.y + 1) != (BLACK):
    pygame.draw.rect(screen, BLACK, (position, 5, 10), 0)
    pygame.display.update()
  elif screen.get_at(position.x, position.y + 1) == (GREEN):
    #find alien position in the array somehow call it alienNum or whatnot.
    del alienArray[alienNum]
  #Rect(left, top, width, height)
  #pygame.draw.rect(Surface, color, Rect, width=0) Width = line thickness 0 = full block
      
