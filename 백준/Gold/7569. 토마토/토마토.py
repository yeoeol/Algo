from collections import deque

m, n, h = map(int, input().split())

graph = []
for _ in range(h):
    l = [list(map(int, input().split())) for _ in range(n)]
    graph.append(l)


tomato = deque()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                tomato.append((k, i, j))

d = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)] # 상하좌우, 윗칸아랫칸

def bfs():
    while tomato:
        k, i, j = tomato.popleft()
        for dir in range(6):
            mk, mi, mj = k+d[dir][0], i+d[dir][1], j+d[dir][2]
            if mk < 0 or mk >= h or mi < 0 or mi >= n or mj < 0 or mj >= m:
                continue
            if graph[mk][mi][mj] == 0:
                graph[mk][mi][mj] = graph[k][i][j] + 1
                tomato.append((mk, mi, mj))

M = 0
bfs()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0:
                print(-1)
                exit(0)
            M = max(M, graph[k][i][j])

print(M-1)