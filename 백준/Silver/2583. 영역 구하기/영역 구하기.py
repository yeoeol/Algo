from collections import deque

m, n, k = map(int, input().split())
grid = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            grid[m-1-y][x] = 1


def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
                queue.append((nx, ny))
                cnt += 1
                visited[nx][ny] = True
    return cnt

visited = [[False] * n for _ in range(m)]
cnt = 0
ans = []
for i in range(m):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 0:
            cnt += 1
            ans.append(bfs(i, j, visited))

print(cnt)
print(*sorted(ans))