###########################################################
#               ICS4U1 movement and animations            #
#                       Group poject                      #
###########################################################
import pygame
AL1a = pygame.image.load("Alien1a.png")
AL1b = pygame.image.load("Alien1b.png")
AL2a = pygame.image.load("Alien2a.png")
AL2b = pygame.image.load("Alien2b.png")
AL3a = pygame.image.load("Alien3a.png")
AL3b = pygame.image.load("Alien3b.png")

# movement for aliens function
for alien1 in alienRow1:
    pygame.draw.rect(screen,White,alien1,0)
    for bullet in bulletCollection:
	if bullet.colliderect(alien1):
	    score += 100
	    bulletCollection.remove(bullet)
	    alienRow1.remove(alien1)
    if move_tick_count >= 1000:
	count += 1
	move_tick_count = 0
	for alien1 in alienRow1:
	    alien1.left += dax
	    print alien1.left
    if (alien1.left < 50 and right == False):
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
	    #alien1.right += 1/2*dax
    elif (alien1.right > 950 and right == True):
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

for alien2 in alienRow2:
    pygame.draw.rect(screen,White,alien2,0)
    for bullet in bulletArray:
	if bullet.colliderect(alien2):
	    score += 40
	    bulletArray.remove(bullet)
	    alienRow2.remove(alien2)
    if move_tick_count2 >= 1000:
	move_tick_count2 = 0
	for alien2 in alienRow2:
	    alien2.left += dax
    if (alien2.left < 50 and right == False):
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
    elif (alien2.right > 950 and right == True):
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





for alien3 in alienRow3:
    pygame.draw.rect(screen,White,alien3,0)
    for bullet in bulletCollection:
	if bullet.colliderect(alien3):
	    score += 40
	    bulletCollection.remove(bullet)
	    alienRow3.remove(alien3)
    if move_tick_count3 >= 1000:
	move_tick_count3 = 0
	for alien3 in alienRow3:
	    alien3.left += dax
    if (alien3.left < 50 and right == False):
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
    elif (alien3.right > 950 and right == True):
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


for alien4 in alienRow4:
    pygame.draw.rect(screen,White,alien4,0)
    for bullet in bulletCollection:
	if bullet.colliderect(alien4):
	    score += 20
	    bulletCollection.remove(bullet)
	    alienRow4.remove(alien4)
    if move_tick_count4 >= 1000:
	move_tick_count4 = 0
	for alien4 in alienRow4:
	    alien4.left += dax
    if (alien4.left < 50 and right == False):
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
    elif (alien4.right > 950 and right == True):
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



for alien5 in alienRow5:
    pygame.draw.rect(screen,White,alien5,0)
    for bullet in bulletCollection:
	if bullet.colliderect(alien5):
	    score += 20
	    bulletCollection.remove(bullet)
	    alienRow5.remove(alien5)
    if move_tick_count5 >= 1000:
	move_tick_count5 = 0
	for alien5 in alienRow5:
	    alien5.left += dax
    if (alien5.left < 50 and right == False):
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
    elif (alien5.right > 950 and right == True):
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
		
		
        
    


# movement for ship
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
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            dsx = 0

	
	
    
screen.fill(Black)
oldx = shipRect.left
shipRect.left += dsx
#if shipRect.collide point(Screen size min + 10, screen size + ship height) or shipRect.collidepoint(Screen size max - 10, screen size + ship height):
    shipRect.left = oldx
