import sys
sys.setrecursionlimit(10**6)

def input(): return sys.stdin.readline().strip()

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
max_length = max(grid[i][j] for i in range(n) for j in range(n))

ans = 0

def check_grid(graph, leng):
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= leng:
                graph[i][j] = 0
            else:
                graph[i][j] = 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
def dfs(graph, x, y, visited):
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(graph, nx, ny, visited)


for length in range(max_length):
    new_grid = [row[:] for row in grid]
    check_grid(new_grid, length)
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and new_grid[i][j] == 1:
                cnt += 1
                dfs(new_grid, i, j, visited)
    ans = max(ans, cnt)

print(ans)