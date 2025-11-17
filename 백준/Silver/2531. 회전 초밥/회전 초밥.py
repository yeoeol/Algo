import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


n, d, k, c = map(int, input().split())
queue = [int(input()) for _ in range(n)]

dic = defaultdict(int)
for i in range(k):
    dic[queue[i]] += 1
dic[c] += 1
max_val = len(dic)

i, j = 0, k-1
for _ in range(n):
    dic[queue[i]] -= 1
    if dic[queue[i]] == 0: del dic[queue[i]]
    i += 1
    j = (j+1)%n
    dic[queue[j]] += 1
    max_val = max(max_val, len(dic))

print(max_val)