import sys

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

def calc(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

dist_sum = 0
dist = []
# 각 인접 체크포인트끼리 거리 계산
for i in range(1, n):
    x1, y1 = arr[i-1]
    x2, y2 = arr[i]
    d = calc(x1, y1, x2, y2)
    dist.append((i-1, i, d))
    dist_sum += d
min_dist = sys.maxsize

# for문을 돌면서 점을 한번씩 건너뛰면서 거리 계산
for i in range(1, len(dist)-1):
    temp = dist_sum - dist[i-1][2] - dist[i][2]
    x1, y1 = arr[dist[i-1][0]]
    x2, y2 = arr[dist[i][1]]
    temp += calc(x1, y1, x2, y2)
    min_dist = min(min_dist, temp)
    
print(min_dist)

