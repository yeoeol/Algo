n, m, r = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def one():
    global grid
    new_grid = []
    for i in range(len(grid)-1, -1, -1):
        new_grid.append(grid[i])
    grid = new_grid

def two():
    global grid
    for g in grid:
        g.reverse()

def three():
    global grid
    new_grid = []
    for g in zip(*grid):
        new_grid.append(list(g))
    grid = new_grid
    two()

def four():
    for _ in range(3): three()

def five():
    n = len(grid)
    m = len(grid[0])
    half_n = len(grid)//2
    half_m = len(grid[0])//2

    # 1 -> temp
    temp = []
    for i in range(half_n):
        arr = []
        for j in range(half_m):
            arr.append(grid[i][j])
        temp.append(arr)

    # 4 -> 1
    for i in range(half_n):
        for j in range(half_m):
            grid[i][j] = grid[i+half_n][j]

    # 3 -> 4
    for i in range(half_n, n):
        for j in range(half_m):
            grid[i][j] = grid[i][j+half_m]

    # 2 -> 3
    for i in range(half_n, n):
        for j in range(half_m, m):
            grid[i][j] = grid[i-half_n][j]

    # temp(1) -> 2
    for i in range(half_n):
        for j in range(half_m, m):
            grid[i][j] = temp[i][j-half_m]

def six():
    for _ in range(3): five()

def func(order):
    if order == 1:
        one()
    elif order == 2:
        two()
    elif order == 3:
        three()
    elif order == 4:
        four()
    elif order == 5:
        five()
    else:
        six()

orders = list(map(int, input().split()))
for order in orders:
    func(order)
for g in grid:
    print(*g)
