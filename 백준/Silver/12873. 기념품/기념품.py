import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

n = int(input())
arr = deque([i for i in range(1, n+1)])

cnt = 0
rnd = 1
while len(arr) != 1:
    arr.rotate(-rnd**3)
    arr.pop()
    rnd += 1

print(arr[0])