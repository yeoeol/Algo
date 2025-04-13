n = int(input())

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

grid = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    grid[y][x] = 1
    dir_arr = [d]
    for _ in range(g):
        for i in range(len(dir_arr)-1, -1, -1):
            dir_arr.append((dir_arr[i]+1)%4)

    for d in dir_arr:
        dx, dy = dxs[d], dys[d]
        x, y = x+dx, y+dy
        grid[y][x] = 1

ans = 0
for i in range(100):
    for j in range(100):
        for x, y in [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]:
            if grid[x][y] != 1:
                break
        else:
            ans += 1
print(ans)
