import sys
sys.setrecursionlimit(150000)

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))


def dfs(s):
    for next_node, cost in graph[s]:
        if dist[next_node] == -1:
            dist[next_node] = dist[s] + cost
            dfs(next_node)

dist = [-1] * (n+1)
dist[1] = 0
dfs(1)
node = dist.index(max(dist))

dist = [-1] * (n+1)
dist[node] = 0
dfs(node)
print(max(dist))