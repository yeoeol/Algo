import sys
from collections import deque, defaultdict


def input():
    return sys.stdin.readline().strip()


n, d, k, c = map(int, input().split())
queue = []
for _ in range(n):
    queue.append(int(input()))

dic = defaultdict(int)
for i in range(k):
    dic[queue[i]] += 1
max_val = len(dic)

i = 0
j = k-1
while i < n:
    if dic[queue[i]] != 0:
        dic[queue[i]] -= 1
        if dic[queue[i]] == 0:
            del dic[queue[i]]
    i += 1
    j = (j+1)%n
    dic[queue[j]] += 1
    temp = set(dic.keys())
    temp.add(c)
    max_val = max(max_val, len(temp))

print(max_val)