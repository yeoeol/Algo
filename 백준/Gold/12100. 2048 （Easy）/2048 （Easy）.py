n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def compress_and_merge(line):
    new_line = [x for x in line if x != 0]

    merged = []
    skip = False
    for i in range(len(new_line)):
        if skip:
            skip = False
            continue
        if i+1 < len(new_line) and new_line[i] == new_line[i+1]:
            merged.append(new_line[i]*2)
            skip = True
        else:
            merged.append(new_line[i])

    while len(merged) < len(line):
        merged.append(0)

    return merged

def move(g, d):
    new_grid = [row[:] for row in g]
    # 위로 밀기
    if d == 0:
        for j, sero in enumerate(zip(*g)):
            arr = compress_and_merge(sero)
            for x in range(n):
                new_grid[x][j] = arr[x]
    # 아래로 밀기
    elif d == 1:
        for j, sero in enumerate(zip(*g)):
            sero = list(reversed(sero))
            arr = compress_and_merge(sero)
            for x in range(n):
                new_grid[n - x - 1][j] = arr[x]
    # 왼쪽으로 밀기
    elif d == 2:
        for i, garo in enumerate(g):
            arr = compress_and_merge(garo)
            for y in range(n):
                new_grid[i][y] = arr[y]
    # 오른쪽으로 밀기
    else:
        for i, garo in enumerate(g):
            garo = list(reversed(garo))
            arr = compress_and_merge(garo)
            for y in range(n):
                new_grid[i][n - y - 1] = arr[y]

    return new_grid


def max_value(grid):
    max_val = -1
    for line in grid:
         max_val = max(max_val, max(line))
    return max_val


def dfs(grid, cnt):
    if cnt == 5:
        return max_value(grid)

    res = 0
    for i in range(4):
        new_grid = move(grid, i)
        res = max(res, dfs(new_grid, cnt+1))

    return res

print(dfs(board, 0))