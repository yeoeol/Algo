import heapq
import sys
input = sys.stdin.readline
INF = 1e8

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
dist = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# print(graph)

def dij(start):
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        d, now_node = heapq.heappop(heap)
        if dist[now_node] < d:
            continue
        for next_node, wei in graph[now_node]:
            cost = wei + d
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(heap, (cost, next_node))


dij(K)
for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])