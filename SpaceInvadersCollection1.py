import pygame
import sys
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

def game():
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

    score = 0
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
    bulletCollection = []
    alienBulletArray = []
    alienBulletTimer = []   #Random numbers as a timer for aliens

    shipRect = pygame.Rect(shipx,shipy,shipw,shiph)

    right = True
    Main = True
    Game = False
    Controls = False
    Loser = False
    Choose = True

    i = 0
    while i < 8:
        shootTime = randint(2, 8)   #randint(minValue, maxValue)
        alienBulletTimer.append(shootTime)
        #print alienBulletTimer[i]  #testing if number randomized works
        i += 1 

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
                # variables for the sprite
                ##                alien1_image = pygame.image.load("Alien1.png")
                ##                alien2_image = pygame.image.load("Alien2.png")
                ##                alien3_image = pygame.image.load("Alien3.png")
                        alien1Rect = pygame.Rect(Ax,Ay,30,30)
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


##    screen.fill(BLACK)
##    pygame.display.update()
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

    game = True
    while Main:
        length = len(bulletCollection)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                Main = False
                #choose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dsx = 5
                elif event.key == pygame.K_LEFT:
                    dsx = -5
                elif event.key == pygame.K_UP and (shipBulletTickCount >= 500) or length <= 5:
                    shipBulletTickCount = 0
                    bulletCollection.append(bulletRect)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dsx = 0

        shipBulletx = shipRect.centerx
        shipBullety = shipRect.centery + 5
        bulletRect = pygame.Rect(shipBulletx,shipBullety,5,10)
        oldx = shipRect.left
        shipRect.left += dsx
        if shipRect.collidepoint(10,725) or shipRect.collidepoint(990,725):
            shipRect.left = oldx
        
        
        screen.fill(BLACK)
        pygame.time.delay(20)
        
        for wallR1 in barrier1:
            pygame.draw.rect(screen,GREEN,wallR1,0)
        for wallR2 in barrier2:
            pygame.draw.rect(screen,GREEN,wallR2,0)
        for wallR3 in barrier3:
            pygame.draw.rect(screen,GREEN,wallR3,0)
        for wallR4 in barrier4:
            pygame.draw.rect(screen,GREEN,wallR4,0)

        move_tick_count = move_tick_count + moveclock.tick()
        move_tick_count2 = move_tick_count2 + moveclock2.tick()
        move_tick_count3 = move_tick_count3 + moveclock3.tick()
        move_tick_count4 = move_tick_count4 + moveclock4.tick()
        move_tick_count5 = move_tick_count5 + moveclock5.tick()

        scoreStr = "Score: " + (str(score))
        scoreFont = pygame.font.SysFont("ariel", 20, True)#Writen by Dylan
        scoreText = scoreFont.render(scoreStr, True, WHITE)
        screen.blit(scoreText, (50, 50))

        for bullet in bulletCollection:#Writen by Dylan
            if bullet.top > 0: #if bullet is not at the top of the screen
                pygame.draw.rect(screen, WHITE, bullet, 0)
                bullet.top += bulletYspeed #Adds a negative value to move the bullet to the top of the screen.
                #pygame.display.update()
            elif bullet.top < 0: #checks collide with top of level
                bulletCollection.remove(bullet)#delete it if it does touch the top
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

        for alien1 in alienRow1:
            screen.blit(AL1Images[imgIndex], (alien1))
            for bullet in bulletCollection:
                if bullet.colliderect(alien1):
                    score += 100
                    bulletCollection.remove(bullet)
                    alienRow1.remove(alien1)
            if move_tick_count >= moveSpeed:
                move_tick_count = 0
                if imgIndex == 0:
                    imgIndex += 1
                elif imgIndex == 1:
                    imgIndex = 0
                for alien1 in alienRow1:
                    alien1.left += dax
                    #print alien1.left
            if (alien1.left < 30 and right == False):
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
                    #alien1.right += (1/2)*dax
                right = True
                if moveSpeed > 100:
                    moveSpeed -= moveSubt
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
            if alien1.bottom >= 650:
                loser()
                    
        for alien2 in alienRow2:
            screen.blit(AL2Images[imgIndex], (alien2))
            for bullet in bulletCollection:
                if bullet.colliderect(alien2):
                    score += 40
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

        for alien3 in alienRow3:
            screen.blit(AL2Images[imgIndex], (alien3))
            for bullet in bulletCollection:
                if bullet.colliderect(alien3):
                    score += 40
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

        for alien4 in alienRow4:
            screen.blit(AL3Images[imgIndex], (alien4))
            for bullet in bulletCollection:
                if bullet.colliderect(alien4):
                    score += 20
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

        for alien5 in alienRow5:
            screen.blit(AL3Images[imgIndex], (alien5))
            for bullet in bulletCollection:
                if bullet.colliderect(alien5):
                    score += 20
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
