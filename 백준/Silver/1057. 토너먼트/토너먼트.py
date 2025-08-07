n, kim, lim = map(int, input().split())
arr = [i for i in range(1, n+1)]

rod = 0
while True:
    rod += 1
    winner = []
    for i in range(0, len(arr), 2):
        # 홀수 명일 때 마지막 사람 부전승
        if i == len(arr)-1:
            winner.append(arr[-1])
            continue

        a, b = arr[i], arr[i+1]
        if (a == kim and b == lim) or (a == lim and b == kim):
            print(rod)
            exit()

        if a == kim or a == lim:
            winner.append(a)
        elif b == kim or b == lim:
            winner.append(b)
        else:
            winner.append(a)
    arr = winner

