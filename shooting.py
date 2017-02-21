import pygame
import pygame.locals


#Need invader location for instantiating
def shoot():
    score = 0  
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 204, 0) #Alien colour placeholder
    bulletYspeed = -3
    bulletCollection = []
    #tank being the tank sprite.
    bulPosition = shipRect.get_rect()
    bulPosition.x = shipRect.get_rect().centerx
    bulPosition.y = shipRect.get_rect().centery - 10


    #done = False
    #while not done:
    #for event in pygame.event.get():
    #   if event.type == pygame.KEYDOWN:
    #       if event.key == pygame.K_UP or event.key == pygame.K_SPACE:
    #Check Surface name!!!
    #bulPosition +Animated ship bulPosition to be above it and in the middle
    #pygame.sprite.collide_rect()
    #find alien bulPosition in the array somehow call it alienNum or whatnot.
    #12 rows of aliens
    #Rect(left, top, width, height)
    #pygame.draw.rect(Surface, color, Rect, width=0) Width = line thickness 0 = full block



    done = False
    while not done:
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bulletCollection.append(bullet)
        for bullet in bulletCollection:          
            bulPosition.y += bulletYspeed
            pygame.draw.rect(screen, WHITE, bulPosition, 0)
            pygame.display.update()
            if bullet.top < 0: #checks clide with top of level
                bulletCollection.remove(bullet)
                pygame.display.update()
            for alien1 in alienArray1:
                if bullet.collidepoint(alien1):
                    bulletCollection.remove(bullet)
                    alienArray1.remove(alien1)
                    pygame.display.update()
                    score += 100
            for alien2 in alienArray2:
                if bullet.collidepoint(alien2):
                    bulletCollection.remove(bullet)
                    alienArray2.remove(alien2)
                    pygame.display.update()
                    score += 100
            for alien3 in alienArray3:
                if bullet.collidepoint(alien3):
                    bulletCollection.remove(bullet)
                    alienArray3.remove(alien3)
                    pygame.display.update()
                    score += 100
            for alien4 in alienArray4:
                if bullet.collidepoint(alien4):
                    bulletCollection.remove(bullet)
                    alienArray4.remove(alien4)
                    pygame.display.update()
                    score += 100
            for alien5 in alienArray5:
                if bullet.collidepoint(alien5):
                    bulletCollection.remove(bullet)
                    alienArray5.remove(alien5)
                    pygame.display.update()
                    score += 100
            for alien6 in alienArray6:
                if bullet.collidepoint(alien6):
                    bulletCollection.remove(bullet)
                    alienArray6.remove(alien6)
                    pygame.display.update()
                    score += 100
            for alien7 in alienArray7:
                if bullet.collidepoint(alien7):
                    bulletCollection.remove(bullet)
                    alienArray7.remove(alien7)
                    pygame.display.update()
                    score += 100
            for alien8 in alienArray8:
                if bullet.collidepoint(alien8):
                    bulletCollection.remove(bullet)
                    alienArray8.remove(alien8)
                    pygame.display.update()
                    score += 100
            for alien9 in alienArray9:
                if bullet.collidepoint(alien9):
                    bulletCollection.remove(bullet)
                    alienArray9.remove(alien9)
                    pygame.display.update()
                    score += 100
            for alien10 in alienArray10:
                if bullet.collidepoint(alien10):
                    bulletCollection.remove(bullet)
                    alienArray10.remove(alien10)
                    pygame.display.update()
                    score += 100
            for alien11 in alienArray11:
                if bullet.collidepoint(alien11):
                    bulletCollection.remove(bullet)
                    alienArray11.remove(alien11)
                    pygame.display.update()
                    score += 100
            for alien12 in alienArray12:
                if bullet.collidepoint(alien12):
                    bulletCollection.remove(bullet)
                    alienArray12.remove(alien12)
                    pygame.display.update()
                    score += 100
            for wallR1 in barrier1:
                if bullet.collidepoint(wallR1):
                    bulletCollection.remove(bullet)
                    barrier1.remove(wallR1)
                    pygame.display.update()
            for wallR2 in barrier2:
                if bullet.collidepoint(wallR2):
                    bulletCollection.remove(bullet)
                    barrier2.remove(wallR2)
                    pygame.display.update()
            for wallR3 in barrier3:
                if bullet.collidepoint(wallR3):
                    bulletCollection.remove(bullet)
                    barrier3.remove(wallR3)
                    pygame.display.update()
            for wallR4 in barrier4:
                if bullet.collidepoint(wallR4):
                    bulletCollection.remove(bullet)
                    barrier4.remove(wallR4)
                    pygame.display.update()
            
        
shoot()
