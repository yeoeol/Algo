import heapq

n, m = map(int, input().split())
c = list(map(int, input().split()))
w = list(map(int, input().split()))

hq = []
for i in range(n):
    heapq.heappush(hq, -c[i])

for i in range(m):
    p = -heapq.heappop(hq)
    if p < w[i]:
        print(0)
        exit()
    p -= w[i]
    heapq.heappush(hq, -p)

print(1)