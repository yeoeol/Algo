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
    max_num = max(counter, key=counter.get)
    if counter[max_num] > t//2:
        print(max_num)
    else:
        print("SYJKGW")

