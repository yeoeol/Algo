from collections import deque

t = int(input())
wheels = deque()
for _ in range(t):
    wheels.append(deque(list(input())))
# index가 2, 6 인 것만 신경쓰기


def rotate(wheels, num, d):
    left, right = wheels[num][6], wheels[num][2]
    wheels[num].rotate(d)
    if num-1 >= 0 and (wheels[num-1][2] == left) and num+1 < len(wheels) and (wheels[num+1][6] == right):
        return
    if num-1 >= 0 and (wheels[num-1][2] != left) and num+1 < len(wheels) and (wheels[num+1][6] != right):
        i, j = num-1, num+1
        d_left, d_right = d, d
        left_flag = False
        while i >= 0:
            d_left *= -1
            if i-1 >= 0 and wheels[i-1][2] == wheels[i][6]:
                left_flag = True
            wheels[i].rotate(d_left)
            if left_flag:
                break
            i -= 1
        right_flag = False
        while j < len(wheels):
            d_right *= -1
            if j+1 < len(wheels) and wheels[j][2] == wheels[j+1][6]:
                right_flag = True
            wheels[j].rotate(d_right)
            if right_flag:
                break
            j += 1
    elif num-1 >= 0 and (wheels[num-1][2] != left):
        i, j = num-1, num+1
        d_left = d
        left_flag = False
        while i >= 0:
            d_left *= -1
            if i-1 >= 0 and wheels[i-1][2] == wheels[i][6]:
                left_flag = True
            wheels[i].rotate(d_left)
            if left_flag:
                break
            i -= 1
    elif num+1 < len(wheels)  and (wheels[num+1][6] != right):
        i, j = num-1, num+1
        d_right = d
        right_flag = False
        while j < len(wheels):
            d_right *= -1
            if j+1 < len(wheels) and wheels[j][2] == wheels[j+1][6]:
                right_flag = True
            wheels[j].rotate(d_right)
            if right_flag:
                break
            j += 1

k = int(input())
for _ in range(k):
    # d=1 : 시계, d=-1 : 반시계
    num, d = map(int, input().split())
    rotate(wheels, num-1, d)

ans = 0
for i in range(t):
    if wheels[i][0] == '1':
        ans += 1
print(ans)