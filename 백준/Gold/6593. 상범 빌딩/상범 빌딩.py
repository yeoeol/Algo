from collections import deque

while True:
    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        break

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    grid = []
    for _ in range(l):
        grid.append([list(input()) for _ in range(r)])
        input()

    def in_range(x, y):
        return 0 <= x < r and 0 <= y < c

    def bfs(floor, x, y):
        queue = deque([(floor, x, y, 0)])
        visited = [[[False]*c for _ in range(r)] for _ in range(l)]
        visited[floor][x][y] = True

        while queue:
            floor, x, y, cnt = queue.popleft()
            if grid[floor][x][y] == 'E':
                return cnt

            for dx, dy in zip(dxs, dys):
                nx, ny = x+dx, y+dy
                if in_range(nx, ny) and not visited[floor][nx][ny] and grid[floor][nx][ny] != '#':
                    queue.append((floor, nx, ny, cnt+1))
                    visited[floor][nx][ny] = True
            for f in [-1, 1]:
                nf = floor+f
                if 0 <= nf < l:
                    if not visited[nf][x][y] and grid[nf][x][y] != '#':
                        queue.append((nf, x, y, cnt+1))
                        visited[nf][x][y] = True
        return -1

    def find_start(grid):
        for f in range(l):
            for i in range(r):
                for j in range(c):
                    if grid[f][i][j] == 'S':
                        return f, i, j
        return 0, 0, 0

    floor, sx, sy = find_start(grid)
    result = bfs(floor, sx, sy)
    if result == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {result} minute(s).")
