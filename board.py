import pygame
from settings import *
class Board():
    def __init__(self):
        self.board = [["後香","後桂","後銀","後金","後王","後金","後銀","後桂","後香"],
                      ["後 ","後飛","後 ","後 ","後 ","後 ","後 ","後角","後 "],
                      ["後歩","後歩","後歩","後歩","後歩","後歩","後歩","後歩","後歩"],
                      ["  ","  ","  ","  ","  ","  ","  ","  ","  ",],
                      ["  ","  ","  ","  ","  ","  ","  ","  ","  ",],
                      ["  ","  ","  ","  ","  ","  ","  ","  ","  ",],
                      ["先歩","先歩","先歩","先歩","先歩","先歩","先歩","先歩","先歩"],
                      ["  ","先角","  ","  ","  ","  ","  ","先飛","  "],
                      ["先香","先桂","先銀","先金","先玉","先金","先銀","先桂","先香"]]

    def drawBoard(self):
        # for rowIndex,row in enumerate(self.board):
        #     for colIndex,tile in enumerate(row):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                boardPosX = MARGINSIZE + MOCHIGOMA + TILESIZE * c
                boardPosY = MARGINSIZE + TILESIZE * r
                pygame.draw.rect(screen,"#ddb892",pygame.Rect(boardPosX,boardPosY,TILESIZE,TILESIZE))

    def drawLines(self):
        for i in range(10):
            if i % 9 == 0:
                pygame.draw.line(screen,"black",(MARGINSIZE + MOCHIGOMA,MARGINSIZE + TILESIZE * i),(WIDTH - (MARGINSIZE + MOCHIGOMA),MARGINSIZE + TILESIZE * i),5)
                pygame.draw.line(screen, "black", (MARGINSIZE + MOCHIGOMA + TILESIZE * i, MARGINSIZE),(MARGINSIZE + MOCHIGOMA + TILESIZE * i, HEIGHT - MARGINSIZE), 5)
            else:
                pygame.draw.line(screen, "black", (MARGINSIZE + MOCHIGOMA, MARGINSIZE + TILESIZE * i),(WIDTH - (MARGINSIZE + MOCHIGOMA), MARGINSIZE + TILESIZE * i), 3)
                pygame.draw.line(screen, "black", (MARGINSIZE + MOCHIGOMA + TILESIZE * i, MARGINSIZE),(MARGINSIZE + MOCHIGOMA + TILESIZE * i, HEIGHT - MARGINSIZE), 3)

        for i in range(2):
            pygame.draw.line(screen, "black", (MARGINSIZE, MARGINSIZE + TILESIZE * 3 * i),(MARGINSIZE + MOCHIGOMA, MARGINSIZE + TILESIZE * 3 * i), 5)
            pygame.draw.line(screen, "black", (MARGINSIZE + TILESIZE * 3 * i, MARGINSIZE),(MARGINSIZE + TILESIZE * 3 * i, MARGINSIZE + TILESIZE * 3), 5)

            pygame.draw.line(screen, "black", (WIDTH - (MARGINSIZE + MOCHIGOMA), HEIGHT - (MARGINSIZE + TILESIZE * 3) + TILESIZE * 3 * i),(WIDTH - MARGINSIZE, HEIGHT - (MARGINSIZE + TILESIZE * 3) + TILESIZE * 3 * i), 5)
            pygame.draw.line(screen, "black", (WIDTH - (MARGINSIZE + MOCHIGOMA) + TILESIZE * 3 * i, HEIGHT - MARGINSIZE - TILESIZE * 3),(WIDTH - (MARGINSIZE + MOCHIGOMA) + TILESIZE * 3 * i, HEIGHT - MARGINSIZE), 5)
    def drawMochigomaStand(self):
        pygame.draw.rect(screen,"#ddb892",pygame.Rect(WIDTH - MOCHIGOMA - MARGINSIZE,HEIGHT - MARGINSIZE - TILESIZE * 3,TILESIZE * 3,TILESIZE * 3))
        pygame.draw.rect(screen, "#ddb892",pygame.Rect(MARGINSIZE, MARGINSIZE, TILESIZE * 3,TILESIZE * 3))

    def display(self):
        self.drawBoard()
        self.drawMochigomaStand()
        self.drawLines()
board = Board()
