from collections import deque

n, k = map(int, input().split())
durability = deque(list(map(int, input().split())))
robots = deque([False] * (2 * n))

zero_cnt = 0
res = 0

up = 0
down = n-1
while True:
    durability.rotate(1)
    robots.rotate(1)
    robots[down] = False

    for i in range(n-2, -1, -1):
        if robots[i] and not robots[i+1] and durability[i+1] > 0:
            robots[i] = False
            robots[i+1] = True
            durability[i+1] -= 1
            if durability[i+1] == 0:
                zero_cnt += 1
    robots[down] = False

    if not robots[up] and durability[up] > 0:
        robots[up] = True
        durability[up] -= 1
        if durability[up] == 0:
            zero_cnt += 1

    res += 1
    if zero_cnt >= k:
        print(res)
        break

