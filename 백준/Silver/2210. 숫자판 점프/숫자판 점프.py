import sys

sys.setrecursionlimit(10**8)

grid = [list(map(int, input().split())) for _ in range(5)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def dfs(x, y, cnt, s):
    if cnt == 5:
        sets.add(s)
        return
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny):
            dfs(nx, ny, cnt+1, s+str(grid[nx][ny]))

sets = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, 0, str(grid[i][j]))
print(len(sets))
