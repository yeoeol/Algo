def check():
    tmp = 0
    # 가로
    for x in bingo:
        if x.count(0) == 5:
            tmp += 1
    # 세로
    for i in range(5):
        ycnt = 0
        for j in range(5):
            if bingo[j][i] == 0:
                ycnt += 1
        if ycnt == 5:
            tmp += 1
    # 왼쪽 위 시작 대각선
    d1 = 0
    for i in range(5):
        if bingo[i][i] == 0:
            d1 += 1
    if d1 == 5:
        tmp += 1
    # 오른쪽 위 시작 대각선
    d2 = 0
    for i in range(5):
        if bingo[i][4-i] == 0:
            d2 += 1
    if d2 == 5:
        tmp += 1

    return tmp

bingo = [list(map(int, input().split())) for _ in range(5)]
call=[]
for _ in range(5):
    call += map(int,input().split())

cnt = 0
for k in range(25):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == call[k]:
                bingo[i][j] = 0
                cnt += 1
                break
    if cnt >= 12:
        t = check()
        if t >= 3:
            print(k+1)
            break

