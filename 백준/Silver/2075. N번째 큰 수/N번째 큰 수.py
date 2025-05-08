import heapq
import sys

def input(): return sys.stdin.readline().strip()

n = int(input())
queue = list(map(int, input().split()))
for _ in range(n-1):
    for num in map(int, input().split()):
        if queue[0] < num:
            heapq.heappushpop(queue, num)

print(queue[0])