#######################################################
#   Final Project: Space Invaders                     #
#   Programmer:  Matthew Litt                         #
#   Class: ICS3U                                      #
#   Teacher: Mr. Holik                                #
#######################################################

import pygame
import sys
from random import randint
pygame.init()
screenSize = (1000,800)
screen = pygame.display.set_mode((screenSize),0)
pygame.display.set_caption("Space Invaders")

White = (255,255,255)
Green = (0,255,0)
Red = (255,0,0)
Blue = (0,0,255)
Black = (0,0,0)

screen.fill(Black)
pygame.display.update()





main = True
game = False
controls = False
loser = False
choose = True
alien2 = True
alien3 = True
while main:
    score = 0
    count = 0
    highScore = 0
    lengthAlien1 = 0
    lengthAlien2 = 0
    lengthAlien3 = 0
    shot = 0
    shot2 = 0
    shot3 = 0
    shot4 = 0
    shot5 = 0
    alienShot5 = True
    alienShot4 = False
    alienShot3 = False
    alienShot2 = False
    alienShot1 = False
    x = 150
    y = 650
    x2 = 350
    x3 = 550
    x4 = 750
    Ax = 115
    tAy = 150
    Ay2 = 200
    Ay3 = 250
    Ay4 = 300
    Ay5 = 350
    shipx = 450
    shipy = 725
    shiph = 35
    shipw = 75
    lx = 100
    ly = 760
    dsx = 0
    dax = 10
    day = 5
    right = True
    oldx = 0
    shipBullety = 0
    shipBulletx = 0
    shipBulletdy = -7
    alienBulletdy = 7
    alienBulletx = 0
    alienBullety = 0
    moveclock = pygame.time.Clock()
    move_tick_count = 0
    moveclock2 = pygame.time.Clock()
    move_tick_count2 = 0
    moveclock3 = pygame.time.Clock()
    move_tick_count3 = 0
    moveclock4 = pygame.time.Clock()
    move_tick_count4 = 0
    moveclock5 = pygame.time.Clock()
    move_tick_count5 = 0
    shipBulletClock = pygame.time.Clock()
    shipBulletTickCount = 0
    alienBulletClock = pygame.time.Clock()
    shotTickCount = 0
    lifeRect = pygame.Rect(lx,ly,20,20)
    playRect = pygame.Rect(350, 300, 200, 50)
    controlsRect = pygame.Rect(350, 400, 200, 50)
    quitRect = pygame.Rect(350, 500, 200, 50)
    menuRect = pygame.Rect(700, 50, 200, 50)
    shipRect = pygame.Rect(shipx,shipy,shipw,shiph)
    Lives = []
    barrier1 = []
    barrier2 = []
    barrier3 = []
    barrier4 = []
    alienRow1 = []
    alienRow2 = []
    alienRow3 = []
    alienRow4 = []
    alienRow5 = []
    bulletArray = []
    alienBulletArray = []
    Barrier = [
        "WWWWWWWWWWWWWWWWWWWW",
        "WWWWWWWWWWWWWWWWWWWW",
        "WWWWWWWWWWWWWWWWWWWW",
        "WWWWW          WWWWW",
        ]
    aliens = [
        "AAAAAAAAAAA"
        ]

    initialLives = [
        "LLL",
        ]

    for row in initialLives:
        for col in row:
            if col == "L":
                lifeRect = pygame.Rect(lx,ly,20,20)
                Lives.append(lifeRect)
            lx += 25
        
            
    for row in aliens:
        for col in row:
            if col == "A":
# variables for the sprite
##                alien1_image = pygame.image.load("Alien1.png")
##                alien2_image = pygame.image.load("Alien2.png")
##                alien3_image = pygame.image.load("Alien3.png")
                alien1Rect = pygame.Rect(Ax,tAy,30,30)
##                screen.blit(alien1_image(alien1Rect))
                alienRow1.append(alien1Rect)
                alien2Rect = pygame.Rect(Ax,Ay2,30,30)
                alienRow2.append(alien2Rect)
##                screen.blit(alien2_image(alien2Rect))
                alien3Rect = pygame.Rect(Ax,Ay3,30,30)
##                screen.blit(alien2_image(alien3Rect))
                alienRow3.append(alien3Rect)
                alien4Rect = pygame.Rect(Ax,Ay4,30,30)
##                screen.blit(alien3_image(alien4Rect))
                alienRow4.append(alien4Rect)
                alien5Rect = pygame.Rect(Ax,Ay5,30,30)
##                screen.blit(alien3_image(alien5Rect))
                alienRow5.append(alien5Rect)
            Ax += 75
        Ax = 115


    for row in Barrier:
        for col in row:
            if col == "W":
                wallRect = pygame.Rect(x,y,5,10)
                barrier1.append(wallRect)
                wall2Rect = pygame.Rect(x2,y,5,10)
                barrier2.append(wall2Rect)
                wall3Rect = pygame.Rect(x3,y,5,10)
                barrier3.append(wall3Rect)
                wall4Rect = pygame.Rect(x4,y,5,10)
                barrier4.append(wall4Rect)
            x += 5
            x2 += 5
            x3 += 5
            x4 += 5
        y += 10
        x = 150
        x2 = 350
        x3 = 550
        x4 = 750
    screen.fill(Black)
    pygame.display.update()
    while choose:
        fontTitle = pygame.font.SysFont("Times New Roman",125)
        textTitle = fontTitle.render("Space Invaders", True, (White))
        screen.blit(textTitle,(100, 100))
        pygame.draw.rect(screen, White, playRect, 0)
        pygame.draw.rect(screen, White, controlsRect, 0)
        pygame.draw.rect(screen, White, quitRect, 0)
        fontTitle = pygame.font.SysFont("Times New Roman",50)
        textTitle = fontTitle.render("Play", True, (Black))
        screen.blit(textTitle,(350,290))
        fontTitle = pygame.font.SysFont("Times New Roman",50)
        textTitle = fontTitle.render("Controls", True, (Black))
        screen.blit(textTitle,(350, 390))
        fontTitle = pygame.font.SysFont("Times New Roman",50)
        textTitle = fontTitle.render("Quit", True, (Black))
        screen.blit(textTitle,(350, 490))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                choose = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    choose = False
                    main = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if playRect.collidepoint(pos):
                    screen.fill(Black)
                    pygame.display.update()
                    game = True
                    choose = False
                elif controlsRect.collidepoint(pos):
                    screen.fill(Black)
                    pygame.display.update()
                    controls = True
                    choose = False
                elif quitRect.collidepoint(pos):
                    choose = False
                    main = False

    while controls:
        fontTitle = pygame.font.SysFont("Times New Roman",125)
        textTitle = fontTitle.render("Controls:", True, (White))
        screen.blit(textTitle,(25, 100))
        fontTitle = pygame.font.SysFont("Times New Roman",100)
        textTitle = fontTitle.render("Movement:", True, (White))
        screen.blit(textTitle,(50, 300))
        fontTitle = pygame.font.SysFont("Times New Roman",45)
        textTitle = fontTitle.render("Use the left and rigth arrow keys to move", True, (White))
        screen.blit(textTitle,(100, 400))
        fontTitle = pygame.font.SysFont("Times New Roman",100)
        textTitle = fontTitle.render("Firing and Rules:", True, (White))
        screen.blit(textTitle,(50, 600))
        fontTitle = pygame.font.SysFont("Times New Roman",45)
        textTitle = fontTitle.render("Use the up arrow key to fire, kill all the aliens to win", True, (White))
        screen.blit(textTitle,(100, 700))
        pygame.draw.rect(screen, White, menuRect, 0)
        fontTitle = pygame.font.SysFont("Times New Roman",50)
        textTitle = fontTitle.render("Menu", True, (Black))
        screen.blit(textTitle,(700, 40))
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen.fill(Black)
                pygame.display.update()
                controls = False
                choose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    screen.fill(Black)
                    pygame.display.update()
                    controls = False
                    choose = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if menuRect.collidepoint(pos):
                    screen.fill(Black)
                    pygame.display.update()
                    controls = False
                    choose = True
        
    while game:
        pygame.time.delay(20)
        shipBulletTickCount += shipBulletClock.tick()
        length = len(bulletArray)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                choose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game = False
                    choose = True
                elif event.key == pygame.K_RIGHT:
                    dsx = 5
                elif event.key == pygame.K_LEFT:
                    dsx = -5
                elif event.key == pygame.K_UP and (shipBulletTickCount >= 500) or length <= 0:
                    shipBulletTickCount = 0
                    bulletArray.append(bulletRect)
                    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if menuRect.collidepoint(pos):
                    screen.fill(Black)
                    pygame.display.update()
                    game = False 
                    choose = True
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dsx = 0

                    
        screen.fill(Black)
        shipBulletx = shipRect.centerx
        shipBullety = shipRect.centery + 5
        bulletRect = pygame.Rect(shipBulletx,shipBullety,5,10)
        oldx = shipRect.left
        shipRect.left += dsx
        
        if shipRect.collidepoint(10,725) or shipRect.collidepoint(990,725):
            shipRect.left = oldx
        
        for bullet in bulletArray:
            bullet.top += shipBulletdy
            pygame.draw.rect(screen,White,bullet,0)
            if (bullet.top < 0):
                bulletArray.remove(bullet)
                    
        for wall1 in barrier1:
            pygame.draw.rect(screen,Green,wall1,0)
            for bullet in bulletArray:
                if bullet.colliderect(wall1):
                    bulletArray.remove(bullet)
                    barrier1.remove(wall1)
            for alienBullet in alienBulletArray:
                if alienBullet.colliderect(wall1):
                    alienBulletArray.remove(alienBullet)
                    barrier1.remove(wall1)
        for wall2 in barrier2:
            pygame.draw.rect(screen,Green,wall2,0)
            for bullet in bulletArray:
                if bullet.colliderect(wall2):
                    bulletArray.remove(bullet)
                    barrier2.remove(wall2)
            for alienBullet in alienBulletArray:
                if alienBullet.colliderect(wall2):
                    alienBulletArray.remove(alienBullet)
                    barrier2.remove(wall2)
        for wall3 in barrier3:
            pygame.draw.rect(screen,Green,wall3,0)
            for bullet in bulletArray:
                if bullet.colliderect(wall3):
                    bulletArray.remove(bullet)
                    barrier3.remove(wall3)
            for alienBullet in alienBulletArray:
                if alienBullet.colliderect(wall3):
                    alienBulletArray.remove(alienBullet)
                    barrier3.remove(wall3)
        for wall4 in barrier4:
            pygame.draw.rect(screen,Green,wall4,0)
            for bullet in bulletArray:
                if bullet.colliderect(wall4):
                    bulletArray.remove(bullet)
                    barrier4.remove(wall4)
            for alienBullet in alienBulletArray:
                if alienBullet.colliderect(wall4):
                    alienBulletArray.remove(alienBullet)
                    barrier4.remove(wall4)
            
        move_tick_count = move_tick_count + moveclock.tick()
        move_tick_count2 = move_tick_count2 + moveclock2.tick()
        move_tick_count3 = move_tick_count3 + moveclock3.tick()
        move_tick_count4 = move_tick_count4 + moveclock4.tick()
        move_tick_count5 = move_tick_count5 + moveclock5.tick()
        shotTickCount += alienBulletClock.tick()



        length5 = len(alienRow1)
        length4 = len(alienRow2)
        length3 = len(alienRow3)
        length2 = len(alienRow4)
        length = len(alienRow5)
        shot = randint(0,length-1)
        shot2 = randint(0,length2-1)
        shot3 = randint(0,length3-1)
        shot4 = randint(0,length4-1)
        shot5 = randint(0,length5-1)
        
        for alien5 in alienRow5:
            count += 1
            if (count == shot and alienShot5 == True):
                abx = alien5[count].centerx
                aby = alien5[count].centery
                alienShot = pygame.Rect(abx,aby,5,10)
                alienBulletArray.append(alienShot)
                print alienBulletArray
                count = 0
                shotTickCount = 0
                
        for alien4 in alienRow4:
            count += 1
            if (count == shot and alienShot4 == True):
                abx = alien4[count].centerx
                aby = alien4[count].centery
                alienShot = pygame.Rect(abx,aby,5,10)
                alienBulletArray.append(alienShot)
                print alienBulletArray
                count = 0
                shotTickCount = 0

        for alien3 in alienRow3:
            count += 1
            if (count == shot and alienShot3 == True):
                abx = alien3[count].centerx
                aby = alien3[count].centery
                alienShot = pygame.Rect(abx,aby,5,10)
                alienBulletArray.append(alienShot)
                print alienBulletArray
                count = 0
                shotTickCount = 0

        for alien2 in alienRow2:
            count += 1
            if (count == shot and alienShot2 == True):
                abx = alien2[count].centerx
                aby = alien2[count].centery
                alienShot = pygame.Rect(abx,aby,5,10)
                alienBulletArray.append(alienShot)
                print alienBulletArray
                count = 0
                shotTickCount = 0
                
        for alien1 in alienRow1:
            count += 1
            if (count == shot and alienShot1 == True):
                abx = alien1[count].centerx
                aby = alien1[count].centery
                alienShot = pygame.Rect(abx,aby,5,10)
                alienBulletArray.append(alienShot)
                print alienBulletArray
                count = 0
                shotTickCount = 0
                
        for alienBullet in alienBulletArray:
            alienBullet.top += alienBulletdy
            pygame.draw.rect(screen,White,alienBullet,0)
            if (alienBullet.bottom > 800):
                alienBulletArray1.remove(alienBullet)
                
        for alien1 in alienRow1:
            pygame.draw.rect(screen,White,alien1,0)
            for bullet in bulletArray:
                if bullet.colliderect(alien1):
                    score += 100
                    bulletArray.remove(bullet)
                    alienRow1.remove(alien1)
            if move_tick_count >= 2000:
                for alien1 in alienRow1:
                    alien1.left += dax
                    if (alien1.right > 950 and right == True):
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
                        for alien1 in alienRow1:
                            alien1.bottom += 10
                            alien1.left += 2*dax
                    elif (alien1.left < 50 and right == False):
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
                            alien1.right += 1/2*dax
                move_tick_count = 0

                    
        for alien2 in alienRow2:
            pygame.draw.rect(screen,White,alien2,0)
            for bullet in bulletArray:
                if bullet.colliderect(alien2):
                    score += 40
                    bulletArray.remove(bullet)
                    alienRow2.remove(alien2)
            if move_tick_count2 >= 2000:
                for alien2 in alienRow2:
                    alien2.left += dax
                    if (alien2.right > 950 and right == True):
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
                    elif (alien2.left < 50 and right == False):
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
                            alien2.right += 1/2*dax
                        for alien1 in alienRow1:
                            alien1.bottom += 10
                            alien1.right += 1/2*dax
                    move_tick_count2 = 0

                
        for alien3 in alienRow3:
            pygame.draw.rect(screen,White,alien3,0)
            for bullet in bulletArray:
                if bullet.colliderect(alien3):
                    score += 40
                    bulletArray.remove(bullet)
                    alienRow3.remove(alien3)
            if move_tick_count3 >= 2000:
                for alien3 in alienRow3:
                    alien3.left += dax
                    if (alien3.right > 950 and right == True):
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
                    elif (alien3.left < 50 and right == False):
                        right = True
                        dax = -dax
                        for alien5 in alienRow5:
                            alien5.bottom += 10
                        for alien4 in alienRow4:
                            alien4.bottom += 10
                        for alien3 in alienRow3:
                            alien3.bottom += 10
                            alien3.right += 1/2*dax
                        for alien2 in alienRow2:
                            alien2.bottom += 10
                            alien2.right += 1/2*dax
                        for alien1 in alienRow1:
                            alien1.bottom += 10
                            alien1.right += 1/2*dax
                    move_tick_count3 = 0


        for alien4 in alienRow4:
            pygame.draw.rect(screen,White,alien4,0)
            for bullet in bulletArray:
                if bullet.colliderect(alien4):
                    score += 20
                    bulletArray.remove(bullet)
                    alienRow4.remove(alien4)
            if move_tick_count4 >= 2000:
                for alien4 in alienRow4:
                    alien4.left += dax
                    if (alien4.right > 950 and right == True):
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
                    elif (alien4.left < 50 and right == False):
                        right = True
                        dax = -dax
                        for alien5 in alienRow5:
                            alien5.bottom += 10
                        for alien4 in alienRow4:
                            alien4.bottom += 10
                            alien4.right += 1/2*dax
                        for alien3 in alienRow3:
                            alien3.bottom += 10
                            alien3.right += 1/2*dax
                        for alien2 in alienRow2:
                            alien2.bottom += 10
                            alien2.right += 1/2*dax
                        for alien1 in alienRow1:
                            alien1.bottom += 10
                            alien1.right += 1/2*dax
                    move_tick_count4 = 0

        for alien5 in alienRow5:
            pygame.draw.rect(screen,White,alien5,0)
            for bullet in bulletArray:
                if bullet.colliderect(alien5):
                    score += 20
                    bulletArray.remove(bullet)
                    alienRow5.remove(alien5)
            if move_tick_count5 >= 2000:
                for alien5 in alienRow5:
                    alien5.left += dax
                    if (alien5.right > 950 and right == True):
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
                    elif (alien5.left < 50 and right == False):
                        right = True
                        dax = -dax
                        for alien5 in alienRow5:
                            alien5.bottom += 10
                            alien5.right += 1/2*dax
                        for alien4 in alienRow4:
                            alien4.bottom += 10
                            alien4.right += 1/2*dax
                        for alien3 in alienRow3:
                            alien3.bottom += 10
                            alien3.right += 1/2*dax
                        for alien2 in alienRow2:
                            alien2.bottom += 10
                            alien2.right += 1/2*dax
                        for alien1 in alienRow1:
                            alien1.bottom += 10
                            alien1.right += 1/2*dax
                    move_tick_count5 = 0

                
        for life in Lives:
            pygame.draw.rect(screen,White,life,0)
##            if (score >= 1000):
##                Lives.append(lifeRect)
##                if life.colliderect(life):
##                    life.left += 25
        pygame.draw.rect(screen,White,shipRect,0)
        fontTitle = pygame.font.SysFont("Times New Roman",30)
        textTitle = fontTitle.render("Score: " + str(score), True, (White))
        screen.blit(textTitle,(20, 50))
        fontTitle = pygame.font.SysFont("Times New Roman",30)
        textTitle = fontTitle.render("Lives: ", True, (White))
        screen.blit(textTitle,(20, 750))
        pygame.draw.rect(screen, White, menuRect, 0)
        fontTitle = pygame.font.SysFont("Times New Roman",50)
        textTitle = fontTitle.render("Menu", True, (Black))
        screen.blit(textTitle,(730, 40))
## changes the highscore
#        newFile = open('SpaceInvadersHighScore.txt', 'r+')
#        if (score > highScore):
#            for line in newFile:
#                line.pop(line)
#                newFile.Write(score)
#            highScore = score
#        elif (score <= highScore):
#            for line in newFile:
#                highScore = line
#            newFile.close()
#       fontTitle = pygame.font.SysFont("Times New Roman",30)
#        textTitle = fontTitle.render("HighScore: " + str(highScore), True, (White))
#        screen.blit(textTitle,(475, 40))
        pygame.display.update()
        if (alien1.bottom >= 650):
            game = False
            loser = True
            screen.fill(Black)
            pygame.display.update()
        elif (alien2.bottom >= 650):
            game = False
            loser = True
            screen.fill(Black)
            pygame.display.update()
        elif (alien3.bottom >= 650):
            game = False
            loser = True
            screen.fill(Black)
            pygame.display.update()
        elif (alien4.bottom >= 650):
            game = False
            loser = True
            screen.fill(Black)
            pygame.display.update()
        elif (alien5.bottom >= 650):
            game = False
            loser = True
            screen.fill(Black)
            pygame.display.update()

        if (length == 0 and length2 == 0 and length3 == 0 and length4 == 0 and length5 == 0):
            wait = True
            while wait:
                fontTitle = pygame.font.SysFont("Times New Roman",100)
                textTitle = fontTitle.render("continue playing Y/N?", True, (White))
                screen.blit(textTitle,(100, 300))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            wait = False
                        elif event.key == pygame.K_n:
                            wait = False
                            game = False
                      
                x = 150
                y = 650
                x2 = 350
                x3 = 550
                x4 = 750
                Ax = 115
                tAy = 150
                Ay2 = 200
                Ay3 = 300
                shipx = 450
                shipy = 725
                shiph = 35
                shipw = 75
                lx = 100
                ly = 760
                dsx = 0
                dax = 10
                da2x = 10
                da3x = 10
                day = 5
                right = True
                oldx = 0
                shipBullety = 0
                shipBulletx = 0
                shipBulletdy = -7
                alienBulletdy = 0
                moveclock = pygame.time.Clock()
                move_tick_count = 0
                moveclock2 = pygame.time.Clock()
                move_tick_count2 = 0
                moveclock3 = pygame.time.Clock()
                move_tick_count3 = 0
                shipBulletClock = pygame.time.Clock()
                shipBulletTickCount = 0
                lifeRect = pygame.Rect(lx,ly,20,20)
                playRect = pygame.Rect(350, 300, 200, 50)
                controlsRect = pygame.Rect(350, 400, 200, 50)
                quitRect = pygame.Rect(350, 500, 200, 50)
                menuRect = pygame.Rect(700, 50, 200, 50)
                shipRect = pygame.Rect(shipx,shipy,shipw,shiph)
                barrier1 = []
                barrier2 = []
                barrier3 = []
                barrier4 = []
                alienRow1 = []
                alienRow2 = []
                alienRow3 = []
                bulletArray = []
                alienBulletArray = []
                Barrier = [
                    "WWWWWWWWWWWWWWWWWWWW",
                    "WWWWWWWWWWWWWWWWWWWW",
                    "WWWWWWWWWWWWWWWWWWWW",
                    "WWWWW          WWWWW",
                    ]
                topAliens = [
                    "AAAAAAAAAAA"
                    ]
                Aliens = [
                    "BBBBBBBBBBB",
                    "BBBBBBBBBBB",
                    ]

                    
                        
                for row in topAliens:
                    for col in row:
                        if col == "A":
                            topAlienRect = pygame.Rect(Ax,tAy,30,30)
                            alienRow1.append(topAlienRect)
                        Ax += 75
                    Ax = 115

                for row in Aliens:
                    for col in row:
                        if col == "B":
                            alien2Rect = pygame.Rect(Ax,Ay2,30,30)
                            alienRow2.append(alien2Rect)
                            alien3Rect = pygame.Rect(Ax,Ay3,30,30)
                            alienRow3.append(alien3Rect)
                        Ax += 75
                    Ax = 115
                    Ay2 += 50
                    Ay3 += 50

                for row in Barrier:
                    for col in row:
                        if col == "W":
                            wallRect = pygame.Rect(x,y,5,10)
                            barrier1.append(wallRect)
                            wall2Rect = pygame.Rect(x2,y,5,10)
                            barrier2.append(wall2Rect)
                            wall3Rect = pygame.Rect(x3,y,5,10)
                            barrier3.append(wall3Rect)
                            wall4Rect = pygame.Rect(x4,y,5,10)
                            barrier4.append(wall4Rect)
                        x += 5
                        x2 += 5
                        x3 += 5
                        x4 += 5
                    y += 10
                    x = 150
                    x2 = 350
                    x3 = 550
                    x4 = 750
                
    while loser:
        fontTitle = pygame.font.SysFont("Times New Roman",125)
        textTitle = fontTitle.render("You Lost!", True, (White))
        screen.blit(textTitle,(300, 100))
        fontTitle = pygame.font.SysFont("Times New Roman",50)
        textTitle = fontTitle.render("your final score was: " + str(score), True, (White))
        screen.blit(textTitle,(350, 400))
        fontTitle = pygame.font.SysFont("Times New Roman",50)
        textTitle = fontTitle.render("Play again Y/N", True, (White))
        screen.blit(textTitle,(350,300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    loser = False
                    game = True
                elif event.key == pygame.K_n:
                    loser = False
                    main = False
    
pygame.quit()
sys.exit()
