import heapq
import sys

def input():
    return sys.stdin.readline().strip()


n, k = map(int, input().split())
position = [[] for _ in range(12)]
for _ in range(n):
    pos, val = map(int, input().split())
    heapq.heappush(position[pos], -val)

select = [0] * 12
for _ in range(k):
    for i in range(1, 12):
        if position[i]:
            val = -heapq.heappop(position[i])
            val = max(0, val-1)
            heapq.heappush(position[i], -val)

res = 0
for i in range(1, 12):
    if position[i]:
        res += -heapq.heappop(position[i])

print(res)