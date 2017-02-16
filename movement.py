###########################################################
#               ICS4U1 movement and animations            #
#                       Group poject                      #
###########################################################
import pygame


# movement for aliens function
for alien in alienArray:
    pygame.draw.rect(screen, White, alien, 0)
    #bullet collision here
    if move_tick_count >= 2000:
        move_tick_count = 0
		for alien in alien_array():
			alien.left += dax
			if (alien.right > 950 and right == True):
				for alien5 in alien_array5():
					alien5.bottom += 10
				for alien4 in alien_array4():
					alien4.bottom += 10
				for alien3 in alien_array3():
					alien3.bottom += 10
				for alien2 in alien_array2():
					alien2.bottom += 10
				for alien in alien_array():
					alien.bottom += 10
					
		for alien2 in alien_array2():
			alien2.left += dax
		for alien3 in alien_array3():
			alien3.left += dax
		for alien4 in alien_array4():
			alien4.left += dax
		for alien5 in alien_array5():
			alien5.left += dax
		
		
        
    


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
