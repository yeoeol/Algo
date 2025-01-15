garo, sero = map(int, input().split()) # 블록의 x최대 좌표, y최대 좌표
n = int(input()) # 상점의 개수

store = {}
for i in range(1, 5):
    store[i] = []
for _ in range(n):
    b, loc = tuple(map(int, input().split()))
    store[b].append(loc)

cur_b, cur_loc = map(int, input().split())
total = 0

for i in range(1, 5):
    lst = store[i]
    for j in lst:
        if cur_b == 1:
            if i == 1:
                total += abs(j-cur_loc)
            elif i == 2:
                total += min((garo-cur_loc+garo-j), (cur_loc+j))
                total += sero
            elif i == 3:
                total += cur_loc+j
            elif i == 4:
                total += garo-cur_loc+j
        elif cur_b == 2:
            if i == 1:
                total += min((garo-cur_loc+garo-j), (cur_loc+j))
                total += sero
            elif i == 2:
                total += abs(j-cur_loc)
            elif i == 3:
                total += cur_loc+sero-j
            elif i == 4:
                total += garo-cur_loc+sero-j
        elif cur_b == 3:
            if i == 1:
                total += cur_loc+j
            elif i == 2:
                total += sero-cur_loc+j
            elif i == 3:
                total += abs(j-cur_loc)
            elif i == 4:
                total += min((sero-cur_loc+sero-j), (cur_loc+j))
                total += garo
        elif cur_b == 4:
            if i == 1:
                total += cur_loc+garo-j
            elif i == 2:
                total += sero-cur_loc+garo-j
            elif i == 3:
                total += min((sero-cur_loc+sero-j), (cur_loc+j))
                total += garo
            elif i == 4:
                total += abs(cur_loc-j)
print(total)