grid = [[0] * 100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            grid[i][j] = 1

def in_range(x, y):
    return 0 <= x < 100 and 0 <= y < 100


cnt = 0
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
for i in range(100):
    for j in range(100):
        if grid[i][j] == 1:
            for dx, dy in zip(dxs, dys):
                nx, ny = i+dx, j+dy
                if not in_range(nx, ny) or grid[nx][ny] == 0:
                    cnt += 1

print(cnt)