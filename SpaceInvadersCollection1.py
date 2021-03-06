import pygame
import sys
import time
from random import randint

pygame.init()

size = (1000,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Invaders")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,51,51)
GREEN = (0,255,0)
BLUE = (0,0,255)

AL1Images = [pygame.image.load("Alien1a.png"), pygame.image.load("Alien1b.png")] #Array for sprite animation
AL2Images = [pygame.image.load("Alien2a.png"), pygame.image.load("Alien2b.png")]
AL3Images = [pygame.image.load("Alien3a.png"), pygame.image.load("Alien3b.png")]
ship = pygame.image.load("SpaceGun.png")

def playerExplosion():
    playerKilled = pygame.mixer.Sound("explosion.wav")
    playerSound = playerKilled.play()

def invaderKilled():
    invaderKilled = pygame.mixer.Sound("invaderkilled.wav")
    invaderSound = invaderKilled.play()

def shoot():
    shoot = pygame.mixer.Sound("shoot.wav")
    shootSound = shoot.play()    

def game():
    pygame.mixer.init()
    imgIndex = 0
    Ax = 115 #alien x position
    Ay = 150 #alien y position for row 1
    Ay2 = 200#row 2
    Ay3 = 250#row 3
    Ay4 = 300#row 4
    Ay5 = 350#row 5

    x1 = 150 #Position of barriers 1-4 x-coordinates
    x2 = 350
    x3 = 550
    x4 = 750
    y = 650 #Position of barriers 1-4 y-coordinate
    alienPosx = 150
    dsx = 0
    dax = 10 #Change in alien x
    oldx = 0
    shipx = 450 #Ship position
    shipy = 725
    shiph = 35#Ship dimentions
    shipw = 75
    
    moveSpeed = 1000 #number which states the tick count of how long aliens can move
    moveSubt = 150 #number which the moveSpeed is subtracted by to move aliens faster

    arrayCount = 0      #used for a loop to make randomized numbers
    bulletYspeed = -5   #bullet speed moving up
    alienBulletdy = 5   #alien bullet speed moving down

    barrier1 = []
    barrier2 = []
    barrier3 = []
    barrier4 = []
    alienRow1 = []
    alienRow2 = []
    alienRow3 = []
    alienRow4 = []
    alienRow5 = []
    Lives = []
    
    bulletCollection = []
    alienBulletArray = []
    alienBulletTimer = []   #Random numbers as a timer for aliens
    alienClockArray = [0,0,0,0,0,0,0,0,0,0,0,0]
    initialLives = [
    "LLL"
    ]

    shipRect = pygame.Rect(shipx,shipy,shipw,shiph)

    barrier = [
            "WWWWWWWWWWWWWWWWWWWW",
            "WWWWWWWWWWWWWWWWWWWW",
            "WWWWWWWWWWWWWWWWWWWW",
            "WWWWW          WWWWW",
            ]
    aliens = ["AAAAAAAAAAAA"]

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
        x1 = 150  #barrier positions x for the first barrier
        x2 = 350
        x3 = 550
        x4 = 750

    for row in aliens:
        for col in row:
            if col == "A":
                alien1Rect = pygame.Rect(Ax,Ay,30,30)#append a position for each alien in an array
                alienRow1.append(alien1Rect)
                alien2Rect = pygame.Rect(Ax,Ay2,30,30)
                alienRow2.append(alien2Rect)
                alien3Rect = pygame.Rect(Ax,Ay3,30,30)
                alienRow3.append(alien3Rect)
                alien4Rect = pygame.Rect(Ax,Ay4,30,30)
                alienRow4.append(alien4Rect)
                alien5Rect = pygame.Rect(Ax,Ay5,30,30)
                alienRow5.append(alien5Rect)
            Ax += 75#move the alien x pos over some so they don't overlap
        Ax = 115#reset it to the beginning for each row of aliens so the are aligned

    moveclock = pygame.time.Clock()
    move_tick_count = 0
    moveclock2 = pygame.time.Clock()#clocks used for how long an alien has to wait befor moving
    move_tick_count2 = 0
    moveclock3 = pygame.time.Clock()#each clock is for each row
    move_tick_count3 = 0
    moveclock4 = pygame.time.Clock()
    move_tick_count4 = 0
    moveclock5 = pygame.time.Clock()
    move_tick_count5 = 0
    shipBulletClock = pygame.time.Clock()
    shipBulletTickCount = 0
    
    alienBulletClock = pygame.time.Clock()
    alienBulletTickCount = 0
    alienBulletClock2 = pygame.time.Clock()
    alienBulletTickCount2 = 0
    alienBulletClock3 = pygame.time.Clock()
    alienBulletTickCount3 = 0
    alienBulletClock4 = pygame.time.Clock()
    alienBulletTickCount4 = 0
    alienBulletClock5 = pygame.time.Clock()
    alienBulletTickCount5 = 0
    alienBulletClock6 = pygame.time.Clock()
    alienBulletTickCount6 = 0
    alienBulletClock7 = pygame.time.Clock()
    alienBulletTickCount7 = 0
    alienBulletClock8 = pygame.time.Clock()
    alienBulletTickCount8 = 0
    alienBulletClock9 = pygame.time.Clock()
    alienBulletTickCount9 = 0
    alienBulletClock10 = pygame.time.Clock()
    alienBulletTickCount10 = 0
    alienBulletClock11 = pygame.time.Clock()
    alienBulletTickCount11 = 0
    alienBulletClock12 = pygame.time.Clock()
    alienBulletTickCount12 = 0
    i = 0
    while i < 12:
        shootTime = randint(8000, 12000)   #randint(minValue, maxValue)
        alienBulletTimer.append(shootTime)
        #print alienBulletTimer[i]  #testing if number randomized works
        i += 1


    lx = 10
    ly = 770
    for row in initialLives:
        for col in row:
            if col == "L":
                lifeRect = pygame.Rect(lx,ly,20,20)
                Lives.append(lifeRect)
            lx += 25
    score = 0
    right = True
    Main = True
    Game = False
    Controls = False
    
    
    while Main:
        shipBulletTickCount += shipBulletClock.tick()
        length = len(bulletCollection)#Checks how many bullets are on the screen. This limits the player from spaming the fire button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Main = False
                #choose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dsx = 5
                elif event.key == pygame.K_LEFT:
                    dsx = -5
                elif event.key == pygame.K_UP and (shipBulletTickCount >= 250) and length <= 5:
                    shipBulletTickCount = 0
                    bulletCollection.append(bulletRect)
                    shoot()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dsx = 0

        shipBulletx = shipRect.centerx#center the bullets based on the ship position.
        shipBullety = shipRect.centery + 5
        bulletRect = pygame.Rect(shipBulletx,shipBullety,5,10)#Draw the bullet based on the coordinates
        oldx = shipRect.left
        shipRect.left += dsx
        if shipRect.collidepoint(10,725) or shipRect.collidepoint(990,725):
            shipRect.left = oldx


        screen.fill(BLACK)
        pygame.time.delay(20)
                
        for life in Lives:
            pygame.draw.rect(screen, WHITE, life, 0)
            for alienBullet in alienBulletArray:
                if alienBullet.colliderect(shipRect):
                    alienBulletArray.remove(alienBullet)
                    Lives.remove(life)
        lifeLength = len(Lives)
        length1 = len(alienRow1)
        length2 = len(alienRow2)
        length3 = len(alienRow3)
        length4 = len(alienRow4)
        length5 = len(alienRow5)
##        print "Length1: " + str(length1)
##        print "Length2: " + str(length2)
##        print "Length3: " + str(length3)
##        print "Length4: " + str(length4)
##        print "Length5: " + str(length5)
        if lifeLength == 0:
            loser()
        if length1 == 0 and length2 == 0 and length3 == 0 and length4 == 0 and length5 == 0:
            imgIndex = 0
            Ax = 115 #alien x position
            Ay = 150 #alien y position for row 1
            Ay2 = 200#row 2
            Ay3 = 250#row 3
            Ay4 = 300#row 4
            Ay5 = 350#row 5
            
            alienPosx = 150

            moveSpeed = 1000 #number which states the tick count of how long aliens can move
            moveSubt = 150 #number which the moveSpeed is subtracted by to move aliens faster

            arrayCount = 0      #used for a loop to make randomized numbers
            bulletYspeed = -5   #bullet speed moving up
            alienBulletdy = 5   #alien bullet speed moving down

            alienRow1 = []
            alienRow2 = []
            alienRow3 = []
            alienRow4 = []
            alienRow5 = []
            
            alienBulletTimer = []   #Random numbers as a timer for aliens
            alienClockArray = [0,0,0,0,0,0,0,0,0,0,0,0]

            aliens = ["AAAAAAAAAAAA"]

            for row in aliens:
                for col in row:
                    if col == "A":
                        alien1Rect = pygame.Rect(Ax,Ay,30,30)#append a position for each alien in an array
                        alienRow1.append(alien1Rect)
                        alien2Rect = pygame.Rect(Ax,Ay2,30,30)
                        alienRow2.append(alien2Rect)
                        alien3Rect = pygame.Rect(Ax,Ay3,30,30)
                        alienRow3.append(alien3Rect)
                        alien4Rect = pygame.Rect(Ax,Ay4,30,30)
                        alienRow4.append(alien4Rect)
                        alien5Rect = pygame.Rect(Ax,Ay5,30,30)
                        alienRow5.append(alien5Rect)
                    Ax += 75#move the alien x pos over some so they don't overlap
                Ax = 115#reset it to the beginning for each row of aliens so the are aligned

            moveclock = pygame.time.Clock()
            move_tick_count = 0
            moveclock2 = pygame.time.Clock()#clocks used for how long an alien has to wait befor moving
            move_tick_count2 = 0
            moveclock3 = pygame.time.Clock()#each clock is for each row
            move_tick_count3 = 0
            moveclock4 = pygame.time.Clock()
            move_tick_count4 = 0
            moveclock5 = pygame.time.Clock()
            move_tick_count5 = 0
            shipBulletClock = pygame.time.Clock()
            shipBulletTickCount = 0
            
            alienBulletClock = pygame.time.Clock()
            alienBulletTickCount = 0
            alienBulletClock2 = pygame.time.Clock()
            alienBulletTickCount2 = 0
            alienBulletClock3 = pygame.time.Clock()
            alienBulletTickCount3 = 0
            alienBulletClock4 = pygame.time.Clock()
            alienBulletTickCount4 = 0
            alienBulletClock5 = pygame.time.Clock()
            alienBulletTickCount5 = 0
            alienBulletClock6 = pygame.time.Clock()
            alienBulletTickCount6 = 0
            alienBulletClock7 = pygame.time.Clock()
            alienBulletTickCount7 = 0
            alienBulletClock8 = pygame.time.Clock()
            alienBulletTickCount8 = 0
            alienBulletClock9 = pygame.time.Clock()
            alienBulletTickCount9 = 0
            alienBulletClock10 = pygame.time.Clock()
            alienBulletTickCount10 = 0
            alienBulletClock11 = pygame.time.Clock()
            alienBulletTickCount11 = 0
            alienBulletClock12 = pygame.time.Clock()
            alienBulletTickCount12 = 0

            i = 0
            while i < 12:
                shootTime = randint(7000, 12000)   #randint(minValue, maxValue)
                alienBulletTimer.append(shootTime)
                #print alienBulletTimer[i]  #testing if number randomized works
                i += 1 
        
        for wallR1 in barrier1:
            pygame.draw.rect(screen,GREEN,wallR1,0)#draw all the barriers using the rect in each barrier array
        for wallR2 in barrier2:
            pygame.draw.rect(screen,GREEN,wallR2,0)
        for wallR3 in barrier3:
            pygame.draw.rect(screen,GREEN,wallR3,0)
        for wallR4 in barrier4:
            pygame.draw.rect(screen,GREEN,wallR4,0)

        move_tick_count += moveclock.tick()
        move_tick_count2 += moveclock2.tick()
        move_tick_count3 += moveclock3.tick()
        move_tick_count4 += moveclock4.tick()
        move_tick_count5 += moveclock5.tick()

        alienBulletTickCount += alienBulletClock.tick()
        alienBulletTickCount2 += alienBulletClock2.tick()
        alienBulletTickCount3 += alienBulletClock3.tick()
        alienBulletTickCount4 += alienBulletClock4.tick()
        alienBulletTickCount5 += alienBulletClock5.tick()
        alienBulletTickCount6 += alienBulletClock6.tick()
        alienBulletTickCount7 += alienBulletClock7.tick()
        alienBulletTickCount8 += alienBulletClock8.tick()
        alienBulletTickCount9 += alienBulletClock9.tick()
        alienBulletTickCount10 += alienBulletClock10.tick()
        alienBulletTickCount11 += alienBulletClock11.tick()
        alienBulletTickCount12 += alienBulletClock12.tick()

        alienClockArray[0] = alienBulletTickCount
        alienClockArray[1] = alienBulletTickCount2
        alienClockArray[2] = alienBulletTickCount3
        alienClockArray[3] = alienBulletTickCount4
        alienClockArray[4] = alienBulletTickCount5
        alienClockArray[5] = alienBulletTickCount6
        alienClockArray[6] = alienBulletTickCount7
        alienClockArray[7] = alienBulletTickCount8
        alienClockArray[8] = alienBulletTickCount9
        alienClockArray[9] = alienBulletTickCount10
        alienClockArray[10] = alienBulletTickCount11
        alienClockArray[11] = alienBulletTickCount12

        scoreStr = "Score: " + (str(score))
        scoreFont = pygame.font.SysFont("ariel", 20, True)#Writen by Dylan
        scoreText = scoreFont.render(scoreStr, True, WHITE)
        screen.blit(scoreText, (50, 50))

        #print alienBulletTickCount
        
        for bullet in bulletCollection:#Writen by Dylan
            if bullet.top > 0: #if bullet is not at the top of the screen
                pygame.draw.rect(screen, WHITE, bullet, 0)
                bullet.top += bulletYspeed #Adds a negative value to move the bullet to the top of the screen.
            elif bullet.top < 0: #checks collide with top of level
                bulletCollection.remove(bullet)#delete it if it does touch the top
				
        for alienBullet in alienBulletArray:
            if alienBullet.bottom > 800:
                alienBulletArray.remove(alienBullet)
            elif alienBullet.bottom < 800:
                pygame.draw.rect(screen, WHITE, alienBullet, 0)
                alienBullet.bottom += alienBulletdy
				
        for wall1 in barrier1:#Writen by Dylan      Each square in barrier 1
            for bullet in bulletCollection: 
                if bullet.colliderect(wall1): #if a bullet hits that square
                    bulletCollection.remove(bullet)#remove the bullet and square from the game
                    barrier1.remove(wall1)
            for alienBullet in alienBulletArray:#Do the same thing for alien bullets
                if alienBullet.colliderect(wall1):
                    alienBulletArray.remove(alienBullet)
                    barrier1.remove(wall1)
        for wall2 in barrier2:#run the same loop as above for each barrier
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


        for alien5 in alienRow5:
            screen.blit(AL3Images[imgIndex], (alien5))
            ALIndex = alienRow5.index(alien5)
            if alienClockArray[ALIndex] >= alienBulletTimer[ALIndex]:
                #print "ClockArray: " + str(alienClockArray[ALIndex])
                #print "AlienBulletTimer: " + str(alienBulletTimer[ALIndex])
                pygame.time.delay(10)
                alienBulPosx = alienRow5[ALIndex].centerx
                alienBulPosy = alienRow5[ALIndex].centery + 25
                alienBulRect = pygame.Rect(alienBulPosx, alienBulPosy, 5, 10)
                alienBulletArray.append(alienBulRect)
                if ALIndex == 0:
                    alienBulletTickCount = 0
                elif ALIndex == 1:
                    alienBulletTickCount2 = 0
                elif ALIndex == 2:
                    alienBulletTickCount3 = 0
                elif ALIndex == 3:
                    alienBulletTickCount4 = 0
                elif ALIndex == 4:
                    alienBulletTickCount5 = 0
                elif ALIndex == 5:
                    alienBulletTickCount6 = 0
                elif ALIndex == 6:
                    alienBulletTickCount7 = 0
                elif ALIndex == 7:
                    alienBulletTickCount8 = 0
                elif ALIndex == 8:
                    alienBulletTickCount9 = 0
                elif ALIndex == 9:
                    alienBulletTickCount10 = 0
                elif ALIndex == 10:
                    alienBulletTickCount11 = 0
                elif ALIndex == 11:
                    alienBulletTickCount12 = 0
                #print alienClockArray[ALIndex]
                #print "Save me!!!"
            for bullet in bulletCollection:
                if bullet.colliderect(alien5):
                    score += 20
                    invaderKilled()
                    bulletCollection.remove(bullet)
                    alienRow5.remove(alien5)
            if move_tick_count5 >= moveSpeed:
                move_tick_count5 = 0
                if imgIndex == 0:
                    imgIndex += 1
                elif imgIndex == 1:
                    imgIndex = 0
                for alien5 in alienRow5:
                    alien5.left += dax
            if (alien5.left < 30 and right == False):
                right = True
                dax = -dax
                for alien5 in alienRow5:
                    alien5.bottom += 10
                for alien4 in alienRow4:
                    alien4.bottom += 10
                for alien3 in alienRow3:
                    alien3.bottom += 10
                for alien2 in alienRow2:
                    alien2.bottom += 10
                for alien1 in alienRow1:
                    alien1.bottom += 10
                if moveSpeed > 100:
                    moveSpeed -= moveSubt
            elif (alien5.right > 970 and right == True):
                right = False
                dax = -dax
                for alien5 in alienRow5:
                    alien5.bottom += 10
                    alien5.left += 2*dax
                for alien4 in alienRow4:
                    alien4.bottom += 10
                for alien3 in alienRow3:
                    alien3.bottom += 10
                for alien2 in alienRow2:
                    alien2.bottom += 10
                for alien1 in alienRow1:
                    alien1.bottom += 10
            if alien5.bottom >= 650:
                loser()

       
        for alien4 in alienRow4:
            screen.blit(AL3Images[imgIndex], (alien4))
            ALIndex = alienRow4.index(alien4)
            alx = alienRow4[ALIndex].x
            aly = alienRow4[ALIndex].y + 50
            if alienClockArray[ALIndex] >= alienBulletTimer[ALIndex]:
                try:
                    if alienRow5[ALIndex].collidepoint(alx, aly) == False:
                        alienBulPosx = alien4.centerx
                        alienBulPosy = alien4.centery + 15
                        alienBulRect = pygame.Rect(alienBulPosx, alienBulPosy, 5, 10)
                        alienBulletArray.append(alienBulRect)
                        if ALIndex == 0:
                            alienBulletTickCount = 0
                        elif ALIndex == 1:
                            alienBulletTickCount2 = 0
                        elif ALIndex == 2:
                            alienBulletTickCount3 = 0
                        elif ALIndex == 3:
                            alienBulletTickCount4 = 0
                        elif ALIndex == 4:
                            alienBulletTickCount5 = 0
                        elif ALIndex == 5:
                            alienBulletTickCount6 = 0
                        elif ALIndex == 6:
                            alienBulletTickCount7 = 0
                        elif ALIndex == 7:
                            alienBulletTickCount8 = 0
                        elif ALIndex == 8:
                            alienBulletTickCount9 = 0
                        elif ALIndex == 9:
                            alienBulletTickCount10 = 0
                        elif ALIndex == 10:
                            alienBulletTickCount11 = 0
                        elif ALIndex == 11:
                            alienBulletTickCount12 = 0
                    elif alienRow5[ALIndex].collidepoint(alx, aly):
                        #print "Don't Shoot row 5"
                        if ALIndex == 0:
                            alienBulletTickCount = 0
                        elif ALIndex == 1:
                            alienBulletTickCount2 = 0
                        elif ALIndex == 2:
                            alienBulletTickCount3 = 0
                        elif ALIndex == 3:
                            alienBulletTickCount4 = 0
                        elif ALIndex == 4:
                            alienBulletTickCount5 = 0
                        elif ALIndex == 5:
                            alienBulletTickCount6 = 0
                        elif ALIndex == 6:
                            alienBulletTickCount7 = 0
                        elif ALIndex == 7:
                            alienBulletTickCount8 = 0
                        elif ALIndex == 8:
                            alienBulletTickCount9 = 0
                        elif ALIndex == 9:
                            alienBulletTickCount10 = 0
                        elif ALIndex == 10:
                            alienBulletTickCount11 = 0
                        elif ALIndex == 11:
                            alienBulletTickCount12 = 0
                except IndexError:
                    #print "Excepted"
                    if ALIndex == 0:
                        alienBulletTickCount = 0
                    elif ALIndex == 1:
                        alienBulletTickCount2 = 0
                    elif ALIndex == 2:
                        alienBulletTickCount3 = 0
                    elif ALIndex == 3:
                        alienBulletTickCount4 = 0
                    elif ALIndex == 4:
                        alienBulletTickCount5 = 0
                    elif ALIndex == 5:
                        alienBulletTickCount6 = 0
                    elif ALIndex == 6:
                        alienBulletTickCount7 = 0
                    elif ALIndex == 7:
                        alienBulletTickCount8 = 0
                    elif ALIndex == 8:
                        alienBulletTickCount9 = 0
                    elif ALIndex == 9:
                        alienBulletTickCount10 = 0
                    elif ALIndex == 10:
                        alienBulletTickCount11 = 0
                    elif ALIndex == 11:
                        alienBulletTickCount12 = 0
            for bullet in bulletCollection:
                if bullet.colliderect(alien4):
                    score += 20
                    invaderKilled()
                    bulletCollection.remove(bullet)
                    alienRow4.remove(alien4)
            if move_tick_count4 >= moveSpeed:
                move_tick_count4 = 0
                if imgIndex == 0:
                    imgIndex += 1
                elif imgIndex == 1:
                    imgIndex = 0
                for alien4 in alienRow4:
                    alien4.left += dax
            if (alien4.left < 30 and right == False):
                right = True
                dax = -dax
                for alien5 in alienRow5:
                    alien5.bottom += 10
                for alien4 in alienRow4:
                    alien4.bottom += 10
                for alien3 in alienRow3:
                    alien3.bottom += 10
                for alien2 in alienRow2:
                    alien2.bottom += 10
                for alien1 in alienRow1:
                    alien1.bottom += 10
                if moveSpeed > 100:
                    moveSpeed -= moveSubt
            elif (alien4.right > 970 and right == True):
                right = False
                dax = -dax
                for alien5 in alienRow5:
                    alien5.bottom += 10
                for alien4 in alienRow4:
                    alien4.bottom += 10
                    alien4.left += 2*dax
                for alien3 in alienRow3:
                    alien3.bottom += 10
                for alien2 in alienRow2:
                    alien2.bottom += 10
                for alien1 in alienRow1:
                    alien1.bottom += 10
            if alien4.bottom >= 650:
                loser()                
                    					
				
        for alien3 in alienRow3:
            screen.blit(AL2Images[imgIndex], (alien3))
            ALIndex = alienRow3.index(alien3)
            alx = alienRow3[ALIndex].x
            aly = alienRow3[ALIndex].y + 50
            if alienClockArray[ALIndex] >= alienBulletTimer[ALIndex]:
                try:
                    if alienRow4[ALIndex].collidepoint(alx, aly) == False:
                        aly += 50
                        #print ALIndex
                        try:
                            if alienRow5[ALIndex].collidepoint(alx, aly) == False:
                                alienBulPosx = alienRow3[ALIndex].centerx
                                alienBulPosy = alienRow3[ALIndex].centery + 15
                                alienBulRect = pygame.Rect(alienBulPosx, alienBulPosy, 5, 10)
                                alienBulletArray.append(alienBulRect)
                                if ALIndex == 0:
                                    alienBulletTickCount = 0
                                elif ALIndex == 1:
                                    alienBulletTickCount2 = 0
                                elif ALIndex == 2:
                                    alienBulletTickCount3 = 0
                                elif ALIndex == 3:
                                    alienBulletTickCount4 = 0
                                elif ALIndex == 4:
                                    alienBulletTickCount5 = 0
                                elif ALIndex == 5:
                                    alienBulletTickCount6 = 0
                                elif ALIndex == 6:
                                    alienBulletTickCount7 = 0
                                elif ALIndex == 7:
                                    alienBulletTickCount8 = 0
                                elif ALIndex == 8:
                                    alienBulletTickCount9 = 0
                                elif ALIndex == 9:
                                    alienBulletTickCount10 = 0
                                elif ALIndex == 10:
                                    alienBulletTickCount11 = 0
                                elif ALIndex == 11:
                                    alienBulletTickCount12 = 0 
                            elif alienRow5[ALIndex].collidepoint(alx, aly):
                                #print "Don't Shoot row 5"
                                if ALIndex == 0:
                                    alienBulletTickCount = 0
                                elif ALIndex == 1:
                                    alienBulletTickCount2 = 0
                                elif ALIndex == 2:
                                    alienBulletTickCount3 = 0
                                elif ALIndex == 3:
                                    alienBulletTickCount4 = 0
                                elif ALIndex == 4:
                                    alienBulletTickCount5 = 0
                                elif ALIndex == 5:
                                    alienBulletTickCount6 = 0
                                elif ALIndex == 6:
                                    alienBulletTickCount7 = 0
                                elif ALIndex == 7:
                                    alienBulletTickCount8 = 0
                                elif ALIndex == 8:
                                    alienBulletTickCount9 = 0
                                elif ALIndex == 9:
                                    alienBulletTickCount10 = 0
                                elif ALIndex == 10:
                                    alienBulletTickCount11 = 0
                                elif ALIndex == 11:
                                    alienBulletTickCount12 = 0
                        except IndexError:
                            if ALIndex == 0:
                                alienBulletTickCount = 0
                            elif ALIndex == 1:
                                alienBulletTickCount2 = 0
                            elif ALIndex == 2:
                                alienBulletTickCount3 = 0
                            elif ALIndex == 3:
                                alienBulletTickCount4 = 0
                            elif ALIndex == 4:
                                alienBulletTickCount5 = 0
                            elif ALIndex == 5:
                                alienBulletTickCount6 = 0
                            elif ALIndex == 6:
                                alienBulletTickCount7 = 0
                            elif ALIndex == 7:
                                alienBulletTickCount8 = 0
                            elif ALIndex == 8:
                                alienBulletTickCount9 = 0
                            elif ALIndex == 9:
                                alienBulletTickCount10 = 0
                            elif ALIndex == 10:
                                alienBulletTickCount11 = 0
                            elif ALIndex == 11:
                                alienBulletTickCount12 = 0
                    elif alienRow4[ALIndex].collidepoint(alx, aly):
                        #print "Don't Shoot row 4"
                        if ALIndex == 0:
                            alienBulletTickCount = 0
                        elif ALIndex == 1:
                            alienBulletTickCount2 = 0
                        elif ALIndex == 2:
                            alienBulletTickCount3 = 0
                        elif ALIndex == 3:
                            alienBulletTickCount4 = 0
                        elif ALIndex == 4:
                            alienBulletTickCount5 = 0
                        elif ALIndex == 5:
                            alienBulletTickCount6 = 0
                        elif ALIndex == 6:
                            alienBulletTickCount7 = 0
                        elif ALIndex == 7:
                            alienBulletTickCount8 = 0
                        elif ALIndex == 8:
                            alienBulletTickCount9 = 0
                        elif ALIndex == 9:
                            alienBulletTickCount10 = 0
                        elif ALIndex == 10:
                            alienBulletTickCount11 = 0
                        elif ALIndex == 11:
                            alienBulletTickCount12 = 0
                except IndexError:
                    if ALIndex == 0:
                        alienBulletTickCount = 0
                    elif ALIndex == 1:
                        alienBulletTickCount2 = 0
                    elif ALIndex == 2:
                        alienBulletTickCount3 = 0
                    elif ALIndex == 3:
                        alienBulletTickCount4 = 0
                    elif ALIndex == 4:
                        alienBulletTickCount5 = 0
                    elif ALIndex == 5:
                        alienBulletTickCount6 = 0
                    elif ALIndex == 6:
                        alienBulletTickCount7 = 0
                    elif ALIndex == 7:
                        alienBulletTickCount8 = 0
                    elif ALIndex == 8:
                        alienBulletTickCount9 = 0
                    elif ALIndex == 9:
                        alienBulletTickCount10 = 0
                    elif ALIndex == 10:
                        alienBulletTickCount11 = 0
                    elif ALIndex == 11:
                        alienBulletTickCount12 = 0
                        
            for bullet in bulletCollection:
                if bullet.colliderect(alien3):
                    score += 40
                    invaderKilled()
                    bulletCollection.remove(bullet)
                    alienRow3.remove(alien3)
            if move_tick_count3 >= moveSpeed:
                move_tick_count3 = 0
                if imgIndex == 0:
                    imgIndex += 1
                elif imgIndex == 1:
                    imgIndex = 0
                for alien3 in alienRow3:
                    alien3.left += dax
            if (alien3.left < 30 and right == False):
                right = True
                dax = -dax
                for alien5 in alienRow5:
                    alien5.bottom += 10
                for alien4 in alienRow4:
                    alien4.bottom += 10
                for alien3 in alienRow3:
                    alien3.bottom += 10
                for alien2 in alienRow2:
                    alien2.bottom += 10
                for alien1 in alienRow1:
                    alien1.bottom += 10
                if moveSpeed > 100:    
                    moveSpeed -= moveSubt
            elif (alien3.right > 970 and right == True):
                right = False
                dax = -dax
                for alien5 in alienRow5:
                    alien5.bottom += 10
                for alien4 in alienRow4:
                    alien4.bottom += 10
                for alien3 in alienRow3:
                    alien3.bottom += 10
                    alien3.left += 2*dax
                for alien2 in alienRow2:
                    alien2.bottom += 10
                for alien1 in alienRow1:
                    alien1.bottom += 10
            if alien3.bottom >= 650:
                loser()
                  

        for alien2 in alienRow2:#Do the same thing for each row. This is because if a row 
            screen.blit(AL2Images[imgIndex], (alien2))
            ALIndex = alienRow2.index(alien2)
            alx = alienRow2[ALIndex].x
            aly = alienRow2[ALIndex].y + 50
            if alienClockArray[ALIndex] >= alienBulletTimer[ALIndex]:
                try:
                    if alienRow3[ALIndex].collidepoint(alx, aly) == False:
                        aly += 50
                        try:
                            if alienRow4[ALIndex].collidepoint(alx, aly) == False:
                                aly += 50
                                #print ALIndex
                                try:
                                    if alienRow5[ALIndex].collidepoint(alx, aly) == False:
                                        alienBulPosx = alienRow2[ALIndex].centerx
                                        alienBulPosy = alienRow2[ALIndex].centery + 15
                                        alienBulRect = pygame.Rect(alienBulPosx, alienBulPosy, 5, 10)
                                        alienBulletArray.append(alienBulRect)
                                        if ALIndex == 0:
                                            alienBulletTickCount = 0
                                        elif ALIndex == 1:
                                            alienBulletTickCount2 = 0
                                        elif ALIndex == 2:
                                            alienBulletTickCount3 = 0
                                        elif ALIndex == 3:
                                            alienBulletTickCount4 = 0
                                        elif ALIndex == 4:
                                            alienBulletTickCount5 = 0
                                        elif ALIndex == 5:
                                            alienBulletTickCount6 = 0
                                        elif ALIndex == 6:
                                            alienBulletTickCount7 = 0
                                        elif ALIndex == 7:
                                            alienBulletTickCount8 = 0
                                        elif ALIndex == 8:
                                            alienBulletTickCount9 = 0
                                        elif ALIndex == 9:
                                            alienBulletTickCount10 = 0
                                        elif ALIndex == 10:
                                            alienBulletTickCount11 = 0
                                        elif ALIndex == 11:
                                            alienBulletTickCount12 = 0
                                    elif alienRow5[ALIndex].collidepoint(alx, aly):
                                        #print "Don't Shoot row 5"
                                        if ALIndex == 0:
                                            alienBulletTickCount = 0
                                        elif ALIndex == 1:
                                            alienBulletTickCount2 = 0
                                        elif ALIndex == 2:
                                            alienBulletTickCount3 = 0
                                        elif ALIndex == 3:
                                            alienBulletTickCount4 = 0
                                        elif ALIndex == 4:
                                            alienBulletTickCount5 = 0
                                        elif ALIndex == 5:
                                            alienBulletTickCount6 = 0
                                        elif ALIndex == 6:
                                            alienBulletTickCount7 = 0
                                        elif ALIndex == 7:
                                            alienBulletTickCount8 = 0
                                        elif ALIndex == 8:
                                            alienBulletTickCount9 = 0
                                        elif ALIndex == 9:
                                            alienBulletTickCount10 = 0
                                        elif ALIndex == 10:
                                            alienBulletTickCount11 = 0
                                        elif ALIndex == 11:
                                            alienBulletTickCount12 = 0
                                except IndexError:
                                    if ALIndex == 0:
                                        alienBulletTickCount = 0
                                    elif ALIndex == 1:
                                        alienBulletTickCount2 = 0
                                    elif ALIndex == 2:
                                        alienBulletTickCount3 = 0
                                    elif ALIndex == 3:
                                        alienBulletTickCount4 = 0
                                    elif ALIndex == 4:
                                        alienBulletTickCount5 = 0
                                    elif ALIndex == 5:
                                        alienBulletTickCount6 = 0
                                    elif ALIndex == 6:
                                        alienBulletTickCount7 = 0
                                    elif ALIndex == 7:
                                        alienBulletTickCount8 = 0
                                    elif ALIndex == 8:
                                        alienBulletTickCount9 = 0
                                    elif ALIndex == 9:
                                        alienBulletTickCount10 = 0
                                    elif ALIndex == 10:
                                        alienBulletTickCount11 = 0
                                    elif ALIndex == 11:
                                        alienBulletTickCount12 = 0
                            elif alienRow4[ALIndex].collidepoint(alx, aly):
                                #print "Don't Shoot row 4"
                                if ALIndex == 0:
                                    alienBulletTickCount = 0
                                elif ALIndex == 1:
                                    alienBulletTickCount2 = 0
                                elif ALIndex == 2:
                                    alienBulletTickCount3 = 0
                                elif ALIndex == 3:
                                    alienBulletTickCount4 = 0
                                elif ALIndex == 4:
                                    alienBulletTickCount5 = 0
                                elif ALIndex == 5:
                                    alienBulletTickCount6 = 0
                                elif ALIndex == 6:
                                    alienBulletTickCount7 = 0
                                elif ALIndex == 7:
                                    alienBulletTickCount8 = 0
                                elif ALIndex == 8:
                                    alienBulletTickCount9 = 0
                                elif ALIndex == 9:
                                    alienBulletTickCount10 = 0
                                elif ALIndex == 10:
                                    alienBulletTickCount11 = 0
                                elif ALIndex == 11:
                                    alienBulletTickCount12 = 0
                        except IndexError:
                            if ALIndex == 0:
                                alienBulletTickCount = 0
                            elif ALIndex == 1:
                                alienBulletTickCount2 = 0
                            elif ALIndex == 2:
                                alienBulletTickCount3 = 0
                            elif ALIndex == 3:
                                alienBulletTickCount4 = 0
                            elif ALIndex == 4:
                                alienBulletTickCount5 = 0
                            elif ALIndex == 5:
                                alienBulletTickCount6 = 0
                            elif ALIndex == 6:
                                alienBulletTickCount7 = 0
                            elif ALIndex == 7:
                                alienBulletTickCount8 = 0
                            elif ALIndex == 8:
                                alienBulletTickCount9 = 0
                            elif ALIndex == 9:
                                alienBulletTickCount10 = 0
                            elif ALIndex == 10:
                                alienBulletTickCount11 = 0
                            elif ALIndex == 11:
                                alienBulletTickCount12 = 0
                    elif alienRow3[ALIndex].collidepoint(alx, aly):
                        #print "Don't Shoot row 3, code 2"
                        if ALIndex == 0:
                            alienBulletTickCount = 0
                        elif ALIndex == 1:
                            alienBulletTickCount2 = 0
                        elif ALIndex == 2:
                            alienBulletTickCount3 = 0
                        elif ALIndex == 3:
                            alienBulletTickCount4 = 0
                        elif ALIndex == 4:
                            alienBulletTickCount5 = 0
                        elif ALIndex == 5:
                            alienBulletTickCount6 = 0
                        elif ALIndex == 6:
                            alienBulletTickCount7 = 0
                        elif ALIndex == 7:
                            alienBulletTickCount8 = 0
                        elif ALIndex == 8:
                            alienBulletTickCount9 = 0
                        elif ALIndex == 9:
                            alienBulletTickCount10 = 0
                        elif ALIndex == 10:
                            alienBulletTickCount11 = 0
                        elif ALIndex == 11:
                            alienBulletTickCount12 = 0
                except IndexError:
                    if ALIndex == 0:
                        alienBulletTickCount = 0
                    elif ALIndex == 1:
                        alienBulletTickCount2 = 0
                    elif ALIndex == 2:
                        alienBulletTickCount3 = 0
                    elif ALIndex == 3:
                        alienBulletTickCount4 = 0
                    elif ALIndex == 4:
                        alienBulletTickCount5 = 0
                    elif ALIndex == 5:
                        alienBulletTickCount6 = 0
                    elif ALIndex == 6:
                        alienBulletTickCount7 = 0
                    elif ALIndex == 7:
                        alienBulletTickCount8 = 0
                    elif ALIndex == 8:
                        alienBulletTickCount9 = 0
                    elif ALIndex == 9:
                        alienBulletTickCount10 = 0
                    elif ALIndex == 10:
                        alienBulletTickCount11 = 0
                    elif ALIndex == 11:
                        alienBulletTickCount12 = 0
            for bullet in bulletCollection:
                if bullet.colliderect(alien2):
                    score += 40
                    invaderKilled()
                    bulletCollection.remove(bullet)
                    alienRow2.remove(alien2)	
            if move_tick_count2 >= moveSpeed:
                move_tick_count2 = 0
                if imgIndex == 0:
                    imgIndex += 1
                elif imgIndex == 1:
                    imgIndex = 0
                for alien2 in alienRow2:
                    alien2.left += dax
            if (alien2.left < 30 and right == False):
                right = True
                dax = -dax
                for alien5 in alienRow5:
                    alien5.bottom += 10
                for alien4 in alienRow4:
                    alien4.bottom += 10
                for alien3 in alienRow3:
                    alien3.bottom += 10
                for alien2 in alienRow2:
                    alien2.bottom += 10
                for alien1 in alienRow1:
                    alien1.bottom += 10
                if moveSpeed > 100:
                    moveSpeed -= moveSubt
            elif (alien2.right > 970 and right == True):
                right = False
                dax = -dax
                for alien5 in alienRow5:
                    alien5.bottom += 10
                for alien4 in alienRow4:
                    alien4.bottom += 10
                for alien3 in alienRow3:
                    alien3.bottom += 10
                for alien2 in alienRow2:
                    alien2.bottom += 10
                    alien2.left += 2*dax
                for alien1 in alienRow1:
                    alien1.bottom += 10
                    alien1.left += 2*dax
            if alien2.bottom >= 650:
                loser()
       

        for alien1 in alienRow1:
            screen.blit(AL1Images[imgIndex], (alien1))#blit the alien based on an array containing images
            ALIndex = alienRow1.index(alien1)
            alx = alienRow1[ALIndex].x
            aly = alienRow1[ALIndex].y + 50
            if alienClockArray[ALIndex] >= alienBulletTimer[ALIndex]:
                try:
                    if alienRow2[ALIndex].collidepoint(alx, aly) == False:
                        #print "Shoot alien 2"
                        #print alienRow2[ALIndex]
                        aly += 50
                        try:
                            if alienRow3[ALIndex].collidepoint(alx, aly) == False:
                                aly += 50
                                try:
                                    if alienRow4[ALIndex].collidepoint(alx, aly) == False:
                                        aly += 50
                                        #print ALIndex
                                        try:
                                            if alienRow5[ALIndex].collidepoint(alx, aly) == False:
                                                alienBulPosx = alienRow1[ALIndex].centerx
                                                alienBulPosy = alienRow1[ALIndex].centery + 15
                                                alienBulRect = pygame.Rect(alienBulPosx, alienBulPosy, 5, 10)
                                                alienBulletArray.append(alienBulRect)
                                                if ALIndex == 0:
                                                    alienBulletTickCount = 0
                                                elif ALIndex == 1:
                                                    alienBulletTickCount2 = 0
                                                elif ALIndex == 2:
                                                    alienBulletTickCount3 = 0
                                                elif ALIndex == 3:
                                                    alienBulletTickCount4 = 0
                                                elif ALIndex == 4:
                                                    alienBulletTickCount5 = 0
                                                elif ALIndex == 5:
                                                    alienBulletTickCount6 = 0
                                                elif ALIndex == 6:
                                                    alienBulletTickCount7 = 0
                                                elif ALIndex == 7:
                                                    alienBulletTickCount8 = 0
                                                elif ALIndex == 8:
                                                    alienBulletTickCount9 = 0
                                                elif ALIndex == 9:
                                                    alienBulletTickCount10 = 0
                                                elif ALIndex == 10:
                                                    alienBulletTickCount11 = 0
                                                elif ALIndex == 11:
                                                    alienBulletTickCount12 = 0
                                            elif alienRow5[ALIndex].collidepoint(alx, aly):
                                                #print "Don't Shoot row 5"
                                                if ALIndex == 0:
                                                    alienBulletTickCount = 0
                                                elif ALIndex == 1:
                                                    alienBulletTickCount2 = 0
                                                elif ALIndex == 2:
                                                    alienBulletTickCount3 = 0
                                                elif ALIndex == 3:
                                                    alienBulletTickCount4 = 0
                                                elif ALIndex == 4:
                                                    alienBulletTickCount5 = 0
                                                elif ALIndex == 5:
                                                    alienBulletTickCount6 = 0
                                                elif ALIndex == 6:
                                                    alienBulletTickCount7 = 0
                                                elif ALIndex == 7:
                                                    alienBulletTickCount8 = 0
                                                elif ALIndex == 8:
                                                    alienBulletTickCount9 = 0
                                                elif ALIndex == 9:
                                                    alienBulletTickCount10 = 0
                                                elif ALIndex == 10:
                                                    alienBulletTickCount11 = 0
                                                elif ALIndex == 11:
                                                    alienBulletTickCount12 = 0
                                        except IndexError:
                                            if ALIndex == 0:
                                                alienBulletTickCount = 0
                                            elif ALIndex == 1:
                                                alienBulletTickCount2 = 0
                                            elif ALIndex == 2:
                                                alienBulletTickCount3 = 0
                                            elif ALIndex == 3:
                                                alienBulletTickCount4 = 0
                                            elif ALIndex == 4:
                                                alienBulletTickCount5 = 0
                                            elif ALIndex == 5:
                                                alienBulletTickCount6 = 0
                                            elif ALIndex == 6:
                                                alienBulletTickCount7 = 0
                                            elif ALIndex == 7:
                                                alienBulletTickCount8 = 0
                                            elif ALIndex == 8:
                                                alienBulletTickCount9 = 0
                                            elif ALIndex == 9:
                                                alienBulletTickCount10 = 0
                                            elif ALIndex == 10:
                                                alienBulletTickCount11 = 0
                                            elif ALIndex == 11:
                                                alienBulletTickCount12 = 0
                                    elif alienRow4[ALIndex].collidepoint(alx, aly):
                                        #print "Don't Shoot row 4"
                                        if ALIndex == 0:
                                            alienBulletTickCount = 0
                                        elif ALIndex == 1:
                                            alienBulletTickCount2 = 0
                                        elif ALIndex == 2:
                                            alienBulletTickCount3 = 0
                                        elif ALIndex == 3:
                                            alienBulletTickCount4 = 0
                                        elif ALIndex == 4:
                                            alienBulletTickCount5 = 0
                                        elif ALIndex == 5:
                                            alienBulletTickCount6 = 0
                                        elif ALIndex == 6:
                                            alienBulletTickCount7 = 0
                                        elif ALIndex == 7:
                                            alienBulletTickCount8 = 0
                                        elif ALIndex == 8:
                                            alienBulletTickCount9 = 0
                                        elif ALIndex == 9:
                                            alienBulletTickCount10 = 0
                                        elif ALIndex == 10:
                                            alienBulletTickCount11 = 0
                                        elif ALIndex == 11:
                                            alienBulletTickCount12 = 0
                                except IndexError:
                                    if ALIndex == 0:
                                        alienBulletTickCount = 0
                                    elif ALIndex == 1:
                                        alienBulletTickCount2 = 0
                                    elif ALIndex == 2:
                                        alienBulletTickCount3 = 0
                                    elif ALIndex == 3:
                                        alienBulletTickCount4 = 0
                                    elif ALIndex == 4:
                                        alienBulletTickCount5 = 0
                                    elif ALIndex == 5:
                                        alienBulletTickCount6 = 0
                                    elif ALIndex == 6:
                                        alienBulletTickCount7 = 0
                                    elif ALIndex == 7:
                                        alienBulletTickCount8 = 0
                                    elif ALIndex == 8:
                                        alienBulletTickCount9 = 0
                                    elif ALIndex == 9:
                                        alienBulletTickCount10 = 0
                                    elif ALIndex == 10:
                                        alienBulletTickCount11 = 0
                                    elif ALIndex == 11:
                                        alienBulletTickCount12 = 0
                            elif alienRow3[ALIndex].collidepoint(alx, aly):
                                #print "Don't Shoot row 3"
                                if ALIndex == 0:
                                    alienBulletTickCount = 0
                                elif ALIndex == 1:
                                    alienBulletTickCount2 = 0
                                elif ALIndex == 2:
                                    alienBulletTickCount3 = 0
                                elif ALIndex == 3:
                                    alienBulletTickCount4 = 0
                                elif ALIndex == 4:
                                    alienBulletTickCount5 = 0
                                elif ALIndex == 5:
                                    alienBulletTickCount6 = 0
                                elif ALIndex == 6:
                                    alienBulletTickCount7 = 0
                                elif ALIndex == 7:
                                    alienBulletTickCount8 = 0
                                elif ALIndex == 8:
                                    alienBulletTickCount9 = 0
                                elif ALIndex == 9:
                                    alienBulletTickCount10 = 0
                                elif ALIndex == 10:
                                    alienBulletTickCount11 = 0
                                elif ALIndex == 11:
                                    alienBulletTickCount12 = 0
                        except IndexError:
                            if ALIndex == 0:
                                alienBulletTickCount = 0
                            elif ALIndex == 1:
                                alienBulletTickCount2 = 0
                            elif ALIndex == 2:
                                alienBulletTickCount3 = 0
                            elif ALIndex == 3:
                                alienBulletTickCount4 = 0
                            elif ALIndex == 4:
                                alienBulletTickCount5 = 0
                            elif ALIndex == 5:
                                alienBulletTickCount6 = 0
                            elif ALIndex == 6:
                                alienBulletTickCount7 = 0
                            elif ALIndex == 7:
                                alienBulletTickCount8 = 0
                            elif ALIndex == 8:
                                alienBulletTickCount9 = 0
                            elif ALIndex == 9:
                                alienBulletTickCount10 = 0
                            elif ALIndex == 10:
                                alienBulletTickCount11 = 0
                            elif ALIndex == 11:
                                alienBulletTickCount12 = 0
                    elif alienRow2[ALIndex].collidepoint(alx, aly):
                        #print "Don't Shoot, row 2"
                        if ALIndex == 0:
                            alienBulletTickCount = 0
                        elif ALIndex == 1:
                            alienBulletTickCount2 = 0
                        elif ALIndex == 2:
                            alienBulletTickCount3 = 0
                        elif ALIndex == 3:
                            alienBulletTickCount4 = 0
                        elif ALIndex == 4:
                            alienBulletTickCount5 = 0
                        elif ALIndex == 5:
                            alienBulletTickCount6 = 0
                        elif ALIndex == 6:
                            alienBulletTickCount7 = 0
                        elif ALIndex == 7:
                            alienBulletTickCount8 = 0
                        elif ALIndex == 8:
                            alienBulletTickCount9 = 0
                        elif ALIndex == 9:
                            alienBulletTickCount10 = 0
                        elif ALIndex == 10:
                            alienBulletTickCount11 = 0
                        elif ALIndex == 11:
                            alienBulletTickCount12 = 0
                except IndexError:
                    if ALIndex == 0:
                        alienBulletTickCount = 0
                    elif ALIndex == 1:
                        alienBulletTickCount2 = 0
                    elif ALIndex == 2:
                        alienBulletTickCount3 = 0
                    elif ALIndex == 3:
                        alienBulletTickCount4 = 0
                    elif ALIndex == 4:
                        alienBulletTickCount5 = 0
                    elif ALIndex == 5:
                        alienBulletTickCount6 = 0
                    elif ALIndex == 6:
                        alienBulletTickCount7 = 0
                    elif ALIndex == 7:
                        alienBulletTickCount8 = 0
                    elif ALIndex == 8:
                        alienBulletTickCount9 = 0
                    elif ALIndex == 9:
                        alienBulletTickCount10 = 0
                    elif ALIndex == 10:
                        alienBulletTickCount11 = 0
                    elif ALIndex == 11:
                        alienBulletTickCount12 = 0
            for bullet in bulletCollection:
                if bullet.colliderect(alien1):
                    score += 100
                    invaderKilled()
                    bulletCollection.remove(bullet)
                    alienRow1.remove(alien1)		
            if move_tick_count >= moveSpeed:#once the move timer is reached
                move_tick_count = 0
                if imgIndex == 0:
                    imgIndex += 1#change the index to change which image is displayed
                elif imgIndex == 1:
                    imgIndex = 0#reset the index to 0 once it hits its maximum
                for alien1 in alienRow1:#and move the alien to left or right(depending which wall is hit)
                    alien1.left += dax
            if (alien1.left < 30 and right == False):#if the alien hits the left wall
                dax = -dax #reverse the direction of the alien so it doesn't go off screen
                for alien5 in alienRow5:
                    alien5.bottom += 10 #move all aliens down 10 pixels
                for alien4 in alienRow4:
                    alien4.bottom += 10  
                for alien3 in alienRow3:
                    alien3.bottom += 10
                for alien2 in alienRow2:
                    alien2.bottom += 10
                for alien1 in alienRow1:
                    alien1.bottom += 10
                right = True
                if moveSpeed > 100: #If the max speed of the aliens isn't reached
                    moveSpeed -= moveSubt #speed the aliens up after hitting the left wall
            if (alien1.right > 970 and right == True):
                dax = -dax
                for alien5 in alienRow5:
                    alien5.bottom += 10
                for alien4 in alienRow4:
                    alien4.bottom += 10
                for alien3 in alienRow3:
                    alien3.bottom += 10
                for alien2 in alienRow2:
                    alien2.bottom += 10
                for alien1 in alienRow1:
                    alien1.bottom += 10
                    alien1.left += 2*dax
                right = False
            if alien1.bottom >= 650:#if the aliens reach the barriers at the bottom
                loser()#it's game over, call loser() function stating it's game over

            
        screen.blit(ship, (shipRect))
        # movement for ship            
        oldx = shipRect.left
        shipRect.left += dsx
        #if shipRect.collide point(Screen size min + 10, screen size + ship height) or shipRect.collidepoint(Screen size max - 10, screen size + ship height):
        shipRect.left = oldx
        pygame.display.update()
        
        
def loser(): #Writen By Dylan
    done = False
    while not done:
        screen.fill(BLACK)
        #pygame.display.update()
        overFont = pygame.font.SysFont("timesnewroman", 100)
        againFont = pygame.font.SysFont("timesnewroman", 40)
        decideFont = pygame.font.SysFont("timesnewroman", 30)
        loserText = overFont.render("Game Over", True, WHITE)
        againText = againFont.render("Would You Like to Play Again?", True, WHITE)
        yesText = decideFont.render("Yes", True, WHITE)
        noText = decideFont.render("No", True, WHITE)
        loserPos = loserText.get_rect(center = (size[0]/2, size[1]/2 - 250))
        againPos = againText.get_rect(center = (size[0]/2, size[1]/2 - 100))
        yesPos = yesText.get_rect(center = (size[0]/2 - 100, size[1]/2 + 100))
        noPos = noText.get_rect(center = (size[0]/2 + 100, size[1]/2 + 100))
        
        #loserPos = (500, 400)
        screen.blit(loserText, loserPos)
        screen.blit(againText, againPos)
        screen.blit(yesText, yesPos)
        screen.blit(noText, noPos)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                if yesPos.collidepoint(mousePos):
                    game()
                    done = True
                elif noPos.collidepoint(mousePos):
                    done = True
                    pygame.quit()
        
game()
pygame.quit()

