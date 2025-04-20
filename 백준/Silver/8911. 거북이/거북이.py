import sys

def input():
    return sys.stdin.readline().strip()

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

t = int(input())
for _ in range(t):
    x, y = 0, 0 # 초기 위치
    d = 0 # 초기에는 북쪽 바라보고 있음

    min_x, max_x = x, x
    min_y, max_y = y, y
    xlst, ylst = [x], [y]

    orders = input()
    for order in orders:
        if order == 'F':
            x += dxs[d]
            y += dys[d]
        elif order == 'B':
            x -= dxs[d]
            y -= dys[d]
        elif order == 'L':
            d = (d+3) % 4
        else:
            d = (d+1) % 4

        min_x, max_x = min(x, min_x), max(x, max_x)
        min_y, max_y = min(y, min_y), max(y, max_y)

    print((max_x-min_x) * (max_y-min_y))
