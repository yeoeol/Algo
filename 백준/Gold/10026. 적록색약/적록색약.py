import sys
sys.setrecursionlimit(10**6)

n = int(input())
grid = [list(input()) for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def dfs(x, y, cur, visited):
    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] in cur:
            dfs(nx, ny, cur, visited)

original = 0
mang = 0

visited = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
cur_color = set()

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            original += 1
            cur_color.add(grid[i][j])
            dfs(i, j, cur_color, visited)

        if not visited2[i][j]:
            mang += 1
            cur_color.add(grid[i][j])
            if grid[i][j] == 'R':
                cur_color.add('G')
            elif grid[i][j] == 'G':
                cur_color.add('R')
            dfs(i, j, cur_color, visited2)

        cur_color.clear()

print(original, mang)