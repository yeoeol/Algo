from itertools import combinations
import sys

def input():
    return sys.stdin.readline().strip()

n, k = map(int, input().split())

def dist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

home = [tuple(map(int, input().split())) for i in range(n)]

INF = sys.maxsize
ans = INF
for selected in combinations(home, k):
    cur = -1
    for i in range(n):
        cur_dist = INF
        for sx, sy in selected:
            cur_dist = min(cur_dist, dist(sx, sy, home[i][0], home[i][1]))
        cur = max(cur, cur_dist)
    ans = min(ans, cur)

print(ans)
