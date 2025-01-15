def get_distance(x, y):
    if x == 1:  # 북
        return y
    if x == 2:  # 남
        return garo + sero + garo - y
    if x == 3:  # 서
        return garo + sero + garo + sero - y
    if x == 4:  # 동
        return garo + y

garo, sero = map(int, input().split()) # 블록의 x최대 좌표, y최대 좌표
n = int(input()) # 상점의 개수

store = []
for _ in range(n+1):
    b, loc = map(int, input().split())
    store.append(get_distance(b, loc))

total = 0
for i in range(n):
    in_course = abs(store[-1]-store[i])
    out_course = (garo+sero)*2 - in_course
    total += min(in_course, out_course)
print(total)