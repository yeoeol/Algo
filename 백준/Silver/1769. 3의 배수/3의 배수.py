x = input()
cnt = 0
_sum = 0
if len(x) == 1:
    _sum = int(x)
    print(0)
else:
    while True:
        x = list(map(int, list(x)))
        _sum = sum(x)
        cnt += 1
        y = str(_sum)
        if len(list(y)) == 1:
            break
        x = y
    print(cnt)
if _sum % 3 == 0:
    print("YES")
else:
    print("NO")