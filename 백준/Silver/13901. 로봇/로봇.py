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


while True:
    is_moved = False
    
    for i in range(len(arr)):
        dx, dy = d[arr[i]-1]
        while True:
            nx, ny = x+dx, y+dy
            if not in_range(nx, ny):
                break
            if grid[nx][ny]:
                break
            is_moved = True
            grid[nx][ny] = True
            x, y = nx, ny
            
    if not is_moved:
        break
print(x, y)
