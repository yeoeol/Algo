import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()

n = int(input())
cnt = defaultdict(int)

for _ in range(n):
    cnt[int(input())] += 1

max_val = max(cnt.values())
candi = []
for k, v in cnt.items():
    if v == max_val:
        candi.append(k)

print(min(candi))