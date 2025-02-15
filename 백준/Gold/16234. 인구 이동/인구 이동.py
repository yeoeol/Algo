import copy
from collections import deque

N, L, R = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(graph, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    uni = [(x, y)]
    while queue:
        px, py = queue.popleft()
        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if (L <= abs(graph[px][py]-graph[nx][ny]) <= R) and (not visited[nx][ny]):
                    uni.append((nx, ny))
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return uni


def sort_graph(graph, union):
    total = 0
    divisor = len(union)
    for ux, uy in union:
        total += graph[ux][uy]
    for ux, uy in union:
        graph[ux][uy] = total//divisor

time = 0
while True:
    visited = [[False]*N for _ in range(N)]
    temp = copy.deepcopy(graph)
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = bfs(graph, i, j, visited)
                sort_graph(graph, union)

    if temp == graph:
        print(time)
        break
    else:
        time += 1
