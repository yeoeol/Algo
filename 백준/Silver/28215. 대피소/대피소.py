import itertools
import sys

n, k = map(int, input().split())

def dist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

home = []
nums = dict()
for i in range(n):
    x, y = map(int, input().split())
    home.append((x, y))
    nums[(x, y)] = i

INF = sys.maxsize
ans = INF
for selected in itertools.combinations(home, k):
    sets = set(nums[(x, y)] for x, y in selected)
    arr = [INF] * n
    for i in range(n):
        if i in sets:
            continue
        for sx, sy in selected:
            arr[i] = min(arr[i], dist(sx, sy, home[i][0], home[i][1]))
    res = 0
    for i in range(n):
        if arr[i] != INF:
            res = max(arr[i], res)
    ans = min(ans, res)
print(ans)


