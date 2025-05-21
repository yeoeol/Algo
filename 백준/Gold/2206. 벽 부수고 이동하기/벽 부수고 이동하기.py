import sys
from collections import deque

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

# 0은 이동 가능, 1은 이동 불가능
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y, visited):
    queue = deque([(x, y, 1, 0)])
    while queue:
        x, y, cnt, broken = queue.popleft()
        if x == n-1 and y == m-1:
            return cnt

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny):
                if not visited[nx][ny][broken] and grid[nx][ny] == '0':
                    queue.append((nx, ny, cnt+1, broken))
                    visited[nx][ny][broken] = True
                elif not visited[nx][ny][1] and broken == 0 and grid[nx][ny] == '1':
                    queue.append((nx, ny, cnt+1, 1))
                    visited[nx][ny][1] = True

    return sys.maxsize

visited = [[[False]*2 for _ in range(m)] for _ in range(n)]
cnt = bfs(0, 0, visited)

print(cnt if cnt != sys.maxsize else -1)

