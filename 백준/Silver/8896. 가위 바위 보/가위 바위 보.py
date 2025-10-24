t = int(input())


def winner(a, b):
    if a == 'R' and b == 'S':
        return a
    elif a == 'R' and b == 'P':
        return b
    elif a == 'S' and b == 'R':
        return b
    elif a == 'S' and b == 'P':
        return a
    elif a == 'P' and b == 'R':
        return a
    elif a == 'P' and b == 'S':
        return b

for _ in range(t):
    n = int(input())
    original_arr = [input() for _ in range(n)]
    arr = original_arr[:]
    m = len(arr[0])
    winners = [[False] * m for _ in range(n)]

    for rnd in range(m):
        dic = dict()
        for i, item in enumerate(zip(*arr)):
            dic[i] = set(item)
        if len(dic[rnd]) == 1 or len(dic[rnd]) == 3:
            continue
        d = dic[rnd]
        a, b = d.pop(), d.pop()
        win = winner(a, b)
        pops = []
        for robot in range(len(arr)):
            if arr[robot][rnd] != win:
                pops.append(robot)
        while pops:
            idx = pops.pop()
            arr.pop(idx)

    if len(arr) >= 2:
        print(0)
    else:
        print(original_arr.index(arr[0])+1)
