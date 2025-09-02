import heapq
import sys


def input():
    return sys.stdin.readline().strip()

INF = sys.maxsize

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

cnt = 1
while True:
    n = int(input())
    if n == 0:
        break

    grid = [list(map(int, input().split())) for _ in range(n)]
    hq = []
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = grid[0][0]
    heapq.heappush(hq, (grid[0][0], 0, 0))

    while hq:
        distance, x, y = heapq.heappop(hq)
        if x == n-1 and y == n-1:
            print(f"Problem {cnt}: {distance}")
            cnt += 1
            break

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny):
                cost = distance + grid[nx][ny]
                if dist[nx][ny] > cost:
                    dist[nx][ny] = distance + grid[nx][ny]
                    heapq.heappush(hq, (dist[nx][ny], nx, ny))
