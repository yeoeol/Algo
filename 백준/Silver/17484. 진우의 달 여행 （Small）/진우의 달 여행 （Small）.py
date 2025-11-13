import sys

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

M = sys.maxsize
visited = [[[M, M, M] for _ in range(m)] for _ in range(n)]
for j in range(m):
    visited[0][j][0] = grid[0][j]
    visited[0][j][1] = grid[0][j]
    visited[0][j][2] = grid[0][j]

for i in range(1, n):
    for j in range(m):
        if j == 0:
            visited[i][j][0] = min(visited[i-1][j+1][1], visited[i-1][j+1][2]) + grid[i][j]
            visited[i][j][1] = min(visited[i-1][j][0], visited[i-1][j][2]) + grid[i][j]
        elif j == m-1:
            visited[i][j][1] = min(visited[i-1][j][0], visited[i-1][j][2]) + grid[i][j]
            visited[i][j][2] = min(visited[i-1][j-1][0], visited[i-1][j-1][1]) + grid[i][j]
        else:
            visited[i][j][0] = min(visited[i-1][j+1][1], visited[i-1][j+1][2]) + grid[i][j]
            visited[i][j][1] = min(visited[i-1][j][0], visited[i-1][j][2]) + grid[i][j]
            visited[i][j][2] = min(visited[i-1][j-1][0], visited[i-1][j-1][1]) + grid[i][j]

res = M
for x, y, z in visited[-1]:
    res = min(res, min(x, y, z))
print(res)
