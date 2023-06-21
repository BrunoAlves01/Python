import pygame
pygame.init()
print('Tocando música')
pygame.mixer.music.load('ex.mp3')
pygame.mixer.music.play()
pygame.event.wait()
