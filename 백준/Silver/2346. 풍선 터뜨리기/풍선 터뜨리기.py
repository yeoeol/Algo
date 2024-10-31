import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
lst = deque([i for i in range(1, n+1)])
arr = list(map(int, input().strip().split()))

ind = 0
while lst:
    p = lst.popleft()
    ind = arr[p-1]
    if ind >= 0:
        lst.rotate(-(ind-1))
    elif ind < 0:
        lst.rotate(-ind)
    print(p, end=' ')
