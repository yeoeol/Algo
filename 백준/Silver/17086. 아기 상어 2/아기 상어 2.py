from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    while sharks:
        x, y = sharks.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                sharks.append((nx, ny))

dist = []
sharks = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            sharks.append((i, j))
    dist.append(grid[i])
    
bfs()
ans = 0
for d in dist:
    ans = max(ans, max(d))
print(ans-1)
