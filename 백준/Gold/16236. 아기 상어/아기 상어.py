import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()

n = int(input())

grid = []
bx, by = 0, 0
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 9:
            bx, by = i, j
    grid.append(arr)

def find_edible_fishes(x, y, baby_size):
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True

    queue = deque([(x, y, 0)])
    min_dist = float('inf')

    fishes = []
    while queue:
        x, y, dist = queue.popleft()
        if dist > min_dist:
            break

        if 0 < grid[x][y] < baby_size:
            fishes.append((dist, x, y))
            min_dist = dist
            continue

        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] <= baby_size:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1))

    return sorted(fishes)

grid[bx][by] = 0
res = 0
eat = 0
baby_size = 2
while True:
    edible_fishes = deque(find_edible_fishes(bx, by, baby_size))

    if len(edible_fishes) == 0:
        break
    else:
        t, bx, by = edible_fishes.popleft()
        fish_size = grid[bx][by]
        grid[bx][by] = 0
        res += t
        eat += 1
        if eat == baby_size:
            baby_size += 1
            eat = 0
print(res)