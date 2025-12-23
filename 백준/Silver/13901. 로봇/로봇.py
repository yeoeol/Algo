import sys


def input():
    return sys.stdin.readline().strip()

r, c = map(int, input().split())
grid = [[False]*c for _ in range(r)]

k = int(input())
for _ in range(k):
    br, bc = map(int, input().split())
    grid[br][bc] = True
x, y = map(int, input().split())
arr = list(map(int, input().split()))

grid[x][y] = True

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def is_possible(x, y):
    sets = set(arr)
    for s in sets:
        dx, dy = d[s-1]
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and not grid[nx][ny]:
            return True
    return False


while True:
    if not is_possible(x, y):
        break
    for i in range(len(arr)):
        dx, dy = d[arr[i]-1]
        while True:
            nx, ny = x+dx, y+dy
            if not in_range(nx, ny):
                break
            if grid[nx][ny]:
                break
            grid[nx][ny] = True
            x, y = nx, ny

print(x, y)
