import pygame
from time import sleep

print('CONTAGEM REGRESSIVA!')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[31mFOGOOOOOO!!!!!\033[m')
pygame.mixer.init()
pygame.mixer.music.load('fogos.mp3')
pygame.mixer.music.play()
input()
