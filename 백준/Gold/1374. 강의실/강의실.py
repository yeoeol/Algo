from heapq import heappush, heappop

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1], x[2]))

hq = []
for i in range(n):
    num, start, end = arr[i]
    if hq:
        e = hq[0]
        if start < e:
            heappush(hq, end)
        else:
            heappop(hq)
            heappush(hq, end)
    else:
        heappush(hq, end)
print(len(hq))