n, m = map(int, input().split())
grid = [list(map(int, input())) for _ in range(n)]


def get_rectangle_sum(x1, y1, x2, y2):
    return (prefix_sum[x2][y2]
            - (prefix_sum[x2][y1-1] if y1>0 else 0)
            - (prefix_sum[x1-1][y2] if x1>0 else 0)
            + (prefix_sum[x1-1][y1-1] if x1>0 and y1>0 else 0))


def get_prefix_sum(arr):
    prefix = [[0]*m for _ in range(n)]
    prefix[0][0] = grid[0][0]
    for i in range(1, n):
        prefix[i][0] = prefix[i-1][0]+arr[i][0]
    for j in range(1, m):
        prefix[0][j] = prefix[0][j-1]+arr[0][j]
    for i in range(1, n):
        for j in range(1, m):
            prefix[i][j] = prefix[i-1][j]+prefix[i][j-1]-prefix[i-1][j-1]+arr[i][j]
    return prefix

prefix_sum = get_prefix_sum(grid)

res = -1
# 세로 3등분
for i in range(1, m-1):
    for j in range(i+1, m):
        left = get_rectangle_sum(0, 0, n - 1, i - 1)
        mid = get_rectangle_sum(0, i, n-1, j-1)
        right = get_rectangle_sum(0, j, n-1, m-1)
        res = max(res, left*mid*right)

# 가로 3등분
for i in range(1, n-1):
    for j in range(i+1, n):
        up = get_rectangle_sum(0, 0, i-1, m-1)
        mid = get_rectangle_sum(i, 0, j-1, m-1)
        down = get_rectangle_sum(j, 0, n-1, m-1)
        res = max(res, up*mid*down)

for j in range(1, m):
    for i in range(1, n):
        right = get_rectangle_sum(0, j, n-1, m-1)
        left_up = get_rectangle_sum(0, 0, i-1, j-1)
        left_down = get_rectangle_sum(i, 0, n-1, j-1)
        res = max(res, right*left_up*left_down)

for j in range(1, m):
    for i in range(1, n):
        left = get_rectangle_sum(0, 0, n-1, j-1)
        right_up = get_rectangle_sum(0, j, i-1, m-1)
        right_down = get_rectangle_sum(i, j, n-1, m-1)
        res = max(res, left*right_up*right_down)

for i in range(1, n):
    for j in range(1, m):
        up = get_rectangle_sum(0, 0, i-1, m-1)
        down_left = get_rectangle_sum(i, 0, n-1, j-1)
        down_right = get_rectangle_sum(i, j, n-1, m-1)
        res = max(res, up*down_left*down_right)

for i in range(1, n):
    for j in range(1, m):
        up_left = get_rectangle_sum(0, 0, i-1, j-1)
        up_right = get_rectangle_sum(0, j, i-1, m-1)
        down = get_rectangle_sum(i, 0, n-1, m-1)
        res = max(res, up_left*up_right*down)

print(res)