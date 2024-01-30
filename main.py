import pygame
from settings import *
from board import *
def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # screen.fill("#2d3436")
        screen.fill("#dfe6e9")
        board.display()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

main()