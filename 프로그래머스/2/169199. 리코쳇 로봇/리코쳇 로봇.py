from collections import deque


dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# d 방향으로 멈출 때까지 쭉 가기
def move(grid, x, y, d):
    n, m = len(grid), len(grid[0])
    dx, dy = dxs[d], dys[d]
    while True:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 'D':
                return (x, y)
        else:
            return (x, y)
        x, y = nx, ny
        
def bfs(grid, x, y, tx, ty):
    queue = deque()
    queue.append((x, y, 0, 0))
    dup = set()
    dup.add((x, y))
    
    while queue:
        x, y, d, cnt = queue.popleft()
        for i in range(4):
            nx, ny = move(grid, x, y, i)
            if nx == tx and ny == ty:
                return cnt+1
            if (nx, ny) not in dup:
                dup.add((nx, ny))
                queue.append((nx, ny, i, cnt+1))
    return -1


def solution(board):
    grid = []
    x, y = 0, 0
    tx, ty = 0, 0
    for i in range(len(board)):
        arr = []
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                x, y = i, j
            elif board[i][j] == 'G':
                tx, ty = i, j
            arr.append(board[i][j])
        grid.append(arr)
        
    return bfs(grid, x, y, tx, ty)