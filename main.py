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
                        elif len(board.clicks) == 1:
                            board.clicks.append(tile)
                            if 0 <= board.clicks[0][0]:
                                board.movePiece()
                            else:
                                board.placeMochigoma()
                            board.clicks.clear()
                        else:
                            board.clicks.clear()

                    if MARGINSIZE < mosPos[0] < MARGINSIZE + MOCHIGOMA and MARGINSIZE < mosPos[1] < MARGINSIZE + TILESIZE * 7:
                        tile = (-1, 6 - ((mosPos[1] - MARGINSIZE) // TILESIZE))
                        if len(board.clicks) < 1 and board.checkMochigomaClick(tile):
                            board.clicks.append(tile)
                        elif len(board.clicks) == 1:
                            board.clicks.append(tile)
                            board.clicks.clear()
                        else:
                            board.clicks.clear()

                    if WIDTH - MARGINSIZE - MOCHIGOMA < mosPos[0] < WIDTH - MARGINSIZE and HEIGHT - MARGINSIZE - TILESIZE * 7 < mosPos[1] < HEIGHT - MARGINSIZE:
                        tile = (-2, (mosPos[1] - MARGINSIZE - (TILESIZE * 2)) // TILESIZE)
                        if len(board.clicks) < 1 and board.checkMochigomaClick(tile):
                            board.clicks.append(tile)
                        elif len(board.clicks) == 1:
                            board.clicks.append(tile)
                            board.clicks.clear()
                        else:
                            board.clicks.clear()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if len(board.moveHistory) > 0:
                        move = board.moveHistory.pop(-1)
                        if move[0][0][0] >= 0:
                            board.board[move[0][0][1]][move[0][0][0]] = move[0][1]
                            board.board[move[1][0][1]][move[1][0][0]] = move[1][1]
                            if move[1][1][1] in board.pieceList:
                                index = board.pieceList.index(move[1][1][1])
                                if board.sente:
                                    if board.goMochigoma.count(move[1][1][1]) > 0:
                                        board.goMochigoma.remove(move[1][1][1])
                                        board.goMochigomaCount[index] -= 1
                                if not board.sente:
                                    if board.senMochigoma.count(move[1][1][1]) > 0:
                                        board.senMochigoma.remove(move[1][1][1])
                                        board.senMochigomaCount[index] -= 1
                            board.getMochigoma()
                            board.sente = not board.sente
                        else:
                            board.board[move[1][0][1]][move[1][0][0]] = move[1][1]
                            if board.sente:
                                board.goMochigoma.append(move[0][1])
                            elif not board.sente:
                                board.senMochigoma.append(move[0][1])
                            board.sente = not board.sente
                            board.getMochigoma()



        screen.fill("#dfe6e9")
        board.display()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

main()