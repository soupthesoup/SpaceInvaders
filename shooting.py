import pygame
import pygame.locals
from random import randint


#Need invader location for instantiating
def shoot():  
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 204, 0) #Barrier colour placeholder
    score = 0
    arrayCount = 0      #used for a loop to make randomized numbers
    bulletYspeed = -3   #bullet speed moving up
    bulletCollection = []
    
    alienBulletArray = []
    alienBulletTimer = []   #Random numbers as a timer for aliens
    while i < 8:
        shootTime = randint(2, 8)   #randint(minValue, maxValue)
        alienBulletTimer.append(shootTime)
        #print alienBulletTimer[i]  #testing if number randomized works
        i += 1    
        
    #shipRect being the tank sprite.
    bulPosition = shipRect.get_rect()

    #find alien bulPosition in the array somehow call it alienNum or whatever.
    #Rect(left, top, width, height)
    #pygame.draw.rect(Surface, color, Rect, width=0) Width = line thickness 0 = full block

    done = False
    while not done:
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bulPosition.x = shipRect.get_rect().centerx
            bulPosition.y = shipRect.get_rect().centery - 10
            #bulPosition.y += bulletYspeed
            #pygame.draw.rect(screen, WHITE, bulPosition, 0)
            bulletCollection.append(bulPosition)
            #pygame.display.update()
        for wall1 in barrier1:
            for bullet in bulletCollection:
                if bullet.colliderect(wall1):
                    bulletCollection.remove(bullet)
                    barrier1.remove(wall1)
            for alienBullet in alienBulletArray:
                if alienBullet.colliderect(wall1):
                    alienBulletArray.remove(alienBullet)
                    barrier1.remove(wall1)
        for wall2 in barrier2:
            for bullet in bulletCollection:
                if bullet.colliderect(wall2):
                    bulletCollection.remove(bullet)
                    barrier2.remove(wall2)
            for alienBullet in alienBulletArray:
                if alienBullet.colliderect(wall2):
                    alienBulletArray.remove(alienBullet)
                    barrier2.remove(wall2)
        for wall3 in barrier3:
            for bullet in bulletCollection:
                if bullet.colliderect(wall3):
                    bulletCollection.remove(bullet)
                    barrier3.remove(wall3)
            for alienBullet in alienBulletArray:
                if alienBullet.colliderect(wall3):
                    alienBulletArray.remove(alienBullet)
                    barrier3.remove(wall3)
        for wall4 in barrier4:
            for bullet in bulletCollection:
                if bullet.colliderect(wall4):
                    bulletCollection.remove(bullet)
                    barrier4.remove(wall4)
            for alienBullet in alienBulletArray:
                if alienBullet.colliderect(wall4):
                    alienBulletArray.remove(alienBullet)
                    barrier4.remove(wall4)
        for bullet in bulletCollection:
            if bullet.top > 0: #if bullet is not at the top of the screen
                pygame.draw.rect(screen, WHITE, bullet, 0)
                bullet.top += bulletYSpeed #Adds a negative value to move the bullet to the top of the screen.
                pygame.display.update()
            elif bullet.top < 0: #checks collide with top of level
                bulletCollection.remove(bullet)#delete it if it does touch the top
                pygame.display.update()
            for alien1 in alienArray1:#checks each row of aliens to see if the bullet collides with it.
                if bullet.colliderect(alien1):#We are using 5 horizontal rows not 12 vertical columns. 
                    bulletCollection.remove(bullet)
                    alienArray1.remove(alien1)
                    pygame.display.update()
                    score += 10
            for alien2 in alienArray2:
                if bullet.colliderect(alien2):
                    bulletCollection.remove(bullet)
                    alienArray2.remove(alien2)
                    pygame.display.update()
                    score += 10
            for alien3 in alienArray3:
                if bullet.colliderect(alien3):
                    bulletCollection.remove(bullet)
                    alienArray3.remove(alien3)
                    pygame.display.update()
                    score += 20
            for alien4 in alienArray4:
                if bullet.colliderect(alien4):
                    bulletCollection.remove(bullet)
                    alienArray4.remove(alien4)
                    pygame.display.update()
                    score += 20
            for alien5 in alienArray5:
                if bullet.colliderect(alien5):
                    bulletCollection.remove(bullet)
                    alienArray5.remove(alien5)
                    pygame.display.update()
                    score += 30
            for wallR1 in barrier1: #Checks collision with each barrier block
                if bullet.colliderect(wallR1):
                    bulletCollection.remove(bullet)#if it does, delete bullet and the barriers block
                    barrier1.remove(wallR1)
                    pygame.display.update()
            for wallR2 in barrier2:
                if bullet.colliderect(wallR2):
                    bulletCollection.remove(bullet)
                    barrier2.remove(wallR2)
                    pygame.display.update()
            for wallR3 in barrier3:
                if bullet.colliderect(wallR3):
                    bulletCollection.remove(bullet)
                    barrier3.remove(wallR3)
                    pygame.display.update()
            for wallR4 in barrier4:
                if bullet.colliderect(wallR4):
                    bulletCollection.remove(bullet)
                    barrier4.remove(wallR4)
                    pygame.display.update()
        #alien shooting from here on out.
        
        for alien1 in alienArray1:#checks each row of aliens to see if the bullet collides with it.
            alienBullPos.x = alien1.get_rect().centerx
            alienBullPos.y = alien1.get_rect().centery
#FINISH          
            pygame.display.update()
                
        for alien2 in alienArray2:
            
            pygame.display.update()
                
        for alien3 in alienArray3:
            
            pygame.display.update()
                
        for alien4 in alienArray4:
            
            pygame.display.update()
                
        for alien5 in alienArray5:
            
            pygame.display.update()
                
                
shoot()

