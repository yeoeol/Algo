import heapq
import sys

n, m, r = map(int, input().split())
items = [0]+list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

INF = sys.maxsize
def dijk(s):
    dist = [INF]*(n+1)
    dist[s] = 0
    hq = []
    heapq.heappush(hq, (0, s))

    while hq:
        distance, cur_node = heapq.heappop(hq)

        for next_node, wei in graph[cur_node]:
            cost = distance+wei
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(hq, (dist[next_node], next_node))
    return dist

res = -1
for i in range(1, n+1):
    dist = dijk(i)
    sum_cnt = 0
    for idx, cnt in enumerate(dist):
        if cnt <= m:
            sum_cnt += items[idx]
    res = max(res, sum_cnt)
print(res)
