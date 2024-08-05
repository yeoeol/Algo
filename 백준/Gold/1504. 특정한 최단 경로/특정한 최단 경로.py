import heapq
import sys
input = sys.stdin.readline
INF = 1e8

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# 시작 지점에서 v1까지 가기 + v1에서 v2까지 가기 + v2에서 N까지 가기
# 시작 지점에서 v2까지 가기 + v2에서 v1까지 가기 + v1에서 N까지 가기
def dij(start):
    dist = [INF] * (V+1)
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
    return dist
l1 = dij(1)
l2 = dij(v1)
l3 = dij(v2)
m_value = min(l1[v1]+l2[v2]+l3[V], l1[v2]+l3[v1]+l2[V])
if m_value >= INF:
    print(-1)
else:
    print(m_value)
