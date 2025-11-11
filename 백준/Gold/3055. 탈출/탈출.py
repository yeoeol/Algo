import sys

def input():
    return sys.stdin.readline().strip()

r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
water = []
x, y = 0, 0

for i in range(r):
    for j in range(c):
        cur = grid[i][j]
        if cur == '*':
            water.append((i, j))
        elif cur == 'S':
            x, y = i, j

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 물, 고슴도치 순으로 확장
def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def bfs_water(water):
    visited = [[False]*c for _ in range(r)]
    new_water = []
    for x, y in water:
        visited[x][y] = True
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == '.':
                visited[nx][ny] = True
                grid[nx][ny] = '*'
                new_water.append((nx, ny))
    water.extend(new_water)

def move_hog():
    global _set

    new_set = set()
    for x, y, cnt in _set:
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny):
                if grid[nx][ny] == 'D':
                    return cnt+1
                elif grid[nx][ny] == '.':
                    new_set.add((nx, ny, cnt+1))
    _set = new_set
    return -1


_set = set()
while True:
    bfs_water(water)
    _set.add((x, y, 0))
    flag = move_hog()

    if flag != -1:
        print(flag)
        break
    else:
        if len(_set) == 0:
            print("KAKTUS")
            break