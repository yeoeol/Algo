import sys
from collections import deque

input = sys.stdin.readline

queue = []
n = int(input().strip())
A = list(map(int, input().strip().split())) # 0:queue, 1:stack
B = list(map(int, input().strip().split()))
for i in range(n):
    if A[i] == 0:
        queue.append(B[i])
queue.reverse()

m = int(input().strip())
C = list(map(int, input().strip().split()))

queue = queue+C
print(*queue[:m])