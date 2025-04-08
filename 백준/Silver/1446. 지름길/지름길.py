import heapq
import sys
from collections import defaultdict

INF = sys.maxsize

n, d = map(int, input().split())
graph = defaultdict(list)

distance = [INF] * (d+1)
distance[0] = 0

for _ in range(n):
    start, end, cost = map(int, input().split())
    if end <= d and end-start > cost:
        graph[start].append((end, cost))

hq = []
heapq.heappush(hq, (0, 0))
def dijkstra():
    while hq:
        dist, now = heapq.heappop(hq)

        if dist > distance[now]:
            continue

        # 1칸 앞으로
        if now+1 <= d and distance[now+1] > dist+1:
            distance[now+1] = dist+1
            heapq.heappush(hq, (dist+1, now+1))

        # 지름길
        for end, cost in graph[now]:
            new_dist = dist+cost
            if end <= d and new_dist < distance[end]:
                distance[end] = new_dist
                heapq.heappush(hq, (new_dist, end))

dijkstra()
print(distance[d])