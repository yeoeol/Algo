import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
if n == 1:
    print(n)
    exit(0)
queue = deque([i for i in range(1, n+1)])

while len(queue) > 0:
    queue.popleft()
    if len(queue) == 1:
        break
    queue.append(queue.popleft())

print(queue[0])