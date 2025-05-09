import heapq
import sys

def input(): return sys.stdin.readline().strip()

t = int(input())
for _ in range(t):


    m = int(input())
    arr = []
    for _ in range(m//10+1):
        arr.extend(list(map(int, input().split())))

    cnt = 0
    res = []
    left_max_hq, right_min_hq = [], []
    for i in range(m):
        if not left_max_hq or -left_max_hq[0] >= arr[i]:
            heapq.heappush(left_max_hq, -arr[i])
        else:
            heapq.heappush(right_min_hq, arr[i])

        if len(left_max_hq) > len(right_min_hq)+1:
            heapq.heappush(right_min_hq, -heapq.heappop(left_max_hq))
        elif len(left_max_hq) < len(right_min_hq):
            heapq.heappush(left_max_hq, -heapq.heappop(right_min_hq))

        if i % 2 == 0:
            cnt += 1
            res.append(-left_max_hq[0])
    print(len(res))
    print(*res)
