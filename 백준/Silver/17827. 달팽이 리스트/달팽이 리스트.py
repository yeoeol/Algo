import sys


def input():
    return sys.stdin.readline().strip()

n, m, v = map(int, input().split())
lst = list(map(int, input().split()))
lst_part = lst[v-1:]
for _ in range(m):
    k = int(input())
    idx = 0
    if k >= n:
        k -= n
        idx = (idx + k)%len(lst_part)
        print(lst_part[idx])
    else:
        print(lst[k])
