from itertools import permutations

n = int(input())
basic = list(permutations(list(range(1, 10)), 3))

for _ in range(n):
    num, strike, ball = map(int, input().split())
    temp = list()

    for check in basic:
        s_cnt, b_cnt = 0, 0

        for strike_idx, strike_num in enumerate(str(num)):
            strike_num = int(strike_num)
            if check[strike_idx] == strike_num:
                s_cnt += 1
            if check[strike_idx] != strike_num and strike_num in check:
                b_cnt += 1

        if s_cnt == strike and b_cnt == ball:
            temp.append(check)
    basic = temp

print(len(basic))