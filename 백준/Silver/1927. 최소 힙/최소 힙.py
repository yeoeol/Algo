import heapq
import sys

def input(): return sys.stdin.readline().strip()

n = int(input())
queue = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if queue:
            print(heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, num)

