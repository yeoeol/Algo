from collections import deque


dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def calc(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def check(grid, x, y):
    # 자기 자신의 상하좌우 먼저 확인
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny):
            if grid[nx][ny] == 'P':
                return False
    # 왼쪽위
    nx, ny = x-1, y-1
    if grid[nx][ny] == 'P' and in_range(nx, ny):
        if not (grid[x-1][y] == 'X' and grid[x][y-1] == 'X'):
            return False
    # 오른쪽 위
    nx, ny = x-1, y+1
    if in_range(nx, ny):
        if grid[nx][ny] == 'P' and not (grid[x-1][y] == 'X' and grid[x][y+1] == 'X'):
            return False
    # 오른쪽 아래
    nx, ny = x+1, y+1
    if in_range(nx, ny):
        if grid[nx][ny] == 'P' and not (grid[x+1][y] == 'X' and grid[x][y+1] == 'X'):
            return False
    # 왼쪽 아래
    nx, ny = x+1, y-1
    if in_range(nx, ny):
        if grid[nx][ny] == 'P' and not (grid[x+1][y] == 'X' and grid[x][y-1] == 'X'):
            return False
    
    # 위 2칸
    nx, ny = x-2, y
    if in_range(nx, ny):
        if grid[nx][ny] == 'P' and not (grid[x-1][y] == 'X'):
            return False
    # 아래 2칸
    nx, ny = x+2, y
    if in_range(nx, ny):
        if grid[nx][ny] == 'P' and not (grid[x+1][y] == 'X'):
            return False
    # 왼쪽 2칸
    nx, ny = x, y-2
    if in_range(nx, ny):
        if grid[nx][ny] == 'P' and not (grid[x][y-1] == 'X'):
            return False
    # 오른쪽 2칸
    nx, ny = x, y+2
    if in_range(nx, ny):
        if grid[nx][ny] == 'P' and not (grid[x][y+1] == 'X'):
            return False
    
    return True

def is_ans(grid):
    for i in range(5):
        for j in range(5):
            if grid[i][j] == 'P':
                if not check(grid, i, j):
                    return False
    return True

def solution(places):
    ans = []
    for place in places:
        if is_ans(place):
            ans.append(1)
        else:
            ans.append(0)
    return ans