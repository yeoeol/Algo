INF = 1e8

n, m = map(int, input().split())

graph = []
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a,b,c))

def bellman(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur_node, next_node, cost = graph[j]
            if dist[cur_node] != INF and dist[next_node] > dist[cur_node] + cost:
                dist[next_node] = dist[cur_node] + cost
                if i == n-1:
                    return False
    return True

if bellman(1):
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
else:
    print(-1)