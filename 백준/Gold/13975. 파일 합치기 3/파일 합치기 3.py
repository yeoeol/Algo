import sys
from heapq import heappush, heappop, heapify

def input():
    return sys.stdin.readline().strip()


t = int(input())
answer = []
for _ in range(t):
    k = int(input())
    arr = list(map(int, input().split()))
    heapify(arr)

    res = 0
    while len(arr) > 1:
        p1 = heappop(arr)
        p2 = heappop(arr)

        res += p1 + p2
        heappush(arr, p1+p2)

    answer.append(res)

print(*answer, sep='\n')