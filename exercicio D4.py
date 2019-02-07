'''
Exercicio Python 4D Curso udemy

Victor A. de Souza Fonseca
'''

import pygame
#Pygame sempre deve ser iniciado antes de qualquer coisa
pygame.init()
pygame.display.set_mode((200,100))
#Buscando a musica na pasta
pygame.mixer.music.load('musica.mp3')
#A musica tem que dar play
pygame.mixer.music.play()
#Usando um wait ate a musica acabar
clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)


