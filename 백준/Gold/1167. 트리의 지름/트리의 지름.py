import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)

V = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(V):
    l = list(map(int, input().split()))
    cur_node = l[0]
    for i in range(1, len(l), 2):
        if l[i] == -1:
            break
        graph[cur_node].append((l[i], l[i+1]))

def func2(start):
    visited[start] = True
    for next_node, wei in graph[start]:
        if not visited[next_node]:
            dist[next_node] = dist[start] + wei
            func2(next_node)
    visited[start] = False

visited = [False] * (V+1)
dist = [0] * (V+1)
func2(1)

node = dist.index(max(dist))
M = dist[node]
dist = [0] * (V+1)
func2(node)
print(max(max(dist), M))
