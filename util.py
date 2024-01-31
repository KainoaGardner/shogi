from os import walk
import pygame
from settings import *
def importFolder(path):
    surfaceDict = {}
    for _,__,imgFiles in walk(path):
        for piece in imgFiles:
            fullPath = path + '/' + piece
            imageSurf = pygame.image.load(f'{fullPath}').convert_alpha()
            imageSurf = pygame.transform.scale(imageSurf,(0.85860 *(TILESIZE - 15),TILESIZE - 15))
            piece = piece.replace('.png','')
            surfaceDict.update({f"{piece}":imageSurf})

    return surfaceDict
