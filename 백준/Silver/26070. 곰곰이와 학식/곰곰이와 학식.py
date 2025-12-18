# 치킨 3장 -> 피자 1장
# 피자 3장 -> 햄버거 1장
# 햄버거 3장 -> 치킨 1장
want = list(map(int, input().split()))
have = list(map(int, input().split()))

ans = 0
# 1장으로 먹일 수 있는 만큼 먹이기
while True:
    if all(want[i] == 0 for i in range(3)):
        break
    if all(have[i] < 3 for i in range(3)):
        for i in range(3):
            ans += min(want[i], have[i])
        break
    for i in range(3):
        if want[i] > have[i]:
            ans += have[i]
            want[i] -= have[i]
            have[i] = 0
        elif want[i] == have[i]:
            ans += have[i]
            want[i], have[i] = 0, 0
        else:
            ans += want[i]
            have[i] -= want[i]
            want[i] = 0
    # 식권 돌리기
    for i in range(3):
        if have[i] >= 3:
            j = (i+1)%3
            have[j] += have[i]//3
            have[i] = have[i]%3
            break
print(ans)