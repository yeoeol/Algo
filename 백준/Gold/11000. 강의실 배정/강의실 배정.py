import sys
from heapq import heappush, heappop

def input():
    return sys.stdin.readline().strip()

n = int(input())

arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))
arr.sort()

cnt = 1
hq = [arr[0][1]]
for i in range(1, n):
    s, e = arr[i]
    if s < hq[0]:
        cnt += 1
    else:
        heappop(hq)
    heappush(hq, e)
print(cnt)