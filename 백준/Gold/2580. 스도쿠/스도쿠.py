board = [list(map(int, input().split())) for _ in range(9)]
space = [
    (i, j)
    for i in range(9)
    for j in range(9)
    if board[i][j] == 0
]

def row_col_check(x, y, num):
    for i in range(9):
        if board[x][i] == num or board[i][y] == num:
            return False
    return True

def box_check(x, y, num):
    x = x // 3 * 3
    y = y // 3 * 3
    for i in range(x, x+3):
        for j in range(y, y+3):
            if board[i][j] == num:
                return False
    return True

def fill(idx):
    if idx >= len(space):
        for b in board:
            print(*b)
        return True

    x, y = space[idx]
    for i in range(1, 10):
        if row_col_check(x, y, i) and box_check(x, y, i):
            board[x][y] = i
            if fill(idx+1):
                return True
            board[x][y] = 0
            
    return False

fill(0)

