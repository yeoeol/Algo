import sys

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())

trains = [[0]*21 for _ in range(n+1)]

def exec_order(orders):
    order = orders[0]
    num = orders[1]
    if order == 1:
        x = orders[2]
        if trains[num][x] == 0:
            trains[num][x] = 1
    elif order == 2:
        x = orders[2]
        trains[num][x] = 0
    elif order == 3:
        for i in range(20, 1, -1):
            trains[num][i] = trains[num][i-1]
        trains[num][1] = 0
    elif order == 4:
        for i in range(1, 20):
            trains[num][i] = trains[num][i+1]
        trains[num][20] = 0

for _ in range(m):
    orders = list(map(int, input().split()))
    exec_order(orders)

trains.sort()

res = 0
j = 2
i = 1
while i <= n:
    res += 1
    while j <= n and trains[i] == trains[j]:
        j += 1
        continue
    i = j
    j += 1
print(res)
