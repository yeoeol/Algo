import sys

def input():
    return sys.stdin.readline().strip()

n, m, h = map(int, input().split())
grid = [[0]*(n+1) for _ in range(h+1)]

for _ in range(m):
    a, b = map(int, input().split())
    grid[a][b] = 1

# 사다리 타기 함수
def ladder():
    for i in range(1, n+1):
        y = i
        for x in range(1, h+1):
            # 양쪽 살피기
            if grid[x][y] == 1:
                y += 1
            elif y > 1 and grid[x][y-1] == 1:
                y -= 1
        if y != i:
            return False
    return True

def dfs(start_x, start_y, depth, max_depth):
    if depth == max_depth:
        if ladder():
            print(depth)
            exit()
        return

    for x in range(start_x, h+1):
        y_range = range(1, n) if x != start_x else range(start_y, n)
        for y in y_range:
            if grid[x][y] == 0 and grid[x][y-1] == 0 and grid[x][y+1] == 0:
                grid[x][y] = 1
                dfs(x, y + 2, depth + 1, max_depth)
                grid[x][y] = 0

for i in range(4):
    dfs(1, 1, 0, i)
print(-1)