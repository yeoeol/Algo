import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().strip().split())
queue = list([i for i in range(1, n+1)])
ind = 0

print('<', end='')
while queue:
    ind = (ind+k-1)%len(queue)
    p = queue.pop(ind)
    if len(queue) != 0:
        print(p, end=', ')
    else:
        print(p, end='')
print('>')
