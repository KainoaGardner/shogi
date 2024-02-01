import pygame
from settings import *
class Button(pygame.sprite.Sprite):
    def __init__(self,sente,text,x,y,color):
        super().__init__()
        self.sente = sente
        self.outLine = self.image = pygame.Surface((TILESIZE + 3,TILESIZE + 5))
        self.outLineRect  = self.outLine .get_rect(topleft = ((MARGINSIZE + TILESIZE * x - 2, MARGINSIZE + TILESIZE * y - 2)))
        self.outLine.fill("Black")

        self.image = pygame.Surface((TILESIZE - 5,TILESIZE - 5))
        self.imageRect = self.image.get_rect(center = self.outLineRect.center)
        self.image.fill("#ecf0f1")
        self.text = fontBig.render(f"{text}", True, color)
        self.textRect = self.text.get_rect(center = self.imageRect.center)

        self.pressed = False


    def draw(self):
        self.checkClick()
        screen.blit(self.outLine,self.outLineRect)
        screen.blit(self.image,self.imageRect)
        screen.blit(self.text,self.textRect)

    def checkClick(self):
        if pygame.mouse.get_pressed()[0] and self.outLineRect.collidepoint(pygame.mouse.get_pos()) and self.pressed == False:
            # self.pressed = True
            return True


buttonGroup = pygame.sprite.Group()
