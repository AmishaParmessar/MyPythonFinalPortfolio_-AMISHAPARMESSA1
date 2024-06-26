import pygame
from pygame.locals import *
pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer') 

#define game variables
tile_size = 250

#Insert images here
GameShow = pygame.image.load('GameShow Background.jpeg')

def draw_grid():
  for line in range (0,6):
    pygame.draw.line(screen, (255,255,255), (0, line * tile_size), (screen_width, line * tile_size))
    pygame.draw.line(screen, (255,255,255), (line * tile_size, 0), (line * tile_size, screen_height))


world_data = [
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1],
]


run = True
while run:

    screen.blit(GameShow, (0,0))

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit() 

