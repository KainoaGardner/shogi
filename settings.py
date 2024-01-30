import pygame
TILESIZE = 75
MARGINSIZE = TILESIZE // 2
MOCHIGOMA = TILESIZE * 3
WIDTH = TILESIZE * 9 + MARGINSIZE * 2 + MOCHIGOMA * 2
HEIGHT = TILESIZE * 9 + MARGINSIZE * 2
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()