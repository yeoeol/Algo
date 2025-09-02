import heapq
import sys


def input():
    return sys.stdin.readline().strip()

INF = sys.maxsize

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

s, e = map(int, input().split())

dist = [INF]*(n+1)
prev = [-1]*(n+1)

def dijk():
    hq = []
    dist[s] = 0
    heapq.heappush(hq, (0, s))

    while hq:
        distance, x = heapq.heappop(hq)
        if x == e:
            break

        for next, wei in graph[x]:
            cost = distance + wei
            if dist[next] > cost:
                dist[next] = cost
                prev[next] = x
                heapq.heappush(hq, (cost, next))

dijk()
route = []
cur = e
while cur != -1:
    route.append(cur)
    cur = prev[cur]
route.reverse()

print(dist[e])
print(len(route))
print(*route)
