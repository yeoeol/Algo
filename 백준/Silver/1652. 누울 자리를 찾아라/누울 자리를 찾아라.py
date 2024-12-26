n = int(input())
room = []
for _ in range(n):
    s = input()
    room.append(s)

width, height = 0, 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if room[i][j] == '.':
            cnt += 1
        if room[i][j] == 'X':
            if cnt >= 2:
                width += 1
            cnt = 0
    if cnt >= 2:
        width += 1

for j in range(n):
    cnt = 0
    for i in range(n):
        if room[i][j] == '.':
            cnt += 1
        if room[i][j] == 'X':
            if cnt >= 2:
                height += 1
            cnt = 0
    if cnt >= 2:
        height += 1

print(width, height)