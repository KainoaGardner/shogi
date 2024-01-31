import pygame
from settings import *
from board import *
def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mosPos = pygame.mouse.get_pos()
                    if MARGINSIZE + MOCHIGOMA < mosPos[0] < WIDTH - (MARGINSIZE + MOCHIGOMA) and MARGINSIZE < mosPos[1] < HEIGHT - MARGINSIZE:
                        tile = ((mosPos[0] - MARGINSIZE - MOCHIGOMA) // TILESIZE,(mosPos[1] - MARGINSIZE) // TILESIZE)
                        if len(board.clicks) < 1 and board.checkClick(tile):
                            board.clicks.append(tile)
                            board.movePiece()
                        elif len(board.clicks) == 1:
                            board.clicks.append(tile)
                            board.movePiece()
                            board.clicks.clear()
                        else:
                            board.clicks.clear()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if len(board.moveHistory) > 0:
                        move = board.moveHistory.pop(-1)
                        board.board[move[0][0][1]][move[0][0][0]] = move[0][1]
                        board.board[move[1][0][1]][move[1][0][0]] = move[1][1]
                        if move[1][1] in board.pieceList:
                            index = board.pieceList.index(move[1][1][1])
                            if board.sente:
                                if board.goMochigoma.count(move[1][1][1]) > 0:
                                    board.goMochigomaCount[index] -= 1
                            if not board.sente:
                                if board.senMochigoma.count(move[1][1][1]) > 0:
                                    board.senMochigomaCount[index] -= 1
                        board.sente = not board.sente






        # screen.fill("#2d3436")
        screen.fill("#dfe6e9")
        board.display()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

main()