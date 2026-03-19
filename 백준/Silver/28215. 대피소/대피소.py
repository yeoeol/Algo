import itertools
import sys

n, k = map(int, input().split())

home = [tuple(map(int, input().split())) for _ in range(n)]

# home에서 k개를 combinations로 선택
def dist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

ans = sys.maxsize
for lst in itertools.combinations(home, k):
    res = dict()
    for x, y in home:
        if (x, y) not in lst:
            for lx, ly in lst:
                if (x, y) not in res:
                    res[(x, y)] = dist(x, y, lx, ly)
                else:
                    res[(x, y)] = min(res[(x, y)], dist(x, y, lx, ly))
    ans = min(ans, max(res.values()))

print(ans)