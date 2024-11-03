from collections import deque

def right(idx, d):
    if idx > 3:
        return
    if wheel[idx-1][2] != wheel[idx][6]:
        right(idx+1, -d)
        wheel[idx].rotate(d)

def left(idx, d):
    if idx < 0:
        return
    if wheel[idx][2] != wheel[idx+1][6]:
        left(idx-1, -d)
        wheel[idx].rotate(d)


wheel = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())

for i in range(k):
    num, direction = map(int, input().split())
    num -= 1
    right(num+1, -direction)
    left(num-1, -direction)

    wheel[num].rotate(direction)




total = 0
for i in range(len(wheel)):
    if wheel[i][0] == 0:
        continue
    if i == 0:
        total += 1
    elif i == 1:
        total += 2
    elif i == 2:
        total += 4
    else:
        total += 8

print(total)