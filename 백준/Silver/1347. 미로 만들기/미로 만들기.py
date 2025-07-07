dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

n = int(input())
s = input()
size = 101
grid = [[0] * size for _ in range(size)]
# 초기 위치(가운데)
x, y = size//2, size//2
grid[x][y] = '.'
direction = 2 # 초기에는 남쪽 바라보는 상태

for order in s:
    if order == 'R':
        direction = (direction+1) % 4
    elif order == 'L':
        direction = (direction+3) % 4
    else: # order == 'F'
        x += dxs[direction]
        y += dys[direction]
        grid[x][y] = '.'

# 격자판의 점 중에 최소 x, 최대 x 찾기
# 격자판의 점 중에 최소 y, 최대 y 찾기
min_x, max_x = size, 0
min_y, max_y = size, 0
for i in range(size):
    for j in range(size):
        if grid[i][j] == '.':
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)

for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        if grid[i][j] == 0:
            grid[i][j] = '#'

for i in range(min_x, max_x+1):
    print(*grid[i][min_y:max_y+1], sep="")
