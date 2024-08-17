import sys
from collections import deque

input = sys.stdin.readline
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

land = []
def bfs(i, j, cnt):
    queue = deque([(i, j)])
    visited[i][j] = cnt
    land.append((i, j, cnt))
    while queue:
        px, py = queue.popleft()
        for i in range(4):
            mx, my = px+d[i][0], py+d[i][1]
            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue
            if graph[mx][my] == 1 and visited[mx][my] == -1:
                visited[mx][my] = cnt
                queue.append((mx, my))
                land.append((mx, my, cnt))

n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

c = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == -1:
            bfs(i, j, c)
            c += 1

# 다리 제작
edge = []
for x, y, cnt in land:
    for dx, dy in d:
        dist = 0
        mx, my = x+dx, y+dy
        while True:
            if mx < 0 or mx >= n or my < 0 or my >= m:
                break
            toLand = visited[mx][my]
            if cnt == toLand:
                break
            if toLand == -1:
                mx += dx; my += dy
                dist += 1
                continue
            if dist < 2:
                break
            edge.append((dist, cnt, toLand))
            break

edge.sort()
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

total = 0
cnt = 0
parent = [i for i in range(c)]
for cost, a, b in edge:
    if find(a) != find(b):
        union(a, b)
        total += cost
        cnt += 1
if cnt == c-1:
    print(total)
else:
    print(-1)
