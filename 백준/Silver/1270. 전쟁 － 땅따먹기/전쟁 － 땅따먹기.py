import sys
from collections import Counter


def input():
    return sys.stdin.readline().strip()

n = int(input())
for _ in range(n):
    lst = list(map(int, input().split()))
    t = lst[0]
    arr = lst[1:]
    counter = Counter(arr)
    for k, v in counter.items():
        if v > t//2:
            print(k)
            break
    else:
        print("SYJKGW")