###########################################################
#               ICS4U1 movement and animations            #
#                       Group poject                      #
###########################################################
import pygame


# movement for aliens function
# def movment(



# movement for ship
def player_move(dsx, dx, dy):
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
        
