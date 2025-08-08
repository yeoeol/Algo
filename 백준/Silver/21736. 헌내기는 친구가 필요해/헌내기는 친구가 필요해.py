import sys
from collections import deque

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())

visited = [[False] * m for _ in range(n)]
grid = [list(input()) for i in range(n)]

x, y = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'I':
            x, y = i, j
        elif grid[i][j] == 'X':
            visited[i][j] = True

visited[x][y] = True

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    cnt = 0
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                if grid[nx][ny] == 'P':
                    cnt += 1
    return cnt

cnt = bfs(x, y)
print(cnt if cnt != 0 else "TT")
