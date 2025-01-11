# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

c, r = map(int, input().split())
k = int(input())
if k > c*r:
    print(0)
else:
    seats = [[0]*c for _ in range(r)]
    d = 0
    num = 1
    x, y = r-1, 0
    while num <= c*r:
        if num == k:
            print(y+1, r-x)
            break
        seats[x][y] = num
        num += 1
        nx, ny = x + dx[d], y + dy[d]

        if d == 0:
            if nx < 0 or seats[nx][ny] != 0:
                d = (d+1) % 4
                mx, my = x + dx[d], y + dy[d]
                x, y = mx, my
            else:
                x, y = nx, ny
        elif d == 1:
            if ny >= c or seats[nx][ny] != 0:
                d = (d+1) % 4
                mx, my = x + dx[d], y + dy[d]
                x, y = mx, my
            else:
                x, y = nx, ny
        elif d == 2:
            if nx >= r or seats[nx][ny] != 0:
                d = (d+1) % 4
                mx, my = x + dx[d], y + dy[d]
                x, y = mx, my
            else:
                x, y = nx, ny
        elif d == 3:
            if ny < 0 or seats[nx][ny] != 0:
                d = (d+1) % 4
                mx, my = x + dx[d], y + dy[d]
                x, y = mx, my
            else:
                x, y = nx, ny

