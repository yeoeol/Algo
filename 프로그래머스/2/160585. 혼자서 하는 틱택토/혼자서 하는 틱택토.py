from collections import deque

dxs = [0, 1, 1, 1]
dys = [1, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def move(grid, x, y, d):
    dx, dy = dxs[d], dys[d]
    for i in range(1, 3):
        nx, ny = x+dx*i, y+dy*i
        if in_range(nx, ny) and grid[nx][ny] == grid[x][y]:
            continue
        return False
    return True

def solution(board):
    # 각 O, X에서 쭉 가는데 세로,가로,대각 중 하나가 완성됐을 때 O,X의 수가 같다면 False
    # 완성되지 않았을 때, 개수 같으면 True
    # 개수 다르면 False
    o_num, x_num = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_num += 1
            elif board[i][j] == 'X':
                x_num += 1
    if o_num == 0 and x_num == 0:
        return 1
    
    o_win, x_win = False, False
    for i in range(3):
        for j in range(3):
            if board[i][j] != '.':
                for d in range(4):
                    if move(board, i, j, d):
                        if board[i][j] == 'O':
                            o_win = True
                        else:
                            x_win = True
    if o_win and x_win:
        return 0
    if o_win:
        return 1 if o_num == x_num+1 else 0
    if x_win:
        return 1 if o_num == x_num else 0
    return 1 if o_num == x_num or o_num == x_num+1 else 0