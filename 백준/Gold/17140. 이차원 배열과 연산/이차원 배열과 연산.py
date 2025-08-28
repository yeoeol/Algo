import sys
from collections import Counter


def input():
    return sys.stdin.readline().strip()

r, c, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(3)]

def R():
    new_arr = []
    max_len = -1
    for arr in grid:
        new = my_sort(arr)
        new_arr.append(new)
        max_len = max(max_len, len(new))

    for a in new_arr:
        if len(a) != max_len:
            for _ in range(max_len-len(a)):
                a.append(0)

    return new_arr

def C():
    new_arr = []
    max_len = -1
    for arr in zip(*grid):
        new = my_sort(arr)
        new_arr.append(new)
        max_len = max(max_len, len(new))

    nnew_arr = []
    for i in range(max_len):
        col = []
        for row in new_arr:
            if i < len(row):
                col.append(row[i])
            else:
                col.append(0)
        nnew_arr.append(col)

    return nnew_arr




def my_sort(arr):
    new_arr = []
    cnt = Counter(arr).items()
    for x, y in sorted(cnt, key=lambda x:(x[1], x[0])):
        if x != 0:
            new_arr.append(x)
            new_arr.append(y)
    return new_arr


t = 0
r, c = r-1, c-1
while True:
    row_cnt = len(grid)
    col_cnt = len(grid[0])

    if r < row_cnt and c < col_cnt:
        if grid[r][c] == k:
            print(t)
            break
    t += 1
    if t > 100:
        print(-1)
        break

    if row_cnt >= col_cnt:
        grid = R()
    else:
        grid = C()

