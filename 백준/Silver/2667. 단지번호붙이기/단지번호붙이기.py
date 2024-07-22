n = int(input())
graph = []

for _ in range(n):
    graph.append(input())

visited = [[False for _ in range(n)] for _ in range(n)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start):
    cnt = 1
    q = [start]
    x, y = start[0], start[1]
    visited[x][y] = True
    while q:
        p = q.pop(0)
        x, y = p[0], p[1]
        for i in range(4):
            mx, my = x+dir[i][0], y+dir[i][1]
            if mx < 0 or mx >= n or my < 0 or my >= n:
                continue
            if graph[mx][my] == '1' and not visited[mx][my]:
                cnt += 1
                q.append((mx, my))
                visited[mx][my] = True
    return cnt

result = 0
r = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visited[i][j]:
            result += 1
            r.append(bfs((i, j)))
print(result)
r.sort()
for i in range(result):
    print(r[i])