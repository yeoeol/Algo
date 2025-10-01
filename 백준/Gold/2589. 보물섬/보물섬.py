import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())
lands = []
grid = []
for i in range(n):
    arr = list(input())
    for j, a in enumerate(arr):
        if a == 'L':
            lands.append((i, j))
    grid.append(arr)

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True

    res = -1
    while queue:
        x, y, d = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 'L':
                visited[nx][ny] = True
                queue.append((nx, ny, d+1))
                res = max(res, d+1)
    return res

answer = -1
for x, y in lands:
    r = bfs(x, y)
    answer = max(answer, r)

print(answer)