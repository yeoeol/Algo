from collections import deque

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

answer = []

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    fire_time = [[-1]*w for _ in range(h)]

    def in_range(x, y):
        return 0 <= x < h and 0 <= y < w

    def spread():
        global grid, fire_time

        queue = deque()
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '*':
                    queue.append((i, j))
                    fire_time[i][j] = 0
        while queue:
            x, y = queue.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x+dx, y+dy
                if in_range(nx, ny) and grid[nx][ny] == '.' and fire_time[nx][ny] == -1:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    queue.append((nx, ny))

    def bfs(x, y):
        queue = deque([(x, y, 0)])
        visited = [[False]*w for _ in range(h)]
        visited[x][y] = True

        while queue:
            x, y, time = queue.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x+dx, y+dy
                if not in_range(nx, ny):
                    return time+1
                if visited[nx][ny] or grid[nx][ny] != '.':
                    continue

                if fire_time[nx][ny] != -1 and fire_time[nx][ny] <= time+1:
                    continue

                queue.append((nx, ny, time+1))
                visited[nx][ny] = True
        return -1

    spread()

    x, y = 0, 0
    f = False
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '@':
                x, y = i, j
                f = True
                break
        if f: break
    res = bfs(x, y)
    answer.append("IMPOSSIBLE" if res == -1 else res)

print(*answer, sep='\n')