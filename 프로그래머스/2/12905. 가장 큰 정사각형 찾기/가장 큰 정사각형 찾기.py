def solution(board):
    garo = len(board[0])
    sero = len(board)

    for i in range(1, sero):
        for j in range(1, garo):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1])+1

    M = 0
    for b in board:
        M = max(M, max(b))
    return M*M