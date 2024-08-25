import bisect
from itertools import combinations

n, c = map(int, input().split())
wei = list(map(int, input().split()))

s1 = wei[:n//2]
s2 = wei[n//2:]
a, b = [], []

# 부분집합 합 만들기
for i in range(1, len(s1)+1):
    for j in combinations(s1, i):
        _sum = sum(j)
        if _sum <= c:
            a.append(_sum)
for i in range(1, len(s2)+1):
    for j in combinations(s2, i):
        _sum = sum(j)
        if _sum <= c:
            b.append(_sum)

b.sort()
cnt = 1
for i in a:
    cnt += bisect.bisect_right(b, c-i)
print(len(a)+len(b)+cnt)