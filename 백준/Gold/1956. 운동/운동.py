import sys

INF = 1e8

V, E = map(int, input().split())

graph = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

def floyd():
    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])


floyd()
result = INF
for i in range(1, V+1):
    if graph[i][i] != INF:
        result = min(graph[i][i], result)

if result == INF:
    print(-1)
else:
    print(result)