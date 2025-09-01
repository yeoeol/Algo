import itertools
import sys

n = int(input())
materials = [tuple(map(int, input().split()))for _ in range(n)]

res = sys.maxsize
for i in range(1, n+1):
    for comb in itertools.combinations(materials, i):
        pro_s, sum_b = 1, 0
        for s, b in comb:
            pro_s *= s
            sum_b += b
        res = min(res, abs(pro_s-sum_b))
print(res)