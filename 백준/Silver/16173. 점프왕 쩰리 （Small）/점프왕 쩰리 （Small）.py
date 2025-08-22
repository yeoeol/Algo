import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        if grid[x][y] == -1:
            return True

        for dx, dy in [(0, 1), (1, 0)]:
            nx, ny = x+dx*grid[x][y], y+dy*grid[x][y]
            if in_range(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return False

can_reach = bfs(0, 0)

if can_reach:
    print("HaruHaru")
else:
    print("Hing")