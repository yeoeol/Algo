import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    n = int(input())
    arr = deque(input().split())
    res = deque()
    res.append(arr.popleft())
    while arr:
        p = arr.popleft()
        if res[0] < p:
            res.append(p)
        else:
            res.appendleft(p)

    print(*res, sep='')