import heapq
import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

res = 0
while len(arr) != 1:
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    res += (x+y)
    heapq.heappush(arr, x+y)

print(res)