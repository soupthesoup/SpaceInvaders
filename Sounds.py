import pygame
# loads different sounds and puts them into variables to be called
player_killed = pygame.mixer.music.load('explosion.wav')
invader_killed = pygame.mixer.music.load('invaderkilled.wav')
shoot = pygame.mixer.music.load('shoot.wav')


# function for different sounds
def player.explosion():
  pygame.mixer.Sound.play(player_killed)
  pygame.mixer.music.stop()

def invader.killed():
	pygame.mixer.Sound.play(invader_killed)
	pygame.mixer.music.stop()

def shoot():
	pygame.mixer.Sound.play(shoot)
	pygame.mixer.music.stop()
  
