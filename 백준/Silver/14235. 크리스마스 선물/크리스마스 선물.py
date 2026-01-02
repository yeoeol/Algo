from heapq import heappush, heappop


n = int(input())
queue = []
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if queue:
            print(-heappop(queue))
        else:
            print(-1)
    else:
        for i in a[1:]:
            heappush(queue, -i)
