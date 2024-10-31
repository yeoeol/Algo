import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
lst = deque([i for i in range(1, n+1)])
arr = list(map(int, input().strip().split()))

ind = 0
p = lst.popleft()
print(p, end=' ')
while lst:
    if arr[p-1] >= 0:
        for i in range(arr[p-1]-1):
            lst.append(lst.popleft())
        p = lst.popleft()
    elif arr[p-1] < 0:
        for i in range(abs(arr[p-1])-1):
            lst.appendleft(lst.pop())
        p = lst.pop()
    print(p, end=' ')
