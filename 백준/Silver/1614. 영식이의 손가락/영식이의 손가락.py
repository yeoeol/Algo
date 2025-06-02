hurt = int(input())
cnt = int(input())

answer = 0
hurt_cnt = 0

if hurt == 1:
    if cnt == 0:
        answer += hurt - 1
    else:
        answer += 8 * cnt
elif hurt == 5:
    if cnt == 0:
        answer += hurt - 1
    else:
        answer += 4 + 8*(cnt)
else:   # 2, 3, 4
    if cnt == 0:
        answer += hurt - 1
    else:
        answer += 4 * (cnt) + 1
        if cnt % 2 == 0:
            answer += hurt - 2
        else:
            answer += 4 - hurt

print(answer)