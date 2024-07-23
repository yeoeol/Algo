n, m = map(int, input().split())

graph = []
dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]

for _ in range(n):
    graph.append(list(map(int, list(input()))))

visited = [[False for _ in range(m)] for _ in range(n)]

def bfs(x, y):
    q = [(x, y)]
    visited[x][y] = True
    while q:
        x, y = q.pop(0)
        for k in range(4):
            mx, my = x+dir[k][0], y+dir[k][1]
            if mx < 0 or mx >= n or my < 0 or my >= m:
                continue
            if graph[mx][my] == 1 and not visited[mx][my]:
                visited[mx][my] = True
                graph[mx][my] += graph[x][y]
                q.append((mx, my))
            if mx == n and my == m:
                break

bfs(0, 0)
# for i in range(n):
#     print(graph[i])
print(graph[n-1][m-1])
