grid = [list(map(int, list(input()))) for _ in range(9)]
blank = [
    (i, j)
    for i in range(9)
    for j in range(9)
    if grid[i][j] == 0
]

rows = [set(grid[i]) for i in range(9)]
cols = list(map(set, zip(*grid)))
boxes = [set() for _ in range(9)]
for i in range(9):
    for j in range(9):
        num = grid[i][j]
        box_idx = (i // 3) * 3 + (j // 3)
        boxes[box_idx].add(num)

def is_same_row_col(x, y, num):
    if num in rows[x]:
        return True
    if num in cols[y]:
        return True
    return False

def is_same_box(x, y, num):
    idx = (x//3)*3+(y//3)
    if num in boxes[idx]:
        return True
    return False

def is_valid(x, y, num):
    return not (is_same_row_col(x, y, num) or is_same_box(x, y, num))

def rec(start):
    if start == len(blank):
        for g in grid:
            print(*g, sep='')
        quit()

    x, y = blank[start]
    idx = (x//3)*3+(y//3)
    for j in range(1, 10):
        if is_valid(x, y, j):
            grid[x][y] = j
            rows[x].add(j)
            cols[y].add(j)
            boxes[idx].add(j)

            rec(start+1)

            grid[x][y] = 0
            rows[x].remove(j)
            cols[y].remove(j)
            boxes[idx].remove(j)

rec(0)

