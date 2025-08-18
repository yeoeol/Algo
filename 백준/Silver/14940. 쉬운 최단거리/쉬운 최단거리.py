from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            x, y = i, j
            break

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    result = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True

    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and grid[nx][ny] == 1 and not visited[nx][ny]:
                result[nx][ny] = result[x][y]+1
                queue.append((nx, ny))
                visited[nx][ny] = True

    return result

res = bfs(x, y)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and res[i][j] == 0:
            print(-1, end=' ')
        else:
            print(res[i][j], end=' ')
    print()