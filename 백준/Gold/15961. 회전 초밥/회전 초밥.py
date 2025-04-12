import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

cnt = defaultdict(int)

for i in range(k):
    cnt[arr[i]] += 1

max_kind = len(cnt) + (1 if c not in cnt else 0)
for i in range(1, n):
    left = arr[i-1]
    cnt[left] -= 1
    if cnt[left] == 0:
        cnt.pop(left)

    right = arr[(i+k-1)%n]
    cnt[right] += 1
    curr_kind = len(cnt) + (1 if c not in cnt else 0)
    max_kind = max(max_kind, curr_kind)

print(max_kind)
