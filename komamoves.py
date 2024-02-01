def valid歩(tilePos, movePos, direction):
    if (tilePos[0], tilePos[1] + direction) == movePos:
        return True

def valid香(tilePos, movePos,sente,board):
    validPos = []
    if tilePos[0] == movePos[0]:
        if (sente and tilePos[1] > movePos[1]):
            for i in range(tilePos[1]):
                if board[tilePos[1] - 1 - i][tilePos[0]][0] == " ":
                    validPos.append((tilePos[0], tilePos[1] - 1 - i))
                elif board[tilePos[1] - 1 - i][tilePos[0]][0] == "後":
                    validPos.append((tilePos[0], tilePos[1] - 1 - i))
                    break
                else:
                    break
        if (not sente and tilePos[1] < movePos[1]):
            for i in range(8 - tilePos[1]):
                if board[tilePos[1] + 1 + i][tilePos[0]][0] == " ":
                    validPos.append((tilePos[0], tilePos[1] + 1 + i))
                elif board[tilePos[1] + 1 + i][tilePos[0]][0] == "先":
                    validPos.append((tilePos[0], tilePos[1] + 1 + i))
                    break
                else:
                    break
        if movePos in validPos:
            return True

def valid桂(tilePos, movePos, direction):
    if (tilePos[0] - 1, tilePos[1] + direction * 2) == movePos or (
    tilePos[0] + 1, tilePos[1] + direction * 2) == movePos:
        return True

def valid銀(tilePos, movePos, direction):
    if (tilePos[0] - 1, tilePos[1] + direction) == movePos or (tilePos[0], tilePos[1] + direction) == movePos or (
    tilePos[0] + 1, tilePos[1] + direction) == movePos:
        return True
    if (tilePos[0] - 1, tilePos[1] - direction) == movePos or (tilePos[0] + 1, tilePos[1] - direction) == movePos:
        return True

def valid金(tilePos, movePos, direction):
    if (tilePos[0] - 1, tilePos[1] + direction) == movePos or (tilePos[0], tilePos[1] + direction) == movePos or (
    tilePos[0] + 1, tilePos[1] + direction) == movePos:
        return True
    if (tilePos[0] - 1, tilePos[1]) == movePos or (tilePos[0] + 1, tilePos[1]) == movePos or (
    tilePos[0], tilePos[1] - direction) == movePos:
        return True

def valid角(tilePos, movePos,sente,board):
    validMoves = []
    # direction = [(-1,-1),(-1,1),(1,-1),(1,1)]
    if sente:
        enemy = "後"
    else:
        enemy = "先"

    for i in range(min(tilePos[0],tilePos[1])):
        if board[tilePos[1] + (i + 1) * -1][tilePos[0] + (i + 1) * -1][0] == " ":
            validMoves.append((tilePos[0] + (i + 1) * -1,tilePos[1] + (i + 1) * -1))
        elif board[tilePos[1] + (i + 1) * -1][tilePos[0] + (i + 1) * -1][0] == enemy:
            validMoves.append((tilePos[0] + (i + 1) * -1,tilePos[1] + (i + 1) * -1))
            break
        else:
            break

    for i in range(min(tilePos[0],8 - tilePos[1])):
        if board[tilePos[1] + (i + 1) * 1][tilePos[0] + (i + 1) * -1][0] == " ":
            validMoves.append((tilePos[0] + (i + 1) * -1,tilePos[1] + (i + 1) * 1))
        elif board[tilePos[1] + (i + 1) * 1][tilePos[0] + (i + 1) * -1][0] == enemy:
            validMoves.append((tilePos[0] + (i + 1) * -1,tilePos[1] + (i + 1) * 1))
            break
        else:
            break

    for i in range(min(8 - tilePos[0],tilePos[1])):
        if board[tilePos[1] + (i + 1) * -1][tilePos[0] + (i + 1) * 1][0] == " ":
            validMoves.append((tilePos[0] + (i + 1) * 1,tilePos[1] + (i + 1) * -1))
        elif board[tilePos[1] + (i + 1) * -1][tilePos[0] + (i + 1) * 1][0] == enemy:
            validMoves.append((tilePos[0] + (i + 1) * 1,tilePos[1] + (i + 1) * -1))
            break
        else:
            break

    for i in range(min(8 - tilePos[0],8 - tilePos[1])):
        if board[tilePos[1] + (i + 1) * 1][tilePos[0] + (i + 1) * 1][0] == " ":
            validMoves.append((tilePos[0] + (i + 1) * 1,tilePos[1] + (i + 1) * 1))
        elif board[tilePos[1] + (i + 1) * 1][tilePos[0] + (i + 1) * 1][0] == enemy:
            validMoves.append((tilePos[0] + (i + 1) * 1,tilePos[1] + (i + 1) * 1))
            break
        else:
            break


    if movePos in validMoves:
        return True

def valid飛(tilePos, movePos,sente,board):
    validMoves = []
    # direction = [(-1,0),(1,0),(0,-1),(0,1)]
    if sente:
        enemy = "後"
    else:
        enemy = "先"

    for i in range(tilePos[0]):
        if board[tilePos[1]][tilePos[0] + (i + 1) * -1][0] == " ":
            validMoves.append((tilePos[0] + (i + 1) * -1,tilePos[1]))
        elif board[tilePos[1]][tilePos[0] + (i + 1) * -1][0] == enemy:
            validMoves.append((tilePos[0] + (i + 1) * -1,tilePos[1]))
            break
        else:
            break

    for i in range(8 - tilePos[0]):
        if board[tilePos[1]][tilePos[0] + (i + 1) * 1][0] == " ":
            validMoves.append((tilePos[0] + (i + 1) * 1,tilePos[1]))
        elif board[tilePos[1]][tilePos[0] + (i + 1) * 1][0] == enemy:
            validMoves.append((tilePos[0] + (i + 1) * 1,tilePos[1]))
            break
        else:
            break

    for i in range(tilePos[1]):
        if board[tilePos[1] + (i + 1) * -1][tilePos[0]][0] == " ":
            validMoves.append((tilePos[0],tilePos[1] + (i + 1) * -1))
        elif board[tilePos[1] + (i + 1) * -1][tilePos[0]][0] == enemy:
            validMoves.append((tilePos[0],tilePos[1] + (i + 1) * -1))
            break
        else:
            break

    for i in range(8 - tilePos[1]):
        if board[tilePos[1] + (i + 1) * 1][tilePos[0]][0] == " ":
            validMoves.append((tilePos[0],tilePos[1] + (i + 1) * 1))
        elif board[tilePos[1] + (i + 1) * 1][tilePos[0]][0] == enemy:
            validMoves.append((tilePos[0],tilePos[1] + (i + 1) * 1))
            break
        else:
            break

    if movePos in validMoves:
        return True

def valid王(tilePos, movePos):
    if (tilePos[0] - 1,tilePos[1] + 1) == movePos or (tilePos[0],tilePos[1] + 1) == movePos or (tilePos[0] + 1,tilePos[1] + 1) == movePos:
        return True
    if (tilePos[0] - 1, tilePos[1]) == movePos or (tilePos[0] + 1, tilePos[1]) == movePos:
        return True
    if (tilePos[0] - 1,tilePos[1] - 1) == movePos or (tilePos[0],tilePos[1] - 1) == movePos or (tilePos[0] + 1,tilePos[1] - 1) == movePos:
        return True
    pass