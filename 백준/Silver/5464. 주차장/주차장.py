from collections import deque

queue = deque()
n, m = map(int, input().split())

charge = [int(input()) for _ in range(n)]   # 주차 공간들의 단위 무게당 요금
car_weight = [0]+[int(input()) for _ in range(m)]   # 1번 차량(idx=1)부터 차량의 무게
parking = [0] * n

answer = 0


def find_parking():
    for i in range(len(parking)):
        if parking[i] == 0:
            return i
    return -1

waiting = deque()
for _ in range(2*m):    # 주차장 출입 순서
    car_num = int(input())
    idx = find_parking()
    if car_num > 0:
        if idx == -1:
            waiting.append(car_num)
            continue
        else:
            parking[idx] = car_num
    else:
        out_idx = parking.index(-car_num)
        parking[out_idx] = 0
        answer += car_weight[-car_num]*charge[out_idx]
        if waiting:
            p = waiting.popleft()
            parking[out_idx] = p

print(answer)