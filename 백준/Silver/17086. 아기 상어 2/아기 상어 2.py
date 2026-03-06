from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

ans = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(grid, x, y):
    queue = deque()
    queue.append((x, y, 0))
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True

    while queue:
        x, y, dist = queue.popleft()
        if grid[x][y] == 1:
            return dist
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist+1))
    return 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            cnt = bfs(grid, i, j)
            ans = max(ans, cnt)
print(ans)