import sys
from collections import deque

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def input():
    return sys.stdin.readline().strip()


n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
s, target_x, target_y = map(int, input().split())


def init_queue():
    queue = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                queue.append((grid[i][j], i, j, 0))
    return sorted(queue)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs():
    queue = deque(init_queue())
    while queue:
        val, x, y, t = queue.popleft()
        if t == s:
            return
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and grid[nx][ny] == 0:
                grid[nx][ny] = val
                queue.append((grid[nx][ny], nx, ny, t+1))

bfs()
print(grid[target_x-1][target_y-1])
