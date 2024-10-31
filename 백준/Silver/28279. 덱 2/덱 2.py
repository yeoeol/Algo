import sys
from collections import deque

input = sys.stdin.readline
deque = deque()

n = int(input().strip())
for i in range(n):
    order = list(map(int, input().strip().split()))
    o = order[0]
    if o == 1:
        deque.appendleft(order[1])
    elif o == 2:
        deque.append(order[1])
    elif o == 3:
        print(deque.popleft()) if deque else print(-1)
    elif o == 4:
        print(deque.pop()) if deque else print(-1)
    elif o == 5:
        print(len(deque))
    elif o == 6:
        print(0) if deque else print(1)
    elif o == 7:
        print(deque[0]) if deque else print(-1)
    elif o == 8:
        print(deque[-1]) if deque else print(-1)

