import pygame
import pygame.locals






#Need invader location for instantiating
WHITE = (255, 255, 255)
done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
        #Check Surface name!!!
        pygame.draw.rect(screen, WHITE, (position, 5, 10), 0)
          #Rect(left, top, width, height)
          #pygame.draw.rect(Surface, color, Rect, width=0) Width = line thickness 0 = full block
      
