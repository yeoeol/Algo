import heapq
import sys

def input(): return sys.stdin.readline().strip()

n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewels.sort()
bags.sort()

ans = 0
hq = []
jewel_idx = 0

# 최소 가방을 꺼냈을 때 넣을 수 있는 보석 중 가격이 가장 큰 것
for bag_w in bags:
    while jewel_idx < n and jewels[jewel_idx][0] <= bag_w:
        heapq.heappush(hq, -jewels[jewel_idx][1])
        jewel_idx += 1

    if hq:
        ans += -heapq.heappop(hq)

print(ans)