n = int(input())
grid = [[' ']*(n*2-1) for _ in range(n)]

def make_triangle(x, y):
    d = [(0, 0), (1, -1), (1, 1), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)]
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        grid[nx][ny] = '*'


def rec(x, y, depth):
    if depth == 3:
        make_triangle(x, y)
        return

    rec(x, y, depth//2)
    rec(x+depth//2, y+depth//2, depth//2)
    rec(x+depth//2, y-depth//2, depth//2)

rec(0, n-1, n)

for row in grid:
    print("".join(row))


