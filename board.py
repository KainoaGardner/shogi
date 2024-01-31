import pygame
from settings import *
from util import importFolder
class Board():
    def __init__(self):
        self.board = [["後香","後桂","後銀","後金","後王","後金","後銀","後桂","後香"],
                      ["  ","後飛","  ","  ","  ","  ","  ","後角","  "],
                      ["後歩","後歩","後歩","後歩","後歩","後歩","後歩","後歩","後歩"],
                      ["  ","  ","  ","  ","  ","  ","  ","  ","  ",],
                      ["  ","  ","  ","  ","先桂","  ","  ","  ","  ",],
                      ["  ","  ","  ","  ","  ","  ","  ","  ","  ",],
                      ["先歩","先歩","先歩","先歩","先歩","先歩","先歩","先歩","先歩"],
                      ["  ","先角","先歩","  ","  ","  ","  ","先飛","  "],
                      ["先香","先桂","先銀","先金","先玉","先金","先銀","先桂","先香"]]

        self.komaDict = importFolder("graphics/駒")
        self.clicks = []
        self.sente = True

        self.pieceList = ["歩", "香", "桂", "銀", "金", "角", "飛"]
        self.senMochigoma = ["歩", "香", "桂", "銀", "金", "角", "飛"]
        self.senMochigomaCount = []
        self.goMochigoma = ["歩", "香", "桂", "銀", "金", "角", "飛"]
        self.goMochigomaCount = []
        self.getMochigoma()

        self.moveHistory = []

    def drawBoard(self):
        # for rowIndex,row in enumerate(self.board):
        #     for colIndex,tile in enumerate(row):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                boardPosX = MARGINSIZE + MOCHIGOMA + TILESIZE * c
                boardPosY = MARGINSIZE + TILESIZE * r
                pygame.draw.rect(screen,"#B0926A",pygame.Rect(boardPosX,boardPosY,TILESIZE,TILESIZE))

    def drawLines(self):
        for i in range(10):
            if i % 9 == 0:
                pygame.draw.line(screen,"black",(MARGINSIZE + MOCHIGOMA,MARGINSIZE + TILESIZE * i),(WIDTH - (MARGINSIZE + MOCHIGOMA),MARGINSIZE + TILESIZE * i),5)
                pygame.draw.line(screen, "black", (MARGINSIZE + MOCHIGOMA + TILESIZE * i, MARGINSIZE),(MARGINSIZE + MOCHIGOMA + TILESIZE * i, HEIGHT - MARGINSIZE), 5)
            else:
                pygame.draw.line(screen, "black", (MARGINSIZE + MOCHIGOMA, MARGINSIZE + TILESIZE * i),(WIDTH - (MARGINSIZE + MOCHIGOMA), MARGINSIZE + TILESIZE * i), 3)
                pygame.draw.line(screen, "black", (MARGINSIZE + MOCHIGOMA + TILESIZE * i, MARGINSIZE),(MARGINSIZE + MOCHIGOMA + TILESIZE * i, HEIGHT - MARGINSIZE), 3)

        for i in range(2):
            pygame.draw.line(screen, "black", (MARGINSIZE, MARGINSIZE + TILESIZE * 7 * i),(MARGINSIZE + MOCHIGOMA, MARGINSIZE + TILESIZE * 7 * i), 5)
            pygame.draw.line(screen, "black", (MARGINSIZE + TILESIZE * i, MARGINSIZE),(MARGINSIZE + TILESIZE * i, MARGINSIZE + TILESIZE * 7), 5)

            pygame.draw.line(screen, "black", (WIDTH - (MARGINSIZE + MOCHIGOMA), HEIGHT - (MARGINSIZE + TILESIZE * 7) + TILESIZE * 7 * i),(WIDTH - MARGINSIZE, HEIGHT - (MARGINSIZE + TILESIZE * 7) + TILESIZE * 7 * i), 5)
            pygame.draw.line(screen, "black", (WIDTH - (MARGINSIZE + MOCHIGOMA) + TILESIZE * i, HEIGHT - MARGINSIZE - TILESIZE * 7),(WIDTH - (MARGINSIZE + MOCHIGOMA) + TILESIZE * i, HEIGHT - MARGINSIZE), 5)
    def drawMochigomaStand(self):
        pygame.draw.rect(screen,"#B0926A",pygame.Rect(WIDTH - MOCHIGOMA - MARGINSIZE,HEIGHT - MARGINSIZE - TILESIZE * 7,TILESIZE,TILESIZE * 7))
        pygame.draw.rect(screen, "#B0926A",pygame.Rect(MARGINSIZE, MARGINSIZE, TILESIZE ,TILESIZE * 7))

    def displayTiles(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] != "  ":
                    tile = self.board[r][c][1]
                    image = self.komaDict.get(tile)
                    if self.board[r][c][0] == "後":
                        image = pygame.transform.flip(image,False,True)
                    x = MARGINSIZE + MOCHIGOMA + TILESIZE * c
                    y = MARGINSIZE + TILESIZE * r
                    imageRect = image.get_rect(center= (x + TILESIZE // 2,y + TILESIZE // 2))
                    screen.blit(image,imageRect)

    def displaySelected(self):
        if len(self.clicks) == 1:
            x = self.clicks[0][0] * TILESIZE + MARGINSIZE + MOCHIGOMA
            y = self.clicks[0][1] * TILESIZE + MARGINSIZE
            screen.blit(highLight,(x,y))

    def movePiece(self):
        if len(self.clicks) == 2:
            tilePos = self.clicks[0]
            tile = self.board[tilePos[1]][tilePos[0]]

            movePos = self.clicks[1]
            endTile = self.board[movePos[1]][movePos[0]]

            if tile != movePos and tile != "  ":
                if self.validMove(tile, tilePos, movePos):
                    if tile[0] != endTile[0]:
                        self.board[movePos[1]][movePos[0]] = tile
                        self.board[tilePos[1]][tilePos[0]] = "  "

                        self.sente = not self.sente
                        self.moveHistory.append(((tilePos,tile),(movePos,endTile)))

    def validMove(self,tile,tilePos,movePos):
        if self.sente:
            direction = -1
        else:
            direction = 1

        if tile[1] == "歩":
            return self.valid歩(tilePos,movePos,direction)
        if tile[1] == "香":
            return self.valid香(tilePos,movePos)
        if tile[1] == "桂":
            return self.valid桂(tilePos,movePos,direction)


        return False

    def valid歩(self,tilePos,movePos,direction):
        if (tilePos[0],tilePos[1] + direction) == movePos:
            return True

    def valid香(self,tilePos,movePos):
        validPos = []
        if tilePos[0] == movePos[0]:
            if (self.sente and tilePos[1] > movePos[1]):
                for i in range(tilePos[1]):
                    if self.board[tilePos[1] - 1 - i][tilePos[0]][0] == " ":
                        validPos.append((tilePos[0], tilePos[1] - 1 - i))
                    elif self.board[tilePos[1] - 1 - i][tilePos[0]][0] == "後":
                        validPos.append((tilePos[0], tilePos[1] - 1 - i))
                        break
                    else:
                        break
            if (not self.sente and tilePos[1] < movePos[1]):
                for i in range(8 - tilePos[1]):
                    if self.board[tilePos[1] + 1 + i][tilePos[0]][0] == " ":
                        validPos.append((tilePos[0], tilePos[1] + 1 + i))
                    elif self.board[tilePos[1] + 1 + i][tilePos[0]][0] == "先":
                        validPos.append((tilePos[0], tilePos[1] + 1 + i))
                        break
                    else:
                        break
            if movePos in validPos:
                return True

    def valid桂(self,tilePos,movePos,direction):
        if (tilePos[0] - 1,tilePos[1] + direction * 2) == movePos or (tilePos[0] + 1,tilePos[1] + direction * 2) == movePos:
            return True

    def valid銀(self,tilePos,movePos,direction):
        pass

    def checkClick(self,pos):
        if self.board[pos[1]][pos[0]] != "  ":
            if self.sente and self.board[pos[1]][pos[0]][0] == "先":
                return  True
            elif not self.sente and self.board[pos[1]][pos[0]][0] == "後":
                return True
        return False

    def getMochigoma(self):
        if self.sente:
            self.senMochigomaCount.clear()
            for tile in self.pieceList:
                amount = self.senMochigoma.count(tile)
                self.senMochigomaCount.append(amount)
        if self.sente:
            self.goMochigomaCount.clear()
            for tile in self.pieceList:
                amount = self.goMochigoma.count(tile)
                self.goMochigomaCount.append(amount)

    def displayMochigoma(self):
        if len(self.senMochigoma) > 0:
            for i in range(len(self.senMochigomaCount)):
                if self.senMochigomaCount[i] > 0:
                    tile = self.komaDict.get(self.pieceList[i])
                    x = WIDTH - MARGINSIZE - MOCHIGOMA
                    y = HEIGHT - MARGINSIZE - TILESIZE * (7 - i)
                    imageRect = tile.get_rect(center=(x + TILESIZE // 2, y + TILESIZE // 2))
                    screen.blit(tile,imageRect)

                    countFont = font.render(f"{self.senMochigomaCount[i]}", True, "#ecf0f1")
                    screen.blit(countFont, (imageRect[0] - 7, imageRect[1]))

        if len(self.goMochigoma) > 0:
            for i in range(len(self.goMochigomaCount)):
                if self.goMochigomaCount[i] > 0:
                    tile = self.komaDict.get(self.pieceList[i])
                    tile = pygame.transform.flip(tile,False,True)
                    x = MARGINSIZE
                    y = MARGINSIZE + TILESIZE * (6 - i)
                    imageRect = tile.get_rect(center=(x + TILESIZE // 2, y + TILESIZE // 2))
                    screen.blit(tile,imageRect)


                    countFont = font.render(f"{self.goMochigomaCount[i]}", True, "#ecf0f1")
                    screen.blit(countFont, (imageRect[0] - 7, imageRect[1]))


    def display(self):
        self.drawBoard()
        self.displaySelected()
        self.displayTiles()
        self.drawMochigomaStand()
        self.displayMochigoma()
        self.drawLines()


board = Board()
