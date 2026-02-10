import heapq
from collections import defaultdict
from heapq import heappush, heappop
import sys

def input():
    return sys.stdin.readline().strip()

t = int(input())


def solution(k):
    min_hq = []
    max_hq = []
    visited = [False] * (k+1)
    for i in range(k):
        order, num = input().split()
        if order == 'D':
            if num == '-1':
                while min_hq:
                    p_num, idx = heappop(min_hq)
                    if not visited[idx]:
                        visited[idx] = True
                        break
            elif num == '1':
                while max_hq:
                    p_num, idx = heappop(max_hq)
                    if not visited[idx]:
                        visited[idx] = True
                        break
        else:
            num = int(num)
            heappush(min_hq, (num, i))
            heappush(max_hq, (-num, i))

    ans = []
    while max_hq:
        p_num, idx = heappop(max_hq)
        if not visited[idx]:
            ans.append(-p_num)
            break
    while min_hq:
        p_num, idx = heappop(min_hq)
        if not visited[idx]:
            ans.append(p_num)
            break
    if ans:
        print(*ans)
    else:
        print("EMPTY")


for _ in range(t):
    k = int(input())
    solution(k)