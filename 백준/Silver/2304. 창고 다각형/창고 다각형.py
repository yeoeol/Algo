n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort()

area = 0
i = idx = 0
for l in points:
    if l[1] > area:
        area = l[1]
        idx = i
    i += 1

left_max_height = points[0][1]
for i in range(idx):
    if points[i+1][1] > left_max_height:
        area += left_max_height * (points[i + 1][0] - points[i][0])
        left_max_height = points[i+1][1]
    else:
        area += left_max_height * (points[i + 1][0] - points[i][0])

right_max_height = points[-1][1]
for i in range(n-1, idx, -1):
    if points[i-1][1] > right_max_height:
        area += right_max_height * (points[i][0]-points[i-1][0])
        right_max_height = points[i-1][1]
    else:
        area += right_max_height * (points[i][0]-points[i-1][0])

print(area)
