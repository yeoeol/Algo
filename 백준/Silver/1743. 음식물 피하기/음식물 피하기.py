import copy, sys
from collections import deque

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().strip()

n, m, k = map(int, input().split())
grid = [[0] * m for _ in range(n)]
arr = []
for _ in range(k):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    arr.append((r, c))
    grid[r][c] = 1

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def dfs(x, y):
    visited[x][y] = True
    size = 1

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] == 1 and not visited[nx][ny]:
            size += dfs(nx, ny)

    return size

max_size = 0
visited = [[False] * m for _ in range(n)]
for r, c in arr:
    current_size = dfs(r, c)
    max_size = max(max_size, current_size)

print(max_size)
