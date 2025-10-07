import sys


def input():
    return sys.stdin.readline().strip()

n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort()

res = -1
for i in range(len(ropes)):
    res = max(res, ropes[i]*(n-i))

print(res)