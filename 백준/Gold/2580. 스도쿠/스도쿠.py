board = [list(map(int, input().split())) for _ in range(9)]
space = [
    (i, j)
    for i in range(9)
    for j in range(9)
    if board[i][j] == 0
]

def row_check(x, y, num):
    for i in range(9):
        if board[x][i] == num:
            return False
    return True

def col_check(x, y, num):
    for i in range(9):
        if board[i][y] == num:
            return False
    return True


def in_range(x, y):
    return 0 <= x < 9 and 0 <= y < 9


def box_check(x, y, num):
    x = x // 3 * 3
    y = y // 3 * 3
    for i in range(x, x+3):
        for j in range(y, y+3):
            if in_range(i, j) and board[i][j] == num:
                return False
    return True

def fill(idx):
    if idx >= len(space):
        for b in board:
            print(*b)
        exit()

    x, y = space[idx]
    for i in range(1, 10):
        if row_check(x, y, i) and col_check(x, y, i) and box_check(x, y, i):
            board[x][y] = i
            fill(idx+1)
            board[x][y] = 0

fill(0)

