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
        
def bfs(grid, queue):
    dup = set()
    
    while queue:
        x, y, d, cnt = queue.popleft()
        dup.add((x, y))
        for i in range(4):
            nx, ny = move(grid, x, y, i)
            if grid[nx][ny] == 'G':
                return cnt+1
            if (nx, ny) not in dup:
                dup.add((nx, ny))
                queue.append((nx, ny, i, cnt+1))
    return -1


def solution(board):
    queue = deque()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                queue.append((i, j, 0, 0))
        
    return bfs(board, queue)