import pygame

pygame.init()

TILESIZE = 90
MARGINSIZE = TILESIZE // 2
MOCHIGOMA = TILESIZE
WIDTH = TILESIZE * 9 + MARGINSIZE * 2 + MOCHIGOMA * 2
HEIGHT = TILESIZE * 9 + MARGINSIZE * 2
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

highLight = pygame.Surface((TILESIZE,TILESIZE))
highLight.fill("#2d3436")
highLight.set_alpha(100)

font = pygame.font.SysFont("BIZ UDPゴシック",50)
