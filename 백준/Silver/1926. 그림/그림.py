from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cnt = 1
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt

visited = [[False] * m for _ in range(n)]
num = 0
res = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i, j, visited)
            res = max(res, cnt)
            num += 1

print(num)
print(res)