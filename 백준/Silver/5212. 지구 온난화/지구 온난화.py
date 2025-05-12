r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
land = [(i, j) for i in range(r) for j in range(c) if grid[i][j] == 'X']

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

def isValid(x, y):
    if not in_range(x, y):
        return True
    if grid[x][y] == '.':
        return True
    return False


def bfs():
    lst = []
    while land:
        x, y = land.pop()
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if isValid(nx, ny):
                cnt += 1
        if cnt >= 3:
            lst.append((x, y))
    return lst

delete_lst = bfs()
for x, y in delete_lst:
    grid[x][y] = '.'

x_lst, y_lst = [], []
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'X':
            x_lst.append(i)
            y_lst.append(j)

min_x = min(x_lst)
max_x = max(x_lst)
min_y = min(y_lst)
max_y = max(y_lst)
for i in range(min_x, max_x+1):
    print(''.join(grid[i][min_y:max_y+1]))
