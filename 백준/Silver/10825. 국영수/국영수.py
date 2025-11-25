import sys


def input():
    return sys.stdin.readline().strip()

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
arr.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(n):
    print(arr[i][0])