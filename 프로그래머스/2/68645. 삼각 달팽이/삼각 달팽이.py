def solution(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2, 3]

    dx = [1, 0, -1]
    dy = [0, 1, -1]
    last_num = 6
    for i in range(4, n+1):
        last_num += i

    snail = [[0]*n for _ in range(n)]

    d = 0
    x, y = 0, 0
    snail[x][y] = 1
    num = 2
    while True:
        if num > last_num:
            break
        x = x+dx[d]
        y = y+dy[d]
        if d == 0:
            if x >= n or snail[x][y] != 0:
                x -= 1
                d = (d+1)%3
                continue
        elif d == 1:
            if y >= n or snail[x][y] != 0:
                y -= 1
                d = (d+1)%3
                continue
        elif d == 2:
            if snail[x][y] != 0:
                x += 1
                y += 1
                d = (d+1)%3
                continue
        snail[x][y] = num
        num += 1

    answer = []
    for i in snail:
        answer += [j for j in i if j != 0]
    return answer

